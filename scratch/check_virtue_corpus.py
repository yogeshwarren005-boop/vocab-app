# -*- coding: utf-8 -*-
import sqlite3
import re

opt_words = ['adopt', 'adoptable', 'adopted', 'adoptee', 'adopter', 'adoption', 'adoptive', 'apoptosis', 'co-opt', 'co-optation', 'co-option', 'diopter', 'dioptre', 'exopterygota', 'opt', 'optative', 'optez', 'optic', 'optical', 'optically', 'optician', 'optics', 'optimal', 'optimally', 'optimisation', 'optimise', 'optimism', 'optimist', 'optimistic', 'optimistically', 'optimization', 'optimize', 'optimum', 'option', 'optional', 'optionally', 'optometrist', 'optometry', 'unadoptable']

rob_words = ['acrobat', 'acrobates', 'acrobatic', 'acrobatics', 'agrobacterium', 'agrobiologic', 'agrobiological', 'agrobiology', 'arroba', 'corroborant', 'corroborate', 'corroboration', 'corroborative', 'corroboratory', 'disrobe', 'enrobe', 'rob', 'robalo', 'robaxin', 'robber', 'robbery', 'robe', 'robe-de-chambre', 'robed', 'robert', 'roberts', 'robertson', 'robeson', 'robespierre', 'robin', 'robinia', 'robinson', 'robitussin', 'roble', 'roborant', 'robot', 'robotic', 'robotics', 'robotlike', 'robust', 'robustious', 'robustly', 'robustness']

virt_words = ['virtu', 'virtual', 'virtuality', 'virtually', 'virtue', 'virtuosity', 'virtuoso', 'virtuous', 'virtuously', 'virtuousness']

all_words = opt_words + rob_words + virt_words

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c = conn.cursor()

corpus_results = {}
for w in all_words:
    clean_w = w.replace('-', ' ')
    try:
        c.execute('''
            SELECT s.author, s.work, s.sentence 
            FROM sentences s 
            JOIN sentences_fts f ON s.id = f.rowid 
            WHERE f.sentence MATCH ? 
            LIMIT 50
        ''', (f'"{clean_w}"',))
        rows = c.fetchall()
        by_author = {}
        for a, work, sent in rows:
            if a not in by_author and len(a) >= 3 and len(work) >= 2:
                by_author[a] = (work, sent)
        corpus_results[w] = by_author
    except Exception as e:
        corpus_results[w] = {}

print(f"Total words: {len(all_words)}")
sufficient = [w for w, auths in corpus_results.items() if len(auths) >= 3]
print(f"Words with >= 3 distinct authors in corpus: {len(sufficient)} / {len(all_words)}")
for w in all_words:
    cnt = len(corpus_results[w])
    if cnt < 3:
        print(f"  {w}: {cnt} authors")
