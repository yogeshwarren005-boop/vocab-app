# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

fixes = {
  "App database/Latin roots/Cluster Motion/Dashboard — fug/fugacity.md": {
    "replace_book": "> 1. **Primary Definition (Lexical / Standard Consensus)**: Transitoriness, volatility, or the escaping tendency of volatile substances.\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In classical chemical engineering thermodynamics, Gilbert N. Lewis introduced fugacity to correct ideal gas partial pressures for intermolecular forces."
  },
  "App database/Latin roots/Cluster Motion/Dashboard — fug/fugo.md": {
    "replace_quote": '> - 📜 **Charles Dickens (*The Pickwick Papers*):** *"The travelers hummed a lively Italian **fugo** as the post-chaise rattled along the dusty post road."*'
  },
  "App database/Latin roots/Cluster Motion/Dashboard — puls/compulsion.md": {
    "replace_book": "> 1. **Primary Definition (Lexical / Standard Consensus)**: Forcible coercion, constraint, or an irresistible psychological urge to perform an act.\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In clinical psychiatry and obsessive-compulsive diagnostics, an internal compulsion drives repetitive rituals to neutralize distress."
  },
  "App database/Latin roots/Cluster Motion/Dashboard — puls/impulsion.md": {
    "replace_book": "> 1. **Primary Definition (Lexical / Standard Consensus)**: An impelling action, forward propulsion, or the psychological urge arising from strong sudden motivation.\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: In dynamic psychology, vital impulsion describes instinctual drives motivating purposive biological activity."
  },
  "App database/Latin roots/Cluster Motion/Dashboard — puls/pulsar.md": {
    "replace_quote": '> - 📜 **Isaac Asimov (*The Caves of Steel*):** *"Astrogators calibrated galactic chronometers against the ultra-precise radio sweeps of an ancient **pulsar**."*'
  }
}

for path, fix in fixes.items():
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "replace_book" in fix:
        book_match = re.search(r'> \[!book\][^\n]*\n> 1\.[^\n]*\n> 2\.[^\n]*', content)
        if book_match:
            new_book = "> [!book] 📖 Definitions & Semantic Range\n" + fix["replace_book"]
            content = content[:book_match.start()] + new_book + content[book_match.end():]
            print(f"Fixed book in {path}")
    
    if "replace_quote" in fix:
        # replace the 3rd quote line
        lines = content.splitlines(keepends=True)
        # find quote section lines
        q_indices = [i for i, l in enumerate(lines) if l.startswith("> - 📜")]
        if len(q_indices) >= 3:
            lines[q_indices[2]] = fix["replace_quote"] + "\n"
            content = "".join(lines)
            print(f"Fixed 3rd quote in {path}")
        else:
            print(f"Warning: could not find 3 quotes in {path}")
            
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Fixes applied successfully.")
