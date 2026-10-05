import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()
check_words = ['corduroy', 'corduroys', 'dura', 'durability', 'durables', 'durum', 'endurable', 'endure', 'obdurately', 'perdurable', 'prima', 'prima donna', 'primaeval', 'primates', 'primed', 'primly', 'primness', 'primogeniture', 'primordial', 'primula']

for w in check_words:
    cur.execute('SELECT s.author, s.work, substr(s.sentence, 1, 120) FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ? LIMIT 5', (f'"{w}"',))
    rows = cur.fetchall()
    print(f'=== {w} === ({len(rows)})')
    for r in rows:
        print(f'  {r[0]} ({r[1]}): {r[2]}')
