import sqlite3, sys

sys.stdout.reconfigure(encoding="utf-8")

for db in ['main app/corpus/local_dictionary.db', 'main app/corpus/citation_corpus.db']:
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
    print(db, cur.fetchall())
