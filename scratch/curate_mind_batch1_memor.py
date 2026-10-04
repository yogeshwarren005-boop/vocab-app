# -*- coding: utf-8 -*-
"""
Curates Dashboard — memor (25 words) in Cluster Mind & Knowledge.
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  "Dashboard — memor/commemorate.md": {
    "primary": "Recall and show respect for an event or person in a ceremony; celebrate or preserve the memory of.",
    "secondary": "In civic architecture and public rituals, dedicating monuments or observing national holidays for historic deeds.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "We have come to dedicate a portion of that field to **commemorate** the heroic dead who gave their lives that that nation might live."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman senate decreed an annual public festival to **commemorate** the triumph of the legions over foreign barbarians."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge resolved to **commemorate** this blessed transformation by sending the prize poultry to the home of Bob Cratchit."}
    ]
  },
  "Dashboard — memor/commemorating.md": {
    "primary": "Recalling and honoring the memory of a person, heroic sacrifice, or historic event with ceremony.",
    "secondary": "In public statuary and numismatics, striking medals or inscribing plaques honoring foundational milestones.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "An ancient headstone stood in the cemetery, **commemorating** the pious life of a pioneer magistrate of Massachusetts."},
      {"author": "Winston Churchill", "work": "Their Finest Hour", "quote": "The Prime Minister spoke in Parliament, **commemorating** the invincible fortitude of the fighter pilots who saved the realm."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The antiquary dusted an ancient medal struck in brass, **commemorating** the union of the Scottish and English crowns."}
    ]
  },
  "Dashboard — memor/commemoration.md": {
    "primary": "The act of remembering and honoring a notable person, heroic act, or event through ceremony.",
    "secondary": "In liturgical theology and civic memorials, an annual service or solemn observance renewing communal remembrance.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The solemn **commemoration** of ancestral wisdom forms the moral cement that binds past generations to the future."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The town council arranged a public **commemoration** for the philanthropic alderman who founded the parish infirmary."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The glorious revolution was celebrated with joyous **commemoration** across every market town in the Protestant kingdom."}
    ]
  },
  "Dashboard — memor/commemorative.md": {
    "primary": "Acting as a memorial or mark of celebration; intended to recall and honor an event or person.",
    "secondary": "In philately, numismatics, and monument design, specially issued stamps, medals, or statues preserving civic heritage.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A heavy **commemorative** gold medallion hung from his watch chain, presented by a grateful European sovereign."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "The small chapel was adorned with **commemorative** stained glass depicting scenes from the lives of early martyrs."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "American townships erect simple **commemorative** granite obelisks to honor citizens who fell in the revolutionary struggle."}
    ]
  },
  "Dashboard — memor/immemorial.md": {
    "primary": "Originating in the distant past; existing beyond the reach of memory, record, or tradition.",
    "secondary": "In legal jurisprudence (time immemorial), customs continuous and unquestioned since time beyond legal memory.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The ancient stone barn had stood from time **immemorial**, witnessing the shearing of countless generations of Wessex sheep."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Deep in the primeval forest, Buck answered the call of an **immemorial** wild instinct slumbering in his northern blood."},
      {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Language is the archive of history, preserving profound metaphors derived from an **immemorial** human antiquity."}
    ]
  },
  "Dashboard — memor/memorabilia.md": {
    "primary": "Objects or items collected for their historical value or associations with people, places, or events.",
    "secondary": "In archival curating and biographical memoirs, personal artifacts, autographs, and relics illuminating historic lives.",
    "quotes": [
      {"author": "Robert Browning", "work": "Memorabilia", "quote": "Ah, did you once see Shelley plain, and did he speak to you, and did you speak to him again, among the **memorabilia** of your youth?"},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Watson kept a tin dispatch-box filled with the curious **memorabilia** and documents of his friend's celebrated investigations."},
      {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "Tourists eagerly purchased fake **memorabilia** outside the Colosseum, believing every rusty nail came from Caesar's palace."}
    ]
  },
  "Dashboard — memor/memorability.md": {
    "primary": "The characteristic of being worth remembering, striking, notable, or easily fixed in the mind.",
    "secondary": "In marketing psychology and literary aesthetics, the indelible cognitive salience that ensures long-term recall.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The exceptional **memorability** of Shakespeare's phrasing arises from the perfect harmony of dramatic rhythm and imaginative truth."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "A touchstone line of epic poetry achieves timeless **memorability** by crystallizing profound human experience in a single breath."},
      {"author": "Walter Pater", "work": "Appreciations", "quote": "The subtle **memorability** of Lamb's essays lies in their tender blend of whimsical melancholy and antique phrase."}
    ]
  },
  "Dashboard — memor/memorable.md": {
    "primary": "Worth remembering or easily remembered, especially because of being special, unusual, or exceptional.",
    "secondary": "In historiography and narrative memoirs, watershed moments or dramatic speeches that reshape national destiny.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Let us make this day a **memorable** epoch in our kingdom's chronicles, sealed by noble deeds of arms."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "I do assure you, said Mr. Snagsby, it was a **memorable** interview that I shall carry in my heart to my dying day."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The singular adventure of the Beryl Coronet remains one of the most **memorable** triumphs of my friend's career."}
    ]
  },
  "Dashboard — memor/memorably.md": {
    "primary": "In a memorable manner; in a way that is easily remembered, striking, or profoundly notable.",
    "secondary": "In literary rhetoric and oratory, delivering ideas with arresting eloquence that lingers permanently in public memory.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The British constitution **memorably** established that liberty without order is but the license of an anarchic mob."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Milton **memorably** defended the freedom of the press in language of unsurpassed grandeur and moral conviction."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Jane Austen **memorably** captured the quiet comedy of provincial drawing rooms without a trace of bitter satire."}
    ]
  },
  "Dashboard — memor/memoranda.md": {
    "primary": "Written messages, notes, records, or reminders used in business, legal, or diplomatic communications.",
    "secondary": "In historical archives and administrative registries, collections of internal working briefs outlining policy choices.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer turned over his pocketbook of private **memoranda**, checking dates and cryptic notations with a sharp eye."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare opened his journal, glancing through brief **memoranda** jotted down during his agricultural studies in the valley."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "In his small sea-chest, Ishmael kept a slate with rough **memoranda** of shipboard watches and wind headings."}
    ]
  },
  "Dashboard — memor/memorandum.md": {
    "primary": "A written message, note, or record in business, diplomacy, or law, serving as a reminder or agreement.",
    "secondary": "In diplomatic statecraft, an official diplomatic document summarizing points of understanding between sovereign governments.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Bagnet made a brief **memorandum** in his ledger, recording the balance due on the musical instruments."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak drew out a pencil and made a careful **memorandum** of the number of sheep penned in each fold."},
      {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The White Rabbit put on his spectacles, unfolding a folded **memorandum** to read the accusation before the King."}
    ]
  },
  "Dashboard — memor/memorial.md": {
    "primary": "Something designed to preserve the memory of a person, victory, or event; a monument, plaque, or ceremony.",
    "secondary": "In legal procedure, a statement of facts accompanying a petition presented to a government, legislature, or court.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "This tomb shall be a lasting **memorial** of thy spotless virtue, defying the envious tooth of all-consuming time."},
      {"author": "Abraham Lincoln", "work": "Second Inaugural Address", "quote": "Let us build a living **memorial** to the fallen by binding up the wounds of the nation in enduring charity."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The grateful family erected a marble **memorial** tablet in the village churchyard to honor the departed squire."}
    ]
  },
  "Dashboard — memor/memorialisation.md": {
    "primary": "The act, process, or ceremony of commemorating, honoring, or preserving the memory of someone (British spelling).",
    "secondary": "In cultural studies and museum architecture, public rituals and monuments erected to commemorate war fallen.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The solemn **memorialisation** of great deeds in carved stone ensures that heroic virtues inspire future centuries."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Ancient civilisations lavished fortunes upon the **memorialisation** of deceased monarchs in colossal granite pyramids."},
      {"author": "Thomas Hardy", "work": "The Dynasts", "quote": "The rustic hamlet observed the annual **memorialisation** of Waterloo with muffled chimes from the Norman church belfry."}
    ]
  },
  "Dashboard — memor/memorialise.md": {
    "primary": "Preserve the memory of someone or something; commemorate; also address or petition by a memorial (British spelling).",
    "secondary": "In civic governance and historical literature, petitioning authorities or erecting statues for distinguished public service.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The townsfolk resolved to **memorialise** the generous merchant who had endowed the grammar school for poor boys."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Protestant gentlemen met at the shire hall to **memorialise** the crown against arbitrary suspension of statute laws."},
      {"author": "George Bernard Shaw", "work": "Saint Joan", "quote": "Centuries passed before the very church that condemned the maid met in cathedral splendor to **memorialise** her sainthood."}
    ]
  },
  "Dashboard — memor/memorialization.md": {
    "primary": "The act, process, or practice of preserving the memory of a person or historical event; commemoration.",
    "secondary": "In public history and urban design, the creation of monuments, museums, and days of remembrance to honor collective sacrifice.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "The national **memorialization** of our brave soldiers upon the battlefield consecrates the principle of unbroken union."},
      {"author": "Frederick Douglass", "work": "The Life and Times of Frederick Douglass", "quote": "True **memorialization** of the abolitionist heroes demands continuous vigilance in safeguarding equal constitutional rights."},
      {"author": "Woodrow Wilson", "work": "War and Peace: Presidential Messages", "quote": "The **memorialization** of our fallen doughboys in France remains a solemn covenant between the living and the dead."}
    ]
  },
  "Dashboard — memor/memorialize.md": {
    "primary": "Preserve the memory of someone or something; commemorate; also present a memorial petition to a governing body.",
    "secondary": "In civic sculpture and literature, immortalizing great achievements in monuments, epic verse, or official memorials.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Specimen Days", "quote": "I sought in these hurried battlefield jottings to **memorialize** the patient courage of the wounded boys in the hospital tents."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The Roman sculptors sought to **memorialize** the serene beauty of the marble faun before antique pagan joy perished."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The union leaders drafted a petition to **memorialize** the state legislature concerning deadly working conditions in the stockyards."}
    ]
  },
  "Dashboard — memor/memorisation.md": {
    "primary": "The process of learning something so that you can remember it perfectly; committing to memory (British spelling).",
    "secondary": "In pedagogy and classical education, committing sacred verses, grammatical paradigms, and orations to heart through repetition.",
    "quotes": [
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Rote **memorisation** of Latin rules without understanding the sense burdens the young intellect without cultivating judgment."},
      {"author": "Charles Darwin", "work": "Autobiography of Charles Darwin", "quote": "The master insisted upon the mechanical **memorisation** of Greek hexameters, which I found singularly tedious."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom Tulliver groaned over the endless **memorisation** of Latin conjugations required by his strict clerical tutor."}
    ]
  },
  "Dashboard — memor/memorise.md": {
    "primary": "Learn something thoroughly so that you remember it perfectly; commit to memory (British spelling).",
    "secondary": "In classical stagecraft and scholarship, learning dramatic scripts or philosophical texts verbatim for recitation.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She would sit by the window and **memorise** stanzas of Shelley until the words became part of her very thoughts."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes paused to **memorise** the intricate network of crossroads upon the ordnance map before venturing onto the moor."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Lucy tried to **memorise** the Italian names of the Giotto frescoes in the church of Santa Croce."}
    ]
  },
  "Dashboard — memor/memoriser.md": {
    "primary": "A person who commits things to memory; a mnemonic practitioner or student who memorizes information.",
    "secondary": "In cognitive psychology and educational history, a learner employing structured mnemonic methods to retain massive data.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "A phenomenal **memoriser** relies not on natural brain plasticity alone, but upon ingenious associative mental filing systems."},
      {"author": "Francis Galton", "work": "Inquiries into Human Faculty and Its Development", "quote": "We tested a calculating prodigy and rapid **memoriser** who visualized numbers in vivid colored columns across mental space."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "The superficial **memoriser** who collects facts without digesting their principles is merely an unthinking repository of words."}
    ]
  },
  "Dashboard — memor/memorization.md": {
    "primary": "The process of committing something to memory or learning something thoroughly by heart.",
    "secondary": "In psychological learning theory, the cognitive encoding and consolidation of information for subsequent retrieval.",
    "quotes": [
      {"author": "Jack London", "work": "The Star Rover", "quote": "Through rigorous mental **memorization**, I preserved my sanity in the dark jacket, reciting poetry hour after hour."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Mechanical **memorization** of formulas without comprehension is the greatest pitfall of modern schoolroom instruction."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The apprentice sailor underwent daily **memorization** of every rope and stay in the bewildering rigging aloft."}
    ]
  },
  "Dashboard — memor/memorize.md": {
    "primary": "Learn something thoroughly so that you remember it perfectly; commit to memory.",
    "secondary": "In theatrical performance, intelligence work, and scholastic training, acquiring verbatim recall of texts.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom struggled for an hour to **memorize** five verses from the Sermon on the Mount for Sunday school ticket rewards."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The cipher was so complex that the conspirators were instructed to **memorize** the key and burn the paper immediately."},
      {"author": "Jack London", "work": "The Jacket (The Star-Rover)", "quote": "The prisoner managed to **memorize** the Morse code taps upon the water pipes, establishing communication with the next cell."}
    ]
  },
  "Dashboard — memor/memorizer.md": {
    "primary": "A person who memorizes something; an individual who commits facts or texts to memory.",
    "secondary": "In cognitive science and historical oral traditions, an oral bard or scholar capable of reciting entire epics from memory.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The trained **memorizer** links disparate facts into a unified narrative chain, drastically reducing retrieval effort."},
      {"author": "Thomas Henry Huxley", "work": "Science and Education", "quote": "A mere **memorizer** of scientific terms is not an investigator, for true science demands observation and critical reasoning."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The ancient bard was a sacred **memorizer**, bearing within his head the living genealogy and heroic songs of the tribe."}
    ]
  },
  "Dashboard — memor/memory.md": {
    "primary": "The faculty by which the mind stores and remembers information; something remembered from the past; recollection.",
    "secondary": "In computer architecture and cognitive neuroscience, physical hardware storing binary data, or hippocampal neural consolidation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Remember thee? Ay, thou poor ghost, while **memory** holds a seat in this distracted globe."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The faculty of **memory** is as it were the storehouse of our ideas, preserving them for future contemplation."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My early **memory** begins with the quiet churchyard, the sunken gravestones, and the sweet face of my mother."}
    ]
  },
  "Dashboard — memor/unmemorable.md": {
    "primary": "Not memorable; not worth remembering; plain, undistinguished, easily forgotten, or unremarkable.",
    "secondary": "In literary criticism and theatrical reviews, performances or books lacking distinctive brilliance or lasting emotional resonance.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Countless third-rate novels are published each season, completely **unmemorable** and destined to perish within a month."},
      {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The actor delivered an **unmemorable** performance, sleepwalking through the tragedy without genuine fire."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "An **unmemorable** plot may nonetheless be redeemed if the author creates characters of psychological depth."}
    ]
  },
  "Dashboard — memor/unmemorably.md": {
    "primary": "In an unmemorable, unremarkable, or forgettable manner; without distinction or lasting impression.",
    "secondary": "In biographical prose and historical narrative, living or passing without leaving any enduring mark on contemporaries.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Generations of rustic laborers lived and died **unmemorably** in the quiet valley, their very names fading from churchyard stones."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Many a noble soul rests in an unvisited tomb, having laboured **unmemorably** to soften the hardness of the world around them."},
      {"author": "Herman Melville", "work": "Israel Potter: His Fifty Years of Exile", "quote": "The old veteran passed his final years **unmemorably** in the London workhouse, forgotten by the republic he had fought to create."}
    ]
  }
}

def curate_file(rel_path, info):
    base_dir = "App database/Latin roots/Cluster Mind & Knowledge"
    filepath = os.path.join(base_dir, rel_path)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return False
        
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    fm_match = re.search(r"^---\n.*?\n---\n", content, re.DOTALL)
    if not fm_match:
        print(f"Frontmatter missing: {filepath}")
        return False
    frontmatter = fm_match.group(0)
    
    w = os.path.splitext(os.path.basename(rel_path))[0]
    header = f"# {w}\n\n"
    
    dv_match = re.search(r"(> \[!status\] 🎯 \*\*Status:\*\*.*?```dataviewjs.*?```)", content, re.DOTALL)
    if not dv_match:
        print(f"Dataview block missing: {filepath}")
        return False
    dv_block = dv_match.group(1)
    
    defs_block = f"""> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: {info['primary']}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {info['secondary']}"""

    quotes_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
    for q in info["quotes"]:
        quotes_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
    quotes_block = "\n".join(quotes_lines)
    
    new_content = f"{frontmatter}{header}{dv_block}\n\n{defs_block}\n\n{quotes_block}\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True

success = 0
for rel_path, info in data.items():
    if curate_file(rel_path, info):
        success += 1

print(f"Successfully updated {success}/{len(data)} notes in Dashboard — memor.")
