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

man_words = [
    'counterman', 'emancipate', 'emancipated', 'emancipation', 'emancipative', 'emancipator', 'man', 'manacle',
    'manage', 'manageable', 'management', 'manager', 'mandatary', 'mandate', 'mandator', 'mandatory', 'maneuver',
    'maneuverable', 'maneuverer', 'manly', 'manned', 'manner', 'mannered', 'mannerism', 'mannerly', 'manor',
    'mansion', 'manual', 'manually', 'manufacture', 'manufactured', 'manufacturer', 'manufacturing', 'manumission',
    'manumit', 'manumitter', 'manure', 'manuscript', 'mismanage', 'mismanagement', 'nonmandatory', 'postman',
    'superman', 'unman', 'unmanageable', 'unmanly', 'unmannerly'
]

found_man = {}
for w in man_words:
    found_man[w] = get_quotes(w)
    print(f"{w}: {len(found_man[w])} found")
