# 模板 · 关于（About）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:About) · [修订 248](https://ballxpit.wiki.gg/index.php?oldid=248) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Hatnote_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:About/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:About/testcases) 页面上进行实验。 |

广义上说，一个帽子应该回答读者的问题:我是否在正确的页面上?

[ ]

#### 目录（Contents）

* [1 使用率](#%E4%BD%BF%E7%94%A8%E7%8E%87)
* [2 参数参数](#%E5%8F%82%E6%95%B0%E5%8F%82%E6%95%B0)
* [3 示例](#%E7%A4%BA%E4%BE%8B)
* [4 典型类型](#%E5%85%B8%E5%9E%8B%E7%B1%BB%E5%9E%8B)
* [5 含义不一致](#%E5%90%AB%E4%B9%89%E4%B8%8D%E4%B8%80%E8%87%B4)
* [6 错误错误](#%E9%94%99%E8%AF%AF%E9%94%99%E8%AF%AF)
* [7 技术细节](#%E6%8A%80%E6%9C%AF%E7%BB%86%E8%8A%82)

#### 使用率

基本使用

```
{{hatnote|text}}
```

所有参数

```
{{hatnote|text|extraclasses=extra classes|selfref=yes|category=no}}
```

#### 参数参数

本模板接受以下参数:

* `1` - 帽子笔记文字(需要)
* `extraclasses` - 任何额外的 CSS 类类要加加的 CSS 类等。
* `selfref` - 如果设置为“是”、“y”、“真实”或“1”, 添加 CSS 类“ selfref ” 。 这用来表示自我引用。
* `category` - 如果设置为“否”、“n”、“false”或“0”,则抑制错误跟踪类别([分类 · 有错误的标签模板（Hatnote templates with errors）](../categories/Hatnote_templates_with_errors.md)))。只有当最左的参数(顶点文字)被省略时，才会产生效果。

#### 示例

* `{{hatnote|Example hatnote text}}` →

  顶顶顶图示

#### 典型类型

{{[主要](Main.md)}}, {{[更多](Further.md)它们是非常相似的，但请指出一个专题的主页或更为详细的相关专题。它们有一套几乎相同的参数。

{{[主要](Main.md)}}
:   当文章内容大时，它往往有摘要和与主要文章的链接，该模板用于摘要标题之后，以显示与所摘要的分专题文章的链接。

{{[更多](Further.md)}}
:   用于链接载有本专题进一步资料的文章。

{{[另见](See_also.md)}}
:   用于与相关专题的补充条款链接。

:   {{[主要](Main.md)|*"主页"*}} →
    :   主题: [主页](../articles/BALL_x_PIT_Wiki.md)

:   {{[主要](Main.md)|*"主页"*|*"主页"*}} →
    :   主要条款: [主页](../articles/BALL_x_PIT_Wiki.md) 及 [主页](../articles/BALL_x_PIT_Wiki.md)

:   * `1`、 `2`、 `3`,...-链接到的页面。如果未指定页名，则使用当前页名(没有命名空间前缀)。 [结结肠技巧](https://ballxpit.wiki.gg/wiki/W%3AHelp%3AColon_trick?action=edit&redlink=1),并与各节链接的链接将自动格式化为 *§ 节*,而不是 MediaWiki 默认 *页页 #页页页*.
    * `l1`、 `l2`、 `l3`, ... *或是*`label 1`、 `label 2`、 `label 3`, ... - 每个链接页面的可选标签(这是用于使用管道链接的文章的标签)。请注意，额外参数使用小写“L”,例如, `l1`、 *没有* `L1`.
    * `selfref` - 如果设置为“是”、“y”、“真实”或“1”,则添加CSS类“felfref”。这用来表示自我引用。

#### 含义不一致

QQ 等模板关于和和和[对于](For.md)}} 适用于无需消歧义的情况。一般仅在有 4 个或更多名称完全或几乎相同、只靠限定词区分的标题时，才使用消歧义页。

{{关于}}
:   将读者与其他标题或概念相似的文章链接起来。

    {{关于|*<Use1>*}} →
    :   其他用途见 [关于(分歧)](https://ballxpit.wiki.gg/wiki/About_%28disambiguation%29?action=edit&redlink=1).

:   {{关于|*`<Use1>`*|*<>*|*"主页"*}} →
    :   此页面是关于 use1的。 关于其他用途，请参见 [主页](../articles/BALL_x_PIT_Wiki.md).

:   {{关于|*`<Use1>`*|*<>*|*"主页"*|*> 和> 键*|*"主页"*}} →
    :   此页面是关于 use1的。 关于其他用途，请参见 [主页](../articles/BALL_x_PIT_Wiki.md) 及 [主页](../articles/BALL_x_PIT_Wiki.md).

:   {{关于|*`<Use1>`*|*`<Use2>`*|*"主页"*}} →
    :   此页面是关于使用 1的。 关于使用 2， 见 [主页](../articles/BALL_x_PIT_Wiki.md).

:   {{关于|*`<Use1>`*|*`<Use2>`*|*"主页"*|*> 和> 键*|*"主页"*}} →
    :   此页面是关于使用 1的。 关于使用 2， 见 [主页](../articles/BALL_x_PIT_Wiki.md) 及 [主页](../articles/BALL_x_PIT_Wiki.md).

:   {{关于|*`<Use1>`*|*`<Use2>`*|*"主页"*|*< 其他用途>*}} →
    :   此页面是关于使用 1的。 关于使用 2， 见 [主页](../articles/BALL_x_PIT_Wiki.md)。关于其他用途，参见 [关于(分歧)](https://ballxpit.wiki.gg/wiki/About_%28disambiguation%29?action=edit&redlink=1).

备选,a `section=yes` 可添加到 {} 的参数关于用于区域顶部的模板。当使用此参数时，模板中的措辞会修改，以具体说明其在某一区域中正在使用:

:   {{关于|*`<Use1>`*|*< section=是>*}} →
    :   本节关于Usus1。 其他用途参见: [关于(分歧)](https://ballxpit.wiki.gg/wiki/About_%28disambiguation%29?action=edit&redlink=1).

:   {{关于|*`<Use1>`*|*<>*|*"主页"*|*< section=是>*}} →
    :   本节关于Usus1。 其他用途参见: [主页](../articles/BALL_x_PIT_Wiki.md).

:   {{关于|*`<Use1>`*|*`<Use2>`*|*"主页"*|*< section=是>*}} →
    :   本节关于Use1。 关于Use2，参见: [主页](../articles/BALL_x_PIT_Wiki.md).

:   {{关于|*`<Use1>`*|*`<Use2>`*|*"主页"*|*> 和> 键*|*"主页"*|*< section=是>*}} →
    :   本节关于Use1。 关于Use2，参见: [主页](../articles/BALL_x_PIT_Wiki.md) 及 [主页](../articles/BALL_x_PIT_Wiki.md).

:   {{关于|*`<Use1>`*|*`<Use2>`*|*"主页"*|*< 其他用途>*|*< section=是>*}} →
    :   本节关于Use1。 关于Use2，参见: [主页](../articles/BALL_x_PIT_Wiki.md)。关于其他用途，参见 [关于(分歧)](https://ballxpit.wiki.gg/wiki/About_%28disambiguation%29?action=edit&redlink=1).

A 文本 在结尾处添加文本; 注意， 只有在真正必要时才使用此选项， 以下列出的其他顶点模板并不足够。 此模板还支持此模板 自定义.

{{[对于](For.md)}}
:   提供最多四条文章或脱节页面的链接。它接受零至五个参数。

:   如果在名为 *Foo* 的页面上没有参数使用，结果就是
    :   其他用途见 [Foo(差异)](https://ballxpit.wiki.gg/wiki/Foo_%28disambiguation%29?action=edit&redlink=1).

    第一个参数会改变顶点本身， 并且应该是纯文本， 例如 {} {} } {}[对于](For.md)|*< 类似术语>** 产量
    :   类似术语，见 [Foo(差异)](https://ballxpit.wiki.gg/wiki/Foo_%28disambiguation%29?action=edit&redlink=1).

    第二个参数用于改变结果的链接，例如 QQ[对于](For.md)|*< 类似术语>*|*"主页"** 产量
    :   类似术语，见 [主页](../articles/BALL_x_PIT_Wiki.md).

:   第三、第四和第五参数用于提供一、二或三个补充链接

    * 类似术语，见 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md) 及 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md).

:   * 类似术语，见 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md)、 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md)和 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md).

:   * 类似术语，见 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md)、 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md)、 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md)和 [主页（Main Page）](../articles/BALL_x_PIT_Wiki.md).

:   最后一个由例如 QQ 生产[对于](For.md)|*< 类似术语>*|*"主页"*|*"主页"*|*"主页"*|*"主页"*}}.

#### 错误错误

如果不提供顶点文字， 模板将输出以下信息 :

* **错误: 没有指定文本 ([帮助帮助帮助](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3ATemplate%3AHatnote?action=edit&redlink=1)).**

如果您看到此错误信息， 原因有四个:

1. 未指定参数( 模板代码是 `{{hatnote}}`请使用。 请使用。 请使用。 `{{hatnote|text}}` 而不是。
2. 一些参数已经指定， 但顶点文字没有包含。 例如， 模板文本 `{{hatnote|extraclasses=seealso}}` 将产生此错误。 请使用( 例如) `{{hatnote|text|extraclasses=seealso}}` 而不是。
3. 指定了顶点文本， 但该文本包含等号 (“ =” ) 。 等号在模板代码中具有特殊含义， 因此无法在不指定参数名称的模板参数中使用。 例如， 模板代码 `{{hatnote|2+2=4}}` 将产生此错误。要围绕此错误工作，您可以通过使用 `1=` 在帽子文字之前，像这样: `{{hatnote|1=2+2=4}}`.
4. 您试图访问 [模块:标签](../site/Module_Hatnote.md) 直接使用 `{{#invoke:hatnote|hatnote|text}}`。这样使用 #invoke 的方式因性能原因被禁用。请使用 `{{hatnote|text}}` 而不是。

包含此错误消息的页面在 [类别:含错误的标签模板](../categories/Hatnote_templates_with_errors.md) 错误信息。

#### 技术细节

此模板模板使用 [Lua 临时语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1),可以找到更多信息 [全球卢亚模块页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Hatnote?action=edit&redlink=1). **此模板的传统维基文本版本见 [模板维基](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3AHatnote?action=edit&redlink=1)**.

由此模板生成的 HTML 代码看起来是这样 :

* `<div role="note" class="hatnote">hatnote text</div>`

**分类**　[分类 · 通知模板](../categories/Notice_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
