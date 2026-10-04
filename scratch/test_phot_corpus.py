import sqlite3

c = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = c.cursor()
words = ['photo', 'photograph', 'photographer', 'photography', 'photon', 'photosynthesis', 'photosphere', 'photochemical']
for w in words:
    cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 5
    ''', (f'"{w}"',))
    res = cur.fetchall()
    print(w, ':', len(res), 'quotes')
    for r in res[:2]:
        print('  ', r[0], f'({r[1]}):', r[2][:80])
