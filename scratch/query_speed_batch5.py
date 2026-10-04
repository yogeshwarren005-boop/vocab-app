import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words_curs = ['accurse', 'accursed', 'accurst', 'curse', 'cursed', 'cursedly', 'cursive', 'cursively', 'cursor', 'cursorial', 'cursorily', 'cursorius', 'cursory', 'curst', 'discursive', 'discursively', 'discursiveness', 'excursion', 'excursionist', 'excursive', 'excursus', 'incursion', 'incursive', 'precursor', 'precursory', 'recursion', 'recursive']
words_curr = ['concurrence', 'concurrency', 'concurrent', 'concurrently', 'concurring', 'countercurrent', 'currajong', 'currant', 'currawong', 'currency', 'current', 'currently', 'currentness', 'curricular', 'curriculum', 'currier', 'currish', 'currishly', 'curry', 'currycomb', 'extracurricular', 'incurrence', 'incurring', 'noncurrent', 'nonoccurrence', 'occurrence', 'occurrent', 'recurrence', 'recurrent', 'recurrently', 'recurring', 'undercurrent']

all_words = words_curs + words_curr

dict_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
dict_cur = dict_conn.cursor()

corpus_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
corpus_cur = corpus_conn.cursor()

results = {}
for w in all_words:
    dict_cur.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    defs = dict_cur.fetchall()
    
    # search quotes via sentences_fts
    search_term = w.replace("-", " ")
    try:
        corpus_cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE f.sentence MATCH ? LIMIT 15
        """, (f'"{search_term}"',))
        quotes = corpus_cur.fetchall()
    except Exception as e:
        quotes = []
    
    results[w] = {
        "defs": [{"source": d[0], "def": d[1]} for d in defs],
        "quotes": [{"author": q[0], "work": q[1], "sentence": q[2]} for q in quotes]
    }

print("Queried", len(results), "words.")
with open("scratch/speed_batch5_raw.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved to scratch/speed_batch5_raw.json")
