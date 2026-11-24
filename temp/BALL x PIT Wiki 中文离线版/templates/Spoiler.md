# 模板 · 剧透（Spoiler）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Spoiler) · [修订 579](https://ballxpit.wiki.gg/index.php?oldid=579) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Spoiler_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Spoiler/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Spoiler/testcases)页面上进行实验。 |

此模板用于标记文本和其他元素为剧透内容。用户可以点击或选择悬停以显示其内容。

[ ]

## 目录（Contents）

* [1 hoverShowSpoilers小工具](#hovershowspoilers%E5%B0%8F%E5%B7%A5%E5%85%B7)
* [2 示例](#%E7%A4%BA%E4%BE%8B)
* [3 依赖项](#%E4%BE%9D%E8%B5%96%E9%A1%B9)
* [4 来源](#%E6%9D%A5%E6%BA%90)
* [5 模板数据](#%E6%A8%A1%E6%9D%BF%E6%95%B0%E6%8D%AE)

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

**分类**　[分类 · 包含剧透的页面](../categories/Pages_with_spoilers.md) · [分类 · 模板格式化](../categories/Formatting_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
