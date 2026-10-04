import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

corpus_conn = sqlite3.connect(r'main app/corpus/citation_corpus.db')
corpus_cur = corpus_conn.cursor()

def test_search(term):
    print(f"--- Searching for: {term} ---")
    try:
        corpus_cur.execute('''
            SELECT s.author, s.work, s.sentence 
            FROM sentences s 
            JOIN sentences_fts f ON s.id = f.rowid 
            WHERE sentences_fts MATCH ? 
            LIMIT 5
        ''', (term,))
        rows = corpus_cur.fetchall()
        print(f"FTS match '{term}': {len(rows)} found")
        for r in rows:
            print(f"  {r[0]} ({r[1]}): {r[2][:100]}...")
    except Exception as e:
        print("FTS error:", e)

    # Also try LIKE on sentences table
    corpus_cur.execute('''
        SELECT author, work, sentence 
        FROM sentences 
        WHERE sentence LIKE ? 
        LIMIT 5
    ''', (f"%{term}%",))
    rows_like = corpus_cur.fetchall()
    print(f"LIKE '%{term}%': {len(rows_like)} found")
    for r in rows_like:
        print(f"  {r[0]} ({r[1]}): {r[2][:100]}...")

for w in ['cernuous', 'secern', 'cogitable', 'misestimate', 'unscrupulously']:
    test_search(w)
