# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding="utf-8")

base = "App database/Latin roots/Cluster Emotion/Dashboard — plac"

# 1. misplacement.md
fpath = os.path.join(base, "misplacement.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The action of putting something in the wrong place, or the state of being misplaced.",
    "The act of putting something in the wrong location, or an erroneous arrangement of objects."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 2. placidity.md
fpath = os.path.join(base, "placidity.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The state or quality of being placid; serenity, calmness, or peaceful quietude.",
    "Serene calmness, tranquil peacefulness, or an undisturbed equilibrium of mind."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", base], capture_output=True, encoding="utf-8")
print(res.stdout)
