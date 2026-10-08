# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

words = [
    'majestic', 'majestically', 'majesty',
    'interregnum', 'regnal', 'regnancy', 'regnant', 'regnellidium',
    'depot', 'pot', 'potable', 'potage', 'potation', 'potence', 'potent', 'potion', 'repot',
    'prince', "prince's-feather", "prince's-plume", "prince-of-wales'-heath",
    'princedom', 'princeling', 'princely', 'princess', 'princeton', 'princewood',
    'principal', 'principality', 'principally', 'principalship', 'principe', 'principen',
    'principle', 'principled', 'unprincipled'
]

results = {}
for w in words:
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 15
    """, (f'"{w}"',))
    rows = cur.fetchall()
    seen = set()
    dedup = []
    for r in rows:
        if r[0] not in seen:
            seen.add(r[0])
            dedup.append({"author": r[0], "work": r[1], "sentence": r[2]})
    results[w] = dedup
    print(f"{w}: {len(dedup)} distinct authors ({[x['author'] for x in dedup[:3]]})")

with open("scratch/part1_corpus_dump.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
