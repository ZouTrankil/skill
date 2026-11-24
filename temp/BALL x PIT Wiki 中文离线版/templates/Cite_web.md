# 模板 · 引用网（Cite web）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Cite_web) · [修订 301](https://ballxpit.wiki.gg/index.php?oldid=301) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Cite_web_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Cite_web/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Cite_web/testcases) 页面上进行实验。 |

此模板用于维基百科中的 [cite 源](https://en.wikipedia.org/wiki/WP%3ACITE) 。 它专门用于不是新闻来源的网站。 此模板替换了已折旧的 [Template:Web reference](https://en.wikipedia.org/wiki/Template%3AWeb_reference)。 它仅提供较低大小写参数。

关于使用模板在维基百科文章中添加公开来源网站内容引用的一般性讨论可在 [引用模板](https://en.wikipedia.org/wiki/Citation_templates)上查阅。

本页使用 [Creative Commons 许可](https://ballxpit.wiki.gg/wiki/W%3AWikia%3ALicensing?action=edit&redlink=1) 内容来自 [Wookiepedia](https://ballxpit.wiki.gg/wiki/W%3Ac%3AWookieepedia%3ATemplate%3ACite_web?action=edit&redlink=1)

#### 使用率

对网页作者身份知之甚少(现日)的案件通常采用的形式

{{Cite web |url= |title= |accessdate=2026-11-24 |format= |work= }}

使用最后， 第一次( 以当前日期)

{{Cite web |url= |title= |accessdate=2026-11-24 |last= |first= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

使用作者( 以当前日期)

{{Cite web |url= |title= |accessdate=2026-11-24 |author= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

使用非链接获取日期， 最后， 第一

{{Cite web |url= |title= |accessmonthday= |accessyear= |last= |first= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

使用无链接检索日期，作者

{{Cite web |url= |title= |accessmonthday= |accessyear= |author= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

所有参数， 水平格式( 删除不需要的参数)

{{Cite web |url= |title= |accessdate= |accessmonthday= |accessdaymonth = |accessyear= |author= |last= |first= |authorlink= |coauthors= |date= |year= |month= |format= |work= |publisher= |pages= |language= |archiveurl= |archivedate= |quote= }}

所有参数， 垂直格式

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

##### 所需参数

* **url**:在线项目的 URL。
* **标题**:在线项目标题。

*生产 [维基链接日期](https://en.wikipedia.org/wiki/WP%3ACONTEXT#Dates) 检索数 :*

:   * **访问日期**: : 访问项目的全日期:项目获得全天天，项目存取的日期:项目，在: [ISO 8601标准](https://en.wikipedia.org/wiki/ISO_8601) 采用 YYYY-MM-DD 格式，例如“accessdate = 2026-11-24”。 *不能是 wiki 链接*

*用于制作非wiki链接的检索日期:*

:   * **每月开放日** 及 **进入年份**：查阅的月份和日期，例如“accessmonthday = May 10”。 *及* 例如“进入年份=2005年”。 *查阅于 2006 年 5 月 10 日。*
    * **开放月** 及 **进入年份**：查阅的月份和日期，例如“accessmonthday = 10 May”。 *及* 例如“进入年份=2005年”。 *查阅于 2006 年 5 月 10 日。*

##### 任择参数

* **作者作者**编辑器
  + **最后一个** 工作与 **初次** 生产 `last, first`
  + **作者链接** 与 **作者作者** 具有或具有 **最后一个** & **初次** 链接到相应的 wikipedia 文章。不使用 URL 。
  + **共同著者**: 允许添加作者
* **日期日期日期**:出版全日，最好在:全出版日，最好在:全出版日，最好在:全出版日，最好在:全出版日期: [ISO 8601标准](https://en.wikipedia.org/wiki/ISO_8601) YYY-MM-DD格式，例如: *2006-02-17*可能是维基连连连维基连连维基连连维基连连连
  + 或: **年份**出版年份:出版年份;出版年份: **月月**:出版月份的名称。如果您同时有日期，请使用 *日期日期日期* 而不是维基链接。
* **format**:格式，例如PDF。 HTML 隐含，如果未指明的话。
* **work**:如果此项目属于较大工程的一部分，该工程的名称。
* **publisher**:出版商，如果有的话。
* **页数**: *第5-7页*:第一页和可选的最后一页。此页用于列出与引用有关的页面，而不是书本中的页面总数。这对PDF格式特别有用，因为该页面可以与 `#page=number` 锁定标记在 URL 结尾处 :

  :   `pages = [http://www.example.org/file.pdf#page=123 p. 123]`
* **语言**:出版语文(不指定“英文”,因为这是默认的)。
* **archievurl**:项目归档位置的 URL( 需要 **存档日期** )
* **存档**:项目被存档的日期(要求款要求) :项目被存档的日期(需要) **档案url**)，在 [ISO 8601标准](https://en.wikipedia.org/wiki/ISO_8601) YYY-MM-DD格式，例如: *2006-02-17*。不能是维基链接;它会自动链接。
* **引号**:在线项目的相关引号。

#### 实例实例实例

一些标准使用案例

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | publisher=Open Publishing | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → John Doe,(2005-04-30年)。 [我最喜欢的事情第二部分](http://www.example.org). *《事物百科全书》*. Open Publishing. Retrieved on July 6, 2005 (英语)。

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → John Doe,(2005-04-30年)。 [我最喜欢的事情第二部分](http://www.example.org). *《事物百科全书》*. Retrieved on July 6, 2005 (英语)。

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | date=2005-04-30 | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → John Doe,(2005-04-30年)。 [我最喜欢的事情第二部分](http://www.example.org). Retrieved on July 6, 2005 (英语)。

* {{Cite web | author=Doe, John | title=My Favorite Things Part II | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → 杜伊，约翰 [我最喜欢的事情第二部分](http://www.example.org). Retrieved on July 6, 2005 (英语)。

* {{Cite web | title=My Favorite Things Part II | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → [我最喜欢的事情第二部分](http://www.example.org). Retrieved on July 6, 2005 (英语)。

* {{Cite web | url=http://www.nfl.com/fans/ | title=Digest of Rules | publisher= National Football League | accessdate=2005-07-06 }}
  → [《规则》摘要汇编](http://www.nfl.com/fans/)。美国国家橄榄球联盟。查阅于 2005 年 7 月 6 日。

检索的非连接日期(使用访问月日和访问年)

* {{Cite web | title=My Favorite Things Part II | work=Encyclopedia of Things | url=http://www.example.org/ | accessmonthday=July 6 | accessyear=2005 }}
   → [我最喜欢的事情第二部分](http://www.example.org/). *《事物百科全书》*. Retrieved on July 6, 2005 (英语)。

使用格式

* {{Cite web | title=List of psychotropic substances under international control | publisher = International Narcotics Control Board | url=http://www.incb.org/pdf/e/list/green.pdf | format = PDF | accessdate=2005-07-06 }}
   → [应受国际管制的精神药物清单](http://www.incb.org/pdf/e/list/green.pdf) （PDF）。国际麻醉品管制局。查阅于 2005 年 7 月 6 日。

语言语言语言

* {{Cite web | author=Joliet, François | title=Honnit soit qui mal y pense | date=2005-04-30 | url=http://www.example.org/ | accessdate=2005-07-06 | language=French }}
  → Joliet, François（2005 年 4 月 30 日）。 [香尼特 soit qui mal y sense y sens y y am am y y](http://www.example.org) （法语 / French）。. Retrieved on July 6, 2005 (英语)。

共同著者

* {{Cite web | first=John | last=Doe | coauthors=Peter Smith, Jim Smythe | title=My Favorite Things Part II | publisher=Open Publishing | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2006-05-16 }}
  → Doe, John; 彼得·史密斯， 吉姆·斯迈思(2005-04-30)。 [我最喜欢的事情第二部分](http://www.example.org/). *《事物百科全书》*. Open Publishing. Retrieved on May 16, 2006 (英语)。

无作者者

* {{Cite web | title=My Favorite Things Part II | publisher=Open Publishing | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2006-05-16 }}
  → [我最喜欢的事情第二部分](http://www.example.org/). *《事物百科全书》*。Open Publishing（2005 年 4 月 30 日）。查阅于 2006 年 5 月 16 日。

没有作者，没有出版商

* {{Cite web | title=My Favorite Things Part II | date=2005-04-30 | work=Encyclopedia of Things | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → [我最喜欢的事情第二部分](http://www.example.org/). *《事物百科全书》* （2005 年 4 月 30 日）。查阅于 2005 年 7 月 6 日。

* {{Cite web | title=My Favorite Things Part II | date=2005-04-30 | url=http://www.example.org/ | accessdate=2005-07-06 }}
  → [我最喜欢的事情第二部分](http://www.example.org/) （2005 年 4 月 30 日）。查阅于 2005 年 7 月 6 日。

* {{Cite web | title=List of psychotropic substances under international control | date=2005-04-30 | url=http://www.incb.org/pdf/e/list/green.pdf | format = PDF | accessdate=2005-07-06 | language=Greek }}
   → [应受国际管制的精神药物清单](http://www.incb.org/pdf/e/list/green.pdf) （希腊语 / Greek）。 （PDF，2005 年 4 月 30 日）。查阅于 2005 年 7 月 6 日。

使用档案和档案档案，以查阅从档案网站查阅的已离开但可从档案网站查阅的物品

* {{Cite web | title=List of psychotropic substances under international control | date=2005-04-30 | url=http://www.incb.org/pdf/e/list/green.pdf | format = PDF | accessdate=2005-07-06 | archiveurl=http://www.archive.org/2005-09-11/www.incb.org/pdf/e/list/green.pdf | archivedate=2005-09-11 }}
   → [应受国际管制的精神药物清单](http://www.archive.org/2005-09-11/www.incb.org/pdf/e/list/green.pdf) (PDF)(2005-04-30)。 Archived from. [永久失效连结] (中文(简体) )。 [原件](http://www.incb.org/pdf/e/list/green.pdf) 于 2005 年 9 月 11 日。查阅于 2005 年 7 月 6 日。

* {{Cite web |url=http://joanjettbadrep.com/cgi-bin/fullStory.cgi?archive=currnews&story=20060405-01shore.htm |title=Interview with Maggie Downs |date=2006-03-31 |publisher=The Desert Sun |archiveurl=http://72.14.207.104/search?q=cache:JAxf4v-pQmgJ:joanjettbadrep.com/cgi-bin/fullStory.cgi%3Farchive%3Dcurrnews%26story%3D20060405-01shore.htm |archivedate=2006-04-26 }}
   → [采访Maggie Downs](http://72.14.207.104/search?q=cache:JAxf4v-pQmgJ:joanjettbadrep.com/cgi-bin/fullStory.cgi%3Farchive%3Dcurrnews%26story%3D20060405-01shore.htm)。《The Desert Sun》（2006 年 3 月 31 日）。存档来源： [原件](http://joanjettbadrep.com/cgi-bin/fullStory.cgi?archive=currnews&story=20060405-01shore.htm) 于 2006 年 4 月 26 日。

使用引号

* {{Cite web | title = My Favorite Things Part II | work = Encyclopedia of Things | url = http://www.example.org/ | accessdate = 2005-07-06 | quote = Lorem ipsum dolor. }}
  → [我最喜欢的事情第二部分](http://www.example.org/). *《事物百科全书》*。查阅于 2005 年 7 月 6 日。“Lorem ipsum dolor.”

无参数( error)

* {{Cite web}}
  → 调用时出错 模板:cite web: 参数 **URL 服务器** 及 **标题标题** 必须指定。

**分类**　[分类 · 一般维基模板](../categories/General_wiki_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
