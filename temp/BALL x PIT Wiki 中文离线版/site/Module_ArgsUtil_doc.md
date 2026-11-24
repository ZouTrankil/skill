# Lua 模块 · ArgsUtil/doc

[原文](https://ballxpit.wiki.gg/wiki/Module:ArgsUtil/doc) · [修订 650](https://ballxpit.wiki.gg/index.php?oldid=650)

```text
This is a basic module for processing args. Usage:

<syntaxhighlight lang="lua">
local util_args = require('Module:ArgsUtil')

local p = {}

function p.main(frame)
  local args = util_args.merge() -- it is not necessary to pass a `frame` object; `merge` will generate its own
  mw.logObject(args)
  -- `args` now contains args passed via the template merged with defaults provided directly via the invoke.
  -- anything the user sent via the template will be given priority.
end

return p
</syntaxhighlight>

== Extending this module ==

By design, {{ml|ArgsUtil}} is shipped with only a single function and no customization available; this simplifies documentation and covers nearly all use cases. An extended version of this module is available at [[support:Module:ArgsUtil|Module:ArgsUtil on the support wiki]] if you want additional functionality; and you can of course feel free to modify this module on your own wiki as needed.
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
