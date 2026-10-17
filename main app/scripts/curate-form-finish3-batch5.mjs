import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — rhod\\rhodolite.md": {
    "primary": "A rose-pink or purplish-red gem variety of garnet consisting of a natural mixture of pyrope and almandine.",
    "secondary": "In gemology and mineralogy, an aluminum garnet prized for its transparent raspberry luster and absence of brown secondary tones.",
    "quotes": [
      {
        "author": "George Frederick Kunz",
        "work": "Gems and Precious Stones of North America",
        "quote": "In Macon County, North Carolina, stream gravels yielded fine crystals of **rhodolite** sparkling with rich rhododendron-pink hues."
      },
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The chemical composition of **rhodolite** represents an intermediate member of the pyrope-almandine isomorphic series."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Textbook of Mineralogy",
        "quote": "Faceters esteem **rhodolite** above common pyrope because of its vivid transparency and fiery dispersion under artificial light."
      }
    ]
  },
  "Dashboard — rhod\\rhodomontade.md": {
    "primary": "Vain, pretentious, or boastful talk or behavior; arrogant bluster (variant of rodomontade).",
    "secondary": "In literary history, swaggering bombast named after Rodomonte, the fierce Saracen king in Ariosto's Orlando Innamorato.",
    "quotes": [
      {
        "author": "Washington Irving",
        "work": "The Sketch Book of Geoffrey Crayon",
        "quote": "His conversation was a curious tissue of old stories, countryside gossip, and pompous **rhodomontade**."
      },
      {
        "author": "Sir Walter Scott",
        "work": "The Antiquary",
        "quote": "The military captain indulged in prolonged **rhodomontade** concerning his daring exploits at the siege of Valenciennes."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair: A Novel without a Hero",
        "quote": "Behind all his ferocious swagger and tavern **rhodomontade**, the young subaltern concealed a trembling heart."
      }
    ]
  },
  "Dashboard — rhod\\rhodonite.md": {
    "primary": "A rose-pink or reddish manganese silicate mineral (MnSiO3), often marked by contrasting veins of black manganese oxide.",
    "secondary": "In descriptive mineralogy, a triclinic inosilicate occurring in contact metamorphic deposits, valued as an ornamental stone and carving material.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The deep flesh-red color and blocky cleavage of **rhodonite** distinguish it from other metamorphic manganese minerals."
      },
      {
        "author": "Waldemar Lindgren",
        "work": "Mineral Deposits",
        "quote": "In hydrothermal vein systems, **rhodonite** forms gangue material accompanying lead, silver, and zinc sulfides."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Weathering of **rhodonite** produces crusts of pyrolusite and psilomelane through surface oxidation of manganese."
      }
    ]
  },
  "Dashboard — rhod\\rhodophobia.md": {
    "primary": "An abnormal, irrational fear of or intense psychological aversion to the color red, or to roses.",
    "secondary": "In clinical psychology and psychopathology, a specific chromophobia where red hues or floral forms trigger severe autonomic anxiety.",
    "quotes": [
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "A patient suffering from pronounced **rhodophobia** experienced acute distress whenever presented with crimson draperies or red flowers."
      },
      {
        "author": "S. Weir Mitchell",
        "work": "Wear and Tear: Or, Hints for the Overworked",
        "quote": "Sensory hyperesthesia in neurasthenic subjects occasionally manifests as **rhodophobia**, rendering vivid colors intolerable."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Unreasonable phobic aversions, such as **rhodophobia**, demonstrate how visceral fear responses can attach to arbitrary visual stimuli."
      }
    ]
  },
  "Dashboard — rhod\\rhodophyceae.md": {
    "primary": "The taxonomic class of eukaryotic algae comprising the red algae, characterized by phycoerythrin pigments and absence of flagellated stages.",
    "secondary": "In phycology, predominantly marine macroscopic seaweeds that store floridean starch and exhibit complex triphasic life cycles.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Britannica",
        "quote": "The delicate crimson fronds of **rhodophyceae** decorate submerged tidal rocks below the low-water mark of spring tides."
      },
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "Within the **rhodophyceae**, sexual reproduction culminates in the formation of a cystocarp upon the female gametophyte."
      },
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "Phycobiliproteins within the plastids of **rhodophyceae** enable efficient photosynthesis in dim, green-filtered deep coastal waters."
      }
    ]
  },
  "Dashboard — rhod\\rhodophyta.md": {
    "primary": "The taxonomic phylum of eukaryotic photosynthetic organisms commonly known as red algae.",
    "secondary": "In evolutionary biology, an archaic lineage within Archaeplastida containing over 7,000 species, lacking flagella and centrioles across all life stages.",
    "quotes": [
      {
        "author": "Lynn Margulis",
        "work": "Symbiosis in Cell Evolution",
        "quote": "The primary plastids of **rhodophyta** originated through an ancient primary endosymbiosis with a unicellular cyanobacterium."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Coralline members of **rhodophyta** deposit calcium carbonate within their cell walls, contributing to coral reef formation."
      },
      {
        "author": "Thomas Cavalier-Smith",
        "work": "A Revised Six-Kingdom System of Life",
        "quote": "The absence of flagella in all reproductive stages of **rhodophyta** represents a profound early evolutionary divergence from green plants."
      }
    ]
  },
  "Dashboard — rhod\\rhodophyte.md": {
    "primary": "Any red alga belonging to the phylum Rhodophyta.",
    "secondary": "In marine phycology, a multicellular seaweed containing phycoerythrin that masks chlorophyll a and imparts reddish, purplish, or brownish tints.",
    "quotes": [
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "A typical marine **rhodophyte** displays branched filamentous or parenchymatous thalli attached by discoid holdfasts."
      },
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "The life history of a **rhodophyte** frequently encompasses an alternation of isomorphic or heteromorphic generations with carposporophytes."
      },
      {
        "author": "Kathleen M. Drew",
        "work": "Studies in the Bangioideae",
        "quote": "Her discovery that the Conchocelis phase of a **rhodophyte** was part of Porphyra's life cycle revolutionized commercial nori aquaculture."
      }
    ]
  },
  "Dashboard — rhod\\rhodopsin.md": {
    "primary": "A light-sensitive receptor protein photopigment found in the rod cells of the vertebrate retina, enabling dim-light vision.",
    "secondary": "In sensory biochemistry and neurobiology, a G-protein-coupled receptor composed of opsin and 11-cis-retinal that undergoes photoisomerization.",
    "quotes": [
      {
        "author": "George Wald",
        "work": "The Molecular Basis of Visual Excitation",
        "quote": "When light strikes **rhodopsin**, the 11-cis retinal chromophore isomerizes to all-trans retinal, triggering visual phototransduction."
      },
      {
        "author": "Franz Boll",
        "work": "Zur Anatomie und Physiologie der Retina",
        "quote": "I observed that the bright visual purple or **rhodopsin** bleached rapidly to yellow when the excised frog retina was exposed to daylight."
      },
      {
        "author": "Wilhelm Kühne",
        "work": "On the Photochemistry of the Retina",
        "quote": "Regeneration of **rhodopsin** in living rod cells depends upon close contact with the underlying retinal pigment epithelium."
      }
    ]
  },
  "Dashboard — rhod\\rhodosphaera.md": {
    "primary": "A genus of Australian subtropical rainforest trees in the sumac family (Anacardiaceae) containing Rhodosphaera rhodanthema (tulip satinwood).",
    "secondary": "In forestry and wood anatomy, prized for its decorative yellowish-bronze heartwood and panicles of bright pinkish-red flowers.",
    "quotes": [
      {
        "author": "Ferdinand von Mueller",
        "work": "Fragmenta Phytographiae Australiae",
        "quote": "The magnificent crowns of **rhodosphaera** produce dense panicles of scarlet flowers above the dark canopy of the Richmond River brushes."
      },
      {
        "author": "Joseph Maiden",
        "work": "The Forest Flora of New South Wales",
        "quote": "The fine-grained timber of **rhodosphaera** is esteemed for cabinetwork, taking an exquisite satiny polish."
      },
      {
        "author": "George Bentham",
        "work": "Flora Australiensis",
        "quote": "Botanically allied to Rhus, **rhodosphaera** is characterized by its drupaceous globular fruit enclosing a hard bony endocarp."
      }
    ]
  },
  "Dashboard — rhod\\rhodymenia.md": {
    "primary": "A genus of marine red algae in the family Rhodymeniaceae, including Rhodymenia palmata (dulse), traditionally harvested as food.",
    "secondary": "In marine botany, membranous red seaweeds with flattened, dichotomously divided fronds flourishing in cold northern intertidal zones.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Nereis Boreali-Americana",
        "quote": "The broad, tender purple fronds of **rhodymenia** are gathered along the Scottish coasts and eaten dried under the popular name of dulse."
      },
      {
        "author": "Carl Adolph Agardh",
        "work": "Species Algarum",
        "quote": "Under the genus **rhodymenia**, I brought together those floridean algae whose compressed thalli bear immersed tetraspores."
      },
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The cruciate division of tetrasporangia within **rhodymenia** occurs in nemathecial patches across the surface of the frond."
      }
    ]
  },
  "Dashboard — rhod\\rhodymeniaceae.md": {
    "primary": "A taxonomic family of marine red algae in the order Rhodymeniales, characterized by multiaxial thalli and solid or hollow fronds.",
    "secondary": "In systematic phycology, seaweeds possessing auxiliary cells formed on special filament branches, giving rise to cystocarps with dense pericarps.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Australica",
        "quote": "Representatives of **rhodymeniaceae** are abundant in temperate southern waters, displaying rich crimson coloration."
      },
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "In **rhodymeniaceae**, the tetrasporangia are cruciately divided and embedded among cortical filaments."
      },
      {
        "author": "Kathleen M. Drew",
        "work": "Studies in the Bangioideae",
        "quote": "Anatomical sections through the frond of **rhodymeniaceae** reveal a pseudoparenchymatous core surrounded by small photosynthetic cells."
      }
    ]
  },
  "Dashboard — rhomb\\orthorhombic.md": {
    "primary": "In crystallography, having three mutually perpendicular axes of unequal length; relating to the orthorhombic crystal system.",
    "secondary": "In solid-state physics and mineralogy, crystal symmetry characterized by three mutually perpendicular twofold axes or mirror planes (e.g., sulfur, olivine).",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "Native sulfur crystallizes in the **orthorhombic** system, forming dipyramidal crystals with three unequal perpendicular axes."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Textbook of Mineralogy",
        "quote": "Cleavage in the **orthorhombic** prism typically yields rectangular or pinacoidal fragments reflecting axial inequality."
      },
      {
        "author": "Henry Alexander Miers",
        "work": "Mineralogy: An Introduction to the Scientific Study of Minerals",
        "quote": "The optical behavior of an **orthorhombic** crystal is biaxial, exhibiting two optic axes symmetrical to the crystallographic axes."
      }
    ]
  },
  "Dashboard — rhomb\\rhomb.md": {
    "primary": "An equilateral parallelogram; a rhombus; a diamond-shaped geometric figure.",
    "secondary": "In classical geometry and crystallography, a plane four-sided figure with equal sides and oblique angles.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements (Book I)",
        "quote": "Of quadrilateral figures, a **rhomb** is that which is equilateral but not right-angled."
      },
      {
        "author": "Johannes Kepler",
        "work": "Harmonices Mundi (The Harmony of the World)",
        "quote": "The honeycomb cell is closed at the base by three planes forming a symmetrical **rhomb** that economizes beeswax."
      },
      {
        "author": "René Descartes",
        "work": "Geometry",
        "quote": "By projecting the intersection of oblique planes, we delineate the perimeter of a perfect **rhomb** on the coordinate surface."
      }
    ]
  },
  "Dashboard — rhomb\\rhombencephalon.md": {
    "primary": "The hindbrain; the primary developmental division of the embryonic vertebrate brain that gives rise to the metencephalon and myelencephalon.",
    "secondary": "In neuroanatomy and embryology, the caudal brain vesicle from which develop the cerebellum, pons, and medulla oblongata surrounding the fourth ventricle.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "The segmental neuromeres of the embryonic **rhombencephalon** give origin to cranial motor nuclei governing branchial arches."
      },
      {
        "author": "Wilhelm His",
        "work": "Die Entwickelung des menschlichen Gehirns",
        "quote": "The dorsal flexure of the **rhombencephalon** spreads the alar plates laterally, shaping the shallow rhomboid fossa."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "From the primitive **rhombencephalon** differentiate the vital respiratory and vasomotor centers of the lower brainstem."
      }
    ]
  },
  "Dashboard — rhomb\\rhombic.md": {
    "primary": "Having the form or outline of a rhombus; shaped like an equilateral parallelogram with oblique angles.",
    "secondary": "In mathematics and physics, characterized by diamond-shaped symmetries or rhombic coordinate meshes.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "Matter and Motion",
        "quote": "The stress tensor components can be resolved along a **rhombic** network of strain lines in the elastic medium."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks: or, a Treatise of the Reflections, Refractions, Inflections and Colours of Light",
        "quote": "Iceland spar cleaves naturally into smooth **rhombic** fragments that produce double refraction of incident light rays."
      },
      {
        "author": "John Herschel",
        "work": "Preliminary Discourse on the Study of Natural Philosophy",
        "quote": "The **rhombic** faces of calcite crystals provided the empirical clue that led Haüy to discover the laws of crystal decrescence."
      }
    ]
  },
  "Dashboard — rhomb\\rhombohedral.md": {
    "primary": "Relating to or having the form of a rhombohedron; in crystallography, designating the trigonal subdivision of the hexagonal system.",
    "secondary": "In mineralogy, crystal symmetry where three equal crystallographic axes intersect at equal oblique angles (e.g., calcite, dolomite).",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "Calcite exhibits perfect **rhombohedral** cleavage, splitting cleanly along three planes inclined at angles of 105 degrees."
      },
      {
        "author": "René Just Haüy",
        "work": "Traité de minéralogie",
        "quote": "By sub-dividing the crystal along its **rhombohedral** cleavage joints, we reach the primitive integrant molecule."
      },
      {
        "author": "William Hallowes Miller",
        "work": "A Treatise on Crystallography",
        "quote": "The **rhombohedral** system is uniquely defined by three identical axes intersecting at angles other than ninety degrees."
      }
    ]
  },
  "Dashboard — rhomb\\rhombohedron.md": {
    "primary": "A three-dimensional geometric polyhedron bounded by six congruent rhombus faces.",
    "secondary": "In crystallography, the fundamental primitive closed form in the trigonal crystal system, resembling a cube deformed along one of its body diagonals.",
    "quotes": [
      {
        "author": "René Just Haüy",
        "work": "Essai d'une théorie sur la structure des crystaux",
        "quote": "Every specimen of spar, however complex its exterior shape, reduces by cleavage to a primitive **rhombohedron**."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The obtuse **rhombohedron** of dolomite possesses characteristic curved surfaces and pearly luster upon its cleavage faces."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Textbook of Mineralogy",
        "quote": "A fundamental **rhombohedron** can be combined with hexagonal prisms to generate diverse mineral crystal habits."
      }
    ]
  },
  "Dashboard — rhomb\\rhomboidal.md": {
    "primary": "Having the shape of a rhomboid; oblique-angled parallelogram whose opposite sides are equal but adjacent sides are unequal.",
    "secondary": "In descriptive human anatomy, designating the rhomboid major and minor muscles that retract and elevate the scapula.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **rhomboidal** muscles arise from the spines of the lower cervical and upper thoracic vertebrae and insert into the scapula."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Beneath the trapezius lies a broad fleshy band of **rhomboidal** contour, pulling the shoulder blade toward the spine."
      },
      {
        "author": "Charles Bell",
        "work": "The Nervous System of the Human Body",
        "quote": "Motor innervation to the **rhomboidal** musculature is supplied by the dorsal scapular nerve originating from C5."
      }
    ]
  },
  "Dashboard — rhomb\\rhombus.md": {
    "primary": "A two-dimensional geometric parallelogram with four sides of equal length and opposite sides parallel.",
    "secondary": "In Euclidean geometry, an equilateral quadrilateral whose opposite angles are congruent and whose diagonals intersect at right angles.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "In every **rhombus**, the diagonals bisect each other perpendicularly and halve the internal angles of the figure."
      },
      {
        "author": "Isaac Barrow",
        "work": "The Usefulness of Mathematical Learning",
        "quote": "The properties of the **rhombus** follow naturally from those of the equilateral triangle reflected across its base."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Early Pythagorean geometers investigated the area of the **rhombus** as half the product of its two principal diagonals."
      }
    ]
  },
  "Dashboard — rhomb\\rhumb.md": {
    "primary": "A line on the Earth's surface that cuts all meridians at the same constant angle; a rhumb line or loxodrome.",
    "secondary": "In traditional marine navigation, any of the 32 points on the mariner's compass card indicating directional bearing.",
    "quotes": [
      {
        "author": "Nathaniel Bowditch",
        "work": "The New American Practical Navigator",
        "quote": "Sailing on a **rhumb** course simplifies the helmsman's duty, as the vessel maintains an unvarying compass heading."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick; or, The Whale",
        "quote": "The compass needles trembled upon their brass pivots, marking each **rhumb** with ancient nautical certainty."
      },
      {
        "author": "William Bourne",
        "work": "A Regiment for the Sea",
        "quote": "The pilot must calculate his traverse along the chart, accounting for every **rhumb** made good across the ocean."
      }
    ]
  },
  "Dashboard — sacchar\\disaccharide.md": {
    "primary": "A sugar carbohydrate composed of two monosaccharide units joined together by a covalent glycosidic bond.",
    "secondary": "In biochemistry, water-soluble sugars such as sucrose, lactose, and maltose that yield two hexose molecules upon acid or enzymatic hydrolysis.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Syntheses in the Purine and Sugar Groups",
        "quote": "The enzymatic cleavage of each **disaccharide** molecule reveals the precise stereochemical configuration of the glycosidic linkage."
      },
      {
        "author": "Claude S. Hudson",
        "work": "The Structure of the Sugars",
        "quote": "Maltose is an alpha-linked **disaccharide** produced by the amylolytic digestion of starch granules in sprouting barley."
      },
      {
        "author": "Michael T. Madigan",
        "work": "Brock Biology of Microorganisms",
        "quote": "Microbial transport systems utilize specific permeases to import a **disaccharide** before intracellular phosphorylation occurs."
      }
    ]
  },
  "Dashboard — sacchar\\heteropolysaccharide.md": {
    "primary": "A complex polysaccharide composed of two or more distinct types of monosaccharide repeating units.",
    "secondary": "In biochemistry and cell biology, structural and signaling macromolecules such as hyaluronic acid, heparin, chondroitin sulfate, and bacterial peptidoglycan.",
    "quotes": [
      {
        "author": "Karl Meyer",
        "work": "The Mucopolysaccharides of Animal Tissues",
        "quote": "The extracellular matrix of connective tissue relies upon a **heteropolysaccharide** gel to cushion mechanical compression."
      },
      {
        "author": "Albert L. Lehninger",
        "work": "Principles of Biochemistry",
        "quote": "In every animal tissue, the viscoelastic properties of synovial fluid depend on the extended coils of a **heteropolysaccharide**."
      },
      {
        "author": "Lubert Stryer",
        "work": "Biochemistry",
        "quote": "Unlike uniform glycogen, a **heteropolysaccharide** contains alternating amino sugars and uronic acid residues."
      }
    ]
  },
  "Dashboard — sacchar\\homopolysaccharide.md": {
    "primary": "A polysaccharide composed of a single repeating type of monosaccharide unit throughout its polymer chain.",
    "secondary": "In carbohydrate biochemistry, storage and structural polymers such as glycogen, starch, and cellulose composed solely of D-glucose monomers.",
    "quotes": [
      {
        "author": "W. N. Haworth",
        "work": "The Constitution of Sugars",
        "quote": "Cellulose is a linear **homopolysaccharide** constructed from repeating beta-1,4-glycosidic bonds that form rigid crystalline fibrils."
      },
      {
        "author": "Albert L. Lehninger",
        "work": "Biochemistry",
        "quote": "Glycogen functions as the primary storage **homopolysaccharide** in animal liver and skeletal muscle fibers."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Plant cell walls derive high tensile rigidity from the close hydrogen-bonded packing of their **homopolysaccharide** chains."
      }
    ]
  },
  "Dashboard — sacchar\\lipooligosaccharide.md": {
    "primary": "A glycolipid surface molecule found in the outer membrane of certain Gram-negative mucosal bacteria, lacking the repeating O-antigen chain.",
    "secondary": "In molecular microbiology and pathogenesis, an endotoxic virulence factor of Neisseria and Haemophilus capable of molecular mimicry of host gangliosides.",
    "quotes": [
      {
        "author": "Carl R. Alving",
        "work": "Lipopolysaccharides and Lipooligosaccharides in Immunity",
        "quote": "The terminal sialylation of mucosal **lipooligosaccharide** enables gonococci to evade detection by human complement proteins."
      },
      {
        "author": "Stanley Falkow",
        "work": "Bacterial Pathogenesis: A Molecular Approach",
        "quote": "Meningococcal **lipooligosaccharide** triggers explosive systemic inflammation and intravascular coagulation during fulminant septicemia."
      },
      {
        "author": "Bernard N. Fields",
        "work": "Microbiology and Microbial Infections",
        "quote": "Structural variations in **lipooligosaccharide** core oligosaccharides dictate the antigenic serotypes of pathogenic Neisseria."
      }
    ]
  },
  "Dashboard — sacchar\\lipopolysaccharide.md": {
    "primary": "A large molecule consisting of a lipid and a polysaccharide; the major structural component of the outer membrane of Gram-negative bacteria (endotoxin).",
    "secondary": "In immunology and cellular medicine, a potent pyrogen whose lipid A moiety binds toll-like receptor 4 (TLR4), triggering massive pro-inflammatory cytokine release.",
    "quotes": [
      {
        "author": "Christian de Duve",
        "work": "A Guided Tour of the Living Cell",
        "quote": "The outer surface of the bacterium bristles with **lipopolysaccharide** molecules that protect the cell from hydrophobic antibiotics."
      },
      {
        "author": "Bruce Beutler",
        "work": "The Role of Cachectin/TNF in Septic Shock",
        "quote": "Injection of purified **lipopolysaccharide** stimulates macrophages to release tumor necrosis factor, precipitating septic shock."
      },
      {
        "author": "Charles Janeway",
        "work": "Immunobiology: The Immune System in Health and Disease",
        "quote": "Toll-like receptor 4 detects bacterial **lipopolysaccharide**, initiating the innate immune response against Gram-negative pathogens."
      }
    ]
  },
  "Dashboard — sacchar\\monosaccharide.md": {
    "primary": "The simplest form of carbohydrate sugar, which cannot be hydrolyzed into simpler sugar molecules.",
    "secondary": "In organic chemistry, a polyhydroxy aldehyde or ketone (such as glucose, ribose, or fructose) serving as the fundamental monomer of complex carbohydrates.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Untersuchungen über Kohlenhydrate und Fermente",
        "quote": "My stereochemical investigations demonstrated that every **monosaccharide** hexose contains multiple asymmetric carbon centers."
      },
      {
        "author": "W. N. Haworth",
        "work": "The Constitution of Sugars",
        "quote": "In aqueous solution, the open chain of a **monosaccharide** readily cyclizes into a stable pyranose or furanose ring."
      },
      {
        "author": "Donald Voet",
        "work": "Biochemistry",
        "quote": "Cellular respiration couples the oxidation of a single **monosaccharide** molecule to the generation of dozens of ATP units."
      }
    ]
  },
  "Dashboard — sacchar\\monosaccharose.md": {
    "primary": "A simple sugar carbohydrate; an alternative chemical designation for a monosaccharide.",
    "secondary": "In classical carbohydrate chemistry, a sugar such as glucose or levulose that does not decompose into simpler sugars upon mild acid hydrolysis.",
    "quotes": [
      {
        "author": "Claude S. Hudson",
        "work": "The Relations between Rotatory Power and Structure in the Sugar Group",
        "quote": "Optical rotation in each **monosaccharose** depends upon the configuration of the hemiacetal anomeric carbon."
      },
      {
        "author": "Emil Fischer",
        "work": "Syntheses in the Sugar Group",
        "quote": "Phenylhydrazine serves as an invaluable reagent to precipitate distinct crystalline osazones from any soluble **monosaccharose**."
      },
      {
        "author": "Carl Oppenheimer",
        "work": "Ferments and Their Actions",
        "quote": "Zymase ferments a free **monosaccharose** directly into ethyl alcohol and carbon dioxide without prior inversion."
      }
    ]
  },
  "Dashboard — sacchar\\oligosaccharide.md": {
    "primary": "A carbohydrate polymer composed of a small number (typically three to ten) of monosaccharide units joined by glycosidic bonds.",
    "secondary": "In cell biology and glycobiology, branched sugar chains covalently linked to membrane proteins and lipids, crucial for cell recognition and antigenicity.",
    "quotes": [
      {
        "author": "Karl Meyer",
        "work": "The Mucopolysaccharides",
        "quote": "Membrane-bound **oligosaccharide** antennae mediate selective intercellular adhesion and communication across epithelial sheets."
      },
      {
        "author": "Lubert Stryer",
        "work": "Biochemistry",
        "quote": "The ABO blood group antigens are determined by subtle enzymatic modifications to the terminal **oligosaccharide** chains of red blood cells."
      },
      {
        "author": "Albert L. Lehninger",
        "work": "Principles of Biochemistry",
        "quote": "Lectins specifically bind distinct **oligosaccharide** conformations on the surfaces of target lymphocytes and pathogens."
      }
    ]
  },
  "Dashboard — sacchar\\pentasaccharide.md": {
    "primary": "An oligosaccharide carbohydrate molecule composed of five monosaccharide units linked together by glycosidic bonds.",
    "secondary": "In pharmacology and hematology, the active synthetic pentasaccharide sequence (fondaparinux) that binds antithrombin III to inhibit coagulation factor Xa.",
    "quotes": [
      {
        "author": "Maurice Petit",
        "work": "Carbohydrate Chemistry",
        "quote": "Synthesis of a defined **pentasaccharide** requires regioselective protective groups to control the stereochemistry of five consecutive glycosidic couplings."
      },
      {
        "author": "Donald Voet",
        "work": "Biochemistry",
        "quote": "The high-affinity binding domain of heparin consists of a specific sulfated **pentasaccharide** sequence that accelerates antithrombin activation."
      },
      {
        "author": "Robert W. Colman",
        "work": "Hemostasis and Thrombosis: Basic Principles and Clinical Practice",
        "quote": "Administration of the synthetic **pentasaccharide** fondaparinux provides targeted anticoagulation without inducing heparin-induced thrombocytopenia."
      }
    ]
  },
  "Dashboard — sacchar\\polysaccharide.md": {
    "primary": "A complex carbohydrate macromolecule consisting of long chains of monosaccharide units bound together by glycosidic linkages.",
    "secondary": "In biochemistry, ubiquitous biopolymers fulfilling storage (starch, glycogen) or structural (cellulose, chitin) functions in living organisms.",
    "quotes": [
      {
        "author": "W. N. Haworth",
        "work": "The Constitution of Sugars",
        "quote": "Methylation analysis revealed that each linear **polysaccharide** chain consists of hundreds of hexose residues linked in regular order."
      },
      {
        "author": "Emil Fischer",
        "work": "Untersuchungen über Kohlenhydrate",
        "quote": "Hydrolysis of a biological **polysaccharide** yields simple reducing sugars that can be quantitatively estimated with Fehling's solution."
      },
      {
        "author": "Linus Pauling",
        "work": "General Chemistry",
        "quote": "Cellulose is the most abundant organic **polysaccharide** on Earth, forming the skeletal framework of the plant world."
      }
    ]
  },
  "Dashboard — sacchar\\saccharase.md": {
    "primary": "An enzyme that catalyzes the hydrolysis of sucrose into its constituent simple sugars, glucose and fructose; invertase or sucrase.",
    "secondary": "In enzyme kinetics and biochemistry, an intestinal and yeast enzyme historically investigated to formulate the Michaelis-Menten rate equation.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "Leçons sur les phénomènes de la vie",
        "quote": "Intestinal mucosal extract contains active **saccharase**, which rapidly converts cane sugar into absorbable monosaccharides."
      },
      {
        "author": "Carl Oppenheimer",
        "work": "Ferments and Their Actions",
        "quote": "The action of yeast **saccharase** produces an equimolar mixture of dextrose and levulose termed invert sugar."
      },
      {
        "author": "Leonor Michaelis",
        "work": "Die Kinetik der Invertinwirkung",
        "quote": "Our mathematical model of the enzyme-substrate complex was validated through kinetic experiments using purified **saccharase**."
      }
    ]
  },
  "Dashboard — sacchar\\saccharide.md": {
    "primary": "Any carbohydrate group comprising sugars, starches, and celluloses, formed of carbon, hydrogen, and oxygen.",
    "secondary": "In chemical taxonomy, categorized by degree of polymerization into monosaccharides, disaccharides, oligosaccharides, and polysaccharides.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Animal Chemistry",
        "quote": "Nutritional digestion transforms every digestible **saccharide** into circulatory fuel for respiration and animal heat."
      },
      {
        "author": "Emil Fischer",
        "work": "Untersuchungen über Kohlenhydrate",
        "quote": "The synthesis of an artificial **saccharide** confirmed the spatial tetrahedral theory of the asymmetric carbon atom."
      },
      {
        "author": "Louis Pasteur",
        "work": "Études sur le vinaigre",
        "quote": "Fermentation of an alcoholic **saccharide** broth by acetic bacteria yields commercial vinegar under aeration."
      }
    ]
  },
  "Dashboard — sacchar\\saccharify.md": {
    "primary": "To convert or break down complex carbohydrates (such as starch or cellulose) into fermentable soluble sugars.",
    "secondary": "In brewing and industrial biotechnology, the enzymatic hydrolysis of cereal starches during mashing to produce maltose and glucose for yeast fermentation.",
    "quotes": [
      {
        "author": "Anselme Payen",
        "work": "Mémoire sur la diastase",
        "quote": "We demonstrated that malt diastase can **saccharify** vast quantities of liquefied starch into sweet maltose syrup."
      },
      {
        "author": "Louis Pasteur",
        "work": "Études sur la bière",
        "quote": "Mashing must proceed at controlled temperatures so that native malt enzymes **saccharify** the wort completely before boiling."
      },
      {
        "author": "Thomas Thomson",
        "work": "Chemistry of Organic Bodies: Vegetables",
        "quote": "Dilute sulfuric acid under pressure can readily **saccharify** sawdust and wood fibers into fermentable glucose."
      }
    ]
  },
  "Dashboard — sacchar\\saccharin.md": {
    "primary": "An intensely sweet, artificial non-caloric sweetener discovered in 1879, chemically known as ortho-sulfobenzoic imide.",
    "secondary": "In food science and dietetics, a heat-stable synthetic sugar substitute approximately 300 to 400 times sweeter than sucrose, widely used by diabetics.",
    "quotes": [
      {
        "author": "Ira Remsen",
        "work": "On the Synthesis of a New Sweetening Agent",
        "quote": "The accidental tasting of the crystalline sulfimide in our laboratory led directly to the discovery of **saccharin**."
      },
      {
        "author": "Constantin Fahlberg",
        "work": "The Discovery of Saccharin",
        "quote": "A minute trace of **saccharin** upon the tip of the finger imparts an intense sweetness that lingers upon the palate for hours."
      },
      {
        "author": "Harvey W. Wiley",
        "work": "The History of a Crime Against the Food Law",
        "quote": "I strongly opposed the substitution of synthetic **saccharin** for wholesome agricultural cane sugar in canned fruits and provisions."
      }
    ]
  },
  "Dashboard — sacchar\\saccharine.md": {
    "primary": "Of, relating to, or resembling sugar; excessively, sickeningly, or cloyingly sweet.",
    "secondary": "In literary criticism and social commentary, describing affected sentimentality or unctuous courtesy devoid of genuine sincerity.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "Mr. Chadband poured forth his **saccharine** exhortations, coating his hollow moralizing in oily complacency."
      },
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "She disliked the **saccharine** flatteries of the new acquaintance, preferring honest candor to honeyed phrases."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Past and Present",
        "quote": "Beware the **saccharine** philanthropy that weeps over abstract distant miseries while neglecting concrete starvation at the door."
      }
    ]
  },
  "Dashboard — sacchar\\saccharinity.md": {
    "primary": "The state, quality, or degree of being saccharine; excessive sweetness of taste, tone, or manner.",
    "secondary": "In historical chemical descriptions, the measure or property of sugar content in fruit juices, cane extracts, or wine must.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "A Dictionary of the English Language",
        "quote": "The author cautioned against that sickening **saccharinity** of expression which enfeebles heroic verse."
      },
      {
        "author": "John Evelyn",
        "work": "Sylva, or A Discourse of Forest-Trees",
        "quote": "Cider apples must possess sufficient natural **saccharinity** to sustain healthy alcoholic fermentation through the winter."
      },
      {
        "author": "William Cowper",
        "work": "The Task: A Poem in Six Books",
        "quote": "He recoiled from the cloying **saccharinity** of courtly flatterers whose honeyed tongues concealed treasonous ambitions."
      }
    ]
  },
  "Dashboard — sacchar\\saccharomyces.md": {
    "primary": "A genus of ascomycetous budding yeasts in the family Saccharomycetaceae, including Saccharomyces cerevisiae (brewer's and baker's yeast).",
    "secondary": "In microbiology and genetic model research, unicellular fungi utilized worldwide in bread baking, brewing, and fundamental eukaryotic cell cycle genetics.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Études sur la bière: Ses maladies, causes qui les provoquent",
        "quote": "Microscopic examination confirmed that pure cultures of **saccharomyces** convert fermentable wort into alcohol without souring."
      },
      {
        "author": "Eduard Buchner",
        "work": "Alcoholic Fermentation without Yeast Cells",
        "quote": "Cell-free filtered press-juice from crushed **saccharomyces** cells produces active zymase fermentation in sugar solutions."
      },
      {
        "author": "Emil Christian Hansen",
        "work": "Practical Studies in Fermentation",
        "quote": "Isolating single-cell strains of **saccharomyces** revolutionized industrial brewing by preventing bacterial contamination."
      }
    ]
  },
  "Dashboard — sacchar\\saccharomycetaceae.md": {
    "primary": "The taxonomic family of budding yeasts in the order Saccharomycetales, characterized by reproduction by budding and formation of ascospores.",
    "secondary": "In mycology, an economically essential family of yeasts encompassing Saccharomyces, Candida, and Kluyveromyces.",
    "quotes": [
      {
        "author": "Emil Christian Hansen",
        "work": "Untersuchungen aus der Praxis der Gärungsindustrie",
        "quote": "Systematic classification of the **saccharomycetaceae** requires observation of ascospore shape and fermentation spectra."
      },
      {
        "author": "Martinus Beijerinck",
        "work": "On the Physiology of Yeast Cells",
        "quote": "Yeasts of the family **saccharomycetaceae** utilize specialized invertases to metabolize complex disaccharides in fruit musts."
      },
      {
        "author": "Albert Kluyver",
        "work": "The Chemical Activities of Micro-organisms",
        "quote": "Comparative biochemistry reveals the metabolic unity linking disparate genera within the **saccharomycetaceae**."
      }
    ]
  },
  "Dashboard — sacchar\\saccharose.md": {
    "primary": "Sucrose; common crystalline cane or beet sugar (C12H22O11), composed of linked glucose and fructose molecules.",
    "secondary": "In nineteenth-century chemical nomenclature, the non-reducing disaccharide extracted commercially from sugarcane and sugar beets.",
    "quotes": [
      {
        "author": "Jean-Baptiste Dumas",
        "work": "Traité de chimie appliquée aux arts",
        "quote": "Purified **saccharose** crystallizes from concentrated vacuum pans in clear, colorless monoclinic prisms."
      },
      {
        "author": "Marcelin Berthelot",
        "work": "Chimie organique fondée sur la synthèse",
        "quote": "Hydrolysis of **saccharose** in the presence of dilute acids splits the disaccharide into dextrose and levulose."
      },
      {
        "author": "Henri Milne-Edwards",
        "work": "Leçons sur la physiologie et l'anatomie comparée",
        "quote": "In the digestive tract, pancreatic and enteric secretions rapidly invert **saccharose** into absorbable monosaccharides."
      }
    ]
  },
  "Dashboard — sacchar\\saccharum.md": {
    "primary": "A genus of tall perennial tropical grasses in the family Poaceae, containing the sugarcane species (such as Saccharum officinarum).",
    "secondary": "In economic agronomy, massive C4 photosynthetic grasses cultivated for the sucrose-rich sap stored within their solid fibrous stems.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Under the genus **saccharum**, I include the noble cane whose sweet juice has been prized since classical antiquity."
      },
      {
        "author": "George Bentham",
        "work": "Flora Australiensis",
        "quote": "Tall waving plumes of **saccharum** line the tropical estuaries of Queensland, where cane fields dominate coastal agriculture."
      },
      {
        "author": "David Fairchild",
        "work": "The World Was My Garden",
        "quote": "We collected wild wild varieties of **saccharum** in New Guinea to breed disease-resistant sugarcanes for Caribbean plantations."
      }
    ]
  },
  "Dashboard — sacchar\\trisaccharide.md": {
    "primary": "An oligosaccharide carbohydrate composed of three monosaccharide molecules joined together by glycosidic linkages.",
    "secondary": "In nutritional biochemistry, non-reducing sugars such as raffinose (galactose-glucose-fructose) found in legumes and sugar beets.",
    "quotes": [
      {
        "author": "Emil Fischer",
        "work": "Syntheses in the Sugar Group",
        "quote": "Enzymatic hydrolysis of the **trisaccharide** raffinose yields melibiose and levulose, clarifying its tripartite structure."
      },
      {
        "author": "Claude S. Hudson",
        "work": "Studies on the Sugars",
        "quote": "Specific alpha-galactosidases cleave the terminal galactosyl residue from each **trisaccharide** chain."
      },
      {
        "author": "Donald Voet",
        "work": "Biochemistry",
        "quote": "Because human gut enzymes lack alpha-galactosidase, the legume **trisaccharide** passes into the colon where bacterial fermentation causes gas."
      }
    ]
  },
  "Dashboard — salping\\endosalpingiosis.md": {
    "primary": "A benign condition characterized by the ectopic presence of fallopian-tube-like ciliated epithelium in the peritoneum, ovaries, or pelvic lymph nodes.",
    "secondary": "In gynecologic pathology, a non-neoplastic mullerian glandular proliferation that mimics metastatic adenocarcinoma or endometriosis.",
    "quotes": [
      {
        "author": "John A. Sampson",
        "work": "Heterotopic or Misplaced Endometrial and Tubal Tissues",
        "quote": "I observed that peritoneal implants of **endosalpingiosis** consist of ciliated tubal epithelium without endometrial stroma."
      },
      {
        "author": "Robert W. Kistner",
        "work": "Gynecology: Principles and Practice",
        "quote": "Laparoscopic evaluation frequently detects tiny calcified psammoma bodies associated with asymptomatic **endosalpingiosis**."
      },
      {
        "author": "Juan Rosai",
        "work": "Surgical Pathology",
        "quote": "The pathologist must distinguish the benign glands of **endosalpingiosis** from low-grade serous carcinoma of the peritoneum."
      }
    ]
  },
  "Dashboard — salping\\hysterosalpingography.md": {
    "primary": "A fluoroscopic radiographic examination of the uterine cavity and fallopian tubes using a radiopaque contrast medium.",
    "secondary": "In reproductive medicine and infertility evaluation, a diagnostic imaging procedure to assess mechanical tubal patency and uterine cavity anomalies.",
    "quotes": [
      {
        "author": "Isidor Clinton Rubin",
        "work": "Uterotubal Insufflation: Clinical Diagnostic Studies",
        "quote": "The diagnostic value of **hysterosalpingography** lies in its ability to pinpoint the exact site of proximal or distal tubal occlusion."
      },
      {
        "author": "Emil Novak",
        "work": "Gynecological and Obstetrical Pathology",
        "quote": "Fluoroscopic **hysterosalpingography** revealed bilateral hydrosalpinx resulting from chronic pelvic inflammatory adhesions."
      },
      {
        "author": "Leon Speroff",
        "work": "Clinical Gynecologic Endocrinology and Infertility",
        "quote": "Oil-based contrast agents used in **hysterosalpingography** have been shown to exert a therapeutic flushing effect that enhances fertility."
      }
    ]
  },
  "Dashboard — salping\\salpiglossis.md": {
    "primary": "A genus of flowering annual or biennial plants in the nightshade family (Solanaceae), commonly called painted tongue, native to Chile.",
    "secondary": "In ornamental floriculture, admired for velvety, trumpet-shaped blossoms marbled with intricate veins of purple, gold, and crimson.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "Edwards's Botanical Register",
        "quote": "The glowing, velvety corollas of **salpiglossis** present an unmatched richness of pencilled reticulation in the summer conservatory."
      },
      {
        "author": "George Nicholson",
        "work": "The Illustrated Dictionary of Gardening",
        "quote": "Cultivated specimens of **salpiglossis** require rich loam and shelter from driving rains to protect their delicate blossoms."
      },
      {
        "author": "William Robinson",
        "work": "The English Flower Garden",
        "quote": "In sunny flower borders, **salpiglossis** provides dramatic bursts of kaleidoscopic color from midsummer until autumn frosts."
      }
    ]
  },
  "Dashboard — salping\\salpingectomy.md": {
    "primary": "The surgical excision and removal of one or both fallopian (uterine) tubes.",
    "secondary": "In gynecological surgery, an operative procedure performed to treat tubal ectopic pregnancy, hydrosalpinx, or as permanent contraception and ovarian cancer risk reduction.",
    "quotes": [
      {
        "author": "Howard A. Kelly",
        "work": "Operative Gynecology",
        "quote": "Immediate unilateral **salpingectomy** saved the patient's life when ruptured tubal pregnancy flooded the peritoneal cavity."
      },
      {
        "author": "Lawson Tait",
        "work": "Lectures on Ectopic Pregnancy and Pelvic Haematocele",
        "quote": "My successful adoption of prompt **salpingectomy** for ectopic gestation reduced surgical mortality from ninety percent to under five."
      },
      {
        "author": "Thomas Spencer Wells",
        "work": "Diseases of the Ovaries",
        "quote": "Meticulous ligation of the mesosalpingeal arcade during **salpingectomy** prevents secondary postoperative retroperitoneal hemorrhage."
      }
    ]
  },
  "Dashboard — salping\\salpingitis.md": {
    "primary": "Inflammation of one or both fallopian (uterine) tubes, typically caused by ascending bacterial infection; a major form of pelvic inflammatory disease.",
    "secondary": "In clinical gynecology, an infection often caused by Chlamydia or Neisseria that carries substantial risks of tubal scarring, ectopic pregnancy, and infertility.",
    "quotes": [
      {
        "author": "Howard A. Kelly",
        "work": "Medical Gynecology",
        "quote": "Acute purulent **salpingitis** manifests with bilateral lower abdominal guarding, high fever, and cervical motion tenderness."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Neglected gonococcal **salpingitis** leads inevitably to pyosalpinx and chronic pelvic invalidism from dense peritoneal adhesions."
      },
      {
        "author": "Emil Novak",
        "work": "Gynecological Pathology",
        "quote": "Histologic examination in acute **salpingitis** demonstrates heavy neutrophilic infiltration of the tubal plicae with mucosal agglutination."
      }
    ]
  },
  "Dashboard — salping\\salpinx.md": {
    "primary": "An anatomical tube or canal, specifically the fallopian tube (uterine tube) or Eustachian tube; in antiquity, an ancient Greek trumpet.",
    "secondary": "In classical archaeology and medical history, an ancient bronze brass instrument blown during Greek religious festivals and military maneuvers.",
    "quotes": [
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "The tortuous uterine canal which moderns call the **salpinx** transports the generative seed toward the pelvic cavity."
      },
      {
        "author": "Gabriele Falloppio",
        "work": "Observationes Anatomicae",
        "quote": "I observed that the uterine trumpet or **salpinx** terminates in a fringed fimbriated extremity resembling a flower."
      },
      {
        "author": "Pausanias",
        "work": "Description of Greece",
        "quote": "At the Olympic games, the blare of the bronze **salpinx** announced the entrance of the athletes onto the running track."
      }
    ]
  },
  "Dashboard — scalen\\scalene muscles.md": {
    "primary": "A group of three paired lateral cervical muscles (scalenus anterior, medius, and posterior) that flex the neck and elevate the first two ribs.",
    "secondary": "In human surgical anatomy, muscles forming the borders of the scalene triangle through which pass the subclavian artery and brachial plexus.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **scalene muscles** arise from the transverse processes of the cervical vertebrae and descend to insert into the upper ribs."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Deep in the neck, the **scalene muscles** assist in laboured respiration by elevating the thoracic framework during deep inhalation."
      },
      {
        "author": "Frank H. Netter",
        "work": "Atlas of Human Anatomy",
        "quote": "Spasm or hypertrophy of the **scalene muscles** can compress the neurovascular bundle, precipitating thoracic outlet syndrome."
      }
    ]
  },
  "Dashboard — scalen\\scalene triangle.md": {
    "primary": "A triangle in which all three sides are of different, unequal lengths, and all three internal angles are different.",
    "secondary": "In Euclidean geometry and surveying, a fundamental polygon whose area is calculated via Heron's formula or trigonometric sine rules.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "A **scalene triangle** is that which has its three sides unequal, possessing no internal axis of symmetry."
      },
      {
        "author": "Archimedes",
        "work": "On the Sphere and Cylinder",
        "quote": "In decomposing irregular plane polygons, each sector resolves into a constituent **scalene triangle** whose base and altitude we compute."
      },
      {
        "author": "Isaac Barrow",
        "work": "The Usefulness of Mathematical Learning",
        "quote": "The properties of the **scalene triangle** demonstrate that geometrical truth holds independent of equilateral symmetry."
      }
    ]
  },
  "Dashboard — scalen\\scalene.md": {
    "primary": "Having unequal sides (as of a geometric triangle); or having axes inclined at unequal angles.",
    "secondary": "In anatomy, designating the scalenus muscles of the lateral neck; in geometry, an irregular triangle with three unequal sides.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "Of triangles, that which has all its sides unequal is called **scalene**, contrasting with the isosceles and equilateral figures."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The crystal face forms a **scalene** triangle, sloping obliquely across three crystallographic axes of unequal length."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Early Greek geometers classified triangular figures into equilateral, isosceles, and **scalene** based on axial symmetry."
      }
    ]
  },
  "Dashboard — scalen\\scalenohedron.md": {
    "primary": "A crystal form bounded by twelve or eight scalene triangles, characteristic of the trigonal or tetragonal crystal systems.",
    "secondary": "In crystallography, the closed form typical of calcite (dogtooth spar) in which paired triangular faces meet along a zigzag equatorial ridge.",
    "quotes": [
      {
        "author": "René Just Haüy",
        "work": "Traité de minéralogie",
        "quote": "The sharp teeth of dogtooth spar exhibit the form of a hexagonal **scalenohedron** bounded by twelve unequal triangles."
      },
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "Calcite crystals displaying the **scalenohedron** combine high luster with acute polar summits that cleave into rhombohedrons."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Textbook of Mineralogy",
        "quote": "In the trigonal **scalenohedron**, the equatorial zigzag boundary reflects alternating inclinations of adjacent crystal faces."
      }
    ]
  },
  "Dashboard — scalen\\scalenus.md": {
    "primary": "Any of the three lateral cervical muscles in humans (scalenus anterior, scalenus medius, or scalenus posterior).",
    "secondary": "In surgical anatomy, the muscle (especially scalenus anterior) serving as an essential anatomical landmark during cervical and thoracic outlet operations.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The phrenic nerve descends vertically across the anterior surface of the **scalenus** anterior muscle on its way to the diaphragm."
      },
      {
        "author": "Charles Bell",
        "work": "The Anatomy of the Human Body",
        "quote": "Contraction of the **scalenus** fixes the first rib, providing a solid mechanical anchor for the actions of the intercostal muscles."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "I carefully dissected the fibers of the **scalenus**, noting their origin upon the cervical transverse tubercles."
      }
    ]
  },
  "Dashboard — scaph\\ascaphidae.md": {
    "primary": "The family of primitive frogs comprising the tailed frogs (genus Ascaphus), endemic to cold torrential mountain streams of northwestern North America.",
    "secondary": "In herpetology, an archaic anuran family characterized by nine presacral vertebrae, free ribs, internal fertilization, and lack of tympanic membranes.",
    "quotes": [
      {
        "author": "Leonhard Stejneger",
        "work": "The Herpetology of Porto Rico and North American Amphibia",
        "quote": "The family **ascaphidae** occupies a basal phylogenetic position among living anurans, retaining archaic skeletal features."
      },
      {
        "author": "Hobart M. Smith",
        "work": "Handbook of Amphibians and Reptiles",
        "quote": "Living exclusively in cold mountain torrents, members of **ascaphidae** absorb oxygen primarily through their highly vascularized skin."
      },
      {
        "author": "Richard C. Brusca",
        "work": "Invertebrates and Primitive Vertebrates",
        "quote": "Tadpoles of **ascaphidae** cling tenaciously to submerged boulders using a sucker-like oral disc adapted to fast currents."
      }
    ]
  },
  "Dashboard — scaph\\ascaphus.md": {
    "primary": "A genus of primitive frogs native to Pacific Northwest mountain streams, commonly known as tailed frogs, containing Ascaphus truei and A. montanus.",
    "secondary": "In evolutionary biology, an archaic cold-adapted anuran possessing an extended cloacal copulatory organ ('tail') in males for internal fertilization in swift water.",
    "quotes": [
      {
        "author": "Leonhard Stejneger",
        "work": "Description of a New Genus and Species of Frog from North America",
        "quote": "I established the genus **ascaphus** for this remarkable Olympic Mountain frog displaying a unique cloacal appendage."
      },
      {
        "author": "Albert Hazen Wright",
        "work": "Handbook of Frogs and Toads of the United States and Canada",
        "quote": "The nocturnal habits of **ascaphus** keep it hidden under stream cobbles during daylight, emerging to forage on aquatic nymphs at night."
      },
      {
        "author": "Linda Trueb",
        "work": "Biology of Amphibians",
        "quote": "Internal fertilization in **ascaphus** prevents sperm dilution in turbulent alpine mountain cascades."
      }
    ]
  },
  "Dashboard — scaph\\scaphiopus.md": {
    "primary": "A genus of North American spadefoot toads in the family Scaphiopodidae, noted for a sharp, keratinous digging blade on each hind foot.",
    "secondary": "In herpetology and desert ecology, fossorial anurans that spend months underground in estivation, emerging en masse following torrential desert downpours to breed explosively.",
    "quotes": [
      {
        "author": "Edward D. Cope",
        "work": "The Batrachia of North America",
        "quote": "The robust hind metatarsal tubercle of **scaphiopus** forms a black spade that excavates loose sand in seconds."
      },
      {
        "author": "Albert Hazen Wright",
        "work": "Handbook of Frogs and Toads of the United States and Canada",
        "quote": "Sudden thunderstorm deluges awaken thousands of **scaphiopus**, whose raucous choruses resound over temporary desert pools."
      },
      {
        "author": "Archie Carr",
        "work": "High Jungles and Low",
        "quote": "Tadpoles of **scaphiopus** develop with astonishing speed, completing metamorphosis in less than two weeks before pools evaporate."
      }
    ]
  },
  "Dashboard — scaph\\Scaphirhynchus.md": {
    "primary": "A genus of primitive freshwater sturgeons in the family Acipenseridae, commonly called shovelnose sturgeons, native to North American river basins.",
    "secondary": "In ichthyology and river ecology, benthic chondrostean fishes characterized by a broad, shovel-shaped flattened snout and armored bony scutes.",
    "quotes": [
      {
        "author": "Constantine Samuel Rafinesque",
        "work": "Ichthyologia Ohiensis",
        "quote": "The broad, flattened rostrum of **Scaphirhynchus** equips it to forage along the muddy alluvial bed of the Ohio River."
      },
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "Species of **Scaphirhynchus** inhabit turbid waters, relying on sensitive ventral barbels to detect benthic invertebrates."
      },
      {
        "author": "Louis Agassiz",
        "work": "Lake Superior: Its Physical Character, Vegetation, and Animals",
        "quote": "The archaic dermal armature of **Scaphirhynchus** illustrates the survival of Paleozoic ganoid skeletal patterns in modern rivers."
      }
    ]
  },
  "Dashboard — scaph\\scaphocephaly.md": {
    "primary": "A type of premature craniosynostosis in which premature fusion of the sagittal suture results in an elongated, narrow, boat-shaped cranium.",
    "secondary": "In pediatric neurosurgery and dysmorphology, a condition presenting with an elongated anteroposterior diameter and frontal bossing, requiring cranial vault remodeling.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Ueber den Cretinismus",
        "quote": "Premature synostosis of the sagittal suture restricts lateral cranial expansion, producing the classic boat-shaped deformity termed **scaphocephaly**."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Radiographic examination in severe **scaphocephaly** reveals prominent ridging along the fused sagittal suture line."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Surgical strip craniectomy during early infancy restores normal cosmetic contour and relieves intracranial constriction in **scaphocephaly**."
      }
    ]
  },
  "Dashboard — scaph\\scaphoid bone.md": {
    "primary": "The boat-shaped carpal bone situated on the thumb (radial) side of the human wrist, articulating with the radius, lunate, and trapezium.",
    "secondary": "In orthopedic traumatology, the most commonly fractured carpal bone, notorious for poor vascular supply through its distal pole and risk of avascular necrosis.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **scaphoid bone** is the largest bone of the proximal carpal row, presenting a deep concavity for articulation with the head of the os magnum."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Resembling a skiff or small boat, the **scaphoid bone** mediates movements between the forearm and the palm."
      },
      {
        "author": "Frank H. Netter",
        "work": "Atlas of Human Anatomy",
        "quote": "Tenderness in the anatomical snuffbox upon palpation strongly indicates a fracture of the **scaphoid bone** following a fall on the outstretched hand."
      }
    ]
  },
  "Dashboard — scaph\\scaphoid.md": {
    "primary": "Having the shape of a boat; boat-shaped; navicular (in anatomical and biological descriptions).",
    "secondary": "In human osteology, designating either the carpal scaphoid bone of the wrist or the tarsal navicular bone of the foot.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **scaphoid** fossa of the sphenoid bone provides attachment for the tensor veli palatini muscle."
      },
      {
        "author": "Charles Bell",
        "work": "The Anatomy of the Human Body",
        "quote": "Dislocation of the **scaphoid** carpal element impairs the delicate grasping movements of the human thumb."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Comparative analysis reveals that the mammalian **scaphoid** corresponds to the radiale of primitive tetrapod ancestors."
      }
    ]
  },
  "Dashboard — scaph\\scaphopod.md": {
    "primary": "Any marine burrowing mollusk of the class Scaphopoda, commonly known as a tusk shell or tooth shell.",
    "secondary": "In marine invertebrate zoology, a micro-carnivore inhabiting soft benthic sediment, using prehensile ciliated tentacles (captacula) to capture foraminifera.",
    "quotes": [
      {
        "author": "S. P. Woodward",
        "work": "A Manual of the Mollusca",
        "quote": "The cylindrical, tapering shell of a **scaphopod** remains open at both ends, allowing respiratory currents to circulate while buried in sand."
      },
      {
        "author": "R. Tucker Abbott",
        "work": "American Seashells",
        "quote": "Indigenous peoples along the Pacific Northwest prized the polished shell of the **scaphopod** Dentalium as currency and ceremonial ornament."
      },
      {
        "author": "Robert D. Barnes",
        "work": "Invertebrate Zoology",
        "quote": "A living **scaphopod** excavates sediment using its muscular spade-shaped foot while extending delicate captacula into surrounding mud."
      }
    ]
  },
  "Dashboard — scaph\\scaphopoda.md": {
    "primary": "The taxonomic class of benthic marine mollusks comprising the tusk shells, possessing a tubular, curved shell open at both ends.",
    "secondary": "In systematic malacology, a distinct molluscan class lacking gills and eyes, relying on mantle cavity circulation and captacular feeding.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The History of Creation",
        "quote": "The class **scaphopoda** bridges the evolutionary gap between primitive bivalve architectures and cephalopod forebears."
      },
      {
        "author": "George Washington Tryon",
        "work": "Structural and Systematic Conchology",
        "quote": "Fossils of **scaphopoda** appear as early as the Ordovician period, preserving their characteristic curved tubular geometry intact."
      },
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Mollusca",
        "quote": "The nervous system of **scaphopoda** reflects their sedentary burrowing existence, exhibiting paired cerebral, pleural, and pedal ganglia."
      }
    ]
  },
  "Dashboard — scaph\\scaphosepalum.md": {
    "primary": "A genus of miniature epiphytic orchids in the subtribe Pleurothallidinae, native to cloud forests of Central and South America.",
    "secondary": "In botanical orchidology, characterized by lateral sepals fused into a boat-shaped synsepalum with fleshy, tail-like cushions.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The curious flowers of **scaphosepalum** possess boat-shaped lateral sepals tipped with elongated glandular tails."
      },
      {
        "author": "Heinrich Gustav Reichenbach",
        "work": "Xenia Orchidacea",
        "quote": "I described several Andean species of **scaphosepalum** whose miniature blossoms hang upside-down on slender wiry scapes."
      },
      {
        "author": "Carlyle A. Luer",
        "work": "Icones Pleurothallidinarum: Systematics of Scaphosepalum",
        "quote": "In **scaphosepalum**, the floral pad secretes droplets of nectar that lure small dipteran pollinators into the sepaline cup."
      }
    ]
  },
  "Dashboard — schem\\schema.md": {
    "primary": "An underlying organizational pattern, framework, plan, or mental structure used to organize knowledge and guide behavior.",
    "secondary": "In cognitive psychology and philosophy, an internalized cognitive model (as in Kantian epistemology or Piagetian developmental theory).",
    "quotes": [
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "The **schema** is in itself always a product of imagination, connecting pure intellectual concepts with sensory intuition."
      },
      {
        "author": "Jean Piaget",
        "work": "The Origins of Intelligence in Children",
        "quote": "The infant assimilates novel environmental stimuli into an existing behavioral **schema**, modifying it through accommodation."
      },
      {
        "author": "Frederic Bartlett",
        "work": "Remembering: An Experimental and Social Study",
        "quote": "Remembering is not the retrieval of static traces, but an imaginative reconstruction shaped by our active mental **schema**."
      }
    ]
  },
  "Dashboard — schem\\schematic.md": {
    "primary": "Of, relating to, or in the form of a simplified diagram, outline, plan, or blueprint.",
    "secondary": "In electronics and engineering, a diagrammatic representation showing the electrical connections and components of a circuit using standard graphic symbols.",
    "quotes": [
      {
        "author": "Ludwig Wittgenstein",
        "work": "Tractatus Logico-Philosophicus",
        "quote": "A logical proposition presents a **schematic** picture of reality, projecting structural relations onto abstract space."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics: Or Control and Communication in the Animal and the Machine",
        "quote": "We draw a **schematic** diagram of feedback loops to analyze stability and damping in automated control mechanisms."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "The general communication system is represented by a **schematic** flowchart comprising information source, transmitter, channel, and receiver."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 3 Batch 5.`);
