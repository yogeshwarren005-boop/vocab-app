import os, sys
sys.stdout.reconfigure(encoding="utf-8")

words = [
    "activeness.md", "activity.md", "actuality.md", "actuation.md",
    "exactitude.md", "inactiveness.md", "inexactitude.md", "inexactness.md",
    "interactivity.md"
]

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — act"

for w in words:
    fpath = os.path.join(base_dir, w)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    print(f"=== {w} ===")
    for i, line in enumerate(lines):
        if "> [!book]" in line:
            print("".join(lines[i:i+4]))
            break
