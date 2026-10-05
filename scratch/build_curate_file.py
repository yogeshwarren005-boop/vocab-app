import json

with open("scratch/data_post.json", "r", encoding="utf-8") as f:
    dp = json.load(f)

with open("scratch/data_temp.json", "r", encoding="utf-8") as f:
    dt = json.load(f)

merged = {}
merged.update(dp)
merged.update(dt)

with open("scratch/curate_time_b4_b5.py", "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nCuration data for Cluster Time Batches 4 and 5 (post and temp, total 150 words)\n"""\n\n')
    f.write("data_time_b4_b5 = ")
    json.dump(merged, f, ensure_ascii=False, indent=2)
    f.write("\n")

print(f"Successfully generated scratch/curate_time_b4_b5.py with {len(merged)} words.")
