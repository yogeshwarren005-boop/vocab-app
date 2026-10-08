import sqlite3
import os
import json

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    # anim (51)
    'anima', 'animadversion', 'animadvert', 'animal', 'animal-worship', 'animalcule', 'animalculum', 'animalia', 'animalisation', 'animalise', 'animalism', 'animalistic', 'animality', 'animalization', 'animalize', 'animate', 'animated', 'animatedly', 'animateness', 'animating', 'animation', 'animatism', 'animatistic', 'animator', 'animatronics', 'anime', 'animise', 'animism', 'animist', 'animistic', 'animize', 'animosity', 'animus', 'equanimity', 'equanimous', 'exanimate', 'inanimate', 'inanimateness', 'longanimity', 'longanimous', 'pusillanimity', 'pusillanimous', 'pusillanimously', 'pusillanimousness', 'reanimate', 'reanimated', 'reanimation', 'unanimated', 'unanimity', 'unanimous', 'unanimously',
    # avi (25)
    'atavism', 'atavist', 'atavistic', 'avian', 'avianise', 'avianize', 'aviary', 'aviate', 'aviation', 'aviator', 'aviatress', 'aviatrix', 'avicenna', 'avicennia', 'avicenniaceae', 'aviculture', 'avifauna', 'avifaunal', 'avifaunistic', 'avine', 'avionic', 'avionics', 'avirulent', 'avitaminosis', 'avitaminotic',
    # simi (23)
    'assimilable', 'assimilate', 'assimilating', 'assimilation', 'assimilative', 'assimilator', 'assimilatory', 'dissimilar', 'dissimilarity', 'dissimilate', 'dissimilation', 'dissimilitude', 'prosimian', 'prosimii', 'simian', 'simiid', 'simiiform', 'similar', 'similarity', 'similarly', 'simile', 'similitude', 'unsimilarity',
    # mur_mouse (32)
    'demur', 'demure', 'demurely', 'demureness', 'demurrage', 'demurral', 'demurrer', 'extramural', 'immure', 'immurement', 'intermural', 'intramural', 'muraenidae', 'mural', 'muralist', 'muramidase', 'muridae', 'murillo', 'murine', 'muritaniya', 'murmansk', 'murmur', 'murmuration', 'murmurer', 'murmuring', 'murmurous', 'muroidea', 'murrain', 'murray', 'murre', 'murrow', 'murrumbidgee'
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
with open(r"scratch/batch3_corpus_hits.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
