# Lua 模块 · BallTree

[原文](https://ballxpit.wiki.gg/wiki/Module:BallTree) · [修订 4171](https://ballxpit.wiki.gg/index.php?oldid=4171)

```lua
--[[============================================================
  Module:BallTree — draws an evolved ball's recipe as a diagram.

  The shape follows Terraria's crafting trees and OSRS's family
  trees: an HTML table where every cell is one grid square, and the
  connecting lines are CSS BORDERS on otherwise empty cells. A table
  is used, rather than absolute positioning, because it makes
  alignment free — a wide card widens its column, and the elbow
  below it is in that same column, so it stays centred with no
  arithmetic.

  Ingredients are at the top, the result at the bottom.

  Unlike those two, the grid here is GENERATED, not hand-typed. It
  can be, because the graph is tiny: at most 3 levels and 9 cards
  (Nosferatu), and 67 of 69 recipes are a plain two-ingredient
  bracket. A tree cannot cross itself, so there is no routing and
  no crossing-minimisation anywhere below.

  Styling lives in Template:BallTree/styles.css.
==============================================================]]
local graph = require('Module:BallGraph')

local ICON_SIZE = '48px'

--  The grid is measured in UNITS, all the same width, with a card
--  spanning CARD_SPAN of them and one unit left as a gutter between
--  siblings. Uniform columns are the whole point: when columns come
--  in two widths, the midpoint COLUMN between two cards is not the
--  midpoint in pixels, and the result card hangs off to one side —
--  and any card that lands in a narrow column gets squeezed into a
--  sliver. One width for everything makes both impossible.
local CARD_SPAN = 3
local p = {}

-- ---------------------------------------------------------------- cards

--- One card: a rounded box holding 1+ balls. Two or more means the
--  slot offers a choice, and they are stacked with an "or" divider
--  rather than drawn as separate branches — Radiation Beam is
--  (Laser H or Laser V) + (Poison or Cell), which as branches would
--  be four trees instead of one.
local function card(options, unlocks)
	local parts = {}
	for i, ball in ipairs(options) do
		if i > 1 then
			table.insert(parts, '<div class="bt-or"><span>or</span></div>')
		end
		local note = unlocks[ball]
		table.insert(parts, table.concat({
			'<div class="bt-ball">',
			'<span class="bt-icon">[[File:', ball, '.png|', ICON_SIZE,
			'|link=', ball, '|alt=]]</span>',
			'<span class="bt-name">[[', ball, ']]</span>',
			note and ('<span class="bt-note">' .. note .. '</span>') or '',
			'</div>',
		}))
	end
	return '<div class="bt-card">' .. table.concat(parts) .. '</div>'
end

-- ---------------------------------------------------------------- layout

--  A block is { rows, width, root }: `rows` is a list of rows of
--  cells, `width` how many columns it occupies, `root` the column
--  its own card sits in. Cells are { card = html } or
--  { edges = 'tlrb' }, the latter naming which borders to draw.

local function blankRow(width)
	local row = {}
	for i = 1, width do row[i] = { edges = '' } end
	return row
end

--- The classes for one connector cell, as two independent runs.
--
--  Lines radiate from the CENTRE of a cell, never from its edges: a
--  card is much wider than a connector, so an edge-drawn line
--  overshoots the card it is supposed to meet — which is what broke
--  the first version. The stylesheet draws the vertical run with
--  ::before and the horizontal run with ::after, each spanning half
--  the cell (up/down/left/right) or all of it (full), so segments in
--  neighbouring cells always meet at the shared boundary.
local function edges(up, left, right, down)
	local classes = {}
	if up and down    then table.insert(classes, 'bt-v-full')
	elseif up         then table.insert(classes, 'bt-v-up')
	elseif down       then table.insert(classes, 'bt-v-down') end
	if left and right then table.insert(classes, 'bt-h-full')
	elseif left       then table.insert(classes, 'bt-h-left')
	elseif right      then table.insert(classes, 'bt-h-right') end
	return table.concat(classes, ' ')
end

local function renderNode(node, unlocks)
	if node.options then
		local row = blankRow(CARD_SPAN)
		local centre = math.ceil(CARD_SPAN / 2)
		row[centre] = { card = card(node.options, unlocks) }
		return { rows = { row }, width = CARD_SPAN, root = centre }
	end

	-- Lay the children out left to right, one blank column between.
	--
	-- INVARIANT: every block is an ODD number of columns wide and its
	-- own card sits in the exact centre column. That is what makes
	-- the result land on the true midpoint of the cards feeding it:
	-- with blocks of unequal width the midpoint falls between two
	-- columns and the card hangs ~1.25em off to one side (Tumor,
	-- where a three-column subtree faces a one-column ball).
	--
	-- It is maintained by padding every child out to the widest one,
	-- equally on both sides. Two odd widths differ by an even number,
	-- so the padding always divides evenly and stays symmetric.
	local blocks, widest = {}, 0
	for i, child in ipairs(node.children) do
		blocks[i] = renderNode(child, unlocks)
		if blocks[i].width > widest then widest = blocks[i].width end
	end
	local width = 0
	for i, block in ipairs(blocks) do
		local pad = (widest - block.width) / 2
		if pad > 0 then
			for r, row in ipairs(block.rows) do
				local padded = blankRow(pad)
				for _, cell in ipairs(row) do table.insert(padded, cell) end
				for _ = 1, pad do table.insert(padded, { edges = '' }) end
				block.rows[r] = padded
			end
			block.root = block.root + pad
			block.width = widest
		end
		if i > 1 then width = width + 1 end
		block.offset = width
		width = width + block.width
	end


	-- Children are bottom-aligned: a deep subtree next to a shallow
	-- one must still meet the same connector row, so the shallow one
	-- is padded at the TOP.
	local height = 0
	for _, block in ipairs(blocks) do height = math.max(height, #block.rows) end
	local rows = {}
	for r = 1, height do rows[r] = blankRow(width) end
	for _, block in ipairs(blocks) do
		local pad = height - #block.rows
		for r, row in ipairs(block.rows) do
			for c, cell in ipairs(row) do
				rows[pad + r][block.offset + c] = cell
			end
		end
	end

	-- The connector row: a horizontal bar spanning the children, with
	-- a stub up into each of them and one down into the result.
	local cols, isChild = {}, {}
	for _, block in ipairs(blocks) do
		local col = block.offset + block.root
		table.insert(cols, col)
		isChild[col] = true
	end
	local first, last = cols[1], cols[#cols]
	local rootCol = math.floor((first + last) / 2)
	local connector = blankRow(width)
	for col = first, last do
		connector[col] = { edges = edges(isChild[col], col > first,
		                                 col < last, col == rootCol) }
	end
	table.insert(rows, connector)

	-- ...and the result itself, directly under that stub.
	local resultRow = blankRow(width)
	resultRow[rootCol] = { card = card({ node.ball }, unlocks) }
	table.insert(rows, resultRow)

	return { rows = rows, width = width, root = rootCol }
end

-- ---------------------------------------------------------------- output

local function toHtml(block)
	local out = { '<div class="bt-scroll"><table class="bt-grid">' }
	-- A zero-height first row of one cell per unit, which is what
	-- fixes the column widths.
	--
	-- NOT a <colgroup>: MediaWiki's sanitiser drops <colgroup> and
	-- <col> — they are not allowed tags in wikitext — so it came out
	-- as literal text on the page, and with no column widths to
	-- apply, table-layout:fixed fell back to sizing from the first
	-- row of colspanned cards. Every card then sat on a column of a
	-- different width and the joins missed their centres. Only
	-- <table>, <tr>, <td> and their attributes survive; build the
	-- grid out of those.
	table.insert(out, '<tr class="bt-ruler">')
	for _ = 1, block.width do table.insert(out, '<td class="bt-unit"></td>') end
	table.insert(out, '</tr>')
	for _, row in ipairs(block.rows) do
		table.insert(out, '<tr>')
		local skip = 0
		for col, cell in ipairs(row) do
			if skip > 0 then
				skip = skip - 1
			elseif cell.card then
				-- centred on its own unit, so it starts half a span back
				local start = col - math.floor(CARD_SPAN / 2)
				for _ = start, col - 1 do
					table.remove(out)   -- reclaim the blanks already emitted
				end
				table.insert(out, '<td class="bt-cell bt-node" colspan="'
				                  .. CARD_SPAN .. '">' .. cell.card .. '</td>')
				skip = CARD_SPAN - 1 - math.floor(CARD_SPAN / 2)
			else
				local class = 'bt-cell'
				if cell.edges ~= '' then class = class .. ' ' .. cell.edges end
				table.insert(out, '<td class="' .. class .. '"></td>')
			end
		end
		table.insert(out, '</tr>')
	end
	table.insert(out, '</table></div>')
	return table.concat(out)
end

--- tree: the {{BallCreationTable}} entry point. An optional first
--  argument overrides the page, so /doc can show a real example.
--  Renders nothing on a base or baby ball, so it is safe anywhere.
function p.tree(frame)
	local root = frame.args[1]
	if root == nil or root == '' then
		root = mw.title.getCurrentTitle().text
	end
	local recipes = graph.recipes()
	if not recipes[root] then return '' end
	return toHtml(renderNode(graph.ancestorTree(root, recipes), graph.unlocks()))
end

return p
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
