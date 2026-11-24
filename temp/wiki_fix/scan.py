#!/usr/bin/env python3
"""扫描 BALL x PIT Wiki 中文离线版的翻译与排版问题，输出清单。只读不改。"""
import os, re, sys, collections

ROOT = '/Users/Apple/zq/work/skill/temp/BALL x PIT Wiki 中文离线版'
OUT = '/Users/Apple/zq/work/skill/temp/wiki_fix/问题清单.md'
DIRS = ['articles', 'categories', 'templates', 'files', 'data', 'site', 'navigation']

CJK = r'[一-鿿]'
# (类名, 正则, 严重度) 严重度: A=机翻残渣 B=误译/不统一 C=标点排版
PATTERNS = [
    ('A 机翻·处理伤害', r'处理\d', 'A'),
    ('A 机翻·QQ模板残渣', r'QQ\s', 'A'),
    ('A 机翻·打个电话', r'打个电话', 'A'),
    ('A 机翻·豪华豪华', r'豪华豪华', 'A'),
    ('A 机翻·骨球ista', r'[一-鿿]ista|ista（', 'A'),
    ('A 机翻·聚会(指建筑/据点)', r'是一个聚会', 'A'),
    ('B 误译·字符', r'字符', 'B'),
    ('B 误译·性格(=角色)', r'性格', 'B'),
    ('B 误译·老板', r'老板', 'B'),
    ('B 误译·坚力', r'坚力', 'B'),
    ('B 误译·球酒', r'球酒', 'B'),
    ('B 误译·凶手(Assassin)', r'凶手', 'B'),
    ('B 误译·贝尔塞克', r'贝尔塞克', 'B'),
    ('B 误译·基本(Elemental)', r'基本（Elemental）', 'B'),
    ('B 误译·迷人(Charm)', r'迷人（Charm）', 'B'),
    ('B 误译·雪风(Blizzard)', r'雪风', 'B'),
    ('B 误译·驱逐的火焰', r'驱逐的火焰', 'B'),
    ('B 误译·麦机', r'麦机', 'B'),
    ('B 误译·冷冻/冷却射线', r'冷冻射线|冷却射线', 'B'),
    ('B 误译·勇士', r'勇士', 'B'),
    ('B 误译·机率', r'机率', 'B'),
    ('B 误译·关键击球', r'关键击球', 'B'),
    ('B 误译·滴滴', r'滴滴', 'B'),
    ('B 误译·游戏规律', r'游戏规律', 'B'),
    ('B 误译·奖金(=加成)', r'奖金', 'B'),
    ('B 误译·比赛(run)', r'比赛开始|比赛模式', 'B'),
    ('B 误译·水平运行', r'水平运行', 'B'),
    ('B 误译·每一水平的', r'每一水平的', 'B'),
    ('B 误译·性格水平', r'性格水平', 'B'),
    ('B 误译·收益水平', r'收益水平', 'B'),
    ('B 误译·Perk残留', r'Perk', 'B'),
    ('B 误译·旗手(Flagellant)', r'旗手', 'B'),
    ('B 误译·小费者', r'小费者', 'B'),
    ('B 误译·Frostburnt', r'Frostburnt', 'B'),
    ('B 误译·小瓦', r'小瓦', 'B'),
    ('B 误译·无摩擦', r'无摩擦', 'B'),
    ('B 误译·收获得到(收获到\d)', r'收获到\d', 'B'),
    ('C 标点·半角逗号', CJK + r',\s*' + CJK, 'C'),
    ('C 标点·半角分号', CJK + r';\s*' + CJK, 'C'),
    ('C 标点·半角冒号', CJK + r':\s*' + CJK, 'C'),
    ('C 排版·尾随／', r'／\s*$', 'C'),
    ('C 排版·全角括号夹斜杠英文', r'（[^）<>]{0,20} / [^）<>]{0,20}）', 'C'),
    ('C 排版·英文序残留(通过…通过)', r'通过 \[.{1,20}\]\(.{1,30}\)\.', 'C'),
]

def main():
    rows = []          # (dir, file, line, cls, sev, excerpt)
    for d in DIRS:
        base = os.path.join(ROOT, d)
        for fn in sorted(os.listdir(base)):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(base, fn)
            with open(path, encoding='utf-8') as f:
                for i, line in enumerate(f, 1):
                    for name, pat, sev in PATTERNS:
                        for m in re.finditer(pat, line):
                            s = max(0, m.start() - 12)
                            e = min(len(line), m.end() + 12)
                            rows.append((d, fn, i, name, sev, line[s:e].strip()))
    # 汇总
    by_cls = collections.Counter(r[3] for r in rows)
    by_file = collections.defaultdict(list)
    for r in rows:
        by_file[(r[0], r[1])].append(r)

    with open(OUT, 'w', encoding='utf-8') as out:
        out.write('# 翻译与排版问题清单（自动扫描）\n\n')
        out.write('扫描时间：2026-11-24 · 严重度：A=机翻残渣（不可读） B=误译/用词不统一 C=标点排版\n\n')
        out.write('## 一、按问题类别统计\n\n| 类别 | 命中数 |\n| --- | ---: |\n')
        for name, n in sorted(by_cls.items()):
            out.write(f'| {name} | {n} |\n')
        out.write(f'\n共 {len(rows)} 处命中，涉及 {len(by_file)} 个文件。\n\n')
        out.write('## 二、逐文件明细\n\n')
        for (d, fn), items in sorted(by_file.items()):
            sevs = ''.join(sorted(set(i[4] for i in items)))
            out.write(f'### {d}/{fn}（{sevs}，{len(items)} 处）\n\n')
            seen = set()
            for _, _, ln, name, sev, exc in items:
                key = (ln, name)
                if key in seen:
                    continue
                seen.add(key)
                out.write(f'- L{ln} [{name}] …{exc}…\n')
            out.write('\n')
    print(f'共 {len(rows)} 处命中，{len(by_file)} 个文件，类别 {len(by_cls)} 个 -> {OUT}')
    # 控制台摘要
    for name, n in sorted(by_cls.items(), key=lambda x: -x[1]):
        print(f'  {n:5d}  {name}')

if __name__ == '__main__':
    main()
