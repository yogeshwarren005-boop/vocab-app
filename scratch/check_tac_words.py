import json

with open('scratch/tact_from_touch.json', 'r', encoding='utf-8') as f:
    tact = json.load(f)

tac_words = ['altace', 'antacid', 'astacidae', 'astacura', 'astacus', 'attacapa', 'attacapan', 'contact', 'cotacachi', 'intact', 'intactness', 'protactinium', 'setaceous', 'tacamahac', 'tacca', 'taccaceae', 'tacit', 'tacitly', 'taciturn', 'taciturnity', 'taciturnly', 'tacitus', 'taco', 'tacoma', 'taconite', 'tact', 'tactful', 'tactfully', 'tactfulness', 'tactic', 'tactical', 'tactically', 'tactician', 'tactics', 'tactile', 'tactility', 'tactless', 'tactlessly', 'tactlessness', 'tactual', 'tactually', 'untactful']

in_tact = [w for w in tac_words if w in tact]
not_in_tact = [w for w in tac_words if w not in tact]

print(f"In tact ({len(in_tact)}): {in_tact}")
print(f"NOT in tact ({len(not_in_tact)}): {not_in_tact}")
