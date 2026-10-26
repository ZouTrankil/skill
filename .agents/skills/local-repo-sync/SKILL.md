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
3. 解释同步会改写当前本地分支历史（rebase），并确认用户希望每日同步哪些分支。清洁工作区才可自动同步；有未提交改动、detached HEAD、正在进行的操作或无法确定上游时跳过并报告。
4. 默认使用技能目录下的 `repos.tsv` 作为仓库清单。每行格式为：`仓库绝对路径<TAB>remote 名称<TAB>远程主干分支<TAB>项目说明（可选）`。本仓库中的清单已加入 `.gitignore`，用于保存本机仓库路径而不提交。技能复制到其他 Git 项目中使用时，也要将该清单加入宿主项目的 `.gitignore`。不要写入凭据。项目说明写简短用途或辨识信息即可。
5. macOS 使用 `scripts/install-launchd.sh` 安装每日任务，Linux 可用 cron/systemd timer 调用 `scripts/sync-repos.sh`。Windows 使用 `scripts/sync-repos.bat` 手动运行或调用 PowerShell 脚本；用 `scripts/install-task.ps1` 安装 Windows 任务计划程序任务。安装前展示触发时间、清单路径和日志路径。

## 同步行为

- 每个仓库先 `git fetch <remote> --prune`，然后对当前分支执行 `git rebase <remote>/<base>`。即使当前分支就是主干，也按此方式快进到远程主干。
- 只操作清洁且可安全 rebase 的本地 checkout。对脏工作区、分支不明、缺失 remote/ref、锁文件或进行中的 Git 操作，跳过该仓库并写明原因。
- 同步永远不执行 push、force push、reset、clean 或 stash。rebase 顺利时不额外造一个提交；rebase 自身会保留并重放开发分支上的本地提交。只有确实产生了独立的冲突修复提交时，才创建本地提交，并说明其内容。
- 遇到冲突时不要凭空自动选 ours/theirs，也不要在无人检查的定时脚本里编造语义修复。保存冲突路径和错误日志，尝试 `git rebase --abort` 回到同步前状态；abort 失败就停止该仓库操作并报告，不能继续其他写操作。由 Codex 在有人发起的工作会话中检查上下文、解决冲突、完成 rebase 并做相关验证。下次定时任务可重试。
- 不把“定时命令已安装”说成“已完成每日同步”。报告清单、调度器状态、最近运行结果和需要人工处理的仓库。

## 本地提交规范

- 需要创建本地提交时，遵循 Conventional Commits：`<type>(<scope>): <中文摘要>`。`scope` 可省略；类型使用 `feat`、`fix`、`docs`、`style`、`refactor`、`perf`、`test`、`build`、`ci`、`chore` 或 `revert` 等标准类型。
- 摘要及正文使用中文，简洁说明改动内容或原因；破坏性变更按规范标记 `!`，并用 `BREAKING CHANGE:` 补充中文说明。
- 示例：`fix(sync): 修正 Windows 清单解析`、`docs(sync): 补充本地提交规范`。
- rebase 正常重放已有提交时不创建额外提交；冲突解决后优先通过 `git rebase --continue` 继续重放。只有流程确实要求独立提交时，才按上述格式创建本地提交；绝不 push。

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
