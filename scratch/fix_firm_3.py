import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")

fixes = {
    "Dashboard — firm/affirmativeness.md": "A positive, assertive disposition characterized by confident agreement and moral assurance.",
    "Dashboard — firm/confirmation.md": "Corroborating proof, formal validation, or an ecclesiastical sacramental rite of Christian initiation.",
    "Dashboard — firm/firmness.md": "Solid structural stability, physical resistance to pressure, or resolute moral fortitude."
}

base_dir = r"App database\Latin roots\Cluster Action & State"

for rel_path, new_pdef in fixes.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    pattern = r"> 1\. \*\*Primary Definition \(Lexical / Standard Consensus\)\*\*: .*?\n"
    replacement = f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {new_pdef}\n"
    content, _ = re.subn(pattern, replacement, content)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {rel_path}")
