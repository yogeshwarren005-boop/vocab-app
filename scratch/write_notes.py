import json
import sys
import os
sys.path.append('c:/Users/user/Desktop/Vocab app')
from scratch.curate_helper import write_curated_note

with open('c:/Users/user/Desktop/Vocab app/scratch/generated_dic.json', 'r') as f:
    data = json.load(f)

for word, content in data.items():
    write_curated_note('dic', word, content['pdef'], content['sdef'], content['quotes'])

print("Notes written.")
