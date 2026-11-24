# 模板 · 标签（Hatnote）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Hatnote) · [修订 124](https://ballxpit.wiki.gg/index.php?oldid=124) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Hatnote_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Hatnote/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Hatnote/testcases)页面上进行实验。 |

用于添加文章间链接的注释，适用于需要更多上下文的情况。广义上讲，注释应回答读者的疑问：我是否找到了正确的页面？

[ ]

## 目录（Contents）

* [1 使用](#%E4%BD%BF%E7%94%A8)
* [2 参数](#%E5%8F%82%E6%95%B0)
* [3 示例](#%E7%A4%BA%E4%BE%8B)
* [4 典型类型](#%E5%85%B8%E5%9E%8B%E7%B1%BB%E5%9E%8B)
* [5 消歧义](#%E6%B6%88%E6%AD%A7%E4%B9%89)
* [6 错误](#%E9%94%99%E8%AF%AF)
* [7 技术细节](#%E6%8A%80%E6%9C%AF%E7%BB%86%E8%8A%82)

## 使用

基本用法

```
{{hatnote|text}}
```

所有参数

```
{{hatnote|text|extraclasses=extra classes|selfref=yes|category=no}}
```

## 参数

此模板接受以下参数：

* `1` - 帽注文本（必填）
* `extraclasses` - 可以添加任何额外的 CSS 类。
* `selfref` 如果设置为“yes”、“y”、“true”或“1”，将添加 CSS 类“selfref”。此类用于表示自我引用。
* `category` 如果设置为“否”、“n”、“false”或“0”，则禁用错误跟踪分类。[分类 · 包含错误的标签模板（Hatnote templates with errors）](../categories/Hatnote_templates_with_errors.md)). 只有当最左侧参数（即脚注文本）被省略时，此效果才会生效。

## 示例

* `{{hatnote|Example hatnote text}}` →

  示例说明文本

## 典型类型

{{[主要](Main.md)}}, {{[进一步](Further.md)}} 非常相似，但分别表示某个主题的主页面或更详细的相关主题。它们的参数几乎完全相同。

{{[主要](Main.md)}}
:   当文章篇幅较长时，通常会有一个摘要以及指向主文章的链接。此模板用于摘要标题之后，以指示指向该摘要子主题的链接。

{{[进一步](Further.md)}}
:   用于链接到包含有关此主题更多信息的文章。

{{[另见](See_also.md)}}
:   用于链接相关主题的附加文章。

:   {{[主要](Main.md)|*〈主页面〉*}} →
    :   主条目：[主页](../articles/BALL_x_PIT_Wiki.md)

:   {{[主要](Main.md)|*〈主页面〉*|*〈主页面〉*}} →
    :   主条目：[主页](../articles/BALL_x_PIT_Wiki.md) 和 [主页](../articles/BALL_x_PIT_Wiki.md)

:   * `1`、 `2`、 `3`, ... – 要链接到的页面。如果未指定页面名称，则使用当前页面名称（不包括命名空间前缀）。类别和文件会自动加上转义字符。 [殖民者技巧](https://ballxpit.wiki.gg/wiki/W%3AHelp%3AColon_trick?action=edit&redlink=1)，以及链接到各个章节的内容会自动进行格式处理。 *页面 § 章节*，而不是 MediaWiki 的默认设置 *page#section*.
    * `l1`、 `l2`、 `l3`, ... *或*`label 1`、 `label 2`、 `label 3`... – 每个链接页面的可选标签（适用于使用管道链接的文章）。请注意，额外的参数使用小写的 'L' 表示。 `l1`、 *不* `L1`.
    * `selfref` – 如果设置为 "yes"、"y"、"true" 或 "1"，则添加 CSS 类 "selfref"。此类用于表示自我引用。

## 消歧义

如{{[关于](About.md)}}和{{[为](For.md)}}这样的模板，仅用于不需要消歧义的情况。一般来说，消歧义页面仅应用于4个或更多在除限定词外大部分或完全相同的标题。

{{[关于](About.md)}}
:   将读者链接到他们可能正在寻找的具有相似标题或概念的其它文章。该模板有多种格式，包括：

    {{[关于](About.md)|*<Use1>*}} →
    :   关于其他用法，请参阅 [注释（消歧义）](https://ballxpit.wiki.gg/wiki/Hatnote_%28disambiguation%29?action=edit&redlink=1)。

:   {{[关于](About.md)|*`<Use1>`*|*<>*|*〈主页面〉*}} →
    :   本页介绍的是 Use1。关于其他用法，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   {{[关于](About.md)|*`<Use1>`*|*<>*|*〈主页面〉*|*〈and〉*|*〈主页面〉*}} →
    :   本页介绍的是 Use1。关于其他用法，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md) 和 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   {{[关于](About.md)|*`<Use1>`*|*`<Use2>`*|*〈主页面〉*}} →
    :   本页面介绍的是 Use1。关于 Use2，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   {{[关于](About.md)|*`<Use1>`*|*`<Use2>`*|*〈主页面〉*|*〈and〉*|*〈主页面〉*}} →
    :   本页介绍的是 Use1。关于 Use2，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md) 和 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   {{[关于](About.md)|*`<Use1>`*|*`<Use2>`*|*〈主页面〉*|*〈其他用途〉*}} →
    :   本页介绍的是 Use1。关于 Use2，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)。其他用法，请参阅 [标签说明（歧义）](https://ballxpit.wiki.gg/wiki/Hatnote_%28disambiguation%29?action=edit&redlink=1)。

或者，一个 `section=yes` 参数可以添加到{{[关于](About.md)}} 用于部分顶部的模板。使用此参数时，模板中的文字会发生变化，以表明它适用于某个部分：

:   {{[关于](About.md)|*`<Use1>`*|*〈section=yes〉*}} →
    :   本部分介绍 Use1。关于其他用法，请参阅 [标签（歧义）](https://ballxpit.wiki.gg/wiki/Hatnote_%28disambiguation%29?action=edit&redlink=1)。

:   {{[关于](About.md)|*`<Use1>`*|*<>*|*〈主页面〉*|*〈section=yes〉*}} →
    :   本部分介绍 Use1。关于其他用法，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   {{[关于](About.md)|*`<Use1>`*|*`<Use2>`*|*〈主页面〉*|*〈section=yes〉*}} →
    :   本部分介绍的是 Use1。关于 Use2，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   {{[关于](About.md)|*`<Use1>`*|*`<Use2>`*|*〈主页面〉*|*〈and〉*|*〈主页面〉*|*〈section=yes〉*}} →
    :   本部分介绍的是 Use1。关于 Use2，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md) 和 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   {{[关于](About.md)|*`<Use1>`*|*`<Use2>`*|*〈主页面〉*|*〈其他用途〉*|*〈section=yes〉*}} →
    :   本部分介绍的是 Use1。关于 Use2，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)。其他用法，请参阅 [标签说明（消歧义）](https://ballxpit.wiki.gg/wiki/Hatnote_%28disambiguation%29?action=edit&redlink=1)。

A text 此选项会在文本末尾添加内容；请注意，仅应在真正必要时使用，以下列出的其他注释模板并不适用。此模板也支持该功能。 selfref.

{{[用于](For.md)}}
:   提供至多四个文章或消歧义页面的链接。可接受零到五个参数。

:   如果在名为 *Foo* 的页面上未使用参数使用时，结果为
    :   关于其他用法，请参阅 [Foo（消歧义）](https://ballxpit.wiki.gg/wiki/Foo_%28disambiguation%29?action=edit&redlink=1)。

    第一个参数用于修改帽子注释本身，应为纯文本，例如 {{[用于](For.md)|*〈相似用语〉*}} 产出
    :   对于类似的术语，请参阅 [Foo（歧义）](https://ballxpit.wiki.gg/wiki/Foo_%28disambiguation%29?action=edit&redlink=1)。

    第二个参数用于更改结果链接，例如 {{[为了](For.md)|*<类似术语>*|*<主页>*}} 会生成
    :   对于类似的术语，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   第三、第四和第五个参数用于提供一个、两个或三个补充链接。

    * 对于类似的术语，请参见 [主页](../articles/BALL_x_PIT_Wiki.md) 和 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   * 对于类似的术语，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)、[主页](../articles/BALL_x_PIT_Wiki.md) 和 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   * 对于类似的术语，请参阅 [主页](../articles/BALL_x_PIT_Wiki.md)、[主页](../articles/BALL_x_PIT_Wiki.md)、[主页](../articles/BALL_x_PIT_Wiki.md) 和 [主页](../articles/BALL_x_PIT_Wiki.md)。

:   最后由例如{{}}生产[用于](For.md)|*〈相似用语〉*|*〈主页面〉*|*〈主页面〉*|*〈主页面〉*|*〈主页面〉*}}.

## 错误

如果未提供帽子注文本，模板将输出以下消息：

* **错误：未指定文本。[帮助](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3ATemplate%3AHatnote?action=edit&redlink=1)).**

如果您看到此错误消息，其原因可能有四种：

1. 未指定参数（模板代码为 `{{hatnote}}`). 请使用 `{{hatnote|text}}` 。
2. 某些参数已指定，但未包含脚注文本。例如，模板文本 `{{hatnote|extraclasses=seealso}}` 会导致此错误。请使用（例如） `{{hatnote|text|extraclasses=seealso}}` 。
3. 帽子注释文本已指定，但该文本包含等号（“=”）。在模板代码中，等号具有特殊含义，因此不能用于未指定参数名称的模板参数中。例如，模板代码 `{{hatnote|2+2=4}}` 将会产生此错误。为了解决这个问题，您可以明确使用参数名称来指定。 `1=` 在注释文本之前，如下所示： `{{hatnote|1=2+2=4}}`.
4. 你试图访问 [Module:Hatnote](../site/Module_Hatnote.md) 直接使用 `{{#invoke:hatnote|hatnote|text}}`. 出于性能原因，以这种方式使用#invoke已被禁用。请使用其他方式。 `{{hatnote|text}}` 。

包含此错误消息的页面被记录在 [分类：包含错误的标签模板](../categories/Hatnote_templates_with_errors.md) 中。

## 技术细节

此模板使用 [Lua 模板语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1)，更多相关信息可以在 [Global Lua Module 页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Hatnote?action=edit&redlink=1)找到。**如需此模板的传统维基文本版本，请参阅  [Templates Wiki 上的注释](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3AHatnote?action=edit&redlink=1)**。

该模板生成的 HTML 代码如下所示：

* `<div role="note" class="hatnote">hatnote text</div>`

**分类**　[分类 · 注意模板](../categories/Notice_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
