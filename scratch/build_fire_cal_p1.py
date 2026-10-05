# -*- coding: utf-8 -*-
"""
Combines batches A, B, C, D into scratch/curate_fire_cal_p1.py
"""
import sys, os

sys.stdout.reconfigure(encoding="utf-8")

from scratch.batch_a import batch_a
from scratch.batch_b import batch_b
from scratch.batch_c import batch_c
from scratch.batch_d import batch_d

all_words = {**batch_a, **batch_b, **batch_c, **batch_d}

expected_words = [
    'alcalescent', 'calaba', 'calabash', 'calabazilla', 'calabria', 'calabura', 'caladenia', 'caladium', 'calais', 'calamagrostis',
    'calamari', 'calamary', 'calamine', 'calamint', 'calamintha', 'calamitous', 'calamity', 'calamus', 'calan', 'calando',
    'calandrinia', 'calanthe', 'calapooya', 'calapuya', 'calash', 'calc-tufa', 'calcaneal', 'calcaneus', 'calcareous', 'calced',
    'calcedony', 'calceiform', 'calceolaria', 'calceolate', 'calceus', 'calcic', 'calcicolous', 'calciferol', 'calciferous', 'calcific',
    'calcification', 'calcifugous', 'calcify', 'calcimine', 'calcination', 'calcine', 'calcite', 'calcitic', 'calcitonin', 'calcium',
    'calcium-cyanamide', 'calculable', 'calculate', 'calculated', 'calculating', 'calculatingly', 'calculation', 'calculative', 'calculator', 'calculous',
    'calculus', 'calcutta', 'calcuttan', 'calean', 'caleche', 'caledonia', 'calefacient', 'calefaction', 'calefactive', 'calefactory',
    'calendar', 'calender', 'calendered', 'calendric', 'calendrical', 'calendula', 'cali', 'caliber', 'calibrate', 'calibrated'
]

print(f"Total curated: {len(all_words)}")
missing = [w for w in expected_words if w not in all_words]
print(f"Missing: {missing}")

# Serialize to scratch/curate_fire_cal_p1.py
with open("scratch/curate_fire_cal_p1.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nCurated definitions and authentic quotations for Dashboard — cal Part 1 (80 words).\n"""\n')
    f.write("import sys\n\nsys.stdout.reconfigure(encoding='utf-8')\n\n")
    f.write("data_fire_cal_p1 = {\n")
    for w in expected_words:
        entry = all_words[w]
        f.write(f'  "{w}": {{\n')
        prim = entry["primary"].replace('"', '\\"')
        sec = entry["secondary"].replace('"', '\\"')
        f.write(f'    "primary": "{prim}",\n')
        f.write(f'    "secondary": "{sec}",\n')
        f.write('    "quotes": [\n')
        for q in entry["quotes"]:
            auth = q["author"].replace('"', '\\"')
            work = q["work"].replace('"', '\\"')
            quote = q["quote"].replace('"', '\\"')
            f.write(f'      {{"author": "{auth}", "work": "{work}", "quote": "{quote}"}},\n')
        f.write('    ]\n')
        f.write('  },\n')
    f.write("}\n")

print("Generated scratch/curate_fire_cal_p1.py successfully!")
