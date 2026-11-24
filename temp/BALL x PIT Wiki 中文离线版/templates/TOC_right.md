# 模板 · 现在的时间（TOC right）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:TOC_right) · [修订 585](https://ballxpit.wiki.gg/index.php?oldid=585) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](TOC_right_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:TOC_right/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:TOC_right/testcases) 页面上进行实验。 |

`{{TOC right}}` 强迫自动生成的目录显示文章浮到页面右侧，以改善文章布局。

#### 使用率

插入插入 `{{TOC right}}` 在文章的点，您想要显示“目录”框的顶部。这通常应放在牵头部分的文字之后，紧接在第一个部分标题之前。 `{{[clear](Clear.md)}}` 避免与文本发生碰撞。 避免将技选委员会置于视力差的地点。 跨过一个区域划分可能不是一个好主意。

限制
:   显示小标题的深度限制。例如，使用 `limit=4` 将隐藏第四层和更深的副标题在等级。 和 `limit=2` 将隐藏所有仅保留主要标题的小标题。 这样做可以隐藏 CSS 的下层。 见 `{{[TOC limit](TOC_limit.md)}}` 详情请见此。

不要放置此模板， 使 TOC 与大图像或信息箱保持一致; 这打破了窄屏幕上的布局( 即使屏幕宽度达到 1024px 的用户也可能遇到问题 ) 。另外，如果可以避免，跨越一个科司的技选委员会可能不是一个好主意。

除非在 `{{TOC right}}` 放置足够长，结果很可能不可取。

它只应用于技选委员会妨碍其他内容或伤害页面布局的情况;它应*而不是*仅仅用于美学，因为它会破坏物品的标准外观。

#### 模板数据

{{TOC right}} forces the auto-generated "Table of Contents" for an article to appear floated to the right side of the page (as seen right), in order to improve article layout.

模板参数 此模板更倾向于参数的内嵌格式化。

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 限制限制 | `limit` | 显示小标题的深度限制。 例如， 使用限制=4将隐藏等级体系中的第四层和更深的子标题。 限制=2将隐藏所有仅留下主要标题的小标题。 这通过以 CSS 隐藏下层来发挥作用。 | 数目 | 可选 |

**分类**　[分类 · 内容表模板](../categories/Table_of_contents_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
