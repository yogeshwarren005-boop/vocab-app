# -*- coding: utf-8 -*-
"""
query_val_corpus.py
Queries citation_corpus.db for all 105 words in Dashboard — val
"""
import sqlite3
import json
import re

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

words = ['circumvallate', 'convalesce', 'convalescence', 'convalescent', 'convallaria', 'convallariaceae', 'covalence', 'covalency', 'covalent', 'devaluate', 'devaluation', 'devalue', 'devalued', 'divalent', 'evaluate', 'evaluation', 'evaluative', 'evaluator', 'interval', 'invalid', 'invalidate', 'invalidated', 'invalidating', 'invalidation', 'invalidator', 'invalidism', 'invalidity', 'invalidness', 'invaluable', 'invaluableness', 'overvaliant', 'overvaluation', 'overvalue', 'prevalence', 'prevalent', 'reevaluate', 'reevaluation', 'revaluation', 'revalue', 'underevaluation', 'undervaluation', 'undervalue', 'unvalued', 'valance', 'vale', 'valediction', 'valedictorian', 'valedictory', 'valence', 'valencia', 'valenciennes', 'valency', 'valent', 'valentine', 'valerian', 'valeriana', 'valerianaceae', 'valerianella', 'valet', 'valetta', 'valetudinarian', 'valetudinarianism', 'valetudinary', 'vali', 'valiance', 'valiancy', 'valiant', 'valiantly', 'valid', 'validate', 'validated', 'validating', 'validation', 'validatory', 'validity', 'validly', 'validness', 'valine', 'valise', 'valium', 'vallecula', 'valletta', 'valley', 'vallisneria', 'valmy', 'valois', 'valor', 'valorous', 'valorously', 'valorousness', 'valour', 'valsartan', 'valse', 'valuable', 'valuableness', 'valuate', 'valuation', 'valuator', 'value-system', 'value', 'valued', 'valueless', 'valuelessness', 'valuer', 'values']

results = {}

for w in words:
    query = f'"{w}"'
    try:
        cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT 300
        """, (query,))
        rows = cur.fetchall()
    except Exception as e:
        rows = []

    seen = set()
    dedup = []
    pattern = re.compile(rf'\b{re.escape(w)}\b', re.IGNORECASE)
    for a, wrk, st in rows:
        if a not in seen:
            seen.add(a)
            # Find and bold the word
            m = pattern.search(st)
            if m:
                start, end = m.span()
                bolded = st[:start] + f"**{st[start:end]}**" + st[end:]
            else:
                bolded = st
            dedup.append({"author": a, "work": wrk, "sentence": bolded})
    results[w] = dedup
    print(f"{w:20}: {len(dedup):3} distinct authors: {[x['author'] for x in dedup[:4]]}")

conn.close()

with open("scratch/val_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nSaved scratch/val_rich_corpus.json successfully.")
