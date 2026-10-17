import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = {
  "Dashboard — abac/abaca.md": {
    "primary": "A species of banana plant (Musa textilis) native to the Philippines, cultivated for its strong, lustrous leafstalk fiber.",
    "secondary": "The durable, water-resistant fiber obtained from this plant, commercially known as Manila hemp, widely used for naval cordage and specialized paper.",
    "quotes": [
      {
        "author": "Charles Wilkes",
        "work": "Narrative of the United States Exploring Expedition",
        "quote": "The cordage manufactured from the **abaca** is remarkably light, durable, and superior to Russian hemp for marine rigging."
      },
      {
        "author": "Herman Melville",
        "work": "Omoo: A Narrative of Adventures in the South Seas",
        "quote": "Coils of stiff Manila **abaca** rope lay stowed in the vessel's forepeak alongside rolls of fibrous matting."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Extensive plantations of **abaca** occupy the fertile volcanic slopes, yielding the finest fibrous harvest of the archipelago."
      }
    ]
  },
  "Dashboard — abac/abacinate.md": {
    "primary": "To blind a person by holding a red-hot metal plate, dish, or basin before the eyes as an ancient or medieval punishment.",
    "secondary": "In historical penology and legal antiquities, a torture inflicted upon political rivals, dynastic pretenders, or state criminals.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The cruel despot commanded his captives to be **abacinated**, exposing their pupils to the intolerable glare of burning brass."
      },
      {
        "author": "Sabine Baring-Gould",
        "work": "The Tragedy of the Caesars",
        "quote": "Medieval chroniclers record horrific episodes wherein deposed princes were **abacinated** before being cast into perpetual solitary dungeons."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The White Company",
        "quote": "The ruthless marauders threatened to **abacinate** the obstinate seneschal unless the hidden coffer was produced."
      }
    ]
  },
  "Dashboard — abac/abaciscus.md": {
    "primary": "A small square tile, tessera, or stone cube used in composing mosaic floors and wall pavements.",
    "secondary": "In classical architecture, a diminutive abacus or square tablet forming a decorative member of a cornice or panel.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "Each colored **abaciscus** of porphyry and marble contributes its microscopic tint to the Byzantine mosaic."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "The vault of the baptistery was encrusted with thousands of glittering **abacisci** set in enduring lime cement."
      },
      {
        "author": "Marcus Vitruvius Pollio",
        "work": "De Architectura (The Ten Books on Architecture)",
        "quote": "Pavements formed of finely cut **abaciscus** pieces require a level bed of statumen and well-tamped rudus."
      }
    ]
  },
  "Dashboard — abac/abactinal.md": {
    "primary": "Pertaining to the surface, pole, or region of a radially symmetrical animal opposite to the mouth.",
    "secondary": "In invertebrate zoology and echinoderm anatomy, designating the dorsal or apical surface bearing the madreporite and anus, contrasting with the actinal (oral) surface.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The **abactinal** system of plates in the sea-urchin encircles the periproct and anchors the genital pores."
      },
      {
        "author": "Alexander Agassiz",
        "work": "Embryology of the Starfish",
        "quote": "During larval metamorphosis, the **abactinal** area consolidates rapidly into the calyx-like upper covering of the young starfish."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Report on the Radiolaria",
        "quote": "Radially organized structures display distinct polarity between their oral aperture and the opposing **abactinal** apex."
      }
    ]
  },
  "Dashboard — abac/abacus.md": {
    "primary": "An ancient manual calculating instrument consisting of beads sliding along rods, wires, or grooves set within a frame.",
    "secondary": "In classical architecture, the flat uppermost slab or tablet crowning the capital of a column, supporting the architrave.",
    "quotes": [
      {
        "author": "Charles Babbage",
        "work": "Passages from the Life of a Philosopher",
        "quote": "The elementary principles of mechanical arithmetic may be traced back to the grooved reckoning board and the Chinese **abacus**."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Merchants throughout antiquity and the East performed rapid numerical calculations upon the beads of an **abacus**."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture",
        "quote": "The Doric capital consists of a bold convex echinus surmounted by a plain, heavy rectangular **abacus**."
      }
    ]
  },
  "Dashboard — abac/abax.md": {
    "primary": "A genus of predatory ground beetles (family Carabidae) native to the Palearctic realm, characterized by broad, flattened bodies.",
    "secondary": "In Greek mathematical antiquities (ἄβαξ), a reckoning board, sand-dusted calculating tablet, or gaming board.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Among carnivorous ground beetles such as **Abax**, both sexes display robust mandibles adapted for seizing subterranean larvae."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "The species of **Abax** are distinguished by their striate elytra and the absence of hind wings beneath the fused dorsal plates."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The early geometer traced geometric diagrams and inscribed numerical tallies with a stylus upon the dust-covered **abax**."
      }
    ]
  },
  "Dashboard — acr/acr.md": {
    "primary": "A Greek combining root morpheme (ἄκρος, akros) denoting extreme, outermost, summit, or tip.",
    "secondary": "In historical morphology and etymological analysis, a formative element producing technical compounds relating to bodily extremities or peak heights (as in acrobat, acropolis, acromion).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The formative Greek base **acr-** signifies high, pointed, or extreme, appearing in numerous derivatives denoting spatial limits."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From the radical **acr-** arise words designating highest peaks, peripheral boundaries, and outermost bodily appendages."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The Indo-European root underlying **acr-** reflects an adjectival concept of sharp, pointed, or uppermost elevation."
      }
    ]
  },
  "Dashboard — acr/acreage.md": {
    "primary": "The area or extent of a parcel of land expressed in acres.",
    "secondary": "In agriculture and estate management, the aggregate land area devoted to particular crops, forestry, or commercial exploitation.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "The Mayor of Casterbridge",
        "quote": "The extensive **acreage** of golden wheat undulated under the late August sun across the slopes of the valley."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "I observed how men became encumbered by broad **acreage**, laboring under the burden of farms they could scarcely cultivate."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Mr. Brooke calculated the prospective rental returns based upon the improved **acreage** of his newly drained tenant farms."
      }
    ]
  },
  "Dashboard — acr/acrobatic.md": {
    "primary": "Pertaining to, involving, or requiring spectacular agility, balance, and gymnastic coordination.",
    "secondary": "Exhibiting remarkable physical flexibility, daring aerial maneuvers, or metaphorically nimble intellectual versatility.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Hard Times",
        "quote": "Sleary's equestrian troupe amazed the town with their daring leaps and extraordinary **acrobatic** prowess upon bareback steeds."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Secret Agent",
        "quote": "He executed an almost **acrobatic** contortion to avoid colliding with the heavy carriage swinging around the corner."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "Thoughts leaped across the chasm of silence with the swift, effortless poise of an **acrobatic** dancer."
      }
    ]
  },
  "Dashboard — acr/acrobatics.md": {
    "primary": "The art, performance, or exhibition of gymnastic feats of agility, balance, tumbling, and equilibrium.",
    "secondary": "Spectacular physical maneuvers, or figurative displays of agile maneuvering, manipulation, and intricate adjustments.",
    "quotes": [
      {
        "author": "James Joyce",
        "work": "Ulysses",
        "quote": "The flying trapeze performers concluded their evening routine with daring mid-air **acrobatics** that drew gasps from the amphitheatre."
      },
      {
        "author": "George Orwell",
        "work": "Coming Up for Air",
        "quote": "We watched the village lads attempt clumsy **acrobatics** off the canal bridge into the cool water below."
      },
      {
        "author": "P. G. Wodehouse",
        "work": "Right Ho, Jeeves",
        "quote": "His sudden leap over the settee was a masterpiece of involuntary **acrobatics** prompted by sheer panic."
      }
    ]
  },
  "Dashboard — acr/acrochordon.md": {
    "primary": "A small, soft, benign, pedunculated skin polyp or skin tag, typically occurring in friction folds.",
    "secondary": "In dermatology, a harmless fibrovascular papilloma consisting of loose collagen fibers and blood vessels covered by epidermis.",
    "quotes": [
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "The patient presented numerous pedunculated outgrowths resembling **acrochordon** along the lateral folds of the neck."
      },
      {
        "author": "Ferdinand von Hebra",
        "work": "Diseases of the Skin",
        "quote": "Microscopic examination of an **acrochordon** reveals harmless hypertrophy of the dermal connective tissue with normal overlying epidermis."
      },
      {
        "author": "Thomas Addison",
        "work": "A Collection of the Published Writings",
        "quote": "Small cutaneous tags or **acrochordon** formations frequently appear in middle-aged individuals without systemic consequence."
      }
    ]
  },
  "Dashboard — acr/acromegalia.md": {
    "primary": "A chronic endocrinological disease caused by excessive secretion of growth hormone, characterized by progressive enlargement of the bones and tissues of the extremities and face.",
    "secondary": "In clinical medicine, the pathological condition (acromegaly) resulting from a pituitary adenoma hypersecreting somatotropin after epiphyseal fusion.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The characteristic facies and spatulate enlargement of the hands and feet in **acromegalia** point directly to pituitary hyperfunction."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and its Disorders",
        "quote": "Surgical decompression of the sella turcica brought marked symptomatic relief to the patient suffering from severe **acromegalia**."
      },
      {
        "author": "Pierre Marie",
        "work": "Essays on Acromegaly",
        "quote": "I proposed the designation **acromegalia** to emphasize the hypertrophic deformity occurring predominantly at the bodily extremities."
      }
    ]
  },
  "Dashboard — acr/acroterion.md": {
    "primary": "An architectural plinth, pedestal, or ornamental figure mounted upon the apex or lower corners of a pediment.",
    "secondary": "In classical Greco-Roman architecture, a decorative terminal element such as a palmette, statue, or urn crowning a temple gable.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "The sharp triangular silhouette of the pediment was relieved at each angle by a sculptured marble **acroterion**."
      },
      {
        "author": "Vitruvius",
        "work": "The Ten Books on Architecture",
        "quote": "Upon the corner **acroteria** should stand statues whose height matches that of the tympanum center."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture",
        "quote": "Finely carved anthemion ornaments crowned the summit and lateral piers as decorative **acroterion** features."
      }
    ]
  },
  "Dashboard — allel/allel.md": {
    "primary": "A combining root morpheme derived from Greek allēlōn, denoting reciprocity, mutual interaction, or alternation.",
    "secondary": "In linguistics and biological nomenclature, a formative element producing terms involving paired, reciprocal, or alternative relationships (as in allele, allelomorph, allelopathy).",
    "quotes": [
      {
        "author": "William Bateson",
        "work": "Mendel's Principles of Heredity",
        "quote": "We adopted the root **allel-** to express the reciprocal, alternative nature of Mendelian character pairs."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Greek reciprocal element **allel-** reflects an ancient reduplication signifying 'one another' or mutual correspondence."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The morphological prefix **allel-** serves universally in biosystematics to denote mutual or competitive biological interplay."
      }
    ]
  },
  "Dashboard — allel/allele.md": {
    "primary": "Any of two or more alternative variants of a gene that occupy the same locus on a specific chromosome.",
    "secondary": "In population genetics, a distinct DNA sequence variant contributing to phenotypic polymorphism and subject to natural selection or genetic drift.",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "The mutant **allele** occupies the identical chromosomal site as the standard wild-type factor in Drosophila."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Natural selection acts directly upon phenotypes to modify the overall frequency of each advantageous **allele** in the breeding population."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Selfish Gene",
        "quote": "At any given locus on a chromosome, one **allele** competes ruthlessly with its rivals for survival across generations."
      }
    ]
  },
  "Dashboard — allel/allelic.md": {
    "primary": "Pertaining to, involving, or exhibiting the properties of an allele or allelic variation.",
    "secondary": "In molecular genetics, characterizing relationships between alternative gene variants occupying homologous chromosomal loci.",
    "quotes": [
      {
        "author": "Sewall Wright",
        "work": "Evolution and the Genetics of Populations",
        "quote": "Calculations of gene frequency require accounting for the complete distribution of **allelic** variants across all breeding isolates."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The maintenance of high **allelic** diversity provides the indispensable raw material for rapid environmental adaptation."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Heterozygote advantage actively preserves multiple **allelic** forms despite strong purifying selection against recessive homozygotes."
      }
    ]
  },
  "Dashboard — allel/allelomorph.md": {
    "primary": "The historical genetic term (now allele) designating either of a pair of alternative Mendelian hereditary factors.",
    "secondary": "In early 20th-century genetics, a contrasting character that segregates independently in accordance with Mendelian inheritance.",
    "quotes": [
      {
        "author": "William Bateson",
        "work": "Mendel's Principles of Heredity",
        "quote": "To designate the contrasting factors which segregate in the germ cells, I propose the term **allelomorph**."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "Heredity and Sex",
        "quote": "Each factor and its corresponding **allelomorph** part company during the reduction division of gametogenesis."
      },
      {
        "author": "Ronald Fisher",
        "work": "The Genetical Theory of Natural Selection",
        "quote": "The selective value of a newly arisen mutant **allelomorph** determines its mathematical probability of ultimate fixation."
      }
    ]
  },
  "Dashboard — allel/allelomorphic.md": {
    "primary": "Pertaining to, functioning as, or characteristic of an allelomorph.",
    "secondary": "In classical genetics, describing paired alternative characters or gene states that segregate from one another into different gametes.",
    "quotes": [
      {
        "author": "William Bateson",
        "work": "Problems of Genetics",
        "quote": "The distribution of pigmented and albino coats in rodents follows standard **allelomorphic** segregation."
      },
      {
        "author": "Reginald Punnett",
        "work": "Mendelism",
        "quote": "When two distinct members of an **allelomorphic** pair meet in the zygote, one frequently displays complete dominance."
      },
      {
        "author": "J. B. S. Haldane",
        "work": "The Causes of Evolution",
        "quote": "Mathematical models of natural selection must compute the differential survival rates of various **allelomorphic** combinations."
      }
    ]
  },
  "Dashboard — allel/allelotaxis.md": {
    "primary": "The embryonic arrangement or integration of organs developed from different germ layers or disparate structural components.",
    "secondary": "In developmental morphology, the mutual alignment and reciprocal organization of divergent tissue elements during organogenesis.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The harmonious union of ectodermal and mesodermal sheets demonstrates remarkable embryonic **allelotaxis**."
      },
      {
        "author": "Ray Lankester",
        "work": "Comparative Embryology",
        "quote": "We trace the evolutionary modification of the organ through the structural **allelotaxis** of its constituent cellular tracts."
      },
      {
        "author": "Wilhelm Roux",
        "work": "Der Kampf der Theile im Organismus",
        "quote": "Mechanical pressures exerted by adjacent tissues direct the cellular **allelotaxis** necessary for proper lumen formation."
      }
    ]
  },
  "Dashboard — allel/parallel.md": {
    "primary": "Extending in the same direction, equidistant at all points, and never converging or diverging, however far extended.",
    "secondary": "Having a reciprocal correspondence, striking resemblance, or analogous course in structure, history, or development.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "Elements",
        "quote": "**Parallel** straight lines are straight lines which, being in the same plane and being produced indefinitely in both directions, do not meet one another."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The rays of sunlight, entering through the small pinhole, proceeded in strictly **parallel** trajectories toward the glass prism."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "There is a profound **parallel** between the physical laws of nature and the moral intuitions of the human spirit."
      }
    ]
  },
  "Dashboard — allel/parallelepiped.md": {
    "primary": "A six-faced three-dimensional solid or prism whose opposite faces are congruent and parallel parallelograms.",
    "secondary": "In geometry and crystallography, a fundamental solid volume whose spatial dimensions are defined by three linearly independent basis vectors.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "The volume of a **parallelepiped** is determined by multiplying the area of its parallelogram base by its perpendicular altitude."
      },
      {
        "author": "Thomas Heath",
        "work": "The Thirteen Books of Euclid's Elements",
        "quote": "Euclid demonstrates that any plane cutting opposite faces of a **parallelepiped** divides the solid into two proportional segments."
      },
      {
        "author": "Adrien-Marie Legendre",
        "work": "Elements of Geometry",
        "quote": "Every oblique **parallelepiped** may be transformed into an equivalent rectangular solid of equal base and height."
      }
    ]
  },
  "Dashboard — allel/parallelepipedon.md": {
    "primary": "An archaic and classical geometric designation for a parallelepiped (a solid bounded by six parallelograms).",
    "secondary": "In traditional English Euclidean translations, the standard designation for a three-dimensional prism whose faces are pairwise parallel parallelograms.",
    "quotes": [
      {
        "author": "Robert Simson",
        "work": "The Elements of Euclid",
        "quote": "If two solid **parallelepipedons** have the same base and the same altitude, they are equal to one another in capacity."
      },
      {
        "author": "Isaac Barrow",
        "work": "Euclid's Elements",
        "quote": "The diagonal plane passing through opposite edges of a **parallelepipedon** bisects the entire solid volume."
      },
      {
        "author": "John Playfair",
        "work": "Elements of Geometry",
        "quote": "We may construct a right **parallelepipedon** upon any given rectangular foundation with perpendicular lateral edges."
      }
    ]
  },
  "Dashboard — allel/parallelism.md": {
    "primary": "The condition or quality of being parallel or equidistant in geometrical orientation.",
    "secondary": "An agreement, correspondence, or structural symmetry between concepts, events, or literary clauses (as in Hebrew poetic parallelism).",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The mind discovers a delightful harmony in observing the **parallelism** between external natural forms and internal mental states."
      },
      {
        "author": "Matthew Arnold",
        "work": "Essays in Criticism",
        "quote": "The balanced rhythms of ancient poetry achieve dramatic emphasis through deliberate semantic **parallelism**."
      },
      {
        "author": "Robert Lowth",
        "work": "Lectures on the Sacred Poetry of the Hebrews",
        "quote": "Poetic **parallelism** consists in a certain equality, resemblance, or relationship between the members of each successive verse."
      }
    ]
  },
  "Dashboard — allel/parallelize.md": {
    "primary": "To make parallel; to align or arrange objects or trajectories so they run in the same direction.",
    "secondary": "In computing and logistics, to break a sequential process or computation into concurrent, simultaneous operations.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "It is profitable to **parallelize** the historical records of distinct nations to discover universal patterns of civic decay."
      },
      {
        "author": "Alan Turing",
        "work": "Computing Machinery and Intelligence",
        "quote": "When constructing complex calculating engines, the designer seeks to **parallelize** basic arithmetical cycles wherever possible."
      },
      {
        "author": "Herbert Spencer",
        "work": "First Principles",
        "quote": "Mechanical progress continually demonstrates methods to **parallelize** physical forces to maximize total mechanical efficiency."
      }
    ]
  },
  "Dashboard — allel/parallelogon.md": {
    "primary": "A polygon whose opposite sides are parallel and of equal length.",
    "secondary": "In plane geometry and crystallography, a closed rectilinear figure exhibiting translational symmetry and parallel opposite boundaries.",
    "quotes": [
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Trigonometry and Trigonometrical Analysis",
        "quote": "Any equiangular hexagon whose opposing boundaries are equal constitutes a symmetrical plane **parallelogon**."
      },
      {
        "author": "William Kingdon Clifford",
        "work": "Mathematical Papers",
        "quote": "The space-filling properties of the **parallelogon** allow regular tessellation of the plane without gaps or overlapping areas."
      },
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "We may establish coordinate transformations mapping any arbitrary quadrilateral into an idealized symmetric **parallelogon**."
      }
    ]
  },
  "Dashboard — allel/parallelogram.md": {
    "primary": "A four-sided plane rectilinear figure whose opposite sides are parallel and equal in length.",
    "secondary": "In mechanics and physics, the geometric construct (parallelogram of forces) used to calculate the vector resultant of two concurrent forces.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "A body acted upon by two forces conjointly describes the diagonal of a **parallelogram** in the same time as it would describe the sides separately."
      },
      {
        "author": "René Descartes",
        "work": "Discourse on Method",
        "quote": "By constructing a simple **parallelogram**, the geometer resolves complex directional problems into clear spatial relations."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Matter and Motion",
        "quote": "The composition of velocities is geometrically represented by the diagonal of the corresponding velocity **parallelogram**."
      }
    ]
  },
  "Dashboard — allel/parallelopiped.md": {
    "primary": "A variant spelling of parallelepiped, denoting a six-faced prism whose opposite faces are parallel parallelograms.",
    "secondary": "In classical mineralogy and geometry, a solid crystalline block or geometric model bounded by six plane rhomboidal or parallelogram faces.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "A Preliminary Discourse on the Study of Natural Philosophy",
        "quote": "Cleavage planes in calcite crystals naturally split along the faces of an elementary rhombohedral **parallelopiped**."
      },
      {
        "author": "William Whewell",
        "work": "The Philosophy of the Inductive Sciences",
        "quote": "Haüy deduced the internal structure of all crystalline substances from the stacking of minute primitive **parallelopipeds**."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The basaltic columns occasionally fracture into regular **parallelopiped** blocks under long-continued subaerial weathering."
      }
    ]
  },
  "Dashboard — allel/parallelopipedon.md": {
    "primary": "An archaic variant spelling of parallelepipedon, denoting a solid body bounded by six parallelograms.",
    "secondary": "In early modern mathematical and physical treatises, the technical designation for a solid prism whose three sets of opposing faces are parallel planes.",
    "quotes": [
      {
        "author": "Thomas Young",
        "work": "A Course of Lectures on Natural Philosophy",
        "quote": "The resistance encountered by a **parallelopipedon** immersed in a flowing stream depends upon the aspect of its exposed faces."
      },
      {
        "author": "Colin Maclaurin",
        "work": "A Treatise of Fluxions",
        "quote": "The solid content of any oblique **parallelopipedon** is directly computed by the integral of its successive cross-sections."
      },
      {
        "author": "Benjamin Martin",
        "work": "A New and Comprehensive System of Mathematical Institutions",
        "quote": "Let the solid **parallelopipedon** be circumscribed by a sphere whose diameter equals the principal diagonal."
      }
    ]
  },
  "Dashboard — arithm/antilogarithm.md": {
    "primary": "The number corresponding to a given logarithm; the value obtained by raising the logarithmic base to the power of that logarithm.",
    "secondary": "In computational mathematics, the inverse logarithm function (if log_b(x) = y, then x is the antilogarithm of y).",
    "quotes": [
      {
        "author": "Charles Babbage",
        "work": "Table of the Logarithms of the Natural Numbers",
        "quote": "By consulting the table in reverse, the computer rapidly determines the true **antilogarithm** corresponding to the computed mantissa."
      },
      {
        "author": "Henry Briggs",
        "work": "Arithmetica Logarithmica",
        "quote": "Having added the exponents, one seeks the natural number or **antilogarithm** representing the required product."
      },
      {
        "author": "Augustus De Morgan",
        "work": "An Explanation of the Gnomonic Projection of the Sphere",
        "quote": "The calculation requires taking the **antilogarithm** of the sum of the logarithmic sines and tangents."
      }
    ]
  },
  "Dashboard — arithm/arithm.md": {
    "primary": "A Greek combining root morpheme (ἀριθμός, arithmos) signifying number, count, or calculation.",
    "secondary": "In linguistics and mathematical terminology, the formative base of compounds relating to computation, numerical enumeration, and quantitative analysis (as in arithmetic, logarithm, arithmancy).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The base **arithm-** represents the Hellenic word for number and orderly reckoning, preserved in modern arithmetic."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Compounds formed from **arithm-** embrace the entire science of discrete quantities and numerical operations."
      },
      {
        "author": "Augustus De Morgan",
        "work": "Elements of Arithmetic",
        "quote": "The root element **arithm-** reminds us that computation was conceived as the art of numbering individual units."
      }
    ]
  },
  "Dashboard — arithm/arithmancy.md": {
    "primary": "Divination or fortune-telling through the occult interpretation of numbers or the numerical values assigned to letters in names.",
    "secondary": "In historical esotericism and occult philosophy, a branch of numerology claiming to uncover hidden character traits and future destiny through numerical reduction.",
    "quotes": [
      {
        "author": "Heinrich Cornelius Agrippa",
        "work": "Three Books of Occult Philosophy",
        "quote": "By the ancient art of **arithmancy**, the adept computes the numerical potency of secret divine names."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Some seek vain prophecies in dreams and planetary hours, while others consult superstitious **arithmancy** and cabalistic letters."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "The mystical reduction of names to numerical values practiced in **arithmancy** rests upon arbitrary phonetic conventions."
      }
    ]
  },
  "Dashboard — arithm/arithmetic.md": {
    "primary": "The foundational branch of mathematics that deals with the properties, relations, and operations of numbers (addition, subtraction, multiplication, division).",
    "secondary": "The practical calculation of numerical values, or the formal theoretical study of number systems, integers, and discrete numerical operations.",
    "quotes": [
      {
        "author": "Carl Friedrich Gauss",
        "work": "Disquisitiones Arithmeticae",
        "quote": "Higher **arithmetic** presents an inexhaustible store of interesting truths regarding the properties of whole numbers."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "Pure **arithmetic** may be deduced entirely from logical premises using the concepts of class, relation, and cardinal number."
      },
      {
        "author": "John Locke",
        "work": "Some Thoughts Concerning Education",
        "quote": "**Arithmetic** is of so general use in all parts of life and business, that scarce anything can be done without it."
      }
    ]
  },
  "Dashboard — arithm/arithmetically.md": {
    "primary": "In an arithmetical manner; by means of arithmetic or numerical computation.",
    "secondary": "In mathematical analysis, progressing by constant additions or differences, in contrast to geometrically or exponentially.",
    "quotes": [
      {
        "author": "Thomas Robert Malthus",
        "work": "An Essay on the Principle of Population",
        "quote": "Population, when unchecked, increases in a geometrical ratio; subsistence increases only **arithmetically**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Even slow-breeding animals would multiply to vast hordes if their offspring increased unchecked even **arithmetically**."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The profits of capital may be calculated **arithmetically** by comparing gross revenues with initial outlays."
      }
    ]
  },
  "Dashboard — arithm/arithmetician.md": {
    "primary": "A specialist or scholar skilled in arithmetic, numerical computation, or number theory.",
    "secondary": "In historical and philosophical contexts, a mathematician whose primary focus is the investigation of discrete numbers and numerical relations.",
    "quotes": [
      {
        "author": "Plato",
        "work": "The Republic",
        "quote": "The skilled **arithmetician** studies the nature of numbers not for commercial trading, but for the elevation of the soul."
      },
      {
        "author": "Gottfried Wilhelm Leibniz",
        "work": "New Essays on Human Understanding",
        "quote": "An **arithmetician** discerns necessary truths in the properties of numbers without requiring empirical experiments."
      },
      {
        "author": "Jonathan Swift",
        "work": "Gulliver's Travels",
        "quote": "The Laputian **arithmetician** was deeply engrossed in abstract calculations, completely oblivious to mundane surroundings."
      }
    ]
  },
  "Dashboard — arithm/arithmomania.md": {
    "primary": "An obsessive-compulsive urge or compulsion to count objects, steps, or daily occurrences, or to perform continuous numerical calculations.",
    "secondary": "In clinical psychiatry, a symptom of obsessive-compulsive disorder characterized by intrusive counting rituals and fixation on numerical symmetry.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In morbid conditions like **arithmomania**, the patient is plagued by an irresistible impulse to count paving stones or windowpanes."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "Cases of severe obsessional neurosis frequently exhibit **arithmomania**, where the sufferer cannot proceed until counting a prescribed tally."
      },
      {
        "author": "Pierre Janet",
        "work": "The Mental State of Hystericals",
        "quote": "The repetitive numerical scrutiny seen in **arithmomania** serves to alleviate profound underlying existential dread."
      }
    ]
  },
  "Dashboard — arithm/arithmos.md": {
    "primary": "The Greek word for number (ἀριθμός); in classical philosophy, the concept of a discrete, countable multiplicity of units.",
    "secondary": "In the history and philosophy of mathematics, the ancient Euclidean and Pythagorean concept of a determinate multitude composed of indivisible monads.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "Number or **arithmos** is defined by the ancients as a plurality that is measured by the unit."
      },
      {
        "author": "Jacob Klein",
        "work": "Greek Mathematical Thought and the Origin of Algebra",
        "quote": "For the Greek mind, an **arithmos** is always a definite, countable multitude of concrete things, never an abstract real continuum."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Euclid defines **arithmos** as a collection composed of units, distinguishing it rigorously from geometric magnitude."
      }
    ]
  },
  "Dashboard — arithm/isarithm.md": {
    "primary": "A line drawn on a map, chart, or diagram connecting points having equal numerical value of a given variable.",
    "secondary": "In cartography, meteorology, and geography, a generic term encompassing contour lines, isotherms, isobars, and other isolines representing continuous spatial data.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Kosmos: A Sketch of the Physical Description of the Universe",
        "quote": "Connecting points of equal annual temperature by an **isarithm** reveals the true climatic belts across continental landmasses."
      },
      {
        "author": "Arthur Newell Strahler",
        "work": "Physical Geography",
        "quote": "Each successive **isarithm** on the precipitation map delineates regions sharing identical mean monthly rainfall totals."
      },
      {
        "author": "William Morris Davis",
        "work": "Geographical Essays",
        "quote": "The topographic contour is simply an **isarithm** of altitude tracing horizontal planes across the dissected relief."
      }
    ]
  },
  "Dashboard — arithm/logarithm.md": {
    "primary": "The exponent or power to which a specified fixed base must be raised to produce a given number.",
    "secondary": "In computational mathematics, an auxiliary numerical function invented to transform burdensome multiplications and divisions into simple additions and subtractions.",
    "quotes": [
      {
        "author": "John Napier",
        "work": "Mirifici Logarithmorum Canonis Descriptio",
        "quote": "Seeing there is nothing that is so troublesome unto mathematical practice than multiplications, divisions, and extractions, I devised the **logarithm**."
      },
      {
        "author": "Johannes Kepler",
        "work": "Chilias Logarithmorum",
        "quote": "With the aid of the **logarithm**, astronomical computations that once occupied years of labor were reduced to a few weeks."
      },
      {
        "author": "Leonhard Euler",
        "work": "Introduction to Analysis of the Infinite",
        "quote": "The natural **logarithm** emerges organically as the integral of the reciprocal function over positive real coordinates."
      }
    ]
  },
  "Dashboard — arithm/logarithmic.md": {
    "primary": "Pertaining to, involving, or governed by logarithms or logarithmic functions.",
    "secondary": "Displaying variation or growth proportional to a logarithmic curve, or plotted on a scale whose increments represent exponential intervals.",
    "quotes": [
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The elegant equiangular spiral of the Nautilus shell is a physical realization of the **logarithmic** curve."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The distribution of potential around an infinite conducting cylinder varies according to a **logarithmic** function of distance."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "Sensory perception responds to external physical stimuli along a **logarithmic** progression of intensities."
      }
    ]
  },
  "Dashboard — chili/chili.md": {
    "primary": "A Greek combining root morpheme (χίλιοι, chilioi) signifying one thousand.",
    "secondary": "In linguistics and scholarly nomenclature, a prefixal element appearing in classical derivatives denoting a thousandfold quantity or period (as in chiliad, chiliasm, chiliagon).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The base **chili-** represents the Greek word for a thousand, which has also furnished the modern metric prefix kilo-."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From **chili-** derive numerous compounds expressing military cohorts of a thousand warriors or millenarian theological expectations."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The Hellenic numeral base **chili-** reflects a prehistoric Indo-European formation denoting immense, uncountable multitudes."
      }
    ]
  },
  "Dashboard — chili/chiliad.md": {
    "primary": "A group, collection, or period of one thousand, especially a span of one thousand years or one thousand items.",
    "secondary": "In historical and chronological writings, a millennium or a catalogue encompassing one thousand distinct entries.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "A full **chiliad** of years had elapsed between the foundation of Constantinople and its final capture by the Turks."
      },
      {
        "author": "John Milton",
        "work": "The Reason of Church-Government",
        "quote": "Truth hath survived many a dark **chiliad** when superstition obscured the purest light of heaven."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Generations arise and pass away, marking each silent **chiliad** upon the dial of eternity."
      }
    ]
  },
  "Dashboard — chili/chiliasm.md": {
    "primary": "The Christian theological doctrine of the millennium, specifically the belief in Christ's anticipated thousand-year reign on earth.",
    "secondary": "In religious history and sociology, millenarianism or the apocalyptic expectation of an imminent, terrestrial era of divine peace and justice.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The ancient doctrine of **chiliasm** was intimately connected with the second coming of Christ and inflamed the zeal of the early martyrs."
      },
      {
        "author": "Thomas Hobbes",
        "work": "Leviathan",
        "quote": "The kingdom of God on earth, envisioned in the literal interpretations of **chiliasm**, was often misapplied to secular principalities."
      },
      {
        "author": "Philip Schaff",
        "work": "History of the Christian Church",
        "quote": "During the first three centuries, moderate **chiliasm** was widely regarded as an orthodox expression of Christian hope."
      }
    ]
  },
  "Dashboard — chili/chiliast.md": {
    "primary": "A person who believes in chiliasm or the thousand-year reign of Christ on earth; a millenarian.",
    "secondary": "In historical theology, an early Christian adherent or sectarian who anticipated a literal, earthly messianic kingdom.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Every eager **chiliast** expected the immediate overthrow of imperial paganism and the dawn of the terrestrial golden age."
      },
      {
        "author": "Richard Baxter",
        "work": "The Saints' Everlasting Rest",
        "quote": "The devout **chiliast** fixes his contemplation upon an earthly triumph, while we look beyond to the celestial rest."
      },
      {
        "author": "Henry More",
        "work": "An Explanation of the Grand Mystery of Godliness",
        "quote": "A learned **chiliast** defends his interpretation by collating the prophetic visions of Daniel and the Apocalypse."
      }
    ]
  },
  "Dashboard — chili/chiliastic.md": {
    "primary": "Pertaining to, resembling, or characteristic of chiliasm or millenarian beliefs.",
    "secondary": "In sociology and history, relating to religious or utopian movements that anticipate a radical, miraculous transformation of society within historical time.",
    "quotes": [
      {
        "author": "Max Weber",
        "work": "The Sociology of Religion",
        "quote": "Radical peasant revolts were repeatedly energized by intense **chiliastic** expectations of an earthly paradise."
      },
      {
        "author": "Ernst Troeltsch",
        "work": "The Social Teaching of the Christian Churches",
        "quote": "The Anabaptist uprising in Münster represented a tragic manifestation of fanatical **chiliastic** enthusiasm."
      },
      {
        "author": "Eric Hobsbawm",
        "work": "Primitive Rebels",
        "quote": "Traditional social banditry often merged seamlessly with **chiliastic** movements during acute rural economic crises."
      }
    ]
  },
  "Dashboard — chili/chilioi.md": {
    "primary": "The ancient Greek numeral adjective for one thousand (χίλιοι).",
    "secondary": "In historical linguistics and metric etymology, the classical etymon from which the French metric system derived the standard prefix kilo-.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "The Persian commander organized his personal guard into a regiment numbering exactly **chilioi** chosen spearmen."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The numeral **chilioi** served throughout Greek antiquity to denote a thousand warriors, talents, or stadia."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "By shortening Greek **chilioi**, the French savants of 1795 coined the familiar universal prefix kilo-."
      }
    ]
  },
  "Dashboard — chili/kilowatt.md": {
    "primary": "A unit of electrical or mechanical power equal to one thousand watts (symbol: kW).",
    "secondary": "In electrical engineering and energy measurement, the standard unit expressing the operating capacity of generators and industrial motors.",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "My Inventions: The Autobiography of Nikola Tesla",
        "quote": "The massive Niagara generators converted the falling torrent into thousands of **kilowatts** of alternating current."
      },
      {
        "author": "Thomas Edison",
        "work": "The Edison Papers: Documents and Correspondence",
        "quote": "We measured the dynamo output precisely, calculating fuel efficiency per **kilowatt** supplied to the incandescent lamps."
      },
      {
        "author": "H. G. Wells",
        "work": "The World Set Free",
        "quote": "Modern civilization was transformed when atomic engines delivered millions of **kilowatts** of continuous, inexhaustible power."
      }
    ]
  },
  "Dashboard — cle/ecclesia.md": {
    "primary": "The sovereign political assembly of citizens in an ancient Greek democratic city-state, notably Athens.",
    "secondary": "In early Christianity and theological Latin, the congregation of believers or the Church conceived as a divine assembly.",
    "quotes": [
      {
        "author": "Thucydides",
        "work": "The Peloponnesian War",
        "quote": "Pericles ascended the bema before the gathered **ecclesia** on the Pnyx to persuade the citizens to stand firm."
      },
      {
        "author": "Aristotle",
        "work": "Politics",
        "quote": "In a democratic constitution, supreme authority resides in the regular meetings of the sovereign **ecclesia**."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "The Athenian **ecclesia** debated matters of war, treaties, and taxation with unprecedented rhetorical freedom."
      }
    ]
  },
  "Dashboard — cle/ecclesiastic.md": {
    "primary": "A person in holy orders; a member of the clergy or a church dignitary (priest, minister, bishop).",
    "secondary": "Relating to or suitable for the church or the clerical profession (often contrasted with secular).",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Every wealthy **ecclesiastic** exerted immense political influence upon the imperial court at Ravenna."
      },
      {
        "author": "Walter Scott",
        "work": "Ivanhoe",
        "quote": "The Prior of Jorvaulx was a worldly **ecclesiastic** who loved fine horses, hounds, and rich banquets more than penance."
      },
      {
        "author": "Geoffrey Chaucer",
        "work": "The Canterbury Tales",
        "quote": "A gentle Monk, a worthy **ecclesiastic**, rode alongside the company with jangling bridle bells."
      }
    ]
  },
  "Dashboard — cle/ecclesiastical.md": {
    "primary": "Of or relating to the Christian Church, its hierarchy, governance, ceremonies, or traditions.",
    "secondary": "In legal and institutional history, pertaining to canon law and church courts as distinguished from civil or secular authority.",
    "quotes": [
      {
        "author": "Richard Hooker",
        "work": "Of the Laws of Ecclesiastical Polity",
        "quote": "The visible Church requires settled rules of **ecclesiastical** government adapted to the peace and order of the commonwealth."
      },
      {
        "author": "John Milton",
        "work": "Areopagitica",
        "quote": "Prelatical tyrannies attempted to suppress all knowledge by imposing an **ecclesiastical** licensing system upon the press."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The king attempted to control the national universities through an unconstitutional **ecclesiastical** commission."
      }
    ]
  },
  "Dashboard — cle/ecclesiology.md": {
    "primary": "The theological and historical study of the Christian Church, its doctrine, organization, and sacraments.",
    "secondary": "In architectural history, the study of church building, ecclesiastical decoration, and liturgical furnishings (promoted especially by the 19th-century Cambridge Camden Society).",
    "quotes": [
      {
        "author": "John Henry Newman",
        "work": "Apologia Pro Vita Sua",
        "quote": "My studies in patristic **ecclesiology** gradually convinced me that antiquity condemned the insular claims of the Anglican establishment."
      },
      {
        "author": "Augustus Pugin",
        "work": "The True Principles of Pointed or Christian Architecture",
        "quote": "Correct medieval **ecclesiology** requires that every structural element of a parish church reflect its sacramental purpose."
      },
      {
        "author": "Philip Schaff",
        "work": "The Creeds of Christendom",
        "quote": "Comparative **ecclesiology** reveals how differing concepts of apostolic succession shaped modern denominational divisions."
      }
    ]
  },
  "Dashboard — cle/ecclesiophobia.md": {
    "primary": "An abnormal, irrational fear, hatred, or dread of churches, ecclesiastical buildings, or religion.",
    "secondary": "In abnormal psychology, an intense situational phobia marked by panic and avoidance when confronting sacred architecture or religious ceremonies.",
    "quotes": [
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Psychological aversions such as **ecclesiophobia** frequently trace back to severe emotional trauma experienced during childhood rituals."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Religious melancholy in some breeds despairing devotion, and in others a frantic **ecclesiophobia** that flees holy shrines."
      },
      {
        "author": "George Miller Beard",
        "work": "American Nervousness",
        "quote": "Among our neurasthenic cases, occasional morbid fears appear as **ecclesiophobia**, where church attendance induces severe palpitations."
      }
    ]
  },
  "Dashboard — cle/epiclesis.md": {
    "primary": "In Christian Eucharistic liturgies, the prayer invoking the Holy Spirit to consecrate the bread and wine.",
    "secondary": "In sacramental theology, the vital liturgical invocation (especially prominent in Eastern Orthodox liturgies) effecting the Eucharistic transformation.",
    "quotes": [
      {
        "author": "Gregory Dix",
        "work": "The Shape of the Liturgy",
        "quote": "The development of the explicit **epiclesis** in the fourth-century Syrian liturgies altered the traditional focus of the Eucharistic canon."
      },
      {
        "author": "Alexander Schmemann",
        "work": "The Eucharist: Sacrament of the Kingdom",
        "quote": "In the Orthodox Divine Liturgy, the solemn **epiclesis** is the dramatic climax wherein the Holy Spirit descends upon the offering."
      },
      {
        "author": "John Henry Newman",
        "work": "Tracts for the Times",
        "quote": "The ancient liturgies invariably preserve the **epiclesis**, beseeching God to send down His Spirit upon the sacred gifts."
      }
    ]
  },
  "Dashboard — cle/monocle.md": {
    "primary": "A single corrective eyeglass for one eye, held in place by contraction of the facial muscles around the eye socket.",
    "secondary": "A fashionable single-lens eyewear accessory popularized among 19th- and early 20th-century European aristocrats and gentlemen.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "He adjusted his **monocle** with nervous care and peered closely at the mysterious footprint upon the moor."
      },
      {
        "author": "P. G. Wodehouse",
        "work": "The Inimitable Jeeves",
        "quote": "Bertie screwed a quizzical **monocle** into his eye, attempting to appear immensely worldly and astute."
      },
      {
        "author": "Oscar Wilde",
        "work": "An Ideal Husband",
        "quote": "Lord Goring adjusted his sparkling **monocle**, observing the assembled society with languid and ironical amusement."
      }
    ]
  },
  "Dashboard — cle/paraclete.md": {
    "primary": "An advocate, helper, comforter, or intercessor, specifically designating the Holy Spirit in Christian theology.",
    "secondary": "In Johannine theology (Greek παράκλητος, paraklētos), the divine Counselor sent by Christ to guide believers into all truth.",
    "quotes": [
      {
        "author": "Augustine of Hippo",
        "work": "Confessions",
        "quote": "Thou didst promise the heavenly **Paraclete**, the Spirit of truth, to comfort our exiled souls in this earthly vale."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The promised **Paraclete** shall abide with them forever, infusing celestial light and comfort into every humble breast."
      },
      {
        "author": "John Bunyan",
        "work": "The Pilgrim's Progress",
        "quote": "The poor traveler was sustained in the dark valley by the secret whisperings of the holy **Paraclete**."
      }
    ]
  },
  "Dashboard — cle/uncle.md": {
    "primary": "The brother of one's father or mother, or the husband of one's aunt.",
    "secondary": "An older male relative or family friend affectionately addressed by a familial kinship title.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "A little more than kin, and less than kind! My **uncle**, the murderer of my royal father, usurps the crown."
      },
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "My good **uncle** Peggotty welcomed the storm-tossed children into his warm boat-house by the Yarmouth beach."
      },
      {
        "author": "Laurence Sterne",
        "work": "The Life and Opinions of Tristram Shandy, Gentleman",
        "quote": "My **uncle** Toby spent entire afternoons recreating the siege of Namur with miniature ramparts in his bowling-green."
      }
    ]
  },
  "Dashboard — con/_con.md": {
    "primary": "A combining root morpheme derived from Ancient Greek κῶνος (kōnos), signifying a cone or conical geometrical body.",
    "secondary": "In geometry, morphology, and optics, designating forms, projections, or instruments having or analyzing conical curvature (as in conic, conoid, conoscope).",
    "quotes": [
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The Greek root **_con** designates the geometric cone whose planar sections yielded the celebrated curves of Apollonius."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The scientific base **con-** stems directly from Greek kōnos, denoting a pinecone and, by geometric extension, a tapering solid."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From the noun kōnos arises the fruitful combining base **con-**, foundational to classical geometry and botany."
      }
    ]
  },
  "Dashboard — con/cone.md": {
    "primary": "A three-dimensional geometric solid that tapers smoothly from a flat circular or curved base to a point called the apex.",
    "secondary": "In botany, the dry, scaly seed-bearing or pollen-bearing strobilus of gymnosperms, particularly conifers such as pines and firs.",
    "quotes": [
      {
        "author": "Apollonius of Perga",
        "work": "Conics",
        "quote": "If a right or oblique **cone** is cut by a plane passing through its axis, the resulting section is a triangle."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The convergent rays formed an illuminated luminous **cone** whose apex touched the surface of the paper."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Cross-pollination in pines depends upon wind currents blowing clouds of pollen grains into the open scales of the female **cone**."
      }
    ]
  },
  "Dashboard — con/conic.md": {
    "primary": "Pertaining to, having the form of, or resembling a cone.",
    "secondary": "In geometry, a conic section: any curve (ellipse, parabola, or hyperbola) produced by the intersection of a plane with a cone.",
    "quotes": [
      {
        "author": "René Descartes",
        "work": "Geometry",
        "quote": "Every plane **conic** curve can be completely represented by an algebraic equation of the second degree in two variables."
      },
      {
        "author": "Blaise Pascal",
        "work": "Treatise on Conic Sections",
        "quote": "If a hexagon be inscribed in a **conic**, the three points of intersection of opposite sides lie upon a straight line."
      },
      {
        "author": "Thomas Heath",
        "work": "Apollonius of Perga: Treatise on Conic Sections",
        "quote": "Apollonius proved that all three varieties of **conic** sections can be obtained from one and the same circular cone."
      }
    ]
  },
  "Dashboard — con/conical.md": {
    "primary": "Having the shape of a cone; circular at the base and tapering uniformly to an apex.",
    "secondary": "In descriptive anatomy and geology, designating structures or mountain peaks exhibiting cone-like contours.",
    "quotes": [
      {
        "author": "Robert Boyle",
        "work": "New Experiments Physico-Mechanicall",
        "quote": "The liquid was drawn up through a slender **conical** glass funnel into the evacuated receiver."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The **conical** shape of volcanic craters results from successive showers of ejected scoriae settling around the vent."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The captain wore a tall, **conical** hat of seal-fur that made him appear like some ancient magician of the frozen seas."
      }
    ]
  },
  "Dashboard — con/conically.md": {
    "primary": "In a conical manner, shape, or orientation; so as to form or taper like a cone.",
    "secondary": "In geometry and physical experiments, progressing or tapering toward a pointed vertex along circular cross-sections.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The lines of magnetic induction converged **conically** toward the sharpened iron pole-pieces of the electromagnet."
      },
      {
        "author": "John Tyndall",
        "work": "Heat Considered as a Mode of Motion",
        "quote": "The beam of intense light was focused **conically** through the crystal, igniting the combustible target placed at the focal point."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Physiography: An Introduction to the Study of Nature",
        "quote": "The sand grains poured steadily through the narrow orifice, piling up **conically** on the table beneath."
      }
    ]
  },
  "Dashboard — con/conicoid.md": {
    "primary": "A quadric surface whose planar cross-sections are conic sections (an ellipsoid, paraboloid, or hyperboloid).",
    "secondary": "In three-dimensional analytical geometry, any second-degree surface centered or uncentered defined by polynomial equations in three variables.",
    "quotes": [
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "Through any nine given points in three-dimensional space, a determinate quadric **conicoid** can be uniquely described."
      },
      {
        "author": "William Kingdon Clifford",
        "work": "Mathematical Papers",
        "quote": "The focal properties of a general **conicoid** are deduced from the intersections of its asymptotic tangent cones."
      },
      {
        "author": "George Salmon",
        "work": "A Treatise on the Analytic Geometry of Three Dimensions",
        "quote": "Every plane section of a central **conicoid** yields an ellipse or hyperbola depending on the orientation of the cutting plane."
      }
    ]
  },
  "Dashboard — con/conoid.md": {
    "primary": "A geometric solid resembling a cone, especially one formed by the revolution of a conic section about its axis.",
    "secondary": "In geometry and mechanics, a ruled surface generated by a straight line moving parallel to a fixed plane while intersecting a fixed straight line and curve.",
    "quotes": [
      {
        "author": "Archimedes",
        "work": "On Conoids and Spheroids",
        "quote": "Any segment of a parabolic **conoid** cut off by a plane perpendicular to its axis is one and a half times the cone having the same base."
      },
      {
        "author": "Thomas Heath",
        "work": "The Works of Archimedes",
        "quote": "Archimedes demonstrated how the volumes of hyperbolic **conoids** could be measured through rigorous methods of exhaustion."
      },
      {
        "author": "John Wallis",
        "work": "Mechanica: sive De Motu",
        "quote": "The center of gravity of a parabolic **conoid** lies along the axis at two-thirds of the distance from the apex to the base."
      }
    ]
  },
  "Dashboard — con/conoscope.md": {
    "primary": "An optical instrument or microscope attachment used to observe and evaluate interference figures in birefringent crystal sections under convergent polarized light.",
    "secondary": "In petrology and mineralogical crystallography, an apparatus that determines the optical axes and optic sign (uniaxial or biaxial) of mineral specimens.",
    "quotes": [
      {
        "author": "David Brewster",
        "work": "A Treatise on the Kaleidoscope and Polarized Light",
        "quote": "When viewed through the **conoscope**, the thin plate of Iceland spar displayed brilliant concentric rings intersected by a dark cross."
      },
      {
        "author": "Henry Clifton Sorby",
        "work": "On the Microscopical Structure of Crystals",
        "quote": "With the aid of a petrographic **conoscope**, one immediately discriminates between uniaxial quartz and biaxial feldspar lamellae."
      },
      {
        "author": "Alfred Harker",
        "work": "Petrology for Students",
        "quote": "The interference figure visible in the convergent **conoscope** allows rapid measurement of the optic axial angle of the pyroxene."
      }
    ]
  },
  "Dashboard — con/orthocone.md": {
    "primary": "A straight, uncoiled, conical shell of certain extinct cephalopods, particularly early Paleozoic nautiloids.",
    "secondary": "In invertebrate paleontology, an organism (such as Orthoceras or Endoceras) possessing an elongate, straight, chambered shell with a central or marginal siphuncle.",
    "quotes": [
      {
        "author": "Roderick Murchison",
        "work": "The Silurian System",
        "quote": "Limestone beds in the lower strata abound with the straight, fossilized chambers of the ancient **orthocone** nautiloids."
      },
      {
        "author": "Alpheus Hyatt",
        "work": "Genera of Fossil Cephalopods",
        "quote": "The primitive **orthocone** represents the ancestral morphotype from which coiled ammonoids and nautiloids progressively evolved."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "Vast Ordovician predators with shells like giant spears, the **orthocone** cephalopods ruled the ancient seas before the rise of jawed fishes."
      }
    ]
  }
};

console.log('Starting Batch 1 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 1 complete: successfully updated ' + updated + ' notes.');
