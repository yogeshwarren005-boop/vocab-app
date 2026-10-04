import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words_sal = [
    'desalinate', 'desalination', 'desalinisation', 'desalinise', 'desalinization', 'desalinize', 'desalt',
    'disallow', 'insalubrious', 'insalubriousness', 'insalubrity', 'resale', 'salaah', 'salaam', 'salaat',
    'salability', 'salable', 'salableness', 'salacious', 'salaciously', 'salaciousness', 'salacity', 'salad',
    'salade', 'saladin', 'salafism', 'salah', 'salai', 'salal', 'salamander', 'salamandra', 'salamandridae',
    'salamandriform', 'salami', 'salaried', 'salary', 'salat', 'sale', 'saleable', 'salem', 'saleratus',
    'salerno', 'saleroom', 'sales', 'salesclerk', 'salesgirl', 'saleslady', 'salesman', 'salesmanship',
    'salesperson', 'salesroom', 'saleswoman', 'salian', 'salicaceae', 'salicales', 'salicornia', 'salicylate',
    'salience', 'saliency', 'salient', 'salientia', 'salientian', 'saliferous', 'salim', 'salina', 'salinate',
    'saline', 'salinger', 'salinity', 'salinometer', 'salisbury', 'salish', 'salishan', 'saliva', 'salivary',
    'salivate', 'salivation', 'salix', 'sallet', 'sallow', 'sallowness', 'sally', 'salmacis', 'salmagundi',
    'salmi', 'salmo', 'salmon', 'salmonberry', 'salmonella', 'salmonellosis', 'salmonid', 'salmonidae',
    'salmwood', 'salol', 'salome', 'salomon', 'salon', 'salonica', 'salonika', 'saloon', 'salsa', 'salsify',
    'salsilla', 'salsola', 'salt', 'salt-cured', 'saltate', 'saltation', 'saltbox', 'saltbush', 'saltcellar',
    'salted', 'salter', 'saltine', 'saltiness', 'salting', 'saltire', 'saltish', 'saltlike', 'saltpan',
    'saltpeter', 'saltpetre', 'saltshaker', 'saltwater', 'saltworks', 'saltwort', 'salty', 'salubrious',
    'salubriousness', 'salubrity', 'saluki', 'salutary', 'salutation', 'salutatorian', 'salutatory',
    'salute', 'saluter', 'salyut', 'unsalable', 'unsalaried', 'unsaleable', 'unsalted'
]

dict_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
dict_cur = dict_conn.cursor()

corpus_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
corpus_cur = corpus_conn.cursor()

results = {}
for w in words_sal:
    dict_cur.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    defs = dict_cur.fetchall()
    
    # search quotes via sentences_fts
    search_term = w.replace("-", " ").replace("'", "")
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
with open("scratch/speed_batch7_raw.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved to scratch/speed_batch7_raw.json")
