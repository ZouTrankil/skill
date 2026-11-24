# 模板 · 主页面框（Main page box）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Main_page_box) · [修订 556](https://ballxpit.wiki.gg/index.php?oldid=556) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此模板用于创建 IMProved 主页（IMP）框架的框体。 **不应直接称之为**，改为使用 `{{[Main page box/start](Main_page_box_start.md)}}` 及 `{{[Main page box/end](Main_page_box_end.md)}}`.

使用下方的框来创建一个已配备所需模板的页面，您可以直接添加内容。

框名不能包含空格，也不能以数字开头。完整命名规则见 MDN 的 [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/custom-ident)。

## 参数

这些是游戏百科中使用的参数。 `{{[Main page box/start](Main_page_box_start.md)}}`. 所有参数均为可选。

| 名称 | 数据类型 | 说明 |
| --- | --- | --- |
| 标题 | Wikitext | 盒子的标题。这可以是空的，在这种情况下，盒子将仅包含内容。 |
| 类别 | CSS类 | 需要传递给盒子的角色列表，用空格分隔，无需引号。标准选项为 `centered-content` 将内容垂直居中，并且 `has-floating-image` 如果盒子中需要浮动图像（通常弹性布局不允许这种情况）。 |
| 风格 | CSS声明 | 直接在不加引号的盒模型中应用内联 CSS。常见的用法是 `text-align:center;` 适用于希望各个框内文本居中的情况。 |

**分类**　[分类 · 主页面模板](../categories/Main_page_templates.md) · [分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
