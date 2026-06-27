#!/usr/bin/env python3
"""
pdb_download.py — Download PDB files for GFP templates
Usage: python pdb_download.py
Output: PDB files in data/pdb/ directory
"""

import os, urllib.request

PDB_CODES = ['2B3P', '2WUR', '7LG4', '2HPW', '2G6X']
OUT_DIR = 'data/pdb'

def download_pdb(pdb_code):
    """Download PDB file from RCSB"""
    url = f'https://files.rcsb.org/download/{pdb_code}.pdb'
    out_path = os.path.join(OUT_DIR, f'{pdb_code}.pdb')
    
    if os.path.exists(out_path):
        size = os.path.getsize(out_path)
        print(f'  {pdb_code}: already exists ({size} bytes)')
        return
    
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f'  Downloading {pdb_code}...', end=' ')
    try:
        urllib.request.urlretrieve(url, out_path)
        size = os.path.getsize(out_path)
        print(f'done ({size} bytes)')
    except Exception as e:
        print(f'FAILED: {e}')

def main():
    print('Downloading PDB structures for GFP templates:')
    for code in PDB_CODES:
        download_pdb(code)
    
    print(f'\nAll files saved to {OUT_DIR}/')
    print()
    for code in PDB_CODES:
        fpath = os.path.join(OUT_DIR, f'{code}.pdb')
        print(f'  {code}: {"OK" if os.path.exists(fpath) else "MISSING"}')

if __name__ == '__main__':
    main()
