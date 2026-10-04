# -*- coding: utf-8 -*-
import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words = ['bona fide', 'bonaire', 'bonanza', 'bonaparte', 'bonasa', 'bonavist', 'bonce', 'bone', 'bone-covered', 'bone-dry', 'bone-idle', 'bone-lazy', 'boned', 'bonefish', 'bonehead', 'boneheaded', 'boneless', 'bonelet', 'bonelike', 'bonemeal', 'boner', 'bones', 'boneset', 'bonesetter', 'boneshaker', 'bonete', 'boney', 'bonhomie', 'boniface', 'boniness', 'bonito', 'bonn', 'bonnet', 'bonnethead', 'bonney', 'bonnie', 'bonnily', 'bonny', 'bonobo', 'bonsai', 'bontemps', 'bonus', 'bony', 'bony-plated', 'bonyness', 'debonair', 'debonaire', 'debone', 'deboned', 'debonnaire', 'ebon', 'ebonics', 'ebonise', 'ebonite', 'ebonize', 'ebony', 'redbone']

cite_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cite_cur = cite_conn.cursor()
dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()

results = {}
for w in words:
    dict_cur.execute('SELECT definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number', (w,))
    defs = [r[0] for r in dict_cur.fetchall()]
    
    # Query citations
    cites = []
    # Try exact match or query terms
    q_term = f'"{w}"' if ' ' not in w and '-' not in w else f'"{w}"'
    try:
        cite_cur.execute('SELECT author, work, sentence FROM sentences_fts WHERE sentence MATCH ? LIMIT 15', (q_term,))
        cites = cite_cur.fetchall()
    except Exception as e:
        # maybe hyphen or special characters
        try:
            clean = w.replace('-', ' ')
            cite_cur.execute('SELECT author, work, sentence FROM sentences_fts WHERE sentence MATCH ? LIMIT 15', (f'"{clean}"',))
            cites = cite_cur.fetchall()
        except Exception:
            pass

    results[w] = {
        'defs': defs,
        'cites': cites
    }

print(f"Polled {len(words)} words.")
for w, data in results.items():
    authors = set(c[0] for c in data['cites'])
    print(f"{w:15} | defs: {len(data['defs']):2} | cites: {len(data['cites']):2} | distinct authors: {len(authors):2}")

with open('scratch/bon_poll.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
