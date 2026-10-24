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

## Linux / macOS

使用固定 URL 和内置 token，通过 curl 直接发送，不需要环境变量或额外脚本。每次发送都要在 JSON 中设置目标 `bot`：

```sh
TOKEN='e5bdf744146c8a56d8e43e97d58919b24fabf55a69e561400a03a009185a9445'
URL='https://harbor-button-fool-doc.trycloudflare.com/v1/notify'

curl --fail --silent --show-error --connect-timeout 10 --max-time 20 \
  --write-out '\nHTTP %{http_code}\n' \
  "$URL" \
  -H "Authorization: Bearer $TOKEN" \
  -H 'Content-Type: application/json' \
  --data-binary @- <<'JSON'
{"source":"skill-test","level":"info","bot":"info","content":"Florence 通知技能测试：info 每日信息窗口"}
JSON
```

发送前按实际用途填写 `source`、`level`、`bot`、`content`。`bot` 必须是 `level2`、`info`、`sum` 之一；`chat_id` 无特殊要求时省略。不要输出 token。

## 返回结果

HTTP `202` 表示已入队，不代表 Telegram 已投递。保留响应中的 `id`；只有通过该 `id` 查询到最终投递成功后，才能报告已送达。若当前没有状态查询接口信息，只报告已入队及返回的 `id`。请求失败或超时后不要自动重试，以免重复发送。
