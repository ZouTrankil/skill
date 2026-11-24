# 模板 · BallTable

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallTable) · [修订 4052](https://ballxpit.wiki.gg/index.php?oldid=4052) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](BallTable_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:BallTable/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:BallTable/testcases)页面上进行实验。 |

位于 [圆球](../articles/Balls.md) 上的三张球桌之一，由 [圆球](../data/Balls.md) 货运桌打造而成。

[ ]

## 目录（Contents）

* [1 放置方式](#%E6%94%BE%E7%BD%AE%E6%96%B9%E5%BC%8F)
* [2 参数](#%E5%8F%82%E6%95%B0)
* [3 列](#%E5%88%97)
* [4 示例](#%E7%A4%BA%E4%BE%8B)
* [5 备注](#%E5%A4%87%E6%B3%A8)

## 放置方式

在……上 [圆球](../articles/Balls.md)每个部分一次。每个表格查询涵盖所有91个球。

```
{{BallTable|class=base}}
{{BallTable|class=evolved}}
{{BallTable|class=baby}}
```

## 参数

| 参数 | 含义 |
| --- | --- |
| `class` | `base`、 `evolved` 或 `baby`. 默认为 `base`. |

## 列

| 类别 | 列 |
| --- | --- |
| `base` | 图标, 名称, 说明, 角色, 解锁条件, 命中时效果, 状态触发条件, 状态效果 |
| `evolved` | 相同，将 **组合** 和 **可进一步进化** 替换成角色和解锁条件 |
| `baby` | 图标，名称，说明 |

“组合”和“可进一步进化”是在同一轮中根据 [圆球配方材料表](../data/BallRecipeEdges.md) 计算得出的——两者都不在任何页面上输入，因此当添加配方时，两者都不会失效。

## 示例

`baby` 只有这一类规模足够小，可以展示在这里——其他两类分别为21行和69行，应该放在…… [圆球](../articles/Balls.md):

```
{{BallTable|class=baby}}
```

## 备注

* 发出 `data-basics` / `data-intermediates` 读取的球过滤脚本属性。
* 要更改一行中的内容，请编辑该球的文章，而不是这个模板。

**分类**　[分类 · 球模板](../categories/Ball_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
