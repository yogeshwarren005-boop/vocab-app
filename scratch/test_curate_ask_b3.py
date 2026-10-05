# -*- coding: utf-8 -*-
import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("scratch"))

from scratch.validator import validate_entry
from scratch.curate_ask_b3 import data_ask_b3

expected_words = ['appetence', 'appetency', 'appetent', 'appetiser', 'appetising', 'appetisingness', 'appetite', 'appetitive', 'appetizer', 'appetizing', 'appetizingness', 'centripetal', 'compete', 'competence', 'competency', 'competent', 'competently', 'competition', 'competitive', 'competitively', 'competitiveness', 'competitor', 'competitory', 'impetiginous', 'impetigo', 'impetuosity', 'impetuous', 'impetuously', 'impetuousness', 'impetus', 'incompetence', 'incompetency', 'incompetent', 'incompetently', 'noncompetitive', 'noncompetitively', 'nonrepetitive', 'perpetrate', 'perpetration', 'perpetrator', 'perpetual', 'perpetually', 'perpetuate', 'perpetuation', 'perpetuity', 'pet', 'petabit', 'petabyte', 'petal', 'petal-like', 'petaled', 'petalled', 'petalless', 'petallike', 'petaloid', 'petalous', 'petard', 'petasites', 'petaurista', 'petauristidae', 'petaurus', 'petchary', 'petcock', 'petechia', 'peter', 'peterburg', 'petersburg', 'petiole', 'petiolule', 'petite', 'petiteness', 'petitio', 'petition', 'petitionary', 'petitioner', 'petrarca', 'petrarch', 'petrel', 'petrifaction', 'petrification', 'petrify', 'petrifying', 'petrissage', 'petrochemical', 'petrocoptis', 'petrogale', 'petroglyph', 'petrograd', 'petrol', 'petrolatum', 'petroleum', 'petrology', 'petromyzon', 'petromyzoniformes', 'petromyzontidae', 'petronius', 'petroselinum', 'petrous', 'petter', 'petteria', 'petticoat', 'petticoated', 'pettifog', 'pettifogger', 'pettifoggery', 'pettily', 'pettiness', 'petting', 'pettish', 'pettishly', 'pettishness', 'petty', 'petulance', 'petulant', 'petulantly', 'petunia', 'repetition', 'repetitious', 'repetitiousness', 'repetitive', 'repetitively', 'repetitiveness', 'unappetising', 'unappetisingness', 'unappetizing', 'unappetizingness', 'uncompetitive']

print(f"Checking {len(expected_words)} words...")
missing = [w for w in expected_words if w not in data_ask_b3]
if missing:
    print(f"Missing words: {missing}")
    sys.exit(1)

total_issues = 0
for w in expected_words:
    issues = validate_entry(w, data_ask_b3[w])
    if issues:
        total_issues += len(issues)
        print(f"Issues in {w}:")
        for i in issues:
            print(f"  - {i}")

if total_issues == 0:
    print("ALL 127 ENTRIES IN data_ask_b3 PASSED VALIDATION PERFECTLY!")
else:
    print(f"Found {total_issues} issues.")
    sys.exit(1)
