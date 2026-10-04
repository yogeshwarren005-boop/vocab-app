import os, sys

sys.stdout.reconfigure(encoding="utf-8")

motion_flu_dir = r"App database\Latin roots\Cluster Motion\Dashboard — flu"
speed_fluct_dir = r"App database\Latin roots\Cluster Movement & Speed\Dashboard — fluct"
speed_flux_dir = r"App database\Latin roots\Cluster Movement & Speed\Dashboard — flux"

if os.path.exists(motion_flu_dir):
    flu_words = {f for f in os.listdir(motion_flu_dir) if f.endswith(".md") and not f.startswith("Dashboard — ")}
    print(f"Motion flu words: {len(flu_words)}")
    
    if os.path.exists(speed_fluct_dir):
        fluct_words = {f for f in os.listdir(speed_fluct_dir) if f.endswith(".md") and not f.startswith("Dashboard — ")}
        print(f"Speed fluct words: {len(fluct_words)}")
        print("Overlap with flu:", flu_words.intersection(fluct_words))
        
    if os.path.exists(speed_flux_dir):
        flux_words = {f for f in os.listdir(speed_flux_dir) if f.endswith(".md") and not f.startswith("Dashboard — ")}
        print(f"Speed flux words: {len(flux_words)}")
        print("Overlap with flu:", flu_words.intersection(flux_words))
