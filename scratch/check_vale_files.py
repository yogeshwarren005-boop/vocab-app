# -*- coding: utf-8 -*-
import os
import re

p = 'App database/Latin roots/Cluster Power/Dashboard — vale'
files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])

for f in files:
    with open(os.path.join(p, f), encoding="utf-8") as fp:
        c = fp.read()
    quotes = re.findall(r'> - 📜 \*\*([^*]+)\s*\(\*([^*]+)\*\):\*\*\s*([^\n]+)', c)
    print(f"\n=== {f[:-3]} ({len(quotes)} quotes) ===")
    for q in quotes:
        print(f"  {q[0]} ({q[1]}): {q[2][:90]}")
