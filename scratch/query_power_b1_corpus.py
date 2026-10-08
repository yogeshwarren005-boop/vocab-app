# -*- coding: utf-8 -*-
import sqlite3
import json

db_path = r"main app/corpus/citation_corpus.db"
conn = sqlite3.connect(db_path)
cur = conn.cursor()

dashboards = {
    'majest': ['majestic', 'majestically', 'majesty'],
    'regn': ['interregnum', 'regnal', 'regnancy', 'regnant', 'regnellidium'],
    'pot': ['depot', 'pot', 'potable', 'potage', 'potation', 'potence', 'potent', 'potion', 'repot'],
    'princ': ['prince', "prince's-feather", "prince's-plume", "prince-of-wales'-heath", 'princedom', 'princeling', 'princely', 'princess', 'princeton', 'princewood', 'principal', 'principality', 'principally', 'principalship', 'principe', 'principen', 'principle', 'principled', 'unprincipled'],
    'vale': ['ambivalence', 'ambivalent', 'convalesce', 'convalescence', 'convalescent', 'covalence', 'covalency', 'covalent', 'divalent', 'equivalence', 'equivalent', 'nonequivalence', 'nonequivalent', 'prevalence', 'prevalent', 'vale', 'valediction', 'valedictorian', 'valence', 'valencia', 'valenciennes', 'valency', 'valent', 'valentine', 'valerian', 'valeriana', 'valerianaceae', 'valerianella', 'valet', 'valetta', 'valetudinarian', 'valetudinarianism', 'valetudinary'],
    'imper': ['imperative', 'imperatively', 'imperativeness', 'imperceptibility', 'imperceptible', 'imperceptibly', 'imperial', 'imperialism', 'imperialist', 'imperialistic', 'imperially', 'imperil', 'imperious', 'imperiously', 'imperiousness', 'imperishability', 'imperishable', 'imperishableness', 'imperishingness', 'imperium', 'impermanence', 'impermanency', 'impermanent', 'impermeability', 'impermeable', 'impermeableness', 'impermissibility', 'impermissible', 'impermissibly', 'impersonal', 'impersonally', 'impersonate', 'impersonation', 'impersonator', 'impertinence', 'impertinent', 'impertinently', 'imperturbability', 'imperturbable', 'imperturbableness']
}

all_words = []
for words in dashboards.values():
    all_words.extend(words)

print(f"Total words: {len(all_words)}")

hits = {}
for w in all_words:
    clean_w = w.replace("'", "").replace("-", " ")
    cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f 
        JOIN sentences s ON f.rowid = s.id 
        WHERE f.sentence MATCH ? LIMIT 15
    """, (f'"{w}"',))
    rows = cur.fetchall()
    if rows:
        # deduplicate by author
        seen = set()
        dedup = []
        for r in rows:
            if r[0] not in seen:
                seen.add(r[0])
                dedup.append({"author": r[0], "work": r[1], "sentence": r[2]})
        hits[w] = dedup

print(f"Words with hits in corpus: {len(hits)} / {len(all_words)}")
with open(r"scratch/power_b1_corpus_hits.json", "w", encoding="utf-8") as f:
    json.dump(hits, f, indent=2, ensure_ascii=False)
