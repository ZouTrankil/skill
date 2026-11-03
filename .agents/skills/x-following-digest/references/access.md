# X 接入与字段

网页登录与开发者 API 授权是不同的凭据。只检查配置存在与权限状态，不输出 token/cookie。不要把用户“已登录”写成“官方 API 已接通”。

## 官方 API

已有用户授权时，按当前官方文档调用 `https://api.x.com/2` 下的只读端点：

| 目的 | 端点 |
| --- | --- |
| 核对登录用户 | `GET /users/me` |
| 分页关注名单 | `GET /users/:id/following` |
| 分页用户动态 | `GET /users/:id/tweets` |
| 时间线候选 | `GET /users/:id/timelines/reverse_chronological` |

以当前接口文档为准核对 OAuth 用户授权、read scopes、套餐额度和分页上限；仅有 app-only Bearer Token 不能假定可读 `/users/me` 或用户首页。不自动购买额度。

请求帖子字段至少包含 `author_id,created_at,conversation_id,referenced_tweets`，通过用户及引用 expansion 补足归属与上下文；长文使用接口当前支持的完整正文字段，缺失则明确记录。逐用户接口携带冻结窗口的 `start_time/end_time`，使用 `meta.next_token` 续页；关注名单同样必须翻到末页。ID 按字符串保存，避免浮点精度丢失。

接口最新返回数量受产品上限影响；拿到末页仍需检查窗口是否被上限截断。首页候选流不能证明每个关注用户均已覆盖，也可能含自发内容或转帖；必须按白名单和帖子类型过滤。

官方参考：

- [关注关系](https://docs.x.com/x-api/users/follows/introduction)
- [动态与时间线](https://docs.x.com/x-api/posts/timelines/introduction)
- [用户身份](https://docs.x.com/x-api/users/lookup/introduction)

## Aside 登录态网页接口

用户选择复用已登录 X 时，先读 `aside-browser` 技能并运行 `aside guide`。检查 `aside skills list` 是否已有 X 专用适配，存在时读取其文档；不能假设有名为 `x` 或 `twitter` 的 REPL 全局。

本机试跑发现：CLI 列表可能漏列 Aside 内部的 `x-twitter` 技能。列表未显示时，可交给 `aside exec` 请求读取内部 X 技能并执行只读采集，不要据此直接判断没有适配器。2026-10-29 的实际文档位于 `/Users/Apple/.aside/u/0/skills/builtin/x-twitter/SKILL.md`；该路径仅为本机定位线索，其他 profile/机器应重新发现。其 agent 内部 REPL 提供：

```js
const me = await twitter.getMe();
const batch = await twitter.getTimeline({ count: 100 });
const next = batch.nextCursor
  ? await twitter.getTimeline({ count: 100, cursor: batch.nextCursor })
  : null;
const author = await twitter.getUser('screenName');
const posts = await twitter.getUserTweets('screenName', { count: 100 });
const post = await twitter.getTweet('postId');
```

这些方法在 Aside agent 内已实际调用，不能推断 CLI 的独立 `aside repl` 拥有同一组全局。适配器返回 `createdAt`、`author.id`、`author.screenName`、`text`、`nextCursor` 等；时间窗口仍需本地过滤。此版本文档没有列出读取完整关注名单的方法，须从网页 Following 名单核验并通过 `getUser` 补稳定 ID。实际时间线混入过非关注内容，必须再过滤；`getTweet` 也可能仍返回截断长文，应到原帖展开核对。时间线中出现一条旧帖不表示后续都已越过窗口，要检查乱序、重复 cursor 及整页覆盖。

需要直接检查页面时先运行 `aside guide repl`；列举标签页、附着现有 X 页面并读取 snapshot，确认账号。只调用当前适配器文档或实际页面请求所证实的只读接口，验证作者、时间、正文及 cursor 的返回结构。网页接口不是官方开发者 API：不硬编码从别处猜测的 GraphQL operation ID，不导出浏览器认证数据到 shell，也不把凭据转发至第三方域名。

Aside 的 cookie-bearing `fetch` 仅按其指南用于安全同源 GET/HEAD；如果实际接口需要当前工具不支持的认证或请求方式，报告“登录态 API 未接通”，不要虚构调用成功。若用户允许改用网页读取，可以从 Following 和逐用户页面补充；仍需证明关注关系与窗口覆盖，并把访问方式标为网页读取。不能把 For you、搜索热榜或加载出的首屏当作完整关注动态。

## Telegram

直连发送参考 [Telegram Bot API](https://core.telegram.org/bots/api#sendmessage)。正文不得超过 `sendMessage` 的长度限制；使用字符串类型保存 chat ID。目标接受已确认的 channel `@username` 或数值 ID；机器人必须具备相应频道发帖权限。

复用 Florence 时按现有 `florence-notify` 技能选择 bot 与显式目标。`info` 是机器人路由名，不能由此推断它对应用户要求的频道。通知中继若无送达查询，发送超时就保留结果未知，不能伪造“恰好一次”保证。
