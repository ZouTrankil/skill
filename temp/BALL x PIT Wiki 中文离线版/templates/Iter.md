# 模板 · 其他（Iter）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Iter) · [修订 505](https://ballxpit.wiki.gg/index.php?oldid=505) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Iter_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Iter/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Iter/testcases) 页面上进行实验。 |

此模板模板帮助您在表格中创建索引化列( 特别是) [货物](https://support.wiki.gg/wiki/Cargo) 查询)和在使用分析器函数时检索迭代器值 `{{#arraymaptemplate` (与扩展部分(Parser Power on wiki.gg)相混合)。

[ ]

#### 目录（Contents）

* [1 简单计数](#%E7%AE%80%E5%8D%95%E8%AE%A1%E6%95%B0)
* [2 重置柜台](#%E9%87%8D%E7%BD%AE%E6%9F%9C%E5%8F%B0)
* [3 多个计数器](#%E5%A4%9A%E4%B8%AA%E8%AE%A1%E6%95%B0%E5%99%A8)
* [4 获取值而不加量](#%E8%8E%B7%E5%8F%96%E5%80%BC%E8%80%8C%E4%B8%8D%E5%8A%A0%E9%87%8F)

#### 简单计数

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

#### 重置柜台

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

#### 多个计数器

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

#### 获取值而不加量

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
