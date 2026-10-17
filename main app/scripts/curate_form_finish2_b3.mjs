import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — pept\\polypeptide.md": {
    "primary": "A linear organic polymer consisting of a large number of amino-acid residues bonded together in a chain, forming part of (or the whole of) a protein molecule.",
    "secondary": "In molecular biochemistry, a polypeptide chain folds into specific secondary and tertiary conformations driven by hydrophobic interactions and hydrogen bonding.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Untersuchungen über Aminosäuren, Polypeptide und Proteine",
        "quote": "The synthesis of an artificial **polypeptide** demonstrated that protein structures are linked by amide bonds between amino acid residues."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Planar peptide units dictate how a **polypeptide** chain twists into an alpha-helix or aligns into a beta-sheet."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Ribosomal translation synthesizes a nascent **polypeptide** from its amino-terminal start to its carboxyl terminus."
      }
    ]
  },
  "Dashboard — pept\\tetrapeptide.md": {
    "primary": "A peptide composed of four amino acid residues joined by three peptide bonds.",
    "secondary": "In neurobiology and pharmacology, many endogenous signaling peptides (such as tuftsin and endomorphin-1) are biologically active tetrapeptide molecules.",
    "quotes": [
      {
        "author": "Vincent du Vigneaud",
        "work": "A Trail of Research",
        "quote": "Stepwise coupling yielded a crystalline **tetrapeptide** that served as an essential intermediate in hormone synthesis."
      },
      {
        "author": "Alan Fersht",
        "work": "Structure and Mechanism in Protein Science",
        "quote": "Binding of a synthetic **tetrapeptide** substrate within the active-site cleft allows precise mapping of subsite affinities."
      },
      {
        "author": "David L. Nelson",
        "work": "Lehninger Principles of Biochemistry",
        "quote": "The degradation of larger oligopeptides by carboxypeptidases often yields an intact **tetrapeptide** core."
      }
    ]
  },
  "Dashboard — pept\\tripeptide.md": {
    "primary": "A peptide composed of three amino acid residues joined by two peptide bonds.",
    "secondary": "In cellular biochemistry, glutathione (gamma-glutamylcysteinylglycine) is an ubiquitous tripeptide antioxidant that protects cells from oxidative damage.",
    "quotes": [
      {
        "author": "Frederick Gowland Hopkins",
        "work": "On an Autoxidisable Constituent of the Cell",
        "quote": "The isolation of glutathione revealed that a simple **tripeptide** could play a central role in intracellular oxidation-reduction equilibria."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Glutathione functions as an abundant cytoplasmic **tripeptide** that scavenges toxic reactive oxygen species."
      },
      {
        "author": "David L. Nelson",
        "work": "Lehninger Principles of Biochemistry",
        "quote": "Thyrotropin-releasing hormone is a modified hypothalamic **tripeptide** that stimulates pituitary thyrotropin secretion."
      }
    ]
  },
  "Dashboard — peri\\aperient.md": {
    "primary": "A medicine or substance that has a mild laxative effect; gently promoting the evacuation of the bowels.",
    "secondary": "In historical pharmacotherapy, mild saline aperient draughts were routinely prescribed to relieve intestinal stagnation without violent purging.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The administration of a mild saline **aperient** in the early morning promotes natural peristaltic evacuation."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "In bilious fevers, a gentle cooling **aperient** prevents toxic humors from corrupting the internal viscera."
      },
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "Mr. Woodhouse was forever consulting his apothecary regarding the propriety of taking a gentle **aperient**."
      }
    ]
  },
  "Dashboard — peri\\aperiodic.md": {
    "primary": "Not periodic; occurring at irregular intervals or lacking a regular repetitive cycle.",
    "secondary": "In physics and mathematics, describing dynamical systems, wave motions, or crystal structures (such as quasicrystals) that do not repeat at fixed intervals.",
    "quotes": [
      {
        "author": "Erwin Schrödinger",
        "work": "What Is Life?",
        "quote": "A gene may be conceived as an **aperiodic** crystal, whose non-repeating molecular architecture encodes hereditary complexity."
      },
      {
        "author": "Benoit Mandelbrot",
        "work": "The Fractal Geometry of Nature",
        "quote": "Chaotic attractors generate **aperiodic** orbits that never retrace their previous trajectories through phase space."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Random information sources generate **aperiodic** signal sequences whose unpredictability maximizes entropy."
      }
    ]
  },
  "Dashboard — peri\\aperitif.md": {
    "primary": "An alcoholic beverage consumed before a meal to stimulate the appetite.",
    "secondary": "In gastronomy and social custom, traditional dry aperitif drinks (such as vermouth, sherry, or bitters) utilize bitter aromatics to stimulate gastric secretion.",
    "quotes": [
      {
        "author": "Ernest Hemingway",
        "work": "The Sun Also Rises",
        "quote": "We sat at a table on the boulevard terrace and ordered an **aperitif** while watching the evening crowd stroll by."
      },
      {
        "author": "M. F. K. Fisher",
        "work": "The Art of Eating",
        "quote": "A light, bitter **aperitif** prepares the palate and awakens the stomach for the savory courses to follow."
      },
      {
        "author": "George Orwell",
        "work": "Down and Out in Paris and London",
        "quote": "The café was noisy with clerks drinking an **aperitif** before departing for their evening meal."
      }
    ]
  },
  "Dashboard — peri\\experience.md": {
    "primary": "Practical contact with and observation of facts or events; knowledge or skill acquired through direct involvement.",
    "secondary": "In epistemology and phenomenology, immediate conscious awareness and sensory engagement with the empirical world.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Whence has the mind all the materials of reason and knowledge? To this I answer, in one word, from **experience**."
      },
      {
        "author": "William James",
        "work": "Essays in Radical Empiricism",
        "quote": "Pure **experience** is the immediate flux of life which furnishes the raw material for our later reflection."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "There can be no doubt that all our knowledge begins with **experience**, though it does not all arise out of it."
      }
    ]
  },
  "Dashboard — peri\\experienced.md": {
    "primary": "Possessing skill, knowledge, or practical wisdom gained through long involvement in an activity or profession.",
    "secondary": "Having undergone, felt, or witnessed specific sensory, emotional, or existential events.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Nicomachean Ethics",
        "quote": "An **experienced** craftsman judges soundly because he perceives the intrinsic principles of his trade through practice."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Secret Sharer",
        "quote": "Only an **experienced** sailor could detect the faint shift in offshore breeze through the pitch-black night."
      },
      {
        "author": "William Shakespeare",
        "work": "All's Well That Ends Well",
        "quote": "He that has **experienced** both fortune's smile and frowning frown knows best how to endure adversity."
      }
    ]
  },
  "Dashboard — peri\\experient.md": {
    "primary": "Having or gaining experience; learning through empirical trial or direct observation.",
    "secondary": "In philosophy of mind, an experiencing subject; an entity capable of subjective awareness or qualia.",
    "quotes": [
      {
        "author": "Alfred North Whitehead",
        "work": "Process and Reality",
        "quote": "The actual occasion is an **experient** subject whose subjective aim directs the concrescence of feelings."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The active mind is not merely a passive recipient, but an **experient** agent constructing its perception."
      },
      {
        "author": "Charles Sanders Peirce",
        "work": "Collected Papers",
        "quote": "Every inquiry transforms the **experient** observer by confronting preconceived theories with recalcitrant facts."
      }
    ]
  },
  "Dashboard — peri\\experiential.md": {
    "primary": "Involving or based on experience and direct observation rather than theory or speculation.",
    "secondary": "In psychology and education, designating learning or therapy centered on personal emotional and sensory engagement.",
    "quotes": [
      {
        "author": "John Dewey",
        "work": "Experience and Education",
        "quote": "All genuine education comes about through personal engagement with **experiential** situations."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The stream of consciousness possesses an **experiential** richness that defies abstract mechanical reduction."
      },
      {
        "author": "Carl Rogers",
        "work": "On Becoming a Person",
        "quote": "Therapeutic change accelerates when the client accesses deep **experiential** awareness in the immediate present."
      }
    ]
  },
  "Dashboard — peri\\experiment.md": {
    "primary": "A scientific procedure undertaken to make a discovery, test a hypothesis, or demonstrate a known fact.",
    "secondary": "In scientific methodology, a controlled empirical manipulation designed to isolate causal relationships between variables.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "Novum Organum",
        "quote": "The true method of **experiment** first lights the candle, and then by means of the candle shows the way."
      },
      {
        "author": "Galileo Galilei",
        "work": "Dialogue Concerning the Two Chief World Systems",
        "quote": "A single rigorous **experiment** suffices to overturn thousands of scholastic conjectures."
      },
      {
        "author": "Richard Feynman",
        "work": "The Character of Physical Law",
        "quote": "If it disagrees with **experiment**, it is wrong; in that simple statement is the key to science."
      }
    ]
  },
  "Dashboard — peri\\experimentalism.md": {
    "primary": "The practice of or reliance on experimentation, especially as a philosophical method or artistic approach.",
    "secondary": "In pragmatist philosophy (notably John Dewey), the doctrine that ideas, beliefs, and values must be continuously tested and revised through empirical inquiry.",
    "quotes": [
      {
        "author": "John Dewey",
        "work": "The Quest for Certainty",
        "quote": "Philosophical **experimentalism** replaces static dogmas with a continuous method of inquiry and self-correction."
      },
      {
        "author": "William James",
        "work": "Pragmatism",
        "quote": "The spirit of radical **experimentalism** welcomes whatever hypothesis can validate itself in the crucible of practical consequences."
      },
      {
        "author": "T. S. Eliot",
        "work": "The Sacred Wood",
        "quote": "Artistic **experimentalism** is justified only when it serves to rejuvenate a decaying poetic tradition."
      }
    ]
  },
  "Dashboard — peri\\experimentally.md": {
    "primary": "By means of experiment; through empirical testing and practical observation.",
    "secondary": "In laboratory sciences, verified through empirical measurement under controlled investigative conditions.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "It is our duty to determine **experimentally** whether electromagnetic induction generates a true galvanic current."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "We verified **experimentally** that alpha particles are high-speed helium nuclei expelled from decaying atoms."
      },
      {
        "author": "Albert Einstein",
        "work": "On the Electrodynamics of Moving Bodies",
        "quote": "The constancy of the speed of light in vacuum has been confirmed **experimentally** across diverse reference frames."
      }
    ]
  },
  "Dashboard — peri\\experimentation.md": {
    "primary": "The process of performing experiments; systematic trial and observation to discover or verify facts.",
    "secondary": "In epistemology and scientific history, the organized manipulation of physical systems to reveal underlying natural laws.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Observation shows what is, while scientific **experimentation** reveals the conditions under which phenomena must be."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "Mendelian genetics owes its rapid advance to controlled **experimentation** with breeding stocks of Drosophila."
      },
      {
        "author": "Louis Pasteur",
        "work": "Germ Theory and Its Applications to Medicine and Surgery",
        "quote": "Rigorous laboratory **experimentation** disproved the phantom doctrine of spontaneous generation once and for all."
      }
    ]
  },
  "Dashboard — peri\\peri 2.md": {
    "primary": "In Persian mythology and folklore, a graceful, benevolent mythical being or fairy, originally regarded in Zoroastrian tradition as a fallen spirit doing penance.",
    "secondary": "In romantic literature and orientalist poetry, an ethereal, beautiful supernatural maiden of radiant charm.",
    "quotes": [
      {
        "author": "Thomas Moore",
        "work": "Lalla Rookh",
        "quote": "One morn a **Peri** at the gate of Eden stood, disconsolate; and as she listened to the Springs of Life within, she wept."
      },
      {
        "author": "Lord Byron",
        "work": "The Bride of Abydos",
        "quote": "Fair as the first that fell of winged **Peri** race, she seemed too pure for mortal clay."
      },
      {
        "author": "Edward FitzGerald",
        "work": "Rubáiyát of Omar Khayyám",
        "quote": "Beside the singing stream, a winged **peri** might pause to catch the fleeting melody of love."
      }
    ]
  },
  "Dashboard — peri\\peri.md": {
    "primary": "A prefix of Greek origin meaning 'about', 'around', 'enclosing', or 'near'.",
    "secondary": "In anatomical and astronomical terminology, forms terms denoting surrounding membranes (pericardium, periosteum) or orbital points of closest approach (perihelion, perigee).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek preposition **peri** signifies around, about, or concerning, forming numerous compound derivatives."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Deriving from Proto-Indo-European *per-, the combining form **peri** denotes spatial enclosure and circumferential proximity."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "In composition with verbs, the preposition **peri** often intensifies the verbal action or signifies circular motion."
      }
    ]
  },
  "Dashboard — peri\\periactin.md": {
    "primary": "A brand name for cyproheptadine, a first-generation antihistamine with antiserotonergic and appetite-stimulating properties.",
    "secondary": "In clinical pharmacology and pediatrics, periactin is used to treat allergic rhinitis, stimulate weight gain, and manage serotonin syndrome.",
    "quotes": [
      {
        "author": "Louis Sanford Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Cyproheptadine, marketed as **periactin**, antagonizes both histamine H1 and serotonin 5-HT2 receptors."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "In severe serotonin toxicity, the administration of **periactin** helps block central serotonergic hyperactivation."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Clinical trials noted marked weight gain in children receiving **periactin** due to hypothalamic appetite modulation."
      }
    ]
  },
  "Dashboard — peri\\perianal.md": {
    "primary": "Situated around or pertaining to the region surrounding the anus.",
    "secondary": "In colorectal surgery and proctology, the perianal skin and subcutaneous tissues are prone to fistulas, abscesses, and pruritus ani.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The external sphincter ani lies embedded within the dense subcutaneous fat of the **perianal** space."
      },
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "Intact **perianal** pinprick sensation confirms preservation of sacral cord segments S4 and S5 in spinal trauma."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Tuberculous ulceration may rarely manifest as painful induration within the **perianal** folds."
      }
    ]
  },
  "Dashboard — peri\\perianth.md": {
    "primary": "The outer envelope of a flower, consisting of the calyx (sepals) and corolla (petals) collectively.",
    "secondary": "In systematic botany, when sepals and petals are undifferentiated in appearance, the individual segments of the perianth are termed tepals.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The **perianth** constitutes the floral envelope, serving to protect the essential organs of reproduction during bud stage."
      },
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "In orchids, one segment of the **perianth** is profoundly modified into an attractive landing stage or labellum."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Vascular traces diverge from the floral receptacle to supply each segment of the biseriate **perianth**."
      }
    ]
  },
  "Dashboard — peri\\periapsis.md": {
    "primary": "The point in an orbit where an orbiting body is closest to the central body around which it revolves.",
    "secondary": "In celestial mechanics and astrodynamics, the distance to periapsis ($r_p$) is related to semimajor axis ($a$) and eccentricity ($e$) by $r_p = a(1 - e)$.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Astronomia Nova",
        "quote": "The planet attains its maximum orbital velocity at **periapsis**, sweeping equal areas in equal times."
      },
      {
        "author": "Howard D. Curtis",
        "work": "Orbital Mechanics for Engineering Students",
        "quote": "Engineers plan velocity impulses at **periapsis** to maximize kinetic energy gains via the Oberth effect."
      },
      {
        "author": "Carl Sagan",
        "work": "Pale Blue Dot",
        "quote": "The robotic probe dipped low through **periapsis**, transmitting close-up radar scans of the planetary surface."
      }
    ]
  },
  "Dashboard — peri\\periarteritis.md": {
    "primary": "Inflammation of the outer coat (tunica adventitia) of an artery and of the tissues immediately surrounding it.",
    "secondary": "In rheumatology and vascular pathology, periarteritis nodosa is a systemic necrotizing vasculitis affecting medium and small muscular arteries.",
    "quotes": [
      {
        "author": "Adolf Kussmaul",
        "work": "Periarteritis Nodosa",
        "quote": "We observed aneurysmal beadings along the mesenteric arteries, characteristic of systemic **periarteritis** nodosa."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Segmental transmural necrosis in **periarteritis** leads to thrombosis, ischemia, and multiple visceral infarctions."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "The histologic hallmark of acute **periarteritis** is intense neutrophilic infiltration with fibrinoid necrosis."
      }
    ]
  },
  "Dashboard — peri\\pericallis.md": {
    "primary": "A genus of flowering plants in the family Asteraceae, native to the Canary Islands and Madeira, including florists' cineraria.",
    "secondary": "In horticulture and floriculture, hybrid cultivars of *Pericallis hybrida* are widely cultivated in greenhouses for their vibrant daisy-like inflorescences.",
    "quotes": [
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "The popular florist cinerarias, classified under the genus **Pericallis**, present magnificent domes of purple, blue, and crimson blossoms."
      },
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Island endemics of the Atlantic archipelago yielded striking composites allied to **Pericallis**."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of Botany",
        "quote": "Greenhouse selections of **Pericallis** exhibit remarkable ray-floret variation under controlled illumination."
      }
    ]
  },
  "Dashboard — peri\\pericardiac.md": {
    "primary": "Relating to or situated near the pericardium; pericardial.",
    "secondary": "In anatomical nomenclature, designating vessels, nerves, or ligaments distributed to the pericardial sac (such as pericardiacophrenic vessels).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **pericardiac** branches of the internal thoracic artery descend alongside the phrenic nerve to supply the fibrous sac."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Embryonic fusion of lateral mesodermal folds encloses the primitive **pericardiac** cavity."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A coarse friction rub heard over the lower sternum confirms **pericardiac** involvement in acute rheumatic fever."
      }
    ]
  },
  "Dashboard — peri\\pericardial.md": {
    "primary": "Of, relating to, or situated near the pericardium (the fibroserous sac surrounding the heart).",
    "secondary": "In cardiology, pericardial effusion refers to an abnormal accumulation of fluid within the pericardial cavity, risking cardiac tamponade.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "A rapid increase in **pericardial** pressure compromises ventricular diastolic filling, precipitating tamponade."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Auscultation over the precordium reveals a pathognomonic to-and-fro **pericardial** friction rub."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Echocardiography reliably identifies even small amounts of fluid in the posterior **pericardial** space."
      }
    ]
  },
  "Dashboard — peri\\pericarditis.md": {
    "primary": "Inflammation of the pericardium, the fibrous sac enclosing the heart.",
    "secondary": "In cardiology, acute pericarditis typically presents with sharp pleuritic chest pain relieved by sitting forward, accompanied by widespread ST-segment elevation on electrocardiogram.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Fibrinous **pericarditis** imparts a rough, bread-and-butter appearance to the cardiac serosa upon autopsy."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Pleuritic chest pain in acute **pericarditis** characteristically improves when the patient leans forward."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Widespread concave-upward ST elevation across multiple leads is the classic electrocardiographic hallmark of acute **pericarditis**."
      }
    ]
  },
  "Dashboard — peri\\pericardium.md": {
    "primary": "The conical fibroserous sac enclosing the heart and the roots of the great cardiac vessels.",
    "secondary": "In cardiovascular anatomy, the pericardium consists of an outer fibrous layer and an inner serous layer whose parietal and visceral lamina lubricate cardiac contraction.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The fibrous **pericardium** is firmly attached below to the central tendon of the diaphragm."
      },
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "The heart pulses freely within the moist enclosure of the **pericardium**, protected from friction against neighboring viscera."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Constriction of a calcified **pericardium** severely limits end-diastolic cardiac filling."
      }
    ]
  },
  "Dashboard — peri\\pericarp.md": {
    "primary": "The wall of a ripened plant ovary (fruit), typically consisting of three distinct layers: epicarp, mesocarp, and endocarp.",
    "secondary": "In carpology and plant morphology, the pericarp can become fleshy and succulent (as in berries and drupes) or dry and dehiscent (as in capsules and legumes).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "In a peach, the outermost skin is the exocarp, the luscious pulp the mesocarp, and the stony pit the endocarp of the **pericarp**."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Parenchyma cells within the developing **pericarp** undergo substantial hypertrophy during fruit enlargement."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Birds feed on fleshy fruits, passing the hard seeds encased inside unharmed by digestion of the **pericarp**."
      }
    ]
  },
  "Dashboard — peri\\pericementoclasia.md": {
    "primary": "The progressive destruction and resorption of the periodontal ligament (pericementum) and alveolar bone surrounding a tooth.",
    "secondary": "In historical dental pathology, pericementoclasia was an earlier clinical term used to describe severe periodontitis and alveolar bone loss leading to tooth exfoliation.",
    "quotes": [
      {
        "author": "G. V. Black",
        "work": "Special Dental Pathology",
        "quote": "Chronic suppurative **pericementoclasia** gradually detaches the periodontal membrane from the cementum of the root."
      },
      {
        "author": "Martin Dewey",
        "work": "Practical Orthodontia",
        "quote": "Excessive mechanical force in moving teeth may initiate traumatic **pericementoclasia** and root resorption."
      },
      {
        "author": "Calvin S. Case",
        "work": "Dental Orthopedia",
        "quote": "Clinicians must recognize early pocket formation before irreversible **pericementoclasia** loosens the dentition."
      }
    ]
  },
  "Dashboard — peri\\periclase.md": {
    "primary": "A cubic magnesium oxide mineral (MgO) formed by high-temperature contact metamorphism of impure dolomitic limestones.",
    "secondary": "In petrology and high-pressure mineral physics, periclase readily hydrates to brucite ($Mg(OH)_2$) and forms ferropericlase, a major constituent of the Earth's lower mantle.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The rare mineral **periclase** occurs in dark octahedrons embedded in metamorphic limestone ejected from Mount Somma."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Under contact metamorphism, thermal decarbonation of dolomite yields calcite and crystalline **periclase**."
      },
      {
        "author": "Norman L. Bowen",
        "work": "Progressive Metamorphism of Siliceous Limestone and Dolomite",
        "quote": "The appearance of **periclase** marks the highest metamorphic grade in carbonate contact aureoles."
      }
    ]
  },
  "Dashboard — peri\\Pericles.md": {
    "primary": "A prominent and influential Greek statesman, orator, and general of Athens during its Golden Age in the fifth century BCE.",
    "secondary": "In classical history, Pericles fostered the Athenian empire, spearheaded the construction of the Parthenon on the Acropolis, and championed direct democratic civic participation.",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "In what was nominally a democracy, power was really in the hands of the first citizen, **Pericles**."
      },
      {
        "author": "Plutarch",
        "work": "Parallel Lives: Life of Pericles",
        "quote": "The noble monuments raised under **Pericles** still impress the traveler with a sense of living eternity."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "The funeral oration of **Pericles** remains the supreme literary testament to Athenian democratic ideals."
      }
    ]
  },
  "Dashboard — peri\\pericope.md": {
    "primary": "An extract or selected passage from a text; especially a selection from the Bible appointed to be read during a church service.",
    "secondary": "In liturgical studies and form criticism, a pericope is an independent literary unit or scriptural excerpt analyzed within its historical and liturgical setting.",
    "quotes": [
      {
        "author": "Rudolf Bultmann",
        "work": "The History of the Synoptic Tradition",
        "quote": "Each gospel **pericope** circulated as an independent oral unit before being woven into a continuous narrative framework."
      },
      {
        "author": "C. H. Dodd",
        "work": "The Parables of the Kingdom",
        "quote": "The context of a single **pericope** often reveals the specific pastoral needs of the early Christian community."
      },
      {
        "author": "John Henry Newman",
        "work": "Parochial and Plain Sermons",
        "quote": "The Sunday **pericope** from the Gospel of Saint John directs our devotion toward Christ’s divine nature."
      }
    ]
  },
  "Dashboard — peri\\peridium.md": {
    "primary": "The outer protective wall, skin, or envelope of the fruiting body of certain fungi, such as puffballs, earthstars, and truffles.",
    "secondary": "In mycology, the peridium may be single- or multi-layered (exoperidium and endoperidium), rupturing by an apical pore or dehiscing stellately to release spores.",
    "quotes": [
      {
        "author": "Elias Magnus Fries",
        "work": "Systema Mycologicum",
        "quote": "In puffballs, mature basidiospores remain sealed within the membranous **peridium** until mechanical shock releases them."
      },
      {
        "author": "Miles Joseph Berkeley",
        "work": "Outlines of British Fungology",
        "quote": "The outer layer of the **peridium** in Geastrum splits into star-like rays that recurve upon the soil."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Raindrop impaction on the flexible **peridium** generates puffs of air that eject spores through the ostiole."
      }
    ]
  },
  "Dashboard — peri\\perigee.md": {
    "primary": "The point in the orbit of the Moon or an artificial satellite where it is nearest to the center of the Earth.",
    "secondary": "In orbital mechanics and astronomy, a celestial body moves with maximum angular velocity and experiences greatest tidal gravitational pull at perigee.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Epitome of Copernican Astronomy",
        "quote": "When the Moon reaches **perigee**, its apparent diameter appears appreciably magnified to the terrestrial observer."
      },
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "Gravitational perturbation from the Sun causes a continuous forward progression of the lunar **perigee**."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Swinging around the Earth at **perigee**, the spacecraft accelerated into its interplanetary transfer orbit."
      }
    ]
  },
  "Dashboard — peri\\perihelion.md": {
    "primary": "The point in the orbit of a planet, asteroid, or comet where it is closest to the Sun.",
    "secondary": "In celestial mechanics and general relativity, the anomalous precession of Mercury’s perihelion provided the first empirical confirmation of Einstein’s theory of gravitation.",
    "quotes": [
      {
        "author": "Albert Einstein",
        "work": "Explanation of the Perihelion Motion of Mercury",
        "quote": "General relativity accounts quantitatively for the unexplained secular advance of forty-three arcseconds in Mercury’s **perihelion**."
      },
      {
        "author": "Johannes Kepler",
        "work": "Astronomia Nova",
        "quote": "A planet achieves its greatest orbital velocity when passing through **perihelion**."
      },
      {
        "author": "Pierre-Simon Laplace",
        "work": "Celestial Mechanics",
        "quote": "Planetary mutual perturbations cause slow secular oscillations in the longitude of **perihelion**."
      }
    ]
  },
  "Dashboard — peri\\peril.md": {
    "primary": "Serious and immediate danger; exposure to the risk of death, injury, loss, or destruction.",
    "secondary": "In marine insurance and maritime law, perils of the sea denote unavoidable accidents, storms, and hazards encountered during ocean voyages.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "Neither a borrower nor a lender be; for loan oft loses both itself and friend, and borrowing dulls the edge of husbandry, exposing honor to grave **peril**."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "He navigated upstream with a profound sense of looming **peril** hidden behind the impenetrable curtain of jungle."
      },
      {
        "author": "John Locke",
        "work": "Second Treatise of Government",
        "quote": "Men enter into civil society to preserve their lives, liberties, and estates from the constant **peril** of lawlessness."
      }
    ]
  },
  "Dashboard — peri\\perilla.md": {
    "primary": "An annual herbaceous plant (Perilla frutescens) of the mint family (Lamiaceae), widely cultivated in East Asia for its culinary leaves and edible seed oil.",
    "secondary": "In organic chemistry and ethnobotany, perilla seed oil is exceptionally rich in alpha-linolenic acid, and perillaldehyde contributes to the distinct aroma of shiso.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The aromatic herb **perilla** belongs to the family of labiates, flourishing in the warm gardens of eastern Asia."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Manual of Cultivated Plants",
        "quote": "The bronzed foliage of ornamental **perilla** serves as a popular bedding plant in temperate gardens."
      },
      {
        "author": "Harold McGee",
        "work": "On Food and Cooking",
        "quote": "In Japanese cuisine, the green leaves of **perilla**, known as shiso, impart an herbaceous, mint-like fragrance to raw seafood."
      }
    ]
  },
  "Dashboard — peri\\perilous.md": {
    "primary": "Full of danger or risk; hazardous; fraught with peril.",
    "secondary": "In philosophical and literary narrative, describing arduous endeavors or existential thresholds fraught with catastrophic jeopardy.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Julius Caesar",
        "quote": "Now could I, Casca, name to thee a man most like this dreadful night, that thunders, lightens, opens graves, and roars in **perilous** defiance."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Lowering whaleboats into tempestuous waters is a desperate and **perilous** enterprise."
      },
      {
        "author": "John Bunyan",
        "work": "The Pilgrim's Progress",
        "quote": "Christian journeyed through the Slough of Despond along a narrow and **perilous** pathway."
      }
    ]
  },
  "Dashboard — peri\\perilously.md": {
    "primary": "In a manner fraught with danger, risk, or severe hazard.",
    "secondary": "To a degree that verges dangerously close to disaster, failure, or death.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "The crippled steamer leaned **perilously** to starboard as mountainous seas crashed over the rusted deck."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "He stepped **perilously** near the edge of the marshes, where the quicksand threatened to swallow him whole."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "We crept **perilously** along the sheer granite precipice, listening for the hound's distant baying."
      }
    ]
  },
  "Dashboard — peri\\perilousness.md": {
    "primary": "The state, condition, or quality of being perilous; extreme hazard or dangerousness.",
    "secondary": "In existential philosophy and literature, the acknowledged severity of mortal vulnerability in heroic or pioneering enterprises.",
    "quotes": [
      {
        "author": "Edmund Burke",
        "work": "A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful",
        "quote": "The sublime arises when terror and the **perilousness** of vast objects are contemplated from a position of safety."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The sheer **perilousness** of the national crisis compelled the Committee to adopt terror as an instrument of state."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "Men overestimate the **perilousness** of simple living because they remain enslaved to imaginary luxuries."
      }
    ]
  },
  "Dashboard — peri\\perilune.md": {
    "primary": "The point in a lunar orbit that is closest to the surface or center of the Moon.",
    "secondary": "In orbital astrodynamics, entering low perilune allows spacecraft to perform high-resolution radar altimetry and terrain mapping.",
    "quotes": [
      {
        "author": "Howard D. Curtis",
        "work": "Orbital Mechanics for Engineering Students",
        "quote": "A retro-rocket firing at **perilune** efficiently inserts the lunar orbiter into a circular circumlunar trajectory."
      },
      {
        "author": "Arthur C. Clarke",
        "work": "The Promise of Space",
        "quote": "At **perilune**, the Apollo spacecraft skimmed merely sixty miles above the craggy lunar highlands."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Automated probes decelerated near **perilune** to land softly upon the basaltic plains of the Ocean of Storms."
      }
    ]
  },
  "Dashboard — peri\\perilymph.md": {
    "primary": "The extracellular fluid located between the membranous labyrinth and the bony labyrinth of the inner ear.",
    "secondary": "In auditory physiology, perilymph resembles cerebrospinal fluid in having high sodium ($Na^+$) and low potassium ($K^+$) concentrations, transmitting sound vibrations to the scala tympani and scala vestibuli.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "On the Sensations of Tone",
        "quote": "Stapedial vibrations transmit wave pulses through the fluid **perilymph** of the cochlear canals to stimulate the basilar membrane."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The scala vestibuli and scala tympani are filled with **perilymph**, whose composition closely mirrors extracellular fluid."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "A thin layer of **perilymph** isolates the fragile membranous semicircular canals from the surrounding petrous bone."
      }
    ]
  },
  "Dashboard — peri\\perimeter.md": {
    "primary": "The continuous line forming the boundary of a closed geometric figure; the total length of such a boundary.",
    "secondary": "In military tactics, security, and urban planning, an outer boundary or fortified defensive perimeter protecting an installation.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "Among plane figures possessing equal **perimeter**, the circle encloses the greatest area."
      },
      {
        "author": "Isaac Newton",
        "work": "The Mathematical Principles of Natural Philosophy",
        "quote": "Inscribing regular polygons of increasing sides allows approximation of the circular **perimeter**."
      },
      {
        "author": "Julian Lowell Coolidge",
        "work": "A Treatise on the Circle and the Sphere",
        "quote": "The isoperimetric theorem establishes that the boundary **perimeter** of an ellipse exceeds that of a circle of equal area."
      }
    ]
  },
  "Dashboard — peri\\perimysium.md": {
    "primary": "The sheath of connective tissue grouping individual muscle fibers into bundles or fascicles within a skeletal muscle.",
    "secondary": "In histology and muscular biomechanics, the perimysium contains intramuscular blood vessels and nerve branches, transmitting passive lateral tensile strain.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Septa of fibrous connective tissue branch inward from the epimysium to form the **perimysium**, enclosing muscle fascicles."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Capillary networks penetrating through the **perimysium** provide oxygen to individual myocytes during sustained contraction."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Collagen fibrils in the **perimysium** ensure that force generated by sarcomeres is transmitted efficiently to the tendon."
      }
    ]
  },
  "Dashboard — peri\\perinasal.md": {
    "primary": "Situated around or near the nasal cavity or external nose.",
    "secondary": "In rhinology and maxillofacial surgery, perinasal tissues and paranasal sinuses are evaluated for inflammatory spreading and trauma.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Branches of the facial artery distribute freely across the **perinasal** musculature and alar cartilages."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Erysipelas frequently begins in the **perinasal** region, spreading rapidly across both cheeks in a butterfly distribution."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Tenderness upon palpation of the **perinasal** bony margins indicates acute maxillary or frontal sinusitis."
      }
    ]
  },
  "Dashboard — peri\\perinatal.md": {
    "primary": "Relating to the period immediately before and after birth, typically from around the 28th week of gestation to the first month after birth.",
    "secondary": "In obstetrics and neonatology, perinatal mortality rates serve as a primary indicator of national maternal-fetal healthcare quality.",
    "quotes": [
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Screening for maternal streptococcal colonization significantly reduces the incidence of severe **perinatal** sepsis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Birth asphyxia during the **perinatal** interval remains a primary cause of spastic diplegia in infants."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Prompt transition from fetal to **perinatal** circulation requires timely closure of the ductus arteriosus."
      }
    ]
  },
  "Dashboard — peri\\perinatologist.md": {
    "primary": "A specialist in maternal-fetal medicine who provides care for high-risk pregnancies, fetuses, and newborns around the time of birth.",
    "secondary": "A subspecialty obstetrician managing complex maternal comorbidities, fetal congenital anomalies, and premature labor.",
    "quotes": [
      {
        "author": "John A. Rock",
        "work": "Te Linde's Operative Gynecology",
        "quote": "The consulting **perinatologist** employs targeted ultrasonography to monitor intrauterine growth restriction."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Patients with severe preeclampsia benefit from immediate co-management by an experienced **perinatologist**."
      },
      {
        "author": "David L. Rimoin",
        "work": "Principles and Practice of Medical Genetics",
        "quote": "Genetic counseling coordinated with a **perinatologist** guides clinical decisions in suspected chromosomal aneuploidies."
      }
    ]
  },
  "Dashboard — peri\\perinatology.md": {
    "primary": "The subspecialty of obstetrics and pediatrics concerned with the care of the mother and fetus during pregnancy, labor, and the early neonatal period.",
    "secondary": "In maternal-fetal medicine, perinatology integrates prenatal genetic screening, fetal imaging, and critical neonatal care.",
    "quotes": [
      {
        "author": "John A. Rock",
        "work": "Te Linde's Operative Gynecology",
        "quote": "Advances in **perinatology** have significantly pushed back the threshold of fetal viability."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Modern **perinatology** utilizes Doppler velocimetry of the umbilical artery to detect early placental insufficiency."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Fetal echocardiography has transformed **perinatology**, permitting intrauterine intervention for critical cardiac malformations."
      }
    ]
  },
  "Dashboard — peri\\perineal.md": {
    "primary": "Of, relating to, or situated in the perineum (the region between the pubic symphysis and the coccyx).",
    "secondary": "In surgical anatomy, the perineal membrane and muscles support the pelvic floor and contain the urogenital triangle.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The superficial **perineal** fascia is attached laterally to the ischiopubic rami, bounding the superficial perineal pouch."
      },
      {
        "author": "Howard A. Kelly",
        "work": "Operative Gynecology",
        "quote": "Careful reconstruction of the **perineal** body restores essential pelvic diaphragm support after obstetric injury."
      },
      {
        "author": "John Hunter",
        "work": "Treatise on the Venereal Disease",
        "quote": "Stricture of the urethra often leads to urinary extravasation into the loose **perineal** tissues."
      }
    ]
  },
  "Dashboard — peri\\perineotomy.md": {
    "primary": "A surgical incision into the perineum; specifically, an episiotomy or incision to relieve urethral obstruction.",
    "secondary": "In operative urology and obstetrics, perineotomy provides surgical access to the bulbous urethra or enlarges the vaginal introitus during delivery.",
    "quotes": [
      {
        "author": "Howard A. Kelly",
        "work": "Operative Gynecology",
        "quote": "A planned lateral **perineotomy** prevents uncontrolled ragged tears through the anal sphincter during delivery."
      },
      {
        "author": "John Hunter",
        "work": "Treatise on the Venereal Disease",
        "quote": "In impassable urethral strictures, external **perineotomy** was historically performed to drain extravasated urine."
      },
      {
        "author": "J. Marion Sims",
        "work": "Clinical Notes on Uterine Surgery",
        "quote": "Prompt primary suture of a **perineotomy** incision prevents subsequent pelvic floor relaxation."
      }
    ]
  },
  "Dashboard — peri\\perineum.md": {
    "primary": "The area of the body between the anus and the scrotum or vulva; the anatomical pelvic outlet bounded by the pelvic bones.",
    "secondary": "In pelvic anatomy, the perineum is divided by an imaginary transverse line into an anterior urogenital triangle and a posterior anal triangle.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **perineum** corresponds to the outlet of the pelvis, bounded anteriorly by the pubic arch and posteriorly by the coccyx."
      },
      {
        "author": "Howard A. Kelly",
        "work": "Operative Gynecology",
        "quote": "Integrity of the central tendon of the **perineum** is essential for maintaining normal rectal and vaginal axis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Subcutaneous hematomas of the **perineum** indicate severe pelvic ring disruption following crush injuries."
      }
    ]
  },
  "Dashboard — peri\\perineurium.md": {
    "primary": "The protective sheath of connective tissue that encloses each bundle or fascicle of nerve fibers within a peripheral nerve.",
    "secondary": "In neurohistology, the perineurium consists of concentric layers of flattened perineurial cells linked by tight junctions, forming the blood-nerve barrier.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Concentric lamellae of the **perineurium** isolate each nerve bundle, maintaining a specialized internal physiological milieu."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **perineurium** is a smooth, transparent membrane that forms an impermeable tubular sleeve around each fascicle."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Tight junctions between perineurial cells in the **perineurium** establish an effective blood-nerve barrier against macromolecules."
      }
    ]
  },
  "Dashboard — peri\\period.md": {
    "primary": "A length or portion of time characterized by specific events, conditions, or features.",
    "secondary": "In mathematics and physics, the interval of time or space required for a cyclical wave or periodic function to complete one full cycle.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Principia",
        "quote": "The orbital **period** of each planet squared is proportional to the cube of its mean distance from the Sun."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The **period** of the Antonines is generally regarded as the happiest epoch in the history of mankind."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "During this vast geological **period**, natural selection unceasingly modified existing organic forms."
      }
    ]
  },
  "Dashboard — peri\\periodically.md": {
    "primary": "At regular intervals of time; recurring cyclically.",
    "secondary": "In physical sciences and economics, describing events or signals that repeat according to a predictable temporal period.",
    "quotes": [
      {
        "author": "Dmitri Mendeleev",
        "work": "The Principles of Chemistry",
        "quote": "The elements, if arranged according to their atomic weights, exhibit an apparent **periodically** recurring sequence of properties."
      },
      {
        "author": "Johannes Kepler",
        "work": "Harmonices Mundi",
        "quote": "The celestial spheres swing **periodically** between aphelion and perihelion according to harmonious ratios."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "Market prices fluctuate **periodically** about the natural price under the oscillating influence of supply and demand."
      }
    ]
  },
  "Dashboard — peri\\periodicity.md": {
    "primary": "The quality, state, or fact of being periodic, or recurring at regular intervals.",
    "secondary": "In chemistry and quantum mechanics, chemical periodicity refers to the recurrent trends in element properties across groups and periods in the periodic table.",
    "quotes": [
      {
        "author": "Dmitri Mendeleev",
        "work": "The Periodic Law of the Chemical Elements",
        "quote": "The law of **periodicity** reveals that the physical and chemical behavior of elements is a function of atomic weight."
      },
      {
        "author": "Niels Bohr",
        "work": "The Theory of Spectra and Atomic Constitution",
        "quote": "Electronic shell filling explains the remarkable **periodicity** observed across the rows of the chemical table."
      },
      {
        "author": "Erwin Schrödinger",
        "work": "What Is Life?",
        "quote": "Unlike ordinary matter which exhibits regular spatial **periodicity**, living molecules display aperiodic structure."
      }
    ]
  },
  "Dashboard — peri\\periodontal.md": {
    "primary": "Relating to or affecting the tissues and structures surrounding and supporting the teeth.",
    "secondary": "In dentistry and periodontology, the periodontal ligament attaches the cementum of the tooth root to the alveolar bone.",
    "quotes": [
      {
        "author": "G. V. Black",
        "work": "Special Dental Pathology",
        "quote": "The **periodontal** membrane contains collagen fibers arranged to resist masticatory impact and cushion the root."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Orthodontic movement depends upon continuous remodeling within the compressed and stretched zones of the **periodontal** ligament."
      },
      {
        "author": "Fermín A. Carranza",
        "work": "Clinical Periodontology",
        "quote": "Destruction of **periodontal** attachment creates deep pathological pockets that harbor anaerobic microbiota."
      }
    ]
  },
  "Dashboard — peri\\periodontia.md": {
    "primary": "The tissues surrounding and supporting the teeth, including the gingiva, periodontal ligament, cementum, and alveolar bone; or an alternative term for periodontics.",
    "secondary": "In dental nomenclature, the anatomical and functional complex that secures teeth within the jaws.",
    "quotes": [
      {
        "author": "G. V. Black",
        "work": "Special Dental Pathology",
        "quote": "Diseases of the **periodontia** begin at the gingival margin and progressively destroy the deep investing tissues."
      },
      {
        "author": "Calvin S. Case",
        "work": "Dental Orthopedia",
        "quote": "The physiological resilience of the **periodontia** permits mechanical repositioning without devitalizing the pulp."
      },
      {
        "author": "Fermín A. Carranza",
        "work": "Carranza's Clinical Periodontology",
        "quote": "Chronic inflammatory breakdown of the **periodontia** results in progressive mobility and tooth migration."
      }
    ]
  },
  "Dashboard — peri\\periodontic.md": {
    "primary": "Of, relating to, or involving periodontics; periodontal.",
    "secondary": "Pertaining to clinical procedures and instruments used to treat diseases of the dental supporting tissues.",
    "quotes": [
      {
        "author": "Fermín A. Carranza",
        "work": "Clinical Periodontology",
        "quote": "Ultrasonic instrumentation has become standard in non-surgical **periodontic** debridement."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Orthodontic tooth alignment should be deferred until active **periodontic** inflammation is fully resolved."
      },
      {
        "author": "G. V. Black",
        "work": "Operative Dentistry",
        "quote": "Careful scaling below the gingival crest is the foundational **periodontic** therapy to preserve the dentition."
      }
    ]
  },
  "Dashboard — peri\\periodontics.md": {
    "primary": "The branch of dentistry concerned with the structures surrounding and supporting the teeth, and the diseases and conditions affecting them.",
    "secondary": "In clinical dental surgery, a specialty focusing on gingival grafting, regenerative bone surgery, and dental implant site preparation.",
    "quotes": [
      {
        "author": "Fermín A. Carranza",
        "work": "Clinical Periodontology",
        "quote": "Modern **periodontics** integrates microbiology, host immune modulation, and microsurgical tissue regeneration."
      },
      {
        "author": "G. V. Black",
        "work": "Special Dental Pathology",
        "quote": "Early investigators laid the groundwork for **periodontics** by demonstrating the microbial etiology of calculus formation."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Interdisciplinary collaboration between orthodontics and **periodontics** is essential for adult patients with reduced bone support."
      }
    ]
  },
  "Dashboard — peri\\periodontist.md": {
    "primary": "A dental specialist who prevents, diagnoses, and treats periodontal disease and places dental implants.",
    "secondary": "A clinician possessing advanced training in soft-tissue grafting, bone regeneration, and managing severe periodontitis.",
    "quotes": [
      {
        "author": "Fermín A. Carranza",
        "work": "Clinical Periodontology",
        "quote": "The consulting **periodontist** performs pocket reduction surgery to facilitate long-term plaque control."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Surgical exposure of impacted canines requires delicate handling by a skilled **periodontist** to preserve attached gingiva."
      },
      {
        "author": "G. V. Black",
        "work": "Special Dental Pathology",
        "quote": "The dedicated **periodontist** educates the patient that daily oral hygiene is the only defense against recurrent infection."
      }
    ]
  },
  "Dashboard — peri\\periodontitis.md": {
    "primary": "Inflammation of the tissue around the teeth, often causing shrinkage of the gums and loosening of the teeth.",
    "secondary": "In clinical dentistry, chronic periodontitis is an infectious disease of polymicrobial etiology resulting in irreversible loss of periodontal ligament and alveolar bone.",
    "quotes": [
      {
        "author": "Fermín A. Carranza",
        "work": "Clinical Periodontology",
        "quote": "Left untreated, chronic **periodontitis** destroys the alveolar bone crest, leading inevitably to tooth mobility and loss."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe oral sepsis secondary to advanced **periodontitis** may serve as a nidus for infective endocarditis."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Systemic epidemiological studies associate severe **periodontitis** with poor glycemic control in type 2 diabetes mellitus."
      }
    ]
  },
  "Dashboard — peri\\periophthalmus.md": {
    "primary": "A genus of amphibious gobies commonly known as mudskippers, capable of moving, breathing, and feeding on land.",
    "secondary": "In evolutionary ichthyology, species of *Periophthalmus* possess muscular pectoral fins adapted for terrestrial locomotion and elevated, protruding periscopic eyes.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Curious mud-loving gobies of the genus **Periophthalmus** hopped along the mangrove mud-flats with the agility of frogs."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The amphibious habits of **Periophthalmus** illustrate how ancestral vertebrates could have ventured from water onto land."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Specimens of **Periophthalmus** use their vascular opercular chambers to breathe atmospheric air during low tide."
      }
    ]
  },
  "Dashboard — peri\\periosteum.md": {
    "primary": "A dense layer of vascular connective tissue enveloping the bones except at the surfaces of the joints.",
    "secondary": "In skeletal histology and orthopedic surgery, the periosteum consists of an outer fibrous layer and an inner cambium layer containing osteoprogenitor cells essential for bone growth and repair.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **periosteum** adheres firmly to the bone by Sharpey's fibers and conveys nutrient blood vessels through Volkmann's canals."
      },
      {
        "author": "John Hunter",
        "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds",
        "quote": "Preserving the **periosteum** intact during surgical exploration is vital for securing rapid osteogenesis in fractured limbs."
      },
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "Stripping the **periosteum** extensively devascularizes the cortical fragment, markedly delaying fracture union."
      }
    ]
  },
  "Dashboard — peri\\peripheral.md": {
    "primary": "Of, relating to, or situated on the edge, periphery, or margin of something; secondary or minor in importance.",
    "secondary": "In human neuroanatomy, the peripheral nervous system (PNS) comprises the cranial and spinal nerves connecting the central nervous system to the limbs and organs.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Unlike central axons, severed **peripheral** nerve fibers possess a remarkable capacity to regenerate within Schwann cell conduits."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Attention focuses upon the vivid focal object while relegating background sensations to a dim **peripheral** fringe."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Routing messages through **peripheral** communication channels minimizes central network bottlenecking."
      }
    ]
  },
  "Dashboard — peri\\peripherally.md": {
    "primary": "In a peripheral manner; on or near the edge, boundary, or periphery; of secondary or non-essential importance.",
    "secondary": "In pharmacology and physiology, acting on peripheral tissues or nerves outside the blood-brain barrier without central nervous system involvement.",
    "quotes": [
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Certain opioid antagonists act only **peripherally**, reversing gut hypomotility without blunting central analgesia."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Sympathetic vasoconstriction acts **peripherally** in arteriolar beds to elevate total systemic vascular resistance."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Objects perceived **peripherally** in the visual field lack chromatic detail yet remain exquisitely sensitive to motion."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 2 Batch 3.`);
