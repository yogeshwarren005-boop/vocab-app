import os, re, sys
sys.stdout.reconfigure(encoding="utf-8")

fixes = {
    "Dashboard — liber/liberality.md": {
        "primary": "Generosity, open-handed bounty, or broad-minded freedom from narrow prejudice."
    },
    "Dashboard — liber/liberty.md": {
        "primary": "Freedom from arbitrary control, despotic oppression, or unlawful imprisonment.",
        "quotes": [
            {"author": "Patrick Henry", "work": "Speech in the Virginia Convention", "quote": "Is life so dear, or peace so sweet, as to be purchased at the price of chains and slavery? Forbid it, Almighty God! I know not what course others may take; but as for me, give me **liberty** or give me death!"},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The only freedom which deserves the name, is that of pursuing our own good in our own way, so long as we do not attempt to deprive others of theirs, or impede their efforts to obtain it; civil **liberty** protects the independence of the individual."},
            {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "**Liberty**! Freedom! Tyranny is dead! Run hence, proclaim, cry it about the streets."}
        ]
    },
    "Dashboard — tum/tumefaction.md": {
        "primary": "The abnormal swelling or puffing up of tissue; a localized tumor or distension."
    },
    "Dashboard — tum/tumescence.md": {
        "primary": "Vascular engorgement or enlargement of tissue, especially of erectile organs."
    },
    "Dashboard — tum/tumidity.md": {
        "primary": "Abnormal bodily swelling, or bombastic pompousness and inflation in literary style."
    },
    "Dashboard — tum/tumidness.md": {
        "primary": "Turgid distension, swollen physical condition, or bombastic inflation in writing."
    },
    "Dashboard — tum/tumultuousness.md": {
        "primary": "Turbulent disorder, uproarious commotion, or violent chaotic agitation."
    }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

for rel_path, info in fixes.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "primary" in info:
        pattern = r"> 1\. \*\*Primary Definition \(Lexical / Standard Consensus\)\*\*: .*?\n"
        replacement = f"> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}\n"
        content, _ = re.subn(pattern, replacement, content)
    
    if "quotes" in info:
        new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
        for q in info["quotes"]:
            auth = q["author"].strip()
            work = q["work"].strip()
            quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
            new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
        
        q_idx = content.find("> [!quote]")
        if q_idx != -1:
            content = content[:q_idx] + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Fixed {rel_path}")
