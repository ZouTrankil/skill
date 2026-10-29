# AI 技能

这里收录可复用、尽量兼容多种 AI 工具的技能包。技能使用通用的 `SKILL.md` 格式。

## 分类与存放约定

本 README 是技能索引，记录用途、来源、使用范围和维护状态。**统一索引不等于全部全局安装**；源码位置与实际启用位置分别管理。

来源分为「本仓库维护」和「第三方」。使用范围分为「全局通用」「项目类共用」「项目专用」。第三方技能也有使用范围，不把来源与范围混成互斥分类。

| 使用范围或来源 | 源码位置 | 启用方式 |
| --- | --- | --- |
| 全局通用 | 本仓库 `.agents/skills/<技能名>/` | 按需安装到用户级技能目录；不默认安装整个仓库 |
| 项目类共用 | 本仓库 `library/project-types/<项目类别>/<技能名>/` | 可全局启用并按任务或配置确定项目，也可复制到项目使用 |
| 项目专用 | 对应项目的 `.agents/skills/<技能名>/` | 随该项目维护，本索引只登记用途和位置 |
| 第三方插件提供 | 插件管理器维护的位置 | 通过原渠道安装和更新，不复制插件缓存到本仓库 |
| 第三方独立技能 | 按使用范围存放；现有 `aihot` 保留在 `.agents/skills/` | 记录上游、版本及本地调整，更新时保留这些调整 |
| 已归档 | 本仓库 `archive/<技能名>/` | 移出自动发现目录，并同步移除或禁用安装入口 |

当前目录如下；`archive/` 在实际需要时创建，不预建空目录：

```text
skill/
├── README.md
├── .agents/skills/              # 现有通用技能；在本仓库中也可被发现
│   ├── aihot/
│   ├── daily-memory-review/
│   └── florence-notify/
├── library/project-types/       # 项目类共用源码，当前通过用户级链接启用
│   └── software-development/
│       ├── code-quality/
│       ├── local-repo-sync/
│       ├── repo-artifact-cleanup/
│       └── worktree-cleanup/
└── scripts/                     # 仓库级安装等工具

<业务项目>/.agents/skills/
├── <项目专用技能>/
└── <接入的项目类共用技能>/
```

技能发现目录保持 `.agents/skills/<技能名>/SKILL.md` 的直接布局，分类写在本索引中，不再套 `global/`、`third-party/` 等目录。单个技能内部的辅助代码放自己的 `scripts/`，不把每个脚本拆成独立技能。

Codex 当前官方文档列出的用户级位置是 `~/.agents/skills/`，项目级位置是项目内的 `.agents/skills/`，并支持技能目录符号链接。项目类共用技能可通过链接接入；需要独立分发时可复制，但应记录来源与版本，避免两边分别修改。同名技能不会自动合并，应避免重复启用。[官方目录说明](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)

本仓库现有安装脚本仍使用 `${CODEX_HOME:-$HOME/.codex}/skills/`，且只安装 `florence-notify`。当前机器保留该技能已有的全局安装，`aihot`、`daily-memory-review` 及 library 中四个项目类共用技能通过 `~/.agents/skills/` 下的符号链接接入源码；不要再为同一技能建立第二个用户级入口。其他客户端按各自支持的发现目录接入。

## 技能索引

「已收录」表示源码存在；「已配置全局」表示当前机器已有有效用户级入口，不代表已配置定时任务或已完成真实环境验收。「设计中」表示尚未实现。后续按实际情况使用「试用中」「使用中」「已归档」，不推断使用状态。

| 技能 | 用途 | 来源 | 使用范围 | 状态 |
| --- | --- | --- | --- | --- |
| [code-quality](./library/project-types/software-development/code-quality/SKILL.md) | 依据项目规范编码、重构与评审，给出有证据的问题和修复建议 | 本仓库维护 | 项目类共用：按当前开发任务确定项目 | 已配置全局，链接 library 源码 |
| [florence-notify](./.agents/skills/florence-notify/SKILL.md) | 按明确要求发送 Florence 通知 | 本仓库维护 | 全局通用：已配置该通知服务的任务 | 已配置全局，保留原安装 |
| [local-repo-sync](./library/project-types/software-development/local-repo-sync/SKILL.md) | 登记本地仓库，配置定期 fetch 与 rebase | 本仓库维护 | 项目类共用：按已有仓库清单确定范围 | 已配置全局，链接 library 源码 |
| [daily-memory-review](./.agents/skills/daily-memory-review/SKILL.md) | 复盘本地每日记录，维护长期上下文并建议次日行动 | 本仓库维护 | 全局通用：个人记录复盘，需配置记录来源 | 已配置全局，链接源码 |
| [aihot](./.agents/skills/aihot/SKILL.md) | 查询 AI 资讯、热点与日报 | 第三方：AIHOT / Virxact，2.0.0；有本地调用约束 | 全局通用：AI 资讯查询，仅明确调用 | 已配置全局，链接源码 |
| [repo-artifact-cleanup](./library/project-types/software-development/repo-artifact-cleanup/SKILL.md) | 批量扫描临时产物，按证据和授权隔离、清理及恢复 | 本仓库维护 | 项目类共用：复用仓库清单，清理范围单独授权 | 已配置全局，流程版；未执行清理验收 |
| [worktree-cleanup](./library/project-types/software-development/worktree-cleanup/SKILL.md) | 核对任务、改动和提交保护后回收 worktree，保留分支 | 本仓库维护 | 项目类共用：复用仓库清单，回收范围单独授权 | 已配置全局，流程版；未执行回收验收 |

当前项目类共用技能归入 `software-development`，已建立用户级全局入口，不要求逐个项目安装；当前没有项目专用技能。分类说明用途，安装位置决定可发现范围，两者独立。

## 使用项目类共用技能

当前用户级入口指向 library 中的唯一源码：

```text
~/.agents/skills/code-quality
  → <本仓库>/library/project-types/software-development/code-quality
~/.agents/skills/local-repo-sync
  → <本仓库>/library/project-types/software-development/local-repo-sync
~/.agents/skills/repo-artifact-cleanup
  → <本仓库>/library/project-types/software-development/repo-artifact-cleanup
~/.agents/skills/worktree-cleanup
  → <本仓库>/library/project-types/software-development/worktree-cleanup
```

`code-quality` 根据当前任务、工作目录和项目约定确定范围。`local-repo-sync` 继续使用技能旁已有的 `repos.tsv` 仓库清单，不重复登记项目；该本机配置已被 Git 忽略。需要临时指定其他清单时使用 `SYNC_REPOS_FILE`。

两个清理技能优先使用本次指定的目录或清单，否则读取 `SYNC_REPOS_FILE`，再否则复用 `local-repo-sync/repos.tsv`。只读取清单，不调用仓库同步，也不继承同步授权。清理路径、保护项、保留期限和自动执行范围使用用户指定的清理策略；未配置时先扫描报告，不依据文件名或时间自动删除。

第一版仅包含 `SKILL.md`，由代理按流程调用现有 Git、文件系统或管理器工具；没有独立定时执行脚本，不创建空的 `scripts/` 或 `references/`。例如可以请求“使用 `$repo-artifact-cleanup` 扫描已有清单中的仓库，先只报告候选”或“使用 `$worktree-cleanup` 检查可回收工作树，先不删除”。正式执行与调度需另有明确范围和授权。

以后需要随项目独立分发时，可将整个技能复制到目标项目 `.agents/skills/<技能名>/`，检查同名内容并记录来源与版本。本机清单按需单独配置并加入目标项目的忽略规则，不随技能源码提交。避免同名全局入口与项目副本重复启用。

全局入口只让技能可被发现，不会自动运行仓库同步或创建定时任务。

## 维护方式

- 新增技能先确定来源、使用范围和维护位置，再更新索引；同一技能源码只在一个位置维护。
- 修改本仓库技能后按需更新安装副本，不直接在多份副本上分别修改；归档时检查已有引用与安装入口。
- 第三方更新保留上游来源、版本和本地调整。`aihot` 的上游为 [AIHOT 技能](https://aihot.news/aihot-skill/)，当前仅显式调用 `$aihot` 或明确要求使用 AIHOT 时启用；升级时保留 `agents/openai.yaml` 中的 `allow_implicit_invocation: false` 和正文调用约束。
- 定期检查重复职责、失效指令和不再使用的技能；索引状态不承担启停控制，定时任务与安装配置分别核对。

## Florence 通知说明

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
