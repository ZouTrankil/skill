---
name: florence-notify
description: 按用户明确要求，通过 Florence 通知网关向指定 Telegram 机器人发送通知。
---

# Florence 通知

只有用户明确要求发送时才调用。每次请求都必须包含 `bot`，用它选定目标聊天窗口：

- `level2`：实时通知
- `info`：每日信息
- `sum`：盘后复盘

按用户明确说明或通知内容的用途选择 bot；用途不清楚时先问用户。用户要求发到多个窗口时，每个 bot 分别发送一条。`chat_id` 默认是 `8401222508`，通常省略。

`bot` 选择目标窗口；`level` 是通知级别，默认 `info`，不要把两者混用。保留用户给出的 `source`；每日信息可用 `daily-info`。

## Linux / macOS / WSL

固定使用下方 URL。`NOTIFY_API_TOKEN` 应已从可信环境载入；WSL 可从 `/mnt/f/tools/channel/.env` 加载。不要打印或写入 token。发送时将标准 JSON 正文传给 curl：

```sh
if [ -z "${NOTIFY_API_TOKEN:-}" ] && [ -r /mnt/f/tools/channel/.env ]; then
  set -a
  . /mnt/f/tools/channel/.env
  set +a
fi
: "${NOTIFY_API_TOKEN:?NOTIFY_API_TOKEN 未设置}"

curl --fail --silent --show-error --connect-timeout 10 --max-time 20 \
  --write-out '\nHTTP %{http_code}\n' \
  'https://harbor-button-fool-doc.trycloudflare.com/v1/notify' \
  -H "Authorization: Bearer ${NOTIFY_API_TOKEN}" \
  -H 'Content-Type: application/json' \
  --data-binary @- <<'JSON'
{"source":"daily-info","level":"info","bot":"info","content":"今天的每日信息推送"}
JSON
```

发送前按实际用途填写 `source`、`level`、`bot`、`content`。`bot` 必须是 `level2`、`info`、`sum` 之一；`chat_id` 无特殊要求时省略。

## Windows

在 `F:\tools\channel` 环境使用会自动读取 `.env` 的脚本，不要直接传 token：

```powershell
& 'F:\tools\channel\scripts\notify.ps1' -Bot info -Source daily-info -Content '今天的每日信息推送'
```

将 `-Bot` 设为 `info`、`sum` 或 `level2`，必须与目标窗口对应。

## 返回结果

HTTP `202` 表示已入队，不代表 Telegram 已投递。保留响应中的 `id`；只有通过该 `id` 查询到最终投递成功后，才能报告已送达。若当前没有状态查询接口信息，只报告已入队及返回的 `id`。请求失败或超时后不要自动重试，以免重复发送。
