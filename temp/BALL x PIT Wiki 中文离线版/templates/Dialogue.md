# 模板 · 对话（Dialogue）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Dialogue) · [修订 79](https://ballxpit.wiki.gg/index.php?oldid=79) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注:未提供值，模板样本的某些部分可能无法见。* |
| 查看或编辑 [此文档](Dialogue_doc.md) ( [关于模板文档](Documentation.md)) |
| 编辑器可以在此模板 [sandbox](https://ballxpit.wiki.gg/wiki/Template:Dialogue/sandbox?action=edit) 和 [测试案例](https://ballxpit.wiki.gg/wiki/Template:Dialogue/testcases) 页面上进行实验。 |

{{对话模板可以处理大多数标准格式的书写对话，可以缩进、弹进或编号。 **此模板模板 *无法不能* be be be 的， 是 `subst:`'d (英语)。**.

此模板模板使用 [Lua 临时语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1),可以找到更多信息 [全球卢亚模块页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Dialogue?action=edit&redlink=1). **此模板的传统维基文本版本见 [关于模板对话框维基](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3ADialogue/wikitext?action=edit&redlink=1)**.

[ ]

#### 目录（Contents）

* [1 语法](#%E8%AF%AD%E6%B3%95)
* [2 参数参数](#%E5%8F%82%E6%95%B0%E5%8F%82%E6%95%B0)
* [3 实例实例实例](#%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B%E5%AE%9E%E4%BE%8B)
  + [3.1 备注](#%E5%A4%87%E6%B3%A8)

#### 语法

这是如何在您的文章中写入 [wikitext](https://ballxpit.wiki.gg/wiki/W%3AHelp%3Awikitext?action=edit&redlink=1) 模板 :

```
{{dialogue
|short=full
|short=full
|short=full
...
|Character|Speech
|Character|Speech
|Character|Speech
...
|cite = dialogue description
}}
```

下文对这些参数作了更详尽的解释。

#### 参数参数

**命名参数指定了名称快捷键。 它们都是可选的。** 它们被放在模板调用的最上方， 例如 :

```
{{dialogue
|short=full
|short=full
|short=full
...
```

名称快捷键适用于主对话框文本。如果您使用此处指定的字符名快捷键，则全名将被替换。

窗体命名参数 "`mood1`", "`mood2`", "`mood3`" 等，最多 "`mood10`" ,指定对应行号的情绪(例如) "`mood1`" 具体说明一行1，它们被置于像这样的一行中:

```
...
|Character|Speech|mood1=angry
|Character|Speech|mood2=quiet
|Character|Speech|mood3=ecstatic
...
```

定位参数构成对话框的文字(即不包含“或”的线条)。`=`" 将被视为对话的一部分。 " ,并被解释为对话的一部分。 " ,将被视为对话的一部分。

:   `Parameter 1` *(必须)*
    :   使用字符名

    `Parameter 2` *(可选)*
    :   要发言的行

    `Parameter 3` *(可选)*
    :   下一个字符

    `Parameter 4` *(可选)*
    :   下一行

    `Parameter 5` *(可选)*
    :   下一个字符

    `Parameter 6` *(可选)*
    :   下一行

    `Parameter 7` *(可选)*
    :   等等。..

注:如果任何字符被称作 "`action`" 然后，该线将被解释为行动方针。 *直行* 尽管如此。

要写入对话框描述/源，请使用 `cite =`

#### 实例实例实例

以下是完全使用模板的例子 :

```
{{dialogue
|harry=Harry Enfield
|bryan=Bryan Adams

|harry|Hello!                |mood1=happy
|bryan|Oh hello there        |mood2=surprised
|harry|How are you?          |mood3=inquisitive
|bryan|Quite fine thank you. |mood4=reserved
|harry|Oh that's spiffing.   |mood5=spiffed
|bryan|It is, isn't it?!     |mood6=multo-spiffed
|harry|Quite so.             |mood7=bored
|bryan|Well, I'm off!        |mood8=joyous
|harry|Ta-ta!                |mood9=relieved
|bryan|Au revoir!            |mood10=sarcastic
}}
```

以上将产生:

> **哈利·恩菲尔德** *(快乐)*
> :   "哈罗!"
>
> **布莱恩·亚当斯** *(惊讶)*
> :   "你好啊你好啊"
>
> **哈利·恩菲尔德** *(问讯)。*
> :   "你好吗?"
>
> **布莱恩·亚当斯** *(保留)*
> :   "很好谢谢"
>
> **哈利·恩菲尔德** *(发音)*
> :   "哦，这是令人毛骨悚然。"
>
> **布莱恩·亚当斯** *(multo-spiffed) (英语)。*
> :   "是吗?"
>
> **哈利·恩菲尔德** *(闷闷不乐)*
> :   "确实如此"
>
> **布莱恩·亚当斯** *(合唱) (合唱) (唱唱) (*
> :   "好了，我要走了! 我该走了!"
>
> **哈利·恩菲尔德** *(释曰。*
> :   "塔 -塔!"
>
> **布莱恩·亚当斯** *(sarcastic) (英语)。*
> :   "再见!"

以下代码展示了扩大使用的例子:

```
{{dialogue
|george=Georgie Boy
|rachel=Rachel

|action|Enter: George and Rachel
|george|Good morrow dearest Rachel!|mood2=happy
|action|Rachel turns to see him
|rachel|Oh, George, it's you!
|george|...
|rachel|Why won't you say anything?!|mood6=worried
|action|Enter: Guards
|Guards|We are announcing George's arrest!
|rachel|Oh my!|mood9=horrified
|action|George is dragged away.
}}
```

以上将产生:

> :   *\[输入:乔治和瑞秋\]*
>
> **乔治男孩** *(快乐)*
> :   "早上好，亲爱的瑞秋"
> :   *\[雷切尔转身见他\]*
>
> **瑞切尔**
> :   "哦，乔治，是你!"
>
> **乔治男孩**
> :   "..."
>
> **瑞切尔** *(烦恼)。*
> :   "为什么你什么都不说?"
> :   *\[输入:警卫\]*
>
> **警卫**
> :   "我们要宣布逮捕乔治!"
>
> **瑞切尔** *(rrorried) (已) (*
> :   "哦，我的天!"
> :   *\[乔治被拖走了。 \]*

##### 备注

您可以在对话框中编号、输入或缩进:

```
:{{dialogue|Me|Hello|You|Howdido!}}
```

:   > **我我我**
    > :   "哈罗"
    >
    > **你，你**
    > :   "豪迪多!"

```
#{{dialogue|Me|Hello|You|Howdido!}}
#{{dialogue|Them|Good afternoon|Us|What a load of rubbish!}}
```

1. > **我我我**
   > :   "哈罗"
   >
   > **你，你**
   > :   "豪迪多!"
2. > **他们**
   > :   "下午好，下午好"
   >
   > **我们我们**
   > :   "胡说八道!"

```
*{{dialogue
|angel=Fortitude
|angel|I am an angel!|Crowd|We don't believe you!}}
*{{dialogue
|angel=Fortitude
|angel|But I'm being quite serious!|Crowd|Too bad for you then!}}
```

* > **坚度**
  > :   "我是个天使!"
  >
  > **人群**
  > :   "我们不相信你!"
* > **坚度**
  > :   "但我是认真的!"
  >
  > **人群**
  > :   "对你来说太糟糕了!"

您将会得到奇异的间距错误( 例如“ 语音” )`<space>`如果你在多条线上进行对话。

**分类**　[分类 · 报价模板](../categories/Quote_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
