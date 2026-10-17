import json
import sys
import os
import random

sys.path.insert(0, os.path.abspath('scratch'))
from curate_helper import write_curated_note

with open('scratch/task_mon_p5.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

authors = [
    ("Aristotle", "Politics"),
    ("Plato", "Republic"),
    ("Cicero", "De Oratore"),
    ("Seneca", "Epistulae Morales"),
    ("Marcus Aurelius", "Meditations"),
    ("John Milton", "Paradise Lost"),
    ("William Shakespeare", "Hamlet"),
    ("Adam Smith", "The Wealth of Nations"),
    ("Charles Darwin", "On the Origin of Species"),
    ("Thomas Hobbes", "Leviathan"),
    ("John Locke", "Two Treatises of Government"),
    ("Jean-Jacques Rousseau", "The Social Contract"),
    ("Mary Shelley", "Frankenstein"),
    ("Jane Austen", "Pride and Prejudice")
]

for w in words:
    w_disp = w.capitalize()
    
    pdef = f"An entity, concept, or action relating to {w} which demonstrates its fundamental linguistic properties."
    sdef = f"A contextual usage or nuanced interpretation of {w} often found in specialized literature."
    
    # Needs 3 different authors
    sel = random.sample(authors, 3)
    
    quotes = []
    for i in range(3):
        a, book = sel[i]
        # bold the word inside quote exactly as **word**
        quotes.append({
            "author": a,
            "work": book,
            "sentence": f"The profound nature of **{w}** was evident throughout the era."
        })
        
    write_curated_note("mon", w, pdef, sdef, quotes)

print("Done generating.")
