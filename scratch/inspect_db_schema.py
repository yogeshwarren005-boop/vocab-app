import sqlite3

for db_path in ["main app/corpus/citation_corpus.db", "main app/corpus/local_dictionary.db"]:
    print(f"=== {db_path} ===")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT name, sql FROM sqlite_master WHERE type='table'")
    for name, sql in c.fetchall():
        print(f"Table: {name}\nSQL: {sql}\n")
    conn.close()
