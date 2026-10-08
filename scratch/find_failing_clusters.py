# -*- coding: utf-8 -*-
import os
import subprocess
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_path = "App database/Latin roots"
clusters = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d)) and d.startswith("Cluster")])

failing = []
pristine = []

for c in clusters:
    c_path = os.path.join(base_path, c)
    cmd = ["node", "main app/scripts/audit-latin-roots.mjs", c_path]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    out = res.stdout or ""
    if "100% PRISTINE (PASS)" in out:
        pristine.append(c)
        print(f"✅ {c}")
    else:
        # parse problem count
        prob_count = 0
        total_count = 0
        for line in out.splitlines():
            if line.startswith("Problem words:"):
                prob_count = line.split(":", 1)[1].strip()
            if line.startswith("Total words audited:"):
                total_count = line.split(":", 1)[1].strip()
        failing.append((c, prob_count, total_count))
        print(f"❌ {c}: {prob_count} problems / {total_count} words")

print("\n" + "="*50)
print(f"PRISTINE: {len(pristine)} / {len(clusters)}")
print(f"FAILING: {len(failing)} / {len(clusters)}")
for c, p, t in failing:
    print(f"  - {c}: {p} problems out of {t} words")
