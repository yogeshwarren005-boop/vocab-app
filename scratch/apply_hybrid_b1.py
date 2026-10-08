# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from curate_hybrid_b1_p1a import CURATED_HYBRID_B1_P1A
from curate_hybrid_b1_p1b import CURATED_HYBRID_B1_P1B

all_curated = {}
all_curated.update(CURATED_HYBRID_B1_P1A)
all_curated.update(CURATED_HYBRID_B1_P1B)

print(f"Total unique curated words in Hybrid Batch 1: {len(all_curated)}")

base_dir = r"App database/Latin roots/Cluster Greek-Latin Hybrid"

APPLE_TOGGLE = '''```dataviewjs
if(!document.getElementById('apple-toggle-css')){const s=document.createElement('style');s.id='apple-toggle-css';s.textContent=':root{--apple-red:#FF375F;--apple-red-glow:rgba(255,55,95,0.45);--apple-amber:#FF9F0A;--apple-amber-glow:rgba(255,159,10,0.45);--apple-green:#30D158;--apple-green-glow:rgba(48,209,88,0.45)}.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--background-secondary,#111624);border:1px solid var(--background-modifier-border,#232d42);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--text-muted,#3b4b6b);transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.35)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:48px;height:18px;background:var(--background-primary,#090d17);border-radius:999px;border:1px solid var(--background-modifier-border,#1c2436);display:flex;align-items:center;justify-content:space-between;padding:0 6px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--text-faint,#334155);opacity:.6}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:14px;height:14px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center;box-sizing:border-box}.apple-c .halo-c .core-dot{width:5px;height:5px;border-radius:999px;background:#fff;box-shadow:0 0 4px #fff}.apple-c .halo-c.p0{transform:translateX(0);background:var(--apple-red);box-shadow:0 0 12px var(--apple-red),0 0 20px var(--apple-red-glow)}.apple-c .halo-c.p1{transform:translateX(15px);background:var(--apple-amber);box-shadow:0 0 12px var(--apple-amber),0 0 20px var(--apple-amber-glow)}.apple-c .halo-c.p2{transform:translateX(30px);background:var(--apple-green);box-shadow:0 0 12px var(--apple-green),0 0 20px var(--apple-green-glow)}.apple-c .label{font-size:11px;font-weight:700;letter-spacing:.2px;transition:color .2s ease;min-width:48px}.apple-c .label.unread{color:var(--apple-red)}.apple-c .label.learning{color:var(--apple-amber)}.apple-c .label.learned{color:var(--apple-green)}';document.head.appendChild(s);}
const p = dv.current();
const rawStatus = p.status || "unread";
const states = [{ key: 'unread', label: 'unread', cls: 'unread', p: 'p0' }, { key: 'learning', label: 'learning', cls: 'learning', p: 'p1' }, { key: 'learned', label: 'learned', cls: 'learned', p: 'p2' }];
let curIdx = states.findIndex(s => s.key === rawStatus);
if (curIdx === -1) curIdx = 0;
const toggle = document.createElement('div');
toggle.className = 'apple-c';
toggle.title = 'Click to glide: unread ➔ learning ➔ learned';
const track = document.createElement('div');
track.className = 'track-c';
track.innerHTML = '<span class="c-dot"></span><span class="c-dot"></span><span class="c-dot"></span><div class="halo-c ' + states[curIdx].p + '"><div class="core-dot"></div></div>';
const label = document.createElement('span');
label.className = 'label ' + states[curIdx].cls;
label.textContent = states[curIdx].label;
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
```'''

total_updated = 0
target_dashboards = [
    'Dashboard — hier',
    'Dashboard — scop',
    'Dashboard — cosm',
    'Dashboard — nom_law',
    'Dashboard — theo',
]

for dirname in target_dashboards:
    target_dir = os.path.join(base_dir, dirname)
    disk_words = sorted([f[:-3] for f in os.listdir(target_dir) if f.endswith('.md') and not f.startswith('Dashboard') and not f.startswith('Word Triage')])
    
    dash_updated = 0
    for word in disk_words:
        if word not in all_curated:
            print(f"[MISSING] {word} not found in all_curated!")
            continue
        item = all_curated[word]
        file_path = os.path.join(target_dir, f"{word}.md")
        
        status = "unread"
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as fp:
                c = fp.read()
            if c.startswith("---"):
                parts = c.split("---", 2)
                if len(parts) >= 3:
                    for line in parts[1].splitlines():
                        if line.startswith("status:"):
                            status = line.split(":", 1)[1].strip()

        frontmatter = f"""---
latin_root: "[[{dirname}]]"
cluster: "[[Cluster Greek-Latin Hybrid]]"
status: {status}
---"""

        quotes_lines = []
        for q in item["quotes"]:
            sentence = q.get('sentence') or q.get('quote')
            quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{sentence}\"*")
        quotes_block = "\n".join(quotes_lines)

        p_def = item.get('primary_definition') or item.get('primary')
        s_def = item.get('secondary_definition') or item.get('secondary')

        new_content = f"""{frontmatter}

# {word}

> [!status] 🎯 **Status:**

{APPLE_TOGGLE}

> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}

> [!quote] 💬 Contextual Usage & Authentic Quotations
{quotes_block}
"""

        with open(file_path, "w", encoding="utf-8") as fp:
            fp.write(new_content)
        dash_updated += 1
        total_updated += 1

    print(f"[OK] Updated {dash_updated} files in {dirname}")

print(f"\n[SUCCESS] Total updated files across Hybrid Batch 1: {total_updated}")
