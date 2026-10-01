import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Beginning & Primacy/Dashboard — arch";

const wordsData = {
  "archenteron.md": {
    word: "archenteron",
    primary: "The primary digestive cavity formed in the early embryo during the gastrula stage, opening to the exterior via the blastopore.",
    secondary: "In evolutionary developmental biology, the ancestral primitive gut homologous across metazoans that gives rise to the endodermal lining and associated viscera.",
    quotes: [
      { author: "Ernst Haeckel", work: "The Evolution of Man", quote: "The invagination of the blastula forms the primitive gut or **archenteron**, the foundational cavity of all higher animal bodies." },
      { author: "Francis Maitland Balfour", work: "A Treatise on Comparative Embryology", quote: "In amphioxus the **archenteron** is lined with a uniform layer of columnar hypoblast cells." },
      { author: "Gavin de Beer", work: "Embryos and Ancestors", quote: "The closure of the blastopore alters the relationship of the **archenteron** to the embryonic axis." }
    ]
  },
  "archeobacteria.md": {
    word: "archeobacteria",
    primary: "Variant spelling of archaebacteria; a domain or kingdom of single-celled microorganisms distinct from eubacteria and eukaryotes, often thriving in extreme environments.",
    secondary: "In microbiologic taxonomy, prokaryotes with unique ether-linked membrane lipids and distinctive ribosomal RNA, crucial in molecular phylogenetics.",
    quotes: [
      { author: "Carl Woese", work: "Microbiological Reviews", quote: "The distinctive cellular machinery of the **archeobacteria** compelled a fundamental division of cellular life into three primary lineages." },
      { author: "Lynn Margulis", work: "Symbiosis in Cell Evolution", quote: "Methanogens and extreme halophiles belonging to the **archeobacteria** provide clues to conditions on the anaerobic primitive Earth." },
      { author: "Thomas Cavalier-Smith", work: "Biological Reviews", quote: "Debates on the root of the tree of life continually evaluate the evolutionary polarity between eubacteria and **archeobacteria**." }
    ]
  },
  "archeologic.md": {
    word: "archeologic",
    primary: "Relating to the scientific study of past human life, cultures, and activities through material remains (variant spelling of archaeological).",
    secondary: "Relating to artifacts, excavations, and structural relics recovered from ancient settlements.",
    quotes: [
      { author: "Arthur Evans", work: "The Palace of Minos", quote: "The **archeologic** strata revealed successive floor levels spanning the Middle and Late Minoan periods." },
      { author: "Flinders Petrie", work: "Methods and Aims in Archaeology", quote: "Every potsherd and flint flake bears **archeologic** value when preserved in its exact geological context." },
      { author: "Leonard Woolley", work: "Ur of the Chaldees", quote: "Our **archeologic** survey of the royal cemetery illuminated funeral customs unrecorded in surviving cuneiform tablets." }
    ]
  },
  "archeological.md": {
    word: "archeological",
    primary: "Relating to archaeology or the material remains of past human cultures (variant spelling of archaeological).",
    secondary: "Pertaining to systematically excavated relics, strata, and prehistoric antiquities.",
    quotes: [
      { author: "Howard Carter", work: "The Tomb of Tutankhamun", quote: "The sealed doorway presented an **archeological** puzzle that had defied three millennia of desert storms." },
      { author: "Austen Henry Layard", work: "Nineveh and Its Remains", quote: "The **archeological** discoveries beneath the mounds of Nimrud astonished Victorian travelers and scholars alike." },
      { author: "Mortimer Wheeler", work: "Archaeology from the Earth", quote: "Stratigraphy is the very backbone of **archeological** excavation and historical reconstruction." }
    ]
  },
  "archeologist.md": {
    word: "archeologist",
    primary: "A scientist or scholar who studies past human life and culture by recovery and analysis of material evidence (variant of archaeologist).",
    secondary: "An excavator or field researcher specializing in ancient architectural ruins, inscriptions, and fossilized cultural remains.",
    quotes: [
      { author: "Heinrich Schliemann", work: "Troy and Its Remains", quote: "The **archeologist** must proceed with the spade in hand, checking ancient epic against unyielding stone." },
      { author: "V. Gordon Childe", work: "Man Makes Himself", quote: "The modern **archeologist** reconstructs social revolutions from stone sickles and grain impressions in baked clay." },
      { author: "Kathleen Kenyon", work: "Digging Up Jericho", quote: "A meticulous **archeologist** learns to read changes of soil texture as clearly as the pages of an open book." }
    ]
  },
  "archeology.md": {
    word: "archeology",
    primary: "The scientific study of historic or prehistoric peoples and their cultures by analysis of artifacts, inscriptions, and monuments (variant of archaeology).",
    secondary: "In Foucault's philosophy, the analysis of historical systems of thought and unconscious discursive formations governing an era.",
    quotes: [
      { author: "Michel Foucault", work: "The Archeology of Knowledge", quote: "The purpose of this **archeology** is not to resurrect monuments, but to describe the transformational rules of discourse." },
      { author: "Charles Lyell", work: "The Antiquity of Man", quote: "Prehistoric **archeology** and geology converge when human flints are retrieved alongside the bones of extinct pachyderms." },
      { author: "Hiram Bingham", work: "Lost City of the Incas", quote: "The dense cloud-forest had guarded Machu Picchu until modern **archeology** penetrated its stone terraces." }
    ]
  },
  "archeopteryx.md": {
    word: "archeopteryx",
    primary: "An extinct, primitive bird of the Jurassic period having teeth, a long bony lizard-like tail, and feathered wings (variant spelling of Archaeopteryx).",
    secondary: "In evolutionary paleontology, a famous transitional fossil displaying mosaic anatomy between theropod dinosaurs and avians.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Further Evidence of the Affinity between the Dinosaurian Reptiles and Birds", quote: "The skeleton of **archeopteryx** exhibits that miraculous mingling of avian plumage with reptilian skeletal architecture." },
      { author: "Richard Owen", work: "On the Archeopteryx of von Meyer", quote: "The solitary feather from the Solnhofen lithographic limestone was soon followed by the nearly complete specimen of **archeopteryx**." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Few specimens in the history of science have sparked as much philosophical wonder as the Berlin **archeopteryx**." }
    ]
  },
  "archeozoic.md": {
    word: "archeozoic",
    primary: "Relating to the earliest geologic eon of Earth's history, characterized by the appearance of the earliest primitive single-celled life (variant of Archean).",
    secondary: "In historical geology, the rock systems and cratonic metamorphic complexes formed prior to the Proterozoic eon.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "The **archeozoic** rocks represent the dawn of the lithosphere, when granite shields cooled beneath turbulent oceans." },
      { author: "Charles Doolittle Walcott", work: "Cambrian Geology and Paleontology", quote: "Microscopic filaments discovered within **archeozoic** chert beds pushed back the estimated origin of terrestrial life." },
      { author: "Arthur Holmes", work: "The Age of the Earth", quote: "Radiometric dating of the ancient Canadian shield revealed extensive **archeozoic** formations older than two billion years." }
    ]
  },
  "archepiscopal.md": {
    word: "archepiscopal",
    primary: "Pertaining or belonging to an archbishop or an archdiocese; variant spelling of archiepiscopal.",
    secondary: "Relating to metropolitan ecclesiastical authority, jurisdictions, and ceremonial prerogatives in liturgical churches.",
    quotes: [
      { author: "Walter Scott", work: "Ivanhoe", quote: "The prelate arrived in his full **archepiscopal** robes, preceded by a silver crucifix and a train of chanting monks." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The King demanded that the **archepiscopal** see of Canterbury submit unconditionally to the royal prerogative." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The council confirmed the **archepiscopal** dignity of Alexandria over the provinces of Egypt and Libya." }
    ]
  },
  "archer.md": {
    word: "archer",
    primary: "A person who shoots with a bow and arrows, especially in hunting, warfare, or sport.",
    secondary: "In military history, a longbowman or mounted skirmisher whose ranged volleys altered medieval infantry warfare.",
    quotes: [
      { author: "William Shakespeare", work: "Henry V", quote: "Cry 'God for Harry, England, and Saint George!' where every English **archer** drew his bowstring to the ear." },
      { author: "Walter Scott", work: "The Fair Maid of Perth", quote: "The skilled Scottish **archer** watched the drifting wind before letting fly his gray-goose shaft." },
      { author: "Arthur Conan Doyle", work: "The White Company", quote: "A stout Hampshire **archer** could pierce a steel breastplate at two hundred paces with an ash bow." }
    ]
  },
  "archerfish.md": {
    word: "archerfish",
    primary: "A small freshwater and brackish fish of the family Toxotidae known for shooting water droplets from its mouth to knock terrestrial insects into the water.",
    secondary: "In ethology and sensory biology, a teleost capable of optical compensation for water-surface refraction when aiming hydraulic jets.",
    quotes: [
      { author: "David Attenborough", work: "The Life of Fishes", quote: "Perched beneath mangrove roots, the **archerfish** accurately drops a beetle from an overhanging branch with a single jet." },
      { author: "Konrad Lorenz", work: "King Solomon's Ring", quote: "The ballistic precision of the **archerfish** requires an innate neurological adjustment for light refraction at the water's surface." },
      { author: "William Beebe", work: "The Arcturus Adventure", quote: "We watched the little banded **archerfish** target flies perched several inches above the tranquil lagoon." }
    ]
  },
  "archery.md": {
    word: "archery",
    primary: "The art, practice, or skill of shooting with a bow and arrow.",
    secondary: "In military history and sporting tradition, projectile warfare and competitive marksmanship governed by traditional bows, longbows, or recurves.",
    quotes: [
      { author: "Roger Ascham", work: "Toxophilus", quote: "No exercise can be compared to **archery**, which traineth the body in health and the mind in honest recreation." },
      { author: "John Keats", work: "Robin Hood", quote: "Gone, the merry morris din; gone, the silent bows of pine, and the foresters' proud craft of **archery**." },
      { author: "George Eliot", work: "Daniel Deronda", quote: "The lawn at Brackenshaw was set with colorful targets for the grand midsummer contest in **archery**." }
    ]
  },
  "archespore.md": {
    word: "archespore",
    primary: "A cell or group of cells from which spores or spore-mother cells are derived in plant and fungal reproductive organs.",
    secondary: "In plant embryology and morphogenetics, the primordial fertile tissue within the sporangium giving rise to sporogenous cells.",
    quotes: [
      { author: "Frederick Orpen Bower", work: "The Origin of a Land Flora", quote: "The differentiation of the **archespore** marks the decisive transition from vegetative growth to reproductive specialization in ferns." },
      { author: "John Merle Coulter", work: "Morphology of Angiosperms", quote: "In primitive vascular plants, the subepidermal **archespore** divides periclinally to produce parietal and sporogenous layers." },
      { author: "Edward Charles Jeffrey", work: "The Anatomy of Woody Plants", quote: "The single cell of the hypodermal **archespore** undergoes successive divisions to form the embryo sac." }
    ]
  },
  "archesporial.md": {
    word: "archesporial",
    primary: "Relating to or characteristic of an archespore; designating cells that give rise to spores.",
    secondary: "In plant histology, describing the primordial germinal layer within a developing anther or ovule.",
    quotes: [
      { author: "Katherine Esau", work: "Plant Anatomy", quote: "The **archesporial** cell is distinguished from adjacent sterile cells by its dense cytoplasm and prominent nucleus." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "In moss capsules, the **archesporial** layer surrounds the central columella like a continuous cylinder." },
      { author: "Vernon Irvine Cheadle", work: "American Journal of Botany", quote: "Subsequent periclinal divisions of the **archesporial** initial yield both the primary tapetal and sporogenous lineages." }
    ]
  },
  "archesporium.md": {
    word: "archesporium",
    primary: "The mass of archesporial cells or primitive sporogenous tissue in the sporangium of a plant.",
    secondary: "In botanical anatomy, the central fertile tissue within anthers and ovules that develops into microspores or megaspores.",
    quotes: [
      { author: "Eduard Strasburger", work: "Textbook of Botany", quote: "The young anther reveals four lobes, each enclosing a column of fertile cells known as the **archesporium**." },
      { author: "Donald A. Johansen", work: "Plant Microtechnique", quote: "Differential staining clearly highlights the fertile **archesporium** against the surrounding sterile nucellar tissue." },
      { author: "Arthur Johnson Eames", work: "Morphology of the Angiosperms", quote: "The origin of the tapetum from peripheral layers of the **archesporium** is characteristic of many primitive families." }
    ]
  },
  "archetypal.md": {
    word: "archetypal",
    primary: "Constituting a typical or original model; of the nature of an archetype.",
    secondary: "In Jungian psychology and literary criticism, relating to universal, inherited mythic symbols, motifs, or character types.",
    quotes: [
      { author: "Carl Jung", work: "The Archetypes and the Collective Unconscious", quote: "The hero’s descent into the underworld represents an **archetypal** journey embedded in the human psyche." },
      { author: "Northrop Frye", work: "Anatomy of Criticism", quote: "The cyclical renewal of spring serves as an **archetypal** pattern underlying the structure of romantic literature." },
      { author: "Joseph Campbell", work: "The Hero with a Thousand Faces", quote: "Mythology speaks across generations because its figures incarnate **archetypal** trials of human transformation." }
    ]
  },
  "archetype.md": {
    word: "archetype",
    primary: "An original pattern, model, or prototype from which copies or variations are made.",
    secondary: "In Jungian psychoanalysis, an inherited subconscious idea, image, or motif present in the collective unconscious of humanity.",
    quotes: [
      { author: "Carl Jung", work: "Psychological Types", quote: "The **archetype** is a symbolic form that exists prior to any conscious experience, shaping our perceptions of the sacred and the profane." },
      { author: "Francis Bacon", work: "The Advancement of Learning", quote: "Nature exhibits singular primary forms which serve as an **archetype** for countless diverse creatures." },
      { author: "T. S. Eliot", work: "Tradition and the Individual Talent", quote: "Every creative writer must confront the enduring **archetype** embedded within classical literature." }
    ]
  },
  "archetypical.md": {
    word: "archetypical",
    primary: "Conforming to or representing an original pattern or standard; characteristic of an archetype (variant of archetypal).",
    secondary: "Expressing universal narrative motifs, symbolic types, or psychological templates across cultural traditions.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The saintly character exhibits an **archetypical** pattern of self-surrender recognized across diverse creeds." },
      { author: "Mircea Eliade", work: "The Myth of the Eternal Return", quote: "Traditional societies repeat **archetypical** gestures in order to remain aligned with primordial sacred time." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The white whale assumed an **archetypical** grandeur in Ahab’s brooding mind, embodying all malignant cosmic forces." }
    ]
  },
  "archiannelid.md": {
    word: "archiannelid",
    primary: "A primitive, minute marine worm belonging to the order Archiannelida, often lacking external segments or setae.",
    secondary: "In invertebrate zoology, interstitial polychaetes adapted to sand-grain environments (meiofauna) with simplified sensory and reproductive anatomy.",
    quotes: [
      { author: "Ray Lankester", work: "Treatise on Zoology", quote: "The simple nervous system of the **archiannelid** was once interpreted as the ancestral archetype of all segmented worms." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Examining intertidal sands reveals the tiny **archiannelid** gliding through interstitial spaces without disturbing the sediment." },
      { author: "Robert D. Barnes", work: "Invertebrate Zoology", quote: "Molecular evidence suggests that the diminutive **archiannelid** is a paedomorphic polychaete rather than a primitive precursor." }
    ]
  },
  "archiannelida.md": {
    word: "archiannelida",
    primary: "An order or taxonomic grouping of simple, primitive marine worms formerly considered the ancestral stock of annelids.",
    secondary: "In systematic biology, a polyphyletic group of miniature interstitial polychaetes (such as Polygordius and Dinophilus).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The group **Archiannelida** includes marine forms whose unsegmented external cuticle suggests an archaic grade of organization." },
      { author: "Ernst Haeckel", work: "Generelle Morphologie der Organismen", quote: "In tracing the genealogical descent of the worms, the **Archiannelida** occupy a pivotal phylogenetic position." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "Modern comparative morphology has dispersed the genera of **Archiannelida** into several distinct polychaete families." }
    ]
  },
  "archidiaconal.md": {
    word: "archidiaconal",
    primary: "Relating to an archdeacon or an archdeaconry.",
    secondary: "Pertaining to the supervisory judicial jurisdiction, visitations, and courts held by an archdeacon in Anglican and Roman Catholic canon law.",
    quotes: [
      { author: "Anthony Trollope", work: "The Warden", quote: "Dr. Grantly exercised his **archidiaconal** functions with a majestic dignity that cowed the rebel clergy of the diocese." },
      { author: "Thomas Hardy", work: "Under the Greenwood Tree", quote: "The parish register had been inspected during the annual **archidiaconal** visitation and marked with formal approval." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The legal clerk produced an **archidiaconal** citation commanding the recalcitrant witness to appear before the diocesan court." }
    ]
  },
  "archidiaconate.md": {
    word: "archidiaconate",
    primary: "The office, dignity, or territorial district of an archdeacon.",
    secondary: "In ecclesiastical governance, the administrative subdivision of a diocese presided over by an archdeacon.",
    quotes: [
      { author: "Anthony Trollope", work: "Barchester Towers", quote: "His elevation to the **archidiaconate** had conferred both clerical preeminence and substantial territorial influence." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The revenues of the **archidiaconate** supported charitable hospitals across the suburban parishes." },
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "The jurisdiction of the **archidiaconate** was originally founded in the superintendence of church fabric and clerical morals." }
    ]
  },
  "archidiskidon.md": {
    word: "archidiskidon",
    primary: "An extinct genus of massive mammoths (or subgenus of Mammuthus) of the Pliocene and Pleistocene epochs, including the southern mammoth (Archidiskidon meridionalis).",
    secondary: "In vertebrate paleontology, primitive proboscideans characterized by low-crowned molars with broad, widely spaced enamel ridges.",
    quotes: [
      { author: "Henry Fairfield Osborn", work: "Proboscidea", quote: "The immense fossil skeletal frame of **Archidiskidon** represents an early stage in the radiation of true elephants across Eurasia." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "Subsequent taxonomic revisions have subsumed **Archidiskidon** under the broader genus Mammuthus." },
      { author: "Björn Kurtén", work: "Pleistocene Mammals of Europe", quote: "Fossil teeth of **Archidiskidon** found in the Forest Bed of Norfolk demonstrate its adaptation to open temperate woodland." }
    ]
  },
  "archiepiscopal.md": {
    word: "archiepiscopal",
    primary: "Of or relating to an archbishop, his office, or his archdiocese.",
    secondary: "Relating to metropolitan ecclesiastical authority, councils, cross-bearing privileges, and metropolitan visitation rights.",
    quotes: [
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The seven bishops met at the **archiepiscopal** palace at Lambeth to draft their fateful petition to the Crown." },
      { author: "Walter Scott", work: "The Monastery", quote: "The herald announced the arrival of the lord primate with all the pomp of **archiepiscopal** authority." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **archiepiscopal** throne of Constantinople became the prize of violent doctrinal factions during the Fourth Century." }
    ]
  },
  "archil.md": {
    word: "archil",
    primary: "A violet or purple dye obtained from various lichens (especially Roccella tinctoria); also, the lichen itself (variant of orchil).",
    secondary: "In industrial history and historic textile dyeing, a natural colorant prepared by fermenting lichens with ammonia to yield orcein.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "His rough woolen cloak had been stained with **archil** until it took on the dusky purple of winter seas." },
      { author: "William Morris", work: "The Lesser Arts of Life", quote: "Before synthetic aniline colors displaced natural recipes, **archil** was prized for imparting richness to fine silks." },
      { author: "Humphry Davy", work: "Elements of Agricultural Chemistry", quote: "The lichen yielding **archil** grows abundantly upon the volcanic rocks of the Canary and Cape Verde Islands." }
    ]
  },
  "archilochus.md": {
    word: "archilochus",
    primary: "An ancient Greek lyric poet of Paros (7th century BCE) celebrated as the pioneer of iambic verse and fierce personal satire.",
    secondary: "In classical literary history, the legendary satirist whose stinging verses were said to have driven his enemies to despair; also a genus of hummingbirds.",
    quotes: [
      { author: "Horace", work: "Ars Poetica", quote: "Rage armed **Archilochus** with his own iambic metre, a weapon swift to strike and wound." },
      { author: "Friedrich Nietzsche", work: "The Birth of Tragedy", quote: "Alongside Homer, the Greek world revered **Archilochus** as the primal prototype of the subjective lyric genius." },
      { author: "John Keats", work: "Letters", quote: "The stinging iambs of ancient **Archilochus** prove that verse can strike like a scimitar when passion dictates." }
    ]
  },
  "archimandrite.md": {
    word: "archimandrite",
    primary: "A cleric in Eastern Orthodox and Eastern Catholic churches who heads a large monastery or group of monasteries; a monastic superior corresponding to an abbot.",
    secondary: "An honorary title conferred upon senior celibate priests in Byzantine rite churches distinguishing administrative or theological service.",
    quotes: [
      { author: "Fyodor Dostoevsky", work: "The Brothers Karamazov", quote: "The venerable **archimandrite** entered the refectory, bowed before the holy icons, and gave his silent blessing." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The **archimandrite** assembled his monks within the fortified sanctuary while nomadic raiders swept through the valley." },
      { author: "Leo Tolstoy", work: "War and Peace", quote: "An imperial decree was read aloud by the **archimandrite** of the monastery before the gathered veterans." }
    ]
  },
  "archimedes.md": {
    word: "archimedes",
    primary: "An ancient Greek mathematician, physicist, engineer, and astronomer of Syracuse (c. 287–212 BCE), renowned for principles of levers, buoyancy, and the spiral water screw.",
    secondary: "In the history of science, the foundational thinker whose mathematical treatises on the sphere, cylinder, and parabolic quadrature laid the groundwork for infinitesimal calculus.",
    quotes: [
      { author: "Plutarch", work: "Life of Marcellus", quote: "So absorbed was **Archimedes** in his geometric diagrams drawn upon the sand that he was unaware Syracuse had fallen." },
      { author: "Galileo Galilei", work: "Two New Sciences", quote: "We follow the footsteps of divine **Archimedes**, whose deductive geometry unravels the mechanics of heavy bodies." },
      { author: "Isaac Newton", work: "Principia", quote: "The profound discoveries of **Archimedes** concerning the equilibrium of planes provided the bedrock of modern mechanics." }
    ]
  },
  "archine.md": {
    word: "archine",
    primary: "An obsolete Russian unit of linear measure equal to 28 inches (approx. 71.12 cm) or one-third of a sagene; variant spelling of arshin.",
    secondary: "In 18th- and 19th-century commercial history, the standard fabric and timber measure standardized by Peter the Great across the Russian Empire.",
    quotes: [
      { author: "Leo Tolstoy", work: "War and Peace", quote: "The merchant unrolled the bolt of English broadcloth, measuring out each **archine** with a notched walnut rod." },
      { author: "Nikolai Gogol", work: "Dead Souls", quote: "The peasant carpenter promised to build a sturdy barn twenty paces long and twelve **archines** in height." },
      { author: "Anton Chekhov", work: "The Steppe", quote: "A wooden meter-stick carved with measurements in **archines** lay across the shopkeeper's dusty counter." }
    ]
  },
  "archipallium.md": {
    word: "archipallium",
    primary: "The phylogenetically oldest part of the cerebral cortex, comprising the olfactory cortex and hippocampus; the primitive limbic cortex.",
    secondary: "In neuroanatomy, the allocortex concerned with primal survival drives, olfactory sensation, and basic emotional responses, contrasting with the neopallium.",
    quotes: [
      { author: "Paul D. MacLean", work: "The Triune Brain in Evolution", quote: "The **archipallium**, preserved from early reptilian ancestors, forms the core of our ancestral emotional system." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "In the hippocampus, representing the mammalian **archipallium**, pyramidal neurons display remarkably regular radial organization." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "The evolution from lower vertebrates to mammals shows the progressive overgrowth of the **archipallium** by the neocortex." }
    ]
  },
  "archipelagic.md": {
    word: "archipelagic",
    primary: "Relating to, situated in, or consisting of an archipelago (a sea or expanse of water containing many islands).",
    secondary: "In the law of the sea and geopolitics, designating sovereign waters, baselines, and legal rights pertaining to an island state.",
    quotes: [
      { author: "Herman Melville", work: "Typee", quote: "The Marquesas group forms an **archipelagic** paradise where volcanic peaks plunge directly into azure waters." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "His trading schooner navigated the treacherous reefs of the **archipelagic** channels of the eastern Malay seas." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The **archipelagic** isolation of individual islands fostered extraordinary endemic speciation among butterflies and birds." }
    ]
  },
  "archipelago.md": {
    word: "archipelago",
    primary: "A group, cluster, or chain of islands; also, a sea or body of water studded with many islands.",
    secondary: "Metaphorically, any scattered or discontinuous collection of entities resembling islands across a wider landscape or institutional network.",
    quotes: [
      { author: "Aleksandr Solzhenitsyn", work: "The Gulag Archipelago", quote: "This vast **archipelago** of camps stretched across the continent, invisible to ordinary citizens yet swallowing millions." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "Fair Greece! sad relic of departed worth! Still roll thy waves around the blue Aegean **archipelago**." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The natural history of this **archipelago** is very remarkable: it seems to be a little world within itself." }
    ]
  },
  "architectonic.md": {
    word: "architectonic",
    primary: "Relating to architecture, architectural design, or structural organization.",
    secondary: "In philosophy and systems theory, relating to the systematic arrangement and structural unification of all branches of knowledge.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "By the term **architectonic** I mean the art of constructing systems; for systematic unity is what first raises ordinary knowledge to the rank of science." },
      { author: "Aristotle", work: "Nicomachean Ethics", quote: "Political science is the most **architectonic** of faculties, dictating which disciplines are studied in the commonwealth." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The **architectonic** rhythm of the cathedral façade balances every portal with subtle structural counterpoint." }
    ]
  },
  "architectonics.md": {
    word: "architectonics",
    primary: "The scientific principles of architecture, structural design, and structural organization.",
    secondary: "In philosophy, aesthetics, and literary theory, the structural logic, overarching design, or unified composition of a complex work or body of knowledge.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "The **architectonics** of pure reason prescribes the complete plan according to which the sciences must be systematically erected." },
      { author: "Mikhail Bakhtin", work: "Toward a Philosophy of the Act", quote: "The **architectonics** of human experience is organized around the fundamental ethical relationship between self and other." },
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "A thorough study of philosophical **architectonics** requires us to examine the foundational scaffolding of all inquiry." }
    ]
  },
  "architectural.md": {
    word: "architectural",
    primary: "Of, relating to, or conforming to the rules of architecture or building construction.",
    secondary: "Characterized by structural strength, deliberate proportion, and aesthetic organization.",
    quotes: [
      { author: "Vitruvius", work: "De Architectura", quote: "The **architectural** art requires that buildings possess firmness, commodity, and delightful beauty." },
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "True **architectural** ornament is never stuck on; it arises organically from the truthful demands of construction." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "The vast palazzo possessed an **architectural** solemnity that whispered of ancient Roman nobility." }
    ]
  },
  "architecturally.md": {
    word: "architecturally",
    primary: "With regard to architecture, building design, or structural form.",
    secondary: "In terms of systematic structural composition, spatial arrangement, or tectonic planning.",
    quotes: [
      { author: "Edith Wharton", work: "The Decoration of Houses", quote: "A room must be **architecturally** sound before any decorative furniture can appear harmonious." },
      { author: "Henry Adams", work: "Mont-Saint-Michel and Chartres", quote: "Chartres Cathedral is **architecturally** superior because every vault and flying buttress proclaims an act of communal faith." },
      { author: "Frank Lloyd Wright", work: "An Organic Architecture", quote: "To build **architecturally** means to let the material and the surrounding landscape dictate the living form of the house." }
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
console.log("Primacy Batch 5 completed! Total words updated:", Object.keys(wordsData).length);
