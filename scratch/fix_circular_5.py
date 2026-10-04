import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")

fixes = {
    "Dashboard — torp/torpidness.md": "Sluggish numbness, physical inertness, or slow physiological responsiveness.",
    "Dashboard — unct/unctuousness.md": "An insincerely flattering, greasy demeanor, or smooth oily physical texture.",
    "Dashboard — ira/irascibility.md": "A hot temper, severe irritability, or persistent susceptibility to anger.",
    "Dashboard — joc/jocoseness.md": "A playful, jesting disposition characterized by witty remarks and good humor.",
    "Dashboard — joc/jocosity.md": "Playful good humor, or a witty sally, jest, or comic remark."
}

base_dir = r"App database\Latin roots\Cluster Action & State"

for rel_path, new_pdef in fixes.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    pattern = r"> 1\. \*\*Primary Definition \(Lexical / Standard Consensus\)\*\*: .*?\n"
    replacement = f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {new_pdef}\n"
    
    new_content, count = re.subn(pattern, replacement, content)
    if count == 1:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {rel_path}")
    else:
        print(f"Failed to match in {rel_path}")
