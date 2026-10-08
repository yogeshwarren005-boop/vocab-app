# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

words = [
    'imperative', 'imperatively', 'imperativeness', 'imperceptibility', 'imperceptible',
    'imperceptibly', 'imperial', 'imperialism', 'imperialist', 'imperialistic',
    'imperially', 'imperil', 'imperious', 'imperiously', 'imperiousness',
    'imperishability', 'imperishable', 'imperishableness', 'imperishingness', 'imperium',
    'impermanence', 'impermanency', 'impermanent', 'impermeability', 'impermeable',
    'impermeableness', 'impermissibility', 'impermissible', 'impermissibly', 'impersonal',
    'impersonally', 'impersonate', 'impersonation', 'impersonator', 'impertinence',
    'impertinent', 'impertinently', 'imperturbability', 'imperturbable', 'imperturbableness'
]

results = {}
for w in words:
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 300
    """, (f'"{w}"',))
    rows = cur.fetchall()
    seen = set()
    dedup = []
    for a, wrk, st in rows:
        if a not in seen:
            seen.add(a)
            dedup.append({"author": a, "work": wrk, "sentence": st})
    results[w] = dedup
    print(f"{w}: {len(dedup)} distinct authors: {[x['author'] for x in dedup[:4]]}")

with open("scratch/imper_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
