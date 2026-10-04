import sqlite3

words = ['adipose', 'cervical', 'dentist', 'dorsal', 'frontal', 'lacrimal']
c = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = c.cursor()
for w in words:
    cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 3
    ''', (f'"{w}"',))
    res = cur.fetchall()
    print(w, '->', len(res), 'quotes found')
    for r in res:
        print('  ', r[0], f'({r[1]}):', r[2][:70])
