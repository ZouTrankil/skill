# 模板 · 迭代（Iter）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Iter) · [修订 505](https://ballxpit.wiki.gg/index.php?oldid=505) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Iter_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Iter/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Iter/testcases)页面上进行实验。 |

此模板有助于您在表格中创建索引列（特别是 [Cargo](https://support.wiki.gg/wiki/Cargo) 查询) 并在使用解析函数时检索迭代器值 `{{#arraymaptemplate` （与 Extension:ParserPower 捆绑在 wiki.gg 上）。

[ ]

## 目录（Contents）

* [1 简单计数](#%E7%AE%80%E5%8D%95%E8%AE%A1%E6%95%B0)
* [2 重置计数器](#%E9%87%8D%E7%BD%AE%E8%AE%A1%E6%95%B0%E5%99%A8)
* [3 多个计数器](#%E5%A4%9A%E4%B8%AA%E8%AE%A1%E6%95%B0%E5%99%A8)
* [4 获取价值而不增加数值](#%E8%8E%B7%E5%8F%96%E4%BB%B7%E5%80%BC%E8%80%8C%E4%B8%8D%E5%A2%9E%E5%8A%A0%E6%95%B0%E5%80%BC)

## 简单计数

```
* {{iter|}}
* {{iter|}}
* {{iter|}}
* {{iter|}}
```

* 1
* 2
* 3
* 4

## 重置计数器

```
* {{iter|reset=yes}}
* {{iter|}}
* {{iter|reset=yes}}
* {{iter|}}
```

* 1
* 2
* 1
* 2

## 多个计数器

```
* {{iter|key1}}
* {{iter|key2}}
* {{iter|key2}}
* {{iter|key1}}
```

* 1
* 1
* 2
* 2

## 获取价值而不增加数值

```
* {{iter|reset=yes}}
* {{iter|}}
* {{iter|}}
* {{iter|get=yes}}
```

* 1
* 2
* 3
* 3

**分类**　[分类 · 模板](../categories/Templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
