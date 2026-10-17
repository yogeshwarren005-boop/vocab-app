import json
import os
import sys

# Ensure scratch is in path
sys.path.append(os.path.abspath("scratch"))
from curate_helper import write_curated_note

def main():
    all_data = []
    for i in range(1, 6):
        part_file = f"scratch/part_{i}.json"
        if not os.path.exists(part_file):
            print(f"Missing {part_file}")
            continue
        
        with open(part_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            all_data.extend(data)
    
    print(f"Loaded {len(all_data)} words.")
    
    dashboard_root = "mon"
    for item in all_data:
        word = item["word"]
        pdef = item["pdef"]
        sdef = item["sdef"]
        quotes = item["quotes"]
        
        write_curated_note(dashboard_root, word, pdef, sdef, quotes)
        print(f"Processed: {word}")

if __name__ == "__main__":
    main()
