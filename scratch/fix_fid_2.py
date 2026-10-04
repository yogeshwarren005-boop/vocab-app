# -*- coding: utf-8 -*-
import os, sys

sys.stdout.reconfigure(encoding="utf-8")

fixes = {
  "Dashboard — fid/infidelity.md": "Unfaithfulness or disloyalty to a spouse, partner, or sworn moral commitment; or the rejection of a religious faith.",
  "Dashboard — fid/perfidy.md": "Deceitfulness, treacherous betrayal of a sworn trust, or deliberate violation of solemn faith."
}

base_dir = r"App database\Latin roots\Cluster Faith"

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

print("Fixed 2 files.")
