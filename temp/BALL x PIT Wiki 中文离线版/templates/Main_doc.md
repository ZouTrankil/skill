# 模板 · 主/doc（Main/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Main%2Fdoc) · [修订 553](https://ballxpit.wiki.gg/index.php?oldid=553) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此帽子注模板用于文章中的各个部分，用于提及其他现有主文章的信息。

模板参数 此模板更倾向于使用内联格式设置参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 文章 | `1` | 主文章。 示例文章 | 页面名称 | 必需 |
| 第二篇 | `2` | 第二主文章。 示例第二篇 | 页面名称 | 可选 |
| 第三篇 | `3` | 第三主文章。 示例第三篇 | 页面名称 | 可选 |

## 示例

| 代码 | 结果 |
| --- | --- |
| `{{Main\|Special:WantedPages}}` | 主页面：[Special:WantedPages](https://ballxpit.wiki.gg/wiki/Special:WantedPages) |
| `{{Main\|Special:WantedPages#Section Title}}` | 主页面：[Special:WantedPages § 章节标题](https://ballxpit.wiki.gg/wiki/Special:WantedPages#Section_Title) |
| `{{Main\|Special:WantedPages\|Special:UncategorizedPages}}` | 主页面：[Special:WantedPages](https://ballxpit.wiki.gg/wiki/Special:WantedPages) 和 [Special:UncategorizedPages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages) |
| `{{Main\|Special:WantedPages\|Special:UncategorizedPages\|Special:UncategorizedCategories}}` | 主页面：[Special:WantedPages](https://ballxpit.wiki.gg/wiki/Special:WantedPages)、[Special:UncategorizedPages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages) 和 [Special:UncategorizedCategories](https://ballxpit.wiki.gg/wiki/Special:UncategorizedCategories) |
| `{{Main\|Special:WantedPages{{!}}Page 1}}` （自定义链接标签 / Custom link label） | 主页面：[第1页](https://ballxpit.wiki.gg/wiki/Special:WantedPages) |

## 依赖项

此模板需要包含 `{{[Hatnote](Hatnote.md)}}` 元模板。

## 来源

大致基于 [Wikipedia的For模板](https://en.wikipedia.org/wiki/Template%3AFor)。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
