# 站点代码 · Gadgets/mpEditLinks/main.js

[原文](https://ballxpit.wiki.gg/wiki/MediaWiki:Gadgets/mpEditLinks/main.js) · [修订 424](https://ballxpit.wiki.gg/index.php?oldid=424)

```js
$.when( $.ready )
.then(function(){

	if(!document.getElementById('mp-container')) return; /* page is not using IMP */
	if(!mw.config.get('wgIsProbablyEditable')) return; /* user does not have permission to edit the page */
	
	var rootpage = document.getElementById('mp-container').dataset['rootpage']; // Get the rootpage passed from the main page module, so we don't need to make an API call

	/* generate the links here instead of in the wikitext, so that users who can't see them don't have them
	* in the DOM at all, and screenreaders and search engines don't get confused */
	function createLinks(){
		$('.mp-box').each(function(_, el){
			var params = '?action=edit';
			
			// only add the long preload stuff if the box doesn't exist, for prettier urls
			if ( $(el).hasClass('missing') ){

				params += '&preload=Template:Main page box/preload&preloadparams[0]=' + el.dataset['boxId'].charAt(0).toUpperCase() + el.dataset['boxId'].slice(1); /* preloadparam is box id with first letter capitalized */
			}
			
			$('<a></a>', {href: mw.util.getUrl(rootpage + '/' + el.dataset['boxId']) + params})
			.msg('gadget-mpEditLinks-edit-link-text', rootpage + '/' + el.dataset['boxId'])
			.appendTo(
				$('<div></div>', {
					class: 'mp-edit-link'
				}).prependTo(el)
			);
		});
	}

	function toggleLinks(){
		$('.mp-edit-link').each(function(_, el){
			$(el).toggle().css('display none;');
		});
	}

	$('<span></span>', {
		text: mw.msg('gadget-mpEditLinks-toggle-link-text'),
		class: 'mp-edit-toggle',
		on: {click: toggleLinks},
	}).appendTo($('#top'));

	createLinks();

});
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
