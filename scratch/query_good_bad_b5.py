# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Good & Bad'
dashboards = ['vil', 'viti', 'vulg']

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

vil_words = words_by_root['vil']
viti_words = words_by_root['viti']
vulg_words = words_by_root['vulg']

print(f"vil: {len(vil_words)} words")
print(f"viti: {len(viti_words)} words")
print(f"vulg: {len(vulg_words)} words")

total_b5 = len(vil_words) + len(viti_words) + len(vulg_words)
print(f"Total Batch 5 words: {total_b5}")

# Divide into 2 parts:
# Part 1: vil 1-36 (36 words)
# Part 2: vil 37-46 (10 words) + viti (11 words) + vulg (15 words) = 36 words
# Total = 36 + 36 = 72 words

p1 = vil_words[0:36]
p2 = vil_words[36:46] + viti_words + vulg_words

print(f"Part 1: {len(p1)} words ({p1[0]} .. {p1[-1]})")
print(f"Part 2: {len(p2)} words ({p2[0]} .. {p2[-1]})")

all_words = p1 + p2

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

with open('scratch/good_bad_b5_corpus.json', 'w', encoding='utf-8') as f:
    json.dump({
        'dir_map': dir_map,
        'p1': p1,
        'p2': p2,
        'results': results
    }, f, ensure_ascii=False, indent=2)

print('Saved to scratch/good_bad_b5_corpus.json')
