import sys
sys.stdout.reconfigure(encoding='utf-8')

from validate_curate import validate_curated_dict
from curate_sending_b4_p4a import CURATED_SENDING_B4_P4A
from curate_sending_b4_p4b import CURATED_SENDING_B4_P4B

combined = {}
combined.update(CURATED_SENDING_B4_P4A)
combined.update(CURATED_SENDING_B4_P4B)

print(f"Total words in Batch 4: {len(combined)}")

errors = validate_curated_dict(combined)
if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)
else:
    print("Batch 4 validation PASSED! All definitions and quotes are compliant.")
