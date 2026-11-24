# 模板 · 议员链接（MP link）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:MP_link) · [修订 551](https://ballxpit.wiki.gg/index.php?oldid=551) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](MP_link_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:MP_link/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:MP_link/testcases) 页面上进行实验。 |

这将创建 [main page](../articles/BALL_x_PIT_Wiki.md) 上的一个模板化和格式化链接。

#### 使用率

此模板格的组组应该包裹在 `<div class="mp-links"></div>` 每个条目应单列一行，在 [无顺序排序列表](https://en.wikipedia.org/wiki/Help%3ALists#Basically)。此 div 可以是其中的一个班级中，一个班级中，一个班级可以给予此 div 。 `columns-x` 其中 x 是 1到 8个数字， 如果空间允许的话， 链接会排成许多列( 默认是 3) 。 也可以选择给 div 分类。 `stretch` 它会垂直拉伸列表以填充空格。见 [Mediawiki:Common.css](../site/MediaWiki_Common.css.md) 用于定义这些类别的全部定义和本模板的型号。

##### 参数参数

在主页上创建标准化和格式化链接。

模板参数 此模板更倾向于参数的内嵌格式化。

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 文本 | `1` | 要显示的文字。 如果不给定链接参数， 则此选项也将是链接目标。 示例附加件 | 字符串字符串 | 建议 |
| 链接链接链接 | `link` | 链接的目标页面，如果与显示文本不同。 示例主页 | 页面名称 | 可选 |
| 图片 | `image` | 用链接显示的图像。 | 文件文件 | 建议 |
| 图像图像大小 | `size` | 图像的大小， 以 px 表示。 默认默认42px (英语)。 | 字符串字符串 | 可选 |
| 图像类 | `imageClass` | 直接给图像的类 建议数值`invert-on-dark` `invert-on-light`示例反倒对称 | 字符串字符串 | 可选 |
| Alt 文本 | `altText` | 用于描述图像的 Alt 文字 示例维基徽标 | 字符串字符串 | 建议 |

#### 实例实例实例

```
<div class="mp-links columns-3">
* {{MP link|Stuff|link=Special:Random|image=Site-logo.png|size=42px}}
* {{MP link|Things|link=Special:Random}}
* {{MP link|Other stuff|link=Special:Random|image=Site-logo.png|size=42px}}
</div>
```

生产:

* [附加件](https://ballxpit.wiki.gg/wiki/Special%3ARandom) [![Site-logo.png](../assets/Site-logo.png)](https://ballxpit.wiki.gg/wiki/Special:Random)
* [事事事](https://ballxpit.wiki.gg/wiki/Special%3ARandom)
* [其它东西](https://ballxpit.wiki.gg/wiki/Special%3ARandom) [![Site-logo.png](../assets/Site-logo.png)](https://ballxpit.wiki.gg/wiki/Special:Random)

**分类**　[分类 · 主页模板](../categories/Main_page_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
