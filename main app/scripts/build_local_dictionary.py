import os
import json
import sqlite3
import urllib.request
from nltk.corpus import wordnet

DB_PATH = os.path.join("main app", "corpus", "local_dictionary.db")
WEBSTER_URL = "https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json"
CACHE_JSON = os.path.join("main app", "corpus", "webster_dictionary.json")

def setup_local_dictionary():
    print(f"--- Setting up Local Dictionary Database: {DB_PATH} ---")
    
    # 1. Download Webster if not already cached
    if not os.path.exists(CACHE_JSON):
        print(f"Downloading Webster dictionary from {WEBSTER_URL}...")
        req = urllib.request.Request(WEBSTER_URL, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp, open(CACHE_JSON, "wb") as f:
            f.write(resp.read())
        print(f"Downloaded and saved to {CACHE_JSON}")
    else:
        print(f"Using cached Webster dictionary at {CACHE_JSON}")

    with open(CACHE_JSON, "r", encoding="utf-8") as f:
        webster_data = json.load(f)
    print(f"Loaded {len(webster_data)} Webster entries.")

    # 2. Initialize SQLite Database
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS dictionary_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        source TEXT NOT NULL,
        definition TEXT NOT NULL,
        sense_number INTEGER DEFAULT 1
    );
    """)
    cur.execute("CREATE INDEX IF NOT EXISTS idx_dict_word ON dictionary_entries(word);")

    # 3. Insert Webster entries
    print("Inserting Webster dictionary entries...")
    webster_rows = []
    for word, defn in webster_data.items():
        clean_word = word.strip().lower()
        if clean_word and defn:
            webster_rows.append((clean_word, "webster_1913", defn.strip(), 1))

    cur.executemany("INSERT INTO dictionary_entries (word, source, definition, sense_number) VALUES (?, ?, ?, ?)", webster_rows)
    con.commit()
    print(f"Inserted {len(webster_rows)} Webster entries.")

    # 4. Insert WordNet synsets
    print("Extracting and inserting Princeton WordNet 3.1 synsets...")
    wn_rows = []
    all_lemmas = set(wordnet.all_lemma_names())
    for lemma in all_lemmas:
        clean_word = lemma.replace("_", " ").strip().lower()
        syns = wordnet.synsets(lemma)
        for idx, s in enumerate(syns[:4]):
            d = s.definition().strip()
            if d:
                pos = s.pos()
                wn_rows.append((clean_word, f"wordnet_{pos}", d, idx + 1))

    cur.executemany("INSERT INTO dictionary_entries (word, source, definition, sense_number) VALUES (?, ?, ?, ?)", wn_rows)
    con.commit()
    print(f"Inserted {len(wn_rows)} WordNet synsets across {len(all_lemmas)} lemmas.")

    total_count = cur.execute("SELECT COUNT(*) FROM dictionary_entries").fetchone()[0]
    print(f"Local Dictionary DB complete! Total entries: {total_count}")
    con.close()

if __name__ == "__main__":
    setup_local_dictionary()
