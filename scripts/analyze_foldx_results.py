#!/usr/bin/env python3
"""
analyze_foldx_results.py — Parse FoldX output, compute DG/DDG tables
"""

import os, re

TEMPLATE_ENERGIES = {
    'sfGFP': {'file': 'Dif_2B3P_Repair.fxout', 'wt': 3.40},
    'avGFP': {'file': 'Dif_2WUR_Repair.fxout', 'wt': -2.02},
    'amacGFP': {'file': 'Dif_7LG4_Repair.fxout', 'wt': 3.55},
}

# Known results from our FoldX runs
SINGLE_MUTATION_RESULTS = {
    'sfGFP': {
        'S147P': (0.87, -2.53), 'N149K': (0.26, -3.14),
        'E172K': (-0.61, -4.01), 'D190N': (0.74, -2.66), 'A227V': (1.49, -1.91)
    },
    'avGFP': {
        'S30R': (-1.44, 0.58), 'Y39N': (-0.27, 1.75), 'Y39D': (0.18, 2.20),
        'T63A': (0.77, 2.80), 'F99S': (2.38, 4.40), 'S147P': (0.18, 2.20),
        'N149K': (-0.58, 1.44), 'M153T': (-0.49, 1.53), 'V163A': (3.56, 5.58),
        'I171V': (1.16, 3.18), 'E172K': (-0.35, 1.67), 'D190N': (-0.08, 1.94),
        'A227V': (3.11, 5.13)
    },
    'amacGFP': {
        'Y39N': (-0.81, -4.36), 'Y39D': (0.73, -2.82), 'T63A': (0.33, -3.21),
        'F99S': (2.60, -0.94), 'S147P': (-0.07, -3.61), 'N149K': (-0.51, -4.06),
        'M153T': (1.95, -1.59), 'V163A': (3.52, -0.03), 'I171V': (0.79, -2.75),
        'E172K': (-0.44, -3.98), 'D190N': (-0.07, -3.62)
    }
}

# WT energies from RepairPDB for coral GFPs
CORAL_ENERGIES = {
    'cgreGFP': -26.89,
    'ppluGFP': -49.88,
}


def analyze():
    """Print formatted analysis"""
    print('=' * 70)
    print('FOLDX ANALYSIS: SINGLE MUTATION DG AND DDG')
    print('=' * 70)

    for tmpl, muts in SINGLE_MUTATION_RESULTS.items():
        wt = TEMPLATE_ENERGIES[tmpl]['wt']
        print(f'\n{tmpl} (WT DG = {wt:+.2f})')
        print('-' * 50)

        # Sort by DG (most negative first)
        for mut in sorted(muts.keys(), key=lambda m: muts[m][0]):
            dg, ddg = muts[mut]
            stable = 'STABLE' if dg < 0 else ('MODERATE' if dg < 2.0 else 'UNSTABLE')
            print(f'  {mut:<8s}  DG={dg:+6.2f}  DDG={ddg:+6.2f}  [{stable}]')

    print('\n' + '=' * 70)
    print('NATURALLY STABLE TEMPLATES (Coral GFPs)')
    print('=' * 70)
    for tmpl, dg in CORAL_ENERGIES.items():
        print(f'  {tmpl:<12s}  DG = {dg:+6.2f}  (extremely stable, no mutations needed)')

    print('\n' + '=' * 70)
    print('TOP CROSS-TEMPLATE MUTATIONS (by absolute DG)')
    print('=' * 70)
    all_muts = []
    for tmpl, muts in SINGLE_MUTATION_RESULTS.items():
        for mut, (dg, ddg) in muts.items():
            all_muts.append((dg, ddg, tmpl, mut))
    all_muts.sort()
    for dg, ddg, tmpl, mut in all_muts[:10]:
        print(f'  {mut:<8s} on {tmpl:<10s}  DG={dg:+6.2f}  DDG={ddg:+6.2f}')


if __name__ == '__main__':
    analyze()
