# 模板 · 球数据/信息框（BallData/Infobox）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallData%2FInfobox) · [修订 4071](https://ballxpit.wiki.gg/index.php?oldid=4071) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](BallData_Infobox_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:BallData/Infobox/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:BallData/Infobox/testcases)页面上进行实验。 |

球类物品信息框。基于 [PortableInfobox](https://mediawiki.org/wiki/Extension%3APortableInfobox) 构建。

[ ]

## 目录（Contents）

* [1 放置方式](#%E6%94%BE%E7%BD%AE%E6%96%B9%E5%BC%8F)
* [2 参数](#%E5%8F%82%E6%95%B0)
* [3 示例](#%E7%A4%BA%E4%BE%8B)
* [4 备注](#%E5%A4%87%E6%B3%A8)

## 放置方式

**从未手动放置过。** {{[BallData](BallData.md)}} 会跳过它，并将参数中已存储的所有值传递过去，因此信息框不会消耗任何Cargo 查询。

这是{{[BallData](BallData.md)}}的子页面，旨在将其设为私有。请编辑文章中的{{[BallData](BallData.md)}}调用值。

## 参数

由 {{[BallData](BallData.md)}} 提供，此处列出仅用于展示信息框中使用的内容。

| 参数 | 从 |
| --- | --- |
| `description` | `summary` |
| `characters` | `starting_characters`，以图标链接的形式呈现 [Module:BallData](../site/Module_BallData.md). 无论有多少——都没有固定的位置。 |
| `characters_label` | “角色”或“角色”，按数量统计 |
| `unlocking` | `unlock_condition` |
| `onhit`、 `triggers`、 `status` | 三个效果领域 |
| `evolutions` | 一个查询——任何配方中包含此成分的球 |
| `name`、 `image` | 可选；默认使用页面名称。 `PageName.png` |

## 示例

流血的信息框，包含值 {{[BallData](BallData.md)}} 将会传递。

## 流血（Bleed）

## 基本信息

### 初始角色（Starting Characters）

[战士](../articles/The_Warrior.md) [![The Warrior.png](../assets/previews/The_Warrior-25px-94d3a92b.png)](../articles/The_Warrior.md)
[伪救世主](../articles/The_False_Messiah.md) [![The False Messiah.png](../assets/previews/The_False_Messiah-25px-a9c0c9f7.png)](../articles/The_False_Messiah.md)

### 解锁

默认解锁

### 状态效果（Status Effects）

[流血](https://ballxpit.wiki.gg/wiki/Status_Effects?action=edit&redlink=1)

### 由状态效果触发

命中时

## 进化（Evolutions）

### 进化成

[狂暴](../articles/Berserk.md) [![Berserk.png](../assets/Berserk.png)](../articles/Berserk.md)
[大出血](../articles/Hemorrhage.md) [![Hemorrhage.png](../assets/Hemorrhage.png)](../articles/Hemorrhage.md)
[水蛭](../articles/Leech.md) [![Leech.png](../assets/Leech.png)](../articles/Leech.md)
[献祭](../articles/Sacrifice.md) [![Sacrifice.png](../assets/Sacrifice.png)](../articles/Sacrifice.md)
[吸血鬼领主](../articles/Vampire_Lord.md) [![Vampire Lord.png](../assets/Vampire_Lord.png)](../articles/Vampire_Lord.md)

```
{{BallData/Infobox
|name         = Bleed
|description  = Inflicts 2 stacks of bleed. Bleeding enemies receive 1 damage per stack when hit by a ball (max 8 stacks).
|characters   = {{#invoke:BallData|charactersList|The Warrior, The False Messiah}}
|characters_label = {{#invoke:BallData|charactersLabel|The Warrior, The False Messiah}}
|unlocking    = Unlocked by default
|triggers     = On-Hit
|status       = Bleed
|evolutions   = {{BallLink|Berserk}}<br>...
}}
```

在真实的文章里，不会出现这些内容——{{[球数据](BallData.md)}} 填充了每一个字段，并且
`evolutions` 不是通过输入文字，而是通过查询得到的。

## 备注

* 发现这里图片缺失了吗？这是由 \_pageName 参数生成的。如果此信息框位于 [https://ballxpit.wiki.gg/wiki/Bleed](../articles/Bleed.md) 页面上，那么

[![Bleed.png](../assets/Bleed.png)](../files/Bleed.png.md) 将出现在“General information”部分的正上方。

* `evolutions` row 从未被输入过。Burn 是十个球中的一种成分，它不指定任何球名；添加第十一颗进化球时，Burn 的信息框会自动更新。
* `type="Ball"` 在 XML 中是指 PortableInfobox 主题键，而不是页面名称。它保持不变。 `Ball`.
* 类别来自{{[球数据](BallData.md)}}, 以...为关键 `ball_class` — 不是来自这里。

**分类**　[分类 · 信息框模板](../categories/Infobox_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
