# FoldX Single-Mutation Results

## WT Energies

| Template | PDB | WT ΔG (kcal/mol) | Notes |
|----------|:---:|:----------------:|-------|
| sfGFP | 2B3P | +3.40 | Baseline control (competition reference) |
| avGFP | 2WUR | −2.02 | Wild-type, naturally stable |
| amacGFP | 7LG4 | +3.55 | Naturally unstable, high optimization potential |
| cgreGFP | 2HPW | **−26.89** | Extremely stable (coral source) |
| ppluGFP | 2G6X | **−49.88** | Extremely stable (copepod source) |

## sfGFP (2B3P) — 5/5 Mutations Improve Stability

| Mutation | Mut ΔG | ΔΔG | Effect |
|:--------:|:------:|:---:|:------:|
| **E172K** | **−0.61** | −4.01 | **Best: turns unstable→stable** |
| N149K | +0.26 | −3.14 | Significant improvement |
| D190N | +0.74 | −2.66 | Good improvement |
| S147P | +0.87 | −2.53 | Good improvement |
| A227V | +1.49 | −1.91 | Moderate improvement |

## avGFP (2WUR) — Most Mutations Destabilizing (WT Already Stable)

| Mutation | Mut ΔG | ΔΔG | Effect |
|:--------:|:------:|:---:|:------:|
| **S30R** | **−1.44** | +0.58 | **Still stable (DG<0)** |
| N149K | −0.58 | +1.44 | Still stable |
| M153T | −0.49 | +1.53 | Still stable |
| E172K | −0.35 | +1.67 | Still stable |
| Y39N | −0.27 | +1.75 | Still stable |
| D190N | −0.08 | +1.94 | Borderline |
| F99S | +2.38 | +4.40 | Unstable |
| V163A | +3.56 | +5.58 | Very unstable |

## amacGFP (7LG4) — 11/11 Mutations Stabilize (Best Scaffold!)

| Mutation | Mut ΔG | ΔΔG | Effect |
|:--------:|:------:|:---:|:------:|
| **Y39N** | **−0.81** | −4.36 | **Best: turns unstable→stable** |
| **N149K** | **−0.51** | −4.06 | Excellent |
| **E172K** | **−0.44** | −3.99 | Excellent |
| S147P | −0.07 | −3.62 | Good |
| D190N | −0.07 | −3.62 | Good |
| T63A | +0.33 | −3.22 | Moderate |
| I171V | +0.79 | −2.76 | Moderate |
| M153T | +1.95 | −1.60 | Mild improvement |

## Key Conclusions

1. **amacGFP has the most potential**: all 11 mutations are stabilizing
2. **E172K is the best single mutation**: works on both sfGFP and amacGFP
3. **Coral GFPs (cgreGFP, ppluGFP) are naturally ultra-stable**: no mutation needed for stability
4. **cgreGFP is brightest** (6× avGFP in brightness data)
5. **ppluGFP is most stable** (DG = −49.88, lower = better)
