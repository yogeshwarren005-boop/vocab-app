import sqlite3, json, sys
sys.stdout.reconfigure(encoding='utf-8')

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()

words = [
  'allogamous', 'allogamy', 'allogeneic', 'allograft', 'allograph', 'allographic', 'analogical', 'analogise', 'analogist', 'analogize', 'analogous', 'analogously', 'analogy', 'anthologise', 'anthologist', 'anthologize', 'anthology', 'antilog', 'antilogarithm', 'apologetic', 'apologise', 'apologist', 'apologize', 'apology', 'archaeologic', 'archaeological', 'archaeologist', 'archaeology', 'biologic', 'biological', 'biologically', 'biologism', 'biologist', 'biologistic', 'biology', 'catalog', 'cataloger', 'catalogue', 'cataloguer', 'collogue', 'cologne', 'dialogue', 'dislogistic', 'ecologic', 'ecological', 'ecologically', 'ecologist', 'ecology', 'epilogue'
]

def search(w):
    cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE sentences_fts MATCH ? 
        LIMIT 30
    ''', (f'"{w}"',))
    rows = cur.fetchall()
    seen = set()
    res = []
    for a, wrk, sent in rows:
        if a not in seen and len(a) > 2 and len(wrk) > 2:
            seen.add(a)
            res.append((a, wrk, sent))
    return res

results = {}
for w in words:
    matches = search(w)
    dict_cur.execute('SELECT definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number', (w,))
    defs = [r[0] for r in dict_cur.fetchall()]
    results[w] = {
        'matches_count': len(matches),
        'defs_count': len(defs),
        'matches': matches[:5],
        'defs': defs[:3]
    }
    print(f"{w}: {len(matches)} corpus authors | {len(defs)} dict defs")

with open('scratch/log_part1_raw.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
