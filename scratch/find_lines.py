with open('scratch/curate_hybrid_b6_p6b.py', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        for w in ['demoniac', 'demoralization']:
            if f'"{w}":' in line:
                print(f'{w}: line {i+1}')
