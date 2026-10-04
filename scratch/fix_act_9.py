import os

fixes = {
    "activeness.md": "Habitual liveliness, vigor, and continuous engagement in physical or mental exertion.",
    "activity.md": "Lively movement, energetic action, or an operational enterprise undertaken by individuals or groups.",
    "actuality.md": "Concrete, observable factual existence as distinguished from theory, mere possibility, or imaginative speculation.",
    "actuation.md": "The mechanical or physical process of initiating motion, triggering an operation, or motivating behavior.",
    "exactitude.md": "Strict adherence to precision, thorough accuracy, and rigorous standards of correctness.",
    "inactiveness.md": "Dormancy, sluggish motion, or disinclination toward physical or mental exertion.",
    "inexactitude.md": "A lack of precision, rigor, or factual correctness; an inaccuracy or error.",
    "inexactness.md": "Deficiency in accuracy, geometric precision, or meticulous thoroughness.",
    "interactivity.md": "Two-way communication, reciprocal responsiveness, or continuous mutual engagement between humans, machines, or systems."
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — act"

for fname, new_pdef in fixes.items():
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace the primary definition line
    import re
    pattern = r"> 1\. \*\*Primary Definition \(Lexical / Standard Consensus\)\*\*: .*?\n"
    replacement = f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {new_pdef}\n"
    
    new_content, count = re.subn(pattern, replacement, content)
    if count == 1:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {fname}")
    else:
        print(f"Failed to match in {fname}")
