import sqlite3

for db_path in ["main app/corpus/local_dictionary.db", "main app/corpus/citation_corpus.db"]:
    print(f"=== {db_path} ===")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
    for row in cur.fetchall():
        print(row)
