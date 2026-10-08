# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, 'scratch')
from corpus_helper import get_corpus_and_dict_data

words = json.load(open('scratch/quantity_b1b_words.json', encoding='utf-8'))
data = get_corpus_and_dict_data(words)

with open('scratch/quantity_b1b_corpus_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

with_quotes = [w for w, v in data.items() if len(v["quotes"]) >= 3]
partial_quotes = [w for w, v in data.items() if 0 < len(v["quotes"]) < 3]
no_quotes = [w for w, v in data.items() if len(v["quotes"]) == 0]
print(f"Total words in Quantity Batch 1B: {len(words)}")
print(f"Words with >=3 authors: {len(with_quotes)}")
print(f"Words with 1-2 authors: {len(partial_quotes)}")
print(f"Words with 0 authors: {len(no_quotes)}")
