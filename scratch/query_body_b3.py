import os
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

c_path = 'App database/Latin roots/Cluster Body'
dashboards = [
    'Dashboard — dens',
    'Dashboard — dexter',
    'Dashboard — faci',
    'Dashboard — fili',
    'Dashboard — gingiv',
    'Dashboard — rud',
    'Dashboard — soror',
    'Dashboard — spin',
    'Dashboard — ped'
]

b3_words = []
for d in dashboards:
    d_path = os.path.join(c_path, d)
    words = [f[:-3] for f in os.listdir(d_path) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')]
    b3_words.extend(words)

b3_words.sort()
print(f"Total words in Body Batch 3: {len(b3_words)}")

def query_words(word_list, output_file):
    results = {}
    found_3 = 0
    for w in word_list:
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
        pattern = re.compile(rf'\b{re.escape(clean_w)}\b', re.IGNORECASE)
        for a, wrk, st in rows:
            if a not in seen:
                if pattern.search(st):
                    clean_st = ' '.join(st.split())
                    if len(clean_st) >= 30 and len(clean_st) <= 450:
                        seen.add(a)
                        dedup.append({"author": a, "work": wrk, "sentence": clean_st})
            if len(dedup) >= 3:
                break
        
        results[w] = dedup
        if len(dedup) >= 3:
            found_3 += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print(f"Results for {len(word_list)} words: {found_3} have 3+ distinct authors.")
    return results

query_words(b3_words, "scratch/body_b3_corpus.json")
