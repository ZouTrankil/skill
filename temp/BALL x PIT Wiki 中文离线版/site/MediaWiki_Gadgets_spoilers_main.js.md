# 站点代码 · Gadgets/spoilers/main.js

[原文](https://ballxpit.wiki.gg/wiki/MediaWiki:Gadgets/spoilers/main.js) · [修订 432](https://ballxpit.wiki.gg/index.php?oldid=432)

```js
/* [[Template:Spoiler]] */
mw.hook('wikipage.content').add(function() {
	$('.spoiler-content')
	.off('click') // in case this code is loaded twice
	.on('click', function(e){
		$(this).toggleClass('show');
	}).find('a').on('click', function(e){
		e.stopPropagation();
	});

});
/* End Template:Spoiler */
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
