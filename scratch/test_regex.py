import re

line1 = '> - 📜 **William Shakespeare (*Hamlet*):** *"To be or not to be."*'
authMatch = re.search(r'📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)', line1)
print("Match 1:", authMatch.groups() if authMatch else None)

colonMatch = re.search(r':\*\*\s*(.+)$', line1)
print("Colon match:", colonMatch.groups() if colonMatch else None)
