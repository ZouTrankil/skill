# 模板 · 球创造（BallCreation）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallCreation) · [修订 4068](https://ballxpit.wiki.gg/index.php?oldid=4068) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

用于显示进化小球自身的配方组合，以用于信息框的“由谁创造”一栏。无参数。忽略基础材料和小球。适用于文章部分。
`{{[BallCreationTable](BallCreationTable.md)}}`.

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](BallCreation_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:BallCreation/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:BallCreation/testcases)页面上进行实验。 |

“由……结合而成”一行：一种经过改良的球自身配方。

## 放置方式

每次进化球文章时，在领先的情况下。无参数。

```
{{BallCreation}}
```

没有安打和小球，所以将其放在共享的页面框架中即可安全无忧。

## 示例

第一个参数会覆盖页面，因此可以在此处显示三种配方形状：

| 来源 | 以渲染形式呈现 |
| --- | --- |
| `{{BallCreation\|Bomb}}` | [灼烧](../articles/Burn.md) [![Burn.png](../assets/Burn.png)](../articles/Burn.md) + [铁](../articles/Iron.md) [![Iron.png](../assets/Iron.png)](../articles/Iron.md) |
| `{{BallCreation\|Assassin}}` | [铁](../articles/Iron.md) [![Iron.png](../assets/Iron.png)](../articles/Iron.md)  + ([黑暗](../articles/Dark.md) [![Dark.png](../assets/Dark.png)](../articles/Dark.md) 或 [幽灵](../articles/Ghost.md) [![Ghost.png](../assets/Ghost.png)](../articles/Ghost.md) ) |
| `{{BallCreation\|Radiation Beam}}` | ([激光（水平）](../articles/Laser_Horizontal.md) [![Laser (Horizontal).png](../assets/Laser_%28Horizontal%29.png)](../articles/Laser_Horizontal.md)  或 [激光（垂直）](../articles/Laser_Vertical.md) [![Laser (Vertical).png](../assets/Laser_%28Vertical%29.png)](../articles/Laser_Vertical.md)) + ([细胞](../articles/Cell.md) [![Cell.png](../assets/Cell.png)](../articles/Cell.md)  或 [中毒](../articles/Poison.md) [![Poison.png](../assets/Poison.png)](../articles/Poison.md) ) |

一个成分，一个带有替代方案的插槽，以及两个这样的插槽——这是游戏中最糟糕的情况，但仍然只有一条线。

朗读 [圆球配方材料表](../data/BallRecipeEdges.md)因此，它总是匹配的。
`ingredient_N_options` 保持一致的想法 {{[球数据](BallData.md)}}.

## 另见

* {{[BallEvolutions](BallEvolutions.md)}} — 反向：这个球体的演变过程 *进入*.

**分类**　[分类 · 球模板](../categories/Ball_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
