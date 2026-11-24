# CLI 账本

记录本仓库维护或相关技能依赖的独立命令行工具，以及本机入口和跨机器接入方式。技能本身见 [技能账本](技能账本.md)；CLI 安装状态需在各机器分别核对。

| CLI | 用途与来源 | 仓库入口或安装方式 | 本机状态（2026-11-24） | 关联技能 |
| --- | --- | --- | --- | --- |
| Unity CLI | Unity 命令行工具及 Bridge；本仓库维护 akiojin/unity-cli 的项目分支 | [源码与使用说明](cli/unitycli/README.zh.md) | `unity-cli` 在 PATH 中：`~/.local/bin/unity-cli`；安装来源与版本未核对 | [unity-headless](library/project-types/software-development/unity-headless/SKILL.md) |
| ast-grep | AST 结构化搜索与代码改写；[上游](https://ast-grep.github.io/) | 按[官方安装说明](https://ast-grep.github.io/guide/quick-start.html)安装；可用 `uvx --from ast-grep-cli ast-grep` 临时运行 | `ast-grep` 不在 PATH 中；使用 uvx 临时运行 0.51.3 | [ast-grep-refactor](.agents/skills/ast-grep-refactor/SKILL.md) |
| MarkItDown | 将文档转为 Markdown；[上游](https://github.com/microsoft/markitdown) | 按环境安装，例如 `uv tool install 'markitdown[all]'` | `markitdown` 不在 PATH 中；未做转换验收 | [doc-to-markdown](.agents/skills/doc-to-markdown/SKILL.md) |
| NotebookLM CLI | 操作 NotebookLM；[上游 notebooklm-py](https://github.com/teng-lin/notebooklm-py) | 按上游及技能说明安装，Google 账号认证单独配置 | `notebooklm` 不在 PATH 中；认证状态未核对 | [notebooklm](.agents/skills/notebooklm/SKILL.md) |

PATH 检查只反映当前 shell 环境，不代表其他环境未安装。迁移时分别安装工具、配置必要认证，并验证实际工作流；不要将技能可发现误认为 CLI 可用。
