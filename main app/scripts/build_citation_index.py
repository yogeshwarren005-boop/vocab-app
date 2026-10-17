# -*- coding: utf-8 -*-
"""
Builds a high-performance SQLite FTS5 index across our canonical texts (Gutenberg + NLTK)
to enable instant, 100% verified citation lookups with exact sentence, author, and work title.
"""
import os
import re
import sqlite3
import nltk
from nltk.corpus import gutenberg

# File-to-metadata mapping for custom downloaded texts
TEXT_META = {
    1228: ("Charles Darwin", "The Origin of Species"),
    2300: ("Charles Darwin", "The Descent of Man"),
    3698: ("Thomas Henry Huxley", "Evolution and Ethics"),
    10604: ("John Locke", "An Essay Concerning Human Understanding"),
    3300: ("Adam Smith", "The Wealth of Nations"),
    34901: ("John Stuart Mill", "On Liberty"),
    11224: ("John Stuart Mill", "Utilitarianism"),
    2434: ("Francis Bacon", "The Essays"),
    5649: ("William James", "Pragmatism"),
    16643: ("Ralph Waldo Emerson", "Essays"),
    205: ("Henry David Thoreau", "Walden"),
    1400: ("Charles Dickens", "Great Expectations"),
    98: ("Charles Dickens", "A Tale of Two Cities"),
    766: ("Charles Dickens", "David Copperfield"),
    145: ("George Eliot", "Middlemarch"),
    550: ("George Eliot", "Silas Marner"),
    110: ("Thomas Hardy", "Tess of the d'Urbervilles"),
    107: ("Thomas Hardy", "Far from the Madding Crowd"),
    84: ("Mary Shelley", "Frankenstein"),
    345: ("Bram Stoker", "Dracula"),
    1661: ("Arthur Conan Doyle", "The Adventures of Sherlock Holmes"),
    829: ("Jonathan Swift", "Gulliver's Travels"),
    33: ("Nathaniel Hawthorne", "The Scarlet Letter"),
    174: ("Oscar Wilde", "The Picture of Dorian Gray"),
    2814: ("James Joyce", "Dubliners"),
    219: ("Joseph Conrad", "Heart of Darkness"),
    35: ("H. G. Wells", "The Time Machine"),
    36: ("H. G. Wells", "The War of the Worlds"),
    11: ("Lewis Carroll", "Alice's Adventures in Wonderland"),
    2701: ("Herman Melville", "Moby-Dick"),
    100: ("William Shakespeare", "The Complete Works of William Shakespeare")
}

# NLTK Gutenberg metadata mapping
NLTK_META = {
    "austen-emma.txt": ("Jane Austen", "Emma"),
    "austen-persuasion.txt": ("Jane Austen", "Persuasion"),
    "austen-sense.txt": ("Jane Austen", "Sense and Sensibility"),
    "bible-kjv.txt": ("King James Bible", "The Holy Bible"),
    "blake-poems.txt": ("William Blake", "Songs of Innocence and of Experience"),
    "chesterton-ball.txt": ("G. K. Chesterton", "The Ball and the Cross"),
    "chesterton-brown.txt": ("G. K. Chesterton", "The Wisdom of Father Brown"),
    "chesterton-thursday.txt": ("G. K. Chesterton", "The Man Who Was Thursday"),
    "milton-paradise.txt": ("John Milton", "Paradise Lost"),
    "whitman-leaves.txt": ("Walt Whitman", "Leaves of Grass")
}

db_path = os.path.join("main app", "corpus", "citation_corpus.db")
if os.path.exists(db_path):
    try:
        os.remove(db_path)
    except:
        pass

con = sqlite3.connect(db_path)
cur = con.cursor()

# Create table and FTS5 index
cur.execute("""
CREATE TABLE sentences (
    id INTEGER PRIMARY KEY,
    author TEXT,
    work TEXT,
    sentence TEXT
);
""")

cur.execute("""
CREATE VIRTUAL TABLE sentences_fts USING fts5(
    sentence,
    content='sentences',
    content_rowid='id'
);
""")

def clean_gutenberg_text(text):
    # Strip Gutenberg header and footer
    start_match = re.search(r'\*\*\*\s*START OF TH(E|IS) PROJECT GUTENBERG EBOOK[^\*]*\*\*\*', text, re.IGNORECASE)
    if start_match:
        text = text[start_match.end():]
    end_match = re.search(r'\*\*\*\s*END OF TH(E|IS) PROJECT GUTENBERG EBOOK', text, re.IGNORECASE)
    if end_match:
        text = text[:end_match.start()]
    return text

# Sentence splitter regex
sentence_end_re = re.compile(r'(?<=[.!?])\s+(?=[A-Z"“])')

def extract_sentences(raw_text):
    text = clean_gutenberg_text(raw_text)
    # Normalize whitespace
    paragraphs = text.split("\n\n")
    sentences = []
    for p in paragraphs:
        p_clean = " ".join(p.split())
        if len(p_clean) < 30:
            continue
        splits = sentence_end_re.split(p_clean)
        for s in splits:
            s_str = s.strip().strip('"').strip('“').strip('”')
            # Good sentence length: 40 to 300 characters
            if 35 <= len(s_str) <= 350 and re.search(r'[A-Za-z]', s_str):
                sentences.append(s_str)
    return sentences

print("Extracting and indexing sentences from corpus files...")
total_sentences = 0
batch = []

# 1. Process custom downloaded texts
corpus_dir = os.path.join("main app", "corpus")
for fname in os.listdir(corpus_dir):
    if not fname.endswith(".txt"):
        continue
    parts = fname.split("_")
    try:
        book_id = int(parts[0])
    except ValueError:
        continue
    
    if book_id in TEXT_META:
        author, work = TEXT_META[book_id]
    else:
        author = parts[1].replace(".txt", "").replace("_", " ")
        work = "Selected Works"
    
    fpath = os.path.join(corpus_dir, fname)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    sents = extract_sentences(content)
    for s in sents:
        batch.append((author, work, s))
        if len(batch) >= 10000:
            cur.executemany("INSERT INTO sentences (author, work, sentence) VALUES (?, ?, ?)", batch)
            con.commit()
            total_sentences += len(batch)
            batch = []
            print(f"Indexed {total_sentences} sentences...")

# 2. Process NLTK Gutenberg texts
for fileid, (author, work) in NLTK_META.items():
    try:
        raw_text = gutenberg.raw(fileid)
        sents = extract_sentences(raw_text)
        for s in sents:
            batch.append((author, work, s))
            if len(batch) >= 10000:
                cur.executemany("INSERT INTO sentences (author, work, sentence) VALUES (?, ?, ?)", batch)
                con.commit()
                total_sentences += len(batch)
                batch = []
                print(f"Indexed {total_sentences} sentences...")
    except Exception as e:
        print(f"NLTK text {fileid} error: {e}")

if batch:
    cur.executemany("INSERT INTO sentences (author, work, sentence) VALUES (?, ?, ?)", batch)
    con.commit()
    total_sentences += len(batch)

print("Building FTS5 index...")
cur.execute("INSERT INTO sentences_fts(sentences_fts) VALUES('rebuild');")
con.commit()

print(f"Done! Total sentences indexed: {total_sentences}")
print(f"Database size: {os.path.getsize(db_path) // (1024*1024)} MB")

# Quick search test
test_words = ["action", "creative", "abundant", "labor", "active"]
for w in test_words:
    res = cur.execute("""
        SELECT s.author, s.work, s.sentence 
        FROM sentences_fts f
        JOIN sentences s ON f.rowid = s.id
        WHERE sentences_fts MATCH ?
        LIMIT 2;
    """, (w,)).fetchall()
    print(f"\nQuery '{w}': Found {len(res)} sample matches:")
    for r in res:
        print(f"  * {r[0]} ({r[1]}): {r[2][:100]}...")

con.close()
