#!/usr/bin/env python3
"""修复后验证：1) 站内 .md 链接与本地资产引用是否都能解析 2) 残留问题复查。只读。"""
import os, re, sys, urllib.parse, collections

ROOT = '/Users/Apple/zq/work/skill/temp/BALL x PIT Wiki 中文离线版'
DIRS = ['articles', 'categories', 'templates', 'files', 'data', 'site', 'navigation']
LINK = re.compile(r'\]\(([^)\s]+)\)')
IMG = re.compile(r'!\[[^\]]*\]\(([^)\s]+)\)')

bad_links = collections.defaultdict(set)
checked = 0

def resolve(base_dir, target):
    t = urllib.parse.unquote(target.split('#')[0])
    if not t or t.startswith(('http://', 'https://', 'mailto:')):
        return True
    p = os.path.normpath(os.path.join(base_dir, t))
    return os.path.exists(os.path.join(ROOT, p)) if not p.startswith('/') else os.path.exists(p)

for d in DIRS:
    base = os.path.join(ROOT, d)
    for fn in sorted(os.listdir(base)):
        if not fn.endswith('.md'):
            continue
        text = open(os.path.join(base, fn), encoding='utf-8').read()
        for m in LINK.finditer(text):
            tgt = m.group(1)
            checked += 1
            if not resolve(d, tgt):
                bad_links[f'{d}/{fn}'].add(tgt)

print(f'检查 {checked} 个链接引用')
if bad_links:
    print(f'!! {sum(len(v) for v in bad_links.values())} 个失效引用：')
    for f, ts in sorted(bad_links.items()):
        for t in sorted(ts):
            print(f'  {f} -> {t}')
else:
    print('所有站内链接与本地资产引用均可解析 ✓')

# 残留复查
LEFT = [r'处理\d', r'QQ ', r'打个电话', r'收获到\d', r'坚力', r'球酒', r'字符', r'老板',
        r'机率', r'关键击球', r'冷冻射线', r'冷却射线', r'凶手', r'贝尔塞克', r'豪华豪华',
        r'骨球ista', r'小费者', r'驱逐的火焰', r'迷人（Charm）', r'雪风（Blizzard）',
        r'基本（Elemental）', r'麦机', r'滴滴', r'奖金', r'性格', r'小瓦', r'卢伯园', r'残局', r'未完成条目', r'冻结射线', r'冻灼', r'分类 · 将军',
        r'生命值等级', r'生命值比例', r'生命值阈值', r'生命值刻度', r'冰境', r'冰界', r'冰岛',
        r'通常的敌人', r'常见的敌人', r'卫生规模', r'副主管', r'正常的（enemy', r'龙兽', r'党派宅邸',
        r'匹配者', r'鼠标（', r'构筑 ／', r'统计精灵图', r'统计等级', r'蒂普托尔', r'球酒', r'坚力']
total = 0
for d in DIRS:
    base = os.path.join(ROOT, d)
    for fn in sorted(os.listdir(base)):
        if not fn.endswith('.md'):
            continue
        for i, line in enumerate(open(os.path.join(base, fn), encoding='utf-8'), 1):
            for pat in LEFT:
                if re.search(pat, line):
                    print(f'  残留 [{pat}] {d}/{fn}:L{i}')
                    total += 1
print(f'残留命中 {total} 处')
