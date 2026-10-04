# -*- coding: utf-8 -*-
import sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")

words = [
  'ducal', 'ducat', 'duce', 'duchess', 'duchy', 'duct', 'ductile',
  'ductileness', 'ductility', 'ductless', 'ductule', 'ductulus', 'educate',
  'educated', 'educatee', 'education', 'educational', 'educationalist',
  'educationally', 'educationist', 'educative', 'educator', 'educe', 'induce',
  'induced', 'inducement', 'inducer', 'inducible', 'inducing', 'inducive',
  'induct', 'inductance', 'inductee', 'induction', 'inductive', 'inductor',
  'introduce', 'introduction', 'introductory', 'irreducible'
]

dict_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
dict_cur = dict_conn.cursor()

quote_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
quote_cur = quote_conn.cursor()

for w in words:
    dict_cur.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    defs = dict_cur.fetchall()
    
    quote_cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 4
    """, (f'"{w}"',))
    quotes = quote_cur.fetchall()
    
    print(f"\n=== {w} === (defs: {len(defs)}, quotes: {len(quotes)})")
    for d in defs[:2]:
        print(f"  [{d[0]}]: {d[1][:100]}")
    for q in quotes[:3]:
        print(f"  - {q[0]} ({q[1]}): {q[2][:90]}")
