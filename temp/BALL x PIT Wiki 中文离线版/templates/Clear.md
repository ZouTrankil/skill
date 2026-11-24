# 模板 · 清除（Clear）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Clear) · [修订 381](https://ballxpit.wiki.gg/index.php?oldid=381) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Clear_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Clear/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Clear/testcases)页面上进行实验。 |

说明

此模板允许您清除页面的左侧、右侧或两侧。清除意味着，在指定侧面的现有内容（例如悬挂或浮动的图片或块）完全显示之前，模板后的内容将不会显示。此模板通常用于防止文本在不相关的图片周围流动。

模板在页面中添加以下代码： `<div style="clear:left/right/both;"></div>` （数值后 `clear` 取决于参数）。此代码会影响具有 CSS 属性的元素。 `float`，包括被放到一边的文件（例如， `[[File:Image.png|right]]`).

语法

- 清除两侧浮动，使用 `{{Clear}}`。
- 只清除左侧浮动，使用 `{{Clear|left}}`。
- 只清除右侧浮动，使用 `{{Clear|right}}`。

也可用 [简写](#%E6%A8%A1%E6%9D%BF--%E6%B8%85%E9%99%A4clear) `{{-}}` 代替 `{{Clear}}`。

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

这段代码产生以下结果：

---

### 第1节

[![Example.jpg](../assets/commons--Example.jpg)](../files/Example.jpg.md)

第1节文本。

### 第2节

第2节文本。

### 第3节

第3节文本。

---

如上所示，第1节中添加的示例图片显示在右侧，并向下延伸至第2节，而{{清除}}模板则位于第二节的末尾，导致示例图片并未紧邻第3节。因此，{{清除}}模板的一个用途就是控制哪些元素应显示在哪些元素的旁边。

## 另见

* [CSS属性 `clear` 在 MDN 上](https://developer.mozilla.org/en-US/docs/Web/CSS/clear)
* [CSS属性 `float` 在 MDN 上](https://developer.mozilla.org/en-US/docs/Web/CSS/float)

**分类**　[分类 · 通用维基模板](../categories/General_wiki_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
