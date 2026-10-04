import sys
sys.path.append('.')
from scratch.list_failing import fails

words = list(fails.keys())
print(f"Total failing: {len(words)}")
print(words)
