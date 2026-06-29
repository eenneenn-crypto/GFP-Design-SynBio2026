# Team default — GFP Design Rationale
## 2026 Protein Design in SynBio Challenges

---

## Team Strategy Overview

**Design Philosophy**: Surface charge engineering + Progressive scaffold optimization + Cross-species chimera

Our team employs **four complementary approaches** across 5 different GFP scaffolds to maximize the dual-performance score (Brightness × Thermal Stability):

| Approach | Description | Designs |
|----------|-------------|---------|
| A. Surface charge engineering | TGP-inspired Glu enrichment to reduce aggregation | G2, G7 |
| B. Progressive stabilization | Stepwise addition of FoldX-verified mutations | G3, G4 |
| C. Brightness combo optimization | Multiple brightness-enhancing mutations on brightest scaffold | G9 |
| D. Cross-species chimera | Hybrid backbone combining best features from multiple GFP species | G11 |

---

## Design 1 — sfGFP_Plus_v2_TGP (default_1)

- **Scaffold**: sfGFP (PDB: 2B3P, 238 aa)
- **WT ΔG**: +3.40 kcal/mol
- **Strategy**: TGP-inspired surface charge engineering + core stabilization

### Mutations

| Mutation | Source | Rationale |
|----------|--------|-----------|
| Q69L | usGFP (Scott 2018) | Core hydrophobic packing |
| K79E | TGP (Close 2015) | **Surface Glu → negative charge, reduce aggregation** |
| N149K | FoldX (ΔΔG = -3.14) | Surface charge optimization |
| N164Y | usGFP (Scott 2018) | Core aromatic stacking |
| E172K | FoldX (ΔΔG = -4.01) | **Best single mutation across all templates** |
| Q204E | TGP (Close 2015) | **Surface Glu → increase negative charge density** |

**Design Logic**: The Thermal Green Protein (TGP, Close 2015) demonstrated that engineering negatively charged Glu residues on the GFP surface dramatically increases thermostability by reducing aggregation and improving solubility. We apply this proven strategy to sfGFP: K79E and Q204E add two negative surface charges while preserving sfGFP's excellent folding characteristics. Combined with core stability mutations (Q69L, N164Y, E172K), this design targets high brightness while gaining significant thermostability.

---

## Design 2 — amacGFP_Plus_v1 (default_2)

- **Scaffold**: amacGFP (PDB: 7LG4, 238 aa)
- **WT ΔG**: +3.55 kcal/mol, **WT Brightness**: 3.97
- **Strategy**: Minimal modification — only 3 high-impact FoldX mutations

### Mutations

| Mutation | ΔΔG (kcal/mol) | Site Function |
|----------|----------------|---------------|
| Y39N | -4.36 | β-strand 2, core H-bond network |
| N149K | -4.06 | Surface, charge optimization |
| E172K | -3.06 | β-barrel surface, universal stabilizer |

**Design Logic**: This is the most conservative design — only 3 mutations, each independently verified by FoldX to have ΔΔG < -3.0 kcal/mol on the amacGFP (7LG4) structure. Y39N alone turns amacGFP from unstable (ΔG = +3.55) to stable (ΔG = -0.81). The minimal perturbation approach maximizes the chance of preserving amacGFP's naturally bright chromophore microenvironment (1.8× avGFP) while achieving thermodynamic stability. This serves as a valuable comparison point for more heavily mutated designs (default_3, team 32-603_2).

---

## Design 3 — amacGFP_Plus_v2 (default_3)

- **Scaffold**: amacGFP (PDB: 7LG4, 238 aa)
- **WT ΔG**: +3.55 kcal/mol, **WT Brightness**: 3.97
- **Strategy**: Moderate optimization — FoldX mutations + usGFP core packing

### Mutations

| Mutation | ΔΔG / Source | Rationale |
|----------|--------------|-----------|
| Y39N | -4.36 | Core stabilization (primary) |
| Q69L | usGFP | Core hydrophobic packing |
| S147P | -2.53 (FoldX) | Loop rigidification |
| N149K | -4.06 | Surface charge |
| N164Y | usGFP | Core aromatic stacking |
| E172K | -3.06 | Universal stabilizer |
| D190N | -2.66 | Loop stabilization |

**Design Logic**: This intermediate design (7 mutations) bridges the minimal (default_2, 3 mutations) and maximum (team 32-603_2, 8 mutations) approaches on amacGFP. All 7 mutations are independently verified as stabilizing. The inclusion of usGFP's core packing mutations (Q69L, N164Y) adds an additional stabilization mechanism by filling the hydrophobic core more efficiently.

---

## Design 4 — ppluGFP_Opt_v2_surface (default_4)

- **Scaffold**: ppluGFP (PDB: 2G6X, 222 aa)
- **WT ΔG**: -49.88 kcal/mol, **WT Brightness**: 4.23
- **Strategy**: Surface Glu engineering on naturally ultra-stable scaffold

### Mutations

| Mutation | Rationale |
|----------|-----------|
| S73E | **Surface Glu → negative charge** |
| S147E | **Surface Glu → negative charge** |
| S174E | **Surface Glu → negative charge** |
| L206E | Brightness optimization + surface charge |
| Y88F | Hydrophobic core packing optimization |
| S148A | Remove phosphorylation site |
| R211F | C-terminal stabilization |

**Design Logic**: ppluGFP is already the most stable scaffold available (ΔG = -49.88 kcal/mol). Following the TGP paradigm (Close 2015), we enhance surface charge density by mutating 3 serine residues to glutamate (S73E, S147E, S174E). These surface Glu residues create a negatively charged shell that prevents aggregation under thermal stress. The L206E mutation serves a dual purpose: brightness enhancement and additional surface charge. This design explores whether surface engineering can further improve the already exceptional stability of ppluGFP.

---

## Design 5 — cgreGFP_Opt_v2 (default_5)

- **Scaffold**: cgreGFP (PDB: 2HPW, 235 aa)
- **WT ΔG**: -26.89 kcal/mol, **WT Brightness**: 4.50
- **Strategy**: Brightness combo — multiple verified bright mutations

### Mutations

| Mutation | Brightness (log) | Rationale |
|----------|-----------------|-----------|
| K8Q | 4.48 (est.) | N-terminal stabilization |
| K167M | **4.57** | Brightest single mutant |
| D170E | 4.56 | Chromophore microenvironment |
| L197P | 4.53 (est.) | C-terminal loop optimization |

**Design Logic**: cgreGFP is already both the brightest WT (4.50 log) and highly stable (ΔG = -26.89). This design takes a pure brightness optimization approach, combining 4 mutations that push brightness even further. K167M is the single highest-brightness mutation identified in the training dataset (4.57 log). The combination of K167M + D170E + L197P targets the chromophore microenvironment from multiple angles — core packing, electrostatic environment, and loop flexibility. K8Q provides N-terminal stability.

---

## Design 6 — Chimera_sf_amac (default_6)

- **Scaffold**: sfGFP backbone + amacGFP features (238 aa)
- **Strategy**: Cross-species chimeric design

### Key Features

| Feature | Source | Rationale |
|---------|--------|-----------|
| sfGFP backbone scaffold | sfGFP (2B3P) | Proven folding efficiency |
| N149K + E172K | FoldX universal | Cross-template stabilizers |
| K79E + Q204E | TGP surface engineering | Anti-aggregation |
| amacGFP chromophore environment | amacGFP | Higher intrinsic brightness |
| Q69L + N164Y | usGFP core stacking | Hydrophobic core stability |

**Design Logic**: This is our most innovative design — a cross-species chimera that combines the best features from multiple GFP families:
- **Backbone**: sfGFP's proven folding scaffold (competition benchmark)
- **Stability**: FoldX-validated universal stabilizers (N149K, E172K)
- **Surface**: TGP-style Glu engineering (K79E, Q204E) for thermostability
- **Core**: usGFP hydrophobic packing (Q69L, N164Y)
- **Brightness**: amacGFP-derived chromophore microenvironment

This integrated approach represents a departure from single-scaffold engineering, aiming to create a novel GFP that inherits the best properties from multiple evolutionary lineages.

---

## Summary

| Seq_ID | Design Name | Scaffold | Length | Strategy Category |
|--------|-------------|----------|--------|-------------------|
| default_1 | sfGFP_Plus_v2_TGP | sfGFP | 238 | Surface charge engineering |
| default_2 | amacGFP_Plus_v1 | amacGFP | 238 | Minimal stabilization (3 mutations) |
| default_3 | amacGFP_Plus_v2 | amacGFP | 238 | Moderate stabilization (7 mutations) |
| default_4 | ppluGFP_Opt_v2_surface | ppluGFP | 222 | Surface engineering on ultra-stable scaffold |
| default_5 | cgreGFP_Opt_v2 | cgreGFP | 235 | Brightness combo |
| default_6 | Chimera_sf_amac | sfGFP+amacGFP | 238 | Cross-species chimera |

---

## References

1. Pédelacq J-D, Cabantous S, Tran T, Terwilliger TC, Waldo GS. Engineering and characterization of a superfolder green fluorescent protein. Nat Biotechnol 2006;24:79-88.
2. Close DW, Paul CD, Langan PS, et al. Thermal green protein, an extremely stable, nonaggregating fluorescent protein created by structure-guided surface engineering. Proteins 2015;83:1225-1237.
3. Scott DJ, Gunn NJ, Yong KJ, et al. A novel ultra-stable, monomeric green fluorescent protein for direct volumetric imaging of whole organs. Sci Rep 2018;8:159.
4. Sarkisyan KS, Bolotin DA, Meer MV, et al. Local fitness landscape of the green fluorescent protein. Nature 2016;533:397-401.
5. Sokalingam S, Raghunathan G, Soundrarajan N, Lee SG. A study on the effect of surface lysine to arginine mutagenesis on protein stability and structure using green fluorescent protein. PLoS ONE 2012;7:e40410.
6. Hirano M, Ando R, Shimozono S, et al. A highly photostable and bright green fluorescent protein. Nat Biotechnol 2022;40:1132-1142.
