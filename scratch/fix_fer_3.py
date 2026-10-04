# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

fixes = {
  "Dashboard — fer/difference.md": "A point or respect in which things are not identical; dissimilarity, distinction, or the degree of variation separating two entities.",
  "Dashboard — fer/fertility.md": "The natural capability to produce abundant offspring, crops, vegetation, or ideas; fecundity and fruitfulness.",
  "Dashboard — fer/inferiority.md": "A lower degree of rank, excellence, status, or value relative to an established standard or competitor."
}

base_dir = r"App database\Latin roots\Cluster Carrying"

for rel_path, new_p_def in fixes.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if line.startswith("> 1. **Primary Definition"):
            lines[i] = f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {new_p_def}\n"
            break
            
    with open(fpath, "w", encoding="utf-8") as f:
        f.writelines(lines)
    print(f"Updated {rel_path}")

print("Fixed 3 files.")
