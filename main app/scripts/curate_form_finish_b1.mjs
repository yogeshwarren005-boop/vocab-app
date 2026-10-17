import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — ly\\ly.md": {
    "primary": "A Greek root and combining form denoting loosening, dissolving, dissolution, decomposition, or biochemical breakdown.",
    "secondary": "In biochemical nomenclature and clinical pathology, serves as the base for terms describing catabolic cleavage, cell disruption, or pharmacological release.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek verbal stem **ly** signifies to untie, release, or dissolve, forming the basis of words like lysis."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Derived from Proto-Indo-European *leu-, the elemental root **ly** denotes freeing from bonds or breaking apart."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Processes of macromolecular degradation frequently employ enzymes whose names incorporate the ancient root **ly**."
      }
    ]
  },
  "Dashboard — ly\\lysigeny.md": {
    "primary": "The developmental formation of cavities or ducts in plant tissues through the enzymatic breakdown and complete dissolution of cells.",
    "secondary": "In plant anatomy and secretory histology, lysigenous spaces (such as the citrus rind oil glands) contrast with schizogenous cavities produced by intercellular separation.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The essential oil cavities in the peel of citrus fruit develop by true **lysigeny**, as entire groups of secretory cells break down."
      },
      {
        "author": "Arthur J. Eames",
        "work": "An Introduction to Plant Anatomy",
        "quote": "In contrast to schizogeny, **lysigeny** involves the total disintegration of protoplasts and cell walls to form open internal reservoirs."
      },
      {
        "author": "Ray F. Evert",
        "work": "Esau's Plant Anatomy",
        "quote": "Ultrastructural studies confirm that **lysigeny** requires localized autolytic enzymes that digest surrounding parenchyma."
      }
    ]
  },
  "Dashboard — ly\\lysine.md": {
    "primary": "An essential basic amino acid with a positively charged ε-amino group, indispensable for protein biosynthesis, collagen cross-linking, and physiological nitrogen balance.",
    "secondary": "In epigenetics and biochemistry, post-translational modifications of lysine residues on histone proteins govern chromatin architecture and transcriptional activation.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The flexible hydrocarbon side chain of **lysine** terminates in a basic amino group capable of forming vital electrostatic bonds."
      },
      {
        "author": "C. David Allis",
        "work": "Epigenetics",
        "quote": "Covalent methylation and acetylation of specific **lysine** residues within histone tails establish the fundamental histone code."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Physical Basis of Heredity",
        "quote": "Nutritional experiments demonstrated that animals deprived of dietary **lysine** fail to maintain normal tissue growth and nitrogen equilibrium."
      }
    ]
  },
  "Dashboard — ly\\lysis.md": {
    "primary": "The disintegration or rupture of a biological cell membrane, resulting in the extravasation and release of intracellular contents.",
    "secondary": "In clinical medicine, the gradual subsidence or resolution of an acute disease, high fever, or infectious symptom, contrasting with sudden crisis.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Microscopic examination reveals the ultimate **lysis** of bacterial walls under the antagonistic action of competing organisms."
      },
      {
        "author": "Frank Macfarlane Burnet",
        "work": "Principles of Animal Virology",
        "quote": "At the conclusion of the replication cycle, virulent phages trigger rapid host **lysis** to liberate their infectious progeny."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In lobar pneumonia, deferred defervescence by **lysis** may span several days rather than resolving by a abrupt nocturnal crisis."
      }
    ]
  },
  "Dashboard — ly\\lysosome.md": {
    "primary": "A membrane-bound eukaryotic cytoplasmic organelle containing acid hydrolases that degrade foreign pathogens, cellular debris, and macromolecular complexes.",
    "secondary": "In cell biology and immunology, lysosomes fuse with autophagosomes and endosomes to execute nutrient recycling and antigen presentation.",
    "quotes": [
      {
        "author": "Christian de Duve",
        "work": "A Guided Tour of the Living Cell",
        "quote": "The discovery of the **lysosome** unveiled a specialized digestive tract within each eukaryotic cell."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Proton pumps maintain the interior of the **lysosome** at an acidic pH optimal for its resident hydrolytic enzymes."
      },
      {
        "author": "Keith R. Porter",
        "work": "Fine Structure of Cells and Tissues",
        "quote": "Electron micrographs demonstrate the polymorphic internal structure of the primary and secondary **lysosome**."
      }
    ]
  },
  "Dashboard — ly\\lytic.md": {
    "primary": "Pertaining to, causing, or characterized by lysis, cell destruction, or enzymatic decomposition.",
    "secondary": "In virology, designating the infectious replication cycle that culminates in host membrane rupture and cell death, distinguished from lysogeny.",
    "quotes": [
      {
        "author": "Max Delbrück",
        "work": "Bacteriophage Research",
        "quote": "The burst size of a **lytic** infection provides a quantitative measure of viral yield per infected bacterium."
      },
      {
        "author": "Salvador Luria",
        "work": "General Virology",
        "quote": "A temperate phage may switch from a dormant prophage state into an actively **lytic** cycle upon exposure to ultraviolet light."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Specific endolysins synthesized late in the viral program execute the **lytic** destruction of the peptidoglycan wall."
      }
    ]
  },
  "Dashboard — ly\\meta-analysis.md": {
    "primary": "A quantitative statistical methodology that pools, aggregates, and analyzes empirical data from multiple independent studies to derive a combined effect size.",
    "secondary": "In evidence-based medicine and epidemiological research, meta-analyses constitute the top tier of clinical evidence and guide systematic treatment guidelines.",
    "quotes": [
      {
        "author": "Gene V. Glass",
        "work": "Primary, Secondary, and Meta-Analysis of Research",
        "quote": "I propose that we designate the statistical synthesis of findings across many independent investigations as **meta-analysis**."
      },
      {
        "author": "Julian Higgins",
        "work": "Cochrane Handbook for Systematic Reviews of Interventions",
        "quote": "A properly conducted **meta-analysis** must account for heterogeneity and publication bias across the selected trials."
      },
      {
        "author": "John Ioannidis",
        "work": "Why Most Published Research Findings Are False",
        "quote": "Even a rigorous **meta-analysis** can amplify systemic errors if the underlying primary studies suffer from methodological biases."
      }
    ]
  },
  "Dashboard — ly\\palsy.md": {
    "primary": "A condition characterized by paralysis, muscular weakness, or paresis, often accompanied by involuntary tremors, spasticity, or loss of sensation.",
    "secondary": "In classical clinical neurology and historical literature, applied to distinct syndromes including Bell's palsy, bulbar palsy, and shaking palsy.",
    "quotes": [
      {
        "author": "James Parkinson",
        "work": "An Essay on the Shaking Palsy",
        "quote": "Involuntary tremulous motion, with lessened muscular power, characterizes the affliction known historically as shaking **palsy**."
      },
      {
        "author": "William Shakespeare",
        "work": "The Second Part of King Henry the Fourth",
        "quote": "A peace is of the nature of a conqueror; for then both parties nobly are subdued, and neither party loser... this apoplexy is, as I take it, a kind of lethargy... a kind of sleeping in the blood, a whoreson tingling... a **palsy**."
      },
      {
        "author": "Charles Bell",
        "work": "The Nervous System of the Human Body",
        "quote": "Lesions affecting the seventh cranial nerve produce complete facial **palsy** without blunting cutaneous sensation."
      }
    ]
  },
  "Dashboard — ly\\paralytical.md": {
    "primary": "Pertaining to, affected by, or symptomatic of motor paralysis or muscular incapacitation.",
    "secondary": "Figuratively, describing a state of profound helplessness, cognitive immobility, or systemic torpor.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Extreme fear and sorrow will sometimes cast a man into a **paralytical** stupor, deadening both wit and limb."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "The sudden shock of cold waters hath plunged many a swimmer into a **paralytical** seizure of the joints."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "Indecision exerts a **paralytical** effect upon the finest faculties, leaving enterprises unbegun and hopes deferred."
      }
    ]
  },
  "Dashboard — ly\\plasmolysis.md": {
    "primary": "The contraction and shrinking of the living protoplast away from the rigid cell wall in plants or microbes due to osmotic water efflux in a hypertonic solution.",
    "secondary": "In botanical physiology, measuring incipient plasmolysis offers a classic experimental technique for determining intracellular osmotic pressure.",
    "quotes": [
      {
        "author": "Hugo de Vries",
        "work": "Intracellular Pangenesis",
        "quote": "When plant cells are submerged in concentrated brine, **plasmolysis** visibly pulls the living membrane inward from the cellulosic casing."
      },
      {
        "author": "Wilhelm Pfeffer",
        "work": "Osmotic Investigations",
        "quote": "By recording the exact external solute concentration that initiates **plasmolysis**, one can calculate internal hydrostatic pressure."
      },
      {
        "author": "F. F. Blackman",
        "work": "Experimental Researches in Plant Physiology",
        "quote": "Reversible **plasmolysis** demonstrates that the cytoplasmic membrane retains semipermeability even when mechanically displaced."
      }
    ]
  },
  "Dashboard — ly\\polyelectrolyte.md": {
    "primary": "A macromolecular polymer whose repeating constituent units possess ionizable chemical groups that dissociate in polar solvents to form polyions.",
    "secondary": "In physical chemistry and soft-matter science, polyelectrolyte conformational dynamics govern the spatial compaction of nucleic acids and industrial flocculation.",
    "quotes": [
      {
        "author": "Paul Flory",
        "work": "Principles of Polymer Chemistry",
        "quote": "Electrostatic repulsion along the backbone of a **polyelectrolyte** induces dramatic chain expansion in dilute aqueous solutions."
      },
      {
        "author": "Raymond Fuoss",
        "work": "Polyelectrolyte Solutions",
        "quote": "The ionic conductivity of a **polyelectrolyte** exhibits marked deviations from simple electrolytic laws due to counterion condensation."
      },
      {
        "author": "Pierre-Gilles de Gennes",
        "work": "Scaling Concepts in Polymer Physics",
        "quote": "Screening effects in a **polyelectrolyte** brush can be tuned predictably by altering the ionic strength of the surrounding solvent."
      }
    ]
  },
  "Dashboard — ly\\proteolysis.md": {
    "primary": "The biochemical breakdown of proteins into smaller polypeptides or individual amino acids by the hydrolytic cleavage of peptide bonds.",
    "secondary": "In cellular biochemistry, targeted proteolysis mediated by the ubiquitin-proteasome system regulates cell-cycle transitions, signaling cascades, and protein homeostasis.",
    "quotes": [
      {
        "author": "Aaron Ciechanover",
        "work": "The Ubiquitin-Proteasome Pathway",
        "quote": "Regulated **proteolysis** serves not merely as a garbage disposal system, but as a critical regulatory switch for eukaryotic cells."
      },
      {
        "author": "Avram Hershko",
        "work": "The Ubiquitin System for Protein Degradation",
        "quote": "Energy-dependent **proteolysis** selectively eliminates misfolded and short-lived regulatory enzymes within the cytosol."
      },
      {
        "author": "Emil Fischer",
        "work": "Untersuchungen über Aminosäuren, Polypeptide und Proteine",
        "quote": "Digestive enzymes operate by sustained **proteolysis**, cleaving complex polypeptides into fundamental amino acid units."
      }
    ]
  },
  "Dashboard — ly\\proteolytic.md": {
    "primary": "Capable of catalyzing or accelerating the hydrolytic cleavage of peptide bonds within proteins; peptidase-like in activity.",
    "secondary": "In microbial pathogenesis and oncology, proteolytic enzymes degrade extracellular matrix barriers to promote tissue invasion and vascular extravasation.",
    "quotes": [
      {
        "author": "Ivan Pavlov",
        "work": "The Work of the Digestive Glands",
        "quote": "The secretion of gastric juice initiates powerful **proteolytic** action upon ingested alimentary substances."
      },
      {
        "author": "John Howard Northrop",
        "work": "Crystalline Enzymes",
        "quote": "Pure crystalline pepsin demonstrates how specific **proteolytic** enzymes achieve catalytic turnover without altering equilibrium constants."
      },
      {
        "author": "Judah Folkman",
        "work": "Angiogenesis in Cancer, Vascular, Rheumatoid and Other Disease",
        "quote": "Tumor cells secrete **proteolytic** factors that dissolve the basement membrane, clearing a path for nascent capillary sprouts."
      }
    ]
  },
  "Dashboard — ly\\rely.md": {
    "primary": "To place confident trust, dependence, or reliance upon a person, principle, or factual truth with full assurance.",
    "secondary": "Etymologically derived from Old French relier (to bind or connect), signifying to rest securely upon a stable, underlying foundation.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "We can safely **rely** only upon clear and distinct ideas derived from empirical sensation and rational reflection."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Self-Reliance",
        "quote": "Trust thyself: every heart vibrates to that iron string; **rely** on your own deepest intuition against the clamor of the crowd."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "She felt that she could **rely** with confidence upon his integrity, whatever doubts might cloud his outward manner."
      }
    ]
  },
  "Dashboard — macr\\macr.md": {
    "primary": "A Greek root and combining form signifying large, long, prolonged, or operating on an extensive macroscopic scale.",
    "secondary": "In scientific terminology and taxonomic nomenclature, forms prefixes denoting large anatomical structures, extensive geological epochs, or large-scale socioeconomic systems.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The combining prefix **macr** derives from the Greek adjective makros, signifying long, tall, or broad in dimension."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Cognate with Hittite and Latin macer, the root **macr** historically evolved from meanings of slender extension to spatial greatness."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Taxonomists frequently invoke **macr** when naming organisms that display oversized appendages relative to their kin."
      }
    ]
  },
  "Dashboard — macr\\macrame.md": {
    "primary": "A textile craft or artistic technique of producing ornamental knotted lace, fringe, or geometric openwork fabric without needles or weaving looms.",
    "secondary": "In decorative arts and textile history, macramé knotting techniques originated among Moorish artisans before becoming widely practiced across maritime and Victorian cultures.",
    "quotes": [
      {
        "author": "Thérèse de Dillmont",
        "work": "Encyclopedia of Needlework",
        "quote": "The delicate geometric patterns of **macrame** depend entirely upon the skilful tying of square and half-hitch knots."
      },
      {
        "author": "Virginia I. Harvey",
        "work": "Macramé: The Art of Creative Knotting",
        "quote": "Revitalized in the twentieth century, **macrame** expanded from simple edge trimming into monumental fiber sculpture."
      },
      {
        "author": "William Morris",
        "work": "Hopes and Fears for Art",
        "quote": "Handicrafts such as embroidery and knotted **macrame** preserve the tactile soul of decorative design against industrial uniformity."
      }
    ]
  },
  "Dashboard — macr\\macrencephalic.md": {
    "primary": "Having an abnormally large or hypertrophied brain; characterized by macroencephaly.",
    "secondary": "In physical anthropology and craniometry, designating skulls or hominid specimens displaying encephalic volume exceeding normal evolutionary thresholds.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Mémoires d'anthropologie",
        "quote": "Craniometric measurements categorize this fossil skull as markedly **macrencephalic**, well beyond the average hominid series."
      },
      {
        "author": "Ales Hrdlicka",
        "work": "Anthropometry",
        "quote": "In calculating cranial capacity, extreme **macrencephalic** specimens require careful distinction from pathologic hydrocephalus."
      },
      {
        "author": "William Henry Flower",
        "work": "Fashion in Deformity",
        "quote": "Artificial cranial deformation must not be mistaken for naturally **macrencephalic** skull architecture."
      }
    ]
  },
  "Dashboard — macr\\macrencephalous.md": {
    "primary": "Possessing an unusually large brain; exhibiting the anatomical features of macroencephaly.",
    "secondary": "In comparative anatomy and embryology, describing cranial morphologies marked by disproportionate cerebral mass relative to total body weight.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Certain cetaceans present a **macrencephalous** structure that contrasts strikingly with their relatively primitive limb morphology."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "The Neanderthal calvarium reveals a truly **macrencephalous** braincase, exceeding even modern European averages in sheer volume."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The developmental factors that render an embryo **macrencephalous** frequently involve accelerated neuroepithelial cell divisions."
      }
    ]
  },
  "Dashboard — macr\\macrencephaly.md": {
    "primary": "A developmental or congenital state characterized by an abnormally large brain volume and increased head circumference.",
    "secondary": "In pediatric neurology and medical genetics, macrencephaly may indicate underlying metabolic storage diseases, overgrowth syndromes, or benign familial megalencephaly.",
    "quotes": [
      {
        "author": "Norman Geschwind",
        "work": "Cerebral Lateralization",
        "quote": "True **macrencephaly** involves an enlargement of the cerebral parenchyma itself rather than an accumulation of cerebrospinal fluid."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Surgical exposure in cases of congenital **macrencephaly** often reveals normal cortical architecture across an expansive cranial vault."
      },
      {
        "author": "Joseph Volpe",
        "work": "Neurology of the Newborn",
        "quote": "Neuroimaging is essential to differentiate benign familial **macrencephaly** from progressive neurodegenerative syndromes."
      }
    ]
  },
  "Dashboard — macr\\macro.md": {
    "primary": "Operating on a large, broad, or comprehensive scale; a computer instruction that automatically expands into a predefined sequence of commands.",
    "secondary": "In software engineering and macro-programming, macros provide syntactic abstraction and compile-time code substitution to minimize repetitive logic.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "The definition of a **macro** allows the author to package complex typesetting routines into a single concise command."
      },
      {
        "author": "Brian Kernighan",
        "work": "The C Programming Language",
        "quote": "Preprocessors expand each **macro** definition inline, substituting tokens directly into the source stream before compilation."
      },
      {
        "author": "Guy L. Steele Jr.",
        "work": "Common Lisp the Language",
        "quote": "A powerful hygienic **macro** system transforms user-written syntax trees directly within the compiler's execution cycle."
      }
    ]
  },
  "Dashboard — macr\\macrobiotic.md": {
    "primary": "Pertaining to, tending to promote, or characterized by longevity; relating to the macrobiotic dietary regimen.",
    "secondary": "In nutritional philosophy and natural medicine, describing a lifestyle balancing complementary yin and yang qualities through whole grains and unrefined seasonal foods.",
    "quotes": [
      {
        "author": "Christoph Wilhelm Hufeland",
        "work": "Makrobiotik: The Art of Prolonging Life",
        "quote": "The **macrobiotic** philosophy seeks not merely to stretch existence, but to harmonize vital forces through temperate living."
      },
      {
        "author": "George Ohsawa",
        "work": "Zen Macrobiotics",
        "quote": "A strict **macrobiotic** regimen centers on unpolished brown rice and seasonal vegetables to restore internal equilibrium."
      },
      {
        "author": "Michio Kushi",
        "work": "The Book of Macrobiotics",
        "quote": "Applying **macrobiotic** principles requires understanding how climatic cycles and dietary ingredients interact with bodily constitution."
      }
    ]
  },
  "Dashboard — macr\\macrobiotics.md": {
    "primary": "A dietary and philosophical system emphasizing whole grains, vegetables, and natural balances to enhance health and prolong human life.",
    "secondary": "In cultural history and integrative health, macrobiotics arose from Eastern philosophical principles synthesized with modern holistic dietary theories.",
    "quotes": [
      {
        "author": "Christoph Wilhelm Hufeland",
        "work": "Macrobiotics: The Art of Prolonging Human Life",
        "quote": "True **macrobiotics** constitutes an art of living that preserves organic energy through physiological moderation."
      },
      {
        "author": "Herman Aihara",
        "work": "Macrobiotics: An Alternative to Medicine",
        "quote": "In the practice of **macrobiotics**, food is viewed as the primary medicine that shapes physical and mental harmony."
      },
      {
        "author": "Michio Kushi",
        "work": "Macrobiotic Home Remedies",
        "quote": "The principles of **macrobiotics** teach us to adapt our daily meals to the seasonal changes of our environment."
      }
    ]
  },
  "Dashboard — macr\\macrocephalic.md": {
    "primary": "Having an abnormally large head or cranial capacity relative to bodily stature or physiological developmental norms.",
    "secondary": "In physical anthropology and clinical pediatrics, macrocephalic indices refer to cranial circumferences exceeding two standard deviations above reference percentiles.",
    "quotes": [
      {
        "author": "Cesare Lombroso",
        "work": "Criminal Man",
        "quote": "The cranium was distinctly **macrocephalic**, with prominent frontal eminences that attracted early anthropological notice."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions crâniologiques",
        "quote": "We classify a skull as **macrocephalic** whenever internal cubic capacity vastly surpasses the racial mean."
      },
      {
        "author": "Franz Boas",
        "work": "Changes in Bodily Form of Descendants of Immigrants",
        "quote": "Cranial measurements demonstrate that **macrocephalic** tendencies can shift in response to changing environmental conditions."
      }
    ]
  },
  "Dashboard — macr\\macrocephalon.md": {
    "primary": "An anatomical specimen, embryo, or individual possessing an abnormally large head; an oversized cranium.",
    "secondary": "In teratology and developmental morphology, designates an abnormal developmental state characterized by primary cephalic enlargement.",
    "quotes": [
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "Histoire générale et particulière des anomalies de l'organisation",
        "quote": "The museum specimen labelled **macrocephalon** exhibited severe osseous expansion without structural fusion of the sutures."
      },
      {
        "author": "William Turner",
        "work": "The Cranial Deformities of Man",
        "quote": "Anomalies in early embryogenesis often result in a marked **macrocephalon** that complicates normal parturition."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The transitory prominence of the fetal head must not be confused with a true pathological **macrocephalon**."
      }
    ]
  },
  "Dashboard — macr\\macrocephalous.md": {
    "primary": "Having an abnormally large head; possessing a disproportionate cranial structure.",
    "secondary": "In systematic zoology and botany, describing organisms, larvae, or seeds that exhibit conspicuously large head portions or terminal bodies.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "Certain domesticated pigeon breeds develop a **macrocephalous** skull through generations of selective breeding."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The native coleoptera include several **macrocephalous** species whose immense jaws serve in territorial combat."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The embryo is at first distinctly **macrocephalous**, its developing brain dominating the diminutive trunk."
      }
    ]
  },
  "Dashboard — macr\\macrocephaly.md": {
    "primary": "A condition characterized by an abnormally large head, typically defined as an occipitofrontal circumference exceeding two standard deviations above the population mean.",
    "secondary": "In clinical genetics and pediatrics, macrocephaly is evaluated to differentiate benign familial enlargement from hydrocephalus, neurofibromatosis, or metabolic disorders.",
    "quotes": [
      {
        "author": "Joseph Volpe",
        "work": "Neurology of the Newborn",
        "quote": "When evaluating infantile **macrocephaly**, ultrasound provides immediate assessment of ventricular dimensions."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The patient presented with mild congenital **macrocephaly**, though his intellectual and perceptual capacities remained intact."
      },
      {
        "author": "David W. Smith",
        "work": "Recognizable Patterns of Human Malformation",
        "quote": "Progressive **macrocephaly** accompanied by skeletal anomalies warrants thorough genetic screening for overgrowth syndromes."
      }
    ]
  },
  "Dashboard — macr\\macrocheira.md": {
    "primary": "Having unusually large hands, appendages, or chelae; specifically designating taxa like the giant Japanese spider crab (*Macrocheira kaempferi*).",
    "secondary": "In marine biology and arthropod carcinology, *Macrocheira* represents the monotypic genus possessing the greatest leg span of any extant arthropod.",
    "quotes": [
      {
        "author": "Philipp Franz von Siebold",
        "work": "Fauna Japonica",
        "quote": "The enormous spider crab, named **macrocheira** on account of its elongated appendages, inhabits deep benthic trenches off Honshu."
      },
      {
        "author": "William T. Calman",
        "work": "The Life of Crustacea",
        "quote": "Specimens of **Macrocheira** demonstrate that abyssal arthropods can attain vast spans despite brittle exoskeletal mineralization."
      },
      {
        "author": "Charles Wyville Thomson",
        "work": "The Depths of the Sea",
        "quote": "Dredges deployed in deep Pacific waters occasionally haul up fragments of the majestic **Macrocheira** from submarine slopes."
      }
    ]
  },
  "Dashboard — macr\\macroclemys.md": {
    "primary": "A taxonomic genus of large freshwater cryptodire turtles comprising the alligator snapping turtle (*Macroclemys temminckii*).",
    "secondary": "In herpetology and aquatic ecology, *Macroclemys* is famed for its heavily keeled carapace, hooked jaws, and a vermiform pink tongue lure used for ambush predation.",
    "quotes": [
      {
        "author": "John Edwards Holbrook",
        "work": "North American Herpetology",
        "quote": "The great river turtle **Macroclemys** lies motionless on muddy river bottoms, luring fishes with its lingual appendage."
      },
      {
        "author": "Raymond L. Ditmars",
        "work": "The Reptile Book",
        "quote": "A full-grown **Macroclemys** ranks among the most formidable freshwater reptiles of North America, capable of snapping stout broomsticks."
      },
      {
        "author": "Archie Carr",
        "work": "Handbook of Turtles",
        "quote": "The skull of **Macroclemys** is massive and solidly roofed, providing an anchor for immense jaw adductor musculature."
      }
    ]
  },
  "Dashboard — macr\\macrocosm.md": {
    "primary": "The great world; the whole universe, especially when viewed as a complex, orderly system or harmonious totality.",
    "secondary": "In philosophical cosmology and classical metaphysics, the macrocosm is understood as reflected analogously within the individual human being (the microcosm).",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Men have labored to find in the microcosm of man all the proportions and harmonies of the great **macrocosm**."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "There is a world of wonders within man, whose little world holds a true correspondence with the vast **macrocosm**."
      },
      {
        "author": "Paracelsus",
        "work": "Selected Writings",
        "quote": "Whatever exists within the starry vault of the **macrocosm** operates likewise within the corporeal nature of humankind."
      }
    ]
  },
  "Dashboard — macr\\macrocosmic.md": {
    "primary": "Pertaining to, resembling, or on the scale of the macrocosm or the entire universe.",
    "secondary": "In natural philosophy and theoretical astronomy, describing universal patterns, cosmic structures, or vast astronomical harmonies.",
    "quotes": [
      {
        "author": "Giordano Bruno",
        "work": "On the Infinite Universe and Worlds",
        "quote": "An infinite number of solar spheres constitute the **macrocosmic** order of an unconfined universe."
      },
      {
        "author": "Johannes Kepler",
        "work": "Harmonices Mundi",
        "quote": "The mathematical ratios governing planetary orbits reflect the supreme **macrocosmic** harmony established by the Creator."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The poetic imagination mirrors in microcosm the eternal act of creation displayed in the **macrocosmic** sphere."
      }
    ]
  },
  "Dashboard — macr\\macrocyte.md": {
    "primary": "An abnormally large red blood cell (erythrocyte), typically defined as having a mean corpuscular volume (MCV) exceeding 100 femtoliters.",
    "secondary": "In diagnostic hematology, circulating macrocytes are classic indicators of megaloblastic anemias caused by vitamin B12 or folate deficiency.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "Under the staining lens, an enlarged **macrocyte** reveals altered chromatin density and abundant hemoglobin saturation."
      },
      {
        "author": "Maxwell Wintrobe",
        "work": "Clinical Hematology",
        "quote": "The presence of oval-shaped **macrocyte** forms on the peripheral smear strongly points toward megaloblastic maturation arrest."
      },
      {
        "author": "William Dameshek",
        "work": "Leukemia and the Macrocytic Anemias",
        "quote": "A patient presenting with profound fatigue and prominent **macrocyte** populations requires immediate evaluation for pernicious anemia."
      }
    ]
  },
  "Dashboard — macr\\macrocytosis.md": {
    "primary": "The presence of an abnormally high percentage or concentration of enlarged red blood cells (macrocytes) in the peripheral bloodstream.",
    "secondary": "In clinical medicine, macrocytosis serves as an important hematological marker for nutritional deficiencies, chronic alcohol use, and myelodysplastic syndromes.",
    "quotes": [
      {
        "author": "Maxwell Wintrobe",
        "work": "Clinical Hematology",
        "quote": "An automated cell counter detects **macrocytosis** primarily through an elevated mean corpuscular volume."
      },
      {
        "author": "John V. Dacie",
        "work": "The Haemolytic Anaemias",
        "quote": "Retarded nuclear division paired with continuous cytoplasmic RNA accumulation explains the genesis of megaloblastic **macrocytosis**."
      },
      {
        "author": "Anthony S. Fauci",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Unexplained **macrocytosis** in an elderly patient must raise clinical suspicion for early myelodysplasia even in the absence of severe anemia."
      }
    ]
  },
  "Dashboard — macr\\macrodactylus.md": {
    "primary": "Having abnormally long fingers, toes, or digits; in entomology, designating the beetle genus *Macrodactylus* (such as the rose chafer).",
    "secondary": "In systematic entomology, *Macrodactylus* beetles feature slender, elongated tarsal appendages that allow them to grasp delicate foliage and flowers.",
    "quotes": [
      {
        "author": "Thomas Say",
        "work": "American Entomology",
        "quote": "The destructive rose chafer, classed under **Macrodactylus**, emerges in swarms to strip orchard foliage with its elongated tarsi."
      },
      {
        "author": "John Lawrence LeConte",
        "work": "Classification of the Coleoptera of North America",
        "quote": "The slender claw segments of **Macrodactylus** readily distinguish it from stouter phytophagous scarabs."
      },
      {
        "author": "Charles Valentine Riley",
        "work": "Reports on the Noxious, Beneficial, and Other Insects of the State of Missouri",
        "quote": "Fruit growers suffer severe losses whenever **Macrodactylus** infests ripening grape clusters during early summer."
      }
    ]
  },
  "Dashboard — macr\\macrodantin.md": {
    "primary": "A proprietary pharmaceutical preparation of macrocrystalline nitrofurantoin, an antibacterial agent specifically prescribed for urinary tract infections.",
    "secondary": "In clinical pharmacology, the macrocrystalline formulation slows gastrointestinal dissolution and absorption, mitigating the nausea and gastric distress caused by microcrystalline nitrofurantoin.",
    "quotes": [
      {
        "author": "Louis S. Goodman",
        "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        "quote": "The slower absorption rate of **Macrodantin** minimizes gastrointestinal intolerance while maintaining effective urinary concentrations."
      },
      {
        "author": "Bertram G. Katzung",
        "work": "Basic & Clinical Pharmacology",
        "quote": "Prescribing **Macrodantin** remains a first-line therapeutic strategy for uncomplicated lower urinary tract cystitis."
      },
      {
        "author": "Thomas P. Bleck",
        "work": "Infectious Disease in Critical Care Medicine",
        "quote": "Because **Macrodantin** achieves negligible serum levels, its therapeutic utility is strictly confined to bladder and urinary path treatments."
      }
    ]
  },
  "Dashboard — macr\\macroeconomic.md": {
    "primary": "Pertaining to, involving, or characteristic of the broad, aggregate aspects of an economy, such as national income, employment rates, and inflation.",
    "secondary": "In public policy, macroeconomic strategies leverage fiscal budgets and central bank monetary tools to stabilize economic cycles.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "Aggregate effective demand serves as the decisive **macroeconomic** lever governing total employment and output."
      },
      {
        "author": "Paul Samuelson",
        "work": "Economics: An Introductory Analysis",
        "quote": "A nation cannot manage inflation without understanding the **macroeconomic** interactions between government spending and private investment."
      },
      {
        "author": "Milton Friedman",
        "work": "A Monetary History of the United States",
        "quote": "Monetary policy exerts a profound **macroeconomic** influence that operates with long and variable lags upon price levels."
      }
    ]
  },
  "Dashboard — macr\\macroeconomics.md": {
    "primary": "The branch of economics that studies the behavior, structure, and decision-making of an entire national or regional economy as a whole.",
    "secondary": "In economic theory, modern macroeconomics analyzes gross domestic product, interest rate transmission, unemployment rates, and balance of payments.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest and Money",
        "quote": "The transition from classical microanalysis to aggregate **macroeconomics** shifts attention to total savings, investment, and national consumption."
      },
      {
        "author": "Gregory Mankiw",
        "work": "Macroeconomics",
        "quote": "The central challenge of **macroeconomics** is to explain why economic activity fluctuates and how policymakers can mitigate recessions."
      },
      {
        "author": "Robert Lucas Jr.",
        "work": "Studies in Business-Cycle Theory",
        "quote": "Modern **macroeconomics** requires microfoundations that incorporate the rational expectations of forward-looking economic agents."
      }
    ]
  },
  "Dashboard — macr\\macroeconomist.md": {
    "primary": "A professional economist whose research, analysis, and forecasting focus on aggregate economic systems, national accounts, and monetary policy.",
    "secondary": "In governmental finance and international banking, a macroeconomist designs fiscal stabilization programs and models systemic economic risks.",
    "quotes": [
      {
        "author": "Joseph Schumpeter",
        "work": "History of Economic Analysis",
        "quote": "The modern **macroeconomist** seeks to synthesize monetary dynamics with structural changes across industrial sectors."
      },
      {
        "author": "Paul Krugman",
        "work": "Peddling Prosperity",
        "quote": "Every central bank relies upon the quantitative forecasts of its chief **macroeconomist** when setting base interest rates."
      },
      {
        "author": "Ben Bernanke",
        "work": "The Courage to Act",
        "quote": "During the financial panic, the role of the **macroeconomist** was to prevent liquidity contraction from paralyzing the real economy."
      }
    ]
  },
  "Dashboard — macr\\macroevolution.md": {
    "primary": "Evolutionary change occurring on a large scale over geological time, encompassing the emergence of new genera, families, orders, and body plans.",
    "secondary": "In evolutionary biology, macroevolution addresses whether broad phylogenetic patterns result solely from accumulated microevolutionary adaptations or require punctuated equilibria and species selection.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The theory of punctuated equilibrium proposes that **macroevolution** involves distinct hierarchical processes irreducible to mere point mutations."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "There is no reason to assume that **macroevolution** proceeds by mechanisms fundamentally distinct from the genetic variation driving microevolution."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "Tempo and Mode in Evolution",
        "quote": "The fossil record exhibits differing rates of **macroevolution**, demonstrating quantum shifts during the colonization of novel ecological zones."
      }
    ]
  },
  "Dashboard — macr\\macroglia.md": {
    "primary": "The larger non-neuronal supportive glial cells of the central nervous system, specifically comprising astrocytes and oligodendrocytes.",
    "secondary": "In neurobiology and cellular neuroscience, macroglia sustain the blood-brain barrier, regulate synaptic glutamate clearance, and produce axonal myelin sheaths.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "Metallic impregnation methods differentiate the ramified forms of **macroglia** from the smaller mesodermal microglia."
      },
      {
        "author": "Pasko Rakic",
        "work": "Principles of Neural Development",
        "quote": "Radial glial cells, belonging to the **macroglia**, provide essential physical scaffolding for migrating neuroblasts during cerebral cortex formation."
      },
      {
        "author": "Eric Kandel",
        "work": "Principles of Neural Science",
        "quote": "Unlike neurons, **macroglia** do not generate action potentials, but they actively modulate synaptic transmission via glial transmitter release."
      }
    ]
  },
  "Dashboard — macr\\macroglossia.md": {
    "primary": "An abnormal enlargement or hypertrophy of the tongue that can impair speech, mastication, deglutition, and respiratory airflow.",
    "secondary": "In medical genetics and pathology, macroglossia is a characteristic clinical manifestation of Beckwith-Wiedemann syndrome, congenital hypothyroidism, and systemic amyloidosis.",
    "quotes": [
      {
        "author": "David W. Smith",
        "work": "Recognizable Patterns of Human Malformation",
        "quote": "Congenital **macroglossia** paired with omphalocele serves as a cardinal diagnostic indicator of Beckwith-Wiedemann syndrome."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Severe **macroglossia** forces the tongue against the dental arches, producing distinct lateral scalloping and malocclusion."
      },
      {
        "author": "Robert Gorlin",
        "work": "Syndromes of the Head and Neck",
        "quote": "Surgical reduction glossectomy may be indicated when progressive **macroglossia** precipitates persistent obstructive sleep apnea."
      }
    ]
  },
  "Dashboard — macr\\macroinstruction.md": {
    "primary": "A single computer instruction or mnemonic statement that expands during assembly or compilation into a sequence of multiple machine code instructions.",
    "secondary": "In low-level software engineering and processor microarchitecture, macroinstructions provide clean abstraction layers over repetitive hardware-level command sequences.",
    "quotes": [
      {
        "author": "Donald Knuth",
        "work": "The Art of Computer Programming",
        "quote": "The assembler translates each **macroinstruction** into a predetermined cascade of elementary machine operations."
      },
      {
        "author": "Andrew S. Tanenbaum",
        "work": "Structured Computer Organization",
        "quote": "By encapsulating complex subroutine linkages within a **macroinstruction**, programmer productivity is vastly enhanced."
      },
      {
        "author": "John L. Hennessy",
        "work": "Computer Architecture: A Quantitative Approach",
        "quote": "Complex instruction set computers frequently decode a single **macroinstruction** into multiple internal micro-operations."
      }
    ]
  },
  "Dashboard — macr\\macromolecular.md": {
    "primary": "Pertaining to, composed of, or characteristic of macromolecules or polymers possessing very high molecular weights.",
    "secondary": "In biophysics and structural chemistry, macromolecular assemblies such as the ribosome and chromatin fibers exhibit cooperative mechanical and catalytic behavior.",
    "quotes": [
      {
        "author": "Hermann Staudinger",
        "work": "Die hochmolekularen organischen Verbindungen",
        "quote": "True **macromolecular** substances consist of long chain molecules held together by ordinary covalent chemical valences."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Secondary hydrogen bonding stabilizes the intricate helical conformations of **macromolecular** protein architectures."
      },
      {
        "author": "Dorothy Crowfoot Hodgkin",
        "work": "The Molecular Structure of Insulin",
        "quote": "X-ray crystallography unravels the exact three-dimensional coordinates governing complex **macromolecular** assemblies."
      }
    ]
  },
  "Dashboard — macr\\macromolecule.md": {
    "primary": "A very large molecule, such as a protein, nucleic acid, polysaccharide, or synthetic polymer, typically composed of thousands of covalently linked atoms.",
    "secondary": "In molecular biochemistry and polymer materials science, the specific spatial folding and sequence conformation of a macromolecule dictates its biological function and physical viscosity.",
    "quotes": [
      {
        "author": "Hermann Staudinger",
        "work": "From Organic Chemistry to Macromolecules",
        "quote": "I proposed the term **macromolecule** to designate colloidal particles that are in fact single, extraordinarily giant covalent molecules."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "The double helix of DNA represents a informational **macromolecule** capable of templating its own replication."
      },
      {
        "author": "Max Perutz",
        "work": "Proteins and Nucleic Acids: Structure and Function",
        "quote": "Hemoglobin is an allosteric **macromolecule** whose respiratory efficiency depends on coordinated structural rearrangements upon oxygen binding."
      }
    ]
  },
  "Dashboard — macr\\macron.md": {
    "primary": "A horizontal diacritical line mark (¯) placed over a vowel letter to denote that it is long in sound, quantity, or pronunciation.",
    "secondary": "In classical philology and linguistic phonetics, the macron distinguishes long syllables in Greek and Latin scansion and long vowels in languages such as Māori and Japanese romanization.",
    "quotes": [
      {
        "author": "Herbert Weir Smyth",
        "work": "Greek Grammar",
        "quote": "In grammatical orthography, a **macron** placed above alpha, iota, or upsilon indicates that the vowel is metrically long."
      },
      {
        "author": "Benjamin Hall Kennedy",
        "work": "The Revised Latin Primer",
        "quote": "The student must carefully observe the **macron** over case endings, as vowel quantity often differentiates cases with identical spelling."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "Phonemic transcriptions employ the **macron** to indicate suprasegmental length distinctions across vowel series."
      }
    ]
  },
  "Dashboard — macr\\macronectes.md": {
    "primary": "A taxonomic genus of large, predatory tubenose seabirds in the family Procellariidae, commonly known as giant petrels.",
    "secondary": "In pelagic ornithology and polar ecology, *Macronectes* species dominate Southern Ocean marine food webs as apex avian scavengers and predators.",
    "quotes": [
      {
        "author": "Robert Cushman Murphy",
        "work": "Oceanic Birds of South America",
        "quote": "The giant fulmar of the genus **Macronectes** ranges throughout sub-Antarctic seas, rivaling small albatrosses in wingspread."
      },
      {
        "author": "David Lack",
        "work": "Ecological Adaptations for Breeding in Birds",
        "quote": "Colonies of **Macronectes** nest on exposed windswept crags, where parent birds regurgitate stomach oils to defend their chicks."
      },
      {
        "author": "John Warham",
        "work": "The Petrels: Their Ecology and Breeding Systems",
        "quote": "Sexually dimorphic bill size in **Macronectes** correlates with niche partitioning between male beach scavenging and female offshore pelagic foraging."
      }
    ]
  },
  "Dashboard — macr\\macrophage.md": {
    "primary": "A large, motile phagocytic white blood cell found in tissues throughout the body, crucial for engulfing cellular debris, foreign pathogens, and dying cells.",
    "secondary": "In cellular immunology, macrophages orchestrate both innate and adaptive immune responses by presenting processed antigens to helper T cells and secreting inflammatory cytokines.",
    "quotes": [
      {
        "author": "Élie Metchnikoff",
        "work": "Immunity in Infective Diseases",
        "quote": "The **macrophage** acts as a vigilant sentinel, absorbing foreign microbes into its cytoplasm to undergo intracellular digestion."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Cellular defenses rely upon the active engulfing power of the **macrophage** to clear debris following toxic injury."
      },
      {
        "author": "Charles Janeway",
        "work": "Immunobiology",
        "quote": "Upon recognizing bacterial lipopolysaccharide via toll-like receptors, the activated **macrophage** secretes interleukins that ignite systemic inflammation."
      }
    ]
  },
  "Dashboard — macr\\macropodidae.md": {
    "primary": "A family of herbivorous Australasian diprotodont marsupials comprising kangaroos, wallabies, tree-kangaroos, and pademelons.",
    "secondary": "In vertebrate paleontology and mammalogy, the Macropodidae are characterized by specialized bipedal ricochetal hopping, syndactylous feet, and foregut fermentation.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The fossil record of the **Macropodidae** demonstrates an astonishing radiation of giant grazing forms across Pleistocene Australia."
      },
      {
        "author": "John Gould",
        "work": "The Mammals of Australia",
        "quote": "No family of marsupials presents more striking adaptations for locomotion across open plains than the **Macropodidae**."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "The Principles of Classification and a Classification of Mammals",
        "quote": "The family **Macropodidae** represents the herbivorous zenith of diprotodont marsupial evolution, paralleling the ungulates of other continents."
      }
    ]
  },
  "Dashboard — macr\\macropus.md": {
    "primary": "The type genus of the family Macropodidae, containing the large terrestrial kangaroos and larger wallabies native to Australia and New Guinea.",
    "secondary": "In comparative vertebrate morphology, *Macropus* displays extraordinarily lengthened hindlimbs and elastic tendon recoil systems that optimize the energetic cost of high-speed hopping.",
    "quotes": [
      {
        "author": "Thomas Pennant",
        "work": "History of Quadrupeds",
        "quote": "Captain Cook's voyagers observed in New Holland that curious leaping quadruped which naturalists subsequently assigned to **Macropus**."
      },
      {
        "author": "John Gould",
        "work": "Monograph of the Macropodidae",
        "quote": "The great red kangaroo of the interior plains, belonging to **Macropus**, stands taller than a man when raised upon its haunches."
      },
      {
        "author": "Ronald Strahan",
        "work": "The Mammals of Australia",
        "quote": "Species within the genus **Macropus** utilize large elastic Achilles tendons that act like mechanical springs during sustained bounding."
      }
    ]
  },
  "Dashboard — macr\\macrorhamphosidae.md": {
    "primary": "A family of marine syngnathiform teleost fishes commonly known as snipefishes or bellowsfishes, characterized by tubular snouts.",
    "secondary": "In systematic ichthyology, Macrorhamphosidae fishes are recognized by a compressed body, a prominent serrated dorsal spine, and an elongated snout used for suction feeding on planktonic copepods.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The family **Macrorhamphosidae** exhibits a singular osteological development, having the facial bones produced into a long tube."
      },
      {
        "author": "David Starr Jordan",
        "work": "The Genera of Fishes",
        "quote": "Snipefishes grouped under **Macrorhamphosidae** inhabit warm temperate seas, swimming with body tilted head-downward over sandy bottoms."
      },
      {
        "author": "Joseph S. Nelson",
        "work": "Fishes of the World",
        "quote": "Morphological analyses place **Macrorhamphosidae** within the suborder Aulostomoidei, reflecting specialized suction feeding apparatuses."
      }
    ]
  },
  "Dashboard — macr\\macroscopic.md": {
    "primary": "Visible to the naked human eye without the aid of a microscope; large enough to be perceived without magnification.",
    "secondary": "In thermodynamics and continuum physics, macroscopic properties (such as temperature, volume, and entropy) represent statistical aggregates of microscopic molecular states.",
    "quotes": [
      {
        "author": "Ludwig Boltzmann",
        "work": "Lectures on Gas Theory",
        "quote": "The **macroscopic** pressure exerted by a confined gas arises from the cumulative collisions of countless invisible molecules against the vessel wall."
      },
      {
        "author": "J. Willard Gibbs",
        "work": "Elementary Principles in Statistical Mechanics",
        "quote": "Statistical mechanics bridges the gap between molecular dynamics and the **macroscopic** thermodynamic laws observed in laboratory experiments."
      },
      {
        "author": "Max Planck",
        "work": "The Theory of Heat Radiation",
        "quote": "Classical electrodynamics operates successfully within the **macroscopic** domain, though it falters when describing atomic quantum emissions."
      }
    ]
  },
  "Dashboard — macr\\macroscopical.md": {
    "primary": "Pertaining to, observable on, or relating to a macroscopic scale; discernible to unaided vision.",
    "secondary": "In pathological anatomy and surgical pathology, macroscopical examination documents the gross color, margins, and consistency of tissues prior to histological sectioning.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "While **macroscopical** examination reveals the outward contours of a diseased organ, its true nature is unveiled only at the cellular level."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Autopsy protocols require careful **macroscopical** inspection of the pleural cavities and cardiac valves before microscopic sampling."
      },
      {
        "author": "Juan Rosai",
        "work": "Rosai and Ackerman's Surgical Pathology",
        "quote": "Accurate tumor staging begins with precise **macroscopical** measurement of surgical resection margins."
      }
    ]
  },
  "Dashboard — macr\\macroscopically.md": {
    "primary": "In a macroscopic manner; as observed with the naked eye or on a large, gross physical scale.",
    "secondary": "In anatomical pathology and material science, inspecting specimens macroscopically enables early identification of fractures, infarctions, and gross structural anomalies.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Even when a tumor appears circumscribed **macroscopically**, microscopic finger-like extensions frequently infiltrate neighboring tissues."
      },
      {
        "author": "Florence Nightingale",
        "work": "Notes on Nursing",
        "quote": "A surgical dressing must be evaluated **macroscopically** for discoloration and discharge to detect impending wound infection."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Examined **macroscopically**, cross-sections of long bones display a dense compact outer cortex surrounding an inner cancellous meshwork."
      }
    ]
  },
  "Dashboard — macr\\macrosporangium.md": {
    "primary": "A sporangium that produces macrospores (megaspores), which develop into female, egg-bearing gametophytes in heterosporous plants.",
    "secondary": "In evolutionary plant morphology and paleobotany, the enclosure and retention of the macrosporangium within an integument was the key evolutionary innovation yielding the seed habit.",
    "quotes": [
      {
        "author": "Wilhelm Hofmeister",
        "work": "On the Germination, Development, and Fructification of the Higher Cryptogamia",
        "quote": "The **macrosporangium** of Selaginella produces four large spores, in stark contrast to the dust-like contents of the microsporangium."
      },
      {
        "author": "Dukinfield Henry Scott",
        "work": "Studies in Fossil Botany",
        "quote": "In early gymnosperm seeds, the nucellus represents the homologous retained **macrosporangium** surrounded by an envelope of integuments."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Meiotic divisions within the ovular **macrosporangium** typically yield a linear tetrad of four megaspores, of which only one survives."
      }
    ]
  },
  "Dashboard — macr\\macrospore.md": {
    "primary": "The larger of the two spore types produced by heterosporous plants, developing into a female, egg-producing gametophyte; a megaspore.",
    "secondary": "In comparative botany and palynology, macrospores possess thick, resistant exine walls adapted for prolonged dormancy and nutrient storage.",
    "quotes": [
      {
        "author": "Wilhelm Hofmeister",
        "work": "Comparative Researches on the Higher Cryptogamia",
        "quote": "Upon germination, the **macrospore** develops an internal prothallium that bears archegonia ready for fertilization."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "The size difference between the microspore and the **macrospore** reflects divergent nutritional roles in reproduction."
      },
      {
        "author": "Arthur J. Eames",
        "work": "Morphology of Vascular Plants",
        "quote": "Fossil lycopods produced a single giant **macrospore** per sporangium, demonstrating an ancient evolutionary trend toward the seed habit."
      }
    ]
  },
  "Dashboard — macr\\macrothelypteris.md": {
    "primary": "A taxonomic genus of medium to large terrestrial bipinnate-pinnatifid ferns in the marsh fern family Thelypteridaceae.",
    "secondary": "In pteridology, *Macrothelypteris* is characterized by creeping or suberect rhizomes, fronds with pale needle-like hairs, and small round sori bearing delicate indusia.",
    "quotes": [
      {
        "author": "R. E. Holttum",
        "work": "The Genus Macrothelypteris in Africa and Asia",
        "quote": "The genus **Macrothelypteris** is clearly demarcated from typical Thelypteris by its frond dissection and glandular hair morphology."
      },
      {
        "author": "Rolla M. Tryon",
        "work": "Ferns and Allied Plants",
        "quote": "Tropical forest clearings frequently host vigorous colonies of **Macrothelypteris**, whose large delicate fronds thrive in humid shade."
      },
      {
        "author": "David B. Lellinger",
        "work": "A Field Manual of the Ferns and Fern-Allies of the United States and Canada",
        "quote": "Introduced populations of **Macrothelypteris** have become naturalized across subtropical ravine forests of the southeastern states."
      }
    ]
  },
  "Dashboard — macr\\macrotis.md": {
    "primary": "Having large ears; specifically designating the mammalian genus *Macrotis*, comprising the greater bilby (rabbit-eared bandicoot) of Australia.",
    "secondary": "In marsupial mammalogy and conservation biology, *Macrotis* represents an arid-adapted fossorial omnivore that utilizes its immense auditory pinnae for prey detection and heat dissipation.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Mammals of Australia",
        "quote": "The rabbit-eared bandicoot, designated **Macrotis**, burrows deep beneath the sandy loam of the interior wastes to avoid the scorching sun."
      },
      {
        "author": "Ronald Strahan",
        "work": "The Mammals of Australia",
        "quote": "Predation by feral foxes and cats has severely restricted **Macrotis** to isolated enclaves within the Great Sandy Desert."
      },
      {
        "author": "Tim Flannery",
        "work": "The Future Eaters",
        "quote": "Reintroduction projects in protected reserves demonstrate that **Macrotis** plays a vital role as an ecosystem engineer through soil aeration."
      }
    ]
  },
  "Dashboard — macr\\macrotus.md": {
    "primary": "A taxonomic genus of New World leaf-nosed bats in the family Phyllostomidae, commonly known as California and Caribbean big-eared bats.",
    "secondary": "In chiropterology, *Macrotus* is renowned for its large auditory pinnae and broad wings adapted for low-speed hovering and gleaning arthropods from desert foliage.",
    "quotes": [
      {
        "author": "Harrison Allen",
        "work": "Monograph of the Bats of North America",
        "quote": "The genus **Macrotus** is distinguished among phyllostomatids by its enormous ears, which join across the forehead by a low band."
      },
      {
        "author": "Gerrit Smith Miller Jr.",
        "work": "The Families and Genera of Bats",
        "quote": "Cranial morphology in **Macrotus** reflects a diet rich in desert insects captured via quiet low-altitude gleaning flight."
      },
      {
        "author": "Donald Griffin",
        "work": "Listening in the Dark",
        "quote": "Echolocation recordings reveal that **Macrotus** emits soft, low-intensity ultrasonic clicks when hovering inches from resting moths."
      }
    ]
  },
  "Dashboard — macr\\macrotyloma.md": {
    "primary": "A taxonomic genus of leguminous climbing or trailing herbs in the family Fabaceae, including the drought-resilient horse gram (*Macrotyloma uniflorum*).",
    "secondary": "In agronomy and tropical crop science, *Macrotyloma* species are valued as high-protein pulse and forage crops capable of thriving on marginal, nutrient-poor arid soils.",
    "quotes": [
      {
        "author": "Bernard Verdcourt",
        "work": "A Manual of New Guinea Legumes",
        "quote": "The African and Asian species of **Macrotyloma** are readily identified by their distinctive stipels and compressed pods."
      },
      {
        "author": "Daniel Zohary",
        "work": "Domestication of Plants in the Old World",
        "quote": "Archaeological excavations in the Deccan plateau identify **Macrotyloma** horse gram as one of India's earliest indigenous domesticates."
      },
      {
        "author": "C. R. Babu",
        "work": "Herbaceous Flora of Dehradun",
        "quote": "During the monsoon, wild trailing forms of **Macrotyloma** carpet rocky slopes, fixing atmospheric nitrogen through root nodulation."
      }
    ]
  },
  "Dashboard — macr\\macrouridae.md": {
    "primary": "A large family of benthopelagic deep-sea gadiform teleost fishes, commonly known as grenadiers, rattails, or whiptails.",
    "secondary": "In deep-sea oceanography and ichthyology, the Macrouridae constitute a dominant biomass on continental slopes, foraging along abyssal plains with subterminal snouts.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "Report on the Deep-Sea Fishes Collected by H.M.S. Challenger",
        "quote": "The trawl nets of the Challenger brought up immense numbers of **Macrouridae** from ocean depths exceeding a thousand fathoms."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "With their long tapering tails and large luminescent organs, the **Macrouridae** are supremely adapted to bathyal abyssal realms."
      },
      {
        "author": "Tomio Iwamoto",
        "work": "Deep-Sea Fishes of the Family Macrouridae",
        "quote": "Taxonomic keys to the **Macrouridae** rely heavily on snout scalation, branchiostegal ray counts, and light organ placement."
      }
    ]
  },
  "Dashboard — macr\\macrozamia.md": {
    "primary": "A genus of ancient palmlike cycads endemic to Australia in the family Zamiaceae, having pinnate fronds and subterranean or emergent woody trunks.",
    "secondary": "In paleobotany and ethnobotany, *Macrozamia* seeds contain toxic azoxyglycosides (macrozamin) that indigenous Australians leached through running water before milling into flour.",
    "quotes": [
      {
        "author": "Ferdinand von Mueller",
        "work": "Fragmenta Phytographiae Australiae",
        "quote": "The robust cones of **Macrozamia** adorn the stony ridges of eastern Australia, persisting as living relics of ancient flora."
      },
      {
        "author": "Charles Joseph Chamberlain",
        "work": "The Living Cycads",
        "quote": "Field studies on **Macrozamia** reveal that pollination is facilitated by specialized weevils that feed within male sporophylls."
      },
      {
        "author": "Knut Norstog",
        "work": "The Biology of the Cycads",
        "quote": "The subterranean coralloid roots of **Macrozamia** harbor cyanobacterial symbionts that perform active nitrogen fixation."
      }
    ]
  },
  "Dashboard — macr\\macrozoarces.md": {
    "primary": "A taxonomic genus of marine zoarcid fishes comprising the ocean pout (*Macrozoarces americanus*), native to the northwest Atlantic continental shelf.",
    "secondary": "In comparative physiology and molecular cryobiology, *Macrozoarces* serves as the classic organism for isolating type III antifreeze proteins that inhibit ice crystallization in sub-zero seawater.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "The heavy-bodied ocean pout, catalogued under **Macrozoarces**, inhabits rocky reefs and muddy bottoms from Labrador to the Carolinas."
      },
      {
        "author": "Henry B. Bigelow",
        "work": "Fishes of the Gulf of Maine",
        "quote": "Winter trawlers frequently capture **Macrozoarces** as it grazes upon hard-shelled mollusks and echinoderms on coastal banks."
      },
      {
        "author": "Choy L. Hew",
        "work": "Structure and Function of Antifreeze Proteins",
        "quote": "Serum analysis of **Macrozoarces** led to the characterization of globular type III antifreeze polypeptides that depress the thermal hysteresis freezing point."
      }
    ]
  },
  "Dashboard — macr\\macruridae.md": {
    "primary": "A historical and alternative family designation for the deep-sea rattail and grenadier fishes, presently classified as Macrouridae.",
    "secondary": "In nineteenth-century systematic ichthyology, the Macruridae encompassed all gadoid fishes possessing tapering whiplike tails lacking distinct caudal fins.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Naturalists grouped these curious abyssal fishes under the family **Macruridae**, drawing attention to their elongated pointed caudal extremities."
      },
      {
        "author": "Albert Günther",
        "work": "The Study of Fishes",
        "quote": "The deep-sea dredging surveys demonstrate that the **Macruridae** represent the most abundant vertebrate scavengers of the oceanic floor."
      },
      {
        "author": "G. Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "In our oceanic monographs we adopted the spelling **Macruridae** when describing the benthic fishes dredged along the Atlantic gulf stream slope."
      }
    ]
  },
  "Dashboard — meg\\Megacles.md": {
    "primary": "A prominent ancient Athenian aristocratic masculine name, famously borne by leading statesmen and reformers of the illustrious Alcmaeonid dynasty.",
    "secondary": "In classical Greek historiography, Megacles the Archon became notorious for the Cylonian sacrilege (c. 632 BC), and his sixth-century BC descendant was ostracized by popular vote.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "The suitors who gathered at the court of Cleisthenes included **Megacles**, son of Alcmaeon, who ultimately won the hand of Agariste."
      },
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The curse of the goddess attached to the house of **Megacles** because he had put to death the suppliants of Cylon at the sacred altar."
      },
      {
        "author": "Plutarch",
        "work": "Parallel Lives: Solon",
        "quote": "Solon persuaded the partisans of **Megacles** to submit their conduct to a court of three hundred aristocratic peers."
      }
    ]
  },
  "Dashboard — met\\metabolous.md": {
    "primary": "Undergoing, characterized by, or pertaining to biological metamorphosis, especially during insect development.",
    "secondary": "In entomology and invertebrate zoology, metabolous insects are divided into hemimetabolous (incomplete metamorphosis) and holometabolous (complete metamorphosis with a pupal stage) orders.",
    "quotes": [
      {
        "author": "John Lubbock",
        "work": "On the Origin and Metamorphoses of Insects",
        "quote": "The distinction between ametabolous and **metabolous** insects marks a profound evolutionary leap in developmental specialization."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "In every truly **metabolous** order, embryonic growth is followed by marked post-embryonic transformations of mouthparts and wings."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Physiology of Insect Senses",
        "quote": "Metamorphic reorganization in a **metabolous** species completely remodels the peripheral nervous system between nymphal and adult stages."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Finish Slice 1 Batch 1.`);
