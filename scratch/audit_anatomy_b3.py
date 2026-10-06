# -*- coding: utf-8 -*-
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

dashboards = [
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — mamm",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — oss",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — pector",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — pelv",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — pulmon",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — sanguin",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — ungui",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — valv",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — ventr",
    r"App database/Latin roots/Cluster Anatomy & Clinical Medicine/Dashboard — viscer"
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
    print("Final Anatomy Batch 3 Verdict: ALL PASS ✅")
else:
    print("Final Anatomy Batch 3 Verdict: SOME FAILED ❌")
