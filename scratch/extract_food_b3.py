import sqlite3
import json
import os

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

pom_words = [
    'pom', 'pomacanthus', 'pomace', 'pomacentridae', 'pomacentrus', 'pomade', 'pomaded',
    'pomaderris', 'pomatomidae', 'pomatomus', 'pomatum', 'pome', 'pomegranate', 'pomelo',
    'pomeranian', 'pommel', 'pommy', 'pomo', 'pomolobus', 'pomologist', 'pomology',
    'pomona', 'pomoxis', 'pomp', 'pompadour', 'pomposity', 'pompous', 'pompously',
    'pompousness', 'unpompous'
]

sati_words = [
    'alsatia', 'alsatian', 'dissatisfaction', 'dissatisfactory', 'dissatisfied', 'dissatisfy',
    'insatiable', 'insatiably', 'insatiate', 'satiable', 'satiate', 'satiated', 'satiation',
    'satie', 'satiety', 'satin', 'satinet', 'satinette', 'satinleaf', 'satinpod',
    'satinwood', 'satiny', 'satire', 'satiric', 'satirical', 'satirically', 'satirise',
    'satirist', 'satirize', 'satisfaction', 'satisfactorily', 'satisfactoriness', 'satisfactory',
    'satisfiable', 'satisfice', 'satisfied', 'satisfier', 'satisfise', 'satisfy',
    'satisfying', 'satisfyingly', 'unsatiable', 'unsatiably', 'unsatiated', 'unsatisfactorily',
    'unsatisfactoriness', 'unsatisfactory', 'unsatisfiable', 'unsatisfied', 'unsatisfying'
]

all_words = pom_words + sati_words

corpus_results = {}
for w in all_words:
    # search for exact word or inflections in citation corpus
    c_cur.execute("""
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 100
    """, (f'"{w}"',))
    rows = c_cur.fetchall()
    
    # Also get dictionary definitions
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ?", (w,))
    d_rows = [r[0] for r in d_cur.fetchall()]
    
    auth_dict = {}
    for author, work, sentence in rows:
        if author not in auth_dict and 25 < len(sentence) < 450:
            auth_dict[author] = {"work": work, "sentence": sentence}
            
    corpus_results[w] = {
        "dict_defs": d_rows,
        "authors_count": len(auth_dict),
        "quotes": auth_dict
    }

os.makedirs("scratch", exist_ok=True)
with open("scratch/food_b3_corpus_dump.json", "w", encoding="utf-8") as f:
    json.dump(corpus_results, f, ensure_ascii=False, indent=2)

print("Dumped corpus results for 80 words.")
