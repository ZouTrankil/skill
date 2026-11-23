# Push this fork to GitLab

Remote is already set:

```text
origin    http://gitlab.sqyx.com/ai/unitycli.git
upstream  https://github.com/akiojin/unity-cli.git
```

Branch `sg/main` contains the `com.sgengine.addressables` package gate in commit `e5d4db2`. The corrected guides are local worktree files. Pushing the current branch publishes the gate commit. To publish the guide updates as well, include `SG_FORK.md` and `PUSH_TO_GITLAB.md` in a branch commit before pushing.

## Publish the branch

Run this from the fork checkout.

```bash
git push -u origin sg/main
```

In `client/client/Packages/manifest.json` in the game repository, replace the temporary `file:` dependency with the GitLab dependency.

```json
"com.akiojin.unity-cli-bridge": "http://gitlab.sqyx.com/ai/unitycli.git?path=/UnityCliBridge/Packages/unity-cli-bridge#sg/main"
```

Open the project in Unity 2022.3 to regenerate `Packages/packages-lock.json`. Check that the bridge entry has `source: git` and resolves to the published branch commit, then run `unity-cli tool call ping` and `unity-cli tool call addressables_manage --json '{"action":"list_groups"}'` from the Unity project folder. The project uses the old Input Manager (`activeInputHandler: 0`), so start the Editor with `unity-cli editor open` to preserve that configuration. If a fresh import prompts to enable the new input backend, choose to keep the current input settings.
