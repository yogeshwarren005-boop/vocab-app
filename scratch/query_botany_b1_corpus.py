# -*- coding: utf-8 -*-
"""
query_botany_b1_corpus.py
Queries citation_corpus.db for all 109 words in Cluster Botany, Minerals & Elements Batch 1
"""
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    'herbicide', 'herbivorous',
    'despumate', 'despumation',
    'horticultural', 'horticulturally', 'horticulture', 'horticulturist',
    'stannary', 'stannate', 'stannic', 'stannite', 'stannous',
    'pulver', 'pulverisation', 'pulverise', 'pulverised', 'pulverization', 'pulverize', 'pulverized', 'pulverulent',
    'hypernatremia', 'hyponatremia', 'natremia', 'natrium', 'natriuresis', 'natriuretic', 'natrix', 'natrolite', 'natron',
    'silica', 'silicate', 'siliceous', 'silicide', 'silicious', 'silicle', 'silicon', 'silicone', 'silicosis',
    'argent', 'argentic', 'argentiferous', 'argentina', 'argentine', 'argentinian', 'argentinidae', 'argentinosaur', 'argentite', 'argentous',
    'eradicable', 'eradicate', 'eradication', 'eradicator', 'ineradicable', 'irradicable', 'radical', 'radicalism', 'radicalize', 'radically', 'radicchio', 'radicle', 'radiculitis',
    'devitrify', 'in vitro', 'unvitrified', 'vitrectomy', 'vitreous', 'vitrification', 'vitrified', 'vitrify', 'vitrine', 'vitriol', 'vitriolic', 'vitriolically', 'vitro',
    'xylaria', 'xylariaceae', 'xylem', 'xylene', 'xylocaine', 'xylocopa', 'xylography', 'xylol', 'xylomelum', 'xylophone', 'xylophonist', 'xylopia', 'xylose', 'xylosma',
    'arbor', 'arbor day', 'arboraceous', 'arborary', 'arboreal', 'arboreous', 'arborescent', 'arboresque', 'arboretum', 'arborical', 'arboriculture', 'arboriculturist', 'arboriform', 'arborise', 'arborist', 'arborize', 'arborolatry', 'arborous', 'arborvitae', 'nonarboreal'
]

results = {}

for w in words:
    # search using FTS
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
    status = "OK (>=3)" if len(dedup) >= 3 else f"LOW ({len(dedup)})"
    print(f"{w:20}: {len(dedup):3} distinct authors -> {status}")

conn.close()

with open("scratch/botany_b1_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSaved scratch/botany_b1_rich_corpus.json successfully.")
