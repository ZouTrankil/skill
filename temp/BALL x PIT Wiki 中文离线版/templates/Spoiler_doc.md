# 模板 · 剧透/文档（Spoiler/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Spoiler%2Fdoc) · [修订 580](https://ballxpit.wiki.gg/index.php?oldid=580) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此模板用于标记文本和其他元素为剧透内容。用户可以点击或选择悬停以显示其内容。

## hoverShowSpoilers小工具

用户可以启用 `[hoverShowSpoilers](../site/MediaWiki_Gadgets_hoverShowSpoilers.md)` 一种可以在悬浮时显示剧透的道具，而不仅仅是在点击时显示。该道具的代码可以在……找到。 [MediaWiki:Gadgets/hoverShowSpoilers/main.css](../site/MediaWiki_Gadgets_hoverShowSpoilers_main.css.md).

## 示例

| 代码 | 结果 |
| --- | --- |
| `{{spoiler\|spoiler text}}` （点击切换 / Click to toggle） | 剧透文本 |
| `{{spoiler\|spoiler text with a [[Template:Navbox\|link]]}}` （点击切换 / Click to toggle） | 剧透文字，带有 [链接](Navbox.md) |
| `{{spoiler\|block=y\|Really long spoiler that spans multiple lines It even has a bulleted list inside it: * Item a * Item b * [[Special:Random\|Item c]] }}` | 真是很长的剧透，横跨了好几行。 里面甚至还有一个项目列表： 物品a；物品b；[物品c](https://ballxpit.wiki.gg/wiki/Special:Random) |

## 依赖项

为了让此模板正常工作，您需要以下内容：

* `spoilers` 带有 JavaScript 代码的设备，用于切换功能 `.spoiler` 点击即开启/关闭类别：
  + [MediaWiki:Gadgets/spoilers](../site/MediaWiki_Gadgets_spoilers.md)
  + [MediaWiki:Gadgets/spoilers/main.js](../site/MediaWiki_Gadgets_spoilers_main.js.md)
* `.spoiler-content` 以及任何相关的职业，位于 [MediaWiki:Common.css](../site/MediaWiki_Common.css.md).

## 来源

基础代码改编自 [Template:Spoiler on Terraria Wiki](https://terraria.wiki.gg/wiki/Template%3ASpoiler)。

## 模板数据

此模板可用于将文本标记为剧透。

模板参数 此模板更倾向于使用内联格式设置参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 文本 | `1` `text` | 要显示的文本。 示例角色A在战斗中死亡。 | 内容 | 必需 |
| 悬浮显示？ | `hover` | 鼠标悬停时显示剧透文本。 默认hover=no示例hover=yes | 布尔逻辑 | 可选 |
| 以块形显示？ | `block` | 如果提供，将剧透以块级形式显示，而非内联。适用于跨多行或包含列表等块级元素的长剧透。 示例y | 布尔逻辑 | 建议 |
| 职业 | `class` | 要应用于剧透的班级或多个班级 | 字符串 | 可选 |
| ID | `id` | 用于应用剧透的 CSS ID。 | 字符串 | 可选 |
| 风格 | `style` `css` | 需传入的Inline CSS样式。 | 字符串 | 可选 |

**分类**　[分类 · 包含剧透的页面](../categories/Pages_with_spoilers.md) · [分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
