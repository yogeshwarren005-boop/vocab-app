import sqlite3
import json

words = ['adjoin', 'conjoin', 'conjoined', 'conjoint', 'conjointly', 'disjoin', 'disjoined', 'disjoint', 'disjointed', 'disjointedly', 'disjointedness', 'enjoin', 'enjoining', 'enjoinment', 'join', 'joined', 'joiner', 'joinery', 'joining', 'joint', 'jointed', 'jointer', 'jointly', 'jointure', 'jointworm', 'rejoin', 'rejoinder', 'subjoin', 'subjoining', 'surrejoinder', 'unjointed',
'connect', 'connected', 'connectedness', 'connecter', 'connecticut', 'connecticuter', 'connection', 'connective', 'connectivity', 'connector', 'disconnect', 'disconnected', 'disconnectedness', 'disconnection', 'interconnect', 'interconnected', 'interconnectedness', 'interconnection', 'nectar', 'nectar-rich', 'nectariferous', 'nectarine', 'nectarous', 'nectary', 'necturus', 'unconnected', 'unconnectedness']

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c = conn.cursor()

corpus_results = {}
for w in words:
    clean_w = w.replace('-', ' ')
    try:
        c.execute('''
            SELECT author, work, sentence FROM sentences 
            WHERE id IN (SELECT rowid FROM sentences_fts WHERE sentences_fts MATCH ?)
        ''', (f'"{clean_w}"',))
        rows = c.fetchall()
        by_author = {}
        for auth, wrk, sent in rows:
            if auth not in by_author and 30 < len(sent) < 350:
                by_author[auth] = {"work": wrk, "sentence": sent}
        corpus_results[w] = by_author
    except Exception as e:
        corpus_results[w] = {}

print("Words with 3+ distinct authors in corpus:")
for w, d in corpus_results.items():
    if len(d) >= 3:
        print(f"  {w}: {len(d)} authors")

print("\nWords with < 3 distinct authors in corpus:")
for w, d in corpus_results.items():
    if len(d) < 3:
        print(f"  {w}: {len(d)} authors")

with open("scratch/corpus_hits_binding.json", "w", encoding="utf-8") as f:
    json.dump(corpus_results, f, indent=2, ensure_ascii=False)
