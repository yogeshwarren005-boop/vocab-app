import sqlite3

c_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c_cur = c_conn.cursor()

d_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
d_cur = d_conn.cursor()

pom_words = ['pom', 'pomacanthus', 'pomace', 'pomacentridae', 'pomacentrus', 'pomade', 'pomaded', 'pomaderris', 'pomatomidae', 'pomatomus', 'pomatum', 'pome', 'pomegranate', 'pomelo', 'pomeranian', 'pommel', 'pommy', 'pomo', 'pomolobus', 'pomologist', 'pomology', 'pomona', 'pomoxis', 'pomp', 'pompadour', 'pomposity', 'pompous', 'pompously', 'pompousness', 'unpompous']

sati_words = ['alsatia', 'alsatian', 'dissatisfaction', 'dissatisfactory', 'dissatisfied', 'dissatisfy', 'insatiable', 'insatiably', 'insatiate', 'satiable', 'satiate', 'satiated', 'satiation', 'satie', 'satiety', 'satin', 'satinet', 'satinette', 'satinleaf', 'satinpod', 'satinwood', 'satiny', 'satire', 'satiric', 'satirical', 'satirically', 'satirise', 'satirist', 'satirize', 'satisfaction', 'satisfactorily', 'satisfactoriness', 'satisfactory', 'satisfiable', 'satisfice', 'satisfied', 'satisfier', 'satisfise', 'satisfy', 'satisfying', 'satisfyingly', 'unsatiable', 'unsatiably', 'unsatiated', 'unsatisfactorily', 'unsatisfactoriness', 'unsatisfactory', 'unsatisfiable', 'unsatisfied', 'unsatisfying']

all_words = pom_words + sati_words
print(f"Total words: {len(all_words)}")

missing_in_db = []
available_in_db = {}

for w in all_words:
    c_cur.execute("""
        SELECT s.author, s.work, s.sentence
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 50
    """, (f'"{w}"',))
    rows = c_cur.fetchall()
    by_author = {}
    for author, work, sentence in rows:
        if author not in by_author and len(sentence) > 30 and len(sentence) < 400:
            by_author[author] = (work, sentence)
    if len(by_author) < 3:
        missing_in_db.append((w, len(by_author)))
    else:
        available_in_db[w] = by_author

print(f"Words with < 3 distinct authors: {len(missing_in_db)}")
print("Missing:", missing_in_db)
