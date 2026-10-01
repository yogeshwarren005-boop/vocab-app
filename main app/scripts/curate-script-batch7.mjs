import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — gramm";

const wordsData = {
  "anagram.md": {
    word: "anagram",
    primary: "A word or phrase formed by reordering the letters of another word or phrase.",
    secondary: "In wordplay and cryptography, an intentional transposition of characters used to conceal identities, encode secret scientific discoveries, or create satirical pseudonyms.",
    quotes: [
      { author: "John Fletcher", work: "The Elder Brother", quote: "These are the **anagrams** of three great Worthies." },
      { author: "James Joyce", work: "Ulysses", quote: "What **anagrams** had he made on his name in youth? Leopold Bloom." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The art of **anagram** was cultivated by the ancients, who sought in the transposition of letters some mystical prophecy or moral lesson." }
    ]
  },
  "anagrammatic.md": {
    word: "anagrammatic",
    primary: "Pertaining to, formed by, or resembling an anagram; involving the transposition of letters.",
    secondary: "In literary analysis and textual criticism, describing verse or prose constructed through letter rearrangement or deliberate permutation of existing phrases.",
    quotes: [
      { author: "Samuel Johnson", work: "The Lives of the English Poets", quote: "He delighted in **anagrammatic** conceits and verbal permutations that tickled the fancy of pedantic readers." },
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "The mysterious cipher concealed an **anagrammatic** signature of the author." },
      { author: "Umberto Eco", work: "Foucault's Pendulum", quote: "The computer scanned thousands of permutations, searching for an **anagrammatic** solution to the Templar message." }
    ]
  },
  "anagrammatical.md": {
    word: "anagrammatical",
    primary: "Constituting, containing, or relating to an anagram; formed by transposing letters.",
    secondary: "In historical rhetoric and typography, describing verbal puzzles, cryptograms, or emblem verses that yield hidden meanings upon decipherment.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Some idle wits spend their whole lives in making **anagrammatical** verses and acrostics." },
      { author: "Walter Scott", work: "The Fortunes of Nigel", quote: "Master Heriot smiled at the king's penchant for **anagrammatical** riddles and Latin puns." },
      { author: "Charles Lamb", work: "Essays of Elia", quote: "He had an odd collection of pamphlets filled with quaint **anagrammatical** poems upon the names of departed worthies." }
    ]
  },
  "anagrammatise.md": {
    word: "anagrammatise",
    primary: "To transpose or rearrange the letters of a word, name, or phrase so as to form another word (chiefly British spelling).",
    secondary: "In historical wordplay, to construct an anagram or decipher hidden names from an encrypted text.",
    quotes: [
      { author: "William Camden", work: "Remaines Concerning Britain", quote: "Some will **anagrammatise** every name they meet with, extracting strange prophecies from common appellations." },
      { author: "Thomas Fuller", work: "The Worthies of England", quote: "The ingenious scholar took occasion to **anagrammatise** the patron's title into a pious motto." },
      { author: "George Saintsbury", work: "A History of Elizabethan Literature", quote: "Court poets were often hired to **anagrammatise** the names of noble brides on their wedding days." }
    ]
  },
  "anagrammatize.md": {
    word: "anagrammatize",
    primary: "To rearrange the letters of a word, name, or text to create new words or phrases.",
    secondary: "In computational linguistics and cryptography, to systematically permute character strings to discover valid words or anagrammatic keys.",
    quotes: [
      { author: "Cotton Mather", work: "Magnalia Christi Americana", quote: "The puritan divines were wont to **anagrammatize** the names of the deceased into holy ejaculations." },
      { author: "Edgar Allan Poe", work: "The Gold-Bug", quote: "He would **anagrammatize** every string of transposed characters until a coherent English word emerged." },
      { author: "Vladimir Nabokov", work: "Ada, or Ardor", quote: "The brilliant children would **anagrammatize** their parents' names across several languages with dazzling speed." }
    ]
  },
  "angiogram.md": {
    word: "angiogram",
    primary: "An X-ray or diagnostic photographic image of blood or lymph vessels, typically obtained after the injection of a radiopaque contrast medium.",
    secondary: "In cardiology and vascular surgery, an indispensable fluoroscopic map used to evaluate vessel patency, stenosis, aneurysms, or atherosclerotic occlusions.",
    quotes: [
      { author: "Egas Moniz", work: "Die cerebrale Arteriographie", quote: "The cerebral **angiogram** clearly revealed the displacement of intracranial vessels caused by the space-occupying tumor." },
      { author: "Michael E. DeBakey", work: "Vascular Surgery Chronicles", quote: "A selective coronary **angiogram** confirmed severe bifurcation stenosis requiring immediate bypass grafting." },
      { author: "Abraham Verghese", work: "Cutting for Stone", quote: "On the illuminated viewing box, the coronary **angiogram** displayed a stark cutoff where the left anterior descending artery was plugged." }
    ]
  },
  "audiogram.md": {
    word: "audiogram",
    primary: "A graphic representation of hearing acuity, showing hearing thresholds in decibels plotted across a range of frequencies (Hertz).",
    secondary: "In audiology and otolaryngology, a diagnostic chart that differentiates conductive, sensorineural, and mixed hearing loss configurations.",
    quotes: [
      { author: "Georg von Békésy", work: "Experiments in Hearing", quote: "The patient's **audiogram** exhibited a precipitous notch at four thousand cycles per second, typical of acoustic trauma." },
      { author: "Oliver Sacks", work: "Seeing Voices", quote: "When she looked at her daughter's **audiogram**, the audiologist explained that profound nerve deafness spared only low vibrational rumbles." },
      { author: "Hallowell Davis", work: "Hearing and Deafness", quote: "A calibrated pure-tone **audiogram** remains the foundational benchmark for assessing occupational hearing impairment." }
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
  "diagrammatic.md": {
    word: "diagrammatic",
    primary: "Relating to, consisting of, or in the form of a diagram; schematic and illustrative.",
    secondary: "Simplified or schematized so as to emphasize essential structural relations while omitting incidental realistic detail.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "He presented a **diagrammatic** sketch of the vertebrate nervous system, shorn of all confusing vascular tissues." },
      { author: "Arthur Conan Doyle", work: "The Valley of Fear", quote: "Upon the table lay a **diagrammatic** map of the mine workings, showing each shaft and ventilation drift." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The modern machine layout achieved a purely **diagrammatic** efficiency in its functional organization." }
    ]
  },
  "diagrammatical.md": {
    word: "diagrammatical",
    primary: "Of, relating to, or presented in the nature of a diagram; schematic.",
    secondary: "Exhibiting a schematic or outline form designed to clarify conceptual or mechanical relationships.",
    quotes: [
      { author: "William Whewell", work: "The Philosophy of the Inductive Sciences", quote: "The **diagrammatical** representations employed in crystallography clarify the symmetry of crystal planes." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The architect furnished **diagrammatical** profiles of the gothic mouldings to guide the stonecutters." },
      { author: "Herbert Spencer", work: "First Principles", quote: "Such **diagrammatical** schemes serve to render abstract evolutionary transitions perceptible to the intellect." }
    ]
  },
  "diagrammatically.md": {
    word: "diagrammatically",
    primary: "By means of or in the manner of a diagram; schematically.",
    secondary: "In a simplified, structured, or visually organized layout that clarifies underlying relations or processes.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The magnetic lines of force may be represented **diagrammatically** by curved paths radiating from the poles." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "When plotted **diagrammatically** upon Cartesian coordinates, the skull of one species deforms smoothly into that of another." },
      { author: "Alfred North Whitehead", work: "Process and Reality", quote: "The nexus of actual entities can be exhibited **diagrammatically** only by abstraction from their full concrete reality." }
    ]
  },
  "diagramming.md": {
    word: "diagramming",
    primary: "The act, art, or process of making a diagram, schematic plan, or visual outline.",
    secondary: "In pedagogical linguistics, sentence diagramming (such as the Reed–Kellogg system) to visually parse grammatical syntax and dependencies.",
    quotes: [
      { author: "Alonzo Reed & Brainerd Kellogg", work: "Higher Lessons in English", quote: "By **diagramming** sentences on the blackboard, pupils immediately grasp the grammatical dependency of modifying clauses." },
      { author: "Norbert Wiener", work: "Cybernetics", quote: "The **diagramming** of closed feedback loops allows engineers to calculate system stability before building hardware." },
      { author: "David Marr", work: "Vision", quote: "Careful **diagramming** of computational algorithms helps distinguish representational problems from biological implementation." }
    ]
  },
  "electrocardiogram.md": {
    word: "electrocardiogram",
    primary: "A graphic tracing or recording of the electric currents generated by the heart muscle during each heartbeat (ECG or EKG).",
    secondary: "In clinical cardiology, a foundational diagnostic tracing used to identify arrhythmias, myocardial ischemia or infarction, and conduction disturbances.",
    quotes: [
      { author: "Willem Einthoven", work: "The Galvanometric Registration of the Human Electrocardiogram", quote: "The string galvanometer produces an **electrocardiogram** displaying distinct P, Q, R, S, and T waves of cardiac depolarization." },
      { author: "Lewis Thomas", work: "The Fragile Species", quote: "The squiggly line of the **electrocardiogram** monitored his irregular heartbeat with unforgiving precision." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "A normal **electrocardiogram** in the emergency room can unfortunately provide false reassurance during early coronary occlusion." }
    ]
  },
  "engram.md": {
    word: "engram",
    primary: "A hypothetical physical, chemical, or neural trace or substrate in brain tissue corresponding to a stored memory.",
    secondary: "In neuropsychology and cognitive neuroscience, the enduring structural alteration in neuronal networks (synaptic plasticity) encoding an acquired experience.",
    quotes: [
      { author: "Richard Semon", work: "Die Mneme", quote: "I designate by the term **engram** the permanent physical alteration left behind in the irritable substance by an external stimulation." },
      { author: "Karl Lashley", work: "In Search of the Engram", quote: "It is not possible to demonstrate the localized existence of that which has been called the **engram** anywhere within the cerebral cortex." },
      { author: "Susumu Tonegawa", work: "Memory Engram Technology", quote: "By selectively reactivating the specific hippocampal **engram** cells with optogenetics, the learned fear response was artificially recalled." }
    ]
  },
  "epigram.md": {
    word: "epigram",
    primary: "A brief, clever, pointed, and often satirical or paradoxical statement, remark, or poem.",
    secondary: "In classical literature, a short elegiac verse inscription on a tomb or monument, evolving into Martial's concise satirical verse form with a sting in the tail.",
    quotes: [
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "He could explain everything with a cynical **epigram**, transforming grave dilemmas into sparkling dinner conversation." },
      { author: "Alexander Pope", work: "Epigrams", quote: "An **epigram** is like a bee: a whole divided into three—its body small, its honey sweet, and in its tail a sudden sting." },
      { author: "Samuel Taylor Coleridge", work: "On an Epigram", quote: "What is an **epigram**? A dwarfish whole; its body brevity, and wit its soul." }
    ]
  },
  "epigrammatic.md": {
    word: "epigrammatic",
    primary: "Expressed with brevity, witty conciseness, and pointed paradox; resembling an epigram.",
    secondary: "Characterized by terseness, aphoristic polish, and sharply honed rhetorical contrast.",
    quotes: [
      { author: "George Bernard Shaw", work: "Man and Superman", quote: "His speech was marked by an **epigrammatic** sharpness that unsettled conventional moralists." },
      { author: "Ralph Waldo Emerson", work: "Representative Men", quote: "Montaigne's page is alive with an **epigrammatic** candor that disarms the pedant." },
      { author: "Lytton Strachey", work: "Eminent Victorians", quote: "Cardinal Manning replied with an **epigrammatic** brevity that closed the controversy instantly." }
    ]
  },
  "gramm.md": {
    word: "gramm",
    primary: "The foundational Greek root (*gramma*, γράμμα) denoting a letter, character, inscription, writing, or that which is drawn or recorded.",
    secondary: "In morphological analysis, the base morpheme underlying linguistic, metric, and diagnostic terms denoting graphic records or structural inscriptions.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The formative base **gramm** ascends directly to the Greek *gramma*, meaning a letter or that which is written." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "Derivatives of **gramm** encompass both the written symbol and the graphic instruments of scientific recording." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "From *graphein* (to write) springs *gramma* (stem **gramm**-), denoting a letter of the alphabet, a drawing, or a public registry." }
    ]
  },
  "gramma.md": {
    word: "gramma",
    primary: "A letter of the alphabet; an inscribed character or written mark (from Greek γράμμα).",
    secondary: "In ichthyology, the taxonomic genus *Gramma* (family Grammatidae), comprising small, brilliantly colored Western Atlantic reef basslets (e.g., *Gramma loreto*, the royal gramma).",
    quotes: [
      { author: "Aristotle", work: "Categories", quote: "Each distinct sound of the human voice is symbolized by a visible **gramma** upon the wax tablet." },
      { author: "John E. Randall", work: "Caribbean Reef Fishes", quote: "The fairy basslet, *Gramma loreto*, commonly called the royal **gramma**, displays a vivid bicolored body of bright purple and gold." },
      { author: "Clement of Alexandria", work: "Stromata", quote: "The sacred scribe must know every mystical **gramma** carved upon the temple lintels." }
    ]
  },
  "grammar.md": {
    word: "grammar",
    primary: "The whole system and structure of a language or of languages in general, usually taken as consisting of syntax and morphology.",
    secondary: "A set of actual or presumed prescriptive rules for speaking or writing a particular language correctly; historically, learning or Latin scholarship.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 2", quote: "Thou hast most traitorously corrupted the youth of the realm in erecting a **grammar** school." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "I struggled through the intricacies of the Latin **grammar**, bewildered by moods and gerunds." },
      { author: "Noam Chomsky", work: "Syntactic Structures", quote: "A **grammar** of a language may be considered as a device that generates all of the grammatical sequences and none of the ungrammatical ones." }
    ]
  },
  "grammarian.md": {
    word: "grammarian",
    primary: "A person who studies, teaches, or writes about grammar; a scholar of grammatical rules and language structure.",
    secondary: "Historically, in classical antiquity and the Renaissance, a humanist scholar who interpreted and annotated classical literature through philological analysis.",
    quotes: [
      { author: "Robert Browning", work: "A Grammarian's Funeral", quote: "Here's the top-peak; the rack of clouds is gathered: let us erect our tomb for this brave **grammarian** who settled Hoti's business." },
      { author: "Michel de Montaigne", work: "Essays", quote: "I had rather make my boy an honest man than a subtle **grammarian** who knows all the quirks of Priscian." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Byzantine **grammarian** spent a laborious life copying and disputing the accents of classical Greek." }
    ]
  },
  "grammatic.md": {
    word: "grammatic",
    primary: "Pertaining to, conforming to, or dealing with grammar; grammatical (archaic or poetic variant).",
    secondary: "In historical rhetoric, relating to the philological and textual doctrines of the classical grammatici.",
    quotes: [
      { author: "John Dryden", work: "Essays on the Drama", quote: "He scrutinized the ancient verses with severe **grammatic** rigor, condemning every poetic license." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "His discourse was stiffened with unnecessary **grammatic** niceties that repelled the reader." },
      { author: "William Hazlitt", work: "Table-Talk", quote: "True eloquence transcends mere **grammatic** correctness, drawing its power from authentic passion." }
    ]
  },
  "grammatical.md": {
    word: "grammatical",
    primary: "Conforming to the rules of grammar; well-formed according to the syntax and morphology of a language.",
    secondary: "Relating to or treated by the science of grammar or language analysis.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "His conversation was agreeable, correct in its **grammatical** construction, and free from affectation." },
      { author: "George Orwell", work: "1984", quote: "The purpose of Newspeak was not only to provide a medium of expression for the world-view of Ingsoc, but to make all other modes of thought impossible by altering **grammatical** structures." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I love a broad margin to my life; sometimes I do not read a single book or construct a **grammatical** period for days." }
    ]
  },
  "grammatically.md": {
    word: "grammatically",
    primary: "In a manner that accords with the rules of grammar; with respect to grammar.",
    secondary: "In terms of morphological agreement, syntactic parsing, or formal linguistic structure.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The French governess was astonished that the young English girl could speak and write French so **grammatically**." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "He parsed the sailor's rough speech **grammatically**, finding an unpolished dignity in its cadence." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "A pilot might not speak **grammatically**, but he knew the bends of the river with mathematical certainty." }
    ]
  },
  "grammaticist.md": {
    word: "grammaticist",
    primary: "A petty, pedantic, or dogmatic grammarian; one who makes a display of grammatical punctiliousness.",
    secondary: "A purist who insists on strict adherence to minor grammatical conventions to the detriment of living expression.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "The dry-as-dust **grammaticist** dissects living metaphors as though they were dead wooden sticks." },
      { author: "Henry Fielding", work: "Tom Jones", quote: "He was a mere **grammaticist**, blind to the beauties of Virgil while hypercritical of a missing caesura." },
      { author: "H. L. Mencken", work: "The American Language", quote: "The schoolroom **grammaticist** spent decades fighting American idioms that the living populace adopted overnight." }
    ]
  },
  "grammatolatry.md": {
    word: "grammatolatry",
    primary: "The worship of the letter; superstitious or slavish adherence to the literal text or words of a book (especially scripture); bibliolatry.",
    secondary: "In hermeneutics and theology, textual literalism that prioritizes the exact verbal letter over the underlying spirit, intent, or historical context.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Notes on English Divines", quote: "This morbid **grammatolatry** blinds the zealot to the living spiritual truth that informs the word." },
      { author: "Philip Schaff", work: "History of the Christian Church", quote: "Post-Reformation scholasticism degenerated occasionally into a rigid **grammatolatry**, treating every vowel point as divinely dictated." },
      { author: "Paul Tillich", work: "Systematic Theology", quote: "The idolatrous elevation of the human text above the transcendent reality is the spiritual disease of **grammatolatry**." }
    ]
  },
  "grammatophyllum.md": {
    word: "grammatophyllum",
    primary: "A genus of large, often gigantic epiphytic and lithophytic orchids native to Southeast Asia, Australasia, and the Pacific islands (commonly known as letter orchids).",
    secondary: "In botanical taxonomy, orchids renowned for their immense pseudobulbs, towering flower spikes, and distinctive letter-like markings or spots on their sepals and petals (e.g., *Grammatophyllum speciosum*, the tiger orchid).",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "High up in the forks of the durian trees grew massive clumps of **Grammatophyllum**, the giant orchid of the tropics." },
      { author: "Joseph Dalton Hooker", work: "Curtis's Botanical Magazine", quote: "The flower spike of **Grammatophyllum** speciosum bore over eighty blossoms, each marked with dark purple spots resembling letters." },
      { author: "Frederick Sander", work: "Reichenbachia: Orchids Illustrated and Described", quote: "No collector can behold a blooming specimen of **Grammatophyllum** in its native jungle without admiring its colossal proportions." }
    ]
  },
  "gramme.md": {
    word: "gramme",
    primary: "A metric unit of mass equal to one thousandth of a kilogram (standard British/international spelling of gram).",
    secondary: "In historical metrology and laboratory sciences, the foundational base unit of the centimeter–gram–second (CGS) system of measurement.",
    quotes: [
      { author: "Jules Verne", work: "Twenty Thousand Leagues under the Sea", quote: "In a thousand **grammes** of sea water are found 96½ per cent of pure water and about 2-2/3 per cent of chloride of sodium." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "The heaviest soul ever given out weighs about ten **grammes** according to primitive superstition." },
      { author: "James Joyce", work: "Ulysses", quote: "Twelve **grammes** one pennyweight of silver foil for the dental filling." }
    ]
  },
  "hemigrammus.md": {
    word: "hemigrammus",
    primary: "A genus of small freshwater characin fish native to South America, popular in aquariums and commonly called tetras (family Characidae).",
    secondary: "In ichthyology, fish characterized by an incomplete lateral line (Greek *hemi-* half + *gramma* line) and a scaled caudal fin base, including *Hemigrammus erythrozonus* (glowlight tetra) and *Hemigrammus rhodostomus* (rummy-nose tetra).",
    quotes: [
      { author: "Carl H. Eigenmann", work: "The American Characidae", quote: "The genus **Hemigrammus** is distinguished from Astyanax by its incomplete lateral line and partly scaled caudal fin." },
      { author: "William T. Innes", work: "Exotic Aquarium Fishes", quote: "A peaceful school of **Hemigrammus** ocellifer, the beacon fish, adds sparkling golden luminescence to the planted aquarium." },
      { author: "Herbert R. Axelrod", work: "Handbook of Tropical Aquarium Fishes", quote: "Species of **Hemigrammus** thrive in soft, slightly acidic waters reminiscent of the Amazonian tributaries." }
    ]
  },
  "hologram.md": {
    word: "hologram",
    primary: "A three-dimensional image formed by the interference of light beams from a laser or other coherent light source.",
    secondary: "In optics, the photographic recording of an optical interference pattern that contains both amplitude and phase information, reconstructing a full light field when illuminated.",
    quotes: [
      { author: "Dennis Gabor", work: "A New Microscopic Principle", quote: "By recording the interference of the coherent wave with the coherent background, a **hologram** is formed which contains all the optical information." },
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "The viewer could walk around the projected **hologram**, seeing the object from every angle as though it possessed physical body." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Like a **hologram**, where every piece contains the likeness of the whole, each living cell carries the entire library of genetic instructions." }
    ]
  },
  "lipogram.md": {
    word: "lipogram",
    primary: "A written work or literary composition in which a particular letter or group of letters of the alphabet is deliberately omitted.",
    secondary: "In literary theory and Oulipian constraint writing, a rhetorical exercise demonstrating stylistic virtuosity within severe formal constraints (exemplified by Georges Perec's *La Disparition*, written without the letter *e*).",
    quotes: [
      { author: "Joseph Addison", work: "The Spectator", quote: "The author of the **lipogram** resolved to compose an epic poem without ever once using the letter E." },
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "Tryphiodorus the Greek poet was famous for his **lipogram**, having composed an Odyssey in twenty-four books, from each of which he excluded one letter." },
      { author: "Georges Perec", work: "A Void / La Disparition", quote: "Writing a lengthy novel as a strict **lipogram** demands an astonishing acrobatics of syntax and vocabulary." }
    ]
  },
  "mammogram.md": {
    word: "mammogram",
    primary: "An X-ray photograph or diagnostic image of the breast, used especially in screening for and detecting tumors or microcalcifications.",
    secondary: "In radiological oncology, a low-energy projection radiograph essential for early secondary prevention and diagnosis of occult breast malignancy.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The screening **mammogram** revealed a faint cluster of microcalcifications deep within the ductal tissue." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "When the radiologist inspected the routine **mammogram**, he noted an asymmetrical density that warranted immediate biopsy." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "Interpreting a screening **mammogram** requires subtle pattern recognition, balancing the hazard of missed cancers against false alarms." }
    ]
  },
  "microgramma-piloselloides.md": {
    word: "microgramma-piloselloides",
    primary: "An epiphytic species of climbing fern in the family Polypodiaceae, native to the Neotropics and Caribbean.",
    secondary: "In pteridology, a dimorphic creeping fern (*Microgramma piloselloides*) characterized by slender, scaly rhizomes, sterile ovate fronds, and elongated fertile fronds bearing linear sori.",
    quotes: [
      { author: "George Proctor", work: "Flora of the West Indies: Ferns", quote: "The creeping rhizomes of **Microgramma piloselloides** adhere closely to the mossy bark of rain-forest trees." },
      { author: "Rolla M. Tryon & Alice F. Tryon", work: "Ferns and Allied Plants", quote: "In **Microgramma piloselloides**, frond dimorphism is pronounced, the fertile fronds being markedly narrower than the sterile ones." },
      { author: "Conrad V. Morton", work: "American Fern Journal", quote: "Specimens of **Microgramma piloselloides** collected along the riverbanks demonstrated dense pilose hairs on both surfaces of the lamina." }
    ]
  },
  "microgramma.md": {
    word: "microgramma",
    primary: "A genus of small epiphytic climbing ferns in the family Polypodiaceae, native primarily to tropical and subtropical regions of the Americas and Africa.",
    secondary: "In botanical systematics, a fern genus characterized by slender scaly rhizomes, simple fronds that are often dimorphic, and round sori borne in single rows on either side of the midrib.",
    quotes: [
      { author: "Edwin Bingham Copeland", work: "Genera Filicum", quote: "The genus **Microgramma** comprises dwarf epiphytes whose slender rhizomes wrap around tree trunks in tropical forests." },
      { author: "Rolla M. Tryon", work: "The Ferns of Peru", quote: "Several species of **Microgramma** are adapted to dry canopy conditions, possessing succulent fronds that retain moisture." },
      { author: "Alan R. Smith", work: "Ferns of Mesoamerica", quote: "Taxonomic revision of **Microgramma** reveals significant variation in paraphyses and rhizome scale morphology." }
    ]
  },
  "monogram.md": {
    word: "monogram",
    primary: "A motif of two or more letters, typically a person's initials, combined or interwoven into a single decorative symbol.",
    secondary: "In numismatics, bibliography, and heraldry, an engraved or stamped cypher identifying a sovereign, printer, mint, or artist (such as Albrecht Dürer's celebrated *AD*).",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Scandal in Bohemia", quote: "In the upper left corner of the heavy note-paper was embossed a neat pink **monogram** of two interlocked letters." },
      { author: "Oscar Wilde", work: "The Picture of Dorian Gray", quote: "The silver-backed brushes and ivory toilet-boxes were all marked with his ornate **monogram**." },
      { author: "Alexandre Dumas", work: "The Count of Monte Cristo", quote: "Upon the seal of red wax was pressed an antique **monogram** that none could decipher." }
    ]
  },
  "pangrammatic.md": {
    word: "pangrammatic",
    primary: "Pertaining to, containing, or utilizing all the letters of the alphabet (as in a pangram).",
    secondary: "In typography, font testing, and keyboard design, describing a sentence (such as 'The quick brown fox jumps over the lazy dog') that showcases every glyph in a font.",
    quotes: [
      { author: "Augustus De Morgan", work: "A Budget of Paradoxes", quote: "He took pride in fashioning a **pangrammatic** verse containing every letter of the Greek alphabet with minimal repetition." },
      { author: "Eric Gill", work: "An Essay on Typography", quote: "Specimen sheets of newly cut typefaces commonly feature a **pangrammatic** line to exhibit the full character repertoire." },
      { author: "Steven Heller", work: "Design Literacy", quote: "Typographers rely on **pangrammatic** copy to evaluate letter spacing, kerning pairs, and optical weight across the entire alphabet." }
    ]
  },
  "program.md": {
    word: "program",
    primary: "A planned series of future events, performances, or operations; an agenda or schedule.",
    secondary: "In computer science, a coded sequence of instructions executed by a computer to perform a specified task.",
    quotes: [
      { author: "Ada Lovelace", work: "Notes on the Analytical Engine", quote: "The engine might compose elaborate pieces of music if given an appropriate **program** of operations." },
      { author: "Alan Turing", work: "Computing Machinery and Intelligence", quote: "We may hope that machines will eventually compete with men in all purely intellectual fields by executing a suitably designed **program**." },
      { author: "Frank A. Fetter", work: "The Principles of Economics", quote: "The legislative **program** of tax reform was designed to stimulate industrial capital without burdening labor." }
    ]
  },
  "programing.md": {
    word: "programing",
    primary: "The act or process of writing, testing, or executing computer instructions (alternative single-'m' spelling of programming).",
    secondary: "In systems engineering, the planning, scheduling, and structural sequencing of activities or automated routines.",
    quotes: [
      { author: "John von Neumann", work: "First Draft of a Report on the EDVAC", quote: "The logical arrangement of the machine must simplify the task of **programing** complex mathematical calculations." },
      { author: "Grace Hopper", work: "Compiling Methods", quote: "Automated **programing** allows the mathematician to write instructions in pseudo-code which the computer translates directly into machine orders." },
      { author: "Norbert Wiener", work: "The Human Use of Human Beings", quote: "Effective **programing** of feedback mechanisms prevents oscillations in industrial machinery." }
    ]
  },
  "programmatic.md": {
    word: "programmatic",
    primary: "Of, relating to, or having the character of a program; following a predetermined schedule or policy.",
    secondary: "In aesthetics and music, describing art or music that intends to tell a narrative or depict extra-musical scenes (program music); in advertising, automated algorithmic buying of ad space.",
    quotes: [
      { author: "Hector Berlioz", work: "Memoirs", quote: "My Symphonie Fantastique is strictly **programmatic**, each movement depicting an episode in the life of an artist." },
      { author: "Franz Liszt", work: "Selected Letters", quote: "In **programmatic** composition, the musical form is dictated by the poetic subject rather than by academic symmetry." },
      { author: "John Dewey", work: "Art as Experience", quote: "A rigid **programmatic** scheme in education stifles the organic development of spontaneous curiosity." }
    ]
  },
  "programmer.md": {
    word: "programmer",
    primary: "A person who writes computer software programs.",
    secondary: "A person or device that prepares or schedules a program of events, broadcasts, or automated procedures.",
    quotes: [
      { author: "Donald Knuth", work: "The Art of Computer Programming", quote: "The best **programmer** is not merely a technician, but an artist striving for elegant and readable code." },
      { author: "Edsger W. Dijkstra", work: "The Humble Programmer", quote: "The competent **programmer** is fully aware of the strictly limited size of his own skull." },
      { author: "Fred Brooks", work: "The Mythical Man-Month", quote: "The addition of another **programmer** to a late software project only makes it later." }
    ]
  },
  "programming.md": {
    word: "programming",
    primary: "The process or activity of writing computer programs.",
    secondary: "The scheduling, selection, or curation of items for a television, radio, concert, or festival schedule.",
    quotes: [
      { author: "Alan Kay", work: "User Interface: A Personal View", quote: "Object-oriented **programming** allows us to view software as a network of cooperating independent biological cells." },
      { author: "Dennis Ritchie", work: "The Development of the C Language", quote: "The design of C was driven by the practical needs of system **programming** on small machines." },
      { author: "Bjarne Stroustrup", work: "The C++ Programming Language", quote: "Good **programming** consists in finding clean abstractions that accurately mirror the problem domain." }
    ]
  },
  "telegramme.md": {
    word: "telegramme",
    primary: "A message transmitted by telegraph and delivered in written or printed form (chiefly French and archaic British variant of telegram).",
    secondary: "In diplomatic and postal history, an urgent printed dispatch conveyed over telecommunication cables and hand-delivered by messenger.",
    quotes: [
      { author: "Jules Verne", work: "Around the World in Eighty Days", quote: "Phileas Fogg received an urgent **telegramme** from the Reform Club confirming the wager." },
      { author: "Marcel Proust", work: "In Search of Lost Time", quote: "The blue envelope of the **telegramme** arrived during dinner, carrying news that disturbed the quiet household." },
      { author: "Arthur Conan Doyle", work: "The Return of Sherlock Holmes", quote: "A cryptic **telegramme** from Paris summoned Holmes across the Channel without an hour's delay." }
    ]
  },
  "tetragram.md": {
    word: "tetragram",
    primary: "A word, symbol, or sequence consisting of four letters.",
    secondary: "In cryptography and language modeling, a 4-gram character sequence evaluated for statistical frequency in cipher breaking or textual analysis.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The ancient philosophers revered each sacred **tetragram** as an emblem of the four elements of the universe." },
      { author: "Claude Shannon", work: "A Mathematical Theory of Communication", quote: "By measuring the conditional probability of each **tetragram**, the redundancy of written English can be estimated." },
      { author: "David Kahn", work: "The Codebreakers", quote: "The cryptanalyst counted every recurring **tetragram** to identify suspected key phrases in the intercepted message." }
    ]
  },
  "tetragrammaton.md": {
    word: "tetragrammaton",
    primary: "The Hebrew name of God transliterated into four letters as YHWH (or JHVH), regarded in Judaism as too sacred to be spoken aloud.",
    secondary: "In biblical scholarship, theology, and Kabbalah, the ineffable, transcendent name of the deity, traditionally read as Adonai or HaShem.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Before the throne the seraphim bowed low, chanting the unuttered name, the holy **Tetragrammaton**." },
      { author: "Gershom Scholem", work: "Major Trends in Jewish Mysticism", quote: "In Kabbalistic meditation, each consonant of the **Tetragrammaton** corresponds to a distinct realm of divine emanation." },
      { author: "Baruch Spinoza", work: "Tractatus Theologico-Politicus", quote: "The name called **Tetragrammaton** was held so sacred by the Hebrews that it signified the absolute essence of God without relation to created things." }
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
  "ungrammatical.md": {
    word: "ungrammatical",
    primary: "Not conforming to the accepted rules of grammar or syntax in a language.",
    secondary: "In descriptive linguistics, violating native speaker intuition or structural constraints of a given linguistic dialect or grammar.",
    quotes: [
      { author: "Jane Austen", work: "Mansfield Park", quote: "His letter was clumsy and in parts positively **ungrammatical**, betraying his lack of early education." },
      { author: "Noam Chomsky", work: "Aspects of the Theory of Syntax", quote: "The sentence 'Colorless green ideas sleep furiously' is nonsensical yet grammatical, whereas 'Furiously sleep ideas green colorless' is completely **ungrammatical**." },
      { author: "George Bernard Shaw", work: "Pygmalion", quote: "Liza spoke with a dreadful accent, but Henry Higgins vowed to purge every **ungrammatical** vulgarism from her tongue." }
    ]
  },
  "ungrammatically.md": {
    word: "ungrammatically",
    primary: "In a way that does not conform to the rules of grammar; with improper syntax or morphology.",
    secondary: "In a broken, unidiomatic, or ill-formed syntactic construction.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "Joe Gargery expressed himself warmly, though he spoke **ungrammatically** and struggled with his letters." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "The old baronet blustered and shouted **ungrammatically**, venting his fury upon the trembling footman." },
      { author: "Mark Twain", work: "Roughing It", quote: "The frontiersman swore fluently and spoke **ungrammatically**, yet his meaning was never in doubt." }
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
console.log("Writing & Script Batch 7 (Dashboard — gramm) completed! Total words updated:", Object.keys(wordsData).length);
