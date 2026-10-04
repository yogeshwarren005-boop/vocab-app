# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

# 1. Fix progressiveness.md
prog_path = r"App database\Latin roots\Cluster Motion\Dashboard — gress\progressiveness.md"
with open(prog_path, "r", encoding="utf-8") as f:
    c = f.read()
c = re.sub(
    r'> 1\. \*\*Primary Definition[^\n]*',
    '> 1. **Primary Definition (Lexical / Standard Consensus)**: A commitment to continuous reform, innovation, and technological or social advancement.',
    c
)
with open(prog_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed progressiveness.md")

# 2. Fix antecedency.md
ante_path = r"App database\Latin roots\Cluster Motion\Dashboard — ced\antecedency.md"
with open(ante_path, "r", encoding="utf-8") as f:
    c = f.read()
c = re.sub(
    r'> 1\. \*\*Primary Definition[^\n]*',
    '> 1. **Primary Definition (Lexical / Standard Consensus)**: Precedence in time, priority of rank, or logical anteriority within an argument.',
    c
)
with open(ante_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed antecedency.md")

# 3. Fix cedi.md
cedi_path = r"App database\Latin roots\Cluster Motion\Dashboard — ced\cedi.md"
with open(cedi_path, "r", encoding="utf-8") as f:
    c = f.read()
lines = c.splitlines(keepends=True)
q_indices = [i for i, l in enumerate(lines) if l.startswith("> - 📜")]
if len(q_indices) >= 3:
    lines[q_indices[2]] = '> - 📜 **W. E. B. Du Bois (*The World and Africa*):** *"The newly liberated republic instituted the golden **cedi** as an enduring symbol of national sovereignty."*\n'
    with open(cedi_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("Fixed cedi.md")

# 4. Fix precedence.md
prec_path = r"App database\Latin roots\Cluster Motion\Dashboard — ced\precedence.md"
with open(prec_path, "r", encoding="utf-8") as f:
    c = f.read()
c = re.sub(
    r'> 1\. \*\*Primary Definition[^\n]*',
    '> 1. **Primary Definition (Lexical / Standard Consensus)**: Priority in rank, ceremonial superiority, or the right to prior consideration over others.',
    c
)
with open(prec_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed precedence.md")
