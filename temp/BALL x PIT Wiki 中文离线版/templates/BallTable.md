# 模板 · 球桌（BallTable）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallTable) · [修订 4052](https://ballxpit.wiki.gg/index.php?oldid=4052) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](BallTable_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:BallTable/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:BallTable/testcases) 页面上进行实验。 |

[圆球](../articles/Balls.md)上的三个球表之一，建于 [圆球](../data/Balls.md)货物表。

[ ]

#### 目录（Contents）

* [1 职位安排](#%E8%81%8C%E4%BD%8D%E5%AE%89%E6%8E%92)
* [2 参数参数](#%E5%8F%82%E6%95%B0%E5%8F%82%E6%95%B0)
* [3 列](#%E5%88%97)
* [4 示例](#%E7%A4%BA%E4%BE%8B)
* [5 备注](#%E5%A4%87%E6%B3%A8)

#### 职位安排

在 [圆球](../articles/Balls.md) 上，每节一次。每个表格有一个查询覆盖所有91个球。

```
{{BallTable|class=base}}
{{BallTable|class=evolved}}
{{BallTable|class=baby}}
```

#### 参数参数

| 参数 | 意义意思意思意思 |
| --- | --- |
| `class` | `base`、 `evolved` 或是 `baby`默认默认值的默认值。默认默认值的默认值。默认值的默认值。默认默认值的默认值。 `base`. |

#### 列

| 班级 | 列 |
| --- | --- |
| `base` | 图标、名称、说明、字符、解除锁状态、触动效果、状态触发器、状态效果 |
| `evolved` | 同样，与 **合并** 和 **可以进一步进化** 以取代字符和解除锁 |
| `baby` | 图标、名称、说明 |

组合和“可以进一步演进”是从同一通行证中的 [BallRecipeEdges](../data/BallRecipeEdges.md)计算出来的，既不在任何页面上打字，也不得在添加配方时腐烂。

#### 示例

`baby` 是一个小到足以在这里展示的班级—— 其他是21和69行， 属于 [圆球](../articles/Balls.md):

```
{{BallTable|class=baby}}
```

#### 备注

* 利用 `data-basics` / `data-intermediates` 属性“球过滤”脚本读取。
* 要更改一行所说的话， 请编辑该球的文章， 而不是此模板。

**分类**　[分类 · 球模板](../categories/Ball_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
