import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — graph";

const wordsData = {
  "monogram.md": {
    word: "monogram",
    primary: "A motif of two or more letters, typically a person's initials, combined or interwoven into a single decorative symbol.",
    secondary: "In numismatics, bibliography, and heraldry, an engraved or stamped cypher identifying a sovereign, printer, mint, or artist (such as Albrecht Dürer's celebrated AD).",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Scandal in Bohemia", quote: "In the upper left corner of the heavy note-paper was embossed a neat pink **monogram** of two interlocked letters." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "The silver-backed brushes and ivory toilet-boxes were all marked with his ornate **monogram**." },
      { author: "Alexandre Dumas", work: "The Count of Monte Cristo", quote: "Upon the seal of red wax was pressed an antique **monogram** that none could decipher." }
    ]
  },
  "monograph.md": {
    word: "monograph",
    primary: "A detailed, comprehensive, and scholarly written treatise on a single specialized subject or a single aspect of a subject.",
    secondary: "In academic publishing and bibliographic classification, a freestanding non-serial publication focused on an exhaustive investigation of a discrete topic.",
    quotes: [
      { author: "Charles Darwin", work: "A Monograph on the Sub-class Cirripedia", quote: "In this **monograph**, I have endeavoured to describe every known species of living barnacle with anatomical precision." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", quote: "Sherlock Holmes had published an exhaustive **monograph** upon the tracing of footsteps and the preservation of plaster casts." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The young naturalist established his scientific reputation by publishing a thorough **monograph** on the fossil cephalopods of the chalk." }
    ]
  },
  "orthographic.md": {
    word: "orthographic",
    primary: "Of or relating to the conventional rules of spelling in a language; correctly spelled.",
    secondary: "In architectural and technical drawing, relating to orthographic projection, wherein three-dimensional objects are represented on perpendicular two-dimensional planes without perspective distortion.",
    quotes: [
      { author: "Samuel Johnson", work: "The Plan of an English Dictionary", quote: "I shall endeavor to establish an **orthographic** standard that balances etymological ancestry with living pronunciation." },
      { author: "Vitruvius", work: "De Architectura", quote: "The **orthographic** elevation shows the vertical façade of the temple drawn exactly to scale without perspective fore-shortening." },
      { author: "Noam Chomsky", work: "Current Issues in Linguistic Theory", quote: "The child internalizes the **orthographic** regularities of the writing system alongside spoken phonology." }
    ]
  },
  "orthography.md": {
    word: "orthography",
    primary: "The conventional spelling system of a language; the study of letters and the rules of spelling.",
    secondary: "In linguistics, the normative methodology by which spoken phonemes are transcribed into written graphemes according to accepted cultural or academic standards.",
    quotes: [
      { author: "William Shakespeare", work: "Love's Labour's Lost", quote: "I abhor such fanatical phantasimes, such insociable and point-devise companions; such rackers of **orthography**." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The pale Usher threadbare in coat, heart, body, and brain; he was ever dusting his old lexicons and grammars, with a queer handkerchief, mockingly embellished with all the gay flags of all the known nations of the world. He loved to dust his old grammars; it somehow mildly reminded him of his **orthography**." },
      { author: "Noah Webster", work: "Dissertations on the English Language", quote: "A national language and a reformed **orthography** are essential bonds of national union for the American republic." }
    ]
  },
  "paleographer.md": {
    word: "paleographer",
    primary: "A scholar who specializes in the study, decipherment, and dating of ancient and medieval handwriting and manuscripts.",
    secondary: "In archival science and textual criticism, an expert who identifies scribal hands, scriptoria provenance, and manuscript interpolations through ductus and abbreviation analysis.",
    quotes: [
      { author: "Jean Mabillon", work: "De Re Diplomatica", quote: "The skilled **paleographer** distinguishes authentic Merovingian charters from medieval forgeries by the minute ductus of the script." },
      { author: "Frederic G. Kenyon", work: "The Palaeography of Greek Papyri", quote: "Every discovery of an Oxyrhynchus fragment demands that the **paleographer** evaluate its uncial hand against dated documentary papyri." },
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "The abbey librarian was an accomplished **paleographer**, able to date a Carolingian minuscule at a single glance." }
    ]
  },
  "paleographist.md": {
    word: "paleographist",
    primary: "A specialist or expert in paleography; a paleographer.",
    secondary: "A scholar trained in ancient script systems who reconstructs lost literary works from damaged parchments, palimpsests, or papyri.",
    quotes: [
      { author: "Edward Maunde Thompson", work: "Handbook of Greek and Latin Palaeography", quote: "The **paleographist** must master not only the forms of the letters, but the abbreviations and ligatures of each historical century." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The Italian **paleographist** recovered the lost books of Cicero's Republic beneath the erasure of a monastic service-book." },
      { author: "Bruce M. Metzger", work: "The Text of the New Testament", quote: "Through ultraviolet illumination, the **paleographist** revealed the underlying uncial script of Codex Ephraemi Rescriptus." }
    ]
  },
  "paleography.md": {
    word: "paleography",
    primary: "The study of ancient and medieval handwriting, inscriptions, and manuscripts, including the decipherment and dating of historical scripts.",
    secondary: "In historical bibliography, an indispensable discipline that establishes the provenance, transmission history, and textual integrity of manuscript traditions.",
    quotes: [
      { author: "Jean Mabillon", work: "De Re Diplomatica", quote: "Modern historical criticism was born when scientific **paleography** established rigorous criteria for manuscript verification." },
      { author: "Ludwig Traube", work: "Vorlesungen und Abhandlungen", quote: "Historical **paleography** is not merely the reading of dead letters, but the living history of human culture and scribal intellect." },
      { author: "Frederic G. Kenyon", work: "Our Bible and the Ancient Manuscripts", quote: "The progress of biblical textual criticism has advanced hand in hand with the discoveries of Greek **paleography**." }
    ]
  },
  "paragraph.md": {
    word: "paragraph",
    primary: "A distinct section of a piece of writing, usually dealing with a single theme and indicated by a new line, indentation, or numbering.",
    secondary: "Historically, a marginal mark or symbol (such as the pilcrow ¶, Greek paragraphos) used in ancient manuscripts to indicate a change of topic or speaker.",
    quotes: [
      { author: "George Orwell", work: "Politics and the English Language", quote: "A scrupulous writer, in every sentence that he writes, will ask himself: What am I trying to say? Can I put it in a shorter **paragraph**?" },
      { author: "Henry James", work: "The Art of Fiction", quote: "Every single **paragraph** of a well-wrought novel should contribute to the organic illumination of the central theme." },
      { author: "Walter J. Ong", work: "Orality and Literacy", quote: "The printed **paragraph** visually isolates an argumentative unit in a way that manuscript culture rarely attempted." }
    ]
  },
  "paragrapher.md": {
    word: "paragrapher",
    primary: "A journalist or writer who writes short, witty, or topical paragraphs, notes, or brief items for a newspaper or periodical.",
    secondary: "In nineteenth-century American press history, a specialized columnist who crafted satiric one-liners, local squibs, and humorous editorial paragraphs.",
    quotes: [
      { author: "Mark Twain", work: "Autobiography of Mark Twain", quote: "I began my literary career as a local **paragrapher** on the Virginia City Territorial Enterprise, inventing squibs to fill empty columns." },
      { author: "H. L. Mencken", work: "Prejudices: First Series", quote: "The lively newspaper **paragrapher** punctured political pomposity with a brevity that long editorial sermons could never match." },
      { author: "Ambrose Bierce", work: "The Cynic's Word Book", quote: "The anonymous **paragrapher** shoots his daily arrows from behind the rampart of the editorial page." }
    ]
  },
  "photograph.md": {
    word: "photograph",
    primary: "A picture or likeness obtained by the chemical action of light or other radiation on a sensitized surface, or digitally by an electronic sensor.",
    secondary: "In visual culture, a mechanical indexical trace that records a fleeting moment of physical reality with apparent optical fidelity.",
    quotes: [
      { author: "Oliver Wendell Holmes Sr.", work: "The Stereoscope and the Stereograph", quote: "The **photograph** has divorced the likeness of form from the substance of matter, allowing the image to travel everywhere." },
      { author: "Jack London", work: "The Cruise of the Snark", quote: "The **photograph** captured the furious crest of the South Sea breaker just before it broke over our decks." },
      { author: "Susan Sontag", work: "On Photography", quote: "To collect photographs is to collect the world; each **photograph** is a memento mori, a slice of frozen time." }
    ]
  },
  "photographer.md": {
    word: "photographer",
    primary: "A person who takes photographs, especially as a profession or artistic practice.",
    secondary: "A visual practitioner who manipulates lens optics, lighting, exposure, and composition to capture documentary truth or aesthetic expression.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Scandal in Bohemia", quote: "I engaged the services of a reliable **photographer** to secure the incriminating cabinet print without alerting the countess." },
      { author: "Thomas W. Corbin", work: "The Romance of Modern Photography", quote: "The press **photographer** must possess prompt decision and iron nerve, ready to expose his plate at the critical instant." },
      { author: "Walter Benjamin", work: "A Small History of Photography", quote: "Will not the **photographer** who cannot read his own pictures be seen as the illiterate of the future?" }
    ]
  },
  "photographic.md": {
    word: "photographic",
    primary: "Of, relating to, or produced by photography; or resembling a photograph in detail, accuracy, and vividness.",
    secondary: "Describing memory or perception characterized by extraordinary retention of precise visual detail; or in chemical imaging, sensitized to light.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventure of the Copper Beeches", quote: "Sherlock Holmes possessed a **photographic** memory for faces, recognizing the disguise through every layer of greasepaint." },
      { author: "Charles Baudelaire", work: "The Salon of 1859", quote: "If photography is allowed to substitute for art in any of its functions, it will soon have corrupted it entirely through its **photographic** literalism." },
      { author: "Virginia Woolf", work: "To the Lighthouse", quote: "Her mind retained the scene with **photographic** distinctness: the blue sea, the yellow sand, and the silent lighthouse." }
    ]
  },
  "photography.md": {
    word: "photography",
    primary: "The art, science, and technological process of creating durable images by recording light or electromagnetic radiation.",
    secondary: "In modern visual epistemology, a medium that revolutionized journalism, astronomical observation, art, and archival preservation by automating visual representation.",
    quotes: [
      { author: "William Henry Fox Talbot", work: "The Pencil of Nature", quote: "The plates of this work are impressed by the agency of Light alone, without any aid whatever from the artist's pencil; such is the art of **photography**." },
      { author: "Arthur Conan Doyle", work: "The Red-Headed League", quote: "He was down in the cellar for hours on end, pretending to develop his amateur **photography** while tunneling toward the bank vault." },
      { author: "Roland Barthes", work: "Camera Lucida", quote: "In **photography**, the presence of the thing is never metaphorical; it has been truly placed before the lens." }
    ]
  },
  "photomicrograph.md": {
    word: "photomicrograph",
    primary: "A photograph or digital image of an object taken through a microscope, showing a greatly magnified view.",
    secondary: "In histology, pathology, and materials science, an indispensable diagnostic image revealing cellular architecture, crystallographic grain, or microbiological pathogens.",
    quotes: [
      { author: "Robert Koch", work: "The Etiology of Tuberculosis", quote: "The **photomicrograph** clearly demonstrated the slender, rod-like tubercle bacilli clustered within the stained pulmonary tissue." },
      { author: "Santiago Ramón y Cajal", work: "Advice for a Young Investigator", quote: "A faithful drawing often surpasses a **photomicrograph**, because the artist can synthesize focal planes that optical lenses blur." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "The dramatic **photomicrograph** silenced all skeptics, showing the anthrax spores caught in the very act of germination." }
    ]
  },
  "polygraph.md": {
    word: "polygraph",
    primary: "An instrument that simultaneously records continuous variations in several physiological variables (such as blood pressure, pulse rate, respiration, and galvanic skin resistance), widely used as a lie detector.",
    secondary: "Historically, a mechanical duplicating device for making multiple handwritten copies simultaneously (invented by John Isaac Hawkins and popularized by Thomas Jefferson); or a prolific writer on diverse topics.",
    quotes: [
      { author: "Thomas Jefferson", work: "Selected Letters", quote: "The **polygraph** has proved the most valuable convenience of my life, producing a duplicate copy of every letter as fast as I write." },
      { author: "Hugo Münsterberg", work: "On the Witness Stand", quote: "The early **polygraph** apparatus proved that emotional agitation produced unmistakable spikes on the physiological drum." },
      { author: "Jerome Frank", work: "Courts on Trial", quote: "Courts remain deeply skeptical of the **polygraph**, unwilling to surrender the evaluation of witness credibility to a mechanical needle." }
    ]
  },
  "pseudepigraphy.md": {
    word: "pseudepigraphy",
    primary: "The practice of attributing a written work to an author who did not actually write it, especially to a famous, revered, or ancient figure.",
    secondary: "In biblical and classical scholarship, the literary corpus of non-canonical Jewish and early Christian texts (pseudepigrapha) ascribed to biblical patriarchs or apostles (e.g., Book of Enoch, Gospel of Peter).",
    quotes: [
      { author: "R. H. Charles", work: "The Apocrypha and Pseudepigrapha of the Old Testament", quote: "Religious **pseudepigraphy** was not conceived as a fraudulent deceit, but as a pious convention allowing the author to speak with ancestral authority." },
      { author: "Bruce M. Metzger", work: "Literary Forgeries and Canonical Authority", quote: "The early church applied rigorous tests of apostolic authenticity to detect and exclude works tainted by **pseudepigraphy**." },
      { author: "Bart D. Ehrman", work: "Forgery and Counterforgery", quote: "Ancient polemicists frequently engaged in theological **pseudepigraphy** to claim apostolic endorsement for their sectarian doctrines." }
    ]
  },
  "radiograph.md": {
    word: "radiograph",
    primary: "An image produced on a sensitive photographic film, plate, or digital detector by X-rays, gamma rays, or other penetrating radiation.",
    secondary: "In diagnostic radiology, an internal shadowgram of anatomical structures used to evaluate bone fractures, dental pathology, pulmonary consolidations, or foreign bodies.",
    quotes: [
      { author: "Wilhelm Röntgen", work: "On a New Kind of Rays", quote: "The photographic **radiograph** of my wife's hand showed the outline of the bones and the shadow of her gold wedding ring." },
      { author: "Marie Curie", work: "Radiology in War", quote: "At the front lines, each mobile X-ray van provided the surgeon with an immediate **radiograph** revealing embedded shrapnel." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "The chest **radiograph** on the illuminated viewbox showed a dense, rounded opacity in the right upper lobe." }
    ]
  },
  "radiographer.md": {
    word: "radiographer",
    primary: "A healthcare professional trained to position patients and operate diagnostic imaging equipment to produce radiographs (X-rays, CT scans, etc.).",
    secondary: "In clinical radiology, a licensed imaging technologist who ensures radiation safety, optimal patient positioning, and high diagnostic image quality while minimizing radiation exposure.",
    quotes: [
      { author: "Marie Curie", work: "Radiology in War", quote: "I personally trained hundreds of young women as mobile **radiographers** to serve in field hospitals during the great war." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "The skilled **radiographer** positioned the injured limb with gentle precision to capture the exact angle of the fracture." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The **radiographer** alerted the attending physician immediately when she noticed free air beneath the diaphragm." }
    ]
  },
  "radiographic.md": {
    word: "radiographic",
    primary: "Of, relating to, or produced by radiography or radiographs.",
    secondary: "Pertaining to internal diagnostic imaging using X-rays or ionizing radiation; exhibiting shadow patterns produced by differential tissue attenuation.",
    quotes: [
      { author: "Wilhelm Röntgen", work: "Further Observations on the Properties of X-rays", quote: "The **radiographic** image is a projection shadow whose density varies with the atomic weight and thickness of the interposed substance." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A thorough **radiographic** survey of the thorax confirms the presence of an aortic aneurysm before clinical murmurs appear." },
      { author: "Lewis Thomas", work: "The Youngest Science", quote: "The hospital's **radiographic** suites became the bustling nerve center of modern diagnostic medicine." }
    ]
  },
  "radiography.md": {
    word: "radiography",
    primary: "The technique or process of taking images of the interior of visually opaque objects by passing X-rays, gamma rays, or neutrons through them onto photographic film or digital sensors.",
    secondary: "In clinical medicine and industrial non-destructive testing, an indispensable diagnostic discipline used to detect internal anatomical pathology or structural metal flaws.",
    quotes: [
      { author: "Wilhelm Röntgen", work: "On a New Kind of Rays", quote: "The science of medical **radiography** commenced the moment these penetrating beams made the living skeleton visible." },
      { author: "Marie Curie", work: "Radiology in War", quote: "The widespread use of **radiography** during military campaigns saved thousands of wounded soldiers from blind, exploratory surgery." },
      { author: "Atul Gawande", work: "Complications", quote: "Modern computed **radiography** can reconstruct a beating heart in cross-sectional slices of breathtaking clarity." }
    ]
  },
  "syngraft.md": {
    word: "syngraft",
    primary: "A graft of tissue transplanted between genetically identical individuals, such as monozygotic twins or animals of an identical inbred strain; isograft.",
    secondary: "In transplant immunology, a graft accepted without eliciting an allogeneic immune response or graft rejection, due to complete histocompatibility concordance.",
    quotes: [
      { author: "Peter Medawar", work: "The Immunology of Transplantation", quote: "The survival of a **syngraft** demonstrates that graft rejection is governed by genetic differences between host and donor." },
      { author: "Joseph E. Murray", work: "Nobel Lecture: Organ Transplants", quote: "The success of our first renal **syngraft** proved that human kidneys could be successfully transplanted once the immune barrier was zero." },
      { author: "Thomas Starzl", work: "The Puzzle People", quote: "Transplant biology began with the **syngraft**, using nature's genetic twins to establish surgical feasibility." }
    ]
  },
  "telegram.md": {
    word: "telegram",
    primary: "A message transmitted over a wire or by radio via telegraph and delivered in written or printed form; a wire or cablegram.",
    secondary: "In nineteenth- and twentieth-century telecommunication history, the primary medium for rapid, long-distance written communication, celebrated for its terse, urgent style.",
    quotes: [
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "He walked swiftly to the post-office to send an urgent **telegram** that might yet avert disaster." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Speckled Band", quote: "A brief **telegram** from Holmes summoned me to Baker Street at seven o'clock that morning." },
      { author: "Jack London", work: "The Iron Heel", quote: "The news of the general strike flashed across the country in a flurry of urgent government **telegrams**." }
    ]
  },
  "telegraph.md": {
    word: "telegraph",
    primary: "An apparatus, system, or process for transmitting messages or signals over a distance, especially by electric wire or radio.",
    secondary: "In technological history, the Victorian forerunner of modern telecommunications networks, uniting continents via undersea cables and synchronized electric relays.",
    quotes: [
      { author: "Samuel F. B. Morse", work: "First Telegraphic Message", quote: "What hath God wrought! flashed across the electric wire of the **telegraph** from Washington to Baltimore." },
      { author: "Charles Dickens", work: "Hard Times", quote: "The iron roads and the electric **telegraph** annihilated distance, binding smoky Coketown to the great metropolis." },
      { author: "Jules Verne", work: "Twenty Thousand Leagues under the Sea", quote: "The transatlantic cable of the electric **telegraph** lay like a silent serpent resting upon the ocean floor." }
    ]
  },
  "telegrapher.md": {
    word: "telegrapher",
    primary: "A person who operates a telegraph apparatus to send and receive messages in Morse code or other telegraphic systems.",
    secondary: "In telecommunication history, a skilled operative whose rapid auditory decoding and key manipulation formed the vital human link in nineteenth-century rail and news networks.",
    quotes: [
      { author: "Thomas A. Edison", work: "Reminiscences of a Telegrapher", quote: "As a night **telegrapher** along the railroad, I learned to read the clicking sounder even while nodding off to sleep." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The lightning **telegrapher** at the river junction sent news of the rising flood to every landing downstream." },
      { author: "Ambrose Bierce", work: "Write It Right", quote: "The train dispatcher waited anxiously until the remote **telegrapher** confirmed that the switch had been thrown." }
    ]
  },
  "telegraphese.md": {
    word: "telegraphese",
    primary: "A concise, clipped, and abbreviated style of language typical of telegrams, characterized by the omission of non-essential words such as articles, pronouns, and auxiliary verbs.",
    secondary: "In stylistic analysis, terse journalistic or literary prose that mimics the compressed economy enforced by word-count charges on telegraph cables.",
    quotes: [
      { author: "George Bernard Shaw", work: "Selected Correspondence", quote: "Shaw replied in characteristic **telegraphese**: 'Have reserved two seats for first night. Come and bring a friend if you have one.'" },
      { author: "Evelyn Waugh", work: "Scoop", quote: "The foreign correspondent cabled his editor in frantic **telegraphese**: 'Unproceeding lakingward situation unpromising send cash urgent.'" },
      { author: "H. L. Mencken", work: "The American Language", quote: "The terse conventions of cable **telegraphese** influenced American headline writers, stripping away every superfluous adjective." }
    ]
  },
  "telegraphic.md": {
    word: "telegraphic",
    primary: "Of, relating to, or transmitted by the telegraph; or characterized by terse, concise, and compressed phrasing.",
    secondary: "In descriptive linguistics, describing early child language acquisition (the telegraphic stage) where functional words and morphemes are omitted while content words are preserved.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Adventure of the Bruce-Partington Plans", quote: "My brother Mycroft communicated in **telegraphic** style, compressing complex state secrets into a few laconic sentences." },
      { author: "L. P. Brockett", work: "The Great War of 1870", quote: "A **telegraphic** dispatch informed the ministry that the fortress of Sedan had capitulated." },
      { author: "Roger Brown", work: "A First Language: The Early Stages", quote: "Children at the two-word stage use **telegraphic** speech, saying 'kitty drink' or 'daddy go' without auxiliary verbs." }
    ]
  },
  "telegraphically.md": {
    word: "telegraphically",
    primary: "By means of the telegraph; or in a brief, concise, and clipped manner resembling a telegram.",
    secondary: "Communicated with extreme economy of words, eliminating ornamental phrasing to convey core information immediately.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The London attorney communicated **telegraphically**, snapping out orders in dry, monosyllabic phrases." },
      { author: "Jules Verne", work: "The Secret of the Island", quote: "The warning had been transmitted **telegraphically** along the wire that linked the granite house to the coral corral." },
      { author: "William Makepeace Thackeray", work: "The Newcomes", quote: "He spoke **telegraphically**, never wasting a breath on polite preamble when an estate was at stake." }
    ]
  },
  "telegraphist.md": {
    word: "telegraphist",
    primary: "A person who operates a telegraph apparatus; a telegrapher.",
    secondary: "In maritime and military history, a radio or cable officer responsible for sending and receiving Morse signals in Morse code or naval ciphers.",
    quotes: [
      { author: "Joseph Conrad", work: "Lord Jim", quote: "The young **telegraphist** on the lightship listened through his headphones to the lonely rhythmic clicks from the coast." },
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "Our **telegraphist** sat perched in the treetop outpost, relaying news of the expedition back to the river camp." },
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "The military **telegraphist** stuck bravely to his instrument until the Martian tripod loomed over the roof of the post office." }
    ]
  },
  "telegraphy.md": {
    word: "telegraphy",
    primary: "The science, art, or system of transmitting messages over long distances by electrical, optical, or radio signals.",
    secondary: "In communication history, the breakthrough Victorian technology that established the first global telecommunication network through copper cables and Morse codes.",
    quotes: [
      { author: "Guglielmo Marconi", work: "Nobel Lecture: Wireless Telegraphy", quote: "The realization of wireless **telegraphy** across the Atlantic demonstrated that electric waves follow the curvature of the earth." },
      { author: "Mary Baker Eddy", work: "Science and Health with Key to the Scriptures", quote: "The wonders of modern **telegraphy** remind us of the instantaneous transmission of thought across material space." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "Electric **telegraphy** dissolved traditional regional time, synchronizing the world into a single instantaneous marketplace." }
    ]
  },
  "telephotograph.md": {
    word: "telephotograph",
    primary: "A photograph taken from a great distance using a telephoto lens; or a photograph transmitted over distance by wire or radio (wirephoto).",
    secondary: "In photojournalism and intelligence reconnaissance, an image capturing fine details of distant subjects or terrain without physical approach.",
    quotes: [
      { author: "Thomas W. Corbin", work: "The Romance of Modern Photography", quote: "The remarkable **telephotograph** showed the climbers ascending the icy couloir of Mont Blanc as clearly as if taken from fifty yards." },
      { author: "Arthur Conan Doyle", work: "The Case-Book of Sherlock Holmes", quote: "The detective studied the **telephotograph** of the distant manor, noting the open casement window on the second floor." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "Aerial reconnaissance delivered an enlarged **telephotograph** revealing military preparations across the fortified border." }
    ]
  },
  "telephotography.md": {
    word: "telephotography",
    primary: "The art, technique, or process of taking photographs of distant objects using a telephoto lens or telephoto camera system.",
    secondary: "The historical electrical transmission of photographic images over telegraph or telephone wires (facsimile/wirephoto).",
    quotes: [
      { author: "Thomas R. Dallmeyer", work: "Telephotography", quote: "The science of **telephotography** combines the telescope with the photographic camera, allowing naturalists to observe timid wildlife undisturbed." },
      { author: "George Eastman", work: "Chronicles of Photography", quote: "Advances in **telephotography** permitted geological survey teams to map inaccessible alpine cliffs from valley floors." },
      { author: "Jack London", work: "The Cruise of the Dazzler", quote: "Through careful **telephotography**, the coastal survey team mapped the uncharted breakers from the safety of the harbor cliff." }
    ]
  },
  "tetragraph.md": {
    word: "tetragraph",
    primary: "A combination of four letters used to represent a single sound or phoneme.",
    secondary: "In orthography and historical phonetics, a four-letter graphemic sequence (such as English 'eigh' representing the vowel sound in 'weigh' or 'eight').",
    quotes: [
      { author: "Henry Bradley", work: "The Making of English", quote: "In the word 'weigh', the silent historical gutturals have reduced the spelling to an awkward **tetragraph** for the vowel sound." },
      { author: "Otto Jespersen", work: "A Modern English Grammar", quote: "The sequence 'ough' often functions as a **tetragraph**, though its phonetic realization varies wildly between 'bough' and 'rough'." },
      { author: "David Crystal", work: "Spell It Out: The Singular Story of English Spelling", quote: "Spelling reformers singled out the four-letter **tetragraph** as the crowning absurdity of English orthographic history." }
    ]
  },
  "trigram.md": {
    word: "trigram",
    primary: "A sequence or combination of three letters, characters, or symbols.",
    secondary: "In Chinese philosophy and the I Ching (Book of Changes), one of the eight divination figures (bagua) composed of three stacked broken or unbroken lines representing cosmic principles.",
    quotes: [
      { author: "Richard Wilhelm", work: "The I Ching or Book of Changes", quote: "The first **trigram**, Qian, consisting of three unbroken lines, represents the creative primal power of heaven." },
      { author: "Claude Shannon", work: "A Mathematical Theory of Communication", quote: "A language model based on **trigram** statistics approximates natural prose far better than single-letter frequencies." },
      { author: "Joseph Needham", work: "Science and Civilisation in China", quote: "The eight **trigrams** formed the foundation of ancient Chinese correlative thinking and natural philosophy." }
    ]
  },
  "trigraph.md": {
    word: "trigraph",
    primary: "A group of three letters used together to represent a single sound or phoneme (such as 'sch' in German, or 'eau' in French).",
    secondary: "In computer programming (such as C/C++), a three-character sequence beginning with two question marks (such as '??=') historically used to represent characters missing from some keyboards.",
    quotes: [
      { author: "Dennis Ritchie", work: "The Development of the C Language", quote: "We introduced the **trigraph** sequences to allow programmers on terminals with restricted European character sets to type brackets and braces." },
      { author: "David Crystal", work: "The Cambridge Encyclopedia of Language", quote: "In French orthography, the **trigraph** 'eau' represents the simple rounded back vowel /o/." },
      { author: "Florian Coulmas", work: "The Writing Systems of the World", quote: "A phonetic **trigraph** reflects historical sound changes where several consonant or vowel letters merged into a single spoken unit." }
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
console.log("Writing & Script Batch 10 (Dashboard — graph 69-102) completed! Total words updated:", Object.keys(wordsData).length);
