import sqlite3

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

def search_term(t):
    c_cur.execute('''
        SELECT distinct s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 10
    ''', (f'"{t}"',))
    res = {}
    for a, w, s in c_cur.fetchall():
        if a not in res and len(s) > 30 and len(s) < 350:
            res[a] = (w, s)
    return res

words = ['animal', 'animals', 'deal', 'dealing', 'dealer', 'dealers', 'real', 'really', 'seal', 'sealed', 'sealing', 'unreal']
for w in words:
    hits = search_term(w)
    print(f"{w}: {len(hits)} authors -> {list(hits.keys())}")
