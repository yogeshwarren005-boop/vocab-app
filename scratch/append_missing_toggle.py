import pathlib

ROOT = pathlib.Path(r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots")

# Apple‑Glide toggle block to be appended when missing
TOGGLE_BLOCK = """\n<style>\n/* Apple‑Glide toggle CSS */\n.apple-toggle-css { /* ... */ }\n</style>\n<script>\n// Apple‑Glide toggle JS\n// ...\n</script>\n"""

def has_toggle(text: str) -> bool:
    """Return True if the toggle code already exists in the file."""
    return "apple-toggle-css" in text or "apple-c" in text

def process_file(fp: pathlib.Path) -> None:
    if fp.suffix.lower() != ".md":
        return
    content = fp.read_text(encoding="utf-8")
    # Only act on vocab notes (they contain a latin_root front‑matter key)
    if "latin_root:" not in content.lower():
        return
    if has_toggle(content):
        return  # nothing to do
    # Append the toggle block at the end of the file, ensuring a final newline
    new_content = content.rstrip() + "\n" + TOGGLE_BLOCK + "\n"
    fp.write_text(new_content, encoding="utf-8")
    print(f"✅ Appended toggle to: {fp.relative_to(ROOT)}")

def main():
    for md_file in ROOT.rglob("*.md"):
        process_file(md_file)

if __name__ == "__main__":
    main()
