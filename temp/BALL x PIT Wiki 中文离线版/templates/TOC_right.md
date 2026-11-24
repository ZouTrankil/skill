# 模板 · TOC 右侧（TOC right）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:TOC_right) · [修订 585](https://ballxpit.wiki.gg/index.php?oldid=585) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](TOC_right_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:TOC_right/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:TOC_right/testcases)页面上进行实验。 |

`{{TOC right}}` 为了改善文章布局，强制将自动生成的文章目录显示在页面右侧。

## 使用

插入 `{{TOC right}}` 在文章中的某个位置，你希望目录框的顶部出现。这通常位于主要部分的文本之后，以及第一个部分标题之前。使用时请遵循…… `{{[clear](Clear.md)}}` 为避免与文本冲突，请避免将 TOC 放置在视觉不佳的位置。跨越章节划分可能不是一个好主意。

限制
:   限制显示的子标题深度。例如，使用 `limit=4` 将隐藏等级中的第四级及更深层次的子标题。并且 `limit=2` 将隐藏所有子标题，仅保留主标题。这是通过 CSS 来隐藏较低级别的关卡实现的。详情请参阅 `{{[TOC limit](TOC_limit.md)}}` 有关此信息的更多详情。

不要放置此模板，以免目录与大型图片或信息框对齐；这会在窄屏上破坏布局（即使屏幕宽度达到 1024px 的用户也可能遇到问题）。此外，如果可以避免的话，让目录跨越部分划分显然是个糟糕的主意。

除非该章节中 `{{TOC right}}` 放置时间太长，结果可能并不理想。

它只应在TOC妨碍其他内容或不利于页面布局的情况下使用；它应该 *不* 仅仅用于美观目的，因为它会破坏文章的标准外观。

## 模板数据

{{TOC right}} forces the auto-generated "Table of Contents" for an article to appear floated to the right side of the page (as seen right), in order to improve article layout.

模板参数 此模板更倾向于使用内联格式设置参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 限制 | `limit` | 限制了显示的子标题深度。例如，使用 limit=4 将隐藏层级中的第四级及更深的子标题。而 limit=2 则隐藏所有子标题，仅保留主标题。这是通过 CSS 隐藏较低层级来实现的。 | 数字 | 可选 |

**分类**　[分类 · 目录模板](../categories/Table_of_contents_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
