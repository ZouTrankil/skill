# 模板 · 圆球配方材料/文档（BallRecipeEdge/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallRecipeEdge%2Fdoc) · [修订 4042](https://ballxpit.wiki.gg/index.php?oldid=4042) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

进化配方中一个槽位内的另一种成分。作为一行数据存储在 [圆球配方材料表](../data/BallRecipeEdges.md) 中，且不显示任何内容。

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

此模板用于写入 Cargo，由生成器自动生成而非手动输入。在此处渲染会违反 *Template:BallRecipeEdge/doc* 的规范。要查看真实的配方边数据，请打开 [Special:CargoTables/BallRecipeEdges](../data/BallRecipeEdges.md)。

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
