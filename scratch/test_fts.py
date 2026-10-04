import sqlite3

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

for q in ['ruin', 'corrode', 'vast', 'delete', 'distinguish']:
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE f.sentence MATCH ? 
        GROUP BY s.author 
        LIMIT 4
    """, (q,))
    rows = cur.fetchall()
    print(f"=== Query '{q}' ({len(rows)} distinct authors) ===")
    for r in rows:
        print(f"  {r[0]} (*{r[1]}*): {r[2][:90]}...")
