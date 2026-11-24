# 模板 · 信息框（MessageBox）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:MessageBox) · [修订 388](https://ballxpit.wiki.gg/index.php?oldid=388) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](MessageBox_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:MessageBox/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:MessageBox/testcases) 页面上进行实验。 |

{{信息框\\ 是一个创建信息框的模板。

它高度定制以类、内嵌样式，并提供 CSS 选择器。 选用功能， 如图像、 左边框、 右侧文字( 例如快捷键) 和卸载函数。

它使用 [Lua 临时语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1),可以找到更多信息 [全球卢亚模块页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Mbox?action=edit&redlink=1)。此版本被修改后产生基于 [模块的基本样式](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3Amediawiki%3AGlobal_Lua_Modules/Mbox.css?action=edit&redlink=1)。要使用本模块的全部功能，并删除默认的外观样式，请删除 [模块:Mbox](../site/Module_Mbox.md).

**此模板的传统维基文本版本见 [模板的 Ambox 维基](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3AAmbox?action=edit&redlink=1)**.

[ ]

#### 目录（Contents）

* [1 参数参数](#%E5%8F%82%E6%95%B0%E5%8F%82%E6%95%B0)
* [2 设计](#%E8%AE%BE%E8%AE%A1)
* [3 实例实例实例](#%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B)
  + [3.1 基本消息框](#%E5%9F%BA%E6%9C%AC%E6%B6%88%E6%81%AF%E6%A1%86)
  + [3.2 使用类型](#%E4%BD%BF%E7%94%A8%E7%B1%BB%E5%9E%8B)
  + [3.3 带有图像](#%E5%B8%A6%E6%9C%89%E5%9B%BE%E5%83%8F)
  + [3.4 与一旁](#%E4%B8%8E%E4%B8%80%E6%97%81)
  + [3.5 标准/ 默认样式](#%E6%A0%87%E5%87%86-%E9%BB%98%E8%AE%A4%E6%A0%B7%E5%BC%8F)

#### 参数参数

关于如何使用这些参数的例子，请参见 [Examples](#%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B)。

| 参数名称 | 描述 | 需要吗? | 默认默认 |
| --- | --- | --- | --- |
| `class` | 根根上的额外类 `.mbox` 元素。 | 没有。 | — |
| `bordercolor` | 厚厚左最左边框的颜色。 | 没有。 | 样式表默认默认 |
| `type` | 在 CSS 中声明的带有变量的 mbox 类型类型。 影响最左最左边框的颜色。 见 [# 用户类型](#%E4%BD%BF%E7%94%A8%E7%B1%BB%E5%9E%8B). | 没有。 | — |
| `bgcolor` | 信箱背景的颜色。 | 没有。 | 样式表默认默认 |
| `style` | root 的附加内线样式 `.mbox` 元素。 | 没有。 | — |
| `image` | 要添加到所有文本内容左侧的图像。 | 没有。 | — |
| `imagewidth` | 图像的宽度( 高度自动调整) 。 | 没有。 | `60px` |
| `imagelink` | 图像点( 可链接到相关维护类别， 以实例为准) 的链接。 如果不包含， 图像将无法单击。 | 没有。 | — |
| `header` | 信头( 粗体文字放在顶部) 。 这通常用来非常简短地解释 mbox 本身的主题， 因为当 mbox 关闭时， 只有信头会显示。 | 没有。 | — |
| `text` | 放在信头下方的非粗体文字，通常用于进一步解释或解释邮箱主题的细节。当邮箱关闭时，此文字将被隐藏。 | 没有。 | — |
| `comment` | 放在主文本下方的小非粗体非粗体文字，通常用于添加关于通知的额外链接或上下文。当关闭了 mbox 时，此文字将被隐藏。 | 没有。 | — |
| `aside` | 文本放在右侧的小部分分配中， 以浅灰色边框分隔。 最常用的文本是显示有关页面的快捷键( 如政策页面上)。 当 mbox 关闭时， 此文本将被隐藏。 | 没有。 | — |
| `id` | 默认情况下， 一个关闭按钮将关闭页面上的所有 mboxes 。 但是， 要更改此选项， 可以使用此参数， 以执行 mbox 的名称( 例如“ Template: Cleanup ” ) `\|id=cleanup`). | 没有。 | — |
| `collapsed` | 默认情况下, mbox 将被解封， 并且将显示全部内容。 但是， 要更改此选项， 此参数可用于将 mbox 设置为默认的崩溃( 例如 , ) 。 `\|collapsed=true` 将会设置默认时要崩溃的存储器) 。 | 没有。 | — |

#### 设计

有些社区可能希望定制模箱的外观，最常用的配方选项见于CSS。

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

* root 的附加内线样式 `.mbox` 可以通过 `style` 模板中的参数。

#### 实例实例实例

##### 基本消息框

```
{{MessageBox
|header      = Header text here
|text        = Normal text here
|id          = test1
}}
```

生产:

这里的页眉文字

这里的普通文本

##### 使用类型

使用类型时，必须添加 CSS 变量，例如:

```
:root {
    --type-important: rgba(200, 0, 0, 0.8);
    --type-moderate: rgba(233, 124, 47, 0.8);
    --type-minor: rgba(241, 197, 37, 0.8);
}
```

如果加上:

```
{{MessageBox
|header = Header text here
|type   = important
|text   = Normal text here
|id     = test2
}}
```

生产:

这里的页眉文字

这里的普通文本

视你的型号而定，上述例子中可能不存在视觉差异。

##### 带有图像

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

生产:

[File:Wiki.png](https://ballxpit.wiki.gg/wiki/Special%3AUpload?wpDestFile=Wiki.png)

这里的页眉文字

这里的普通文本

##### 与一旁

```
{{MessageBox
|header = Header text here
|type   = important
|text   = Normal text here
|aside  = Aside text here
|id     = test4
}}
```

生产:

这里的页眉文字

这里的普通文本

在此附加文字文本

##### 标准/ 默认样式

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

生产:

[File:Wiki.png](https://ballxpit.wiki.gg/wiki/Special%3AUpload?wpDestFile=Wiki.png)

这里的页眉文字

这里的普通文本

这里的注释文字

在此附加文字文本

**分类**　[分类 · 有破损文件链接的页面](../categories/Pages_with_broken_file_links.md) · [分类 · 通知模板](../categories/Notice_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
