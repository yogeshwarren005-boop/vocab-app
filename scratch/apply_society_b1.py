# -*- coding: utf-8 -*-
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.dirname(__file__))

from curate_society_b1 import CURATED_SOCIETY_B1

BASE_DIR = r"App database/Latin roots/Cluster Society"
TARGET_DASHBOARDS = [
    "Dashboard — famul",
    "Dashboard — gent",
    "Dashboard — pater",
    "Dashboard — patr",
    "Dashboard — matr"
]

def check_file_pristine(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    if not content.startswith('---'): return False
    if not re.search(r'status:\s*(unread|learning|learned)', content): return False
    if 'apple-toggle-css' not in content or 'apple-c' not in content: return False
    p = re.search(r'1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', content)
    s = re.search(r'2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', content)
    if not p or not s: return False
    if len(p.group(2).strip()) < 25 or len(s.group(2).strip()) < 25: return False
    circ = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    if circ.search(p.group(2)) or circ.search(s.group(2)): return False
    banned = ['In academic literature,', 'Academic Lexicon', 'Classic Author', 'In specialized and domain usage', 'In technical and systematic terminology', 'In functional and operational contexts']
    if any(b in content for b in banned): return False
    q_sec = content.split('> [!quote]')
    if len(q_sec) < 2: return False
    qlines = [l for l in q_sec[1].split('\n') if l.strip().startswith('>') and '📜' in l]
    if len(qlines) != 3: return False
    return True

def extract_from_vault_match(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        c = f.read()

    p_match = re.search(r'1\.\s+\*\*Primary Definition[^*]*\*\*:\s*([^\n\r]+)', c)
    s_match = re.search(r'2\.\s+\*\*Secondary[^*]*\*\*:\s*([^\n\r]+)', c)
    quotes_matches = re.findall(r'> - 📜 \*\*([^*]+)\s+\(\*([^*]+)\*\):\*\*\s+\*\"([^\"]+)\"\*', c)

    if not p_match or not s_match or len(quotes_matches) != 3:
        raise ValueError(f"Could not parse vault match from {filepath}")

    quotes = []
    for a, w, sent in quotes_matches:
        quotes.append({"author": a.strip(), "work": w.strip(), "sentence": sent.strip()})

    return {
        "primary_definition": p_match.group(1).strip(),
        "secondary_definition": s_match.group(1).strip(),
        "quotes": quotes
    }

APPLE_TOGGLE = '''```dataviewjs
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
```'''

def main():
    print("Finding pristine vault notes across other clusters...")
    vault_notes = {}
    vault_root = "App database/Latin roots"
    for root, dirs, files in os.walk(vault_root):
        if 'Cluster Society' in root or '03_Reference_and_Rules' in root:
            continue
        for f in files:
            if f.endswith('.md') and not any(f.startswith(p) for p in ['Dashboard —', 'Word Triage —', 'Cluster', 'Semantic Field']):
                w = f[:-3].lower().strip()
                fp = os.path.join(root, f)
                if w not in vault_notes and check_file_pristine(fp):
                    vault_notes[w] = fp
    
    print(f"Total vault matches available: {len(vault_notes)}")

    total_updated = 0
    missing = []

    for dirname in TARGET_DASHBOARDS:
        target_dir = os.path.join(BASE_DIR, dirname)
        disk_files = sorted([f for f in os.listdir(target_dir) if f.endswith('.md') and not any(f.startswith(p) for p in ['Dashboard —', 'Word Triage —', 'Cluster', 'Semantic Field'])])
        
        for fname in disk_files:
            word = fname[:-3]
            w_lower = word.lower().strip()
            
            if w_lower in CURATED_SOCIETY_B1:
                item = CURATED_SOCIETY_B1[w_lower]
            elif w_lower in vault_notes:
                try:
                    item = extract_from_vault_match(vault_notes[w_lower])
                except Exception as e:
                    missing.append(f"{w_lower} (failed extraction: {e})")
                    continue
            else:
                missing.append(w_lower)
                continue

            file_path = os.path.join(target_dir, fname)

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
cluster: "[[Cluster Society]]"
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
> 1. **Primary Definition (Lexical / Consensus)**: {p_def}
> 2. **Secondary / Nuanced Definition (Contextual / Classical)**: {s_def}

> [!quote] 💬 Contextual Usage & Authentic Quotations
{quotes_block}
"""

            with open(file_path, "w", encoding="utf-8") as fp:
                fp.write(new_content)
            total_updated += 1

    if missing:
        print(f"[ERROR] Missing {len(missing)} words: {missing}")
        sys.exit(1)

    print(f"\n[SUCCESS] Total updated files in Society Batch 1: {total_updated}")

if __name__ == '__main__':
    main()
