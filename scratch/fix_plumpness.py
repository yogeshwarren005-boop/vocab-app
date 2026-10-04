with open('scratch/curate_animal_batch2.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '"primary": "The state or condition of being pleasantly fat, rounded, full, or fleshy in physical form."'
replacement = '"primary": "Pleasing roundness, fullness, or fleshiness of physical form and contour."'

text = text.replace(target, replacement)

with open('scratch/curate_animal_batch2.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated curate_animal_batch2.py successfully')
