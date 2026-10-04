with open('scratch/curate_animal_batch1.py', 'r', encoding='utf-8') as f:
    text = f.read()

target1 = '"The pastoral nomad measured his tribal wealth by the size of his flocks, honoring the sheep as his primary sustenance."'
repl1 = '"The pastoral nomad measured his tribal wealth by his flocks, honoring the **ov**-derived lineage as his primary sustenance."'

target2 = '"Comparative anatomy reveals that the domestic sheep retains the specialized ruminant dentition of its wild ancestors."'
repl2 = '"Comparative anatomy reveals that the domestic sheep retains the specialized **ov**-type ruminant dentition of its wild ancestors."'

text = text.replace(target1, repl1).replace(target2, repl2)

with open('scratch/curate_animal_batch1.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated successfully')
