#!/usr/bin/env python3
"""跨批次最终译名对齐。全部精确字符串替换，统计并记录。"""
import os, collections

ROOT = '/Users/Apple/zq/work/skill/temp/BALL x PIT Wiki 中文离线版'
DIRS = ['articles', 'categories', 'templates', 'files', 'data', 'site', 'navigation']
EXACT = [
    # Stub 类统一为 待完善（磁盘主导形式，与正文提示一致）
    ('分类 · 未完成条目（Stubs）', '分类 · 待完善（Stubs）'),
    ('分类 · 残局', '分类 · 待完善'),
    ('未完成条目', '待完善'),
    # General 分类统一为 通用（保留"退役将军"正文）
    ('分类 · 将军', '分类 · 通用'),
    # Cut Content 统一为 删减内容（与"测试版与删减内容"一致）
    ('分类 · 删除内容', '分类 · 删减内容'),
    # 精灵图分类族统一（注意先长后短）
    ('分类 · 敌人角色图像', '分类 · 敌人精灵图'),
    ('分类 · 球精灵图', '分类 · 圆球精灵图'),
    ('分类 · 角色图像', '分类 · 角色精灵图'),
    # 术语归一
    ('冻结射线', '冰冻射线'),
    ('冻灼', '霜灼'),
    ('构筑 ／ 积分', '建造点'),
]

total = collections.Counter()
changed = []
for d in DIRS:
    base = os.path.join(ROOT, d)
    for fn in sorted(os.listdir(base)):
        if not fn.endswith('.md'):
            continue
        path = os.path.join(base, fn)
        text = open(path, encoding='utf-8').read()
        orig = text
        for old, new in EXACT:
            n = text.count(old)
            if n:
                total[f'{old} → {new}'] += n
                text = text.replace(old, new)
        if text != orig:
            changed.append(f'{d}/{fn}')
            open(path, 'w', encoding='utf-8').write(text)
for k in sorted(total, key=lambda k: -total[k]):
    print(f'{total[k]:5d}  {k}')
print(f'修改文件数 {len(changed)}')
open('/Users/Apple/zq/work/skill/temp/wiki_fix/对齐记录.txt', 'w', encoding='utf-8').write(
    ''.join(f'{total[k]:5d}  {k}\n' for k in sorted(total, key=lambda k: -total[k]))
    + f'\n修改文件数 {len(changed)}\n' + '\n'.join(changed) + '\n')
