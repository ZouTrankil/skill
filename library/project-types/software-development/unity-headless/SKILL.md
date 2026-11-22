---
name: unity-headless
description: 在 Unity 工程中执行无界面资源查询、EditMode 或 PlayMode 测试、已有 Editor 静态方法和烘焙任务。按任务选择原生 batchmode 或复用已接入 akiojin unity-cli Bridge 的 Editor，适用于连续改测和定位启动耗时。
---

# Unity 无界面执行

## 先确定工程和验收目标

从用户指定目录或当前仓库定位同时含有 `Assets/`、`Packages/manifest.json`、`ProjectSettings/ProjectVersion.txt` 的工程，读取版本和项目自带的测试或构建入口。多个工程时按任务所指资源定位，仍不明确再询问。按本机安装信息选择对应版本的 Editor。

| 要验收的结果 | 运行方式 | 核对什么 |
| --- | --- | --- |
| 资源元数据、对象状态、无需渲染的测试 | `-batchmode -nographics`，连续查询可复用 Bridge | 具体资源、字段或断言；进入 Play Mode 后等待实际状态变化 |
| 已有 Editor 静态方法、构建或导出 | 使用项目现有 runner，原生入口为 `-executeMethod Namespace.Type.Method` | 目标平台、方法完成信号、输出文件或构建报告 |
| 光照烘焙、需要 GPU 的离屏任务 | `-batchmode` 并保留图形设备；确认主机和目标图形 API 可用 | 作业终态、成功标记及产物 |
| 窗口焦点、真实设备输入、最终显示效果 | 按需求选择 GUI Editor 或目标 Player | 指定窗口或设备中的交互与画面 |

## 减少重复等待

- 只查 Unity 版本、包依赖或已导出的报告时，直接读文件。需要 Unity 解析资源引用、查询导入结果或执行游戏逻辑时，再使用 Editor。
- 一次性验收若有多组同模式用例，将相关用例放进同一次 test run，用过滤条件选中它们。需要全新进程验证启动行为的用例单独运行。
- 连续改资源、查结果或改代码、跑用例时，复用同一工程的 Editor。将一组相关修改写完，按工程工作流触发或等待导入、编译和域重载；确认编译无错、Bridge 重新就绪后再跑目标用例。每轮使用独立报告路径。
- 重复验证时保持 Editor 版本、构建目标一致，复用工程已有的 `Library/` 导入缓存。若验收目标就是首次导入，用独立工作副本测量，保留开发工程的缓存。
- 用户问速度时，以命令发起到结果可用的墙钟时间为准。分别记录启动到 ready、常驻首轮及后续轮次、原生启动到退出；注明缓存状态和测试过滤条件，核对实际用例一致。XML 的测试耗时另列。

## 原生 Unity

工程已有测试脚本时优先使用它。以下为已接入 Unity Test Framework 的 POSIX 示例。在实际 Unity 工程根目录执行，令 `UNITY_EDITOR` 指向 Editor 可执行文件，`TEST_FILTER` 为该工程已有的测试名或类名，`RESULT_DIR` 为当前任务的输出目录。

```sh
project=$(pwd -P)
mkdir -p "$RESULT_DIR"
"$UNITY_EDITOR" -batchmode -nographics -projectPath "$project" \
  -runTests -testPlatform EditMode -testFilter "$TEST_FILTER" \
  -testResults "$RESULT_DIR/results.xml" -logFile "$RESULT_DIR/editor.log"
```

为本次运行使用新报告路径。检查退出码、报告中实际命中的用例、失败和跳过原因；零用例不能证明指定测试通过。原生测试由 test runner 控制退出。异步导出或烘焙应等待完成再退出。

## 工程已有 akiojin unity-cli Bridge 时

1. 检查本机 `unity-cli editor open --help`、包依赖及工程是否已被 Editor 打开。该 CLI 的 `--headless` 在新实例上使用 `-batchmode -nographics`。复用已有实例时其启动模式保持原状；同一工程同时只开一个 Editor。
2. 在实际 Unity 工程根目录设置 `project=$(pwd -P)`，运行 `unity-cli --project-path "$project" --output json editor open --headless --wait-ready 150`。记录返回的 `data.launched`、`data.pid` 和 `data.port`，将实际端口赋给 `port`。
3. 先执行下列 ping，核对 `data.projectPath` 与工程规范路径一致。已知工具名时只取该工具的参数 schema；需要盘点接口时省略工具名，导出当前工程的完整清单。版本、可选包、输入后端以及宿主模式都会影响可执行范围。
4. 若任务结束且本次启动了实例，再次核对端口、工程路径、Editor PID，执行 `unity-cli --project-path "$project" --port "$port" editor close`。复用的 Editor 留给原使用者。

```sh
unity-cli --project-path "$project" --port "$port" --output json raw ping
unity-cli --project-path "$project" --port "$port" --output json tool schema "$tool_name"
```

同一实例上反复跑 EditMode 测试，可用 `unity-cli --project-path "$project" --port "$port" test --mode editmode --filter "$TEST_FILTER" --output "$RESULT_DIR/$run_id.xml"`。先创建结果目录，每轮给 `run_id` 赋不同值，按报告核对目标用例。

需确认宿主模式且工具清单包含 `eval_csharp` 时，执行以下只读探针。核对调用完成、无异常及 `data.value`；`True/Null` 表示批处理且未初始化图形设备。

```sh
unity-cli --project-path "$project" --port "$port" --output json tool call eval_csharp \
  --json '{"code":"UnityEngine.Application.isBatchMode.ToString() + \"/\" + UnityEngine.SystemInfo.graphicsDeviceType.ToString()"}'
```

需要为图形批处理启动常驻 Bridge 时，直接启动对应 Unity Editor，传入 `-batchmode -projectPath` 和 `-logFile`，保留图形设备。对支持该设置的 akiojin Bridge，设置 `UNITY_CLI_ALLOW_BATCH_HOST=1`；如需指定端口，使用 `UNITY_CLI_PORT_OVERRIDE`。等待目标实例通过 ping 后再派发作业。
