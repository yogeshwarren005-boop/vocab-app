# -*- coding: utf-8 -*-
import os, glob, re, sqlite3
from nltk.corpus import wordnet

db_path = os.path.join("main app", "corpus", "citation_corpus.db")
con = sqlite3.connect(db_path)
cur = con.cursor()

files = glob.glob('App database/Latin roots/Cluster Action/Dashboard — act/*.md')
words = [os.path.splitext(os.path.basename(f))[0] for f in files if not os.path.basename(f).startswith('Dashboard') and not os.path.basename(f).startswith('Word Triage')]

print(f"Total target words in act: {len(words)}")

for w in words[:15]:
    syns = wordnet.synsets(w.replace(' ', '_'))
    def1 = syns[0].definition() if syns else "None"
    def2 = syns[1].definition() if len(syns) > 1 else "None"
    
    # Query FTS5
    # clean query string
    q_word = re.sub(r'[^a-zA-Z0-9]', '', w)
    res = []
    if q_word:
        try:
            matches = cur.execute("""
                SELECT s.author, s.work, s.sentence 
                FROM sentences_fts f
                JOIN sentences s ON f.rowid = s.id
                WHERE sentences_fts MATCH ?
                LIMIT 10;
            """, (f'"{q_word}"',)).fetchall()
            
            # Filter for exact word boundary
            pat = re.compile(rf'\b{re.escape(w)}\b', re.IGNORECASE)
            seen_authors = set()
            for r in matches:
                if r[0] not in seen_authors and pat.search(r[2]):
                    seen_authors.add(r[0])
                    res.append(r)
                if len(res) >= 3:
                    break
        except Exception as e:
            pass
            
    print(f"\nWord: {w}")
    print(f"  Def 1: {def1}")
    print(f"  Def 2: {def2}")
    print(f"  Corpus Quotes ({len(res)}):")
    for r in res:
        print(f"    - {r[0]} ({r[1]}): {r[2][:80]}...")

con.close()
