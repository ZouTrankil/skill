# 模板 · MessageBox

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:MessageBox) · [修订 388](https://ballxpit.wiki.gg/index.php?oldid=388) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](MessageBox_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:MessageBox/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:MessageBox/testcases)页面上进行实验。 |

{{MessageBox}} 是一个用于创建消息框的模板。

它可以通过职业、内联样式以及提供的 CSS 选择器进行高度定制。还提供了可选功能，如图片、左边界、右侧文本（例如快捷方式）以及取消功能。

它使用了 [Lua 模板语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1)，更多相关信息可以在 [Global Lua Module 页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Mbox?action=edit&redlink=1)找到。此版本经过修改，采用了基于 [模块中的基础样式](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3Amediawiki%3AGlobal_Lua_Modules/Mbox.css?action=edit&redlink=1)的起始样式。若要充分利用该模块的功能并去除默认样式，请移除 [Module:Mbox](../site/Module_Mbox.md)中指定的部分内容。

**如需此模板的传统 Wikitext 版本，请参阅 [Ambox on Templates Wiki](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3AAmbox?action=edit&redlink=1)**。

[ ]

## 目录（Contents）

* [1 参数](#%E5%8F%82%E6%95%B0)
* [2 设计](#%E8%AE%BE%E8%AE%A1)
* [3 示例](#%E7%A4%BA%E4%BE%8B)
  + [3.1 基础信息框](#%E5%9F%BA%E7%A1%80%E4%BF%A1%E6%81%AF%E6%A1%86)
  + [3.2 使用类型](#%E4%BD%BF%E7%94%A8%E7%B1%BB%E5%9E%8B)
  + [3.3 带有图片](#%E5%B8%A6%E6%9C%89%E5%9B%BE%E7%89%87)
  + [3.4 附带说明](#%E9%99%84%E5%B8%A6%E8%AF%B4%E6%98%8E)
  + [3.5 标准/默认风格](#%E6%A0%87%E5%87%86%E9%BB%98%E8%AE%A4%E9%A3%8E%E6%A0%BC)

## 参数

关于如何使用这些参数的示例，请参阅 [#Examples](#%E7%A4%BA%E4%BE%8B)。

| 参数名称 | 说明 | 是否必填 | 默认 |
| --- | --- | --- | --- |
| `class` | 对根类添加额外类别 `.mbox` 元素。 | 否 | — |
| `bordercolor` | 最左侧粗边框的颜色。 | 否 | 默认战术表 |
| `type` | 如 CSS 中所述，使用变量声明 mbox 的类型。影响最左侧粗边框的颜色。参见 [#使用类型](#%E4%BD%BF%E7%94%A8%E7%B1%BB%E5%9E%8B)。 | 否 | — |
| `bgcolor` | mbox背景的颜色。 | 否 | 默认战术表 |
| `style` | 为根元素添加额外的内联样式 `.mbox` 元素。 | 否 | — |
| `image` | 需要添加在所有文本内容左侧的图像。 | 否 | — |
| `imagewidth` | 图像宽度（高度会自动调整）。 | 否 | `60px` |
| `imagelink` | 图片指向的链接（例如，可以链接到相关的维护分类）。如果未包含此链接，图片将无法点击。 | 否 | — |
| `header` | 标题（位于顶部的加粗文本）。通常用于非常简短地解释 mbox 的主题，因为当 mbox 关闭时，只有标题会显示出来。 | 否 | — |
| `text` | 标题下方放置的“NonBold”文本，通常用于进一步详细说明 mbox 的主题。当 mbox 关闭时，此文本将隐藏。 | 否 | — |
| `comment` | 主文本下方有较小的非加粗文本，通常用于添加关于通知的额外链接或背景信息。当 mbox 关闭时，此文本将被隐藏。 | 否 | — |
| `aside` | 右侧小区域内放置的文本被浅灰色边框分隔，通常用于显示相关页面的快捷链接（例如政策页面）。当 mbox 关闭时，此文本将隐藏。 | 否 | — |
| `id` | 默认情况下，关闭按钮会关闭页面上的所有mbox。但是，若要更改此设置，可以使用此参数，其名称应为mbox实现的名称（例如，“Template:Cleanup”）。 `\|id=cleanup`). | 否 | — |
| `collapsed` | 默认情况下，mboxbox将保持展开状态，并显示全部内容。但是，若要更改此设置，可以使用该参数将mboxbox设置为默认展开状态（例如： `\|collapsed=true` 将默认情况下使 mbox 折叠。 | 否 | — |

## 设计

某些社区可能希望自定义 mbox 的外观。最常见的样式选项在 CSS 中有所说明。

```
.mbox {
    /* the background of the entire box */;
    background-color: ;

    /* the border color of the entire box */
    border-color: ;

    /* the border thickness of the entire box */
    border-width: ;

    /* the default thick left border color; note this can be changed from within the template implementations using the "color" parameter */
    border-left-color: ;

    /* the rounded-ness of the corners */;
    border-radius: ;

    /* the baseline font-size of the mbox */
    font-size: ;
}

.mbox__content {
    /* the padding inside the mbox */
    padding: ;
}

.mbox__content__image {
    /* the minimum width of the mbox's image (if bigger, use the "imagewidth" parameter in the template) */
    width: ;

    /* the spacing to the left of the text (i.e., the right of the image) */
    padding-right: ;
}

.mbox__content__text__comment {
    /* the size of the text in the "comment" parameter */
    font-size: ;
}

.mbox__content__aside {
    /* any particular modifications to the "aside" area can go here */

    /* the maximum width of the aside area */
    width: ;
}

.mbox__close {
    /* the appearance of the close symbol here */
}

.mbox__close:after {
    /* overwrite "content" here if you do not wish for the close symbol to be × */
    content: '';
}

.mw-collapsed + .mbox__close {
   /* modifications to the close symbol when the box is closed */
}

.mw-collapsed + .mbox__close:after {
   /* overwrite "content" here if you do not wish for the close symbol to be + when the box is closed */
   content: '';
}
```

技术说明

* 为根元素添加额外的内联样式 `.mbox` 可以通过该方式获得元素。 `style` 模板中的参数。

## 示例

### 基础信息框

```
{{MessageBox
|header      = Header text here
|text        = Normal text here
|id          = test1
}}
```

显示效果

标题文本此处

普通文本在此

### 使用类型

要使用类型，必须添加 CSS 变量，例如：

```
:root {
    --type-important: rgba(200, 0, 0, 0.8);
    --type-moderate: rgba(233, 124, 47, 0.8);
    --type-minor: rgba(241, 197, 37, 0.8);
}
```

如果添加：

```
{{MessageBox
|header = Header text here
|type   = important
|text   = Normal text here
|id     = test2
}}
```

显示效果

标题文本此处

普通文本在此

根据你的造型，在上述示例中可能不会有视觉上的差异。

### 带有图片

```
{{MessageBox
|header     = Header text here
|text       = Normal text here
|image      = Wiki.png
|imagelink  =
|imagewidth = 50px
|id         = test3
}}
```

显示效果

[File:Wiki.png](https://ballxpit.wiki.gg/wiki/Special%3AUpload?wpDestFile=Wiki.png)

标题文本此处

普通文本在此

### 附带说明

```
{{MessageBox
|header = Header text here
|type   = important
|text   = Normal text here
|aside  = Aside text here
|id     = test4
}}
```

显示效果

标题文本此处

普通文本在此

此处为旁白文本

### 标准/默认风格

```
{{MessageBox
|header  = Header text here
|text    = Normal text here
|comment = Comment text here
|image   = Wiki.png
|aside   = Aside text here
|id      = standard
}}
```

显示效果

[File:Wiki.png](https://ballxpit.wiki.gg/wiki/Special%3AUpload?wpDestFile=Wiki.png)

标题文本此处

普通文本在此

在此处输入评论文本

此处为旁白文本

**分类**　[分类 · 文件链接失效的页面](../categories/Pages_with_broken_file_links.md) · [分类 · 注意模板](../categories/Notice_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
