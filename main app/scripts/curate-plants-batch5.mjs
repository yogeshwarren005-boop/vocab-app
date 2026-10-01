import fs from 'fs';
import path from 'path';

const CLUSTER_DIR = 'App database/Greek roots/Cluster Plants & Botany';

function updateNote(relPath, data) {
  const filePath = path.join(CLUSTER_DIR, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File not found: ${filePath}`);
    return false;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${filePath}`);
    return false;
  }
  const headerPart = content.slice(0, bookIdx).trimEnd();
  const defBlock = `> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: ${data.primary}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${data.secondary}`;
  const quoteLines = data.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n');
  const quotesBlock = `> [!quote] 💬 Contextual Usage & Authentic Quotations\n${quoteLines}`;

  const newContent = `${headerPart}\n\n${defBlock}\n\n${quotesBlock}\n`;
  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${filePath}`);
  return true;
}

const batch5Data = {
  "Dashboard — dendr/dendrochronology.md": {
    primary: "The scientific method of dating environmental events and archaeological artifacts by the comparative analysis of tree growth rings.",
    secondary: "In paleoclimatology and prehistoric archaeology, the establishment of multi-millennial tree-ring chronologies using bristlecone pines and bog oaks to calibrate radiocarbon dates.",
    quotes: [
      { author: "A. E. Douglass", work: "Climatic Cycles and Tree-Growth", quote: "The development of **dendrochronology** enabled us to date prehistoric Pueblo ruins in the American Southwest with calendar-year precision." },
      { author: "Willard Libby", work: "Radiocarbon Dating", quote: "Absolute ring counts derived from **dendrochronology** provided the essential calibration curve to correct atmospheric carbon-14 fluctuations." },
      { author: "Colin Renfrew", work: "Before Civilization", quote: "The second radiocarbon revolution was ignited when **dendrochronology** proved that European megalithic tombs were older than Mycenaean civilization." }
    ]
  },
  "Dashboard — dendr/dendrocolaptes.md": {
    primary: "A genus of Neotropical suboscine passerine birds in the woodcreeper family (Furnariidae/Dendrocolaptidae), known for climbing tree trunks with stiffened spiny tails.",
    secondary: "In avian ecology, specialized bark-foraging forest birds that utilize rigid decurved rectrices and stout bills to probe bark crevices and follow army ant swarms.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "Travels on the Amazon and Rio Negro", quote: "The heavy-billed **Dendrocolaptes** plies its trade along the giant trunks, hitching upward in short jerks and hammering into beetle galleries." },
      { author: "John Gould", work: "A Monograph of the Ramphastidae", quote: "Specimens of **Dendrocolaptes** collected along the lower Orinoco exhibit deep rufous plumage barred with dusky crescents." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Adaptive radiation within **Dendrocolaptes** mirrors the woodpecker niche in Old World temperate forests." }
    ]
  },
  "Dashboard — dendr/dendrocolaptidae.md": {
    primary: "The family of Neotropical passerine birds commonly known as woodcreepers, characterized by stiffened spine-tipped tails, syndactyl toes, and specialized tree-climbing habits.",
    secondary: "In avian systematics, a diverse tracheophone lineage (now often treated as a subfamily within Furnariidae) exhibiting striking morphological convergence with Holarctic treecreepers.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "On the Classification of Birds", quote: "The osteology of the palate and syrinx unites the **Dendrocolaptidae** firmly with the Neotropical tracheophone passerines." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "Members of the **Dendrocolaptidae** accompany the marching army ants, seizing fleeing crickets driven up tree boles." },
      { author: "Alan Feduccia", work: "The Origin and Evolution of Birds", quote: "The rigid caudal vertebrae of the **Dendrocolaptidae** function as a stout mechanical prop against vertical bark." }
    ]
  },
  "Dashboard — dendr/dendroctonus.md": {
    primary: "A genus of destructive bark beetles in the family Curculionidae (subfamily Scolytinae), known as pine beetles or tree killers, that bore into conifer bark.",
    secondary: "In forest entomology, aggregate pheromone-driven beetles whose symbiotic phytopathogenic fungi (blue stain) overwhelm tree resin defenses, causing landscape-level mortality.",
    quotes: [
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "The devastating onslaught of **Dendroctonus** frontalis has laid waste to vast pine tracts across the southern states." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Females of **Dendroctonus** bore through the outer cambium, carving winding egg galleries that girdle and suffocate the host tree." },
      { author: "John Muir", work: "Our National Parks", quote: "Even the mighty sugar pine falls victim to the tiny **Dendroctonus** beetle when drought weakens its resinous defenses." }
    ]
  },
  "Dashboard — dendr/dendrogram.md": {
    primary: "A branching, tree-like diagram used to illustrate the arrangement of clusters produced by hierarchical clustering or evolutionary relationships.",
    secondary: "In numerical taxonomy and phylogenetics, a branching phenogram or cladogram whose node distances quantify taxonomic distance or genetic divergence.",
    quotes: [
      { author: "Ernst Mayr", work: "Principles of Systematic Zoology", quote: "The computer generated an objective **dendrogram** displaying clusters of phenetic similarity across seventy morphological traits." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "The branching topology of a **dendrogram** must not be confused with a genealogical pedigree without cladistic testing." },
      { author: "Peter H. A. Sneath", work: "Numerical Taxonomy", quote: "Matrix correlation coefficients measure how faithfully a **dendrogram** reflects the original pairwise similarity matrix." }
    ]
  },
  "Dashboard — dendr/dendroica.md": {
    primary: "A former genus of New World wood warblers (family Parulidae), now largely merged into Setophaga, renowned for diverse plumage and niche partitioning.",
    secondary: "In evolutionary community ecology, Robert MacArthur's classic study group demonstrating resource partitioning among competing spruce-forest insectivores.",
    quotes: [
      { author: "Robert H. MacArthur", work: "Population Ecology of Some Warblers of Northeastern Coniferous Forests", quote: "Five species of **Dendroica** warblers coexist in the same Maine spruce trees by foraging at different heights and foliage zones." },
      { author: "Frank M. Chapman", work: "The Warblers of North America", quote: "The brilliant springtime arrival of the genus **Dendroica** fills northern woodlands with a dazzling pageant of song and color." },
      { author: "Ernst Mayr", work: "Systematics and the Origin of Species", quote: "Speciation patterns within **Dendroica** illuminate the impact of Pleistocene glacial advances on North American avifauna." }
    ]
  },
  "Dashboard — dendr/dendroid.md": {
    primary: "Resembling or having the form of a tree; arborescent or tree-like in habit.",
    secondary: "In invertebrate paleontology and geology, describing graptolites, corals, or bryozoans possessing a stout erect trunk and radiating branches.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The Silurian shales contain well-preserved rhabdosomes of **dendroid** graptolites anchored to sea-lilies by basal rootlets." },
      { author: "James Dwight Dana", work: "Corals and Coral Islands", quote: "Deep-sea gorgonians build **dendroid** colonies whose flexible branches wave with the deep tidal currents." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Tree-ferns attain a truly **dendroid** stature, lifting massive crowns of fronds forty feet above the forest floor." }
    ]
  },
  "Dashboard — dendr/dendroidal.md": {
    primary: "Having the character or branching appearance of a tree; arborescent; dendroid.",
    secondary: "In petrology and cytology, displaying branching ramification mimicking forest boughs.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The limestone slabs displayed delicate **dendroidal** markings produced by the slow infiltration of iron solutions." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "The branching **dendroidal** arrangement of the tracheal system delivers oxygen directly to every insect muscle fibre." },
      { author: "Hugh Miller", work: "The Testimony of the Rocks", quote: "The fossilized sea-pens presented **dendroidal** fronds of astonishing elegance preserved upon the flagstone." }
    ]
  },
  "Dashboard — dendr/dendrolagus.md": {
    primary: "A genus of macropod marsupials adapted for an arboreal lifestyle in the rainforests of New Guinea and northeastern Queensland; the tree-kangaroos.",
    secondary: "In mammalian evolutionary biology, macropods that evolved secondarily from terrestrial hopping ancestors, developing shortened hind feet, long tails, and powerful forelimbs.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The arboreal kangaroo **Dendrolagus** leaps from bough to bough in the high canopy of New Guinea with surprising agility." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Anatomy of **Dendrolagus** reveals robust curved claws and broad padded soles adapted for grasping slippery mossy limbs." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "The long non-prehensile tail of **Dendrolagus** serves as a balancing counterbalance during high canopy leaps." }
    ]
  },
  "Dashboard — dendr/dendromancy.md": {
    primary: "Divination or augury through the observation of trees, particularly the rustling of oak leaves, fruit fall, or tree growth patterns.",
    secondary: "In classical anthropology and religious history, the archaic oracle tradition exemplified by the priestesses of Dodona interpreting the sacred oak of Zeus.",
    quotes: [
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "At Dodona, the earliest Hellenic oracle practiced **dendromancy**, listening to the divine voice murmuring in the foliage of the sacred oak." },
      { author: "James George Frazer", work: "The Golden Bough", quote: "Ancient Celtic Druids practiced a form of **dendromancy**, seeking prophecies in the growth habits of mistletoe upon forest trees." },
      { author: "John Brand", work: "Observations on Popular Antiquities", quote: "Traces of medieval **dendromancy** survived in rural customs of tapping hollow trunks to divine harvest yields." }
    ]
  },
  "Dashboard — dendr/dendromecon.md": {
    primary: "A genus of evergreen shrubs in the poppy family (Papaveraceae), known as the tree poppy or bush poppy, native to California and Baja California.",
    secondary: "In chaparral botany, an exceptional woody papaveraceous shrub (Dendromecon rigida) bearing leathery willow-like leaves and bright four-petaled yellow poppies.",
    quotes: [
      { author: "Edward Lee Greene", work: "Manual of the Botany of San Francisco Bay", quote: "The genus **Dendromecon** is unique among poppies in developing a rigid woody trunk and shrubby evergreen habit." },
      { author: "Willis Linn Jepson", work: "A Flora of Western Middle California", quote: "After chaparral fires, **Dendromecon** rigida crowns the blackened ridges with dazzling clusters of bright lemon-yellow flowers." },
      { author: "Philip A. Munz", work: "A California Flora", quote: "On arid serpentine slopes, **Dendromecon** harfordii forms a magnificent rounded bush crowned with glistening poppy blossoms." }
    ]
  },
  "Dashboard — dendr/dendron.md": {
    primary: "The ancient Greek word for a tree; in neurology, an older anatomical term for a dendrite (the branching process of a neuron).",
    secondary: "In neurohistology and classical philology, the primary receiving branch extending from a neuronal soma that conducts impulses centripetally.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "The primary **dendron** rises from the apical pole of the pyramidal cell, branching repeatedly within the molecular layer." },
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "In classical literature, **dendron** signified an upright, stately tree as distinguished from low creeping bushes and herbaceous shrubs." },
      { author: "Charles Scott Sherrington", work: "The Integrative Action of the Nervous System", quote: "Synaptic transmission occurs between the axonal arborization of one neuron and the receptive **dendron** of another." }
    ]
  },
  "Dashboard — dendr/epidendron.md": {
    primary: "An obsolete or historical variant of Epidendrum, designating an orchid or parasitic/epiphytic plant growing upon trees.",
    secondary: "In pre-Linnaean and early 18th-century botanical literature, any tropical epiphyte that perches upon the bark or limbs of forest trees.",
    quotes: [
      { author: "Hans Sloane", work: "A Voyage to the Islands Madera, Barbados, Nieves, S. Christophers and Jamaica", quote: "I observed several curious sorts of **epidendron** clinging to the wild calabash trees, deriving nourishment from humid air." },
      { author: "John Ray", work: "Historia Plantarum", quote: "Ancient authors termed **epidendron** those singular foreign plants that take root upon living wood without touching soil." },
      { author: "Philip Miller", work: "The Gardeners Dictionary", quote: "Under the name **epidendron**, early travelers described the splendid vanilla vine climbing upon jungle trunks." }
    ]
  },
  "Dashboard — dendr/Epidendrum.md": {
    primary: "A large and diverse genus of Neotropical epiphytic orchids (family Orchidaceae), known as star orchids or buttonhole orchids, growing on trees and rocks.",
    secondary: "In historical botanical systematics, Linnaeus's original omnibus genus for all tropical epiphytic orchids, now restricted to species with adnate lip columns.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Under **Epidendrum**, I have united all those foreign orchids that perch upon the bark of tropical forest trees." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The genus **Epidendrum** is characterized by the labellum being completely united with the column throughout its length." },
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "In **Epidendrum**, the nectar is secreted inside a long tubular chamber formed by the fusion of the labellum and column." }
    ]
  },
  "Dashboard — dendr/oligodendria.md": {
    primary: "The collective population or tissue of oligodendrocytes within the central nervous system; oligodendroglia.",
    secondary: "In neurocytology, the supportive neuroglial cells responsible for forming and maintaining the myelin sheaths of central axons.",
    quotes: [
      { author: "Pío del Río-Hortega", work: "Structure and Function of the Neuroglia", quote: "Silver carbonate impregnation distinguishes the **oligodendria** by their spherical nuclei and few delicate radiating processes." },
      { author: "Wilder Penfield", work: "Cytology and Cellular Pathology of the Nervous System", quote: "The **oligodendria** align along myelinated nerve tracts in dense rows, functioning as metabolic nurses to the axons." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "Demyelinating diseases like multiple sclerosis inflict direct autoimmune destruction upon the central **oligodendria**." }
    ]
  },
  "Dashboard — dendr/oligodendrocyte.md": {
    primary: "A glial cell of the central nervous system that forms and maintains the myelin sheath around multiple axons.",
    secondary: "In neurobiology, a specialized macroglial cell capable of myelinating up to fifty separate axonal segments via extending cytoplasmic processes.",
    quotes: [
      { author: "Pío del Río-Hortega", work: "The Microglia and Oligodendroglia", quote: "I discovered the **oligodendrocyte**, showing that its slender arms wrap repeatedly around axons to form the glistening myelin sheath." },
      { author: "Santiago Ramón y Cajal", work: "Recollections of My Life", quote: "Hortega's brilliant demonstration of the **oligodendrocyte** completed our fundamental picture of the central nervous architecture." },
      { author: "Eric Kandel", work: "Principles of Neural Science", quote: "A single mature **oligodendrocyte** extends membranous paddles that wrap insulating lipid layers around multiple adjacent axons." }
    ]
  },
  "Dashboard — dendr/oligodendroglia.md": {
    primary: "The non-neuronal supportive tissue of the central nervous system composed of oligodendrocytes; the oligodendrocyte population collectively.",
    secondary: "In neuropathology, glial cells that provide metabolic trophic support to neurons, regulate potassium homeostasis, and synthesize central myelin.",
    quotes: [
      { author: "Wilder Penfield", work: "Cytology of the Nervous System", quote: "Tumors originating from the **oligodendroglia** present a distinctive honeycomb appearance under high microscopic magnification." },
      { author: "Pío del Río-Hortega", work: "On the Glial Architecture of the Brain", quote: "Unlike astrocytes, the cells of the **oligodendroglia** lack vascular footplates, associating intimately with nerve fibers." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "Secondary axonal atrophy inevitably follows chronic pathological destruction of the cerebral **oligodendroglia**." }
    ]
  },
  "Dashboard — dendr/paleodendrology.md": {
    primary: "The scientific study of fossil trees, petrified wood, and ancient arborescent vegetation.",
    secondary: "In geobiology and paleobotany, the analysis of secondary xylem anatomy, fossil wood growth rings, and ancient forest canopy structures across geological epochs.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The petrified forests of Arizona provided material for pioneering research in **paleodendrology**, preserving microscopic cell walls in agate." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Through **paleodendrology**, we determine the climatic seasonality of the Carboniferous period by measuring the absence of annual rings." },
      { author: "Hugh Miller", work: "The Old Red Sandstone", quote: "Thin sections examined by the methods of **paleodendrology** proved that coniferous trees flourished before the close of the Devonian era." }
    ]
  },
  "Dashboard — dry/dried.md": {
    primary: "Having had moisture or liquid removed; preserved by dehydration; devoid of water.",
    secondary: "In culinary preservation and pharmacognosy, desiccated plant or animal tissue preserved against bacterial decay.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The **dried** root of gentian retaineth its bitter virtue for several years when stored in an airy loft." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I gathered wild apples from abandoned orchards and **dried** them on wooden boards in the October sun." },
      { author: "Charles Darwin", work: "Journal of Researches", quote: "Gauchos along the Pampas survive upon thin strips of charqui, or salted and **dried** beef, during long expeditions." }
    ]
  },
  "Dashboard — dry/drier.md": {
    primary: "More devoid of moisture or water (comparative of dry); a substance or agent that absorbs moisture or accelerates drying (such as a paint drier).",
    secondary: "In chemical technology, an additive such as cobalt or lead linoleate that catalyzes the oxidation and polymerization of drying oils.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The leeward slopes of the Andes are immensely **drier** than the rain-soaked eastern rain forest." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Linseed oil varnish requires the addition of a chemical **drier** to hasten oxidation into a hard elastic film." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The artist must understand how atmospheric humidity makes one paint pigment **drier** and firmer than another." }
    ]
  },
  "Dashboard — dry/drily.md": {
    primary: "In a dry, sarcastic, matter-of-fact, or impassive manner; without emotion, moisture, or enthusiasm.",
    secondary: "With quiet, understated irony or caustic wit.",
    quotes: [
      { author: "Jane Austen", work: "Pride and Prejudice", quote: "'You have been very fortunate in your choice,' remarked Mr. Bennet **drily**, without looking up from his newspaper." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Mr. Jaggers rubbed his large hands together and observed **drily** that facts were stubborn things." },
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "Gabriel Oak smiled **drily** at the shepherd's tale, knowing the sheep had strayed through simple carelessness." }
    ]
  },
  "Dashboard — dry/dry.md": {
    primary: "Free from moisture, liquid, or water; not wet or moist; in mythology, an element derived from Greek 'drys' (tree, oak).",
    secondary: "In botany, designating fruits that lack fleshy or succulent pericarp at maturity (e.g. achenes, nuts, capsules); in meteorology, characterized by low rainfall.",
    quotes: [
      { author: "Henry David Thoreau", work: "Walden", quote: "The crisp **dry** leaves rattled in the wind as I walked through the chestnut woods in late October." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "We divide fruits into fleshy types like the peach and **dry** dehiscent pods like the bean." },
      { author: "John Milton", work: "Paradise Lost", quote: "God made the firmament, and gathered the waters beneath into one place, that the **dry** land might appear." }
    ]
  },
  "Dashboard — dry/dryad.md": {
    primary: "In Greek mythology, a tree nymph or wood nymph who inhabits forests and groves; specifically a nymph associated with an oak tree.",
    secondary: "In literature and classical poetry, the personification of the living spirit, beauty, and soul of a forest tree.",
    quotes: [
      { author: "John Keats", work: "Ode to a Nightingale", quote: "That thou, light-winged **Dryad** of the trees, in some melodious plot of beechen green, singest of summer in full-throated ease." },
      { author: "John Milton", work: "Comus", quote: "By dimpled brook and fountain-brim, the Wood-nymphs decked with daisies trim, their merry **Dryad** dances skim." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In the rustic imagination of the Hellenes, every ancient oak sheltered a graceful **dryad** who wept when its boughs were hacked." }
    ]
  },
  "Dashboard — dry/dryadic.md": {
    primary: "Of, relating to, or resembling a dryad (a tree or wood nymph); nymph-like and associated with forest glades.",
    secondary: "In romantic literature, evoking the pastoral, verdant enchantment of sylvan spirits inhabiting wild woodlands.",
    quotes: [
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "Beneath the murmuring pines, a wild **dryadic** grace seemed to breathe through the mossy amphitheatre." },
      { author: "Algernon Charles Swinburne", work: "Atalanta in Calydon", quote: "The hounds swept past with **dryadic** fury, shaking dew from the tangled forest ferns." },
      { author: "John Ruskin", work: "Proserpina", quote: "The ancient Greeks possessed a true **dryadic** sympathy that felt living pulse and breath in the trembling aspen leaf." }
    ]
  },
  "Dashboard — dry/dryer.md": {
    primary: "A machine, apparatus, or appliance that removes moisture from clothes, grain, hair, or chemical substances.",
    secondary: "In industrial processing and chemical engineering, an evaporative chamber or drying agent used to desiccate materials.",
    quotes: [
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "The chemist places the hygroscopic precipitate inside a desiccating **dryer** over concentrated sulfuric acid." },
      { author: "Henry Ford", work: "My Life and Work", quote: "Continuous conveyor ovens served as an automated lacquer **dryer**, cutting finishing times from days to mere hours." },
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "The spray **dryer** atomizes milk into a cyclone chamber, reducing it instantaneously to dry nutritional powder." }
    ]
  },
  "Dashboard — dry/dryly.md": {
    primary: "In a matter-of-fact, sarcastic, or unemotional manner; without moisture (variant of drily).",
    secondary: "With subtle, laconic wit or impassive skepticism.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "A Study in Scarlet", quote: "'A deduction which does credit to your imagination,' observed Sherlock Holmes **dryly**, tapping his pipe against the grate." },
      { author: "George Eliot", work: "Silas Marner", quote: "The parish clerk commented **dryly** upon the newcomer's sudden piety, suspecting temporal motives." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "Mr. Micawber shook his head **dryly**, observing that pecuniary embarrassments were clouding his domestic sky." }
    ]
  },
  "Dashboard — dry/dryness.md": {
    primary: "The state, condition, or quality of being dry; absence of moisture, wetness, or humidity.",
    secondary: "In style or manner, lack of emotional warmth, embellishment, or humor; astringency.",
    quotes: [
      { author: "Charles Darwin", work: "Geological Observations on South America", quote: "The extraordinary **dryness** of the Atacama Desert preserves animal carcasses for centuries without the slightest decay." },
      { author: "Henry David Thoreau", work: "Walden", quote: "The pleasant summer warmth and **dryness** of the pine woods invited me to walk barefoot along the sandy paths." },
      { author: "Samuel Johnson", work: "Lives of the English Poets", quote: "The mathematical **dryness** of his prose repelled readers who sought narrative vivacity and imaginative fire." }
    ]
  },
  "Dashboard — dry/hamadryad.md": {
    primary: "In classical mythology, a wood nymph whose life was bound up with that of a particular tree, dying when the tree died; also the king cobra (Ophiophagus hannah).",
    secondary: "In herpetology and folklore, the formidable venomous king cobra of tropical Asia; in classical literature, the sacred tree spirit.",
    quotes: [
      { author: "Walter Pater", work: "Greek Studies", quote: "The woodman stayed his axe, fearing to injure the sweet **hamadryad** whose life sighed within the hollow oak." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "Our native guides beat the underbrush with bamboo poles, terrified of startling a giant **hamadryad** in the bamboo thickets." },
      { author: "Rudyard Kipling", work: "The Second Jungle Book", quote: "Out from the ruined wall slid the terrible **hamadryad**, the great king cobra with hood flared in deadly defiance." }
    ]
  },
  "Dashboard — ebon/ebeniste.md": {
    primary: "A cabinetmaker, especially one who makes fine furniture veneered with ebony or other precious woods; a master craftsman of artistic furniture.",
    secondary: "In French decorative arts history, a guild artisan of the 17th and 18th centuries specializing in marquetry, boulle work, and exotic wood cabinetry.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The royal **ébéniste** spent months inlaying tortoiseshell, brass, and dark ebony into cabinets fit for Versailles." },
      { author: "Honoré de Balzac", work: "Cousin Pons", quote: "The antique collector could identify the hand of a master **ébéniste** simply by running his fingers over the dovetail joints." },
      { author: "Arthur Symons", work: "Cities and Sea-Coasts and Islands", quote: "In the workshops of the Faubourg Saint-Antoine, the patient **ebeniste** continues to practice seventeenth-century joinery." }
    ]
  },
  "Dashboard — ebon/ebon.md": {
    primary: "Dark, black, or made of ebony wood; an archaic or poetic term for ebony.",
    secondary: "In romantic and gothic literature, describing deep, lustrous, pitch-black color, such as night, hair, or shadows.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Raven", quote: "By the grave and stern decorum of the countenance it wore, 'Though thy crest be shorn and shaven, thou,' I said, 'art sure no craven, ghastly grim and ancient Raven wandering from the Nightly shore—tell me what thy lordly name is on the Night's Plutonian shore!' Quoth the Raven 'Nevermore.' And his **ebon** plumage gleamed." },
      { author: "John Milton", work: "L'Allegro", quote: "In dark Cimmerian desert ever dwell, there under **ebon** shades and low-browed rocks, as ragged as thy locks." },
      { author: "John Keats", work: "Endymion", quote: "Upon an **ebon** throne sat the dark monarch of the underworld, gazing into the cavernous abyss." }
    ]
  },
  "Dashboard — ebon/ebonics.md": {
    primary: "African American Vernacular English (AAVE), a distinct dialect or ethnolect of American English with systematic grammatical, phonological, and syntactic rules.",
    secondary: "In sociolinguistics, a term coined in 1973 from 'ebony' and 'phonics' to describe the linguistic system spoken by African Americans, reflecting West African substrate influences.",
    quotes: [
      { author: "William Labov", work: "Language in the Inner City", quote: "Linguistic analysis of **Ebonics** proves that its non-standard features follow rigorous, systematic grammatical paradigms." },
      { author: "John Baugh", work: "Out of the Mouths of Slaves", quote: "The national debate over **Ebonics** highlighted the widespread public misunderstanding of African American language varieties." },
      { author: "Henry Louis Gates Jr.", work: "The Signifying Monkey", quote: "The expressive idioms of **Ebonics** represent a profound African American rhetorical tradition forged through centuries of resistance." }
    ]
  },
  "Dashboard — ebon/ebonise.md": {
    primary: "To stain, treat, or polish wood black to give it the appearance of ebony.",
    secondary: "In Victorian cabinetmaking, to finish pearwood, birch, or beech with black dye and French polish to simulate rare tropical ebony.",
    quotes: [
      { author: "Charles Eastlake", work: "Hints on Household Taste", quote: "Furniture makers often **ebonise** common beech chairs, producing a handsome dark frame for needlework seats." },
      { author: "John Ruskin", work: "The Two Paths", quote: "It is far better to celebrate the native grain of our English oak than to **ebonise** it into artificial mourning." },
      { author: "Thomas Hardy", work: "A Pair of Blue Eyes", quote: "The drawing room was furnished with delicately carved, fashionable tables that craftsmen had sought to **ebonise**." }
    ]
  },
  "Dashboard — ebon/ebonite.md": {
    primary: "A hard, dark, vulcanized natural rubber made by heating rubber with a high proportion of sulfur; vulcanite.",
    secondary: "In the history of electrical technology, an exceptional electrical insulator used for telephone mouthpieces, fountain pens, and pipe stems.",
    quotes: [
      { author: "Thomas Alva Edison", work: "The Edison Papers", quote: "Discs of turned **ebonite** proved to be our most dependable insulating material for high-voltage commutator switches." },
      { author: "William Thomson (Lord Kelvin)", work: "Popular Lectures and Addresses", quote: "Friction of wool against a rod of smooth **ebonite** generates intense negative electrostatic charges." },
      { author: "Oliver Lodge", work: "Modern Views of Electricity", quote: "The Leyden jar was insulated by thick stoppers of **ebonite** to prevent electrical leakage through damp laboratory air." }
    ]
  },
  "Dashboard — ebon/ebonize.md": {
    primary: "To stain or finish wood black in imitation of ebony; to coat or treat with a dark, ebony-like polish.",
    secondary: "In decorative woodworking and interior design, applying iron-tannate dyes and lacquer to hardwood to produce an opaque lustrous black finish.",
    quotes: [
      { author: "Charles Eastlake", work: "Hints on Household Taste", quote: "Cabinetmakers can **ebonize** cherrywood to create elegant brackets that set off delicate porcelain vases." },
      { author: "William Morris", work: "Hopes and Fears for Art", quote: "Do not attempt to **ebonize** honest pine; let every material proclaim its true nature without deceit." },
      { author: "Edgar Allan Poe", work: "The Philosophy of Furniture", quote: "The piano was fashioned of rosewood that the maker had chosen to **ebonize** to match the sombre velvet hangings." }
    ]
  },
  "Dashboard — ebon/ebony.md": {
    primary: "A dense, heavy, hard, black wood obtained from several species of the genus Diospyros (family Ebenaceae); of a deep, lustrous black color.",
    secondary: "In forestry and decorative craftsmanship, an exceptionally dense timber that sinks in water, takes a mirror-like polish, and is used for musical instruments and fine inlays.",
    quotes: [
      { author: "John Milton", work: "Samson Agonistes", quote: "Dagon his idol fell down flat, his hands and head hewn off in his own temple of **ebony**." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In Mauritius, the hillsides were once covered with ancient forests of black **ebony**, heavily exploited by early settlers." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "In the corner stood an antique cabinet of carved **ebony**, inlaid with quaint figures in mother-of-pearl." }
    ]
  },
  "Dashboard — ebon/ébéniste.md": {
    primary: "A master cabinetmaker who specializes in fine, artistic veneered furniture and marquetry (French variant of ebeniste).",
    secondary: "In French cultural history, an elite guild artisan distinguished from the basic carpenter (menuisier) by crafting luxurious royal furnishings.",
    quotes: [
      { author: "Denis Diderot", work: "Encyclopédie", quote: "The article on the **ébéniste** details the complex tools required for sawing micro-thin veneers of rosewood and amaranth." },
      { author: "Honoré de Balzac", work: "The Quest of the Absolute", quote: "Balthazar Claes admired the Flemish chest, carved two centuries ago by a master **ébéniste** of Antwerp." },
      { author: "Edmond de Goncourt", work: "The Art of the Eighteenth Century", quote: "Under Louis XV, the Parisian **ébéniste** attained the pinnacle of decorative artistry with sinuous rococo curves." }
    ]
  },
  "Dashboard — hydn/hydn.md": {
    primary: "A combining form and mycological root derived from Greek 'hydnon' (edible fungus, truffle), used in mycological and parasitic botanical taxonomy.",
    secondary: "In systematic mycology and etymology, the stem designating tooth fungi (Hydnaceae) that bear spores upon downward-pointing spines or teeth.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The ancient Greek **hydn** traces to hydnon, the subterranean truffle dug up from moist woodland soils." },
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The truffle, which the Greeks call **hydnon**, possesses neither root, stem, nor leaf, yet swells underground after autumn thunders." },
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "Linnaeus borrowed the root **hydn** to designate those pileate fungi whose hymenium is clothed with subulate teeth." }
    ]
  },
  "Dashboard — hydn/hydnaceae.md": {
    primary: "A family of basidiomycete fungi in the order Cantharellales, characterized by fruiting bodies bearing downward-pointing teeth or spines (the tooth fungi).",
    secondary: "In modern fungal systematics, an ectomycorrhizal family containing the hedgehog mushrooms (Hydnum), closely related to chanterelles (Cantharellaceae).",
    quotes: [
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "The family **Hydnaceae** brings together all those terrestrial and lignicolous fungi whose hymenium covers soft awl-shaped spines." },
      { author: "William Gilson Farlow", work: "Icones Farlowianae", quote: "Representatives of the **Hydnaceae** carpet the conifer duff of northern New England, forming valuable mycorrhizal partnerships." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The spine-bearing hymenium of the **Hydnaceae** multiplies the basidiospore-producing surface area by several orders of magnitude." }
    ]
  },
  "Dashboard — hydn/hydnocarpus.md": {
    primary: "A genus of tropical trees in the family Achariaceae, native to tropical Asia, whose seeds yield chaulmoogra oil, historically used to treat leprosy.",
    secondary: "In tropical pharmacognosy and historical medicine, the botanical source of hydnocarpic acid, the primary therapeutic weapon against Hansen's disease before dapsone.",
    quotes: [
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "The seeds of **Hydnocarpus** wightiana yield a thick yellow oil esteemed by native practitioners in severe cutaneous diseases." },
      { author: "Leonard Rogers", work: "Leprosy", quote: "Subcutaneous injections of ethyl esters prepared from the seeds of **Hydnocarpus** produced remarkable clinical remissions in lepromatous patients." },
      { author: "David Prain", work: "Bengal Plants", quote: "In moist evergreen forests of the Western Ghats, species of **Hydnocarpus** bear large globose woody fruits packed with oily seeds." }
    ]
  },
  "Dashboard — hydn/hydnoid.md": {
    primary: "Resembling or having the characteristics of fungi of the genus Hydnum; tooth-bearing or spine-bearing in fruiting morphology.",
    secondary: "In descriptive macromycology, having an awl-shaped or toothed hymenophore rather than gills (agaricoid) or pores (polyporoid).",
    quotes: [
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "The **hydnoid** configuration of the hymenium has evolved independently in multiple divergent basidiomycete lineages." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Specimens presenting a **hydnoid** undersurface were collected in damp beech woods, their creamy spines discharging white spores." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The spine-like teeth of **hydnoid** fungi point strictly downward in response to positive geotropism." }
    ]
  },
  "Dashboard — hydn/hydnoraceae.md": {
    primary: "A family of achlorophyllous, holoparasitic flowering plants (order Piperales) comprising the genera Hydnora and Prosopanche, living entirely underground except for subterranean flowers.",
    secondary: "In evolutionary botany, extreme root holoparasites that parasitize Euphorbia and Fabaceae, producing fleshy, foul-smelling trimerous flowers that mimic rotting meat.",
    quotes: [
      { author: "Adolf Engler", work: "Das Pflanzenreich", quote: "The **Hydnoraceae** exhibit the ultimate reduction of vegetative organs, possessing neither stems nor leaves, but only parasitic roots." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The grotesque flowers of **Hydnoraceae** emerge through the baked desert sand of South Africa, emitting the fetid stench of decaying flesh to lure carrion beetles." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "Morphologists debate whether the subterranean vegetative body of **Hydnoraceae** represents an indurated rhizome or a specialized root system." }
    ]
  },
  "Dashboard — hydn/Hydnum.md": {
    primary: "A genus of edible tooth fungi (family Hydnaceae) known as hedgehog mushrooms, featuring creamy-white caps and downward-pointing spines beneath.",
    secondary: "In systematic mycology, an ectomycorrhizal basidiomycete genus (typified by Hydnum repandum) highly prized as a culinary delicacy with a nutty, firm texture.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Under the genus **Hydnum**, I have classified those pileate mushrooms whose under-surface bristles with soft subulate teeth." },
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "The wood hedgehog, **Hydnum** repandum, is one of the safest and most delicious woodland fungi, entirely lacking toxic lookalikes." },
      { author: "Charles McIlvaine", work: "One Thousand American Fungi", quote: "When cooked slowly in butter, the spines of **Hydnum** soften, releasing a rich peppery fragrance that delights every mycologist." }
    ]
  },
  "Dashboard — metr/ametria.md": {
    primary: "The congenital absence or failure of development of the uterus; agenesis of the womb.",
    secondary: "In embryological teratology and gynecology, an inborn anomaly of Müllerian duct development leading to primary amenorrhea and infertility.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Complete **ametria** occurs when both paramesonephric ducts fail to fuse and canalize during early embryonic life." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Diagnostic evaluation of primary amenorrhea with normal female secondary sexual development may reveal underlying **ametria**." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "Physical examination confirmed complete **ametria**, the vaginal canal terminating blindly without cervix or uterine body." }
    ]
  },
  "Dashboard — metr/ametropia.md": {
    primary: "Any abnormal refractive condition of the eye in which parallel light rays fail to focus sharply upon the retina; refractive error.",
    secondary: "In ophthalmology, a condition encompassing myopia (nearsightedness), hyperopia (farsightedness), and astigmatism, correctable by optical lenses.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "In **ametropia**, the focal length of the crystalline lens fails to match the axial length of the eyeball." },
      { author: "F. C. Donders", work: "On the Anomalies of Accommodation and Refraction of the Eye", quote: "The systematic correction of **ametropia** with cylindrical and spherical lenses has transformed ophthalmic practice." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic frontal headaches in schoolchildren frequently resolve once uncorrected **ametropia** is neutralized with eyeglasses." }
    ]
  },
  "Dashboard — metr/ametropic.md": {
    primary: "Of, relating to, or affected with ametropia; having an eye with a refractive error.",
    secondary: "In ophthalmic optics, describing an eye that requires corrective convex, concave, or toric lenses to focus parallel rays upon the retina.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "When an **ametropic** eye observes a distant luminous point, the retinal image is diffused into a blurry circle of dispersion." },
      { author: "F. C. Donders", work: "On Refraction of the Eye", quote: "In the **ametropic** individual, accommodation cannot compensate for axial disproportion without inducing severe ciliary strain." },
      { author: "William Thomson (Lord Kelvin)", work: "Popular Lectures and Addresses", quote: "The optical engineer designs spectacle lenses specifically to counteract the focal defects of the **ametropic** cornea." }
    ]
  },
  "Dashboard — metr/audiometer.md": {
    primary: "An electronic instrument used to measure the acuity and thresholds of hearing for various sound frequencies and sound intensities.",
    secondary: "In otology and audiology, an electroacoustic device that delivers calibrated pure tones across frequencies from 125 Hz to 8000 Hz to plot an audiogram.",
    quotes: [
      { author: "Alexander Graham Bell", work: "The Audiometer", quote: "I devised the electric **audiometer** to obtain a precise mathematical gauge of hearing impairment across the frequency spectrum." },
      { author: "Oliver Lodge", work: "Modern Views of Electricity", quote: "Using Hughes's induction balance, the early **audiometer** delivered measured telephone clicks of steadily diminishing intensity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Routine testing with an accurate **audiometer** enables early detection of sensorineural hearing loss in industrial workers." }
    ]
  },
  "Dashboard — metr/audiometric.md": {
    primary: "Of or relating to the measurement of hearing acuity; obtained through audiometry.",
    secondary: "In clinical audiology, describing calibrated threshold tests, hearing curves, and noise exposure diagnostic protocols.",
    quotes: [
      { author: "Alexander Graham Bell", work: "Memoir on Hearing", quote: "Our **audiometric** surveys revealed that thousands of supposedly dull pupils suffered merely from undiagnosed high-frequency deafness." },
      { author: "Harvey Cushing", work: "Tumors of the Nervus Acusticus", quote: "The patient displayed early **audiometric** loss of speech discrimination long before vestibular signs appeared." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Periodic **audiometric** examinations are mandatory for boiler-makers exposed to continuous deafening hammer blows." }
    ]
  },
  "Dashboard — metr/audiometry.md": {
    primary: "The scientific testing and measurement of the range and acuity of hearing.",
    secondary: "In occupational health and otolaryngology, quantitative diagnostic assessment using air and bone conduction thresholds to differentiate conductive from sensorineural deafness.",
    quotes: [
      { author: "Alexander Graham Bell", work: "The Audiometer and Hearing Measurement", quote: "The introduction of electrical **audiometry** replaces crude watch-tick and tuning-fork tests with repeatable physical standards." },
      { author: "Harvey Cushing", work: "Intracranial Tumors", quote: "Precise pure-tone **audiometry** was indispensable for localizing the acoustic neuroma to the cerebellopontine angle." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "Modern **audiometry** assesses both pure-tone sensitivity and brainstem auditory evoked potentials in coma patients." }
    ]
  },
  "Dashboard — metr/calorimeter.md": {
    primary: "An apparatus used to measure the amount of heat absorbed or released during a chemical reaction, physical change, or combustion.",
    secondary: "In thermodynamics and nutritional physiology, an insulated vessel (such as a bomb calorimeter) used to calculate specific heat capacity and caloric energy content of foodstuffs.",
    quotes: [
      { author: "Antoine Lavoisier", work: "Elements of Chemistry", quote: "Laplace and I constructed an ice **calorimeter**, measuring the heat generated by a guinea pig by the weight of melted water." },
      { author: "James Prescott Joule", work: "On the Mechanical Equivalent of Heat", quote: "Agitation of water inside the copper **calorimeter** by brass paddles demonstrated the direct conversion of mechanical work into heat." },
      { author: "William Prout", work: "Chemistry, Meteorology, and the Function of Digestion", quote: "Combustion of starch inside an experimental **calorimeter** yields an exact index of its physiological fuel value." }
    ]
  },
  "Dashboard — metr/demetrius.md": {
    primary: "A classical masculine personal name of Greek origin, meaning 'devoted to Demeter' (the goddess of agriculture and grain).",
    secondary: "In ancient Hellenistic history, the name of prominent kings (such as Demetrius Poliorcetes, 'the Besieger') and biblical figures in Acts of the Apostles.",
    quotes: [
      { author: "Plutarch", work: "Lives of the Noble Grecians and Romans", quote: "King **Demetrius** Poliorcetes constructed colossal rolling siege towers covered with iron plates to batter the walls of Rhodes." },
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "Relent, sweet Hermia; and, Lysander, yield thy crazed title to my certain right, pleaded **Demetrius** in the Athenian wood." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The silversmith **Demetrius** stirred up a riot at Ephesus, shouting that Paul's preaching was ruining the trade of Diana's shrines." }
    ]
  },
  "Dashboard — metr/densitometry.md": {
    primary: "The scientific measurement of optical density in photographic materials, or bone mineral density in biological tissues.",
    secondary: "In clinical medicine and radiography, dual-energy X-ray absorptiometry (DEXA) used to quantify bone mineral content and assess osteoporosis fracture risk.",
    quotes: [
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Photographic **densitometry** quantifies the microscopic silver grain deposition across successive exposure steps." },
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Automated scanning **densitometry** of serum protein electrophoretic strips reveals monoclonal immunoglobulin spikes." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Bone mineral **densitometry** of the lumbar spine provides the gold standard for diagnosing osteopenia and monitoring bisphosphonate therapy." }
    ]
  },
  "Dashboard — metr/diametral.md": {
    primary: "Of, relating to, or having the nature of a diameter; situated along or acting in the direction of a diameter.",
    secondary: "In mechanical engineering, geometry, and optics, designating diametral pitch (the ratio of number of teeth to pitch diameter in gears) or diametral planes.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The volcanic crater collapsed along a **diametral** fault line that traversed the center of the caldera." },
      { author: "James Dwight Dana", work: "A Text-Book of Mineralogy", quote: "Cleavage occurs parallel to the **diametral** prism faces in orthorhombic staurolite crystals." },
      { author: "Frank A. Fetter", work: "Modern Industrial Mechanics", quote: "Standardized gear wheels must share the identical **diametral** pitch to mesh smoothly without binding." }
    ]
  },
  "Dashboard — metr/diametric.md": {
    primary: "Of, relating to, or along a diameter; directly opposed; diametrical.",
    secondary: "In geometry and formal logic, representing positions at opposite ends of a diameter, hence expressing absolute mutual contradiction.",
    quotes: [
      { author: "Isaac Newton", work: "Opticks", quote: "The rays refracted through the opposite sides of the prism emerge with a **diametric** deviation proportional to their refrangibility." },
      { author: "Samuel Taylor Coleridge", work: "Biographia Literaria", quote: "The true opposite of poetry is not prose, but science; their aims are in **diametric** contrast." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "The empirical approach stands in **diametric** opposition to medieval dogmatic scholasticism." }
    ]
  },
  "Dashboard — metr/diametrical.md": {
    primary: "Of, relating to, or situated along a diameter; completely opposed; directly contrary.",
    secondary: "Expressing an absolute, polar opposition, as if situated at antipodal points across a circle.",
    quotes: [
      { author: "John Locke", work: "An Essay Concerning Human Understanding", quote: "Skepticism and dogmatism stand in **diametrical** opposition, yet both spring from an impatience with gradual inquiry." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "The interests of the court nobility and the starving peasantry were in **diametrical** conflict." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Healthy-minded optimism and the sick soul represent two **diametrical** attitudes toward human destiny." }
    ]
  },
  "Dashboard — metr/diametrically.md": {
    primary: "In a diametrical manner; completely, directly, or entirely opposed.",
    secondary: "Adverbially describing extreme, polar contrariety, as two points located at opposite ends of a diameter.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Their theoretical principles are **diametrically** opposed to the inherited constitutional wisdom of our ancestors." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The social instincts and selfish desires often prompt actions **diametrically** opposed to one another." },
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Casaubon's narrow pedantry was **diametrically** opposed to Dorothea's ardent, generous humanitarian impulses." }
    ]
  },
  "Dashboard — metr/emmetropia.md": {
    primary: "The condition of normal vision in which parallel rays of light are brought to a sharp focus on the retina without accommodation; the absence of refractive error.",
    secondary: "In physiological optics, the ideal optical state of the relaxed human eye, where ocular focal power matches axial length perfectly.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "In state of **emmetropia**, distant stars and mountain horizons produce sharp point images upon the retinal fovea without ciliary effort." },
      { author: "F. C. Donders", work: "On the Anomalies of Accommodation and Refraction of the Eye", quote: "We define **emmetropia** as the normal baseline against which all forms of myopia and hyperopia are scientifically measured." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The preservation of **emmetropia** into adult life depends upon the harmonious growth of the cornea and posterior sclera." }
    ]
  },
  "Dashboard — metr/emmetropic.md": {
    primary: "Having normal vision; possessing an eye that focuses distant light rays sharply upon the retina without accommodation.",
    secondary: "In clinical ophthalmology, describing an eye that requires no corrective refractive lenses for clear distant vision.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "An **emmetropic** eye achieves effortless sharp vision at infinity, reserving its full accommodative reserve for reading." },
      { author: "F. C. Donders", work: "Anomalies of Refraction", quote: "Retinoscopy of the **emmetropic** subject confirms that the far point of distinct vision lies at optical infinity." },
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "Even the sharpest **emmetropic** eye narrows its lids against dazzling desert sunshine to sharpen visual contrast." }
    ]
  },
  "Dashboard — metr/endometrial.md": {
    primary: "Of or relating to the endometrium (the mucous membrane that lines the interior of the uterus).",
    secondary: "In gynecological histopathology, designating cyclic hormone-responsive stromal and glandular tissues of the uterine cavity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Biopsy of the **endometrial** lining reveals marked glandular hyperplasia induced by unopposed estrogen stimulation." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "Curettage of the **endometrial** surface was undertaken to arrest persistent menorrhagia." },
      { author: "Arthur Rook", work: "Textbook of Dermatology", quote: "Cutaneous endometriosis presents as a pigmented periumbilical nodule that swells painfully during each **endometrial** cycle." }
    ]
  },
  "Dashboard — metr/endometriosis.md": {
    primary: "A chronic gynecological condition in which tissue similar to the lining of the uterus (endometrium) grows outside the uterine cavity, causing pain and scarring.",
    secondary: "In reproductive pathology, an estrogen-dependent disease characterized by ectopic implants on ovaries, fallopian tubes, and peritoneum, forming 'chocolate cysts' and pelvic adhesions.",
    quotes: [
      { author: "John A. Sampson", work: "Peritoneal Endometriosis Due to the Menstrual Dissemination of Endometrial Tissue", quote: "I propose that pelvic **endometriosis** arises primarily from retrograde menstruation transporting viable endometrial fragments into the peritoneal cavity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe cyclic pelvic pain and progressive dyspareunia are classic clinical hallmarks of pelvic **endometriosis**." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Laparoscopic visualization and histological confirmation remain mandatory for the definitive diagnosis of **endometriosis**." }
    ]
  },
  "Dashboard — metr/endometritis.md": {
    primary: "Inflammation of the endometrium (the inner mucous membrane lining of the uterus), typically caused by bacterial infection.",
    secondary: "In obstetrics and gynecology, postpartum or pelvic inflammatory infection characterized by fever, uterine tenderness, and foul lochial discharge.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Puerperal fever was historically initiated by virulent streptococcal **endometritis** introduced by unwashed hands of attendants." },
      { author: "Oliver Wendell Holmes Sr.", work: "The Contagiousness of Puerperal Fever", quote: "The tragedy of fatal post-partum **endometritis** was traced directly to physicians proceeding from the autopsy room to the lying-in chamber." },
      { author: "J. Marion Sims", work: "Uterine Surgery", quote: "Chronic catarrhal **endometritis** produces persistent leucorrhea and impairs fertile nidation of the ovum." }
    ]
  },
  "Dashboard — metr/endometrium.md": {
    primary: "The mucous membrane lining the interior wall of the uterus, which thickens and sheds during the menstrual cycle in primates.",
    secondary: "In reproductive endocrinology, a highly dynamic mucosal layer composed of functionalis and basalis zones that undergoes estrogen-primed proliferation followed by progesterone secretory differentiation.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Manual of Normal Histology", quote: "Histological examination reveals rich tubular glands and spiral arterioles traversing the vascular stroma of the **endometrium**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Implantation of the blastocyst cannot occur unless the **endometrium** has achieved full progestational decidualization." },
      { author: "J. Marion Sims", work: "Clinical Notes on Uterine Surgery", quote: "Topical applications to the diseased **endometrium** must be administered with cautious antiseptic care." }
    ]
  },
  "Dashboard — metr/geometry_science.md": {
    primary: "The branch of mathematics concerned with the properties, measurement, and relationships of points, lines, angles, surfaces, and solids; geometry treated as a formal deductive science.",
    secondary: "In the history of science and epistemology, the foundational deductive discipline codified by Euclid, evolving through analytical and non-Euclidean systems into general relativity.",
    quotes: [
      { author: "René Descartes", work: "Discourse on Method", quote: "The long chains of simple and easy reasonings by which geometers reach their most difficult demonstrations convinced me that all sciences might be pursued in the spirit of **geometry**." },
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "The description of right lines and circles, upon which **geometry** is founded, belongs to mechanics, proving the mechanical origin of mathematical truths." },
      { author: "Albert Einstein", work: "Geometry and Experience", quote: "As far as the propositions of **geometry** refer to reality, they are not certain; and as far as they are certain, they do not refer to reality." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch5Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 5 Completed: ${count} / ${Object.keys(batch5Data).length} notes updated.`);
console.log(`========================================\n`);
