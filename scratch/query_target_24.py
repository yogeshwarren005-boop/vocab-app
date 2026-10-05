import sqlite3, json

conn_corp = sqlite3.connect("main app/corpus/citation_corpus.db")
conn_dict = sqlite3.connect("main app/corpus/local_dictionary.db")

target_words = [
    # 3 missing dict words:
    'benediction', 'benedictive', 'unpredicted',
    # 21 tac words:
    'altace', 'antacid', 'astacidae', 'astacura', 'astacus', 'attacapa', 'attacapan',
    'cotacachi', 'setaceous', 'tacamahac', 'tacca', 'taccaceae', 'tacit', 'tacitly',
    'taciturn', 'taciturnity', 'taciturnly', 'tacitus', 'taco', 'tacoma', 'taconite'
]

cur_dict = conn_dict.cursor()
cur_corp = conn_corp.cursor()

results = {}

for w in target_words:
    # Look up dict
    cur_dict.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? LIMIT 5", (w,))
    defs = cur_dict.fetchall()
    
    # Look up corpus quotes
    query = """
    SELECT s.author, s.work, s.sentence 
    FROM sentences s 
    JOIN sentences_fts f ON s.id = f.rowid 
    WHERE f.sentence MATCH ?
    LIMIT 25
    """
    quotes = []
    try:
        cur_corp.execute(query, (f'"{w}"',))
        quotes = cur_corp.fetchall()
    except Exception as e:
        pass
    
    distinct_authors = {}
    for auth, work, sent in quotes:
        if auth not in distinct_authors:
            distinct_authors[auth] = (work, sent)
            
    results[w] = {
        'defs': defs,
        'quotes': [{'author': a, 'work': wk, 'sentence': st} for a, (wk, st) in distinct_authors.items()]
    }
    print(f"{w:15} | defs: {len(defs):2} | authors: {len(distinct_authors):2}")

with open("scratch/target_24_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

conn_corp.close()
conn_dict.close()
