# -*- coding: utf-8 -*-
import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("scratch/pat_db_dump.json", encoding="utf-8") as f:
    data = json.load(f)

words = list(data.keys())[66:]
for w in words:
    qs = data[w]["quotes"]
    if len(qs) > 0:
        print(f"{w}: {len(qs)} quotes found")
        for q in qs[:3]:
            print(f"   {q['author']} ({q['work']}): {q['sentence'][:75]}...")
