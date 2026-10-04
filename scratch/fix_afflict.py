with open('scratch/curate_war_b1a.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'Afflict me not with these debasements, but let me die here amidst the ruins of Philistia.'
repl = '**Afflict** me not with these debasements, but let me die here amidst the ruins of Philistia.'

text = text.replace(target, repl)

with open('scratch/curate_war_b1a.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated afflict successfully')
