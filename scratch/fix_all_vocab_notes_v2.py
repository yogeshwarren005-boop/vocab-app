import os, re, pathlib

ROOT_DIR = pathlib.Path(r"C:\\Users\\user\\Desktop\\Vocab app\\App database\\Latin roots")

STATUS_BLOCK = "> [!status] 🎯 **Status:** unread\n"
APPLE_TOGGLE_BLOCK = """
<style>
/* Apple‑Glide toggle CSS */
.apple-toggle-css { /* ... */ }
</style>
<script>
// Apple‑Glide toggle JS
// ...
</script>
"""

AUTHORS = ["Ada Lovelace", "Nikola Tesla", "Marie Curie"]
WORKS = ["Collected Works", "Visionary Essays", "Scientific Memoirs"]

def insert_status_and_toggle(text: str) -> str:
    lines = text.splitlines(keepends=True)
    new_lines = []
    inserted_status = False
    inserted_toggle = False
    for i, line in enumerate(lines):
        new_lines.append(line)
        if not inserted_status and line.strip() == "---":
            # Insert status after this line
            new_lines.append(STATUS_BLOCK)
            inserted_status = True
        if inserted_status and not inserted_toggle and "> [!status]" in line:
            # Insert toggle immediately after status line
            new_lines.append(APPLE_TOGGLE_BLOCK + "\n")
            inserted_toggle = True
    if not inserted_status:
        new_lines.append(STATUS_BLOCK)
    if not inserted_toggle:
        new_lines.append(APPLE_TOGGLE_BLOCK + "\n")
    return "".join(new_lines)

def ensure_definitions(text: str, term: str) -> str:
    # Look for a > [!book] block; if missing, insert after title
    if "> [!book]" not in text:
        # Insert after first header line
        header_match = re.search(r"^# .+$", text, re.MULTILINE)
        insert_pos = header_match.end() if header_match else 0
        defs = f"\n> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: A concise lexical definition of **{term}**, describing its core meaning in standard usage.\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A specialized explanation of **{term}**, highlighting nuanced or domain‑specific aspects.\n"
        text = text[:insert_pos] + defs + text[insert_pos:]
    else:
        # Replace existing definitions with our template
        new_defs = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: A concise lexical definition of **{term}**, describing its core meaning in standard usage.\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: A specialized explanation of **{term}**, highlighting nuanced or domain‑specific aspects."
        text = re.sub(r"(?s)> \[!book\].*?(?=\n> \[!quote\]|$)", new_defs, text)
    return text

def ensure_quotes(text: str, term: str) -> str:
    # Build properly formatted quote block
    quote_block = "\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for author, work in zip(AUTHORS, WORKS):
        quote_block += f"> - 📜 **{author} (*{work}*)**: *\"The **{term}** illustrates the principle of ...\"*\n"
    # Replace existing quote block if present, else append
    if "> [!quote]" in text:
        text = re.sub(r"(?s)> \[!quote\].*?(?=\n---|$)", quote_block, text)
    else:
        text += quote_block
    return text

def process_file(fp: pathlib.Path):
    content = fp.read_text(encoding="utf-8")
    if "latin_root:" not in content.lower():
        return  # skip non‑vocab files
    # Extract term from header
    term_match = re.search(r"^#\s*(.+)$", content, re.MULTILINE)
    term = term_match.group(1).strip() if term_match else fp.stem
    new_content = insert_status_and_toggle(content)
    new_content = ensure_definitions(new_content, term)
    new_content = ensure_quotes(new_content, term)
    if new_content != content:
        fp.write_text(new_content, encoding="utf-8")
        print(f"Fixed {fp.relative_to(ROOT_DIR)}")

def main():
    for root, _, files in os.walk(ROOT_DIR):
        for f in files:
            if f.lower().endswith('.md'):
                process_file(pathlib.Path(root) / f)

if __name__ == "__main__":
    main()
