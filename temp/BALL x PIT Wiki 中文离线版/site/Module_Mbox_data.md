# Lua 模块 · Mbox/data

[原文](https://ballxpit.wiki.gg/wiki/Module:Mbox/data) · [修订 383](https://ballxpit.wiki.gg/index.php?oldid=383)

```lua
local localStyle = {
    ['mbox'] = {
        ['display'] = 'flex',
        ['position'] = 'relative',
        ['border'] = '1px solid #d6d6d6',
        ['border-left-width'] = '8px',
        ['border-left-color'] = '#d6d6d6',
        ['border-radius'] = '3px',
        ['margin-bottom'] = '5px',
        ['min-height'] = '32px'
    },
    ['mbox__content'] = {
        ['display'] = 'table',
        ['box-sizing'] = 'border-box',
        ['width'] = '100%',
        ['padding'] = '8px 15px'
    },
    ['mbox__content__image'] = {
        ['display'] = 'table-cell',
        ['width'] = '40px',
        ['height'] = '100%',
        ['text-align'] = 'center',
        ['vertical-align'] = 'middle',
        ['padding-right'] = '15px'
    },
    ['mbox__content__wrapper'] = {
        ['display'] = 'table-cell',
        ['vertical-align'] = 'middle'
    },
    ['mbox__content__header'] = {
        ['display'] = 'block',
        ['font-weight'] = 'bold'
    },
    ['mbox__content__text'] = {
        ['display'] = 'block'
    },
    ['mbox__content__text__comment'] = {
        ['font-size'] = 'small'
    },
    ['mbox__content__aside'] = {
        ['display'] = 'table-cell',
        ['width'] = '100px',
        ['vertical-align'] = 'middle',
        ['text-align'] = 'center',
        ['padding-left'] = '15px',
        ['border-left'] = '1px solid #d6d6d6'
    },
    ['mbox__close'] = {
        ['position'] = 'absolute',
        ['right'] = '0',
        ['top'] = '0',
        ['padding'] = '2px 7px',
        ['font-weight'] = 'bold',
        ['font-size'] = '16px',
        ['color'] = '#bbb',
        ['cursor'] = 'pointer',
        ['transition'] = 'all .15s ease-in'
    }
}
return { localStyle = localStyle }
```

[返回总入口](../%E7%90%83%E6%AF%94%E4%BC%A6%E6%88%98%E8%AE%B0%20Wiki.md) · [返回本分目录](%E7%9B%AE%E5%BD%95.md)
