import sqlite3
import os
import json

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = [
    'anticancer', 'arcane', 'arcanum', 'can', 'canaan', 'canaanite', 'canaanitic', 'canachites', 'canada', 'canadian', 'canafistola', 'canafistula', 'canal', 'canalicular', 'canaliculate', 'canaliculus', 'canalisation', 'canalise', 'canalization', 'canalize',
    'cananga', 'canangium', 'canape', 'canara', 'canard', 'canarese', 'canaries', 'canary', 'canary-yellow', 'canasta', 'canavalia', 'canavanine', 'cancan', 'cancel', 'cancellate', 'cancellated', 'cancellation', 'cancelled', 'cancellous', 'cancer',
    'cancerous', 'cancerweed', 'cancridae', 'cancroid', 'cancun', 'cane', 'canebrake', 'canecutter', 'canella', 'canella-alba', 'canellaceae', 'canescent', 'canetti', 'canicula', 'canicular', 'canicule', 'canid', 'canidae', 'canine', 'caning',
    'canis', 'canistel', 'canister', 'canna', 'cannabidaceae', 'cannabin', 'cannabis', 'cannaceae', 'cannae', 'canned', 'cannelloni', 'cannery', 'cannes', 'cannibal', 'cannibalic', 'cannibalise', 'cannibalism', 'cannibalistic', 'cannibalize', 'cannikin',
    'cannily', 'cannister', 'cannon', 'cannonade', 'cannonball', 'cannoneer', 'cannula', 'cannular', 'cannulate', 'cannulation', 'cannulisation', 'cannulise', 'cannulization', 'cannulize', 'canny', 'canoe', 'canoeist', 'canola', 'canon', 'canonic',
    'canonical', 'canonically', 'canonisation', 'canonise', 'canonised', 'canonist', 'canonization', 'canonize', 'canonized', 'canoodle', 'canopied', 'canopus', 'canopy', 'canorous', 'cant', 'cantabile', 'cantabrigian', 'cantala', 'cantaloup', 'cantaloupe',
    'cantankerous', 'cantankerously', 'cantata', 'canted', 'canteen', 'canter', 'canterbury', 'cantering', 'cantharellus', 'canthus', 'canticle', 'canticles', 'cantilever', 'cantillate', 'cantillation', 'cantle', 'canto', 'canton', 'cantonal', 'cantonese',
    'cantonment', 'cantor', 'canty', 'canuck', 'canulate', 'canulation', 'canulisation', 'canulization', 'canute', 'canyon', 'canyonside', 'cosecant', 'decant', 'decantation', 'decanter', 'discant', 'incan', 'incantation', 'precancerous', 'recant',
    'recantation', 'secant', 'uncannily', 'uncanny'
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
with open(r"scratch/can_dog_corpus_hits.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
