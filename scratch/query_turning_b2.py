# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Turning'
dashboards = ['flect', 'flex', 'orb', 'rot', 'torqu', 'tors', 'trop']

all_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
dir_map = {}
for root in dashboards:
    matched = [d for d in all_dirs if d.split('—')[-1].strip() == root or d.endswith(' ' + root)][0]
    dir_map[root] = matched

print('Matched directories:', dir_map)

b2_words = []
word_to_dir = {}
words_by_root = {}
for root, dirname in dir_map.items():
    dp = os.path.join(base_path, dirname)
    words = sorted([f[:-3] for f in os.listdir(dp) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    print(f'{dirname}: {len(words)} words')
    words_by_root[root] = words
    for w in words:
        b2_words.append(w)
        word_to_dir[w] = dirname

print(f'Total files in Turning Batch 2: {len(b2_words)}')
unique_words = sorted(list(set(b2_words)))
print(f'Total unique words in Turning Batch 2: {len(unique_words)}')

db_path = 'main app/corpus/citation_corpus.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

results = {}
found_3 = 0
found_less = []

for w in unique_words:
    clean_w = w.replace('-', ' ')
    query = f'"{clean_w}"'
    try:
        cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 400
        """, (query,))
        rows = cur.fetchall()
    except Exception as e:
        rows = []

    seen = set()
    dedup = []
    pattern = re.compile(rf'\b{re.escape(clean_w)}\b', re.IGNORECASE)
    for a, wrk, st in rows:
        if a not in seen:
            if pattern.search(st):
                clean_st = ' '.join(st.split())
                if len(clean_st) >= 35 and len(clean_st) <= 450:
                    seen.add(a)
                    dedup.append({'author': a, 'work': wrk, 'sentence': clean_st})
        if len(dedup) >= 3:
            break
    
    results[w] = dedup
    if len(dedup) >= 3:
        found_3 += 1
    else:
        found_less.append((w, len(dedup)))

print(f'Found 3+ quotes for {found_3}/{len(unique_words)} words')
print(f'Words with < 3 quotes: {len(found_less)}')

with open('scratch/turning_b2_corpus.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

with open('scratch/turning_b2_words.json', 'w', encoding='utf-8') as f:
    json.dump({
        'total_files': len(b2_words),
        'unique_words': unique_words,
        'dir_map': dir_map,
        'words_by_root': words_by_root,
        'found_less': found_less
    }, f, indent=2, ensure_ascii=False)

print('Saved to scratch/turning_b2_corpus.json and scratch/turning_b2_words.json')
