# 模板 · 文档（Tl/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Tl%2Fdoc) · [修订 588](https://ballxpit.wiki.gg/index.php?oldid=588) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

![](../assets/previews/commons--Wikipedia-48px-8d183814.png)

此代码改编自 [Wikipedia](https://en.wikipedia.org/wiki/Main_Page)。

关于原始代码，请参见以下页面：[Module:Template link general](https://en.wikipedia.org/wiki/Module%3ATemplate_link_general)，[模板:Tlx](https://en.wikipedia.org/wiki/Template%3ATlx)

![](../assets/previews/commons--Lua-48px-e7e95a21.png)

此模板使用了一个或多个用 Lua 编程语言编写的模块。

如需更多信息，请参阅 [Wikipedia:Lua](https://en.wikipedia.org/wiki/Wikipedia%3ALua) 或 [MediaWiki.org 上的 Lua 参考手册](https://mediawiki.org/wiki/Extension%3AScribunto/Lua_reference_manual)。使用的模块包括：**[模板链接](../site/Module_Template_link.md)**。

此模板在模板存在时，会返回其示例用法，并链接到模板说明页面。

## 使用

```
{{tl|<Template name>}}
{{tl|<Template name>|<Template parameters>}}
```

*未命名参数* 1
:   模板名称（不含 `Template:` 前缀）

*未命名参数* 2 - 9
:   可选。模板参数

nl
:   可选标志用于显示未链接的模板使用情况。

## 示例

:   `{{tl|stub}}` 返回 `{{[stub](Stub.md)}}`
:   `{{tl|stub|1}}` 返回 `{{[stub](Stub.md)|1}}`
:   `{{tl|stub|1|2|nl{{=}}y}}` 返回 `{{[stub](Stub.md)|1|2|nl=y}}`
:   `{{tl|for|page|t1{{=}}alt text}}` 返回 `{{[for](For.md)|page|t1=alt text}}`

## 另见

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
