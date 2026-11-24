# 模板 · TOC限制（TOC limit）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:TOC_limit) · [修订 583](https://ballxpit.wiki.gg/index.php?oldid=583) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](TOC_limit_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:TOC_limit/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:TOC_limit/testcases)页面上进行实验。 |

此模板会插入一个目录，但会省略超过一定深度的子标题。该目录遵循与 \_\_TOC\_\_ [魔法词](https://mediawiki.org/wiki/Help%3AMagic_words) 相同的布局规则。被省略的章节在文章正文中仍具有章节编辑链接。此模板的主要用途是当需要章节编辑链接以便于编辑，但不希望显示完整的目录时。**在使用此模板之前，请考虑它是否以及为何对读者和其他编辑有帮助。**

[ ]

## 目录（Contents）

* [1 使用](#%E4%BD%BF%E7%94%A8)
* [2 TOC关卡与Wiki文本标题关卡对比](#toc%E5%85%B3%E5%8D%A1%E4%B8%8Ewiki%E6%96%87%E6%9C%AC%E6%A0%87%E9%A2%98%E5%85%B3%E5%8D%A1%E5%AF%B9%E6%AF%94)
* [3 冲突](#%E5%86%B2%E7%AA%81)
* [4 模板数据](#%E6%A8%A1%E6%9D%BF%E6%95%B0%E6%8D%AE)

## 使用

`{{TOC limit}}` 或 `{{TOC limit|3}}`

模板默认包含第二级和第三级的标题，例如目录中编号为“1”和“1.1”的那些。（注意：） `{{TOC limit|1}}` 无操作：页面上的一级标题默认即为页面标题。）

您可以通过添加标题等级来指定不同的限制。

`{{TOC limit|4}}`

4允许使用第四级标题，例如“1.1.1”，但会省略TOC中低于该级别的任何子标题。

该模板通过 CSS 隐藏较低关卡的显示。请参阅 [Mediawiki:Common.css](../site/MediaWiki_Common.css.md)。

## TOC关卡与Wiki文本标题关卡对比

TOC中的标题关卡通常对应wiki文本中的标题关卡，因此 `== Level-2 header ==` 通常会生成一级（“1”）的TOC标题，一个 `=== Level-3 header ===` 通常会生成二级（“1.1”）的TOC标题，依此类推。这种对应关系是这样的。 *不* 如果页面包含相关内容，则保持停留。 `= Level-1 headers =` 或者跳过标题关卡。例如这样的维基文本：

```
== Level-2 heading (A) ==
=== Level-3 heading (B) ===
== Level-2 heading (C) ==
====== Level-6 heading (D) ======
= Level-1 heading (E) =
== Level-2 heading (F) ==
=== Level-3 heading (G) ===
```

将生成如下的TOC：

|  |
| --- |
| **目录** 1 等级-2标题 (A)1.1 等级-3标题（B）；2 等级-2章节 (C)2.1 等级-6 标题 (D)；3 等级-1标题（E）3.1 等级-2标题（F）3.1.1 等级-3标题（G） |

使用 `{{TOC limit}}` 在此页面上 *不会* 隐藏标题D，因为尽管它是6级标题，但在目录中却位于第二级。而且它 *会* 隐藏标题G，尽管它和标题B一样都是3级标题，因为标题G显示在目录的第三级，而标题B则显示在第二级。

## 冲突

此模板与以下内容交互不佳。 `{{[TOC right](TOC_right.md)}}` 模板。要实现正确的效果，请使用带有限制参数的模板。例如： `{{[TOC right](TOC_right.md)|limit=2}}` 具有该效果 `{{[TOC right](TOC_right.md)}}` 及 `{{TOC limit|2}}` 如果它们协同工作的话，就会……

## 模板数据

插入一个目录，省略超过一定深度的子标题。

模板参数

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 限制 | `1` `limit` | 目录中需包含上限值的标题深度 默认3 | 数字 | 建议 |

**分类**　[分类 · 目录模板](../categories/Table_of_contents_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
