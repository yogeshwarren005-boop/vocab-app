# -*- coding: utf-8 -*-
import sqlite3, os, sys

sys.stdout.reconfigure(encoding="utf-8")

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

folder = "App database/Latin roots/Cluster Emotion/Dashboard — tim"
files = [f for f in os.listdir(folder) if f.endswith(".md") and not f.startswith("Dashboard") and not f.startswith("Word Triage")]

quote_rich = []
quote_scarce = []

for f in files:
    w = f[:-3]
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ? LIMIT 2", (w,))
    defs = d_cur.fetchall()
    
    # check citations via FTS
    clean_w = w.replace("-", " ")
    try:
        c_cur.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 25
        """, (f'"{clean_w}"',))
        quotes = c_cur.fetchall()
    except Exception as e:
        quotes = []
    
    # Filter for exact word match in sentence
    valid_quotes = []
    seen_authors = set()
    import re
    word_pattern = re.compile(rf"\b{re.escape(w)}\b", re.IGNORECASE)
    for q in quotes:
        author, work, sent = q
        if author not in seen_authors and word_pattern.search(sent):
            seen_authors.add(author)
            valid_quotes.append(q)
            
    if len(seen_authors) >= 3:
        quote_rich.append((w, len(defs)))
    else:
        quote_scarce.append((w, len(seen_authors), len(defs)))

print(f"Total words: {len(files)}")
print(f"Quote rich (>= 3 distinct authors): {len(quote_rich)}")
print(f"Quote scarce (< 3 distinct authors): {len(quote_scarce)}")
print("\nQuote scarce words (< 3 authors in corpus):")
for w, na, nd in quote_scarce:
    print(f"  {w} (authors: {na}, defs: {nd})")

c_conn.close()
d_conn.close()
