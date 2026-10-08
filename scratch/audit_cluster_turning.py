# -*- coding: utf-8 -*-
import os
import subprocess
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"App database/Latin roots/Cluster Turning"
dashboards = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])
print(f"Total dashboards in Cluster Turning: {len(dashboards)}")

total_audited = 0
total_pristine = 0
total_problems = 0

for d in dashboards:
    target = os.path.join(base_dir, d)
    cmd = ["node", "main app/scripts/audit-latin-roots.mjs", target]
    res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    out = res.stdout
    pristine = 0
    problems = 0
    for line in out.splitlines():
        if "Pristine words:" in line:
            pristine = int(line.split(":")[1].strip())
        elif "Problem words:" in line:
            problems = int(line.split(":")[1].strip())
    total_pristine += pristine
    total_problems += problems
    total_audited += (pristine + problems)
    status_icon = "PASS" if problems == 0 else "FAIL"
    print(f"[{status_icon}] {d}: {pristine} pristine, {problems} problems")

print(f"\n========================================")
print(f"CLUSTER TURNING OVERALL AUDIT:")
print(f"Total Words Audited: {total_audited}")
print(f"Total Pristine Words: {total_pristine}")
print(f"Total Problem Words: {total_problems}")
verdict = "100% PRISTINE (PASS)" if total_problems == 0 and total_audited == 592 else "FAIL"
print(f"Verdict: {verdict}")
print(f"========================================")
