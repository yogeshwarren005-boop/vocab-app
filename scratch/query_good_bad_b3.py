# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Good & Bad'
dp = os.path.join(base_path, 'Dashboard — mal')

words = sorted([f[:-3] for f in os.listdir(dp) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
print(f'Dashboard — mal: {len(words)} words')

p1a = words[0:39]
p1b = words[39:78]
p2a = words[78:117]
p2b = words[117:155]

print(f'Part 1a: {len(p1a)} words ({p1a[0]} .. {p1a[-1]})')
print(f'Part 1b: {len(p1b)} words ({p1b[0]} .. {p1b[-1]})')
print(f'Part 2a: {len(p2a)} words ({p2a[0]} .. {p2a[-1]})')
print(f'Part 2b: {len(p2b)} words ({p2b[0]} .. {p2b[-1]})')

all_words = words
print(f'Total words in Batch 3: {len(all_words)}')

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
for w, count in found_less:
    print(f'  {w}: {count}')

with open('scratch/good_bad_b3_corpus.json', 'w', encoding='utf-8') as f:
    json.dump({
        'p1a': p1a,
        'p1b': p1b,
        'p2a': p2a,
        'p2b': p2b,
        'results': results
    }, f, ensure_ascii=False, indent=2)

print('Saved to scratch/good_bad_b3_corpus.json')
