# 模板 · 主页（Main page）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Main_page) · [修订 554](https://ballxpit.wiki.gg/index.php?oldid=554) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Main_page_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Main_page/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Main_page/testcases)页面上进行实验。 |

![](../assets/previews/commons--Lua-48px-e7e95a21.png)

此模板使用了一个或多个用 Lua 编程语言编写的模块。

如需更多信息，请参阅 [Wikipedia:Lua](https://en.wikipedia.org/wiki/Wikipedia%3ALua) 或 [Mediawiki.org 上的 Lua 参考手册](https://mediawiki.org/wiki/Extension%3AScribunto/Lua_reference_manual)。使用的模块包括：**[主页面](../site/Module_Main_page.md)**。

此模板用于创建 IMP 主页。它使用 [Module:Main page](../site/Module_Main_page.md) 来排列一系列 [Template:Main page boxes](Main_page_box.md) 形成 [CSS grid](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout) 布局。

[ ]

## 目录（Contents）

* [1 简单解释](#%E7%AE%80%E5%8D%95%E8%A7%A3%E9%87%8A)
* [2 技术说明](#%E6%8A%80%E6%9C%AF%E8%AF%B4%E6%98%8E)
* [3 依赖项](#%E4%BE%9D%E8%B5%96%E9%A1%B9)
* [4 模板数据](#%E6%A8%A1%E6%9D%BF%E6%95%B0%E6%8D%AE)

## 简单解释

布局采用关键词以网格形式排列的方式构建。在桌面宽度屏幕上，该网格有3列；在平板电脑上有2列；在手机上则只有1列。每列可以包含任意多的行。每个关键词代表同一部分，并可以跨越多行和/或多列，但*必须*形成任意尺寸的连续矩形（1x1、1x2、2x2、2x3等）。

例如，以下桌面输入：

```
welcome welcome welcome
about links links
about contribute contribute
```

将生成如下的网格：

|  |  |  |
| --- | --- | --- |
| 欢迎 | 欢迎 | 欢迎 |
| 关于 | 链接 | 链接 |
| 关于 | 贡献 | 贡献 |

在哪里 `welcome` 是的内容 [欢迎来到百科](../articles/BALL_x_PIT_Wiki_welcome.md)、 `about` 是的内容 [游戏简介](../articles/BALL_x_PIT_Wiki_about.md)等等。请参见 [模板：主页面框](Main_page_box.md) 有关创建自己箱子的更多信息。

如果您输入的关键词尚未对应的框位，在保存或预览页面时，系统会提示您创建该框位。

如果您在某个布局中遗漏了某个关键词，它就不会在该布局中显示。如果这是意外，编辑预览界面的顶部会显示警告，但如果是有意遗漏的，则可以放心忽略。

如需更多提示和信息，请查看主页上的评论，或向 wiki.gg 的工作人员寻求帮助。

## 技术说明

对于熟悉CSS的人来说，本节将解释其底层工作原理。

桌面、平板电脑和手机的输入已创建 [CSS变量](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) 这些随后被用作数值。 [grid-template-areas](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas) 针对屏幕宽度大于等于1350px、大于等于990px且小于990px的情况，使用媒体查询。这些盒子会根据其子页面名称被分配一个ID，该ID会被模块用来查找模板，同时也会被盒子模板用来为其分配CSS ID。 `mp-box-<keyword>`由于这些关键词直接用于网格布局中，因此它们必须遵循规则。 [〈custom-ident〉](https://developer.mozilla.org/en-US/docs/Web/CSS/custom-ident) 命名。

## 依赖项

为了让此模板正常工作，您需要以下内容：

* [模块：主页](../site/Module_Main_page.md)
* 所有模板位于 [分类：主页面模板](../categories/Main_page_templates.md)。
* 位于 [MediaWiki:Common.css](../site/MediaWiki_Common.css.md) 中的“主页面布局”部分内的所有 CSS 样式。

`[mpEditLinks](../site/MediaWiki_Gadgets_mpEditLinks.md)` gadget也非常推荐。其代码可以在……找到。 [MediaWiki:Gadgets/mpEditLinks/main.css](../site/MediaWiki_Gadgets_mpEditLinks_main.css.md) 及 [MediaWiki:Gadgets/mpEditLinks/main.js](../site/MediaWiki_Gadgets_mpEditLinks_main.js.md).

## 模板数据

创建IMP主页。

模板参数 此模板更倾向于使用块格式来排列参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 桌面版 | `desktop` | 宽屏布局 | 字符串 | 必需 |
| 平板电脑 | `tablet` | 中宽屏幕的布局 | 字符串 | 必需 |
| 移动版 | `mobile` | 窄屏版布局 | 字符串 | 必需 |

**分类**　[分类 · 主页面模板](../categories/Main_page_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
