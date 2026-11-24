# 模板 · 文件（Documentation）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Documentation) · [修订 305](https://ballxpit.wiki.gg/index.php?oldid=305) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Documentation_doc.md) ( 关于模板文档) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Documentation/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Documentation/testcases) 页面上进行实验。 |

[ ]

#### 目录（Contents）

* [1 描述](#%E6%8F%8F%E8%BF%B0)
* [2 语法](#%E8%AF%AD%E6%B3%95)
* [3 使用率](#%E4%BD%BF%E7%94%A8%E7%8E%87)
  + [3.1 在模板页面上](#%E5%9C%A8%E6%A8%A1%E6%9D%BF%E9%A1%B5%E9%9D%A2%E4%B8%8A)
  + [3.2 文件页](#%E6%96%87%E4%BB%B6%E9%A1%B5)

#### 描述

此模板用于在模板页面插入描述。

#### 语法

添加添加添加 `<noinclude>{{Documentation}}</noinclude>` 在模板页面结尾处。

添加添加添加 `<noinclude>{{Documentation|<documentation page>}}</noinclude>` 以从/doc 子页中清除替代页面。

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

请注意，上述例子也使用了 [模板:T](T.md) 模板。

**分类**　[分类 · 文件模板](../categories/Documentation_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
