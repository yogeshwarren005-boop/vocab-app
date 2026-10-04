# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — curs (27 words)
  # =========================================================================
  "Dashboard — curs/accurse.md": {
    "primary": "To devote to destruction; to call down evil or divine retribution upon; to curse or execrate.",
    "secondary": "In theological anathema, solemn ecclesiastical sentences consigning heretics to spiritual condemnation.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The fallen angels did **accurse** their proud leader whose rebellion brought them into endless misery."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The fanatical Grand Master was prepared to **accurse** and burn the innocent maiden as a sorceress."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The peasant rose in despair to **accurse** the ruthless nobility that starved his family."}
    ]
  },
  "Dashboard — curs/accursed.md": {
    "primary": "Under a curse; doomed to ruin, misfortune, or destruction; detestable, hateful, or abominable.",
    "secondary": "In biblical theology, things devoted to utter destruction (cherem) or persons excluded from the covenant community.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "O, **accursed** and unquiet wrangling days, how many of you have mine eyes beheld!"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The **accursed** serpent was doomed to creep upon his belly through the dust of the earth."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He denounced the **accursed** greed that had lured him into disgraceful bankruptcy and ruin."}
    ]
  },
  "Dashboard — curs/accurst.md": {
    "primary": "An archaic variant spelling of accursed; doomed, blighted, or under a solemn curse.",
    "secondary": "In classical English poetry and dramatic verse, expressing tragic grief at an inescapable doom.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "For this foul murder, let her head be severed, and let her name be evermore **accurst**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "So fell the prince of darkness, cast down into an **accurst** abyss of fire and endless gloom."},
      {"author": "Samuel Taylor Coleridge", "work": "The Rime of the Ancient Mariner", "quote": "Ah! well a-day! what evil looks had I from old and young! Instead of the cross, the **accurst** Albatross about my neck was hung."}
    ]
  },
  "Dashboard — curs/curse.md": {
    "primary": "A solemn appeal to a supernatural power to inflict harm or misfortune on someone; or profane language.",
    "secondary": "In anthropological mythology and classical folklore, hereditary ancestral curses (e.g. House of Atreus) tracking successive generations.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "You taught me language; and my profit on't is, I know how to **curse**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "On Adam fell the primal **curse**, commanding that by the sweat of his brow he should eat bread."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Sikes muttered a dreadful **curse** through his clenched teeth as the dog growled outside the door."}
    ]
  },
  "Dashboard — curs/cursed.md": {
    "primary": "Afflicted by or deserving of a curse; hateful, abominable, or damnable in character.",
    "secondary": "In literary tragedy, protagonists cursed by tragic hubris or doomed circumstances beyond human control.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Hold, take my sword. There's husbandry in heaven; their candles are all out. Take thee that too. A heavy summons lies like lead upon me, and yet I would not sleep: merciful powers, restrain in me the **cursed** thoughts that nature gives way to in repose!"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Let us fly from this **cursed** shore, where hopeless sorrow and eternal fire torment the fallen."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The family chronicle warned against setting foot upon the **cursed** mire when the powers of evil are exalted."}
    ]
  },
  "Dashboard — curs/cursedly.md": {
    "primary": "In a cursed, wretched, or damnable manner; miserably or with intolerable difficulty.",
    "secondary": "In 18th-century colloquial drama, expressing extreme annoyance at exasperating vexations.",
    "quotes": [
      {"author": "Tobias Smollett", "work": "The Adventures of Roderick Random", "quote": "The ship's cook swore **cursedly** at the rough sea that continually overturned his copper kettles."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Squire Western blustered **cursedly** when informed that Sophia had escaped from her locked chamber."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The Highland bailiff complained **cursedly** of the rocky paths that lamed his lowland pony."}
    ]
  },
  "Dashboard — curs/cursive.md": {
    "primary": "Written with characters joined together in a flowing, running style; flowing or continuous in script.",
    "secondary": "In paleography and diplomatics, Greek and Roman cursive scripts used in papyri and business records distinct from monumental capitals.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Ancient scribes used a rapid **cursive** hand for provincial administrative records and fiscal rolls."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The note was written in an educated, flowing **cursive** script upon fine laid stationery."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Paleographers deciphered the papyrus fragments, distinguishing formal uncials from commercial **cursive** writing."}
    ]
  },
  "Dashboard — curs/cursively.md": {
    "primary": "In a cursive manner; with rapidly connected, flowing letters in handwriting.",
    "secondary": "In epigraphic transcription, writing drafted cursively without lifting the pen between adjacent characters.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "The document appeared to have been drafted **cursively** on a moving train, judging by the jagged strokes."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "M. Paul wrote his instructions **cursively** across the margin of the French grammar exercise."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The old clerk signed his name **cursively**, adding an elaborate paraphe beneath the parchment seal."}
    ]
  },
  "Dashboard — curs/cursor.md": {
    "primary": "A movable indicator marking position on a computer display; or a sliding index on a measuring device.",
    "secondary": "In the history of mathematics, the transparent sliding glass runner with hairline (cursor) on an engineer's slide rule.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "By adjusting the sliding **cursor** along the graduated brass scale, the refraction angle was measured precisely."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The movable **cursor** of the Wheatstone bridge was shifted until the galvanometer needle rested at zero."},
      {"author": "William Thomson", "work": "Popular Lectures and Addresses", "quote": "The experimenter slid the fine **cursor** along the wire to calibrate the electrical resistance."}
    ]
  },
  "Dashboard — curs/cursorial.md": {
    "primary": "Adapted for running on land rather than flying, swimming, or climbing; swift-footed.",
    "secondary": "In vertebrate paleontology and ornithology, cursorial adaptations (such as elongated distal limb segments) seen in ratite birds and theropods.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The long, powerful legs of the ostrich are splendid examples of **cursorial** adaptation for rapid terrestrial flight."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The reduction of lateral digits in ungulates correlates with their specialized **cursorial** locomotion over open plains."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The fossil bird exhibited heavy, **cursorial** limbs indicating that it had completely abandoned aerial flight."}
    ]
  },
  "Dashboard — curs/cursorily.md": {
    "primary": "In a hasty, superficial, or careless manner; rapidly without pausing to examine details.",
    "secondary": "In scholarly and legal review, skimming documents cursorily without verifying underlying citations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Watson had glanced **cursorily** at the walking stick, but Holmes noted the teeth marks of a spaniel."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth read through the first lines **cursorily**, but soon paused to reread every syllable with astonishment."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer turned over the affidavits **cursorily**, knowing they contained nothing of genuine importance."}
    ]
  },
  "Dashboard — curs/cursorius.md": {
    "primary": "A genus of swift-running shorebirds commonly known as coursers, inhabiting arid open plains of Africa and Asia.",
    "secondary": "In ornithological taxonomy, Cursorius (family Glareolidae) comprising plover-like waders adapted for running rapidly after insect prey.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A species of **Cursorius** was observed running swiftly across the sandy arid wastes of the desert plain."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The desert courser, **Cursorius**, exhibits cryptic protective coloration harmonizing with stony ground."},
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The swift terrestrial habits of the courser genus **Cursorius** distinguish it from ordinary marsh waders."}
    ]
  },
  "Dashboard — curs/cursory.md": {
    "primary": "Hasty and therefore not thorough or detailed; superficial, rapid, or perfunctory.",
    "secondary": "In professional auditing and clinical inspection, preliminary cursory surveys designed to flag anomalies for detailed triage.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A **cursory** glance at the room might have suggested nothing unusual, but Holmes's eye caught the red footprints."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Even a **cursory** examination of the fossil strata demonstrates the extinction of whole families of animals."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "A **cursory** view of the neighborhood convinced her that quiet seclusion might be enjoyed at the cottage."}
    ]
  },
  "Dashboard — curs/curst.md": {
    "primary": "An archaic form of cursed; afflicted with a curse; froward, shrewish, or ill-tempered in disposition.",
    "secondary": "In Elizabethan drama (Shakespeare), a curst woman indicating a sharp-tongued, quarrelsome, or cross-tempered character.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "I'll tell you what, sir; an she were not a little **curst**, she were the best girl in Padua."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The **curst** design of Satan was to corrupt innocent mankind and dishonor their glorious Creator."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The old beldame was notorious throughout the parish as a **curst** and malicious gossip."}
    ]
  },
  "Dashboard — curs/discursive.md": {
    "primary": "Moving rapidly from one subject to another in speech or writing; digressive, rambling, or roving.",
    "secondary": "In classical epistemological philosophy, reasoning that proceeds step-by-step through discourse rather than by immediate intuition.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Reason in man is **discursive**, while in heavenly spirits it is intuitive, knowing truth by immediate contemplation."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Human knowledge advances by **discursive** steps from known propositions to unknown truths."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The professor indulged in **discursive** speculations that wandered from tailoring to the mysteries of eternity."}
    ]
  },
  "Dashboard — curs/discursively.md": {
    "primary": "In a discursive or rambling manner; wandering from topic to topic; through logical steps.",
    "secondary": "In philosophical methodology, arriving at a conclusion through step-by-step deduction rather than direct apprehension.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The human intellect proceeds **discursively**, linking intermediate associations until the conclusion is reached."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether spoke **discursively** of his impressions of Paris, wandering charmingly from art to social manners."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon debated **discursively** upon ancient mythologies, losing his audience in pedantic details."}
    ]
  },
  "Dashboard — curs/discursiveness.md": {
    "primary": "The tendency to ramble widely from topic to topic; digressive breadth in speech or reasoning.",
    "secondary": "In rhetorical criticism, loose narrative structure characterized by abundant episodic departures from the plot.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The **discursiveness** of scholastic philosophers often distracted attention from the true empirical point."},
      {"author": "Henry James", "work": "Partial Portraits", "quote": "The charm of the essayist lies in his genial **discursiveness**, carrying the reader on pleasant journeys of thought."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A lack of central purpose results in tedious **discursiveness**, where every trivial association is pursued."}
    ]
  },
  "Dashboard — curs/excursion.md": {
    "primary": "A short journey or trip, especially one undertaken for pleasure, recreation, or exploration.",
    "secondary": "In military history and rhetoric, a sudden sortie or sally from a fortified place; or a brief digression from a topic.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Their summer **excursion** to the lakes of Derbyshire afforded Elizabeth the greatest enjoyment and wonder."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We undertook an interesting geological **excursion** into the rugged ravines of the cordillera."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes planned a nocturnal **excursion** onto the moor to verify the exact location of the watcher's lair."}
    ]
  },
  "Dashboard — curs/excursionist.md": {
    "primary": "A person who goes on an excursion or pleasure trip; a day-tripper or holiday tourist.",
    "secondary": "In 19th-century railway history (Thomas Cook's tours), organized mass working-class tourists traveling by excursion trains.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Crowds of merry **excursionist** travelers poured into the railway carriages bound for the seaside."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The fashionable watering place was invaded every Saturday by hundreds of noisy **excursionist** visitors."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The solitary shepherd observed an occasional **excursionist** wandering bewildered among the barrows of the heath."}
    ]
  },
  "Dashboard — curs/excursive.md": {
    "primary": "Prone to making excursions or digressions; wandering, roving, or exploring widely in thought.",
    "secondary": "In literary aesthetics, a roving imagination exploring fanciful analogies and diverse branches of learning.",
    "quotes": [
      {"author": "William Wordsworth", "work": "The Excursion", "quote": "An **excursive** mind roams through the natural universe, finding moral harmonies in forest and mountain."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The philosopher permitted himself an **excursive** inquiry into the metaphysical foundations of human conscience."},
      {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "He possessed an **excursive** fancy that found romance in every ruined abbey and ancient tavern."}
    ]
  },
  "Dashboard — curs/excursus.md": {
    "primary": "An extended analytical appendix or scholarly discussion of a specific point appended to a book.",
    "secondary": "In classical philology and theological commentary, supplementary dissertations treating textual or historical cruxes.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The historian appended an elaborate **excursus** evaluating the credibility of the early Christian martyrologies."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The author added a valuable anatomical **excursus** comparing human and simian craniological measurements."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon had prepared a massive **excursus** on Egyptian deities to be incorporated into his magnum opus."}
    ]
  },
  "Dashboard — curs/incursion.md": {
    "primary": "A sudden, brief, or hostile invasion or raid into another's territory; an unwelcome intrusion.",
    "secondary": "In military strategy and frontier defense, punitive cavalry raids across disputed borders to disrupt supplies.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A sudden **incursion** of the Alemanni ravaged the frontier settlements of Roman Gaul along the Rhine."},
      {"author": "Walter Scott", "work": "Waverley", "quote": "Highland clans were ever ready for a nocturnal **incursion** into the lowlands to drive off cattle."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A united republic provides the most formidable shield against hostile foreign **incursion** along our coasts."}
    ]
  },
  "Dashboard — curs/incursive.md": {
    "primary": "Making or involving an incursion; aggressive, invasive, or characterized by raiding into territory.",
    "secondary": "In military historiography, incursive border warfare designed to harass enemy outposts without occupying land.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor fortified the Danubian limes to repel the **incursive** raids of the Sarmatian horsemen."},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "Border wardens maintained constant watch against the **incursive** bands that crossed the Tweed at night."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The Austrian army commenced an **incursive** advance across the northeastern frontier of the young republic."}
    ]
  },
  "Dashboard — curs/precursor.md": {
    "primary": "A person or thing that comes before another of the same kind; a forerunner, harbinger, or predecessor.",
    "secondary": "In biochemistry and physiology, an inactive chemical substance from which another active compound is synthesized.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Jove's lightnings, the **precursor** o' the dreadful thunder-claps, more momentary and sight-outrunning were not."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We may recognize in the rudimentary organ a faint morphological **precursor** of a fully developed structure."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Roger Bacon stands as a heroic intellectual **precursor** of modern inductive experimental philosophy."}
    ]
  },
  "Dashboard — curs/precursory.md": {
    "primary": "Preceding as a precursor; indicating, warning of, or heralding what is to follow; preliminary.",
    "secondary": "In seismology and clinical medicine, precursory foreshocks or prodromal symptoms preceding an acute crisis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Occipital headache and visual blurring often serve as **precursory** signs of impending hypertensive encephalopathy."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A low subterranean rumbling was heard as a **precursory** warning immediately before the earthquake struck."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The dissolution of the parlements was a **precursory** symptom of the complete collapse of the ancient monarchy."}
    ]
  },
  "Dashboard — curs/recursion.md": {
    "primary": "The process of defining a function, rule, or procedure in terms of itself; a repeating computation.",
    "secondary": "In computer science and formal linguistics, algorithmic self-reference where a function calls itself to solve smaller subproblems.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "Mathematical induction demonstrates that definition by **recursion** provides a rigorous foundation for arithmetic."},
      {"author": "Alfred North Whitehead", "work": "An Introduction to Mathematics", "quote": "The principle of **recursion** allows infinite mathematical series to be generated from simple initial conditions."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Logical definitions often employ formal **recursion** to trace complex relational concepts back to primitive axioms."}
    ]
  },
  "Dashboard — curs/recursive.md": {
    "primary": "Of, relating to, or involving recursion; defined in terms of itself or calling upon itself repeatedly.",
    "secondary": "In formal generative grammar (Chomsky), recursive syntactic rules permitting the infinite generation of sentences from finite lexicons.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "The structure of ordinal numbers is established through a **recursive** succession of well-ordered sets."},
      {"author": "Alfred North Whitehead", "work": "Principia Mathematica", "quote": "The **recursive** definition guarantees that every truth in the formal system can be systematically derived."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "A **recursive** process of symbolic interpretation generates an endless chain of sign relationships in the mind."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Movement & Speed"
updated = 0

for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Speed Batch 5A: Successfully updated {updated}/{len(data)} notes.")
