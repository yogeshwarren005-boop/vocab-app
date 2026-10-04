# -*- coding: utf-8 -*-
import sqlite3, os, sys, json, re

sys.stdout.reconfigure(encoding="utf-8")

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

folder = "App database/Latin roots/Cluster Emotion/Dashboard — pat"
files = sorted([f for f in os.listdir(folder) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")])

results = {}

for f in files:
    w = f[:-3]
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ? LIMIT 5", (w,))
    defs = [r[0] for r in d_cur.fetchall()]
    
    clean_w = w.replace("-", " ")
    try:
        c_cur.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 50
        """, (f'"{clean_w}"',))
        raw_quotes = c_cur.fetchall()
    except Exception as e:
        raw_quotes = []
        
    pattern = re.compile(rf"\b{re.escape(w)}\b", re.IGNORECASE)
    quotes_by_author = {}
    for author, work, sent in raw_quotes:
        sent = sent.strip()
        if len(sent) < 30 or len(sent) > 400:
            continue
        m = pattern.search(sent)
        if m and author not in quotes_by_author:
            quotes_by_author[author] = {
                "author": author,
                "work": work,
                "sentence": sent
            }
            
    results[w] = {
        "defs": defs,
        "quotes": list(quotes_by_author.values())
    }

with open("scratch/pat_db_dump.json", "w", encoding="utf-8") as out:
    json.dump(results, out, ensure_ascii=False, indent=2)

print(f"Total words in Dashboard — pat: {len(results)}")
ready_count = sum(1 for w, d in results.items() if len(d["quotes"]) >= 3)
print(f"Words with >= 3 distinct authentic quotes directly in DB: {ready_count}")
print(f"Words needing supplemented quotes: {len(results) - ready_count}")

c_conn.close()
d_conn.close()
