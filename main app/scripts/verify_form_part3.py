import json, os, re

base = r"App database\Greek roots\Cluster Form & Space"
with open(r"main app\scripts\slice-form-part3.json", "r", encoding="utf-8") as f:
    slice_data = json.load(f)

errors = 0
for rel in slice_data:
    fp = os.path.join(base, rel)
    with open(fp, "r", encoding="utf-8") as fp_in:
        c = fp_in.read()
    if "> 1. **Primary Definition" not in c:
        errors += 1
        print("Missing def 1:", rel)
    if "> 2. **Secondary / Nuanced Definition" not in c:
        errors += 1
        print("Missing def 2:", rel)
    quotes = len(re.findall(r"> - 📜 \*\*[^*]+\(\*[^*]+\*\):\*\* \*\"[^\"]+\"\*", c))
    if quotes < 3:
        errors += 1
        print(f"Missing quotes ({quotes}): {rel}")

print(f"Checked {len(slice_data)} notes in Form Part 3. Total errors: {errors}")
