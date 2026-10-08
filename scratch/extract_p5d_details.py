# -*- coding: utf-8 -*-
import sqlite3
import json

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

words = json.load(open('scratch/number_b5_words.json', encoding='utf-8'))[186:]

defs_map = {}
for w in words:
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number ASC", (w,))
    defs = [r[0].strip() for r in d_cur.fetchall()]
    defs_map[w] = defs

with open('scratch/p5d_defs.json', 'w', encoding='utf-8') as f:
    json.dump(defs_map, f, ensure_ascii=False, indent=2)

print("Saved scratch/p5d_defs.json")
