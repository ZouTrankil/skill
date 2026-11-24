# 模板 · 为/doc（For/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:For%2Fdoc) · [修订 499](https://ballxpit.wiki.gg/index.php?oldid=499) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此帽子注模板用于展示读者可能想要访问的相关页面。

模板参数 此模板更倾向于使用内联格式设置参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 主题 | `1` | 以下页面的内容主题与此相关。 示例更多信息 | 线 | 必需 |
| 相关页面 | `2` | 相关页面。 示例相关页面 | 页面名称 | 必需 |
| 第二页 | `3` | 第二个相关页面。 示例相关第二页面 | 页面名称 | 可选 |
| 第三页 | `4` | 第三个相关页面。 示例相关第三页 | 页面名称 | 可选 |

## 示例

| 代码 | 结果 |
| --- | --- |
| `{{For\|more information\|Special:WantedPages}}` | 更多信息，请参阅 [Special:WantedPages](https://ballxpit.wiki.gg/wiki/Special:WantedPages)。 |
| `{{For\|more information\|Special:WantedPages\|Special:UncategorizedPages}}` | 更多信息，请参阅 [Special:WantedPages](https://ballxpit.wiki.gg/wiki/Special:WantedPages) 和 [Special:UncategorizedPages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages)。 |
| `{{For\|more information\|Special:WantedPages\|Special:UncategorizedPages\|Special:UncategorizedCategories}}` | 更多信息，请参阅 [Special:WantedPages](https://ballxpit.wiki.gg/wiki/Special:WantedPages)、[Special:UncategorizedPages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages) 和 [Special:UncategorizedCategories](https://ballxpit.wiki.gg/wiki/Special:UncategorizedCategories)。 |
| `{{For\|more information\|Special:WantedPages{{!}}Page 1}}` （自定义链接标签 / Custom link label） | 更多信息，请参阅 [第1页](https://ballxpit.wiki.gg/wiki/Special:WantedPages)。 |

## 依赖项

为了让此模板正常工作，您需要以下内容：

* `{{[Hatnote](Hatnote.md)}}` 基础模板。
* `.hatnote` 类别，可在 [MediaWiki:Common.css](../site/MediaWiki_Common.css.md).

## 来源

大致基于 [Wikipedia的For模板](https://en.wikipedia.org/wiki/Template%3AFor)。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
