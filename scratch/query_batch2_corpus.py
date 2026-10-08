import sqlite3
import os
import json

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    # ap (37)
    'agape', 'ape', 'aper', 'aperitif', 'aperture', 'apery', 'apiarian', 'apiary', 'appetizer', 'appetizing', 'appetizingness', 'applaud', 'applaudable', 'applauder', 'applause', 'appraisal', 'appraise', 'appraiser', 'appraising', 'appreciate', 'appreciated', 'appreciation', 'appreciative', 'appreciatively', 'appreciativeness', 'appreciator', 'diaper', 'overappraisal', 'reap', 'reaper', 'reappraisal', 'reappraise', 'unappetizing', 'unappetizingness', 'unappreciated', 'unappreciative', 'unappreciatively',
    # greg (32)
    'aggregate', 'aggregated', 'aggregation', 'aggregative', 'aggregator', 'congregant', 'congregate', 'congregating', 'congregation', 'congregational', 'congregationalism', 'congregationalist', 'desegregate', 'desegregation', 'egregious', 'gregarine', 'gregarinida', 'gregarious', 'gregariously', 'gregariousness', 'gregorian', 'gregory', 'nongregarious', 'nonsegregated', 'segregate', 'segregated', 'segregation', 'segregationism', 'segregationist', 'segregator', 'ungregarious', 'unsegregated',
    # ran (43)
    'abranchial', 'abranchiate', 'abranchious', 'agranulocytic', 'agranulocytosis', 'agranulosis', 'arrant', 'crane', 'eranthis', 'rana', 'ranales', 'ranatra', 'ranch', 'rancher', 'ranching', 'rancid', 'rancidity', 'rancidness', 'rancor', 'rancorous', 'rancour', 'ranee', 'rani', 'ranid', 'ranidae', 'ranier', 'ranine', 'ranitidine', 'ranivorous', 'ransack', 'ransacked', 'ransacking', 'ransom', 'ransomed', 'rant', 'ranter', 'ranting', 'ranula', 'ranunculaceae', 'ranunculales', 'ranunculus', 'supranational', 'supranormal'
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
with open(r"scratch/batch2_corpus_hits.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
