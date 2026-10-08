# -*- coding: utf-8 -*-
"""
query_botany_b2_corpus.py
Queries citation_corpus.db for all 131 words in Cluster Botany Batch 2
"""
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    # nuc (21)
    'cornucopia', 'enucleate', 'enucleation', 'nucellus', 'nucifraga', 'nuclear', 'nuclease', 'nucleate', 'nucleated', 'nucleic', 'nucleole', 'nucleolus', 'nucleon', 'nucleonics', 'nucleoplasm', 'nucleoprotein', 'nucleoside', 'nucleosynthesis', 'nucleotide', 'nucleus', 'pronucleus',
    # foli (23)
    'bifolium', 'defoliant', 'defoliate', 'defoliated', 'defoliation', 'defoliator', 'exfoliant', 'exfoliate', 'exfoliation', 'foliaceous', 'foliage', 'foliaged', 'foliar', 'foliate', 'foliated', 'foliation', 'folie', 'folio', 'foliolate', 'foliose', 'folium', 'interfoliate', 'perfoliate',
    # flor (28)
    'defloration', 'effloresce', 'efflorescence', 'efflorescent', 'flora', 'floral', 'floreal', 'florence', 'florentine', 'florescence', 'florescent', 'floret', 'florey', 'floricultural', 'floriculture', 'florid', 'florida', 'floridian', 'floridity', 'floridly', 'floridness', 'floriferous', 'florilegium', 'florin', 'florio', 'florist', 'flory', 'inflorescence',
    # petr (29)
    'empetraceae', 'empetrum', 'perpetrate', 'perpetration', 'perpetrator', 'petrarca', 'petrarch', 'petrel', 'petrifaction', 'petrification', 'petrify', 'petrifying', 'petrissage', 'petrochemical', 'petrocoptis', 'petrogale', 'petroglyph', 'petrograd', 'petrography', 'petrol', 'petrolatum', 'petroleum', 'petrology', 'petromyzon', 'petromyzoniformes', 'petromyzontidae', 'petronius', 'petroselinum', 'petrous',
    # ole (30)
    'adolesce', 'adolescence', 'adolescent', 'anole', 'apolemia', 'atole', 'cooler', 'linoleum', 'olea', 'oleaceae', 'oleaceous', 'oleaginous', 'oleaginousness', 'oleales', 'oleander', 'oleandra', 'oleandraceae', 'olearia', 'oleaster', 'olecranon', 'oleic', 'olein', 'oleo', 'oleomargarine', 'oleophilic', 'oleophobic', 'oleoresin', 'preadolescent', 'redolence', 'redolent'
]

results = {}

for w in words:
    clean_w = w.replace('-', ' ')
    query = f'"{clean_w}"'
    try:
        cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 300
        """, (query,))
        rows = cur.fetchall()
    except Exception as e:
        rows = []

    seen = set()
    dedup = []
    pattern = re.compile(rf'\b{re.escape(w)}\b', re.IGNORECASE)
    for a, wrk, st in rows:
        if a not in seen:
            seen.add(a)
            m = pattern.search(st)
            if m:
                start, end = m.span()
                bolded = st[:start] + f"**{st[start:end]}**" + st[end:]
            else:
                bolded = st
            dedup.append({"author": a, "work": wrk, "sentence": bolded})
    results[w] = dedup
    status = "OK (>=3)" if len(dedup) >= 3 else f"LOW ({len(dedup)})"
    print(f"{w:20}: {len(dedup):3} distinct authors -> {status}")

conn.close()

with open("scratch/botany_b2_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSaved scratch/botany_b2_rich_corpus.json successfully.")
