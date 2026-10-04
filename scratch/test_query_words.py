# -*- coding: utf-8 -*-
import sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")

words_8e = ['underwear', 'underweight', 'underwing', 'underwood', 'underworld', 'underwrite', 'underwriter', 'undescended', 'undescriptive', 'undeserved', 'undeservedly', 'undeserving', 'undesigned', 'undesirability', 'undesirable', 'undesirably', 'undesired', 'undesiring', 'undesirous', 'undestroyable', 'undetectable', 'undetected', 'undeterminable', 'undetermined', 'undeterred', 'undeveloped', 'undeviating', 'undiagnosable', 'undiagnosed', 'undies', 'undifferentiated', 'undigested', 'undignified', 'undiluted', 'undiminished', 'undimmed', 'undine', 'undiplomatic', 'undiplomatically', 'undirected', 'undiscerning', 'undischarged', 'undiscipline', 'undisciplined', 'undisclosed', 'undiscouraged', 'undiscoverable', 'undiscovered', 'undiscriminating', 'undisguised', 'undismayed', 'undisputable']

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_c = dict_conn.cursor()

cite_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cite_c = cite_conn.cursor()

print("--- Checking definitions and citations ---")
for w in words_8e[:10]:
    dict_c.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    defs = dict_c.fetchall()
    
    cite_c.execute("SELECT sentences.author, sentences.work, sentences.sentence FROM sentences JOIN sentences_fts ON sentences.id = sentences_fts.rowid WHERE sentences_fts MATCH ? LIMIT 5", (f'"{w}"',))
    cites = cite_c.fetchall()
    
    print(f"Word: {w}")
    print(f"  Defs count: {len(defs)}")
    for d in defs[:2]:
        print(f"    [{d[0]}] {d[1][:80]}...")
    print(f"  Cites count: {len(cites)}")
    for c in cites[:2]:
        print(f"    ({c[0]}, {c[1]}): {c[2][:80]}...")
