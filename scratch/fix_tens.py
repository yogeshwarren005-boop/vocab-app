# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

fixes = {
  "distension.md": "Enlargement, swelling, or outward expansion resulting from internal fluid or gas pressure.",
  "extension.md": "An elongation, enlargement, or additional part joined to an existing structure or timeline.",
  "intensity.md": "Extreme strength, concentrated energy, depth of emotion, or high magnitude in a physical property.",
  "intensiveness.md": "Thoroughness, concentration of effort, or depth of application across an activity or process.",
  "tenseness.md": "Rigid physical tightness, emotional strain, or nervous apprehension in a person or situation.",
  "tension.md": "A pulling mechanical force exerted along a cable, or acute emotional strain between conflicting forces."
}

base = r"App database\Latin roots\Cluster Motion\Dashboard — tens"
for fname, new_p in fixes.items():
    p = os.path.join(base, fname)
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    c = re.sub(
        r'> 1\. \*\*Primary Definition[^\n]*',
        f'> 1. **Primary Definition (Lexical / Standard Consensus)**: {new_p}',
        c
    )
    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Fixed {fname}")

print("Tens fixes applied.")
