# 模板 · 文档资料/文档（Documentation/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Documentation%2Fdoc) · [修订 396](https://ballxpit.wiki.gg/index.php?oldid=396) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

## 说明

此模板用于插入模板页面上的描述。

## 语法

添加 `<noinclude>{{[Documentation](Documentation.md)}}</noinclude>` 在模板页面末尾。

添加 `<noinclude>{{[Documentation](Documentation.md)|<documentation page>}}</noinclude>` 要引用/doc子页面中的其他页面。

## 使用

### 在模板页面上

这是使用时的常规格式：

```
TEMPLATE CODE
<includeonly>Any categories to be inserted into articles by the template</includeonly>
<noinclude>{{Documentation}}</noinclude>
```

*如果您的模板不是完整的 div 或 table，您可能需要在即将结束之前关闭标签。 `{{Documentation}}` 已插入（在 noinclude 标签内）。*

*就在换行之前 `{{Documentation}}` 这也有用，因为它有助于防止文档模板“遇到”之前的代码。*

### 在文档页面上

文档页面通常位于模板的 /doc 子页面上，但可以通过模板的第一个参数指定其他页面（参见 [语法](#%E8%AF%AD%E6%B3%95)）。

通常，您会在文档页面上写入类似以下内容：

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

使用上述说明/语法/示例输出部分中的任意或全部内容。您也可以添加“参见”或其他部分。

请注意，上述示例也使用了 [模板:T](T.md) 模板。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
