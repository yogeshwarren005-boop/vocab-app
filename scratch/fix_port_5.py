# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

fixes = {
    "inopportuneness.md": "Untimeliness, awkward inconvenience, or unfortunate timing of an occurrence.",
    "opportuneness.md": "Timeliness, favorable convenience, or advantageous coincidence of circumstances.",
    "portability.md": "The capacity to be carried, moved, or transported with ease; lightweight convenience.",
    "proportionality.md": "A harmonious or balanced relationship between components; proper comparative ratio.",
    "proportionateness.md": "Proper comparative balance, harmonious symmetry, or calibrated relationship."
}

base_dir = r"App database\Latin roots\Cluster Carrying\Dashboard — port"

for fname, new_p in fixes.items():
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # replace the line > 1. **Primary Definition (Lexical / Standard Consensus)**: ...
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("> 1. **Primary Definition"):
            lines[i] = f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {new_p}"
            break
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Fixed {fname}")

print("Done fixing 5 port definitions!")
