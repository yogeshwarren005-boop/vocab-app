import os, sqlite3, json, sys
sys.stdout.reconfigure(encoding='utf-8')

p = r'App database/Latin roots/Cluster Thought/Dashboard — cogn'
files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')])

corpus_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
corpus_cur = corpus_conn.cursor()

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()

def search_corpus(w):
    corpus_cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE sentences_fts MATCH ? 
        LIMIT 30
    ''', (f'"{w}"',))
    return corpus_cur.fetchall()

cogn_data = {}
for f in files:
    w = f[:-3].lower()
    with open(os.path.join(p, f), 'r', encoding='utf-8') as fin:
        content = fin.read()
    
    # get dict defs
    dict_cur.execute('SELECT source, definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number', (w,))
    dict_defs = [r[1] for r in dict_cur.fetchall()]

    # get corpus
    corpus_rows = search_corpus(w)
    
    # distinct authors
    distinct_quotes = []
    seen = set()
    for a, wrk, s in corpus_rows:
        if a not in seen and len(a) > 2 and len(wrk) > 2:
            seen.add(a)
            distinct_quotes.append({'author': a, 'work': wrk, 'sentence': s})

    cogn_data[w] = {
        'dict_defs': dict_defs,
        'distinct_quotes': distinct_quotes[:5],
        'existing_content': content
    }

print(f"Loaded {len(cogn_data)} words in Dashboard — cogn.")
with open('scratch/cogn_raw.json', 'w', encoding='utf-8') as fout:
    json.dump(cogn_data, fout, indent=2, ensure_ascii=False)

for w, d in cogn_data.items():
    print(f"{w}: {len(d['dict_defs'])} defs | {len(d['distinct_quotes'])} corpus quotes")
