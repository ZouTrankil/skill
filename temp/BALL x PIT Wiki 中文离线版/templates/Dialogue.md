# 模板 · 对话（Dialogue）

[原文与贡献者记录](https://ballxpit.wiki.gg/wiki/Template:Dialogue) · [修订 79](https://ballxpit.wiki.gg/index.php?oldid=79) · [返回目录](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md)

| 模板文档 |
| --- |
| *注意：如果没有提供数值，模板样本的部分内容可能无法显示。* |
| 查看或编辑 [此文档](Dialogue_doc.md)。（[关于模板文档](Documentation.md)） |
| 编辑可以在此模板的[沙盒](https://ballxpit.wiki.gg/wiki/Template:Dialogue/sandbox?action=edit)和[测试案例](https://ballxpit.wiki.gg/wiki/Template:Dialogue/testcases)页面上进行实验。 |

{{对话}} 有助于以标准格式编写对话。该模板可以处理大多数标准的对话编写格式，并且可以缩进、添加项目符号或编号。 **此模板 *无法* 是 `subst:`'d**.

此模板使用 [Lua 模板语言](https://ballxpit.wiki.gg/wiki/W%3AHelp%3ALua?action=edit&redlink=1)，更多相关信息可以在 [全局 Lua 模块页面](https://ballxpit.wiki.gg/wiki/W%3Ac%3Adev%3AGlobal_Lua_Modules/Dialogue?action=edit&redlink=1)找到。**如需此模板的传统 Wikitext 版本，请参阅 [Template 讨论页](https://ballxpit.wiki.gg/wiki/W%3Ac%3Atemplates%3ATemplate%3ADialogue/wikitext?action=edit&redlink=1)**。

[ ]

## 目录（Contents）

* [1 语法](#%E8%AF%AD%E6%B3%95)
* [2 参数](#%E5%8F%82%E6%95%B0)
* [3 示例](#%E7%A4%BA%E4%BE%8B)
  + [3.1 备注](#%E5%A4%87%E6%B3%A8)

## 语法

这是如何在[wiki文本](https://ballxpit.wiki.gg/wiki/W%3AHelp%3Awikitext?action=edit&redlink=1)中为您的文章编写模板的：

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

这些参数在下方有更详细的说明。

## 参数

**命名参数指定了名称快捷方式。它们都是可选的。**它们被放置在模板调用的顶部，如下所示：

```
{{dialogue
|short=full
|short=full
|short=full
...
```

名称缩写适用于你的主要对话文本。如果你在这里为角色名称使用了缩写，那么其完整名称将会被替换。

形式为“”的命名参数`mood1`", "`mood2`", "`mood3`”, 等等，直至 “`mood10`", 为相应的行号指定情绪（例如“`mood1`“指定第1行）。它们按以下方式排列：

```
...
|Character|Speech|mood1=angry
|Character|Speech|mood2=quiet
|Character|Speech|mood3=ecstatic
...
```

位置参数构成了对话文本（即任何不包含“`=`将被视为对话的一部分。

:   `Parameter 1` *（必填）*
    :   角色发言

    `Parameter 2` *（可选）*
    :   请发言

    `Parameter 3` *（可选）*
    :   下一个角色

    `Parameter 4` *（可选）*
    :   下一行

    `Parameter 5` *（可选）*
    :   下一个角色

    `Parameter 6` *（可选）*
    :   下一行

    `Parameter 7` *（可选）*
    :   如此而已……

注意：如果任何角色被提及`action`那么，那一行将被解释为一条行动线。它仍然算数。 *线* 尽管如此。

要编写对话说明/来源，请使用 `cite =`

## 示例

下面是完整的模板用法。

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

以上内容将生成：

> **哈里·恩菲尔德** *（开心）*
> :   "你好！"
>
> **Bryan Adams** *（惊讶）*
> :   "哦，你好啊"
>
> **哈里·恩菲尔德** *（好奇的）*
> :   "你怎么样？"
>
> **Bryan Adams** *（保留）*
> :   "挺好的，谢谢。"
>
> **哈里·恩菲尔德** *（神气活现）*
> :   "哦，真不错。"
>
> **布莱恩·亚当斯** *（打扮得很俏）*
> :   "没错吧？！"
>
> **哈里·恩菲尔德** *（无聊）*
> :   "确实如此。"
>
> **布莱恩·亚当斯** *（高兴）*
> :   "好吧，我走了！"
>
> **哈里·恩菲尔德** *（松了一口气）*
> :   "回头见！"
>
> **布莱恩·亚当斯** *（讽刺地）*
> :   "再见！"

以下代码展示了扩展使用的示例：

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

以上内容将生成：

> :   *\[进入：乔治和瑞秋\]*
>
> **乔治·博伊** *（开心）*
> :   "清晨好，亲爱的瑞秋！"
> :   *\[瑞秋转头看向他\]*
>
> **瑞秋**
> :   "哦，乔治，是你！"
>
> **Georgie Boy**
> :   "..."
>
> **瑞秋** *（担忧）*
> :   "你为什么什么都不说？！"
> :   *\[进入：守卫\]*
>
> **守卫**
> :   "我们宣布乔治已被逮捕！"
>
> **瑞秋** *（惊恐不已）*
> :   "哦，我的天！"
> :   *\[乔治被拖走了。\]*

### 备注

你可以为对话编号、添加项目符号或缩进：

```
:{{dialogue|Me|Hello|You|Howdido!}}
```

:   > **我**
    > :   "你好"
    >
    > **你**
    > :   "你好呀！"

```
#{{dialogue|Me|Hello|You|Howdido!}}
#{{dialogue|Them|Good afternoon|Us|What a load of rubbish!}}
```

1. > **我**
   > :   "你好"
   >
   > **你**
   > :   "你好呀！"
2. > **它们**
   > :   "下午好"
   >
   > **Us**
   > :   "真是胡说八道！"

```
*{{dialogue
|angel=Fortitude
|angel|I am an angel!|Crowd|We don't believe you!}}
*{{dialogue
|angel=Fortitude
|angel|But I'm being quite serious!|Crowd|Too bad for you then!}}
```

* > **坚韧**
  > :   "我是个天使！"
  >
  > **人群**
  > :   "我们不相信你！"
* > **坚韧**
  > :   "但我可是认真的！"
  >
  > **人群**
  > :   "那你就太可惜了！"

您会遇到奇数间距错误（例如“Speech`<space>`") 如果你将对话分多行列出。

**分类**　[分类 · 引用模板](../categories/Quote_templates.md)

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
