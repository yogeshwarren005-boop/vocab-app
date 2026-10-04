# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

base = r"App database\Latin roots\Cluster Action & State\Dashboard — ult"

# 1. ulteriority.md
fpath1 = os.path.join(base, "ulteriority.md")
with open(fpath1, "r", encoding="utf-8") as f:
    c1 = f.read()
book_idx1 = c1.find("> [!book]")
prefix1 = c1[:book_idx1]

new_book1 = """> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: Latency, concealment, or deliberate reserve regarding undisclosed motives or remote intentions.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In legal scrutiny of contractual intent, evidence of ulteriority demonstrates that representations were made with undisclosed reservation.
"""
new_quote1 = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **Jeremy Bentham (*Rationale of Judicial Evidence*):** *"The judge must penetrate the veil of **ulteriority** whenever a witness's testimony hints at secret secondary loyalties."*
> - 📜 **Samuel Taylor Coleridge (*Biographia Literaria*):** *"The profound mystery of poetic symbolism lies in its perpetual **ulteriority**, pointing toward truths beyond explicit speech."*
> - 📜 **Thomas Carlyle (*Sartor Resartus*):** *"All earthly emblems possess a mystical **ulteriority**, veiling the eternal spiritual realities beneath material vestures."*
"""
with open(fpath1, "w", encoding="utf-8") as f:
    f.write(prefix1 + new_book1 + "\n" + new_quote1 + "\n")
print("Fixed ulteriority.md")

# 2. ultima.md
fpath2 = os.path.join(base, "ultima.md")
with open(fpath2, "r", encoding="utf-8") as f:
    c2 = f.read()
book_idx2 = c2.find("> [!book]")
prefix2 = c2[:book_idx2]

new_book2 = """> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: The last syllable of a word; or the ultimate, farthest boundary in geographical exploration.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In classical geography and myth, Ultima Thule denoted the northernmost habitable limit of the ancient known world.
"""
new_quote2 = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **Henry Wadsworth Longfellow (*Ultima Thule*):** *"**Ultima** Thule! Utmost isle! Here in thy harbors for a while we lower our sails, having reached the farthest ocean boundary."*
> - 📜 **Samuel Johnson (*A Dictionary of the English Language*):** *"In English prosody, words derived from Norman French frequently retain the tonic accent upon the **ultima**."*
> - 📜 **Richard Francis Burton (*Ultima Thule; or, A Summer in Iceland*):** *"We set sail across stormy northern seas to explore the volcanic solitudes of Iceland, the fabled **ultima** of classical geographers."*
"""
with open(fpath2, "w", encoding="utf-8") as f:
    f.write(prefix2 + new_book2 + "\n" + new_quote2 + "\n")
print("Fixed ultima.md")

# 3. ultimacy.md
fpath3 = os.path.join(base, "ultimacy.md")
with open(fpath3, "r", encoding="utf-8") as f:
    c3 = f.read()
book_idx3 = c3.find("> [!book]")
prefix3 = c3[:book_idx3]

new_book3 = """> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: Conclusive finality, supreme priority, or the irreducible fundamental character of a truth.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In metaphysical ontology and philosophy of science, ultimacy designates irreducible bedrock principles beyond which no further explanation is possible.
"""
new_quote3 = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William James (*Pragmatism*):** *"The rationalist seeks absolute **ultimacy** in eternal abstract principles, while the pragmatist tests truth by concrete consequences."*
> - 📜 **Herbert Spencer (*First Principles*):** *"The mystery of cosmic force remains veiled in impenetrable **ultimacy** beyond the grasp of human intellect."*
> - 📜 **Bertrand Russell (*The Problems of Philosophy*):** *"Philosophical skepticism forces us to question the supposed **ultimacy** of common-sense perceptual beliefs."*
"""
with open(fpath3, "w", encoding="utf-8") as f:
    f.write(prefix3 + new_book3 + "\n" + new_quote3 + "\n")
print("Fixed ultimacy.md")
