#!/usr/bin/env python3
"""
foldx_single_mutations.py — Run FoldX BuildModel for single mutations
on the 5 reference GFP templates.

Requirements:
- FoldX 5.1 installed at FOLDX_PATH
- PDB files (repaired) in the same directory

Output: Dif_*.fxout files with WT and mutant energies
"""

import os, subprocess, time

FOLDX = 'foldx_1_20270131.exe'  # Update path as needed
WORK_DIR = '.'  # Directory containing PDBs and FoldX binary

# Reference sequences (from competition data pack)
SEQUENCES = {
    'sfGFP': 'MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGMDELYK',
    'avGFP': 'MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTLSYGVQCFSRYPDHMKQHDFFKSAMPEGYVQERTIFFKDDGNYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNVYIMADKQKNGIKVNFKIRHNIEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITHGMDELYK',
    'amacGFP': 'MSKGEELFTGIVPVLIELDGDVHGHKFSVRGEGEGDADYGKLEIKFICTTGKLPVPWPTLVTTLSYGILCFARYPEHMKMNDFFKSAMPEGYIQERTIFFQDDGKYKTRGEVKFEGDTLVNRIELKGMDFKEDGNILGHKLEYNFNSHNVYIMPDKANNGLKVNFKIRHNIEGGGVQLADHYQTNVPLGDGPVLIPINHYLSCQTAISKDRNETRDHMVFLEFFSACGHTHGMDELYK',
}

# Template → PDB file → WT energy (from RepairPDB)
TEMPLATES = {
    'sfGFP': {'pdb': '2B3P_Repair.pdb', 'wt_energy': 3.3986},
    'avGFP': {'pdb': '2WUR_Repair.pdb', 'wt_energy': -2.0219},
    'amacGFP': {'pdb': '7LG4_Repair.pdb', 'wt_energy': 3.5458},
}

# All mutations to test (in reference sequence numbering)
MUTATIONS = [
    'S30R', 'Y39N', 'Y39D', 'T63A', 'F64L', 'F99S', 'S147P', 'N149K',
    'M153T', 'V163A', 'I171V', 'E172K', 'D190N', 'A227V'
]


def run_foldx_single(pdb_file, mutation_str):
    """Run FoldX BuildModel with a single mutation"""
    list_path = os.path.join(WORK_DIR, 'individual_list_batch.txt')
    with open(list_path, 'w') as f:
        f.write(mutation_str)

    base_name = pdb_file.replace('.pdb', '')
    dif_file = os.path.join(WORK_DIR, f'Dif_{base_name}.fxout')

    # Backup existing output
    dif_bak = dif_file + '.bak'
    if os.path.exists(dif_file):
        os.replace(dif_file, dif_bak)

    result = subprocess.run(
        [os.path.join(WORK_DIR, FOLDX),
         '--command=BuildModel',
         f'--pdb={pdb_file}',
         '--mutant-file=individual_list_batch.txt',
         '--output-dir=.',
         '--numberOfRuns=3'],
        cwd=WORK_DIR, capture_output=True, text=True, timeout=180
    )

    # Parse result
    mut_energy = None
    if os.path.exists(dif_file):
        with open(dif_file) as f:
            lines = f.readlines()
        for line in lines:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                try:
                    mut_energy = float(parts[1])
                except ValueError:
                    pass

    # Cleanup
    for f in [dif_bak]:
        if os.path.exists(f):
            os.remove(f)
    for i in [1, 2, 3]:
        for p in [f'WT_{base_name}.pdb', f'{base_name}_{i}.pdb']:
            p_path = os.path.join(WORK_DIR, p)
            if os.path.exists(p_path):
                os.remove(p_path)

    return result.returncode == 0, mut_energy


def check_mutation_applicable(template_name, mut_name):
    """Check if a mutation is applicable (scaffold has the expected WT residue)"""
    seq = SEQUENCES[template_name]
    wt_aa = mut_name[0]
    pos = int(mut_name[1:-1])
    if pos > len(seq):
        return False
    return seq[pos - 1] == wt_aa


def main():
    results = []
    for tmpl, cfg in TEMPLATES.items():
        seq = SEQUENCES[tmpl]
        wt = cfg['wt_energy']

        for mut in MUTATIONS:
            if not check_mutation_applicable(tmpl, mut):
                continue

            pdb_pos = int(mut[1:-1])
            foldx_mut = f'{mut[0]}{pdb_pos}{mut[-1]};'
            ok, me = run_foldx_single(cfg['pdb'], foldx_mut)

            if ok and me is not None:
                ddg = me - wt
                results.append((tmpl, mut, wt, me, ddg))
                print(f'{tmpl} {mut}: WT={wt:.2f} Mut={me:.2f} DDG={ddg:+.2f}')
            else:
                print(f'{tmpl} {mut}: FAILED')

    # Summary table
    print('\n' + '=' * 60)
    print('FOLDX SINGLE MUTATION SUMMARY')
    print('=' * 60)
    for tmpl, mut, wt, me, ddg in sorted(results, key=lambda x: x[4]):
        print(f'{tmpl:<10} {mut:<8} DG={me:+.2f}  DDG={ddg:+.2f}')


if __name__ == '__main__':
    main()
