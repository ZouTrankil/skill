# 模板 · 主页框（Main page box）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Main_page_box) · [修订 556](https://ballxpit.wiki.gg/index.php?oldid=556) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此模板用于创建 IMProved 主页（IMP） 框架框。 **不应该直接叫它**,而不是使用 `{{[Main page box/start](Main_page_box_start.md)}}` 及 `{{[Main page box/end](Main_page_box_end.md)}}`.

使用下面的框创建页面时， 需要的模板已经到位， 可以添加内容。

框名称不能包含空格， 也不能以数字开头。 这可能是您唯一会遇到的限制， 但完整列表请查看 [MDN 网站上的“ 客户识别” 文件](https://developer.mozilla.org/en-US/docs/Web/CSS/custom-ident).

#### 参数参数

这些参数是 `{{[Main page box/start](Main_page_box_start.md)}}`。所有参数都是可选的。

| 名称 | 数据类型 | 描述 |
| --- | --- | --- |
| 标题标题 | Wikitext | 框的标题。此选项可以是空的， 在这样的情况下， 框将只包含内容。 |
| 班级 | CSS 班级 | 向框中传送的类别列表，按空格和不引号分隔。标准选项 `centered-content` 垂直居中内容，以及 `has-floating-image` 如果框中需要浮动图像( 通常灵活布局不允许) 。 |
| 样式 | CSS 声明 | 直接适用于框框的内嵌 CSS ,无引号。 `text-align:center;` 对于单个框希望以中文本为主的情况。 |

**分类**　[分类 · 主页模板](../categories/Main_page_templates.md) · [分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
