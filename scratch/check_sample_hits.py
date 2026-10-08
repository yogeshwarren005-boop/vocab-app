import sqlite3, json, sys, re

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

def get_quotes(word, limit=5):
    query = f'"{word}"'
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 100
    """, (query,))
    rows = cur.fetchall()
    pattern = re.compile(rf'\b{re.escape(word)}\b', re.IGNORECASE)
    res = []
    seen = set()
    for a, wrk, st in rows:
        clean = ' '.join(st.split())
        if a not in seen and pattern.search(clean) and 35 <= len(clean) <= 450:
            seen.add(a)
            res.append((a, wrk, clean))
            if len(res) >= limit:
                break
    return res

words = ['elaborate', 'elaborately', 'collaborate', 'collaborator', 'label', 'labor', 'laboratory', 'labile']
for w in words:
    q = get_quotes(w)
    print(f"=== {w}: {len(q)} found ===")
    for a, wrk, s in q[:3]:
        print(f"  {a} ({wrk}): {s}")
