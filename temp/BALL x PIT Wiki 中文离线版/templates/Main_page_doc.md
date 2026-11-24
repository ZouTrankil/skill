# 模板 · 主页/文档（Main page/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Main_page%2Fdoc) · [修订 555](https://ballxpit.wiki.gg/index.php?oldid=555) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

![](../assets/commons--Lua.svg)

本模板使用用Lua编程语言撰写的一个或多个模块。

详情见 [维基百科:](https://en.wikipedia.org/wiki/Wikipedia%3ALua) 或是 [关于媒体wiki.org的Lua参考手册](https://mediawiki.org/wiki/Extension%3AScribunto/Lua_reference_manual)所使用的模块包括: **[主页](../site/Module_Main_page.md)**.

此模板用于创建 IMP 主页。 它使用 [模块: main page](../site/Module_Main_page.md) 来安排一系列 [Template:Main pagebox](Main_page_box.md) 在 [CSS 网格](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_grid_layout) 中。

#### 简单解释

版式使用网格排列的关键词。 此网格在桌面宽屏幕上有3列， 在平板电脑上有2列， 在移动屏幕上有1列。 每列可以任意多行。 每个关键词代表相同的区域， 可以跨多行和/或列， 但是 *必须* 形成任何维的毗连矩形(1x1, 1x2, 2x2, 2X3等)。

例如，对桌面的以下输入:

```
welcome welcome welcome
about links links
about contribute contribute
```

将产生一个类似以下内容的网格:

|  |  |  |
| --- | --- | --- |
| 欢迎欢迎欢迎 | 欢迎欢迎欢迎 | 欢迎欢迎欢迎 |
| 约约 | 链接链接 | 链接链接 |
| 约约 | 捐款 | 捐款 |

何处 `welcome` 是 [欢迎来到百科](../articles/BALL_x_PIT_Wiki_welcome.md)、 `about` 是 [游戏简介](../articles/BALL_x_PIT_Wiki_about.md)例如，等等，等等。 [模板:主页框](Main_page_box.md) 用于创建您自己的框的更多信息。

如果您输入的关键字没有对应的框， 在保存或预览页面时会提示您创建关键字。

如果您将某个关键字从某个布局中留出， 它将不会显示在该布局上。 如果这是意外的， 将会在编辑预览的顶部发出警告， 但是如果是故意的， 可以安全地忽略。

更多信息，请见您主页上的评论或询问 wiki.gg 工作人员求助。

#### 技术性解释

对于CSS Savvy, 本节解释它是如何工作的有点在引擎盖下。

桌面、平板和移动创建的输入 [CSS 变数](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) 然后用作 [网格板块区域](https://developer.mozilla.org/en-US/docs/Web/CSS/grid-template-areas) 在媒体查询屏幕宽度的QQ1350px、XQ990px和<990px。根据它们的子页面名称给框一个ID,然后由模块用来找到模板，以及由框模板来指定一个 CSS ID 。 `mp-box-<keyword>`由于这些关键字在网格布局中直接使用，因此这些关键字必须遵循 [< 海关识别>](https://developer.mozilla.org/en-US/docs/Web/CSS/custom-ident) 命名。

#### 依赖性

此模板要正常工作， 您需要以下信息:

* [模块:主页](../site/Module_Main_page.md)
* [分类:主页模板](../categories/Main_page_templates.md) 中的所有模板。
* 在 [MediaWiki:Common.cs](../site/MediaWiki_Common.css.md)中找到的“主页面布局”部分内的所有 CSS 。

其他 `[mpEditLinks](../site/MediaWiki_Gadgets_mpEditLinks.md)` 也高度推荐使用该技术。 [MediaWiki:Gadgets/mpEditLinks/main.css](../site/MediaWiki_Gadgets_mpEditLinks_main.css.md) 及 [MediaWiki:Gadgets/mpEditLinks/main.js](../site/MediaWiki_Gadgets_mpEditLinks_main.js.md).

#### 模板数据

创建 IMP 主页。

模板参数 此模板更喜欢参数的块格式化。

| 参数 |  | 描述 | 类型 | 状态 |
| --- | --- | --- | --- | --- |
| 桌面 | `desktop` | 宽屏幕布局 | 字符串字符串 | 需要 |
| 表格表格 | `tablet` | 中宽屏幕的布局 | 字符串字符串 | 需要 |
| 流动移动 | `mobile` | 窄屏幕的布局 | 字符串字符串 | 需要 |

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
