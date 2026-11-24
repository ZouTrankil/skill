# 模板 · 圆球配方材料（BallRecipeEdge）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallRecipeEdge) · [修订 4041](https://ballxpit.wiki.gg/index.php?oldid=4041) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](BallRecipeEdge_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:BallRecipeEdge/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:BallRecipeEdge/testcases)页面上进行实验。 |

进化配方中一个槽位内的另一种成分。作为一行数据存储在 [圆球配方材料表](../data/BallRecipeEdges.md) 中，且不显示任何内容。

[ ]

## 目录（Contents）

* [1 放置方式](#%E6%94%BE%E7%BD%AE%E6%96%B9%E5%BC%8F)
* [2 参数](#%E5%8F%82%E6%95%B0)
* [3 写入的数据](#%E5%86%99%E5%85%A5%E7%9A%84%E6%95%B0%E6%8D%AE)
* [4 此处省略运行示例的原因](#%E6%AD%A4%E5%A4%84%E7%9C%81%E7%95%A5%E8%BF%90%E8%A1%8C%E7%A4%BA%E4%BE%8B%E7%9A%84%E5%8E%9F%E5%9B%A0)

## 放置方式

**从未手动放置过。** [Module:BallData](../site/Module_BallData.md) 会为每个选项展开一次调用，
数据来自同一页面上 {{[球数据](BallData.md)}} 的 `ingredient_N_options` 参数。

自己输入内容会生成一份已存储的配方的手写副本，而这份副本可能会与上方的内容不一致。请改在 {{[BallData](BallData.md)}} 上编辑该配方。

## 参数

| 参数 | 含义 |
| --- | --- |
| `slot_index` | 1–4. 共享同一槽位的行是 **替代选项**；不同的槽位则是 **共同成分**。 |
| `ingredient` | 另一个圆球的页面标题。别名从不显示。 |

结果是存储该行的页面，所以没有 `result`
参数。

## 写入的数据

辐射束是 *(激光 H 或激光 V) + (中毒或细胞)*，共四行：

| slot\_index | 材料 |
| --- | --- |
| 1 | 激光（水平 / Horizontal） |
| 1 | 激光（垂直 / Vertical） |
| 2 | 中毒 |
| 2 | 细胞 |

## 此处省略运行示例的原因

此模板用于写入 Cargo，采用生成方式而非手动输入。在此处渲染会违反 *Template:BallRecipeEdge/doc* 的规范。如需查看真实的配方边数据，请打开 [Special:CargoTables/BallRecipeEdges](../data/BallRecipeEdges.md)。

**分类**　[分类 · 球模板](../categories/Ball_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
