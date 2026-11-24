# 模板 · Discord/文档（Discord/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Discord%2Fdoc) · [修订 491](https://ballxpit.wiki.gg/index.php?oldid=491) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此模板允许您使用 [DiscordCompact](https://support.wiki.gg/wiki/DiscordCompact) 或 [DiscordWidget](https://support.wiki.gg/wiki/DiscordWidget) 来显示有关特定 Discord 服务器的信息。

## 使用

若要在你的维基上显示 Discord 服务器小部件，请先进入你的 Discord 服务器并执行以下操作：

* 打开 `Server Settings`, 那就去那里。 `Engagement` 章节。
* 向下滚动至 `Server Widget`.
* 启用小部件。
* 复制 `Server ID`.

然后，根据您想要使用的小部件类型（紧凑型或全尺寸型），执行以下操作。

### 紧凑型小部件（默认）

主条目：[DiscordCompact](https://support.wiki.gg/wiki/DiscordCompact)

紧凑型小部件是默认设置。

要使用它，只需将包含服务器ID的模板添加即可。 **首先** 参数或如所述 `id` 参数

* `{{Discord|serverID}}`
* `{{Discord|id=serverID}}`

### 完整小部件

主条目：[DiscordWidget](https://support.wiki.gg/wiki/DiscordWidget)

要使用完整的 Discord 小部件，你必须进行指定。 `full=yes` 作为模板参数之一，其ID可以是 **首先** 参数或如所述 `id` 参数

* `{{Discord|serverID|full=yes}}`
* `{{Discord|full=yes|id=serverID}}`

您可以使用该工具进一步自定义 Widget。 `width`、 `height` 以及其他参数。请参阅示例部分以及 DiscordWidget 的完整文档。 [支持维基](https://support.wiki.gg/wiki/DiscordWidget).

## 示例

| 代码 | 结果 |
| --- | --- |
| `{{Discord\|951501892553424917}}` ／ `{{Discord\|id=951501892553424917}}` |  |
| `{{Discord\|951501892553424917}\|full=yes}` | 如果您看到此提示，可能是您的JavaScript被禁用，或者DiscordIntegrator插件无法正常工作。如果是后者，请联系维基管理员。 |
| `{{Discord\|full=yes \|id = 951501892553424917 \|width = 300px \|height = 500px }}` | 如果您看到此提示，可能是您的JavaScript被禁用，或者DiscordIntegrator插件无法正常工作。如果是后者，请联系维基管理员。 |

## 依赖项

* 如前所述，无论是 Compact 还是 Widget，都要求指定的 Discord 服务器在服务器设置中启用了 Widget。
* Compact和Widget都需要 `discordTemplate` 小工具
  + [MediaWiki:Gadgets/discordTemplate](../site/MediaWiki_Gadgets_discordTemplate.md)
  + [MediaWiki:Gadgets/discordTemplate/main.js](../site/MediaWiki_Gadgets_discordTemplate_main.js.md)

## 模板数据

此模板允许您使用 DiscordCompact 或 DiscordWidget 来显示有关特定 Discord 服务器的信息。

模板参数 此模板更倾向于使用块格式来排列参数。

| 参数 |  | 说明 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 服务器ID | `1` `id` | Discord服务器的ID。 示例951501892553424917 | 线 | 必需 |
| 使用完整小部件 | `full` | 您想使用完整的小部件吗？ 示例是 | 布尔逻辑 | 可选 |
| 宽度（仅适用于完整小部件） | `width` | 为整个小部件设置自定义宽度。 示例300px | 线 | 可选 |
| 身高（仅限完整小部件） | `height` | 为完整小部件设置自定义高度。 示例500px | 线 | 可选 |

**分类**　[分类 · 包含Discord嵌入内容的页面](../categories/Pages_with_Discord_embeds.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
