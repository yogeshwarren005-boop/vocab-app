import os, sys

sys.stdout.reconfigure(encoding="utf-8")

# Map of target file path -> source file path
grafts = [
    # Dashboard — celer (13 words from Cluster Action & State / Dashboard — cel)
    ("App database/Latin roots/Cluster Movement & Speed/Dashboard — celer", "App database/Latin roots/Cluster Action & State/Dashboard — cel"),
    # Dashboard — fluct (4 words from Cluster Motion / Dashboard — flu)
    ("App database/Latin roots/Cluster Movement & Speed/Dashboard — fluct", "App database/Latin roots/Cluster Motion/Dashboard — flu")
]

total_grafted = 0

for target_dir, source_dir in grafts:
    target_files = [f for f in os.listdir(target_dir) if f.endswith(".md") and not f.startswith(("Dashboard", "Word Triage"))]
    for fname in target_files:
        src_path = os.path.join(source_dir, fname)
        tgt_path = os.path.join(target_dir, fname)
        if not os.path.exists(src_path):
            print(f"Source not found: {src_path}")
            continue
        
        with open(src_path, "r", encoding="utf-8") as sf:
            src_content = sf.read()
        
        with open(tgt_path, "r", encoding="utf-8") as tf:
            tgt_content = tf.read()
            
        src_book_idx = src_content.find("> [!book]")
        tgt_book_idx = tgt_content.find("> [!book]")
        
        if src_book_idx == -1 or tgt_book_idx == -1:
            print(f"Skipping {fname}: book callout not found")
            continue
            
        tgt_prefix = tgt_content[:tgt_book_idx]
        src_suffix = src_content[src_book_idx:]
        
        new_content = tgt_prefix + src_suffix
        
        with open(tgt_path, "w", encoding="utf-8") as tf:
            tf.write(new_content)
        total_grafted += 1

print(f"Successfully grafted {total_grafted} notes.")
