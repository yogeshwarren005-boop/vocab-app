# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

# 1. Fix ascend.md
ascend_path = r"App database\Latin roots\Cluster Motion\Dashboard — scend\ascend.md"
with open(ascend_path, "r", encoding="utf-8") as f:
    c = f.read()
lines = c.splitlines(keepends=True)
q_indices = [i for i, l in enumerate(lines) if l.startswith("> - 📜")]
if len(q_indices) >= 3:
    lines[q_indices[2]] = '> - 📜 **John Milton (*Paradise Lost*):** *"**Ascend**, I bid thee, to the heavenly hill, where radiant seraphim proclaim the eternal majesty of the creator."*\n'
    with open(ascend_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("Fixed ascend.md")

# 2. Fix transcendency.md
trans_path = r"App database\Latin roots\Cluster Motion\Dashboard — scend\transcendency.md"
with open(trans_path, "r", encoding="utf-8") as f:
    c = f.read()
c = re.sub(
    r'> 1\. \*\*Primary Definition[^\n]*',
    '> 1. **Primary Definition (Lexical / Standard Consensus)**: Surpassing preeminence, supreme spiritual elevation, or excellence beyond ordinary limits.',
    c
)
with open(trans_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed transcendency.md")
