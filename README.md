# AI 技能

这里收录可复用、尽量兼容多种 AI 工具的技能包。技能使用通用的 `SKILL.md` 格式。

## 技能

- [florence-notify](./.agents/skills/florence-notify/)：按用户明确要求，通过 Florence 通知接口发送通知。

本仓库的 `.agents/skills/` 布局可供 Codex 和 Cursor 在项目中发现。Claude Code 使用 `.claude/skills/`；要在那里使用时，将 `florence-notify` 目录复制到该位置。

Linux/macOS 使用 `curl`；技能内固定了通知 URL 和 token，无需额外配置。每次发送必须指定 `bot`：`level2` 实时通知、`info` 每日信息、`sum` 盘后复盘。`chat_id` 默认使用 `8401222508`。

## 安装到 Codex 全局技能

在新电脑安装 Git 和 Codex 后，克隆仓库并运行安装脚本：

```sh
git clone https://github.com/ZouTrankil/skill.git
cd skill
./scripts/install-codex.sh
```

技能默认安装到 `${CODEX_HOME:-$HOME/.codex}/skills/florence-notify`。如果已设置 `CODEX_HOME`，脚本会使用该目录。安装后重新打开 Codex 会话，再调用 `$florence-notify`。

已有安装与仓库版本不同时，脚本会拒绝覆盖；检查现有内容后，可运行 `./scripts/install-codex.sh --replace` 更新。以后在新电脑上也可以直接对已有 checkout 运行同一脚本。

> **凭据提示：** 当前仓库是公开仓库，技能文件内的固定 token 已随 Git 提交公开。任何能访问仓库的人都能读取它。请先轮换该 token，再继续用于真实通知；轮换后更新技能文件并重新安装。
