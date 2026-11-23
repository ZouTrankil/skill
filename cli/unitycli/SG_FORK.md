# Sqyx / ballpit2 fork notes

本目录已并入 skill 仓库，以下独立仓库的推送和同步命令保留为迁移前记录。当前源码使用 skill 仓库的 Git 历史管理。

Upstream: https://github.com/akiojin/unity-cli (`upstream` remote, track `develop`).
GitLab: http://gitlab.sqyx.com/ai/unitycli.git (`origin`).

## Branch

- `sg/main` — ballpit2 adaptations on top of upstream develop.

## Changes in this fork (bridge 0.19.2)

- `versionDefines`: `com.sgengine.addressables` also defines `UNITY_ADDRESSABLES` (same as official package id).
- Addressables-unavailable errors mention the SG fork package id.

SG-specific read-only CLI tools (`sg_addressables_*`) live in the **game project** via `[UnityCliTool]`, not in this repo:
`ballpit2/client/client/Assets/SGEngine/ResourceManagementCustom/Editor/UnityCliTools/`.

## Push (when credentials ready)

```bash
cd /Volumes/WD-SSD/work/ai/unitycli
git push -u origin sg/main
# optional tag
git tag sg-0.19.2-1
git push origin sg-0.19.2-1
```

After GitLab has the branch, point the Unity project at:

```json
"com.akiojin.unity-cli-bridge": "http://gitlab.sqyx.com/ai/unitycli.git?path=/UnityCliBridge/Packages/unity-cli-bridge#sg/main"
```

Until then, ballpit2 uses a local `file:` path to this clone.

## Sync upstream

```bash
git fetch upstream
git switch sg/main
git merge upstream/develop
```

Preserve the SG package gate and error details when resolving conflicts. Verify the bridge in the Unity 2022.3 project using `ping`, `addressables_manage` with `list_groups`, and the four `sg_addressables_*` tools. Publish the verified update with `git push origin sg/main`.
