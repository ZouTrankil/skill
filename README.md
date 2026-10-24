# AI 技能

这里收录可复用、尽量兼容多种 AI 工具的技能包。技能使用通用的 `SKILL.md` 格式。

## 技能

- [florence-notify](./.agents/skills/florence-notify/)：按用户明确要求，通过 Florence 通知接口发送通知。

本仓库的 `.agents/skills/` 布局可供 Codex 和 Cursor 在项目中发现。Claude Code 使用 `.claude/skills/`；要在那里使用时，将 `florence-notify` 目录复制到该位置。

Linux/macOS/WSL 使用 `curl` 和 `NOTIFY_API_TOKEN`；Windows 使用自动读取 `.env` 的 `F:\tools\channel\scripts\notify.ps1`。每次发送必须指定 `bot`：`level2` 实时通知、`info` 每日信息、`sum` 盘后复盘。URL 固定在技能内。
