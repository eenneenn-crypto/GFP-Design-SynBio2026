"""Run FoldX BuildModel for each mutation independently and collect results"""
import os, subprocess, time

FOLDX = r'D:\openclaw_work\foldx5\foldx_1_20270131.exe'
WORK_DIR = r'D:\openclaw_work\foldx5'

# Templates and their valid mutations
# Format: (output_name, pdb_file, list_of_mutations)
# Each mutation: (mutation_name, res_string)
jobs = [
    ('2WUR_avGFP', '2WUR_Repair.pdb', [
        ('S30R', 'SA30R;'),
        ('Y39N', 'YA39N;'),
        ('Y39D', 'YA39D;'),
        ('T63A', 'TA63A;'),
        ('F99S', 'FA99S;'),
        ('S147P', 'SA147P;'),
        ('N149K', 'NA149K;'),
        ('M153T', 'MA153T;'),
        ('V163A', 'VA163A;'),
        ('I171V', 'IA171V;'),
        ('E172K', 'EA172K;'),
        ('D190N', 'DA190N;'),
        ('A227V', 'AA227V;'),
    ]),
    ('7LG4_amacGFP', '7LG4_Repair.pdb', [
        ('Y39N', 'YA39N;'),
        ('Y39D', 'YA39D;'),
        ('T63A', 'TA63A;'),
        ('F99S', 'FA99S;'),
        ('S147P', 'SA147P;'),
        ('N149K', 'NA149K;'),
        ('M153T', 'MA153T;'),
        ('V163A', 'VA163A;'),
        ('I171V', 'IA171V;'),
        ('E172K', 'EA172K;'),
        ('D190N', 'DA190N;'),
    ]),
    ('2B3P_sfGFP', '2B3P_A_Repair_1.pdb', [
        ('S147P', 'SA147P;'),
        ('N149K', 'NA149K;'),
        ('E172K', 'EA172K;'),
        ('D190N', 'DA190N;'),
        ('A227V', 'AA227V;'),
    ]),
]

# Setup: read the final Dif file reference to get WT energy
def get_wt_info(pdb_name):
    """Get WT total energy from existing data"""
    dif_path = os.path.join(WORK_DIR, 'Dif_{}.fxout'.format(pdb_name.replace('.pdb', '')))
    if os.path.exists(dif_path):
        with open(dif_path) as f:
            lines = f.readlines()
        # Find the first data line (after header), get its total energy (column 1)
        for i, line in enumerate(lines):
            if line.strip().startswith('Pdb'):
                # Header line found, next data line is WT
                if i + 1 < len(lines):
                    parts = lines[i+1].strip().split('\t')
                    if len(parts) >= 2:
                        return lines[i+1].strip(), float(parts[1])
    return None, 0

# Run each mutation
results = []

for tmpl_name, pdb_file, mutations in jobs:
    base_name = pdb_file.replace('.pdb', '')
    print('\n' + '=' * 60)
    print('TEMPLATE: {} (PDB: {})'.format(tmpl_name, pdb_file))
    print('=' * 60)
    
    # Get WT info
    wt_line, wt_energy = get_wt_info(base_name)
    if wt_line:
        print('  WT energy: {:.4f}'.format(wt_energy))
    else:
        print('  WARNING: No WT info found, will need to recalculate')
    
    for mut_name, mut_str in mutations:
        # Create individual_list file
        list_path = os.path.join(WORK_DIR, 'individual_list_batch.txt')
        with open(list_path, 'w', encoding='ascii') as f:
            f.write(mut_str)
        
        print('\n  Running {} ({}): '.format(mut_name, mut_str.strip()), end='', flush=True)
        
        # Backup existing Dif/Average files (FoldX will overwrite)
        dif_backup = os.path.join(WORK_DIR, 'Dif_{}.fxout.bak'.format(base_name))
        avg_backup = os.path.join(WORK_DIR, 'Average_{}.fxout.bak'.format(base_name))
        dif_file = os.path.join(WORK_DIR, 'Dif_{}.fxout'.format(base_name))
        avg_file = os.path.join(WORK_DIR, 'Average_{}.fxout'.format(base_name))
        raw_file = os.path.join(WORK_DIR, 'Raw_{}.fxout'.format(base_name))
        
        if os.path.exists(dif_file):
            os.replace(dif_file, dif_backup)
        if os.path.exists(avg_file):
            os.replace(avg_file, avg_backup)
        
        try:
            # Run FoldX
            start = time.time()
            result = subprocess.run(
                [FOLDX, '--command=BuildModel', '--pdb={}'.format(pdb_file),
                 '--mutant-file=individual_list_batch.txt',
                 '--output-dir=.', '--numberOfRuns=3'],
                cwd=WORK_DIR, capture_output=True, text=True, timeout=180
            )
            elapsed = time.time() - start
            print('{:.1f}s '.format(elapsed), end='')
            
            if result.returncode == 0:
                # Parse the Dif file - now it has 2 entries (WT + mutant)
                if os.path.exists(dif_file):
                    with open(dif_file) as f:
                        lines = f.readlines()
                    
                    # Find data lines (after header row starting with 'Pdb')
                    data_rows = []
                    header_found = False
                    for line in lines:
                        if line.strip().startswith('Pdb'):
                            header_found = True
                            continue
                        if header_found and line.strip():
                            parts = line.strip().split('\t')
                            if len(parts) >= 2:
                                try:
                                    total_energy = float(parts[1])
                                    data_rows.append(total_energy)
                                except ValueError:
                                    pass
                    
                    if len(data_rows) >= 2:
                        mut_energy = data_rows[-1]  # Last entry is the mutant
                        ddg = mut_energy - wt_energy
                        print('WT={:.2f} Mut={:.2f} DDG={:+.2f}'.format(wt_energy, mut_energy, ddg), end='')
                        results.append((tmpl_name, mut_name, wt_energy, mut_energy, ddg))
                    elif len(data_rows) == 1:
                        # Only one entry - might be the mutant
                        mut_energy = data_rows[0]
                        ddg = mut_energy - wt_energy
                        print('Mut={:.2f} DDG={:+.2f} (single entry)'.format(mut_energy, ddg), end='')
                        results.append((tmpl_name, mut_name, wt_energy, mut_energy, ddg))
                    else:
                        print('NO DATA in Dif file', end='')
                else:
                    print('NO Dif file', end='')
            else:
                print('ERROR rc={}'.format(result.returncode), end='')
        
        except Exception as e:
            print('EXCEPTION: {}'.format(str(e)[:50]), end='')
        
        # Clean up backup files
        for bk in [dif_backup, avg_backup]:
            if os.path.exists(bk):
                os.remove(bk)
        
        # Clean up temp PDB files created by FoldX
        wt_pdb = os.path.join(WORK_DIR, 'WT_{}.pdb'.format(base_name))
        if os.path.exists(wt_pdb):
            os.remove(wt_pdb)
        
        for i in [1,2,3]:
            pdb_out = os.path.join(WORK_DIR, '{}_{}.pdb'.format(base_name, i))
            if os.path.exists(pdb_out):
                os.remove(pdb_out)
    
    print()

# Print full results
print('\n\n' + '=' * 60)
print('FULL RESULTS')
print('=' * 60)

summary = {}
for tmpl, mut, wt_e, mut_e, ddg in results:
    if tmpl not in summary:
        summary[tmpl] = []
    summary[tmpl].append((mut, ddg))

for tmpl, muts in summary.items():
    print('\n--- {} ---'.format(tmpl))
    # Sort by DDG (most negative = most stable first)
    muts_sorted = sorted(muts, key=lambda x: x[1])
    for mut, ddg in muts_sorted:
        marker = '🟢' if ddg < 0 else '🔴'
        print('  {} {}: {:+.2f} kcal/mol'.format(marker, mut, ddg))

print('\nDone!')
