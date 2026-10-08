import sqlite3, re

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

def get_quotes(word, limit=5):
    clean_w = word.replace('-', ' ')
    query = f'"{clean_w}"'
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 100
    """, (query,))
    rows = cur.fetchall()
    pattern = re.compile(rf'\b{re.escape(clean_w)}\b', re.IGNORECASE)
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

pod_words = [
    'dipodidae', 'dipodomys', 'pod', 'podalgia', 'podalyria', 'podargidae', 'podargus', 'podaxaceae',
    'podcast', 'podetium', 'podiatrist', 'podiatry', 'podiceps', 'podicipedidae', 'podicipediformes',
    'podicipitiformes', 'podilymbus', 'podium', 'podlike', 'podocarp', 'podocarpaceae', 'podocarpus',
    'podophyllum', 'podsol'
]

found_pod = {}
for w in pod_words:
    found_pod[w] = get_quotes(w)
    print(f"{w}: {len(found_pod[w])} found")
