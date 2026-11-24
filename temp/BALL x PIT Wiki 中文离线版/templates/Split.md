# 模板 · 分割（Split）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Split) · [修订 577](https://ballxpit.wiki.gg/index.php?oldid=577) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

![](../assets/commons--Split.svg)

有人提议将此页面拆分为一个新页面，标题为 [示例](Ambox.md)。

![](../assets/commons--Split.svg)

建议将此页面拆分为新页面，标题分别为 [示例 1](Ambox.md)、[示例 2](Ambox.md) 和 [示例 3](Ambox.md)。

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Ambox_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Split/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Split/testcases)页面上进行实验。 |

此 **消息模板**是一个 [文章消息框](Ambox.md)，或 **ambox**。以下文档介绍了如何使用维基提供的每种 ambox。

[ ]

## 目录（Contents）

* [1 预组卡包](#%E9%A2%84%E7%BB%84%E5%8D%A1%E5%8C%85)
  + [1.1 问题通知弹窗](#%E9%97%AE%E9%A2%98%E9%80%9A%E7%9F%A5%E5%BC%B9%E7%AA%97)
  + [1.2 信息框](#%E4%BF%A1%E6%81%AF%E6%A1%86)
  + [1.3 可选参数](#%E5%8F%AF%E9%80%89%E5%8F%82%E6%95%B0)
* [2 创建自定义AMbox](#%E5%88%9B%E5%BB%BA%E8%87%AA%E5%AE%9A%E4%B9%89ambox)
* [3 依赖项](#%E4%BE%9D%E8%B5%96%E9%A1%B9)

## 预组卡包

### 问题通知弹窗

这些公告框是临时用来通知其他编辑和访客关于文章问题的工具。这些公告框支持以下参数：

* `|tiny=`: 如果设置为 `yes`此时，该图标会有较少的填充，且大小会比默认情况小得多。
* `|class=`: 需要添加到 ambox 容器元素中的任何额外的 CSS 类。
* `|date=`: 该ambox被添加到页面的日期。
* `|nocat=`: 如果设置为 `yes`，页面将不会添加任何分类。仅用于在创建文档时使用。

**注意：** 预组卡包需要基础材料 `{{[Ambox](Ambox.md)}}` 模板可以正常使用。

| 代码 | 结果 |
| --- | --- |
| {{[Cleanup](Cleanup.md)}} | ![](../assets/commons--Cleanup.svg) 此页面不符合 **BALL x PIT Wiki** 的页面质量标准。您可以 [编辑它](https://ballxpit.wiki.gg/wiki/Template:Split?action=edit)，帮助修复语法、格式或代码问题。 |
| {{[Delete](Delete.md)}} | 删除候选条目 此页面已被提名从维基中移除。在删除之前，请务必查看 [这里的链接](https://ballxpit.wiki.gg/wiki/Special:WhatLinksHere/Template:Split) 和 [页面历史记录](https://ballxpit.wiki.gg/wiki/Template:Split?action=history)。 |
| {{[Merge](Merge.md)\|Example}} | ![](../assets/commons--Merge.svg) 有人提议将此页面改为 [合并](https://support.wiki.gg/wiki/Merge) 与 [示例](Ambox.md). |
| {{[Move](Move.md)\|Example}} | ![](../assets/previews/commons--Move-48px-99a20bdf.png) 有人提议将此页面移动到 [示例](Ambox.md)。 |
| `{{Split\|Example}}` ／ `{{Split\|Example 1\|Example 2\|Example 3}}` | ![](../assets/commons--Split.svg) 有人提议将此页面拆分为一个新页面，标题为 [示例](Ambox.md)。 ![](../assets/commons--Split.svg) 建议将此页面拆分为新页面，标题分别为 [示例 1](Ambox.md)、[示例 2](Ambox.md) 和 [示例 3](Ambox.md)。 |
| {{[Stub](Stub.md)}} | 待完善 *此条目为 [待完善（stub）](../categories/Stubs.md). 你可以通过帮助 BALL x PIT 维基贡献一份力量。 [补充内容（expanding it）](https://ballxpit.wiki.gg/wiki/Template:Split?action=edit).* |

### 信息框

这些弹窗旨在作为页面的永久固定元素，用于向访客通报与页面相关的信息。除了已列出的参数外，这些弹窗还支持以下参数：

* `|tiny=`: 如果设置为 `yes`此时，该图标会有较少的填充，且大小会比默认情况小得多。
* `|class=`: 需要添加到 ambox 容器元素中的任何额外的 CSS 类。

| 代码 | 附加参数 | 结果 |
| --- | --- | --- |
| {{[Spoiler warning](Spoiler_warning.md)}} |  | ![](../assets/previews/commons--Warning-red-48px-69a5013e.png) 剧透警告 本页面包含 **剧透**。请自行决定是否查看。 |
| {{[No direct use](No_direct_use.md)}} |  | ![](../assets/previews/commons--Warning-red-48px-69a5013e.png) 不要直接从任何内容页面调用此模板！ 此模板适用于在其他模板中使用。然后，该模板可依次用于内容页面。 |
| {{[Uses Lua](Uses_Lua.md)}} | `\|1=`, 使用的模块列表，用逗号分隔 | ![](../assets/previews/commons--Lua-48px-e7e95a21.png) 此模板使用了一个或多个用 Lua 编程语言编写的模块。 更多信息，请参阅 [Wikipedia:Lua](https://en.wikipedia.org/wiki/Wikipedia:Lua) 或 [Mediawiki.org 上的 Lua 参考手册](https://mediawiki.org/wiki/Extension:Scribunto/Lua_reference_manual)。使用的模块包括：*无提供*。 |

### 可选参数

您可以使用可选参数来进一步自定义预置的 ambox。下面的示例就是使用了这些参数。 `tiny=yes` 及 `date=01/01/2021`.

![](../assets/previews/commons--Cleanup-20px-3f910d51.png)

此页面不符合要求。 **球比伦战记百科**的页面质量标准。你可以 [编辑它](https://ballxpit.wiki.gg/wiki/Template%3ASplit?action=edit) 用于帮助修正语法、格式或代码问题。（消息添加日期：2021年1月1日）

## 创建自定义AMbox

您可以根据需要使用以下参数创建额外的 ambox 模板：

```
{{Ambox
| color = The left border color.
| icon = The icon image to be displayed.
| title = The optional title.
| message = The explanation text displayed.
| tiny = If you want the tiny version of the ambox, fill the parameter with "yes".
| date = An optional date of creation for the message.
| class = An optional CSS class for the ambox.
}}
```

## 依赖项

为了让此模板正常工作，您需要以下内容：

* `.ambox` 以及任何相关的职业，位于 [MediaWiki:Common.css](../site/MediaWiki_Common.css.md).

**分类**　[分类 · 删除候选条目](../categories/Candidates_for_deletion.md) · [分类 · 待完善](../categories/Stubs.md) · [分类 · 注意模板](../categories/Notice_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
