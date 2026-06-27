"""Check PDB residue numbers for all templates"""
aa3to1 = {
    'ALA':'A','ARG':'R','ASN':'N','ASP':'D','CYS':'C',
    'GLN':'Q','GLU':'E','GLY':'G','HIS':'H','ILE':'I',
    'LEU':'L','LYS':'K','MET':'M','PHE':'F','PRO':'P',
    'SER':'S','THR':'T','TRP':'W','TYR':'Y','VAL':'V',
}

targets = list(range(1, 239))  # All positions 1-238

for path, name in [
    (r'D:\openclaw_work\foldx5\2B3P_A_Repair_1.pdb', '2B3P_sfGFP'),
    (r'D:\openclaw_work\foldx5\2WUR_Repair.pdb', '2WUR_avGFP'),
    (r'D:\openclaw_work\foldx5\7LG4_Repair.pdb', '7LG4_amacGFP'),
    (r'D:\openclaw_work\foldx5\2HPW_Repair.pdb', '2HPW_cgreGFP'),
    (r'D:\openclaw_work\foldx5\2G6X_Repair.pdb', '2G6X_ppluGFP'),
]:
    seq_map = {}
    with open(path) as f:
        for line in f:
            if line.startswith('ATOM') and line[12:16].strip() == 'CA':
                resnum = int(line[22:26].strip())
                resname = line[17:20].strip()
                if resnum not in seq_map:
                    seq_map[resnum] = aa3to1.get(resname, 'X')
    resnums = sorted(seq_map.keys())
    print(f'\n{name}: residues {resnums[0]}-{resnums[-1]} ({len(resnums)} total)')
    
    # Check key target positions
    check = [2, 8, 30, 39, 48, 63, 64, 69, 73, 78, 79, 85, 96, 99, 105, 118, 
             124, 145, 147, 149, 153, 157, 160, 163, 164, 167, 168, 170, 171, 172,
             174, 190, 197, 199, 204, 206, 221, 227]
    for t in check:
        if t in seq_map:
            print(f'  PDB[{t:>3}] = {seq_map[t]}', end='')
            if t < len(seq_map):
                ref_idx = t
                # Simple direct check
            print()
