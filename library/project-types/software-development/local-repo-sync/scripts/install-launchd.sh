#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "用法：$0 <清单绝对路径> [运行小时 0-23]" >&2
  exit 2
fi
manifest=$1
hour=${2:-8}
if [[ "$manifest" != /* || ! -r "$manifest" ]]; then
  echo '清单必须是可读的绝对路径' >&2
  exit 2
fi
if [[ ! "$hour" =~ ^([0-9]|1[0-9]|2[0-3])$ ]]; then
  echo '运行小时必须是 0 到 23 的整数（本机时区）' >&2
  exit 2
fi

script_dir=$(cd "$(dirname "$0")" && pwd -P)
home_dir=${HOME:?HOME 未设置}
uid=$(id -u)
label=local-repo-sync.daily
plist_dir="$home_dir/Library/LaunchAgents"
plist="$plist_dir/$label.plist"
log_dir="$home_dir/Library/Logs/local-repo-sync"
mkdir -p "$plist_dir" "$log_dir" "$home_dir/.local/state/local-repo-sync"

if [[ -e "$plist" ]]; then
  echo "任务已存在，未覆盖：$plist" >&2
  exit 3
fi

python3 - "$plist" "$label" "$script_dir/sync-repos.sh" "$manifest" \
  "$home_dir/.local/state/local-repo-sync/sync.log" "$log_dir" "$hour" <<'PY'
import plistlib
import sys

path, label, script, manifest, log, log_dir, hour = sys.argv[1:]
data = {
    "Label": label,
    "ProgramArguments": ["/bin/bash", script],
    "EnvironmentVariables": {
        "SYNC_REPOS_FILE": manifest,
        "SYNC_REPOS_LOG": log,
        "PATH": "/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin",
    },
    "StartCalendarInterval": {"Hour": int(hour), "Minute": 0},
    "StandardOutPath": f"{log_dir}/launchd.out.log",
    "StandardErrorPath": f"{log_dir}/launchd.err.log",
}
with open(path, "wb") as output:
    plistlib.dump(data, output)
PY
chmod 600 "$plist"
if ! plutil -lint "$plist"; then
  rm "$plist"
  exit 4
fi
if ! launchctl bootstrap "gui/$uid" "$plist"; then
  echo "任务文件已创建但未能加载：$plist" >&2
  exit 5
fi
echo "已安装：每天本机时间 ${hour}:00 运行。清单：$manifest"
echo "日志：$home_dir/.local/state/local-repo-sync/sync.log"
