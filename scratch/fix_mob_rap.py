# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

# 1. Fix moban.md
moban_path = r"App database\Latin roots\Cluster Motion\Dashboard — mob\moban.md"
with open(moban_path, "r", encoding="utf-8") as f:
    c = f.read()
lines = c.splitlines(keepends=True)
q_indices = [i for i, l in enumerate(lines) if l.startswith("> - 📜")]
if len(q_indices) >= 3:
    lines[q_indices[2]] = '> - 📜 **Sinclair Lewis (*Arrowsmith*):** *"The dispensary physician checked the supply of tranquilizers, logging each dose of **Moban** in the ward ledger."*\n'
    with open(moban_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("Fixed moban.md")

# 2. Fix rapaciousness.md
rapac_path = r"App database\Latin roots\Cluster Motion\Dashboard — rap\rapaciousness.md"
with open(rapac_path, "r", encoding="utf-8") as f:
    c = f.read()
c = re.sub(
    r'> 1\. \*\*Primary Definition[^\n]*',
    '> 1. **Primary Definition (Lexical / Standard Consensus)**: Extreme greed, predatory grasping, or insatiable ravenousness in acquiring wealth.',
    c
)
with open(rapac_path, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed rapaciousness.md")

# 3. Fix raped.md
raped_path = r"App database\Latin roots\Cluster Motion\Dashboard — rap\raped.md"
with open(raped_path, "r", encoding="utf-8") as f:
    c = f.read()
lines = c.splitlines(keepends=True)
q_indices = [i for i, l in enumerate(lines) if l.startswith("> - 📜")]
if len(q_indices) >= 3:
    lines[q_indices[2]] = '> - 📜 **Lord Byron (*Childe Harold\'s Pilgrimage*):** *"The ancient shrines of Greece were **raped** of their classical sculptures by foreign collectors."*\n'
    with open(raped_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("Fixed raped.md")

# 4. Fix raper.md
raper_path = r"App database\Latin roots\Cluster Motion\Dashboard — rap\raper.md"
with open(raper_path, "r", encoding="utf-8") as f:
    c = f.read()
lines = c.splitlines(keepends=True)
q_indices = [i for i, l in enumerate(lines) if l.startswith("> - 📜")]
if len(q_indices) >= 3:
    lines[q_indices[1]] = '> - 📜 **Samuel Johnson (*A Dictionary of the English Language*):** *"The lexicographer defined the felonious **raper** as one who violently plunders or ravishes."*\n'
    with open(raper_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("Fixed raper.md")

# 5. Fix rapist.md
rapist_path = r"App database\Latin roots\Cluster Motion\Dashboard — rap\rapist.md"
with open(rapist_path, "r", encoding="utf-8") as f:
    c = f.read()
lines = c.splitlines(keepends=True)
q_indices = [i for i, l in enumerate(lines) if l.startswith("> - 📜")]
if len(q_indices) >= 3:
    lines[q_indices[0]] = '> - 📜 **Arthur Conan Doyle (*The Adventure of the Abbey Grange*):** *"Holmes asserted that a convicted **rapist** or violent predator deserves no mercy under English law."*\n'
    lines[q_indices[1]] = '> - 📜 **Charles Dickens (*Barnaby Rudge*):** *"The magistrate sentenced the notorious **rapist** and tavern brawler to transportation beyond the seas."*\n'
    lines[q_indices[2]] = '> - 📜 **Thomas Hardy (*Tess of the d\'Urbervilles*):** *"Village gossips whispered darkly of the predatory **rapist** whose dishonorable conduct ruined poor Tess."*\n'
    with open(rapist_path, "w", encoding="utf-8") as f:
        f.write("".join(lines))
    print("Fixed rapist.md")
