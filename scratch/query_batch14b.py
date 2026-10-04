import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words_b = [
    'provencal', 'provence', 'provenience', 'reconvene', 'reinvention', 
    'revenant', 'revenue', 'revenuer', 'seven', 'sevener', 
    'sevens', 'sevensome', 'seventh', 'seventhly', 'souvenir', 
    'supervene', 'uneven', 'unevenly', 'unevenness', 'uneventful', 
    'uneventfully', 'unproven', 'vena', 'venal', 'venality', 
    'venally', 'venation', 'veneer', 'veneering', 'venerability', 
    'venerable', 'venerableness', 'venerate', 'venerating', 'veneration'
]

dict_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
dict_cur = dict_conn.cursor()

corpus_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
corpus_cur = corpus_conn.cursor()

results = {}
for w in words_b:
    dict_cur.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    defs = dict_cur.fetchall()
    
    # search quotes via sentences_fts
    try:
        corpus_cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE f.sentence MATCH ? LIMIT 15
        """, (f'"{w}"',))
        quotes = corpus_cur.fetchall()
    except Exception as e:
        quotes = []
    
    results[w] = {
        "defs": [{"source": d[0], "def": d[1]} for d in defs],
        "quotes": [{"author": q[0], "work": q[1], "sentence": q[2]} for q in quotes]
    }

print("Queried", len(results), "words.")
with open("scratch/batch14b_raw.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved to scratch/batch14b_raw.json")
