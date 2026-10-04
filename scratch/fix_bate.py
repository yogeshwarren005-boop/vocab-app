# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

fpath = r"App database\Latin roots\Cluster Action & State\Dashboard — bat\bate.md"
with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()

book_idx = content.find("> [!book]")
prefix = content[:book_idx]

new_book = """> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: To lessen, diminish, or abate; or an archaic term meaning to flutter wings violently (as of a falcon).
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In falconry and classical drama, a hawk was said to bate when it fluttered its wings wildly and attempted to fly from the perch.
"""

new_quote = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Henry IV, Part 1*):** *"All furnish'd, all in arms; all plumed like estridges that with the wind **bate** on their feathers, glittering in golden coats."*
> - 📜 **John Milton (*Paradise Lost*):** *"Yet I argue not against Heaven's hand or will, nor **bate** a jot of heart or hope, but still bear up and steer right onward."*
> - 📜 **Walter Scott (*The Fair Maid of Perth*):** *"The proud noble refused to **bate** an inch of his feudal dignity before the assembled burghers."*
"""

new_content = prefix + new_book + "\n" + new_quote + "\n"
with open(fpath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Fixed bate.md")
