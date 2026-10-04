# -*- coding: utf-8 -*-
import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words = ['delete', 'deleterious', 'deletion', 'mordacious', 'mordaciously', 'mordacity', 'mordant', 'quassia', 
         'detruncate', 'truncate', 'truncated', 'truncation', 'truncheon', 'truncocolumella',
         'devastate', 'devastating', 'devastation', 'sevastopol', 'vast', 'vastly', 'vastness',
         'ruin', 'ruination', 'ruined', 'ruiner', 'ruining', 'ruinous', 'ruinously',
         'contradistinguish', 'distinguish', 'distinguishable', 'distinguished', 'indistinguishability', 'indistinguishable', 'indistinguishably', 'undistinguished',
         'acrodont', 'corrode', 'corroded', 'corrodentia', 'corroding', 'corrosion', 'corrosive', 'corrosively', 'corrosiveness', 'corroval', 'electrodeless', 'erode', 'eroded', 'eroding', 'erosion', 'erosive', 'rodent']

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()

cite_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cite_cur = cite_conn.cursor()

results = {}
for w in words:
    dict_cur.execute('SELECT definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number', (w,))
    defs = [r[0] for r in dict_cur.fetchall()]
    
    try:
        cite_cur.execute('SELECT author, work, sentence FROM sentences_fts WHERE sentence MATCH ? LIMIT 10', (f'"{w}"',))
        cites = cite_cur.fetchall()
    except Exception as e:
        cites = []
        
    results[w] = {
        'defs_count': len(defs),
        'defs': defs[:3],
        'cites_count': len(cites),
        'cites': cites[:5]
    }

have_defs = sum(1 for w, d in results.items() if d['defs_count'] > 0)
have_cites = sum(1 for w, d in results.items() if d['cites_count'] >= 3)
print(f"Polled {len(words)} words:")
print(f"Words with Webster defs: {have_defs}/{len(words)}")
print(f"Words with >=3 FTS citations: {have_cites}/{len(words)}")

with open('scratch/destruction_batch1_poll.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
