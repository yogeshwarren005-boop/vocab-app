# -*- coding: utf-8 -*-
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from curate_law_b2_p2a import CURATED_LAW_B2_P2A
from curate_law_b2_p2b import CURATED_LAW_B2_P2B
from validate_curate import validate_curated_dict

print(f"Part 2a words: {len(CURATED_LAW_B2_P2A)}")
print(f"Part 2b words: {len(CURATED_LAW_B2_P2B)}")

combined = {}
combined.update(CURATED_LAW_B2_P2A)
combined.update(CURATED_LAW_B2_P2B)

print(f"Total unique words in combined dictionary: {len(combined)}")

# Check against disk directories
base_dir = r"App database/Latin roots/Cluster Law"

# leg should have all 107 words
leg_dir = os.path.join(base_dir, "Dashboard — leg")
leg_words = sorted([f[:-3] for f in os.listdir(leg_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
print(f"Total leg disk words: {len(leg_words)}")

# mand should have 31 words in this batch
mand_dir = os.path.join(base_dir, "Dashboard — mand")
mand_words = sorted([f[:-3] for f in os.listdir(mand_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
mand_b2 = mand_words[:31]
print(f"Total mand B2 words: {len(mand_b2)}")

expected_words = set(leg_words + mand_b2)
print(f"Total expected words in Batch 2: {len(expected_words)}")

missing = [w for w in expected_words if w not in combined]
if missing:
    print(f"MISSING WORDS ({len(missing)}): {missing}")

extra = [w for w in combined if w not in expected_words]
if extra:
    print(f"EXTRA WORDS ({len(extra)}): {extra}")

ok = validate_curated_dict(combined, "Cluster Law Batch 2 Complete (138 words across leg and mand[:31])")
if ok and not missing and not extra:
    print("\n🎉 ALL 138 WORDS OF CLUSTER LAW BATCH 2 ARE 100% VALIDATED AND READY TO APPLY!")
else:
    print("\n❌ VALIDATION OR WORD COUNT MISMATCH ENCOUNTERED.")
    sys.exit(1)
