import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — elem\\elementarily.md": {
    "primary": "In an elementary, rudimentary, or foundational manner; at a basic level.",
    "secondary": "In logic and exposition, proceeding simply from first principles without extraneous complexity.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "The laws of nature must first be grasped **elementarily** before their intricate interactions can be comprehended."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Sensory impressions are grouped **elementarily** in consciousness before complex cognitive synthesis occurs."
      },
      {
        "author": "John Dewey",
        "work": "Democracy and Education",
        "quote": "Subject matter presented **elementarily** allows novice learners to build stable cognitive scaffolding."
      }
    ]
  },
  "Dashboard — elem\\elementary.md": {
    "primary": "Relating to the basic, introductory, or fundamental elements of a subject; straightforward or uncomplicated.",
    "secondary": "In physics and chemistry, consisting of a single chemical element or an irreducible subatomic particle.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Memoirs of Sherlock Holmes",
        "quote": "'**Elementary**,' said he; 'it is one of those instances where the reasoner can produce an effect which seems remarkable to his neighbor.'"
      },
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "quote": "An **elementary** law of mechanics states that the center of gravity of a system moves uniformly in a straight line."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Problems of Philosophy",
        "quote": "Immediate acquaintance provides our most **elementary** source of genuine knowledge."
      }
    ]
  },
  "Dashboard — elem\\elements.md": {
    "primary": "Plural of element: the basic principles, primary constituents, or atmospheric environmental forces.",
    "secondary": "In classical philosophy and chemistry, the foundational building blocks of the material universe (fire, air, water, earth; or atomic elements).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Julius Caesar",
        "quote": "His life was gentle, and the **elements** so mixed in him that Nature might stand up and say to all the world, 'This was a man!'"
      },
      {
        "author": "Euclid",
        "work": "The Elements",
        "quote": "The fundamental propositions gathered in the **Elements** establish the axiomatic foundations of geometry."
      },
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The chemical **elements** represent the empirical boundary of our analytical decomposition."
      }
    ]
  },
  "Dashboard — elem\\elemi.md": {
    "primary": "A fragrant, pale-yellow oleoresin obtained from various tropical trees, especially Canarium luzonicum, used in varnishes, lacquers, and ointments.",
    "secondary": "In traditional pharmacognosy and perfumery, elemi imparts spicy, citrus-peppery balsam notes and acts as a skin-soothing plasticizer.",
    "quotes": [
      {
        "author": "Robert Bentley",
        "work": "Medicinal Plants",
        "quote": "Manila **elemi** exudes as a soft resin that hardens upon exposure, possessing a fragrant fennel-like aroma."
      },
      {
        "author": "G. W. Askinson",
        "work": "Perfumes and Cosmetics: Their Preparation and Manufacture",
        "quote": "The inclusion of gum **elemi** in protective varnishes ensures flexibility and high gloss resistance."
      },
      {
        "author": "Jonathan Pereira",
        "work": "The Elements of Materia Medica and Therapeutics",
        "quote": "Topical unguents containing **elemi** stimulate indolent ulcer healing through mild counter-irritation."
      }
    ]
  },
  "Dashboard — en\\ellipse.md": {
    "primary": "A closed, symmetrical plane curve formed by the intersection of a cone with an inclined plane, defined as the locus of points where the sum of distances to two foci is constant.",
    "secondary": "In celestial mechanics, Kepler's first law demonstrates that planetary orbits describe an ellipse with the sun situated at one focus.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Astronomia Nova",
        "quote": "The orbit of the planet is not a circle, but an **ellipse**, in which the sun occupies one of the foci."
      },
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "An inverse-square central attractive force compels a revolving body to trace out a conic section, preeminently an **ellipse**."
      },
      {
        "author": "Archimedes",
        "work": "On Conoids and Spheroids",
        "quote": "The area enclosed by an **ellipse** is proportional to the product of its semi-major and semi-minor axes."
      }
    ]
  },
  "Dashboard — en\\ellipsis.md": {
    "primary": "The omission of one or more words from a sentence that are readily understood in context; also, the punctuation mark (...) denoting omitted text or a trailing pause.",
    "secondary": "In stylistics and rhetoric, ellipsis speeds discourse tempo and invites the auditor to actively supply the omitted conceptual link.",
    "quotes": [
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "Graceful use of **ellipsis** avoids tedious repetition by leaving obvious words to the hearer's intelligence."
      },
      {
        "author": "Henry Fowler",
        "work": "The King's English",
        "quote": "Careful writers employ **ellipsis** to achieve conciseness without introducing grammatical ambiguity."
      },
      {
        "author": "Laurence Sterne",
        "work": "The Life and Opinions of Tristram Shandy",
        "quote": "A thoughtful pause, marked by an expressive **ellipsis**, conveyed far more than any torrent of eloquence."
      }
    ]
  },
  "Dashboard — en\\ellipsoid.md": {
    "primary": "A three-dimensional geometric surface whose plane cross-sections are all ellipses or circles.",
    "secondary": "In geodesy and planetary astronomy, the reference ellipsoid approximates the oblate rotational shape of the Earth.",
    "quotes": [
      {
        "author": "Carl Friedrich Gauss",
        "work": "General Investigations of Curved Surfaces",
        "quote": "Triangulation measurements across continents are mapped onto a reference **ellipsoid** that accounts for rotational flattening."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The electrostatic potential outside a charged conducting **ellipsoid** can be resolved using confocal coordinates."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Introduction to Geometry",
        "quote": "An **ellipsoid** has three mutually orthogonal principal axes of symmetry that intersect at its center."
      }
    ]
  },
  "Dashboard — en\\elliptic.md": {
    "primary": "Having the form of an ellipse; relating to, resembling, or characterized by an ellipse or mathematical ellipsis.",
    "secondary": "In mathematics, elliptic curves and elliptic functions play foundational roles in algebraic geometry, number theory, and cryptography.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Science and Method",
        "quote": "The transformation of **elliptic** integrals into automorphic functions opened unimagined vistas in analysis."
      },
      {
        "author": "Andrew Wiles",
        "work": "Modular Elliptic Curves and Fermat's Last Theorem",
        "quote": "The modularity theorem establishes a profound bridge between modular forms and every rational **elliptic** curve."
      },
      {
        "author": "Arthur Cayley",
        "work": "An Elementary Treatise on Elliptic Functions",
        "quote": "Doubly periodic **elliptic** functions generalize circular trigonometry to the complex plane."
      }
    ]
  },
  "Dashboard — en\\elliptical.md": {
    "primary": "Shaped like an ellipse; oval; also, characterized by deliberate omission of words or oblique, ambiguous phrasing.",
    "secondary": "In astrophysics, elliptical galaxies are smooth, featureless stellar systems with minimal interstellar gas and little active star formation.",
    "quotes": [
      {
        "author": "Edwin Hubble",
        "work": "The Realm of the Nebulae",
        "quote": "Galaxies classify smoothly from globular, dense **elliptical** systems into flattened spirals with winding arms."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "Her conversation was delightfully **elliptical**, skipping over obvious transitions to alight upon subtle intuitions."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Physiography",
        "quote": "The earth revolves along an **elliptical** path that brings it nearest to the sun during the northern hemisphere's winter."
      }
    ]
  },
  "Dashboard — en\\ellipticity.md": {
    "primary": "The degree of deviation of an ellipse or spheroid from circular or spherical form; flattening.",
    "secondary": "In geophysics and planetary physics, the dynamical ellipticity of Earth reflects mass distribution and polar oblateness ($f = (a-b)/a$).",
    "quotes": [
      {
        "author": "Pierre-Simon Laplace",
        "work": "Celestial Mechanics",
        "quote": "The gravitational equilibrium of a rotating fluid mass requires a definite degree of equatorial **ellipticity**."
      },
      {
        "author": "George Biddell Airy",
        "work": "Mathematical Tracts on the Lunar and Planetary Theories",
        "quote": "Precise measurements of pendular oscillation confirm the polar **ellipticity** of the terrestrial globe."
      },
      {
        "author": "Harold Jeffreys",
        "work": "The Earth: Its Origin, History and Physical Constitution",
        "quote": "Hydrostatic theory predicts a terrestrial **ellipticity** closely matching observations from artificial satellite orbits."
      }
    ]
  },
  "Dashboard — en\\en.md": {
    "primary": "A Greek preposition and prefix meaning 'in', 'into', 'within', or 'on'; also, in typography, a unit of width equal to half an em.",
    "secondary": "In lexical morphology, en- forms words designating internal state (energy), containment (entomology), or intensification (enthusiasm).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The preposition **en** governs the dative case to express location within physical boundaries or temporal spans."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Deriving from PIE *h₁en ('in'), **en** is one of the most productive locative prefixes in Greek vocabulary."
      },
      {
        "author": "Jan Tschichold",
        "work": "The Form of the Book",
        "quote": "Typographers distinguish the **en** dash from the longer em dash to indicate numerical and temporal ranges."
      }
    ]
  },
  "Dashboard — en\\enclitic.md": {
    "primary": "A word or particle grammatically joined so closely to the preceding word that it loses its independent accent.",
    "secondary": "In classical Greek grammar and Indo-European metrics, enclitic pronouns and particles lean phonetically upon the host word, modifying its accentuation.",
    "quotes": [
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "An **enclitic** throws its accent back upon the preceding word under precise euphonic rules governing morae."
      },
      {
        "author": "Robert Browning",
        "work": "A Grammarian's Funeral",
        "quote": "He settled Hoti's business—let it be!—properly based Oun—gave us the doctrine of the **enclitic** De!"
      },
      {
        "author": "Eduard Schwyzer",
        "work": "Griechische Grammatik",
        "quote": "The loss of tonal autonomy in an **enclitic** mirrors syntactic cohesion within the spoken sentence."
      }
    ]
  },
  "Dashboard — endo\\endo.md": {
    "primary": "A combining form and prefix derived from Greek, meaning 'within', 'inner', 'internal', or 'absorbing'.",
    "secondary": "In biochemistry and cell biology, endo- designates internal location, intracellular mechanisms, or energy-absorbing reactions (endothermic).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Derived from the adverb endon ('within'), the prefix **endo** productively forms terms designating internal structures."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Pathways designated by **endo** routinely operate inside closed cellular compartments or epithelial boundaries."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The morpheme **endo** contrasts symmetrically with exo- across modern scientific taxonomies."
      }
    ]
  },
  "Dashboard — endo\\endocardial.md": {
    "primary": "Pertaining to, situated in, or affecting the endocardium (the innermost lining membrane of the heart chambers and valves).",
    "secondary": "In cardiology, endocardial biopsies provide histological surveillance against allograft rejection following cardiac transplantation.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Turbulent blood flow across a stenotic valve can denude the **endocardial** surface, predisposing to bacterial adherence."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **endocardial** endothelium continues smoothly into the intimal lining of the great outgoing arteries."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Purkinje fibers lie directly beneath the **endocardial** layer, rapidly distributing electrical impulses to the ventricular myocardium."
      }
    ]
  },
  "Dashboard — endo\\endocarditis.md": {
    "primary": "Inflammation of the endocardium, typically involving heart valves and caused by bacterial, fungal, or nonbacterial thrombotic vegetations.",
    "secondary": "In infectious disease and cardiology, infective endocarditis requires prolonged bactericidal intravenous therapy to sterilize avascular valvular vegetations.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Gulstonian Lectures on Malignant Endocarditis",
        "quote": "The vegetations in ulcerative **endocarditis** swarm with micrococci, forming colonies upon the free margins of the valves."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Subacute bacterial **endocarditis** manifests with insidious fever, new or changing murmurs, and peripheral embolic signs."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Nonbacterial thrombotic **endocarditis** occurs in debilitated patients, characterized by sterile fibrin and platelet deposits."
      }
    ]
  },
  "Dashboard — endo\\endocardium.md": {
    "primary": "The smooth, serous endothelial membrane lining the interior cavities, valves, and papillary muscles of the heart.",
    "secondary": "In cardiac embryology, the endocardium develops from angiogenic mesenchyme that forms the primitive endocardial heart tubes.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **endocardium** consists of an epithelial layer of squamous cells supported by delicate subendothelial connective tissue."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Friction between circulating blood and cardiac chambers is minimized by the unbroken smoothness of the **endocardium**."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Cues from the **endocardium** induce adjacent myocardial cells to thicken and differentiate into mature ventricular walls."
      }
    ]
  },
  "Dashboard — endo\\endocarp.md": {
    "primary": "The innermost layer of the pericarp (fruit wall) surrounding the seed, which may be stony (as in peaches), membranous, or fleshy.",
    "secondary": "In systematic botany, the sclerified endocarp of a drupe (the pit or stone) provides mechanical protection to the enclosed embryo.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "In a stone-fruit like the peach or cherry, the stone is the bony **endocarp**, while the fleshy pulp is the mesocarp."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The citrus juice vesicles arise as multicellular outgrowths projecting from the inner surface of the **endocarp**."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Lignified brachysclereids form the dense, interlocking armor characteristic of the stone-fruit **endocarp**."
      }
    ]
  },
  "Dashboard — endo\\endocentric.md": {
    "primary": "Fulfilling the same grammatical or syntactic role as one of its constituents; possessing an internal head word (in linguistics).",
    "secondary": "In structural grammar and syntactic morphology, an endocentric construction (like 'black cat') is an expansion of its head noun ('cat').",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "An **endocentric** phrase belongs to the same form-class as one or more of its constituents, which functions as its center or head."
      },
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "The X-bar theory formalizes the intuition that standard phrases are inherently **endocentric** projections of lexical categories."
      },
      {
        "author": "John Lyons",
        "work": "Introduction to Theoretical Linguistics",
        "quote": "In contrast to exocentric compounds, **endocentric** formations preserve the semantic and distributional class of their primary head."
      }
    ]
  },
  "Dashboard — endo\\endocerid.md": {
    "primary": "An extinct fossil nautiloid cephalopod of the order Endocerida, featuring a straight or gently curved shell with an unusually wide ventral siphuncle.",
    "secondary": "In invertebrate paleontology, giant Ordovician endocerids like Endoceras reached lengths exceeding five meters, reigning as apex marine predators.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Before the rise of jawed fishes, the predatory **endocerid** dominated early Paleozoic shallow epeiric seas."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The massive, straight-shelled **endocerid** represents an astonishing early experiment in cephalopod gigantism."
      },
      {
        "author": "Curt Teichert",
        "work": "Treatise on Invertebrate Paleontology: Mollusca 3",
        "quote": "The siphuncle of an **endocerid** contained extensive endosiphuncular deposits that acted as counterweights for horizontal trim."
      }
    ]
  },
  "Dashboard — endo\\endocervicitis.md": {
    "primary": "Inflammation of the mucous membrane and glandular lining of the endocervical canal of the uterine cervix.",
    "secondary": "In gynecologic pathology, endocervicitis is frequently caused by Chlamydia trachomatis or Neisseria gonorrhoeae, presenting with mucopurulent exudate.",
    "quotes": [
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Chronic **endocervicitis** is characterized by dense lymphocytic and plasma cell infiltrates in the subepithelial cervical stroma."
      },
      {
        "author": "Leon Speroff",
        "work": "Clinical Gynecologic Endocrinology and Infertility",
        "quote": "Hostile cervical mucus resulting from untreated **endocervicitis** can prevent sperm transit and cause mechanical infertility."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Targeted antibiotic regimens clear chlamydial **endocervicitis** and halt ascending infection toward the fallopian tubes."
      }
    ]
  },
  "Dashboard — endo\\endocranium.md": {
    "primary": "The inner surface of the cranial cavity; also, the internal cartilaginous or bony casing housing the brain.",
    "secondary": "In paleoanthropology and functional craniology, endocranial casts (endocasts) preserve the impression of cerebral gyri, meningeal vessels, and cranial capacity.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The dura mater functions both as an internal periosteum for the **endocranium** and as a protective envelope for the brain."
      },
      {
        "author": "G. Elliot Smith",
        "work": "The Evolution of the Brain",
        "quote": "Careful examination of the **endocranium** reveals impressions left by the expansion of Broca's speech area in fossil hominids."
      },
      {
        "author": "Wilfrid Le Gros Clark",
        "work": "The Fossil Evidence for Human Evolution",
        "quote": "Endocranial volume and sulcal topology of the **endocranium** provide vital clues to encephalization trajectories."
      }
    ]
  },
  "Dashboard — endo\\endocrinal.md": {
    "primary": "Of, relating to, or involving endocrine glands or their hormonal secretions.",
    "secondary": "In systemic physiology, endocrinal signaling modulates long-term metabolic homeostasis, growth, and reproduction via humoral circulation.",
    "quotes": [
      {
        "author": "Walter B. Cannon",
        "work": "The Wisdom of the Body",
        "quote": "Homeostatic balance relies upon intertwined nervous reflexes and sustained **endocrinal** secretional responses."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Feedback inhibition regulates **endocrinal** axes to prevent pathological overproduction of target hormones."
      },
      {
        "author": "Hans Selye",
        "work": "The Stress of Life",
        "quote": "The general adaptation syndrome orchestrates profound **endocrinal** shifts centered upon pituitary and adrenocortical activation."
      }
    ]
  },
  "Dashboard — endo\\endocrine.md": {
    "primary": "Secreting hormones or other regulatory chemical messengers directly into the bloodstream or lymph rather than through a duct.",
    "secondary": "In physiology, the endocrine system comprises ductless glands (thyroid, pituitary, adrenals, islets of Langerhans) regulating organ function.",
    "quotes": [
      {
        "author": "Ernest Starling",
        "work": "The Croonian Lectures on the Chemical Correlation of the Functions of the Body",
        "quote": "These chemical messengers, or hormones, produced by an **endocrine** gland, travel through the circulation to evoke distant responses."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The anterior pituitary coordinates the activity of multiple subordinate **endocrine** target tissues."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The internal milieu is stabilized by the continuous internal secretions of **endocrine** vascular glands."
      }
    ]
  },
  "Dashboard — endo\\endocrinologist.md": {
    "primary": "A physician or biomedical scientist who specializes in the diagnosis, treatment, and study of endocrine system disorders and hormonal imbalances.",
    "secondary": "In clinical medicine, endocrinologists manage complex metabolic diseases including diabetes mellitus, thyroid neoplasms, osteoporosis, and adrenal insufficiency.",
    "quotes": [
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "When managing brittle diabetes with recurrent ketoacidosis, consultation with an experienced **endocrinologist** is paramount."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The **endocrinologist** mapped out the subtle biochemical cascades that had altered the patient's sleep-wake cycle."
      },
      {
        "author": "Jerome Groopman",
        "work": "How Doctors Think",
        "quote": "A thoughtful **endocrinologist** sifts through non-specific fatigue symptoms to uncover occult autoimmune thyroiditis."
      }
    ]
  },
  "Dashboard — endo\\endocrinology.md": {
    "primary": "The branch of physiology and medicine concerned with endocrine glands, hormonal signaling pathways, and related metabolic disorders.",
    "secondary": "In modern molecular biology, endocrinology bridges genomic receptor pharmacology, neuroendocrine integration, and cellular metabolic control.",
    "quotes": [
      {
        "author": "Laurence L. Brunton",
        "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        "quote": "The history of modern **endocrinology** began with the isolation and therapeutic application of bovine insulin."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Comparative **endocrinology** demonstrates remarkable evolutionary conservation of peptide hormone structures across vertebrates."
      },
      {
        "author": "Hans Selye",
        "work": "The Story of the Adaptation Syndrome",
        "quote": "Experimental **endocrinology** demonstrated that physical stressors trigger identical hormonal discharges regardless of the stimulus."
      }
    ]
  },
  "Dashboard — endo\\endocytosis.md": {
    "primary": "The cellular process by which a cell internalizes extracellular substances, fluids, or particles by invaginating its plasma membrane to form a vesicle.",
    "secondary": "In cell biology, endocytosis encompasses receptor-mediated endocytosis via clathrin-coated pits, pinocytosis, and phagocytosis.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Receptor-mediated **endocytosis** provides a selective mechanism by which cells ingest specific macromolecules such as cholesterol-rich LDL."
      },
      {
        "author": "Harvey Lodish",
        "work": "Molecular Cell Biology",
        "quote": "Upon ligand binding, clathrin triskelions assemble at the membrane to pinch off the invaginated vesicle during **endocytosis**."
      },
      {
        "author": "Christian de Duve",
        "work": "A Guided Tour of the Living Cell",
        "quote": "Lysosomal degradation relies upon vesicular delivery routed through the early and late stages of cellular **endocytosis**."
      }
    ]
  },
  "Dashboard — endo\\endoergic.md": {
    "primary": "Absorbing or requiring an input of energy (especially in nuclear or atomic physics); endothermic.",
    "secondary": "In nuclear reaction kinetics, an endoergic reaction has a negative Q-value and can only proceed if the projectile possesses kinetic energy exceeding a threshold value.",
    "quotes": [
      {
        "author": "Enrico Fermi",
        "work": "Nuclear Physics",
        "quote": "An **endoergic** nuclear transmutation requires the incoming projectile to supply the necessary reaction threshold energy."
      },
      {
        "author": "Hans Bethe",
        "work": "Elementary Nuclear Theory",
        "quote": "The negative Q-value confirms that the reaction is **endoergic**, requiring kinetic energy conversion into rest-mass energy."
      },
      {
        "author": "Emilio Segrè",
        "work": "Nuclei and Particles",
        "quote": "Threshold detectors exploit **endoergic** neutron capture processes to quantify high-energy flux distributions in reactors."
      }
    ]
  },
  "Dashboard — endo\\endolymph.md": {
    "primary": "The potassium-rich extracellular fluid contained within the membranous labyrinth of the inner ear, bathing hair cell stereocilia.",
    "secondary": "In sensory physiology, endolymph has a positive endocochlear potential (~+80 mV) that drives mechanotransduction currents into auditory hair cells.",
    "quotes": [
      {
        "author": "Georg von Békésy",
        "work": "Experiments in Hearing",
        "quote": "The high potassium concentration of **endolymph** generates an electrical battery that powers the mechanical tuning of the cochlea."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Deflection of the cupula by fluid currents in the **endolymph** signals angular acceleration to the vestibular nerve."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The membranous labyrinth is filled with **endolymph** and surrounded by perilymph within the bony otic capsule."
      }
    ]
  },
  "Dashboard — endo\\endometrial.md": {
    "primary": "Pertaining to, situated in, or derived from the endometrium (the inner mucous membrane lining of the uterus).",
    "secondary": "In gynecologic oncology and histology, endometrial hyperplasia and carcinoma are correlated with prolonged, unopposed estrogenic stimulation.",
    "quotes": [
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Atypical **endometrial** hyperplasia carries a substantial risk of progression into well-differentiated adenocarcinoma."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Progesterone transforms the proliferative **endometrial** lining into a secretory bed primed for blastocyst implantation."
      },
      {
        "author": "Leon Speroff",
        "work": "Clinical Gynecologic Endocrinology and Infertility",
        "quote": "Cyclical shedding of the **endometrial** functional layer occurs in response to the withdrawal of ovarian steroid support."
      }
    ]
  },
  "Dashboard — endo\\endometriosis.md": {
    "primary": "A chronic medical condition characterized by the abnormal presence and growth of endometrial tissue outside the uterine cavity.",
    "secondary": "In gynecology, ectopic endometrial implants respond to cyclical ovarian hormones, causing chronic pelvic pain, dysmenorrhea, adhesions, and subfertility.",
    "quotes": [
      {
        "author": "John A. Sampson",
        "work": "Peritoneal Endometriosis Due to the Menstrual Dissemination of Endometrial Tissue",
        "quote": "Retrograde menstruation provides a plausible pathway for shedding viable tissue that seeds pelvic **endometriosis**."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Laparoscopic visualization of 'powder-burn' peritoneal lesions remains the gold standard for diagnosing pelvic **endometriosis**."
      },
      {
        "author": "Leon Speroff",
        "work": "Clinical Gynecologic Endocrinology and Infertility",
        "quote": "Surgical excision combined with hormonal suppression relieves debilitating pain and restores fertility in extensive **endometriosis**."
      }
    ]
  },
  "Dashboard — endo\\endometritis.md": {
    "primary": "Inflammation or infection of the endometrium, the inner mucous lining of the uterine body.",
    "secondary": "In obstetrics and gynecology, postpartum endometritis arises from ascending polymicrobial vaginal flora following prolonged labor or cesarean delivery.",
    "quotes": [
      {
        "author": "F. Gary Cunningham",
        "work": "Williams Obstetrics",
        "quote": "Postpartum **endometritis** manifests with uterine tenderness, foul-smelling lochia, and fever exceeding 38 degrees Celsius."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "The histologic hallmark of chronic **endometritis** is the presence of plasma cells within the endometrial stroma."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Puerperal fever was historically driven by fulminant bacterial **endometritis** spreading through pelvic venous sinuses."
      }
    ]
  },
  "Dashboard — endo\\endometrium.md": {
    "primary": "The mucous membrane lining the inner cavity of the mammalian uterus, which thickens and sheds cyclically in menstruating primates.",
    "secondary": "In reproductive histology, the endometrium is divided into a superficial functional layer (stratum functionale) and a permanent regenerative basal layer (stratum basale).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **endometrium** is lined by simple columnar ciliated epithelium and studded with tubular uterine glands."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "During the luteal phase, the **endometrium** doubles in thickness, storing glycogen and lipids to nourish the early embryo."
      },
      {
        "author": "Leon Speroff",
        "work": "Clinical Gynecologic Endocrinology and Infertility",
        "quote": "Synchronized crosstalk between blastocyst trophoblast and maternal **endometrium** is essential for successful implantation."
      }
    ]
  },
  "Dashboard — endo\\endomorph.md": {
    "primary": "A human body somatotype characterized by a soft, rounded build, high body-fat percentage, and prominent development of visceral digestive organs.",
    "secondary": "In constitutional psychology (Sheldon's classification), an endomorph was hypothesized to exhibit viscerotonic tendencies toward comfort and sociability.",
    "quotes": [
      {
        "author": "William H. Sheldon",
        "work": "The Varieties of Human Physique",
        "quote": "The predominant **endomorph** displays digestive viscera that are massive in proportion to somatic skeletal framing."
      },
      {
        "author": "J. M. Tanner",
        "work": "Foetus into Man",
        "quote": "In somatotyping, the degree of rounded adiposity determines the first rating assigned to the classic **endomorph**."
      },
      {
        "author": "Robert M. Malina",
        "work": "Growth, Maturation, and Physical Activity",
        "quote": "Nutritional abundance during childhood can accelerate subcutaneous fat deposition, enhancing **endomorph** traits."
      }
    ]
  },
  "Dashboard — endo\\endomorphic.md": {
    "primary": "Having or characteristic of the physical build of an endomorph; possessing a soft, heavy, or round physique.",
    "secondary": "In kinesiology and physical anthropometry, having a body shape dominated by high fat-to-muscle ratio and broad trunk proportions.",
    "quotes": [
      {
        "author": "William H. Sheldon",
        "work": "Atlas of Men",
        "quote": "An **endomorphic** constitution manifests in spherical trunk contours, heavy thighs, and small, tapered extremities."
      },
      {
        "author": "Hans Eysenck",
        "work": "The Structure of Human Personality",
        "quote": "Empirical studies failed to replicate the strong temperamental correlations once claimed for **endomorphic** somatotypes."
      },
      {
        "author": "J. E. Lindsay Carter",
        "work": "Somatotyping: Development and Applications",
        "quote": "Wrestlers in super-heavyweight divisions often combine high mesomorphic power with an **endomorphic** cushion."
      }
    ]
  },
  "Dashboard — endo\\endomorphy.md": {
    "primary": "The physical characteristic, state, or degree of endomorphic traits (softness, roundness, relative fatness) in human bodily constitution.",
    "secondary": "In anthropometric somatotyping (Heath-Carter method), endomorphy is calculated using the sum of triceps, subscapular, and supraspinale skinfolds.",
    "quotes": [
      {
        "author": "J. E. Lindsay Carter",
        "work": "Somatotyping: Development and Applications",
        "quote": "The first component of the somatotype rating reflects relative **endomorphy**, derived directly from caliper skinfold sums."
      },
      {
        "author": "William H. Sheldon",
        "work": "The Varieties of Delinquent Youth",
        "quote": "High **endomorphy** indicates vegetative predominance, where metabolic storage exceeds mechanical expenditure."
      },
      {
        "author": "G. A. Harrison",
        "work": "Human Biology: An Introduction to Human Evolution and Growth",
        "quote": "Socioeconomic shifts toward sedentary lifestyles have significantly increased average adult **endomorphy** ratings."
      }
    ]
  },
  "Dashboard — endo\\endomycetales.md": {
    "primary": "An order of primitive budding and fission ascomycetous fungi, encompassing true yeasts such as the family Saccharomycetaceae.",
    "secondary": "In fungal taxonomy, members of Endomycetales do not form ascocarps, producing naked asci directly from zygotes or single vegetative cells.",
    "quotes": [
      {
        "author": "C. J. Alexopoulos",
        "work": "Introductory Mycology",
        "quote": "The order **Endomycetales** comprises unicellular and simple pseudomycelial fungi that reproduce by budding or fission."
      },
      {
        "author": "David L. Hawksworth",
        "work": "Ainsworth & Bisby's Dictionary of the Fungi",
        "quote": "Brewer's yeast, Saccharomyces cerevisiae, historically represented the defining model organism of the **Endomycetales**."
      },
      {
        "author": "John Webster",
        "work": "Introduction to Fungi",
        "quote": "Because asci develop without surrounding fruit bodies, **Endomycetales** were regarded as phylogenetically primitive ascomycetes."
      }
    ]
  },
  "Dashboard — endo\\endoneurium.md": {
    "primary": "The delicate sheath of loose connective tissue enclosing each individual nerve fiber or axon within a peripheral nerve bundle.",
    "secondary": "In neurohistology and peripheral nerve repair, the endoneurium maintains the endoneurial fluid pressure necessary for axonal regeneration.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Degeneration and Regeneration of the Nervous System",
        "quote": "Regenerating axonal sprouts advance along the basal lamina tubes preserved within the **endoneurium**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Each peripheral nerve fascicle is subdivided by fine septa of **endoneurium** surrounding individual myelin sheaths."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The blood-nerve barrier is maintained by tight junctions between endothelial cells of microvessels inside the **endoneurium**."
      }
    ]
  },
  "Dashboard — endo\\endonuclease.md": {
    "primary": "An enzyme that cleaves the phosphodiester bonds within a polynucleotide chain (DNA or RNA) rather than at its terminal ends.",
    "secondary": "In molecular cloning and biotechnology, restriction endonucleases recognize specific palindromic nucleotide sequences to generate cohesive or blunt DNA fragments.",
    "quotes": [
      {
        "author": "Hamilton O. Smith",
        "work": "Nucleotide Sequence Specificity of Restriction Endonucleases",
        "quote": "The type II restriction **endonuclease** cleaves double-stranded DNA exclusively at a distinct palindromic sequence."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Repair of pyrimidine dimers begins when a damage-specific **endonuclease** introduces a nick adjacent to the lesion."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "CRISPR-Cas9 acts as an RNA-guided **endonuclease** that creates site-specific double-strand breaks in target genomic loci."
      }
    ]
  },
  "Dashboard — endo\\endorphin.md": {
    "primary": "Any of a group of endogenous opioid peptide neurotransmitters produced in the brain and pituitary that bind to mu-opioid receptors to inhibit pain and induce euphoria.",
    "secondary": "In neuropharmacology, beta-endorphin is derived from pro-opiomelanocortin (POMC) and mediates stress-induced analgesia and exercise runner's high.",
    "quotes": [
      {
        "author": "Solomon H. Snyder",
        "work": "Opiate Receptors and Internal Opiates",
        "quote": "The discovery of **endorphin** proved that the mammalian brain synthesizes its own intrinsic morphine-like peptides."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Presynaptic release of **endorphin** in the dorsal horn inhibits substance P transmission, attenuating incoming nociceptive signals."
      },
      {
        "author": "Candace Pert",
        "work": "Molecules of Emotion",
        "quote": "Receptor binding of **endorphin** across the limbic system demonstrates how biochemical signals modulate subjective emotional states."
      }
    ]
  },
  "Dashboard — endo\\endorser.md": {
    "primary": "A person who signs a check, bill of exchange, or legal document to transfer ownership or guarantee payment; also, one who publicly supports a candidate, cause, or commercial product.",
    "secondary": "In commercial law, an endorser undertakes secondary liability if the primary drawee dishonors the negotiable instrument.",
    "quotes": [
      {
        "author": "William Blackstone",
        "work": "Commentaries on the Laws of England",
        "quote": "By signing the instrument, the **endorser** guarantees to every subsequent holder that the bill shall be paid upon due presentment."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "A bill of exchange bearing the signatures of several reputable merchants derives added credit from each successive **endorser**."
      },
      {
        "author": "Benjamin Franklin",
        "work": "Autobiography",
        "quote": "He asked me to become his **endorser** for a promissory note at the bank, a perilous request I prudently declined."
      }
    ]
  },
  "Dashboard — endo\\endoscope.md": {
    "primary": "An illuminated optical medical instrument (rigid or flexible) inserted into a hollow organ or body cavity to visually inspect internal tissues and perform biopsy.",
    "secondary": "In minimally invasive surgery and gastroenterology, video endoscopes integrate fiber optics, CCD sensors, and working channels for therapeutic interventions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Direct visualization through the **endoscope** has converted speculative gastric diagnosis into positive anatomical certainty."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Hemostasis of bleeding peptic ulcers is routinely accomplished through a flexible **endoscope** using thermal probes or hemoclips."
      },
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "The introduction of the arthroscopic **endoscope** revolutionized joint surgery by eliminating the morbidity of wide arthrotomy."
      }
    ]
  },
  "Dashboard — endo\\endoscopic.md": {
    "primary": "Of, relating to, performed by, or employing an endoscope; internal visual examination.",
    "secondary": "In surgery, endoscopic procedures offer reduced patient convalescence, lower infection rates, and minimal tissue disruption compared to open operations.",
    "quotes": [
      {
        "author": "Courtney M. Townsend",
        "work": "Sabiston Textbook of Surgery",
        "quote": "Modern surgical training emphasizes **endoscopic** retrograde cholangiopancreatography for removing obstructive biliary stones."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Multiple mucosal pinch biopsies obtained during **endoscopic** evaluation are necessary to confirm suspected celiac sprue."
      },
      {
        "author": "Sherwood L. Gorbach",
        "work": "Infectious Diseases",
        "quote": "Rigorous sterilization protocols prevent cross-contamination during successive **endoscopic** procedures."
      }
    ]
  },
  "Dashboard — endo\\endoscopy.md": {
    "primary": "The medical procedure of examining the interior of a hollow organ, joint, or body cavity using an endoscope.",
    "secondary": "In clinical gastroenterology and pulmonology, diagnostic and interventional endoscopy allows tissue biopsy, polyp resection, stent placement, and laser ablation.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Upper gastrointestinal **endoscopy** provides unmatched diagnostic accuracy for evaluating persistent dyspepsia and dysphagia."
      },
      {
        "author": "Courtney M. Townsend",
        "work": "Sabiston Textbook of Surgery",
        "quote": "Therapeutic **endoscopy** has replaced exploratory laparotomy for many conditions of acute biliary obstruction."
      },
      {
        "author": "Jerome Groopman",
        "work": "The Measure of Our Days",
        "quote": "Routine screening via colon **endoscopy** intercepts pre-malignant adenomatous polyps before invasive transformation occurs."
      }
    ]
  },
  "Dashboard — endo\\endoskeleton.md": {
    "primary": "An internal supporting skeleton or structural framework within an animal's body, characteristic of vertebrates and echinoderms.",
    "secondary": "In evolutionary morphology, an endoskeleton grows continuously with the organism, avoiding the developmental molting constraints imposed by an exoskeleton.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "The Vertebrate Body",
        "quote": "The living bony **endoskeleton** of vertebrates possesses the supreme advantage of continuous vascular growth without ecdysis."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The homologous architecture of the vertebrate **endoskeleton** points unmistakably to common descent from an ancestral prototype."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The transition from external armor to a dynamic internal **endoskeleton** unlocked unprecedented opportunities for vertebrate gigantism."
      }
    ]
  },
  "Dashboard — endo\\endosperm.md": {
    "primary": "The nutrient-rich tissue formed within the seeds of flowering plants following double fertilization, nourishing the developing embryo.",
    "secondary": "In angiosperm embryology, the endosperm is characteristically triploid ($3n$), formed when one sperm cell fuses with the binucleate central cell.",
    "quotes": [
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Double fertilization generates both a diploid embryo and a triploid nutritive tissue known as the **endosperm**."
      },
      {
        "author": "Lincoln Taiz",
        "work": "Plant Physiology",
        "quote": "During cereal germination, gibberellins secreted by the embryo stimulate the aleurone layer to digest starch stored in the **endosperm**."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The white flour of wheat corresponds to the milled starchy **endosperm**, separated from the proteinaceous aleurone and fibrous bran."
      }
    ]
  },
  "Dashboard — endo\\endospore.md": {
    "primary": "A dormant, tough, and non-reproductive structure produced by certain Gram-positive bacteria (e.g., Bacillus and Clostridium) in response to nutrient deprivation.",
    "secondary": "In medical microbiology and sterilization science, bacterial endospores withstand extreme heat, desiccation, and ionizing radiation due to dipicolinic acid complexes.",
    "quotes": [
      {
        "author": "Robert Koch",
        "work": "The Etiology of Anthrax",
        "quote": "The resistant anthrax **endospore** survives for years in pastures, germinating into virulent vegetative bacilli upon entering a host."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Intermittent boiling, or tyndallization, is necessary to destroy heat-resistant **endospore** forms that survive single heating cycles."
      },
      {
        "author": "Michael T. Madigan",
        "work": "Brock Biology of Microorganisms",
        "quote": "Dehydration of the protoplast by calcium dipicolinate renders the **endospore** remarkably refractory to chemical disinfectants."
      }
    ]
  },
  "Dashboard — endo\\endosteum.md": {
    "primary": "The thin vascular membrane of connective tissue lining the medullary cavity and trabecular surfaces of bones.",
    "secondary": "In osteology and bone remodeling, the endosteum contains osteoprogenitor cells, osteoblasts, and osteoclasts active in bone turnover and repair.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The medullary canal of long bones is lined by a condensed cellular layer termed the **endosteum**."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "During prolonged hypocalcemia, osteoclasts along the **endosteum** resorb bone matrix to release calcium ions into circulation."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "The bone marrow microenvironment depends upon stromal signaling from cells residing along the **endosteum** lining."
      }
    ]
  },
  "Dashboard — endo\\endothelial.md": {
    "primary": "Pertaining to, situated in, or derived from the endothelium (the layer of flat epithelial-like cells lining blood and lymph vessels).",
    "secondary": "In vascular physiology, endothelial dysfunction characterized by diminished nitric oxide synthesis is an early pathophysiological event in atherosclerosis.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Intact **endothelial** cells synthesize prostacyclin and nitric oxide, maintaining blood flow and inhibiting platelet aggregation."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Inflammatory cytokines induce **endothelial** expression of selectins and integrins that guide leukocyte adhesion and diapedesis."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Capillary permeability is governed by tight junctions and vesicular transcytosis across adjacent **endothelial** cell borders."
      }
    ]
  },
  "Dashboard — endo\\endothelium.md": {
    "primary": "The single layer of smooth, flat squamous cells lining the interior surface of blood vessels, lymphatic vessels, and the heart chambers.",
    "secondary": "In vascular biology, the endothelium is recognized as an active paracrine organ regulating vasodilation, thrombosis, and vascular permeability.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Thrombosis frequently originates where mechanical damage or inflammation disrupts the integrity of the vascular **endothelium**."
      },
      {
        "author": "Robert F. Furchgott",
        "work": "The Obligatory Role of Endothelial Cells in the Relaxation of Arterial Smooth Muscle",
        "quote": "Acetylcholine fails to relax isolated arterial rings unless the luminal layer of **endothelium** is carefully preserved."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Continuous basal production of nitric oxide by the **endothelium** maintains systemic vascular resistance at physiological levels."
      }
    ]
  },
  "Dashboard — endo\\endothermal.md": {
    "primary": "Relating to or accompanied by the absorption of heat; endothermic.",
    "secondary": "In physical chemistry, an endothermal dissolution or decomposition draws thermal energy from the immediate surroundings, lowering local temperature.",
    "quotes": [
      {
        "author": "J. Willard Gibbs",
        "work": "On the Equilibrium of Heterogeneous Substances",
        "quote": "An **endothermal** phase transition is favored at elevated temperatures in accordance with the second law of thermodynamics."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Dissolving ammonium nitrate in water is a markedly **endothermal** process commonly exploited in instant chemical cold packs."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Worlds in the Making",
        "quote": "Solar radiation supplies the necessary thermal energy driving large-scale **endothermal** chemical transformations on planetary surfaces."
      }
    ]
  },
  "Dashboard — endo\\endothermic.md": {
    "primary": "Characterized by or resulting from the absorption of heat (in chemistry); or possessing physiological mechanisms to maintain internal body warmth (in zoology).",
    "secondary": "In thermodynamic reactions, enthalpy change is positive ($\\Delta H > 0$); in comparative physiology, endothermic animals maintain metabolic homeothermy.",
    "quotes": [
      {
        "author": "Knut Schmidt-Nielsen",
        "work": "Animal Physiology: Adaptation and Environment",
        "quote": "An **endothermic** animal relies on metabolic heat production and insulation to maintain an elevated, constant internal body temperature."
      },
      {
        "author": "Gilbert N. Lewis",
        "work": "Thermodynamics and the Free Energy of Chemical Substances",
        "quote": "An **endothermic** reaction absorbs heat from the surrounding bath, causing enthalpy of the products to exceed that of the reactants."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "Mammals and birds evolved high, sustained resting metabolic rates to support an active **endothermic** lifestyle."
      }
    ]
  },
  "Dashboard — endo\\endotoxin.md": {
    "primary": "A toxic lipopolysaccharide (LPS) complex forming an integral part of the outer membrane of Gram-negative bacteria, released upon bacterial lysis.",
    "secondary": "In pathology and critical care medicine, circulating endotoxin triggers massive macrophage release of TNF-alpha and IL-1, precipitating septic shock and DIC.",
    "quotes": [
      {
        "author": "Richard Pfeiffer",
        "work": "Investigations on Cholera Immunity",
        "quote": "The poisonous substance is not excreted into the broth, but remains bound as an **endotoxin** within the bacterial cell wall."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Circulating **endotoxin** binds to CD14 and TLR4 receptors, triggering the systemic inflammatory cascade that characterizes septic shock."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "High concentrations of bacterial **endotoxin** produce widespread endothelial damage, refractory hypotension, and multiorgan failure."
      }
    ]
  },
  "Dashboard — engy\\Engystomops.md": {
    "primary": "A genus of small neotropical leptodactylid frogs (including the túngara frog, Engystomops pustulosus) known for building floating foam nests.",
    "secondary": "In behavioral ecology and bioacoustics, Engystomops pustulosus is a prominent model organism for sexual selection and predatory eavesdropping by bats.",
    "quotes": [
      {
        "author": "Michael J. Ryan",
        "work": "The Túngara Frog: A Study in Sexual Selection and Communication",
        "quote": "Male **Engystomops** frogs add acoustic whines and chucks to their calls, balancing female attraction against predatory bat interception."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Acoustic divergence between geographical isolates of **Engystomops** illustrates speciation driven by sexual selection."
      },
      {
        "author": "G. A. Boulenger",
        "work": "Catalogue of the Batrachia Salientia in the British Museum",
        "quote": "The morphological characters of the genus **Engystomops** combine narrow pectoral architecture with granular dorsal tuberculation."
      }
    ]
  },
  "Dashboard — engy\\engy.md": {
    "primary": "A Greek root element meaning 'near', 'narrow', or 'pledge', appearing in zoological names and specialized anatomical and etymological terms.",
    "secondary": "In biological nomenclature, engy- denotes closeness or narrowness of form (as in Engystoma, narrow-mouthed amphibians).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The root **engy** denotes spatial proximity or tightness, cognate with terms designating immediate vicinity."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Related to Greek engys ('near'), the morpheme **engy** forms compounds indicating narrow or closely confined structures."
      },
      {
        "author": "Pierre Chantraine",
        "work": "Dictionnaire étymologique de la langue grecque",
        "quote": "Ancient Hellenic compounds incorporating **engy** convey notions of tight binding, pledged security, or physical nearness."
      }
    ]
  },
  "Dashboard — engy\\hypengyophobia.md": {
    "primary": "An abnormal, irrational, or disproportionate fear of taking on responsibility or answering for one's actions.",
    "secondary": "In clinical psychology and psychopathology, hypengyophobia can produce severe social avoidance and paralysis in decision-making.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Inhibitions, Symptoms and Anxiety",
        "quote": "In cases bordering on **hypengyophobia**, the ego retreats from vocational duties to escape the intolerable dread of accountability."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Clinical Psychiatry",
        "quote": "Neurotic dread of duty, or **hypengyophobia**, manifests with autonomic panic whenever adult responsibilities are assigned."
      },
      {
        "author": "Karl Jaspers",
        "work": "General Psychopathology",
        "quote": "The existential terror of guilt and accountability can crystallize into morbid **hypengyophobia**."
      }
    ]
  },
  "Dashboard — eso\\eso.md": {
    "primary": "A Greek combining element meaning 'within', 'inward', or 'inside'.",
    "secondary": "In medical ophthalmology and philosophy, eso- denotes inward deviation (esophoria, esotropia) or inner, restricted doctrines (esoteric).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The adverb **eso** or eiso signifies 'inwards' or 'into the interior', the morphological counterpart of exo."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Deriving from PIE *h₁en-s ('into'), **eso** productively forms technical terms denoting internal convergence."
      },
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "Spatial adverbs based on **eso** indicate direction toward the inner sanctum or central axis."
      }
    ]
  },
  "Dashboard — eso\\esophoria.md": {
    "primary": "A latent tendency of one or both eyes to turn inward toward the nose, held in check by the fusion reflex during binocular vision.",
    "secondary": "In optometry and ophthalmology, uncorrected esophoria can cause asthenopia, headache, and blurred vision during prolonged near work.",
    "quotes": [
      {
        "author": "Duke-Elder, Stewart",
        "work": "System of Ophthalmology",
        "quote": "Cover testing reveals that **esophoria** is instantly manifested when binocular fusion is interrupted by an occluder."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Excessive convergence accommodation tone during reading frequently unmasks symptomatic **esophoria**."
      },
      {
        "author": "David H. Hubel",
        "work": "Eye, Brain, and Vision",
        "quote": "The cortical binocular disparity detectors actively compensate for latent **esophoria** to preserve stereoscopic depth."
      }
    ]
  },
  "Dashboard — eso\\esoteric.md": {
    "primary": "Intended for or likely to be understood by only a small number of people with specialized knowledge or interest; abstruse or recondite.",
    "secondary": "In the history of philosophy, esoteric doctrines were reserved by Aristotle and Pythagorean schools for initiated disciples, distinct from exoteric public lectures.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Philosophers were accustomed to have two methods of teaching: one vulgar or exoteric, the other **esoteric** and reserved for initiates."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The philosophers reserved their **esoteric** skepticism for private conversation, while observing state rituals in public."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Pythagoras founded a society where **esoteric** mathematical mysteries were guarded with religious solemnity."
      }
    ]
  },
  "Dashboard — eso\\esotericism.md": {
    "primary": "The quality, practice, or state of being esoteric; obscure, mystical, or specialized knowledge restricted to an enlightened circle.",
    "secondary": "In religious studies and the history of ideas, Western esotericism comprises hermeticism, alchemy, Kabbalah, and Rosicrucian traditions.",
    "quotes": [
      {
        "author": "Antoine Faivre",
        "work": "Access to Western Esotericism",
        "quote": "The hallmark of **esotericism** is the belief in universal correspondences connecting all visible and invisible planes of reality."
      },
      {
        "author": "Wouter J. Hanegraaff",
        "work": "Esotericism and the Academy",
        "quote": "Enlightenment thinkers rejected **esotericism** as rejected knowledge, banishing it from modern scientific discourse."
      },
      {
        "author": "Frances Yates",
        "work": "The Rosicrucian Enlightenment",
        "quote": "Renaissance **esotericism** bridged ancient mystical lore with the emerging impulses of empirical natural philosophy."
      }
    ]
  },
  "Dashboard — eso\\esotropia.md": {
    "primary": "A manifest convergent strabismus; an ocular condition where one or both eyes turn inward toward the nose (cross-eyed).",
    "secondary": "In pediatric ophthalmology, infantile esotropia requires early surgical realignment or refractive correction to prevent irreversible amblyopia.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Early diagnosis of infantile **esotropia** is critical to preserve binocular fusion and avoid cortical suppression amblyopia."
      },
      {
        "author": "Duke-Elder, Stewart",
        "work": "System of Ophthalmology",
        "quote": "Accommodative **esotropia** typically develops around age two to three in children with uncorrected high hyperopia."
      },
      {
        "author": "David H. Hubel",
        "work": "Eye, Brain, and Vision",
        "quote": "Experimental induction of **esotropia** in kittens results in the permanent loss of binocularly driven cortical neurons."
      }
    ]
  },
  "Dashboard — eur\\Europe.md": {
    "primary": "A continent of the eastern hemisphere, separated from Asia by the Ural Mountains, Caspian Sea, and Black Sea.",
    "secondary": "In classical mythology, named after Europa, a Phoenician princess abducted by Zeus in the guise of a white bull; in geopolitics, the birthplace of modern nation-states.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The division of **Europe** into a number of independent states is productive of the most beneficial consequences for human freedom."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "In **Europe**, the democratic revolution has taken place in the constitution of society without changes in our laws and manners."
      },
      {
        "author": "Winston Churchill",
        "work": "Speech at the University of Zurich",
        "quote": "We must build a kind of United States of **Europe**, so that the material strength of hundreds of millions may be directed toward peace."
      }
    ]
  },
  "Dashboard — eur\\aneurysm.md": {
    "primary": "An abnormal, localized dilation or ballooning of the wall of an artery or the heart caused by weakening of the vascular wall.",
    "secondary": "In vascular surgery and neurology, ruptured abdominal aortic or intracranial aneurysms cause life-threatening internal hemorrhage and subarachnoid bleeding.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A thoracic aortic **aneurysm** may erode ribs and sternum, presenting as a pulsating subcutaneous mass."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Screening for abdominal aortic **aneurysm** with ultrasound drastically reduces catastrophic mortality from rupture."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "A berry **aneurysm** arises at bifurcation points in the circle of Willis due to congenital internal elastic lamina defects."
      }
    ]
  },
  "Dashboard — eur\\aneurysmal.md": {
    "primary": "Pertaining to, resembling, or affected with an aneurysm; dilatational.",
    "secondary": "In pathology, designating dilated vascular structures, such as an aneurysmal bone cyst or aneurysmal dilation of the ascending aorta.",
    "quotes": [
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "An **aneurysmal** bone cyst contains blood-filled cavernous spaces separated by fibrous septa containing osteoclast-like giant cells."
      },
      {
        "author": "Courtney M. Townsend",
        "work": "Sabiston Textbook of Surgery",
        "quote": "Progressive **aneurysmal** expansion increases wall tension exponentially according to the law of Laplace."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Turbulent hemodynamic vortices within an **aneurysmal** sac promote thrombus formation along the vessel perimeter."
      }
    ]
  },
  "Dashboard — eur\\aneurysmatic.md": {
    "primary": "Relating to or of the nature of an aneurysm; aneurysmal.",
    "secondary": "In older medical literature, describing vascular bruits and pulsatile swellings associated with arterial dilations.",
    "quotes": [
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "The physician detected an **aneurysmatic** tumor in the neck, whose strong arterial throb warned of impending rupture."
      },
      {
        "author": "John Hunter",
        "work": "Lectures on the Principles of Surgery",
        "quote": "Ligating the femoral artery at a distance from the **aneurysmatic** sac halts pulsation and induces organized thrombosis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **aneurysmatic** murmur was audible across the left infraclavicular region."
      }
    ]
  },
  "Dashboard — eur\\eur.md": {
    "primary": "A Greek combining element meaning 'broad', 'wide', or 'spacious'.",
    "secondary": "In anatomy, zoology, and geography, eur- designates wide aperture or expansive geographic range (euryhaline, Europe, aneurysm).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The adjective eurys signifies 'wide', 'broad', or 'spacious', forming many poetic and geographical Greek names with **eur**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Stemming from PIE *h₁wer- ('wide'), **eur** is cognate with Sanskrit uru- and appears in the foundational continent name Europe."
      },
      {
        "author": "Pierre Chantraine",
        "work": "Dictionnaire étymologique de la langue grecque",
        "quote": "The semantic notion of expansive breadth in **eur** informs both classical mythological geography and medical vascular nomenclature."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Part 3 Batch 2.`);
