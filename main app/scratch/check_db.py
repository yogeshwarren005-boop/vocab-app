import sqlite3
con = sqlite3.connect("main app/corpus/citation_corpus.db")
cur = con.cursor()
tables = [r[0] for r in cur.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()]
print("Tables:", tables)
count = cur.execute("SELECT COUNT(*) FROM sentences").fetchone()[0]
print("Total sentences in db:", count)
authors = cur.execute("SELECT author, COUNT(*) FROM sentences GROUP BY author").fetchall()
print("Authors count:", len(authors))
for a, c in authors[:15]:
    print(f"  {a}: {c}")
