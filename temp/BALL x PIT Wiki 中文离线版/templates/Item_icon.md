# 模板 · 项目图标（Item icon）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Item_icon) · [修订 503](https://ballxpit.wiki.gg/index.php?oldid=503) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Item_icon_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Item_icon/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Item_icon/testcases) 页面上进行实验。 |

#### 总结

使用此模板来显示页面链接旁边的图标。 此模板假设每页都有一个图标上传到特定位置， 即“ 文件: Page Name (Itrom. png ” 。（项目 / Item）

模板参数 此模板更倾向于参数的内嵌格式化。

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 页面名称页名 | `1` `page` | 目标页面的名称。 示例页面名称页名 | 页面名称 | 需要 |
| 链接标签 | `2` `label` | 在链接图标标签上显示要显示的文本。 示例替代页面名称 | 线线 | 可选 |

#### 实例实例实例

举例如下: `File:Mystic Feather (Item).png` 用作一个页面的图标 `Mystic Feather`.

| 《法典法典法典》 | 结果 |
| --- | --- |
| `{{Item icon\|Mystic Feather}}` | [![](../assets/commons--Item_link_example_image.png)](https://ballxpit.wiki.gg/wiki/Mystic_Feather) [神秘羽毛](https://ballxpit.wiki.gg/wiki/Mystic_Feather?action=edit&redlink=1) |
| `{{Item icon\|Mystic Feather\|Mystic Feathers}}` | [![](../assets/commons--Item_link_example_image.png)](https://ballxpit.wiki.gg/wiki/Mystic_Feather) [神秘羽毛](https://ballxpit.wiki.gg/wiki/Mystic_Feather?action=edit&redlink=1) |
| `{{Item icon\|Mystic Feather\|notext}}` | [![](../assets/commons--Item_link_example_image.png)](https://ballxpit.wiki.gg/wiki/Mystic_Feather) |
| `{{Item icon\|Missing Item}}` （错过页面图标 / Missing Page Icon） | [?](https://ballxpit.wiki.gg/wiki/Special:Upload?wpDestFile=Missing_Item_%28Item%29.png) [遗失物品](https://ballxpit.wiki.gg/wiki/Missing_Item?action=edit&redlink=1) |

#### 依赖性

此模板要正常工作， 您需要以下信息:

* 基底 `{{[Link icon](Link_icon.md)}}` 模板。
* 其他 `.link-icon` 和任何相关类别，见 [MediaWiki:Common.css](../site/MediaWiki_Common.css.md).

**分类**　[分类 · 有破损文件链接的页面](../categories/Pages_with_broken_file_links.md) · [分类 · 格式化模板](../categories/Formatting_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
