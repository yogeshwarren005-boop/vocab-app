# -*- coding: utf-8 -*-
import sqlite3, json, sys, re
sys.stdout.reconfigure(encoding="utf-8")

words = ['appetence', 'appetency', 'appetent', 'appetiser', 'appetising', 'appetisingness', 'appetite', 'appetitive', 'appetizer', 'appetizing', 'appetizingness', 'centripetal', 'compete', 'competence', 'competency', 'competent', 'competently', 'competition', 'competitive', 'competitively', 'competitiveness', 'competitor', 'competitory', 'impetiginous', 'impetigo', 'impetuosity', 'impetuous', 'impetuously', 'impetuousness', 'impetus', 'incompetence', 'incompetency', 'incompetent', 'incompetently', 'noncompetitive', 'noncompetitively', 'nonrepetitive', 'perpetrate', 'perpetration', 'perpetrator', 'perpetual', 'perpetually', 'perpetuate', 'perpetuation', 'perpetuity', 'pet', 'petabit', 'petabyte', 'petal', 'petal-like', 'petaled', 'petalled', 'petalless', 'petallike', 'petaloid', 'petalous', 'petard', 'petasites', 'petaurista', 'petauristidae', 'petaurus', 'petchary', 'petcock', 'petechia', 'peter', 'peterburg', 'petersburg', 'petiole', 'petiolule', 'petite', 'petiteness', 'petitio', 'petition', 'petitionary', 'petitioner', 'petrarca', 'petrarch', 'petrel', 'petrifaction', 'petrification', 'petrify', 'petrifying', 'petrissage', 'petrochemical', 'petrocoptis', 'petrogale', 'petroglyph', 'petrograd', 'petrol', 'petrolatum', 'petroleum', 'petrology', 'petromyzon', 'petromyzoniformes', 'petromyzontidae', 'petronius', 'petroselinum', 'petrous', 'petter', 'petteria', 'petticoat', 'petticoated', 'pettifog', 'pettifogger', 'pettifoggery', 'pettily', 'pettiness', 'petting', 'pettish', 'pettishly', 'pettishness', 'petty', 'petulance', 'petulant', 'petulantly', 'petunia', 'repetition', 'repetitious', 'repetitiousness', 'repetitive', 'repetitively', 'repetitiveness', 'unappetising', 'unappetisingness', 'unappetizing', 'unappetizingness', 'uncompetitive']

cite_conn = sqlite3.connect('main app/corpus/citation_corpus.db')
cite_c = cite_conn.cursor()

dict_conn = sqlite3.connect('main app/corpus/local_dictionary.db')
dict_c = dict_conn.cursor()

corpus_results = {}

for w in words:
    dict_c.execute("SELECT source, definition FROM dictionary_entries WHERE word = ? COLLATE NOCASE", (w,))
    defs = [{"source": r[0], "definition": r[1]} for r in dict_c.fetchall()]
    
    qw = w.replace("-", " ")
    try:
        cite_c.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences s 
            JOIN sentences_fts f ON s.id = f.rowid 
            WHERE sentences_fts MATCH ? 
            LIMIT 50
        """, (f'"{qw}"',))
        raw_cites = cite_c.fetchall()
    except Exception as e:
        raw_cites = []
        
    # Deduplicate citations by author, picking best sentence (reasonable length)
    author_quotes = {}
    for auth, work, sentence in raw_cites:
        if auth not in author_quotes:
            if 30 <= len(sentence) <= 400:
                author_quotes[auth] = {"author": auth, "work": work, "sentence": sentence}
        elif len(sentence) < len(author_quotes[auth]["sentence"]) and len(sentence) >= 40:
            author_quotes[auth] = {"author": auth, "work": work, "sentence": sentence}
            
    corpus_results[w] = {
        "definitions": defs,
        "quotes": list(author_quotes.values())
    }

with open("scratch/pet_corpus_dump.json", "w", encoding="utf-8") as f:
    json.dump(corpus_results, f, ensure_ascii=False, indent=2)

print("Saved scratch/pet_corpus_dump.json")
num_3_quotes = sum(1 for w, d in corpus_results.items() if len(d["quotes"]) >= 3)
print(f"Words with >= 3 distinct author quotes in corpus: {num_3_quotes} / {len(words)}")
