# -*- coding: utf-8 -*-
import sqlite3
import json

words = [
    'lactobacillaceae', 'lactobacillus', 'lactobacteriaceae', 'lactoflavin', 'lactogen', 'lactogenic', 'lactophrys', 'lactoprotein', 'lactose', 'lactosuria', 'lactuca', 'prolactin',
    'mellaril', 'melliferous', 'mellification', 'mellifluent', 'mellifluous', 'mellisonant', 'mellisugent', 'mellivora', 'mellon', 'mellow', 'mellowed', 'mellowing', 'mellowingly', 'mellowly', 'mellowness',
    'companion', 'companionship', 'empanada', 'pan', 'panic', 'panification', 'panivorous', 'pannier', 'pantry',
    'potable', 'potage', 'potash', 'potassium', 'potation', 'potato'
]

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()
found = {}
for w in words:
    clean = w.replace('-', ' ')
    try:
        cur.execute('SELECT distinct s.author, s.work, s.sentence FROM sentences s JOIN sentences_fts f ON s.id = f.rowid WHERE f.sentence MATCH ? LIMIT 8', (f'"{clean}"',))
        rows = cur.fetchall()
        if rows:
            found[w] = [{'author': r[0], 'work': r[1], 'sentence': r[2]} for r in rows]
    except Exception as e:
        pass

print(f"Words with corpus hits: {len(found)} / {len(words)}")
for w in sorted(found.keys()):
    print(f"  {w}: {len(found[w])} hits")

with open('scratch/food_b1_p3_hits.json', 'w', encoding='utf-8') as f:
    json.dump(found, f, indent=2, ensure_ascii=False)
