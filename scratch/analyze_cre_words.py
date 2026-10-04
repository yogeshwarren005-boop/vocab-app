# -*- coding: utf-8 -*-
import os, sqlite3, re, json

cre_dir = r"App database\Latin roots\Cluster Action\Dashboard — cre"
creat_dir = r"App database\Latin roots\Cluster Action\Dashboard — creat"

creat_files = set(f for f in os.listdir(creat_dir) if f.endswith('.md'))
all_cre_files = sorted([f for f in os.listdir(cre_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])

remaining = [f for f in all_cre_files if f not in creat_files]
print(f"Remaining words to curate in cre: {len(remaining)}")

c_dict = sqlite3.connect('main app/corpus/local_dictionary.db')
c_cit = sqlite3.connect('main app/corpus/citation_corpus.db')

words_info = {}
for fname in remaining:
    w = fname[:-3]
    d_rows = c_dict.execute('SELECT source, definition FROM dictionary_entries WHERE word = ?', (w,)).fetchall()
    if not d_rows:
        d_rows = c_dict.execute('SELECT source, definition FROM dictionary_entries WHERE word = ?', (w.replace('-', ' '),)).fetchall()
    
    q_rows = []
    try:
        q_rows = c_cit.execute('SELECT s.author, s.work, s.sentence FROM sentences_fts fts JOIN sentences s ON fts.rowid = s.id WHERE sentences_fts MATCH ? LIMIT 15', (w,)).fetchall()
    except:
        pass
    
    pattern = re.compile(rf'\b({re.escape(w)})\b', re.IGNORECASE)
    valid_q = []
    seen = set()
    for a, wk, sent in q_rows:
        if a in seen: continue
        if pattern.search(sent) and 25 < len(sent) < 300:
            seen.add(a)
            valid_q.append((a, wk, sent))
            if len(valid_q) == 3: break
            
    words_info[fname] = {
        'word': w,
        'defs': d_rows[:2],
        'quotes': valid_q
    }

with open('scratch/cre_remaining_raw.json', 'w', encoding='utf-8') as f:
    json.dump(words_info, f, indent=2)

print(f"Done dumping cre_remaining_raw.json. Total words with 3 quotes: {sum(1 for v in words_info.values() if len(v['quotes']) == 3)} / {len(remaining)}")
