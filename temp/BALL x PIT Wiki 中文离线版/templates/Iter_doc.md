# 模板 · Iter/doc(意大利)（Iter/doc）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Iter%2Fdoc) · [修订 506](https://ballxpit.wiki.gg/index.php?oldid=506) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

此模板模板帮助您在表格中创建索引化列( 特别是) [货物](https://support.wiki.gg/wiki/Cargo) 查询)和在使用分析器函数时检索迭代器值 `{{#arraymaptemplate` (与扩展部分(Parser Power on wiki.gg)相混合)。

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

**分类**　[分类 · 模板文档](../categories/Template_documentation.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
