# 模板 · BallTree/styles.css

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallTree%2Fstyles.css) · [修订 4319](https://ballxpit.wiki.gg/index.php?oldid=4319) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

```
<a id="p-2056-4cfbc7b051a8" name="p-2056-4cfbc7b051a8"></a>/* Template:BallTree/styles.css — the evolution recipe diagram.
<a id="p-2056-396d298ace45" name="p-2056-396d298ace45"></a>   Rendered by Module:BallTree. Requires TemplateStylesExtender for var().
<a id="p-2056-70b7535e9c27" name="p-2056-70b7535e9c27"></a>
<a id="p-2056-c4370901ef8d" name="p-2056-c4370901ef8d"></a>   Line art: the module tags each connector cell with at most one
<a id="p-2056-17f1db714097" name="p-2056-17f1db714097"></a>   vertical run (bt-v-up / -down / -full) and one horizontal run
<a id="p-2056-42b86d896d1d" name="p-2056-42b86d896d1d"></a>   (bt-h-left / -right / -full). Each run is drawn from the CELL
<a id="p-2056-03cd228dff7a" name="p-2056-03cd228dff7a"></a>   CENTRE outwards by a pseudo-element, never as a border on the
<a id="p-2056-90bf3de33aec" name="p-2056-90bf3de33aec"></a>   cell's edge — a card is far wider than a connector, so an
<a id="p-2056-cf42a3517a10" name="p-2056-cf42a3517a10"></a>   edge-drawn line misses the card's centre and the elbows stagger. */
<a id="p-2056-f248212e73b7" name="p-2056-f248212e73b7"></a>
<a id="p-2056-ef49a6733c1a" name="p-2056-ef49a6733c1a"></a>.bt-scroll {
<a id="p-2056-e2a47e773bfa" name="p-2056-e2a47e773bfa"></a>	overflow-x: auto;     /* Nosferatu is 11 columns; phones are not */
<a id="p-2056-cd189718ed03" name="p-2056-cd189718ed03"></a>	max-width: 100%;
<a id="p-2056-5dd254528f43" name="p-2056-5dd254528f43"></a>}
<a id="p-2056-25498efab7d3" name="p-2056-25498efab7d3"></a>
<a id="p-2056-affae50f0064" name="p-2056-affae50f0064"></a>.bt-grid {
<a id="p-2056-1fcb4d0b29b8" name="p-2056-1fcb4d0b29b8"></a>	--bt-line: #816750;
<a id="p-2056-93ca9add08ec" name="p-2056-93ca9add08ec"></a>	--bt-line-width: 2px;       /* the card outline */
<a id="p-2056-84c532163a5a" name="p-2056-84c532163a5a"></a>	--bt-join-width: 1px;       /* the joins between cards, a touch finer */
<a id="p-2056-f184206caf89" name="p-2056-f184206caf89"></a>	--bt-card-bg: rgba(255, 255, 255, 0.03);
<a id="p-2056-b344bc965dce" name="p-2056-b344bc965dce"></a>	--bt-unit: 4em;             /* ONE width for every column: a card
<a id="p-2056-dfddfa11a942" name="p-2056-dfddfa11a942"></a>	                               spans three of them, a gutter is
<a id="p-2056-a95da0afd675" name="p-2056-a95da0afd675"></a>	                               one. Two widths and the midpoint
<a id="p-2056-0b5a6cc62e3b" name="p-2056-0b5a6cc62e3b"></a>	                               column stops being the midpoint.
<a id="p-2056-896716b7162d" name="p-2056-896716b7162d"></a>	                               4em: a card is three units wide and
<a id="p-2056-285d84a3c772" name="p-2056-285d84a3c772"></a>	                               no wider, so this fits the longest
<a id="p-2056-a0fea3dec303" name="p-2056-a0fea3dec303"></a>	                               name (Voluptuous Egg Sac) unwrapped. */
<a id="p-2056-35fc11f2baac" name="p-2056-35fc11f2baac"></a>	table-layout: fixed;
<a id="p-2056-494707584e4c" name="p-2056-494707584e4c"></a>	/* separate, not collapse: a collapsed cell cannot take a
<a id="p-2056-38ff5456bb2e" name="p-2056-38ff5456bb2e"></a>	   border-radius, and the card outline is drawn on the cell. */
<a id="p-2056-707355623d53" name="p-2056-707355623d53"></a>	border-collapse: separate;
<a id="p-2056-f4296db22efa" name="p-2056-f4296db22efa"></a>	border-spacing: 0;
<a id="p-2056-02f2ca3f15a7" name="p-2056-02f2ca3f15a7"></a>	margin: 0 auto;
<a id="p-2056-276085980459" name="p-2056-276085980459"></a>}
<a id="p-2056-fb6ee5e330f9" name="p-2056-fb6ee5e330f9"></a>/* The ruler row: invisible, one cell per unit, and the thing that
<a id="p-2056-5f3f28232526" name="p-2056-5f3f28232526"></a>   actually sets the column widths. See Module:BallTree — a colgroup
<a id="p-2056-ce925a11afbe" name="p-2056-ce925a11afbe"></a>   would be stripped by MediaWiki before it ever reached the page. */
<a id="p-2056-5a03a315e031" name="p-2056-5a03a315e031"></a>.bt-grid .bt-ruler { height: 0; }
<a id="p-2056-ee83d4eaf46d" name="p-2056-ee83d4eaf46d"></a>.bt-grid .bt-unit { width: var(--bt-unit); height: 0; padding: 0; border: 0; }
<a id="p-2056-69a32cedacd2" name="p-2056-69a32cedacd2"></a>.bt-grid .bt-ruler .bt-unit::before,
<a id="p-2056-dfd47b38533a" name="p-2056-dfd47b38533a"></a>.bt-grid .bt-ruler .bt-unit::after { content: none; }
<a id="p-2056-e2f62828e327" name="p-2056-e2f62828e327"></a>
<a id="p-2056-1f4a632acf3a" name="p-2056-1f4a632acf3a"></a>.bt-grid .bt-cell {
<a id="p-2056-a25da0821ff1" name="p-2056-a25da0821ff1"></a>	position: relative;
<a id="p-2056-0ddf0f274c77" name="p-2056-0ddf0f274c77"></a>	height: 1.75em;
<a id="p-2056-1f1b37e0c739" name="p-2056-1f1b37e0c739"></a>	min-width: 1.5em;
<a id="p-2056-5ccf9ab24b41" name="p-2056-5ccf9ab24b41"></a>	padding: 0;
<a id="p-2056-113152312c93" name="p-2056-113152312c93"></a>}
<a id="p-2056-a4ebedce08a5" name="p-2056-a4ebedce08a5"></a>
<a id="p-2056-80c78e4ad16b" name="p-2056-80c78e4ad16b"></a>/* The card IS the cell. Every cell in a table row is as tall as the
<a id="p-2056-6846dfa06360" name="p-2056-6846dfa06360"></a>   tallest one in every browser, so drawing the outline on the <td>
<a id="p-2056-b62e392a1fd5" name="p-2056-b62e392a1fd5"></a>   gives equal-height siblings for free, and the outline's edges sit
<a id="p-2056-11274d56135e" name="p-2056-11274d56135e"></a>   exactly on the row boundary where the connector stubs start.
<a id="p-2056-58632641b02f" name="p-2056-58632641b02f"></a>
<a id="p-2056-b728c25078e5" name="p-2056-b728c25078e5"></a>   An earlier version drew the outline on a <div> inside the cell and
<a id="p-2056-80d026bc1e64" name="p-2056-80d026bc1e64"></a>   stretched it with height:100%. That percentage resolves differently
<a id="p-2056-5f573a43ab8b" name="p-2056-5f573a43ab8b"></a>   per engine: Chrome needs a fixed height on the cell to honour it,
<a id="p-2056-e1c57a18023e" name="p-2056-e1c57a18023e"></a>   and Firefox then takes that fixed height literally, so the card
<a id="p-2056-472cd154cdc3" name="p-2056-472cd154cdc3"></a>   collapsed to 1.75em with its contents spilling out. Nothing here
<a id="p-2056-da0cb5b85534" name="p-2056-da0cb5b85534"></a>   depends on a percentage height. */
<a id="p-2056-d8279cca473d" name="p-2056-d8279cca473d"></a>.bt-grid .bt-node {
<a id="p-2056-1521f0720deb" name="p-2056-1521f0720deb"></a>	height: auto;
<a id="p-2056-d3403e576ca8" name="p-2056-d3403e576ca8"></a>	padding: 0.45em 0.6em;
<a id="p-2056-7fbbe8351a03" name="p-2056-7fbbe8351a03"></a>	vertical-align: middle;
<a id="p-2056-165460b4458e" name="p-2056-165460b4458e"></a>	text-align: center;
<a id="p-2056-a2e4543c5d46" name="p-2056-a2e4543c5d46"></a>	border: var(--bt-line-width) solid var(--bt-line);
<a id="p-2056-b84b811fc516" name="p-2056-b84b811fc516"></a>	border-radius: 8px;
<a id="p-2056-38dcbac22ab3" name="p-2056-38dcbac22ab3"></a>	background: var(--bt-card-bg);
<a id="p-2056-6595098da51e" name="p-2056-6595098da51e"></a>}
<a id="p-2056-80f8e8f57fb2" name="p-2056-80f8e8f57fb2"></a>
<a id="p-2056-7cf48ad230bc" name="p-2056-7cf48ad230bc"></a>/* The two runs. ::before is vertical, ::after is horizontal; both sit
<a id="p-2056-a3a3ff72ede2" name="p-2056-a3a3ff72ede2"></a>   on the centre line of the cell, so neighbours meet exactly. */
<a id="p-2056-469a94fbffa7" name="p-2056-469a94fbffa7"></a>.bt-grid .bt-cell::before,
<a id="p-2056-83a396056457" name="p-2056-83a396056457"></a>.bt-grid .bt-cell::after { content: ""; position: absolute; }
<a id="p-2056-b36f7a2907c8" name="p-2056-b36f7a2907c8"></a>
<a id="p-2056-68506e7d28e0" name="p-2056-68506e7d28e0"></a>.bt-grid [class*="bt-v-"]::before {
<a id="p-2056-f4e7adffd847" name="p-2056-f4e7adffd847"></a>	left: 50%;
<a id="p-2056-052b7891063b" name="p-2056-052b7891063b"></a>	border-left: var(--bt-join-width) solid var(--bt-line);
<a id="p-2056-9f3961dd63c5" name="p-2056-9f3961dd63c5"></a>}
<a id="p-2056-97e5e110fb38" name="p-2056-97e5e110fb38"></a>.bt-grid .bt-v-up::before   { top: 0;   height: 50%; }
<a id="p-2056-fd8758442287" name="p-2056-fd8758442287"></a>.bt-grid .bt-v-down::before { top: 50%; height: 50%; }
<a id="p-2056-e952d0e64a98" name="p-2056-e952d0e64a98"></a>.bt-grid .bt-v-full::before { top: 0;   height: 100%; }
<a id="p-2056-db7fa345cf46" name="p-2056-db7fa345cf46"></a>
<a id="p-2056-ff862468c223" name="p-2056-ff862468c223"></a>.bt-grid [class*="bt-h-"]::after {
<a id="p-2056-d58f64e2e90b" name="p-2056-d58f64e2e90b"></a>	top: 50%;
<a id="p-2056-0bd4b6ef0b0e" name="p-2056-0bd4b6ef0b0e"></a>	border-top: var(--bt-join-width) solid var(--bt-line);
<a id="p-2056-0a4c8569651b" name="p-2056-0a4c8569651b"></a>}
<a id="p-2056-0b1186e9a97e" name="p-2056-0b1186e9a97e"></a>.bt-grid .bt-h-left::after  { left: 0;   width: 50%; }
<a id="p-2056-d43c9b343ed4" name="p-2056-d43c9b343ed4"></a>.bt-grid .bt-h-right::after { left: 50%; width: 50%; }
<a id="p-2056-ce98983eac69" name="p-2056-ce98983eac69"></a>.bt-grid .bt-h-full::after  { left: 0;   width: 100%; }
<a id="p-2056-4cb06ab10141" name="p-2056-4cb06ab10141"></a>
<a id="p-2056-98bf02fd87fe" name="p-2056-98bf02fd87fe"></a>/* A card's contents: image on top, linked name under it, condition
<a id="p-2056-5006145043aa" name="p-2056-5006145043aa"></a>   under that. The box itself is the cell (.bt-node, above). */
<a id="p-2056-b15b11019c4b" name="p-2056-b15b11019c4b"></a>.bt-card {
<a id="p-2056-5c1072754e02" name="p-2056-5c1072754e02"></a>	display: flex;
<a id="p-2056-691b8c0f0361" name="p-2056-691b8c0f0361"></a>	flex-direction: column;
<a id="p-2056-dda2b18ce118" name="p-2056-dda2b18ce118"></a>	align-items: center;
<a id="p-2056-f7b7c0e4d71e" name="p-2056-f7b7c0e4d71e"></a>	gap: 0.15em;
<a id="p-2056-826019672266" name="p-2056-826019672266"></a>}
<a id="p-2056-58bbf333e4d7" name="p-2056-58bbf333e4d7"></a>.bt-ball { display: flex; flex-direction: column; align-items: center; gap: 0.1em; }
<a id="p-2056-fc0ba72b461e" name="p-2056-fc0ba72b461e"></a>.bt-icon { line-height: 1; }
<a id="p-2056-b7d8eb9253f3" name="p-2056-b7d8eb9253f3"></a>.bt-name { font-weight: bold; }
<a id="p-2056-4d8f3b235c07" name="p-2056-4d8f3b235c07"></a>
<a id="p-2056-68a70f6ee831" name="p-2056-68a70f6ee831"></a>/* The unlock condition. Deliberately quiet: a footnote on a node,
<a id="p-2056-88e323e098cf" name="p-2056-88e323e098cf"></a>   not a second title. */
<a id="p-2056-8aed7eda7135" name="p-2056-8aed7eda7135"></a>.bt-note {
<a id="p-2056-582204a87f9f" name="p-2056-582204a87f9f"></a>	font-size: 0.75em;
<a id="p-2056-3bed7872f313" name="p-2056-3bed7872f313"></a>	font-weight: normal;
<a id="p-2056-5525cbcae4f0" name="p-2056-5525cbcae4f0"></a>	opacity: 0.7;
<a id="p-2056-4e64fa192385" name="p-2056-4e64fa192385"></a>	max-width: 11em;
<a id="p-2056-a99f6c51e846" name="p-2056-a99f6c51e846"></a>	white-space: normal;
<a id="p-2056-91b5195c9d71" name="p-2056-91b5195c9d71"></a>	text-align: center;
<a id="p-2056-c5524cc66e81" name="p-2056-c5524cc66e81"></a>}
<a id="p-2056-0ebf76aeaa0f" name="p-2056-0ebf76aeaa0f"></a>
<a id="p-2056-6e28d915bdd2" name="p-2056-6e28d915bdd2"></a>/* "A or B" inside one card: a rule across the box with the word set
<a id="p-2056-b524191512af" name="p-2056-b524191512af"></a>   into the middle of it. */
<a id="p-2056-0ef986f0af7d" name="p-2056-0ef986f0af7d"></a>.bt-or {
<a id="p-2056-0eed987f8e2f" name="p-2056-0eed987f8e2f"></a>	display: flex;
<a id="p-2056-1821069749c6" name="p-2056-1821069749c6"></a>	align-items: center;
<a id="p-2056-1b134240e11a" name="p-2056-1b134240e11a"></a>	gap: 0.4em;
<a id="p-2056-24887c88dcee" name="p-2056-24887c88dcee"></a>	width: 100%;
<a id="p-2056-bda2770064e5" name="p-2056-bda2770064e5"></a>	margin: 0.15em 0;
<a id="p-2056-091f84652966" name="p-2056-091f84652966"></a>	font-size: 0.7em;
<a id="p-2056-ef492a8b071b" name="p-2056-ef492a8b071b"></a>	text-transform: uppercase;
<a id="p-2056-e3998c482a73" name="p-2056-e3998c482a73"></a>	letter-spacing: 0.08em;
<a id="p-2056-8b192b7751de" name="p-2056-8b192b7751de"></a>	opacity: 0.6;
<a id="p-2056-8aec49e27508" name="p-2056-8aec49e27508"></a>}
<a id="p-2056-96d5359fd0eb" name="p-2056-96d5359fd0eb"></a>.bt-or::before,
<a id="p-2056-2fa94f572721" name="p-2056-2fa94f572721"></a>.bt-or::after {
<a id="p-2056-e6a7bfd3acd9" name="p-2056-e6a7bfd3acd9"></a>	content: "";
<a id="p-2056-d643e7a3df2a" name="p-2056-d643e7a3df2a"></a>	flex: 1;
<a id="p-2056-e5b96339b76c" name="p-2056-e5b96339b76c"></a>	border-top: var(--bt-join-width) solid var(--bt-line);
<a id="p-2056-2128eb4cb88d" name="p-2056-2128eb4cb88d"></a>}
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
