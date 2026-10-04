import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")

fixes = {
    "Dashboard — lax/laxness.md": "Slackness, looseness, or a marked deficiency in strict discipline.",
    "Dashboard — lax/relaxation.md": "Release from tension, mental anxiety, or physical strain; rest and recreation.",
    "Dashboard — solut/irresoluteness.md": "Chronic indecision, vacillation of will, or lack of firm purpose.",
    "Dashboard — solut/resoluteness.md": "Firm determination, unwavering purpose, and moral constancy.",
    "Dashboard — ars/coarseness.md": "Roughness of texture, vulgarity of manners, or deficiency in delicacy."
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
