# Windows 构建与验收交接

目标：在 Windows x64 机器上构建 SG Unity CLI，验证连接 Ballpit Unity Editor，并将验证后的程序上传到现有 GitLab 产物分支。

## 当前状态

- 源码仓库：`http://gitlab.sqyx.com/ai/unitycli.git`，源码分支 `sg/main`，Bridge 位于 `UnityCliBridge/Packages/unity-cli-bridge`。
- 已验证的代码基线为 `e5d4db29d006f55af72b12782b5f2b1cecc1b24d`；后续源码分支提交是使用文档。构建前确认实际 HEAD 和差异，并在产物记录中写明构建 commit。
- CLI 版本 `0.19.1`、Bridge 版本 `0.19.2`。macOS Apple Silicon 构建已上传 `sg/binaries`，本机 Unity 2022.3.62f3 下 ping、Addressables 分组查询和项目工具调用通过；Bridge 使用的是本机 `file:` 引用。
- Windows 尚未构建或实机验证。macOS 上交叉编译 `x86_64-pc-windows-gnu` 失败，原因是 `ort-sys` 无该目标的 ONNX Runtime 预编译库。上游构建流程使用 `x86_64-pc-windows-msvc`。
- `sg_addressables_*` 工具属于 Ballpit 工程，不在 CLI 仓库。此前测试的项目文件及 Bridge 引用在 Mac 工作区中尚未提交；Windows 上要先确认目标 Ballpit 代码是否包含这些工具，不能假定拉取仓库就有。

## 目标机器准备

- Windows x64；Unity Hub 安装 Unity `2022.3.62f3` 并能打开 Ballpit 工程。
- Git、Git LFS、Rust stable 和 MSVC C++ 构建工具（Visual Studio 或 Build Tools，包含 C++ 桌面开发工具及 Windows SDK）。命令均在 PowerShell 运行。
- 有 GitLab 仓库读取和推送权限，网络能下载 Cargo 依赖及 ONNX Runtime 构建依赖。不要输出或写入令牌。
- 先确认目标目录和仓库现有分支、staged、unstaged、未跟踪文件；保留已有改动。以下路径请自行替换，不要覆盖已有仓库或项目。

## 1. 获取源码并构建

```powershell
git clone --branch sg/main --single-branch http://gitlab.sqyx.com/ai/unitycli.git C:\work\unitycli
Set-Location C:\work\unitycli
git status --short --branch
git log -1 --oneline
rustc -Vv
cargo -V
rustup target add x86_64-pc-windows-msvc
cargo build --locked --release --target x86_64-pc-windows-msvc
if ($LASTEXITCODE -ne 0) { throw 'Windows 构建失败；保留完整错误并定位原因' }
$exe = (Resolve-Path '.\target\x86_64-pc-windows-msvc\release\unity-cli.exe').Path
$env:UNITY_CLI_NO_AUTO_UPDATE = '1'
& $exe --version
& $exe --help
Get-FileHash $exe -Algorithm SHA256
git rev-parse HEAD
```

上述 clone 假设目录不存在；如果已有工作副本，先检查状态并复用，不要强制覆盖或切换有未提交改动的工作树。记录 Rust、Windows、commit、CLI 版本、SHA-256 和构建结果；`--help` 成功仅证明程序可启动。

## 2. 准备 Bridge 并验证真实工程

先检查 Windows Ballpit 工程的 `Packages/manifest.json`、`packages-lock.json` 和工作区状态。若尚未配置 Bridge，在保留已有变更的前提下，参照 [SG Unity CLI 使用说明](SG-Unity-CLI使用说明.md) 使用 GitLab 固定 commit 引用；这会修改游戏项目配置，Unity 解析时可能更新锁文件，需记录差异。确保 Unity 使用的 Git 能访问 GitLab。保留项目原有 Input Manager 设置。

在 Unity Hub 打开 Ballpit 工程并等待包解析、编译结束；项目根目录是包含 `Assets`、`Packages`、`ProjectSettings` 的目录。以下变量替换为实际路径：

```powershell
$project = 'C:\work\ballpit2\client\client'
$env:UNITY_CLI_NO_AUTO_UPDATE = '1'
& $exe --project-path $project --output json raw ping
& $exe --project-path $project --output json tool call addressables_manage --json '{"action":"list_groups"}'
& $exe --project-path $project --output json tool schema sg_addressables_find_entry
& $exe --project-path $project --output json tool call sg_addressables_report_first_pack_flags
```

验收要看 JSON 的 `success`、错误信息和返回内容：ping 应返回 `pong`、实际项目路径及 Bridge 版本；Addressables 应返回实际分组；自定义工具应能发现并返回实际数据。若缺少 `sg_addressables_*`，记录为项目工具代码未接入或未编译，先检查该工程的实际文件与 Console 错误，不把 Bridge 成功误记为项目工具通过。已有 Editor 由使用者保留，不要关闭不属于本任务的进程。

## 3. 上传构建产物

仅在构建和真实调用验证通过后发布。`sg/binaries` 是独立的 Git LFS 产物分支，已有 macOS 文件、README 和 SHA256SUMS，必须保留它们。单独克隆该分支到新目录，避免切换源码工作区：

```powershell
git clone --branch sg/binaries --single-branch http://gitlab.sqyx.com/ai/unitycli.git C:\work\unitycli-binaries
Set-Location C:\work\unitycli-binaries
git lfs install --local
git lfs pull
git status --short --branch
git lfs ls-files
Copy-Item $exe .\unity-cli-windows-x64.exe
git lfs track 'unity-cli-*'
Get-FileHash .\unity-cli-windows-x64.exe -Algorithm SHA256
```

重新读取并更新现有 `README.md`，写入 Windows 文件名、构建 commit、CLI/Bridge/Unity 版本及实际验收范围；在 `SHA256SUMS` 中保留 macOS 原有校验行，新增 Windows 的小写 SHA-256 和文件名（以两个空格分隔）。核对 `git status`、`.gitattributes` 和 `git diff` 后，只暂存本次相关文件并提交、推送：

```powershell
git add .gitattributes README.md SHA256SUMS unity-cli-windows-x64.exe
git diff --cached --stat
git diff --cached --check
git commit -m 'build(cli): 发布 Windows x64 构建'
git push origin sg/binaries:sg/binaries
```

推送前检查远端是否有新提交；若被拒绝，先 fetch 并检查双方差异，保留其他人的产物，不强推。推送后从新的独立目录克隆 `sg/binaries`，运行 `git lfs install --local`、`git lfs pull`，用 `Get-FileHash` 与 `SHA256SUMS` 比较并执行下载后的程序 `--version`，确认拿到的是真实二进制而非 LFS 指针。最后按验证结果更新源码分支中的 [使用说明](SG-Unity-CLI使用说明.md)，使 Windows 下载状态与实际一致。

## 交付记录

记录源码 commit、构建命令和日志、产物 SHA-256、Windows 和 Unity 版本、Bridge 来源、ping 及各工具结果、GitLab 产物分支 commit、远端重下载结果，以及未通过项。若构建或运行受凭据、依赖下载、编译错误或 Unity 环境阻塞，保留具体错误和恢复条件，不上传未经验证的产物冒充完成。
