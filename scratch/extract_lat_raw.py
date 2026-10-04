import sqlite3, json, sys, re, os

sys.stdout.reconfigure(encoding="utf-8")

p = r"App database\Latin roots\Cluster Carrying\Dashboard — lat"
words = [f.replace(".md", "") for f in sorted(os.listdir(p)) if f.endswith(".md") and not f.startswith("Dashboard — ") and not f.startswith("Word Triage — ")]

print(f"Total words in lat: {len(words)}")

conn_dict = sqlite3.connect("main app/corpus/local_dictionary.db")
c_dict = conn_dict.cursor()

conn_cit = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cit = conn_cit.cursor()

results = {}

for w in words:
    defs = c_dict.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,)).fetchall()
    
    clean_w = re.sub(r'[^a-zA-Z0-9]', '', w)
    cits = []
    if clean_w:
        rows = c_cit.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 15
        """, (f'"{clean_w}"',)).fetchall()
        for r in rows:
            pattern = re.compile(r'\b' + re.escape(w) + r'\b', re.IGNORECASE)
            if pattern.search(r[2]):
                cits.append({"author": r[0], "work": r[1], "sentence": r[2]})

    results[w] = {
        "definitions": [{"source": d[0], "text": d[1]} for d in defs],
        "citations": cits
    }

with open("scratch/lat_raw.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved scratch/lat_raw.json successfully!")
has_cits = sum(1 for w, v in results.items() if len(v["citations"]) >= 3)
has_defs = sum(1 for w, v in results.items() if len(v["definitions"]) > 0)
print(f"Words with >=3 citations: {has_cits}/{len(words)}")
print(f"Words with definitions: {has_defs}/{len(words)}")
