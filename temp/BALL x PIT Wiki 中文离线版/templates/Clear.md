# 模板 · 清晰（Clear）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Clear) · [修订 381](https://ballxpit.wiki.gg/index.php?oldid=381) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Clear_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Clear/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Clear/testcases) 页面上进行实验。 |

描述

此模板允许您清除页面的左侧、 右侧或两侧。清除意指在完全显示指定边上的现有内容(例如“挂接”或浮动图像或区块)之前，模板之后的内容不会显示。此模板经常被使用， 以便文本不会围绕不相干图像流动。

该模板在页面中添加以下代码: `<div style="clear:left/right/both;"></div>` (数值在 `clear` 此代码影响 CSS 属性的元素 `float`,包括漂浮到侧面的文件(例如, `[[File:Image.png|right]]`).

语法

* 为了清除页面的两边，请添加代码清晰}}.
* 要清除页面左侧，请添加代码 QQ清晰|*左侧*}}.
* 仅清除页面右侧，请添加代码QQ清晰|*< 右侧>*}}.

您也可以使用 QQ 语句[-](#%E6%A8%A1%E6%9D%BF--%E6%B8%85%E6%99%B0clear)而不是。..清晰* 作为此模板的速记电话。

示例

```
=== Section 1 ===
[[File:Example.jpg|200px|right]]
Section 1 text.

=== Section 2 ===
Section 2 text.
{{Clear|right}}

=== Section 3 ===
Section 3 text.
```

该代码产生以下结果:

---

##### 第1节

[![Example.jpg](../assets/commons--Example.jpg)](../files/Example.jpg.md)

第1节案文。

##### 第2节

第2节案文。

##### 第3节

第3节案文。

---

如上所示，第1节中添加的示例图像显示在右侧，并通过第2节向下延伸，而QQ则向下延伸。清晰在第二部分结尾处调用模板，导致示例图像不在第3节旁边。清晰模板用于控制在其它元素旁边显示的元素。

#### 另见

* [CSS 财产 `clear` 在 MDN 上](https://developer.mozilla.org/en-US/docs/Web/CSS/clear)
* [CSS 财产 `float` 在 MDN 上](https://developer.mozilla.org/en-US/docs/Web/CSS/float)

**分类**　[分类 · 一般维基模板](../categories/General_wiki_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
