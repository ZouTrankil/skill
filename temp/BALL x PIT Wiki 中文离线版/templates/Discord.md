# 模板 · Discord

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Discord) · [修订 490](https://ballxpit.wiki.gg/index.php?oldid=490) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Discord_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Discord/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Discord/testcases) 页面上进行实验。 |

此模板允许您使用 [Discoord Contract](https://support.wiki.gg/wiki/DiscordCompact) 或 [Discodoffice](https://support.wiki.gg/wiki/DiscordWidget) 来显示特定 Discod服务器的信息。

[ ]

#### 目录（Contents）

* [1 使用率](#%E4%BD%BF%E7%94%A8%E7%8E%87)
  + [1.1 压缩部件( 默认)](#%E5%8E%8B%E7%BC%A9%E9%83%A8%E4%BB%B6-%E9%BB%98%E8%AE%A4)
  + [1.2 完整部件](#%E5%AE%8C%E6%95%B4%E9%83%A8%E4%BB%B6)
* [2 实例实例实例](#%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B)
* [3 依赖性](#%E4%BE%9D%E8%B5%96%E6%80%A7)
* [4 模板数据](#%E6%A8%A1%E6%9D%BF%E6%95%B0%E6%8D%AE)

#### 使用率

为了能够在您的 Wiki 上显示一个 Discord 服务器部件， 请先去您的 Discord服务器， 并进行以下操作 :

* 打开 `Server Settings`,然后去到 ,,然后去到 ,去到 ,,然后去到 `Engagement` 节内
* 向下滚动到 `Server Widget`.
* 启用部件。
* 复制 `Server ID`.

然后，根据您要使用的部件类型( 精密或完整) , 执行以下操作。

##### 压缩部件( 默认)

主题: [不一致](https://support.wiki.gg/wiki/DiscordCompact)

压缩部件是默认部件。

要使用它，只需将模板添加到服务器 ID 中即可 **初次** 参数或作为 `id` 参数 :

* `{{Discord|serverID}}`
* `{{Discord|id=serverID}}`

##### 完整部件

主题: [不和谐](https://support.wiki.gg/wiki/DiscordWidget)

要使用 Discord 部件的完整版本， 您必须指定 `full=yes` 作为模板参数之一的模板参数, ID 或作为 **初次** 参数或作为 `id` 参数 :

* `{{Discord|serverID|full=yes}}`
* `{{Discord|full=yes|id=serverID}}`

您可以用 `width`、 `height` 和其他参数。请参见“DiscoordWid”的示例部分和完整文档 [维基支持](https://support.wiki.gg/wiki/DiscordWidget).

#### 实例实例实例

| 《法典法典法典》 | 结果 |
| --- | --- |
| `{{Discord\|951501892553424917}}` ／ `{{Discord\|id=951501892553424917}}` |  |
| `{{Discord\|951501892553424917}\|full=yes}` | 如果您看到这个， 您的 JavaScript 可能会被禁用， 或者 Discoord Ingroductor 插件无法工作。 如果后一个插件无效， 请联系wiki 管理员。 |
| `{{Discord\|full=yes \|id = 951501892553424917 \|width = 300px \|height = 500px }}` | 如果您看到这个， 您的 JavaScript 可能会被禁用， 或者 Discoord Ingroductor 插件无法工作。 如果后一个插件无效， 请联系wiki 管理员。 |

#### 依赖性

* 如前所述，契约和元件都要求给定的不一致服务器在其服务器设置中启用部件。
* 契约和部件都要求 `discordTemplate` 工具 :
  + [MediaWiki: Gaddgets/ DiscoordTemplate 介质维基: Gadgets/ discodTemplate](../site/MediaWiki_Gadgets_discordTemplate.md)
  + [MediaWiki:Gadgets/discordTemplate/main.js](../site/MediaWiki_Gadgets_discordTemplate_main.js.md)

#### 模板数据

此模板允许您使用 Discoord Contractact 或 Discocolption 来显示特定 Discoord 服务器的信息。

模板参数 此模板更喜欢参数的块格式化。

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 服务器ID | `1` `id` | Discord 服务器的ID 。 示例951501892553424917 | 线线 | 需要 |
| 使用完整部件 | `full` | 您想要使用完整部件吗 ? 示例是是 | 布尔 | 可选 |
| 宽度( 仅全部件) | `width` | 全部件自定义宽度。 示例300px (英语)。 | 线线 | 可选 |
| 高度( 仅全部件) | `height` | 完整部件的自定义高度。 示例500px (英语)。 | 线线 | 可选 |

**分类**　[分类 · 页面有分歧嵌入式](../categories/Pages_with_Discord_embeds.md) · [分类 · 模板](../categories/Templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
