# -*- coding: utf-8 -*-
import sqlite3
import re

c_conn = sqlite3.connect("main app/corpus/citation_corpus.db")
c_cur = c_conn.cursor()

d_conn = sqlite3.connect("main app/corpus/local_dictionary.db")
d_cur = d_conn.cursor()

lig_words = ['alligator', 'alligatored', 'alligatorfish', 'alligatoridae', 'colligate', 'colligation', 'coreligionist', 'diligence', 'diligent', 'diligently', 'disoblige', 'disobliging', 'eligibility', 'eligible', 'ineligibility', 'ineligible', 'irreligion', 'irreligionist', 'irreligious', 'irreligiousness', 'ligament', 'ligan', 'ligand', 'ligate', 'ligation', 'ligature', 'liger', 'ligne', 'ligneous', 'lignify', 'lignin', 'lignite', 'lignosae', 'lignum', 'ligularia', 'ligule', 'liguria', 'ligustrum', 'nonobligatory', 'obligate', 'obligated', 'obligation', 'obligational', 'obligato', 'obligatorily', 'obligatory', 'oblige', 'obliged', 'obliger', 'obliging', 'obligingly', 'obligingness', 'oligarch', 'oligarchic', 'oligarchical', 'oligarchy', 'religion', 'religionism', 'religionist', 'religiosity', 'religious', 'religiousism', 'religiously', 'religiousness', 'unobligated', 'unobliging']
strict_words = ['constrict', 'constricted', 'constricting', 'constriction', 'constrictive', 'constrictor', 'derestrict', 'district', 'nonrestrictive', 'restrict', 'restricted', 'restricting', 'restriction', 'restrictive', 'restrictively', 'restrictiveness', 'strict', 'strictly', 'strictness', 'stricture', 'unconstricted', 'unrestricted', 'unrestrictive']
string_words = ['astringe', 'astringence', 'astringency', 'astringent', 'constringe', 'nonastringent', 'string', 'stringency', 'stringent', 'stringently', 'stringer', 'strings', 'stringy', 'stringybark', 'substring', 'superstring', 'unstring']

all_words = lig_words + strict_words + string_words

def bold_word(text, w):
    # Regex match case-insensitive word boundary
    pattern = re.compile(rf'\b({re.escape(w)}[a-z]*)\b', re.IGNORECASE)
    return pattern.sub(r'**\1**', text)

available_quotes = {}
for w in all_words:
    try:
        c_cur.execute("""
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 30
        """, (f'"{w}"',))
        rows = c_cur.fetchall()
    except:
        rows = []
    
    by_author = {}
    for auth, work, sent in rows:
        if not auth or not work or not sent:
            continue
        auth = auth.strip()
        work = work.strip()
        sent = sent.strip().replace('"', "'")
        if auth not in by_author and len(sent) > 20:
            by_author[auth] = {"author": auth, "work": work, "quote": bold_word(sent, w)}
    
    if len(by_author) >= 3:
        available_quotes[w] = list(by_author.values())[:3]

print(f"Words with 3+ unique author corpus quotes: {len(available_quotes)} / {len(all_words)}")
for w in sorted(available_quotes.keys()):
    auths = [q['author'] for q in available_quotes[w]]
    print(f"  {w}: {auths}")
