import sqlite3, json, sys, re, os

sys.stdout.reconfigure(encoding="utf-8")

p = r"App database\Latin roots\Cluster Carrying\Dashboard — trib"
words = [f.replace(".md", "") for f in sorted(os.listdir(p)) if f.endswith(".md") and not f.startswith("Dashboard — ") and not f.startswith("Word Triage — ")]

print(f"Total words in trib: {len(words)}")

conn_dict = sqlite3.connect("main app/corpus/local_dictionary.db")
c_dict = conn_dict.cursor()

conn_cit = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cit = conn_cit.cursor()

results = {}

for w in words:
    # 1. Fetch definitions
    defs = c_dict.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,)).fetchall()
    
    # 2. Fetch citations from FTS
    # Try exact match first
    # Clean word for FTS
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
            # Check if sentence actually contains whole word
            pattern = re.compile(r'\b' + re.escape(w) + r'\b', re.IGNORECASE)
            if pattern.search(r[2]):
                cits.append({"author": r[0], "work": r[1], "sentence": r[2]})

    results[w] = {
        "definitions": [{"source": d[0], "text": d[1]} for d in defs],
        "citations": cits
    }

with open("scratch/trib_raw.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved scratch/trib_raw.json successfully!")
for w in words[:15]:
    d_count = len(results[w]["definitions"])
    c_count = len(results[w]["citations"])
    print(f"  {w}: {d_count} defs, {c_count} citations")
