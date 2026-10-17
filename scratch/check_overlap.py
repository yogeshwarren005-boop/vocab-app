import os

latin_dir = 'App database/Latin roots'
greek_dir = 'App database/Greek roots'

def collect_roots(base_dir):
    roots = {}
    for cluster in os.listdir(base_dir):
        c_path = os.path.join(base_dir, cluster)
        if not os.path.isdir(c_path) or not cluster.startswith('Cluster '):
            continue
        for d in os.listdir(c_path):
            d_path = os.path.join(c_path, d)
            if not os.path.isdir(d_path):
                continue
            clean_name = d.replace('Dashboard — ', '').replace('Dashboard - ', '').replace('Dashboard \u2014 ', '').strip()
            dash_file = None
            for f in os.listdir(d_path):
                if f.startswith('Dashboard') and f.endswith('.md'):
                    dash_file = os.path.join(d_path, f)
                    break
            words = [f[:-3] for f in os.listdir(d_path) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
            roots[clean_name] = {'cluster': cluster, 'folder': d, 'path': d_path, 'dash_file': dash_file, 'words': words}
    return roots

l_roots = collect_roots(latin_dir)
g_roots = collect_roots(greek_dir)

print(f'Total Latin root folders: {len(l_roots)}')
print(f'Total Greek root folders: {len(g_roots)}')

common = set(l_roots.keys()) & set(g_roots.keys())
print(f'Root names in BOTH: {len(common)}')

total_dup_words_in_common = 0
for r in sorted(common):
    lw = set(l_roots[r]['words'])
    gw = set(g_roots[r]['words'])
    overlap_words = lw & gw
    total_dup_words_in_common += len(overlap_words)
    print(f"Root: {r:15} | Latin ({l_roots[r]['cluster'][:20]}): {len(lw):3} words | Greek ({g_roots[r]['cluster'][:20]}): {len(gw):3} words | Word overlap: {len(overlap_words)}")

print(f'Total identical words in overlapping roots: {total_dup_words_in_common}')
