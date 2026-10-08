# -*- coding: utf-8 -*-
"""
query_botany_b3_corpus.py
Queries citation_corpus.db for all 135 words in Cluster Botany Batch 3:
- Dashboard — aurum (31)
- Dashboard — calc (51)
- Dashboard — carb (53)
"""
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    # aurum (31)
    'aura', 'aural', 'aurally', 'aureate', 'aurelius', 'aureolaria', 'aureole', 'aureomycin', 'auric', 'auricle', 'auricula', 'auricular', 'auriculare', 'auricularia', 'auriculariaceae', 'auriculariales', 'auriculate', 'auriculated', 'auriculoventricular', 'auriferous', 'auriform', 'aurify', 'auriga', 'auriparus', 'auriscope', 'aurochs', 'aurora', 'auroral', 'aurorean', 'auroscope', 'aurous',
    # calc (51)
    'calcaneal', 'calcaneus', 'calcareous', 'calced', 'calcedony', 'calceiform', 'calceolaria', 'calceolate', 'calceus', 'calcic', 'calcicolous', 'calciferol', 'calciferous', 'calcific', 'calcification', 'calcifugous', 'calcify', 'calcimine', 'calcination', 'calcine', 'calcite', 'calcitic', 'calcitonin', 'calcium', 'calcium-cyanamide', 'calculable', 'calculate', 'calculated', 'calculating', 'calculatingly', 'calculation', 'calculative', 'calculator', 'calculous', 'calculus', 'calcutta', 'calcuttan', 'decalcification', 'decalcify', 'decalcomania', 'discalceate', 'discalced', 'incalculable', 'miscalculate', 'miscalculation', 'recalcitrance', 'recalcitrancy', 'recalcitrant', 'recalcitrate', 'recalculate', 'recalculation',
    # carb (53)
    'carbamate', 'carbamide', 'carbide', 'carbine', 'carbineer', 'carbocyclic', 'carbohydrate', 'carbolated', 'carboloy', 'carbomycin', 'carbon', 'carbonaceous', 'carbonado', 'carbonara', 'carbonate', 'carbonated', 'carbonation', 'carbondale', 'carbonic', 'carboniferous', 'carbonisation', 'carbonise', 'carbonization', 'carbonize', 'carbonous', 'carbonyl', 'carbonylic', 'carborundum', 'carboxyl', 'carboxylate', 'carboxylic', 'carboy', 'carbuncle', 'carbuncled', 'carbuncular', 'carburet', 'carburetor', 'carburettor', 'carburise', 'carburize', 'cocarboxylase', 'decarbonate', 'decarbonise', 'decarbonize', 'decarboxylase', 'decarboxylate', 'decarboxylation', 'decarburise', 'decarburize', 'dicarboxylic', 'noncarbonated', 'procarbazine', 'uncarbonated'
]

results = {}
low_words = []

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
    if len(dedup) < 3:
        low_words.append((w, len(dedup)))

conn.close()

with open("scratch/botany_b3_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"Total words queried: {len(words)}")
print(f"Words with >= 3 distinct authors: {len(words) - len(low_words)}")
print(f"Words with < 3 distinct authors: {len(low_words)}")
print("\nLow author count words:")
for w, cnt in low_words:
    print(f"  {w:25}: {cnt} hits")
