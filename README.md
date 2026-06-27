# GFP Design for 2026 SynBio Challenges

**Team**: [Team Name]  
**Track**: 2026 Protein Design in SynBio Challenges  
**Objective**: Design 6 novel GFP sequences with high initial brightness and extreme thermal stability (72°C, 10 min)

---

## 🏗 Repository Structure

```
GFP-Design-SynBio2026/
├── README.md                      # This file
├── scripts/                        # Analysis & design scripts
│   ├── foldx_single_mutations.py   # Run FoldX BuildModel for single mutations
│   ├── foldx_batch_pipeline.py     # Complete FoldX pipeline for 5 templates
│   ├── align_pdb_sequences.py      # Align PDB sequences to references
│   ├── analyze_foldx_results.py    # Parse FoldX output & compute DG/DDG
│   ├── design_variants.py          # Generate 6+ candidate sequences
│   ├── check_exclusions.py         # Validate against exclusion list
│   └── generate_report.py          # Create Excel summary report
├── data/
│   ├── sequences/                  # Reference sequences (from official package)
│   │   ├── sfGFP.fasta
│   │   ├── avGFP.fasta
│   │   ├── amacGFP.fasta
│   │   ├── cgreGFP.fasta
│   │   └── ppluGFP.fasta
│   ├── pdb_download.py             # Script to download PDB files (2B3P, 2WUR, 7LG4, 2HPW, 2G6X)
│   └── mutation_lists/             # Individual mutation files for FoldX
├── results/
│   ├── foldx_results.md            # FoldX single-mutation DG/DDG tables
│   ├── design_rationale.md         # Design strategy explanation
│   ├── final_6_sequences.csv       # 6 submission-ready sequences
│   └── supplementary_variants.csv  # Additional candidates for testing
├── references/                     # Key literature
│   ├── superfolder.pdf             # Pédelacq 2006 (sfGFP)
│   ├── TGP.pdf                     # Close 2015 (thermal green protein)
│   ├── usGFP.pdf                   # Scott 2018 (ultra-stable GFP)
│   └── fitness_landscape.pdf       # Sarkisyan 2016 (avGFP fitness)
└── requirements.txt                # Python dependencies
```

## 🔧 Environment Requirements

### Software
- **Python 3.10+** with packages listed in `requirements.txt`
- **FoldX 5.1** (http://foldxsuite.crg.eu/) — for protein stability calculations
- **R 4.4+** (optional, for visualization)
- **GROMACS 2025+** (optional, for MD validation)

### Python Dependencies
```bash
pip install -r requirements.txt
```

Main packages:
- `openpyxl` — Excel report generation
- `requests` — PDB downloading
- `biopython` — PDB file parsing
- `matplotlib` — data visualization (optional)

## 🚀 How to Reproduce

### Step 1: Download PDB Templates
```bash
python data/pdb_download.py
```

### Step 2: Run FoldX RepairPDB
```bash
cd scripts/
# For each template PDB:
# foldx --command=RepairPDB --pdb=2B3P.pdb
# foldx --command=RepairPDB --pdb=2WUR_Repair.pdb
# ...
```

### Step 3: Run Single-Mutation FoldX Analysis
```bash
python foldx_single_mutations.py
```
This:
- Generates individual_list files for 29 mutations across 3 templates
- Runs FoldX BuildModel (numberOfRuns=3)
- Extracts ΔG and ΔΔG from output

### Step 4: Analyze Results
```bash
python analyze_foldx_results.py
```
Produces stability ranking tables.

### Step 5: Design Candidate Sequences
```bash
python design_variants.py
```
Generates 11 candidate sequences from 5 templates with:
- Literature-based stabilizing mutations
- FoldX-validated mutations (ΔG and ΔΔG)
- Surface charge engineering (TGP-style)
- Brightness-optimizing mutations (from GFP_data.xlsx)

### Step 6: Generate Final Report
```bash
python generate_report.py
```
Creates Excel report with:
- Full sequences
- Design rationale
- ΔG and ΔΔG values
- Source references

## 📊 Design Strategy

| Template | WT_ΔG(kcal/mol) | Strategy |
|----------|:--------------:|----------|
| sfGFP (2B3P) | +3.40 | Add E172K + N149K + surface charge → ΔG turns negative |
| amacGFP (7LG4) | +3.55 | 3~8 stabilizing mutations (Y39N/N149K/E172K...) → all DDG<0 |
| avGFP (2WUR) | -2.02 | Import superfolder mutations (S30R/Y39N/F99S/M153T/V163A...) |
| cgreGFP (2HPW) | **-26.89** | Naturally super-stable; optimize brightness only |
| ppluGFP (2G6X) | **-49.88** | Naturally super-stable; optimize brightness only |

### Key Findings
- **amacGFP** has the most optimization potential: 11/11 tested mutations are stabilizing
- **cgreGFP** is naturally 6× brighter than avGFP
- **ppluGFP** is naturally the most stable (ΔG = −49.88)
- **E172K** is the best single mutation across templates

## 📚 Key References

1. **Pédelacq et al. 2006** — Superfolder GFP (sfGFP)  
   *Nat Biotechnol* 24:79-88. DOI: 10.1038/nbt1172

2. **Close et al. 2015** — Thermal Green Protein (TGP)  
   *Proteins* 83:1225-1237. DOI: 10.1002/prot.24699

3. **Scott et al. 2018** — Ultra-Stable GFP (usGFP/muGFP)  
   *Sci Rep* 8:159. DOI: 10.1038/s41598-017-18045-y

4. **Sarkisyan et al. 2016** — avGFP Fitness Landscape  
   *Nature* 533:397-401. DOI: 10.1038/nature17995

5. **Sokalingam et al. 2012** — Surface Lys→Arg mutagenesis  
   *PLoS ONE* 7:e40410. DOI: 10.1371/journal.pone.0040410

## ✅ Submission Checklist

- [ ] All 6 sequences within 220-250 aa
- [ ] All start with Methionine (M)
- [ ] No sequence in Exclusion_List.csv
- [ ] Design rationale documented in PDF
- [ ] Open-source code uploaded to GitHub
