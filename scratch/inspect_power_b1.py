# -*- coding: utf-8 -*-
import os
import re

dashboards = ['Dashboard — majest', 'Dashboard — regn', 'Dashboard — pot', 'Dashboard — princ', 'Dashboard — vale']
base = 'App database/Latin roots/Cluster Power'
for d in dashboards:
    p = os.path.join(base, d)
    files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])
    print(f"\n=== {d} ({len(files)} files) ===")
    for f in files[:4]:
        with open(os.path.join(p, f), encoding='utf-8') as fp:
            c = fp.read()
        quotes = re.findall(r'> - 📜 \*\*([^*]+)\s*\(\*([^*]+)\*\):\*\*\s*([^\n]+)', c)
        print(f"  {f}: {len(quotes)} quotes")
        for q in quotes:
            print(f"    - {q[0]} ({q[1]}): {q[2][:70]}...")
