# -*- coding: utf-8 -*-
import sqlite3, os, json

folder = r"App database\Latin roots\Cluster Action\Dashboard — mer"
files = sorted([f for f in os.listdir(folder) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
b2_files = files[50:100]

c_dict = sqlite3.connect('main app/corpus/local_dictionary.db')
c_cit = sqlite3.connect('main app/corpus/citation_corpus.db')

b2_info = {}
for fname in b2_files:
    w = fname[:-3]
    d_rows = c_dict.execute('SELECT source, definition FROM dictionary_entries WHERE word = ?', (w,)).fetchall()
    if not d_rows:
        d_rows = c_dict.execute('SELECT source, definition FROM dictionary_entries WHERE word = ?', (w.replace('-', ' '),)).fetchall()
    
    q_rows = []
    try:
        q_rows = c_cit.execute('SELECT s.author, s.work, s.sentence FROM sentences_fts fts JOIN sentences s ON fts.rowid = s.id WHERE sentences_fts MATCH ? LIMIT 15', (w,)).fetchall()
    except:
        pass
    
    b2_info[fname] = {
        'word': w,
        'defs': d_rows[:3],
        'quotes': q_rows[:5]
    }

with open('scratch/mer_b2_raw.json', 'w', encoding='utf-8') as f:
    json.dump(b2_info, f, indent=2)

print('Dumped mer_b2_raw.json for', len(b2_files), 'words:')
for i, f in enumerate(b2_files):
    print(f'{i+51}: {f}')
