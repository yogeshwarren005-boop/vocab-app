import pathlib, re

ROOT = pathlib.Path(r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots")
TOGGLE_BLOCK = """\n<style>\n/* Apple‑Glide toggle CSS */\n.apple-toggle-css { /* ... */ }\n</style>\n<script>\n// Apple‑Glide toggle JS\n// ...\n</script>\n"""

def has_toggle(text: str) -> bool:
    return "apple-toggle-css" in text or "apple-c" in text

def clean_file(fp: pathlib.Path) -> None:
    if fp.suffix.lower() != ".md":
        return
    content = fp.read_text(encoding="utf-8")
    if "latin_root:" not in content.lower():
        return
    lines = content.splitlines()
    # Identify front‑matter block (first occurrence of --- line)
    fm_end = None
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if fm_end is None:
                # first delimiter – keep it
                fm_end = i
            else:
                # second delimiter – end of front‑matter
                fm_end = i
                break
    if fm_end is None:
        # no front‑matter, just return
        return
    # Ensure exactly one status line immediately after front‑matter
    # Find the first status line after fm_end
    status_idx = None
    for i in range(fm_end+1, len(lines)):
        if lines[i].strip().startswith('> [!status]'):
            status_idx = i
            break
    # If missing, insert a default status line after front‑matter
    if status_idx is None:
        lines.insert(fm_end+1, '> [!status] 🎯 **Status:** unread')
        status_idx = fm_end+1
    # Remove any other status lines
    cleaned = []
    for i, line in enumerate(lines):
        if i != status_idx and line.strip().startswith('> [!status]'):
            continue
        cleaned.append(line)
    # Ensure toggle block exists after the status line
    after_status = cleaned[status_idx+1:] if status_idx+1 < len(cleaned) else []
    if not any('apple-toggle-css' in l for l in after_status):
        cleaned.insert(status_idx+1, TOGGLE_BLOCK.strip())
    new_content = "\n".join(cleaned) + "\n"
    if new_content != content:
        fp.write_text(new_content, encoding='utf-8')
        print(f"Cleaned {fp.relative_to(ROOT)}")

def main():
    for md in ROOT.rglob('*.md'):
        clean_file(md)

if __name__ == '__main__':
    main()
