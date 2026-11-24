# 模板 · 球数据/信息箱/doc（BallData/Infobox/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:BallData%2FInfobox%2Fdoc) · [修订 4023](https://ballxpit.wiki.gg/index.php?oldid=4023) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

圆柱文章信息框。 建在 [便携式信息框](https://mediawiki.org/wiki/Extension%3APortableInfobox) 上。

#### 职位安排

**从未被手牵过** {{[球数据](BallData.md)过滤并传递它已经储存的参数的每一个值， 因此信息箱不需任何货物查询。

这是 QQ 的子页[球数据](BallData.md)}}，表示它仅供该页面使用。请在条目的 {{ 中编辑数值。[球数据](BallData.md)打个电话

#### 参数参数

由 {{ 提供[球数据](BallData.md),在这里列出只是为了显示信息框使用的内容。

| 参数 | 调自 |
| --- | --- |
| `description` | `summary` |
| `characters` | `starting_characters`的图标链接 [模块:BallData](../site/Module_BallData.md)然而，仍然有许多——没有固定的空位——没有固定的空位。 然而，仍然有许多——没有固定的空位。 |
| `characters_label` | 或"魅力人" 或"魅力人" |
| `unlocking` | `unlock_condition` |
| `onhit`、 `triggers`、 `status` | 三效果字段 |
| `evolutions` | a 查询——每个配方包括此球的球 |
| `name`、 `image` | 可选; 默认页面名称和 `PageName.png` |

#### 示例

Bleed 的信息箱， 值为 QQ[球数据](BallData.md)会通过。

#### 流血（Bleed）

#### 一般信息

##### 开始的角色

[战士](../articles/The_Warrior.md) [![The Warrior.png](../assets/The_Warrior.png)](../articles/The_Warrior.md)
[伪救世主](../articles/The_False_Messiah.md) [![The False Messiah.png](../assets/The_False_Messiah.png)](../articles/The_False_Messiah.md)

##### 解锁

默认解锁

##### 状态效果（Status Effects）

[流血](https://ballxpit.wiki.gg/wiki/Status_Effects?action=edit&redlink=1)

##### 由于状态影响

命中时

#### 发展情况（Evolutions）

##### 演变为

[贝尔塞克](../articles/Berserk.md) [![Berserk.png](../assets/Berserk.png)](../articles/Berserk.md)
[输血](../articles/Hemorrhage.md) [![Hemorrhage.png](../assets/Hemorrhage.png)](../articles/Hemorrhage.md)
[李克](../articles/Leech.md) [![Leech.png](../assets/Leech.png)](../articles/Leech.md)
[牺牲](../articles/Sacrifice.md) [![Sacrifice.png](../assets/Sacrifice.png)](../articles/Sacrifice.md)
[吸血鬼主](../articles/Vampire_Lord.md) [![Vampire Lord.png](../assets/Vampire_Lord.png)](../articles/Vampire_Lord.md)

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

在你写的文章上,[球数据](BallData.md)填满每个字段,
`evolutions` 来源于查询而不是被输入。

#### 备注

* 在此注意到图像丢失吗 ? 它是由 \_ pageName 参数生成的。 如果此信息框被放在 [https://ballxpit.wiki.gg/wiki/Bleed](../articles/Bleed.md) 页面上， 那么

[![Bleed.png](../assets/Bleed.png)](../files/Bleed.png.md)
仅显示在一般信息部分上方。

* 其他 `evolutions` 从不键入行。 烧灼是十个球的成分， 并且没有列出其中任何一个; 添加一个第十一进化的球， 自动更新 Burn 的信息箱。
* `type="Ball"` 在 XML 中, XML 是便携式信息框主题键，而不是页面名称。它会保留 `Ball`.
* 类别来自 QQ[球数据](BallData.md)*,以 `ball_class` -不是从这里

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
