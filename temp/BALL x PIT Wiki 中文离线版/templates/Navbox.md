# 模板 · 导航框（Navbox）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Navbox) · [修订 733](https://ballxpit.wiki.gg/index.php?oldid=733) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Navbox_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Navbox/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Navbox/testcases)页面上进行实验。 |

说明
:   此模板用于创建基本的导航框。您可以通过“语法”下的步骤调用该模板，但建议通过“导航框创建”下的步骤**逐字复制代码**。

导航框创建

1. 为你的导航框想一个名称，比如“Navbox Foo”。在上方字段中输入它，点击按钮，然后立即保存页面。准备好返回*此*页面查看其余说明。
2. 以源模式编辑生成的页面。
3. 替换 `{{{header}}}` 您希望出现在标题栏中的文本。
4. 替换 `{{{body}}}` 希望出现在正文中的文本。
5. 要添加另一个章节，请立即在现有代码中与该代码相似的这几行下方复制这四行代码：

```
|-
! style="padding:0.2em 0.5em;" nowrap="nowrap" class="color1" | {{{header}}}
|-
| style="padding:0.2em 0.5em;" | {{{body}}}
```

在添加了所需的所有部分并填充内容后，保存页面。您还可以创建一个 /doc 子页面来解释，要调用生成的模板，只需输入内容即可。 `{{Navbox Foo}}`或者更确切地说，我们在步骤1中决定给模板命名的名称。

语法

```
{{navbox
|header=Land of Bob
|body=This [[place]] and that [[place]].
}}
```

:   结果在...

[共享导航](../navigation/nav-75fd388f1d9d.md)

**分类**　[分类 · 导航模板](../categories/Navigation_templates.md) · [分类 · 带有导航框的页面](../categories/Pages_with_navboxes.md) · [分类 · 导航框模板](../categories/Navbox_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
