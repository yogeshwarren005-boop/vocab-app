# -*- coding: utf-8 -*-
import os

base_action = r"App database\Latin roots\Cluster Action"
fac_dir = os.path.join(base_action, "Dashboard — fac")
fac_files = set(f for f in os.listdir(fac_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage'))

dashboards = ["Dashboard — fact", "Dashboard — fict", "Dashboard — fec"]

grafted = 0
for d in dashboards:
    d_dir = os.path.join(base_action, d)
    if not os.path.exists(d_dir): continue
    files = set(f for f in os.listdir(d_dir) if f.endswith('.md'))
    common = fac_files.intersection(files)
    for fname in common:
        src_path = os.path.join(d_dir, fname)
        tgt_path = os.path.join(fac_dir, fname)
        with open(src_path, "r", encoding="utf-8") as f:
            src_c = f.read()
        b_idx_src = src_c.find("> [!book]")
        if b_idx_src == -1: continue
        tail = src_c[b_idx_src:]
        
        with open(tgt_path, "r", encoding="utf-8") as f:
            tgt_c = f.read()
        b_idx_tgt = tgt_c.find("> [!book]")
        if b_idx_tgt == -1: continue
        head = tgt_c[:b_idx_tgt]
        
        with open(tgt_path, "w", encoding="utf-8") as f:
            f.write(head + tail)
        grafted += 1

print(f"Successfully grafted {grafted} shared notes into Dashboard — fac.")
