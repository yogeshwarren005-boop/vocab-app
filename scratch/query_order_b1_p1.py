# -*- coding: utf-8 -*-
"""
query_order_b1_p1.py
Queries citation_corpus.db for 57 words in Cluster Order Batch 1 Part 1
"""
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    # secut (8)
    'consecutive', 'consecutively', 'persecute', 'persecution', 'persecutor', 'prosecute', 'prosecution', 'prosecutor',
    # sort (14)
    'assort', 'assorted', 'assortment', 'consort', 'consortium', 'resort', 'sort', 'sorted', 'sorter', 'sortie', 'sortilege', 'sorting', 'sortition', 'unsorted',
    # class (35)
    'class', 'classic', 'classical', 'classicalism', 'classically', 'classicise', 'classicism', 'classicist', 'classicistic', 'classicize', 'classics', 'classifiable', 'classification', 'classificatory', 'classified', 'classifier', 'classify', 'classless', 'classmate', 'classroom', 'classy', 'declassification', 'declassified', 'declassify', 'nonclassical', 'outclass', 'outclassed', 'reclassification', 'reclassify', 'subclass', 'superclass', 'unclassifiable', 'unclassified', 'underclass', 'underclassman'
]

results = {}
high_count = 0

for w in words:
    clean_w = w.replace('-', ' ')
    query = f'"{clean_w}"'
    try:
        cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 300
        """, (query,))
        rows = cur.fetchall()
    except Exception as e:
        rows = []

    seen = set()
    dedup = []
    pattern = re.compile(rf'\b{re.escape(w)}\b', re.IGNORECASE)
    for a, wrk, st in rows:
        if a not in seen:
            seen.add(a)
            m = pattern.search(st)
            if m:
                start, end = m.span()
                bolded = st[:start] + f"**{st[start:end]}**" + st[end:]
            else:
                bolded = st
            dedup.append({"author": a, "work": wrk, "sentence": bolded})
    results[w] = dedup
    if len(dedup) >= 3:
        high_count += 1

conn.close()

with open("scratch/order_b1_p1_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Total words: {len(words)}")
print(f"Words with >= 3 distinct authors: {high_count}")
for w in words:
    print(f"  {w:22}: {len(results[w])}")
