import os

p = r'App database/Latin roots/Cluster Thought/Dashboard — log'
files = sorted([f for f in os.listdir(p) if f.endswith('.md') and not f.startswith('Dashboard —') and not f.startswith('Word Triage —')])

words = [f[:-3] for f in files]
print("Total words:", len(words))
print("Part 1 (0:45):", words[0], "to", words[44], f"({len(words[0:45])} words)")
print("Part 2 (45:90):", words[45], "to", words[89], f"({len(words[45:90])} words)")
print("Part 3 (90:):", words[90], "to", words[-1], f"({len(words[90:])} words)")
print("\nPart 2 words:", words[45:90])
