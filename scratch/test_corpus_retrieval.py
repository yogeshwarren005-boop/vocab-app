import sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")

conn_corp = sqlite3.connect("main app/corpus/citation_corpus.db")
conn_dict = sqlite3.connect("main app/corpus/local_dictionary.db")

test_words = ["debacle", "debar", "debase", "debenture", "debility", "debt", "debtor"]

for w in test_words:
    print(f"\n=== Word: {w} ===")
    
    # Dict definitions
    cur = conn_dict.cursor()
    cur.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? LIMIT 3", (w,))
    defs = cur.fetchall()
    print("Definitions found:", len(defs))
    for s, d in defs:
        print(f"  [{s}] {d[:100]}...")
        
    # Corpus quotes
    cur = conn_corp.cursor()
    query = """
    SELECT s.author, s.work, s.sentence 
    FROM sentences s 
    JOIN sentences_fts f ON s.id = f.rowid 
    WHERE f.sentence MATCH ?
    LIMIT 20
    """
    try:
        cur.execute(query, (f'"{w}"',))
        quotes = cur.fetchall()
        print("Quotes found:", len(quotes))
        distinct_authors = {}
        for auth, work, sent in quotes:
            if auth not in distinct_authors:
                distinct_authors[auth] = (work, sent)
        print(f"Distinct authors ({len(distinct_authors)}): {list(distinct_authors.keys())[:5]}")
    except Exception as e:
        print("Query error:", e)
