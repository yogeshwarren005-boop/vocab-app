with open('scratch/curate_bell_part1.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '"primary": "The state or condition of being at war or actively engaged in military conflict; recognized status of a belligerent party."'
repl = '"primary": "Active engagement in declared armed hostilities; recognized international legal status of a sovereign combatant party."'

text = text.replace(target, repl)

with open('scratch/curate_bell_part1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated belligerency successfully')
