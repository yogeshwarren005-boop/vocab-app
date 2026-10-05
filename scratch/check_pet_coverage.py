# -*- coding: utf-8 -*-
import sqlite3, sys
sys.stdout.reconfigure(encoding="utf-8")

words = ['appetence', 'appetency', 'appetent', 'appetiser', 'appetising', 'appetisingness', 'appetite', 'appetitive', 'appetizer', 'appetizing', 'appetizingness', 'centripetal', 'compete', 'competence', 'competency', 'competent', 'competently', 'competition', 'competitive', 'competitively', 'competitiveness', 'competitor', 'competitory', 'impetiginous', 'impetigo', 'impetuosity', 'impetuous', 'impetuously', 'impetuousness', 'impetus', 'incompetence', 'incompetency', 'incompetent', 'incompetently', 'noncompetitive', 'noncompetitively', 'nonrepetitive', 'perpetrate', 'perpetration', 'perpetrator', 'perpetual', 'perpetually', 'perpetuate', 'perpetuation', 'perpetuity', 'pet', 'petabit', 'petabyte', 'petal', 'petal-like', 'petaled', 'petalled', 'petalless', 'petallike', 'petaloid', 'petalous', 'petard', 'petasites', 'petaurista', 'petauristidae', 'petaurus', 'petchary', 'petcock', 'petechia', 'peter', 'peterburg', 'petersburg', 'petiole', 'petiolule', 'petite', 'petiteness', 'petitio', 'petition', 'petitionary', 'petitioner', 'petrarca', 'petrarch', 'petrel', 'petrifaction', 'petrification', 'petrify', 'petrifying', 'petrissage', 'petrochemical', 'petrocoptis', 'petrogale', 'petroglyph', 'petrograd', 'petrol', 'petrolatum', 'petroleum', 'petrology', 'petromyzon', 'petromyzoniformes', 'petromyzontidae', 'petronius', 'petroselinum', 'petrous', 'petter', 'petteria', 'petticoat', 'petticoated', 'pettifog', 'pettifogger', 'pettifoggery', 'pettily', 'pettiness', 'petting', 'pettish', 'pettishly', 'pettishness', 'petty', 'petulance', 'petulant', 'petulantly', 'petunia', 'repetition', 'repetitious', 'repetitiousness', 'repetitive', 'repetitively', 'repetitiveness', 'unappetising', 'unappetisingness', 'unappetizing', 'unappetizingness', 'uncompetitive']

cite_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cite_c = cite_conn.cursor()

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_c = dict_conn.cursor()

print(f"Total words: {len(words)}")

low_cites = []
for w in words:
    qw = w.replace("-", " ")
    try:
        cite_c.execute("SELECT DISTINCT sentences.author FROM sentences JOIN sentences_fts ON sentences.id = sentences_fts.rowid WHERE sentences_fts MATCH ? LIMIT 10", (f'"{qw}"',))
        authors = [r[0] for r in cite_c.fetchall()]
    except Exception as e:
        authors = []
    
    dict_c.execute("SELECT count(*) FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    d_cnt = dict_c.fetchone()[0]
    
    if len(authors) < 3:
        low_cites.append((w, len(authors), authors, d_cnt))

print(f"Words with < 3 authors: {len(low_cites)}")
for w, cnt, auths, d_cnt in low_cites:
    print(f"{w}: {cnt} authors ({auths}), {d_cnt} defs in dict")
