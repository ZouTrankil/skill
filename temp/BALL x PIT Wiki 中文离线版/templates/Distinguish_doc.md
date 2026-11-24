# 模板 · 区分/doc（Distinguish/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Distinguish%2Fdoc) · [修订 493](https://ballxpit.wiki.gg/index.php?oldid=493) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此帽子注模板用于指出读者可能想要寻找的替代选项。

模板参数 此模板更倾向于使用内联格式设置参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 替代方案 | `1` | 备用页面。 示例替代页面 | 页面名称 | 建议 |
| 第二种选择 | `2` | 第二个备用页面。 示例第二备选页面 | 页面名称 | 可选 |
| 第三选择 | `3` | 第三个备用页面。 示例第三备选页面 | 页面名称 | 可选 |
| 替代文本 | `text` | 您可以使用完整的替代文本，而不是页面。此参数会覆盖其他提供的参数。 示例备用页面，\[\[备用页面\]\] | 线 | 可选 |

## 示例

| 代码 | 结果 |
| --- | --- |
| `{{Distinguish\|Special:Uncategorizedpages}}` | 请勿与 [Special:Uncategorizedpages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages) 混淆。 |
| `{{Distinguish\|Special:Uncategorizedpages\|Special:Uncategorizedfiles}}` | 请勿与 [Special:Uncategorizedpages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages) 或 [Special:Uncategorizedfiles](https://ballxpit.wiki.gg/wiki/Special:UncategorizedFiles) 混淆。 |
| `{{Distinguish\|Special:Uncategorizedpages\|Special:Uncategorizedfiles\|Special:Uncategorizedcategories}}` | 请勿与 [Special:Uncategorizedpages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages)、[Special:Uncategorizedfiles](https://ballxpit.wiki.gg/wiki/Special:UncategorizedFiles) 或 [Special:Uncategorizedcategories](https://ballxpit.wiki.gg/wiki/Special:UncategorizedCategories) 混淆。 |
| `{{Distinguish\|Special:Uncategorizedpages{{!}}Page 1}}` （自定义链接标签 / Custom link label） | 请勿与 [第1页](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages)混淆。 |
| `{{Distinguish\|text = Page 1, another name for [[Special:Uncategorizedpages]]}}` | 请勿与第 1 页混淆，后者是 [Special:Uncategorizedpages](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages) 的另一个名称。 |

## 依赖项

为了让此模板正常工作，您需要以下内容：

* `{{[Hatnote](Hatnote.md)}}` 基础模板。
* `.hatnote` 类别，可在 [MediaWiki:Common.css](../site/MediaWiki_Common.css.md).

## 来源

大致基于 [Wikipedia的Distinguish模板](https://en.wikipedia.org/wiki/Template%3ADistinguish)。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
