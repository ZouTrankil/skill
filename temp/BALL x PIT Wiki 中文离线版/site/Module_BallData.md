# Lua 模块 · BallData

[原文](https://ballxpit.wiki.gg/wiki/Module:BallData) · [修订 4178](https://ballxpit.wiki.gg/index.php?oldid=4178)

```lua
--[[--------------------------------------------------------------
  Module:BallData

  Two jobs:
    1. storeEdges  — turn the ingredient_N_options parameters an
       editor typed into {{BallData}} into BallRecipeEdges rows.
    2. renderCombination / evolvesInto — read those rows back and
       render them.

  TERMINOLOGY: this models EVOLUTION. The Fusion Reactor is a pickup
  that lets you either evolve max-level balls into a named Evolved
  Ball or fuse two into a generic Fused Ball.

  IDENTITY: everything keys on Cargo's built-in _pageName. There is
  no page_name field and no display alias anywhere in this file.
  An alias in an ingredient value is a failed join, and the
  maintenance report lists it — see Project:Cargo tables.
----------------------------------------------------------------]]

local p = {}

-- The player can never hold more than 4 balls, so a recipe can never
-- have more than 4 ingredient slots. A game rule, not a guess.
local MAX_SLOTS = 4

--- Split a comma-separated option list into trimmed, non-empty names.
--  Values are canonical _pageNames -- the article title exactly,
--  never a redirect or a display alias.
local function splitOptions(s)
	local out = {}
	if not s then return out end
	for item in string.gmatch(s, '([^,]+)') do
		local trimmed = mw.text.trim(item)
		if trimmed ~= '' then
			table.insert(out, trimmed)
		end
	end
	return out
end

--- Collect the populated slots, in order, from the invoke args.
--  Returns { {opt, opt}, {opt} } — outer index is the slot.
local function gatherSlots(frame)
	local slots = {}
	for i = 1, MAX_SLOTS do
		local opts = splitOptions(frame.args[i])
		if #opts > 0 then
			table.insert(slots, opts)
		end
	end
	return slots
end

--[[----------------------------------------------------------------
  storeEdges

  Called from the <includeonly> of Template:BallData. Expands one
  {{BallRecipeEdge}} per alternative, which is where the actual
  #cargo_store happens.

  slot_index is the position AFTER empty slots are dropped, so a
  recipe authored in slots 1 and 3 stores as 1 and 2. Slot numbers
  carry no meaning beyond "these are different co-ingredients".

  WHY frame:preprocess: Scribunto does not re-expand a module's
  return value — parser functions in returned text are treated as
  already-expanded text — so the store calls have to be expanded
  here. This is the single most fragile line in the whole schema and
  P2 exists to prove it fires. Check Special:CargoTables/BallRecipeEdges
  after saving Radiation Beam; it must show four rows.
------------------------------------------------------------------]]
function p.storeEdges(frame)
	local wikitext = {}
	for slotIndex, options in ipairs(gatherSlots(frame)) do
		for _, ingredient in ipairs(options) do
			table.insert(wikitext, string.format(
				'{{BallRecipeEdge|slot_index=%d|ingredient=%s}}',
				slotIndex, ingredient))
		end
	end
	if #wikitext == 0 then return '' end          -- base and baby balls
	return frame:preprocess(table.concat(wikitext))
end

--[[----------------------------------------------------------------
  Reading the recipe back
------------------------------------------------------------------]]

--- All edges for one ball, grouped into slots.
--  Returns { {ingredient, ingredient}, {ingredient} }.
local function recipeOf(pageName)
	local rows = mw.ext.cargo.query('BallRecipeEdges',
		'slot_index,ingredient',
		{ where = '_pageName = "' .. pageName .. '"',
		  orderBy = 'slot_index,ingredient',
		  limit = 50 })
	local slots = {}
	for _, row in ipairs(rows) do
		local i = tonumber(row.slot_index)
		slots[i] = slots[i] or {}
		table.insert(slots[i], row.ingredient)
	end
	return slots
end

--- renderCombination: "Iron + (Ghost or Dark)".
--  A slot with one option renders bare; a slot with alternatives is
--  parenthesised and joined with "or". That parenthesisation is the
--  slot boundary — it is the reason slot_index is stored at all.
function p.renderCombination(frame)
	local pageName = frame.args[1] or mw.title.getCurrentTitle().text
	local parts = {}
	for _, options in ipairs(recipeOf(pageName)) do
		local links = {}
		for _, name in ipairs(options) do
			table.insert(links, '{{il|' .. name .. '}}')
		end
		if #links == 1 then
			table.insert(parts, links[1])
		else
			table.insert(parts, '(' .. table.concat(links, ' or ') .. ')')
		end
	end
	if #parts == 0 then return '' end
	return frame:preprocess(table.concat(parts, ' + '))
end

--- evolvesInto: every ball that lists this one as an ingredient.
--  This fills the Evolutions block in the article infobox and the
--  "Can be evolved further" column on [[Balls]]. Never stored.
function p.evolvesInto(frame)
	local pageName = frame.args[1] or mw.title.getCurrentTitle().text
	local rows = mw.ext.cargo.query('BallRecipeEdges',
		'_pageName',
		{ where = 'ingredient = "' .. pageName .. '"',
		  groupBy = '_pageName',
		  orderBy = '_pageName',
		  limit = 200 })
	local links = {}
	for _, row in ipairs(rows) do
		table.insert(links, '{{il|' .. row._pageName .. '}}')
	end
	return frame:preprocess(table.concat(links, ', '))
end

--[[----------------------------------------------------------------
  RENDER FUNCTIONS

  These are the only things here that query Cargo. Everything a page
  knows about ITSELF is passed in as a template parameter and never
  queried — see ../BallTemplates/ARTICLE_PLAN.md.

  UNTESTED ON-WIKI. evolutionsTable, creationLine, ballTable and
  navboxGroup have never run against a real Cargo install.
------------------------------------------------------------------]]

--- charactersList: render starting_characters as icon links.
--  Takes the whole list and renders all of it. The infobox used to take
--  character1 and character2, a cap inherited from hand-typed days: the
--  field is a list, four balls already have two, and nothing in the game
--  says three is impossible.
function p.charactersList(frame)
	local out = {}
	for _, name in ipairs(splitOptions(frame.args[1])) do
		table.insert(out, string.format(
			'<span class="pixel-img">[[File:%s.png|25px|link=%s]]</span> [[%s]]',
			name, name, name))
	end
	return table.concat(out, '<br>')
end

--- charactersLabel: "Character" or "Characters", by count.
function p.charactersLabel(frame)
	return #splitOptions(frame.args[1]) > 1 and 'Starting Characters' or 'Starting Character'
end

--- furtherEvolvable: which of these balls are themselves an ingredient?
--  ONE query for the whole list, not one per row. A ball "can be evolved
--  further" exactly when some recipe uses it, which is what having a row
--  in BallRecipeEdges.ingredient means.
local function furtherEvolvable(names)
	if #names == 0 then return {} end
	local quoted = {}
	for _, n in ipairs(names) do
		table.insert(quoted, '"' .. n .. '"')
	end
	local rows = mw.ext.cargo.query('BallRecipeEdges', 'ingredient',
		{ where = '_pageNamespace = 0 AND ingredient IN ('
		          .. table.concat(quoted, ',') .. ')',
		  groupBy = 'ingredient', limit = 200 })
	local set = {}
	for _, row in ipairs(rows) do set[row.ingredient] = true end
	return set
end

--- Every slot of every named ball, in ONE query.
--  Returns { [ball] = { [slot_index] = {ingredient, ...} } }.
local function recipesOf(names)
	if #names == 0 then return {} end
	local quoted = {}
	for _, n in ipairs(names) do
		table.insert(quoted, '"' .. n .. '"')
	end
	local rows = mw.ext.cargo.query('BallRecipeEdges',
		'_pageName,slot_index,ingredient',
		{ where = '_pageNamespace = 0 AND _pageName IN ('
		          .. table.concat(quoted, ',') .. ')',
		  orderBy = '_pageName,slot_index,ingredient',
		  limit = 500 })
	local out = {}
	for _, row in ipairs(rows) do
		local ball = row._pageName
		local i = tonumber(row.slot_index)
		out[ball] = out[ball] or {}
		out[ball][i] = out[ball][i] or {}
		table.insert(out[ball][i], row.ingredient)
	end
	return out
end

--- Slots as a dense, ordered list.
local function denseSlots(slotMap)
	local out = {}
	for i = 1, MAX_SLOTS do
		if slotMap[i] then table.insert(out, slotMap[i]) end
	end
	return out
end

--- Render one slot: bare if single, parenthesised "or" list if not.
local function renderSlot(options)
	local links = {}
	for _, name in ipairs(options) do
		table.insert(links, '{{BallLink|' .. name .. '}}')
	end
	if #links == 1 then return links[1] end
	return '(' .. table.concat(links, ' or ') .. ')'
end

--- Cartesian product of slots -> a list of concrete ingredient sets.
--  Burn + (Poison or Stone) gives {{Poison}, {Stone}}: two
--  alternative recipes, which is why Brimstone renders as two lines.
local function expand(slots)
	local out = {{}}
	for _, options in ipairs(slots) do
		local nextOut = {}
		for _, partial in ipairs(out) do
			for _, opt in ipairs(options) do
				local copy = {}
				for _, v in ipairs(partial) do table.insert(copy, v) end
				table.insert(copy, opt)
				table.insert(nextOut, copy)
			end
		end
		out = nextOut
	end
	return out
end

--- creationLine: this ball's own recipe, in the slot/options shape.
--  Silent on base and baby balls, so it is safe in a shared skeleton.
function p.creationLine(frame)
	-- An explicit ball name overrides the page, so /doc can show a real
	-- example and any page can render another ball's recipe.
	local this = frame.args[1]
	if this == nil or this == '' then this = mw.title.getCurrentTitle().text end
	local slots = denseSlots(recipesOf({ this })[this] or {})
	if #slots == 0 then return '' end
	local parts = {}
	for _, options in ipairs(slots) do
		table.insert(parts, renderSlot(options))
	end
	-- The bare combination, with no sentence around it: this is the
	-- value of the infobox's "Created by" row, which supplies the
	-- label. A prose line would read "Created by Created by combining
	-- X + Y". The page-level section uses {{BallCreationTable}}.
	return frame:preprocess(table.concat(parts, ' + '))
end

--[[--------------------------------------------------------------
  creationTable — the same recipe as the "== Evolution Recipe ==" block.

  The table is assembled HERE, not in {{BallCreationTable}}, because a
  wikitable cannot be passed through a parser function: every "|" in
  "{|", "|-", "| cell" and "|}" is read as an argument separator, so
  {{#if:x|{| class="wikitable" … |}}} shreds the table and emits
  fragments like `class="wikitable" ! Combination}`. In Lua a pipe is
  an ordinary character, and the emptiness test is a plain if.

  Returns '' on a base or baby ball, so the caller needs no guard.
----------------------------------------------------------------]]
function p.creationTable(frame)
	local combination = p.creationLine(frame)
	if combination == '' then return '' end
	return table.concat({
		'{| class="wikitable"',
		'! Combination',
		'|-',
		'| ' .. combination,
		'|}',
	}, '\n')
end

--- evolutionsTable: the "== Evolutions ==" section.
--  For every ball whose recipe includes this one, render that recipe's
--  OTHER slots. {{Combination}} already prefixes {{PAGENAME}}, so only
--  the co-ingredients are passed.
function p.evolutionsTable(frame)
	local this = frame.args[1]
	if this == nil or this == '' then this = mw.title.getCurrentTitle().text end

	-- _pageNamespace = 0 keeps user sandboxes out. Anything transcluding
	-- {{BallData}} stores rows, so without this a test page in User: space
	-- appears in every article's Evolutions table, rendered with its full
	-- namespace-qualified title.
	local rows = mw.ext.cargo.query('BallRecipeEdges', '_pageName',
		{ where = '_pageNamespace = 0 AND ingredient = "' .. this .. '"',
		  groupBy = '_pageName', orderBy = '_pageName', limit = 200 })
	local results = {}
	for _, row in ipairs(rows) do table.insert(results, row._pageName) end

	-- A terminal ball (and every baby ball) is an ingredient of nothing.
	-- The section heading is on the page either way, so saying so beats
	-- an empty section that reads as a broken template.
	if #results == 0 then
		return "''This ball cannot be evolved further.''"
	end

	local recipes = recipesOf(results)
	local further = furtherEvolvable(results)
	local marked = false
	local out = { '{| class="wikitable sortable"', '|-', '! Combination !! Evolution' }
	for _, ball in ipairs(results) do
		local others = {}
		for _, options in ipairs(denseSlots(recipes[ball] or {})) do
			local holdsThis = false
			for _, name in ipairs(options) do
				if name == this then holdsThis = true end
			end
			if not holdsThis then table.insert(others, options) end
		end
		local lines = {}
		for _, combo in ipairs(expand(others)) do
			table.insert(lines, '{{Combination|' .. table.concat(combo, '|') .. '}}')
		end
		local mark = ''
		if further[ball] then
			mark = '<sup>*</sup>'
			marked = true
		end
		table.insert(out, '|-')
		table.insert(out, '| ' .. table.concat(lines, '<br>') ..
			' || {{BallLink|' .. ball .. '}}' .. mark)
	end
	table.insert(out, '|}')

	-- The legend only appears when something carries the marker: a
	-- footnote explaining a symbol that is not on the page is noise.
	if marked then
		table.insert(out, "<small>* Can be evolved further.</small>")
	end
	return frame:preprocess(table.concat(out, '\n'))
end

--- navboxGroup: the balls of one class, as icon links.
function p.navboxGroup(frame)
	local rows = mw.ext.cargo.query('Balls', '_pageName',
		{ where = '_pageNamespace = 0 AND ball_class = "'
		          .. (frame.args[1] or 'base') .. '"',
		  orderBy = '_pageName', limit = 200 })
	-- A bullet per ball, which is the shape the hand-maintained navbox
	-- used and what {{Navbox}}'s pill styling expects. The leading
	-- newline matters: a "*" only starts a list at the start of a line.
	local links = {}
	for _, row in ipairs(rows) do
		table.insert(links, '*{{BallLink|' .. row._pageName .. '}}')
	end
	if #links == 0 then return '' end
	return frame:preprocess('\n' .. table.concat(links, '\n'))
end

--- ballTable: one of the three tables on [[Balls]].
--  TODO before P4: emit the data-basics / data-intermediates
--  attributes evoball-filter.js reads, and fill "Can be evolved
--  further" — both come from the closure walk sketched below.
function p.ballTable(frame)
	local class = frame.args[1] or 'base'
	local rows = mw.ext.cargo.query('Balls',
		'_pageName,display_name,summary,starting_characters,' ..
		'unlock_condition,on_hit_effects,status_triggers,status_effects',
		{ where = '_pageNamespace = 0 AND ball_class = "' .. class .. '"',
		  orderBy = '_pageName', limit = 200 })

	local header
	if class == 'base' then
		header = '! Icon !! Name !! Description !! Character !! Unlock Condition ' ..
		         '!! On-Hit Effect(s) !! Status Trigger(s) !! Status Effect(s)'
	elseif class == 'evolved' then
		header = '! Icon !! Name !! Description !! Combination ' ..
		         '!! On-Hit Effect(s) !! Status Trigger(s) !! Status Effect(s) ' ..
		         '!! Can be evolved further'
	else
		header = '! Icon !! Name !! Description'
	end

	local names = {}
	for _, row in ipairs(rows) do table.insert(names, row._pageName) end
	local recipes = (class == 'evolved') and recipesOf(names) or {}

	local out = { '{| class="sortable wikitable trackable"', '|-', header }
	for _, row in ipairs(rows) do
		local label = row.display_name
		if label == nil or label == '' then label = row._pageName end
		local cells = {
			'[[File:' .. row._pageName .. '.png|25px|link=' .. row._pageName .. ']]',
			'[[' .. row._pageName .. '|' .. label .. ']]',
			row.summary,
		}
		if class == 'evolved' then
			local parts = {}
			for _, options in ipairs(denseSlots(recipes[row._pageName] or {})) do
				table.insert(parts, renderSlot(options))
			end
			table.insert(cells, table.concat(parts, ' + '))
		end
		if class ~= 'baby' then
			if class == 'base' then
				table.insert(cells, row.starting_characters)
				table.insert(cells, row.unlock_condition)
			end
			table.insert(cells, row.on_hit_effects)
			table.insert(cells, row.status_triggers)
			table.insert(cells, row.status_effects)
		end
		if class == 'evolved' then
			table.insert(cells, '')
		end
		table.insert(out, '|-')
		table.insert(out, '| ' .. table.concat(cells, ' || '))
	end
	table.insert(out, '|}')
	return frame:preprocess(table.concat(out, '\n'))
end

--[[----------------------------------------------------------------
  P6 — transitive closure

  resolveBasics(ball) returns every BASE ball reachable through the
  evolution graph:
    Armageddon -> Inferno + Storm
               -> (Burn, Time, Wind) + (Lightning, Wind)
               -> Burn, Lightning, Time, Wind

  Do NOT store the result: it depends on an arbitrary chain of other
  pages, and Cargo has no recursive CTE.

  Implementation:
    1. ONE query for the whole edge list —
         mw.ext.cargo.query('BallRecipeEdges', '_pageName,ingredient',
                            { limit = 500 })
       plus one for Balls (_pageName, ball_class).
    2. Build ball -> {ingredients} and ball -> class in local tables.
    3. Depth-first walk with a visited set. Recursion stops at
       ball_class == 'base'. The graph is a DAG today, but guard for
       cycles anyway — one bad edit introduces one.
    4. Memoise per parse: a page with 69 rows must not walk 69 times.

  Regression target: reproduce the data-basics / data-intermediates
  attributes already in balls/evoball_table_filterable.mediawiki. That
  file is a known-good fixture — diff against it, do not eyeball it.
------------------------------------------------------------------]]

--[[--------------------------------------------------------------
  linkEffects — link the NAMED status effects in a stored list.

  status_effects holds two kinds of value and always has:

    named effects   Burn, Bleed, Berserk, Petrify...   -> linked
    action phrases  "Kill instantly", "Steal health",
                    "Spawn stone \[\[Baby Ball\]\]"        -> left alone

  Only the first kind is a thing with a name a reader can look up, so
  only the first kind is linked, and the link is to a section of
  \[\[Status Effects\]\] rather than to a page per effect. Doing it here
  and not in the stored value is deliberate: the database keeps a bare
  name that can be sorted, matched and joined to a StatusEffects table
  later, and adding an effect to EFFECTS below links it on all 91
  articles at once. Berserk was the case that prompted this — it is a
  real effect with no article, and a bare word in the infobox.

  An action phrase that already carries its own \[\[link\]\] passes
  through untouched: it is linking a page (Baby Ball), not an effect.
----------------------------------------------------------------]]
local EFFECTS = {
	'Berserk', 'Bleed', 'Blind', 'Burn', 'Charm', 'Curse', 'Darkflame',
	'Disease', 'Freeze', 'Frostburn', 'Landslide', 'Lovestruck',
	'Meteor shower', 'Overgrowth', 'Petrify', 'Poison', 'Radiation',
	'Slow', 'Timestop Field', 'Tumor', 'Venom',
}
local EFFECT_SET = {}
for _, name in ipairs(EFFECTS) do EFFECT_SET[name] = true end

function p.linkEffects(frame)
	local out = {}
	for _, value in ipairs(splitOptions(frame.args[1])) do
		if EFFECT_SET[value] then
			table.insert(out, '[[Status Effects#' .. value .. '|' .. value .. ']]')
		else
			table.insert(out, value)
		end
	end
	return table.concat(out, ', ')
end

return p
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
