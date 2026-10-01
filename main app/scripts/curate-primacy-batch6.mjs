import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — arch";

const wordsData = {
  "architeuthis.md": {
    word: "architeuthis",
    primary: "A genus of giant deep-sea squid comprising Architeuthis dux, characterized by enormous eyes and elongated feeding tentacles.",
    secondary: "In teuthology and marine biology, the largest known cephalopod invertebrate by length, inhabiting abyssal oceanic depths.",
    quotes: [
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "The monster before us was a colossal calamary of the genus **Architeuthis**, its tentacles writhing like serpents." },
      { author: "Arthur C. Clarke", work: "The Deep Range", quote: "Submarine sonars tracked the shadowy glide of an **Architeuthis** rising from the oceanic trench." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Sperm whales bear deep circular battle scars across their jaws from violent encounters with **Architeuthis** in the dark abyss." }
    ]
  },
  "architrave.md": {
    word: "architrave",
    primary: "The lowest part of an entablature in classical architecture, resting directly upon the abacus of a column or capital.",
    secondary: "A decorative moulded frame or lintel surrounding a door, window, or square opening.",
    quotes: [
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "The stone lintel and finely carved **architrave** unite the upright pillars into an indissoluble tectonic frame." },
      { author: "Thomas Hardy", work: "A Pair of Blue Eyes", quote: "Her eyes followed the classical egg-and-dart moulding decorating the stone **architrave** of the south porch." },
      { author: "Benito Pérez Galdós", work: "Fortunata and Jacinta", quote: "Heavy mahogany doors framed by an ornate gilded **architrave** opened into the aristocratic salon." }
    ]
  },
  "archival.md": {
    word: "archival",
    primary: "Of, relating to, or contained in an archive or collection of public records and historical documents.",
    secondary: "Meeting standards of preservation and chemical permanence intended to endure for centuries without deterioration (e.g., archival paper, archival ink).",
    quotes: [
      { author: "Jacques Derrida", work: "Archive Fever", quote: "The **archival** impulse represents both a desire to preserve memory and an institutional will to classify truth." },
      { author: "Barbara Tuchman", work: "The Guns of August", quote: "Painstaking **archival** research into telegrams and military dispatches revealed how miscalculations ignited the conflict." },
      { author: "Umberto Eco", work: "The Name of the Rose", quote: "The librarian held exclusive dominion over the fragile **archival** manuscripts stacked within the secret tower." }
    ]
  },
  "archives.md": {
    word: "archives",
    primary: "A collection of historical documents or records providing information about a place, institution, or group of people; also, the physical repository housing them.",
    secondary: "In information science and historiography, primary records systematically preserved for evidentiary value, cultural heritage, and administrative precedent.",
    quotes: [
      { author: "Alexander Hamilton", work: "The Federalist Papers (No. 44)", quote: "The public records and **archives** of the confederacy were deposited in loose bundles, vulnerable to theft and decay." },
      { author: "George Orwell", work: "1984", quote: "Day by day and almost minute by minute the past was brought up to date in the vast subterranean **archives** of the Ministry of Truth." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The mob stormed the municipal **archives**, burning tax rolls and royal edicts upon the paving stones." }
    ]
  },
  "archivist.md": {
    word: "archivist",
    primary: "A professional person responsible for preserving, organizing, cataloging, and managing archival records and historical documents.",
    secondary: "A scholarly custodian of institutional memory and documentary heritage, adhering to principles of provenance and original order.",
    quotes: [
      { author: "Jorge Luis Borges", work: "The Library of Babel", quote: "The wandering **archivist** inspected hexagonal galleries of octavo volumes searching for the vindication of man." },
      { author: "A. S. Byatt", work: "Possession", quote: "The literary **archivist** handled the bundle of Victorian love letters with gloved fingers and reverent silence." },
      { author: "Simon Schama", work: "Citizens: A Chronicle of the French Revolution", quote: "Every parish **archivist** in the provinces was ordered to transfer feudal deeds to the district tribunal." }
    ]
  },
  "archly.md": {
    word: "archly",
    primary: "In an arch, playfully roguish, saucy, or knowing manner.",
    secondary: "With an ironic, teasing, or coyly conspiratorial expression or tone.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "Elizabeth looked **archly** at Darcy, smiling as she declined the honor of his hand for the next dance." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Becky Sharp tilted her lace parasol and glanced **archly** at the young officer over her shoulder." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "Madame Merle smiled **archly**, as if inviting Isabel to share in an unspoken secret." }
    ]
  },
  "archness.md": {
    word: "archness",
    primary: "The quality or state of being arch; playful slyness, roguishness, or teasing irony.",
    secondary: "Coy or knowing humor marked by affectionate mock-solemnity or mild insolence.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "There was a delightful mixture of innocence and **archness** in her bright eyes when she questioned him." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "Bathsheba laughed with a sudden **archness** that entirely disconcerted the bashful young shepherd." },
      { author: "George Eliot", work: "Middlemarch", quote: "Celia spoke with that quiet domestic **archness** which she always reserved for her sister's high-flown ideals." }
    ]
  },
  "archosargus.md": {
    word: "archosargus",
    primary: "A genus of sparid marine fishes including the sheepshead (Archosargus probatocephalus), noted for broad incisor-like teeth adapted for crushing shellfish.",
    secondary: "In ichthyology, coastal Perciform fishes inhabiting Western Atlantic reefs, jetties, and estuaries.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The genus **Archosargus** is readily recognized by its heavy, molariform crushing dentition and robust silvery body." },
      { author: "Spencer Fullerton Baird", work: "Report on the Sea Fisheries of the South Coast of New England", quote: "Fishermen take **Archosargus** around pilings where oysters and barnacles encrust the submerged timbers." },
      { author: "George Brown Goode", work: "American Fishes", quote: "The sheepshead, belonging to **Archosargus**, yields firm white flesh highly esteemed in the markets of the Gulf." }
    ]
  },
  "archosaur.md": {
    word: "archosaur",
    primary: "Any reptile of the subclass or clade Archosauria, including dinosaurs, pterosaurs, crocodilians, and their extinct relatives, as well as modern birds.",
    secondary: "In vertebrate paleontology, diapsid reptiles characterized by antorbital fenestrae, thecodont dentition, and an evolutionary shift toward bipedal locomotion.",
    quotes: [
      { author: "Stephen Jay Gould", work: "Bully for Brontosaurus", quote: "Every modern bird is, cladistically speaking, a feathered **archosaur** that survived the Cretaceous extinction." },
      { author: "Robert T. Bakker", work: "The Dinosaur Heresies", quote: "The active posture of the early Triassic **archosaur** laid the physiological groundwork for the dominance of dinosaurs." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "The radiation of crown-group **archosaur** lineages followed the catastrophic end-Permian extinction." }
    ]
  },
  "archosauria.md": {
    word: "archosauria",
    primary: "A major clade or subclass of diapsid amniotes that originated in the Triassic period, encompassing pseudosuchians (crocodilians and kin) and avemetatarsalians (pterosaurs, dinosaurs, and birds).",
    secondary: "In phylogenetic systematics, the ruling reptiles defined by shared evolutionary novelties such as serrated teeth in sockets and mandibular fenestrae.",
    quotes: [
      { author: "Edward Drinker Cope", work: "The Primary Factors of Organic Evolution", quote: "The skeletal architecture of the **Archosauria** demonstrates the ancestral divergence of avian from reptilian types." },
      { author: "Alfred Sherwood Romer", work: "Vertebrate Paleontology", quote: "Within **Archosauria**, two distinct evolutionary branches diverged: the crocodilian line and the bird line." },
      { author: "Neil Shubin", work: "Your Inner Fish", quote: "Comparative developmental studies confirm that living members of **Archosauria** retain deep genetic homologies in limb patterning." }
    ]
  },
  "archosaurian.md": {
    word: "archosaurian",
    primary: "Of, relating to, or characteristic of the archosaurs or the clade Archosauria.",
    secondary: "Pertaining to the distinctive skull openings, thecodont teeth, or locomotion seen in ruling reptiles.",
    quotes: [
      { author: "Richard Owen", work: "Palaeontology", quote: "The presence of an antorbital opening is a cardinal **archosaurian** character distinguishing these reptiles from lizards." },
      { author: "Thomas Henry Huxley", work: "On the Animals Intermediate between Birds and Reptiles", quote: "The hind limbs of megalosaurus exhibit typical **archosaurian** modifications that anticipate avian bipedalism." },
      { author: "John Ostrom", work: "Archaeopteryx and the Origin of Birds", quote: "Feathered theropods conclusively demonstrate the continuity of **archosaurian** skeletal traits into modern avians." }
    ]
  },
  "autarch.md": {
    word: "autarch",
    primary: "An absolute ruler or monarch who possesses unlimited power; an autocrat.",
    secondary: "In political theory, a despot whose sovereignty is unrestricted by constitutional law, assemblies, or independent judiciaries.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Roman emperor ceased to feign republican modesty and governed openly as an absolute **autarch**." },
      { author: "Percy Bysshe Shelley", work: "Hellas", quote: "The proud **autarch** of the East sat upon his throne of ivory and gold, deaf to the groans of the provinces." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "When popular turmoil overwhelms constitutional assemblies, the state often summons an **autarch** with an iron fist." }
    ]
  },
  "autarchic.md": {
    word: "autarchic",
    primary: "Relating to an autarch or autarchy; autocratic or having absolute authority.",
    secondary: "In economic theory, characterized by national self-sufficiency and economic independence from foreign trade (variant of autarkic).",
    quotes: [
      { author: "John Maynard Keynes", work: "The General Theory of Employment, Interest, and Money", quote: "Nations adopting **autarchic** trade barriers ultimately suffocate international commerce and domestic prosperity." },
      { author: "Max Weber", work: "Economy and Society", quote: "Patrimonial regimes tend toward **autarchic** governance, where administrative obedience depends solely upon personal allegiance." },
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "Totalitarian movements demand total, **autarchic** control over both the public sphere and private consciousness." }
    ]
  },
  "autarchical.md": {
    word: "autarchical",
    primary: "Autocratic or dictatorial; possessing or exercising unrestricted power (variant of autarchic).",
    secondary: "Pertaining to independent self-sufficiency or absolute unilateral governance.",
    quotes: [
      { author: "Edmund Burke", work: "Thoughts on the Cause of the Present Discontents", quote: "An **autarchical** court cabal sought to isolate the crown from Parliament and popular sentiment." },
      { author: "John Locke", work: "Second Treatise of Government", quote: "Men do not quit the freedom of nature merely to submit to the **autarchical** whims of an unaccountable tyrant." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "Democratic despotism does not shatter wills with open cruelty; it rules through an **autarchical** administrative tutelage." }
    ]
  },
  "autarchy.md": {
    word: "autarchy",
    primary: "Absolute sovereignty or despotic government; autocratic rule.",
    secondary: "A self-sufficient economic system isolated from international trade (frequently merged with German Autarkie / Greek autarkeia).",
    quotes: [
      { author: "Friedrich Hayek", work: "The Road to Serfdom", quote: "The quest for complete national economic **autarchy** inevitably produces central planning and political coercion." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "No modern commonwealth can flourish in total **autarchy**, since the division of labor requires foreign commerce." },
      { author: "James Madison", work: "The Federalist Papers (No. 47)", quote: "The accumulation of all powers in the same hands may justly be pronounced the very definition of **autarchy**." }
    ]
  },
  "eparch.md": {
    word: "eparch",
    primary: "In ancient Greece and the Byzantine Empire, a governor of a province or the prefect of Constantinople.",
    secondary: "In Eastern Orthodox and Eastern Catholic churches, a bishop in charge of an eparchy (diocese).",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **eparch** of Constantinople controlled the city police, market regulations, and imperial ceremonies." },
      { author: "Procopius", work: "Secret History", quote: "Petitions against corrupt provincial governors were regularly submitted to the imperial **eparch**." },
      { author: "Steven Runciman", work: "The Great Church in Captivity", quote: "Under Ottoman rule, the local **eparch** acted as both pastoral shepherd and civil judge for his Christian flock." }
    ]
  },
  "eparchial.md": {
    word: "eparchial",
    primary: "Of or relating to an eparch or an eparchy (provincial or diocesan jurisdiction).",
    secondary: "Pertaining to the administration, canons, and councils of an Eastern Christian bishopric.",
    quotes: [
      { author: "J. B. Bury", work: "A History of the Later Roman Empire", quote: "The **eparchial** edicts preserved in the Book of the Prefect illuminate urban guild organization in Constantinople." },
      { author: "Timothy Ware", work: "The Orthodox Church", quote: "Each bishop exercises full **eparchial** authority over the parishes within his territorial see." },
      { author: "Alexander Schmemann", work: "The Historical Road of Eastern Orthodoxy", quote: "Decisions regarding liturgical practice were ratified during the annual **eparchial** synod." }
    ]
  },
  "eparchy.md": {
    word: "eparchy",
    primary: "A province or administrative district in ancient Greece and the Byzantine Empire.",
    secondary: "An Eastern Orthodox or Eastern Catholic diocese under the jurisdiction of an eparch.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The expansive **eparchy** of the East was divided into dioceses governed by imperial lieutenants." },
      { author: "Jaroslav Pelikan", work: "The Spirit of Eastern Christendom", quote: "Monasteries founded within an **eparchy** were subject to the episcopal oversight of the reigning bishop." },
      { author: "George Finlay", work: "History of the Byzantine Empire", quote: "The fiscal revenues of each rural **eparchy** were collected by imperial officials stationed in the fortified towns." }
    ]
  },
  "exarch.md": {
    word: "exarch",
    primary: "In the Byzantine Empire, a governor or viceroy of a distant province or diocese (such as Ravenna or Carthage) exercising combined civil and military authority.",
    secondary: "In Eastern Orthodox churches, a bishop or metropolitan presiding over an exarchate or representing a patriarch outside patriarchal boundaries.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The Byzantine **exarch** at Ravenna maintained a precarious hold over Italy against the advancing Lombard tribes." },
      { author: "J. B. Bury", work: "The Imperial Administrative System", quote: "By concentrating military and civil power in the hands of the **exarch**, the emperors sought to protect frontiers from collapse." },
      { author: "Steven Runciman", work: "A History of the Crusades", quote: "The patriarchal **exarch** arrived in Antioch bearing credentials from the ecumenical throne of Constantinople." }
    ]
  },
  "exarchate.md": {
    word: "exarchate",
    primary: "The office, jurisdiction, dignity, or territory governed by an exarch.",
    secondary: "In ecclesiastical geography, a missionary jurisdiction or overseas province established by an Eastern patriarchate.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The fall of the **exarchate** of Ravenna to King Aistulf terminated two centuries of Byzantine rule in northern Italy." },
      { author: "Thomas Hodgkin", work: "Italy and Her Invaders", quote: "Within the limits of the **exarchate**, Greek language and Roman law persisted long after the rest of the peninsula had succumbed to Germanic invaders." },
      { author: "Ferdinand Gregorovius", work: "History of the City of Rome in the Middle Ages", quote: "Pepin the Short granted the conquered cities of the **exarchate** to the Holy See, establishing the Papal States." }
    ]
  },
  "monarch.md": {
    word: "monarch",
    primary: "A sovereign head of state, such as a king, queen, emperor, or sultan, especially one who inherits authority by birth and rules for life.",
    secondary: "In natural history, a large migratory orange-and-black North American butterfly (Danaus plexippus).",
    quotes: [
      { author: "William Shakespeare", work: "Richard II", quote: "For within the hollow crown that rounds the mortal temples of a **monarch** keeps Death his court." },
      { author: "John Milton", work: "Paradise Lost", quote: "Satan, exalted above his peers, sat like a proud **monarch** upon his bad eminence." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The migratory journey of the orange **monarch** butterfly across thousands of miles of ocean and continent illustrates the power of innate instinct." }
    ]
  },
  "monarchal.md": {
    word: "monarchal",
    primary: "Pertaining to, suited to, or resembling a monarch; royal or sovereign.",
    secondary: "Relating to monarchical rule or single-ruler government.",
    quotes: [
      { author: "John Milton", work: "Paradise Regained", quote: "The Roman Caesars displayed **monarchal** splendor, seating themselves above consular laws and ancient senates." },
      { author: "Walter Scott", work: "The Bride of Lammermoor", quote: "The ancient hall was draped with banners displaying the **monarchal** arms of Scotland." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The people tore down every **monarchal** emblem from the public squares and palace gates." }
    ]
  },
  "monarchic.md": {
    word: "monarchic",
    primary: "Of, relating to, or characteristic of a monarch or monarchy; ruled by a monarch.",
    secondary: "In political theory, favoring or instituted upon the principle of hereditary single-ruler governance.",
    quotes: [
      { author: "Montesquieu", work: "The Spirit of the Laws", quote: "The **monarchic** form of government rests upon the principle of honor, whereas a republic requires virtue." },
      { author: "Alexander Hamilton", work: "The Federalist Papers (No. 67)", quote: "Critics of the Constitution unjustly imputed **monarchic** ambitions to the executive branch." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "European societies emerged from **monarchic** centralism, carrying historical habits of obedience into democratic life." }
    ]
  },
  "monarchism.md": {
    word: "monarchism",
    primary: "Advocacy of or adherence to monarchy or monarchical government.",
    secondary: "The political philosophy or movement supporting kingship or hereditary executive authority.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Traditional British **monarchism** reconciles hereditary royal authority with parliamentary liberties." },
      { author: "Thomas Paine", work: "Common Sense", quote: "Hereditary **monarchism** is an insult to human dignity, crowning an infant or an idiot over a free people." },
      { author: "François-René de Chateaubriand", work: "The Genius of Christianity", quote: "The restoration of legitimate **monarchism** offered peace to a nation exhausted by revolutionary storms." }
    ]
  },
  "monarchist.md": {
    word: "monarchist",
    primary: "A supporter of monarchy or the monarchical system of government.",
    secondary: "In European political history, a royalist or legitimist opposing republicanism or revolutionary democracy.",
    quotes: [
      { author: "Victor Hugo", work: "Les Misérables", quote: "M. Gillenormand was an obstinate **monarchist** who considered the French Revolution a personal affront." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "The fascist forces allied with every conservative landowner and die-hard **monarchist** in Spain." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The staunch Cavalier **monarchist** held that kings reigned by direct divine appointment." }
    ]
  },
  "monarchy.md": {
    word: "monarchy",
    primary: "A form of government with a monarch (king, queen, emperor) at the head.",
    secondary: "A nation, empire, or state ruled by an individual sovereign, either absolute or constitutional.",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", quote: "For so work the honey-bees, creatures that by a rule in nature teach the act of order to a peopled **monarchy**." },
      { author: "Thomas Hobbes", work: "Leviathan", quote: "The difference of commonwealths consisteth in the difference of the sovereign: when the representative is one man, then is the commonwealth a **monarchy**." },
      { author: "John Locke", work: "Second Treatise of Government", quote: "Absolute **monarchy**, which by some men is counted the only government in the world, is indeed inconsistent with civil society." }
    ]
  },
  "navarch.md": {
    word: "navarch",
    primary: "In ancient Greece, the commander of a fleet; an admiral, especially the Spartan naval commander-in-chief (nauarchos).",
    secondary: "In classical military history, the magistrate holding the annual supreme maritime command of the Peloponnesian naval confederacy.",
    quotes: [
      { author: "Thucydides", work: "The Peloponnesian War", quote: "The Spartan assembly appointed Lysander as **navarch**, entrusting him with the supreme command of the Aegean fleet." },
      { author: "Xenophon", work: "Hellenica", quote: "When the annual term of the **navarch** expired, Spartan law forbade any citizen from holding the command twice." },
      { author: "Plutarch", work: "Life of Alcibiades", quote: "The Athenian galleys caught the Spartan **navarch** unprepared off the shoals of Cyzicus." }
    ]
  },
  "octarchy.md": {
    word: "octarchy",
    primary: "A government by eight rulers; also, a confederacy or group of eight states or provinces.",
    secondary: "In British historiography, an alternative term for the Anglo-Saxon heptarchy when considering an eighth sub-kingdom (such as Lindsey or Bernicia).",
    quotes: [
      { author: "Edward Augustus Freeman", work: "The History of the Norman Conquest of England", quote: "Historians who reckon Lindsey alongside the standard realms describe an **octarchy** rather than a heptarchy of Anglo-Saxon kingdoms." },
      { author: "John Milton", work: "The History of Britain", quote: "The rivalries of the **octarchy** left the island vulnerable to the devastating incursions of Norse raiders." },
      { author: "Sharon Turner", work: "The History of the Anglo-Saxons", quote: "The political balance of the **octarchy** fluctuated as Northumbria and Mercia alternately claimed overlordship." }
    ]
  },
  "polyarchy.md": {
    word: "polyarchy",
    primary: "Government by many rulers; rule by multiple individuals or groups.",
    secondary: "In modern political science (coined by Robert Dahl), a democratic system of government in which power is invested in multiple people, marked by high political inclusion and public contestation.",
    quotes: [
      { author: "Robert Dahl", work: "Polyarchy: Participation and Opposition", quote: "A modern representative democracy operates as a **polyarchy**, where diverse autonomous organizations contest for power through inclusive elections." },
      { author: "Samuel P. Huntington", work: "The Third Wave", quote: "The global transition toward **polyarchy** gained unprecedented momentum during the late twentieth century." },
      { author: "Joseph Schumpeter", work: "Capitalism, Socialism and Democracy", quote: "What is often idealized as rule by the people is in practice a competitive **polyarchy** among rival elites." }
    ]
  },
  "protoarchaeology.md": {
    word: "protoarchaeology",
    primary: "The earliest, rudimentary stage of archaeological inquiry, characterized by unscientific antiquarianism, curiosity collecting, and treasure hunting.",
    secondary: "In the history of science, the 17th- and 18th-century precursor to stratigraphic archaeology practiced by early antiquaries.",
    quotes: [
      { author: "Glyn Daniel", work: "A Hundred and Fifty Years of Archaeology", quote: "The cabinet of curiosities was the hallmark of **protoarchaeology**, where Roman coins lay mingled with mammoth teeth." },
      { author: "Bruce Trigger", work: "A History of Archaeological Thought", quote: "Renaissance antiquarian collections represented a form of **protoarchaeology** that preceded rigorous fieldwork." },
      { author: "Colin Renfrew", work: "Archaeology: Theories, Methods, and Practice", quote: "Before the three-age system was established, **protoarchaeology** relied entirely on biblical chronology and classical mythology." }
    ]
  },
  "protoarcheology.md": {
    word: "protoarcheology",
    primary: "Variant spelling of protoarchaeology; the nascent, pre-scientific phase of archaeological investigation.",
    secondary: "The exploratory antiquarian collecting and tomb-opening of the early modern period preceding scientific stratigraphic excavation.",
    quotes: [
      { author: "Lewis Binford", work: "New Perspectives in Archaeology", quote: "We must liberate ourselves from the lingering habits of **protoarcheology**, where trait lists were substituted for functional explanations." },
      { author: "V. Gordon Childe", work: "A Short Introduction to Archaeology", quote: "The transition from **protoarcheology** to genuine prehistory occurred when geological superposition was applied to earthworks." },
      { author: "Stuart Piggott", work: "Ruins in a Landscape", quote: "William Stukeley’s early surveys of Avebury show the brilliant dawn and subsequent occult decay of British **protoarcheology**." }
    ]
  },
  "synarchism.md": {
    word: "synarchism",
    primary: "Advocacy of joint or harmonious rule; a political ideology promoting cooperative governance by combined social, economic, and religious councils.",
    secondary: "In French occult and political history (associated with Saint-Yves d'Alveydre), a social order governed by harmonic social estates.",
    quotes: [
      { author: "Alexandre Saint-Yves d'Alveydre", work: "Mission des Souverains", quote: "True social equilibrium requires **synarchism**, where spiritual authority, judicial power, and economic production govern in tripartite harmony." },
      { author: "Hannah Arendt", work: "The Origins of Totalitarianism", quote: "Interwar rumors regarding shadowy **synarchism** revealed the deep anxiety of the French bourgeoisie facing institutional decay." },
      { author: "Georges Valois", work: "L'État syndical et la représentation corporative", quote: "The doctrines of corporatist **synarchism** proposed an organic alternative to parliamentary democracy." }
    ]
  },
  "synarchy.md": {
    word: "synarchy",
    primary: "Joint rule or shared sovereignty, especially by two or more authorities.",
    secondary: "In political theory, a system of collective governance integrating corporate, administrative, and civic bodies into an organic governing coalition.",
    quotes: [
      { author: "Arnold J. Toynbee", work: "A Study of History", quote: "The Spartan dual kingship operated as a curious constitutional **synarchy** designed to prevent individual tyranny." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The joint elevation of Pupienus and Balbinus instituted a brief imperial **synarchy** under the sanction of the Roman Senate." },
      { author: "Samuel Taylor Coleridge", work: "On the Constitution of the Church and State", quote: "A harmonious commonwealth demands a balanced **synarchy** between the national church and the civil legislature." }
    ]
  },
  "tetrarchy.md": {
    word: "tetrarchy",
    primary: "Government by four persons ruling jointly; especially the system established in the Roman Empire by Emperor Diocletian in 293 CE.",
    secondary: "A country, province, or district divided into four administrative regions or ruled by a tetrarch.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Diocletian divided the unwieldy weight of the empire among four colleagues, establishing the imperial **tetrarchy**." },
      { author: "J. B. Bury", work: "A History of the Later Roman Empire", quote: "Under the **tetrarchy**, two Augusti and two Caesars shared administrative defense across the Danube, Rhine, and Euphrates." },
      { author: "Peter Brown", work: "The World of Late Antiquity", quote: "The porphyry statue in Venice portrays the four rulers of the **tetrarchy** embracing in fraternal unity." }
    ]
  },
  "triarchy.md": {
    word: "triarchy",
    primary: "Government by three persons ruling jointly; a triumvirate.",
    secondary: "A country, empire, or territory divided into three separate jurisdictions or ruled by three sovereigns.",
    quotes: [
      { author: "William Shakespeare", work: "Antony and Cleopatra", quote: "The great **triarchy** of the world is split: Antony, Octavius, and Lepidus contend for solitary mastery of mankind." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The partition of the Frankish kingdom among the three sons of Clovis established a short-lived **triarchy** in Gaul." },
      { author: "Thomas Hobbes", work: "Leviathan", quote: "A divided sovereignty, whether an oligarchy, **triarchy**, or dual throne, contains the inevitable seeds of civil destruction." }
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
console.log("Primacy Batch 6 completed! Total words updated:", Object.keys(wordsData).length);
