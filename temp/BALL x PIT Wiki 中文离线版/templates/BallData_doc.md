# 模板 · 球数据/doc（BallData/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallData%2Fdoc) · [修订 4040](https://ballxpit.wiki.gg/index.php?oldid=4040) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

这是关于球类游戏的百科模板。它**存储**球类的行在[圆球](../data/Balls.md)Cargo 表中**并渲染**信息框，因此页面上的内容不会重复输入。

## 放置方式

每次球类文章时，在顶部位置。这是大多数编辑唯一需要输入的球类模板。

做 **不** 页面名称：您放置该文章的页面名称 *是* 球。也不要传递图标。 [IconLink](IconLink.md) 其名称源自该页面的名称。

## 参数

所有选项均为可选择的；空白字段则完全不存在该行和信息框中。

| 参数 | 含义 |
| --- | --- |
| `ball_class` | `base`、 `evolved` 或 `baby`. 设置文章的分类。强制要求——留空则会将页面归档。 [分类：无类别的球](https://ballxpit.wiki.gg/wiki/Category:Balls_with_no_class?action=edit&redlink=1). |
| `display_name` | 游戏内的标签， **仅限** 这与页面标题有所不同。今天每个球都是空白的。 |
| `starting_characters` | 以这个球开头的角色。用逗号分隔的列表：流血、地震、铁与闪电各有两个。 |
| `unlock_condition` | `Unlocked by default`或者例如。 `Clear The SNOWYxSHORES`. 仅限基础圆球。 |
| `release_group` | `base-game` 或 `post-launch`. |
| `summary` | 在 [圆球（Balls）](../articles/Balls.md) 的表格中显示的短行。一组数字，大小适合扫描90行。 |
| `stat_combined_description` | 较长的工具提示行，每级数值用斜杠表示。有重叠部分。 `summary` 故意地 — **如果你编辑了一个，也编辑另一个。**. |
| `on_hit_effects` | 球撞击时的反应： `Self-destruct`、 `Pass-through`、 `Spawn`. 非范围效果。 |
| `status_triggers` | 效果生效的原因： `On-Hit`、 `AOE`、 `Full screen AOE`、 `On-Timer`、 `On-shoot`、 `Spawn`、 `On-timer spawn`、 `On-bounce spawn`、 `On-kill spawn`. 如果球没有状态效果，则留空。 |
| `status_effects` | 已施加效果。游戏效果名称保持不变。`Burn`、 `Poison`); 描述动作的词语应以动词开头（Spawn [Baby Ball](../articles/Baby_Ball.md)、 `Kill instantly`). |
| `ingredient_1_options` … `_4` | 进化配方。每个槽位都是 **选项** 的列表；不同的槽位是共同成分。最多只能持有四个球，即四个槽位的上限。 |

`?` 在任何地方都是合法的值，意味着目前还没有人确认它。

## 配方

```
|ingredient_1_options = Laser (Horizontal), Laser (Vertical)
|ingredient_2_options = Poison, Cell
```

表现为 *(激光 H **或** 激光 V) + (中毒 **或** 细胞)*。基础球和小球完全省略这些效果。

配方在 [圆球配方材料表](../data/BallRecipeEdges.md) 中按每种替代方案存储为一行，而非此处按列存储。正是这种结构使得任何页面都能询问“灼烧会进化成什么”，而无需在灼烧的页面中列出任何内容。

## 语法

```
{{BallData
|ball_class                = evolved
|release_group             = base-game
|summary                   =
|stat_combined_description =
|on_hit_effects            =
|status_triggers           =
|status_effects            =
|ingredient_1_options      =
|ingredient_2_options      =
}}
```

棒球掉落原料槽，并添加 `starting_characters` 及
`unlock_condition`.

## 此处省略运行示例的原因

此模板 **写入 Cargo**。在页面上渲染它会为 *Template:BallData/doc* 生成一行 [圆球](../data/Balls.md) 记录——这是一个不存在的球，存在于所有查询和表中，直到有人注意到并由管理员执行了 *重新创建数据*。对于 {{[BallStat](BallStat.md)}} 和 {{[圆球配方材料](BallRecipeEdge.md)}} 也是如此。

只有 *阅读* 的 Cargo 才能展示的模板包括：{{[BallData/Infobox](BallData_Infobox.md)}}、{{[BallEvolutions](BallEvolutions.md)}}、{{[BallCreation](BallCreation.md)}}、{{[圆球列表](https://ballxpit.wiki.gg/wiki/Template%3ABallsTable?action=edit&redlink=1)}} 和 {{[圆球](Balls.md)}}。

如需完整的文章内容，请参阅 [灼烧](../articles/Burn.md)。

## 备注

* **仅限主空间。** 在其他任何命名空间中，此模板会渲染但不会存储任何内容，因此沙箱副本无法投掷不存在的球。在保护机制存在之前创建的行，需要在沙箱页面上进行空值编辑以清除。
* 行不会填充。添加此模板在页面下次解析之前没有任何效果——请直接编辑为空。
* 通过 [模板:BallData/Infobox](BallData_Infobox.md) 渲染；Evolution 块是一个查询，因此它永远不会过时。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
