# -*- coding: utf-8 -*-
import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words = ['bona fide', 'bonaire', 'bonanza', 'bonaparte', 'bonasa', 'bonavist', 'bonce', 'bone', 'bone-covered', 'bone-dry', 'bone-idle', 'bone-lazy', 'boned', 'bonefish', 'bonehead', 'boneheaded', 'boneless', 'bonelet', 'bonelike', 'bonemeal', 'boner', 'bones', 'boneset', 'bonesetter', 'boneshaker', 'bonete', 'boney', 'bonhomie', 'boniface', 'boniness', 'bonito', 'bonn', 'bonnet', 'bonnethead', 'bonney', 'bonnie', 'bonnily', 'bonny', 'bonobo', 'bonsai', 'bontemps', 'bonus', 'bony', 'bony-plated', 'bonyness', 'debonair', 'debonaire', 'debone', 'deboned', 'debonnaire', 'ebon', 'ebonics', 'ebonise', 'ebonite', 'ebonize', 'ebony', 'redbone']

cite_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cite_cur = cite_conn.cursor()

found = {}
for w in words:
    q = w.replace('-', ' ')
    try:
        cite_cur.execute('''
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE sentences_fts MATCH ? 
            LIMIT 15
        ''', (f'"{q}"',))
        rows = cite_cur.fetchall()
        if rows:
            found[w] = rows
    except Exception as e:
        pass

print(f"Found matches for {len(found)} / {len(words)} words:")
for w in sorted(found.keys()):
    authors = list(set(r[0] for r in found[w]))
    print(f"  {w:15}: {len(found[w])} rows, {len(authors)} authors: {authors[:4]}")

with open('scratch/bon_corpus_matches.json', 'w', encoding='utf-8') as f:
    json.dump(found, f, indent=2, ensure_ascii=False)
