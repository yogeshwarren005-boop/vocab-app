# -*- coding: utf-8 -*-
import os
import sqlite3
import json
import re

base_path = 'App database/Latin roots/Cluster Turning'
dashboards = ['mut', 'tort', 'vers']

all_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]
dir_map = {}
for root in dashboards:
    matched = [d for d in all_dirs if d.split('—')[-1].strip() == root or d.endswith(' ' + root)][0]
    dir_map[root] = matched

words_by_root = {}
for root, dname in dir_map.items():
    tdir = os.path.join(base_path, dname)
    files = sorted([f[:-3] for f in os.listdir(tdir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    if root == 'vers':
        words_by_root[root] = files[:35]
    else:
        words_by_root[root] = files

all_words = []
for root in ['mut', 'tort', 'vers']:
    all_words.extend(words_by_root[root])

print(f"Total words for Batch 3: {len(all_words)}")
for r, ws in words_by_root.items():
    print(f"  {r}: {len(ws)}")

# Save word list
with open('scratch/turning_b3_words.json', 'w', encoding='utf-8') as f:
    json.dump({
        'dir_map': dir_map,
        'words_by_root': words_by_root,
        'all_words': all_words
    }, f, indent=2)

# Query corpus database if available
corpus_hits = {}
db_path = 'App database/Corpus/vocab.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    
    # Check tables
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [r[0] for r in cur.fetchall()]
    print("Tables:", tables)
    
    # Query sentences for each word
    for word in all_words:
        hits = []
        cur.execute("SELECT author, work, sentence FROM sentences WHERE word = ? LIMIT 10", (word,))
        rows = cur.fetchall()
        for r in rows:
            hits.append({
                'author': r[0],
                'work': r[1],
                'sentence': r[2]
            })
        if hits:
            corpus_hits[word] = hits
            
    conn.close()

print(f"Words with corpus hits: {len(corpus_hits)} / {len(all_words)}")
with open('scratch/turning_b3_corpus.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_hits, f, indent=2)
