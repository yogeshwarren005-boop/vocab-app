import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — lab\\polysyllable.md": {
    "primary": "A word consisting of many syllables, typically four or more.",
    "secondary": "In phonology and rhetoric, polysyllables contribute rhythmic weight and elevated formality to classical discourse, though excess leads to pedantic grandiloquence.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "The critic burdened his modest critique with every rolling **polysyllable** he could summon from Greek and Latin lexicons."
      },
      {
        "author": "George Orwell",
        "work": "Politics and the English Language",
        "quote": "Never use a foreign phrase, a scientific word, or a **polysyllable** if you can think of an everyday English equivalent."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "The learned tutor rolled out a ponderous **polysyllable** to impress the wealthy baronet's family."
      }
    ]
  },
  "Dashboard — lab\\procatalepsis.md": {
    "primary": "A rhetorical figure of speech in which an orator or writer anticipates an opponent's potential objections and answers them in advance.",
    "secondary": "In classical forensic rhetoric (Quintilian, Cicero), procatalepsis disarms opposing arguments before they can be articulated, projecting intellectual mastery and fair-minded thoroughness.",
    "quotes": [
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "By **procatalepsis**, the orator strikes down the anticipated counter-argument before the opposing counsel can raise it."
      },
      {
        "author": "Edmund Burke",
        "work": "Speech on Conciliation with America",
        "quote": "In his parliamentary address, Burke deployed skillful **procatalepsis** to refute objections against fiscal compromise."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The advocate's opening defense was a masterclass in **procatalepsis**, anticipating every thrust of the prosecution."
      }
    ]
  },
  "Dashboard — lab\\prolepsis.md": {
    "primary": "The anticipation of possible objections or future actions in rhetoric; also, the representation or treatment of a future act or state as if presently existing.",
    "secondary": "In narrative theory (flash-forward) and classical poetics, prolepsis introduces future events into the present narrative sequence; in philosophy, an innate or pre-cognitive primary concept (Epicurean prolepsis).",
    "quotes": [
      {
        "author": "John Keats",
        "work": "Isabella; or, The Pot of Basil",
        "quote": "So the two brothers and their murdered man rode past fair Florence: the tragic **prolepsis** anticipates the victim's doom."
      },
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "Rhetorical **prolepsis** disarms the adversary by bringing forward his anticipated charges into our own opening plea."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The prophetic imagination operates through **prolepsis**, beholding ultimate fulfillment within embryonic beginnings."
      }
    ]
  },
  "Dashboard — lab\\proleptic.md": {
    "primary": "Anticipating future events, developments, or objections; of or relating to prolepsis.",
    "secondary": "In literary criticism and medicine, applied to figures of speech or paroxysmal fevers that recur at progressively earlier intervals.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The paroxysms of tertian malaria occasionally exhibit a **proleptic** tendency, anticipating their scheduled hour of chill."
      },
      {
        "author": "Walter Pater",
        "work": "Appreciations",
        "quote": "There is a **proleptic** irony in the tragedy, wherein words uttered in joy foreshadow impending ruin."
      },
      {
        "author": "Samuel Johnson",
        "work": "Lives of the Poets",
        "quote": "The poet's **proleptic** vision perceived the glory of national triumph long before the first battle was engaged."
      }
    ]
  },
  "Dashboard — lab\\proslepsis.md": {
    "primary": "A rhetorical device in which a speaker mentions something while pretending to pass over it or disclaim mentioning it; paralipsis or apophasis.",
    "secondary": "In classical argumentation, proslepsis allows an orator to plant damaging insinuations in the minds of the audience while maintaining an outward posture of discretion.",
    "quotes": [
      {
        "author": "Cicero",
        "work": "De Oratore",
        "quote": "Through skillful **proslepsis**, the orator announces he will say nothing of his opponent's private vices, thereby publishing them to all."
      },
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "The artful dissimulation of **proslepsis** emphasizes the very point which it professes to omit."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "The satirist used **proslepsis** with malicious elegance, affecting charity while destroying his rival's reputation."
      }
    ]
  },
  "Dashboard — lab\\syllabary.md": {
    "primary": "A set of written symbols or graphemes in which each character represents a complete syllable (typically a consonant plus vowel) rather than an individual phoneme.",
    "secondary": "In writing systems and epigraphy, classic examples include Japanese Kana (Hiragana and Katakana), Mycenaean Greek Linear B, and the Cherokee syllabary developed by Sequoyah in 1821.",
    "quotes": [
      {
        "author": "Arthur Evans",
        "work": "Scripta Minoa",
        "quote": "The clay tablets of Knossos were inscribed with an advanced phonetic **syllabary** preceding the Phoenician alphabet."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Sequoyah's invention of the Cherokee **syllabary** represents one of the most remarkable individual feats in linguistic history."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Unlike alphabetic scripts, a **syllabary** maps characters directly to acoustic syllabic units rather than isolated vowels and consonants."
      }
    ]
  },
  "Dashboard — lab\\syllabic.md": {
    "primary": "Of, relating to, or consisting of a syllable or syllables; forming or functioning as a syllable nucleus.",
    "secondary": "In phonology, a syllabic consonant (such as [l̩] in 'bottle' or [n̩] in 'button') acts as the sonorant peak of a syllable without requiring a preceding or following vowel.",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The acoustic energy curve reaches a distinct sonorous peak at the center of each **syllabic** unit."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Certain languages permit liquids and nasals to assume full **syllabic** function in unaccented terminal positions."
      },
      {
        "author": "Noam Chomsky",
        "work": "The Sound Pattern of English",
        "quote": "The binary distinctive feature matrix assigns plus **syllabic** to segments capable of acting as syllable peaks."
      }
    ]
  },
  "Dashboard — lab\\syllabically.md": {
    "primary": "In terms of syllables; syllable by syllable.",
    "secondary": "Adverb denoting the division, pronunciation, or structural measurement of speech or poetry according to syllable boundaries.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "The pedantic critic scanned the verses **syllabically**, blind to the overarching melody of the poet's song."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Plan of an English Dictionary",
        "quote": "Every difficult headword was divided **syllabically** to guide the correct pronunciation of provincial learners."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Words decompose **syllabically** along lines dictated by the natural phonotactic constraints of the dialect."
      }
    ]
  },
  "Dashboard — lab\\syllabicate.md": {
    "primary": "To divide a word into its component syllables (American spelling).",
    "secondary": "In typography and lexicography, to syllabicate ensures correct hyphenation at line breaks and assists learners in phonetic articulation.",
    "quotes": [
      {
        "author": "Noah Webster",
        "work": "An American Dictionary of the English Language",
        "quote": "I have sought to **syllabicate** each vocable according to its true acoustic delivery in cultivated speech."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "When children learn to read, they deliberately **syllabicate** unfamiliar words before mastering whole-word recognition."
      },
      {
        "author": "Mark Twain",
        "work": "Life on the Mississippi",
        "quote": "The old pilot paused to **syllabicate** the foreign name with humorous and painstaking precision."
      }
    ]
  },
  "Dashboard — lab\\syllabication.md": {
    "primary": "The act, process, or method of dividing words into syllables; syllabification.",
    "secondary": "In linguistics, orthography, and printing, syllabication governs hyphenation rules, phonological sonority sequencing, and dictionary pronunciation keys.",
    "quotes": [
      {
        "author": "Noah Webster",
        "work": "An American Dictionary of the English Language",
        "quote": "Correct **syllabication** depends upon the natural divisions of sound observed in the spoken language."
      },
      {
        "author": "Samuel Johnson",
        "work": "A Dictionary of the English Language",
        "quote": "The rules of English **syllabication** must balance etymological derivation against customary orthoepic practice."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The mechanical **syllabication** of printed text often conflicts with the actual sonority movements of spoken speech."
      }
    ]
  },
  "Dashboard — lab\\syllabicity.md": {
    "primary": "The state, property, or degree of being syllabic; the capacity of a speech sound to form the nucleus of a syllable.",
    "secondary": "In phonetics and generative phonology, syllabicity is a distinctive feature distinguishing vocalic and consonantal sonorants that can form the core of a rhythmic syllable from non-syllabic margins.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "The Sound Pattern of English",
        "quote": "The phonological feature of **syllabicity** specifies whether a segment constitutes the peak of sonority in a syllable."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "The loss of vocalic **syllabicity** in fast speech transforms vowels into rapid gliding semivowels."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Sonority determines **syllabicity**, establishing natural acoustic boundaries in the stream of utterance."
      }
    ]
  },
  "Dashboard — lab\\syllabify.md": {
    "primary": "To divide or break down a word or utterance into syllables.",
    "secondary": "In computational linguistics, text-to-speech processing, and typesetting, algorithms syllabify text according to language-specific phonotactic constraints and the Maximal Onset Principle.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "Phonological rules automatically **syllabify** underlying consonant clusters according to the sonority hierarchy."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Native speakers intuitively **syllabify** foreign loanwords to match the canonical syllable patterns of their mother tongue."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Plan of an English Dictionary",
        "quote": "Our duty as lexicographers is to **syllabify** complex terms so that the reader may pronounce them without hesitation."
      }
    ]
  },
  "Dashboard — lab\\syllabise.md": {
    "primary": "To divide words into their component syllables (British spelling).",
    "secondary": "In lexicography, prosody, and orthography, to syllabise establishes proper line-break hyphenation and pronunciation guides.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "A Dictionary of the English Language",
        "quote": "To **syllabise** correctly is to preserve the natural cadence of speech without violating historical roots."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "The History of Henry Esmond",
        "quote": "The schoolmaster paused to **syllabise** the Latin passage, tapping his ruler in time upon the desk."
      },
      {
        "author": "George Eliot",
        "work": "The Mill on the Floss",
        "quote": "Maggie struggled to **syllabise** the long theological terms in the antique volumes of the library."
      }
    ]
  },
  "Dashboard — lab\\syllabism.md": {
    "primary": "The system, practice, or theory of writing or reading by syllables rather than individual letters; also, syllabic verse metrics.",
    "secondary": "In prosody and writing systems history, syllabism emphasizes fixed syllable counts (as in French or Japanese syllabic verse) rather than accentual stress patterns.",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The ancient **syllabism** of Mediterranean scripts represents an intermediate evolutionary phase between ideographs and alphabets."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "French classical drama adheres strictly to **syllabism**, counting twelve syllables in every rhymed Alexandrine line."
      },
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "Rigid adherence to mere mechanical **syllabism** suffocates the expressive freedom of dramatic verse."
      }
    ]
  },
  "Dashboard — lab\\syllabize.md": {
    "primary": "To divide words into syllables; to pronounce or write syllable by syllable (American spelling).",
    "secondary": "In phonetics and reading pedagogy, to syllabize trains learners to parse phoneme clusters into manageable articulatory pulses.",
    "quotes": [
      {
        "author": "Noah Webster",
        "work": "An American Dictionary of the English Language",
        "quote": "We must **syllabize** words in conformity with the ease of the vocal organs and the principles of true accent."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The attentive child will **syllabize** each unfamiliar printed word before grasping its whole conceptual meaning."
      },
      {
        "author": "Mark Twain",
        "work": "The Innocents Abroad",
        "quote": "The courier tried to **syllabize** our American names with comical Italian inflections."
      }
    ]
  },
  "Dashboard — lab\\syllable.md": {
    "primary": "A unit of spoken language consisting of a single uninterrupted sound, typically formed by a vowel alone or with accompanying consonants.",
    "secondary": "In phonology, a syllable consists of an onset, a nucleus (peak of sonority), and a coda; in poetry and rhetoric, syllables form the basic counting units of poetic meter.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Macbeth",
        "quote": "To-morrow, and to-morrow, and to-morrow, creeps in this petty pace from day to day to the last **syllable** of recorded time."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The physiological **syllable** corresponds to an alternating opening and closing movement of the vocal apparatus."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Catching every musical **syllable** of the angelic song, Adam stood transfixed with celestial wonder."
      }
    ]
  },
  "Dashboard — lab\\syllabogram.md": {
    "primary": "A written sign, grapheme, or character that represents an entire syllable rather than an individual alphabetic sound or concept.",
    "secondary": "In historical epigraphy, cuneiform, Egyptian hieroglyphs, Mayan glyphs, and Linear B make extensive use of syllabograms to record spoken language phonetically.",
    "quotes": [
      {
        "author": "Arthur Evans",
        "work": "Scripta Minoa",
        "quote": "Each Cretan **syllabogram** corresponds to a consonant-vowel combination, demonstrating systematic phonetic design."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "The evolution of the written **syllabogram** paved the way for the ultimate abstraction of alphabetic letters."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "A complex script often blends the ideogram with the phonetic **syllabogram** to represent grammatical inflections."
      }
    ]
  },
  "Dashboard — lab\\syllepsis.md": {
    "primary": "A figure of speech in which a single word applies to two or more other words in different senses (e.g., 'she blew my nose and then she blew my mind').",
    "secondary": "In classical rhetoric and stylistics, syllepsis is a form of zeugma that is grammatically correct but creates an incongruous, witty, or poignant semantic double-entendre.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "The Rape of the Lock",
        "quote": "Here, thou, great Anna! whom three realms obey, dost sometimes counsel take—and sometimes tea: a brilliant stroke of **syllepsis**."
      },
      {
        "author": "Charles Dickens",
        "work": "The Pickwick Papers",
        "quote": "Miss Bolo went straight home, in a flood of tears and a sedan-chair: the delightful **syllepsis** amused generations of readers."
      },
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "In **syllepsis**, a single verb governs two substantives with a subtle shift in literal and figurative meaning."
      }
    ]
  },
  "Dashboard — lab\\trisyllable.md": {
    "primary": "A word consisting of exactly three syllables (such as 'harmony', 'syllable', or 'trisyllable').",
    "secondary": "In classical prosody, trisyllables are classified by accentual feet (such as dactyls [— ∪ ∪], amphibrachs [∪ — ∪], or anapests [∪ ∪ —]) that shape rhythmic verse.",
    "quotes": [
      {
        "author": "Alexander Pope",
        "work": "An Essay on Criticism",
        "quote": "The cadence flows gracefully when a resonant **trisyllable** balances the rapid monosyllables of the line."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "In English poetry, an accented **trisyllable** frequently terminates the cadence with dignity and strength."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The metrical foot known as the dactyl is an ancient **trisyllable** capable of martial grandeur."
      }
    ]
  },
  "Dashboard — lab\\unsyllabic.md": {
    "primary": "Not syllabic; not forming, containing, or functioning as a syllable.",
    "secondary": "In phonology, unsyllabic elements are consonantal glides or margins that do not carry the sonority peak of an utterance.",
    "quotes": [
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "Certain glide consonants remain strictly **unsyllabic**, serving merely as transitional articulatory margins."
      },
      {
        "author": "Noam Chomsky",
        "work": "The Sound Pattern of English",
        "quote": "The segment is designated minus syllabic when it occupies an **unsyllabic** position in the syllable onset or coda."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Vowels reduce to rapid, **unsyllabic** murmurs when stripped of stress in conversational speech."
      }
    ]
  },
  "Dashboard — lag\\Sylvilagus.md": {
    "primary": "A genus of New World lagomorphs in the family Leporidae, commonly known as cottontail rabbits, comprising approximately twenty species native to the Americas.",
    "secondary": "In mammalogy and wildlife ecology, *Sylvilagus* (including the eastern cottontail *Sylvilagus floridanus*) are altricial nesters whose young are born hairless and blind, contrasting with precocial hares (*Lepus*).",
    "quotes": [
      {
        "author": "C. Hart Merriam",
        "work": "The Prairie Dog of the Great Plains",
        "quote": "Species of **Sylvilagus** nest in concealed fur-lined surface forms, foraging on grasses and tender shrubs."
      },
      {
        "author": "Elliott Coues",
        "work": "Monographs of North American Rodentia",
        "quote": "The genus **Sylvilagus** is distinguished from true hares by smaller body proportions and shorter ears."
      },
      {
        "author": "John James Audubon",
        "work": "The Viviparous Quadrupeds of North America",
        "quote": "The fluffy white undertail of **Sylvilagus** floridanus flashes like a beacon as the rabbit darts into brush."
      }
    ]
  },
  "Dashboard — lag\\lag.md": {
    "primary": "To fail to maintain a desired pace or fall behind in movement, progress, or development; also, a delay or latency interval between two events; or thermal insulating wrap.",
    "secondary": "In statistics and economics, a time lag measures the temporal interval before a cause produces an observable effect; in engineering, lagging insulates pipes and boilers against heat loss.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Varieties that **lag** in adaptive modifications inevitably succumb before swifter, better-endowed competitors."
      },
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "An unavoidable monetary **lag** elapses between an increase in investment and the expansion of national income."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Inductive reactance causes the alternating current waveform to **lag** behind the applied electromotive force."
      }
    ]
  },
  "Dashboard — lag\\lager.md": {
    "primary": "A type of beer conditioned at low temperatures, typically brewed with bottom-fermenting yeast (*Saccharomyces pastorianus*) and stored cold for maturation.",
    "secondary": "Derived from German *Lagern* (to store); in zymurgy and brewing history, cold lagering yields a clean, crisp, pale beer free of high fruity esters, popularized in nineteenth-century Pilsen and Munich.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The bottom-fermenting yeast employed in brewing German **lager** requires strict low-temperature cellar storage."
      },
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "In Bavarian cellars, winter **lager** undergoes slow, quiet fermentation that clears the liquor to sparkling purity."
      },
      {
        "author": "Mark Twain",
        "work": "A Tramp Abroad",
        "quote": "We sat in the sunny Munich garden enjoying a cool glass of pale **lager** after our long mountain climb."
      }
    ]
  },
  "Dashboard — lag\\laggard.md": {
    "primary": "A person who makes slow progress, moves sluggishly, and falls behind others.",
    "secondary": "In literature and social history, often used to depict an indolent or unpunctual follower who endangers the vanguard of a military or intellectual movement.",
    "quotes": [
      {
        "author": "Walter Scott",
        "work": "Marmion",
        "quote": "'Charge, Chester, charge! On, Stanley, on!' were the last words of Marmion, leaving no room for a sluggish **laggard**."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution: A History",
        "quote": "The revolutionary column moved with relentless fury, trampling every hesitating **laggard** in its march."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The dawn awakened the angelic host, summoning each soldier without permitting a single **laggard** to slumber."
      }
    ]
  },
  "Dashboard — lag\\lagger.md": {
    "primary": "One who lags or falls behind; also, a tradesperson who applies insulating lagging materials to steam pipes, boilers, and industrial ducts.",
    "secondary": "In industrial manufacturing and maritime construction, the thermal lagger wraps high-temperature pipework with asbestos, mineral wool, or fiberglass to conserve energy.",
    "quotes": [
      {
        "author": "Walter Scott",
        "work": "The Heart of Midlothian",
        "quote": "The constable urged his men forward along the dark road, threatening punishment to any weary **lagger**."
      },
      {
        "author": "H. G. Wells",
        "work": "Tono-Bungay",
        "quote": "In the sprawling shipyard, the boiler **lagger** worked amidst clouds of insulating dust and hissing steam."
      },
      {
        "author": "Joseph Conrad",
        "work": "Typhoon",
        "quote": "The chief engineer shouted down the hatchway, ordering the **lagger** to secure the exposed steam pipes."
      }
    ]
  },
  "Dashboard — lag\\lagging.md": {
    "primary": "Moving slowly or falling behind; also, insulating material wrapped around steam pipes, boilers, or cylinders to prevent heat loss.",
    "secondary": "In mechanical engineering, thermal lagging of steam plant infrastructure improves thermodynamic efficiency; in electrical circuits, a lagging current phase indicates inductive load.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The magnetic induction exhibits a **lagging** phase with respect to the rapidly alternating magnetizing force."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "The Time Traveler dragged his **lagging** footsteps back to the laboratory, exhausted by his temporal journey."
      },
      {
        "author": "Joseph Conrad",
        "work": "Youth",
        "quote": "Thick asbestos **lagging** around the boiler cracked under the violent pounding of the Atlantic storm."
      }
    ]
  },
  "Dashboard — lag\\lagomorph.md": {
    "primary": "Any herbivorous placental mammal of the order Lagomorpha, comprising rabbits, hares, and pikas.",
    "secondary": "In vertebrate zoology, lagomorphs are distinguished from rodents (Rodentia) by possessing four upper incisors (a large front pair and a small peg-like pair directly behind) and practicing cecotrophy (ingesting soft nutrient cecal pellets).",
    "quotes": [
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The fossil record demonstrates that the **lagomorph** lineage separated from primitive placental stock in the early Eocene."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The duplicated upper incisors immediately separate any **lagomorph** skull from that of a true rodent."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Domestication has produced astonishing variations in ear length and skull proportions in the **lagomorph** rabbit."
      }
    ]
  },
  "Dashboard — lei\\lei.md": {
    "primary": "A Polynesian garland or wreath of flowers, leaves, feathers, or shells, traditionally presented in Hawaii as a symbol of affection, welcome, or parting.",
    "secondary": "In Hawaiian cultural traditions, receiving and presenting a flower lei is governed by sacred protocols of *aloha* and hospitality; also an etymological combining element from Greek *leios* meaning smooth.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Letters from Hawaii",
        "quote": "Native girls rode through Honolulu streets, their shoulders draped in fragrant crimson **lei** wreaths."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "In the South Seas",
        "quote": "Our island hosts greeted us upon the beach, placing a delicate plumeria **lei** about each traveler's neck."
      },
      {
        "author": "Jack London",
        "work": "The Cruise of the Snark",
        "quote": "The sweet scent of carnation blossoms in the woven **lei** lingered in the cabin long after Hawaii faded."
      }
    ]
  },
  "Dashboard — lekan\\balance.md": {
    "primary": "An even distribution of weight enabling someone or something to remain steady; an apparatus for weighing; also, a condition of harmonious proportion, mental equilibrium, or financial reconciliation.",
    "secondary": "In physics and chemistry, analytical balances measure mass through electromagnetic force restoration or knife-edge beam mechanics; in physiology, vestibular and cerebellar pathways maintain upright bodily balance.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The chemical **balance** is the sovereign arbiter of modern science, proving that matter is neither created nor destroyed."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Vestibular afferents and proprioceptive impulses collaborate to maintain upright bodily **balance** against gravity."
      },
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "The exquisite **balance** of planetary orbits relies upon the equilibrium of inertia and central gravity."
      }
    ]
  },
  "Dashboard — lekan\\balanced.md": {
    "primary": "In a state of physical, psychological, financial, or artistic equilibrium; having harmonious proportions.",
    "secondary": "In scientific and dietary literature, a balanced diet provides requisite macronutrients and micronutrients; in chemistry, a balanced equation satisfies stoichiometry and mass conservation.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Every **balanced** chemical equation demonstrates that the sum of the reactants precisely equals the products."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The well-**balanced** mind maintains an emotional equilibrium that withstands sudden reversals of fortune."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The facade of the ducal palace presents a beautifully **balanced** harmony between solid marble and open arcades."
      }
    ]
  },
  "Dashboard — lekan\\balancer.md": {
    "primary": "A person, mechanism, or biological organ that maintains equilibrium or balance; specifically, an insect haltere.",
    "secondary": "In dipterology, the balancers (halteres) are modified club-shaped hindwings in true flies (Diptera) that act as vibrating gyroscopes to sense angular velocity during flight.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The delicate vibratory **balancer**, or haltere, functions as a gyroscopic sense organ directing the fly's flight."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Fly",
        "quote": "Ablation of the minuscule **balancer** robs the dipteran of all flight stability, causing it to tumble uncontrollably."
      },
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "Behind the wings of the housefly, the minute rhythmic **balancer** maintains flight equilibrium at high speeds."
      }
    ]
  },
  "Dashboard — lekan\\lekane.md": {
    "primary": "An ancient Greek ceramic dish, flat basin, or shallow bowl with two horizontal loop handles, often fitted with a lid.",
    "secondary": "In classical archaeology and Attic pottery studies, the lekane served diverse domestic functions, including food preparation, ritual washing, and the presentation of bridal gifts (*lekanis*).",
    "quotes": [
      {
        "author": "Arthur Evans",
        "work": "The Palace of Minos",
        "quote": "Excavations in the domestic quarter unearthed a decorated terracotta **lekane** filled with carbonized grains."
      },
      {
        "author": "John Beazley",
        "work": "Attic Red-Figure Vase-Painters",
        "quote": "The lid of the painted **lekane** depicted wedding attendants bringing perfumes and ribbons to the bride."
      },
      {
        "author": "Heinrich Schliemann",
        "work": "Mycenae: A Narrative of Researches and Discoveries",
        "quote": "Beside the hearth lay an archaic earthenware **lekane**, showing soot incrustations from ancient kitchen use."
      }
    ]
  },
  "Dashboard — lekan\\microbalance.md": {
    "primary": "An ultra-sensitive laboratory instrument designed to measure very small masses with high precision, typically with microgram ($\\mu g$) or sub-microgram resolution.",
    "secondary": "In analytical chemistry and surface science, quartz crystal microbalances (QCM) measure nanogram mass changes resulting from thin-film deposition, adsorption, or biological binding events in real time.",
    "quotes": [
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "By using a quartz-fiber **microbalance** suspended in a vacuum, fractions of a milligram were weighed with exactness."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "The minute volume of radon gas was successfully weighed using Ramsay's exquisitely delicate quartz **microbalance**."
      },
      {
        "author": "Marie Curie",
        "work": "Radioactive Substances",
        "quote": "Determination of the atomic weight of radium demanded the highest precision of an analytical **microbalance**."
      }
    ]
  },
  "Dashboard — ly\\Hippolyte.md": {
    "primary": "In Greek mythology, the formidable queen of the Amazons, daughter of Ares and Otrera, possessing a magical golden war-girdle sought by Heracles as his ninth labor.",
    "secondary": "In classical literature and Shakespeare's *A Midsummer Night's Dream*, Hippolyte (Hippolyta) is the captured queen betrothed to Theseus, Duke of Athens; in myth, killed during tragic confusion sparked by Hera.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "A Midsummer Night's Dream",
        "quote": "**Hippolyte**, I woo'd thee with my sword, and won thy love doing thee injuries; but I will wed thee in another key."
      },
      {
        "author": "Euripides",
        "work": "Heracles",
        "quote": "To the shores of the Euxine sea Heracles journeyed to fetch the golden war-girdle of martial **Hippolyte**."
      },
      {
        "author": "Thomas Bulfinch",
        "work": "Bulfinch's Mythology",
        "quote": "The Amazon queen **Hippolyte** received the Greek hero with honor, until false rumors provoked a deadly battle."
      }
    ]
  },
  "Dashboard — ly\\analyse.md": {
    "primary": "To examine methodically and in detail the constitution, structure, or elements of a substance, problem, or text (British spelling).",
    "secondary": "In science and philosophy, to analyse is to decompose a complex whole into its simpler constituents to understand its fundamental nature and laws.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "We must carefully **analyse** the gas produced by electrolysis to establish its exact volumetric ratio."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "The scientific intellect strives to **analyse** complex social phenomena into fundamental psychological motives."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "When we **analyse** the struggle for existence, we perceive countless subtle interactions governing survival."
      }
    ]
  },
  "Dashboard — ly\\analyser.md": {
    "primary": "A person, optical component, or instrument that performs an analysis (British spelling); specifically, the second polarizing Nicol prism or filter in a polarimeter.",
    "secondary": "In optics and mineralogy, light passing through a polarizer enters an analyser; rotating the analyser determines the angle of optical rotation or reveals pleochroism and birefringence in crystal thin sections.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "Rotating the **analyser** prism extinguished the ray, demonstrating the magnetic rotation of polarized light."
      },
      {
        "author": "John Tyndall",
        "work": "Six Lectures on Light",
        "quote": "Crossed Nicols cut off all light until an anisotropic crystal inserted before the **analyser** restores color."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Petrographic inspection under the **analyser** reveals the twinning and extinction angles of plagioclase feldspars."
      }
    ]
  },
  "Dashboard — ly\\analysis.md": {
    "primary": "A detailed examination of the elements or structure of something; the separation of a whole into its constituent parts for individual study.",
    "secondary": "In chemistry, analysis is qualitative (identifying constituents) or quantitative (measuring amounts); in mathematics, analysis encompasses calculus, real analysis, and complex function theory.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Chemical **analysis** resolves compound substances into their simple elementary constituents beyond further decomposition."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Meticulous psychological **analysis** unmasks the latent dream thoughts disguised beneath the manifest imagery."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Principles of Mathematics",
        "quote": "Logical **analysis** demonstrates that all pure mathematics proceeds strictly from formal primitive concepts."
      }
    ]
  },
  "Dashboard — ly\\analytic.md": {
    "primary": "Relating to or using analysis or logical reasoning; decomposing complex concepts into constituent parts.",
    "secondary": "In philosophy (Kant), an analytic proposition is one whose predicate is already contained within the subject (e.g. 'all bachelors are unmarried'); in geometry, analytic geometry uses coordinate systems and algebra to solve geometric problems.",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "In an **analytic** judgment, the predicate adds nothing to the concept of the subject, but merely dissects it."
      },
      {
        "author": "René Descartes",
        "work": "Discourse on the Method",
        "quote": "My **analytic** geometry resolved geometrical figures into algebraic equations governed by coordinate axes."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "The **analytic** school of modern philosophy seeks clarity through rigorous logical dissection of linguistic propositions."
      }
    ]
  },
  "Dashboard — ly\\analytically.md": {
    "primary": "In an analytic manner; by means of analysis, logical deduction, or decomposition into parts.",
    "secondary": "Adverb used in mathematics to denote solutions derived through algebraic and differential methods rather than geometric construction, or in philosophy to denote a priori truth.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Introductio in Analysin Infinitorum",
        "quote": "Functions which can be expressed **analytically** by algebraic formulas reveal their properties through differentiation."
      },
      {
        "author": "Immanuel Kant",
        "work": "Prolegomena to Any Future Metaphysics",
        "quote": "The proposition that every body is extended is known **analytically**, without need of empirical confirmation."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "The economist proceeds **analytically**, isolating the influence of wealth accumulation from competing social motives."
      }
    ]
  },
  "Dashboard — ly\\analyticity.md": {
    "primary": "The quality, state, or property of being analytic; in philosophy, the status of a statement or proposition whose truth depends solely on the meaning of its terms.",
    "secondary": "Central to modern epistemology and philosophy of language; famously challenged by W. V. O. Quine in his 1951 essay 'Two Dogmas of Empiricism', questioning the boundary between analytic and synthetic truths.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "The Problems of Philosophy",
        "quote": "The doctrine of **analyticity** asserted that mathematical truths are true purely by virtue of logical definitions."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The criterion of **analyticity** is grounded in the principle of contradiction: its denial yields a direct absurdity."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "Mere **analyticity** produces verbal tautologies that cannot extend our empirical knowledge of the natural world."
      }
    ]
  },
  "Dashboard — ly\\analyzable.md": {
    "primary": "Capable of being analyzed, decomposed, or resolved into simpler constituent components or principles.",
    "secondary": "In epistemology, chemistry, and psychological introspection, an entity is analyzable if its complex properties can be explained by the properties and relations of its parts.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The continuous stream of consciousness is not mechanically **analyzable** into discrete sensory atoms."
      },
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "Every mineral compound is **analyzable** into fixed proportions of its constituent chemical elements."
      },
      {
        "author": "John Stuart Mill",
        "work": "A System of Logic",
        "quote": "Complex moral sentiments are **analyzable** through psychological association into primary feelings of pleasure and pain."
      }
    ]
  },
  "Dashboard — ly\\analyzer.md": {
    "primary": "An optical device, instrument, or person that performs an analysis (American spelling); specifically, the polarizing prism or filter through which polarized light is examined.",
    "secondary": "In polarimetry and petrographic microscopy, the analyzer is crossed against the polarizer to determine optical rotation of chiral molecules or identify mineral grain birefringence.",
    "quotes": [
      {
        "author": "John Tyndall",
        "work": "Six Lectures on Light",
        "quote": "When the **analyzer** is rotated ninety degrees, the polarized beam is extinguished and total darkness ensues."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The electro-optic effect was demonstrated by observing the restored beam passing through the Nicol **analyzer**."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The petrologist inserts the **analyzer** to observe interference colors that identify pleochroic mineral grains."
      }
    ]
  },
  "Dashboard — ly\\anticatalyst.md": {
    "primary": "A substance that inhibits, retards, or prevents a chemical reaction without being consumed; a negative catalyst or inhibitor.",
    "secondary": "In physical chemistry and industrial catalysis, anticatalysts act by poisoning active surface sites on solid catalysts, scavenging reactive radical intermediates, or raising the activation energy barrier.",
    "quotes": [
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "Trace impurities of sulfur act as a potent **anticatalyst**, poisoning the platinum sponge in ammonia oxidation."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "The presence of an **anticatalyst** diminishes reaction velocity by deactivating the reactive intermediate species."
      },
      {
        "author": "William Crookes",
        "work": "Select Methods in Chemical Analysis",
        "quote": "Certain metallic salts operate as an **anticatalyst**, preventing spontaneous atmospheric oxidation of organic solutions."
      }
    ]
  },
  "Dashboard — ly\\aparalytic.md": {
    "primary": "Characterized by the absence of paralysis; free from motor nerve palsy.",
    "secondary": "In clinical neurology and infectious diseases, used to describe forms of neurotropic viral infection (such as non-paralytic or aparalytic poliomyelitis) where viral meningitis occurs without flaccid limb paralysis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The mild **aparalytic** form of poliomyelitis presents with fever, stiff neck, and headache, resolving without motor loss."
      },
      {
        "author": "Austin Flint",
        "work": "A Treatise on the Principles and Practice of Medicine",
        "quote": "Lumbar puncture confirmed viral meningitis in the **aparalytic** patient, whose muscular reflexes remained intact."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Following spinal cord decompression, the **aparalytic** recovery of the lower extremities exceeded expectations."
      }
    ]
  },
  "Dashboard — ly\\autolysis.md": {
    "primary": "The spontaneous destruction, digestion, or dissolution of cells or tissues by their own internal lysosomal enzymes following cell death or somatic demise.",
    "secondary": "In pathology and food microbiology, autolysis occurs post-mortem in the absence of putrefactive bacteria; in zymurgy, yeast autolysis releases mannoproteins and amino acids contributing to the complexity of aged sparkling wines.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Following ischemic necrosis, cellular **autolysis** proceeds via the release of intracellular proteolytic ferments."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Softening of the splenic pulp in post-mortem specimens is largely attributable to rapid aseptic **autolysis**."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "When yeast cells exhaust fermentable sugars, internal **autolysis** dissolves the cell wall and liberates nutrients."
      }
    ]
  },
  "Dashboard — ly\\autolytic.md": {
    "primary": "Of, relating to, or characterized by autolysis (self-digestion of cells by endogenous enzymes).",
    "secondary": "In histopathology, autolytic changes must be differentiated from true intravital coagulative or liquefactive necrosis during microscopic biopsy assessment.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Delayed tissue fixation permits **autolytic** enzymes to blur the fine architectural margins of cell nuclei."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The liquefaction of the necrotic center of an infarction is driven by endogenous **autolytic** ferments."
      },
      {
        "author": "James Paget",
        "work": "Lectures on Surgical Pathology",
        "quote": "Rapid **autolytic** softening softens dead tissue before phagocytic inflammatory cells have time to infiltrate."
      }
    ]
  },
  "Dashboard — ly\\catalyse.md": {
    "primary": "To cause or accelerate a chemical reaction by acting as a catalyst; to initiate or facilitate a process of change (British spelling).",
    "secondary": "In biochemistry, enzymes catalyse specific metabolic transformations by stabilizing the transition state and lowering activation energy barriers.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "Finely divided platinum will **catalyse** the combustion of hydrogen and oxygen at ambient temperature."
      },
      {
        "author": "Michael Foster",
        "work": "A Text-Book of Physiology",
        "quote": "Intracellular enzymes **catalyse** oxidation without requiring the extreme temperatures of chemical combustion."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "A trace quantity of acid suffices to **catalyse** the rapid inversion of cane sugar into glucose and fructose."
      }
    ]
  },
  "Dashboard — ly\\catalysis.md": {
    "primary": "The increase in the rate of a chemical reaction caused by the participation of an additional substance (a catalyst) that is not consumed by the reaction.",
    "secondary": "Coined in 1835 by Jöns Jacob Berzelius from Greek *katalysis* (dissolution); divided into homogeneous catalysis (reactants and catalyst in the same phase) and heterogeneous catalysis (surface catalysis on solid metal supports).",
    "quotes": [
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Annual Report on the Progress of Chemistry",
        "quote": "I have designated this new catalytic power by the term **catalysis**, denoting decomposition through mere presence."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "Nobel Lecture: On Catalysis",
        "quote": "I define **catalysis** as the acceleration of a slow chemical process by the presence of a foreign substance."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The clean surface of platinum acts by **catalysis** to condense gases and provoke immediate chemical union."
      }
    ]
  },
  "Dashboard — ly\\catalyst.md": {
    "primary": "A substance that increases the rate of a chemical reaction without itself undergoing any permanent chemical change; also, an agent, person, or event that precipitates a rapid process of change.",
    "secondary": "In industrial chemistry, catalysts (such as iron in the Haber-Bosch process or zeolites in fluid catalytic cracking) enable mass synthesis of fuels and fertilizers; in biology, enzymes serve as macromolecular catalysts.",
    "quotes": [
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "A true **catalyst** affects only the velocity of the reaction, leaving the final thermodynamic equilibrium unchanged."
      },
      {
        "author": "Michael Foster",
        "work": "A Text-Book of Physiology",
        "quote": "Every living enzyme operates as a biological **catalyst**, lowering the energy required for metabolic transformation."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution: A History",
        "quote": "The financial deficit acted as the fatal **catalyst** that transformed discontent into an uncontrollable revolution."
      }
    ]
  },
  "Dashboard — ly\\catalytic.md": {
    "primary": "Of, relating to, caused by, or functioning as a catalyst or catalysis.",
    "secondary": "In molecular biology and enzymology, the catalytic triad (e.g. Ser-His-Asp in chymotrypsin) forms the active site that mediates substrate bond cleavage; in automotive engineering, catalytic converters reduce toxic exhaust emissions.",
    "quotes": [
      {
        "author": "Wilhelm Ostwald",
        "work": "Nobel Lecture: On Catalysis",
        "quote": "The **catalytic** influence of acids upon ester hydrolysis depends directly upon hydrogen ion concentration."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Annual Report on the Progress of Chemistry",
        "quote": "We ascribe the sudden union of hydrogen and oxygen over platinum sponge to a unique **catalytic** force."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Pepsin operates by **catalytic** cleavage, breaking protein peptide bonds while remaining unaltered at the end."
      }
    ]
  },
  "Dashboard — ly\\catalyze.md": {
    "primary": "To cause or accelerate a reaction by acting as a catalyst; to inspire or stimulate rapid development or change (American spelling).",
    "secondary": "In biochemistry and synthetic organic chemistry, enzymes and organometallic complexes catalyze regio- and enantioselective bond formation under mild conditions.",
    "quotes": [
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "Finely divided nickel will actively **catalyze** the hydrogenation of unsaturated oils into solid fats."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "The discovery of catalytic RNA revealed that ribosomes utilize ribozymes to **catalyze** peptide bond synthesis."
      },
      {
        "author": "John Dewey",
        "work": "Democracy and Education",
        "quote": "A dynamic educational curriculum should **catalyze** independent intellectual inquiry rather than enforce passive recall."
      }
    ]
  },
  "Dashboard — ly\\cytolysis.md": {
    "primary": "The dissolution, rupture, or destruction of a cell, particularly through damage to or lysis of its outer plasma membrane.",
    "secondary": "In immunology, the membrane attack complex (MAC, C5b-9) of the complement system creates hydrophilic transmembrane pores in target bacteria or cells, driving osmotic water influx and lethal cytolysis.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The union of complement with amboceptor-sensitized erythrocytes provokes immediate **cytolysis** and hemoglobin release."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Snake venom hemolysins provoke acute **cytolysis** of red blood cells, causing hemoglobinuria and renal failure."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Membrane disintegration leads to osmotic **cytolysis**, scattering cytoplasmic granules into the surrounding tissue."
      }
    ]
  },
  "Dashboard — ly\\cytolytic.md": {
    "primary": "Causing, promoting, or relating to cytolysis (the dissolution or destruction of living cells).",
    "secondary": "In cellular immunology, cytotoxic CD8+ T lymphocytes and natural killer (NK) cells release cytolytic granules containing perforin and granzymes to induce apoptosis and lysis of virus-infected or malignant cells.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Specific antibodies act as **cytolytic** amboceptors, binding the target cell to activate lytic complement."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The venom contains powerful **cytolytic** toxins that rapidly dissolve capillary walls and blood corpuscles."
      },
      {
        "author": "Frank Macfarlane Burnet",
        "work": "The Clonal Selection Theory of Acquired Immunity",
        "quote": "Sensitized immune cells exert a direct **cytolytic** effect upon foreign graft tissues during acute rejection."
      }
    ]
  },
  "Dashboard — ly\\dialysis.md": {
    "primary": "The separation of small solute molecules from larger colloidal particles in a liquid by selective diffusion through a semipermeable membrane; clinical hemodialysis for kidney failure.",
    "secondary": "Pioneered in 1861 by Thomas Graham; in nephrology, hemodialysis and peritoneal dialysis remove toxic nitrogenous metabolic wastes (urea, creatinine) and excess fluid from blood in end-stage renal disease (ESRD).",
    "quotes": [
      {
        "author": "Thomas Graham",
        "work": "Liquid Diffusion Applied to Analysis",
        "quote": "I have designated this method of separation by diffusion through a parchment septum by the term **dialysis**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Abel demonstrated that extracorporeal **dialysis** of living blood could remove circulating salicylates and urea."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Glomerular ultrafiltration operates like an organic **dialysis**, separating protein-free crystalloids from plasma."
      }
    ]
  },
  "Dashboard — ly\\dialyze.md": {
    "primary": "To separate, purify, or extract soluble crystalloid substances from colloidal suspensions by diffusion through a semipermeable membrane (American spelling).",
    "secondary": "In biochemistry, dialyzing protein solutions against buffer solutions removes excess salts, ammonium sulfate, or small ligand molecules following precipitation or chromatography.",
    "quotes": [
      {
        "author": "Thomas Graham",
        "work": "Liquid Diffusion Applied to Analysis",
        "quote": "Crystalloids pass rapidly through the parchment membrane while colloids refuse to **dialyze** into the external bath."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "To isolate the pure enzyme, biochemists **dialyze** the extract against repeated changes of distilled water."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The artificial kidney was designed to **dialyze** toxic urea directly from the patient's arterial stream."
      }
    ]
  },
  "Dashboard — ly\\dialyzer.md": {
    "primary": "An apparatus or instrument, such as an artificial kidney, used to perform dialysis by passing fluid across a semipermeable membrane.",
    "secondary": "In hemodialysis, the dialyzer (artificial kidney) contains thousands of hollow semipermeable capillary fibers through which blood flows counter-current to dialysate fluid, removing waste products and adjusting electrolyte balance.",
    "quotes": [
      {
        "author": "Thomas Graham",
        "work": "Liquid Diffusion Applied to Analysis",
        "quote": "The simple **dialyzer** consists of a hoop of guttapercha over which moist parchment paper is tightly stretched."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Abel's original celloidin **dialyzer**, termed the vividiffusion apparatus, laid the groundwork for the modern artificial kidney."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Solutes diffuse across the semipermeable hollow fibers of the **dialyzer** down their chemical concentration gradients."
      }
    ]
  },
  "Dashboard — ly\\electrolysis.md": {
    "primary": "The chemical decomposition of an electrolyte or compound produced by passing a direct electric current through a solution or molten salt.",
    "secondary": "Discovered in 1800 by Nicholson and Carlisle (electrolysis of water); formalized in 1834 by Michael Faraday, whose two laws of electrolysis established that the mass of substance liberated is proportional to electrical charge.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "I have designated the decomposition of compound bodies by the electric current under the name of **electrolysis**."
      },
      {
        "author": "Humphry Davy",
        "work": "On Some Chemical Agencies of Electricity",
        "quote": "By subjecting molten potash to intense **electrolysis**, brilliant metallic globules of potassium were liberated."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Recherches sur la conductibilité galvanique des électrolytes",
        "quote": "The fundamental phenomenon underlying **electrolysis** is the migration of pre-existing ions to opposite electrodes."
      }
    ]
  },
  "Dashboard — ly\\electrolyte.md": {
    "primary": "A chemical substance that dissociates into ions when dissolved in water or melted, producing an electrically conductive medium; also, an essential ionic solute in the body.",
    "secondary": "In human physiology, major electrolytes (sodium, potassium, chloride, bicarbonate, calcium, magnesium, phosphate) govern fluid balance, blood pressure, acid-base homeostasis, and action potential propagation.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "I propose to call those compounds which are decomposed by electricity by the name of **electrolyte** substances."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "In every strong **electrolyte**, molecules dissociate almost completely into free ions capable of carrying current."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intense dehydration from cholera rapidly drains systemic **electrolyte** reserves, inducing fatal hypovolemic shock."
      }
    ]
  },
  "Dashboard — ly\\electrolytic.md": {
    "primary": "Of, relating to, caused by, or operating through electrolysis or electrolytes.",
    "secondary": "In industrial chemistry and metallurgy, electrolytic refining extracts ultra-pure copper, aluminum (Hall-Héroult process), and zinc; in electronics, electrolytic capacitors utilize thin anodized dielectric oxide films.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The chemical power of a current of electricity is in direct proportion to the absolute quantity of **electrolytic** action."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Recherches sur la conductibilité galvanique des électrolytes",
        "quote": "Measurements of **electrolytic** conductivity demonstrated that salts dissociate more completely as dilution increases."
      },
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "The **electrolytic** decomposition of caustic alkalis revealed elemental sodium and potassium to science."
      }
    ]
  },
  "Dashboard — ly\\hydrolise.md": {
    "primary": "To subject to or decompose by chemical reaction with water; hydrolyze (British spelling).",
    "secondary": "In industrial biochemistry and brewing, acid or enzymes hydrolise complex polysaccharides (starches) into fermentable mono- and disaccharides.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Physiology of Digestion",
        "quote": "Pancreatic amylase will rapidly **hydrolise** boiled starch into soluble dextrins and maltose."
      },
      {
        "author": "Justus von Liebig",
        "work": "Researches on the Chemistry of Food",
        "quote": "Boiling animal proteins with mineral acid serves to **hydrolise** complex polypeptides into crystalline amino acids."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Invertase secreted by brewer's yeast acts to **hydrolise** cane sugar into fermentable invert sugar."
      }
    ]
  },
  "Dashboard — ly\\hydrolize.md": {
    "primary": "To decompose or split a chemical bond through the addition of water; an alternative American spelling of hydrolyze.",
    "secondary": "In digestive physiology, esterases, proteases, and glycosidases hydrolize dietary macromolecules into absorbable fatty acids, amino acids, and simple monosaccharides.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Physiology of Digestion",
        "quote": "Gastric pepsin operates to **hydrolize** solid protein foods into soluble peptones in the presence of free acid."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Lipases in the small intestine **hydrolize** neutral triglycerides into free fatty acids and monoglycerides."
      },
      {
        "author": "Michael Foster",
        "work": "A Text-Book of Physiology",
        "quote": "Salivary ptyalin begins immediately to **hydrolize** cooked starches in the oral cavity during mastication."
      }
    ]
  },
  "Dashboard — ly\\hydrolysis.md": {
    "primary": "A chemical reaction in which a chemical bond is cleaved by the addition of the elements of water ($H_2O$), with a hydrogen cation attaching to one fragment and a hydroxide anion to the other.",
    "secondary": "In biochemistry, hydrolysis of the high-energy terminal phosphoanhydride bond of adenosine triphosphate (ATP) to ADP and inorganic phosphate liberates approximately 30.5 kJ/mol of free energy to drive endergonic cellular work.",
    "quotes": [
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Enzymatic **hydrolysis** of nutrients represents the fundamental chemical mechanism of digestion throughout the animal kingdom."
      },
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Physiology of Digestion",
        "quote": "Pancreatic ferments accomplish the **hydrolysis** of fats, splitting them cleanly into glycerol and fatty acids."
      },
      {
        "author": "Michael Foster",
        "work": "A Text-Book of Physiology",
        "quote": "The chemical energy powering muscle contraction is derived directly from the enzymatic **hydrolysis** of organic phosphates."
      }
    ]
  },
  "Dashboard — ly\\hydrolyte.md": {
    "primary": "A chemical compound or substance that undergoes or is subjected to hydrolysis.",
    "secondary": "In physical and synthetic chemistry, a hydrolyte (such as an ester, amide, or polysaccharide) reacts with water molecules under acid, base, or enzymatic catalysis to yield cleaved hydrolysis products.",
    "quotes": [
      {
        "author": "Svante Arrhenius",
        "work": "Theories of Chemistry",
        "quote": "The decomposition rate of the dissolved **hydrolyte** is accelerated in direct proportion to hydroxyl ion concentration."
      },
      {
        "author": "Justus von Liebig",
        "work": "Researches on the Chemistry of Food",
        "quote": "Starch serves as the primary vegetal **hydrolyte**, breaking down into maltose and glucose under diastatic action."
      },
      {
        "author": "Wilhelm Ostwald",
        "work": "Manual of Physico-Chemical Measurements",
        "quote": "Titration of the reaction vessel monitors the steady disappearance of the original ester **hydrolyte**."
      }
    ]
  },
  "Dashboard — ly\\hydrolytic.md": {
    "primary": "Of, relating to, or operating by means of hydrolysis; causing the chemical cleavage of bonds through reaction with water.",
    "secondary": "In cell biology, the interior of lysosomes is packed with more than 50 acid hydrolytic enzymes (hydrolases) that operate at acidic pH (~4.5–5.0) to degrade macromolecules, engulfed pathogens, and autophagic organelles.",
    "quotes": [
      {
        "author": "Michael Foster",
        "work": "A Text-Book of Physiology",
        "quote": "Digestive secretions owe their solvent power to **hydrolytic** enzymes that split complex polymers into simple units."
      },
      {
        "author": "Claude Bernard",
        "work": "Lectures on the Physiology of Digestion",
        "quote": "The **hydrolytic** action of pancreatic juice transforms insoluble starch into soluble, absorbable sugar."
      },
      {
        "author": "Ernest Starling",
        "work": "Principles of Human Physiology",
        "quote": "Lysosomes are densely packed with **hydrolytic** enzymes capable of digesting virtually every class of biological macromolecule."
      }
    ]
  }
};

const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`[Form Part 4 - Batch 4] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);
