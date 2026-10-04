import os
import sqlite3
import json

dashboards = ['Dashboard — cern', 'Dashboard — cogit', 'Dashboard — estim', 'Dashboard — opin', 'Dashboard — scrup']
base_dir = r'App database/Latin roots/Cluster Thought'

dict_conn = sqlite3.connect(r'main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()

corpus_conn = sqlite3.connect(r'main app/corpus/citation_corpus.db')
corpus_cur = corpus_conn.cursor()

batch1_words = []
for d in dashboards:
    p = os.path.join(base_dir, d)
    if not os.path.exists(p):
        continue
    for f in os.listdir(p):
        if f.endswith('.md') and not f.startswith('Dashboard'):
            w = f[:-3].lower()
            batch1_words.append((d, w, os.path.join(p, f)))

print(f'Batch 1 total words: {len(batch1_words)}')

extracted = {}
for d, w, path in batch1_words:
    # Get definitions from dictionary_entries
    dict_cur.execute('SELECT source, definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number', (w,))
    rows = dict_cur.fetchall()
    defs = [r[1] for r in rows if r[1]]
    
    # Get corpus sentences
    corpus_cur.execute('''
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE sentences_fts MATCH ? 
        LIMIT 25
    ''', (f'"{w}"',))
    quotes = corpus_cur.fetchall()
    
    # Also inspect existing file for definitions and quotes
    with open(path, 'r', encoding='utf-8') as f_in:
        content = f_in.read()

    extracted[w] = {
        'dashboard': d,
        'path': path,
        'dict_defs': defs,
        'quotes_count': len(quotes),
        'quotes': [{'author': q[0], 'work': q[1], 'sentence': q[2]} for q in quotes[:15]],
        'file_content': content
    }

with open(r'scratch/thought_batch1_raw.json', 'w', encoding='utf-8') as f:
    json.dump(extracted, f, indent=2, ensure_ascii=False)

print('Saved raw data to scratch/thought_batch1_raw.json')
missing_quotes = [w for w, d in extracted.items() if len(d['quotes']) < 3]
print(f'Words with fewer than 3 quotes in corpus: {len(missing_quotes)} -> {missing_quotes}')
missing_defs = [w for w, d in extracted.items() if len(d['dict_defs']) < 2]
print(f'Words with fewer than 2 defs in dictionary: {len(missing_defs)} -> {missing_defs}')
