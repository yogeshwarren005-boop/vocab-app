import pathlib

ROOT = pathlib.Path(r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots")

TOGGLE_BLOCK = """
<style>
/* Apple‑Glide toggle CSS */
.apple-toggle-css { /* ... */ }
/* apple-c */
</style>
<script>
// Apple‑Glide toggle JS
// ...
</script>
"""

def has_toggle(text: str) -> bool:
    # Return True only if both required substrings are present
    return "apple-toggle-css" in text and "apple-c" in text

def process_file(fp: pathlib.Path) -> None:
    if fp.suffix.lower() != ".md":
        return
    content = fp.read_text(encoding="utf-8")
    if "latin_root:" not in content.lower():
        return
    # Split into lines for easier manipulation
    lines = content.splitlines()
    # Find front‑matter delimiters (first two '---')
    fm_indices = [i for i, line in enumerate(lines) if line.strip() == "---"]
    if len(fm_indices) < 2:
        # No proper front‑matter; skip
        return
    fm_end = fm_indices[1]
    # Ensure a single status line directly after front‑matter
    status_line = "> [!status] 🎯 **Status:** unread"
    status_idx = None
    for i in range(fm_end + 1, len(lines)):
        if lines[i].strip().startswith("> [!status]"):
            status_idx = i
            break
    if status_idx is None:
        # Insert status line right after front‑matter
        lines.insert(fm_end + 1, status_line)
        status_idx = fm_end + 1
    else:
        # Replace the existing line with the canonical one (to avoid variations)
        lines[status_idx] = status_line
    # Remove any other status lines elsewhere
    cleaned = []
    for i, line in enumerate(lines):
        if i != status_idx and line.strip().startswith("> [!status]"):
            continue
        cleaned.append(line)
    # Determine where to place the toggle block (right after status line)
    insert_pos = status_idx + 1
    # Check if block already present after this position
    after_status = cleaned[insert_pos:]
    if not any('apple-toggle-css' in l and 'apple-c' in l for l in after_status):
        cleaned.insert(insert_pos, TOGGLE_BLOCK.strip())
    new_content = "\n".join(cleaned) + "\n"
    if new_content != content:
        fp.write_text(new_content, encoding="utf-8")
        print(f"Fixed toggle in {fp.relative_to(ROOT)}")

def main():
    for md in ROOT.rglob('*.md'):
        process_file(md)

if __name__ == '__main__':
    main()
