# 模板 · 引用网页（Cite web）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Cite_web) · [修订 301](https://ballxpit.wiki.gg/index.php?oldid=301) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Cite_web_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Cite_web/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Cite_web/testcases)页面上进行实验。 |

此模板用于在维基百科中[引用来源](https://en.wikipedia.org/wiki/WP%3ACITE)，专用于非新闻来源的网站。该模板取代了已废弃的[Template:Web reference](https://en.wikipedia.org/wiki/Template%3AWeb_reference)。它仅支持小写参数。

关于在维基百科文章中使用模板添加开源网络内容引用的一般讨论，可参阅 [引用模板](https://en.wikipedia.org/wiki/Citation_templates)。

本页面使用了来自 [Wookieepedia](https://ballxpit.wiki.gg/wiki/W%3Ac%3AWookieepedia%3ATemplate%3ACite_web?action=edit&redlink=1) 的 [Creative Commons 许可](https://ballxpit.wiki.gg/wiki/W%3AWikia%3ALicensing?action=edit&redlink=1) 内容。

## 使用

当页面作者身份不太明确时（当前日期）的常见形式

{{Cite web |url= |title= |accessdate=2026-11-24 |format= |work= }}

使用最近一次，最早的（包含当前日期）

{{Cite web |url= |title= |accessdate=2026-11-24 |last= |first= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

使用作者（含当前日期）

{{Cite web |url= |title= |accessdate=2026-11-24 |author= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

使用非关联检索日期，最后，最初

{{Cite web |url= |title= |accessmonthday= |accessyear= |last= |first= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

使用非关联检索的日期，作者

{{Cite web |url= |title= |accessmonthday= |accessyear= |author= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

所有参数，水平格式（删除不需要的参数）

{{Cite web |url= |title= |accessdate= |accessmonthday= |accessdaymonth = |accessyear= |author= |last= |first= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

所有参数，垂直格式

```
{{Cite web
| url =
| title =
| accessdate =
| accessdaymonth =
| accessmonthday =
| accessyear =
| author =
| last =
| first =
| authorlink =
| coauthors =
| date =
| year =
| month =
| format =
| work =
| publisher =
| pages =
| language =
| archiveurl =
| archivedate =
| quote =
}}
```

### 必填参数

* **url**: 在线物品的URL。
* **title**: 在线物品的标题。

*为了制作 [wikilinked 日期](https://en.wikipedia.org/wiki/WP%3ACONTEXT#Dates) 检索方式：*

:   * **访问日期**：项目被访问的完整日期，采用 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD 格式，例如“访问日期 = 2026-11-24”。*不得添加维基链接*

*为了生成非维基链接的检索日期：*

:   * **访问月份日期** 及 **访问年份**：查阅的月份和日期，例如“accessmonthday = May 10”。 *及* 访问该物品时的年份，例如“accessyear = 2005”。生成： *查阅于 2006 年 5 月 10 日。*
    * **accessdaymonth** 和 **accessyear**：访问项目时的月份和日期，例如 "accessmonthday = 10 May"，*以及*访问项目时的年份，例如 "accessyear = 2005"。生成结果：*获取于 10 May 2006。*

### 可选参数

* **作者**: 作者
  + **最后** 与配合 **首先** 生产 `last, first`
  + **authorlink** 可以与 **author** 或 **last** 和 **first** 结合使用，以链接到相应的 Wikipedia 文章。不适用于 URL。
  + **合著者**: 允许添加其他作者
* **日期**: 出版完整日期，最好为 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD格式，例如： *2006-02-17*. 可以加维基链接。
  + OR: **年份**: 出版年份，**月份**: 出版月份的名称。如果还有日期，请使用 *日期*。不得使用维基链接。
* **format**: 格式，例如 PDF。若未指定，则默认为 HTML。
* **作品**: 如果此项目是更大作品的一部分，请注明该作品的名称。
* **发行商**: 如有发行商，请注明。
* **页面**: *第5–7页*：第一页和可选的最后一页。这是用于列出与引用相关的页面，而不是书的总页数。这对于PDF格式尤其有用，因为可以通过链接到相应的页面。 `#page=number` URL末尾带有锚点：

  :   `pages = [http://www.example.org/file.pdf#page=123 p. 123]`
* **语言**: 出版语言（请勿指定“英语”，因为这是默认语言）。
* **archiveurl**：该物品存档位置的URL（需要 **archivedate**）
* **存档日期**：项目存档的日期（需要 **存档链接**，格式为 [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD 格式，例如 *2006-02-17*。不得使用维基链接；系统会自动生成链接。
* **引用**：来自在线物品的相关引用。

## 示例

一些常见的使用场景

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | publisher=Open Publishing | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → Doe, John（2005-04-30）。 [我最爱的东西第二部分](http://www.example.org). *游戏百科*. Open Publishing. 检索于6日,2005日。

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → Doe, John（2005-04-30）。 [我最爱的东西第二部分](http://www.example.org). *游戏百科*检索于6日，2005日。

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | date=2005-04-30 | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → Doe, John（2005-04-30）。 [我最爱的东西第二部分](http://www.example.org)检索于6日，2005日。

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → 多伊，约翰。 [我最爱的东西第二部分](http://www.example.org)检索于6日，2005日。

* {{Cite web | title=My Favorite Things Part II | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → [我最爱的东西第二部分](http://www.example.org)检索于6日，2005日。

* {{Cite web | url=http://www.nfl.com/fans/ | title=Digest of Rules | publisher= National Football League | accessdate=2005-07-06 }}
  → [规则摘要](http://www.nfl.com/fans/)。美国国家橄榄球联盟。查阅于 2005 年 7 月 6 日。

非链接检索日期（使用accessmonthday和accessyear）

* {{Cite web | title=My Favorite Things Part II | work=Encyclopedia of Things | url=http://www.example.org/ | accessmonthday=July 6 | accessyear=2005 }}
   → [我最爱的东西第二部分](http://www.example.org/). *游戏百科*检索于6日，2005日。

使用格式

* {{Cite web | title=List of psychotropic substances under international control | publisher = International Narcotics Control Board | url=http://www.incb.org/pdf/e/list/green.pdf | format = PDF | accessdate=2005-07-06 }}
   → [国际管制精神药物清单](http://www.incb.org/pdf/e/list/green.pdf) （PDF）。国际麻醉品管制局。查阅于 2005 年 7 月 6 日。

语言

* {{Cite web | author=Joliet, François | title=Honnit soit qui mal y pense | date=2005-04-30 | url=http://www.example.org/ | accessdate=2005-07-06 | language=French }}
  → Joliet, François（2005 年 4 月 30 日）。 [Honnit soit qui mal y pense](http://www.example.org) （法语 / French）检索于6日，2005日。

合著者

* {{Cite web | first=John | last=Doe | coauthors=Peter Smith, Jim Smythe | title=My Favorite Things Part II | publisher=Open Publishing | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2006-05-16 }}
  → Doe, John、Peter Smith、Jim Smythe（2005-04-30）。 [我最爱的东西第二部分](http://www.example.org/). *游戏百科*. Open Publishing. 检索于16日,2006日。

无作者

* {{Cite web | title=My Favorite Things Part II | publisher=Open Publishing | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2006-05-16 }}
  → [我最爱的东西第二部分](http://www.example.org/). *游戏百科*。Open Publishing（2005 年 4 月 30 日）。查阅于 2006 年 5 月 16 日。

无作者，无出版商

* {{Cite web | title=My Favorite Things Part II | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → [我最爱的东西第二部分](http://www.example.org/). *游戏百科* （2005 年 4 月 30 日）。查阅于 2005 年 7 月 6 日。

* {{Cite web | title=My Favorite Things Part II | date=2005-04-30 | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → [我最爱的东西第二部分](http://www.example.org/) （2005 年 4 月 30 日）。查阅于 2005 年 7 月 6 日。

* {{Cite web | title=List of psychotropic substances under international control | date=2005-04-30 | url=http://www.incb.org/pdf/e/list/green.pdf | format = PDF | accessdate=2005-07-06 | language=Greek }}
   → [国际管制精神药物清单](http://www.incb.org/pdf/e/list/green.pdf) （希腊语 / Greek） （PDF，2005 年 4 月 30 日）。查阅于 2005 年 7 月 6 日。

使用 archiveurl 和 archivedate 来引用那些已消失但从存档网站可获得的资源

* {{Cite web | title=List of psychotropic substances under international control | date=2005-04-30 | url=http://www.incb.org/pdf/e/list/green.pdf | format = PDF | accessdate=2005-07-06 | archiveurl=http://www.archive.org/2005-09-11/www.incb.org/pdf/e/list/green.pdf | archivedate=2005-09-11 }}
   → [国际管制精神药物清单](http://www.archive.org/2005-09-11/www.incb.org/pdf/e/list/green.pdf) （PDF） （2005-04-30）. 存档于 [原文](http://www.incb.org/pdf/e/list/green.pdf) 于 2005 年 9 月 11 日。查阅于 2005 年 7 月 6 日。

* {{Cite web |url=http://joanjettbadrep.com/cgi-bin/fullStory.cgi?archive=currnews&story=20060405-01shore.htm |title=Interview with Maggie Downs |date=2006-03-31 |publisher=The Desert Sun |archiveurl=http://72.14.207.104/search?q=cache:JAxf4v-pQmgJ:joanjettbadrep.com/cgi-bin/fullStory.cgi%3Farchive%3Dcurrnews%26story%3D20060405-01shore.htm |archivedate=2006-04-26 }}
   → [与玛吉·唐斯访谈](http://72.14.207.104/search?q=cache:JAxf4v-pQmgJ:joanjettbadrep.com/cgi-bin/fullStory.cgi%3Farchive%3Dcurrnews%26story%3D20060405-01shore.htm)。《The Desert Sun》（2006 年 3 月 31 日）。存档来源： [原文](http://joanjettbadrep.com/cgi-bin/fullStory.cgi?archive=currnews&story=20060405-01shore.htm) 于 2006 年 4 月 26 日。

使用引号

* {{Cite web | title = My Favorite Things Part II | work = Encyclopedia of Things | url = http://www.example.org/ | accessdate = 2005-07-06 | quote = Lorem ipsum dolor. }}
  → [我最爱的东西第二部分](http://www.example.org/). *游戏百科*。查阅于 2005 年 7 月 6 日。“Lorem ipsum dolor.”

无参数（错误）

* {{Cite web}}
  → 调用时出错 模板:cite web: 参数 **url** 及 **标题** 必须指定。

**分类**　[分类 · 通用维基模板](../categories/General_wiki_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
