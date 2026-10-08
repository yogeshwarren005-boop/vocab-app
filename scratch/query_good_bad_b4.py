# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Good & Bad'
dashboards = ['pecc', 'prav', 'pur', 'suav', 'van']

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

pecc_words = words_by_root['pecc']
prav_words = words_by_root['prav']
pur_words = words_by_root['pur']
suav_words = words_by_root['suav']
van_words = words_by_root['van']

print(f"pecc: {len(pecc_words)} words")
print(f"prav: {len(prav_words)} words")
print(f"pur: {len(pur_words)} words")
print(f"suav: {len(suav_words)} words")
print(f"van: {len(van_words)} words")

total_b4 = len(pecc_words) + len(prav_words) + len(pur_words) + len(suav_words) + len(van_words)
print(f"Total Batch 4 words: {total_b4}")

# Divide into balanced parts:
# Part 1a: pecc (8) + prav (6) + suav (4) + pur 1-21 (21) = 39 words
# Part 1b: pur 22-56 (35 words)
# Part 2a: pur 57-77 (21 words) + van 1-18 (18) = 39 words
# Part 2b: van 19-47 (29 words)
# Total = 39 + 35 + 39 + 29 = 142 words

p1a = pecc_words + prav_words + suav_words + pur_words[0:21]
p1b = pur_words[21:56]
p2a = pur_words[56:77] + van_words[0:18]
p2b = van_words[18:47]

print(f"Part 1a: {len(p1a)} words ({p1a[0]} .. {p1a[-1]})")
print(f"Part 1b: {len(p1b)} words ({p1b[0]} .. {p1b[-1]})")
print(f"Part 2a: {len(p2a)} words ({p2a[0]} .. {p2a[-1]})")
print(f"Part 2b: {len(p2b)} words ({p2b[0]} .. {p2b[-1]})")

all_words = p1a + p1b + p2a + p2b
print(f"Total words in Batch 4: {len(all_words)}")

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

with open('scratch/good_bad_b4_corpus.json', 'w', encoding='utf-8') as f:
    json.dump({
        'dir_map': dir_map,
        'p1a': p1a,
        'p1b': p1b,
        'p2a': p2a,
        'p2b': p2b,
        'results': results
    }, f, ensure_ascii=False, indent=2)

print('Saved to scratch/good_bad_b4_corpus.json')
