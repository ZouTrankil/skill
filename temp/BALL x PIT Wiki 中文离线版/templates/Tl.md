# 模板 · 调值（Tl）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Tl) · [修订 587](https://ballxpit.wiki.gg/index.php?oldid=587) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Tl_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Tl/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Tl/testcases) 页面上进行实验。 |

![](../assets/commons--Wikipedia.svg)

此代码由 [维基百科](https://en.wikipedia.org/wiki/Main_Page) 调适。

原始代码见以下页面: [Module:Template链接通用](https://en.wikipedia.org/wiki/Module%3ATemplate_link_general), [模板:Tlx](https://en.wikipedia.org/wiki/Template%3ATlx)

![](../assets/commons--Lua.svg)

本模板使用用Lua编程语言撰写的一个或多个模块。

详情见 [维基百科:](https://en.wikipedia.org/wiki/Wikipedia%3ALua) 或是 [关于媒体wiki.org的Lua参考手册](https://mediawiki.org/wiki/Extension%3AScribunto/Lua_reference_manual)所使用的模块包括: **[模板链接](../site/Module_Template_link.md)**.

如果模板存在， 此模板将返回模板在链接到模板描述页面时的外观使用。

#### 使用率

```
{{tl|<Template name>}}
{{tl|<Template name>|<Template parameters>}}
```

*未命名参数* 1
:   模板模板名称( 没有 `Template:` 前缀)

*未命名参数* 2 - 9
:   可选的模板参数

无
:   显示未连接模板使用的可选标志。

#### 实例实例实例

:   `{{tl|stub}}` 返回返回返回 `{{[stub](Stub.md)}}`
:   `{{tl|stub|1}}` 返回返回返回 `{{[stub](Stub.md)|1}}`
:   `{{tl|stub|1|2|nl{{=}}y}}` 返回返回返回 `{{[stub](Stub.md)|1|2|nl=y}}`
:   `{{tl|for|page|t1{{=}}alt text}}` 返回返回返回 `{{[for](For.md)|page|t1=alt text}}`

#### 另见

**分类**　[分类 · 格式化模板](../categories/Formatting_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
