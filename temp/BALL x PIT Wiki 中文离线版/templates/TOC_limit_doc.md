# 模板 · 工作时间限制/doc（TOC limit/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:TOC_limit%2Fdoc) · [修订 584](https://ballxpit.wiki.gg/index.php?oldid=584) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

本模板插入一个目录，其中略去超出一定深度的子标题。该表格遵循与 TOC 相同的布局规则。 [魔法单词](https://mediawiki.org/wiki/Help%3AMagic_words)。在文章正文中， 寄出部分仍然有部分编辑链接。本模板的主要用途是您想要部分编辑链接以方便编辑，但不希望有完整的目录。 **在使用这个模板之前，考虑是否和为什么它对读者和其他编辑有帮助。**

#### 使用率

`{{[TOC limit](TOC_limit.md)}}` 或是 `{{[TOC limit](TOC_limit.md)|3}}`

模板默认包含第二和第三级标题，如在技术选择委员会中编号为“1”和“1.1”的标题(注: `{{[TOC limit](TOC_limit.md)|1}}` 什么都没有:页面的第一个级别标题默认是页标题。 )

您可以通过添加信头级别指定不同的限制 :

`{{[TOC limit](TOC_limit.md)|4}}`

4允许四级标题，例如“1.1.1”,但略去技选委员会下的任何小标题。

该模板以 CSS 隐藏下层。 见 [Mediawiki:Common.cs](../site/MediaWiki_Common.css.md) 。

#### TOC 级别与维基文本标题级别

技术选择委员会中的标题水平通常与wikitext 中的标题水平相对应，因此a `== Level-2 header ==` 通常生成第一级 (“ 1”) TOC 标题, a `=== Level-3 header ===` 通常将生成二级 (“1.1”) TOC 标题等。 *没有* 如果页面包含 `= Level-1 headers =` 或跳过页眉级别。 例如, wikitext 像这样 :

```
== Level-2 heading (A) ==
=== Level-3 heading (B) ===
== Level-2 heading (C) ==
====== Level-6 heading (D) ======
= Level-1 heading (E) =
== Level-2 heading (F) ==
=== Level-3 heading (G) ===
```

将产生像这样的技选委员会:

使用 `{{TOC limit}}` 此页面上的 *不会* 隐藏标题 D , 因为即使它是第6级标题， 它也显示在 TOC 的第二层。 而且它 *将* 隐藏页眉 G , 尽管这是一个级别-3的标题与标题 B 一样， 因为标题 G 在 TOC 第三级显示， 而标题 B 在第二级显示。

#### 冲突冲突

此模板与 `{{[TOC right](TOC_right.md)}}` 模板。要实现正确效果，请使用带有限制参数的模板。例如, `{{[TOC right](TOC_right.md)|limit=2}}` 具有以下效果 `{{[TOC right](TOC_right.md)}}` 及 `{{[TOC limit](TOC_limit.md)|2}}` 如果他们一起工作的话

#### 模板数据

插入一个目录，其中略去超出一定深度的子标题。

模板参数

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 限制限制 | `1` `limit` | 包含在目录表中的最大页眉深度 默认默认3 | 数目 | 建议 |

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
