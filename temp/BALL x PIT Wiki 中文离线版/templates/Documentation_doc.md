# 模板 · 文件/文档（Documentation/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Documentation%2Fdoc) · [修订 396](https://ballxpit.wiki.gg/index.php?oldid=396) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

#### 描述

此模板用于在模板页面插入描述。

#### 语法

添加添加添加 `<noinclude>{{[Documentation](Documentation.md)}}</noinclude>` 在模板页面结尾处。

添加添加添加 `<noinclude>{{[Documentation](Documentation.md)|<documentation page>}}</noinclude>` 以从/doc 子页中清除替代页面。

#### 使用率

##### 在模板页面上

使用时此格式为常规格式 :

```
TEMPLATE CODE
<includeonly>Any categories to be inserted into articles by the template</includeonly>
<noinclude>{{Documentation}}</noinclude>
```

*如果您的模板不是一个完整的 div 或表格， 您可能需要在之前关闭标签 `{{Documentation}}` 插入(在“不包括”标签内)。*

*前面的换行符 `{{Documentation}}` 也可以有用，因为它有助于防止文档模板“运行到”以前的代码。*

##### 文件页

文件页面通常位于模板的/doc 子页面上，但可以用模板的第一个参数指定不同的页面(见 [Syntax](#%E8%AF%AD%E6%B3%95))。

通常情况下，您要在文档页面上写下类似内容:

```
==Description==
This template is used to do something.

==Syntax==
Type <code>{{t|templatename}}</code> somewhere.

==Samples==
<code><nowiki>{{templatename|input}}</nowiki></code>

results in...

{{templatename|input}}

<includeonly>Any categories for the template itself</includeonly>
<noinclude>[[Category:Template documentation]]</noinclude>
```

使用上述描述/ 语法/ 样本输出部分的任何或全部。 您也可以添加“ 另参看” 或其他部分。

请注意，上述示例还使用 [模板:T](T.md)模板。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
