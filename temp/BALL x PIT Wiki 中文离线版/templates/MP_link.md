# 模板 · MP链接（MP link）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:MP_link) · [修订 551](https://ballxpit.wiki.gg/index.php?oldid=551) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](MP_link_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:MP_link/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:MP_link/testcases)页面上进行实验。 |

这构成了 [主页](../articles/BALL_x_PIT_Wiki.md)上那些风格化且格式化的链接之一。

## 使用

此模板的组应被包裹在内。 `<div class="mp-links"></div>` 并且每个条目都应该是单行文本。 [无序列表](https://en.wikipedia.org/wiki/Help%3ALists#Basically). 这个角色可以分配其中一个职业。 `columns-x` 其中 x 是一个从 1 到 8 的数字，如果空间允许，链接将排列成相应数量的列（默认值为 3）。该 div 也可以选择性地赋予该类别。 `stretch` 它将垂直拉伸列表以填充空白空间。见 [Mediawiki:Common.css](../site/MediaWiki_Common.css.md) 用于获取这些职业的完整定义以及该模板的样式。

### 参数

在主页面上创建风格化且格式化的链接。

模板参数 此模板更倾向于使用内联格式设置参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 文本 | `1` | 要显示的文本。如果未提供链接参数，则也将作为链接目标。 示例物品 | 字符串 | 建议 |
| Link | `link` | 链接的目标页面，如果与显示文本不同。 示例主页 | 页面名称 | 可选 |
| 图片 | `image` | 带有链接的显示图片。 | 文件 | 建议 |
| 图片大小 | `size` | 图像的大小，单位：像素。 默认42px | 字符串 | 可选 |
| 图像类别 | `imageClass` | 直接给予该图片的一个班级 建议数值`invert-on-dark` `invert-on-light`示例invert-on-dark | 字符串 | 可选 |
| Alt文本 | `altText` | 图片的替代文本描述 示例Wiki标志 | 字符串 | 建议 |

## 示例

```
<div class="mp-links columns-3">
* {{MP link|Stuff|link=Special:Random|image=Site-logo.png|size=42px}}
* {{MP link|Things|link=Special:Random}}
* {{MP link|Other stuff|link=Special:Random|image=Site-logo.png|size=42px}}
</div>
```

显示效果

* [物品](https://ballxpit.wiki.gg/wiki/Special%3ARandom) [![Site-logo.png](../assets/previews/Site-logo-42px-7b5daa64.png)](https://ballxpit.wiki.gg/wiki/Special:Random)
* [事情](https://ballxpit.wiki.gg/wiki/Special%3ARandom)
* [其他内容](https://ballxpit.wiki.gg/wiki/Special%3ARandom) [![Site-logo.png](../assets/previews/Site-logo-42px-7b5daa64.png)](https://ballxpit.wiki.gg/wiki/Special:Random)

**分类**　[分类 · 主页面模板](../categories/Main_page_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
