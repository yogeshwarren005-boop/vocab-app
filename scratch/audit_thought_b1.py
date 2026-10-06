# -*- coding: utf-8 -*-
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

dashboards = [
    r"App database/Latin roots/Cluster Thought/Dashboard — cern",
    r"App database/Latin roots/Cluster Thought/Dashboard — cogit",
    r"App database/Latin roots/Cluster Thought/Dashboard — cogn",
    r"App database/Latin roots/Cluster Thought/Dashboard — estim",
    r"App database/Latin roots/Cluster Thought/Dashboard — ment",
    r"App database/Latin roots/Cluster Thought/Dashboard — opin"
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
    print("Final Thought Batch 1 Verdict: ALL PASS ✅")
else:
    print("Final Thought Batch 1 Verdict: SOME FAILED ❌")
