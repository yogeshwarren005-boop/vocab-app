# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

p_ven = r"App database\Latin roots\Cluster Motion\Dashboard — ven"
p_vent = r"App database\Latin roots\Cluster Motion\Dashboard — vent"

ven_files = sorted([f for f in os.listdir(p_ven) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])
vent_files = sorted([f for f in os.listdir(p_vent) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])

common = set(ven_files).intersection(set(vent_files))
only_ven = [f for f in ven_files if f not in common]

print(f"Total in ven: {len(ven_files)}")
print(f"Total in vent: {len(vent_files)}")
print(f"Common files (in both ven and vent): {len(common)}")
print(f"Only in ven: {len(only_ven)}")
print("\nFirst 30 words only in ven:")
print([f[:-3] for f in only_ven[:30]])
