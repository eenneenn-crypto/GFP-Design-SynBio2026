"""Re-analyze FoldX results by absolute DG (not DDG)"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

data = {
    'avGFP (2WUR) [WT = -2.02]': [
        ('S30R', -1.44, 0.58), ('Y39N', -0.27, 1.75), ('Y39D', 0.18, 2.20),
        ('T63A', 0.77, 2.80), ('F99S', 2.38, 4.40), ('S147P', 0.18, 2.20),
        ('N149K', -0.58, 1.44), ('M153T', -0.49, 1.53), ('V163A', 3.56, 5.58),
        ('I171V', 1.16, 3.18), ('E172K', -0.35, 1.67), ('D190N', -0.08, 1.94),
        ('A227V', 3.11, 5.13)
    ],
    'amacGFP (7LG4) [WT = +3.55]': [
        ('Y39N', -0.81, -4.35), ('Y39D', 0.73, -2.82), ('T63A', 0.33, -3.21),
        ('F99S', 2.60, -0.94), ('S147P', -0.07, -3.61), ('N149K', -0.51, -4.06),
        ('M153T', 1.95, -1.59), ('V163A', 3.52, -0.03), ('I171V', 0.79, -2.75),
        ('E172K', -0.44, -3.98), ('D190N', -0.07, -3.62)
    ],
    'sfGFP (2B3P) [WT = +3.40]': [
        ('S147P', 0.87, -2.53), ('N149K', 0.26, -3.14), ('E172K', -0.61, -4.01),
        ('D190N', 0.74, -2.66), ('A227V', 1.49, -1.91)
    ],
    'cgreGFP (2HPW) [WT = -26.89]': [],
    'ppluGFP (2G6X) [WT = -49.88]': [],
}

print('=' * 75)
print('FoldX 结果分析：按绝对能量 DG 分类')
print('=' * 75)

for title, muts in data.items():
    print()
    print(title)
    print('-' * 65)
    print(f"  {'突变':<10} {'Mut DG':>8} {'DDG':>8}  {'DDG评价':<12} {'绝对稳定?':<10}")
    print('  ' + '-' * 55)
    
    for mut, me, ddg in muts:
        # DDG evaluation
        if ddg < -1.0:
            ddg_eval = '大幅稳定!'
        elif ddg < 0:
            ddg_eval = '轻微稳定'
        elif ddg < 1.0:
            ddg_eval = '轻微不稳定'
        elif ddg < 3.0:
            ddg_eval = '不稳定'
        else:
            ddg_eval = '很不稳定'
        
        # Absolute stability
        if me < 0:
            abs_eval = '稳定'
        elif me < 2.0:
            abs_eval = '偏高'
        else:
            abs_eval = '不稳定'
        
        # Combined assessment
        if ddg < 0 and me < 0:
            final = 'DDG+DG双优'
        elif ddg < 0 and me >= 0:
            final = 'DDG好但DG仍正'
        elif ddg >= 0 and me < 0:
            final = 'DDG差但DG可接受'
        else:
            final = '双差'
        
        print(f"  {mut:<10} {me:>+8.2f} {ddg:>+8.2f}  {ddg_eval:<12} {abs_eval:<10} [{final}]")
    
    if not muts:
        print(f"  珊瑚GFP天然已极稳！无需突变测试")

print()
print('=' * 75)
print('按 Mut_DG 排序的最佳突变（排名越靠前越好）')
print('=' * 75)

all_muts = []
for title, muts in data.items():
    for mut, me, ddg in muts:
        all_muts.append((me, mut, title.split('[')[0].strip(), ddg))

all_muts.sort()  # Most negative first

print(f"\n{'#':<3} {'突变':<10} {'骨架':<14} {'Mut DG':>8} {'DDG':>8}")
print('-' * 50)
for i, (me, mut, tmpl, ddg) in enumerate(all_muts[:15]):
    print(f"{i+1:<3} {mut:<10} {tmpl:<14} {me:>+8.2f} {ddg:>+8.2f}")
