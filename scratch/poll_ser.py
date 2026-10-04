# -*- coding: utf-8 -*-
import sqlite3, json, sys

sys.stdout.reconfigure(encoding="utf-8")

words = ['anser', 'anseres', 'anseriformes', 'anserinae', 'anserine', 'antiserum', 'assert', 'assertable', 'asserted', 'asserter', 'asserting', 'assertion', 'assertive', 'assertively', 'assertiveness', 'desert', 'deserted', 'deserter', 'desertification', 'desertion', 'deserts', 'dissertate', 'dissertation', 'exsert', 'insert', 'insertion', 'nonassertive', 'overserious', 'reassert', 'reassertion', 'seraglio', 'serail', 'serape', 'seraph', 'seraphic', 'seraphical', 'serax', 'sere', 'serenade', 'serendipitous', 'serendipity', 'serene', 'serenely', 'sereness', 'serengeti', 'serenity', 'serenoa', 'serer', 'serial', 'serialisation', 'serialise', 'serialism', 'serialization', 'serialize', 'serially', 'seriatim', 'sericeous', 'sericocarpus', 'sericterium', 'serictery', 'sericultural', 'sericulture', 'sericulturist', 'seriema', 'series', 'serif', 'serigraph', 'serigraphy', 'serin', 'serine', 'serinus', 'seriocomedy', 'seriocomic', 'seriocomical', 'seriola', 'serious', 'serious-minded', 'serious-mindedness', 'seriously', 'seriousness', 'seriph', 'seriphidium', 'seriphus', 'sermon', 'sermonise', 'sermoniser', 'sermonize', 'sermonizer', 'serologic', 'serological', 'serologist', 'serology', 'serosa', 'serotine', 'serotonin', 'serous', 'serow', 'serra', 'serranid', 'serranidae', 'serranus', 'serrasalmus', 'serrate', 'serrated', 'serratia', 'serration', 'serratula', 'serratus', 'serried', 'serrulate', 'sertraline', 'sertularia', 'sertularian', 'serum', 'unassertive', 'unassertively', 'unassertiveness']

cite_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cite_cur = cite_conn.cursor()
dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_cur = dict_conn.cursor()

results = {}
for w in words:
    dict_cur.execute('SELECT definition FROM dictionary_entries WHERE word = ? ORDER BY sense_number', (w,))
    defs = [r[0] for r in dict_cur.fetchall()]
    
    cites = []
    q_term = f'"{w}"'
    try:
        cite_cur.execute('''
            SELECT s.author, s.work, s.sentence
            FROM sentences_fts f
            JOIN sentences s ON f.rowid = s.id
            WHERE sentences_fts MATCH ?
            LIMIT 25
        ''', (q_term,))
        cites = cite_cur.fetchall()
    except Exception as e:
        try:
            clean = w.replace('-', ' ')
            cite_cur.execute('''
                SELECT s.author, s.work, s.sentence
                FROM sentences_fts f
                JOIN sentences s ON f.rowid = s.id
                WHERE sentences_fts MATCH ?
                LIMIT 25
            ''', (f'"{clean}"',))
            cites = cite_cur.fetchall()
        except Exception:
            pass

    results[w] = {
        'defs': defs,
        'cites': cites
    }

print(f'Polled {len(words)} words.')
few_authors = []
for w, data in results.items():
    authors = set(c[0] for c in data['cites'])
    if len(authors) < 3:
        few_authors.append((w, len(authors), len(data['cites'])))

print(f'{len(few_authors)} words have fewer than 3 distinct authors in citation corpus:')
for w, a_cnt, c_cnt in few_authors:
    print(f'  {w}: {a_cnt} authors, {c_cnt} cites')

with open('scratch/ser_poll.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
