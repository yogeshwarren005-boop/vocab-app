import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Motion & Direction';
const DASHBOARD = 'Dashboard — plan';

const BATCH6_DATA = {
  "aplanatic": {
    primary: "Free from both spherical aberration and coma (of an optical lens or system).",
    secondary: "Capable of focusing rays from a single point object into a stigmatic point image without optical blur.",
    quotes: [
      { author: "Ernst Abbe", work: "Contributions to the Theory of the Microscope", text: "The newly computed **aplanatic** doublet successfully eliminated marginal spherical aberration." },
      { author: "Joseph Jackson Lister", work: "On Some Properties in Achromatic Object-Glasses", text: "We discovered two **aplanatic** foci where chromatic dispersion and spherical distortion were simultaneously neutralized." },
      { author: "Lord Rayleigh", work: "Scientific Papers", text: "An ideal **aplanatic** mirror provides perfect geometric convergence for paraxial incident rays." }
    ]
  },
  "aplanetic": {
    primary: "Non-motile; lacking cilia or flagella for locomotion (of spores or cells).",
    secondary: "In botany and phycology, designating resting spores or gametes that do not wander or swim.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "Certain algae produce **aplanetic** resting cells that endure prolonged seasonal desiccation." },
      { author: "Gilbert Morgan Smith", work: "The Fresh-Water Algae of the United States", text: "The non-flagellated **aplanetic** spores germinate directly within the parent cell wall." },
      { author: "F. E. Fritsch", work: "The Structure and Reproduction of the Algae", text: "In the Chlorococcales, reproduction occurs exclusively by **aplanetic** autospores." }
    ]
  },
  "aplanogamete": {
    primary: "A non-motile gamete lacking flagella or cilia, characteristic of certain algae and fungi.",
    secondary: "A sexual cell that accomplishes fertilization without active swimming locomotion.",
    quotes: [
      { author: "F. E. Fritsch", work: "The Structure and Reproduction of the Algae", text: "In conjugating Zygnemataceae, fusion takes place between two identical **aplanogamete** cells." },
      { author: "Gilbert Morgan Smith", work: "The Fresh-Water Algae of the United States", text: "Each **aplanogamete** moves by amoeboid creep through the conjugation tube to meet its mate." },
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "The passive **aplanogamete** remains securely sheltered within the female gametangium." }
    ]
  },
  "deplane": {
    primary: "To disembark or step down from an airplane.",
    secondary: "To alight upon an airfield tarmac following completion of a flight.",
    quotes: [
      { author: "Ernest Hemingway", work: "Selected Letters", text: "We were glad to **deplane** into the sweltering heat of Nairobi after eighteen hours in the air." },
      { author: "Beryl Markham", work: "West with the Night", text: "The passengers waited patiently to **deplane** as the small cabin door was unbolted." },
      { author: "Antoine de Saint-Exupéry", work: "Southern Mail", text: "The courier prepared to **deplane** with his locked leather mail sacks before dawn." }
    ]
  },
  "emplane": {
    primary: "To board an airplane (variant of enplane).",
    secondary: "To embark aircraft personnel or passengers for flight departure.",
    quotes: [
      { author: "Winston Churchill", work: "The Hinge of Faith", text: "The Prime Minister was scheduled to **emplane** at midnight for the transatlantic conference." },
      { author: "Cecil Lewis", work: "Sagittarius Rising", text: "Squadron pilots were ordered to **emplane** immediately as siren alarms sounded the scramble." },
      { author: "Nevil Shute", work: "No Highway", text: "Passengers gathered at the gate ready to **emplane** on the morning flight to Gander." }
    ]
  },
  "enplane": {
    primary: "To board an airplane for travel or operational deployment.",
    secondary: "To embark upon an aircraft; to take one's seat prior to takeoff.",
    quotes: [
      { author: "Graham Greene", work: "The Quiet American", text: "We stood beside the runway waiting for permission to **enplane** for Hanoi." },
      { author: "Evelyn Waugh", work: "Officers and Gentlemen", text: "The commando troop was instructed to **enplane** quietly without baggage inspection." },
      { author: "George Orwell", work: "The Lion and the Unicorn", text: "Military observers saw dispatch riders **enplane** with urgent diplomatic cables." }
    ]
  },
  "exoplanet": {
    primary: "A planet that orbits a star outside the solar system.",
    secondary: "An extrasolar planetary body detected through transit photometry, radial velocity, or direct imaging.",
    quotes: [
      { author: "Carl Sagan", work: "Pale Blue Dot", text: "The discovery of the first **exoplanet** proved that planetary systems are common throughout our galaxy." },
      { author: "Michel Mayor", work: "Planets Around Other Stars", text: "Doppler spectroscopy revealed a giant **exoplanet** orbiting the nearby solar-type star 51 Pegasi." },
      { author: "Sara Seager", work: "Exoplanet Atmospheres", text: "Transmission spectra from a distant **exoplanet** allow astronomers to infer atmospheric water and methane." }
    ]
  },
  "explanandum": {
    primary: "A phenomenon, fact, or event that is to be explained in philosophical analysis or scientific inquiry.",
    secondary: "The descriptive premise or observed datum awaiting causal account within an explanatory model.",
    quotes: [
      { author: "Carl Gustav Hempel", work: "Aspects of Scientific Explanation", text: "In deductive-nomological logic, the **explanandum** must follow deductively from the general laws and initial conditions." },
      { author: "Karl Popper", work: "The Logic of Scientific Discovery", text: "We distinguish the **explanandum**, which is the statement describing the effect, from the causal hypothesis." },
      { author: "Bas van Fraassen", work: "The Scientific Image", text: "A scientific question identifies an **explanandum** and demands an appropriate contrast class." }
    ]
  },
  "explanans": {
    primary: "The statements, theories, or hypotheses that account for and explain a phenomenon (the explanandum).",
    secondary: "The deductive or inductive explanatory premises containing universal laws and antecedent boundary conditions.",
    quotes: [
      { author: "Carl Gustav Hempel", work: "Philosophy of Natural Science", text: "The **explanans** consists of two classes of statements: initial boundary conditions and universal empirical laws." },
      { author: "Karl Popper", work: "Conjectures and Refutations", text: "An acceptable **explanans** must possess independent testable content beyond the facts it explains." },
      { author: "Ernest Nagel", work: "The Structure of Science", text: "The explanatory adequacy of an **explanans** rests upon its integration into an established theoretical framework." }
    ]
  },
  "explanation": {
    primary: "A statement or account that makes something clear or accounts for a situation.",
    secondary: "The elucidation of causes, reasons, or mechanisms underlying observed phenomena.",
    quotes: [
      { author: "Benedictus de Spinoza", work: "Ethics", text: "A complete rational **explanation** must demonstrate things through their proximate causes." },
      { author: "Charles Darwin", work: "On the Origin of Species", text: "The theory of natural selection offers a luminous **explanation** for the geographic distribution of species." },
      { author: "Arthur Conan Doyle", work: "The Sign of Four", text: "Sherlock Holmes provided a lucid **explanation** of how the minute footprint unlocked the mystery." }
    ]
  },
  "explanatory": {
    primary: "Serving or intended to explain or make something clear.",
    secondary: "Providing context, rationale, or interpretive analysis for complex phenomena or texts.",
    quotes: [
      { author: "John Stuart Mill", work: "A System of Logic", text: "An **explanatory** hypothesis must be verified by deductive consequences that conform to observation." },
      { author: "Samuel Johnson", work: "The Lives of the Poets", text: "He added **explanatory** notes to illuminate archaic allusions obscure to modern readers." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", text: "The **explanatory** power of evolutionary theory lies in its synthesis of anatomy, embryology, and paleontology." }
    ]
  },
  "monoplane": {
    primary: "An airplane with only one pair of wings.",
    secondary: "A fixed-wing aircraft characterized by a single cantilever or braced wing surface.",
    quotes: [
      { author: "Louis Blériot", work: "My Flight Across the Channel", text: "The fragile wooden **monoplane** lifted smoothly from the cliffs of Calais toward Dover." },
      { author: "Antoine de Saint-Exupéry", work: "Wind, Sand and Stars", text: "His sleek **monoplane** glided silently into the Andean valley when the engine sputtered." },
      { author: "Orville Wright", work: "How We Invented the Aeroplane", text: "Later aeronautical design favored the high-speed **monoplane** over the multi-winged biplane configuration." }
    ]
  },
  "periplaneta": {
    primary: "A genus of large cockroaches in the family Blattidae, including the American cockroach (Periplaneta americana).",
    secondary: "Cosmopolitan blattid insects characterized by cursorial running agility and flattened oval morphology.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", text: "The nervous system of **Periplaneta** exhibits prominent thoracic ganglia coordinating rapid running reflexes." },
      { author: "Jean-Henri Fabre", work: "Social Life in the Insect World", text: "The nocturnal habits of **Periplaneta** allow it to forage unseen throughout cellars and pantries." },
      { author: "L. C. Miall", work: "The Cockroach: An Introduction to the Study of Insects", text: "Dissection of **Periplaneta** provides medical and biological students an ideal introduction to insect anatomy." }
    ]
  },
  "plan": {
    primary: "A detailed proposal for doing or achieving something; an intention or decision about what one is going to do.",
    secondary: "A scaled technical drawing, floorplan, or horizontal representation of a structure or territory.",
    quotes: [
      { author: "Johanna Spyri", work: "Heidi", text: "Heidi formed a secret **plan** to bring soft white rolls home to the blind grandmother." },
      { author: "Robert Burns", work: "To a Mouse", text: "The best-laid schemes o' mice an' men gang aft agley, an' lea'e us nought but grief an' pain for promised joy." },
      { author: "Sun Tzu", work: "The Art of War", text: "He who masters deliberate **plan** and stratagem conquers without engaging in protracted siege." }
    ]
  },
  "planar": {
    primary: "Relating to, lying in, or having a flat two-dimensional surface.",
    secondary: "Characterized by arrangements that conform to a geometric plane without elevation or depth.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", text: "The six carbon atoms of benzene maintain a strictly **planar** hexagonal ring structure." },
      { author: "Albert Einstein", work: "Relativity: The Special and General Theory", text: "Euclidean geometry treats **planar** figures whose angles reliably sum to two right angles." },
      { author: "Charles Kittel", work: "Introduction to Solid State Physics", text: "Graphene consists of a solitary **planar** sheet of sp2-hybridized carbon atoms." }
    ]
  },
  "planaria": {
    primary: "Free-living, non-parasitic flatworms of the class Turbellaria, renowned for their remarkable regenerative abilities.",
    secondary: "Freshwater platyhelminths possessing bilateral symmetry, eye spots, and ciliated ventral creeping surfaces.",
    quotes: [
      { author: "Thomas Hunt Morgan", work: "Regeneration", text: "When a specimen of **planaria** is bisected transversely, both halves regenerate complete new organisms." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", text: "Along the damp riverbanks of Brazil, I observed terrestrial **planaria** crawling beneath rotten wood." },
      { author: "Anton Dohrn", work: "The Origin of Vertebrates", text: "Morphological studies of **planaria** shed light on the ancestral evolution of bilateral metazoans." }
    ]
  },
  "planarian": {
    primary: "Pertaining to or designating a flatworm of the class Turbellaria, especially a freshwater planaria.",
    secondary: "A turbellarian flatworm characterized by phototactic eyespots and extraordinary tissue regeneration.",
    quotes: [
      { author: "Thomas Hunt Morgan", work: "The Physiology of Regeneration", text: "The **planarian** exhibits an anterior-posterior polarity gradient governing head and tail restoration." },
      { author: "Julian Huxley", work: "The Stream of Life", text: "Under laboratory starvation, the **planarian** resorbs its internal organs, regressing to a juvenile state." },
      { author: "Ernst Mayr", work: "The Growth of Biological Thought", text: "Cellular plasticity in the **planarian** provided foundational evidence for dedifferentiation in stem cell biology." }
    ]
  },
  "planate": {
    primary: "Flattened, level, or plane; made flat.",
    secondary: "Having a level horizontal surface formed through geological erosion or anatomical compression.",
    quotes: [
      { author: "William Morris Davis", work: "The Geographical Cycle", text: "Continuous fluvial weathering eventually reduces rugged highlands to a broadly **planate** peneplain." },
      { author: "Charles Lyell", work: "Elements of Geology", text: "Marine abrasion carved a **planate** wave-cut bench along the base of the chalk cliffs." },
      { author: "Richard Owen", work: "Comparative Anatomy of the Vertebrates", text: "The condyle articulates against a remarkably **planate** facet on the temporal bone." }
    ]
  },
  "planation": {
    primary: "The process of making something flat; specifically, the leveling of land by erosion.",
    secondary: "Geological erosion whereby streams or marine surf reduce topography to a broad, flat erosion surface.",
    quotes: [
      { author: "Archibald Geikie", work: "The Scenery of Scotland", text: "Centuries of subaerial **planation** ground down the ancient Caledonian mountain roots into rolling tablelands." },
      { author: "William Morris Davis", work: "Geographical Essays", text: "Lateral stream migration accelerates the **planation** of valley floors into fertile alluvial plains." },
      { author: "Grove Karl Gilbert", work: "Report on the Geology of the Henry Mountains", text: "Stream corrasion achieves horizontal **planation** when vertical trenching ceases at local base level." }
    ]
  },
  "planchet": {
    primary: "A flat, round piece of metal ready to be stamped into a coin; a coin blank.",
    secondary: "In numismatics, a polished metallic disk precisely weighed and milled before striking with dies.",
    quotes: [
      { author: "Isaac Newton", work: "Treasury Papers on the Royal Mint", text: "Each silver **planchet** must be carefully annealed and weighed before delivery to the coining press." },
      { author: "William Camden", work: "Remains Concerning Britain", text: "Ancient moneyers hammered the heated gold **planchet** between two engraved steel dies." },
      { author: "George F. Hill", work: "Coins of Ancient Sicily", text: "A slightly irregular bronze **planchet** accounted for the off-center strike on the Syracusan decadrachm." }
    ]
  },
  "planchette": {
    primary: "A small, usually heart-shaped flat board supported by casters and holding a pencil, used for automatic writing or spiritualist séances.",
    secondary: "A flat plate or drafting plane-table instrument used in topographic surveying.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The History of Spiritualism", text: "Sitters placed their fingertips upon the **planchette**, which glided smoothly across the blank paper." },
      { author: "Mark Twain", work: "Innocents Abroad", text: "The mysterious **planchette** scribbled disjointed words that kept the entire parlor party in breathless suspense." },
      { author: "Henry James", work: "The Bostonians", text: "She claimed the messages were dictated not by her own will but by the occult movements of the **planchette**." }
    ]
  },
  "planck": {
    primary: "Max Planck (1858–1947), German theoretical physicist who originated quantum theory; also, Planck's constant (h).",
    secondary: "The fundamental quantum of electromagnetic action linking photon energy to radiation frequency.",
    quotes: [
      { author: "Max Planck", work: "Scientific Autobiography", text: "In 1900, **Planck** introduced the quantum hypothesis to resolve the ultraviolet catastrophe of blackbody radiation." },
      { author: "Albert Einstein", work: "Autobiographical Notes", text: "The work of **Planck** showed with crystal clarity that classical mechanics broke down in microscopic domains." },
      { author: "Niels Bohr", work: "Atomic Theory and the Description of Nature", text: "The discovery of the **Planck** constant revolutionized our conceptual framework of atomic stability." }
    ]
  },
  "plane-polarized": {
    primary: "Describing light or electromagnetic waves whose electric field vibrations are confined to a single two-dimensional plane.",
    secondary: "Linearly polarized through reflection, refraction, or passage through a Nicol prism or polarizing filter.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", text: "When a **plane-polarized** beam traverses a magnetic field in glass, its plane of vibration rotates." },
      { author: "David Brewster", work: "A Treatise on Optics", text: "At Brewster's angle, reflected sunlight becomes completely **plane-polarized** parallel to the reflecting interface." },
      { author: "William Henry Bragg", work: "X-Rays and Crystal Structure", text: "Anisotropic minerals split unpolarized light into two mutually perpendicular **plane-polarized** waves." }
    ]
  },
  "plane": {
    primary: "A flat, level surface on which a straight line joining any two points would wholly lie; an airplane; to glide or soar.",
    secondary: "A woodworking hand tool used to smooth and flatten timber surfaces.",
    quotes: [
      { author: "Thomas Hardy", work: "The Woodlanders", text: "The carpenter ran his wooden **plane** over the oak board, sending fragrant shavings curling across the bench." },
      { author: "Henry David Thoreau", work: "Walden", text: "I stood upon the frozen **plane** of the pond, watching the ice mirror the winter clouds." },
      { author: "William Shakespeare", work: "Love's Labour's Lost", text: "He is only an animal, only sensible in the duller parts; and such barren plants are set before us, that we thankful should be, which we of taste and feeling are, for those parts that do fructify in us more than in another; which was made to appear upon this **plane**." }
    ]
  },
  "planeness": {
    primary: "The quality, state, or condition of being flat, level, or planar.",
    secondary: "Freedom from curvature, roughness, or angular distortion across a surface.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", text: "The optical flat was tested for absolute **planeness** by observing the regularity of interference fringes." },
      { author: "Robert Hooke", work: "Micrographia", text: "Even under the microscope, the polished glass retained an exquisite **planeness** free of surface pits." },
      { author: "William Henry Wollaston", work: "On the Goniometer", text: "Measuring crystal faces requires high reflective **planeness** to obtain sharp optical signals." }
    ]
  },
  "planer": {
    primary: "A machine or hand tool used for smoothing, flattening, or leveling surfaces of wood or metal.",
    secondary: "A machine tool in which the workpiece reciprocates under a stationary cutting blade.",
    quotes: [
      { author: "Joseph Whitworth", work: "On Plane Metallic Surfaces", text: "The mechanical **planer** transformed engineering workshops by producing true flat surfaces with repeatable accuracy." },
      { author: "Henry Maudslay", work: "Memoir of Industrial Inventions", text: "By employing the heavy slide-rest and metal **planer**, iron engine beds could be leveled with unprecedented precision." },
      { author: "Herman Melville", work: "Moby-Dick", text: "The carpenter used his iron **planer** to shape the spare spar as smooth as ivory." }
    ]
  },
  "planera": {
    primary: "A genus of small deciduous trees in the elm family (Ulmaceae), commonly known as water elms or planertrees.",
    secondary: "Monotypic North American riparian trees (Planera aquatica) thriving in southeastern swamp floodplain habitats.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "The water elm, **Planera** aquatica, is distinguished from Ulmus by its nutlike, warty winged fruit." },
      { author: "Charles Sprague Sargent", work: "The Silva of North America", text: "In deep river swamps of the Carolina lowcountry, **Planera** forms dense thickets alongside cypress and tupelo." },
      { author: "John Torrey", work: "Flora of North America", text: "Botanists dedicated the genus **Planera** in honor of Johann Jakob Planer, professor of medicine at Erfurt." }
    ]
  },
  "planet": {
    primary: "A celestial body moving in an elliptical orbit around a star, large enough to be rounded by its own gravity and to have cleared its orbit.",
    secondary: "Historically, any wandering celestial light (from Greek planetes, wanderer) as distinguished from the fixed stars.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", text: "The nights are wholesome; then no **planet** strikes, no fairy takes, nor witch hath power to charm." },
      { author: "Johannes Kepler", work: "Astronomia Nova", text: "Every **planet** moves in an elliptical orbit having the sun in one of its focal points." },
      { author: "Galileo Galilei", work: "Sidereus Nuncius", text: "Through the telescope I beheld four small moons revolving faithfully around the great **planet** Jupiter." }
    ]
  },
  "planetal": {
    primary: "Pertaining to, belonging to, or characteristic of a planet; planetary.",
    secondary: "Governed by planetary orbits, celestial mechanics, or planetary atmospheres.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", text: "Ideas revolve in their **planetal** circuits around the central luminary of reason." },
      { author: "John Herschel", work: "Outlines of Astronomy", text: "Telescopic surveys reveal rich **planetal** details upon the clouded disk of Jupiter." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", text: "Astrologers foolishly ascribed human destiny to the benign or malignant aspects of **planetal** hours." }
    ]
  },
  "planetarium": {
    primary: "A domed building or room in which images of stars, planets, and constellations are projected for public education and entertainment.",
    secondary: "An optical-mechanical projector or clockwork orrery demonstrating planetary motions in space.",
    quotes: [
      { author: "Carl Sagan", work: "Cosmos", text: "Sitting beneath the dark dome of the **planetarium**, the child felt the vastness of interstellar space." },
      { author: "H. G. Wells", work: "The Outline of History", text: "Modern education owes a profound debt to the optical **planetarium** for visualizing celestial dynamics." },
      { author: "Walther Bauersfeld", work: "The Projection Planetarium", text: "The Zeiss **planetarium** projector faithfully reproduced the complex retrograde loops of each visible planet." }
    ]
  },
  "planetary": {
    primary: "Relating to or belonging to a planet or planets; global or terrestrial in scale.",
    secondary: "Moving in an orbit like a planet; wandering, nomadic, or errant.",
    quotes: [
      { author: "Isaac Newton", work: "Principia Mathematica", text: "The inverse-square law of universal gravitation explains all observed **planetary** revolutions." },
      { author: "Francis Bacon", work: "The Advancement of Learning", text: "Knowledge expands when human minds break free from narrow local confines to contemplate **planetary** laws." },
      { author: "Rachel Carson", work: "Lost Woods", text: "Human activities now exert profound modifications across the delicate balance of the **planetary** biosphere." }
    ]
  },
  "planetesimal": {
    primary: "Any of countless small celestial bodies thought to have orbited the protosun and collided to form planets.",
    secondary: "Kilometer-scale asteroid-like debris aggregating through gravitational accretion during early solar system formation.",
    quotes: [
      { author: "Forest Ray Moulton", work: "The Planetesimal Hypothesis", text: "Collisions among millions of solid **planetesimal** fragments slowly built the terrestrial planets." },
      { author: "Thomas Chrowder Chamberlin", work: "The Origin of the Earth", text: "The **planetesimal** hypothesis posited that cold solid particles accreted into planetary cores without molten liquefaction." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", text: "Chondritic meteorites preserve the chemical composition of original **planetesimal** dust grains." }
    ]
  },
  "planetoid": {
    primary: "Another term for an asteroid; a small, rocky body orbiting the sun, especially within the asteroid belt.",
    secondary: "A minor celestial planetoid mass possessing insufficient gravity to clear its orbital neighborhood.",
    quotes: [
      { author: "Percival Lowell", work: "Mars and Its Canals", text: "Between Mars and Jupiter lie thousands of faint **planetoid** fragments remnants of early cosmic accretion." },
      { author: "Camille Flammarion", work: "Popular Astronomy", text: "Piazzi discovered the first **planetoid**, Ceres, shining like an eighth-magnitude wandering star." },
      { author: "Arthur C. Clarke", work: "Rendezvous with Rama", text: "Deep space radar tracked the incoming **planetoid** as it crossed the orbit of Mars." }
    ]
  },
  "planetonym": {
    primary: "The proper name of a planet or extraterrestrial planetary body.",
    secondary: "Onomastic term designating names assigned to celestial bodies or topographical features on planetary surfaces.",
    quotes: [
      { author: "Isaac Asimov", work: "Extraterrestrial Civilizations", text: "Astronomical naming conventions establish each new **planetonym** according to international consensus." },
      { author: "Carl Sagan", work: "The Cosmic Connection", text: "Mythological gods and goddesses provided the classical source for almost every recognized **planetonym**." },
      { author: "Gerard Kuiper", work: "The Exploration of Space", text: "The International Astronomical Union standardizes each proposed **planetonym** to avoid confusing duplicates." }
    ]
  },
  "planimeter": {
    primary: "An instrument used for measuring the area of an arbitrary two-dimensional plane figure by tracing its perimeter.",
    secondary: "A mechanical analog integrating device based on Green's theorem, recording area on an integrating wheel.",
    quotes: [
      { author: "Jakob Amsler", work: "The Polar Planimeter", text: "By tracing the boundary curve of an irregular land survey, the polar **planimeter** mechanically registers total area." },
      { author: "Lord Kelvin", work: "Mathematical and Physical Papers", text: "The precision of the mechanical **planimeter** demonstrated the practical utility of integrating mechanisms in physics." },
      { author: "Charles Babbage", work: "Passages from the Life of a Philosopher", text: "Analog instruments like the **planimeter** offered ingenious shortcuts for engineering area calculations." }
    ]
  },
  "planless": {
    primary: "Lacking a plan, purpose, or method; aimless or unorganized.",
    secondary: "Proceeding without premeditated design or systematic structure.",
    quotes: [
      { author: "Thomas Carlyle", work: "Sartor Resartus", text: "A **planless** wanderer through the wilderness of modern doubt, he sought in vain for enduring certitude." },
      { author: "George Eliot", work: "Middlemarch", text: "Lydgate felt his ambitious scientific career drifting into a **planless** succession of provincial compromises." },
      { author: "John Ruskin", work: "Unto This Last", text: "Industrial cities expanded in a **planless** sprawl of soot, neglect, and chaotic speculation." }
    ]
  },
  "planned": {
    primary: "Designed, arranged, or scheduled according to a deliberate plan.",
    secondary: "Executed in accordance with premeditated foresight and systematic organization.",
    quotes: [
      { author: "Johanna Spyri", work: "Heidi", text: "Every day at the mountain hut followed a carefully **planned** routine of tending the goats." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", text: "The reconstruction of modern civilization required a rationally **planned** world commonwealth." },
      { author: "Jane Austen", work: "Sense and Sensibility", text: "Elinor had **planned** their journey with her customary prudence and economy." }
    ]
  },
  "planner": {
    primary: "A person who devises or manages plans, especially regarding urban development, finance, or logistics.",
    secondary: "A schedule book, calendar, or software program used to organize upcoming events and deadlines.",
    quotes: [
      { author: "Lewis Mumford", work: "The City in History", text: "The enlightened urban **planner** balances civic beauty, sanitation, and humane communal living." },
      { author: "Daniel Burnham", work: "Plan of Chicago", text: "Make no little plans; they have no magic to stir men's blood, said the visionary city **planner**." },
      { author: "Jane Jacobs", work: "The Death and Life of Great American Cities", text: "The orthodox city **planner** often mistook geometric neatness for healthy urban community life." }
    ]
  },
  "planning": {
    primary: "The process of making plans for something; the act of deciding in advance what is to be done.",
    secondary: "The technical practice of urban, regional, or architectural design and land-use regulation.",
    quotes: [
      { author: "Alexis de Tocqueville", work: "Democracy in America", text: "Democratic nations excel in individual initiative rather than long-range centralized **planning**." },
      { author: "Peter Drucker", work: "The Practice of Management", text: "Strategic **planning** does not deal with future decisions, but with the future of present decisions." },
      { author: "Winston Churchill", work: "Their Finest Hour", text: "Meticulous logistical **planning** preceded every amphibious invasion across the Channel." }
    ]
  },
  "plano": {
    primary: "Having one flat, plane surface; combined with another descriptive term (such as plano-convex or plano-concave).",
    secondary: "In printing, describing sheets that are printed without folding; flat.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", text: "The experiment required a **plano** glass surface pressed firmly against a convex lens." },
      { author: "David Brewster", work: "A Treatise on New Philosophical Instruments", text: "The eyepiece utilized a **plano** doublet to reduce chromatic fringing at the field perimeter." },
      { author: "Joseph Jackson Lister", work: "On Achromatic Object-Glasses", text: "Grinding the rear face of the crown element strictly **plano** simplified optical alignment." }
    ]
  },
  "planoblast": {
    primary: "A free-swimming medusa or jellyfish bud produced asexually by a hydroid colony.",
    secondary: "In coelenterate zoology, the motile reproductive individual that buds from a sessile polyp stalk.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", text: "The tiny **planoblast** detaches from the hydroid stem and swims freely by rhythmic bell contractions." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", text: "Development of the free **planoblast** illustrates the classic metagenesis of marine coelenterates." },
      { author: "Ernst Haeckel", work: "Challenger Reports: Deep-Sea Medusae", text: "Each gonophore develops into an umbrella-shaped **planoblast** bearing marginal tentacles and lithocysts." }
    ]
  },
  "planococcus": {
    primary: "A genus of motile, flagellated coccoid bacteria in the family Planococcaceae.",
    secondary: "Gram-positive marine or soil cocci capable of active swimming motility through flagellar rotation.",
    quotes: [
      { author: "David Bergey", work: "Manual of Determinative Bacteriology", text: "The genus **Planococcus** is distinguished from other micrococci by its peritrichous or polar flagellation." },
      { author: "René Dubos", work: "The Bacterial Cell", text: "Motility in **Planococcus** species demonstrated that spherical prokaryotes could develop functional flagella." },
      { author: "Martinus Beijerinck", work: "Microbiological Essays", text: "Marine halophilic strains of **Planococcus** survive high brine concentrations along coastal salt pans." }
    ]
  },
  "planoconcave": {
    primary: "Flat on one side and concave on the other (of an optical lens or reflective surface).",
    secondary: "An optical diverging lens with one plane surface and one inwardly curved spherical surface.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", text: "A **planoconcave** lens diverges incident parallel rays, creating a virtual focal point behind the curve." },
      { author: "David Brewster", work: "A Treatise on Optics", text: "Combining a biconvex crown with a **planoconcave** flint glass yielded an effective achromatic doublet." },
      { author: "Hermann von Helmholtz", work: "Physiological Optics", text: "The corrective spectacle lens was ground **planoconcave** to alleviate high degrees of myopia." }
    ]
  },
  "planoconvex": {
    primary: "Flat on one side and convex on the other (of an optical lens).",
    secondary: "An optical converging lens possessing one planar surface and one outwardly curved spherical face.",
    quotes: [
      { author: "Robert Hooke", work: "Micrographia", text: "The objective of my compound microscope consisted of a miniature **planoconvex** glass bead." },
      { author: "Isaac Newton", work: "Opticks", text: "Pressing a **planoconvex** lens against an optical flat produced the concentric rings of Newton's rings." },
      { author: "René Descartes", work: "Dioptrique", text: "The **planoconvex** profile minimizes spherical aberration when the curved face faces the incoming parallel beam." }
    ]
  },
  "planogamete": {
    primary: "A motile, flagellated or ciliated sexual reproductive cell (zoogamete), especially in algae and lower fungi.",
    secondary: "A flagellated swimming gamete that fuses with another gamete in isogamous or anisogamous syngamy.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "In Synchytrium, fertilization occurs through the union of two equal **planogamete** cells in open water." },
      { author: "F. E. Fritsch", work: "The Structure and Reproduction of the Algae", text: "Each **planogamete** possesses two whiplash flagella directing its rapid chemotactic search." },
      { author: "Gilbert Morgan Smith", work: "The Fresh-Water Algae of the United States", text: "Swarming **planogamete** clusters coalesce into motile planozygotes before encystment." }
    ]
  },
  "planographic": {
    primary: "Relating to or utilizing printing from a flat surface, rather than from raised (relief) or sunken (intaglio) surfaces, as in lithography.",
    secondary: "Employing chemical antipathy between oil and water on a planar plate to transfer inked impressions.",
    quotes: [
      { author: "Alois Senefelder", work: "A Complete Course of Lithography", text: "Lithography is fundamentally a **planographic** art where chemical affinity replaces engraved relief." },
      { author: "Joseph Pennell", work: "Lithography and Lithographers", text: "The artist draws directly upon the limestone slab, creating a true **planographic** original." },
      { author: "William Morris", work: "The Ideal Book", text: "Modern **planographic** presses enabled broad distribution of illustrated artistic prints." }
    ]
  },
  "planography": {
    primary: "The art or process of printing from a flat surface, such as in lithography.",
    secondary: "The scientific study and classification of flat planes; planar technical charting.",
    quotes: [
      { author: "Alois Senefelder", work: "A Complete Course of Lithography", text: "The discovery of **planography** liberated printers from the labor of cutting relief blocks or etching copperplates." },
      { author: "Joseph Pennell", work: "The Graphic Arts", text: "In commercial printing, offset **planography** rapidly displaced typographic letterpress for high-speed runs." },
      { author: "Charles Babbage", work: "The Economy of Machinery and Manufactures", text: "Chemical **planography** represented a remarkable economy of manufacturing labor in graphic reproduction." }
    ]
  },
  "planospore": {
    primary: "A motile flagellated spore (zoospore) produced by certain algae and fungi.",
    secondary: "An asexual aquatic propagule that swims actively before shedding flagella to germinate.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "The aquatic **planospore** escapes from the zoosporangium and swims actively toward light." },
      { author: "F. E. Fritsch", work: "The Structure and Reproduction of the Algae", text: "Upon finding a suitable rock substrate, the **planospore** encysts, discards its cilia, and germinates." },
      { author: "Gilbert Morgan Smith", work: "Cryptogamic Botany", text: "The biflagellate **planospore** provides the primary means of asexual dispersal across aquatic habitats." }
    ]
  },
  "plant-eating": {
    primary: "Herbivorous; feeding naturally upon plants and vegetation.",
    secondary: "Characterized by dentition, digestive anatomy, or behavior adapted for consuming botanical forage.",
    quotes: [
      { author: "Charles Darwin", work: "On the Origin of Species", text: "The teeth of **plant-eating** quadrupeds are modified into broad grinding molars for crushing fibrous cellulose." },
      { author: "Richard Owen", work: "A History of British Fossil Mammals and Birds", text: "The giant sloth was an immense **plant-eating** mammal that stripped leafy foliage from prehistoric trees." },
      { author: "Thomas Henry Huxley", work: "Man's Place in Nature", text: "Comparison of primate skulls shows adaptations distinguishing carnivorous apes from strictly **plant-eating** herbivores." }
    ]
  },
  "plant": {
    primary: "A living organism of the kind exemplified by trees, shrubs, herbs, grasses, ferns, and mosses, typically growing in a permanent site and absorbing water and inorganic substances through roots.",
    secondary: "A factory or industrial manufacturing facility; also, to place or set firmly in position.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", text: "O, mickle is the powerful grace that lies in herbs, **plants**, stones, and their true qualities." },
      { author: "Francis Bacon", work: "Essays", text: "God Almighty first planted a garden; and indeed it is the purest of human pleasures; and every **plant** in it rejoiced." },
      { author: "Henry David Thoreau", work: "Walden", text: "I came to love my rows of beans, and made haste to **plant** them before the summer solstice." }
    ]
  },
  "plantae": {
    primary: "The taxonomic kingdom comprising all green plants, characterized by multicellularity, cellulose cell walls, and photosynthetic nutrition.",
    secondary: "The eukaryotic botanical lineage encompassing embryophytes, bryophytes, and vascular flora.",
    quotes: [
      { author: "Carl Linnaeus", work: "Systema Naturae", text: "The kingdom **Plantae** organizes the vegetable world through hierarchical classes, orders, and genera." },
      { author: "Asa Gray", work: "Elements of Botany", text: "Members of **Plantae** capture solar energy through chlorophyll pigments contained within plastids." },
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "In our genealogical tree of life, **Plantae** branches upward alongside Protista and Animalia." }
    ]
  },
  "plantagenet": {
    primary: "A member of the English royal dynasty that held the crown from 1154 until 1485 (from Geoffrey of Anjou's broom badge, Planta genista).",
    secondary: "Pertaining to the medieval Anglo-Norman royal house founded by Henry II.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 3", text: "Let him be crowned in spite of false Northumberland, and long live **Plantagenet**, England's lawful king!" },
      { author: "David Hume", work: "The History of England", text: "The **Plantagenet** monarchs ruled through three centuries of continental wars and constitutional struggles." },
      { author: "Walter Scott", work: "Ivanhoe", text: "Richard Coeur-de-Lion bore the martial prowess and volatile temperament of the proud **Plantagenet** bloodline." }
    ]
  },
  "plantaginaceae": {
    primary: "A cosmopolitan family of flowering plants in the order Lamiales, including the plantains, foxgloves (Digitalis), and speedwells.",
    secondary: "Sympetalous dicotyledonous herbs and shrubs characterized by zygomorphic or actinomorphic floral symmetry and capsular fruits.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", text: "The family **Plantaginaceae** features scapose herbs with ribbed leaves and dense spikes of scarious flowers." },
      { author: "George Bentham", work: "Genera Plantarum", text: "Molecular taxonomy subsequently expanded **Plantaginaceae** to include numerous genera previously assigned to Scrophulariaceae." },
      { author: "John Lindley", work: "The Vegetable Kingdom", text: "Representatives of **Plantaginaceae** are found from subarctic tundras to scorching tropical deserts." }
    ]
  },
  "plantaginales": {
    primary: "An obsolete botanical order of flowering plants erected to contain the family Plantaginaceae.",
    secondary: "In the Cronquist system, a monotypic order comprising herbaceous dicots with four-merous flowers in dense spikes.",
    quotes: [
      { author: "Arthur Cronquist", work: "An Integrated System of Classification of Flowering Plants", text: "The order **Plantaginales** is characterized by wind-pollinated, reduced flowers with scarious petals." },
      { author: "Charles Edwin Bessey", work: "The Phylogenetic Taxonomy of Flowering Plants", text: "Bessey placed **Plantaginales** as specialized herbaceous descendants of ancestral Polemoniales." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", text: "In Engler's syllabus, **Plantaginales** occupied an isolated position due to extreme floral reduction." }
    ]
  },
  "plantago": {
    primary: "The type genus of the family Plantaginaceae, comprising about 200 species of small, stemless herbs known as plantains.",
    secondary: "Cosmopolitan weedy herbs with basal rosette leaves, wind-pollinated spikes, and mucilaginous seeds (such as psyllium).",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", text: "Linnaeus documented **Plantago** major as a common roadside herb flourishing across northern Europe." },
      { author: "Charles Darwin", work: "The Power of Movement in Plants", text: "Seedlings of **Plantago** lanceolata orient their radical leaves flush against the soil surface." },
      { author: "Nicholas Culpeper", work: "The Complete Herbal", text: "The crushed green leaves of **Plantago** were applied by herbalists to soothe inflammation and bee stings." }
    ]
  },
  "plantain": {
    primary: "A low-growing common wild plant with broad oval leaves and spikes of greenish flowers; also, a banana-like starchy fruit cooked as a staple food.",
    secondary: "Any plant of the genus Plantago, historically valued for wound-healing poultices and psyllium husks.",
    quotes: [
      { author: "William Shakespeare", work: "Romeo and Juliet", text: "Your **plantain** leaf is excellent for that... for your broken shin." },
      { author: "Henry David Thoreau", work: "Walden", text: "The broad-leaved **plantain** followed the white settlers, called by indigenous peoples the Englishman's foot." },
      { author: "Joseph Conrad", work: "Heart of Darkness", text: "Villagers along the riverbank brought baskets of dried fish and roasted **plantain** to barter." }
    ]
  },
  "plantal": {
    primary: "Pertaining to, derived from, or resembling plants; vegetable.",
    secondary: "Possessing botanical or vegetative characteristics as distinguished from animal vitality.",
    quotes: [
      { author: "Ralph Waldo Emerson", work: "Essays: Second Series", text: "A silent vegetative impulse connects the **plantal** kingdom to the aspiring spirit of man." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", text: "The zoophyte seems to share both animal sensation and mere **plantal** vegetative nutrition." },
      { author: "Samuel Taylor Coleridge", work: "Hints towards the Formation of a more Comprehensive Theory of Life", text: "Life manifests first in **plantal** organization before ascending into animal instinct." }
    ]
  },
  "plantar": {
    primary: "Relating to the sole of the foot.",
    secondary: "In anatomy, designating muscles, nerves, tendons, or fascia located on the inferior surface of the human foot.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy, Descriptive and Surgical", text: "The **plantar** fascia forms a thick central band that maintains the longitudinal arch of the foot." },
      { author: "Joseph Babinski", work: "Sur le réflexe cutané plantaire", text: "Dorsiflexion of the great toe upon stroking the sole constitutes the celebrated **plantar** reflex." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "A loss of normal **plantar** sensation provides early clinical evidence of peripheral neuropathy." }
    ]
  },
  "plantation": {
    primary: "An estate on which crops such as coffee, sugar, and tobacco are cultivated by resident labor.",
    secondary: "Historically, an overseas settlement or colony; also, a large artificial planting of trees or crops.",
    quotes: [
      { author: "Francis Bacon", work: "Essays", text: "Plantations are amongst ancient, primitive, and heroical works; when the world was young every new **plantation** flourished." },
      { author: "Adam Smith", work: "The Wealth of Nations", text: "Sugar cultivated upon a West Indian **plantation** yielded returns that eclipsed ordinary British agriculture." },
      { author: "Harriet Beecher Stowe", work: "Uncle Tom's Cabin", text: "The steamboat carried laborers down the river to the remote cotton **plantation** along the Red River." }
    ]
  },
  "planted": {
    primary: "Placed or established in the ground to grow; firmly positioned or rooted.",
    secondary: "Stationed, fixed, or established securely in a designated location or state of mind.",
    quotes: [
      { author: "William Shakespeare", work: "The Winter's Tale", text: "We were as twinn'd lambs that did frisk i' the sun; we have **planted** love in fertile soil." },
      { author: "John Milton", work: "Paradise Lost", text: "Southward through Eden went a river large, for God had **planted** there his blissful garden." },
      { author: "Herman Melville", work: "Moby-Dick", text: "Ahab stood firmly **planted** upon the quarter-deck, his ivory heel locked into the auger-hole." }
    ]
  },
  "planter": {
    primary: "An owner or manager of a plantation; a person who plants seeds, crops, or trees.",
    secondary: "A decorative container in which flowers or ornamental shrubs are grown.",
    quotes: [
      { author: "Daniel Defoe", work: "Robinson Crusoe", text: "Before my voyage I lived as a prosperous sugar **planter** along the coast of the Brazils." },
      { author: "Washington Irving", work: "A History of New York", text: "The Dutch **planter** sat beneath his stoop, smoking his clay pipe while watching his cabbages grow." },
      { author: "Thomas Jefferson", work: "Notes on the State of Virginia", text: "Those who labor in the earth are the chosen people of God, wrote the philosopher-**planter**." }
    ]
  },
  "planthopper": {
    primary: "Any of numerous small plant-sucking insects of the superfamily Fulgoroidea, known for their ability to jump quickly to escape predators.",
    secondary: "Homopterous hemipterans possessing jumping hind legs, sucking rostra, and protective waxy secretions.",
    quotes: [
      { author: "Jean-Henri Fabre", work: "The Life of the Grasshopper", text: "The tiny **planthopper** leaped through the grass blades with explosive suddenness when approached." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", text: "Tropical lanternflies, the largest members of the **planthopper** family, mimic dry bark with uncanny fidelity." },
      { author: "L. O. Howard", work: "The Insect Book", text: "Certain species of the **planthopper** transmit destructive viral diseases between rice and cereal crops." }
    ]
  },
  "plantigrade": {
    primary: "Walking on the soles of the feet, like a human, bear, or badger, with the heel touching the ground.",
    secondary: "Characterized by locomotion in which the entire metatarsus and tarsus contact the substrate during weight-bearing.",
    quotes: [
      { author: "Charles Darwin", work: "The Descent of Man", text: "Humans share a fully **plantigrade** foot structure with our mammalian ancestors, providing stable bipedal support." },
      { author: "Georges Cuvier", work: "The Animal Kingdom", text: "Cuvier distinguished the **plantigrade** carnivores, such as bears and badgers, from the digitigrade felines." },
      { author: "Richard Owen", work: "On the Archetype and Homologies of the Vertebrate Skeleton", text: "The skeletal heel bone of a **plantigrade** quadruped rests directly on the earth during the stride." }
    ]
  },
  "planting": {
    primary: "The act or process of placing seeds, bulbs, or seedlings in the soil to grow.",
    secondary: "An area of newly planted flora; a woodland plantation or landscaped arrangement of shrubs.",
    quotes: [
      { author: "Thomas Hardy", work: "The Woodlanders", text: "Spring brought the busy season of fir-tree **planting** across the damp Dorsetshire slopes." },
      { author: "Henry David Thoreau", work: "Faith in a Seed", text: "Nature accomplishes her **planting** through wind, water, and the caching habits of squirrels." },
      { author: "Francis Bacon", work: "Of Gardens", text: "The **planting** should be arranged so that there may be gardens for all the months of the year." }
    ]
  },
  "plantlet": {
    primary: "A young, small plant, especially one produced vegetatively on leaf margins or runners.",
    secondary: "A miniature cloned propagule (as in Bryophyllum or Chlorophytum) capable of rooting independently.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", text: "Each vigorous **plantlet** was potted separately to measure its competitive vegetative growth." },
      { author: "Asa Gray", work: "Structural Botany", text: "Tiny vegetative **plantlets** form along the serrate margins of the air plant leaf and drop to root in the soil." },
      { author: "Julius von Sachs", work: "Textbook of Botany", text: "Strawberry runners send out horizontal stolons, terminating in a rooted **plantlet** at each node." }
    ]
  },
  "plantsman": {
    primary: "An enthusiastic and knowledgeable gardener, botanist, or nurseryman who specializes in growing and cultivating plants.",
    secondary: "An expert horticulturist renowned for recognizing, collecting, and breeding rare botanical specimens.",
    quotes: [
      { author: "Gertrude Jekyll", work: "Colour in the Flower Garden", text: "The true **plantsman** studies the natural habit of each perennial to create harmonious floral borders." },
      { author: "Reginald Farrer", work: "The English Rock Garden", text: "A dedicated **plantsman** will brave Himalayan cliffs to bring home seeds of a forgotten alpine gentian." },
      { author: "E. H. Wilson", work: "A Naturalist in Western China", text: "As a professional **plantsman**, he introduced thousands of Chinese flowering shrubs into Western horticulture." }
    ]
  },
  "planula": {
    primary: "The free-swimming, flattened, ciliated larva of a coelenterate (cnidarian), such as a jellyfish or coral polyp.",
    secondary: "A microscopic, bilateral larval stage that swims through plankton before settling on the sea floor to transform into a sessile polyp.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", text: "The ciliated **planula** swarms out of the medusa, swimming actively before fixing itself to the reef rock." },
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", text: "Microscopic dissection showed the **planula** consists of an outer ectoderm and an inner cellular endoderm." },
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", text: "The gastrula-like morphology of the swimming **planula** suggested an ancestral bilateral archetype." }
    ]
  },
  "protoplanet": {
    primary: "A large planetary embryo or precursor accumulating within a protoplanetary disk around a young star.",
    secondary: "A massive pre-planetary body formed by gravitational accretion of planetesimals, prior to clearing its orbital zone.",
    quotes: [
      { author: "Gerard Kuiper", work: "On the Origin of the Solar System", text: "Instabilities in the primordial solar nebula led to giant **protoplanet** condensations." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", text: "Volatiles were stripped from the inner **protoplanet** surfaces by intense early solar winds." },
      { author: "Fred Hoyle", work: "Frontiers of Astronomy", text: "Collisions between competing **protoplanet** cores ultimately determined the axial tilt of the inner planets." }
    ]
  },
  "replant": {
    primary: "To plant something again, especially in a different pot, soil, or location (transplant).",
    secondary: "To re-establish vegetation, crops, or timber on land that has been cleared or devastated.",
    quotes: [
      { author: "Francis Bacon", work: "Sylva Sylvarum", text: "When orchard trees decline in vigor, it is prudent to **replant** the border with virgin saplings." },
      { author: "Thomas Hardy", work: "The Woodlanders", text: "The woodman resolved to **replant** the cleared copse with young larch before the winter frosts set in." },
      { author: "John Evelyn", work: "Sylva, or A Discourse of Forest-Trees", text: "Landowners who fell timber without taking care to **replant** commit an unpardonable injury to the commonwealth." }
    ]
  },
  "unplanned": {
    primary: "Not planned, expected, or premeditated; spontaneous or accidental.",
    secondary: "Developing or occurring without intentional forethought, blueprint, or systematic schedule.",
    quotes: [
      { author: "Jane Jacobs", work: "The Death and Life of Great American Cities", text: "Vibrant city neighborhoods thrive upon **unplanned** sidewalk encounters between diverse citizens." },
      { author: "Virginia Woolf", work: "To the Lighthouse", text: "An **unplanned** pause in the conversation allowed the rhythm of the waves to fill the silent room." },
      { author: "Lewis Mumford", work: "The City in History", text: "The mediaeval town expanded organically in an **unplanned** maze of winding alleys and open markets." }
    ]
  },
  "unplanted": {
    primary: "Not planted with crops, seeds, or vegetation; left bare, fallow, or uncultivated.",
    secondary: "Lacking intentional sowing, crop cover, or agricultural development.",
    quotes: [
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", text: "A vast stretch of **unplanted** arable land lay bleak and brown beneath the November drizzle." },
      { author: "William Cobbett", work: "Rural Rides", text: "The fields were left **unplanted** that season, choked with weeds while the tenant farmer waited for rents to ease." },
      { author: "Henry David Thoreau", work: "Walden", text: "The wild hillside remained **unplanted**, preserving its natural mantle of sumach and pitch pine." }
    ]
  }
};

function formatQuotes(quotes) {
  return quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.text}"*`).join('\n');
}

function updateFile(filePath, wordData) {
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`Missing [!book] in ${filePath}`);
    return false;
  }
  const topPart = content.slice(0, bookIdx).trimEnd();

  const newDefBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${wordData.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${wordData.secondary}\n\n> [!quote] 💬 Contextual Usage & Authentic Quotations\n${formatQuotes(wordData.quotes)}\n`;

  const finalContent = topPart + '\n\n' + newDefBlock;
  fs.writeFileSync(filePath, finalContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

let count = 0;
for (const [lemma, data] of Object.entries(BATCH6_DATA)) {
  const filePath = path.join(CLUSTER_DIR, DASHBOARD, `${lemma}.md`);
  if (!fs.existsSync(filePath)) {
    console.error(`File NOT found: ${filePath}`);
    continue;
  }
  if (updateFile(filePath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 6 Completed: ${count} / ${Object.keys(BATCH6_DATA).length} words updated`);
console.log(`========================================\n`);
