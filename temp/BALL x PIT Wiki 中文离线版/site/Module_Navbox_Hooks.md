# Lua 模块 · Navbox/Hooks

[原文](https://ballxpit.wiki.gg/wiki/Module:Navbox/Hooks) · [修订 654](https://ballxpit.wiki.gg/index.php?oldid=654)

```lua
-- as of Module:Navbox version 1.2.5

local p = {}
---------------------------------------------------

-- Runs before RANGER does args sanitizing
-- `inputArgs` is the merged input arguments from the template (frame.args + frame:getParent().args)
function p.onSanitizeArgsStart(inputArgs)
end

-- Runs after RANGER does args sanitizing
-- `args` parameter is the sanitized arguments table with normalized keys (in lowercase underscore-case with canonical names) and normalized values.
function p.onSanitizeArgsEnd(args, inputArgs)
end

-- Runs when RANGER loads config table (after onSanitizeArgsEnd and before onBuildTreeStart)
-- `config` parameter is the default config table.
-- `args` parameter is the sanitized arguments table (has not yet merged the DEFAUT_ARGS table).
function p.onLoadConfig(config, args)
end

-- Runs before RANGER converts sanitized arguments table to structured data tree
-- `args` parameter is the sanitized arguments table that has the DEFAUT_ARGS merged.
function p.onBuildTreeStart(args)
end

-- Runs after RANGER converts sanitized arguments table to structured data tree
-- `tree` parameter is the structured data.
-- `args` parameter is the sanitized arguments table.
function p.onBuildTreeEnd(tree, args)
end

---------------------------------------------------
return p
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
