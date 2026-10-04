with open('scratch/curate_equ_part1.py', 'r', encoding='utf-8') as f:
    t1 = f.read()

# adequateness
t1 = t1.replace(
    '"primary": "The quality or state of being sufficient, suitable, or satisfactory for a given purpose; sufficiency."',
    '"primary": "Sufficiency, suitability, or satisfactory competence to meet a designated requirement."'
)

# equality
t1 = t1.replace(
    '"primary": "The state of being equal, especially in status, rights, opportunities, or value."',
    '"primary": "Identical status, rights, opportunities, or value shared among all individuals or entities."'
)

with open('scratch/curate_equ_part1.py', 'w', encoding='utf-8') as f:
    f.write(t1)

with open('scratch/curate_equ_part2.py', 'r', encoding='utf-8') as f:
    t2 = f.read()

# equity
t2 = t2.replace(
    '"primary": "The quality of being fair and impartial; justice according to natural right; the value of shares issued by a company; fairness."',
    '"primary": "Fairness, impartiality, and justice according to natural right; net value of commercial ownership interest."'
)

# equivalence
t2 = t2.replace(
    '"primary": "The condition of being equivalent or identical in value, function, meaning, importance, or quantitative force."',
    '"primary": "Identical value, function, meaning, importance, or quantitative force between corresponding entities."'
)

# inadequacy
t2 = t2.replace(
    '"primary": "The state or condition of being insufficient, inadequate, or failing to meet required standards or demands."',
    '"primary": "Insufficiency, defectiveness, or failure to satisfy required standards, capacities, or demands."'
)

# inequality
t2 = t2.replace(
    '"primary": "The condition of being unequal, especially in status, rights, opportunities, or distribution of wealth and privileges."',
    '"primary": "Disparity or unfair differentiation in status, rights, opportunities, or economic distribution."'
)

with open('scratch/curate_equ_part2.py', 'w', encoding='utf-8') as f:
    f.write(t2)

print('Updated 6 words across part1 and part2 successfully!')
