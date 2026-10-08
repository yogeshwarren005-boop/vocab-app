# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Good & Bad'
dashboards = ['apt', 'bas']

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

apt_words = words_by_root['apt']
bas_words = words_by_root['bas']

p1a = apt_words
p1b = bas_words[:37]
p2a = bas_words[37:74]
p2b = bas_words[74:]

print(f'Part 1a (apt): {len(p1a)}')
print(f'Part 1b (bas 1-37): {len(p1b)}')
print(f'Part 2a (bas 38-74): {len(p2a)}')
print(f'Part 2b (bas 75-111): {len(p2b)}')

all_words = apt_words + bas_words
print(f'Total words in Batch 1: {len(all_words)}')

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

with open('scratch/good_bad_b1_corpus.json', 'w', encoding='utf-8') as f:
    json.dump({
        'dir_map': dir_map,
        'p1a': p1a,
        'p1b': p1b,
        'p2a': p2a,
        'p2b': p2b,
        'results': results
    }, f, indent=2)
