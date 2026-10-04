# -*- coding: utf-8 -*-
import sqlite3, re, json

words = ['defectiveness', 'effectivity', 'feces', 'fecula', 'feculence', 'feculent', 'fecund', 'fecundate', 'fecundation', 'fecundity', 'imperfect', 'imperfectibility', 'imperfectible', 'imperfection', 'imperfective', 'imperfectly', 'imperfectness', 'ineffective', 'ineffectively', 'ineffectiveness', 'ineffectual', 'ineffectuality', 'ineffectually', 'ineffectualness', 'infect', 'infected', 'infection', 'infectious', 'infectiously', 'infective', 'noninfectious', 'perfect', 'perfecta', 'perfected', 'perfecter', 'perfectibility', 'perfectible', 'perfection', 'perfectionism', 'perfectionist', 'perfective', 'perfectly', 'prefect', 'prefectural', 'prefecture', 'refection', 'refectory', 'superfecta', 'superfecundation', 'superinfect', 'superinfection', 'suprainfection', 'unaffected', 'unaffectedness', 'unaffecting', 'unaffectionate', 'uneffective', 'uninfected']

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cursor = conn.cursor()

results = {}
for w in words:
    # Use FTS MATCH
    try:
        query = f"SELECT s.author, s.work, s.sentence FROM sentences_fts fts JOIN sentences s ON fts.rowid = s.id WHERE sentences_fts MATCH ? LIMIT 100"
        cursor.execute(query, (w,))
        rows = cursor.fetchall()
    except Exception as e:
        rows = []
    
    pattern = re.compile(rf'\b({re.escape(w)})\b', re.IGNORECASE)
    seen_authors = set()
    valid_quotes = []
    for auth, work, sent in rows:
        if auth in seen_authors:
            continue
        if pattern.search(sent) and len(sent) > 30 and len(sent) < 300:
            # check bolding capability
            seen_authors.add(auth)
            valid_quotes.append({
                "author": auth,
                "work": work,
                "sentence": sent
            })
            if len(valid_quotes) == 3:
                break
    results[w] = valid_quotes

with open('scratch/fec_found_quotes.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print("Finished searching. Summary:")
for w, q in results.items():
    print(f"{w}: {len(q)} quotes")
