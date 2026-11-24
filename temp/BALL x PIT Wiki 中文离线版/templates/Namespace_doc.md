# 模板 · 名称空间/doc（Namespace/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Namespace%2Fdoc) · [修订 352](https://ballxpit.wiki.gg/index.php?oldid=352) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

这是。..[名称空间](Namespace.md)元模板。它有助于其他模板检测其页面的类型。

它将Fandom使用的所有不同的 [命名空间](https://en.wikipedia.org/wiki/Namespace#Enumeration) 检测和分组为几种类型:

主要
:   主要(即物品)空间，存放正常物品。

谈谈
:   任何谈话空间， 包括以“ 演讲: ” 开头的页面名称、 “ 用户演讲: ” “ 发言: ” 、 “ 游戏演讲: ” 等等。

用户用户

文件文件

媒体

模板

帮助帮助帮助

类别
:   剩余命名空间。

其他
:   未指定为模板参数的任何命名空间(见下文解释)。

对于后向兼容性， 此模板处理 **映像** , 好像 **文件** 。 **映像** ([[图像: ] ]) 现在被折旧。

**注:** 对于大多数情况，最好使用更简单的命名空间探测模板(见 [另见下文](https://ballxpit.wiki.gg/wiki/Template%3ANamespace%2Fdoc#See_also) 节)。这个模板更容易出现人为错误，如拼错参数名称。

此模板模板使用 [Lua 临时语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1),可以找到更多信息 [全球卢亚模块页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Namespace_detect?action=edit&redlink=1). **此模板的传统维基文本版本见 [模板上的名称空间\_ 探测](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3ANamespace_detect?action=edit&redlink=1)**.

#### 使用率

此模板使用上面所列不同页面类型后命名的一个或多个参数。 例如 :

```
{{Namespace
 | main  = Article text
 | talk  = Talk page text
 | other = Other pages text
}}
```

如果模板在主页(文章)页面上， 它会返回此模板 :

:   条条案文

如果模板在文章或谈话页面以外的任何页面上， 它会返回 :

:   其他页数

上述示例使模板返回了所有页面类型的某种内容。 但如果我们不使用 **其它** 参数或将其留空， 它将不会返回其它页面类型的任何内容。 例如 :

```
{{Namespace
 | file     = File page text
 | category = Category page text
 | other    =
}}
```

除档案和分类页外，上述代码在任何页面上都无济于事。

使用空参数可以使模板无法对特定页面类型产生任何效果。例如 :

```
{{Namespace
 | main  =
 | other = Other pages text
}}
```

在主空间(文章)页面上，上述代码将无任何作用，但在其他页面上，则将归还:

:   其他页数

#### 空间和页面

为测试和演示目的，该模板可使用两个参数，即 **demospace** 和 **page**。

**demospace** 理解此模板所使用的任何页面类型名称， 包括 **其它** 类型。 它告诉模板在某特定类型的页面上的行为方式。 例如 :

```
{{Namespace
 | main  = Article text
 | other = Other pages text
 | demospace = main
}}
```

无论上面的代码使用哪页， 它都会返回:

:   条条案文

**page** 参数取一个普通的页名，使本模板的行为与该页完全相同。页名不必是已有的页。像这样:

```
{{Namespace
 | user  = User page text
 | other = Other pages text
 | page  = User:Example
}}
```

无论上面的代码使用哪页， 它都会返回:

:   用户网页文本

让您的模板理解 **振动空间** 和/或 **页次** 参数并发送到QQ[名称空间](Namespace.md)模板。像这样:

```
{{Namespace
 | main  = Article text
 | other = Other pages text
 | demospace = {{{demospace|}}}
 | page  = {{{page|}}}
}}
```

如果**demospace**和**page**两个参数都是空的或未定义的，模板将照常检测页面类型。

#### 参数参数

全部参数列表 :

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

#### 技术细节

如果您打算将表格作为内容反馈到此模板的编号参数， 您需要知道这一点 :

[模板](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ATemplate?action=edit&redlink=1) 含有管道的处理参数数据存在问题 "`|`除非管子在另一个模板里 `{{name|param1}}` 或管道链接内 `[[w:Help:Template|help]]`。因此模板无法处理 [维基通](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ATable?action=edit&redlink=1) 作为输入输入，除非使用 `{{!}}` [魔法单词](https://ballxpit.wiki.gg/wiki/W%3AHelp%3AMagic_words?action=edit&redlink=1)。这使得很难使用维基字符作为模板的参数。相反，通常的解决方案是使用 HTML 维基马克来表示表格代码，因为表格代码更坚固。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
