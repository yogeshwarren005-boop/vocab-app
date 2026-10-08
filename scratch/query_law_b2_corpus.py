# -*- coding: utf-8 -*-
import sqlite3
import json
import re

with open('scratch/law_words.json', encoding='utf-8') as f:
    d = json.load(f)['words_by_root']

leg_words = d['leg']
mand_words = d['mand']

b2_words = leg_words + mand_words[:31]
print(f"Batch 2 words: {len(b2_words)} (leg: {len(leg_words)}, mand[:31]: {len(mand_words[:31])})")

db_path = 'main app/corpus/citation_corpus.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

results = {}
for w in b2_words:
    clean_w = w.replace('-', ' ')
    query = f'"{clean_w}"'
    try:
        cur.execute('''
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 150
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

found_count = sum(1 for w, v in results.items() if len(v) >= 3)
print(f"Batch 2 words with >=3 corpus hits: {found_count} / {len(b2_words)}")

with open('scratch/law_b2_corpus_hits.json', 'w', encoding='utf-8') as f:
    json.dump({
        'leg_words': leg_words,
        'mand_words_p1': mand_words[:31],
        'mand_words_p2': mand_words[31:],
        'hits': results
    }, f, ensure_ascii=False, indent=2)

print("Saved to scratch/law_b2_corpus_hits.json")
