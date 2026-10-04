import sqlite3

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

test_words = ["facial", "facile", "facilitate", "facility", "facsimile", "faculty", "magnificent", "manufacture", "office", "official"]

for w in test_words:
    # check dictionary
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ? LIMIT 2", (w,))
    defs = [r[0] for r in d_cur.fetchall()]
    
    # check citations via FTS
    c_cur.execute("""
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 5
    """, (f'"{w}"',))
    quotes = c_cur.fetchall()
    
    print(f"=== {w} ===")
    print(f"  Defs found: {len(defs)}")
    print(f"  Quotes found: {len(quotes)} (authors: {list(set(q[0] for q in quotes))})")

c_conn.close()
d_conn.close()
