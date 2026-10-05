import sqlite3, json

words = ['appreciable', 'appreciably', 'appreciate', 'appreciated', 'appreciation', 'appreciative', 'appreciatively', 'appreciativeness', 'appreciator', 'deprecate', 'deprecating', 'deprecation', 'deprecative', 'deprecatively', 'deprecatory', 'depreciate', 'depreciating', 'depreciation', 'depreciative', 'depreciator', 'depreciatory', 'imprecate', 'imprecation', 'imprecise', 'imprecisely', 'impreciseness', 'imprecision', 'inappreciable', 'precambrian', 'precancerous', 'precarious', 'precariously', 'precariousness', 'precast', 'precative', 'precatory', 'precaution', 'precautional', 'precautionary', 'precava', 'precede', 'precedence', 'precedency', 'precedent', 'precedented', 'precedentedly', 'precedential', 'preceding', 'precentor', 'precentorship', 'precept', 'preceptor', 'preceptorship', 'precess', 'precession', 'precinct', 'preciosity', 'precious', 'preciously', 'preciousness', 'precipice', 'precipitance', 'precipitancy', 'precipitant', 'precipitate', 'precipitately', 'precipitateness', 'precipitating', 'precipitation', 'precipitator', 'precipitin', 'precipitous', 'precipitously', 'precipitousness', 'precis', 'precise', 'precisely', 'preciseness', 'precision', 'preclinical', 'preclude', 'preclusion', 'preclusive', 'precocial', 'precocious', 'precociously', 'precociousness', 'precocity', 'precognition', 'precognitive', 'preconceive', 'preconceived', 'preconception', 'preconcerted', 'precondition', 'preconditioned', 'precook', 'precooked', 'precooled', 'precordial', 'precordium', 'precursor', 'precursory', 'unappreciated', 'unappreciative', 'unappreciatively', 'unprecedented', 'unprecedentedly']

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

d_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
d_cur = d_conn.cursor()

results = {}
for w in words:
    d_cur.execute('SELECT definition FROM dictionary_entries WHERE word = ?', (w,))
    defs = [r[0] for r in d_cur.fetchall()]
    
    # search citations
    c_cur.execute('''
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 25
    ''', (f'"{w}"',))
    quotes = [{'author': r[0], 'work': r[1], 'sentence': r[2]} for r in c_cur.fetchall()]
    
    results[w] = {
        'defs': defs,
        'quotes': quotes,
        'unique_authors': len(set(q['author'] for q in quotes))
    }

c_conn.close()
d_conn.close()

with open('scratch/prec_raw_check.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

low_quotes = [w for w, v in results.items() if v['unique_authors'] < 3]
print(f'Total words: {len(words)}')
print(f'Words with >=3 unique authors in corpus: {len(words) - len(low_quotes)}')
print(f'Words with < 3 unique authors in corpus: {len(low_quotes)}')
print('Low quote words:', low_quotes)
