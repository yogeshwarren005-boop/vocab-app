# -*- coding: utf-8 -*-
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from curate_good_bad_b3_p1a import CURATED_GOOD_BAD_B3_P1A
from curate_good_bad_b3_p1b import CURATED_GOOD_BAD_B3_P1B
from curate_good_bad_b3_p2a import CURATED_GOOD_BAD_B3_P2A
from curate_good_bad_b3_p2b import CURATED_GOOD_BAD_B3_P2B
from validate_curate import validate_curated_dict

print(f"Part 1a words: {len(CURATED_GOOD_BAD_B3_P1A)}")
print(f"Part 1b words: {len(CURATED_GOOD_BAD_B3_P1B)}")
print(f"Part 2a words: {len(CURATED_GOOD_BAD_B3_P2A)}")
print(f"Part 2b words: {len(CURATED_GOOD_BAD_B3_P2B)}")

combined = {}
combined.update(CURATED_GOOD_BAD_B3_P1A)
combined.update(CURATED_GOOD_BAD_B3_P1B)
combined.update(CURATED_GOOD_BAD_B3_P2A)
combined.update(CURATED_GOOD_BAD_B3_P2B)

print(f"Total unique words in combined dictionary: {len(combined)}")

# Check against disk directory
dp = 'App database/Latin roots/Cluster Good & Bad/Dashboard — mal'
disk_words = sorted([f[:-3] for f in os.listdir(dp) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
print(f"Disk words in Dashboard — mal: {len(disk_words)}")

missing = [w for w in disk_words if w not in combined]
extra = [w for w in combined if w not in disk_words]

if missing:
    print(f"MISSING WORDS ({len(missing)}): {missing}")
if extra:
    print(f"EXTRA WORDS ({len(extra)}): {extra}")

ok = validate_curated_dict(combined, "Cluster Good & Bad Batch 3 Complete (155 words across mal)")
if ok and not missing and not extra:
    print("\n🎉 ALL 155 WORDS OF BATCH 3 (mal) ARE 100% VALIDATED AND READY TO APPLY!")
else:
    print("\n❌ VALIDATION OR WORD COUNT MISMATCH ENCOUNTERED.")
    sys.exit(1)
