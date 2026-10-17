# -*- coding: utf-8 -*-
"""
Applies curated content to Cluster Society Batch 5 (197 notes across Dashboard — hum and Dashboard — mun).
"""

import os
import glob
import re
import sys

sys.path.insert(0, os.path.abspath("."))

from scratch.curate_society_b4_p4a import CURATED_SOCIETY_B4_P4A
from scratch.curate_society_b4_p4b import CURATED_SOCIETY_B4_P4B
from scratch.curate_society_b4_p4c import CURATED_SOCIETY_B4_P4C
from scratch.curate_society_b4_p4d import CURATED_SOCIETY_B4_P4D
from scratch.curate_society_b4_extra import CURATED_SOCIETY_B4_EXTRA

from scratch.curate_society_b5_p1 import CURATED_SOCIETY_B5_P1
from scratch.curate_society_b5_p2 import CURATED_SOCIETY_B5_P2
from scratch.curate_society_b5_p3 import CURATED_SOCIETY_B5_P3
from scratch.curate_society_b5_p4 import CURATED_SOCIETY_B5_P4

ALL_CURATED = {}
# B4 overlap
ALL_CURATED.update(CURATED_SOCIETY_B4_P4A)
ALL_CURATED.update(CURATED_SOCIETY_B4_P4B)
ALL_CURATED.update(CURATED_SOCIETY_B4_P4C)
ALL_CURATED.update(CURATED_SOCIETY_B4_P4D)
ALL_CURATED.update(CURATED_SOCIETY_B4_EXTRA)
# B5 parts
ALL_CURATED.update(CURATED_SOCIETY_B5_P1)
ALL_CURATED.update(CURATED_SOCIETY_B5_P2)
ALL_CURATED.update(CURATED_SOCIETY_B5_P3)
ALL_CURATED.update(CURATED_SOCIETY_B5_P4)

APPLE_TOGGLE = """```dataviewjs
if(!document.getElementById('apple-toggle-css')){const s=document.createElement('style');s.id='apple-toggle-css';s.textContent=':root{--apple-red:#FF375F;--apple-red-glow:rgba(255,55,95,0.45);--apple-amber:#FF9F0A;--apple-amber-glow:rgba(255,159,10,0.45);--apple-green:#30D158;--apple-green-glow:rgba(48,209,88,0.45)}.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--background-secondary,#111624);border:1px solid var(--background-modifier-border,#232d42);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--text-muted,#3b4b6b);transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.35)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:48px;height:18px;background:var(--background-primary,#090d17);border-radius:999px;border:1px solid var(--background-modifier-border,#1c2436);display:flex;align-items:center;justify-content:space-between;padding:0 6px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--text-faint,#334155);opacity:.6}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:14px;height:14px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center}.apple-c .halo-c::after{content:"";width:6px;height:6px;border-radius:999px;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.4)}.apple-c .halo-c.pos-0{transform:translateX(0);background-color:var(--apple-red);box-shadow:0 0 8px var(--apple-red-glow)}.apple-c .halo-c.pos-1{transform:translateX(15px);background-color:var(--apple-amber);box-shadow:0 0 8px var(--apple-amber-glow)}.apple-c .halo-c.pos-2{transform:translateX(30px);background-color:var(--apple-green);box-shadow:0 0 8px var(--apple-green-glow)}.apple-c .label{font-size:10px;font-weight:700;letter-spacing:.5px;text-transform:uppercase;margin-left:2px}.apple-c .label.s-0{color:var(--apple-red)}.apple-c .label.s-1{color:var(--apple-amber)}.apple-c .label.s-2{color:var(--apple-green)}';document.head.appendChild(s)}
const p=dv.current();
const states=[{key:'unread',label:'Unread',cls:'s-0',p:'pos-0'},{key:'learning',label:'Learning',cls:'s-1',p:'pos-1'},{key:'learned',label:'Learned',cls:'s-2',p:'pos-2'}];
const statusVal=p.status||'unread';
let curIdx=states.findIndex(s=>s.key===statusVal);
if(curIdx===-1)curIdx=0;
const cur=states[curIdx];
const toggle=document.createElement('div');
toggle.className='apple-c';
const track=document.createElement('div');
track.className='track-c';
track.innerHTML='<span class="c-dot"></span><span class="c-dot"></span><span class="c-dot"></span><div class="halo-c '+cur.p+'"></div>';
const label=document.createElement('span');
label.className='label '+cur.cls;
label.textContent=cur.label;
toggle.appendChild(track);
toggle.appendChild(label);
toggle.addEventListener('click', async (e) => {
    e.stopPropagation();
    curIdx = (curIdx + 1) % 3;
    const nxt = states[curIdx];
    track.querySelector('.halo-c').className = 'halo-c ' + nxt.p;
    label.className = 'label ' + nxt.cls;
    label.textContent = nxt.label;
    const file = app.vault.getAbstractFileByPath(p.file.path);
    if (file) {
        await app.fileManager.processFrontMatter(file, fm => { fm.status = nxt.key; });
        new Notice('' + (p.file.name) + ': marked ' + (nxt.key) + '');
    }
});
dv.container.appendChild(toggle);
```"""

DASHBOARDS = [
    "Dashboard — hum",
    "Dashboard — mun",
]

BASE_DIR = os.path.join("App database", "Latin roots", "Cluster Society")

updated = 0
not_found = []

for dash in DASHBOARDS:
    dash_dir = os.path.join(BASE_DIR, dash)
    files = glob.glob(os.path.join(dash_dir, "*.md"))
    for file_path in files:
        base_name = os.path.basename(file_path)
        stem = os.path.splitext(base_name)[0]
        if stem.startswith("Dashboard —") or stem.startswith("Word Triage —"):
            continue
        
        lookup_key = stem.lower()
        if lookup_key not in ALL_CURATED:
            not_found.append((file_path, lookup_key))
            continue
        
        data = ALL_CURATED[lookup_key]
        
        # Read existing file to extract status
        status = "unread"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                m = re.search(r"^status:\s*(\w+)", content, re.MULTILINE)
                if m:
                    status = m.group(1)
        
        pdef = data.get("primary_definition", "")
        sdef = data.get("secondary_definition", "")
        quotes = data.get("quotes", [])
        
        lines = []
        lines.append("---")
        lines.append(f'latin_root: "[[{dash}]]"')
        lines.append('cluster: "[[Cluster Society]]"')
        lines.append(f"status: {status}")
        lines.append("---")
        lines.append("")
        lines.append(f"# {stem}")
        lines.append("")
        lines.append("> [!status] 🎯 **Status:**")
        lines.append("")
        lines.append(APPLE_TOGGLE)
        lines.append("")
        lines.append("> [!book] 📖 Definitions & Semantic Range")
        lines.append(f"> 1. **Primary Definition (Lexical / Consensus)**: {pdef}")
        lines.append(f"> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: {sdef}")
        lines.append("")
        lines.append("> [!quote] 💬 Contextual Usage & Authentic Quotations")
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            sentence = q.get("sentence", "")
            lines.append(f'> - 📜 **{author} (*{work}*):** *"{sentence}"*')
        lines.append("")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        
        updated += 1

print(f"Updated: {updated} notes in Batch 5")
if not_found:
    print(f"Not found ({len(not_found)}):")
    for p, k in not_found:
        print(f"  {k}: {p}")
