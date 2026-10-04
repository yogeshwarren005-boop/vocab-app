# -*- coding: utf-8 -*-
import os, sqlite3, re, json

with open('scratch/fac_157_problem_words.json', encoding='utf-8') as f:
    b1_files = json.load(f)[:50]

c_dict = sqlite3.connect('main app/corpus/local_dictionary.db')
c_cit = sqlite3.connect('main app/corpus/citation_corpus.db')

words_info = {}
for fname in b1_files:
    w = fname[:-3]
    d_rows = c_dict.execute('SELECT source, definition FROM dictionary_entries WHERE word = ?', (w,)).fetchall()
    if not d_rows:
        d_rows = c_dict.execute('SELECT source, definition FROM dictionary_entries WHERE word = ?', (w.replace('-', ' '),)).fetchall()
    
    q_rows = []
    try:
        q_rows = c_cit.execute('SELECT s.author, s.work, s.sentence FROM sentences_fts fts JOIN sentences s ON fts.rowid = s.id WHERE sentences_fts MATCH ? LIMIT 20', (w,)).fetchall()
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

with open('scratch/fac_b1_raw.json', 'w', encoding='utf-8') as f:
    json.dump(words_info, f, indent=2)

print(f"Dumped fac_b1_raw.json for {len(b1_files)} words.")
print(f"Words with 3 quotes: {sum(1 for v in words_info.values() if len(v['quotes']) == 3)} / {len(b1_files)}")
