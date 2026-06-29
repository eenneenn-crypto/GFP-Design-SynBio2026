# GFP-Design-SynBio2026

**Track**: 2026 Protein Design in SynBio Challenges  
**Objective**: Design 6 novel GFP sequences with high initial brightness and extreme thermal stability (72°C, 10 min)

---

## Two Teams

### Team 32-603 — Data-driven computational optimization + Literature-validated mutations
| Seq_ID | Design | Scaffold | Strategy |
|--------|--------|----------|----------|
| 32-603_1 | sfGFP_Plus_v1 | sfGFP | FoldX-driven stabilization (7 mutations) |
| 32-603_2 | amacGFP_Plus_v3_max | amacGFP | Maximum FoldX optimization (8 mutations) |
| 32-603_3 | ppluGFP_Opt_v1_bright | ppluGFP | Ultra-stable scaffold + brightness optimization |
| 32-603_4 | cgreGFP_Opt_v1_bright | cgreGFP | Brightest WT scaffold + brightness optimization |
| 32-603_5 | avGFP_Superfold | avGFP | Cross-species superfolder transplant |
| 32-603_6 | sfGFP_N39D_Frenzel | sfGFP | Literature-verified mutation (885× fluorescence at 60°C) |

### Team default — Surface engineering + Progressive stabilization + Chimera design
| Seq_ID | Design | Scaffold | Strategy |
|--------|--------|----------|----------|
| default_1 | sfGFP_Plus_v2_TGP | sfGFP | TGP-inspired surface charge engineering |
| default_2 | amacGFP_Plus_v1 | amacGFP | Minimal stabilization (3 FoldX mutations) |
| default_3 | amacGFP_Plus_v2 | amacGFP | Moderate stabilization (7 mutations) |
| default_4 | ppluGFP_Opt_v2_surface | ppluGFP | Surface Glu engineering on ultra-stable scaffold |
| default_5 | cgreGFP_Opt_v2 | cgreGFP | Brightness combo optimization |
| default_6 | Chimera_sf_amac | sfGFP+amacGFP | Cross-species chimeric design |

---

## Repository Structure

```
GFP-Design-SynBio2026/
├── README.md
├── submissions/
│   ├── team_32-603/
│   │   ├── design_sequences.csv      # 6 submission-ready sequences
│   │   ├── design_rationale.pdf       # Design rationale document
│   │   └── design_rationale.md        # Markdown source
│   └── team_default/
│       ├── design_sequences.csv      # 6 submission-ready sequences
│       ├── design_rationale.pdf       # Design rationale document
│       └── design_rationale.md        # Markdown source
├── scripts/                           # Analysis & design scripts
│   ├── foldx_single_mutations.py
│   ├── foldx_batch_pipeline.py
│   ├── align_pdb_sequences.py
│   ├── analyze_foldx_results.py
│   ├── design_variants.py
│   ├── check_exclusions.py
│   └── generate_report.py
├── data/
│   ├── sequences/                     # Reference sequences
│   ├── pdb_download.py
│   └── mutation_lists/
├── results/
│   ├── GFP_design_report.xlsx        # Complete design table (12 designs)
│   ├── foldx_results.md
│   ├── design_rationale.md
│   ├── final_6_sequences.csv
│   └── supplementary_variants.csv
├── references/                        # Key literature PDFs
└── requirements.txt
```

## Requirements

- Python 3.10+ with packages listed in `requirements.txt`
- FoldX 5.1 (http://foldxsuite.crg.eu/) — for protein stability calculations
- R 4.4+ (optional, for visualization)
- GROMACS 2025+ (optional, for MD validation)

## Setup

```bash
pip install -r requirements.txt
```

## Design Process

1. **FoldX analysis**: Single-mutation stability (ΔG/ΔΔG) across 3 templates
2. **Data-driven brightness**: 141,572 mutation-brightness records from GFP_data.xlsx
3. **Literature integration**: sfGFP, TGP, usGFP, StayGold references
4. **Sequence generation**: 12 candidate designs across 5 scaffolds
5. **Exclusion check**: All sequences validated against Exclusion_List.csv (135,415 entries)
6. **Two-team split**: 6 sequences per team with diverse design strategies

## References

1. Pédelacq et al. (2006) Nat Biotechnol 24:79-88 — Superfolder GFP
2. Close et al. (2015) Proteins 83:1225-1237 — Thermal Green Protein (TGP)
3. Scott et al. (2018) Sci Rep 8:159 — Ultra-Stable GFP (usGFP)
4. Sarkisyan et al. (2016) Nature 533:397-401 — avGFP Fitness Landscape
5. Frenzel et al. (2018) — N39D thermostability enhancement
6. Hirano et al. (2022) Nat Biotechnol 40:1132-1142 — StayGold
7. Zhang et al. (2024) Nat Methods 21:657-665 — mBaoJin
