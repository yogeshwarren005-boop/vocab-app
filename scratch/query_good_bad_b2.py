# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Good & Bad'
dashboards = ['bene', 'culp', 'fam', 'felic', 'mend', 'noxa']

all_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
dir_map = {}
for root in dashboards:
    matched = [d for d in all_dirs if d.split('—')[-1].strip() == root or d.endswith(' ' + root)][0]
    dir_map[root] = matched

print('Matched directories:', dir_map)

words_by_root = {}
for root, dirname in dir_map.items():
    dp = os.path.join(base_path, dirname)
    words = sorted([f[:-3] for f in os.listdir(dp) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    print(f'{dirname}: {len(words)} words')
    words_by_root[root] = words

bene_words = words_by_root['bene']
culp_words = words_by_root['culp']
fam_words = words_by_root['fam']
felic_words = words_by_root['felic']
mend_words = words_by_root['mend']
noxa_words = words_by_root['noxa']

# Sub-batches for Batch 2:
# Part 1a: bene (15) + culp (17) = 32 words
# Part 1b: fam (34) = 34 words
# Part 2a: felic (10) + mend (32) = 42 words
# Part 2b: noxa (34) = 34 words
# Total = 32 + 34 + 42 + 34 = 142 words

p1a = bene_words + culp_words
p1b = fam_words
p2a = felic_words + mend_words
p2b = noxa_words

print(f'Part 1a (bene + culp): {len(p1a)}')
print(f'Part 1b (fam): {len(p1b)}')
print(f'Part 2a (felic + mend): {len(p2a)}')
print(f'Part 2b (noxa): {len(p2b)}')

all_words = p1a + p1b + p2a + p2b
print(f'Total words in Batch 2: {len(all_words)}')

db_path = 'main app/corpus/citation_corpus.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

results = {}
found_3 = 0
found_less = []

for w in all_words:
    clean_w = w.replace('-', ' ')
    query = f'"{clean_w}"'
    try:
        cur.execute('''
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 300
        ''', (query,))
        rows = cur.fetchall()
    except Exception as e:
        rows = []

    seen = set()
    dedup = []
    pattern = re.compile(rf'\b{re.escape(clean_w)}\b', re.IGNORECASE)
    for a, wrk, st in rows:
        if a not in seen:
            if pattern.search(st):
                bolded_sentence = pattern.sub(lambda m: f'**{m.group(0)}**', st)
                seen.add(a)
                dedup.append({
                    'author': a,
                    'work': wrk,
                    'sentence': bolded_sentence
                })
                if len(dedup) == 5:
                    break

    results[w] = dedup
    if len(dedup) >= 3:
        found_3 += 1
    else:
        found_less.append((w, len(dedup)))

print(f'Words with >= 3 corpus citations: {found_3}/{len(all_words)}')
print(f'Words with < 3 citations: {len(found_less)}')

with open('scratch/good_bad_b2_corpus.json', 'w', encoding='utf-8') as f:
    json.dump({
        'dir_map': dir_map,
        'words_by_root': words_by_root,
        'p1a': p1a,
        'p1b': p1b,
        'p2a': p2a,
        'p2b': p2b,
        'results': results
    }, f, indent=2)
