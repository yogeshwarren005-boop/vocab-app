import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')
conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

def search(w):
    cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 10
    ''', (f'"{w}"',))
    rows = cur.fetchall()
    print(f'=== {w} ({len(rows)} hits) ===')
    seen = set()
    for a, wrk, st in rows:
        if a not in seen:
            seen.add(a)
            clean_s = ' '.join(st.split())
            print(f'  {a} | {wrk} | {clean_s[:90]}...')

words = [
    'fallibility', 'fallible', 'fallout', 'falseness', 'falsetto', 
    'falsification', 'falsify', 'falsity', 'falstaff', 'infallibility', 
    'unfaltering', 'unfalteringly', 'approbate', 'approbation', 
    'approbative', 'approbatory', 'disapprobation', 'improbability', 
    'improbable', 'opprobrious', 'opprobrium'
]
for w in words:
    search(w)
