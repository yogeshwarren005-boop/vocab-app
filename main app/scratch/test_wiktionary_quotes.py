import urllib.request, json, re

def get_wiktionary_citations(word):
    url = f"https://en.wiktionary.org/w/api.php?action=parse&page={urllib.parse.quote(word)}&prop=wikitext&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": "VocabAppCitationBot/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            wikitext = data.get("parse", {}).get("wikitext", {}).get("*", "")
            
            # Find quote templates: {{quote-book|...}}, {{quote-journal|...}}, {{quote-web|...}}, {{quote|...}}, {{quote-news|...}}
            # or lines starting with #* or #*:
            quotes = []
            
            # Match {{quote-book ... }} or {{quote-journal ... }}
            pat_tmpl = re.compile(r'\{\{quote-(book|journal|news|web|song|text)[^}]+\}\}', re.DOTALL | re.IGNORECASE)
            for m in pat_tmpl.finditer(wikitext):
                raw = m.group(0)
                # extract author, title/work, quote/passage
                author_m = re.search(r'\|(?:author|last|first|editor)=([^|}]+)', raw)
                title_m = re.search(r'\|(?:title|work|journal)=([^|}]+)', raw)
                passage_m = re.search(r'\|(?:passage|quote|text)=([^|}]+)', raw)
                
                author = author_m.group(1).strip() if author_m else None
                title = title_m.group(1).strip() if title_m else None
                passage = passage_m.group(1).strip() if passage_m else None
                
                if author and passage:
                    # clean wikitext brackets
                    clean_passage = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', passage)
                    clean_passage = re.sub(r"'''?", "", clean_passage)
                    clean_title = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', title) if title else "Published Work"
                    quotes.append((author, clean_title, clean_passage))
                    
            # Also check for #* lines (Wiktionary standard citation line)
            # e.g. #* '''year''', author, ''title''...
            lines = wikitext.split("\n")
            for idx, line in enumerate(lines):
                if line.startswith("#*") and not line.startswith("#*:"):
                    # the citation metadata is here, and next line #*: is often the passage!
                    # check next line
                    passage_line = ""
                    if idx + 1 < len(lines) and lines[idx+1].startswith("#*:"):
                        passage_line = lines[idx+1].lstrip("#*: ")
                    elif line.count("'''") >= 2:
                        passage_line = line
                    if passage_line:
                        clean_passage = re.sub(r'\[\[(?:[^|\]]*\|)?([^\]]+)\]\]', r'\1', passage_line)
                        clean_passage = re.sub(r"'''?", "", clean_passage)
                        # extract author if possible
                        m_auth = re.search(r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b", line)
                        auth_name = m_auth.group(1) if m_auth else "Literary Source"
                        quotes.append((auth_name, "Attested Usage", clean_passage))
                        
            return quotes
    except Exception as e:
        print(f"Error fetching {word}: {e}")
        return []

test_words = ['proactive', 'interactive', 'reactive', 'hyperactivity', 'overreact']
for w in test_words:
    qs = get_wiktionary_citations(w)
    print(f"=== Citations for {w} ({len(qs)} found) ===")
    for a, t, p in qs[:3]:
        print(f"  {a} (*{t}*): {p[:90]}...")
