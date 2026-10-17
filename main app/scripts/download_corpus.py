# -*- coding: utf-8 -*-
"""
Downloads a curated collection of foundational literary, scientific, and philosophical texts
from Project Gutenberg to form our local Ground-Truth Citation Corpus.
"""
import os
import urllib.request
import time

TEXTS = [
    # Natural Science & Biology
    {"id": 1228, "author": "Charles Darwin", "work": "The Origin of Species"},
    {"id": 2300, "author": "Charles Darwin", "work": "The Descent of Man"},
    {"id": 3698, "author": "Thomas Henry Huxley", "work": "Evolution and Ethics"},
    
    # Philosophy & Social Science
    {"id": 10604, "author": "John Locke", "work": "An Essay Concerning Human Understanding"},
    {"id": 3300, "author": "Adam Smith", "work": "The Wealth of Nations"},
    {"id": 34901, "author": "John Stuart Mill", "work": "On Liberty"},
    {"id": 11224, "author": "John Stuart Mill", "work": "Utilitarianism"},
    {"id": 2434, "author": "Francis Bacon", "work": "The Essays"},
    {"id": 5649, "author": "William James", "work": "Pragmatism"},
    {"id": 16643, "author": "Ralph Waldo Emerson", "work": "Essays"},
    {"id": 205, "author": "Henry David Thoreau", "work": "Walden"},
    
    # Victorian & Classical Fiction
    {"id": 1400, "author": "Charles Dickens", "work": "Great Expectations"},
    {"id": 98, "author": "Charles Dickens", "work": "A Tale of Two Cities"},
    {"id": 766, "author": "Charles Dickens", "work": "David Copperfield"},
    {"id": 145, "author": "George Eliot", "work": "Middlemarch"},
    {"id": 550, "author": "George Eliot", "work": "Silas Marner"},
    {"id": 110, "author": "Thomas Hardy", "work": "Tess of the d'Urbervilles"},
    {"id": 107, "author": "Thomas Hardy", "work": "Far from the Madding Crowd"},
    {"id": 84, "author": "Mary Shelley", "work": "Frankenstein"},
    {"id": 345, "author": "Bram Stoker", "work": "Dracula"},
    {"id": 1661, "author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes"},
    {"id": 829, "author": "Jonathan Swift", "work": "Gulliver's Travels"},
    {"id": 33, "author": "Nathaniel Hawthorne", "work": "The Scarlet Letter"},
    {"id": 174, "author": "Oscar Wilde", "work": "The Picture of Dorian Gray"},
    {"id": 2814, "author": "James Joyce", "work": "Dubliners"},
    {"id": 219, "author": "Joseph Conrad", "work": "Heart of Darkness"},
    {"id": 35, "author": "H. G. Wells", "work": "The Time Machine"},
    {"id": 36, "author": "H. G. Wells", "work": "The War of the Worlds"},
    {"id": 11, "author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland"},
    {"id": 2701, "author": "Herman Melville", "work": "Moby-Dick"},
    {"id": 100, "author": "William Shakespeare", "work": "The Complete Works of William Shakespeare"}
]

out_dir = os.path.join("main app", "corpus")
os.makedirs(out_dir, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

downloaded = 0
for item in TEXTS:
    fname = f"{item['id']}_{item['author'].replace(' ', '_')}.txt"
    fpath = os.path.join(out_dir, fname)
    if os.path.exists(fpath) and os.path.getsize(fpath) > 1000:
        continue
    
    url = f"https://www.gutenberg.org/cache/epub/{item['id']}/pg{item['id']}.txt"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp:
            content = resp.read()
            with open(fpath, "wb") as f:
                f.write(content)
            downloaded += 1
            print(f"[{downloaded}/{len(TEXTS)}] Downloaded: {item['author']} - {item['work']} ({len(content)//1024} KB)")
        time.sleep(0.5)
    except Exception as e:
        print(f"Failed {item['author']} - {item['work']} ({item['id']}): {e}")

print(f"Finished. Total downloaded: {downloaded}. Total in corpus: {len(os.listdir(out_dir))}")
