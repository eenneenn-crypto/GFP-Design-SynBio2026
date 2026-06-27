#!/usr/bin/env python3
"""
design_variants.py — Generate candidate GFP sequences for SynBio Challenges
Based on FoldX ΔG/ΔΔG analysis + literature mutations
"""

REF_SEQS = {
    'sfGFP': 'MSKGEELFTGVVPILVELDGDVNGHKFSVRGEGEGDATNGKLTLKFICTTGKLPVPWPTLVTTLTYGVQCFSRYPDHMKRHDFFKSAMPEGYVQERTISFKDDGTYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNFNSHNVYITADKQKNGIKANFKIRHNVEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSVLSKDPNEKRDHMVLLEFVTAAGITHGMDELYK',
    'avGFP': 'MSKGEELFTGVVPILVELDGDVNGHKFSVSGEGEGDATYGKLTLKFICTTGKLPVPWPTLVTTLSYGVQCFSRYPDHMKQHDFFKSAMPEGYVQERTIFFKDDGNYKTRAEVKFEGDTLVNRIELKGIDFKEDGNILGHKLEYNYNSHNVYIMADKQKNGIKVNFKIRHNIEDGSVQLADHYQQNTPIGDGPVLLPDNHYLSTQSALSKDPNEKRDHMVLLEFVTAAGITHGMDELYK',
    'amacGFP': 'MSKGEELFTGIVPVLIELDGDVHGHKFSVRGEGEGDADYGKLEIKFICTTGKLPVPWPTLVTTLSYGILCFARYPEHMKMNDFFKSAMPEGYIQERTIFFQDDGKYKTRGEVKFEGDTLVNRIELKGMDFKEDGNILGHKLEYNFNSHNVYIMPDKANNGLKVNFKIRHNIEGGGVQLADHYQTNVPLGDGPVLIPINHYLSCQTAISKDRNETRDHMVFLEFFSACGHTHGMDELYK',
    'cgreGFP': 'MTALTEGAKLFEKEIPYITELEGDVEGMKFIIKGEGTGDATTGTIKAKYICTTGDLPVPWATILSSLSYGVFCFAKYPRHIADFFKSTQPDGYSQDRIISFDNDGQYDVKAKVTYENGTLYNRVTVKGTGFKSNGNILGMRVLYHSPPHAVYILPDRKNGGMKIEYNKAFDVMGGGHQMARHAQFNKPLGAWEEDYPLYHHLTVWTSFGKDPDDDETDHLTIVEVIKAVDLETYR',
    'ppluGFP': 'MPAMKIECRITGTLNGVEFELVGGGEGTPEQGRMTNKMKSTKGALTFSPYLLSHVMGYGFYHFGTYPSGYENPFLHAINNGGYTNTRIEKYEDGGVLHVSFSYRYEAGRVIGDFKVVGTGFPEDSVIFTDKIIRSNATVEHLHPMGDNVLVGSFARTFSLRDGGYYSFVVDSHMHFKSAIHPSILQNGGPMFAFRRVEELHSNTELGIVEYQHAFKTPIAFA',
}


def mutate(seq, pos1, new_aa):
    """Return sequence with aa at 1-indexed position changed"""
    return seq[:pos1 - 1] + new_aa + seq[pos1:]


def generate_variants():
    """Generate all variants and return list of dicts"""
    variants = []

    # --- sfGFP-based ---
    s1 = REF_SEQS['sfGFP']
    for p, a in [(69, 'L'), (147, 'P'), (149, 'K'), (164, 'Y'),
                  (172, 'K'), (190, 'N'), (227, 'V')]:
        s1 = mutate(s1, p, a)
    variants.append({
        'id': 'G1', 'name': 'sfGFP_Plus_v1',
        'scaffold': 'sfGFP',
        'seq': s1,
        'rationale': 'sfGFP backbone + 7 stabilizing mutations (E172K best) + usGFP core packing',
        'source': 'FoldX analysis, Pédelacq 2006, Scott 2018'
    })

    s2 = REF_SEQS['sfGFP']
    for p, a in [(69, 'L'), (79, 'E'), (149, 'K'), (164, 'Y'),
                  (172, 'K'), (204, 'E')]:
        s2 = mutate(s2, p, a)
    variants.append({
        'id': 'G2', 'name': 'sfGFP_TGP_surface',
        'scaffold': 'sfGFP',
        'seq': s2,
        'rationale': 'sfGFP + TGP-style surface charge engineering (Q79E, Q204E) + core stability',
        'source': 'Close 2015 (TGP), FoldX analysis'
    })

    # --- amacGFP-based ---
    a1 = REF_SEQS['amacGFP']
    for p, a in [(39, 'N'), (149, 'K'), (172, 'K')]:
        a1 = mutate(a1, p, a)
    variants.append({
        'id': 'G3', 'name': 'amacGFP_core3',
        'scaffold': 'amacGFP',
        'seq': a1,
        'rationale': 'amacGFP + 3 best FoldX mutations (all DG<0, DDG<-3.9)',
        'source': 'FoldX analysis (Y39N=-0.81, N149K=-0.51, E172K=-0.44)'
    })

    a2 = REF_SEQS['amacGFP']
    for p, a in [(39, 'N'), (69, 'L'), (147, 'P'), (149, 'K'),
                  (164, 'Y'), (172, 'K'), (190, 'N')]:
        a2 = mutate(a2, p, a)
    variants.append({
        'id': 'G4', 'name': 'amacGFP_plus7',
        'scaffold': 'amacGFP',
        'seq': a2,
        'rationale': 'amacGFP + 7 stabilizing mutations + usGFP mutations',
        'source': 'FoldX analysis + Scott 2018'
    })

    # --- ppluGFP-based ---
    p1 = REF_SEQS['ppluGFP']
    for p, a in [(48, 'E'), (118, 'E'), (199, 'H'), (206, 'E'), (221, 'E')]:
        p1 = mutate(p1, p, a)
    variants.append({
        'id': 'G5', 'name': 'ppluGFP_bright',
        'scaffold': 'ppluGFP',
        'seq': p1,
        'rationale': 'Naturally stable (DG=-49.88) + brightness optimization + surface charge',
        'source': 'GFP_data.xlsx, Close 2015'
    })

    # --- cgreGFP-based ---
    c1 = REF_SEQS['cgreGFP']
    for p, a in [(78, 'G'), (167, 'M'), (168, 'V'), (172, 'E')]:
        c1 = mutate(c1, p, a)
    variants.append({
        'id': 'G6', 'name': 'cgreGFP_bright',
        'scaffold': 'cgreGFP',
        'seq': c1,
        'rationale': 'Naturally brightest (6x avGFP) + stable (DG=-26.89) + top brightness mutations',
        'source': 'GFP_data.xlsx (brightness data)'
    })

    return variants


def main():
    variants = generate_variants()
    print(f'Generated {len(variants)} variants')
    for v in variants:
        print(f'  {v["id"]:4s} {v["name"]:<25s} {v["scaffold"]:<10s} '
              f'len={len(v["seq"]):3d}  {v["rationale"][:50]}...')


if __name__ == '__main__':
    main()
