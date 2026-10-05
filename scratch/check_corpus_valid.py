import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

conn = sqlite3.connect("main app/corpus/citation_corpus.db")
cur = conn.cursor()

def search_word(w):
    clean = w.replace("-", " ")
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences s 
        JOIN sentences_fts f ON s.id = f.rowid 
        WHERE f.sentence MATCH ?
        LIMIT 50
    """, (f'"{clean}"',))
    rows = cur.fetchall()
    by_auth = {}
    for a, wk, s in rows:
        if not a or a in ["Classic Author", "Academic Lexicon"] or "Author" in a:
            continue
        if a not in by_auth:
            by_auth[a] = (wk, s)
    return by_auth

words = ["ascites", "ascitic", "citadel", "citation", "cite", "citizen", "citizenry", "citizenship", 
         "citrate", "citric", "citron", "citrus", "city", "city-state", "cityscape", "citywide", 
         "excitable", "excitation", "excite", "excited", "excitedly", "excitement", "exciting", "excitingly", 
         "incite", "incitement", "recital", "recitation", "recitative", "recite",
         "annunciation", "denunciation", "denunciatory", "enunciate", "enunciation", "nuncio", "pronunciation", "renunciation"]

for w in words:
    res = search_word(w)
    print(f"{w}: {len(res)} valid distinct authors -> {list(res.keys())[:4]}")
