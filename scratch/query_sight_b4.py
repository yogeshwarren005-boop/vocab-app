# -*- coding: utf-8 -*-
"""
query_sight_b4.py
Queries citation_corpus.db for the 68 new words in Dashboard — spec:
"""
import sqlite3
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

words = ['conspecific', 'disrespectful', 'disrespectfully', 'especial', 'especially', 'interspecies', 'interspecific', 'intraspecies', 'intraspecific', 'introspectively', 'nonspecific', 'nonspecifically', 'overspecialise', 'overspecialize', 'respectful', 'respectfully', 'respectfulness', 'spec', 'special', 'specialisation', 'specialise', 'specialised', 'specialiser', 'specialism', 'specialist', 'specialistic', 'speciality', 'specialization', 'specialize', 'specialized', 'specializer', 'specially', 'specialness', 'specialty', 'speciate', 'speciation', 'specie', 'species', 'specifiable', 'specific', 'specifically', 'specification', 'specificity', 'specified', 'specifier', 'specify', 'specimen', 'specious', 'speciously', 'speciousness', 'specs', 'specular', 'speculate', 'speculation', 'speculative', 'speculatively', 'speculativeness', 'speculator', 'speculum', 'subspecies', 'suspect', 'suspected', 'unspecialised', 'unspecialized', 'unspecific', 'unspecified', 'unsuspected', 'unsuspecting']

print(f"Total words to query: {len(words)}")

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
cur = conn.cursor()

hits = {}
for w in words:
    clean = w.replace('-', ' ')
    try:
        cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 15
        """, (f'"{clean}"',))
        rows = cur.fetchall()
        if rows:
            by_author = {}
            for auth, work, sen in rows:
                if auth not in by_author:
                    by_author[auth] = []
                by_author[auth].append({'work': work, 'sentence': sen})
            hits[w] = by_author
    except Exception as e:
        pass

print(f"Words with hits: {len(hits)} / {len(words)}")
for w in sorted(hits.keys()):
    print(f"  {w}: {len(hits[w])} authors -> {list(hits[w].keys())[:3]}")

with open("scratch/sight_b4_corpus.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
