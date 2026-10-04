with open('scratch/curate_animal_batch3.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'Break all the spokes and fellies from her wheel, and bowl the round nave down the hill of heaven, as low as to the fiends!'
repl = 'Break all the spokes and **felloe** rims from her wheel, and bowl the round nave down the hill of heaven, as low as to the fiends!'

text = text.replace(target, repl)

with open('scratch/curate_animal_batch3.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated felloe successfully')
