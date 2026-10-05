# -*- coding: utf-8 -*-
import sys
import re

sys.path.append('scratch')
from build_chunk2 import part2_words
from build_chunk3 import part3_words
from build_chunk4 import part4_words

with open('scratch/curate_fire_cal_p2.py', 'r', encoding='utf-8') as f:
    text = f.read()

loc = {}
exec(text, {}, loc)
part1_words = loc['data_fire_cal_p2']

all_data = {}
all_data.update(part1_words)
all_data.update(part2_words)
all_data.update(part3_words)
all_data.update(part4_words)

target_words = ['calibration', 'calibre', 'caliche', 'caliche-topped', 'calico', 'calicular', 'caliculus', 'calid', 'calidris', 'calif', 'calif.', 'california', 'californian', 'californium', 'caliginous', 'caligula', 'caliper', 'caliph', 'caliphate', 'calisaya', 'calisthenic', 'calisthenics', 'call', 'call-back', 'call-board', 'call-in', 'call-out', 'calla', 'callable', 'callas', 'callathump', 'callback', 'caller', 'caller-out', 'caller-up', 'calliandra', 'callicebus', 'calligraph', 'calligrapher', 'calligraphic', 'calligraphical', 'calligraphist', 'calligraphy', 'callimorpha', 'callinectes', 'calling', 'callionymidae', 'calliope', 'calliophis', 'calliopsis', 'calliper', 'calliphora', 'calliphoridae', 'callipygian', 'callipygous', 'callirhoe', 'callisaurus', 'callistephus', 'callisthenics', 'callisto', 'callithricidae', 'callithrix', 'callithump', 'callithumpian', 'callitrichaceae', 'callitriche', 'callitris', 'callophis', 'callorhinus', 'callosectomy', 'callosity', 'callosotomy', 'callous', 'calloused', 'callously', 'callousness', 'callow', 'callowness', 'calluna', 'callus']

errors = []

for w in target_words:
    entry = all_data[w]
    prim = entry.get('primary', '')
    sec = entry.get('secondary', '')
    quotes = entry.get('quotes', [])
    
    if len(prim) < 25:
        errors.append(f'{w}: primary < 25 chars ({len(prim)})')
    if len(sec) < 25:
        errors.append(f'{w}: secondary < 25 chars ({len(sec)})')
        
    for pat in [r'\bquality of being\b', r'\bstate of being\b', r'\bcondition of being\b']:
        if re.search(pat, prim, re.IGNORECASE):
            errors.append(f'{w}: primary contains circular formula: {re.findall(pat, prim, re.IGNORECASE)}')
            
    if len(quotes) != 3:
        errors.append(f'{w}: quotes count != 3 ({len(quotes)})')
        
    authors = [q.get('author', '').strip() for q in quotes]
    if len(set(authors)) != 3:
        errors.append(f'{w}: authors not 3 distinct ({authors})')
        
    for i, q in enumerate(quotes):
        txt = q.get('quote', '')
        bolds = re.findall(r'\*\*([^*]+)\*\*', txt)
        if not bolds:
            errors.append(f'{w} quote {i}: no bolded word found in "{txt}"')
        if 'In academic literature' in txt or 'Academic Lexicon' in txt:
            errors.append(f'{w} quote {i}: synthetic boilerplate detected')

print(f'Checked {len(target_words)} words.')
print(f'Total errors: {len(errors)}')
for e in errors:
    print('  ERROR:', e)
