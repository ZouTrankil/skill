#!/usr/bin/env python3
"""离线整理 Aside 采集结果；不访问网络，不发送消息。"""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path


def timestamp(value):
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("时间必须包含时区")
    return result.astimezone(timezone.utc)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("raw", "following", "start", "end", "output-dir"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args()
    start, end = timestamp(args.start), timestamp(args.end)
    if start >= end:
        parser.error("start 必须早于 end")
    following = json.loads(Path(args.following).read_text(encoding="utf-8"))
    accounts = following["accounts"]
    handles = {a["handle"].lstrip("@").casefold(): a for a in accounts}
    if len(handles) != len(accounts):
        parser.error("关注名单存在重复 handle，先检查来源")
    counts = Counter()
    candidates, reposts, rejected = {}, {}, []
    # 按 LF 读取 JSONL，不能用 splitlines 拆开正文中的 U+2028 等字符。
    with Path(args.raw).open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            counts["raw_records"] += 1
            try:
                record = json.loads(line)
                post = record["tweet"]
                author = post["author"]
                post_id, author_id = post["id"], author["id"]
                if not isinstance(post_id, str) or not isinstance(author_id, str):
                    raise ValueError("帖子与作者 ID 必须为字符串")
                handle = author["screenName"].lstrip("@").casefold()
                body = post["text"]
                if not isinstance(body, str):
                    raise ValueError("正文必须是字符串")
                created = timestamp(post["createdAt"])
                if handle not in handles:
                    counts["nonfollowing_records"] += 1
                    continue
                known_id = handles[handle].get("id")
                if known_id is not None and known_id != author_id:
                    raise ValueError("作者 ID 与关注名单不一致")
                if not start <= created < end:
                    counts["outside_window_records"] += 1
                    continue
                # 当前适配器以 RT 前缀表示部分转发；其 createdAt 不保证是转发时间。
                is_repost = body.startswith("RT @")
                row = {
                    "id": post_id, "author_id": author_id,
                    "handle": author["screenName"],
                    "url": f"https://x.com/{author['screenName']}/status/{post_id}",
                    "created_at": created.isoformat(), "text": body,
                    "type": "repost_unverified" if is_repost else
                            "reply" if post.get("inReplyToId") else
                            "quote" if post.get("quotedTweet") else "original",
                    "in_reply_to_id": post.get("inReplyToId"),
                    "quoted_post": post.get("quotedTweet"),
                    "text_completeness": "unverified",
                    "follow_evidence": handles[handle],
                    "follow_identity_match": "id" if known_id is not None else "current_handle_only",
                    "raw_line": line_number,
                }
                target = reposts if is_repost else candidates
                key = (post_id, author_id)
                if key in target:
                    counts["duplicate_eligible_records"] += 1
                    previous = target[key]
                    if previous["text"] != body:
                        counts["differing_text_duplicates"] += 1
                        previous["text_completeness"] = "conflicting_versions"
                        previous.setdefault("alternate_raw_lines", []).append(line_number)
                    continue
                target[key] = row
            except (KeyError, TypeError, ValueError, AttributeError) as error:
                rejected.append({"raw_line": line_number, "reason": str(error)})
    counts.update({"following_accounts": len(handles), "candidate_posts": len(candidates),
                   "candidate_authors": len({r["author_id"] for r in candidates.values()}),
                   "reposts_needing_event_time": len(reposts), "invalid_records": len(rejected)})
    out = Path(args.output_dir).expanduser()
    # 使用新目录，避免覆盖采集原件、上次摘要或发送账本。
    out.mkdir(parents=True, exist_ok=False)
    for filename, rows in (("candidates.jsonl", candidates.values()),
                           ("reposts.jsonl", reposts.values()), ("rejected.jsonl", rejected)):
        with (out / filename).open("w", encoding="utf-8") as stream:
            for row in rows:
                stream.write(json.dumps(row, ensure_ascii=False) + "\n")
    report = {"window_start": start.isoformat(), "window_end": end.isoformat(),
              "bounds": "[start,end)", "counts": dict(counts),
              "source_files": {"raw": str(Path(args.raw).resolve()),
                               "following": str(Path(args.following).resolve())},
              "collection_completeness": "not_assessed",
              "notes": ["仅离线过滤，不证明关注名单、正文或采集覆盖完整。",
                        "reposts 仅按返回的 createdAt 筛选，不能据此认定转发发生在窗口内。",
                        "未按长度、主题或热度删除候选；广告与实质内容交给后续语义筛选。"]}
    (out / "preparation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"output_dir": str(out), **report}, ensure_ascii=False, indent=2))
    return 2 if rejected else 0


if __name__ == "__main__":
    raise SystemExit(main())
