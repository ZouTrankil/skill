# SG Unity CLI 使用说明

SG Unity CLI 由本机命令行程序和 Unity Editor 内的 Bridge 组成，用于连接同版本 Unity 工程并执行项目工具。

## 使用前准备

- 能访问公司 GitLab 的 `ai/unitycli` 仓库和目标游戏项目。
- Unity Editor 使用团队约定版本（Ballpit 当前为 2022.3.62f3）。
- macOS 使用 Apple Silicon 版本；Windows 使用 x64 版本。CLI 和 Bridge 应来自同一套发布记录，不要混用上游安装脚本或自动更新。
- CLI 本身不能替代 Unity Editor；Editor 必须正常编译并加载 Bridge。

## 安装 CLI

构建产物保存在同一 GitLab 仓库的 `sg/binaries` 分支，通过 Git LFS 存储；它是独立的产物分支，不需要合并到源码分支。先安装 Git LFS，再执行：

```sh
git clone --branch sg/binaries --single-branch http://gitlab.sqyx.com/ai/unitycli.git unitycli-binaries
cd unitycli-binaries
git lfs install --local
git lfs pull
```

当前只有 `unity-cli-macos-arm64`；Windows 版本尚待 Windows MSVC 构建及实机验证。对照该分支的 `SHA256SUMS` 校验，例如 macOS 运行 `shasum -a 256 -c SHA256SUMS`。将可执行文件复制到个人工具目录并按需改名为 `unity-cli`，加入 PATH，重新打开终端后运行：

```text
unity-cli --version
unity-cli --help
```

macOS 可在终端执行 `chmod +x /路径/unity-cli`，然后直接运行该文件。Windows 可在 PowerShell 使用 `& 'C:\路径\unity-cli.exe' --version`。如果系统阻止运行，先核对文件来源和校验值，再由用户按系统提示处理。

为了避免 fork 被上游版本自动覆盖，在启动 CLI 的环境设置 `UNITY_CLI_NO_AUTO_UPDATE=1`。macOS 当前终端执行 `export UNITY_CLI_NO_AUTO_UPDATE=1`；PowerShell 当前窗口执行 `$env:UNITY_CLI_NO_AUTO_UPDATE = '1'`。长期使用时需在自己的 shell 环境配置中设置。不要使用默认指向上游的 `unity-cli cli install` 或上游安装脚本更新 SG 构建。

## 接入 Bridge

本仓库的 Bridge 位于 `UnityCliBridge/Packages/unity-cli-bridge`。在游戏项目的 `Packages/manifest.json` 中，已有同名依赖时替换其值，不要添加重复项。示例固定到首次 SG 适配提交：

```json
"com.akiojin.unity-cli-bridge": "http://gitlab.sqyx.com/ai/unitycli.git?path=/UnityCliBridge/Packages/unity-cli-bridge#e5d4db29d006f55af72b12782b5f2b1cecc1b24d"
```

也可以在本机克隆仓库后用 `file:` 引用其包目录；应保证路径在该电脑上存在。Git URL 方式要求 Unity 调用的 Git 可以访问仓库。重新打开工程，等待 Package Manager 解析和 Editor 编译完成，检查 Console 中的错误。项目使用旧 Input Manager；遇到切换输入后端的提示时保留原设置。

## 验证连接和使用

打开目标 Unity 工程后，在该工程的 Unity 根目录执行：

```text
unity-cli system ping
unity-cli tool list
unity-cli tool schema sg_addressables_find_entry
```

`system ping` 成功返回 pong 才说明当前 CLI 已连接到 Editor。`sg_addressables_*` 是 Ballpit 项目内扩展，并非 Bridge 自带工具；只有项目包含并成功编译相应 Editor 代码时才会出现。需要指定项目时可使用 `unity-cli --project-path <Unity工程目录> system ping`。

如果提示 `EDITOR_NOT_FOUND`，先确认 Editor 打开的是目标工程；若连接失败，运行 `unity-cli --project-path <Unity工程目录> doctor`，检查 Bridge 包解析、编译错误和端口。工具列表出现不等于每个操作均已实测，具体项目操作应单独验证。

## 更新

从同一发布记录获取对应平台 CLI、Bridge 提交和校验值；先验证新版本，再更换项目的 Bridge 引用和本机可执行文件。已安装的文件不会自动跟随 Git 分支更新。Git 引用固定到 commit 时，更新需要显式修改 commit 并重新解析包。
