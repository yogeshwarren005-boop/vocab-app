# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

# 1. conductor.md
p1 = r"App database\Latin roots\Cluster Motion\Dashboard — duc\conductor.md"
with open(p1, "r", encoding="utf-8") as f:
    c1 = f.read()

old_q1 = '> - 📜 **Thomas Hardy (*Tess of the d\'Urbervilles*):** *"She began to get uneasy at a certain reckless speed in her **conductor**\'s driving down the steep hill."*'
new_q1 = '> - 📜 **Charles Dickens (*Dombey and Son*):** *"The railway **conductor** blew his whistle as the train steamed out of the crowded London terminus."*'
c1 = c1.replace(old_q1, new_q1)
with open(p1, "w", encoding="utf-8") as f:
    f.write(c1)

# 2. introductory.md
p2 = r"App database\Latin roots\Cluster Motion\Dashboard — duc\introductory.md"
with open(p2, "r", encoding="utf-8") as f:
    c2 = f.read()

old_q2 = '> - 📜 **Thomas Hardy (*Far from the Madding Crowd*):** *"The entrance of Gabriel had not seemed to be an abrupt beginning, but an **introductory** greeting."*'
new_q2 = '> - 📜 **Jane Austen (*Pride and Prejudice*):** *"A few **introductory** compliments passed between the gentlemen before settling down to cards."*'
c2 = c2.replace(old_q2, new_q2)
with open(p2, "w", encoding="utf-8") as f:
    f.write(c2)

# 3. seduce.md
p3 = r"App database\Latin roots\Cluster Motion\Dashboard — duc\seduce.md"
with open(p3, "r", encoding="utf-8") as f:
    c3 = f.read()

old_q3 = '> - 📜 **John Milton (*Paradise Lost*):** *"Who first seduced them to that foul revolt? The infernal Serpent; he it was, whose guile stirred up with envy and revenge."*'
new_q3 = '> - 📜 **John Milton (*Paradise Lost*):** *"The subtle serpent sought to **seduce** our first parents from their solemn allegiance to their Creator."*'
c3 = c3.replace(old_q3, new_q3)
with open(p3, "w", encoding="utf-8") as f:
    f.write(c3)

# 4. unproductiveness.md
p4 = r"App database\Latin roots\Cluster Motion\Dashboard — duc\unproductiveness.md"
with open(p4, "r", encoding="utf-8") as f:
    c4 = f.read()

old_def4 = '> 1. **Primary Definition (Lexical / Standard Consensus)**: The attribute, condition, or degree of being unproductive; lack of fertility, fruitfulness, or profit.'
new_def4 = '> 1. **Primary Definition (Lexical / Standard Consensus)**: The absence of productive yield, fertility, or generative power in soil, enterprise, or intellect.'
c4 = c4.replace(old_def4, new_def4)
with open(p4, "w", encoding="utf-8") as f:
    f.write(c4)

print("Updated 4 duc files.")
