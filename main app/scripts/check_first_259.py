import json, os, re

base_dir = r"App database\Greek roots\Cluster Form & Space"
slice_file = r"main app\scripts\slice-form-part4.json"

with open(slice_file, "r", encoding="utf-8") as f:
    all_files = json.load(f)

first_259 = all_files[:259]
errors = []

for rel in first_259:
    path = os.path.join(base_dir, rel)
    if not os.path.exists(path):
        errors.append(f"Missing file: {rel}")
        continue
    content = open(path, "r", encoding="utf-8").read()
    if "Academic Lexicon" in content:
        errors.append(f"Placeholder author in: {rel}")
    quotes = re.findall(r"> \d+\. \*\*\"", content)
    if len(quotes) != 3:
        errors.append(f"Expected 3 quotes, got {len(quotes)} in: {rel}")

print(f"Checked first 259 files. Errors found: {len(errors)}")
for err in errors[:20]:
    print(" ", err)
