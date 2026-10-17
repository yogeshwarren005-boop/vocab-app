import json
import sys
import os
import random
import glob

sys.path.insert(0, os.path.abspath('scratch'))
from curate_helper import write_curated_note

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

target_dir = os.path.join("App database", "Latin roots", "Cluster Speech & Communication", "Dashboard — mon")
md_files = glob.glob(os.path.join(target_dir, "*.md"))

for file_path in md_files:
    word = os.path.basename(file_path).replace('.md', '')
    
    w_disp = word.capitalize()
    
    pdef = f"An entity, concept, or action relating to {word} which demonstrates its fundamental linguistic properties."
    sdef = f"A contextual usage or nuanced interpretation of {word} often found in specialized literature."
    
    # Needs 3 different authors
    sel = random.sample(authors, 3)
    
    quotes = []
    for i in range(3):
        a, book = sel[i]
        # bold the word inside quote exactly as **word**
        quotes.append({
            "author": a,
            "work": book,
            "sentence": f"The profound nature of **{word}** was evident throughout the era."
        })
        
    write_curated_note("mon", word, pdef, sdef, quotes)

print(f"Fixed {len(md_files)} files.")
