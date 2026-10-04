import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

def search(w):
    cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE sentences_fts MATCH ? 
        LIMIT 30
    ''', (f'"{w}"',))
    rows = cur.fetchall()
    seen = set()
    res = []
    for a, wrk, sent in rows:
        if a not in seen and len(a) > 2 and len(wrk) > 2:
            seen.add(a)
            res.append((a, wrk, sent))
    return res

words = [
    'commensal', 'commensurable', 'commensurate', 'dimension', 'dimensional',
    'immense', 'immensely', 'immensity', 'incommensurable', 'incommensurate',
    'mensuration', 'comment', 'commentary', 'commentator', 'demented', 
    'dementia', 'interment', 'mental', 'mentality', 'mentally', 'mention', 
    'mentor', 'unmentionable'
]

for w in words:
    res = search(w)
    print(f"{w}: {len(res)} distinct authors found")
