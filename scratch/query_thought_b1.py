# -*- coding: utf-8 -*-
import sqlite3
import os
import json

target = r"App database/Latin roots/Cluster Thought"
dirs = [
    'Dashboard — cern',
    'Dashboard — cogit',
    'Dashboard — cogn',
    'Dashboard — estim',
    'Dashboard — ment',
    'Dashboard — opin'
]

words = []
for d in dirs:
    dp = os.path.join(target, d)
    for f in os.listdir(dp):
        if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field')):
            words.append(f[:-3])

words = sorted(list(set(words)))
print(f"Total unique words to query in Thought Batch 1: {len(words)}")

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
            WHERE f.sentence MATCH ? LIMIT 10
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

with open("scratch/thought_b1_corpus.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
