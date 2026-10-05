import json

with open('scratch/post_local_dict_dump.json', 'r', encoding='utf-8') as f:
    dict_data = json.load(f)

for w, rows in dict_data.items():
    print(f"=== {w} ===")
    for r in rows:
        print(f"  [{r[0]}:{r[1]}] {r[2][:150]}")
