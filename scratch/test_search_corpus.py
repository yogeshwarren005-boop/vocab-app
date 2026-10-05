import sqlite3

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c = conn.cursor()

def search_term(t):
    try:
        c.execute('SELECT s.author, s.work, s.sentence FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ? LIMIT 10', (f'"{t}"',))
        res = c.fetchall()
        print(f'Term {t}: {len(res)} hits')
        for a, w, s in res[:3]:
            print(f'  {a} ({w}): {s[:100]}...')
    except Exception as e:
        print(f'Error searching {t}: {e}')

for t in ['antacid', 'tacit', 'taciturn', 'tacitus', 'taco', 'tacoma', 'taconite', 'setaceous', 'crayfish', 'poplar']:
    search_term(t)

conn.close()
