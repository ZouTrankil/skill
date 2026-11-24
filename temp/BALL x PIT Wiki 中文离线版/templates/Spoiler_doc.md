# 模板 · 恶作剧/doc（Spoiler/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Spoiler%2Fdoc) · [修订 580](https://ballxpit.wiki.gg/index.php?oldid=580) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此模板用于标记文本和其他元素作为播放器。 用户可以单击或随意悬浮以显示其内容。

#### 悬浮在沙丘上喷水器的装置

用户可以启用 `[hoverShowSpoilers](../site/MediaWiki_Gadgets_hoverShowSpoilers.md)` 让破坏者在悬盘上表演， 而不仅仅是点击。 此工具的代码可以在 [MediaWiki:Gadgets/hoverShowSpoilers/main.css](../site/MediaWiki_Gadgets_hoverShowSpoilers_main.css.md).

#### 实例实例实例

| 《法典法典法典》 | 结果 |
| --- | --- |
| `{{spoiler\|spoiler text}}` （点击切换 / Click to toggle） | 破坏器文本文本 |
| `{{spoiler\|spoiler text with a [[Template:Navbox\|link]]}}` （点击切换 / Click to toggle） | 含有 [链接链接](Navbox.md) |
| `{{spoiler\|block=y\|Really long spoiler that spans multiple lines It even has a bulleted list inside it: * Item a * Item b * [[Special:Random\|Item c]] }}` | 跨越多个线条的真正的长长的搅拌器 里面甚至还有一张子弹清单 项目a 项目a；项目b；[项目c](https://ballxpit.wiki.gg/wiki/Special:Random) |

#### 依赖性

此模板要正常工作， 您需要以下信息:

* 其他 `spoilers` 使用 JavaScript 代码来切换 `.spoiler` 点击打开/关闭类 :
  + [MediaWiki: 谷地/锅炉](../site/MediaWiki_Gadgets_spoilers.md)
  + [MediaWiki:Gadgets/spoilers/main.js](../site/MediaWiki_Gadgets_spoilers_main.js.md)
* 其他 `.spoiler-content` 和任何相关类别, [MediaWiki:Common.css](../site/MediaWiki_Common.css.md).

#### 来源来源

从 [Template:Terraria Wiki](https://terraria.wiki.gg/wiki/Template%3ASpoiler)上改编的基码。

#### 模板数据

此模板可用于将文本标记为破坏器。

模板参数 此模板更倾向于参数的内嵌格式化。

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 文本 | `1` `text` | 要显示的文本。 示例A在战斗中死亡 | 内容 | 需要 |
| 炫耀在Hover? | `hover` | 鼠标悬浮时显示破坏器文本。 默认默认悬盘=无示例悬盘=是 | 布尔 | 可选 |
| 显示为块吗 ? | `block` | 如果给定了， 则将搅拌器显示为一个块而不是内嵌。 对于横跨多行或使用块级元素如列表的长期搅拌器有用。 示例y 语句 | 布尔 | 建议 |
| 班级 | `class` | 适用于破坏者的一个或数个类别 | 字符串字符串 | 可选 |
| ID | `id` | A CSS CSS ID ID 申请申请到 | 字符串字符串 | 可选 |
| 样式 | `style` `css` | 内嵌的 CSS 样式要通过。 | 字符串字符串 | 可选 |

**分类**　[分类 · 页面有散播符](../categories/Pages_with_spoilers.md) · [分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
