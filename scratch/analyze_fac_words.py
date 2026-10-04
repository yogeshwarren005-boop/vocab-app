# -*- coding: utf-8 -*-
import os, sqlite3, re, json

base_action = r"App database\Latin roots\Cluster Action"
fac_dir = os.path.join(base_action, "Dashboard — fac")

all_fac = sorted([f for f in os.listdir(fac_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])

# check which ones are already grafted / passing
import subprocess
passing = set()
for f in all_fac:
    fpath = os.path.join(fac_dir, f)
    with open(fpath, "r", encoding="utf-8") as file:
        content = file.read()
    if "📜 **" in content and "Academic Lexicon" not in content and "Classic Author" not in content:
        # verify with audit
        res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", fpath], capture_output=True, encoding="utf-8", errors="replace")
        if "100% PRISTINE" in res.stdout:
            passing.add(f)

print(f"Total words in fac: {len(all_fac)}")
print(f"Already passing in fac: {len(passing)}")
remaining = [f for f in all_fac if f not in passing]
print(f"Remaining to curate: {len(remaining)}")

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

with open('scratch/fac_remaining_raw.json', 'w', encoding='utf-8') as f:
    json.dump(words_info, f, indent=2)

print(f"Dumped fac_remaining_raw.json for {len(remaining)} words.")
