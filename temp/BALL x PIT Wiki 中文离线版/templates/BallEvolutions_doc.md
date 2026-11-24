# 模板 · 球演变/doc（BallEvolutions/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallEvolutions%2Fdoc) · [修订 4176](https://ballxpit.wiki.gg/index.php?oldid=4176) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

`== Evolutions ==` 圆球条目中的表格列出了以本圆球为材料的所有配方，以及各配方需要的其他材料。

## 放置方式

每次球比伦战记游戏百科中，在……条件下 `== Evolutions ==` 标题。没有参数——文章就是球。

```
== Evolutions ==
{{BallEvolutions}}
```

## 示例

可选的第一个参数可以覆盖页面，这是将该模板展示在球类文章之外的唯一方式。

```
{{BallEvolutions|Burn}}
```

灼烧是十个球中的一种成分，在其单独页面中并未单独列出名称。

当没有配方使用该球时，表格将被一条说明该情况的行替代，而不是让该部分保持空位：

```
{{BallEvolutions|Armageddon}}
```

这已经涵盖了维基百科的一半内容——69个进化圆球中已有49个已经绝迹，[小球](../articles/Baby_Ball.md)也是如此。

## 这些行来自何处

[圆球配方材料表](../data/BallRecipeEdges.md)，因此表格不会过时：一个新的进化球会从**其自身**页面获取边缘信息，并出现在此处，而无需修改这篇文章。

每一行显示的是配方中的**其他**槽位，因为{{[组合](Combination.md)}}已经为当前页面添加了前缀。三种形态都出现在[灼烧](../articles/Burn.md)上：

| 配方 | 以渲染形式呈现 |
| --- | --- |
| 灼烧 + 铁 | 一种成分 |
| 灼烧 + （中毒 **或**石头） | 两条线，每个选项一条。 |
| 灼烧 + 风 + 冻结 + 地震 | 一行三成分 |

## 另见

* {{[球创造](BallCreation.md)}} — 反向：一种改良后的球自身配方。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
