# -*- coding: utf-8 -*-
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

dashboards = ['adip', 'aur_ear', 'cervic', 'dent', 'front', 'lacrim', 'maxill', 'ocul']
all_pass = True

for d in dashboards:
    target = f"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — {d}"
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", target], capture_output=True, text=True, encoding="utf-8")
    if "100% PRISTINE (PASS)" in res.stdout:
        print(f"✅ Dashboard — {d:10}: 100% PRISTINE (PASS)")
    else:
        all_pass = False
        print(f"❌ Dashboard — {d:10}: FAIL")
        print(res.stdout)

print(f"\nFinal Anatomy Batch 1 Verdict: {'ALL PASS ✅' if all_pass else 'FAIL ❌'}")
