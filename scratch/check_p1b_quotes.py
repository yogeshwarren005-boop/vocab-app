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

words_p1b = [
    'labored', 'laborer', 'laboring', 'laborious', 'laboriously', 'laboriousness', 'laborsaving', 'labour-intensive',
    'labour', 'laboured', 'labourer', 'labouring', 'labourite', 'laboursaving', 'labrador', 'labret', 'labridae',
    'labrocyte', 'labrouste', 'labrum', 'laburnum', 'labyrinth', 'labyrinthian', 'labyrinthine', 'labyrinthitis',
    'labyrinthodont', 'labyrinthodonta', 'labyrinthodontia', 'mislabeled', 'unelaborate', 'unelaborated', 'unlabeled', 'unlabelled'
]

found = {}
for w in words_p1b:
    found[w] = get_quotes(w)

for w in ['laborer', 'laboring', 'laborious', 'laboriously', 'laboured', 'labourer', 'labouring', 'labyrinth']:
    print('=== ' + w + ' ===')
    for a, wrk, s in found[w][:3]:
        print(f'  {a} ({wrk}): {s}')

