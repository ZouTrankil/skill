# 模板 · 球统计/doc（BallStat/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallStat%2Fdoc) · [修订 4044](https://ballxpit.wiki.gg/index.php?oldid=4044) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

一级一球。 在 [BallStatsBylevel](../data/BallStatsByLevel.md) **中储存一行， 并将该行写成** 。

#### 职位安排

每篇圆球条目使用三次，放在等级表的 {{ 下。[球数据](BallData.md)。文章是球，所以没有球名。

婴儿球没有水平，也没有这些。

#### 参数参数

| 参数 | 意义意思意思意思 |
| --- | --- |
| `1` | 级别 : `1`、 `2` 或是 `3`. |
| `damage` | 仅伤害范围，例如: `3.5 to 6.5`。没有 Stat 名称，没有“数据”——这些在绘制时被添加，而光区域是该列可以排序的。 |
| `effect` | 球在这个级别上做什么? |
| `stat` | 任择状态图标，例如。 `st` 强力。 **交付但从未储存** - 存储字段内的一个 Stat 图标将被平整，以便在数据库中输入标记。 |

使用使用 `?` 跨级别总计和上限 (“ 最多 8堆叠 ” ) do **没有** 在这里，他们属于 `stat_combined_description` 在 {{[球数据](BallData.md)}}.

#### 语法

表格页眉以文章为主， 因为三个不同的切除无法共享一个折叠件 :

```
== Levels ==
{| class="wikitable"
! Level !! Damage !! Effect
{{BallStat|1|stat=st|damage=3.5 to 6.5|effect=Add 1 stack of [[Status Effects|Burn]] on hit for 3 seconds (max 3 stacks).}}
{{BallStat|2|stat=st|damage=?|effect=?}}
{{BallStat|3|stat=st|damage=?|effect=?}}
|}
```

#### 为什么这里没有活生生的例子

此模板向 Cargo 写入。 在此提交时会根据 *模板:BallStat/doc* 提交一个级别列。 表格的位置请参见 [灼烧](../articles/Burn.md) 。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
