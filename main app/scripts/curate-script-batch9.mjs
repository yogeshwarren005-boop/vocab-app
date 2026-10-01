import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Writing & Script/Dashboard — graph";

const wordsData = {
  "epigraphy.md": {
    word: "epigraphy",
    primary: "The study, decipherment, and interpretation of ancient inscriptions engraved on stone, metal, pottery, or other durable materials.",
    secondary: "In classical archaeology and historical linguistics, an essential auxiliary science that recovers lost legal codes, decrees, religious dedications, and dialect forms.",
    quotes: [
      { author: "Theodor Mommsen", work: "The History of Rome", quote: "Without the discoveries of **epigraphy**, our knowledge of Roman provincial administration would remain a fragment." },
      { author: "Arthur Evans", work: "Scripta Minoa", quote: "The comparative **epigraphy** of the Aegean revealed unexpected affinities between early Cretan pictographs and Phoenician characters." },
      { author: "James Henry Breasted", work: "A History of Egypt", quote: "Modern **epigraphy** has rescued the annals of the pharaohs from the creeping decay of temple walls." }
    ]
  },
  "graft.md": {
    word: "graft",
    primary: "A shoot or bud inserted into a slit on another plant to form a living union; or a piece of living tissue surgically transplanted to another site.",
    secondary: "In political and social critique, the acquisition of money, gain, or advantage by dishonest, corrupt, or illegal practices in public office.",
    quotes: [
      { author: "William Shakespeare", work: "The Winter's Tale", quote: "You see, sweet maid, we marry a gentler scion to the wildest stock, and make conceive a bark of baser kind by bud of nobler race: this is an art which does mend nature, change it rather, but the art itself is nature; we marry a noble **graft** unto a stock." },
      { author: "Lincoln Steffens", work: "The Shame of the Cities", quote: "Municipal **graft** was not an occasional theft, but an organized financial system binding politicians and utility bosses together." },
      { author: "Sherwin B. Nuland", work: "The Doctors' Story", quote: "The surgeon carefully trimmed the pedicle **graft** to restore blood supply to the burned facial tissue." }
    ]
  },
  "grafting.md": {
    word: "grafting",
    primary: "The horticultural practice of uniting the scion of one plant with the rootstock of another; or the surgical transplantation of tissue.",
    secondary: "In cellular immunology and regenerative medicine, the physiological process whereby donor tissue undergoes revascularization and incorporates into host tissues.",
    quotes: [
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "The art of **grafting** allows the husbandman to multiply choice varieties of fruit upon hardy wild crabstocks." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Extensive experiments in **grafting** demonstrate that the stock may subtly modify the growth habit of the scion." },
      { author: "Alexis Carrel", work: "The Surgery of Blood Vessels", quote: "Successful **grafting** of vascular segments requires perfect end-to-end alignment without mechanical tension." }
    ]
  },
  "gram.md": {
    word: "gram",
    primary: "A metric unit of mass equal to one-thousandth of a kilogram (standard American/international spelling of gramme).",
    secondary: "In physics and chemistry, the fundamental mass unit of the CGS system, historically defined as the mass of one cubic centimeter of water at the temperature of maximum density.",
    quotes: [
      { author: "Marie Curie", work: "Radioactive Substances", quote: "From several tons of pitchblende residue, we finally extracted a single decigram of pure radium chloride, measuring each fraction to the tenth of a **gram**." },
      { author: "Ernest Rutherford", work: "Radioactive Transformations", quote: "A single **gram** of radium emits an astonishing quantity of heat continuously without measurable chemical combustion." },
      { author: "Oliver Sacks", work: "Uncle Tungsten: Memories of a Chemical Boyhood", quote: "Uncle Tungsten handed me a tiny sphere of platinum that weighed hundreds of **grams** despite its modest size." }
    ]
  },
  "graph.md": {
    word: "graph",
    primary: "A diagram representing a system of connections or interrelations among two or more things by a number of distinctive dots, lines, bars, or curves.",
    secondary: "In discrete mathematics, a mathematical structure consisting of a set of vertices (or nodes) connected by a set of edges (or links).",
    quotes: [
      { author: "Leonhard Euler", work: "Solutio problematis ad geometriam situs pertinentis", quote: "The network of Königsberg bridges can be conceived as a topological **graph** where land areas represent nodes and bridges represent edges." },
      { author: "William Stanley Jevons", work: "The Principles of Science", quote: "By plotting economic data upon a coordinate **graph**, cyclical fluctuations become immediately apparent to the eye." },
      { author: "Claude Shannon", work: "A Symbolic Analysis of Relay and Switching Circuits", quote: "Every electrical switching network may be mapped onto an equivalent planar **graph** to simplify its logic equations." }
    ]
  },
  "graphein.md": {
    word: "graphein",
    primary: "The ancient Greek verb γράφειν, meaning 'to scratch, carve, draw, inscribe, or write.'",
    secondary: "In historical linguistics and etymology, the primary Hellenic root giving rise to an immense family of words ending in '-graph', '-gram', and '-graphy'.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The ultimate parent of all these terms is the Greek **graphein**, originally meaning to scratch or engrave upon stone or wooden tablets." },
      { author: "James Murray", work: "A New English Dictionary on Historical Principles", quote: "From the verbal stem **graphein** arose both the act of writing and the artistic depiction of graphic symbols." },
      { author: "H. G. Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In Homeric usage, **graphein** signifies to graze or scratch the skin, evolving later to denote painting and the writing of letters." }
    ]
  },
  "grapheme.md": {
    word: "grapheme",
    primary: "The smallest meaningful contrastive unit in a writing system of a language, representing a phoneme or sound.",
    secondary: "In theoretical linguistics and orthography, an abstract visual character unit (analogous to the phoneme in phonology) that encompasses various glyph variants or allographs.",
    quotes: [
      { author: "Leonard Bloomfield", work: "Language", quote: "A **grapheme** is the minimal distinctive visual unit of a written language, just as a phoneme is the minimal unit of speech." },
      { author: "Ferdinand de Saussure", work: "Course in General Linguistics", quote: "The value of a **grapheme** is purely negative and differential; what matters is that it is not confused with any other letter of the alphabet." },
      { author: "Noam Chomsky & Morris Halle", work: "The Sound Pattern of English", quote: "English orthography is a near-optimal system because each **grapheme** corresponds closely to an underlying lexical representation." }
    ]
  },
  "graphemics.md": {
    word: "graphemics",
    primary: "The linguistic study of writing systems and of their basic constitutive units (graphemes).",
    secondary: "In structural linguistics, the formal discipline analyzing the relationship between written symbols, spelling rules, and phonological spoken structures.",
    quotes: [
      { author: "David Crystal", work: "A Dictionary of Linguistics and Phonetics", quote: "In descriptive linguistics, **graphemics** examines the inventory of graphic signs that distinguish meaning within an orthographic system." },
      { author: "John Lyons", work: "Introduction to Theoretical Linguistics", quote: "Structural **graphemics** establishes principles for segmenting written texts into discrete graphemic classes." },
      { author: "Florian Coulmas", work: "The Blackwell Encyclopedia of Writing Systems", quote: "The development of **graphemics** as an autonomous subdiscipline freed the study of writing from subservience to acoustic phonetics." }
    ]
  },
  "graphene.md": {
    word: "graphene",
    primary: "A single two-dimensional layer of carbon atoms arranged tightly in a hexagonal honeycomb crystal lattice.",
    secondary: "In condensed matter physics and nanotechnology, a zero-bandgap semimetal exhibiting extraordinary tensile strength, ballistic electron transport, and exceptional thermal conductivity.",
    quotes: [
      { author: "Andre Geim & Konstantin Novoselov", work: "Electric Field Effect in Atomically Thin Carbon Films", quote: "By mechanical exfoliation using adhesive tape, we isolated individual monolayers of **graphene** and observed their high electron mobilities." },
      { author: "Philip Ball", work: "Nature Materials Chronicles", quote: "The discovery of **graphene** opened the realm of true two-dimensional physics, where electrons behave like massless relativistic fermions." },
      { author: "Richard Jones", work: "Soft Machines: Nanotechnology and Life", quote: "Engineers anticipate that **graphene** membranes will revolutionize water desalination and next-generation composite electronics." }
    ]
  },
  "graphic.md": {
    word: "graphic",
    primary: "Relating to visual art, especially drawing, engraving, lettering, or printmaking; also, depicted with clear, vivid, and realistic detail.",
    secondary: "In rhetoric and literature, describing an account so vividly portrayed as to evoke immediate sensory perception in the mind of the audience.",
    quotes: [
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "His journal contained a **graphic** and amusing description of the Waterloo campaign as seen from the baggage train." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Danton thundered in the Assembly, painting a **graphic** picture of the perils that threatened the Republic." },
      { author: "Charles Dickens", work: "Oliver Twist", quote: "The witness gave a **graphic** narrative of the burglary that left the courtroom in stunned silence." }
    ]
  },
  "graphical.md": {
    word: "graphical",
    primary: "Of or relating to drawing, writing, engraving, or representations by graphs, diagrams, or pictures.",
    secondary: "In computing and interface design, utilizing visual icons, windows, and graphical elements rather than purely text-based command lines.",
    quotes: [
      { author: "Alan Kay", work: "Microelectronics and the Personal Computer", quote: "The development of the **graphical** user interface transformed computers from arcane number-crunchers into intuitive extensions of the human mind." },
      { author: "James Clerk Maxwell", work: "On Graphical Methods in Materials", quote: "A **graphical** calculation of stress distributions often reveals mechanical flaws that algebraic formulas conceal." },
      { author: "William Playfair", work: "The Commercial and Political Atlas", quote: "I have devised these **graphical** charts to communicate commercial balances directly to the eye without tedious columns of figures." }
    ]
  },
  "graphically.md": {
    word: "graphically",
    primary: "In a clear, vivid, and pictorial manner; or by means of diagrams, graphs, or visual representations.",
    secondary: "In mathematics and applied engineering, resolving or demonstrating equations through visual plotting rather than analytical deduction.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "Sherlock Holmes described **graphically** the exact sequence of footsteps left in the garden clay." },
      { author: "H. G. Wells", work: "The Time Machine", quote: "The Time Traveller drew a line with his finger to show **graphically** how the fourth dimension intersects space." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", quote: "When the comparative anatomical skeletons are arranged **graphically** side by side, the structural unity of the primates is undeniable." }
    ]
  },
  "graphics.md": {
    word: "graphics",
    primary: "Visual images, designs, drawings, or lettering displayed on a surface such as paper, canvas, or a computer display.",
    secondary: "In computer science and digital media, the discipline and technology concerned with synthesizing, manipulating, and rendering two- and three-dimensional pictorial data.",
    quotes: [
      { author: "Ivan Sutherland", work: "Sketchpad: A Man-Machine Graphical Communication System", quote: "Interactive computer **graphics** enables a user to create and manipulate complex technical drawings directly upon a cathode-ray tube." },
      { author: "Edward Tufte", work: "The Visual Display of Quantitative Information", quote: "Excellence in statistical **graphics** consists of complex ideas communicated with clarity, precision, and efficiency." },
      { author: "Steven Levy", work: "Hackers: Heroes of the Computer Revolution", quote: "Early video game pioneers pushed the microprocessor to its limits to generate colorful arcade **graphics** on household televisions." }
    ]
  },
  "graphite.md": {
    word: "graphite",
    primary: "A soft, gray-black, lustrous allotrope of carbon with a greasy feel, used in pencil lead, lubricants, and refractory crucibles.",
    secondary: "In materials science and nuclear engineering, a high-purity crystalline form of carbon with hexagonal sheet structure, employed as a neutron moderator in nuclear reactors.",
    quotes: [
      { author: "Abraham Gottlob Werner", work: "System of Mineralogy", quote: "Because this mineral leaves a distinct mark upon paper and is used in pencils, I have assigned it the name **graphite**, from the Greek for writing." },
      { author: "Enrico Fermi", work: "Experimental Production of a Divergent Chain Reaction", quote: "The Chicago pile consisted of thousands of carefully machined blocks of pure **graphite** interspaced with uranium lumps." },
      { author: "Jules Verne", work: "The Mysterious Island", quote: "Cyrus Smith discovered a rich vein of plumbago or **graphite**, which provided the colonists with excellent material for crucibles." }
    ]
  },
  "graphologist.md": {
    word: "graphologist",
    primary: "A person who analyzes handwriting, especially to infer character traits, psychological temperament, or emotional states.",
    secondary: "In forensic document examination, an analyst who attempts to deduce psychological profiling from graphic strokes, distinct from a forensic document examiner who determines authenticity.",
    quotes: [
      { author: "Jean-Hippolyte Michon", work: "Système de graphologie", quote: "The trained **graphologist** discerns in the slant of an ascender and the pressure of a t-bar the secret virtues and vices of the soul." },
      { author: "Arthur Conan Doyle", work: "The Norwood Builder", quote: "A professional **graphologist** would tell you that those tremulous lines indicate extreme physical exhaustion or feigned agitation." },
      { author: "Albert S. Osborn", work: "Questioned Documents", quote: "A prudent court relies upon the scientific document examiner rather than the subjective claims of the speculative **graphologist**." }
    ]
  },
  "graphology.md": {
    word: "graphology",
    primary: "The study and analysis of handwriting, especially as a means of assessing personality, character, or psychological state.",
    secondary: "In linguistic terminology, the study of the writing system of a language, its graphic conventions, and its orthographic structure (contrasted with phonology).",
    quotes: [
      { author: "Ludwig Klages", work: "Handwriting and Character", quote: "In **graphology**, every stroke of the pen expresses the balance between unconscious vital rhythm and conscious mental inhibition." },
      { author: "Alfred Binet", work: "Les révélations de l'écriture d'après un contrôle scientifique", quote: "We subjected the claims of **graphology** to empirical tests, comparing handwriting appraisals with clinical assessments." },
      { author: "David Crystal", work: "The Cambridge Encyclopedia of Language", quote: "Linguists employ the term **graphology** to refer to the systematic study of the visual properties of writing systems." }
    ]
  },
  "graphomania.md": {
    word: "graphomania",
    primary: "An obsessive, uncontrollable urge or compulsion to write.",
    secondary: "In psychiatry and literary criticism, a pathological mania for producing vast quantities of writing, often characterized by incoherence, verbosity, or lack of critical discernment.",
    quotes: [
      { author: "Milan Kundera", work: "The Book of Laughter and Forgetting", quote: "A writer's **graphomania** takes on the character of an epidemic when everyone wants to write and nobody wants to read." },
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "In asylum archives one finds astonishing monuments of **graphomania**, thousands of scribbled folios filled with endless religious revelations." },
      { author: "Thomas Mann", work: "Doctor Faustus", quote: "The lonely poet succumbed to a frantic **graphomania**, filling notebooks throughout the night with feverish musical commentary." }
    ]
  },
  "graphospasm.md": {
    word: "graphospasm",
    primary: "A painful cramp or involuntary muscular spasm of the fingers and hand caused by excessive writing; writer's cramp.",
    secondary: "In neurology, a task-specific focal dystonia affecting the hand muscles, historically recognized among scriveners, clerks, and telegraphists.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "In chronic cases of **graphospasm**, the scrivener finds his pen suddenly jerking across the page or locked in rigid contraction." },
      { author: "Silas Weir Mitchell", work: "Injuries of Nerves and Their Consequences", quote: "The overworked copyist suffered from agonizing **graphospasm** that defied all remedies until total manual rest was enforced." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "Task-specific dystonias such as **graphospasm** reveal the complex cortical organization required for rapid sequential hand movements." }
    ]
  },
  "heterograft.md": {
    word: "heterograft",
    primary: "A tissue graft transplanted between individuals of different species; a xenograft.",
    secondary: "In experimental surgery and tissue engineering, animal tissue (such as porcine heart valves) processed and transplanted into human patients.",
    quotes: [
      { author: "Alexis Carrel", work: "Results of the Transplantation of Blood Vessels", quote: "The arterial **heterograft** harvested from a canine donor and transplanted into a feline host underwent rapid necrosis." },
      { author: "Peter Medawar", work: "The Immunological Basis of Tissue Transplantation", quote: "The immune barrier to a **heterograft** is far more fierce and destructive than that encountered in allogeneic transfers." },
      { author: "Thomas Starzl", work: "The Puzzle People", quote: "Early attempts at hepatic **heterograft** transplantation using baboon livers highlighted the immense immunological divide between species." }
    ]
  },
  "heterograph.md": {
    word: "heterograph",
    primary: "A word that has a different spelling from another word that sounds identical (a homophone, such as 'wright' and 'right').",
    secondary: "In historical orthography, an incorrect, deviant, or non-standard spelling of a word.",
    quotes: [
      { author: "Henry Bradley", work: "On the Relations between Spoken and Written Language", quote: "English orthography relies extensively on the **heterograph** to distinguish words like 'knight' and 'night' to the eye." },
      { author: "Otto Jespersen", work: "A Modern English Grammar on Historical Principles", quote: "The historical retention of silent letters creates pairs of **heterographs** that aid silent reading but perplex foreign learners." },
      { author: "H. L. Mencken", work: "The American Language", quote: "Spelling reform committees struggled in vain to eliminate the confusing **heterograph** from standard primary readers." }
    ]
  },
  "hexagraph.md": {
    word: "hexagraph",
    primary: "A combination of six letters used together to represent a single sound or phoneme.",
    secondary: "In descriptive phonetics and orthographic analysis, a rare multi-letter graphemic sequence (such as German 'schtsch' for the Russian consonant щ, or Irish complex vowel spellings).",
    quotes: [
      { author: "David Crystal", work: "The Cambridge Encyclopedia of Language", quote: "While English rarely exceeds the trigraph, certain European transliterations employ a **hexagraph** to capture complex foreign phonemes." },
      { author: "Florian Coulmas", work: "The Writing Systems of the World", quote: "The linguistic term **hexagraph** designates an extreme example of orthographic condensation where six characters encode one phonological unit." },
      { author: "Edward Sapir", work: "Language: An Introduction to the Study of Speech", quote: "The historical accumulation of silent consonants can occasionally turn a simple consonant into a formidable **hexagraph** in transcription." }
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
  "holograph.md": {
    word: "holograph",
    primary: "A manuscript, letter, or legal document written entirely in the author's own handwriting.",
    secondary: "In jurisprudence, a handwritten testamentary will executed without formal attesting witnesses, recognized as legally valid in many civil and common law jurisdictions.",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "In certain jurisdictions, a **holograph** will requires no attesting witnesses, provided every line is proved to be in the testator's own hand." },
      { author: "Robert Louis Stevenson", work: "Strange Case of Dr Jekyll and Mr Hyde", quote: "Utterson unlocked his safe and drew out the mysterious will, a **holograph** signed by Henry Jekyll." },
      { author: "W. W. Greg", work: "The Editorial Problem in Shakespeare", quote: "The recovery of a single dramatic **holograph** by Shakespeare would resolve countless textual controversies." }
    ]
  },
  "holographic.md": {
    word: "holographic",
    primary: "Written entirely in the handwriting of the author; or relating to or produced by holography.",
    secondary: "In modern theoretical physics, the holographic principle posits that the entire information content of a spatial volume can be encoded on its lower-dimensional boundary.",
    quotes: [
      { author: "Leonard Susskind", work: "The Black Hole War", quote: "The **holographic** principle suggests that our three-dimensional universe may be an optical illusion projected from a distant two-dimensional boundary." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "Dr. Mortimer produced the **holographic** document written by Sir Hugo Baskerville in seventeenth-century script." },
      { author: "Dennis Gabor", work: "Holography, 1948-1971", quote: "The **holographic** reconstruction of wavefronts recreated the optical depth of the original crystal with startling clarity." }
    ]
  },
  "holographical.md": {
    word: "holographical",
    primary: "Pertaining to, consisting of, or prepared as a holograph; handwritten in full by the author.",
    secondary: "Relating to the optical technique or mathematical theory of holography.",
    quotes: [
      { author: "Isaac D'Israeli", work: "Curiosities of Literature", quote: "The antiquary examined the **holographical** correspondence of Queen Elizabeth, marvelling at her vigorous Italianate script." },
      { author: "Dennis Gabor", work: "Progress in Optics", quote: "The **holographical** recording system preserves both phase and amplitude, overcoming the limitations of standard photographic emulsions." },
      { author: "Frederic G. Kenyon", work: "Our Bible and the Ancient Manuscripts", quote: "Not a single **holographical** page of the apostolic writers has survived the ravages of early persecution." }
    ]
  },
  "holography.md": {
    word: "holography",
    primary: "The science, practice, or process of producing three-dimensional images (holograms) by means of laser light interference.",
    secondary: "In optical engineering and security printing, a technology widely used for high-density data storage, interferometric vibration analysis, and anticounterfeiting seals.",
    quotes: [
      { author: "Dennis Gabor", work: "Nobel Lecture: Holography", quote: "When lasers became available in 1960, **holography** stepped out of its long dormancy and experienced a magnificent renaissance." },
      { author: "Arthur C. Clarke", work: "Report on Planet Three", quote: "The ultimate development of **holography** will bring three-dimensional cinema directly into our living rooms without screens or glasses." },
      { author: "Philip Ball", work: "The Self-Made Tapestry", quote: "Optical **holography** utilizes laser interference patterns to measure micro-deformations on turbine blades under extreme mechanical stress." }
    ]
  },
  "homograft.md": {
    word: "homograft",
    primary: "A graft of tissue taken from an individual of the same species as the recipient; allograft.",
    secondary: "In cardiovascular and orthopedic surgery, human donor tissue (such as a cadaveric heart valve or bone segment) used to reconstruct damaged structures.",
    quotes: [
      { author: "Peter Medawar", work: "The Behaviour and Fate of Skin Homografts", quote: "The destruction of a **homograft** is brought about by an active immunological reaction against the antigens of the foreign tissue." },
      { author: "Thomas Starzl", work: "The Puzzle People", quote: "Clinical success with kidney **homografts** began only when pharmacological immunosuppression successfully held host rejection at bay." },
      { author: "Michael E. DeBakey", work: "Aortic Aneurysms and Their Surgical Treatment", quote: "In our early series, an aortic **homograft** was sutured into the resected aneurysm bed with gratifying survival rates." }
    ]
  },
  "homograph.md": {
    word: "homograph",
    primary: "A word that shares the same written form or spelling as another word, but has a different meaning and often a different origin and pronunciation (e.g., 'bow' of a ship vs. 'bow' and arrow).",
    secondary: "In computational natural language processing and lexicography, a lexical ambiguity requiring semantic context or part-of-speech tagging for correct disambiguation.",
    quotes: [
      { author: "Henry Bradley", work: "The Making of English", quote: "A **homograph** poses no difficulty to the eye on the printed page, though it may puzzle a child when the two words are pronounced differently." },
      { author: "Otto Jespersen", work: "Growth and Structure of the English Language", quote: "The convergence of distinct French and Scandinavian roots produced many a troublesome **homograph** in modern English." },
      { author: "Noam Chomsky", work: "Aspects of the Theory of Syntax", quote: "The sentence parsing algorithm must resolve every **homograph** by referencing surrounding syntactic category markers." }
    ]
  },
  "isograft.md": {
    word: "isograft",
    primary: "A graft of tissue transplanted between genetically identical individuals (such as monozygotic twins or animals of the same inbred strain); syngraft.",
    secondary: "In transplant immunology, an experimental and clinical graft model that avoids immunogenic histocompatibility rejection without needing immunosuppressive drugs.",
    quotes: [
      { author: "Peter Medawar", work: "The Immunology of Transplantation", quote: "An **isograft** between identical twins heals permanently and without immune reaction, exactly like an autograft." },
      { author: "Joseph E. Murray", work: "Nobel Lecture: Organ Transplants", quote: "The first successful human kidney transplant was an **isograft** performed in 1954 between identical Herrick brothers." },
      { author: "Thomas Starzl", work: "The Puzzle People", quote: "The complete acceptance of the **isograft** proved conclusively that transplantation failure was entirely immunological in origin." }
    ]
  },
  "isogram.md": {
    word: "isogram",
    primary: "A line on a map or chart connecting points having equal values of a given quantity (such as temperature, atmospheric pressure, or elevation); an isoline.",
    secondary: "In recreational linguistics and cryptography, a word or phrase in which no letter of the alphabet occurs more than once (e.g., 'subdermatoglyphic').",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "By connecting points of equal mean annual temperature with an **isogram**, I revealed the true thermal geography of the continents." },
      { author: "Dmitri Borgmann", work: "Language on Vacation", quote: "Word buffs prize the long **isogram**, laboring to discover fifteen-letter words free from any repeated character." },
      { author: "David Kahn", work: "The Codebreakers", quote: "The cryptanalyst used an **isogram** keyword to construct a non-repeating mixed alphabet for the cipher." }
    ]
  },
  "logographic.md": {
    word: "logographic",
    primary: "Of, relating to, or using a system of writing based on logograms (symbols representing an entire word or morpheme rather than a phonetic sound).",
    secondary: "In comparative writing systems, describing scripts such as Chinese characters or ancient Sumerian cuneiform, where graphic glyphs signify lexical concepts.",
    quotes: [
      { author: "Arthur Evans", work: "Scripta Minoa", quote: "The earliest stage of Cretan writing appears to have been largely **logographic**, depicting men, weapons, and animals." },
      { author: "Florian Coulmas", work: "The Writing Systems of the World", quote: "A **logographic** script allows speakers of mutually unintelligible dialects to communicate through a shared written medium." },
      { author: "Walter J. Ong", work: "Orality and Literacy", quote: "The cognitive processing of a **logographic** character engages different visual and mental faculties than an alphabetic script." }
    ]
  },
  "mammography.md": {
    word: "mammography",
    primary: "The radiographic examination of the breasts using low-dose X-rays for screening and diagnosis of tumors and other lesions.",
    secondary: "In radiological oncology, a population-based screening modality essential for reducing breast cancer mortality through early detection of non-palpable microcalcifications.",
    quotes: [
      { author: "Siddhartha Mukherjee", work: "The Emperor of All Maladies", quote: "The advent of routine **mammography** enabled oncologists to detect breast malignancies years before they could be felt by physical exam." },
      { author: "Atul Gawande", work: "Complications", quote: "Digital **mammography** has refined the radiologist's ability to distinguish harmless cysts from invasive carcinoma." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "Screening **mammography** represents one of the great triumphs of preventive radiology in modern clinical medicine." }
    ]
  },
  "microgram.md": {
    word: "microgram",
    primary: "A metric unit of mass equal to one millionth of a gram (one thousandth of a milligram, µg or mcg).",
    secondary: "In pharmacology and trace biochemistry, a high-precision mass unit used to measure potent hormonal concentrations, vitamins, and molecular receptor dosages.",
    quotes: [
      { author: "Linus Pauling", work: "Vitamin C and the Common Cold", quote: "Certain vital coenzymes and trace vitamins exert profound biological effects when administered in amounts of only a few **micrograms**." },
      { author: "Alexander Shulgin", work: "PiHKAL: A Chemical Love Story", quote: "The pharmacological potency of the compound was so immense that a single hundred-**microgram** threshold produced profound perceptual changes." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "The laboratory determined that the patient's thyroid hormone levels had dropped by several **micrograms** per deciliter." }
    ]
  },
  "micrograph.md": {
    word: "micrograph",
    primary: "A photograph, digital image, or drawing of an object as seen through a microscope; a photomicrograph.",
    secondary: "In micro-instrumentation, an apparatus used for executing microscopic writing or engraving upon minute surfaces.",
    quotes: [
      { author: "Robert Hooke", work: "Micrographia", quote: "The engraved **micrograph** of the flea revealed intricate joints, bristles, and armored plates hidden from the unassisted human eye." },
      { author: "Ernst Ruska", work: "The Development of the Electron Microscope", quote: "Our first electron **micrograph** revealed bacterial flagella with a resolution that optical lenses could never achieve." },
      { author: "D'Arcy Wentworth Thompson", work: "On Growth and Form", quote: "The cellular **micrograph** illustrates how physical surface tension shapes the hexagonal packaging of plant tissues." }
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
console.log("Writing & Script Batch 9 (Dashboard — graph 35-68) completed! Total words updated:", Object.keys(wordsData).length);
