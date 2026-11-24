# Lua 模块 · ArgsUtil

[原文](https://ballxpit.wiki.gg/wiki/Module:ArgsUtil) · [修订 649](https://ballxpit.wiki.gg/index.php?oldid=649)

```lua
local p = {}

function p.merge()
	local f = mw.getCurrentFrame()
	local origArgs = f.args
	local parentArgs = f:getParent().args

	local args = {}
	
	for k, v in pairs(origArgs) do
		v = mw.text.trim(tostring(v))
		if v ~= '' then
			args[k] = v
		end
	end
	
	for k, v in pairs(parentArgs) do
		v = mw.text.trim(v)
		if v ~= '' then
			args[k] = v
		end
	end
	
	return args
end

return p
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
