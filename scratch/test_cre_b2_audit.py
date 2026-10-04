# -*- coding: utf-8 -*-
import subprocess, os, re

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — cre"
with open("scratch/generate_cre_batch2.py", encoding="utf-8") as f:
    c = f.read()

fnames = re.findall(r'"([a-z0-9\-]+\.md)": \{', c)
print(f"Auditing {len(fnames)} files in cre Batch 2...")

failed = 0
for fname in fnames:
    fpath = os.path.join(base_dir, fname)
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", fpath], capture_output=True, encoding="utf-8", errors="replace")
    if "FAIL" in res.stdout or "❌" in res.stdout:
        print(f"Fail: {fname}")
        for l in res.stdout.splitlines():
            if "❌" in l or "   -" in l:
                print(" ", l)
        failed += 1

print(f"Result: {len(fnames) - failed}/{len(fnames)} PASSED.")
