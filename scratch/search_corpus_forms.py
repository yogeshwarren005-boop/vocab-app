# -*- coding: utf-8 -*-
import sqlite3
import re

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

def search_stem(stem):
    try:
        c_cur.execute('''
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 30
        ''', (f'{stem}*',))
        rows = c_cur.fetchall()
        authors = {}
        for a, w, sent in rows:
            if a not in authors:
                authors[a] = (w, sent)
        return authors
    except Exception as e:
        return {}

test_words = ['decoy', 'decry', 'decouple', 'decrepit', 'decree', 'decrement', 'decrypt', 'decumbent', 'decussate']
for tw in test_words:
    res = search_stem(tw)
    print(f"Stem '{tw}*': {len(res)} distinct authors -> {list(res.keys())[:5]}")
