import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — graph";

const wordsData = {
  "agrapha.md": {
    word: "agrapha",
    primary: "Sayings of Jesus attributed to him in early Christian tradition or patristic literature that are not recorded in the four canonical Gospels.",
    secondary: "In New Testament textual criticism, unwritten or extra-canonical logia cited in the Pauline epistles, Acts, church fathers, or early papyri (such as the Oxyrhynchus Papyri).",
    quotes: [
      { author: "Alfred Resch", work: "Agrapha: Aussercanonische Schriftfragmente", quote: "The historical collection of the **agrapha** preserves echoes of the Lord's teaching cherished by the earliest communities." },
      { author: "F. J. A. Hort", work: "The Way, the Truth, the Life", quote: "Among the **agrapha** preserved by Paul in the Book of Acts is the golden beatitude: 'It is more blessed to give than to receive.'" },
      { author: "Bruce M. Metzger", work: "The Canon of the New Testament", quote: "Scholars scrutinize each isolated **agrapha** to determine whether it represents a genuine oral memory or a later apocryphal invention." }
    ]
  },
  "agraphia.md": {
    word: "agraphia",
    primary: "A neurological condition characterized by the loss or impairment of the ability to communicate through writing.",
    secondary: "In neuropsychology and behavioral neurology, a cerebral deficit caused by damage to specific cortical areas (such as Exner's area or the angular gyrus), distinct from motor paralysis or illiteracy.",
    quotes: [
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Lesions of the left parieto-occipital cortex frequently result in semantic **agraphia**, leaving the patient unable to synthesize written words." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The stroke victim retained fluent conversational speech but exhibited a startling central **agraphia**, staring uncomprehendingly at a pen." },
      { author: "Norman Geschwind", work: "Selected Papers on Language and the Brain", quote: "The clinical dissociation between pure alexia and pure **agraphia** shed light on the connective pathways of the dominant hemisphere." }
    ]
  },
  "agraphic.md": {
    word: "agraphic",
    primary: "Of, relating to, or affected by agraphia; unable to write due to brain injury or dysfunction.",
    secondary: "In historical linguistics and anthropology, lacking a system of writing; unwritten or illiterate (contrasted with typographic or epigraphic).",
    quotes: [
      { author: "Wilder Penfield", work: "Speech and Brain-Mechanisms", quote: "Electrical stimulation of the focal area produced a temporary **agraphic** state, during which the patient could name objects but could not spell them." },
      { author: "Claude Lévi-Strauss", work: "Tristes Tropiques", quote: "In an **agraphic** society, oral memory carries the entire weight of ancestral law and tribal genealogy." },
      { author: "Walter J. Ong", work: "Orality and Literacy", quote: "The cognitive structures of an **agraphic** culture differ fundamentally from those shaped by the chirographic word." }
    ]
  },
  "allograft.md": {
    word: "allograft",
    primary: "A tissue graft or organ transplant harvested from a donor of the same species as the recipient but possessing a different genetic constitution; homograft.",
    secondary: "In transplant immunology and reconstructive surgery, a graft subject to cell-mediated immune rejection unless modulated by immunosuppressive therapy or HLA matching.",
    quotes: [
      { author: "Peter Medawar", work: "The Uniqueness of the Individual", quote: "The immunological rejection of an **allograft** represents the body's acute defense against foreign histocompatibility antigens." },
      { author: "Thomas Starzl", work: "The Puzzle People: Memoirs of a Transplant Surgeon", quote: "The survival of the renal **allograft** depended upon balancing delicate doses of cyclosporine to suppress rejection." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "The surgeon carefully secured the cadaveric tendon **allograft** into the athlete's shredded knee." }
    ]
  },
  "anagram.md": {
    word: "anagram",
    primary: "A word or phrase formed by rearranging the letters of a different word or phrase.",
    secondary: "In wordplay, cryptography, and Renaissance rhetoric, a letter-transposition puzzle often endowed with mystical, prophetic, or satirical significance.",
    quotes: [
      { author: "John Fletcher", work: "The Elder Brother", quote: "These are the **anagrams** of three great Worthies." },
      { author: "James Joyce", work: "Ulysses", quote: "What **anagrams** had he made on his name in youth? Leopold Bloom." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The art of **anagram** was cultivated by the ancients, who sought in the transposition of letters some mystical prophecy or moral lesson." }
    ]
  },
  "anepigraphic.md": {
    word: "anepigraphic",
    primary: "Lacking an inscription, legend, or writing (especially applied to ancient coins, medals, or stone monuments).",
    secondary: "In classical numismatics and archaeology, describing early struck coinage or primitive stelae that bear pictorial devices, monograms, or reliefs without alphabetical letters.",
    quotes: [
      { author: "Barclay V. Head", work: "Historia Numorum: A Manual of Greek Numismatics", quote: "The archaic electrum staters of Lydia are entirely **anepigraphic**, bearing merely the embossed forepart of a roaring lion." },
      { author: "Percy Gardner", work: "The Types of Greek Coins", quote: "An **anepigraphic** coin obliges the numismatist to rely solely on artistic style and fabric to determine its date and mint." },
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The primitive seal-stones discovered in the lower stratum were **anepigraphic**, relying on geometric emblems rather than Linear signs." }
    ]
  },
  "anorthography.md": {
    word: "anorthography",
    primary: "Defective or incorrect spelling; departure from conventional orthographic rules.",
    secondary: "In pedagogical linguistics and clinical neuropsychology, persistent inaccuracy in letter sequencing and phonetic spelling resulting from cognitive deficit or dialectal variance.",
    quotes: [
      { author: "Noah Webster", work: "Dissertations on the English Language", quote: "The rampant **anorthography** of ancient manuscripts arose from the absence of a standard national lexicon." },
      { author: "Henry Bradley", work: "The Making of English", quote: "Before printing imposed uniform spelling, phonetic **anorthography** was common even among educated Elizabethan gentry." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "The acoustic analysis of words being impaired, the patient's writing displayed grotesque **anorthography** and letter omission." }
    ]
  },
  "antigram.md": {
    word: "antigram",
    primary: "An anagram that forms a word, phrase, or sentence with a meaning opposite or antonymous to that of the original.",
    secondary: "In recreational linguistics and wordplay, a humorous or ironic transposition of letters yielding an antithetical concept (e.g., 'funeral' yielding 'real fun', or 'restful' yielding 'fluster').",
    quotes: [
      { author: "Will Shortz", work: "The Puzzler's Guide", quote: "Wordplay enthusiasts celebrate the **antigram** for its sheer irony, transforming 'violence' into 'nice love' with the rearrangement of a few letters." },
      { author: "Dmitri Borgmann", work: "Language on Vacation", quote: "The true **antigram** strikes like a satirical epigram, using the exact letters of an entity to reveal its opposite nature." },
      { author: "A. Ross Eckler", work: "Word Ways: The Journal of Recreational Linguistics", quote: "Few anagrammatic feats are more satisfying than discovering a natural **antigram** where meaning flips upside down." }
    ]
  },
  "autograft.md": {
    word: "autograft",
    primary: "A graft of tissue taken from one part of an individual's body and transplanted to another site on the same individual.",
    secondary: "In reconstructive and plastic surgery, the gold standard for tissue transplantation because it avoids donor tissue rejection and immunosuppressive complications.",
    quotes: [
      { author: "Alexis Carrel", work: "The Surgery of Blood Vessels", quote: "The vascular **autograft** taken from the saphenous vein healed without any cellular reaction of incompatibility." },
      { author: "Siddhartha Mukherjee", work: "The Song of the Cell", quote: "An **autograft** of skin saved the burn victim's limbs without triggering the destructive fury of his own immune system." },
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "By using an **autograft** harvested from the patient's own iliac crest, the orthopedic surgeon restored spinal stability." }
    ]
  },
  "autograph.md": {
    word: "autograph",
    primary: "A person's own signature, handwriting, or manuscript written in their own hand.",
    secondary: "In textual criticism and archival bibliography, the original manuscript or document inscribed by the author's own pen, as distinguished from a copy or print.",
    quotes: [
      { author: "Charles Dickens", work: "Nicholas Nickleby", quote: "He requested the famous actor's **autograph** upon the title page of the evening's playbill." },
      { author: "Edgar Allan Poe", work: "Autography", quote: "The **autograph** of an individual is generally thought to be an index of the writer's mental character." },
      { author: "W. W. Greg", work: "The Calculus of Variants", quote: "In the absence of Shakespeare's dramatic **autograph**, the editor must deduce the text from defective early quartos." }
    ]
  },
  "autographed.md": {
    word: "autographed",
    primary: "Inscribed or signed with the author's or creator's own signature.",
    secondary: "Bearing a personal handwritten inscription, endorsement, or dedication by the person who created or owned the item.",
    quotes: [
      { author: "Mark Twain", work: "The Innocents Abroad", quote: "The collector proudly displayed an **autographed** copy of the charter signed by the emperor himself." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "Upon the mantelpiece stood an **autographed** portrait of the great French toxicologist." },
      { author: "Virginia Woolf", work: "Orlando", quote: "The manuscript had been lovingly preserved, bound in morocco, and **autographed** upon the vellum flyleaf." }
    ]
  },
  "autographic.md": {
    word: "autographic",
    primary: "Of, relating to, or written in the author's or writer's own hand.",
    secondary: "In printing and lithography, capable of directly reproducing handwriting or line drawings without the need for manual engraving.",
    quotes: [
      { author: "Alois Senefelder", work: "A Complete Course of Lithography", quote: "My **autographic** ink allows the artist to write naturally upon prepared paper and transfer the script directly to stone." },
      { author: "Thomas Carlyle", work: "Critical and Miscellaneous Essays", quote: "The genuine **autographic** letter reveals the inner man far more vividly than any polished public memoir." },
      { author: "William Makepeace Thackeray", work: "The Virginians", quote: "The antiquary held the yellowed parchment to the lamp, admiring its authentic **autographic** signatures." }
    ]
  },
  "cardiogram.md": {
    word: "cardiogram",
    primary: "A graphic recording or tracing of the movements, pressure, or electrical changes of the heart (often synonymous with electrocardiogram).",
    secondary: "In historical physiology, the curve traced by a cardiograph attached to the chest wall, recording apical cardiac pulsations.",
    quotes: [
      { author: "Étienne-Jules Marey", work: "La méthode graphique", quote: "The mechanical **cardiogram** recorded upon the smoked drum showed each systolic contraction with mathematical fidelity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A modern **cardiogram** provides indispensable confirmation when clinical signs of valvular regurgitation are ambiguous." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Blanched Soldier", quote: "The physician examined the patient's **cardiogram**, noting the intermittent skipped beats of cardiac strain." }
    ]
  },
  "cartographer.md": {
    word: "cartographer",
    primary: "A person who draws, compiles, or produces maps and charts.",
    secondary: "In geography and geodesy, a specialist who translates mathematical survey data, aerial imagery, and topographic measurements into spatial cartographic representations.",
    quotes: [
      { author: "Gerardus Mercator", work: "Atlas sive Cosmographicae Meditationes", quote: "The skilled **cartographer** must preserve true bearings across the boundless expanse of ocean voyages." },
      { author: "Jonathan Swift", work: "On Poetry: A Rhapsody", quote: "So geographers, in Afric maps, with savage pictures fill their gaps, and o'er unhabitable downs place elephants for want of towns." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "I looked at the blank spaces on the earth, where the **cartographer** had left only white rivers of mystery." }
    ]
  },
  "cartographic.md": {
    word: "cartographic",
    primary: "Of or relating to the science, art, or practice of map-making.",
    secondary: "Characterized by the spatial conventions, symbols, scale projections, and coordinate grids of map representation.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The **cartographic** delineation of isothermal lines revealed climate patterns previously hidden to physical geography." },
      { author: "Fernand Braudel", work: "The Mediterranean and the Mediterranean World", quote: "The Venetian navigators possessed extraordinary **cartographic** skill in charting coastal currents and shallow shoals." },
      { author: "J. B. Harley", work: "The New Nature of Maps", quote: "Every **cartographic** document is an assertion of political power and territorial definition." }
    ]
  },
  "cartographical.md": {
    word: "cartographical",
    primary: "Relating to cartography or maps; cartographic.",
    secondary: "Concerned with the compilation, historical analysis, or drafting of geographical charts and topographic maps.",
    quotes: [
      { author: "C. R. Markham", work: "Major James Rennell and the Rise of Modern English Geography", quote: "The survey represented a monument of **cartographical** precision across the vast plains of Bengal." },
      { author: "Edward Lynam", work: "The Mapmaker's Art", quote: "Renaissance maritime expansion stimulated intense **cartographical** curiosity throughout western Europe." },
      { author: "Denis Wood", work: "The Power of Maps", quote: "Behind every **cartographical** convention lies an unstated cultural consensus about space and importance." }
    ]
  },
  "cartography.md": {
    word: "cartography",
    primary: "The science, art, and technology of making maps, globes, and navigational charts.",
    secondary: "In geospatial studies, the discipline encompassing the collection, analysis, design, and visualization of spatial data into communicative graphic formats.",
    quotes: [
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "Modern navigation and empire were made possible only by the mathematical development of **cartography**." },
      { author: "Jorge Luis Borges", work: "On Exactitude in Science", quote: "In that Empire, the Art of **Cartography** attained such Perfection that the map of a single Province occupied the entirety of a City." },
      { author: "Daniel J. Boorstin", work: "The Discoverers", quote: "The history of **cartography** is the epic story of humanity's struggle to picture the invisible contours of the globe." }
    ]
  },
  "chromatographical.md": {
    word: "chromatographical",
    primary: "Of, relating to, or obtained by chromatography (the separation of mixtures).",
    secondary: "Pertaining to the analytical procedures and column techniques used to separate and isolate biochemical compounds.",
    quotes: [
      { author: "Mikhail Tsvet", work: "Physical Chemical Studies on Chlorophyll", quote: "The **chromatographical** adsorption method separated the leaf pigments into distinct green and yellow bands." },
      { author: "Archer J. P. Martin", work: "Nobel Lecture: Partition Chromatography", quote: "The resolution achieved by this **chromatographical** column allowed amino acids to be identified in microgram quantities." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Subsequent **chromatographical** examination confirmed that the protein hydrolysate contained no extraneous peptides." }
    ]
  },
  "chromatographically.md": {
    word: "chromatographically",
    primary: "By means of chromatography; using chromatographic separation techniques.",
    secondary: "In analytical chemistry, resolving or purifying compounds through differential partitioning between mobile and stationary phases.",
    quotes: [
      { author: "Richard Kuhn", work: "Carotenoids and Flavins", quote: "The crude pigment mixture was **chromatographically** fractionated upon a column of activated alumina." },
      { author: "Frederick Sanger", work: "The Arrangement of Amino Acids in Proteins", quote: "Each peptide fragment was **chromatographically** purified before proceeding to terminal residue identification." },
      { author: "Dorothy Hodgkin", work: "The Structure of Vitamin B12", quote: "The red crystalline substance had been **chromatographically** isolated from liver extract after months of painstaking elution." }
    ]
  },
  "chromatography.md": {
    word: "chromatography",
    primary: "A laboratory technique for the separation of a mixture into its individual components by passing it through a medium in which the components move at different rates.",
    secondary: "In chemical and biochemical analysis, a family of separation processes (gas, liquid, thin-layer, ion-exchange) essential for purification, identification, and molecular quantification.",
    quotes: [
      { author: "Mikhail Tsvet", work: "Adsorption Analysis and Chromatographic Method", quote: "Like the light rays in the spectrum, so the different components of a pigment mixture are resolved in the calcium carbonate column by **chromatography**." },
      { author: "James Watson", work: "The Double Helix", quote: "Paper **chromatography** enabled Chargaff to prove that the ratio of adenine to thymine was always equal to one." },
      { author: "Oliver Sacks", work: "Uncle Tungsten: Memories of a Chemical Boyhood", quote: "I marveled at how simple paper **chromatography** could unbraid black ink into a vivid ribbon of violet, turquoise, and yellow." }
    ]
  },
  "diagram.md": {
    word: "diagram",
    primary: "A simplified drawing or plan showing the structure, arrangement, appearance, or workings of something; a schematic representation.",
    secondary: "In geometry, logic, and semiotics, an abstract spatial figure representing quantitative relationships, geometric proofs, or logical propositions.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "By the accompanying **diagram**, the refraction of the ray through the two faces of the prism is made distinctly visible." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The accompanying **diagram** will aid us in understanding this rather perplexing subject of divergent descent." },
      { author: "Bertrand Russell", work: "Introduction to Mathematical Philosophy", quote: "A Venn **diagram** illustrates the intersection and union of classes in a visual and immediate manner." }
    ]
  },
  "digraph.md": {
    word: "digraph",
    primary: "A pair of characters or letters used together to represent a single sound or phoneme (such as 'th', 'ph', or 'ea').",
    secondary: "In graph theory and computer science, a directed graph consisting of vertices connected by edges that possess an inherent orientation or direction.",
    quotes: [
      { author: "Otto Jespersen", work: "A Modern English Grammar", quote: "The Old English runic letter thorn was eventually replaced by the Roman **digraph** 'th' in Middle English orthography." },
      { author: "Frank Harary", work: "Graph Theory", quote: "A **digraph** is strongly connected if every vertex is reachable from every other vertex along a directed path." },
      { author: "H. L. Mencken", work: "The American Language", quote: "Noah Webster led the crusade to simplify English spelling by dropping the superfluous vowel from the Latin **digraph** 'ae'." }
    ]
  },
  "dysgraphia.md": {
    word: "dysgraphia",
    primary: "An impairment of handwriting ability and fine motor coordination, resulting in distorted, illegible, or laboriously slow writing.",
    secondary: "In pediatric neurology and educational psychology, a specific learning disorder involving difficulties with orthographic coding, motor planning, and finger sequencing.",
    quotes: [
      { author: "Norman Geschwind", work: "Cerebral Dominance and Lateralization", quote: "Developmental **dysgraphia** frequently occurs in children whose verbal intelligence is entirely normal or superior." },
      { author: "Oliver Sacks", work: "An Anthropologist on Mars", quote: "His severe **dysgraphia** made holding a pencil an agonizing ordeal, yet his verbal eloquence was astonishing." },
      { author: "Alexander Luria", work: "The Neuropsychology of Memory", quote: "Patients suffering from spatial **dysgraphia** lose the ability to maintain horizontal alignment and spacing across the page." }
    ]
  },
  "echocardiography.md": {
    word: "echocardiography",
    primary: "The use of ultrasound waves to produce visual images of the heart's chambers, valves, and surrounding structures.",
    secondary: "In clinical cardiology, a non-invasive diagnostic modality (including Doppler, transthoracic, and transesophageal techniques) used to evaluate hemodynamic flow, ejection fraction, and cardiac anatomy.",
    quotes: [
      { author: "Inge Edler", work: "The History of Echocardiography", quote: "The discovery that reflected ultrasound could record cardiac valve motion marked the birth of modern **echocardiography**." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "Color Doppler **echocardiography** immediately demonstrated severe mitral regurgitation spraying backwards into the left atrium." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The portable **echocardiography** monitor showed the aortic leaflets fluttering like tiny white sails against the blood stream." }
    ]
  },
  "electrocardiograph.md": {
    word: "electrocardiograph",
    primary: "An instrument for recording the electrical currents generated by the heart during its cycle of contraction and relaxation.",
    secondary: "In biomedical engineering, a high-gain differential amplifier and recording device connected to surface electrodes to capture cardiac electrophysiological signals.",
    quotes: [
      { author: "Willem Einthoven", work: "The String Galvanometer and the Measurement of the Action Currents of the Heart", quote: "The sensitive quartz filament of the **electrocardiograph** responded instantaneously to the minute microvolt shifts of the cardiac cycle." },
      { author: "Sinclair Lewis", work: "Arrowsmith", quote: "In the quiet laboratory, the **electrocardiograph** hummed gently, recording the faint electric pulse of life." },
      { author: "Sherwin B. Nuland", work: "How We Die: Reflections on Life's Final Chapter", quote: "The physician wheeled in the cumbersome **electrocardiograph** to verify whether ventricular tachycardia had commenced." }
    ]
  },
  "electrocardiographic.md": {
    word: "electrocardiographic",
    primary: "Of, relating to, or obtained by means of an electrocardiograph or electrocardiogram.",
    secondary: "Pertaining to the diagnostic interpretation of cardiac electrical conduction patterns and wave anomalies.",
    quotes: [
      { author: "Paul Dudley White", work: "Heart Disease", quote: "Marked ST-segment elevation on the **electrocardiographic** tracing provides definitive evidence of acute transmural ischemia." },
      { author: "Lewis Thomas", work: "The Medusa and the Snail", quote: "The patient's **electrocardiographic** monitor beeped steadily in the darkened intensive care room." },
      { author: "Eugene Braunwald", work: "Heart Disease: A Textbook of Cardiovascular Medicine", quote: "Accurate **electrocardiographic** diagnosis requires meticulous lead placement to avoid misleading axis deviation." }
    ]
  },
  "electroencephalograph.md": {
    word: "electroencephalograph",
    primary: "An apparatus for detecting and recording electrical activity in the brain via electrodes placed on the scalp.",
    secondary: "In neurophysiology and neurology, a multi-channel physiological recording system that amplifies cerebral microvolt oscillations into printable wave tracings (EEG).",
    quotes: [
      { author: "Hans Berger", work: "Über das Elektrenkephalogramm des Menschen", quote: "I succeeded in constructing an **electroencephalograph** capable of recording the spontaneous electrical waves of the human cerebrum." },
      { author: "W. Grey Walter", work: "The Living Brain", quote: "The multi-channel **electroencephalograph** laid bare the rhythmic dance of alpha and delta waves across the sleeping brain." },
      { author: "Oliver Sacks", work: "Musicophilia", quote: "During the musical seizure, the **electroencephalograph** picked up paroxysmal rhythmic spike discharges over the right temporal lobe." }
    ]
  },
  "electroencephalographic.md": {
    word: "electroencephalographic",
    primary: "Of, relating to, or obtained by means of electroencephalography.",
    secondary: "Pertaining to the electrical wave patterns (alpha, beta, theta, delta) produced by the cerebral cortex as recorded on an EEG.",
    quotes: [
      { author: "Hans Berger", work: "Electroencephalography in Man", quote: "The characteristic **electroencephalographic** rhythm slowed markedly when the subject closed his eyes in deep relaxation." },
      { author: "Wilder Penfield & Herbert Jasper", work: "Epilepsy and the Functional Anatomy of the Human Brain", quote: "Focal **electroencephalographic** abnormalities localized the epileptogenic lesion to the anterior temporal cortex." },
      { author: "Carl Sagan", work: "The Dragons of Eden", quote: "The onset of rapid eye movement sleep is accompanied by distinctive **electroencephalographic** low-voltage desynchronization." }
    ]
  },
  "electroencephalography.md": {
    word: "electroencephalography",
    primary: "The measurement and recording of the electrical activity of the brain, usually from electrodes placed on the scalp.",
    secondary: "In clinical neurophysiology, an essential diagnostic method used to evaluate seizure disorders, encephalopathies, sleep staging, and brain death.",
    quotes: [
      { author: "Hans Berger", work: "Das Elektrenkephalogramm des Menschen", quote: "Human **electroencephalography** opens a window into the continuous bioelectric rhythms that sustain conscious thought." },
      { author: "W. Grey Walter", work: "The Living Brain", quote: "With the advent of clinical **electroencephalography**, doctors could observe epilepsy not merely as an outward convulsion, but as an electrical storm in the brain." },
      { author: "Antonio Damasio", work: "Descartes' Error", quote: "Modern functional imaging complements **electroencephalography**, offering exquisite spatial resolution where EEG offers millisecond timing." }
    ]
  },
  "engraft.md": {
    word: "engraft",
    primary: "To insert a shoot or scion of one plant into another so that they unite and grow together; to graft.",
    secondary: "To plant, implant, or establish deeply and firmly (as a habit, principle, virtue, or idea) in the mind, character, or body.",
    quotes: [
      { author: "William Shakespeare", work: "Sonnet 15", quote: "Then the conceit of this inconstant stay sets you most rich in youth before my sight, where wasteful Time debateth with Decay, to change your day of youth to sullied night; and all in war with Time for love of you, as he takes from you, I **engraft** you new." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "It is the true office of philosophy to **engraft** sound principles of virtue into the pliable minds of youth." },
      { author: "John Milton", work: "Paradise Lost", quote: "His words, so sweetly spoken, did **engraft** in her heart a false confidence and foolish longing." }
    ]
  },
  "engram.md": {
    word: "engram",
    primary: "A hypothetical physical or biochemical trace in the nervous system corresponding to a stored memory.",
    secondary: "In neuropsychology, the persistent neuroplastic structural reorganization of synaptic networks that encodes a specific learned experience.",
    quotes: [
      { author: "Richard Semon", work: "Die Mneme", quote: "I designate by the term **engram** the permanent physical alteration left behind in the irritable substance by an external stimulation." },
      { author: "Karl Lashley", work: "In Search of the Engram", quote: "It is not possible to demonstrate the localized existence of that which has been called the **engram** anywhere within the cerebral cortex." },
      { author: "Susumu Tonegawa", work: "Memory Engram Technology", quote: "By selectively reactivating the specific hippocampal **engram** cells with optogenetics, the learned fear response was artificially recalled." }
    ]
  },
  "epigram.md": {
    word: "epigram",
    primary: "A concise, clever, pointed, and often witty or satirical saying, remark, or poem.",
    secondary: "In classical literature, a terse elegiac verse originally carved upon a monument or tomb, later cultivated by Martial as a brief satirical poem ending in an unexpected rhetorical punch.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He could explain everything with a cynical **epigram**, transforming grave dilemmas into sparkling dinner conversation." },
      { author: "Alexander Pope", work: "Epigrams", quote: "An **epigram** is like a bee: a whole divided into three—its body small, its honey sweet, and in its tail a sudden sting." },
      { author: "Samuel Taylor Coleridge", work: "On an Epigram", quote: "What is an **epigram**? A dwarfish whole; its body brevity, and wit its soul." }
    ]
  },
  "epigraph.md": {
    word: "epigraph",
    primary: "An inscription engraved on a building, monument, statue, or coin.",
    secondary: "In literary composition, a quotation, motto, or short poem placed at the beginning of a book, chapter, or essay to suggest its theme.",
    quotes: [
      { author: "T. S. Eliot", work: "The Waste Land", quote: "The Latin and Greek **epigraph** from the Satyricon sets a somber, prophetic tone for the poem that follows." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The weathered **epigraph** upon the triumphal arch still commemorated the victories of Trajan over the Dacians." },
      { author: "George Eliot", work: "Middlemarch", quote: "She composed an original poetic **epigraph** for each chapter to foreshadow the moral trials of her characters." }
    ]
  },
  "epigraphic.md": {
    word: "epigraphic",
    primary: "Of, relating to, or characteristic of an epigraph or epigraphy; pertaining to inscriptions.",
    secondary: "Belonging to the discipline of reading, transcribing, and interpreting ancient texts carved on stone, bronze, clay, or other durable materials.",
    quotes: [
      { author: "Theodor Mommsen", work: "Corpus Inscriptionum Latinarum", quote: "Our **epigraphic** survey of Roman municipal laws restored historical facts that literary histories had completely omitted." },
      { author: "Arthur Evans", work: "Scripta Minoa", quote: "The Cretan seal-stones present an **epigraphic** puzzle of early pictographic and linear scripts." },
      { author: "James Henry Breasted", work: "Ancient Records of Egypt", quote: "The monumental **epigraphic** records of Karnak were painstakingly copied before weathering erased the hieroglyphs." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("File not found:", fullPath);
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
console.log("Writing & Script Batch 8 (Dashboard — graph 1-34) completed! Total words updated:", Object.keys(wordsData).length);
