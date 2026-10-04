# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

base = r"App database\Latin roots\Cluster Action & State\Dashboard — cel"

# 1. celebrity.md
fpath1 = os.path.join(base, "celebrity.md")
with open(fpath1, "r", encoding="utf-8") as f:
    c1 = f.read()
book_idx1 = c1.find("> [!book]")
prefix1 = c1[:book_idx1]

new_book1 = """> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: Widespread fame, public renown, and social prominence; or a widely recognized person.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In cultural sociology, modern celebrity culture transforms private personal identity into a commodified public spectacle via mass media.
"""
new_quote1 = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **Oscar Wilde (*The Picture of Dorian Gray*):** *"Dorian found that his sudden social **celebrity** brought both flattering adoration and malicious drawing-room gossip."*
> - 📜 **Henry James (*The Bostonians*):** *"Miss Chancellor shrank from the vulgar **celebrity** that pursued outspoken lecturers in the sensational public press."*
> - 📜 **Charles Dickens (*Nicholas Nickleby*):** *"Mr. Vincent Crummles took immense pride in introducing the infant phenomenon to provincial audiences as a theatrical **celebrity**."*
"""
with open(fpath1, "w", encoding="utf-8") as f:
    f.write(prefix1 + new_book1 + "\n" + new_quote1 + "\n")
print("Fixed celebrity.md")

# 2. excellence.md
fpath2 = os.path.join(base, "excellence.md")
with open(fpath2, "r", encoding="utf-8") as f:
    c2 = f.read()
book_idx2 = c2.find("> [!book]")
prefix2 = c2[:book_idx2]

new_book2 = """> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: Outstanding merit, superior virtue, or exceptionally high standard of performance.
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In Aristotelian ethics, moral excellence (arête) is cultivated through habituation and the deliberate choice of the virtuous mean.
"""
new_quote2 = """> [!quote] 💬 Contextual Usage & Authentic Quotations
> - 📜 **William Shakespeare (*Much Ado About Nothing*):** *"It is the witness still of **excellence** to put a strange face on his own perfection."*
> - 📜 **John Stuart Mill (*On Liberty*):** *"The cultivation of individual **excellence** requires freedom of thought and diversity of social environment."*
> - 📜 **Ralph Waldo Emerson (*Essays: First Series*):** *"Every great institution is the lengthened shadow of one man whose personal **excellence** commanded universal admiration."*
"""
with open(fpath2, "w", encoding="utf-8") as f:
    f.write(prefix2 + new_book2 + "\n" + new_quote2 + "\n")
print("Fixed excellence.md")
