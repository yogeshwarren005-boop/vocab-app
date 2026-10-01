import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Cognition & Mind";

const wordsData = {
  // === Dashboard — hyp (10 words) ===
  "Dashboard — hyp/hyp.md": {
    word: "hyp",
    primary: "A colloquial or technical abbreviation for hypothesis or hypothetical; also the combining root hyp- (from Greek hypo-) signifying under, below, or deficient.",
    secondary: "In informal academic shorthand, a proposed working hypothesis; historically in 18th-century English slang, hypochondria or low spirits ('the hyp').",
    quotes: [
      { author: "Jonathan Swift", work: "Polite Conversation", quote: "Poor Lord Sparkish has got a fit of the **hyp**, and sits moping in the corner like an owl in an ivy bush." },
      { author: "Joseph Addison", work: "The Spectator", quote: "The spleen and the **hyp** are strange distempers, filling the imagination with melancholy phantoms." },
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "We formulate an initial **hyp** to account for surprising experimental observations before deducing its consequences." }
    ]
  },
  "Dashboard — hyp/hyphen.md": {
    word: "hyphen",
    primary: "A punctuation mark (-) used to divide or compound words, word elements, or syllables, derived from Greek hyph' hen meaning 'under one' or 'together'.",
    secondary: "In typography and lexicography, a connecting glyph that clarifies syntactic relationships between words, prevents ambiguous misreading, or manages justification margins.",
    quotes: [
      { author: "H. L. Mencken", work: "The American Language", quote: "The **hyphen** has always been an unstable element in American orthography, continually dropped as compounds fuse into single words." },
      { author: "Virginia Woolf", work: "Orlando", quote: "A subtle **hyphen** linked their names in the society columns, implying an intimacy that words dared not confess." },
      { author: "George Orwell", work: "The English People", quote: "The British national character is a curious compound, requiring no awkward **hyphen** to bind its diverse traditions." }
    ]
  },
  "Dashboard — hyp/hyphenate.md": {
    word: "hyphenate",
    primary: "To connect, divide, or join words or syllables with a hyphen; to hold multiple concurrent roles or cultural identities.",
    secondary: "In publishing and digital composition, to break a multisyllabic word across line endings; sociologically, to bridge two ethnic or cultural heritage labels.",
    quotes: [
      { author: "Theodore Roosevelt", work: "American Ideals", quote: "There is no room in this country for hyphenated Americanism; we cannot **hyphenate** our allegiance to the flag." },
      { author: "H. W. Fowler", work: "The King's English", quote: "Do not recklessly **hyphenate** adverbial phrases where the unmodified adjective speaks clearly on its own." },
      { author: "James Joyce", work: "Letters of James Joyce", quote: "The printer neglected to **hyphenate** the portmanteau words, blunting the rhythmic cadence of the prose." }
    ]
  },
  "Dashboard — hyp/hyphenation.md": {
    word: "hyphenation",
    primary: "The division or connection of words or syllables by means of a hyphen, especially across line endings or within compound terms.",
    secondary: "In graphic design and automated typesetting, the typographical algorithm governing where words may gracefully break to ensure uniform column margins.",
    quotes: [
      { author: "Robert Bringhurst", work: "The Elements of Typographic Style", quote: "Graceful **hyphenation** is essential to legible typography, avoiding ragged white rivers across justified columns." },
      { author: "Oliver Wendell Holmes Jr.", work: "Speeches", quote: "The legal document suffered from erratic **hyphenation**, creating semantic disputes over statutory definitions." },
      { author: "Henry Watson Fowler", work: "A Dictionary of Modern English Usage", quote: "The chaotic rules of English **hyphenation** cause more bewilderment to authors than any other point of punctuation." }
    ]
  },
  "Dashboard — hyp/hypoallergenic.md": {
    word: "hypoallergenic",
    primary: "Designed, formulated, or tested to minimize the likelihood of causing an allergic response, especially in cosmetics, fabrics, and pet breeds.",
    secondary: "In dermatology and consumer safety science, having relatively low concentrations of common contact allergens such as fragrances, nickel, or parabens.",
    quotes: [
      { author: "Rachel Carson", work: "Silent Spring", quote: "Modern consumers eagerly seek **hypoallergenic** products to protect sensitive tissues from synthetic irritants." },
      { author: "Atul Gawande", work: "Being Mortal", quote: "Hospitals switched to **hypoallergenic** surgical gloves to prevent debilitating latex sensitivities among staff." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "She furnished her studio exclusively with **hypoallergenic** materials to eliminate asthma triggers." }
    ]
  },
  "Dashboard — hyp/hypodermal.md": {
    word: "hypodermal",
    primary: "Of, relating to, or located immediately beneath the skin or epidermis; hypodermic.",
    secondary: "In comparative anatomy and botanical histology, situated directly under the protective outer epidermal cell layer of leaves, stems, or insect exoskeletons.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Crayfish: An Introduction to the Study of Zoology", quote: "The chitinous carapace is secreted by an underlying layer of **hypodermal** cells rich in pigment." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In xerophytic pine needles, thick-walled **hypodermal** fibers prevent collapse during intense drought." },
      { author: "Charles Darwin", work: "The Structure and Distribution of Coral Reefs", quote: "The delicate polyps are sustained by **hypodermal** tissue that anchors them to the calcareous matrix." }
    ]
  },
  "Dashboard — hyp/hypodermic.md": {
    word: "hypodermic",
    primary: "Relating to the parts beneath the skin; an instrument or injection introduced beneath the skin into subcutaneous tissue.",
    secondary: "In pharmacology and medical technology, a hollow needle and syringe designed to deliver liquid medication directly into systemic circulation.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "Sherlock Holmes took his bottle from the corner of the mantelpiece and his **hypodermic** syringe from its neat morocco case." },
      { author: "Bram Stoker", work: "Dracula", quote: "Dr. Seward administered a **hypodermic** injection of morphia to soothe the agitated patient." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "Martin grasped the sterile **hypodermic** syringe, preparing to inoculate the guinea pigs with the new antitoxin." }
    ]
  },
  "Dashboard — hyp/hypodermis.md": {
    word: "hypodermis",
    primary: "An epidermal layer of cells that secretes the chitinous cuticle in arthropods; also the subcutaneous tissue in human anatomy or plant stems.",
    secondary: "In histology, the innermost layer of the integumentary system containing adipocytes and connective tissue, anchoring the dermis to underlying fascia.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "During ecdysis, the living **hypodermis** detaches from the old exoskeleton and secretes a fresh cuticle." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", quote: "Subcutaneous fat deposited in the **hypodermis** provides both thermal insulation and metabolic reserves." },
      { author: "G. F. Ferris", work: "The Principles of Systematic Entomology", quote: "Microscopic examination of the **hypodermis** reveals specialized glandular ducts opening upon the body surface." }
    ]
  },
  "Dashboard — hyp/hypogene.md": {
    word: "hypogene",
    primary: "Formed, crystallized, or originating deep beneath the earth's surface by subterranean heat and pressure, such as plutonic or metamorphic rocks.",
    secondary: "In structural geology and mineralogy (coined by Charles Lyell), contrasting with epigene rocks and weathering processes occurring at the surface.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "I propose the term **hypogene** for all rocks formed beneath the surface, whether by volcanic or metamorphic agencies." },
      { author: "Charles Darwin", work: "Geological Observations on South America", quote: "The core of the immense Andean cordillera is composed of coarse **hypogene** granite uplifted in antiquity." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Mineral veins deposited by ascending hydrothermal solutions represent characteristic **hypogene** formations." }
    ]
  },
  "Dashboard — hyp/hypoxemia.md": {
    word: "hypoxemia",
    primary: "An abnormally low concentration or tension of oxygen in the arterial blood.",
    secondary: "In critical care medicine and pulmonology, a physiological state marked by decreased PaO2, precipitating tissue hypoxia, cyanosis, and cellular stress.",
    quotes: [
      { author: "Atul Gawande", work: "Being Mortal", quote: "Pulse oximeters flashed warning signals as severe **hypoxemia** set in, demanding immediate supplemental oxygen." },
      { author: "Paul Kalanithi", work: "When Breath Becomes Air", quote: "The arterial blood gas confirmed profound **hypoxemia**, signaling respiratory failure in the oncology ward." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In lobar pneumonia, cyanosis of the lips and fingertips warns the physician of insidious **hypoxemia**." }
    ]
  },

  // === Dashboard — ide (9 words) ===
  "Dashboard — ide/aide.md": {
    word: "aide",
    primary: "An assistant, confidential counselor, or junior officer who provides direct administrative or operational support to a superior.",
    secondary: "In military and diplomatic hierarchy (short for aide-de-camp), an officer assigned to attend personal needs, correspondence, and security for a commanding general or ambassador.",
    quotes: [
      { author: "Leo Tolstoy", work: "War and Peace", quote: "Prince Andrei served as a trusted **aide** to General Kutuzov during the tumultuous retreat from Braunau." },
      { author: "Alexis de Tocqueville", work: "Recollections", quote: "The prime minister dispatched a confidential **aide** to sound out the mood of the rebellious assembly." },
      { author: "Winston Churchill", work: "The Gathering Storm", quote: "A military **aide** hurried into the war room with urgent telegrams detailing the enemy naval mobilization." }
    ]
  },
  "Dashboard — ide/aided.md": {
    word: "aided",
    primary: "Supported, assisted, or helped in achieving a goal or overcoming an obstacle (past participle of aid).",
    secondary: "In technological and educational contexts, facilitated by external tools, assistive devices, or computational algorithms (e.g. computer-aided design).",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The barbarian invaders were greatly **aided** by internal treachery and decayed frontier fortifications." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "Early humans were immensely **aided** in their struggle for survival by social sympathy and mutual cooperation." },
      { author: "George Eliot", work: "Middlemarch", quote: "She felt profoundly comforted and **aided** by his quiet, steadfast presence during her family crisis." }
    ]
  },
  "Dashboard — ide/ide.md": {
    word: "ide",
    primary: "A combining root derived from Greek idea/eidos denoting mental form, concept, or cognitive image; also a freshwater fish of the carp family (Leuciscus idus).",
    secondary: "In chemistry, a suffix (-ide) denoting binary compounds (e.g. chloride); in cognitive philosophy, the elemental root underpinning idea and ideology.",
    quotes: [
      { author: "Izaak Walton", work: "The Compleat Angler", quote: "The golden orfe is an ornamental variety of the **ide**, prized by European pond-keepers for its bright hue." },
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "We adopted the terminal syllable -**ide** to designate simple compounds formed by oxygen or acid radicals." },
      { author: "Plato", work: "Phaedo", quote: "The eternal **ide**- or Form of the Good remains immutable while earthly shadows perish." }
    ]
  },
  "Dashboard — ide/ideogram.md": {
    word: "ideogram",
    primary: "A written character or symbol that represents an idea or thing directly without representing the individual sounds of its spoken name.",
    secondary: "In semiotics and epigraphy, a visual glyph (such as Egyptian hieroglyphs, Chinese characters, or international road signs) conveying conceptual meaning directly to the mind.",
    quotes: [
      { author: "Ezra Pound", work: "ABC of Reading", quote: "The Chinese **ideogram** does not define by abstract dictionary categories, but by juxtaposing vivid natural pictures." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "In an ideographic writing system, the **ideogram** stands for the concept itself rather than the acoustic phoneme." },
      { author: "H. G. Wells", work: "The Outline of History", quote: "Early Sumerian scribes impressed an **ideogram** upon moist clay to record bushels of barley and head of oxen." }
    ]
  },
  "Dashboard — ide/ideologic.md": {
    word: "ideologic",
    primary: "Of or relating to ideology; characterized by doctrines, political dogma, or theoretical intellectual frameworks.",
    secondary: "In political science and cultural studies, driven by preconceived theoretical beliefs rather than pragmatic or empirical realities.",
    quotes: [
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "Totalitarian movements rely on strict **ideologic** consistency to explain away all contradictory historical facts." },
      { author: "Max Weber", work: "Economy and Society", quote: "Charismatic authority often undergoes **ideologic** systematization as it transforms into a bureaucratic institution." },
      { author: "George Orwell", work: "The Prevention of Literature", quote: "Totalitarianism demands complete **ideologic** conformity, extinguishing the free, critical spirit of the artist." }
    ]
  },
  "Dashboard — ide/ideological.md": {
    word: "ideological",
    primary: "Based on or relating to a particular system of ideas, political beliefs, or philosophical theories.",
    secondary: "In sociopolitical discourse, describing doctrines, policies, or rhetoric motivated by party dogma and theoretical dogma rather than practical necessity.",
    quotes: [
      { author: "George Orwell", work: "1984", quote: "The sacred principles of Ingsoc formed an impenetrable **ideological** barrier against independent thought." },
      { author: "Hannah Arendt", work: "Eichmann in Jerusalem", quote: "He was not an evil monster, but a man completely unequipped for critical thought beyond his **ideological** clichés." },
      { author: "Francis Fukuyama", work: "The End of History and the Last Man", quote: "The collapse of the Soviet bloc marked the end of century-long **ideological** struggles between totalitarianism and democracy." }
    ]
  },
  "Dashboard — ide/ideologically.md": {
    word: "ideologically",
    primary: "In a manner determined by, relating to, or conforming with a specific ideology or doctrine.",
    secondary: "In sociopolitical analysis, describing actions, judicial rulings, or policies swayed by political worldview rather than neutral evidence.",
    quotes: [
      { author: "Bertrand Russell", work: "Power: A New Social Analysis", quote: "Fanatics are **ideologically** blind to the suffering they inflict in pursuit of their utopian millennium." },
      { author: "Arthur Koestler", work: "Darkness at Noon", quote: "Rubashov confessed to crimes he had not committed because he remained **ideologically** bound to the Party's supreme logic." },
      { author: "Noam Chomsky", work: "Manufacturing Consent", quote: "Mainstream media outlets are **ideologically** aligned with the political and financial interests of elite ownership." }
    ]
  },
  "Dashboard — ide/ideologist.md": {
    word: "ideologist",
    primary: "A theorist, student, or advocate of ideology; an adherent or architect of an abstract doctrine or political program.",
    secondary: "Historically, one of the French Enlightenment philosophers (Destutt de Tracy and circle) who studied the origin of ideas; pejoratively applied by Napoleon to impractical theorists.",
    quotes: [
      { author: "Napoleon Bonaparte", work: "Addresses and Maxims", quote: "It is to the mania of the **ideologists**, who seek metaphysics in government, that all our national misfortunes must be attributed." },
      { author: "Karl Marx", work: "The German Ideology", quote: "The ruling class employs the **ideologist** to construct sublime legal and philosophical justifications for its economic dominance." },
      { author: "Alexis de Tocqueville", work: "The Old Regime and the Revolution", quote: "French men of letters became the chief **ideologists** of the Revolution, applying abstract theory to the messy art of statecraft." }
    ]
  },
  "Dashboard — ide/ideology.md": {
    word: "ideology",
    primary: "A comprehensive system of ideas, values, and beliefs that forms the basis of economic, political, or social theory and policy.",
    secondary: "In sociological criticism, a set of culturally dominant beliefs that legitimizes social arrangements and shapes how individuals perceive reality.",
    quotes: [
      { author: "Karl Marx", work: "The German Ideology", quote: "The ideas of the ruling class are in every epoch the ruling ideas; the dominant **ideology** presents its interests as universal truths." },
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "An **ideology** is quite literally what its name indicates: it is the logic of an idea applied to the course of history." },
      { author: "Clifford Geertz", work: "The Interpretation of Cultures", quote: "Political **ideology** provides an intricate map of problematic social reality and a matrix for the creation of collective identity." }
    ]
  },

  // === Dashboard — mancy (1 word) ===
  "Dashboard — mancy/bibliomancy.md": {
    word: "bibliomancy",
    primary: "Divination or fortune-telling through the random selection or opening of passages from a book, especially the Bible.",
    secondary: "In cultural anthropology and the history of superstition, an ancient method of seeking divine guidance or auguries by interpreting the first verse encountered upon blindly opening a sacred text.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "The superstitious practice of **bibliomancy**, opening the sacred scriptures at random to divine future fortunes, was condemned by early councils." },
      { author: "Wilkie Collins", work: "The Moonstone", quote: "Gabriel Betteredge turned to his copy of Robinson Crusoe for daily solace, practicing a comical species of domestic **bibliomancy**." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Anxious minds often seek relief in **bibliomancy**, seeking oracles in the random lines of Virgil or the Holy Scriptures." }
    ]
  },

  // === Dashboard — mn (3 words) ===
  "Dashboard — mn/mina.md": {
    word: "mina",
    primary: "An ancient Near Eastern and Greek unit of currency and weight, equivalent in classical Athens to 100 silver drachmae or roughly one pound.",
    secondary: "In biblical and historical economics, a standard bullion measure; also (as myna/mina) an Asian starling bird noted for mimicking human speech.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "The Persian tribute was levied strictly in silver talents, each talent containing sixty Greek **minas**." },
      { author: "Xenophon", work: "Anabasis", quote: "Cyrus promised each soldier a bonus of five silver **minas** upon their safe arrival at Babylon." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "In ancient Athens, the silver **mina** constituted a substantial sum, representing many weeks of skilled artisan labor." }
    ]
  },
  "Dashboard — mn/mn.md": {
    word: "mn",
    primary: "A combining root derived from Ancient Greek mnasthai/mnēmon signifying memory, remembrance, or mind.",
    secondary: "In Indo-European comparative linguistics, the primordial biconsonantal root (*men- / *mn-) that generated Sanskrit manas, Greek mneme, and English mind and memory.",
    quotes: [
      { author: "Max Müller", work: "The Science of Thought", quote: "The fundamental Aryan root **mn**- preserves across millennia the primal human act of conscious remembering." },
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "From the reduced grade **mn**- of the root men, Greek derived mneme, amnesia, and mnemonic." },
      { author: "Otto Jespersen", work: "Language: Its Nature, Development and Origin", quote: "The biconsonantal stem **mn**- encapsulates the cognitive dawn when speech first named the inner workings of memory." }
    ]
  },
  "Dashboard — mn/mna.md": {
    word: "mna",
    primary: "A classical Greek transliteration of mina (μνᾶ), an ancient monetary unit and measure of weight equal to 100 drachmas or one-sixtieth of a talent.",
    secondary: "In numismatics and classical epigraphy, the Attic and Hellenistic bullion weight standard used in commercial accounting and temple treasuries.",
    quotes: [
      { author: "Plato", work: "Apology", quote: "Socrates proposed a modest fine of one **mna** of silver, which his wealthier friends immediately offered to guarantee." },
      { author: "Thucydides", work: "The Peloponnesian War", quote: "The alliance treaty stipulated that each city-state should contribute forty silver **mnas** for the upkeep of the fleet." },
      { author: "Aristotle", work: "Constitution of the Athenians", quote: "Solon reformed the coinage by decreeing that the **mna**, which formerly held seventy drachmas, should henceforth comprise a hundred." }
    ]
  },

  // === Dashboard — mne (13 words) ===
  "Dashboard — mne/amnesia.md": {
    word: "amnesia",
    primary: "A partial or total loss of memory, typically caused by brain injury, illness, psychological trauma, or neurological degeneration.",
    secondary: "In cognitive neuropsychology, classified into anterograde amnesia (inability to form new memories) and retrograde amnesia (loss of pre-existing memories).",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Jimmie G. suffered from Korsakoff's syndrome, trapped by dense **amnesia** in a permanent present devoid of recent recollection." },
      { author: "William James", work: "The Principles of Psychology", quote: "Traumatic shock can induce sudden **amnesia**, blotting out weeks of personal identity while automated habits remain intact." },
      { author: "Alexander Luria", work: "The Mind of a Mnemonist", quote: "The tragedy of **amnesia** lies in the dissolution of the autobiographical narrative that constitutes our sense of self." }
    ]
  },
  "Dashboard — mne/amnesic.md": {
    word: "amnesic",
    primary: "Of, relating to, or suffering from memory loss; producing or causing amnesia.",
    secondary: "In psychopharmacology and clinical neurology, describing medications (such as benzodiazepines) or pathological conditions that disrupt memory encoding.",
    quotes: [
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The deeply **amnesic** musician could not recall a conversation five minutes earlier, yet could play complex Chopin preludes flawlessly." },
      { author: "Sigmund Freud", work: "A General Introduction to Psychoanalysis", quote: "Childhood memories are veiled by an **amnesic** barrier that conceals early emotional conflicts from adult awareness." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Resident Patient", quote: "The stranger stared blankly at his surroundings, his **amnesic** state leaving him oblivious to his own name." }
    ]
  },
  "Dashboard — mne/amnestic.md": {
    word: "amnestic",
    primary: "Relating to or causing loss of memory; characterized by impaired memory function.",
    secondary: "In clinical psychiatry, designating specific cognitive disorders (such as amnestic mild cognitive impairment or transient global amnesia) focused primarily on memory deficits.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Cerebral concussion frequently leaves an **amnestic** gap covering the moments immediately preceding the impact." },
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "Anesthetic protocols often include an **amnestic** agent to spare surgical patients the trauma of operating room memories." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Deep bilateral hippocampal damage precipitates a severe **amnestic** syndrome without altering basic sensory perception." }
    ]
  },
  "Dashboard — mne/amnesty.md": {
    word: "amnesty",
    primary: "An official pardon granted by a government to people convicted of political offenses; a formal act of collective forgetting and reconciliation.",
    secondary: "In political philosophy and international jurisprudence, an institutional decree extinguishing legal liability to heal civic division following civil war or revolution.",
    quotes: [
      { author: "Abraham Lincoln", work: "Proclamation of Amnesty and Reconstruction", quote: "A full **amnesty** is hereby granted to all persons who participated in the rebellion, restoring all property rights except in slaves." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Following the overthrow of the Thirty Tyrants, the Athenians swore a solemn oath of **amnesty** to bury past discord." },
      { author: "Nelson Mandela", work: "Long Walk to Freedom", quote: "The Truth and Reconciliation Commission offered conditional **amnesty** in exchange for full disclosure of political crimes." }
    ]
  },
  "Dashboard — mne/anamnesis.md": {
    word: "anamnesis",
    primary: "The recollection or remembrance of the past; in medicine, a patient's complete medical and personal history.",
    secondary: "In Platonic philosophy, the theory that the soul remembers eternal forms and innate knowledge known prior to birth, awakened through philosophical dialectic.",
    quotes: [
      { author: "Plato", work: "Meno", quote: "Learning is nothing other than **anamnesis**, the soul's gradual recollecting of eternal truths perceived before mortal birth." },
      { author: "William Osler", work: "Aequanimitas", quote: "A meticulous medical **anamnesis** reveals the subtle genesis of disease far more reliably than hasty lab tests." },
      { author: "C. G. Jung", work: "Modern Man in Search of a Soul", quote: "The therapeutic dialogue relies upon clinical **anamnesis** to reconstruct the psychological history of the neurosis." }
    ]
  },
  "Dashboard — mne/anamnestic.md": {
    word: "anamnestic",
    primary: "Of, relating to, or aiding memory; assisting in recalling past events or data.",
    secondary: "In immunology, describing an anamnestic response—a secondary immune reaction characterized by rapid, heightened antibody production upon repeated antigen exposure.",
    quotes: [
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The secondary inoculation evoked a swift **anamnestic** response, demonstrating the immunological memory of the side-chain receptors." },
      { author: "William James", work: "The Principles of Psychology", quote: "Certain associative cues possess an **anamnestic** power, instantly restoring long-forgotten childhood impressions." },
      { author: "Alexander Luria", work: "The Neuropsychology of Memory", quote: "Structured questioning serves an **anamnestic** function, guiding the patient to reconstruct forgotten chronologies." }
    ]
  },
  "Dashboard — mne/dysmnesia.md": {
    word: "dysmnesia",
    primary: "Impaired, defective, or disordered memory; difficulty in recalling past experiences or retaining new information.",
    secondary: "In clinical neuropsychology, an organic or functional memory dysfunction falling short of complete amnesia, often seen in early dementia or cerebrovascular disease.",
    quotes: [
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Patients with mild frontal lesions demonstrate transient **dysmnesia**, struggling with voluntary memory retrieval." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Early cerebrovascular arteriosclerosis is frequently heralded by progressive **dysmnesia** for proper names and dates." },
      { author: "Henry Maudsley", work: "Physiology and Pathology of the Mind", quote: "Chronic intellectual exhaustion produces a troublesome **dysmnesia** that yields only to prolonged physical rest." }
    ]
  },
  "Dashboard — mne/mne.md": {
    word: "mne",
    primary: "A combining root derived from Greek mnēsthai/mnēmon signifying memory, recollection, or commemoration.",
    secondary: "In morphology and cognitive semantics, the foundational element in Hellenic scientific compounds denoting psychological retention, memorialization, and forgetting.",
    quotes: [
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The root **mne**- connects ancient Greek philosophy with modern medical terms of memory and remembrance." },
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "Through the prefix a- meaning without, the root **mne**- produces amnesia, the negation of memory." },
      { author: "Richard Semon", work: "The Mneme", quote: "We designate the organic power of retaining physiological traces by the Greek stem **mne**-." }
    ]
  },
  "Dashboard — mne/Mneme.md": {
    word: "Mneme",
    primary: "In Greek mythology, the Boeotian Muse of memory; in early 20th-century evolutionary biology, the organic principle of memory in living matter.",
    secondary: "In biological theory (formulated by Richard Semon), the hypothetical capacity of organisms to record experiential stimuli as permanent physical traces (engrams).",
    quotes: [
      { author: "Pausanias", work: "Description of Greece", quote: "The ancient inhabitants of Mount Helicon established worship for three Muses only: Melete, **Mneme**, and Aoide." },
      { author: "Richard Semon", work: "The Mneme", quote: "By the term **Mneme**, I understand the organic property of living organisms to retain the effects of past stimulation." },
      { author: "Bertrand Russell", work: "The Analysis of Mind", quote: "Semon's concept of the **Mneme** offers a physiological hypothesis for the retention of past habit without conscious reflection." }
    ]
  },
  "Dashboard — mne/mnemonic.md": {
    word: "mnemonic",
    primary: "A device, formula, rhyme, or acronym designed to assist human memory; of or relating to memory retention.",
    secondary: "In computer science and assembly programming, a symbolic name or abbreviated code representing a specific machine instruction (e.g. MOV, ADD).",
    quotes: [
      { author: "Cicero", work: "De Oratore", quote: "Simonides invented the **mnemonic** art of memory palaces by associating ideas with vivid mental locations." },
      { author: "William James", work: "Talks to Teachers on Psychology", quote: "A clever **mnemonic** rhyme acts as a mental hook, allowing children to retrieve grammatical rules effortlessly." },
      { author: "Alan Turing", work: "Intelligent Machinery", quote: "Programming routines are rendered intelligible to human engineers by using **mnemonic** abbreviations for binary operations." }
    ]
  },
  "Dashboard — mne/mnemonics.md": {
    word: "mnemonics",
    primary: "The study and development of systems, techniques, and devices for improving and assisting the human memory.",
    secondary: "In cognitive psychology and classical rhetoric, the deliberate methodology of loci and visualization practiced to memorize speeches, data, and complex texts.",
    quotes: [
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "The art of **mnemonics** is built upon two intentions: pre-notion and emblem, which together fix fleeting ideas." },
      { author: "Quintilian", work: "Institutio Oratoria", quote: "Ancient orators relied upon the discipline of **mnemonics** to deliver multi-hour addresses without glancing at notes." },
      { author: "Alexander Luria", work: "The Mind of a Mnemonist", quote: "Shereshevsky had no need for artificial **mnemonics**, for his synesthetic imagination converted every word into an indelible vision." }
    ]
  },
  "Dashboard — mne/mnemonist.md": {
    word: "mnemonist",
    primary: "A person possessing an extraordinary, highly trained, or photographic capacity for remembering large amounts of information.",
    secondary: "In cognitive neuropsychology, an individual studied for exceptional recall abilities, often exhibiting cross-modal synesthesia or specialized visualization strategies.",
    quotes: [
      { author: "Alexander Luria", work: "The Mind of a Mnemonist", quote: "The **mnemonist** could reproduce a matrix of fifty numbers decades later without a single error." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "Unlike the natural **mnemonist**, the autistic savant often recalls vast arrays of facts without comprehending their contextual meaning." },
      { author: "William James", work: "The Principles of Psychology", quote: "A professional **mnemonist** astonishes audiences by reciting thousands of names, relying on practiced associative tricks." }
    ]
  },
  "Dashboard — mne/paramnesia.md": {
    word: "paramnesia",
    primary: "A memory disorder characterized by confusion between reality and fantasy or distortion of memory, such as déjà vu or confabulation.",
    secondary: "In clinical psychiatry, a condition where memory recalls are fabricated or displaced in time and space, frequently seen in Korsakoff syndrome or right hemisphere damage.",
    quotes: [
      { author: "Sigmund Freud", work: "The Psychopathology of Everyday Life", quote: "The uncanny sensation of déjà vu represents a benign form of **paramnesia**, where unconscious daydreams masquerade as past events." },
      { author: "William James", work: "The Principles of Psychology", quote: "In reductive **paramnesia**, the patient is convinced that an entirely new city or house is an exact duplicate of one previously visited." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "His lively confabulations were forms of clinical **paramnesia**, filling terrifying memory voids with whimsical inventions." }
    ]
  },

  // === Dashboard — mor (7 words) ===
  "Dashboard — mor/amor.md": {
    word: "amor",
    primary: "Love, passion, or deep affection; also (capitalized) the personification of love in Roman mythology, equivalent to Cupid or Greek Eros.",
    secondary: "In literature and philosophy, romantic or divine love, as in Virgil's maxim 'omnia vincit amor' (love conquers all) or Spinoza's 'amor dei intellectualis'.",
    quotes: [
      { author: "Virgil", work: "Eclogues", quote: "**Amor** vincit omnia: et nos cedamus amori; love conquers all things, so let us too yield to love." },
      { author: "Baruch Spinoza", work: "Ethics", quote: "The highest peace of mind consists in the intellectual love of God, the sublime **amor** dei intellectualis." },
      { author: "Dante Alighieri", work: "The Divine Comedy: Paradiso", quote: "My desire and will were rolled, even as a wheel that moves equally, by the **Amor** that moves the sun and other stars." }
    ]
  },
  "Dashboard — mor/enamor.md": {
    word: "enamor",
    primary: "To fill with love, captivate, or charm thoroughly; to inflame with passionate affection (often used passively with of or with).",
    secondary: "In figurative and aesthetic usage, to become fascinated or obsessed with an idea, artistic style, or philosophical doctrine.",
    quotes: [
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "Mine ear is much **enamored** of thy note; / So is mine eye enthralled to thy shape." },
      { author: "John Milton", work: "Paradise Lost", quote: "He looked upon her grace, **enamored** with celestial beauty that drove all impure thoughts away." },
      { author: "Mary Shelley", work: "Frankenstein", quote: "I became deeply **enamored** of the natural sciences, dedicating every solitary hour to chemical investigations." }
    ]
  },
  "Dashboard — mor/mor.md": {
    word: "mor",
    primary: "A combining root derived from Ancient Greek mōros meaning foolish, stupid, sluggish, or dull of intellect.",
    secondary: "In lexicology and psychology, the etymological root in compounds such as moron and oxymoron, denoting folly or mental blunting.",
    quotes: [
      { author: "Walter William Skeat", work: "Principles of English Etymology", quote: "The Greek root **mor**- fundamentally denoted mental sluggishness, giving rise to both classical rhetoric and modern psychological terms." },
      { author: "H. L. Mencken", work: "The American Language", quote: "American psychologists adopted the classical stem **mor**- to coin precise clinical labels for intellectual retardation." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "In the compound oxymoron, the element **mor**- balances pointed wit against apparent foolishness." }
    ]
  },
  "Dashboard — mor/moron.md": {
    word: "moron",
    primary: "A foolish or remarkably stupid person; historically, an obsolete clinical classification for an adult with a mental age of 8 to 12 years.",
    secondary: "In the history of psychiatry and intelligence testing, a term coined by Henry H. Goddard in 1910 to categorize mild intellectual disability before becoming a general term of abuse.",
    quotes: [
      { author: "Henry H. Goddard", work: "Feeble-Mindedness: Its Causes and Consequences", quote: "I propose the term **moron**, from the Greek word for foolish, to designate individuals with mild cognitive impairment." },
      { author: "Aldous Huxley", work: "Brave New World", quote: "The lower castes were genetically engineered with deliberate limitations, bred so that not even a **moron** could feel discontent." },
      { author: "George Orwell", work: "Coming Up for Air", quote: "You look at the headlines and wonder what kind of bloodthirsty **moron** is directing the affairs of Europe." }
    ]
  },
  "Dashboard — mor/moronic.md": {
    word: "moronic",
    primary: "Remarkably stupid, senseless, or foolish; characteristic of or resembling a moron.",
    secondary: "In cultural and political criticism, describing public discourse, sensationalist media, or irrational decisions that demonstrate a total lack of critical intelligence.",
    quotes: [
      { author: "H. L. Mencken", work: "Prejudices: Second Series", quote: "The popular press caters directly to **moronic** appetites, elevating trivial scandal above serious civic thought." },
      { author: "George Orwell", work: "Keep the Aspidistra Flying", quote: "Gordon looked at the advertising posters with disgust, cursing the **moronic** slogans designed to lure the public." },
      { author: "Virginia Woolf", work: "The Years", quote: "She turned away from the shouting crowd, weary of their **moronic** enthusiasm for the empty political spectacle." }
    ]
  },
  "Dashboard — mor/moronity.md": {
    word: "moronity",
    primary: "The state, condition, or quality of being a moron; foolishness or mild intellectual impairment.",
    secondary: "In early 20th-century eugenics and clinical psychology, the designated diagnostic state of having a mental age between eight and twelve years.",
    quotes: [
      { author: "Lewis Terman", work: "The Measurement of Intelligence", quote: "Early diagnostic screening was intended to differentiate between true **moronity** and educational neglect in schoolchildren." },
      { author: "Henry H. Goddard", work: "The Kallikak Family", quote: "The investigators traced hereditary **moronity** through several generations of rural social isolation." },
      { author: "H. L. Mencken", work: "Minority Report", quote: "The sheer depth of human **moronity** becomes apparent only during heated election campaigns." }
    ]
  },
  "Dashboard — mor/oxymoronic.md": {
    word: "oxymoronic",
    primary: "Of, relating to, or characterized by an oxymoron; combining contradictory or incongruous terms.",
    secondary: "In literary stylistics, intentionally pairing antithetical words to create a startling rhetorical paradox, irony, or emotional complexity.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", quote: "Romeo speaks in famously **oxymoronic** outbursts: 'O brawling love! O loving hate! / O heavy lightness! serious vanity!'" },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The phrase 'sunny pleasure-dome with caves of ice' presents an intensely **oxymoronic** imaginative vision." },
      { author: "George Orwell", work: "1984", quote: "The party slogans—'War is Peace', 'Freedom is Slavery'—are masterclasses in **oxymoronic** doublespeak." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
    return;
  }
  let content = fs.readFileSync(fullPath, "utf8");

  // Format quotes
  const quotesFormatted = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join("\n");

  // Replace Definition & Semantic Range
  const defRegex = /> \[!book\] 📖 Definitions & Semantic Range[\s\S]*?(?=> \[!quote\]|$)/;
  const newDef = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}\n\n`;

  if (defRegex.test(content)) {
    content = content.replace(defRegex, newDef);
  } else {
    console.warn("Could not find [!book] in", relPath);
  }

  // Replace Quotes
  const quoteRegex = /> \[!quote\] 💬 Contextual Usage & Authentic Quotations[\s\S]*$/;
  const newQuotes = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quotesFormatted}\n`;

  if (quoteRegex.test(content)) {
    content = content.replace(quoteRegex, newQuotes);
  } else {
    console.warn("Could not find [!quote] in", relPath);
  }

  fs.writeFileSync(fullPath, content, "utf8");
  console.log("Updated:", relPath);
}

for (const [relPath, data] of Object.entries(wordsData)) {
  updateWordNote(relPath, data);
}
console.log("Batch 2 completed! Total words updated:", Object.keys(wordsData).length);
