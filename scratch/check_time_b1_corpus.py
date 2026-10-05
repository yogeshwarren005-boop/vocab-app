# -*- coding: utf-8 -*-
import sqlite3
import json

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

words = [
    # cras (9)
    'crass', 'crassitude', 'crassness', 'crassostrea', 'crassula', 'crassulaceae', 'procrastinate', 'procrastination', 'procrastinator',
    # di (15)
    'antemeridian', 'circadian', 'cordial', 'cordiality', 'cordially', 'dial', 'diarist', 'diary', 'diurnal', 'meridian', 'meridional', 'postmeridian', 'precordial', 'precordium', 'uncordial',
    # ev (3)
    'coeval', 'ev', 'longevity',
    # nov (21)
    'innovate', 'innovation', 'innovational', 'innovative', 'innovativeness', 'innovator', 'nov', 'nova', 'novate', 'novation', 'novel', 'novelette', 'novelise', 'novelist', 'novelize', 'novelty', 'novice', 'renovate', 'renovation', 'renovator', 'supernova',
    # saecul (7)
    'secular', 'secularisation', 'secularise', 'secularism', 'secularist', 'secularization', 'secularize',
    # simul (16)
    'dissimulate', 'dissimulation', 'dissimulative', 'dissimulator', 'simulacrum', 'simulate', 'simulated', 'simulation', 'simulator', 'simulcast', 'simuliidae', 'simulium', 'simultaneity', 'simultaneous', 'simultaneously', 'simultaneousness'
]

results = {}

for w in words:
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ?", (w,))
    defs = [r[0] for r in d_cur.fetchall()]
    
    quotes = []
    try:
        c_cur.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 20
        """, (f'"{w}"',))
        quotes = [{"author": r[0], "work": r[1], "sentence": r[2]} for r in c_cur.fetchall()]
    except Exception as e:
        pass
    
    # Check distinct authors
    auths = list(set(q["author"] for q in quotes))
    results[w] = {
        "defs": defs,
        "quotes_count": len(quotes),
        "distinct_authors": len(auths),
        "authors": auths[:5]
    }
    print(f"{w:18} | defs: {len(defs):2} | quotes: {len(quotes):2} | auths: {len(auths):2}")

with open("scratch/check_time_b1_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("Done! Total words checked:", len(words))
