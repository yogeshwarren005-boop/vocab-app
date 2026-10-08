# -*- coding: utf-8 -*-
import sqlite3
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cur = conn.cursor()

words = [
    'coregonidae', 'coregonus', 'corregidor', 'deregulate', 'deregulating', 'deregulation',
    'disregard', 'disregarded', 'disregarding', 'disregardless', 'interregnum', 'irregardless',
    'irregular', 'irregularity', 'irregularly', 'regain', 'regaining', 'regal', 'regale',
    'regalecidae', 'regalia', 'regally', 'regard', 'regardant', 'regardful', 'regardless',
    'regatta', 'regency', 'regenerate', 'regenerating', 'regeneration', 'regent', 'regicide',
    'regime', 'regimen', 'regiment', 'regimental', 'regimentally', 'regimentals',
    'regimentation', 'regimented', 'regina', 'regiomontanus', 'region', 'regional',
    'regionalism', 'regionally', 'register', 'registered', 'registrant', 'registrar',
    'registration', 'registry', 'reglaecus', 'regnant', 'regnellidium', 'regorge',
    'regosol', 'regress', 'regression', 'regressive', 'regret', 'regretful', 'regretfully',
    'regrets', 'regrettable', 'regrettably', 'regroup', 'regrow', 'regular',
    'regularisation', 'regularise', 'regularity', 'regularization', 'regularize',
    'regularly', 'regulate', 'regulated', 'regulating', 'regulation', 'regulative',
    'regulator', 'regulatory', 'regulus', 'regur', 'regurgitate', 'regurgitation',
    'subregent', 'unregenerate', 'unregenerated', 'unregistered', 'unregretful',
    'unregretting', 'unregularity', 'unregulated'
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

with open("scratch/reg_rich_corpus.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
