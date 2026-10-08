# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

words = [
    'antiviral', 'invirase', 'provirus', 'retrovir', 'retrovirus',
    'triumvirate', 'viracept', 'viraemia', 'virago', 'viral',
    'viramune', 'virazole', 'virchow', 'viremia', 'vireo',
    'vireonidae', 'viricidal', 'viricide', 'viridity', 'virile',
    'virilisation', 'virilise', 'virilism', 'virility', 'virilization',
    'virilize', 'virino', 'virion', 'viroid', 'virological',
    'virologist', 'virology', 'virtu', 'virtual', 'virtually',
    'virtue', 'virtuosity', 'virtuoso', 'virtuous', 'virtuously',
    'virtuousness', 'virucidal', 'virucide', 'virulence', 'virulency',
    'virulent', 'virulently', 'virus', 'virusoid'
]

results = {}
for w in words:
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 300
    """, (f'"{w}"',))
    rows = cur.fetchall()
    seen = set()
    dedup = []
    for a, wrk, st in rows:
        if a not in seen:
            seen.add(a)
            dedup.append({"author": a, "work": wrk, "sentence": st})
    results[w] = dedup
    print(f"{w}: {len(dedup)} distinct authors: {[x['author'] for x in dedup[:4]]}")

with open("scratch/vir_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
