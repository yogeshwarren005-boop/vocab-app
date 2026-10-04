# -*- coding: utf-8 -*-
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

base = "App database/Latin roots/Cluster Emotion"

fixes = {
  "Dashboard — furi/furiousness.md": {
    "target": "The characteristic condition of being furious; intense rage, violent tempestuousness, or turbulence.",
    "repl": "An extreme condition of wild rage, tempestuous anger, or violent turbulence."
  },
  "Dashboard — furi/infuriation.md": {
    "target": "The condition of being infuriated, or the process of driving someone into extreme anger or frenzy.",
    "repl": "Extreme anger, wrath, or acute exasperation provoked by provocative treatment."
  },
  "Dashboard — miser/miserableness.md": {
    "target": "The state, quality, or condition of being miserable; wretchedness, squalor, or unhappiness.",
    "repl": "Extreme wretchedness, severe squalor, or profound desolation of spirit."
  },
  "Dashboard — miser/misery.md": {
    "target": 'Misery acquaints a man with strange bedfellows;',
    "repl": '**Misery** acquaints a man with strange bedfellows;'
  },
  "Dashboard — sever/perseverance.md": {
    "target": 'Perseverance, dear my lord, keeps honor bright;',
    "repl": '**Perseverance**, dear my lord, keeps honor bright;'
  },
  "Dashboard — sever/severeness.md": {
    "target": "The quality or state of being severe; harshness, sternness, or intense rigor.",
    "repl": "A harsh, stern, or rigorous demeanor characterized by strict adherence to discipline."
  },
  "Dashboard — sever/severity.md": {
    "target": "The fact or condition of being severe; harshness, sternness, rigor, or extreme intensity.",
    "repl": "Extreme harshness, uncompromising sternness, rigor, or acute intensity."
  }
}

for rel_path, change in fixes.items():
    fpath = os.path.join(base, rel_path)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    if change["target"] not in content:
        print(f"Target not found in {rel_path}!")
    else:
        new_content = content.replace(change["target"], change["repl"])
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Fixed {rel_path}")

dashes = [
  "Dashboard — furi",
  "Dashboard — miser",
  "Dashboard — sever"
]

for d in dashes:
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base}/{d}"], capture_output=True, encoding="utf-8")
    if "Audit Verdict: ✅ 100% PRISTINE (PASS)" in res.stdout:
        print(f"✅ {d}: PASS")
    else:
        print(f"❌ {d}: FAIL")
        print(res.stdout)
