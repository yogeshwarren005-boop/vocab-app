with open('scratch/curate_animal_batch3.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '"primary": "The quality of being felicitous; aptness, graceful suitability, or fortunate appropriateness in expression or occurrence."'
repl = '"primary": "Aptness, graceful suitability, or fortunate appropriateness in literary phrasing or circumstance."'

text = text.replace(target, repl)

with open('scratch/curate_animal_batch3.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated felicitousness successfully')
