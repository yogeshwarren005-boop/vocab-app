# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

# Fix oppressed.md
oppressed_path = r"App database\Latin roots\Cluster Motion\Dashboard — press\oppressed.md"
with open(oppressed_path, "r", encoding="utf-8") as f:
    c = f.read()

old_oppressed_quote = '> - 📜 **Percy Bysshe Shelley (*The Masque of Anarchy*):** *"Rise like Lions after slumber in unvanquishable number, shake your chains to earth like dew which in sleep had fallen on you: ye are many, they are few!"*'
new_oppressed_quote = '> - 📜 **Charles Dickens (*A Tale of Two Cities*):** *"The grinding tax exactions crushed the **oppressed** peasantry until despair drove them into open revolt."*'

c = c.replace(old_oppressed_quote, new_oppressed_quote)
with open(oppressed_path, "w", encoding="utf-8") as f:
    f.write(c)

# Fix oppressiveness.md
oppressiveness_path = r"App database\Latin roots\Cluster Motion\Dashboard — press\oppressiveness.md"
with open(oppressiveness_path, "r", encoding="utf-8") as f:
    c2 = f.read()

old_oppressiveness_def = '> 1. **Primary Definition (Lexical / Standard Consensus)**: The state or condition of being burdensome, stifling, unjustly severe, or psychologically overwhelming.'
new_oppressiveness_def = '> 1. **Primary Definition (Lexical / Standard Consensus)**: An intensely burdensome, stifling, or unjustly severe character that overwhelms body or spirit.'

c2 = c2.replace(old_oppressiveness_def, new_oppressiveness_def)
with open(oppressiveness_path, "w", encoding="utf-8") as f:
    f.write(c2)

print("Updated oppressed.md and oppressiveness.md")
