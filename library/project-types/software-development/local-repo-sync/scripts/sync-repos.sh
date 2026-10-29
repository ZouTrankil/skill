#!/usr/bin/env bash
set -u

script_dir=$(cd "$(dirname "$0")" && pwd -P)
manifest=${SYNC_REPOS_FILE:-"$script_dir/../repos.tsv"}
log_file=${SYNC_REPOS_LOG:-"${HOME}/.local/state/local-repo-sync/sync.log"}

if [[ ! -r "$manifest" ]]; then
  echo "清单不存在或不可读：$manifest" >&2
  exit 2
fi
mkdir -p "$(dirname "$log_file")" || exit 2
exec >>"$log_file" 2>&1
printf '\n[%s] 同步开始\n' "$(date '+%Y-%m-%d %H:%M:%S %z')"

failed=0
while IFS=$'\t' read -r repo remote base description extra || [[ -n "${repo:-}" ]]; do
  [[ -z "${repo:-}" || "$repo" == \#* ]] && continue
  if [[ -z "${remote:-}" || -z "${base:-}" || -n "${extra:-}" ]]; then
    printf '跳过：清单行格式错误：%q\n' "$repo"
    failed=1
    continue
  fi
  printf '\n仓库：%s（%s/%s）\n' "$repo" "$remote" "$base"
  if ! git -C "$repo" rev-parse --show-toplevel >/dev/null 2>&1; then
    echo '跳过：不是可访问的 Git 仓库'
    failed=1
    continue
  fi
  if [[ "$(git -C "$repo" rev-parse --show-toplevel)" != "$repo" ]]; then
    echo '跳过：清单路径必须是仓库根目录'
    failed=1
    continue
  fi
  if [[ -n "$(git -C "$repo" status --porcelain)" ]]; then
    echo '跳过：工作区或暂存区不干净'
    failed=1
    continue
  fi
  if git -C "$repo" rev-parse -q --verify REBASE_HEAD >/dev/null || \
     git -C "$repo" rev-parse -q --verify MERGE_HEAD >/dev/null || \
     git -C "$repo" rev-parse -q --verify CHERRY_PICK_HEAD >/dev/null; then
    echo '跳过：存在进行中的 Git 操作'
    failed=1
    continue
  fi
  if ! git -C "$repo" show-ref --verify --quiet "refs/heads/$(git -C "$repo" branch --show-current)"; then
    echo '跳过：当前为 detached HEAD 或分支无效'
    failed=1
    continue
  fi
  if ! git -C "$repo" remote get-url "$remote" >/dev/null 2>&1; then
    echo "跳过：remote 不存在：$remote"
    failed=1
    continue
  fi
  if ! git -C "$repo" fetch "$remote" --prune; then
    echo '失败：fetch 未完成'
    failed=1
    continue
  fi
  if ! git -C "$repo" show-ref --verify --quiet "refs/remotes/$remote/$base"; then
    echo "跳过：fetch 后找不到远程分支 $remote/$base"
    failed=1
    continue
  fi
  if git -C "$repo" rebase "$remote/$base"; then
    printf '完成：当前分支 %s 已基于 %s/%s\n' \
      "$(git -C "$repo" branch --show-current)" "$remote" "$base"
  else
    echo '冲突或 rebase 失败：尝试 abort，需人工检查'
    if git -C "$repo" rebase --abort; then
      echo '已 abort，工作区回到 rebase 前状态'
    else
      echo '严重：rebase --abort 失败，请立即检查仓库状态'
    fi
    failed=1
  fi
done < "$manifest"

printf '[%s] 同步结束（exit=%s）\n' "$(date '+%Y-%m-%d %H:%M:%S %z')" "$failed"
exit "$failed"
