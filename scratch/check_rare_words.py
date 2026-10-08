# -*- coding: utf-8 -*-
import os
import re

dashboards = ['Dashboard — regn', 'Dashboard — pot', 'Dashboard — princ']
base = 'App database/Latin roots/Cluster Power'
words_to_check = [
    'interregnum', 'regnal', 'regnancy', 'regnant', 'regnellidium',
    'potable', 'potage', 'potation', 'potence', 'repot',
    "prince's-feather", "prince's-plume", "prince-of-wales'-heath",
    'princedom', 'princeling', 'princeton', 'princewood',
    'principality', 'principalship', 'principe', 'principen', 'principled'
]

for d in dashboards:
    p = os.path.join(base, d)
    for w in words_to_check:
        fpath = os.path.join(p, f"{w}.md")
        if os.path.exists(fpath):
            with open(fpath, encoding="utf-8") as fp:
                c = fp.read()
            quotes = re.findall(r'> - 📜 \*\*([^*]+)\s*\(\*([^*]+)\*\):\*\*\s*([^\n]+)', c)
            print(f"\n=== {w} ===")
            for q in quotes:
                print(f"  {q[0]} ({q[1]}): {q[2][:90]}")
