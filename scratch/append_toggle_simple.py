import pathlib

ROOT = pathlib.Path(r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots")
TOGGLE_BLOCK = """
<style>
/* Apple‑Glide toggle CSS */
.apple-toggle-css { /* ... */ }
</style>
<script>
// Apple‑Glide toggle JS
// ...
</script>
"""

def has_toggle(text: str) -> bool:
    return "apple-toggle-css" in text or "apple-c" in text

def process_file(fp: pathlib.Path) -> None:
    if fp.suffix.lower() != ".md":
        return
    content = fp.read_text(encoding="utf-8")
    if "latin_root:" not in content.lower():
        return
    if not has_toggle(content):
        # Ensure file ends with a newline before appending
        new_content = content.rstrip() + "\n\n" + TOGGLE_BLOCK.strip() + "\n"
        fp.write_text(new_content, encoding="utf-8")
        print(f"Added toggle to {fp.relative_to(ROOT)}")

def main():
    for md in ROOT.rglob('*.md'):
        process_file(md)

if __name__ == '__main__':
    main()
