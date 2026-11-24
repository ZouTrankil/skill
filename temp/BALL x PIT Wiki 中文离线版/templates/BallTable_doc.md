# 模板 · 球表/doc（BallTable/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallTable%2Fdoc) · [修订 4053](https://ballxpit.wiki.gg/index.php?oldid=4053) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

[圆球](../articles/Balls.md)上的三个球表之一，建于 [圆球](../data/Balls.md)货物表。

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

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
