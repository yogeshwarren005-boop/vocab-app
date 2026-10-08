import pathlib

ROOT = pathlib.Path(r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots")
TOGGLE_BLOCK = """\n<style>\n/* Apple‑Glide toggle CSS */\n.apple-toggle-css { /* ... */ }\n</style>\n<script>\n// Apple‑Glide toggle JS\n// ...\n</script>\n"""

def has_toggle(text: str) -> bool:
    return "apple-toggle-css" in text or "apple-c" in text

def process_file(fp: pathlib.Path) -> None:
    if fp.suffix.lower() != ".md":
        return
    content = fp.read_text(encoding="utf-8")
    if "latin_root:" not in content.lower():
        return
    if has_toggle(content):
        return
    lines = content.splitlines(keepends=True)
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and line.strip().startswith("> [!status]"):
            new_lines.append(TOGGLE_BLOCK)
            inserted = True
    if not inserted:
        new_lines.append(TOGGLE_BLOCK)
    fp.write_text("".join(new_lines), encoding="utf-8")
    print(f"✅ Added toggle to: {fp.relative_to(ROOT)}")

def main():
    for md in ROOT.rglob("*.md"):
        process_file(md)

if __name__ == "__main__":
    main()
