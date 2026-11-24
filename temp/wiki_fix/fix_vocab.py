#!/usr/bin/env python3
"""按术语表批量修复。先打印每条替换的命中数与样例（--dry），--apply 才写盘。"""
import os, re, sys, collections

ROOT = '/Users/Apple/zq/work/skill/temp/BALL x PIT Wiki 中文离线版'
DIRS = ['articles', 'categories', 'templates', 'files', 'data', 'site', 'navigation']
APPLY = '--apply' in sys.argv

# 顺序敏感：长串/专名在前
EXACT = [
    ('骨球ista（Bone Ballista）', '骨制弩炮（Bone Ballista）'),
    ('骨球ista', '骨制弩炮'),
    ('豪华豪华豪华者', '挥霍者'),
    ('小费者', '蹑足者'),
    ('旗星', '自笞者'),
    ('旗手', '自笞者'),
    ('卢伯园', '木工场'),
    ('海关链接标签', '自定义链接标签'),
    ('错过页面图标', '缺失页面图标'),
    ('（专用PC / PC exclusive）', '（PC 专用 / PC exclusive）'),
    ('（范围效果 / AOE）', '（AOE）'),
    ('（poison或单元格 / Poison or Cell）', '（毒或细胞 / Poison or Cell）'),
    ('（升级 / Achievement）', '（成就 / Achievement）'),
    ('（项目 / Item）', '（道具 / Item）'),
    ('激光 （水平 / Horizontal）', '激光 (水平)（Laser (Horizontal)）'),
    ('激光 （垂直 / Vertical）', '激光 (垂直)（Laser (Vertical)）'),
    ('工人公会', '工人协会'),
    ('勇士协会', '战士协会'),
    ('" 勇士 "', '"战士"'),
    ('勇士的起步球', '战士的起步球'),
    ('因此，勇士是', '因此，战士是'),
    ('基本奖金', '基础加成'),
    ('马克斯奖金', '最大加成'),
    ('马克斯', '最大'),
    ('水平向上提升 Perk', '升级可选加成'),
    ('性格水平要求', '角色等级要求'),
    ('性格水平的进步', '角色等级进度'),
    ('性格水平', '角色等级'),
    ('性格升级奖励', '角色升级奖励'),
    ('开始的性格', '初始角色'),
    ('水平运行', '关卡对局'),
    ('比赛开始时可用', '对局开始时可用'),
    ('每一水平的', '每一级的'),
    ('收益水平', '角色等级机制'),
    ('游戏规律', '游戏机制'),
    ('迷你老板', '小首领'),
    ('老板', '首领'),
    ('滴滴', '掉落物'),
    ('冷冻射线', '冰冻射线'),
    ('冷却射线', '冰冻射线'),
    ('机率', '概率'),
    ('魅力', '魅惑'),
    ('导致敌人暴躁', '使敌人狂暴'),
    ('关键击球', '暴击'),
    ('麦机', '小麦收割机'),
    ('Frostburnt', '霜灼'),
    ('奖金', '加成'),
    ('字符', '角色'),
    ('性格', '角色'),
    ('坚力', '待补充条目'),
    ('球酒', '圆球图像'),
    ('凶手', '刺客'),
    ('贝尔塞克', '狂暴'),
    ('基本（Elemental）', '元素（Elemental）'),
    ('迷人（Charm）', '魅惑（Charm）'),
    ('雪风（Blizzard）', '暴风雪（Blizzard）'),
    ('驱逐的火焰', '放逐之焰'),
    ('块小瓦', '格'),
    ('小瓦', '格'),
]

# 正则规则（按行应用，跳过链接目标括号内不影响：模式均为 CJK 邻接，不会命中 URL/文件名）
REGEX = [
    ('标点·半角逗号→全角', re.compile(r'([一-鿿])\s*,\s*([一-鿿])'), r'\1，\2'),
    ('标点·半角分号→全角', re.compile(r'([一-鿿])\s*;\s*([一-鿿])'), r'\1；\2'),
    ('标点·半角冒号→全角', re.compile(r'([一-鿿])\s*:\s*([一-鿿])'), r'\1：\2'),
    ('排版·句末／(紧邻表格线)', re.compile(r'\s*／(?=\s*\|)'), ''),
]

def main():
    total = collections.Counter(); files_changed = []
    samples = collections.defaultdict(list)
    for d in DIRS:
        base = os.path.join(ROOT, d)
        for fn in sorted(os.listdir(base)):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(base, fn)
            with open(path, encoding='utf-8') as f:
                text = f.read()
            orig = text
            for old, new in EXACT:
                n = text.count(old)
                if n:
                    total[f'{old} → {new}'] += n
                    if len(samples[f'{old} → {new}']) < 2:
                        i = text.find(old)
                        samples[f'{old} → {new}'].append(text[max(0, i-15):i+len(old)+15].replace('\n', ' '))
                    text = text.replace(old, new)
            for name, pat, rep in REGEX:
                text, n = pat.subn(rep, text)
                if n:
                    total[f'[re] {name}'] += n
            if text != orig:
                files_changed.append(f'{d}/{fn}')
                if APPLY:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(text)
    for k in sorted(total, key=lambda k: -total[k]):
        print(f'{total[k]:5d}  {k}')
        for s in samples.get(k, []):
            print(f'        …{s}…')
    print(f'\n{"已写入" if APPLY else "试运行(未写盘)"}：{len(files_changed)} 个文件被修改')
    with open('/Users/Apple/zq/work/skill/temp/wiki_fix/脚本修复记录.txt', 'w', encoding='utf-8') as f:
        for k in sorted(total, key=lambda k: -total[k]):
            f.write(f'{total[k]:5d}  {k}\n')
        f.write(f'\n修改文件数 {len(files_changed)}\n')
        f.write('\n'.join(files_changed) + '\n')

if __name__ == '__main__':
    main()
