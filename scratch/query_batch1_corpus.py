import sqlite3
import os
import re
import json

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    # corn (13)
    'bicorn', 'bicornate', 'bicorned', 'corn', 'corneal', 'corned', 'corneous', 'cornerstone', 'cornet', 'cornetist', 'cornucopia', 'corny', 'unicorn',
    # herb (12)
    'herb', 'herbaceous', 'herbage', 'herbal', 'herbalist', 'herbarium', 'herbart', 'herbert', 'herbicide', 'herbivore', 'herbivorous', 'herborize',
    # porc (9)
    'porc', 'porcelain', 'porcelainize', 'porcellio', 'porcellionidae', 'porcine', 'porcupine', 'porcupinefish', 'porcupines',
    # taur (6)
    'tauriform', 'taurine', 'taurobolium', 'tauromachy', 'taurotragus', 'taurus',
    # vulp (5)
    'vulpecula', 'vulpecular', 'vulpes', 'vulpicide', 'vulpine',
    # zo (5)
    'azoic', 'epizootic', 'protozoa', 'zodiac', 'zodiacal',
    # pisc (15)
    'episcia', 'episcleritis', 'episcopacy', 'episcopal', 'episcopalian', 'episcopalianism', 'episcopate', 'piscary', 'piscatorial', 'piscatory', 'pisces', 'pisciculture', 'piscidia', 'piscine', 'piscivorous',
    # ov (17)
    'anovulation', 'obovate', 'ov', 'oval', 'ovalbumin', 'ovarian', 'ovary', 'ovate', 'oviparous', 'ovipositor', 'ovoid', 'ovoviviparous', 'ovular', 'ovulate', 'ovulation', 'ovule', 'ovum',
    # capr (25)
    'capra', 'caprella', 'capreolus', 'capri', 'capriccio', 'caprice', 'capricious', 'capriciously', 'capriciousness', 'capricorn', 'capricornis', 'capricornus', 'caprid', 'caprifig', 'caprifoliaceae', 'caprimulgid', 'caprimulgidae', 'caprimulgiformes', 'caprimulgus', 'caprine', 'capriole', 'caproic', 'caproidae', 'capromyidae', 'capros'
]

hits = {}
for w in words:
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 10
    """, (f'"{w}"',))
    rows = cur.fetchall()
    if rows:
        hits[w] = [{"author": r[0], "work": r[1], "sentence": r[2]} for r in rows]

print(f"Total words: {len(words)}, Words with hits in corpus: {len(hits)}")
with open(r"scratch/batch1_corpus_hits.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
