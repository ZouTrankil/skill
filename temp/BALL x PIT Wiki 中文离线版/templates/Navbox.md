# 模板 · 航行箱（Navbox）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Navbox) · [修订 733](https://ballxpit.wiki.gg/index.php?oldid=733) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Navbox_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Navbox/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Navbox/testcases) 页面上进行实验。 |

描述
:   此模板用于创建基本导航框。 您可以通过“ 语法” 下的“ 语法 ” 步骤调用该模板， 从而创建基本导航框， 但建议您通过“ 创建纳夫箱” 下的步骤 **复制代码逐字记录** 。

创建导航框

1. 想象一下您的 navbox 的名称， 比如“ Navbox Foo ” 。 在上述字段中键入它， 按下按钮并立即保存页面。 准备返回 *此* 页面以查看其余的说明。
2. 以源模式编辑所产生的页面。
3. 替换 `{{{header}}}` 您想要在页眉中出现文本。
4. 替换 `{{{body}}}` 与您想要在身体中出现的文本一起出现。
5. 在增加另一节时，请将这四行代码复制至其类似现有代码下方的直线下方:

```
|-
! style="padding:0.2em 0.5em;" nowrap="nowrap" class="color1" | {{{header}}}
|-
| style="padding:0.2em 0.5em;" | {{{body}}}
```

一旦您根据需要添加了尽可能多的章节， 并用内容填入页面。 您也可以创建 / doc 子页面， 解释要调用结果模板， 只需输入 `{{Navbox Foo}}`,或者说，不管我们决定在步骤1中命名模板。

语法

```
{{navbox
|header=Land of Bob
|body=This [[place]] and that [[place]].
}}
```

:   结果是。..

[共享导航](../navigation/nav-75fd388f1d9d.md)

**分类**　[分类 · 导航模板](../categories/Navigation_templates.md) · [分类 · 页面有导航框](../categories/Pages_with_navboxes.md) · [分类 · Navbox 模板](../categories/Navbox_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
