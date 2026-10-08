# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

words = [
    'comfort', 'comfortable', 'comfortableness', 'comfortably', 'comforted',
    'comforter', 'comforting', 'comfortingly', 'comfortless', 'comforts',
    'discomfort', 'effort', 'effortless', 'effortlessly', 'effortlessness',
    'fort', 'fortaz', 'forte', 'forte-piano', 'fortemente',
    'forties', 'fortieth', 'fortification', 'fortified', 'fortify',
    'fortissimo', 'fortitude', 'fortnight', 'fortnightly', 'fortran',
    'fortress', 'fortuitous', 'fortuitously', 'fortuitousness', 'fortuity',
    'fortuna', 'fortunate', 'fortunately', 'fortune', 'fortunella',
    'fortuneteller', 'fortunetelling', 'forty', 'forty-eight', 'forty-eighth',
    'forty-fifth', 'forty-first', 'forty-five', 'forty-four', 'forty-fourth',
    'forty-nine', 'forty-niner', 'forty-ninth', 'forty-one', 'forty-second',
    'forty-seven', 'forty-seventh', 'forty-six', 'forty-sixth', 'forty-third',
    'forty-three', 'forty-two', 'misfortunate', 'misfortune', 'pianoforte',
    'uncomfortable', 'uncomfortableness', 'uncomfortably', 'unfortunate', 'unfortunately'
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

with open("scratch/fort_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
