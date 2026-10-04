# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding="utf-8")

base = "App database/Latin roots/Cluster Emotion/Dashboard — cup"

# 1. occupy.md
fpath = os.path.join(base, "occupy.md")
with open(fpath, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("'occupy'", "'**occupy**'")
with open(fpath, "w", encoding="utf-8") as f:
    f.write(c)

# 2. preoccupation.md
fpath = os.path.join(base, "preoccupation.md")
with open(fpath, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace(
    "The state or condition of being engrossed in or absorbed by thought; distraction.",
    "Deep absorption or engrossment in thought; mental distraction by an obsessive concern."
)
with open(fpath, "w", encoding="utf-8") as f:
    f.write(c)

res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", base], capture_output=True, encoding="utf-8")
print(res.stdout)
