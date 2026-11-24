# 模板 · 球状态（BallStat）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallStat) · [修订 4043](https://ballxpit.wiki.gg/index.php?oldid=4043) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](BallStat_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:BallStat/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:BallStat/testcases)页面上进行实验。 |

一个球的一个等级。存储一行数据
[圆球分级数值表](../data/BallStatsByLevel.md) **并呈现出来** 文章关卡表中那一行。

[ ]

## 目录（Contents）

* [1 放置方式](#%E6%94%BE%E7%BD%AE%E6%96%B9%E5%BC%8F)
* [2 参数](#%E5%8F%82%E6%95%B0)
* [3 语法](#%E8%AF%AD%E6%B3%95)
* [4 此处省略运行示例的原因](#%E6%AD%A4%E5%A4%84%E7%9C%81%E7%95%A5%E8%BF%90%E8%A1%8C%E7%A4%BA%E4%BE%8B%E7%9A%84%E5%8E%9F%E5%9B%A0)

## 放置方式

每颗球三次的条目位于关卡表格内，属于{{[BallData](BallData.md)}}下的部分。该条目指的是球，因此不需要传递球名称。

小球没有关卡，也不包含这些元素。

## 参数

| 参数 | 含义 |
| --- | --- |
| `1` | 等级： `1`、 `2` 或 `3`. |
| `damage` | 仅伤害范围，例如 `3.5 to 6.5`. 没有属性名称，也没有“Damage” — 这些是在渲染时添加的，而仅有的数值范围才是使该列可排序的原因。 |
| `effect` | 在这个等级下，球会做什么。 |
| `stat` | 可选属性图标，例如： `st` 为了力量。 **已渲染但未存储** — 存储在字段中的统计数据图标将在数据库中被展平为文件标记。 |

使用 `?` 对于任何未确认的信息。跨层总数和上限（“最多8层”）均适用。 **不** 点击这里 — 它们属于此处 `stat_combined_description` 在 {{[球数据](BallData.md)}}.

## 语法

表格标题保留在文章中，因为三个独立的跨列引用无法共享同一个容器：

```
== Levels ==
{| class="wikitable"
! Level !! Damage !! Effect
{{BallStat|1|stat=st|damage=3.5 to 6.5|effect=Add 1 stack of [[Status Effects|Burn]] on hit for 3 seconds (max 3 stacks).}}
{{BallStat|2|stat=st|damage=?|effect=?}}
{{BallStat|3|stat=st|damage=?|effect=?}}
|}
```

## 此处省略运行示例的原因

此模板用于写入Cargo 信息。在此处渲染会生成一条与等级相关的记录。

*模板:BallStat/doc*. 参见 [灼烧](../articles/Burn.md) 放置好桌子。

**分类**　[分类 · 球模板](../categories/Ball_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
