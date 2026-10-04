# -*- coding: utf-8 -*-
import json, sys

sys.stdout.reconfigure(encoding="utf-8")

with open("scratch/tim_db_dump.json", encoding="utf-8") as f:
    data = json.load(f)

for w in list(data.keys())[:44]:
    qs = data[w]["quotes"]
    if len(qs) > 0:
        print(f"{w}: {len(qs)} quotes found")
        for q in qs[:3]:
            print(f"   {q['author']} ({q['work']}): {q['sentence'][:80]}...")
