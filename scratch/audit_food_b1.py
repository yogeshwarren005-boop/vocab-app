# -*- coding: utf-8 -*-
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

dashboards = ['bib', 'coct', 'coqu', 'ed', 'lact', 'mell', 'pan', 'pota']
all_pass = True

for d in dashboards:
    target = f"App database/Latin roots/Cluster Food, Eating & Drink/Dashboard — {d}"
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", target], capture_output=True, text=True, encoding="utf-8")
    if "100% PRISTINE (PASS)" in res.stdout:
        print(f"✅ Dashboard — {d:6}: 100% PRISTINE (PASS)")
    else:
        all_pass = False
        print(f"❌ Dashboard — {d:6}: FAIL")
        print(res.stdout)

print(f"\nFinal Batch 1 Verdict: {'ALL PASS ✅' if all_pass else 'FAIL ❌'}")
