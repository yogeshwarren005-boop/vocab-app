# -*- coding: utf-8 -*-
import os
import json

base_path = 'App database/Latin roots/Cluster Turning'
dashboards = ['vers', 'vert']

all_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
dir_map = {}
for root in dashboards:
    matched = [d for d in all_dirs if d.split('—')[-1].strip() == root or d.endswith(' ' + root)][0]
    dir_map[root] = matched

words_by_root = {}
for root, dname in dir_map.items():
    tdir = os.path.join(base_path, dname)
    files = sorted([f[:-3] for f in os.listdir(tdir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    if root == 'vers':
        words_by_root[root] = files[35:]
    else:
        words_by_root[root] = files

all_words = words_by_root['vers'] + words_by_root['vert']
print(f"Total words for Batch 4: {len(all_words)}")
print(f"  vers (36-93): {len(words_by_root['vers'])}")
print(f"  vert (1-91): {len(words_by_root['vert'])}")

# Sub-batches
p1a = words_by_root['vers'][:29]
p1b = words_by_root['vers'][29:]
p2a = words_by_root['vert'][:45]
p2b = words_by_root['vert'][45:]

print(f"  Part 1a (vers 36-64): {len(p1a)}")
print(f"  Part 1b (vers 65-93): {len(p1b)}")
print(f"  Part 2a (vert 1-45): {len(p2a)}")
print(f"  Part 2b (vert 46-91): {len(p2b)}")

with open('scratch/turning_b4_words.json', 'w', encoding='utf-8') as f:
    json.dump({
        'dir_map': dir_map,
        'words_by_root': words_by_root,
        'p1a': p1a,
        'p1b': p1b,
        'p2a': p2a,
        'p2b': p2b,
        'all_words': all_words
    }, f, indent=2)
