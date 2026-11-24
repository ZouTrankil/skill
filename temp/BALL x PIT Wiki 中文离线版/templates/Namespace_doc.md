# 模板 · 命名空间/doc（Namespace/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Namespace%2Fdoc) · [修订 352](https://ballxpit.wiki.gg/index.php?oldid=352) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

这是 {{[Namespace](Namespace.md)}} 元模板。它有助于其他模板识别自己所处的页面类型。

它检测并归类了Fandom上使用的所有不同的[命名空间](https://en.wikipedia.org/wiki/Namespace#Enumeration)，将其分为几类：

主要
:   主页空间，用于放置常规文章。

讨论
:   任何聊天空间，包括以“Talk:”、“User talk:”、“File talk:”等开头的页面名称。

用户

文件

mediawiki

模板

帮助

分类
:   剩余的命名空间。

其他
:   任何未作为模板参数指定的命名空间（详见下文说明）。

为了向后兼容，此模板将 **图像** 视为 **文件** 进行处理。**图像**（[[Image:...]]) 现已过时。

**注意：**在大多数情况下，使用更简单的命名空间检测模板可能更为合适（请参阅下面的[另见](https://ballxpit.wiki.gg/wiki/Template%3ANamespace%2Fdoc#See_also)部分）。该模板更容易出现人为错误，例如参数名称拼写错误。

此模板使用 [Lua 模板语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1)，更多相关信息可参见 [全局 Lua 模块页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Namespace_detect?action=edit&redlink=1)。**如需此模板的传统 Wikitext 版本，请参阅 [Templates Wiki 上的 Namespace\_detect](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3ANamespace_detect?action=edit&redlink=1)**。

## 使用

此模板接受一个或多个名为上述不同页面类型的参数。例如：

```
{{Namespace
 | main  = Article text
 | talk  = Talk page text
 | other = Other pages text
}}
```

如果模板位于主页面上，它将返回此内容：

:   文章文本

如果模板位于文章或讨论页以外的其他页面上，它将返回此提示：

:   其他页面文本

上述示例使模板能够为所有页面类型返回内容。但如果我们不使用 **其他** 参数或将其留空，则其他页面类型将不会返回任何内容。例如：

```
{{Namespace
 | file     = File page text
 | category = Category page text
 | other    =
}}
```

在文件页面和分类页面之外的任何页面上，上述代码将不会显示任何内容。

通过使用空参数，你可以让模板对某些特定页面类型不显示任何内容。例如：

```
{{Namespace
 | main  =
 | other = Other pages text
}}
```

当在主空间（文章）页面时，上述代码将不显示任何内容，但在其他页面时会返回此内容：

:   其他页面文本

## Demospace和页面

出于测试和演示目的，此模板可以接受两个名为 **demospace** 和 **page** 的参数。

**demospace** 理解此模板所使用的任何页面类型名称，包括 **other** 类型。它告诉模板表现得就像它位于某种特定类型的页面上。例如：

```
{{Namespace
 | main  = Article text
 | other = Other pages text
 | demospace = main
}}
```

无论上述代码用于哪种页面，它都会返回此结果：

:   文章文本

**page**参数可以接受普通的页面名称，使得此模板的行为完全如同在该页面上一样。页面名称不必是现有的页面。例如：

```
{{Namespace
 | user  = User page text
 | other = Other pages text
 | page  = User:Example
}}
```

无论上述代码用于哪种页面，它都会返回此结果：

:   用户页面文本

让模板理解 **demospace** 和/或 **page** 参数，并将其传递给 {{[Namespace](Namespace.md)}} 模板，这样会非常方便。

```
{{Namespace
 | main  = Article text
 | other = Other pages text
 | demospace = {{{demospace|}}}
 | page  = {{{page|}}}
}}
```

如果 **demospace** 和 **page** 参数均为空或未定义，模板将像往常一样检测页面类型。

## 参数

所有参数列表：

```
{{Namespace
| main  =
...
| other =
| demospace = {{{demospace|}}} / main / talk / user /
              file / mediawiki / template /
              help / category / other
| page  = {{{page|}}} / User:Example
}}
```

## 技术细节

如果您打算将表格作为内容提供给该模板中的编号参数，您需要了解以下事项：

[模板](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ATemplate?action=edit&redlink=1) 处理包含管道的参数数据时遇到问题。`|`除非管道位于另一个模板内部 `{{name|param1}}` 或位于管道链接内 `[[w:Help:Template|help]]`. 因此，模板无法处理这种情况。 [维基表格](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ATable?action=edit&redlink=1) 作为输入，除非你使用退出功能来避开它们。 `{{!}}` [魔法词](https://ballxpit.wiki.gg/wiki/W%3AHelp%3AMagic_words?action=edit&redlink=1). 这使得将维基表格作为模板参数变得困难。通常的解决方案是使用HTML维基标记来编写表格代码，这种方法更为可靠。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
