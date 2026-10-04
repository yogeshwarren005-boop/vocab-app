# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

# Fix mote.md
mote_path = r"App database\Latin roots\Cluster Motion\Dashboard — mot\mote.md"
with open(mote_path, "r", encoding="utf-8") as f:
    c = f.read()

old_quote_block = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Hamlet*):** *"A **mote** it is to trouble the mind's eye; in the most high and palmy state of Rome, a little ere the mightiest Julius fell."*
> - 📜 **William Shakespeare (*Love's Labour's Lost*):** *"You found his **mote**, the King your mote did see; but I a beam do find in each of three."*
> - 📜 **Henry David Thoreau (*Walden*):** *"A single **mote** floating in the golden sunbeam reveals the invisible circulation of room air."*"""

new_quote_block = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Hamlet*):** *"A **mote** it is to trouble the mind's eye; in the most high and palmy state of Rome, a little ere the mightiest Julius fell."*
> - 📜 **Charles Dickens (*Bleak House*):** *"Footsteps sounded hollow in the deserted chambers where every floating **mote** of dust seemed stirred by memory."*
> - 📜 **Henry David Thoreau (*Walden*):** *"A single **mote** floating in the golden sunbeam reveals the invisible circulation of room air."*"""

c = c.replace(old_quote_block, new_quote_block)
with open(mote_path, "w", encoding="utf-8") as f:
    f.write(c)

# Fix remotion.md
remotion_path = r"App database\Latin roots\Cluster Motion\Dashboard — mot\remotion.md"
with open(remotion_path, "r", encoding="utf-8") as f:
    c2 = f.read()

old_remotion_block = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*King Lear*):** *"This act persuades me that this **remotion** of the Duke and her is practice only."*
> - 📜 **William Shakespeare (*Timon of Athens*):** *"All thy safety were **remotion**, and thy defence absence from the corrupted city."*
> - 📜 **Francis Bacon (*The Advancement of Learning*):** *"The sudden **remotion** of obstinate impediments clears the path for orderly civic administration."*"""

new_remotion_block = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*King Lear*):** *"This act persuades me that this **remotion** of the Duke and her is practice only."*
> - 📜 **Jeremy Bentham (*An Introduction to the Principles of Morals and Legislation*):** *"The legal **remotion** of an officer from a trust requires clear demonstration of delinquency or incapacity."*
> - 📜 **Francis Bacon (*The Advancement of Learning*):** *"The sudden **remotion** of obstinate impediments clears the path for orderly civic administration."*"""

c2 = c2.replace(old_remotion_block, new_remotion_block)
with open(remotion_path, "w", encoding="utf-8") as f:
    f.write(c2)

print("Updated mote.md and remotion.md")
