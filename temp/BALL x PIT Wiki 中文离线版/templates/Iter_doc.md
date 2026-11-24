# 模板 · 迭代/文档（Iter/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Iter%2Fdoc) · [修订 506](https://ballxpit.wiki.gg/index.php?oldid=506) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此模板有助于您在表格中创建索引列（特别是 [Cargo](https://support.wiki.gg/wiki/Cargo) 查询) 并在使用解析函数时检索迭代器值 `{{#arraymaptemplate` （与 Extension:ParserPower 捆绑在 wiki.gg 上）。

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

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
