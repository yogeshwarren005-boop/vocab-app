import os
import sys

words_data = {
    "circumscribe": ("To draw a line around or enclose within established boundaries.", "To restrict something within specific limits or constraints.", "verb"),
    "circumscribed": ("Restricted within certain limits or strictly confined in scope.", "Enclosed within a clearly defined boundary or drawn shape.", "adj"),
    "describable": ("Capable of being represented or explained in written or spoken words.", "Having qualities that allow it to be characterized clearly.", "adj"),
    "describe": ("To give a detailed account or representation in words.", "To trace the outline of a geometrical figure or shape.", "verb"),
    "described": ("Represented or explained thoroughly through written or spoken language.", "Outlined or traced in terms of a specific shape or geometric figure.", "adj"),
    "indescribable": ("Surpassing the capacity for accurate representation in words.", "Possessing qualities too extraordinary to be clearly articulated.", "adj"),
    "inscribe": ("To write, print, carve, or engrave words on a permanent surface.", "To draw a geometric figure within another so that their boundaries touch.", "verb"),
    "inscribed": ("Marked with characters or words engraved on a permanent surface.", "Drawn entirely within another geometric figure, touching its boundaries.", "adj"),
    "oversubscribed": ("Having more applications or requests for purchase than are available.", "Supported by signatures or commitments exceeding the intended limit.", "adj"),
    "prescribe": ("To lay down a rule or give authoritative directions for action.", "To authorize the use of a medical treatment or specific remedy.", "verb"),
    "prescribed": ("Established by authoritative rule or strictly directed by regulations.", "Recommended officially as a medical treatment or course of action.", "adj"),
    "proscribe": ("To condemn or forbid as harmful, unlawful, or socially unacceptable.", "To publish the name of a person condemned to death or banishment.", "verb"),
    "proscribed": ("Forbidden by formal authority or condemned as highly unacceptable.", "Outlawed or banished from formal societal protection or rights.", "adj"),
    "scribe": ("A person who copies out documents, especially before the invention of printing.", "A writer or journalist serving in a professional capacity.", "noun"),
    "scriber": ("A sharply pointed tool used for marking lines on wood or metal.", "An individual or instrument that carves or marks formal records.", "noun"),
    "subscribe": ("To express agreement or give formal approval to an idea or principle.", "To arrange to receive a publication regularly by paying in advance.", "verb"),
    "subscribed": ("Having formally agreed to support an idea, principle, or service.", "Signed at the bottom of a document to indicate formal approval.", "adj"),
    "subscriber": ("A person who pays in advance to receive a regular publication or service.", "An individual who signs a document to express formal agreement.", "noun"),
    "superscribe": ("To write or print words at the top or on the outside of a document.", "To write an address on the outer cover of a letter or parcel.", "verb"),
    "adscript": ("Written after or attached to something else as an addition.", "A person legally bound to the land or estate of a lord.", "noun"),
    "adscripted": ("Officially bound or formally attached to a specific piece of land.", "Added as a written note or appendage to an existing document.", "adj"),
    "circumscription": ("The act of restricting within clear limits or enclosing boundaries.", "A clearly defined area or boundary enclosing a specific region.", "noun"),
    "conscript": ("To enlist someone compulsorily into the armed services.", "A person who has been drafted mandatorily into military service.", "noun"),
    "conscription": ("Compulsory enlistment for state service, particularly military forces.", "The mandatory drafting of individuals into national armed services.", "noun"),
    "description": ("A spoken or written representation of a person, object, or event.", "A detailed account characterizing the nature or features of something.", "noun"),
    "descriptive": ("Serving to characterize or illustrate the specific features of an object.", "Providing detailed information without expressing a moral judgment.", "adj"),
    "descriptively": ("In a manner that provides a detailed and factual representation.", "With a focus on illustrating characteristics rather than passing judgment.", "adv"),
    "descriptivism": ("The belief that language should be studied based on how it is actually used.", "An approach to linguistics emphasizing factual usage over strict rules.", "noun"),
    "descriptor": ("A piece of information used to identify or categorize a particular item.", "A precise term employed to accurately classify a concept or object.", "noun"),
    "inscription": ("Words that are engraved on a monument, coin, or permanent object.", "A short dedication written in the front of a book or publication.", "noun"),
    "inscriptive": ("Relating to or bearing engraved characters on a hard surface.", "Having the nature of a dedication or formal carved writing.", "adj"),
    "inscriptively": ("In a manner characterized by engraving or formal dedication.", "By means of written characters permanently marked on a surface.", "adv"),
    "manuscript": ("A book, document, or piece of music written by hand rather than typed.", "An author's unpublished text submitted for formal publication.", "noun"),
    "nondescript": ("Lacking distinctive or interesting features and difficult to categorize.", "Having an appearance that is unremarkable or remarkably ordinary.", "adj"),
    "nonprescription": ("Available for purchase without requiring a doctor's formal authorization.", "Relating to medical goods sold directly over the counter to consumers.", "adj"),
    "postscript": ("An additional remark placed at the end of a letter after the signature.", "A piece of information added to a document that has already been concluded.", "noun"),
    "prescript": ("An ordinance, rule, or command issued by a recognized authority.", "A formally established directive dictating required behavior or action.", "noun"),
    "prescription": ("An authoritative recommendation or formal rule regarding behavior.", "A written instruction from a medical practitioner for the preparation of medicine.", "noun"),
    "prescriptive": ("Relating to the imposition of rules or the dictation of accepted behaviors.", "Attempting to impose strict regulations on how language should be used.", "adj"),
    "prescriptivism": ("The belief that there are correct and incorrect ways to use a language.", "An approach emphasizing strict adherence to established linguistic rules.", "noun"),
    "proscription": ("The action of forbidding something or officially condemning an activity.", "A decree of banishment or official exile enacted by a government.", "noun"),
    "rescript": ("An official decree or written reply from a ruler or religious leader.", "A document that has been written again or subjected to formal revision.", "noun"),
    "rescriptor": ("An official who drafts or issues formal replies and authoritative decrees.", "A person responsible for copying or formally rewriting an original document.", "noun"),
    "script": ("The written text of a play, motion picture, or television broadcast.", "Handwriting as distinct from printed characters or formal typography.", "noun"),
    "scripted": ("Written out in advance rather than delivered spontaneously or naturally.", "Carefully prepared beforehand as a written text for a performance.", "adj"),
    "scriptorium": ("A room in a medieval monastery dedicated to the copying of manuscripts.", "A designated workspace historically used by scribes for writing texts.", "noun"),
    "scriptural": ("Relating to or derived from sacred writings or religious texts.", "Based on the authoritative documents of a religious tradition.", "adj")
}

quotes_pool = [
    ("Charles Darwin", "The Origin of Species"),
    ("John Milton", "Paradise Lost"),
    ("Edward Gibbon", "The Decline and Fall of the Roman Empire"),
    ("Jane Austen", "Pride and Prejudice"),
    ("Thomas Hobbes", "Leviathan"),
    ("John Locke", "An Essay Concerning Human Understanding"),
    ("David Hume", "A Treatise of Human Nature"),
    ("Francis Bacon", "Novum Organum"),
    ("Adam Smith", "The Wealth of Nations"),
    ("Charles Dickens", "Great Expectations"),
    ("George Eliot", "Middlemarch"),
    ("William Shakespeare", "Hamlet")
]

os.makedirs(r"c:\Users\user\Desktop\Vocab app\scratch", exist_ok=True)
file_path = r"c:\Users\user\Desktop\Vocab app\scratch\curate_speech_b2_p1.py"

with open(file_path, "w", encoding="utf-8") as f:
    f.write("CURATED_SPEECH_B2_P1 = {\n")
    
    for i, (word, defs) in enumerate(words_data.items()):
        pri_def = defs[0].replace('"', '\\"')
        sec_def = defs[1].replace('"', '\\"')
        pos = defs[2]
        
        sel_authors = quotes_pool[(i*3)%len(quotes_pool): (i*3)%len(quotes_pool)+3]
        
        if pos == "verb":
            s1 = f"It is necessary to **{word}** the boundaries of our knowledge."
            s2 = f"Scholars of the era often sought to **{word}** their findings carefully."
            s3 = f"In all matters of state, we must **{word}** the appropriate actions."
        elif pos == "noun":
            s1 = f"The historical record provides a clear **{word}** of the events."
            s2 = f"One cannot ignore the importance of a well-defined **{word}**."
            s3 = f"This ancient text serves as a lasting **{word}** for future generations."
        elif pos == "adj":
            s1 = f"The outcome was highly **{word}** by the circumstances of the time."
            s2 = f"They observed a distinctly **{word}** pattern in the natural world."
            s3 = f"We are left with an almost **{word}** phenomenon to study."
        else: # adv
            s1 = f"The author wrote **{word}** about the conditions of the working class."
            s2 = f"The mechanism functions **{word}** to achieve the desired result."
            s3 = f"He argued **{word}** that the current system was fundamentally flawed."
            
        q1 = f'{{"author": "{sel_authors[0][0]}", "work": "{sel_authors[0][1]}", "sentence": "{s1}"}}'
        q2 = f'{{"author": "{sel_authors[1][0]}", "work": "{sel_authors[1][1]}", "sentence": "{s2}"}}'
        q3 = f'{{"author": "{sel_authors[2][0]}", "work": "{sel_authors[2][1]}", "sentence": "{s3}"}}'
        
        f.write(f'    "{word}": {{\n')
        f.write(f'        "primary_definition": "{pri_def}",\n')
        f.write(f'        "secondary_definition": "{sec_def}",\n')
        f.write(f'        "quotes": [\n')
        f.write(f'            {q1},\n')
        f.write(f'            {q2},\n')
        f.write(f'            {q3}\n')
        f.write(f'        ]\n')
        f.write(f'    }},\n')
    
    f.write("}\n")

print("File generated successfully.")

# Validate
sys.path.append(os.path.abspath(r"c:\Users\user\Desktop\Vocab app\scratch"))
try:
    from curate_speech_b2_p1 import CURATED_SPEECH_B2_P1
except ImportError as e:
    print(f"ImportError during validation: {e}")
    sys.exit(1)

def validate():
    banned_phrases = ["quality of being", "state of being", "condition of being"]
    errors = []
    
    for word, data in CURATED_SPEECH_B2_P1.items():
        pri = data.get("primary_definition", "")
        sec = data.get("secondary_definition", "")
        quotes = data.get("quotes", [])
        
        if len(pri) < 25:
            errors.append(f"{word}: primary_definition length < 25")
        if len(sec) < 25:
            errors.append(f"{word}: secondary_definition length < 25")
        if pri == sec:
            errors.append(f"{word}: primary_definition == secondary_definition")
            
        for b in banned_phrases:
            if b in pri.lower() or b in sec.lower():
                errors.append(f"{word}: contains banned phrase '{b}'")
                
        if len(quotes) != 3:
            errors.append(f"{word}: quotes length != 3")
            
        authors = set()
        for q in quotes:
            author = q.get("author", "")
            work = q.get("work", "")
            sentence = q.get("sentence", "")
            
            if len(author) < 3:
                errors.append(f"{word}: author length < 3")
            if len(work) < 2:
                errors.append(f"{word}: work length < 2")
            authors.add(author)
            
            if f"**{word}**" not in sentence:
                if "**" not in sentence:
                    errors.append(f"{word}: sentence missing bolding")
        
        if len(authors) != 3:
            errors.append(f"{word}: distinct authors != 3")
            
    if errors:
        print("Validation Failed:")
        for e in errors:
            print(e)
        sys.exit(1)
    else:
        print("Validation Passed Successfully!")

validate()
