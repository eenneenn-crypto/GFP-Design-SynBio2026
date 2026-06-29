# GFP-Design-SynBio2026

**Track**: 2026 Protein Design in SynBio Challenges

---

## Two Teams

### Team 32-603 - Data-driven + Literature-verified
| Seq_ID | Design | Scaffold | Strategy |
|--------|--------|----------|----------|
| 32-603_1 | sfGFP_Plus_v1 | sfGFP | FoldX stabilization (7 mutations) |
| 32-603_2 | amacGFP_Plus_v3_max | amacGFP | Max FoldX optimization (8 mutations) |
| 32-603_3 | ppluGFP_Opt_v1_bright | ppluGFP | Ultra-stable + brightness optimization |
| 32-603_4 | cgreGFP_Opt_v1_bright | cgreGFP | Brightest WT + brightness optimization |
| 32-603_5 | avGFP_Superfold | avGFP | sfGFP superfolder cross-species transplant |
| 32-603_6 | sfGFP_N39D_top2025 | Top 2025 Seq | **N39D on 2025 top sequence** |

### Team default - Surface engineering + Chimera
| Seq_ID | Design | Scaffold | Strategy |
|--------|--------|----------|----------|
| default_1 | sfGFP_Plus_v2_TGP | sfGFP | TGP-inspired surface charge engineering |
| default_2 | amacGFP_Plus_v1 | amacGFP | Minimal stabilization (3 FoldX mutations) |
| default_3 | amacGFP_Plus_v2 | amacGFP | Moderate stabilization (7 mutations) |
| default_4 | ppluGFP_Opt_v2_surface | ppluGFP | Surface Glu engineering |
| default_5 | cgreGFP_Opt_v2 | cgreGFP | Brightness combo optimization |
| default_6 | Chimera_sf_amac | sfGFP+amacGFP | Cross-species chimera |

## Repository Structure
```
submissions/
  team_32-603/    - CSV + PDF design rationale
  team_default/   - CSV + PDF design rationale
scripts/          - Analysis & design scripts
data/             - Reference sequences
results/          - FoldX results, design report
references/       - Key literature PDFs
```
