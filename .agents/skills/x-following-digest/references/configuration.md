# 配置与运行检查

## 本机配置

默认配置为 `~/.local/state/x-following-digest/config.json`。实际账号、profile、目标和历史证据只放本机状态目录，不写进公共技能。以下是字段结构示例，`null` 表示尚未配置，不能直接用于推送：

```json
{
  "version": 1,
  "timezone": "Asia/Shanghai",
  "x": {
    "user_id": null,
    "handle": null,
    "access": {
      "method": "aside",
      "profile_id": null
    }
  },
  "telegram": {
    "transport": "florence",
    "skill_path": null,
    "bot": "info",
    "chat_id": null,
    "target_kind": null,
    "target_authorized": false
  }
}
```

- `x.user_id`、`x.handle`：核验得到的账号 ID 字符串及用户名。运行时 `getMe` 的 ID 必须匹配；handle 更名按同一 ID 更新，有冲突则停止。
- `x.access.method=aside`：`profile_id` 是从 Aside 枚举并经 `getMe` 验证的浏览器 profile，同时是登录态凭据引用，不另索取开发者 token。不能把 Aside 账户序号或历史 session ID 当 profile ID。
- `x.access.method=official_api`：改用 `credential_ref` 指向已有用户授权，例如 `env:X_ACCESS_TOKEN` 或现有密钥存储引用。引用存在不代表权限可用，仍需按接入指南验证。
- `telegram.transport=florence`：`skill_path` 指向用户选择的 `SKILL.md`，也是中继凭据及地址的引用，每轮读取它；不复制其 token/URL。`bot` 按实际技能取值，`chat_id` 必须显式保存。每日信息适用 `info`，但路由名不能替代目标。
- `telegram.transport=bot_api`：使用 `credential_ref`、`chat_id`，发送前验证机器人、目标和权限。
- `target_kind` 为 `channel` 或用户明确授权的 `private`/`group`；`target_authorized` 仅在有用户指定或既有授权证据时设为 `true`。这是本机授权记录，不能据字段自行制造授权或跳过实际目标验证。
- 可附 `provenance` 保存来源验证时间、会话 ID 和目标授权摘要；不存 token、cookie 或整段会话。

正式运行先执行（路径按实际技能位置替换）：

```sh
python3 <技能目录>/scripts/check_config.py --config ~/.local/state/x-following-digest/config.json --mode send
```

明确预览用 `--mode preview`，只检查来源。退出码 0 表示结构和必要字段齐备，2 表示缺项/无效；输出不回显字段值或凭据。此检查不联网、不发送，也不证明来源当前可用或消息已送达。若本次明确参数覆盖配置，先合并这些参数，再对最终配置检查；临时覆盖不自动永久改写目标。

## 首次配置与从预览恢复

1. 普通执行发现缺配置时按请求结束，记录具体字段；只有用户要求配置/修复时才进入恢复流程。
2. 读取既有运行的 `coverage.json`、`delivery.json`、`request.txt` 及必要的来源日志。历史账号只作定位线索：`preview_only`、`sent=false` 不能当成功发送记录，也不能推出 Telegram 目标。
3. 枚举实际 profile，选取与证据相符的来源并重新 `getMe`。成功后保存账号、访问方式和验证证据；未知字段保留 `null`。预览不要求 Telegram 配置，不丢弃已验证的来源。
4. 缺发送目标时，只问用户真实缺项。用户指定发送技能后先读该技能；若与先前“仅频道/不发默认私聊”冲突，确认具体目标。明确选择后固化路由、目标及凭据引用。
5. 写入前重新读当前配置，保留其他窗口新增字段。新文件排他创建；更新只改本次确认字段，不覆盖不相关设置。配置检查通过后报告“配置齐备”，不要称为全量采集或投递验收通过。

## 运行与发送账本

新运行冻结实际截止时刻及前 24 小时；恢复既有运行沿用其窗口、正文和检查点。按账号、窗口、目标检查已有账本并持有单实例锁，不能仅依赖目录名前缀判断重复。

历史预览保留原样，正式运行不能改写其 `preview_only`；另建正式记录并保留对预览来源的引用。`sent` 且有成功回执的段跳过；`sending` 中断、`unknown` 或无最终回执的 `pending` 先核对状态，不能重新发送。没有可查询回执的未知段停止并报告。配置恢复不会重置发送状态，也不扩大时间窗口去补历史空缺。

Florence 的 HTTP 202 只记 `pending` 和通知 ID。实际技能未提供状态查询方法时，不猜查询端点、不声称已送达，也不自动重发；这与配置是否齐备分开报告。
