import sqlite3
import re

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

def search_corpus(term):
    c_cur.execute('''
        SELECT distinct s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 10
    ''', (f'"{term}"',))
    res = []
    seen = set()
    for a, w, s in c_cur.fetchall():
        if a not in seen:
            seen.add(a)
            res.append((a, w, s))
    return res

words_to_check = ['coal', 'coalesce', 'coalescence', 'deal', 'postal', 'real', 'really', 'seal', 'unseal', 'unsealed', 'aliment', 'alimentary', 'animalism', 'auroral', 'criminality', 'oratorical', 'palliative', 'realist']
for w in words_to_check:
    hits = search_corpus(w)
    print(f"{w}: {len(hits)} unique authors -> {[h[0] for h in hits]}")
