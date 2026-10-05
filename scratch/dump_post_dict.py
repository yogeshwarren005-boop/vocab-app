import sqlite3
import json

WORDS = [
    'compost', 'expostulate', 'expostulation', 'impost', 'imposter', 'impostor', 'imposture',
    'post', 'postage', 'postal', 'postcard', 'postcava', 'postcode', 'posted', 'poster',
    'posterboard', 'posterior', 'posteriority', 'posterity', 'postern', 'postexilic',
    'postgraduate', 'posthumous', 'posthumously', 'postiche', 'postictal', 'postilion',
    'postillion', 'postimpressionist', 'postindustrial', 'posting', 'postlude', 'postman',
    'postmark', 'postmaster', 'postmenopausal', 'postmeridian', 'postmillennial', 'postmistress',
    'postmodern', 'postmodernism', 'postmodernist', 'postmortal', 'postmortem', 'postnatal',
    'postnuptial', 'postoperative', 'postoperatively', 'postpone', 'postponement', 'postponer',
    'postscript', 'postulant', 'postulate', 'postulation', 'postulational', 'postulator',
    'postum', 'postural', 'posture', 'posturer', 'posturing', 'preposterous', 'preposterously'
]

conn = sqlite3.connect('main app/corpus/local_dictionary.db')
cur = conn.cursor()

dict_data = {}
for w in WORDS:
    cur.execute("SELECT source, sense_number, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    rows = cur.fetchall()
    dict_data[w] = rows

with open('scratch/post_local_dict_dump.json', 'w', encoding='utf-8') as f:
    json.dump(dict_data, f, indent=2, ensure_ascii=False)

print(f"Dumped dictionary entries for {len(dict_data)} words.")
for w in WORDS:
    senses = dict_data[w]
    print(f"{w}: {len(senses)} senses (sources: {[s[0] for s in senses]})")
