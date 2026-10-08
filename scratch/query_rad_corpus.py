# -*- coding: utf-8 -*-
"""
query_rad_corpus.py
Queries citation_corpus.db for all 102 words in Dashboard — rad
"""
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    'abradant', 'abrade', 'abrader', 'comrade', 'comradeliness', 'comradely', 'comradery', 'comradeship', 'conrad', 'conradina', 'corrade', 'eradicable', 'eradicate', 'eradication', 'eradicator', 'ineradicable', 'irradiate', 'irradiation', 'nonradioactive', 'rad', 'radar', 'radial', 'radial-ply', 'radially', 'radian', 'radiance', 'radiancy', 'radiant', 'radiantly', 'radiate', 'radiating', 'radiation', 'radiator', 'radical', 'radicalism', 'radicalize', 'radically', 'radicchio', 'radicle', 'radiculitis', 'radiigera', 'radio', 'radio-controlled', 'radio-gramophone', 'radio-opacity', 'radio-opaque', 'radio-phonograph', 'radioactive', 'radioactively', 'radioactivity', 'radiobiologist', 'radiobiology', 'radiocarbon', 'radiochemist', 'radiochemistry', 'radiochlorine', 'radiocommunication', 'radiogram', 'radiograph', 'radiographer', 'radiographic', 'radiography', 'radioimmunoassay', 'radioisotope', 'radiolaria', 'radiolarian', 'radiolocate', 'radiolocation', 'radiological', 'radiologist', 'radiology', 'radiolucent', 'radiolysis', 'radiometer', 'radiomicrometer', 'radiopacity', 'radiopaque', 'radiopharmaceutical', 'radiophone', 'radiophonic', 'radiophoto', 'radiophotograph', 'radiophotography', 'radioprotection', 'radioscopy', 'radiosensitive', 'radiosensitivity', 'radiotelegraph', 'radiotelegraphy', 'radiotelephone', 'radiotelephonic', 'radiotelephony', 'radiotherapist', 'radiotherapy', 'radiothorium', 'radish', 'radium', 'radius', 'radix', 'radome', 'radon', 'radyera'
]

results = {}
high_count = 0

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
    if len(dedup) >= 3:
        high_count += 1

conn.close()

with open("scratch/rad_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Total words: {len(words)}")
print(f"Words with >= 3 distinct authors in corpus: {high_count}")
for w in words:
    print(f"  {w:22}: {len(results[w])}")
