# 模板 · 区分/doc（Distinguish/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Distinguish%2Fdoc) · [修订 493](https://ballxpit.wiki.gg/index.php?oldid=493) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

该帽子模板意在用来表明读者希望找到的替代材料的可能替代品。

模板参数 此模板更倾向于参数的内嵌格式化。

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 替代 | `1` | 备选页。 示例备选网页替代网页 | 页面名称 | 建议 |
| 第二替代品 | `2` | 替代页的第二个替代页的第二页替代替代页第二页。 示例第二次备选替代页 | 页面名称 | 可选 |
| 第三替代品 | `3` | 第三个替代页面。 示例第三替代页 | 页面名称 | 可选 |
| 备选案文 | `text` | 无需使用页面，您可以提供一个完整的替代文本。此参数高于其他提供的参数。 示例\[替代页\] | 线线 | 可选 |

#### 实例实例实例

| 《法典法典法典》 | 结果 |
| --- | --- |
| `{{Distinguish\|Special:Uncategorizedpages}}` | 不应与 [特别:未分类网页](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages). |
| `{{Distinguish\|Special:Uncategorizedpages\|Special:Uncategorizedfiles}}` | 不应与 [特别:未分类网页](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages) 或是 [特别:未分类文件](https://ballxpit.wiki.gg/wiki/Special:UncategorizedFiles). |
| `{{Distinguish\|Special:Uncategorizedpages\|Special:Uncategorizedfiles\|Special:Uncategorizedcategories}}` | 不应与 [特别:未分类网页](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages)、 [特别:未分类文件](https://ballxpit.wiki.gg/wiki/Special:UncategorizedFiles) 或是 [特别:未分类类别](https://ballxpit.wiki.gg/wiki/Special:UncategorizedCategories). |
| `{{Distinguish\|Special:Uncategorizedpages{{!}}Page 1}}` （海关链接标签 / Custom link label） | 不应与 [第1页](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages). |
| `{{Distinguish\|text = Page 1, another name for [[Special:Uncategorizedpages]]}}` | 不与第1页相混淆 [特别:未分类网页](https://ballxpit.wiki.gg/wiki/Special:UncategorizedPages). |

#### 依赖性

此模板要正常工作， 您需要以下信息:

* 其他 `{{[Hatnote](Hatnote.md)}}` 基准模板。
* 其他 `.hatnote` 类，在 [MediaWiki:Common.css](../site/MediaWiki_Common.css.md).

#### 来源来源

基本基于 [维基百科的杰出模板](https://en.wikipedia.org/wiki/Template%3ADistinguish)。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
