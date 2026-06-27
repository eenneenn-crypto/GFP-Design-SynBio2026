# Design Rationale for Final 6 Sequences

## Competition Rules
- **Baseline**: sfGFP (brightness = 100%)
- **Scoring**: Initial brightness × Thermal stability retention (72°C, 10 min)
- **6 sequences**, each 220-250 aa, start with M
- **Full-sequence free design**: no mutation count limit

## Overall Strategy

We use **three complementary approaches** across 5 different GFP scaffolds:

### Approach A: Stability-optimized (FoldX-driven)
Using FoldX BuildModel to identify mutations with **negative ΔG** (stable) and favorable **ΔΔG**.

### Approach B: Surface charge engineering (TGP-inspired)
Following Close et al. 2015 — increase negative surface charges to reduce aggregation and improve solubility.

### Approach C: Brightness-optimized (data-driven)
Using the GFP_data.xlsx brightness dataset (141,573 records) to select brightness-enhancing mutations.

---

## 6 Final Sequences

### G1: sfGFP_Plus_v1
- **Scaffold**: sfGFP (baseline, known to fold well)
- **Mutations**: Q69L, S147P, N149K, N164Y, E172K, D190N, A227V
- **Rationale**: Take competition baseline sfGFP and fix its only weakness — instability (WT DG = +3.40). E172K alone brings DG to −0.61
- **Literature support**: Pédelacq 2006 (sfGFP), Scott 2018 (usGFP Q69L/N164Y), this FoldX analysis

### G2: sfGFP_TGP_surface
- **Scaffold**: sfGFP
- **Mutations**: Q69L, K79E, N149K, N164Y, E172K, Q204E
- **Rationale**: Add TGP-style surface Glu residues (K79E, Q204E) to increase negative surface charge
- **Literature support**: Close 2015 (TGP surface engineering)

### G3: amacGFP_core3
- **Scaffold**: amacGFP (naturally bright, 1.8× avGFP)
- **Mutations**: Y39N, N149K, E172K
- **Rationale**: 3 mutations that each turn WT DG from +3.55 to negative, all with ΔΔG < −3.9
- **Literature support**: This FoldX analysis (all 3 verified on 7LG4 PDB)

### G4: amacGFP_plus7
- **Scaffold**: amacGFP
- **Mutations**: Y39N, Q69L, S147P, N149K, N164Y, E172K, D190N
- **Rationale**: Maximum safe optimization — 7 mutations, all with negative ΔΔG
- **Literature support**: This FoldX analysis + Scott 2018

### G5: ppluGFP_bright
- **Scaffold**: ppluGFP (Pontellina plumata GFP, 3.2× avGFP brightness)
- **Mutations**: K48E, S118E, L199H, G206E, A221E
- **Rationale**: Naturally most stable (DG = −49.88). Add brightness mutations from data + surface Glu for solubility
- **Literature support**: GFP_data.xlsx, TGP surface engineering

### G6: cgreGFP_bright
- **Scaffold**: cgreGFP (Clytina gregaria GFP, 6.0× avGFP brightness)
- **Mutations**: R78G, K167M, A168V, M172E
- **Rationale**: Naturally brightest scaffold + extremely stable (DG = −26.89). Add top brightness-enhancing single mutations (all >4.53 log brightness)
- **Literature support**: GFP_data.xlsx (brightness maxima)

## Exclusion Check
All 6 sequences have been validated against the official Exclusion_List.csv (135,414 sequences) — none are present.

## References
1. Pédelacq JD, et al. (2006) *Nat Biotechnol* — superfolder GFP
2. Close DW, et al. (2015) *Proteins* — TGP surface engineering
3. Scott DJ, et al. (2018) *Sci Rep* — ultra-stable GFP (usGFP)
4. Sarkisyan KS, et al. (2016) *Nature* — avGFP fitness landscape
5. Sokalingam S, et al. (2012) *PLoS ONE* — surface K→R mutations
