# -*- coding: utf-8 -*-
"""
Assembles and writes scratch/curate_fire_cal_p2.py containing all 80 curated entries.
"""
import sys
import json

sys.path.append('scratch')
from build_chunk2 import part2_words
from build_chunk3 import part3_words
from build_chunk4 import part4_words

with open('scratch/curate_fire_cal_p2.py', 'r', encoding='utf-8') as f:
    text = f.read()

loc = {}
exec(text, {}, loc)
part1_words = loc['data_fire_cal_p2']

target_words = ['calibration', 'calibre', 'caliche', 'caliche-topped', 'calico', 'calicular', 'caliculus', 'calid', 'calidris', 'calif', 'calif.', 'california', 'californian', 'californium', 'caliginous', 'caligula', 'caliper', 'caliph', 'caliphate', 'calisaya', 'calisthenic', 'calisthenics', 'call', 'call-back', 'call-board', 'call-in', 'call-out', 'calla', 'callable', 'callas', 'callathump', 'callback', 'caller', 'caller-out', 'caller-up', 'calliandra', 'callicebus', 'calligraph', 'calligrapher', 'calligraphic', 'calligraphical', 'calligraphist', 'calligraphy', 'callimorpha', 'callinectes', 'calling', 'callionymidae', 'calliope', 'calliophis', 'calliopsis', 'calliper', 'calliphora', 'calliphoridae', 'callipygian', 'callipygous', 'callirhoe', 'callisaurus', 'callistephus', 'callisthenics', 'callisto', 'callithricidae', 'callithrix', 'callithump', 'callithumpian', 'callitrichaceae', 'callitriche', 'callitris', 'callophis', 'callorhinus', 'callosectomy', 'callosity', 'callosotomy', 'callous', 'calloused', 'callously', 'callousness', 'callow', 'callowness', 'calluna', 'callus']

all_data = {}
all_data.update(part1_words)
all_data.update(part2_words)
all_data.update(part3_words)
all_data.update(part4_words)

out_lines = [
    '# -*- coding: utf-8 -*-',
    '"""',
    'Curated definitions and authentic quotations for Dashboard — cal Part 2 (80 words).',
    'Words: calibration to callus.',
    '"""',
    'import sys',
    '',
    'sys.stdout.reconfigure(encoding="utf-8")',
    '',
    'data_fire_cal_p2 = {'
]

for w in target_words:
    entry = all_data[w]
    prim = entry["primary"].replace('"', '\\"')
    sec = entry["secondary"].replace('"', '\\"')
    out_lines.append(f'    "{w}": {{')
    out_lines.append(f'        "primary": "{prim}",')
    out_lines.append(f'        "secondary": "{sec}",')
    out_lines.append('        "quotes": [')
    for q in entry["quotes"]:
        author = q["author"].replace('"', '\\"')
        work = q["work"].replace('"', '\\"')
        quote = q["quote"].replace('"', '\\"')
        out_lines.append(f'            {{"author": "{author}", "work": "{work}", "quote": "{quote}"}},')
    out_lines.append('        ]')
    out_lines.append('    },')

out_lines.append('}')
out_lines.append('')

full_code = '\n'.join(out_lines)

with open('scratch/curate_fire_cal_p2.py', 'w', encoding='utf-8') as f:
    f.write(full_code)

print("Successfully wrote full scratch/curate_fire_cal_p2.py with 80 words.")
