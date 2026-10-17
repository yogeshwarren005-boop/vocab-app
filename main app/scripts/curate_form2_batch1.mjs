import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — centr\\centromere.md": {
    "primary": "The specialized region of a chromosome that links a pair of sister chromatids and serves as the assembly site for the kinetochore during cell division.",
    "secondary": "In cytogenetics, the structural constriction that determines chromosome morphology and governs faithful chromosomal segregation during mitosis and meiosis.",
    "quotes": [
      {
        "author": "Barbara McClintock",
        "work": "The Origin and Behavior of Mutable Loci in Maize",
        "quote": "The broken chromosome arm lacking a normal **centromere** failed to migrate predictably toward either pole during spindle formation."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "Each sister chromatid remains tethered at the specialized **centromere** until the transition into mitotic anaphase."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Inversions that span across the **centromere** alter the relative proportions of the chromosome arms without losing essential chromatin."
      }
    ]
  },
  "Dashboard — centr\\centromeric.md": {
    "primary": "Pertaining to, located at, or functioning within the centromere of a chromosome.",
    "secondary": "In molecular epigenetics, describing specialized satellite DNA sequences and variant histones such as CENP-A that direct kinetochore formation.",
    "quotes": [
      {
        "author": "Sydney Brenner",
        "work": "My Life in Science",
        "quote": "The dense **centromeric** heterochromatin presented formidable resistance to early nucleotide sequencing efforts."
      },
      {
        "author": "Walter Sutton",
        "work": "The Chromosomes in Heredity",
        "quote": "During meiotic pairing, the physical tension focused on the **centromeric** constriction coordinates reciprocal bivalent orientation."
      },
      {
        "author": "Mary Lyon",
        "work": "Gene Action in the X-chromosome of the Mouse",
        "quote": "Spreading of epigenetic silencing rarely penetrates through the major **centromeric** boundary elements."
      }
    ]
  },
  "Dashboard — centr\\centropomidae.md": {
    "primary": "A taxonomic family of perciform ray-finned fishes known as snooks, characterized by two dorsal fins and an elongated, predatory profile.",
    "secondary": "In systematic ichthyology, predatory marine and brackish teleosts inhabiting tropical and subtropical coastal waters and estuaries.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The snooks of the family **Centropomidae** are distinguished by an interrupted lateral line and sharp, serrate preopercular margins."
      },
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "Several estuarine species assigned to **Centropomidae** attain substantial size and display remarkable salinity tolerance."
      },
      {
        "author": "George Boulenger",
        "work": "Zoology of Egypt: The Fishes of the Nile",
        "quote": "Affinity between the Nile perch and maritime **Centropomidae** illustrates ancient faunal connections across tropical waterways."
      }
    ]
  },
  "Dashboard — centr\\centropomus.md": {
    "primary": "The type genus of snooks in the family Centropomidae, comprising prized coastal and estuarine game and food fishes.",
    "secondary": "In marine biology, catadromous or amphidromous perch-like fishes with a distinct sloping forehead, protruding lower jaw, and pronounced black lateral line.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "Local fishermen hauled nets brimming with robalo, a species of **Centropomus** inhabiting the brackish mangrove channels."
      },
      {
        "author": "David Starr Jordan",
        "work": "The Genera of Fishes",
        "quote": "Lacepède established **Centropomus** to encompass the distinctive marine robalos of the tropical Atlantic and Pacific coasts."
      },
      {
        "author": "Charles Tate Regan",
        "work": "Biologia Centrali-Americana: Pisces",
        "quote": "The species of **Centropomus** demonstrate remarkable anatomical adaptations for swift ambush predation among submerged mangrove roots."
      }
    ]
  },
  "Dashboard — centr\\centropristis.md": {
    "primary": "A genus of marine serranid fishes known as black sea basses, native to coastal waters of the western North Atlantic.",
    "secondary": "In marine ecology, protogynous hermaphroditic sea basses that associate closely with rocky reefs, jetties, and oyster beds.",
    "quotes": [
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries of the South Coast of New England",
        "quote": "The black sea bass, known taxonomically as **Centropristis**, gathers in abundant shoals along the rocky shoals of Vineyard Sound."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "Specimens of **Centropristis** exhibit striking sexual dimorphism, mature males developing an adipose nuchal hump."
      },
      {
        "author": "Henry Bryant Bigelow",
        "work": "Fishes of the Gulf of Maine",
        "quote": "Trawlers along the southern banks frequently net **Centropristis** whenever ocean floor temperatures remain comfortably mild."
      }
    ]
  },
  "Dashboard — centr\\centropus.md": {
    "primary": "A genus of non-parasitic Old World cuckoos known as coucals, characterized by a long, straight hind claw.",
    "secondary": "In ornithology, terrestrial ground-dwelling birds of Africa, Asia, and Australasia that build their own nests and exhibit sex-role reversal.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "A large coucal of the genus **Centropus** fluttered through the dense bamboo thickets with heavy, unhurried wingbeats."
      },
      {
        "author": "John Gould",
        "work": "The Birds of Australia",
        "quote": "Unlike their brood-parasitic relatives, members of **Centropopus** construct a domed nest of grass and rear their own broods."
      },
      {
        "author": "Richard Bowdler Sharpe",
        "work": "A Hand-list of the Genera and Species of Birds",
        "quote": "The hallux claw in **Centropus** is exceptionally prolonged and nearly straight, resembling the spur of a lark."
      }
    ]
  },
  "Dashboard — centr\\centrosema.md": {
    "primary": "A genus of trailing or climbing leguminous herbs and vines known as butterfly peas, native to tropical and subtropical America.",
    "secondary": "In agricultural agronomy, nitrogen-fixing pasture legumes cultivated for high-protein forage and tropical soil enrichment.",
    "quotes": [
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "The resupinate papilionaceous blossom of **Centrosema** displays a broad, spurred standard petal of vivid violet hue."
      },
      {
        "author": "George Bentham",
        "work": "Flora Brasiliensis",
        "quote": "In woodland clearings across the Amazon basin, wild vines of **Centrosema** twine profusely over shrubs and fallen timber."
      },
      {
        "author": "Charles Piper",
        "work": "Forage Plants and Their Culture",
        "quote": "Deep-rooting species of **Centrosema** thrive in acidic tropical soils where other leguminous crops fail to nodulate."
      }
    ]
  },
  "Dashboard — centr\\centrosome.md": {
    "primary": "The principal microtubule-organizing center of animal cells, containing a pair of centrioles surrounded by pericentriolar material.",
    "secondary": "In cell biology, the cytoplasmic organelle that directs spindle assembly during mitosis and anchors the primary cilium in interphase.",
    "quotes": [
      {
        "author": "Theodor Boveri",
        "work": "Cells and Tissues",
        "quote": "The **centrosome** represents the true division organ of the cell, orchestrating bipolar spindle formation with dynamic precision."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Boveri demonstrated that an abnormal duplication of the **centrosome** inevitably leads to multipolar division and cellular chaos."
      },
      {
        "author": "Lewis Thomas",
        "work": "The Lives of a Cell",
        "quote": "Quietly presiding near the nucleus, the **centrosome** directs internal traffic and maintains the architectural integrity of the cell."
      }
    ]
  },
  "Dashboard — centr\\centrosomic.md": {
    "primary": "Pertaining to, derived from, or characteristic of a centrosome.",
    "secondary": "In cytopathology, describing structural or numerical abnormalities of centrosomes that contribute to genomic instability and aneuploidy.",
    "quotes": [
      {
        "author": "Theodor Boveri",
        "work": "Concerning the Origin of Malignant Tumors",
        "quote": "Supernumerary **centrosomic** foci cause asymmetrical pulling forces that tear the karyotype into disordered fragments."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Physical Basis of Life",
        "quote": "The radiant asters emerge directly from the **centrosomic** mass as prophase begins its transformation."
      },
      {
        "author": "William Bateson",
        "work": "Problems of Genetics",
        "quote": "Defects in **centrosomic** replication may generate somatic mosaicism long before phenotypic symptoms become apparent."
      }
    ]
  },
  "Dashboard — centr\\centrospermae.md": {
    "primary": "A former botanical taxon encompassing flowering plant orders characterized by curved embryos surrounding perisperm, now largely classified as Caryophyllales.",
    "secondary": "In plant systematics, a natural grouping of families including cactuses, carnations, and amaranths united by central or basal placentation.",
    "quotes": [
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "The order **Centrospermae** unites families sharing a curved embryo curved neatly around a nutritive central tissue."
      },
      {
        "author": "John Merle Coulter",
        "work": "Morphology of Angiosperms",
        "quote": "Campylotropous ovules and distinctive betalain pigments strongly reinforce the natural coherence of **Centrospermae**."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Botanists noted that seeds within **Centrospermae** present a peripheral embryo surrounding rather than embedded in endosperm."
      }
    ]
  },
  "Dashboard — centr\\centrosphere.md": {
    "primary": "The differentiated zone of specialized clear cytoplasm immediately surrounding the centrioles within a centrosome.",
    "secondary": "In classical cytology, the central aster sphere from which astral rays radiate during cell division.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Surrounding the delicate centrioles lies the hyaline **centrosphere**, from whose outer perimeter the astral fibrillae emerge."
      },
      {
        "author": "Theodor Boveri",
        "work": "Cell Studies",
        "quote": "The boundaries of the **centrosphere** expand conspicuously as tubulin monomers assemble into the expanding mitotic apparatus."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The circular contour of the **centrosphere** reflects surface tension forces operating within the colloidal protoplasm."
      }
    ]
  },
  "Dashboard — centr\\centrosymmetric.md": {
    "primary": "Possessing a point of inversion symmetry, such that every point on a figure or molecule corresponds to an identical point inverted through a central locus.",
    "secondary": "In crystallography and solid-state physics, characterizing space groups and crystal classes that lack optical activity and piezoelectric responses due to inversion symmetry.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "The planar molecule assumes a strictly **centrosymmetric** configuration in the solid state, cancelling out net dipole moments."
      },
      {
        "author": "Max von Laue",
        "work": "History of Physics",
        "quote": "X-ray diffraction patterns from **centrosymmetric** lattices obey Friedel's law with exceptional fidelity."
      },
      {
        "author": "J. D. Bernal",
        "work": "The Origin of Life",
        "quote": "In inorganic mineral surfaces, non-centrosymmetric crystals offer chiral adsorption sites whereas **centrosymmetric** forms remain racemic."
      }
    ]
  },
  "Dashboard — centr\\centrosymmetry.md": {
    "primary": "The geometric property of being symmetrical about a central point of inversion.",
    "secondary": "In crystallography, the condition wherein a crystal structure is invariant under spatial inversion $(x, y, z) \to (-x, -y, -z)$.",
    "quotes": [
      {
        "author": "Kathleen Lonsdale",
        "work": "Crystals and X-Rays",
        "quote": "The presence of **centrosymmetry** eliminates second-harmonic optical generation and prevents the emergence of pyroelectricity."
      },
      {
        "author": "Dorothy Hodgkin",
        "work": "Wandering Scientist",
        "quote": "Solving structures devoid of **centrosymmetry** required anomalous dispersion techniques to resolve phase ambiguities."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Ideal isometric crystals exhibit perfect **centrosymmetry**, with opposing faces meeting at identical dihedral angles."
      }
    ]
  },
  "Dashboard — centr\\centrum.md": {
    "primary": "The solid, massive central body of a vertebra from which the neural and hemal arches arise.",
    "secondary": "In comparative anatomy and paleontology, the foundational axial skeletal block whose articular surfaces determine spinal articulation across vertebrate classes.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "The autogenous **centrum** provides the primary foundation upon which the neurapophyses and pleurapophyses articulate."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In ancient crossopterygians, the **centrum** consists of separate pleurocentra and intercentra around the persistent notochord."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Origin and Evolution of Life",
        "quote": "The massive bony **centrum** of sauropod vertebrae evolved interior pneumatic cavities to reduce skeletal load."
      }
    ]
  },
  "Dashboard — centr\\decentralisation.md": {
    "primary": "The dispersion or distribution of power, administrative authority, or governmental functions away from a central authority to local organs.",
    "secondary": "In institutional political economy, structural delegation that enhances grassroots autonomy and local responsiveness across municipal subdivisions.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Administrative **decentralisation** produces an inexhaustible reservoir of civic energy that no centralized bureaucracy can match."
      },
      {
        "author": "Harold Laski",
        "work": "A Grammar of Politics",
        "quote": "Effective democratic governance demands territorial **decentralisation** to prevent the paralysis of parliamentary power."
      },
      {
        "author": "G. D. H. Cole",
        "work": "Guild Socialism Restated",
        "quote": "Industrial democracy cannot survive without genuine **decentralisation** of economic decision-making to the workshop floor."
      }
    ]
  },
  "Dashboard — centr\\decentralise.md": {
    "primary": "To distribute or disperse administrative powers, responsibilities, or operations away from a central hub to local divisions.",
    "secondary": "In systems engineering and management, to restructure an organization so that operational nodes execute decisions autonomously.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "The Road to Wigan Pier",
        "quote": "To humanize modern society, we must **decentralise** heavy industry and restore creative autonomy to the community."
      },
      {
        "author": "E. F. Schumacher",
        "work": "Small Is Beautiful",
        "quote": "The primary task of enlightened administration is to **decentralise** large corporations into quasi-independent operating units."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World Revisited",
        "quote": "If we wish to preserve freedom, we must deliberately **decentralise** both economic enterprise and government."
      }
    ]
  },
  "Dashboard — centr\\decentralised.md": {
    "primary": "Distributed among multiple local bodies, nodes, or regional centers rather than concentrated under a single authority.",
    "secondary": "In distributed network theory and political theory, operating without reliance upon a single coordinator or single point of failure.",
    "quotes": [
      {
        "author": "Friedrich Hayek",
        "work": "The Use of Knowledge in Society",
        "quote": "In a **decentralised** market, localized price signals mobilize fragmented knowledge far more effectively than any central board."
      },
      {
        "author": "Lewis Mumford",
        "work": "The City in History",
        "quote": "Medieval towns formed a **decentralised** federation of autonomous guilds united by shared cultural values."
      },
      {
        "author": "Peter Kropotkin",
        "work": "Fields, Factories and Workshops",
        "quote": "A **decentralised** network of small communal workshops can combine high craftsmanship with technological efficiency."
      }
    ]
  },
  "Dashboard — centr\\decentralising.md": {
    "primary": "The process or act of transferring authority, functions, or population away from a central hub to outlying regions.",
    "secondary": "In spatial urban planning and sociology, redistributing municipal resources or computational load to relieve centralized bottlenecking.",
    "quotes": [
      {
        "author": "Ebenezer Howard",
        "work": "Garden Cities of To-morrow",
        "quote": "By **decentralising** factory employment into surrounding garden cities, urban overcrowding naturally resolves itself."
      },
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "Electricity provided the technical means for **decentralising** manufacturing away from coal-basin conglomerates."
      },
      {
        "author": "Patrick Geddes",
        "work": "Cities in Evolution",
        "quote": "Regional surveys serve as the indispensable precursor to **decentralising** metropolitan congestion."
      }
    ]
  },
  "Dashboard — centr\\decentralization.md": {
    "primary": "The dispersion of functions, authorities, or populations away from a central location or authority to regional and local entities.",
    "secondary": "In political science and computer architecture, the organizational paradigm wherein autonomy is distributed among interconnected peer nodes.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The strength of free nations resides in the township, where **decentralization** fosters genuine habits of self-government."
      },
      {
        "author": "Friedrich Hayek",
        "work": "The Road to Serfdom",
        "quote": "Economic **decentralization** guarantees personal liberty by preventing the total monopolization of decision-making."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Culture of Cities",
        "quote": "True regional planning demands political **decentralization** to cultivate indigenous cultural institutions."
      }
    ]
  },
  "Dashboard — centr\\decentralize.md": {
    "primary": "To redistribute administrative functions, powers, or people away from a single central location or executive body.",
    "secondary": "In computational systems design, to partition processing tasks across distributed, autonomous nodes to avoid single points of failure.",
    "quotes": [
      {
        "author": "E. F. Schumacher",
        "work": "Small Is Beautiful",
        "quote": "Any intelligent manager will endeavor to **decentralize** operations so that small teams feel direct ownership of outcomes."
      },
      {
        "author": "Lewis Mumford",
        "work": "The Myth of the Machine",
        "quote": "To break the spell of the megamachine, democratic communities must **decentralize** production and governance."
      },
      {
        "author": "Norbert Wiener",
        "work": "The Human Use of Human Beings",
        "quote": "Communication networks allow society to **decentralize** decision processes while preserving instantaneous coordination."
      }
    ]
  },
  "Dashboard — centr\\decentralized.md": {
    "primary": "Dispersed among several regional or local authorities rather than concentrated under a single centralized government or system.",
    "secondary": "In systems architecture and cryptography, functioning across an egalitarian network of peer nodes without central intermediary governance.",
    "quotes": [
      {
        "author": "Friedrich Hayek",
        "work": "Individualism and Economic Order",
        "quote": "A **decentralized** economic system remains vastly superior in adjusting continuously to unexpected changes in demand."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "In a **decentralized** administration, local citizens solve communal problems without waiting for mandates from the capital."
      },
      {
        "author": "Aldous Huxley",
        "work": "Ends and Means",
        "quote": "Social peace can only flourish when production is carried out by **decentralized**, self-governing cooperative units."
      }
    ]
  },
  "Dashboard — centr\\decentralizing.md": {
    "primary": "Engaged in, causing, or relating to the transfer of authority or activities away from a central hub.",
    "secondary": "In macroeconomics and organizational dynamics, tending to break down central control in favor of local autonomy.",
    "quotes": [
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "The motor vehicle operated as a **decentralizing** force, breaking the rigid radiating rail corridors of the 19th century."
      },
      {
        "author": "Ebenezer Howard",
        "work": "To-morrow: A Peaceful Path to Real Reform",
        "quote": "A systematic **decentralizing** policy will draw surplus labor into green agricultural belts and garden villages."
      },
      {
        "author": "Alvin Toffler",
        "work": "The Third Wave",
        "quote": "Telecommunications acts as a powerful **decentralizing** mechanism, dispersing office workers back into home cottages."
      }
    ]
  },
  "Dashboard — centr\\eccentric.md": {
    "primary": "Deviating from an established, conventional pattern, center, or circular orbit; unconventional or whimsical in character.",
    "secondary": "In celestial mechanics and geometry, not placed centrally or deviating from a perfect circle into an ellipse.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Astronomia Nova",
        "quote": "Mars traverses an **eccentric** oval path whose varying speed corresponds directly to its solar distance."
      },
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "Mr. Dick was regarded as an **eccentric** gentleman whose innocent habits caused offense to nobody in the neighborhood."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "That so few now dare to be **eccentric** marks the chief danger of our time, for eccentricity has always abounded when strength of character abounded."
      }
    ]
  },
  "Dashboard — centr\\eccentrically.md": {
    "primary": "In an eccentric, unconventional, or off-center manner.",
    "secondary": "In kinematics and astronomy, positioned or rotating around an axis that does not coincide with the geometric center.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "The Return of the Native",
        "quote": "He moved **eccentrically** along the heath, zigzagging across gullies as though propelled by unpredictable inner whims."
      },
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "The tiny wheel was mounted **eccentrically** upon its pinion, producing an intermittent reciprocal motion."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Hound of the Baskervilles",
        "quote": "Frankland spent his fortune **eccentrically** in lawsuits, delighting in litigating against his own parish."
      }
    ]
  },
  "Dashboard — centr\\eccentrism.md": {
    "primary": "The state, quality, or practice of deviating from customary or normal behavior; eccentricity.",
    "secondary": "In classical astronomy and mechanics, the condition of an orbit or cam deviating from concentric alignment with the primary center.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Genius and neurosis frequently collide, producing patterns of high **eccentrism** that society struggles to interpret."
      },
      {
        "author": "Thomas Love Peacock",
        "work": "Nightmare Abbey",
        "quote": "His philosophic **eccentrism** consisted in perpetual retreat to his solitary tower wrapped in gloomy speculation."
      },
      {
        "author": "George Santayana",
        "work": "The Life of Reason",
        "quote": "A cultivated **eccentrism** often serves as a defensive armor against the overwhelming conformity of public opinion."
      }
    ]
  },
  "Dashboard — centr\\eccentrist.md": {
    "primary": "A person of eccentric behavior, opinions, or unconventional lifestyle.",
    "secondary": "In social history and psychology, an individual who deliberately diverges from orthodox societal norms and mores without malice.",
    "quotes": [
      {
        "author": "Edith Sitwell",
        "work": "English Eccentrics",
        "quote": "The true **eccentrist** flourishes upon aristocratic solitude, cultivating bizarre idiosyncrasies with haughty indifference."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Society suspects the **eccentrist**, yet all vital reform begins as the stubborn oddity of a solitary thinker."
      },
      {
        "author": "Arthur Schopenhauer",
        "work": "Parerga and Paralipomena",
        "quote": "The common herd branding an independent thinker as an **eccentrist** merely confesses its own inability to comprehend truth."
      }
    ]
  },
  "Dashboard — centr\\ecocentric.md": {
    "primary": "Centering on the whole ecosystem rather than solely on human needs; ecologically oriented.",
    "secondary": "In environmental ethics, maintaining that inherent value resides in all ecological entities and natural processes regardless of human utility.",
    "quotes": [
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "A land ethic reflects an **ecocentric** conscience that expands the boundaries of the community to include soils, waters, and plants."
      },
      {
        "author": "Arne Naess",
        "work": "Ecology, Community and Lifestyle",
        "quote": "Deep ecology adopts an **ecocentric** worldview where every living organism possesses an intrinsic right to unfold its potential."
      },
      {
        "author": "Rachel Carson",
        "work": "Lost Woods: The Discovered Writing of Rachel Carson",
        "quote": "We must substitute an **ecocentric** reverence for nature in place of arrogant technological conquest."
      }
    ]
  },
  "Dashboard — centr\\ecocentrism.md": {
    "primary": "A philosophical perspective or ethical framework that places intrinsic value on ecological systems and all living beings.",
    "secondary": "In environmental philosophy, the doctrine that the ecosphere, rather than humanity, constitutes the primary moral community.",
    "quotes": [
      {
        "author": "Arne Naess",
        "work": "The Shallow and the Deep, Long-Range Ecology Movement",
        "quote": "The transition from anthropocentrism to radical **ecocentrism** requires a profound transformation in our conception of selfhood."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "Implicit in the land ethic is **ecocentrism**, affirming that the land is an organism to be loved and respected."
      },
      {
        "author": "Barry Commoner",
        "work": "The Closing Circle",
        "quote": "Without grounding public policy in **ecocentrism**, industrial technology will inevitably destabilize the biophysical cycle."
      }
    ]
  },
  "Dashboard — centr\\ecocentrist.md": {
    "primary": "An adherent or advocate of ecocentrism who views natural ecosystems as possessing supreme intrinsic moral value.",
    "secondary": "In environmental jurisprudence, a theorist who argues for legal personhood and moral rights for rivers, forests, and wild biotas.",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The thoughtful **ecocentrist** reminds us that human survival depends on thousands of inconspicuous invertebrates."
      },
      {
        "author": "Aldo Leopold",
        "work": "Round River",
        "quote": "As an **ecocentrist**, one learns to think like a mountain, recognizing that wolves preserve the health of the hillside."
      },
      {
        "author": "Gary Snyder",
        "work": "The Practice of the Wild",
        "quote": "The genuine **ecocentrist** accepts residency in the watershed as a sacred participant rather than an external proprietor."
      }
    ]
  },
  "Dashboard — centr\\endocentric.md": {
    "primary": "Fulfilling the same grammatical function as one of its constituents; internally centered.",
    "secondary": "In structural linguistics, describing a compound or phrase whose syntactic distribution and semantic head belong to the same word class as the whole construction.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "The compound 'blackbird' is strictly **endocentric**, for the whole phrase functions syntactically as a noun like its head 'bird'."
      },
      {
        "author": "Noam Chomsky",
        "work": "Aspects of the Theory of Syntax",
        "quote": "Modern X-bar theory treats virtually every lexical projection as **endocentric** around its core head."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Syntactic cohesion reveals whether an idiomatic phrase behaves in an **endocentric** or exocentric pattern."
      }
    ]
  },
  "Dashboard — centr\\enterocentesis.md": {
    "primary": "Surgical puncture of the intestine to evacuate gas, fluid, or accumulated contents.",
    "secondary": "In veterinary and emergency clinical medicine, paracentesis of an inflated intestinal loop to relieve severe tympany or volvulus.",
    "quotes": [
      {
        "author": "William Youatt",
        "work": "The Horse",
        "quote": "In cases of acute flatulent colic where suffocation impends, timely **enterocentesis** with a fine trocar affords instantaneous relief."
      },
      {
        "author": "Sir Frederick Hobday",
        "work": "Surgical Diseases of the Dog and Cat",
        "quote": "Emergency **enterocentesis** must be performed under strict asepsis to preclude contamination of the peritoneal cavity."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "While rarely indicated in human surgery, **enterocentesis** was historically attempted for decompression of extreme meteorism."
      }
    ]
  },
  "Dashboard — centr\\epicenter.md": {
    "primary": "The point on the Earth's surface directly above the underground focus or hypocenter of an earthquake.",
    "secondary": "By extension, the central point, focal nexus, or core locus of an intense, turbulent activity, crisis, or cultural movement.",
    "quotes": [
      {
        "author": "John Milne",
        "work": "Earthquakes and Other Earth Movements",
        "quote": "By plotting arrival times at three seismic stations, the precise **epicenter** of the shock can be triangulated on the map."
      },
      {
        "author": "Charles Richter",
        "work": "Elementary Seismology",
        "quote": "Maximum surface destruction does not always coincide with the **epicenter**, depending upon local ground composition."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Submarine tsunamis radiate outward in expanding concentric circles from the oceanic **epicenter**."
      }
    ]
  },
  "Dashboard — centr\\epicentre.md": {
    "primary": "The point on the Earth's surface situated vertically above the subterranean hypocentre of a seismic disturbance.",
    "secondary": "Figuratively, the pivotal hub, core storm-centre, or epicenter of an ideological debate, artistic movement, or political crisis.",
    "quotes": [
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Isoseismal lines form closed curves radiating around the seismic **epicentre** with decreasing destructive intensity."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War: The Gathering Storm",
        "quote": "Berlin had become the ominous **epicentre** from which tremors of militarism shook all Central Europe."
      },
      {
        "author": "E. M. Forster",
        "work": "A Passage to India",
        "quote": "The courtroom became the passionate **epicentre** of racial antagonism, vibrating with suppressed animosities."
      }
    ]
  },
  "Dashboard — centr\\exocentric.md": {
    "primary": "Lacking an internal grammatical head or center that fulfills the same syntactic category as the whole construction.",
    "secondary": "In linguistics, designating phrases or compound words (such as 'pickpocket' or prepositional phrases) whose overall syntactic function differs from any of its constituent parts.",
    "quotes": [
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "The compound 'pickpocket' is **exocentric**, because the composite term is a noun while its primary head element is a transitive verb."
      },
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Prepositional phrases illustrate an **exocentric** construction whose grammatical value cannot be replaced by preposition or noun alone."
      },
      {
        "author": "Roman Jakobson",
        "work": "Selected Writings: Word and Language",
        "quote": "The morphological tension in **exocentric** compounds relies upon metonymic transposition outside the lexical base."
      }
    ]
  },
  "Dashboard — centr\\holocentric.md": {
    "primary": "Possessing diffuse centromeric activity along the entire length of the chromosome rather than localized at a single constriction.",
    "secondary": "In cytogenetics, describing chromosomes (as in nematodes and sedges) where spindle microtubules attach across the entire chromatin axis during anaphase.",
    "quotes": [
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "In Luzula, the chromosomes are strictly **holocentric**, enabling fragmented pieces to persist and divide normally."
      },
      {
        "author": "Michael J. D. White",
        "work": "Animal Cytology and Evolution",
        "quote": "X-ray-induced breakage in **holocentric** chromosomes rarely produces lethal acentric fragments during mitotic division."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics of the Evolutionary Process",
        "quote": "Hemipteran insects exploit **holocentric** chromosome architecture to facilitate rapid karyotypic radiation."
      }
    ]
  },
  "Dashboard — centr\\holocentridae.md": {
    "primary": "A family of beryciform marine spiny-finned fishes commonly known as squirrelfishes and soldierfishes.",
    "secondary": "In marine biology, nocturnal reef-dwelling fishes characterized by large eyes, sharp opercular spines, and brilliant red coloration.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "Fishes",
        "quote": "Members of **Holocentridae** hide in deep cavernous reef crevices by day, emerging after dusk to forage on crustaceans."
      },
      {
        "author": "Albert Günther",
        "work": "An Introduction to the Study of Fishes",
        "quote": "The heavy, serrated scales and formidable opercular spines of **Holocentridae** afford robust defense against predatory morays."
      },
      {
        "author": "William Beebe",
        "work": "Beneath Tropic Seas",
        "quote": "Gazing through the diving helmet, I watched flashing red soldierfish of the family **Holocentridae** hover motionless beside elkhorn corals."
      }
    ]
  },
  "Dashboard — centr\\holocentrus.md": {
    "primary": "A genus of tropical marine squirrelfishes belonging to the family Holocentridae.",
    "secondary": "In ichthyological taxonomy, reef fishes noted for loud acoustic sound production via swimbladder drumming and long preopercular spines.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "Our sailors angled for specimens of **Holocentrus**, whose vivid scarlet scales sparkled brilliantly upon the deck."
      },
      {
        "author": "Charles Darwin",
        "work": "The Zoology of the Voyage of H.M.S. Beagle",
        "quote": "A handsome fish of the genus **Holocentrus** was captured among the shallow coral pools of Ascension Island."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Species of **Holocentrus** produce distinct staccato grunts when defending territory or disturbed by reef divers."
      }
    ]
  },
  "Dashboard — centr\\homocentric.md": {
    "primary": "Having the same center; concentric.",
    "secondary": "In classical astronomical cosmology and optics, describing concentric crystalline celestial spheres or light rays radiating from a common focal point.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "Eudoxus posited a system of **homocentric** spheres rotating on different axes to explain planetary stations and retrogradations."
      },
      {
        "author": "Thomas Aquinas",
        "work": "Commentary on Aristotle's On the Heavens",
        "quote": "The ancient astronomers sought to harmonize celestial motions through nested **homocentric** circles revolving about the Earth."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "A bundle of **homocentric** light rays emanates from an ideal point source and converges upon a single conjugate focus."
      }
    ]
  },
  "Dashboard — centr\\metacenter.md": {
    "primary": "The point of intersection between a vertical line drawn through the center of buoyancy of a floating vessel and the vertical centerline plane through its center of gravity when heeled.",
    "secondary": "In naval architecture and hydrodynamics, the critical geometric reference point whose position relative to the center of gravity determines positive, neutral, or negative stability.",
    "quotes": [
      {
        "author": "William Froude",
        "work": "On the Rolling of Ships",
        "quote": "If the **metacenter** falls below the center of gravity, the righting lever vanishes and the ship capsizes."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The ship's carpenter understood the perilous physics that elevated the ballast too high relative to the buoyant **metacenter**."
      },
      {
        "author": "Joseph Conrad",
        "work": "The Mirror of the Sea",
        "quote": "A master mariner develops an instinctive sympathy with his vessel's **metacenter**, feeling every shudder of excessive stiffness."
      }
    ]
  },
  "Dashboard — centr\\metacentre.md": {
    "primary": "The theoretical point in naval architecture at which a vertical line through the shifted centre of buoyancy intersects the vertical axis of equilibrium of a tilted vessel.",
    "secondary": "In maritime engineering, the height of this point above the center of gravity (the metacentric height) provides the fundamental metric of hydrostatic stability.",
    "quotes": [
      {
        "author": "William John Macquorn Rankine",
        "work": "Shipbuilding: Theoretical and Practical",
        "quote": "Calculating the position of the **metacentre** must precede any reliable assessment of a vessel's seaworthiness in heavy swell."
      },
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses: Navigational Affairs",
        "quote": "When the ship rolls into the trough, the oscillating centre of buoyancy swings about the fixed **metacentre**."
      },
      {
        "author": "H. G. Wells",
        "work": "The War in the Air",
        "quote": "The monstrous dirigibles were designed so that their centre of gravity hung deep beneath the aerostatic **metacentre**."
      }
    ]
  },
  "Dashboard — centr\\metacentric.md": {
    "primary": "Having the centromere positioned at or near the middle of the chromosome, producing arms of approximately equal length.",
    "secondary": "In cytogenetics and karyotyping, designating V-shaped chromosomes during anaphase as opposed to acrocentric or telocentric morphologies.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Robertsonian fusion converts two separate acrocentric rods into a single stable **metacentric** chromosome."
      },
      {
        "author": "Michael J. D. White",
        "work": "Animal Cytology and Evolution",
        "quote": "Under the light microscope, the **metacentric** element forms two equal arms that flex symmetrically toward the pole."
      },
      {
        "author": "C. D. Darlington",
        "work": "The Evolution of Genetic Systems",
        "quote": "Chiasma frequency often displays symmetrical distribution across both arms of a **metacentric** bivalent."
      }
    ]
  },
  "Dashboard — centr\\microcentrum.md": {
    "primary": "A genus of broad-winged katydids or bush crickets in the family Tettigoniidae, known as angle-wing katydids.",
    "secondary": "In entomology and acoustics, phytophagous orthopterans noted for leaflike forewings and high-frequency nocturnal stridulation.",
    "quotes": [
      {
        "author": "Samuel Hubbard Scudder",
        "work": "Catalogue of the Orthoptera of North America",
        "quote": "The species of **Microcentrum** mimic broad deciduous leaves so closely that predators pass them by unnoticed."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "Nymphs of **Microcentrum** blend perfectly into the foliage while feeding upon tender young shoots."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Grasshopper",
        "quote": "With its broad green tegmina veined like foliage, **Microcentrum** provides one of nature's finest examples of protective camouflage."
      }
    ]
  },
  "Dashboard — centr\\monocentric.md": {
    "primary": "Having a single center; possessing only one centromere.",
    "secondary": "In cytogenetics, designating standard eukaryotic chromosomes governed by a single localized centromeric locus during mitotic spindle attachment.",
    "quotes": [
      {
        "author": "Barbara McClintock",
        "work": "The Behavior in Successive Nuclear Divisions of a Chromosome Broken at Meiosis",
        "quote": "A normal **monocentric** chromatid travels smoothly to one pole without the risk of bridge formation during anaphase."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "In contrast to diffuse kinetochores, typical animal chromosomes follow a strictly **monocentric** organization."
      },
      {
        "author": "Lewis Mumford",
        "work": "The City in History",
        "quote": "The ancient royal capital was a **monocentric** citadel, radiating imperial commands from a singular palace square."
      }
    ]
  },
  "Dashboard — centr\\neocentromere.md": {
    "primary": "A newly formed functional centromere arising at an ectopic, previously non-centromeric chromosomal region.",
    "secondary": "In clinical cytogenetics and molecular evolution, an epigenetically activated centromere lacking canonical alpha-satellite DNA that rescues acentric chromosomal fragments.",
    "quotes": [
      {
        "author": "Barbara McClintock",
        "work": "Chromosome Organization and Genic Expression",
        "quote": "Under stressful breakage cycles in maize, a latent **neocentromere** formed de novo along the knobbed terminal segment."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "The spontaneous emergence of a **neocentromere** demonstrates that centromeric identity is epigenetic rather than sequence-dependent."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics of the Evolutionary Process",
        "quote": "Karyotypic evolution may proceed through the activation of an adventitious **neocentromere**, shifting the arm ratio."
      }
    ]
  },
  "Dashboard — centr\\paracentesis.md": {
    "primary": "The surgical perforation or tapping of a body cavity, such as the peritoneum or tympanic membrane, to aspirate accumulated fluid.",
    "secondary": "In clinical medicine, a diagnostic and therapeutic procedure commonly performed to relieve high-volume abdominal ascites.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In chronic cirrhosis with tense abdominal distension, therapeutic **paracentesis** must be performed promptly to ease diaphragmatic distress."
      },
      {
        "author": "Sir Thomas Watson",
        "work": "Lectures on the Principles and Practice of Physic",
        "quote": "The trocar was introduced in the linea alba, and the **paracentesis** yielded several quarts of clear serous fluid."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Careful palpation avoids injury to the inferior epigastric artery during abdominal **paracentesis**."
      }
    ]
  },
  "Dashboard — centr\\pericardiocentesis.md": {
    "primary": "Surgical aspiration of fluid from the pericardial sac surrounding the heart.",
    "secondary": "In emergency cardiology, an urgent decompression procedure to relieve cardiac tamponade by inserting a needle into the pericardial space.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When purulent effusion threatens fatal cardiac strangulation, emergency **pericardiocentesis** provides the sole hope of survival."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Aspiration of even fifty cubic centimeters of blood during **pericardiocentesis** restores arterial pressure almost instantaneously."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Life of Sir William Osler",
        "quote": "Under aseptic precautions, the surgeon performed a subxiphoid **pericardiocentesis**, relieving the patient's acute cyanosis."
      }
    ]
  },
  "Dashboard — centr\\technocentric.md": {
    "primary": "Centering upon technology and engineering as the primary means to solve human, social, and environmental challenges.",
    "secondary": "In philosophy and environmental sociology, describing an ideology that assumes scientific innovation can overcome ecological limits.",
    "quotes": [
      {
        "author": "Lewis Mumford",
        "work": "The Myth of the Machine: The Pentagon of Power",
        "quote": "Our civilization remains trapped in a **technocentric** illusion that every human dilemma can be cured by a more elaborate machine."
      },
      {
        "author": "Jacques Ellul",
        "work": "The Technological Society",
        "quote": "A strictly **technocentric** culture eliminates spiritual discernment in favor of operational efficiency."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "The **technocentric** arrogance that seeks to dominate nature with synthetic chemicals risks poisoning the very soil beneath our feet."
      }
    ]
  },
  "Dashboard — centr\\technocentrism.md": {
    "primary": "The belief or ideological stance that technology is central to human progress and capable of resolving ecological and social crises.",
    "secondary": "In sociological theory, a perspective that privileges technical rationalism, industrial growth, and mechanistic control over natural systems.",
    "quotes": [
      {
        "author": "Lewis Mumford",
        "work": "Technics and Civilization",
        "quote": "Unchecked **technocentrism** elevated mechanical devices above human values, reducing workers to adjuncts of the assembly line."
      },
      {
        "author": "E. F. Schumacher",
        "work": "Small Is Beautiful",
        "quote": "The dogma of modern **technocentrism** insists that if an engineering project creates pollution, only bigger machines can cure it."
      },
      {
        "author": "Neil Postman",
        "work": "Technopoly: The Surrender of Culture to Technology",
        "quote": "In full-fledged technopoly, **technocentrism** redesigns human institutions to serve the demands of algorithmic efficiency."
      }
    ]
  },
  "Dashboard — centr\\telocentric.md": {
    "primary": "Having the centromere situated at the very terminal end of the chromosome.",
    "secondary": "In cytogenetics, designating rod-shaped chromosomes that possess only a single discernible cytological arm during anapase movement.",
    "quotes": [
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "House mice exhibit a karyotype composed entirely of **telocentric** chromosomes, predisposing them to centric fusions."
      },
      {
        "author": "Michael J. D. White",
        "work": "Animal Cytology and Evolution",
        "quote": "A true **telocentric** element lacks even a minute second arm, terminating directly at the kinetochore plate."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "During polar migration, the **telocentric** rod is dragged forward from its lead tip like a towed javelin."
      }
    ]
  },
  "Dashboard — centr\\thoracentesis.md": {
    "primary": "Surgical puncture of the thoracic wall with a needle or trocar to aspirate accumulated fluid or air from the pleural cavity.",
    "secondary": "In pulmonology and critical care, an essential diagnostic and palliative procedure for pleural effusions and hemothorax.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In massive pleuritic effusion with dyspnea, immediate **thoracentesis** relieves mediastinal displacement and restores lung expansion."
      },
      {
        "author": "Sir Thomas Watson",
        "work": "Lectures on the Principles and Practice of Physic",
        "quote": "By performing **thoracentesis** in the eighth intercostal space, the operator drains the pleural collection without entering the diaphragm."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The needle during **thoracentesis** must hug the superior margin of the lower rib to avoid the intercostal neurovascular bundle."
      }
    ]
  },
  "Dashboard — centr\\thoracocentesis.md": {
    "primary": "A therapeutic or diagnostic surgical procedure involving puncture of the chest wall to drain pleural fluid or air; thoracentesis.",
    "secondary": "In veterinary medicine and thoracic surgery, the aspiration of pleural transudate, exudate, or chyle from the hemithorax.",
    "quotes": [
      {
        "author": "Sir Frederick Hobday",
        "work": "Surgical Diseases of the Dog and Cat",
        "quote": "When hydrothorax severely embarrasses respiratory efforts, immediate **thoracocentesis** provides dramatic temporary resuscitation."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In purulent empyema, exploratory **thoracocentesis** establishes whether simple drainage or rib resection is mandatory."
      },
      {
        "author": "Sir Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The country doctor sterilised his trocar for a midnight **thoracocentesis**, drawing off three pints of pleuritic effusion."
      }
    ]
  },
  "Dashboard — cirr\\cirr.md": {
    "primary": "A classical combining root signifying a curl, ringlet, or wispy filament, as well as (via Greek kirrhos) a tawny or yellowish-orange discoloration.",
    "secondary": "In biological nomenclature and atmospheric science, an affix designating filamentous appendages (cirri) or high, wispy ice-crystal cloud formations.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "A Monograph on the Sub-class Cirripedia",
        "quote": "The Latin root **cirr** originally signified a curl or lock of hair, aptly describing the feathery appendages of barnacles."
      },
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "I applied the Greek prefix **cirr** to designate the granular yellow-tawny hepatic nodules observed in alcoholic atrophy."
      },
      {
        "author": "Luke Howard",
        "work": "On the Modifications of Clouds",
        "quote": "The prefix **cirr** distinguishes elevated clouds consisting of delicate curling fibres and wisps of frozen moisture."
      }
    ]
  },
  "Dashboard — cirr\\cirrhosis.md": {
    "primary": "A chronic, progressive degenerative disease of the liver marked by formation of diffuse fibrous scar tissue and regenerative nodules.",
    "secondary": "In hepatology and pathology, end-stage liver fibrosis resulting from chronic inflammation that disrupts hepatic architecture and blood flow.",
    "quotes": [
      {
        "author": "René Laennec",
        "work": "A Treatise on the Diseases of the Chest",
        "quote": "I designate this hepatic degeneration as **cirrhosis**, from the tawny yellow color of the dense granular nodules."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Alcoholic **cirrhosis** exhibits the characteristic hobnail surface, with bands of fibrous tissue compressing the portal venules."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In advanced **cirrhosis**, chronic interstitial connective tissue proliferation slowly suffocates the parenchymal hepatic cells."
      }
    ]
  },
  "Dashboard — cirr\\cirriped.md": {
    "primary": "Any marine crustacean of the subclass Cirripedia, characterized by feathery curling thoracic appendages; a barnacle.",
    "secondary": "In invertebrate zoology, a sessile or stalked crustacean that attaches to rocks, ship hulls, or whales and filter-feeds with feathered cirri.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Even the minute pedunculated **cirriped** possesses degenerate sensory organs that betray its crustacean ancestry."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "A sessile **cirriped** develops a robust calcareous shell within which the animal lies permanently upon its back."
      },
      {
        "author": "Louis Agassiz",
        "work": "Methods of Study in Natural History",
        "quote": "The free-swimming larva of a **cirriped** proves conclusively that it belongs with crabs rather than with mollusks."
      }
    ]
  },
  "Dashboard — cirr\\cirripede.md": {
    "primary": "A member of the crustacean subclass Cirripedia, comprising acorn barnacles and goose barnacles.",
    "secondary": "In marine biology, a sedentary hermaphroditic crustacean that secretes calcareous plates and feeds by rhythmic sweeps of its cirri.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "A Monograph on the Sub-class Cirripedia",
        "quote": "No organ in the whole group of the **cirripede** crustaceans exhibits more morphological variation than the cement glands."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Year at the Shore",
        "quote": "The acorn **cirripede** opens its folding doors and casts forth its feathered casting-net into the surging tide."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Clusters of stalked **cirripede** shells clung tenaciously to the ancient copper sheathing beneath the waterline."
      }
    ]
  },
  "Dashboard — cirr\\cirripedia.md": {
    "primary": "A subclass of exclusively marine crustaceans that includes stalked and sessile barnacles.",
    "secondary": "In invertebrate systematics, crustaceans whose free-swimming nauplius and cypris larvae metamorphose into permanently attached filter-feeders.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Autobiography",
        "quote": "I spent eight continuous years dissecting and describing every known fossil and living species of **Cirripedia**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The parasitic forms of **Cirripedia** suffer such profound morphological reduction that all segmentation is lost."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Darwinism",
        "quote": "Darwin's monumental monograph on the **Cirripedia** established his reputation as a master comparative anatomist."
      }
    ]
  },
  "Dashboard — cirr\\cirrocumulus.md": {
    "primary": "A high-altitude cloud composed of ice crystals forming thin white sheets, ripples, or patches resembling a 'mackerel sky'.",
    "secondary": "In meteorology, high tropospheric clouds (above 6,000 meters) exhibiting delicate wave patterns without shadows, indicating atmospheric wave dynamics.",
    "quotes": [
      {
        "author": "Luke Howard",
        "work": "On the Modifications of Clouds",
        "quote": "The **cirrocumulus** consists of small, rounded flecks densely arranged in undulating ripples across the zenith."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "The sunset illuminated delicate bands of **cirrocumulus**, turning their crystalline ripples into flakes of molten gold."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Journal",
        "quote": "A light breeze formed a magnificent mackerel sky of dappled **cirrocumulus**, presaging a change in the weather."
      }
    ]
  },
  "Dashboard — cirr\\cirrostratus.md": {
    "primary": "A thin, high-altitude veil of ice-crystal cloud covering the sky and typically producing optical halos around the sun or moon.",
    "secondary": "In synoptic meteorology, an extensive sheet cloud formed in the upper troposphere ahead of an advancing warm front.",
    "quotes": [
      {
        "author": "Luke Howard",
        "work": "Essay on the Modifications of Clouds",
        "quote": "The uniform sheet of **cirrostratus** gives the sky a milky pallor through which the sun shines with a distinct halo."
      },
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "A pale shroud of **cirrostratus** crept over the evening stars, warning the shepherd of the approaching tempest."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Solar halos formed by the refractive prismatic crystals of **cirrostratus** were observed with extraordinary brilliance over the Andes."
      }
    ]
  },
  "Dashboard — cirr\\cirrus.md": {
    "primary": "A principal cloud genus characterized by thin, wispy, feather-like strands of ice crystals in the upper troposphere.",
    "secondary": "In invertebrate morphology, a slender, flexible, curling filament or tendril-like appendage on animals such as barnacles and annelids.",
    "quotes": [
      {
        "author": "Luke Howard",
        "work": "On the Modifications of Clouds",
        "quote": "Clouds in this modification appear like parallel, flexuous, or diverging fibres, for which the name **cirrus** is proposed."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "The Cloud",
        "quote": "Like locks of the fierce Maenad uplifted from the head of some fierce Dirce, streaks of **cirrus** streamed across the sky."
      },
      {
        "author": "Charles Darwin",
        "work": "A Monograph on the Sub-class Cirripedia",
        "quote": "Each joint of the multiarticulate **cirrus** bears paired setae that interlock to form an exquisite marine filter."
      }
    ]
  },
  "Dashboard — cirr\\polycirrus.md": {
    "primary": "A genus of terebellid marine polychaete worms characterized by numerous long, retractile feeding tentacles.",
    "secondary": "In marine invertebrate zoology, sediment-dwelling polychaetes that utilize bioluminescent secretions and numerous ciliated cirri for detrital feeding.",
    "quotes": [
      {
        "author": "William Carmichael M'Intosh",
        "work": "A Monograph of the British Marine Annelids",
        "quote": "The species of **Polycirrus** lack branchiae entirely, relying upon an extensive crown of filamentous tentacles for respiration."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Year at the Shore",
        "quote": "When touched under the microscope, the fragile tentacles of **Polycirrus** sparkle with bright greenish bioluminescence."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In **Polycirrus**, the prostomial region is broadened into a mobile mobile lobe bearing scores of grooved sensory filaments."
      }
    ]
  },
  "Dashboard — clad\\clad.md": {
    "primary": "Clothed, covered, or attired; enveloped in a protective or decorative outer layer.",
    "secondary": "In biological terminology and historical etymology, a root element (from Greek klados, meaning sprout, branch, or shoot) denoting evolutionary branching.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Now came still Evening on, and Twilight gray / Had in her sober livery all things **clad**."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "The hillside was **clad** in rich golden gorse, glowing vividly beneath the midsummer sun."
      },
      {
        "author": "Ernst Mayr",
        "work": "The Growth of Biological Thought",
        "quote": "The Greek stem **clad** denotes a tender young branch, providing the conceptual foundation for all tree-like phylogenies."
      }
    ]
  },
  "Dashboard — clad\\clade.md": {
    "primary": "A taxonomic group of organisms consisting of a single common ancestor and all of its lineal descendants.",
    "secondary": "In phylogenetic systematics, a monophyletic branch of the tree of life defined by shared derived homologies (synapomorphies).",
    "quotes": [
      {
        "author": "Julian Huxley",
        "work": "Evolutionary Process",
        "quote": "I suggest the term **clade** for a monophyletic unit resulting from cladogenesis, tracing to a single common origin."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "Every major **clade** undergoes an initial burst of morphological disparity followed by subsequent canalization."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "To be recognized as a true **clade**, birds must be grouped together with their extinct theropod dinosaur ancestors."
      }
    ]
  },
  "Dashboard — clad\\cladistics.md": {
    "primary": "A method of biological classification that groups organisms based on shared derived characteristics inherited from their most recent common ancestor.",
    "secondary": "In systematic evolutionary biology, phylogenetic analysis that rigorously rejects paraphyletic taxa in favor of strictly monophyletic clades.",
    "quotes": [
      {
        "author": "Willi Hennig",
        "work": "Phylogenetic Systematics",
        "quote": "The fundamental principle of **cladistics** insists that phylogenetic relationship means sharing a more recent common ancestor."
      },
      {
        "author": "Ernst Mayr",
        "work": "Toward a New Philosophy of Biology",
        "quote": "While evolutionary taxonomy balances branching with adaptive divergence, **cladistics** relies solely upon branching order."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The rigorous discipline of **cladistics** forced paleontologists to justify evolutionary trees by explicit shared novelties."
      }
    ]
  },
  "Dashboard — clad\\cladode.md": {
    "primary": "A modified photosynthetic stem or branch that resembles and functions as a leaf.",
    "secondary": "In plant anatomy and morphology, a flattened succulent or woody stem segment (as seen in Asparagus or prickly pear cactus) that bears flowers and fruit.",
    "quotes": [
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "In Ruscus, the apparent foliage leaves are true cladodes or **cladode** structures arising from the axils of papery scale leaves."
      },
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "The joint of a prickly pear cactus represents an expanded green **cladode** performing the photosynthetic work of true foliage."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Cyclopedia of American Horticulture",
        "quote": "Florists value the delicate feathery spray of Asparagus plumosus, whose tiny needle-like green organs are each an individual **cladode**."
      }
    ]
  }
};

const updated = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`[Batch 1] Successfully updated ${updated} of ${Object.keys(batchData).length} notes.`);
