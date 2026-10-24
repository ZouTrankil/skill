# AI 技能

这里收录可复用、尽量兼容多种 AI 工具的技能包。技能使用通用的 `SKILL.md` 格式。

## 技能

- [florence-notify](./.agents/skills/florence-notify/)：按用户明确要求，通过 Florence 通知接口发送通知。

本仓库的 `.agents/skills/` 布局可供 Codex 和 Cursor 在项目中发现。Claude Code 使用 `.claude/skills/`；要在那里使用时，将 `florence-notify` 目录复制到该位置。

Linux/macOS 使用 `curl`；技能内固定了通知 URL 和 token，无需额外配置。每次发送必须指定 `bot`：`level2` 实时通知、`info` 每日信息、`sum` 盘后复盘。`chat_id` 默认使用 `8401222508`。
