# -*- coding: utf-8 -*-
import sqlite3
import json

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

lig_words = ['alligator', 'alligatored', 'alligatorfish', 'alligatoridae', 'colligate', 'colligation', 'coreligionist', 'diligence', 'diligent', 'diligently', 'disoblige', 'disobliging', 'eligibility', 'eligible', 'ineligibility', 'ineligible', 'irreligion', 'irreligionist', 'irreligious', 'irreligiousness', 'ligament', 'ligan', 'ligand', 'ligate', 'ligation', 'ligature', 'liger', 'ligne', 'ligneous', 'lignify', 'lignin', 'lignite', 'lignosae', 'lignum', 'ligularia', 'ligule', 'liguria', 'ligustrum', 'nonobligatory', 'obligate', 'obligated', 'obligation', 'obligational', 'obligato', 'obligatorily', 'obligatory', 'oblige', 'obliged', 'obliger', 'obliging', 'obligingly', 'obligingness', 'oligarch', 'oligarchic', 'oligarchical', 'oligarchy', 'religion', 'religionism', 'religionist', 'religiosity', 'religious', 'religiousism', 'religiously', 'religiousness', 'unobligated', 'unobliging']
strict_words = ['constrict', 'constricted', 'constricting', 'constriction', 'constrictive', 'constrictor', 'derestrict', 'district', 'nonrestrictive', 'restrict', 'restricted', 'restricting', 'restriction', 'restrictive', 'restrictively', 'restrictiveness', 'strict', 'strictly', 'strictness', 'stricture', 'unconstricted', 'unrestricted', 'unrestrictive']
string_words = ['astringe', 'astringence', 'astringency', 'astringent', 'constringe', 'nonastringent', 'string', 'stringency', 'stringent', 'stringently', 'stringer', 'strings', 'stringy', 'stringybark', 'substring', 'superstring', 'unstring']

all_words = sorted(list(set(lig_words + strict_words + string_words)))

print(f"Total target words: {len(all_words)}")

res = {}
missing_quotes = []

for w in all_words:
    d_cur.execute("SELECT definition FROM dictionary_entries WHERE word = ?", (w,))
    defs = [r[0] for r in d_cur.fetchall()]
    
    # check quotes
    try:
        c_cur.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
        """, (f'"{w}"',))
        quotes = c_cur.fetchall()
    except Exception as e:
        quotes = []
        
    authors = list(set(q[0] for q in quotes if q[0]))
    res[w] = {
        "defs": defs,
        "quotes_count": len(quotes),
        "unique_authors": len(authors),
        "authors": authors
    }
    if len(authors) < 3:
        missing_quotes.append((w, len(authors)))

print(f"Words with < 3 unique authors in corpus: {len(missing_quotes)}")
for w, c in missing_quotes:
    print(f"  {w}: {c} authors")

c_conn.close()
d_conn.close()
