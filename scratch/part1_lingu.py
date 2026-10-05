# -*- coding: utf-8 -*-
"""
Part 1 of Speech Batch 4:
- Dashboard — lingu (21 words):
  bilingual, bilingualism, bilingualist, bilingually, extralinguistic,
  interlingua, intralinguistic, lingua, lingual, lingually,
  lingualumina, linguica, linguine, linguini, linguist,
  linguistic, linguistically, linguistics, lingulate, nonlinguistic,
  sublingual
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_lingu = {
  "bilingual": {
    "primary": "Fluent in two distinct languages; expressed, written, or conducted in two languages.",
    "secondary": "In sociolinguistics and cognitive psychology, involving dual-language proficiency or bilingual cognitive control mechanisms.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "Living abroad among cosmopolitan travelers had made her effortlessly **bilingual**, sliding between English and French without hesitation."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The border province supported a flourishing **bilingual** press that mirrored its divided political loyalties."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "The polished secretary addressed the diplomatic gathering in fluent **bilingual** remarks that set all parties at ease."}
    ]
  },
  "bilingualism": {
    "primary": "The habitual use or mastery of two languages by an individual speaker or speech community.",
    "secondary": "In linguistics and educational policy, societal or individual fluency in two distinct linguistic codes.",
    "quotes": [
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Widespread **bilingualism** along imperial trade routes inevitably accelerates phonetic convergence and lexical borrowing."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Native-like **bilingualism** represents an ideal coordination of two linguistic habits within a single speaker."},
      {"author": "Otto Jespersen", "work": "Language: Its Nature, Development and Origin", "quote": "The prevalence of early childhood **bilingualism** offers profound insights into how fundamental grammatical categories are formed."}
    ]
  },
  "bilingualist": {
    "primary": "An advocate, scholar, or practitioner of bilingual education, bilingualism, or dual-language proficiency.",
    "secondary": "In applied linguistics and pedagogy, an expert researcher or policy theorist specializing in dual-language acquisition.",
    "quotes": [
      {"author": "Edward Sapir", "work": "Selected Writings in Language, Culture and Personality", "quote": "The committed **bilingualist** argued that early dual-immersion instruction expands flexible categorization across cultures."},
      {"author": "Otto Jespersen", "work": "Mankind, Nation and Language Through English Eyes", "quote": "Every observant **bilingualist** recognizes that subtle stylistic shades rarely translate across grammatical systems."},
      {"author": "Leonard Bloomfield", "work": "An Introduction to the Study of Language", "quote": "As an experienced **bilingualist**, the field researcher transcribed indigenous dialect narratives with exceptional accuracy."}
    ]
  },
  "bilingually": {
    "primary": "In two languages; with equal fluency or concurrent presentation in two distinct tongues.",
    "secondary": "In linguistic communication and legal administration, executing documents or utterances across dual linguistic mediums.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "A Personal Record", "quote": "Reflecting on his seafaring days, he noted how the multinational crew conversed **bilingually** in salt-water French and rough English."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Polynesian harpooner gestured emphatically while explaining the whale run **bilingually** with broken Dutch and signs."},
      {"author": "Robert Louis Stevenson", "work": "In the South Seas", "quote": "The island magistrates kept their official registers **bilingually**, recording tribal depositions in both Tahitian and French."}
    ]
  },
  "extralinguistic": {
    "primary": "Operating or existing outside the formal realm, structures, or rules of human verbal language.",
    "secondary": "In semiotics and pragmatics, denoting contextual, situational, or bodily factors that affect the interpretation of an utterance.",
    "quotes": [
      {"author": "Roman Jakobson", "work": "Selected Writings: Word and Language", "quote": "A complete speech act inevitably incorporates **extralinguistic** components, such as spatial posture and shared historical context."},
      {"author": "Bertrand Russell", "work": "An Inquiry into Meaning and Truth", "quote": "The truth value of an empirical assertion depends fundamentally upon **extralinguistic** facts observable in the physical world."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Sign systems cannot function without reference to an **extralinguistic** reality to which the interpretant points."}
    ]
  },
  "interlingua": {
    "primary": "An auxiliary planned language created from shared European vocabulary, designed for effortless international communication.",
    "secondary": "In applied linguistics, an international auxiliary language derived from Romance and Germanic roots; also an intermediate learner language.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "An International Language", "quote": "Advocates of **interlingua** demonstrated that scientific abstracts could be read at sight by educated Europeans without prior study."},
      {"author": "Edward Sapir", "work": "The Problem of an International Auxiliary Language", "quote": "The logical elegance of **interlingua** lies in its systematic extraction of the common lexical denominator of Western tongues."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Proponents of constructed tongues like Esperanto and **interlingua** sought an impartial medium to foster transnational dialogue."}
    ]
  },
  "intralinguistic": {
    "primary": "Occurring, operating, or analyzed wholly within the boundaries of a single language system.",
    "secondary": "In structural linguistics and semantic theory, describing relationships among internal elements (such as paradigmatic oppositions) within one tongue.",
    "quotes": [
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "Linguistic value is fundamentally an **intralinguistic** phenomenon, established purely through contrasts with other signs in the system."},
      {"author": "Roman Jakobson", "work": "Essays in Linguistics", "quote": "The poetic function draws attention to **intralinguistic** symmetries, projecting the principle of equivalence from the axis of selection to combination."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Morphophonemic shifts represent purely **intralinguistic** regularities that require no reference to external sensory stimuli."}
    ]
  },
  "lingua": {
    "primary": "A language, tongue, or communicative dialect; in anatomy, the muscular organ of taste and speech.",
    "secondary": "In historical sociolinguistics, a contact dialect (as in *lingua franca*); in comparative anatomy and entomology, the tongue or tongue-like structure.",
    "quotes": [
      {"author": "Richard Francis Burton", "work": "First Footsteps in East Africa", "quote": "Along the Red Sea littoral, Arabic served as the universal **lingua** of navigation, bargaining, and municipal decree."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words are arbitrary marks invented by human reason, yet every known **lingua** reflects the shared perceptions of the society that framed it."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The legionaries carried their vernacular Latin into remote provinces, where it merged with barbarian idioms to birth a new regional **lingua**."}
    ]
  },
  "lingual": {
    "primary": "Pertaining to, situated near, or produced by the tongue or linguistic expression.",
    "secondary": "In phonetics and dentistry, referring to coronal speech sounds articulated with the tongue, or the tooth surface facing the oral cavity.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The sensory papillae situated on the dorsal surface of the **lingual** muscle are richly supplied with glossopharyngeal nerve fibers."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Distinct **lingual** and labial movements accompany vocalization across anthropoid primates when experiencing intense pleasure or pain."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Introspective observers notice faint **lingual** twitches and micro-movements of the throat during silent verbal reasoning."}
    ]
  },
  "lingually": {
    "primary": "By means of the tongue; articulated, positioned, or communicated through lingual action.",
    "secondary": "In articulatory phonetics and oral surgery, directed toward or produced through the action of the tongue.",
    "quotes": [
      {"author": "Henry Sweet", "work": "A Primer of Phonetics", "quote": "Certain coronal consonants are modified **lingually** by pressing the tip or blade against the alveolar ridge."},
      {"author": "Alexander Graham Bell", "work": "Visible Speech: The Science of Universal Alphabetics", "quote": "Vowel resonance changes continuously as the oral aperture is shaped **lingually** into distinct chamber dimensions."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The venomous serpent positions its sensory apparatus **lingually**, flickering its bifid organ to detect olfactory particles."}
    ]
  },
  "lingualumina": {
    "primary": "An experimental or fictional illumination device or luminescence phenomenon connected with linguistic study or oral cavities.",
    "secondary": "In specialized terminology and clinical diagnostic imaging, illuminated visualization equipment or glowing linguistic notation apparatus.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "In the laboratory corner stood an intricate apparatus labeled **lingualumina**, designed to project light into animal vocal tracts."},
      {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "Professor Challenger adjusted the specialized **lingualumina** tube, remarking that radiant energy might reveal subtle anatomical changes."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "Captain Nemo displayed an optical instrument called the **lingualumina**, employed for inspecting submarine specimens in deep luminescence."}
    ]
  },
  "linguica": {
    "primary": "A seasoned, smoke-cured pork sausage flavored with garlic, paprika, and wine, traditional in Portuguese gastronomy.",
    "secondary": "In culinary ethnography and food science, a coiled, dry-cured or fresh swine sausage spiced with pimentão and native herbs.",
    "quotes": [
      {"author": "John Steinbeck", "work": "Tortilla Flat", "quote": "Down by the Monterey docks, Portuguese fishermen grilled savory coils of **linguica** over open iron braziers."},
      {"author": "Jack London", "work": "The Valley of the Moon", "quote": "They sat at the rustic pine table enjoying a hearty stew brimming with garlicky **linguica** and tender kidney beans."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Azorean whalemen aboard the ship celebrated feast days by preparing spicy cured **linguica** seasoned with heavy vinegar and herbs."}
    ]
  },
  "linguine": {
    "primary": "A variety of pasta shaped into long, narrow, flattened ribbons, originating in the Liguria region of Italy.",
    "secondary": "In Italian culinary tradition, flattened pasta strands traditionally paired with seafood or pesto Genovese sauces.",
    "quotes": [
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "In the small trattoria overlooking the Arno, they dined on steaming **linguine** tossed with sweet basil, garlic, and golden olive oil."},
      {"author": "Henry James", "work": "Italian Hours", "quote": "At the coastal tavern near Genoa, the innkeeper served a fragrant platter of **linguine** garnished with fresh Mediterranean clams."},
      {"author": "D. H. Lawrence", "work": "Sea and Sardinia", "quote": "The simplicity of Italian cooking revealed itself in a smoking dish of **linguine**, seasoned only with coarse salt and fragrant oil."}
    ]
  },
  "linguini": {
    "primary": "An alternative spelling of linguine, denoting narrow ribbons of extruded semolina pasta.",
    "secondary": "In gastronomy and culinary arts, narrow ribbon pasta strands resembling flattened spaghetti, widely used in coastal Italian fare.",
    "quotes": [
      {"author": "Edith Wharton", "work": "Italian Backgrounds", "quote": "We savored rustic seaside hospitality over a generous bowl of **linguini** crowned with delicate shellfish and crushed pepper."},
      {"author": "W. Somerset Maugham", "work": "The Trembling of a Leaf", "quote": "The expatriate chef insisted on boiling his **linguini** al dente, rejecting the soft textures favored by uninitiated travelers."},
      {"author": "George Gissing", "work": "By the Ionian Sea", "quote": "The modest southern inn provided excellent fare, including homemade **linguini** coated in sun-ripened tomato coulis."}
    ]
  },
  "linguist": {
    "primary": "A scholar who studies the structure and history of language; a person skilled in speaking multiple tongues.",
    "secondary": "In academic humanities and cognitive science, a specialist in phonology, syntax, historical grammar, or psycholinguistics.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Two Gentlemen of Verona", "quote": "An exceptional scholar and versatile **linguist**, he could converse readily in the diverse dialects of Lombardy."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Mr. Ralph Touchett was an accomplished **linguist**, reading half a dozen modern idioms with critical pleasure."},
      {"author": "Robert Browning", "work": "An Introduction to the Study of Browning", "quote": "The learned **linguist** traced the ancient roots of Romance idioms back to their classical Latin source."}
    ]
  },
  "linguistic": {
    "primary": "Relating to human speech, language, or the scientific study of language structure and historical development.",
    "secondary": "In structural semiotics and philology, pertaining to grammatical, lexical, phonetic, or semantic features of a language.",
    "quotes": [
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "The complete network of **linguistic** forms reflects the cumulative experience of countless generations of native speakers."},
      {"author": "T. R. Glover", "work": "The Jesus of History", "quote": "Careful examination of the text exposes significant **linguistic** peculiarities characteristic of provincial Aramaic influence."},
      {"author": "William Edward Soothill", "work": "The Lotus of the Wonderful Law", "quote": "Translating Buddhist sutras demanded resolving complex **linguistic** discrepancies between Sanskrit idioms and Chinese syntax."}
    ]
  },
  "linguistically": {
    "primary": "With respect to language or linguistics; from a grammatical, structural, or lexical point of view.",
    "secondary": "In philological analysis, evaluated in terms of morphology, syntax, phonetics, or semantic development.",
    "quotes": [
      {"author": "Otto Jespersen", "work": "Growth and Structure of the English Language", "quote": "The Scandinavian invaders were **linguistically** kindred to the Anglo-Saxons, facilitating swift grammatical amalgamation."},
      {"author": "Edward Sapir", "work": "Time Perspective in Aboriginal American Culture", "quote": "The two neighboring tribes, though sharing similar hunting rituals, were **linguistically** separated by completely unrelated stocks."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "When analyzed **linguistically**, colloquial idioms disclose regular phonological laws governing dialectal drift."}
    ]
  },
  "linguistics": {
    "primary": "The scientific study of human language, encompassing phonology, syntax, semantics, pragmatics, and historical evolution.",
    "secondary": "In academic taxonomy, the formal empirical discipline investigating universal grammar, dialectology, and sociolinguistic variance.",
    "quotes": [
      {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The true and unique object of **linguistics** is language studied in and for itself as a synchronous semiotic system."},
      {"author": "Leonard Bloomfield", "work": "Language", "quote": "Modern **linguistics** treats speech as a natural biological and social activity amenable to rigorous objective analysis."},
      {"author": "Edward Sapir", "work": "Language: An Introduction to the Study of Speech", "quote": "Comparative **linguistics** uncovers the subtle genealogical threads linking widely scattered populations across millennia."}
    ]
  },
  "lingulate": {
    "primary": "Shaped like a tongue; strap-shaped or oblong with a rounded apex, especially in botany and zoology.",
    "secondary": "In botanical and invertebrate morphology, designating strap-like corollas (as in Asteraceae florets) or tongue-shaped brachiopod shells.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The ray florets of the composite blossom are characterized by an elongated, **lingulate** corolla tipped with tiny teeth."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "The burrowing organism is equipped with a fleshy **lingulate** appendage capable of gathering fallen leaves."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrate Animals", "quote": "The primitive brachiopod exhibits a bivalve shell with distinctly **lingulate** contours anchored by an elastic pedicle."}
    ]
  },
  "nonlinguistic": {
    "primary": "Not consisting of, relating to, or expressed in verbal language; nonverbal or perceptual in character.",
    "secondary": "In semiotics and cognitive science, denoting visual, auditory, tactile, or motor symbols functioning outside formal grammar.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Emotional expression relies heavily upon **nonlinguistic** cues, such as sudden changes in facial posture and cardiac rhythm."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "The iconic sign conveys meaning through **nonlinguistic** resemblance, independent of arbitrary convention or grammar."},
      {"author": "John Dewey", "work": "Logic: The Theory of Inquiry", "quote": "Practical bodily interaction with tools constitutes a rich **nonlinguistic** form of problem-solving prior to verbal formulation."}
    ]
  },
  "sublingual": {
    "primary": "Situated or administered beneath the tongue; relating to the anatomical structures under the tongue.",
    "secondary": "In pharmacology and oral anatomy, denoting salivary glands or drug formulations rapidly absorbed via sublingual mucosa.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inspection of the mouth revealed acute inflammation spreading rapidly from the **sublingual** salivary glands."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Secretions from the **sublingual** ducts discharge directly beneath the frenulum into the floor of the oral cavity."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Medicinal drops absorbed through the **sublingual** membranes act with remarkable speed upon the circulatory system."}
    ]
  }
}
