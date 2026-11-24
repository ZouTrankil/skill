# 模板 · BallTable/文档（BallTable/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallTable%2Fdoc) · [修订 4053](https://ballxpit.wiki.gg/index.php?oldid=4053) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

位于 [圆球](../articles/Balls.md) 上的三张球桌之一，由 [圆球](../data/Balls.md) 货运桌打造而成。

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

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
