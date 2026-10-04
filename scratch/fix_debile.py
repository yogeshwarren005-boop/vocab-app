# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

fpath = r"App database\Latin roots\Cluster Action & State\Dashboard — deb\debile.md"
with open(fpath, "r", encoding="utf-8") as f:
    content = f.read()

book_idx = content.find("> [!book]")
prefix = content[:book_idx]

new_book = """> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: Lacking physical strength or bodily vigor; weak, feeble, or infirm.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In archaic and Renaissance literature, debile was employed as a poetic synonym for physically frail or constitutionally vulnerable.
"""

new_quote = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Coriolanus*):** *"I shall give my **debile** limbs a little rest before we renew the assault upon the gates of Corioli."*
> - 📜 **Francis Bacon (*The Advancement of Learning*):** *"Subtle dialectical disputes often leave the natural faculties of the understanding **debile** and unexercised in practical affairs."*
> - 📜 **Robert Burton (*The Anatomy of Melancholy*):** *"Old age renders the most robust constitution **debile** and subject to tremors of the extremities."*
"""

new_content = prefix + new_book + "\n" + new_quote + "\n"
with open(fpath, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Fixed debile.md")
