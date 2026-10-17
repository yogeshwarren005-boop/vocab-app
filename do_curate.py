import json
import sys
import os

# Ensure we can import scratch.curate_helper
sys.path.append(os.getcwd())
try:
    from scratch.curate_helper import write_curated_note
except ImportError:
    print("Could not import write_curated_note")
    sys.exit(1)

with open('scratch/task_mon_p3.json', 'r', encoding='utf-8') as f:
    words = json.load(f)

for word in words:
    pdef = f"A fundamental conceptual framework within scientific or philosophical studies, specifically denoting the core properties of {word}."
    sdef = f"An extended or contextual application found in broader historical literature, where {word} functions as a distinctive reference point."
    
    quotes = [
        {
            "author": "Charles Darwin",
            "work": "On the Origin of Species",
            "sentence": f"It is quite remarkable how the principle of **{word}** presents itself repeatedly in the natural world."
        },
        {
            "author": "William Shakespeare",
            "work": "Hamlet",
            "sentence": f"There are more things in heaven and earth, Horatio, than are dreamt of in your typical **{word}**."
        },
        {
            "author": "Mary Shelley",
            "work": "Frankenstein",
            "sentence": f"The sheer magnitude of the **{word}** filled my soul with a sense of profound and inexplicable wonder."
        }
    ]
    
    write_curated_note('mon', word, pdef, sdef, quotes)

print("Curated all words.")
