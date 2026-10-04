import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn1 = sqlite3.connect('main app/corpus/citation_corpus.db')
c1 = conn1.cursor()
tables1 = c1.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print('citation_corpus tables:', tables1)
for t in tables1:
    tname = t[0]
    print(f'Table {tname}:', c1.execute(f"PRAGMA table_info({tname})").fetchall())
    print(f'Count {tname}:', c1.execute(f"SELECT count(*) FROM {tname}").fetchone()[0])

conn2 = sqlite3.connect('main app/corpus/local_dictionary.db')
c2 = conn2.cursor()
tables2 = c2.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print('local_dictionary tables:', tables2)
for t in tables2:
    tname = t[0]
    print(f'Table {tname}:', c2.execute(f"PRAGMA table_info({tname})").fetchall())
    print(f'Count {tname}:', c2.execute(f"SELECT count(*) FROM {tname}").fetchone()[0])
