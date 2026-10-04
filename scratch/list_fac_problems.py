# -*- coding: utf-8 -*-
import subprocess, json

res = subprocess.run(['node', 'main app/scripts/audit-latin-roots.mjs', 'App database/Latin roots/Cluster Action/Dashboard — fac'], capture_output=True, encoding='utf-8', errors='replace')
bad_words = []
for l in res.stdout.splitlines():
    if l.startswith('❌ '):
        w = l.replace('❌ ', '').split(':')[0].strip()
        bad_words.append(w)

print(f"Total bad words in fac: {len(bad_words)}")
with open('scratch/fac_157_problem_words.json', 'w', encoding='utf-8') as f:
    json.dump(bad_words, f, indent=2)

print("Batch 1 (1-50):", bad_words[:50])
print("Batch 2 (51-100):", bad_words[50:100])
print("Batch 3 (101-157):", bad_words[100:])
