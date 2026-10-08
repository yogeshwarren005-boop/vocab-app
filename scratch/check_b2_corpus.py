# -*- coding: utf-8 -*-
import sqlite3
import json

words = json.load(open('scratch/number_b2_words.json', encoding='utf-8'))
c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

has_3_authors = 0
words_with_hits = {}
for w in words:
    # try fts match
    query = f'"{w}"'
    try:
        c_cur.execute('''
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
        ''', (query,))
        rows = c_cur.fetchall()
    except Exception as e:
        rows = []
    authors = set(r[0] for r in rows)
    words_with_hits[w] = len(authors)
    if len(authors) >= 3:
        has_3_authors += 1

print(f"Words with >= 3 distinct authors in citation_corpus: {has_3_authors} / {len(words)}")
zero_hits = [w for w, count in words_with_hits.items() if count == 0]
print(f"Words with 0 authors: {len(zero_hits)}: {zero_hits[:15]}")
c_conn.close()
