# 模板 · 球统计/doc（BallStat/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallStat%2Fdoc) · [修订 4044](https://ballxpit.wiki.gg/index.php?oldid=4044) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

一个球的一个等级。存储一行数据
[圆球分级数值表](../data/BallStatsByLevel.md) **并呈现出来** 文章关卡表中那一行。

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

此模板用于写入 Cargo。在此处渲染会导致向 *Template:BallStat/doc* 提交一条等级行。有关具体表格，请参阅 [灼烧](../articles/Burn.md)。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
