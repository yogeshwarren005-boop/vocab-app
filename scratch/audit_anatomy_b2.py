# -*- coding: utf-8 -*-
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

dashboards = [
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — chir",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — dors",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — nas",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — nerv",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — pariet",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — vertebr"
]

all_pass = True

for d in dashboards:
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", d], capture_output=True, text=True, encoding="utf-8")
    d_name = d.split("— ")[-1]
    if "✅ 100% PRISTINE (PASS)" in res.stdout:
        print(f"✅ Dashboard — {d_name:<10}: 100% PRISTINE (PASS)")
    else:
        print(f"❌ Dashboard — {d_name:<10}: FAIL")
        print(res.stdout)
        all_pass = False

print()
if all_pass:
    print("Final Anatomy Batch 2 Verdict: ALL PASS ✅")
else:
    print("Final Anatomy Batch 2 Verdict: SOME FAILED ❌")
