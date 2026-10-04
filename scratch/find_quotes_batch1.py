import sqlite3, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

def get_distinct_quotes(word, limit=10):
    cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE sentences_fts MATCH ? 
        LIMIT 50
    ''', (f'"{word}"',))
    rows = cur.fetchall()
    
    # filter by distinct authors
    seen_authors = set()
    res = []
    for a, w, sent in rows:
        if a not in seen_authors and len(a) > 2 and len(w) > 2:
            seen_authors.add(a)
            res.append((a, w, sent))
            if len(res) >= limit:
                break
    return res

words = [
    'concern', 'concerned', 'concernedly', 'discern', 'discernible', 
    'discerning', 'discernment', 'indiscernible', 'unconcern', 
    'unconcerned', 'unconcernedly', 'undiscerning',
    'cogitate', 'cogitation', 'estimable', 'estimate', 'estimation', 
    'inestimable', 'overestimate', 'underestimate', 'opine', 'opinion', 
    'opinionated', 'scruple', 'scruples', 'scrupulous', 'scrupulously', 
    'scrupulousness', 'unscrupulous'
]

for w in words:
    quotes = get_distinct_quotes(w, 5)
    print(f"=== {w} ({len(quotes)} distinct author matches) ===")
    for a, wrk, s in quotes[:3]:
        print(f"  * {a} ({wrk}): {s[:100]}...")
