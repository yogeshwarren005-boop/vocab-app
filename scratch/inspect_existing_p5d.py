# -*- coding: utf-8 -*-
import json
import os
import re

words = json.load(open('scratch/number_b5_words.json', encoding='utf-8'))[186:]
dirpath = 'App database/Latin roots/Cluster Number & Measure/Dashboard — dec'

for w in words[:10]:
    fp = os.path.join(dirpath, f"{w}.md")
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    print("="*40)
    print("WORD:", w)
    print(content[:300])
