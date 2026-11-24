# Lua 模块 · BallGraph

[原文](https://ballxpit.wiki.gg/wiki/Module:BallGraph) · [修订 4165](https://ballxpit.wiki.gg/index.php?oldid=4165)

```lua
--[[============================================================
  Module:BallGraph — the evolution graph, with no rendering in it.

  Everything that reads BallRecipeEdges as a GRAPH lives here, so
  the walk is written once and tested once. Module:BallTree draws
  it; Module:BallData asks it questions for the Balls tables.

  NOT a cache. Scribunto gives every #invoke a fresh Lua state —
  module-level memoisation does not survive between invokes on the
  same page (verified 2026-09-15: a counter reads 1, 1, 1 across
  three invokes, and so does a mutation of a required module's own
  table). So each invoke pays for its own query. Measured at
  ~0.02s for all 160 edges; if that ever matters, the fix is one
  invoke rendering several things, not a cache that cannot work.
==============================================================]]
local p = {}

local MAX_SLOTS = 4
local MAX_ROWS  = 500
local MAX_DEPTH = 6   -- the real graph is 2 deep; this only stops a cycle

--- recipes: ball -> { {ingredient, ...}, {ingredient, ...} }
--  Outer list is SLOTS (co-ingredients, "and"); inner list is the
--  alternatives for that slot ("or"). Slots are densified: a recipe
--  that somehow stored slot 1 and 3 reads back as 1 and 2.
function p.recipes()
	local rows = mw.ext.cargo.query('BallRecipeEdges', '_pageName,slot_index,ingredient',
		{ where = '_pageNamespace = 0',
		  orderBy = '_pageName,slot_index,ingredient',
		  limit = MAX_ROWS })
	local sparse = {}
	for _, row in ipairs(rows) do
		local ball = row._pageName
		local slot = tonumber(row.slot_index)
		if slot then
			sparse[ball] = sparse[ball] or {}
			sparse[ball][slot] = sparse[ball][slot] or {}
			table.insert(sparse[ball][slot], row.ingredient)
		end
	end
	local out = {}
	for ball, slots in pairs(sparse) do
		local dense = {}
		for i = 1, MAX_SLOTS do
			if slots[i] then table.insert(dense, slots[i]) end
		end
		out[ball] = dense
	end
	return out
end

--- unlocks: ball -> unlock condition, for the conditions worth printing.
--  14 of the 21 base balls say "Unlocked by default", which under a
--  diagram node is noise. Only the 7 that name a pit come back.
function p.unlocks()
	local rows = mw.ext.cargo.query('Balls', '_pageName,unlock_condition',
		{ where = '_pageNamespace = 0 AND unlock_condition != "" '
		          .. 'AND unlock_condition != "Unlocked by default"',
		  limit = MAX_ROWS })
	local out = {}
	for _, row in ipairs(rows) do out[row._pageName] = row.unlock_condition end
	return out
end

--- ancestorTree: the recipe of `root`, expanded down to base balls.
--
--  A TREE, not the graph: a ball reached twice appears twice.
--  Nosferatu needs Vampire through two different paths and draws it
--  twice. Sharing the node would mean an edge crossing columns,
--  which is the whole hard problem of graph layout — and the reason
--  this renderer is 150 lines instead of a layout engine.
--
--  Node shapes, one of:
--    { options = { 'Stone', 'Poison' } }        a leaf card, 1+ balls
--    { ball = 'Brimstone', children = { ... } } a recipe
--
--  A multi-option slot is ALWAYS a leaf. That is not a shortcut: no
--  slot in the game offers an evolved ball as an alternative (checked
--  across all 69 recipes). If one ever does, it renders as a leaf
--  card rather than wrongly — losing depth, not correctness.
function p.ancestorTree(root, recipes)
	local function build(ball, depth, seen)
		local slots = recipes[ball]
		if not slots or depth > MAX_DEPTH or seen[ball] then
			return { options = { ball } }
		end
		seen = mw.clone(seen)
		seen[ball] = true
		local node = { ball = ball, children = {} }
		for _, options in ipairs(slots) do
			if #options == 1 then
				table.insert(node.children, build(options[1], depth + 1, seen))
			else
				table.insert(node.children, { options = options })
			end
		end
		return node
	end
	return build(root, 1, {})
end

--- isIngredient: which balls are used in some recipe, i.e. can be
--  evolved further. One pass over the same data the caller already has.
function p.isIngredient(recipes)
	local out = {}
	for _, slots in pairs(recipes) do
		for _, options in ipairs(slots) do
			for _, ingredient in ipairs(options) do out[ingredient] = true end
		end
	end
	return out
end

return p
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
