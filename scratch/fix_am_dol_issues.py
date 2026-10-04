# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding="utf-8")

base = "App database/Latin roots/Cluster Emotion"

# 1. am/enamoredness.md
fpath = os.path.join(base, "Dashboard — am", "enamoredness.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The state or condition of being enamored; deep romantic infatuation, captivation, or love.",
    "Deep romantic infatuation, passionate captivation, or intense loving absorption in another."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 2. dol/dolichocephaly.md
fpath = os.path.join(base, "Dashboard — dol", "dolichocephaly.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The physical condition of being long-headed; having a cephalic index of less than 75.",
    "Cranial elongation characterized by a cephalic index of less than 75; dolichocephalism."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

for d in ["Dashboard — am", "Dashboard — dol"]:
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base}/{d}"], capture_output=True, encoding="utf-8")
    print(res.stdout)
