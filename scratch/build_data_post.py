import json
import sys
import os

sys.path.insert(0, os.path.abspath("scratch"))

from curate_post_part1 import part1_data
from curate_post_part2 import part2_data
from curate_post_part3 import part3_data

combined = {}
combined.update(part1_data)
combined.update(part2_data)
combined.update(part3_data)

out_file = 'scratch/data_post.json'
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(combined, f, indent=2, ensure_ascii=False)

print(f"Successfully combined {len(combined)} entries into {out_file}.")
