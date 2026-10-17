import sqlite3, re

con = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = con.cursor()

authors = cur.execute('SELECT s.author, COUNT(*) FROM sentences_fts f JOIN sentences s ON f.rowid = s.id WHERE sentences_fts MATCH \'"act"\' GROUP BY s.author').fetchall()
print('Authors with act:', len(authors))
for a, c in authors[:10]:
    print(f'  {a}: {c}')
