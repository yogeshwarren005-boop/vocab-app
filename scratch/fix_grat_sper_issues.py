# -*- coding: utf-8 -*-
import os, sys, subprocess

sys.stdout.reconfigure(encoding="utf-8")

base = "App database/Latin roots/Cluster Emotion"

# 1. grat/gratefulness.md
fpath = os.path.join(base, "Dashboard — grat", "gratefulness.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The feeling or quality of being grateful; sincere thankfulness and appreciation.",
    "A warm feeling of heartfelt thankfulness, appreciation, or indebtedness for benefits received."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 2. grat/ingrate.md
fpath = os.path.join(base, "Dashboard — grat", "ingrate.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace("Ingrate, he had of me", "**Ingrate**, he had of me")
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 3. grat/ingratitude.md
fpath = os.path.join(base, "Dashboard — grat", "ingratitude.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace("Ingratitude, thou marble-hearted", "**Ingratitude**, thou marble-hearted")
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 4. sper/dispersion.md
fpath = os.path.join(base, "Dashboard — sper", "dispersion.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The action or process of distributing or scattering; state of being widely distributed.",
    "The act or process of scattering, spreading, or distributing things over a wide geographic area."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 5. sper/interspersal.md
fpath = os.path.join(base, "Dashboard — sper", "interspersal.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The act of interspersing, or the state of being interspersed; scattering among other things.",
    "The act or process of scattering, placing, or inserting contrasting elements irregularly among other things."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 6. sper/interspersion.md
fpath = os.path.join(base, "Dashboard — sper", "interspersion.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The condition of being interspersed; the scattering of one thing among others.",
    "The irregular scattering, insertion, or intermingling of one thing among other distinct elements."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

# 7. sper/prosperity.md
fpath = os.path.join(base, "Dashboard — sper", "prosperity.md")
with open(fpath, "r", encoding="utf-8") as f: c = f.read()
c = c.replace(
    "The state of being prosperous; good fortune, financial success, or physical well-being.",
    "Thriving financial success, abundant good fortune, and physical or material well-being."
)
with open(fpath, "w", encoding="utf-8") as f: f.write(c)

for d in ["Dashboard — grat", "Dashboard — sper"]:
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base}/{d}"], capture_output=True, encoding="utf-8")
    print(res.stdout)
