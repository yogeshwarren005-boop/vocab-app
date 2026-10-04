import sqlite3, json, os, re

# Connect to databases
dict_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
dict_cur = dict_conn.cursor()

corpus_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
corpus_cur = corpus_conn.cursor()

cluster_dir = r"App database\Latin roots\Cluster Sacred"
dashboards = sorted([d for d in os.listdir(cluster_dir) if os.path.isdir(os.path.join(cluster_dir, d))])

inventory = {}
for d in dashboards:
    d_path = os.path.join(cluster_dir, d)
    files = sorted([f for f in os.listdir(d_path) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])
    for f in files:
        w = f[:-3]
        rel_path = os.path.join(d, f)
        
        # Look up definitions
        dict_cur.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
        raw_defs = dict_cur.fetchall()
        
        # Look up corpus quotes
        search_term = w.replace('-', ' ')
        try:
            corpus_cur.execute("""
                SELECT s.author, s.work, s.sentence 
                FROM sentences_fts f
                JOIN sentences s ON f.rowid = s.id
                WHERE f.sentence MATCH ? LIMIT 10
            """, (f'"{search_term}"',))
            raw_quotes = corpus_cur.fetchall()
        except:
            raw_quotes = []
            
        inventory[rel_path] = {
            "word": w,
            "dashboard": d,
            "defs": [{"source": src, "def": df} for src, df in raw_defs],
            "quotes": [{"author": a, "work": wk, "sentence": s} for a, wk, s in raw_quotes]
        }

print(f"Loaded inventory for {len(inventory)} words across {len(dashboards)} dashboards.")
with open("scratch/sacred_inventory.json", "w", encoding="utf-8") as f:
    json.dump(inventory, f, ensure_ascii=False, indent=2)
print("Saved to scratch/sacred_inventory.json")
