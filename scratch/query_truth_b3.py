import os
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

base_path = 'App database/Latin roots/Cluster Truth, Deception & Error'
ver_dir = [d for d in os.listdir(base_path) if d.endswith('ver')][0]
p = os.path.join(base_path, ver_dir)
all_words = sorted([f[:-3] for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])

b3_words = all_words[:160]
print(f"Total words in Truth Batch 3: {len(b3_words)}")

results = {}
found_3 = 0
for w in b3_words:
    clean_w = w.replace('-', ' ')
    query = f'"{clean_w}"'
    try:
        cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 400
        """, (query,))
        rows = cur.fetchall()
    except Exception as e:
        rows = []

    seen = set()
    dedup = []
    pattern = re.compile(rf'\b{re.escape(clean_w)}\b', re.IGNORECASE)
    for a, wrk, st in rows:
        if a not in seen:
            if pattern.search(st):
                clean_st = ' '.join(st.split())
                if len(clean_st) >= 35 and len(clean_st) <= 450:
                    seen.add(a)
                    dedup.append({"author": a, "work": wrk, "sentence": clean_st})
        if len(dedup) >= 3:
            break
    
    results[w] = dedup
    if len(dedup) >= 3:
        found_3 += 1

print(f"Found 3+ quotes for {found_3}/{len(b3_words)} words")

with open('scratch/truth_b3_corpus.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Saved to scratch/truth_b3_corpus.json")
