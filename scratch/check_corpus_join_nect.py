import sqlite3
import re

words_join = ['adjoin', 'conjoin', 'conjoined', 'conjoint', 'conjointly', 'disjoin', 'disjoined', 'disjoint', 'disjointed', 'disjointedly', 'disjointedness', 'enjoin', 'enjoining', 'enjoinment', 'join', 'joined', 'joiner', 'joinery', 'joining', 'joint', 'jointed', 'jointer', 'jointly', 'jointure', 'jointworm', 'rejoin', 'rejoinder', 'subjoin', 'subjoining', 'surrejoinder', 'unjointed']
words_nect = ['connect', 'connected', 'connectedness', 'connecter', 'connecticut', 'connecticuter', 'connection', 'connective', 'connectivity', 'connector', 'disconnect', 'disconnected', 'disconnectedness', 'disconnection', 'interconnect', 'interconnected', 'interconnectedness', 'interconnection', 'nectar', 'nectar-rich', 'nectariferous', 'nectarine', 'nectarous', 'nectary', 'necturus', 'unconnected', 'unconnectedness']

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c = conn.cursor()

all_words = words_join + words_nect

for w in all_words:
    clean_w = w.replace('-', ' ')
    try:
        c.execute("SELECT count(DISTINCT author) FROM sentences WHERE id IN (SELECT rowid FROM sentences_fts WHERE sentences_fts MATCH ?)", (f'"{clean_w}"',))
        auth_cnt = c.fetchone()[0]
    except Exception as e:
        auth_cnt = 0
    print(f"{w}: {auth_cnt} distinct authors")

conn.close()
