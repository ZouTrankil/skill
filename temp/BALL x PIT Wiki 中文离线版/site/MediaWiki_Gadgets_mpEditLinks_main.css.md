# 站点代码 · Gadgets/mpEditLinks/main.css

[原文](https://ballxpit.wiki.gg/wiki/MediaWiki:Gadgets/mpEditLinks/main.css) · [修订 423](https://ballxpit.wiki.gg/index.php?oldid=423)

```css
.mp-edit-link {
	display:block;
	position:absolute;
	z-index:99;
	right:0.5em;
	top:0.5em;
	background:var(--wiki-content-background-color);
}

.mp-edit-link a {
	display:block;
	padding:0.1em;
	border:1px solid var(--wiki-content-link-color);
}

.mp-edit-link a::before {
	display:inline-block;
	content:'';
	background-image:url("data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%2220%22 height=%2220%22 viewBox=%220 0 20 20%22%3E%3Ctitle%3E edit %3C/title%3E%3Cpath d=%22m16.77 8 1.94-2a1 1 0 0 0 0-1.41l-3.34-3.3a1 1 0 0 0-1.41 0L12 3.23zM1 14.25V19h4.75l9.96-9.96-4.75-4.75z%22/%3E%3C/svg%3E");
	background-size:contain;
	width:1em;
	height:1em;
	filter:var(--wiki-icon-to-link-filter);
	vertical-align:text-top;
	margin-right:0.2em;
}
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
