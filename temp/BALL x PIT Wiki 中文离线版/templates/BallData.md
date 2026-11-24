# 模板 · 球数据（BallData）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallData) · [修订 4066](https://ballxpit.wiki.gg/index.php?oldid=4066) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](BallData_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:BallData/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:BallData/testcases) 页面上进行实验。 |

球文章的数据模板。 **stories**该球在 [圆球](../data/Balls.md)货物表 **中的行，使** 成为相同值的信息框，因此页面上没有输入两次。

[ ]

#### 目录（Contents）

* [1 职位安排](#%E8%81%8C%E4%BD%8D%E5%AE%89%E6%8E%92)
* [2 参数参数](#%E5%8F%82%E6%95%B0%E5%8F%82%E6%95%B0)
* [3 食食权](#%E9%A3%9F%E9%A3%9F%E6%9D%83)
* [4 语法](#%E8%AF%AD%E6%B3%95)
* [5 为什么这里没有活生生的例子](#%E4%B8%BA%E4%BB%80%E4%B9%88%E8%BF%99%E9%87%8C%E6%B2%A1%E6%9C%89%E6%B4%BB%E7%94%9F%E7%94%9F%E7%9A%84%E4%BE%8B%E5%AD%90)
* [6 备注](#%E5%A4%87%E6%B3%A8)

#### 职位安排

每个球文章一次， 在最上面。 这是编辑最需要输入的唯一的球模板。

使用 **不** 传递一个页面名称:您将其放置在球上 *is* 上的文章。 不要通过图标 - [IconLink](IconLink.md) 从页面名称中获取。

#### 参数参数

全部可选; 空字段仅在行和信息框中找不到。

| 参数 | 意义意思意思意思 |
| --- | --- |
| `ball_class` | `base`、 `evolved` 或是 `baby`。设置文章的类别。有效要求 — 空白的一页将页面存档到 [类别:无等级的篮球](https://ballxpit.wiki.gg/wiki/Category:Balls_with_no_class?action=edit&redlink=1). |
| `display_name` | 游戏标签 **仅** 与页标题不同，今天每个球都是空白的 |
| `starting_characters` | 以此球开头的字符。 逗号分隔列表: 布莱德、 地震、 铁和闪电各有两个。 |
| `unlock_condition` | `Unlocked by default`,或如: . `Clear The SNOWYxSHORES`基球的球仅 . . |
| `release_group` | `base-game` 或是 `post-launch`. |
| `summary` | [圆球](../articles/Balls.md)表格中显示的短线。一组数字，大小为90行扫描。 |
| `stat_combined_description` | 较长的工具提示行， 以斜线标记为单位水平值。 重叠 `summary` 目的 - **如果编辑一个，编辑另一个**. |
| `on_hit_effects` | 球在撞击时会做什么: `Self-destruct`、 `Pass-through`、 `Spawn`AOOE. 不是范围效果。不是AOOE. |
| `status_triggers` | 何种效果可适用于: `On-Hit`、 `AOE`、 `Full screen AOE`、 `On-Timer`、 `On-shoot`、 `Spawn`、 `On-timer spawn`、 `On-bounce spawn`、 `On-kill spawn`。如果球没有状态效果，则留空。 |
| `status_effects` | 效果应用。 游戏效果名称保持原样。`Burn`、 `Poison`;任何描述动作的文字都是动词第一(动词第一())Spawn [Baby Ball](../articles/Baby_Ball.md)、 `Kill instantly`). |
| `ingredient_1_options` … `_4` | 进化配方。 每个槽是 **替代品** 列表; 不同的槽是共序。 四个槽是上限， 最多不能持有四个球。 |

`?` 任何地点都是合法的价值，意味着还没有人证实。

#### 食食权

```
|ingredient_1_options = Laser (Horizontal), Laser (Vertical)
|ingredient_2_options = Poison, Cell
```

原文原文原文为 *(Laser HH(拉拉瑟H(拉拉拉瑟)) **或是** 激光V)+(球) **或是** 单元格)*基球和婴儿球和婴儿球都完全忽略了这些。..

食谱在[BallRecipeEdges](../data/BallRecipeEdges.md)中作为每一替代物的一行存储，而不是作为列在这里，这就是让任何一页都问"Burn进化成什么",而不让Burn的一页列出任何东西。

#### 语法

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

基球会掉下成分槽并添加 `starting_characters` 及
`unlock_condition`.

#### 为什么这里没有活生生的例子

此模板模板 **写到 Cargo**。将它放在这页上， 将备有
[圆球](../data/Balls.md) 列对列 *模板:BallData/doc* - 球是不存在的， 坐在每一个询问和每个桌子直到有人注意到，一个管理员跑
*重新创建数据*。 。 。 这同样也是。[球状](BallStat.md)和和和[Ball 矩形](BallRecipeEdge.md)}}.

模板 *读为* 货物可以证明，并且:[球数据/信息框](BallData_Infobox.md)}}, {{[球演变](BallEvolutions.md)}}, {{[球体](BallCreation.md)}}, {{[球表](https://ballxpit.wiki.gg/wiki/Template%3ABallsTable?action=edit&redlink=1)}}, {{[圆球](Balls.md)}}.

完整工作文章见 [灼烧](../articles/Burn.md)。

#### 备注

* **只允许主空间。** 在任何其他名称空间中， 此模板只能存储任何内容， 所以一个沙箱副本无法归档一个不存在的球。 之前创建的行需要从沙盒页面上进行空格编辑才能清除。
* 各行不回填。在下一页解析之前， 添加此模板无任何作用， 无效编辑它。
* 通过 [模板:BallData/Infobox](BallData_Infobox.md) 进行调试; Evolutions 块是一个查询， 因此永远不会过时。

**分类**　[分类 · 球模板](../categories/Ball_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
