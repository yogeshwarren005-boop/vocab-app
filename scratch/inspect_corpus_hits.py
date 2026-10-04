import sqlite3
import json

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c = conn.cursor()

with open("scratch/corpus_hits_virtue.json", "r", encoding="utf-8") as f:
    hits = json.load(f)

for w, authors in hits.items():
    if len(authors) >= 3:
        print(f"=== {w} ({len(authors)} authors) ===")
        for auth, data in list(authors.items())[:4]:
            print(f"  {auth} ({data['work']}): {data['sentence'][:100]}...")
