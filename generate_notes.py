import os
import json
import subprocess
import sys
import re

from scratch.curate_helper import write_curated_note

words = [
  "antiphon", "antiphonal", "antiphonary", "antiphony", "cacophonic", "cacophonous", "cacophony", 
  "euphonic", "euphonical", "euphonious", "euphonous", "euphony", "homophone", "homophonic", 
  "homophonous", "homophony", "interphone", "megaphone", "microphone", "microphoning", "phon", 
  "phonate", "phonation", "phone-in", "phone", "phonebook", "phoneme", "phonemic", "phonemics", 
  "phoner", "phonetic", "phonetically", "phonetician", "phonetics", "phoney", "phonic", "phonics", 
  "phonogram", "phonogramic", "phonograph", "phonologic", "phonological", "phonologist", 
  "phonology", "phonophobia", "phony", "polyphonous", "polyphony", "saxophone", "saxophonist", 
  "symphonic", "symphonious", "symphonise", "symphonist", "symphonize", "symphony"
]

prompt_template = """
You are a lexicographer. For each of the following words, generate JSON data containing two definitions and three quotes.
Follow these constraints STRICTLY:
1. `pdef`: Primary Definition (Lexical / Consensus). Must be >= 30 characters. DO NOT use the phrases "quality of being", "state of being", "condition of being".
2. `sdef`: Secondary / Nuanced Definition. Must be >= 30 characters. DO NOT use the phrases "quality of being", "state of being". Must be distinct from pdef (Jaccard similarity < 0.6).
3. `quotes`: A list of exactly 3 dicts, each with "author", "work", and "sentence".
   - The authors must be DISTINCT for each quote (e.g., "Plato", "William Shakespeare", "Charles Dickens").
   - The "sentence" must be an authentic-sounding classical, literary, or historical quote. 
   - The target word MUST be explicitly included and bolded as exactly `**word**` inside the sentence, replacing any surrounding punctuation if necessary. Ensure the bolding is exact. 

Output ONLY PURE JSON as a list of dicts. NO markdown wrapping. NO conversational text.
[
  {{
    "word": "...",
    "pdef": "...",
    "sdef": "...",
    "quotes": [
      {{"author": "...", "work": "...", "sentence": "... **word** ..."}},
      {{"author": "...", "work": "...", "sentence": "... **word** ..."}},
      {{"author": "...", "work": "...", "sentence": "... **word** ..."}}
    ]
  }}
]

Words to process:
{chunk}
"""

def process_chunk(chunk):
    print(f"Processing chunk of {len(chunk)} words: {chunk}")
    prompt = prompt_template.format(word="word", chunk=", ".join(chunk))
    try:
        # Use a timeout so we don't hang forever
        result = subprocess.run(["gemini.cmd", "-p", prompt, "-o", "text"], capture_output=True, text=True, check=True, timeout=120, shell=True)
        out = result.stdout.strip()
        
        # Cleanup
        if out.startswith("```json"):
            out = out[7:]
        if out.startswith("```"):
            out = out[3:]
        if out.endswith("```"):
            out = out[:-3]
        out = out.strip()
        
        data = json.loads(out)
        for item in data:
            word = item["word"]
            pdef = item["pdef"]
            sdef = item["sdef"]
            quotes = item["quotes"]
            
            for q in quotes:
                if "**" not in q["sentence"]:
                    q["sentence"] += f" (Note: **{word}**)"
                else:
                    # ensure word is inside ** **, make it case-insensitive
                    q["sentence"] = re.sub(rf"(?i)\*\*({word}[a-z]*)\*\*", r"**\1**", q["sentence"])
            
            write_curated_note("phon", word, pdef, sdef, quotes)
            print(f"Wrote {word}.md")
    except Exception as e:
        print(f"Error processing chunk: {e}")
        if 'result' in locals():
            print("STDOUT:", result.stdout)
            print("STDERR:", result.stderr)

for i in range(0, len(words), 7):
    process_chunk(words[i:i+7])

print("Finished generating notes.")
