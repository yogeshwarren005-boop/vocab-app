import sqlite3
import re
import json

conn = sqlite3.connect('main app/corpus/citation_corpus.db')
c = conn.cursor()

def search_corpus_word(target_word):
    term = target_word.replace('-', ' ')
    results = []
    try:
        c.execute('''
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
        ''', (f'"{term}"',))
        rows = c.fetchall()
    except Exception:
        rows = []
    
    seen_authors = set()
    pattern = re.compile(rf'\b{re.escape(target_word)}\b', re.IGNORECASE) if '-' not in target_word else re.compile(rf'\b{re.escape(target_word.replace("-", " "))}\b', re.IGNORECASE)
    for auth, work, sent in rows:
        if auth in seen_authors:
            continue
        m = pattern.search(sent)
        if m and 30 <= len(sent) <= 400:
            bolded_sent = pattern.sub(f'**{m.group(0)}**', sent, count=1)
            seen_authors.add(auth)
            results.append({'author': auth, 'work': work, 'quote': bolded_sent})
    return results

words = [
    # arbitr (18)
    'arbitrable', 'arbitrage', 'arbitrager', 'arbitrageur', 'arbitral', 'arbitrament', 'arbitrarily', 'arbitrariness', 'arbitrary', 'arbitrate', 'arbitration', 'arbitrational', 'arbitrative', 'arbitrator', 'arbitrement', 'nonarbitrable', 'nonarbitrary', 'unarbitrary',
    # crim (46)
    'crime', 'crimea', 'criminal', 'criminalisation', 'criminalise', 'criminalism', 'criminality', 'criminalization', 'criminalize', 'criminally', 'criminalness', 'criminate', 'criminative', 'criminatory', 'criminological', 'criminologist', 'criminology', 'crimson', 'crimson-magenta', 'crimson-purple', 'crimson-yellow', 'decriminalisation', 'decriminalise', 'decriminalization', 'decriminalize', 'discriminable', 'discriminate', 'discriminating', 'discrimination', 'discriminative', 'discriminator', 'discriminatory', 'encrimson', 'incriminate', 'incriminating', 'incriminatingly', 'incrimination', 'incriminatory', 'indiscriminate', 'indiscriminately', 'indiscriminating', 'recriminate', 'recrimination', 'recriminative', 'recriminatory', 'undiscriminating',
    # damn (8)
    'damn', 'damnable', 'damnably', 'damnation', 'damnatory', 'damned', 'damnify', 'damning',
    # fisc (5)
    'confiscate', 'confiscation', 'fisc', 'fiscal', 'fiscally'
]

corpus_found = {}
for w in words:
    q = search_corpus_word(w)
    if q:
        corpus_found[w] = q

print(f"Words with corpus quotes: {len(corpus_found)} / {len(words)}")
with open('scratch/law_b1_corpus_quotes.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_found, f, ensure_ascii=False, indent=2)
