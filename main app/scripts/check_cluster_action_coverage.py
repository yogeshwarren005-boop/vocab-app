# -*- coding: utf-8 -*-
import os, glob, re, sqlite3

db_path = os.path.join('main app', 'corpus', 'citation_corpus.db')
con = sqlite3.connect(db_path)
cur = con.cursor()

base = 'App database/Latin roots/Cluster Action'
files = glob.glob(f'{base}/*/*.md')
words = [os.path.splitext(os.path.basename(f))[0] for f in files if not os.path.basename(f).startswith('Dashboard') and not os.path.basename(f).startswith('Word Triage')]

matched_3 = 0
matched_1_2 = 0
matched_0 = 0

for w in words:
    q_word = re.sub(r'[^a-zA-Z0-9]', '', w)
    if not q_word:
        matched_0 += 1
        continue
    try:
        rows = cur.execute('SELECT s.author, s.work, s.sentence FROM sentences_fts f JOIN sentences s ON f.rowid = s.id WHERE sentences_fts MATCH ? LIMIT 20;', (f'"{q_word}"',)).fetchall()
        pat = re.compile(rf'\b{re.escape(w)}\b', re.IGNORECASE)
        authors = set()
        for r in rows:
            if pat.search(r[2]):
                authors.add(r[0])
        if len(authors) >= 3:
            matched_3 += 1
        elif len(authors) >= 1:
            matched_1_2 += 1
        else:
            matched_0 += 1
    except:
        matched_0 += 1

print(f"Total words in Cluster Action: {len(words)}")
print(f"Words with >= 3 distinct author matches: {matched_3} ({matched_3/len(words)*100:.1f}%)")
print(f"Words with 1-2 author matches: {matched_1_2} ({matched_1_2/len(words)*100:.1f}%)")
print(f"Words with 0 matches: {matched_0} ({matched_0/len(words)*100:.1f}%)")

con.close()
