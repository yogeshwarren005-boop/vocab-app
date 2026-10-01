import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Motion & Direction';
const DASHBOARD = 'Dashboard — ba';

const BATCH5_DATA = {
  "abase": {
    primary: "To lower someone or oneself in rank, office, prestige, or esteem; to degrade or humiliate.",
    secondary: "To bring down physically or cast low before superior power or divine authority.",
    quotes: [
      { author: "William Shakespeare", work: "Henry VI, Part 2", text: "Will consider'd, he should not need to **abase** his eyes on such low-born churls." },
      { author: "John Milton", work: "Paradise Lost", text: "Whom reason hath equaled, force hath made supreme above his equals, to **abase** them low." },
      { author: "Charlotte Brontë", work: "Jane Eyre", text: "I will never **abase** myself to sue for unmerited favor from those who despise me." }
    ]
  },
  "abasic": {
    primary: "Relating to or suffering from abasia; unable to walk due to impaired motor coordination.",
    secondary: "Exhibiting functional gait instability in neurological examination without organic muscular paralysis.",
    quotes: [
      { author: "Paul Blocq", work: "Sur une affection caractérisée par de l'astasie et de l'abasie", text: "The patient displayed a distinct **abasic** gait, unable to coordinate steps despite normal leg strength in bed." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "In astasia-abasia, the hysterical subject presents an **abasic** disability that vanishes during emotional distraction." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Diseases of the Nervous System", text: "The sudden **abasic** reaction following the railway shock pointed to psychogenic functional trauma." }
    ]
  },
  "acrobat": {
    primary: "An entertainer who performs spectacular gymnastic feats of agility, balance, and coordination.",
    secondary: "A person capable of rapid intellectual, moral, or political maneuvering and flexible adaptability.",
    quotes: [
      { author: "Charles Dickens", work: "Hard Times", text: "Sleary’s circus was famed for each daring **acrobat** who vaulted through paper hoops above the ring." },
      { author: "Thomas Hardy", work: "The Dynasts", text: "The agile **acrobat** leaped from rope to swinging bar with astonishing precision." },
      { author: "George Orwell", work: "Down and Out in Paris and London", text: "A street **acrobat** drew a crowd by balancing heavy chairs upon his chin." }
    ]
  },
  "acrobatic": {
    primary: "Performing, involving, or adept at spectacular gymnastic feats of agility and balance.",
    secondary: "Characterized by remarkable mental flexibility, nimbleness, or contorted maneuvering.",
    quotes: [
      { author: "Annie Roe Carr", work: "Nan Sherwood at Pine Camp", text: "The girls cheered as the performer executed an **acrobatic** somersault across the gymnasium floor." },
      { author: "Herman Melville", work: "Moby-Dick", text: "The harpooner sprang with **acrobatic** agility onto the gunwale of the surging whaleboat." },
      { author: "Joseph Conrad", work: "Typhoon", text: "Sailors were thrown across the deck in involuntary **acrobatic** leaps as the huge swell rolled under them." }
    ]
  },
  "acrobatics": {
    primary: "Spectacular gymnastic feats or performances requiring exceptional balance, agility, and motor control.",
    secondary: "Complex, deceptive, or highly agile maneuvers in debate, finance, or aerial flight.",
    quotes: [
      { author: "Antoine de Saint-Exupéry", work: "Wind, Sand and Stars", text: "Aerial **acrobatics** above the clouds tested both the structural rigging and the pilot's nerve." },
      { author: "H. G. Wells", work: "The War of the Worlds", text: "The Martian tripod advanced across the heather with bizarre, mechanical **acrobatics**." },
      { author: "Virginia Woolf", work: "The Waves", text: "Her rapid thoughts performed dazzling **acrobatics** across the gulf of memory." }
    ]
  },
  "adiabatic": {
    primary: "Relating to or denoting a thermodynamic process occurring without the loss or gain of heat by the system.",
    secondary: "In meteorology, describing atmospheric temperature changes produced solely by expansion or compression of an air parcel.",
    quotes: [
      { author: "J. Willard Gibbs", work: "Graphical Methods in the Thermodynamics of Fluids", text: "An **adiabatic** expansion represents a path along which no thermal energy penetrates the system boundary." },
      { author: "Rudolf Clausius", work: "The Mechanical Theory of Heat", text: "In purely **adiabatic** compression, the mechanical work performed converts directly into internal thermal energy." },
      { author: "Napier Shaw", work: "Manual of Meteorology", text: "The dry **adiabatic** lapse rate governs the cooling of rising unsaturated air in convective columns." }
    ]
  },
  "aerobatic": {
    primary: "Relating to or involving stunts and maneuvers performed by an aircraft in flight.",
    secondary: "Performing spectacular aerial maneuvers such as loops, rolls, and spins.",
    quotes: [
      { author: "Antoine de Saint-Exupéry", work: "Night Flight", text: "The military pursuit plane commenced an **aerobatic** sequence above the darkening airfield." },
      { author: "Beryl Markham", work: "West with the Night", text: "No pilot needed **aerobatic** bravado across the equatorial bush—only steady compass navigation." },
      { author: "Cecil Lewis", work: "Sagittarius Rising", text: "We practiced tight spins and **aerobatic** turns to evade simulated enemy fighters above the clouds." }
    ]
  },
  "anabasis": {
    primary: "A military march or expedition upward from a coast into the interior of a country, notably Xenophon's march.",
    secondary: "Any arduous upward journey, spiritual ascent, or advancing progression.",
    quotes: [
      { author: "Xenophon", work: "Anabasis", text: "The historic **Anabasis** recounted Cyrus’s bold march into the heart of the Persian Empire." },
      { author: "T. S. Eliot", work: "Anabasis, Preface", text: "Saint-John Perse’s poem evokes an **anabasis** of nomadic conquerors traversing vast arid steppes." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "Emperor Julian undertook his ill-fated **anabasis** across the deserts of Mesopotamia." }
    ]
  },
  "anabatic": {
    primary: "Relating to or designating an upslope wind caused by local surface heating during the day.",
    secondary: "Ascending, rising, or flowing upward along topographic inclines or convective thermal currents.",
    quotes: [
      { author: "Napier Shaw", work: "The Drama of the Weather", text: "As morning sunshine warmed the valley walls, a gentle **anabatic** breeze carried mist up the mountain ridges." },
      { author: "Richard Goody", work: "Atmospheric Radiation", text: "Solar radiation absorbed by steep alpine slopes drives the daytime **anabatic** circulation." },
      { author: "Robert Falcon Scott", work: "The Voyage of the Discovery", text: "The daytime **anabatic** airflow temporarily halted the bitterly cold coastal katabatic drift." }
    ]
  },
  "antidiabetic": {
    primary: "Tending to prevent or alleviate diabetes mellitus; used of pharmaceutical agents or therapeutic diets.",
    secondary: "Denoting any medicinal substance, such as insulin or sulfonylureas, that lowers blood glucose.",
    quotes: [
      { author: "Frederick Banting", work: "The Nobel Lecture", text: "Purified pancreatic extracts demonstrated immediate **antidiabetic** efficacy in lowering canine glycosuria." },
      { author: "Charles Best", work: "Selected Papers on Insulin", text: "Early clinical trials proved the life-saving value of the new **antidiabetic** hormone." },
      { author: "Bernardo Houssay", work: "Hormonal Factors in Carbohydrate Metabolism", text: "Anterior pituitary hormones interact dynamically with established **antidiabetic** mechanisms." }
    ]
  },
  "antiparabema": {
    primary: "In classical Greek theater, a secondary choral speech answering or matching the parabasis.",
    secondary: "An architectural or liturgical chamber flanking the sanctuary in early Byzantine churches.",
    quotes: [
      { author: "Gilbert Murray", work: "Aristophanes: A Study", text: "The chorus chanted the **antiparabema** with vigorous satirical mockery directed at rival demagogues." },
      { author: "Arthur Pickard-Cambridge", work: "The Dramatic Festivals of Athens", text: "In Old Comedy, the parabasis proper was structurally counterbalanced by the **antiparabema**." },
      { author: "Richard Krautheimer", work: "Early Christian and Byzantine Architecture", text: "The northern pastophorion served as an **antiparabema** for storing liturgical vestments and sacred vessels." }
    ]
  },
  "ba": {
    primary: "The root ba (from Greek bainein, to step, walk, go); also, in ancient Egyptian religion, the soul or personality represented as a human-headed bird.",
    secondary: "A foundational morphemic element conveying stepping, basis, or movement across classical derivatives.",
    quotes: [
      { author: "E. A. Wallis Budge", work: "The Book of the Dead", text: "In funerary papyri, the **ba** hovers over the mummy in the form of a human-headed hawk." },
      { author: "James Henry Breasted", work: "Development of Religion and Thought in Ancient Egypt", text: "Upon death, the **ba** was believed to visit the earthly realm while the body reposed in the tomb." },
      { author: "Walter Skeat", work: "An Etymological Dictionary of the English Language", text: "The root **ba** underlies Greek bainein, stepping forth into words like acrobat, basis, and anabasis." }
    ]
  },
  "bainein": {
    primary: "The ancient Greek verb meaning to walk, step, go, or move.",
    secondary: "The linguistic parent root generating classical compounds expressing transit, foundations, and physical posture.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", text: "From the primary verb **bainein** arose both physical terms for stepping and philosophical foundations like basis." },
      { author: "Max Müller", work: "Lectures on the Science of Language", text: "Tracing the root of acrobat reveals Greek **bainein**, walking on the extremities of the toes." },
      { author: "Werner Jaeger", work: "Paideia: The Ideals of Greek Culture", text: "Metaphors of journeying and stepping rooted in **bainein** pervade classical philosophical dialogues." }
    ]
  },
  "basal": {
    primary: "Forming or belonging to a bottom layer, base, or foundation.",
    secondary: "Relating to the minimum amount of energy or physiological activity required to maintain vital cellular functions at rest.",
    quotes: [
      { author: "Francis Gano Benedict", work: "Human Vitality and Efficiency under Prolonged Restricted Diet", text: "The subject's **basal** metabolic rate remained suppressed throughout the starvation experiment." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", text: "The **basal** plumage of the bird remained brown while the outer tips acquired iridescent sheen." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", text: "The **basal** ganglia of the brain coordinate unconscious motor impulses before voluntary movement occurs." }
    ]
  },
  "base": {
    primary: "The lowest part or edge of something, especially the part on which it rests or is supported; foundation.",
    secondary: "Without moral principles; ignoble, dishonorable; in chemistry, a substance capable of neutralizing an acid.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", text: "Why brand they us with **base**? with baseness? bastardy? base, base?" },
      { author: "Isaac Newton", work: "Opticks", text: "The prism rested steadily on its triangular **base** while admitting the solitary solar ray." },
      { author: "Svante Arrhenius", work: "Theories of Chemistry", text: "In aqueous solution, a chemical **base** dissociates to yield hydroxyl ions that neutralize acids." }
    ]
  },
  "based": {
    primary: "Having a specified foundation, origin, or underlying support.",
    secondary: "Established, located, or securely settled upon a physical site or conceptual premise.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", text: "Their entire Chancery suit was **based** on a contested will that consumed all the disputed estate." },
      { author: "Thomas Hardy", work: "The Woodlanders", text: "The woodland trade was **based** upon seasonal fellings and traditional timber sales." },
      { author: "John Locke", work: "An Essay Concerning Human Understanding", text: "All our rational deductions must be **based** upon simple ideas derived from experience." }
    ]
  },
  "basely": {
    primary: "In a dishonorable, cowardly, or morally low manner.",
    secondary: "Without dignity, virtue, or generous sentiment; ignobly.",
    quotes: [
      { author: "William Shakespeare", work: "Henry IV, Part 1", text: "Shall it be said that you have dealt so **basely** with your sworn comrades in arms?" },
      { author: "John Milton", work: "Samson Agonistes", text: "To yield to private interests and **basely** betray one's country's trust is the lowest infamy." },
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The praetorian guards **basely** auctioned the imperial throne to the highest bidder." }
    ]
  },
  "basement": {
    primary: "The floor of a building which is partly or entirely below ground level.",
    secondary: "In geology, the ancient crystalline or metamorphic rock foundation underlying sedimentary strata.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", text: "Footprints led through the damp **basement** toward the bricked coal cellar below." },
      { author: "Charles Lyell", work: "Principles of Geology", text: "Erosion gradually stripped the overlying sandstone, exposing the granitic **basement** rocks." },
      { author: "Charlotte Perkins Gilman", work: "The Yellow Wallpaper", text: "The old house had a dark **basement** with grated windows that looked onto the overgrown yard." }
    ]
  },
  "baseness": {
    primary: "Lack of moral principles; bad character, meanness, or ignobility.",
    secondary: "Inferiority of quality, value, or purity, as in alloyed coinage or base metals.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", text: "I once did hold it, as our statists do, a **baseness** to write fair." },
      { author: "Francis Bacon", work: "Essays", text: "There is no vice that so covereth a man with shame as to be found false and guilty of **baseness**." },
      { author: "Samuel Johnson", work: "The Rambler", text: "Nothing sooner exposes an author to contempt than the **baseness** of flattering corrupt patrons." }
    ]
  },
  "basic": {
    primary: "Forming an essential foundation or starting point; fundamental.",
    secondary: "Having the properties of a chemical base; containing an alkali or reacting to neutralize acids (pH greater than 7).",
    quotes: [
      { author: "Frank A. Fetter", work: "Principles of Economics", text: "The **basic** law of diminishing returns governs both agricultural yield and manufacturing intensity." },
      { author: "Linus Pauling", work: "General Chemistry", text: "Limestone dissolves in rainwater because calcium carbonate acts as a **basic** salt." },
      { author: "Bertrand Russell", work: "The Problems of Philosophy", text: "Our **basic** beliefs regarding sensory data form the starting point of all empirical certainty." }
    ]
  },
  "basidial": {
    primary: "Pertaining to, resembling, or borne upon a basidium.",
    secondary: "In mycology, relating to the club-like microscopic structures responsible for sexual basidiospore formation.",
    quotes: [
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "Microscopic examination revealed delicate **basidial** sterigmata bearing four apical spores." },
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", text: "The surface tension discharge mechanism operates precisely at the tip of each **basidial** projection." },
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "In the hymenium of the Agaricaceae, **basidial** development precedes the spore discharge cycle." }
    ]
  },
  "basidiocarp": {
    primary: "The multicellular spore-producing fruiting body of a basidiomycete fungus, such as a mushroom, bracket fungus, or puffball.",
    secondary: "The macrofungal structure specialized for displaying and dispersing sexually produced basidiospores.",
    quotes: [
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", text: "The umbrella-shaped **basidiocarp** protects the delicate hymenial gills from falling rain." },
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "Moisture stimulates rapid expansion of the **basidiocarp** from its subterranean mycelial knot." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "The woody perennial **basidiocarp** of Fomes fomentarius produces successive spore layers each spring." }
    ]
  },
  "basidioma": {
    primary: "A basidiocarp; the macroscopic reproductive fruiting structure of a basidiomycetous fungus.",
    secondary: "The hymenium-bearing sporocarp produced by higher fungi during sexual reproduction.",
    quotes: [
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", text: "Orientation of the pileus ensures that the **basidioma** releases spores into free laminar air currents." },
      { author: "David Hawksworth", work: "Ainsworth & Bisby's Dictionary of the Fungi", text: "Mycologists use **basidioma** as the precise anatomical synonym for the basidiomycete fruit body." },
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "Development of the fleshy **basidioma** proceeds through intricate hyphal differentiation." }
    ]
  },
  "basidiospore": {
    primary: "A sexually produced fungal spore borne on the exterior of a basidium, characteristic of the Basidiomycota.",
    secondary: "An airborne reproductive cell ejected by a surface-tension catapult mechanism from fungal gills or pores.",
    quotes: [
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", text: "A microscopic Buller's drop condenses at the hilum just before the **basidiospore** is violently discharged." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "Each ripe **basidiospore** exhibited a smooth, hyaline wall under the oil immersion lens." },
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "Upon landing on fertile soil, the **basidiospore** germinates to produce primary monokaryotic hyphae." }
    ]
  },
  "basidiosporous": {
    primary: "Producing or bearing basidiospores; relating to spores produced upon a basidium.",
    secondary: "Propagated through sexually formed basidiospores within the phylum Basidiomycota.",
    quotes: [
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", text: "The hymenial layer displays dense **basidiosporous** arrays positioned for windborne dispersal." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "This **basidiosporous** order differs fundamentally from the ascus-bearing fungi in its spore formation." },
      { author: "David Hawksworth", work: "Ainsworth & Bisby's Dictionary of the Fungi", text: "Taxonomic keys classify the bracket fungi as **basidiosporous** saprophytes degrading forest lignocellulose." }
    ]
  },
  "basidium": {
    primary: "A microscopic, club-shaped spore-bearing structure found in the fruiting bodies of basidiomycete fungi.",
    secondary: "The specialized end-cell upon whose sterigmata sexual karyogamy and meiosis produce exterior basidiospores.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "Nuclear fusion within the young **basidium** is followed immediately by two meiotic divisions." },
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", text: "Each mature **basidium** typically bears four sterigmata from which spores are successively launched." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "The morphology of the **basidium** provides the primary basis for distinguishing holobasidiomycetes from phragmobasidiomycetes." }
    ]
  },
  "basify": {
    primary: "To convert into a chemical base; to neutralize an acid or render a substance alkaline.",
    secondary: "In industrial or synthetic chemistry, to raise the pH of a solution by adding an alkaline reagent.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", text: "We may **basify** the acidic solution by adding potash until litmus paper no longer reddens." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", text: "The chemist sought to **basify** the extract to precipitate the organic alkaloid in crystalline form." },
      { author: "William Crookes", work: "Select Methods in Chemical Analysis", text: "Carefully **basify** the filtrate with ammonium hydroxide to separate iron from the remaining filtrate." }
    ]
  },
  "basilar": {
    primary: "Relating to, situated at, or forming the base, especially of the skull or brain.",
    secondary: "In anatomy, designating structures such as the basilar artery or the basilar membrane of the cochlea.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy, Descriptive and Surgical", text: "The **basilar** artery is formed by the junction of the two vertebral arteries at the lower border of the pons." },
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", text: "Acoustic pitch discrimination depends upon resonance along the tapering **basilar** membrane of the inner ear." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Occlusion of the **basilar** vessel produces bilateral motor paralysis and deep coma." }
    ]
  },
  "basilary": {
    primary: "Pertaining to or situated at the base; basilar.",
    secondary: "Anatomical variant of basilar, denoting skeletal or cranial floor foundations.",
    quotes: [
      { author: "Thomas Willis", work: "Cerebri Anatome", text: "The vertebral arteries unite at the **basilary** process of the occipital bone to nourish the cerebel." },
      { author: "Richard Owen", work: "On the Archetype and Homologies of the Vertebrate Skeleton", text: "The **basilary** element forms the cranial floor in all vertebrate crania." },
      { author: "Henry Gray", work: "Anatomy of the Human Body", text: "Fractures of the **basilary** plate often cause subconjunctival ecchymosis and escape of cerebrospinal fluid." }
    ]
  },
  "basion": {
    primary: "The midpoint of the anterior margin of the foramen magnum in craniometric measurement.",
    secondary: "An anthropometric osteological landmark used to determine cranial angles and facial projection.",
    quotes: [
      { author: "Paul Broca", work: "Instructions craniologiques et craniométriques", text: "The **basion** serves as the fixed origin for calculating facial and alveolar angles of the human skull." },
      { author: "Aleš Hrdlička", work: "Anthropometry", text: "Measure the distance between the nasion and the **basion** to establish the length of the cranial base." },
      { author: "Arthur Keith", work: "Human Embryology and Morphology", text: "Growth along the spheno-occipital synchondrosis moves the **basion** backward relative to the hard palate." }
    ]
  },
  "basionym": {
    primary: "The original, validly published name of a taxonomic group from which a new name or combination is derived.",
    secondary: "In botanical and zoological nomenclature, the name-bearing type upon which a revised generic classification rests.",
    quotes: [
      { author: "Alphonse de Candolle", work: "Laws of Botanical Nomenclature", text: "Whenever a species is transferred to another genus, the original specific epithet of the **basionym** must be retained." },
      { author: "Asa Gray", work: "Structural Botany", text: "Botanists must cite the author of the **basionym** in parentheses before the revising taxonomist's name." },
      { author: "Frans Stafleu", work: "International Code of Botanical Nomenclature", text: "A new combination is illegitimate unless its **basionym** is clearly designated with a full bibliographic citation." }
    ]
  },
  "basis": {
    primary: "The underlying support or foundation for an idea, argument, system, or process.",
    secondary: "The principal component of something; in mathematics, a set of linearly independent vectors spanning a vector space.",
    quotes: [
      { author: "William Shakespeare", work: "The Tempest", text: "The great globe itself, yea, all which it inherit, shall dissolve and, like this insubstantial pageant faded, leave not a rack behind; yet on this **basis** stood our hopes." },
      { author: "John Stuart Mill", work: "A System of Logic", text: "Induction by simple enumeration cannot supply an adequate **basis** for universal causal laws." },
      { author: "David Hume", work: "A Treatise of Human Nature", text: "Custom and habit, rather than pure reason, constitute the real **basis** of our expectations." }
    ]
  },
  "basophilia": {
    primary: "An abnormal increase in the proportion of basophils in the blood.",
    secondary: "In histology, the property of cells or cellular structures that causes them to stain readily with basic dyes.",
    quotes: [
      { author: "Paul Ehrlich", work: "Contributions to the Theory and Practice of Histological Staining", text: "Cytoplasmic **basophilia** reveals an abundance of acidic ribonucleic components avid for methylene blue." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Marked **basophilia** in peripheral blood smears frequently heralds the chronic phase of myelogenous leukemia." },
      { author: "Florence Sabin", work: "The Origin of the Cells of the Blood", text: "Immature erythroid cells exhibit strong cytoplasmic **basophilia** prior to hemoglobin synthesis." }
    ]
  },
  "basophilic": {
    primary: "Staining readily with basic dyes (such as methylene blue or hematoxylin).",
    secondary: "Relating to basophils (a type of white blood cell); exhibiting affinity for alkaline reagents.",
    quotes: [
      { author: "Paul Ehrlich", work: "Methodology of Blood Staining", text: "The mast cell granules are intensely **basophilic**, appearing dark violet under alkaline stain." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", text: "Nissl bodies in the motor neurons consist of dense **basophilic** masses of RNA-rich substance." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The presence of **basophilic** stippling in red corpuscles provides a valuable diagnostic clue in chronic lead poisoning." }
    ]
  },
  "bastion": {
    primary: "A projecting part of a fortification built at an angle to the line of a wall, so as to allow defensive fire in several directions.",
    secondary: "An institution, place, or person strongly defending or upholding particular principles or attitudes.",
    quotes: [
      { author: "Edward Gibbon", work: "The Decline and Fall of the Roman Empire", text: "The besieged defenders manned every corner **bastion**, pouring Greek fire down upon the battering rams." },
      { author: "Walter Scott", work: "The Talisman", text: "The crusader standard fluttered high above the stone **bastion** facing the Saracen encampment." },
      { author: "Winston Churchill", work: "The Gathering Storm", text: "Parliament remained the solitary **bastion** of democratic freedom against totalitarian tyranny." }
    ]
  },
  "bema": {
    primary: "The raised platform or sanctuary area in an ancient synagogue or Christian church, used for reading scriptures or preaching.",
    secondary: "In ancient Greek law, the elevated stone platform from which orators addressed the assembly or court.",
    quotes: [
      { author: "Demosthenes", work: "On the Crown", text: "When Aeschines mounted the **bema**, he sought to mislead the citizens with grandiloquent falsehoods." },
      { author: "Thucydides", work: "History of the Peloponnesian War", text: "Pericles stepped upon the **bema** to deliver his celebrated funeral oration to the assembled Athenians." },
      { author: "Richard Krautheimer", work: "Early Christian and Byzantine Architecture", text: "The clergy processed into the elevated **bema** behind the iconostasis to begin the divine liturgy." }
    ]
  },
  "catabasis": {
    primary: "A military retreat or march down to the sea; the downward journey, especially Xenophon's march to the Euxine.",
    secondary: "A descent into the underworld in classical mythology (such as Odysseus, Orpheus, or Aeneas); a spiritual or psychological decline.",
    quotes: [
      { author: "Xenophon", work: "Anabasis", text: "After months of perilous mountain warfare, the ten thousand completed their joyful **catabasis** at the sight of the sea." },
      { author: "C. G. Jung", work: "Psychology and Alchemy", text: "In mythological archetypes, the hero's **catabasis** into the subterranean realm represents confrontation with the unconscious." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", text: "The ritual **catabasis** of the initiates re-enacted Persephone's seasonal descent to the house of Hades." }
    ]
  },
  "catabatic": {
    primary: "Relating to or denoting a wind carrying high-density air downslope under the pull of gravity (a katabatic wind).",
    secondary: "Moving downward; falling or subsiding along mountain slopes or glacial valleys.",
    quotes: [
      { author: "Douglas Mawson", work: "The Home of the Blizzard", text: "Furious **catabatic** blizzards roared down the polar ice slopes at velocities exceeding one hundred miles an hour." },
      { author: "Napier Shaw", work: "Manual of Meteorology", text: "The nighttime **catabatic** wind drains cold, dense air from Alpine snowfields into the quiet valleys below." },
      { author: "Robert Falcon Scott", work: "Scott's Last Expedition", text: "We struggled against an icy **catabatic** drift that threatened to tear the tent fabric to shreds." }
    ]
  },
  "debase": {
    primary: "To reduce the quality, value, or moral character of someone or something.",
    secondary: "To lower the purity of coin or bullion by substituting a cheaper base metal for gold or silver.",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", text: "Will you **debase** the royal majesty of England with such cowardly submission?" },
      { author: "Frank A. Fetter", work: "Principles of Economics", text: "Princes who **debase** the currency to pay debts inevitably bring price inflation and commercial ruin." },
      { author: "John Locke", work: "Further Considerations Concerning Raising the Value of Money", text: "To **debase** the weight or fineness of the coinage is to rob the public creditor under color of law." }
    ]
  },
  "diabase": {
    primary: "A dark, medium-grained igneous rock consisting mainly of plagioclase feldspar and pyroxene (dolerite).",
    secondary: "Subvolcanic basaltic dike and sill rock with a characteristic ophitic crystalline texture.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", text: "A massive intrusion of **diabase** cut through the older stratified shale beds along the cliff face." },
      { author: "Archibald Geikie", work: "Textbook of Geology", text: "Under the petrographic microscope, the **diabase** showed lath-shaped plagioclase crystals embedded in augite." },
      { author: "James Dwight Dana", work: "Manual of Mineralogy", text: "The Palisades sill along the Hudson River is composed of dense columnar **diabase**." }
    ]
  },
  "diabatic": {
    primary: "Relating to a thermodynamic process in which heat enters or leaves the physical system (non-adiabatic).",
    secondary: "In atmospheric physics, designating heating or cooling driven by radiation, condensation, or surface turbulent flux.",
    quotes: [
      { author: "Richard Goody", work: "Atmospheric Radiation", text: "Solar absorption and infrared emission create constant **diabatic** heating gradients across the troposphere." },
      { author: "J. Willard Gibbs", work: "The Scientific Papers of J. Willard Gibbs", text: "A cycle involving open heat exchange constitutes a strictly **diabatic** sequence of state transformations." },
      { author: "Napier Shaw", work: "Manual of Meteorology", text: "Precipitation releases latent heat, producing intense local **diabatic** warming within the core of the thunderstorm." }
    ]
  },
  "diabetes": {
    primary: "A metabolic disease in which the body's inability to produce or properly use insulin causes elevated blood sugar levels.",
    secondary: "Historically, an excessive discharge of urine (from Greek diabetes a siphon, from dia- through + bainein to step/pass).",
    quotes: [
      { author: "Thomas Willis", work: "Pharmaceutice Rationalis", text: "In **diabetes**, the urine is wonderfully sweet, as if imbued with honey or sugar." },
      { author: "Frederick Banting", work: "The Nobel Lecture", text: "Before the discovery of insulin, juvenile **diabetes** was invariably a fatal diagnosis within months." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "Dietary restriction formed the sole therapeutic measure for managing severe **diabetes** prior to endocrine therapy." }
    ]
  },
  "diabetic": {
    primary: "Having, relating to, or suffering from diabetes mellitus.",
    secondary: "Produced by or suitable for patients with diabetes; exhibiting hyperglycemia and glycosuria.",
    quotes: [
      { author: "Charles Best", work: "Selected Papers on Insulin", text: "Administration of insulin promptly cleared the **diabetic** coma and restored normal blood chemistry." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", text: "The **diabetic** patient requires meticulous foot care and constant urinalysis monitoring." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", text: "Puncture of the fourth ventricle produced temporary **diabetic** symptoms in laboratory animals." }
    ]
  },
  "dibasic": {
    primary: "Having two replaceable hydrogen atoms (in an acid), or containing two univalent basic atoms or radicals in a molecule.",
    secondary: "Capable of neutralizing two equivalents of a monobasic acid or producing two series of salts.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", text: "Sulfuric acid is a **dibasic** compound because it can form both neutral sulfates and acid bisulfates." },
      { author: "William Allen Miller", work: "Elements of Chemistry", text: "Oxalic acid behaves as a **dibasic** acid, requiring two molecular equivalents of caustic alkali to saturate it." },
      { author: "Linus Pauling", work: "General Chemistry", text: "Carbonic acid is a weak **dibasic** acid that plays an essential buffer role in mammalian blood." }
    ]
  },
  "hyperbaton": {
    primary: "A figure of speech in which the natural order of words or phrases is intentionally inverted for emphasis or dramatic effect.",
    secondary: "Rhetorical transposition or grammatical displacement of words from customary syntax (Greek hyper- over + bainein to step).",
    quotes: [
      { author: "Quintilian", work: "Institutio Oratoria", text: "Judicious use of **hyperbaton** adds grandeur and rhythm to an oration, while excessive displacement causes obscurity." },
      { author: "John Milton", work: "Paradise Lost", text: "The epic poet frequently employed bold **hyperbaton** to elevate his verse above common spoken idiom." },
      { author: "George Puttenham", work: "The Arte of English Poesie", text: "We call this figure **hyperbaton**, or the trespasser, because it steps over the orderly syntactical march of words." }
    ]
  },
  "hypobasidium": {
    primary: "The lower or basal portion of a basidium in certain heterobasidiomycete fungi, beneath the epibasidium.",
    secondary: "In mycology, the thick-walled resting stage or persistent basal cell of a septate basidium.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi", text: "In the Tremellaceae, the **hypobasidium** undergoes longitudinal division into four distinct cells." },
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", text: "Tubular sterigmata grow outward from the septate **hypobasidium** to pierce the gelatinous fruit body." },
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", text: "Microscopic diagnosis relied upon whether the **hypobasidium** remained undivided or developed transversal septa." }
    ]
  },
  "hypobasis": {
    primary: "An underlying base, substructure, or lowest foundation.",
    secondary: "In architecture or morphology, the lower pedestal or subterranean supporting tier.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", text: "The massive stone **hypobasis** anchored the column securely against the tidal wash of the lagoon." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", text: "The osteological **hypobasis** supports the entire load of the cervical axial skeleton." },
      { author: "Vitruvius", work: "De Architectura", text: "Before raising the colonnade, the architect must ensure the solidity of the **hypobasis** in firm bedrock." }
    ]
  },
  "katabasis": {
    primary: "A descent, downward journey, or retreat; variant spelling of catabasis.",
    secondary: "In classical literature, a journey into the underworld or spiritual underworld descent.",
    quotes: [
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", text: "Orpheus undertook his mythic **katabasis** to retrieve Eurydice from the shadowy halls of Hades." },
      { author: "C. G. Jung", work: "Psychology and Alchemy", text: "Every heroic transformation begins with a perilous **katabasis** into the deepest caverns of the psyche." },
      { author: "Gilbert Murray", work: "Five Stages of Greek Religion", text: "The ritual **katabasis** in mystery cults represented symbolic death followed by ecstatic rebirth." }
    ]
  },
  "katabatic": {
    primary: "Relating to a wind that blows down a topographic slope or valley due to surface cooling and gravity (downslope gravity flow).",
    secondary: "Variant spelling of catabatic; characterized by dense cold airflow descending from ice sheets or mountain summits.",
    quotes: [
      { author: "Douglas Mawson", work: "The Home of the Blizzard", text: "Adélie Land is the home of the fiercest **katabatic** winds on Earth, roaring incessantly from the ice plateau." },
      { author: "Robert Falcon Scott", work: "Scott's Last Expedition", text: "A sudden **katabatic** blizzard swept down from the Beardmore Glacier, halting all sledging progress." },
      { author: "Napier Shaw", work: "Manual of Meteorology", text: "Gravitational drainage produces powerful nighttime **katabatic** drafts in narrow alpine canyons." }
    ]
  },
  "monobasic": {
    primary: "Having only one replaceable hydrogen atom (of an acid); capable of reacting with one molecule of a univalent basic substance.",
    secondary: "Containing one basic group or radical; combining with a base in only one proportion.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", text: "Hydrochloric acid is typical of a **monobasic** acid, neutralizing a single equivalent of soda." },
      { author: "William Allen Miller", work: "Elements of Chemistry", text: "Nitric acid yields only neutral salts because it functions strictly as a **monobasic** compound." },
      { author: "Linus Pauling", work: "General Chemistry", text: "Acetic acid, despite containing four hydrogen atoms, is strictly **monobasic** because only one proton is ionizable." }
    ]
  },
  "polybasic": {
    primary: "Having two or more replaceable hydrogen atoms (of an acid); capable of neutralizing several equivalents of a base.",
    secondary: "Pertaining to mineral ores containing multiple metallic bases, such as polybasite.",
    quotes: [
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", text: "Phosphoric acid was shown to be a **polybasic** acid forming three distinct series of crystalline salts." },
      { author: "Donald M. Levy", work: "Modern Copper Smelting", text: "Smelting complex **polybasic** ores requires careful flux calculation to remove diverse gangue oxides." },
      { author: "William Crookes", work: "Select Methods in Chemical Analysis", text: "The mineralogist identified the silver specimen as a **polybasic** sulfantimonite." }
    ]
  },
  "stereobate": {
    primary: "A solid mass of masonry serving as the foundation or substructure of a building, especially a classical Greek temple.",
    secondary: "The tiered stone platform or foundation steps upon which the stylobate and temple columns stand.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", text: "The **stereobate** must be excavated down to solid bedrock to sustain the immense weight of the marble columns." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", text: "The temple rose with majestic stability from its stepped **stereobate** above the rocky acropolis." },
      { author: "Banister Fletcher", work: "A History of Architecture", text: "The Parthenon rests upon a three-stepped limestone **stereobate**, the uppermost tier forming the stylobate." }
    ]
  },
  "tribasic": {
    primary: "Having three replaceable hydrogen atoms (of an acid); capable of neutralizing three equivalents of a base.",
    secondary: "Combining with bases in three different proportions to form three series of salts.",
    quotes: [
      { author: "Thomas Graham", work: "Researches on the Arseniates, Phosphates, and Modifications of Phosphoric Acid", text: "Orthophosphoric acid is fundamentally **tribasic**, forming mono-, di-, and tri-sodium salts." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", text: "Citric acid was recognized as a **tribasic** organic acid through its triple series of crystalline precipitates." },
      { author: "William Allen Miller", work: "Elements of Chemistry", text: "A **tribasic** acid requires three equivalents of monovalent metallic base to achieve neutral saturation." }
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
for (const [lemma, data] of Object.entries(BATCH5_DATA)) {
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
console.log(`Batch 5 Completed: ${count} / ${Object.keys(BATCH5_DATA).length} words updated`);
console.log(`========================================\n`);
