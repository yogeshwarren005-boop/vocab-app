# -*- coding: utf-8 -*-
import os, sys
sys.stdout.reconfigure(encoding="utf-8")

p_ven = r"App database\Latin roots\Cluster Motion\Dashboard — ven"
p_vent = r"App database\Latin roots\Cluster Motion\Dashboard — vent"

ven_files = sorted([f for f in os.listdir(p_ven) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])
vent_files = sorted([f for f in os.listdir(p_vent) if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage'))])

common = set(ven_files).intersection(set(vent_files))

grafted = 0
for f in common:
    vent_path = os.path.join(p_vent, f)
    ven_path = os.path.join(p_ven, f)
    
    with open(vent_path, "r", encoding="utf-8") as file_vent:
        content_vent = file_vent.read()
    
    with open(ven_path, "r", encoding="utf-8") as file_ven:
        content_ven = file_ven.read()
        
    b_idx_vent = content_vent.find("> [!book]")
    b_idx_ven = content_ven.find("> [!book]")
    
    if b_idx_vent != -1 and b_idx_ven != -1:
        # Keep everything in ven up to > [!book], take everything from vent starting at > [!book]
        prefix_ven = content_ven[:b_idx_ven]
        body_vent = content_vent[b_idx_vent:]
        
        new_content_ven = prefix_ven + body_vent
        with open(ven_path, "w", encoding="utf-8") as file_ven:
            file_ven.write(new_content_ven)
        grafted += 1

print(f"Grafted {grafted} pristine notes from vent to ven.")
