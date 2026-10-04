with open('scratch/curate_war_milit.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '"primary": "The state or condition of being militant; active, combative, or aggressive support of a cause or viewpoint."'
repl = '"primary": "Active, combative, or aggressive support of a cause or viewpoint through direct action."'

text = text.replace(target, repl)

with open('scratch/curate_war_milit.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated militancy successfully')
