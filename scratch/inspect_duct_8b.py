# -*- coding: utf-8 -*-
import sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")

words = [
  'introductory', 'misconduct', 'nonconducting', 'nonconductive', 'nonconductor',
  'nondeductible', 'nonproductive', 'overproduction', 'product', 'production',
  'productive', 'productively', 'productiveness', 'productivity', 'reductant',
  'reductase', 'reductio', 'reduction', 'reductionism', 'reductionist',
  'reductive', 'reductivism', 'reintroduction', 'reproduction', 'reproductive',
  'seduction', 'seductive', 'seductively', 'seductress', 'subduction',
  'superconductivity', 'transduction', 'underproduction', 'unproductive',
  'unproductively', 'unproductiveness', 'unseductive'
]

dict_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
dict_cur = dict_conn.cursor()

quote_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
quote_cur = quote_conn.cursor()

for w in words:
    dict_cur.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    drows = dict_cur.fetchall()
    
    quote_cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 5
    """, (f'"{w}"',))
    qrows = quote_cur.fetchall()
    
    print(f"\n=== Word: {w} ===")
    print(f"  Defs: {len(drows)}")
    for d in drows[:2]:
        print(f"    [{d[0]}]: {d[1][:100]}...")
    print(f"  Quotes: {len(qrows)}")
    for q in qrows[:3]:
        print(f"    - {q[0]} (*{q[1]}*): {q[2][:90]}...")
