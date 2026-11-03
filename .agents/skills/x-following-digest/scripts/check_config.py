#!/usr/bin/env python3
"""只检查本机配置的结构与缺项；不读取凭据、不联网、不发送。"""
import argparse
import json
from pathlib import Path
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


def check(config, mode):
    errors = []
    if not isinstance(config, dict):
        return [{"field": "config", "reason": "必须是 JSON 对象"}]

    def value(path):
        item = config
        for key in path.split("."):
            if not isinstance(item, dict):
                return None
            item = item.get(key)
        return item

    def fail(path, reason):
        errors.append({"field": path, "reason": reason})

    def string(path):
        item = value(path)
        if not isinstance(item, str) or not item.strip():
            fail(path, "缺失或不是非空字符串")
            return None
        return item

    def choice(path, allowed):
        item = string(path)
        if item is not None and item not in allowed:
            fail(path, "不支持的取值")
        return item

    if type(value("version")) is not int or value("version") != 1:
        fail("version", "必须为整数 1")
    tz = string("timezone")
    if tz:
        try:
            ZoneInfo(tz)
        except (ZoneInfoNotFoundError, ValueError):
            fail("timezone", "不是可识别的 IANA 时区")
    uid = string("x.user_id")
    if uid and not (uid.isascii() and uid.isdecimal()):
        fail("x.user_id", "必须为数字 ID 字符串")
    string("x.handle")
    method = choice("x.access.method", ("aside", "official_api"))
    if method == "aside":
        string("x.access.profile_id")
    elif method == "official_api":
        string("x.access.credential_ref")

    if mode == "send":
        transport = choice("telegram.transport", ("florence", "bot_api"))
        string("telegram.chat_id")
        choice("telegram.target_kind", ("channel", "private", "group"))
        if value("telegram.target_authorized") is not True:
            fail("telegram.target_authorized", "缺少明确目标授权记录")
        if transport == "florence":
            choice("telegram.bot", ("info", "level2", "sum"))
            skill = string("telegram.skill_path")
            if skill:
                try:
                    exists = Path(skill).expanduser().is_file()
                except (OSError, ValueError):
                    exists = False
                if not exists:
                    fail("telegram.skill_path", "指定的技能文件不存在或不可访问")
        elif transport == "bot_api":
            string("telegram.credential_ref")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="~/.local/state/x-following-digest/config.json")
    parser.add_argument("--mode", choices=("send", "preview"), default="send")
    args = parser.parse_args()
    try:
        config = json.loads(Path(args.config).expanduser().read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors = [{"field": "config", "reason": "配置文件不存在"}]
    except (OSError, UnicodeError, ValueError):
        errors = [{"field": "config", "reason": "配置不可读或不是有效 JSON"}]
    else:
        errors = check(config, args.mode)
    print(json.dumps({"status": "invalid" if errors else "configured",
                      "mode": args.mode, "errors": errors,
                      "scope": "仅配置检查，未验证在线权限或投递"}, ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
