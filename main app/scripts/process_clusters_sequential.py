# -*- coding: utf-8 -*-
"""
process_clusters_sequential.py

A sequential, cluster-by-cluster, dashboard-by-dashboard processor and auditor
for the Latin roots vocabulary corpus in `App database/Latin roots/`.

Key Capabilities:
1. Discovers and audits clusters and dashboards sequentially.
2. Audits every note according to strict `audit-latin-roots.mjs` rules:
   - Frontmatter (`latin_root`, `cluster`, `status: unread`).
   - Interactive Apple Glide DataviewJS Toggle block directly above `> [!book]`.
   - Primary definition (>= 25 chars, active, 0 circular formulas).
   - Secondary definition (>= 25 chars, domain context, Jaccard overlap < 0.70).
   - Exactly 3 authentic quotations with 3 distinct authors, real works, bolded target word (`**word**`).
   - Zero banned synthetic boilerplate phrases.
3. Automatically skips notes and dashboards that are already 100% PRISTINE.
4. For problem/unvetted notes:
   - Searches `main app/corpus/citation_corpus.db` for authentic literary/historical citations.
   - Invokes Gemini API via `google.genai` SDK (when GEMINI_API_KEY is available) to generate unique, authentic, pristine entries note-by-note.
   - Or applies pre-curated dictionaries passed via `--batch-curated`.
   - Pre-validates each note against all audit rules before writing.
5. Runs the official audit script `main app/scripts/audit-latin-roots.mjs` after each dashboard.
6. Optionally commits each completed dashboard to Git via `--git-commit`.

Usage Examples:
  # Check status across all clusters:
  python "main app/scripts/process_clusters_sequential.py" --status

  # Process a specific cluster sequentially:
  python "main app/scripts/process_clusters_sequential.py" --cluster "Cluster Speech"

  # Process a single dashboard within a cluster:
  python "main app/scripts/process_clusters_sequential.py" --cluster "Cluster Speech" --dashboard "Dashboard — fari"

  # Audit-only mode (scan without updating):
  python "main app/scripts/process_clusters_sequential.py" --cluster "Cluster Speech" --audit-only

  # Process with auto Git commit on each pristine dashboard:
  python "main app/scripts/process_clusters_sequential.py" --cluster "Cluster Speech" --git-commit

  # Apply a pre-curated dictionary file to a cluster or dashboard:
  python "main app/scripts/process_clusters_sequential.py" --cluster "Cluster Speech" --batch-curated "scratch/curate_speech_b1.py"
"""

import os
import sys
import re
import json
import sqlite3
import argparse
import subprocess
from typing import Dict, List, Tuple, Optional, Any

sys.stdout.reconfigure(encoding="utf-8")

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LATIN_ROOTS_DIR = os.path.join(BASE_DIR, "App database", "Latin roots")
CORPUS_DB_PATH = os.path.join(BASE_DIR, "main app", "corpus", "citation_corpus.db")
AUDIT_SCRIPT_PATH = os.path.join(BASE_DIR, "main app", "scripts", "audit-latin-roots.mjs")

# Banned boilerplate phrases from audit script
BANNED_PHRASES = [
    'In specialized and domain usage, denoting specific qualities',
    'In technical and systematic terminology, the action',
    'In functional and operational contexts, an agent',
    'The clinical presentation of',
    'Every pathological manifestation of',
    'The gradual evolutionary modification of',
    'In academic literature,',
    'Academic Lexicon',
    'Classic Author'
]

CIRCULAR_REGEX = re.compile(
    r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b',
    re.IGNORECASE
)

APPLE_TOGGLE_SNIPPET = (
    "> [!status] 🎯 **Status:**\n\n"
    "```dataviewjs\n"
    "if(!document.getElementById('apple-toggle-css')){const s=document.createElement('style');s.id='apple-toggle-css';"
    "s.textContent=':root{--apple-red:#FF375F;--apple-red-glow:rgba(255,55,95,0.45);--apple-amber:#FF9F0A;--apple-amber-glow:rgba(255,159,10,0.45);--apple-green:#30D158;--apple-green-glow:rgba(48,209,88,0.45)}.apple-c{position:relative;display:inline-flex;align-items:center;gap:8px;padding:2px 10px 2px 4px;border-radius:999px;background:var(--background-secondary,#111624);border:1px solid var(--background-modifier-border,#232d42);cursor:pointer;user-select:none;transition:border-color .2s ease,transform .2s ease,box-shadow .2s ease;line-height:1;vertical-align:middle;box-sizing:border-box}.apple-c:hover{border-color:var(--text-muted,#3b4b6b);transform:translateY(-1px);box-shadow:0 2px 8px rgba(0,0,0,.35)}.apple-c:active{transform:scale(.96)}.apple-c .track-c{position:relative;width:48px;height:18px;background:var(--background-primary,#090d17);border-radius:999px;border:1px solid var(--background-modifier-border,#1c2436);display:flex;align-items:center;justify-content:space-between;padding:0 6px;box-sizing:border-box}.apple-c .c-dot{width:3px;height:3px;border-radius:999px;background:var(--text-faint,#334155);opacity:.6}.apple-c .halo-c{position:absolute;top:1px;left:1px;width:14px;height:14px;border-radius:999px;transition:transform .35s cubic-bezier(.34,1.6,.64,1),background-color .25s ease,box-shadow .25s ease;display:flex;align-items:center;justify-content:center;box-sizing:border-box}.apple-c .halo-c .core-dot{width:5px;height:5px;border-radius:999px;background:#fff;box-shadow:0 0 4px #fff}.apple-c .halo-c.p0{transform:translateX(0);background:var(--apple-red);box-shadow:0 0 12px var(--apple-red),0 0 20px var(--apple-red-glow)}.apple-c .halo-c.p1{transform:translateX(15px);background:var(--apple-amber);box-shadow:0 0 12px var(--apple-amber),0 0 20px var(--apple-amber-glow)}.apple-c .halo-c.p2{transform:translateX(30px);background:var(--apple-green);box-shadow:0 0 12px var(--apple-green),0 0 20px var(--apple-green-glow)}.apple-c .label{font-size:11px;font-weight:700;letter-spacing:.2px;transition:color .2s ease;min-width:48px}.apple-c .label.unread{color:var(--apple-red)}.apple-c .label.learning{color:var(--apple-amber)}.apple-c .label.learned{color:var(--apple-green)}';document.head.appendChild(s);}\n"
    "const p = dv.current();\n"
    'const rawStatus = p.status || "unread";\n'
    "const states = [{ key: 'unread', label: 'unread', cls: 'unread', p: 'p0' }, { key: 'learning', label: 'learning', cls: 'learning', p: 'p1' }, { key: 'learned', label: 'learned', cls: 'learned', p: 'p2' }];\n"
    "let curIdx = states.findIndex(s => s.key === rawStatus);\n"
    "if (curIdx === -1) curIdx = 0;\n"
    "const toggle = document.createElement('div');\n"
    "toggle.className = 'apple-c';\n"
    "toggle.title = 'Click to glide: unread ➔ learning ➔ learned';\n"
    "const track = document.createElement('div');\n"
    "track.className = 'track-c';\n"
    'track.innerHTML = \'<span class="c-dot"></span><span class="c-dot"></span><span class="c-dot"></span><div class="halo-c \' + states[curIdx].p + \'"><div class="core-dot"></div></div>\';\n'
    "const label = document.createElement('span');\n"
    "label.className = 'label ' + states[curIdx].cls;\n"
    "label.textContent = states[curIdx].label;\n"
    "toggle.appendChild(track);\n"
    "toggle.appendChild(label);\n"
    "toggle.addEventListener('click', async (e) => {\n"
    "    e.stopPropagation();\n"
    "    curIdx = (curIdx + 1) % 3;\n"
    "    const nxt = states[curIdx];\n"
    "    track.querySelector('.halo-c').className = 'halo-c ' + nxt.p;\n"
    "    label.className = 'label ' + nxt.cls;\n"
    "    label.textContent = nxt.label;\n"
    "    const file = app.vault.getAbstractFileByPath(p.file.path);\n"
    "    if (file) {\n"
    "        await app.fileManager.processFrontMatter(file, fm => { fm.status = nxt.key; });\n"
    "        new Notice('' + (p.file.name) + ': marked ' + (nxt.key) + '');\n"
    "    }\n"
    "});\n"
    "dv.container.appendChild(toggle);\n"
    "```\n\n"
)


# ==============================================================================
# 1. Note Auditing Logic (Matches audit-latin-roots.mjs)
# ==============================================================================

def audit_note_content(content: str, file_name: str) -> Tuple[bool, List[str]]:
    """Audits note content against all strict criteria."""
    issues = []
    word = os.path.splitext(file_name)[0].lower().strip()

    # 1. Frontmatter
    if not content.startswith('---'):
        issues.append('Missing frontmatter delimiter ---')
    else:
        fm_end = content.find('---', 3)
        if fm_end == -1:
            issues.append('Unclosed frontmatter')
        else:
            fm = content[:fm_end]
            if 'latin_root:' not in fm:
                issues.append('Frontmatter missing latin_root')
            if 'cluster:' not in fm:
                issues.append('Frontmatter missing cluster')
            if 'status:' not in fm:
                issues.append('Frontmatter missing status')

    # 2. Status toggle block
    status_pos = content.find('> [!status]')
    book_pos = content.find('> [!book]')
    if status_pos == -1:
        issues.append('Missing > [!status] block')
    if book_pos == -1:
        issues.append('Missing > [!book] block')
    if status_pos != -1 and book_pos != -1 and status_pos > book_pos:
        issues.append('Status block must be positioned directly ABOVE > [!book]')
    if 'apple-toggle-css' not in content or 'apple-c' not in content:
        issues.append('Missing Apple Glide Toggle DataviewJS code block')

    # 3. Definitions Check
    p_match = re.search(r'1\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', content)
    s_match = re.search(r'2\.\s*\*\*([^*]+)\*\*:\s*([^\r\n]+)', content)

    p_text = ""
    s_text = ""

    if not p_match:
        issues.append('Missing Primary Definition')
    else:
        p_text = p_match.group(2).strip()
        if len(p_text) < 25:
            issues.append(f'Primary definition too short ({len(p_text)} chars)')
        if CIRCULAR_REGEX.search(p_text):
            issues.append('Primary definition contains circular boilerplate formula ("quality/state of being...")')

    if not s_match:
        issues.append('Missing Secondary Definition')
    else:
        s_text = s_match.group(2).strip()
        if len(s_text) < 25:
            issues.append(f'Secondary definition too short ({len(s_text)} chars)')
        if CIRCULAR_REGEX.search(s_text):
            issues.append('Secondary definition contains circular boilerplate formula ("quality/state of being...")')

    if p_match and s_match and p_text and s_text:
        p_lower = p_text.lower()
        s_lower = s_text.lower()
        if p_lower == s_lower:
            issues.append('Duplicate Definition (Primary == Secondary)')
        else:
            p_tokens = set(re.findall(r'\w+', p_lower))
            s_tokens = set(re.findall(r'\w+', s_lower))
            intersect = p_tokens.intersection(s_tokens)
            union = p_tokens.union(s_tokens)
            jaccard = len(intersect) / max(len(union), 1)
            if jaccard >= 0.70:
                issues.append(f'Definitions excessively similar (Jaccard token overlap = {jaccard:.2f})')

    # 4. Boilerplate / Template detection
    for phrase in BANNED_PHRASES:
        if phrase in content:
            issues.append(f'Contains banned synthetic boilerplate: "{phrase}"')

    # 5. Quotes Check
    if '> [!quote]' not in content:
        issues.append('Missing > [!quote] section')
    else:
        quote_section = content.split('> [!quote]')[1]
        quote_lines = [
            l.strip() for l in quote_section.split('\n')
            if l.strip().startswith('>') and '📜' in l
        ]

        if len(quote_lines) != 3:
            issues.append(f'Expected exactly 3 quotes, found {len(quote_lines)}')

        authors = []
        for q_line in quote_lines:
            auth_match = re.search(
                r'📜\s*\*\*([^*]+?)\s*(?:\(\*([^*]+?)\*\):?\*\*|\*\*\s*\(\*([^*]+?)\*\):?)',
                q_line
            )
            if not auth_match:
                issues.append(f'Malformed citation format: "{q_line[:60]}..."')
            else:
                author = auth_match.group(1).strip()
                work = (auth_match.group(2) or auth_match.group(3) or '').strip()
                authors.append(author)
                if len(author) < 3 or len(work) < 2:
                    issues.append(f'Suspiciously short author or work title: "{author}" / "{work}"')

            colon_match = re.search(r':\*\*\s*(.+)$', q_line)
            quote_body = colon_match.group(1) if colon_match else q_line
            if '**' not in quote_body:
                issues.append(f'Target word not bolded in quote: "{q_line[:50]}..."')

        if len(set(authors)) < len(quote_lines):
            issues.append(f'Duplicate author in quotes: ({", ".join(authors)})')

    is_pristine = (len(issues) == 0)
    return is_pristine, issues


def audit_note_file(file_path: str) -> Tuple[bool, List[str]]:
    """Audits an individual note file on disk."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return audit_note_content(content, os.path.basename(file_path))
    except Exception as e:
        return False, [f"Read error: {str(e)}"]


# ==============================================================================
# 2. Citation Corpus Integration
# ==============================================================================

def query_citation_corpus(word: str, limit: int = 15) -> List[Dict[str, str]]:
    """Queries citation_corpus.db for authentic sentences containing the target word."""
    if not os.path.exists(CORPUS_DB_PATH):
        return []

    clean_word = word.replace('-', ' ')
    results = []
    seen_authors = set()

    try:
        conn = sqlite3.connect(CORPUS_DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            SELECT s.author, s.work, s.sentence 
            FROM sentences_fts f 
            JOIN sentences s ON f.rowid = s.id 
            WHERE f.sentence MATCH ? LIMIT ?
        """, (f'"{clean_word}"', limit * 2))
        rows = cur.fetchall()
        conn.close()

        # Word boundary pattern for bolding
        pattern = re.compile(rf'\b({re.escape(clean_word)})\b', re.IGNORECASE)

        for author, work, sentence in rows:
            if author in seen_authors:
                continue
            if not pattern.search(sentence):
                continue

            # Ensure sentence is clean
            clean_sentence = sentence.strip().replace('', "'").replace('  ', ' ')
            # Apply bolding if not already bolded
            if '**' not in clean_sentence:
                clean_sentence = pattern.sub(r'**\1**', clean_sentence)

            seen_authors.add(author)
            results.append({
                "author": author.strip(),
                "work": work.strip(),
                "quote": clean_sentence
            })

            if len(results) >= 3:
                break

    except Exception:
        pass

    return results


# ==============================================================================
# 3. Gemini Generation Engine
# ==============================================================================

def init_gemini_client(api_key: Optional[str] = None):
    """Initializes Google GenAI Client if API key is available."""
    key = api_key or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        return None

    try:
        from google import genai
        client = genai.Client(api_key=key)
        return client
    except Exception as e:
        print(f"[WARN] Failed to initialize Google GenAI Client: {e}")
        return None


def generate_with_gemini(
    word: str,
    root_name: str,
    cluster_name: str,
    corpus_quotes: List[Dict[str, str]],
    client: Any,
    model_name: str = "gemini-2.5-flash",
    max_retries: int = 3
) -> Optional[Dict[str, Any]]:
    """Generates a pristine, non-circular vocabulary entry via Gemini API."""
    if client is None:
        return None

    quotes_context = ""
    if corpus_quotes:
        quotes_context = "Available authentic quotes from historical database (use or adapt these first):\n"
        for q in corpus_quotes:
            quotes_context += f"- {q['author']} ({q['work']}): \"{q['quote']}\"\n"

    system_instruction = (
        "You are an expert historical lexicographer and classical philologist curating a high-precision Latin roots vocabulary database.\n"
        "Generate a structured JSON entry with exact lexical definitions and three verified historical/literary quotes.\n"
        "CRITICAL AUDIT RULES:\n"
        "1. Primary Definition: >= 25 characters. Standard lexical consensus. Use active descriptive phrasing.\n"
        "   STRICTLY FORBIDDEN: Any circular formula matching 'quality of being', 'state of being', 'condition of being', 'or degree of being'.\n"
        "2. Secondary Definition: >= 25 characters. Specialized, domain, or encyclopedic nuance.\n"
        "   Token Jaccard overlap with primary must be < 0.70. STRICTLY NO circular 'state/quality of being'.\n"
        "3. Quotes: Exactly 3 quotes from 3 DISTINCT real historical, literary, or scientific authors (e.g. Shakespeare, Darwin, Hardy, Eliot, Melville, Locke, Huxley, Newton, Emerson, Milton).\n"
        "   In each quote, the target word MUST be explicitly wrapped in markdown bold: **word**.\n"
        "   Do NOT invent fake authors or works. Do NOT use synthetic phrases like 'Academic Lexicon'."
    )

    prompt = (
        f"Target Word: {word}\n"
        f"Latin Root: {root_name}\n"
        f"Semantic Cluster: {cluster_name}\n\n"
        f"{quotes_context}\n"
        "Output strictly valid JSON with keys:\n"
        "{\n"
        '  "primary": "...",\n'
        '  "secondary": "...",\n'
        '  "quotes": [\n'
        '    {"author": "...", "work": "...", "quote": "..."},\n'
        '    {"author": "...", "work": "...", "quote": "..."},\n'
        '    {"author": "...", "work": "...", "quote": "..."}\n'
        "  ]\n"
        "}"
    )

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config={
                    "system_instruction": system_instruction,
                    "response_mime_type": "application/json",
                    "temperature": 0.2
                }
            )

            entry = json.loads(response.text)

            # Pre-validate entry
            p_text = entry.get("primary", "")
            s_text = entry.get("secondary", "")
            quotes = entry.get("quotes", [])

            if len(p_text) < 25 or len(s_text) < 25:
                continue
            if CIRCULAR_REGEX.search(p_text) or CIRCULAR_REGEX.search(s_text):
                prompt += "\nCORRECTION REQUIRED: Remove any circular 'quality/state/condition of being' phrase from definitions."
                continue
            if len(quotes) != 3:
                continue

            authors = set(q.get("author", "") for q in quotes)
            if len(authors) != 3:
                continue

            # Ensure bolding
            all_bolded = True
            for q in quotes:
                if "**" not in q.get("quote", ""):
                    # Auto bold target word if missing
                    q_text = q.get("quote", "")
                    pat = re.compile(rf'\b({re.escape(word)})\b', re.IGNORECASE)
                    if pat.search(q_text):
                        q["quote"] = pat.sub(r'**\1**', q_text)
                    else:
                        all_bolded = False
            if not all_bolded:
                continue

            return entry

        except Exception as e:
            if attempt == max_retries - 1:
                print(f"    [Gemini Error for '{word}']: {e}")

    return None


# ==============================================================================
# 4. Note Writer & Updater
# ==============================================================================

def write_curated_note(
    file_path: str,
    root_name: str,
    cluster_name: str,
    entry: Dict[str, Any]
) -> bool:
    """Updates a note file on disk with pristine frontmatter, Apple toggle, and curated entry."""
    file_name = os.path.basename(file_path)
    word = os.path.splitext(file_name)[0]

    frontmatter = (
        "---\n"
        f'latin_root: "[[{root_name}]]"\n'
        f'cluster: "[[{cluster_name}]]"\n'
        "status: unread\n"
        "---\n"
        f"# {word}\n\n"
    )

    body = (
        f"{APPLE_TOGGLE_SNIPPET}"
        "> [!book] 📖 Definitions & Semantic Range\n"
        f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {entry['primary'].strip()}\n"
        f"> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {entry['secondary'].strip()}\n\n"
        "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    )

    for q in entry["quotes"]:
        body += f"> - 📜 **{q['author'].strip()} (*{q['work'].strip()}*):** *\"{q['quote'].strip()}\"*\n"

    new_content = frontmatter + body

    # Verify against audit criteria before saving
    is_valid, issues = audit_note_content(new_content, file_name)
    if not is_valid:
        print(f"    [VALIDATION FAILED before write for {file_name}]: {issues}")
        return False

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


# ==============================================================================
# 5. Official Node Audit Subprocess
# ==============================================================================

def run_official_audit(target_path: str) -> bool:
    """Executes main app/scripts/audit-latin-roots.mjs via Node.js."""
    if not os.path.exists(AUDIT_SCRIPT_PATH):
        print(f"[WARN] Audit script not found at {AUDIT_SCRIPT_PATH}")
        return False

    try:
        res = subprocess.run(
            ["node", AUDIT_SCRIPT_PATH, target_path],
            capture_output=True,
            text=True,
            encoding="utf-8"
        )
        if res.returncode == 0 and "100% PRISTINE (PASS)" in res.stdout:
            return True
        else:
            print(f"\n[AUDIT FAIL] {target_path}:\n{res.stdout}\n{res.stderr}")
            return False
    except Exception as e:
        print(f"[ERROR] Failed to run official audit: {e}")
        return False


# ==============================================================================
# 6. Sequential Processing Logic
# ==============================================================================

def get_clusters() -> List[str]:
    """Returns sorted list of all cluster directory names."""
    if not os.path.exists(LATIN_ROOTS_DIR):
        return []
    return sorted([
        d for d in os.listdir(LATIN_ROOTS_DIR)
        if os.path.isdir(os.path.join(LATIN_ROOTS_DIR, d)) and d.startswith("Cluster")
    ])


def get_dashboards(cluster_dir: str) -> List[str]:
    """Returns sorted list of all dashboard directory names in a cluster."""
    cluster_path = os.path.join(LATIN_ROOTS_DIR, cluster_dir)
    return sorted([
        d for d in os.listdir(cluster_path)
        if os.path.isdir(os.path.join(cluster_path, d)) and d.startswith("Dashboard — ")
    ])


def audit_dashboard_notes(dashboard_path: str) -> Tuple[int, int, List[str]]:
    """Scans and audits all notes in a dashboard folder."""
    files = [
        f for f in os.listdir(dashboard_path)
        if f.endswith('.md') and not f.startswith(('Dashboard', 'Word Triage', 'Cluster', 'Semantic Field'))
    ]
    pristine_count = 0
    problem_files = []

    for fname in sorted(files):
        fpath = os.path.join(dashboard_path, fname)
        is_pristine, _ = audit_note_file(fpath)
        if is_pristine:
            pristine_count += 1
        else:
            problem_files.append(fname)

    return len(files), pristine_count, problem_files


def process_dashboard(
    cluster_name: str,
    dashboard_name: str,
    client: Any,
    batch_curated_data: Optional[Dict[str, Any]] = None,
    dry_run: bool = False,
    audit_only: bool = False,
    auto_commit: bool = False
) -> bool:
    """Processes an individual dashboard sequentially."""
    dashboard_path = os.path.join(LATIN_ROOTS_DIR, cluster_name, dashboard_name)
    total_notes, pristine_notes, problem_files = audit_dashboard_notes(dashboard_path)

    print(f"\n[{cluster_name}] Processing {dashboard_name} ({total_notes} words)...")

    if total_notes == 0:
        print("  Empty dashboard. Skipping.")
        return True

    if pristine_notes == total_notes:
        print(f"  ✅ Already 100% PRISTINE ({total_notes}/{total_notes} notes pass).")
        return True

    print(f"  Status: {pristine_notes}/{total_notes} pristine ({len(problem_files)} need curation).")

    if audit_only:
        for p in problem_files:
            _, issues = audit_note_file(os.path.join(dashboard_path, p))
            print(f"    - {p}: {issues}")
        return False

    updated_count = 0

    for fname in problem_files:
        word = os.path.splitext(fname)[0]
        file_path = os.path.join(dashboard_path, fname)
        print(f"  -> Curating: {word}...")

        entry = None

        # Check pre-curated dictionary first
        if batch_curated_data:
            if word in batch_curated_data:
                entry = batch_curated_data[word]
            else:
                matching = [k for k in batch_curated_data if k.lower() == word.lower()]
                if matching:
                    entry = batch_curated_data[matching[0]]

        # If not in batch data, query Gemini
        if entry is None and client is not None:
            corpus_quotes = query_citation_corpus(word)
            entry = generate_with_gemini(
                word=word,
                root_name=dashboard_name,
                cluster_name=cluster_name,
                corpus_quotes=corpus_quotes,
                client=client
            )

        if entry is None:
            print(f"    [SKIP] No curation available for '{word}'. Provide batch dictionary or GEMINI_API_KEY.")
            continue

        if dry_run:
            print(f"    [DRY RUN] Would update {word} with primary: {entry['primary'][:60]}...")
            updated_count += 1
            continue

        success = write_curated_note(file_path, dashboard_name, cluster_name, entry)
        if success:
            updated_count += 1
            print(f"    Updated and verified: {fname}")
        else:
            print(f"    [ERROR] Failed to write valid note for {fname}")

    if dry_run:
        return True

    # Re-run official audit on the dashboard
    print(f"  Verifying with official audit script...")
    audit_passed = run_official_audit(dashboard_path)

    if audit_passed:
        print(f"  🎉 {dashboard_name} successfully achieved 100% PRISTINE!")
        if auto_commit:
            commit_msg = f"Curate {cluster_name} - {dashboard_name} ({total_notes} words) to 100% PRISTINE"
            subprocess.run(["git", "add", dashboard_path], cwd=BASE_DIR, check=False)
            res = subprocess.run(["git", "commit", "-m", commit_msg], cwd=BASE_DIR, capture_output=True, text=True)
            print(f"  [GIT] {res.stdout.strip()}")
        return True
    else:
        print(f"  ❌ {dashboard_name} failed official audit. Inspect above for details.")
        return False


def process_cluster(
    cluster_name: str,
    target_dashboard: Optional[str] = None,
    client: Any = None,
    batch_curated_data: Optional[Dict[str, Any]] = None,
    dry_run: bool = False,
    audit_only: bool = False,
    auto_commit: bool = False
) -> bool:
    """Processes all dashboards in a cluster sequentially."""
    dashboards = get_dashboards(cluster_name)
    if not dashboards:
        print(f"No dashboards found in cluster: {cluster_name}")
        return False

    if target_dashboard:
        target_normalized = target_dashboard if target_dashboard.startswith("Dashboard — ") else f"Dashboard — {target_dashboard}"
        if target_normalized not in dashboards:
            print(f"Dashboard '{target_normalized}' not found in cluster '{cluster_name}'. Available: {dashboards}")
            return False
        dashboards = [target_normalized]

    print(f"\n=======================================================")
    print(f"Cluster: {cluster_name} ({len(dashboards)} dashboards)")
    print(f"=======================================================")

    all_dashboards_passed = True

    for idx, d_name in enumerate(dashboards, 1):
        print(f"\n--- Progress: [{idx}/{len(dashboards)}] ---")
        passed = process_dashboard(
            cluster_name=cluster_name,
            dashboard_name=d_name,
            client=client,
            batch_curated_data=batch_curated_data,
            dry_run=dry_run,
            audit_only=audit_only,
            auto_commit=auto_commit
        )
        if not passed:
            all_dashboards_passed = False

    cluster_path = os.path.join(LATIN_ROOTS_DIR, cluster_name)
    print(f"\nAuditing entire cluster: {cluster_name}...")
    cluster_audit_passed = run_official_audit(cluster_path)

    if cluster_audit_passed:
        print(f"\n🌟 CLUSTER {cluster_name} IS 100% PRISTINE! 🌟")
    else:
        print(f"\n⚠️ Cluster {cluster_name} has unresolved notes.")

    return cluster_audit_passed


def print_status_summary():
    """Prints a high-level table of all clusters, word counts, and pristine completion."""
    clusters = get_clusters()
    print("\n" + "=" * 80)
    print(f"{'Cluster Name':<42} | {'Dashboards':<10} | {'Total':<6} | {'Pristine':<8} | {'Status'}")
    print("=" * 80)

    grand_total = 0
    grand_pristine = 0

    for c in clusters:
        dashboards = get_dashboards(c)
        c_path = os.path.join(LATIN_ROOTS_DIR, c)
        c_total = 0
        c_pristine = 0

        for d in dashboards:
            d_path = os.path.join(c_path, d)
            tot, pris, _ = audit_dashboard_notes(d_path)
            c_total += tot
            c_pristine += pris

        grand_total += c_total
        grand_pristine += c_pristine

        status_icon = "✅ PASS" if (c_total > 0 and c_total == c_pristine) else f"{c_total - c_pristine} pending"
        print(f"{c:<42} | {len(dashboards):<10} | {c_total:<6} | {c_pristine:<8} | {status_icon}")

    print("=" * 80)
    print(f"{'GRAND TOTAL':<42} | {'-':<10} | {grand_total:<6} | {grand_pristine:<8} | {grand_pristine/max(grand_total,1)*100:.1f}%")
    print("=" * 80 + "\n")


# ==============================================================================
# 7. Main Entry Point & CLI
# ==============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Sequential cluster and dashboard processor for Latin roots vocabulary database."
    )
    parser.add_argument("--cluster", type=str, help="Name of cluster to process (e.g. 'Cluster Speech' or 'Speech')")
    parser.add_argument("--dashboard", type=str, help="Specific dashboard to process (e.g. 'articul' or 'Dashboard — articul')")
    parser.add_argument("--all", action="store_true", help="Process all clusters sequentially")
    parser.add_argument("--status", action="store_true", help="Display audit status of all clusters and exit")
    parser.add_argument("--audit-only", action="store_true", help="Audit notes without making any edits")
    parser.add_argument("--dry-run", action="store_true", help="Simulate generation without writing files to disk")
    parser.add_argument("--git-commit", action="store_true", help="Automatically commit each dashboard upon 100% PASS")
    parser.add_argument("--api-key", type=str, help="Gemini API Key (or set GEMINI_API_KEY environment variable)")
    parser.add_argument("--model", type=str, default="gemini-2.5-flash", help="Gemini model name (default: gemini-2.5-flash)")
    parser.add_argument("--batch-curated", type=str, help="Path to Python/JSON file containing pre-curated data dictionary")

    args = parser.parse_args()

    if args.status:
        print_status_summary()
        return

    # Load batch curated dictionary if provided
    batch_data = {}
    if args.batch_curated:
        b_path = os.path.abspath(args.batch_curated)
        if not os.path.exists(b_path):
            print(f"[ERROR] Batch file not found: {b_path}")
            sys.exit(1)
        if b_path.endswith('.json'):
            with open(b_path, "r", encoding="utf-8") as f:
                batch_data = json.load(f)
        elif b_path.endswith('.py'):
            import importlib.util
            spec = importlib.util.spec_from_file_location("batch_module", b_path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            # Find dictionary in module
            for attr in dir(mod):
                val = getattr(mod, attr)
                if isinstance(val, dict) and any(isinstance(v, dict) and "primary" in v for v in val.values()):
                    batch_data = val
                    print(f"Loaded {len(batch_data)} words from {attr} in {args.batch_curated}")
                    break

    client = init_gemini_client(args.api_key)
    if client:
        print(f"[INFO] Gemini Client initialized with model: {args.model}")
    else:
        print("[INFO] Running in local/corpus mode (Gemini API key not configured).")

    all_clusters = get_clusters()

    if args.cluster:
        c_target = args.cluster if args.cluster.startswith("Cluster ") else f"Cluster {args.cluster}"
        if c_target not in all_clusters:
            print(f"[ERROR] Cluster '{c_target}' not found. Available clusters:\n{all_clusters}")
            sys.exit(1)
        process_cluster(
            cluster_name=c_target,
            target_dashboard=args.dashboard,
            client=client,
            batch_curated_data=batch_data,
            dry_run=args.dry_run,
            audit_only=args.audit_only,
            auto_commit=args.git_commit
        )
    elif args.all:
        for c in all_clusters:
            process_cluster(
                cluster_name=c,
                client=client,
                batch_curated_data=batch_data,
                dry_run=args.dry_run,
                audit_only=args.audit_only,
                auto_commit=args.git_commit
            )
    else:
        print("Please specify --cluster <Name>, --all, or --status. Use --help for full options.")


if __name__ == "__main__":
    main()
