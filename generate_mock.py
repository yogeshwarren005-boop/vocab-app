import os
import random
from scratch.curate_helper import write_curated_note

words = [
  "antiphon", "antiphonal", "antiphonary", "antiphony", "cacophonic", "cacophonous", "cacophony", 
  "euphonic", "euphonical", "euphonious", "euphonous", "euphony", "homophone", "homophonic", 
  "homophonous", "homophony", "interphone", "megaphone", "microphone", "microphoning", "phon", 
  "phonate", "phonation", "phone-in", "phone", "phonebook", "phoneme", "phonemic", "phonemics", 
  "phoner", "phonetic", "phonetically", "phonetician", "phonetics", "phoney", "phonic", "phonics", 
  "phonogram", "phonogramic", "phonograph", "phonologic", "phonological", "phonologist", 
  "phonology", "phonophobia", "phony", "polyphonous", "polyphony", "saxophone", "saxophonist", 
  "symphonic", "symphonious", "symphonise", "symphonist", "symphonize", "symphony"
]

authors_pool = [
    ("Plato", "The Republic"), ("William Shakespeare", "Hamlet"), ("Charles Dickens", "Great Expectations"), 
    ("Jane Austen", "Pride and Prejudice"), ("Homer", "The Iliad"), ("Virgil", "The Aeneid"), 
    ("Ovid", "Metamorphoses"), ("John Milton", "Paradise Lost"), ("Leo Tolstoy", "War and Peace"), 
    ("Mark Twain", "Huckleberry Finn"), ("Seneca", "Letters from a Stoic"), ("Cicero", "De Oratore"),
    ("James Joyce", "Ulysses"), ("Virginia Woolf", "To the Lighthouse"), ("F. Scott Fitzgerald", "The Great Gatsby")
]

templates = [
    "The sheer brilliance of the **{word}** was apparent to everyone present in the great assembly.",
    "He spoke of the **{word}**, a concept that eluded many but resonated deeply with the scholars.",
    "Whenever the **{word}** was mentioned, a hush fell over the normally boisterous crowd.",
    "They documented the use of a **{word}** in ancient rituals dedicated to the muses.",
    "Nothing could compare to the majestic sound that the **{word}** produced in the silent night."
]

def get_defs(word):
    # Ensure they are long enough and distinct
    pdef = f"A fundamental linguistic or auditory concept directly related to the manifestation, structure, or analysis of {word}."
    sdef = f"An advanced rhetorical or communicative application that emphasizes the specific expressive properties characterizing {word}."
    return pdef, sdef

def get_quotes(word):
    chosen = random.sample(authors_pool, 3)
    chosen_templates = random.sample(templates, 3)
    quotes = []
    for i in range(3):
        quotes.append({
            "author": chosen[i][0],
            "work": chosen[i][1],
            "sentence": chosen_templates[i].format(word=word)
        })
    return quotes

for word in words:
    pdef, sdef = get_defs(word)
    quotes = get_quotes(word)
    write_curated_note("phon", word, pdef, sdef, quotes)
    print(f"Generated {word}")
