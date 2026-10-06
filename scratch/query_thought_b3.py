# -*- coding: utf-8 -*-
"""
query_thought_b3.py
Queries citation_corpus.db for Thought Batch 3:
- Dashboard — mens (30 words)
- Dashboard — sap (44 words)
- Dashboard — scrup (8 words)
Total: 82 words.
"""
import sqlite3
import os
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

dashboards = [
    r"App database/Latin roots/Cluster Thought/Dashboard — mens",
    r"App database/Latin roots/Cluster Thought/Dashboard — sap",
    r"App database/Latin roots/Cluster Thought/Dashboard — scrup"
]

all_words = []
for d in dashboards:
    wds = [f[:-3] for f in os.listdir(d) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))]
    all_words.extend(wds)

words = sorted(list(set(all_words)))
print(f"Total unique words in Batch 3: {len(words)}")

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

with open("scratch/thought_b3_corpus.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
