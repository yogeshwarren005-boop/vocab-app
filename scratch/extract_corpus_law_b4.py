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
    pat_str = rf'\b{re.escape(target_word)}\b' if '-' not in target_word else rf'\b{re.escape(target_word.replace("-", " "))}\b'
    pattern = re.compile(pat_str, re.IGNORECASE)
    for auth, work, sent in rows:
        if auth in seen_authors:
            continue
        m = pattern.search(sent)
        if m and 35 <= len(sent) <= 400:
            bolded_sent = pattern.sub(f'**{m.group(0)}**', sent, count=1)
            seen_authors.add(auth)
            results.append({'author': auth, 'work': work, 'quote': bolded_sent})
    return results

words_merces = ['commercial', 'commercial-grade', 'commercialisation', 'commercialise', 'commercialised', 'commercialism', 'commercialization', 'commercialize', 'commercialized', 'commercially', 'mercenaria', 'mercenary', 'merciless', 'mercilessly', 'mercilessness', 'noncommercial', 'uncommercial', 'uncommercialised', 'uncommercialized', 'unmercenary']
words_sanc = ['sanctification', 'sanctified', 'sanctify', 'sanctimonious', 'sanctimoniously', 'sanctimoniousness', 'sanctimony', 'sanction', 'sanctionative', 'sanctioned', 'sanctioning', 'sanctitude', 'sanctity', 'sanctuary', 'sanctum', 'unsanctification', 'unsanctified', 'unsanctify', 'unsanctioned']
words_vic = ['advice', 'arvicola', 'convict', 'convictfish', 'conviction', 'device', 'devices', 'evict', 'eviction', 'reconvict', 'vicar', 'vicar-general', 'vicarage', 'vicarial', 'vicariate', 'vicarious', 'vicariously', 'vicarship', 'vice', 'vice versa', 'vice-', 'vice-chancellor', 'vice-presidency', 'vice-presidential', 'vice-regent', 'vicegerent', 'vicenary', 'vicennial', 'viceregal', 'vicereine', 'viceroy', 'viceroyalty', 'viceroyship', 'vicia', 'vicinal', 'vicinity', 'vicious', 'viciously', 'viciousness', 'vicissitude', 'victim', 'victimisation', 'victimise', 'victimised', 'victimiser', 'victimization', 'victimize', 'victimized', 'victimizer', 'victor', 'victoria', 'victorian', 'victoriana', 'victorious', 'victoriously', 'victory', 'victrola', 'victual', 'victualer', 'victualler', 'victuals', 'vicugna', 'vicuna']

all_words = words_merces + words_sanc + words_vic
corpus_hits = {w: search_corpus_word(w) for w in all_words}
with open('scratch/law_b4_corpus_hits.json', 'w', encoding='utf-8') as f:
    json.dump(corpus_hits, f, ensure_ascii=False, indent=2)

print('Saved hits for', len(all_words), 'words.')
for w, q in corpus_hits.items():
    if len(q) > 0:
        print(f'{w}: {len(q)} quotes ({[x["author"] for x in q]})')
