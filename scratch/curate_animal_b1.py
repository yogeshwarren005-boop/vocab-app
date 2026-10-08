# -*- coding: utf-8 -*-
"""
curate_animal_b1.py
Combines:
- curate_animal_b1_p1 (50 words)
- curate_animal_b1_p2 (57 words)
Total: 107 words across 9 dashboards in Cluster Animal & Plant:
  - Dashboard — corn (13 words)
  - Dashboard — herb (12 words)
  - Dashboard — porc (9 words)
  - Dashboard — taur (6 words)
  - Dashboard — vulp (5 words)
  - Dashboard — zo (5 words)
  - Dashboard — pisc (15 words)
  - Dashboard — ov (17 words)
  - Dashboard — capr (25 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.append(".")

from scratch.curate_animal_b1_p1 import data_animal_b1_p1
from scratch.curate_animal_b1_p2 import data_animal_b1_p2

data_animal_b1 = {}
data_animal_b1.update(data_animal_b1_p1)
data_animal_b1.update(data_animal_b1_p2)

if __name__ == "__main__":
    print(f"Total words in data_animal_b1: {len(data_animal_b1)}")
    # Verify all 107 words
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_animal_b1.items():
        if len(d["primary"]) < 25:
            errors.append(f"{w}: primary too short")
        if len(d["secondary"]) < 25:
            errors.append(f"{w}: secondary too short")
        if CIRCULAR.search(d["primary"]):
            errors.append(f"{w}: primary circular")
        if CIRCULAR.search(d["secondary"]):
            errors.append(f"{w}: secondary circular")
        if len(d["quotes"]) != 3:
            errors.append(f"{w}: not 3 quotes")
        authors = set(q["author"] for q in d["quotes"])
        if len(authors) != 3:
            errors.append(f"{w}: duplicate author")
        for q in d["quotes"]:
            if "**" not in q["quote"]:
                errors.append(f"{w}: quote missing bold")
    if errors:
        print(f"FAILED validation ({len(errors)} issues):")
        for e in errors:
            print("  ", e)
    else:
        print("ALL 107 words in Batch 1 PASSED local pre-audit validation!")
