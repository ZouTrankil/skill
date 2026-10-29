---
name: local-repo-sync
description: Register local Git checkouts and configure or run daily local-only synchronization with their remote base branches. Use when setting up or maintaining scheduled fetch and rebase workflows across repositories.
metadata:
  short-description: Sync local repositories daily
---

# 本地仓库每日同步

为用户指定的本地 Git 仓库建立清单，并配置每天获取远程更新、将当前分支 rebase 到对应远程主干的流程。适用于 GitHub、GitLab 等 Git 远程服务；不依赖托管平台。

## 初始化

1. 先确认用户要纳入的目录、运行机器和每天运行时间。不要扫描整个磁盘或自行登记仓库。
2. 对每个目录检查 Git 根目录、remote、默认主干、当前分支、工作区状态及是否已有 rebase。主干优先从 remote 的 `HEAD` 符号引用读取；无法读取时询问用户，不能猜 `main` 或 `master`。
3. 解释同步会改写当前本地分支历史（rebase），并确认用户希望每日同步哪些分支。登记后按清单指定的主干同步当前分支；有未提交改动时先按下述本地提交流程审阅和提交，不因工作区脏就直接跳过。
4. 默认使用技能目录下的 `repos.tsv` 作为仓库清单。每行格式为：`仓库绝对路径<TAB>remote 名称<TAB>远程主干分支<TAB>项目说明（可选）`。本仓库中的清单已加入 `.gitignore`，用于保存本机仓库路径而不提交。技能复制到其他 Git 项目中使用时，也要将该清单加入宿主项目的 `.gitignore`。不要写入凭据。项目说明写简短用途或辨识信息即可。
5. macOS 使用 `scripts/install-launchd.sh` 安装每日任务，Linux 可用 cron/systemd timer 调用 `scripts/sync-repos.sh`。Windows 使用 `scripts/sync-repos.bat` 手动运行或调用 PowerShell 脚本；用 `scripts/install-task.ps1` 安装 Windows 任务计划程序任务。安装前展示触发时间、清单路径和日志路径。

## 同步行为

- 每个仓库先检查当前分支、staged / unstaged / untracked 变更和进行中的 Git 操作。不要因为工作区不干净就立即跳过。
- 有多项本地改动时，先读完整 diff 并按独立、连贯的功能或文档主题分批；每批只 stage 对应文件或 hunk，写一条中文 Conventional Commit。一个连贯的小改动可作为一批。不得用 `git add -A` 或盲目提交整个工作区。
- 提交前排除凭据、令牌、个人隐私、缓存 / 构建产物、无法确认来源的生成文件，以及明显不属于本次登记项目的改动。对用途不清、二进制或范围不明的变更，不猜测、不提交，保留原状并报告。
- 用户已授权将清单中仓库的清晰本地改动提交到本地。不要 amend、squash 或改写已有提交；每个变更批次创建独立 commit。提交只落在本地，绝不 push。
- 若 commit 因作者配置、签名、hook 或冲突失败，不绕过检查、不删 hook、不伪造作者；保留现场并报告。提交后复查 `git status` 和提交列表。
- 只有相关仓库工作区已清洁、当前分支明确、没有进行中的 Git 操作时，才运行同步：`git fetch <remote> --prune`，然后对当前分支执行 `git rebase <remote>/<base>`。即使当前分支就是主干，也按此方式快进到远程主干。
- 有无法安全提交的剩余改动、detached HEAD、缺失 remote/ref、锁文件或进行中的操作时，跳过该仓库的 fetch / rebase 并写明原因；已经安全创建的本地提交保留。
- 同步永远不执行 push、force push、reset、clean 或 stash。rebase 顺利时不额外造一个提交；rebase 自身会保留并重放开发分支上的本地提交。若人工解决冲突后确需独立冲突修复提交，才创建本地提交，并说明其内容。
- 遇到冲突时不要凭空自动选 ours/theirs，也不要在无人检查的定时脚本里编造语义修复。保存冲突路径和错误日志，尝试 `git rebase --abort` 回到同步前状态；abort 失败就停止该仓库操作并报告，不能继续其他写操作。由 Codex 在有人发起的工作会话中检查上下文、解决冲突、完成 rebase 并做相关验证。下次定时任务可重试。
- 不把“定时命令已安装”说成“已完成每日同步”。报告清单、调度器状态、最近运行结果和需要人工处理的仓库。

## 本地提交规范

- 需要创建本地提交时，遵循 Conventional Commits：`<type>(<scope>): <中文摘要>`。`scope` 可省略；类型使用 `feat`、`fix`、`docs`、`style`、`refactor`、`perf`、`test`、`build`、`ci`、`chore` 或 `revert` 等标准类型。
- 摘要及正文使用中文，简洁说明改动内容或原因；破坏性变更按规范标记 `!`，并用 `BREAKING CHANGE:` 补充中文说明。
- 示例：`fix(sync): 修正 Windows 清单解析`、`docs(sync): 补充本地提交规范`。
- rebase 正常重放已有提交时不创建额外提交；冲突解决后优先通过 `git rebase --continue` 继续重放。只有流程确实要求独立提交时，才按上述格式创建本地提交；绝不 push。
- 多批改动示例：`feat(combat): 增加战士受击规则`、`docs(sync): 补充本地同步说明`。每批摘要准确对应该批内容，不把不相关主题合并成一个宽泛提交。

同步脚本 `scripts/sync-repos.sh` 和 `scripts/sync-repos.ps1` 只处理清洁工作区，不会替代理解、分组或提交。使用技能的 AI 应先完成上述本地分批提交，再运行脚本；脚本仍发现脏状态时应停止该仓库同步并报告，不要绕过检查。

## 执行入口

macOS/Linux 手动运行：

```sh
SYNC_REPOS_LOG="$HOME/.local/state/local-repo-sync/sync.log" \
bash /path/to/local-repo-sync/scripts/sync-repos.sh
```

Windows 手动运行：

```bat
call C:\path\to\local-repo-sync\scripts\sync-repos.bat
```

每行一个仓库，空行和以 `#` 开头的行为注释。字段以制表符分隔；仓库路径、remote 和分支名不能包含制表符。第四列项目说明可留空。每次实际运行后检查日志和 `git status`；脚本以非零状态表示至少一个仓库未能同步。
