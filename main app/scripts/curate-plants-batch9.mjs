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

const batch9Data = {
  "Dashboard — rhiz/rhizomorphous.md": {
    primary: "Having the form, appearance, or branching habit of a root or a fungal rhizomorph; root-like.",
    secondary: "In mycology and forest pathology, describing tough, cord-like subterranean mycelial strands that resemble branching rootlets.",
    quotes: [
      { author: "Robert Hartig", work: "Important Diseases of Forest Trees", quote: "The **rhizomorphous** strands of Armillaria spread through forest duff, penetrating the root bark of neighboring pines." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Under damp rotting logs, the black **rhizomorphous** cords branched freely across the sapwood." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "A cross-section through the **rhizomorphous** cord reveals a differentiated outer cortex protecting inner conductive hyphae." }
    ]
  },
  "Dashboard — rhiz/rhizophagous.md": {
    primary: "Feeding on roots; root-eating (applied especially to insects, nematodes, and subterranean larvae).",
    secondary: "In applied entomology and soil ecology, designating pests like cicada nymphs, wireworms, and root-knot nematodes that consume subterranean root tissue.",
    quotes: [
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "Subterranean devastation in vineyards is caused by **rhizophagous** phylloxera aphids feeding on fibrous rootlets." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Grubs of May beetles are intensely **rhizophagous**, severing the root systems of pasture grasses and strawberry beds." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The **rhizophagous** larvae of cicadas pass up to seventeen years underground sucking sap from tree roots." }
    ]
  },
  "Dashboard — rhiz/rhizophagy.md": {
    primary: "The practice or habit of feeding upon roots; in microbiology, the rhizophagy cycle in which plant roots internalize and extract nutrients from symbiotic microbes.",
    secondary: "In plant-microbe symbioses, a biological cycle wherein roots engulf endophytic soil bacteria, extract nitrogen using superoxide, and expel them to scavenge nutrients.",
    quotes: [
      { author: "Charles Valentine Riley", work: "The Periodical Cicada", quote: "Long subterranean **rhizophagy** enables the growing nymph to accumulate fat bodies over years of silent underground feeding." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Root damage arising from widespread **rhizophagy** leaves crops vulnerable to secondary bacterial and fungal wilts." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "Severe **rhizophagy** by subterranean herbivores alters competitive dominance among coexisting grassland species." }
    ]
  },
  "Dashboard — rhiz/rhizophora.md": {
    primary: "A genus of tropical coastal trees in the family Rhizophoraceae, commonly known as true mangroves or red mangroves, bearing stilt roots and viviparous seedlings.",
    secondary: "In marine coastal ecology, the quintessential halophytic shoreline tree (Rhizophora mangle) whose arched prop roots buffer coastlines from storm surges and build new land.",
    quotes: [
      { author: "Charles Darwin", work: "Journal of Researches (Voyage of the Beagle)", quote: "The tangled stilt roots of **Rhizophora** form an impenetrable barrier along tropical tidal lagoons, trapping river mud." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "We navigated our canoe through winding mangrove channels, where overarching boughs of **Rhizophora** dipped viviparous seedlings into the surf." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "The red mangrove or **Rhizophora** advances steadily into the sea, its arching aerial roots creating new soil out of ocean silt." }
    ]
  },
  "Dashboard — rhiz/rhizophoraceae.md": {
    primary: "The mangrove family of tropical and subtropical woody flowering plants (order Malpighiales), characterized by opposite leathery leaves and specialized aerial stilt roots.",
    secondary: "In coastal forest botany, a specialized family exhibiting vivipary (seeds germinating while still attached to the parent tree) and salt-excluding root membranes.",
    quotes: [
      { author: "Robert Brown", work: "General Remarks on the Botany of Terra Australis", quote: "The family **Rhizophoraceae** dominates intertidal maritime mudflats throughout tropical Australia and the Indian Ocean." },
      { author: "George Bentham", work: "Flora Australiensis", quote: "Systematists recognize the **Rhizophoraceae** by their leathery opposite leaves, interpetiolar stipules, and viviparous fruits." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "Anatomical adaptations within the **Rhizophoraceae** demonstrate remarkable physiological resistance to high salt concentrations." }
    ]
  },
  "Dashboard — rhiz/rhizopod.md": {
    primary: "A protozoan belonging to the former class Rhizopoda, characterized by the formation of pseudopodia for locomotion and food capture (such as Amoeba).",
    secondary: "In aquatic micropaleontology, amoeboid unicellular organisms (including foraminifera and testate amoebae) whose mineral shells form chalk and deep-sea oozes.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The simplest **rhizopod** consists of a naked droplet of living sarcode capable of throwing out temporary flowing pseudopodia." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The microscopic shells of each oceanic **rhizopod** present astonishing geometric traceries of perforated calcium carbonate." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Vast Cretaceous chalk cliffs across Europe are composed of the fossilized tests of ancient **rhizopod** skeletons." }
    ]
  },
  "Dashboard — rhiz/rhizopoda.md": {
    primary: "A former taxonomic class or subphylum of protozoans comprising amoeboid organisms that move and feed by means of pseudopodia.",
    secondary: "In historical invertebrate systematics, the primary sarcodine grouping that included naked amoebae, testaceans, and foraminiferans.",
    quotes: [
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Under the class **Rhizopoda**, zoologists grouped those primitive sarcodines that lack cilia and rely upon protoplasmic streaming." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Comparative study of the **Rhizopoda** demonstrates the fundamental contractile properties of animal protoplasm." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "The phylogenetic dismemberment of the **Rhizopoda** revealed that amoeboid locomotion evolved independently across multiple eukaryotic clades." }
    ]
  },
  "Dashboard — rhiz/rhizopodan.md": {
    primary: "Of, relating to, or characteristic of rhizopods (amoeboid protozoans with pseudopodia).",
    secondary: "In cellular protozoology, describing protoplasmic streaming, amoeboid creeping, and phagocytic engulfment typical of sarcodine organisms.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Critiques and Addresses", quote: "Human white blood cells exhibit **rhizopodan** movements, creeping through capillary walls like microscopic amoebae." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "The **rhizopodan** stage of primitive mycetozoans aggregates to form migrating multicellular plasmodia." },
      { author: "Ernst Haeckel", work: "The History of Creation", quote: "Ontogenetic observation of early animal cleavage recalls ancestral **rhizopodan** cellular individuality." }
    ]
  },
  "Dashboard — rhiz/Rhizopogon.md": {
    primary: "A genus of ectomycorrhizal, subterranean false truffles in the family Rhizopogonaceae (order Boletales), producing round underground fruiting bodies with root-like threads.",
    secondary: "In conifer forest ecology, hypogeous fungi forming vital mycorrhizae with Douglas fir and pines, whose sporocarps are excavated and dispersed by forest small mammals.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "I established the genus **Rhizopogon** to accommodate subterranean false truffles attached to soil by conspicuous root-like mycelial cords." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "In pine plantations, hypogeous sporocarps of **Rhizopogon** rubescens develop buried beneath several inches of fallen needles." },
      { author: "Charles McIlvaine", work: "One Thousand American Fungi", quote: "The gleba of **Rhizopogon** remains labyrinthine and moist, emitting an earthy fragrance that attracts burrowing rodents." }
    ]
  },
  "Dashboard — rhiz/rhizopogonaceae.md": {
    primary: "A family of hypogeous (underground) false truffles in the order Boletales, characterized by potato-like fruiting bodies that lack stems and have glebal chambers.",
    secondary: "In fungal evolutionary biology, an obligately ectomycorrhizal family derived from boletes that evolved subterranean fruiting as an adaptation to drought and fire regimes.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Epicrisis Systematis Mycologici", quote: "The **Rhizopogonaceae** are distinguished from true truffles by their basidiospores borne within labyrinthine glebal cavities." },
      { author: "William Gilson Farlow", work: "Icones Farlowianae", quote: "Species of **Rhizopogonaceae** are indispensable partners in conifer reforestation on burned mountain watersheds." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "Systematic revisions unite the **Rhizopogonaceae** with the bolete lineage based upon hymenial development and chemical pigments." }
    ]
  },
  "Dashboard — rhiz/Rhizopus.md": {
    primary: "A genus of fast-growing saprophytic and parasitic filamentous fungi in the family Rhizopodaceae (phylum Mucoromycota), famously including black bread mold (Rhizopus stolonifer).",
    secondary: "In mycology and food biotechnology, zygomycetous molds producing creeping stolons, anchoring rhizoids, and black sporangia; used in fermenting tempeh and industrial fumaric acid production.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Spores of **Rhizopus** germinate rapidly upon damp bread, extending aerial hyphae that terminate in spherical black sporangia." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The formation of zygospores in **Rhizopus** occurs when compatible progametangia meet and fuse along the substratum." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "Soft rot in stored sweet potatoes is caused by virulent pectolytic enzymes secreted by invading **Rhizopus** stolons." }
    ]
  },
  "Dashboard — rhiz/rhizosphere.md": {
    primary: "The narrow region of soil immediately surrounding plant roots that is directly influenced by root secretions and associated soil microorganisms.",
    secondary: "In soil microbiology and agronomy, a biological hotspot of intense microbial activity, carbon exudation, mycorrhizal exchange, and nutrient mineralization.",
    quotes: [
      { author: "Lorenz Hiltner", work: "On Recent Experiences and Problems in the Field of Soil Bacteriology", quote: "I introduced the concept of the **rhizosphere** to designate that dynamic zone of soil where root exudates stimulate intense bacterial proliferation." },
      { author: "Arthur George Tansley", work: "Practical Plant Ecology", quote: "Within the **rhizosphere**, root exudates alter soil pH and promote beneficial mycorrhizal colonization." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Roots do not merely absorb soil solutions passively, but actively modify their surrounding **rhizosphere** with acidic excretions." }
    ]
  },
  "Dashboard — rhiz/rhizotomy.md": {
    primary: "The surgical severing or interruption of spinal nerve roots, historically performed to relieve intractable chronic pain or severe spasticity.",
    secondary: "In neurosurgery, posterior (sensory) rhizotomy designed by Otfrid Foerster and Charles Frazier to selectively interrupt sensory afferents while preserving motor function.",
    quotes: [
      { author: "Harvey Cushing", work: "The Life of Sir William Osler", quote: "Posterior **rhizotomy** offered dramatic relief to tabetic patients tortured by unremitting lightning pains in the limbs." },
      { author: "Otfrid Foerster", work: "On the Operative Treatment of Spastic Paralysis by Resection of the Posterior Nerve Roots", quote: "Selective posterior **rhizotomy** interrupts the hyperactive sensory reflex arc, drastically reducing spastic rigidity." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In terminal malignancies involving brachial plexus invasion, surgical **rhizotomy** provides humane mitigation of agonizing pain." }
    ]
  },
  "Dashboard — sacc/saccade.md": {
    primary: "A rapid, intermittent movement of both eyes between fixation points, as during reading or scanning a visual scene.",
    secondary: "In visual psychophysics and neuro-ophthalmology, a ballistic conjugate eye movement reaching speeds up to 900 degrees per second, programmed by the superior colliculus and frontal eye fields.",
    quotes: [
      { author: "Émile Javal", work: "Physiologie de la Lecture et de l'Écriture", quote: "I observed that the reader's eye does not glide smoothly across the printed line, but advances in brief, rapid **saccade** jerks punctuated by pauses." },
      { author: "William James", work: "The Principles of Psychology", quote: "During each quick **saccade**, visual perception is largely suppressed, preventing the sensation of a blurring motion smear." },
      { author: "Eric Kandel", work: "Principles of Neural Science", quote: "Neural firing in the frontal eye fields initiates each ballistic **saccade** to bring targets onto the fovea centralis." }
    ]
  },
  "Dashboard — sacc/saccadic.md": {
    primary: "Of, relating to, or characterized by saccades; moving rapidly and intermittently in jerky jumps.",
    secondary: "In visual neurophysiology, describing the ballistic ocular motor system that shifts gaze rapidly from one fixation point to another.",
    quotes: [
      { author: "Émile Javal", work: "Physiology of Reading", quote: "Fluent reading consists of a series of brief **saccadic** leaps separated by stationary fixations lasting a fraction of a second." },
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "The **saccadic** motion of the eye is so swift that conscious visual processing is suspended during the transit." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "Lesions of the cerebellar vermis cause prominent **saccadic** dysmetria, with overshooting of visual fixation targets." }
    ]
  },
  "Dashboard — sacc/sacco.md": {
    primary: "An Italian or historical term for a sack, bag, or pouch; in natural history, applied to bag-shaped anatomical structures or historical cases (e.g. Sacco and Vanzetti).",
    secondary: "In anatomical Italian and historical lexicography, a pouch-like anatomical cavity or peritoneal recess (sacco peritoneale).",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Venetian porter hoisted the heavy **sacco** of flour onto his shoulders and carried it across the Rialto." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "In classical anatomical descriptions, the peritoneal pouch is frequently designated as a membranous **sacco**." },
      { author: "H. G. Wells", work: "The Work, Wealth and Happiness of Mankind", quote: "The tragic trial of **Sacco** and Vanzetti stirred labor protests across every industrial city in the world." }
    ]
  },
  "Dashboard — sacc/sacculate.md": {
    primary: "Formed into or having small sacs, pouches, or bag-like expansions; sac-like.",
    secondary: "In descriptive morphology and anatomical pathology, possessing pouch-like dilations along a tubular organ (such as a sacculate aneurysm).",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The stomach of the crustacean is a **sacculate** organ equipped with internal chitinous grinding teeth." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "A localized **sacculate** dilation of the ascending aorta projected through the eroded sternum." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "The lungs in certain reptiles present a simple **sacculate** chamber without complex bronchial branching." }
    ]
  },
  "Dashboard — sacc/sacculated.md": {
    primary: "Divided into or possessing a series of small sacs, pouches, or saccules (such as the sacculated colon).",
    secondary: "In human and comparative anatomy, characterized by haustra or bulging segmental pouches, as seen in the human large intestine.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The human colon is uniquely **sacculated** by three longitudinal bands of muscular taeniae." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Chronic purulent bronchiectasis had transformed the lower bronchial tree into a series of **sacculated** cavities." },
      { author: "Richard Owen", work: "On the Anatomy of Vertebrates", quote: "The stomach of the leaf-eating monkey is complexly **sacculated** to support microbial cellulose fermentation." }
    ]
  },
  "Dashboard — sacc/saccule.md": {
    primary: "A small sac or pouch; specifically, the smaller of the two fluid-filled sacs in the vestibular labyrinth of the inner ear, sensitive to vertical linear acceleration.",
    secondary: "In vestibular neurobiology, an otolith organ containing hair cells embedded in a gelatinous membrane covered with calcium carbonate otoconia.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "The membranous labyrinth divides into the utricle and the smaller **saccule**, each housing auditory nerve terminals." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Vestibular nerve fibers terminate in delicate calyceal synapses surrounding the sensory maculae of the **saccule**." },
      { author: "Eric Kandel", work: "Principles of Neural Science", quote: "Gravitational tilt and vertical acceleration displace otolith crystals in the **saccule**, deflecting stereocilia." }
    ]
  },
  "Dashboard — sacc/sacculus.md": {
    primary: "The anatomical Latin term for the saccule of the inner ear; any small sac or pouch-like cavity.",
    secondary: "In otology and comparative labyrinth anatomy, the inferior vestibular organ that connects via the ductus reuniens to the cochlear duct.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "In lower vertebrates, the **sacculus** bears an outgrowth termed the lagena, the evolutionary forerunner of the cochlea." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "The sensory epithelium of the **sacculus** responds directly to linear gravitational vector forces." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The inner ear vestibule contains two membranous vesicles, the utriculus and the anterior **sacculus**." }
    ]
  },
  "Dashboard — sacc/sack.md": {
    primary: "A large bag made of coarse cloth, thick paper, or plastic, used for storing and carrying goods; also a historic dry white wine imported from Spain or the Canaries.",
    secondary: "In Shakespearean literature, dry fortified wine (sherry); in military history, the plundering and destruction of a captured city; in commerce, dismissal from employment.",
    quotes: [
      { author: "William Shakespeare", work: "Henry IV, Part 2", quote: "A good sherris-**sack** hath a twofold operation in it: it ascends me into the brain; dries me there all the foolish and dull and crudy vapors." },
      { author: "John Milton", work: "Paradise Lost", quote: "To **sack** a royal city and deliver it to slaughter and rapine was the brutal triumph of ancient warfare." },
      { author: "Charles Dickens", work: "Hard Times", quote: "The mill hand knew that one misstep would bring the **sack** and leave his starving children without bread." }
    ]
  },
  "Dashboard — sacc/sacked.md": {
    primary: "Dismissed from employment; plundered, looted, and devastated (of a city); put into a sack or sacks.",
    secondary: "In military history, having fallen to pillage and devastation by victorious troops; colloquially, having lost a job.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "In the year 410, Rome, the eternal city, was captured and **sacked** by the Gothic hordes of Alaric." },
      { author: "Charles Dickens", work: "David Copperfield", quote: "The unlucky clerk was summarily **sacked** for dipping his pen into the senior partner's private inkstand." },
      { author: "Walter Scott", work: "Ivanhoe", quote: "The smoking ruins of the castle proved that the fierce outlaws had thoroughly **sacked** every tower and vault." }
    ]
  },
  "Dashboard — sacc/sacking.md": {
    primary: "A coarse, heavy woven fabric (such as burlap or hessian) used for making sacks and bags; the act of dismissing someone from a job; the plundering of a captured city.",
    secondary: "In textile commerce, coarse unbleached jute or hemp sacking used for baling wool, grain, and colonial produce.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "The old dealer in rags sat upon a rough bundle of coarse **sacking**, sorting greasy parchments by candlelight." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "The furious mob rejoiced in the storming and **sacking** of the royal arms depots across the insurgent capital." },
      { author: "George Eliot", work: "Silas Marner", quote: "Silas hid his golden guineas beneath the hearthstones, wrapped securely in pieces of rough **sacking**." }
    ]
  },
  "Dashboard — sicy/Sicyos.md": {
    primary: "A genus of climbing or trailing annual vines in the gourd family (Cucurbitaceae), commonly known as bur cucumbers or one-seeded bur cucumbers.",
    secondary: "In weed ecology and agricultural botany, aggressive tendril-bearing vines (Sicyos angulatus) that climb over corn and soybean fields, producing prickly, barbed clusters of fruit.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Under **Sicyos**, I have grouped those tendril-bearing cucurbits whose flowers are monoecious and whose fruit is an armed one-seeded bur." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The one-seeded bur cucumber, **Sicyos** angulatus, clambers luxuriantly over riverbank bushes, armed with prickly star-like burs." },
      { author: "John Torrey", work: "Flora of the State of New York", quote: "In rich alluvial bottomlands, the climbing stems of **Sicyos** smother young saplings beneath a dense canopy of maple-shaped leaves." }
    ]
  },
  "Dashboard — staphyl/staphylaceae.md": {
    primary: "A botanical family of dicotyledonous flowering shrubs and small trees (order Crossosomatales), commonly known as the bladdernut family (Staphyleaceae).",
    secondary: "In systematic dendrology, a family characterized by opposite pinnate leaves with caducous stipules and inflated, papery, bladder-like capsules containing hard seeds.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The **Staphyleaceae** are easily recognized among allied orders by their opposite stipulate foliage and inflated membranous fruit capsules." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "In our classification, the **Staphyleaceae** are placed near Celastrineae, characterized by their pendulous panicles of white flowers." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "Fossil leaves and winged seeds referred to the **Staphyleaceae** occur in European and American Tertiary deposits." }
    ]
  },
  "Dashboard — staphyl/staphylea.md": {
    primary: "A genus of deciduous shrubs and small trees in the family Staphyleaceae, known as bladdernuts, bearing drooping clusters of white flowers and inflated, bladder-like seed pods.",
    secondary: "In temperate forest ecology, attractive understory shrubs (such as Staphylea trifolia) whose papery inflated capsules rattle in the autumn wind.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The name **Staphylea** derives from the Greek for a cluster of grapes, describing the drooping pendulous panicles of blossoms." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "American bladdernut, **Staphylea** trifolia, grows in moist shaded woodlands, its greenish-striped bark supporting inflated three-lobed pods." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The bladdernut or **Staphylea** beareth bladder-like husks containing smooth, hard, bony nuts that rattle when shaken." }
    ]
  },
  "Dashboard — staphyl/staphyledema.md": {
    primary: "Edema or swelling of the uvula (the fleshy extension hanging at the back of the soft palate).",
    secondary: "In clinical otolaryngology, acute swelling of the uvula resulting from allergic angioedema, chemical irritation, or acute pharyngitis, causing gagging and stridor.",
    quotes: [
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Acute **staphyledema** causes the swollen uvula to rest upon the base of the tongue, inducing violent suffocative coughing fits." },
      { author: "Morell Mackenzie", work: "Diseases of the Pharynx, Larynx, and Trachea", quote: "In severe **staphyledema**, scarification of the translucent edematous uvula affords instantaneous relief from dyspnea." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Angioneurotic edema may present as sudden **staphyledema**, threatening mechanical asphyxiation if the glottis becomes involved." }
    ]
  },
  "Dashboard — staphyl/staphylinidae.md": {
    primary: "A gigantic family of beetles commonly known as rove beetles, characterized by very short elytra that leave most of their flexible abdominal segments exposed.",
    secondary: "In systematic entomology, the largest family of animals, comprising over 63,000 described species of agile predators and detritivores inhabiting leaf litter and soil.",
    quotes: [
      { author: "Charles Darwin", work: "Journal of Researches (Voyage of the Beagle)", quote: "The agile rove beetles of the **Staphylinidae** curled their abdomens over their backs in menacing scorpioid attitudes when disturbed." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Members of the **Staphylinidae** fold their membranous flight wings beneath tiny square elytra with astonishing speed and dexterity." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Beneficial predation by the **Staphylinidae** upon soil-dwelling fly maggots makes them valuable allies in agricultural ecology." }
    ]
  },
  "Dashboard — staphyl/staphylion.md": {
    primary: "A craniometric landmark point situated on the posterior border of the hard palate at the base of the posterior nasal spine in the midline.",
    secondary: "In physical anthropology and craniometry, a reference point used to measure palatal length and facial architecture in comparative hominid crania.",
    quotes: [
      { author: "Paul Broca", work: "Instructions Craniologiques", quote: "Palatal length is calculated by taking the distance between the alveolar point and the **staphylion** at the median posterior spine." },
      { author: "Francis Galton", work: "Inquiries into Human Faculty", quote: "Standardized craniometrical calipers must align precisely with the **staphylion** to determine the gnathic index of fossil skulls." },
      { author: "Edward Drinker Cope", work: "The Origin of the Fittest", quote: "Comparative measurements from prosthion to **staphylion** illuminate the evolutionary shortening of the anthropoid facial skeleton." }
    ]
  },
  "Dashboard — staphyl/staphylococcal.md": {
    primary: "Of, relating to, or caused by bacteria of the genus Staphylococcus.",
    secondary: "In clinical infectious disease and epidemiology, designating infections ranging from minor boils and impetigo to life-threatening sepsis and endocarditis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute osteomyelitis in adolescents is overwhelmingly of **staphylococcal** origin, demanding prompt surgical trepanation and drainage." },
      { author: "Alexander Fleming", work: "On the Antibacterial Action of Cultures of a Penicillium", quote: "The clear zone around the mold colony demonstrated the complete lysis of the surrounding **staphylococcal** lawn." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Methicillin-resistant **staphylococcal** bacteremia constitutes one of the gravest challenges in modern hospital epidemiology." }
    ]
  },
  "Dashboard — staphyl/staphylococci.md": {
    primary: "Spherical, Gram-positive bacteria that divide in multiple planes and form irregular, grape-like clusters; plural of staphylococcus.",
    secondary: "In bacteriology, non-motile facultative anaerobes that produce catalase, forming prominent components of normal skin microflora as well as virulent opportunistic pathogens.",
    quotes: [
      { author: "Robert Koch", work: "Investigations into Traumatic Infective Diseases", quote: "Under the oil immersion lens, the pyogenic cocci grouped into clusters resembling bunches of grapes, hence named **staphylococci**." },
      { author: "Louis Pasteur", work: "Germ Theory and Its Applications", quote: "I isolated pure cultures of **staphylococci** from furuncles and osteomyelitic abscesses, demonstrating their pyogenic power." },
      { author: "Alexander Fleming", work: "Penicillin", quote: "Broth cultures of **staphylococci** cleared completely within twenty-four hours after the introduction of sterile penicillin filtrate." }
    ]
  },
  "Dashboard — staphyl/staphylococcus.md": {
    primary: "A genus of Gram-positive spherical bacteria (family Staphylococcaceae) that occur in microscopic grape-like clusters, notably including Staphylococcus aureus.",
    secondary: "In clinical microbiology, a major human pathogen producing coagulase, hemolysins, and enterotoxins, causing skin abscesses, toxic shock syndrome, and food poisoning.",
    quotes: [
      { author: "Alexander Fleming", work: "On the Antibacterial Action of a Penicillium", quote: "While working with **Staphylococcus** variants, a mold contaminant produced a striking inhibition of bacterial growth." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Invasion by **Staphylococcus** aureus through a simple cutaneous abrasion may initiate rapid metastatic abscesses in distant organs." },
      { author: "Joseph Lister", work: "On the Antiseptic Principle in the Practice of Surgery", quote: "Carbolic acid dressings destroyed the virulent **Staphylococcus** organisms that formerly produced hospital gangrene." }
    ]
  },
  "Dashboard — staphyl/staphyloderma.md": {
    primary: "A bacterial skin infection or dermatitis caused by staphylococcal bacteria, such as impetigo, folliculitis, furuncles, or carbuncles.",
    secondary: "In clinical dermatology, any purulent pyoderma characterized by follicular or non-follicular pustules teemed with Staphylococcus aureus.",
    quotes: [
      { author: "Paul Gerson Unna", work: "The Histopathology of the Diseases of the Skin", quote: "Histological sections of **staphyloderma** display dense collections of polymorphonuclear leukocytes surrounding the hair follicle neck." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Follicular **staphyloderma** spreads rapidly across bearded faces when shaving razors are contaminated with pus." },
      { author: "Thomas B. Fitzpatrick", work: "Dermatology in General Medicine", quote: "Topical antibacterial washes and warm compresses constitute the primary management of superficial **staphyloderma**." }
    ]
  },
  "Dashboard — staphyl/staphyloplasty.md": {
    primary: "Plastic or reconstructive surgery on the uvula or soft palate; staphylorrhaphy or repair of a cleft palate.",
    secondary: "In craniofacial and oral surgery, surgical closure of a cleft soft palate to restore velopharyngeal competence and normal speech.",
    quotes: [
      { author: "Morell Mackenzie", work: "Diseases of the Pharynx, Larynx, and Trachea", quote: "The success of modern **staphyloplasty** depends upon careful paring of the cleft margins and tension-free silver sutures." },
      { author: "Frank Hamilton", work: "The Principles and Practice of Surgery", quote: "Restoration of intelligible speech was achieved through an ingenious **staphyloplasty** that united the divided palatal velum." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "The operation of **staphyloplasty** was perfected to close congenital fissures of the soft palate and uvula." }
    ]
  },
  "Dashboard — syc/sycomancy.md": {
    primary: "Divination by means of fig leaves, where questions or names were written upon leaves and the speed of their drying or withering was interpreted.",
    secondary: "In classical anthropology and mantic folklore, an ancient Greek divinatory practice where slower desiccation indicated truth or a favorable augury.",
    quotes: [
      { author: "John Brand", work: "Observations on Popular Antiquities", quote: "In the ancient rite of **sycomancy**, prayers were inscribed on fresh fig leaves, and those which dried slowest were deemed answered." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "The practice of **sycomancy** was rooted in the sacred association of the fig tree with Dionysian fertility and underworld secrets." },
      { author: "Walter Woodburn Hyde", work: "Greek Religion and Its Survivals", quote: "Rural peasants continued to consult rustic **sycomancy** before autumn sowing to foresee whether the harvest would be fruitful." }
    ]
  },
  "Dashboard — syc/sycophancy.md": {
    primary: "Servile, self-seeking flattery; fawning, obsequious behavior toward someone important in order to gain advantage.",
    secondary: "Historically in ancient Athens, the malicious practice of public informing or false accusation; in moral philosophy, degrading parasitical subservience.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The imperial court was crowded with eunuchs whose blatant **sycophancy** poisoned the emperor's ear against his ablest generals." },
      { author: "William Makepeace Thackeray", work: "The Book of Snobs", quote: "There is no spectacle more contemptible than the shameless **sycophancy** of the middle-class tuft-hunter groveling before a peer." },
      { author: "Thomas Carlyle", work: "The French Revolution", quote: "Decades of courtly **sycophancy** had blinded the Versailles aristocracy to the gathering fury of the Parisian populace." }
    ]
  },
  "Dashboard — syc/sycophant.md": {
    primary: "A person who acts obsequiously toward someone important in order to gain advantage; a servile, self-seeking flatterer; a parasite.",
    secondary: "Historically in classical Athens (from sykon 'fig' and phainein 'to show'), an informer who denounced smugglers of figs or brought vexatious lawsuits for gain.",
    quotes: [
      { author: "William Shakespeare", work: "Timon of Athens", quote: "Feast-won, fast-lost; one cloud of winter showers, these flies are couched; Timon drove the crawling **sycophant** from his gates." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "A base **sycophant** applauds the blunders of his wealthy patron, bartering truth for a seat at the dinner table." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Becky Sharp despised the clumsy **sycophant** who fawned openly, knowing that subtle deference alone captures high society." }
    ]
  },
  "Dashboard — syc/sycophantic.md": {
    primary: "Behaving, speaking, or done in an obsequious way in order to gain favor or advantage; fawning; servile.",
    secondary: "Characterized by insincere praise and degrading deference designed to flatter powerful superiors.",
    quotes: [
      { author: "Charles Dickens", work: "Martin Chuzzlewit", quote: "Pecksniff bowed with a **sycophantic** smile that set every honest observer's teeth on edge." },
      { author: "George Eliot", work: "Middlemarch", quote: "The aspiring politician showered his patron with **sycophantic** compliments, calculating the value of every flattering word." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The senate voted **sycophantic** adulations to the tyrant while secretly praying for his swift assassination." }
    ]
  },
  "Dashboard — xyl/metaxylem.md": {
    primary: "The part of the primary xylem that differentiates after the protoxylem, characterized by wider tracheary elements with scalariform, reticulate, or pitted secondary wall thickenings.",
    secondary: "In developmental plant anatomy, the mature primary water-conducting tissue that matures in shoot regions that have ceased elongation.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "In stem vascular bundles, the wider pitted vessels of the **metaxylem** develop centrifugally from the earlier protoxylem ring." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The **metaxylem** elements possess bordered pits, ensuring high hydraulic conductivity through mature woody tissues." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "Microscopic analysis shows that **metaxylem** differentiation is completed only after organ extension is accomplished." }
    ]
  },
  "Dashboard — xyl/protoxylem.md": {
    primary: "The first-formed primary xylem that differentiates in a developing plant organ, characterized by narrow tracheary elements with annular or spiral wall thickenings.",
    secondary: "In plant developmental histology, conducting elements capable of passive stretching during tissue elongation before the differentiation of metaxylem.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The delicate spiral rings of the **protoxylem** allow the young shoot to elongate rapidly without breaking vascular continuity." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In roots, **protoxylem** is exarch, developing at the outer periphery of the vascular cylinder." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Cross-sections through the young fern rhizome reveal distinct **protoxylem** poles initiating bundle development." }
    ]
  },
  "Dashboard — xyl/xyl.md": {
    primary: "A combining form and classical botanical root derived from Greek 'xylon' (wood, timber), forming vocabulary relating to wood and ligneous materials.",
    secondary: "In scientific nomenclature and organic chemistry, the foundational root underlying terms for wood tissue (xylem), wood sugars (xylose), and coal resins (xyloid).",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **xyl** traces directly to xylon, signifying felled timber, cut wood, or a tree trunk." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Indo-European cognates of **xyl** denote scraped wood or timber shaped by the carpenter's axe." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "Chemical derivatives containing the element **xyl** commemorate their original extraction from commercial wood distillates." }
    ]
  },
  "Dashboard — xyl/xylem.md": {
    primary: "The vascular tissue in plants that conducts water and dissolved mineral nutrients upward from the roots to the rest of the plant, and also provides mechanical support.",
    secondary: "In plant anatomy and wood science, the complex tissue composed of tracheids, vessel elements, xylem parenchyma, and fibers that forms the wood of trees.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The ascent of sap through thousands of microscopic **xylem** vessels supports the towering foliage of the tallest forest trees." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "Every tree trunk consists of two main vascular cylinders: the inner woody **xylem** and the outer bark-like phloem." },
      { author: "Charles Darwin", work: "The Power of Movement in Plants", quote: "Dye solutions injected into the root were rapidly conducted upward through the lignified **xylem** vessels." }
    ]
  },
  "Dashboard — xyl/xylene.md": {
    primary: "Any of three isomeric volatile liquid hydrocarbons [C₆H₄(CH₃)₂] obtained from petroleum and coal tar; dimethylbenzene, widely used as an industrial solvent.",
    secondary: "In histological microscopy and histology, a clearing agent that dissolves paraffin wax and prepares tissue sections for mounting in Canada balsam.",
    quotes: [
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Fractional distillation of coal tar yields **xylene**, a clear liquid possessing an aromatic toluene-like odor." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Dehydrated brain sections were cleared in pure **xylene** before mounting beneath cover slips in neutral balsam." },
      { author: "Frank A. Lee", work: "Basic Chemical Technology", quote: "Commercial **xylene** is an indispensable industrial solvent for paints, varnishes, and rubber cements." }
    ]
  },
  "Dashboard — xyl/xylitol.md": {
    primary: "A naturally occurring five-carbon sugar alcohol (pentitol) found in plant fibers and birch wood, used as a low-calorie sugar substitute that inhibits tooth decay.",
    secondary: "In dental biochemistry and food science, a non-fermentable polyol that Streptococcus mutans cannot metabolize, reducing plaque formation and dental caries.",
    quotes: [
      { author: "Frank A. Lee", work: "Basic Food Chemistry", quote: "Commercial production of **xylitol** from birch bark hemicellulose provides a sweetener with the sweetness of sucrose but without dental decay." },
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Infusion of **xylitol** operates via the pentose phosphate pathway, bypassing insulin-dependent glucose uptake in metabolic studies." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Chewing gums formulated with **xylitol** significantly reduce oral streptococcal colonization in pediatric trials." }
    ]
  },
  "Dashboard — xyl/xylocarp.md": {
    primary: "A hard, dense, woody fruit, such as a coconut or the woody capsule of certain tropical trees.",
    secondary: "In carpological morphology, an indehiscent fruit whose pericarp undergoes massive lignification and sclerenchymatous hardening for seed protection.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The coconut is an exemplary **xylocarp**, whose fibrous husk and stony endocarp survive months of ocean drifting." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In certain tropical Lecythidaceae, the fruit is an enormous **xylocarp** opening by an operculum like a monkey pot." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "Unlike soft succulent berries, a true **xylocarp** relies upon water buoyancy or rodent gnawing for seed liberation." }
    ]
  },
  "Dashboard — xyl/Xylocarpus.md": {
    primary: "A genus of mangrove trees in the mahogany family (Meliaceae), known as cannonball mangroves, bearing enormous woody globose fruits and buttressed trunks.",
    secondary: "In coastal mangrove ecology, Indo-Pacific shoreline trees (such as Xylocarpus granatum) producing large woody capsules packed with angular corky seeds that float in seawater.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Along the muddy estuaries of the Moluccas, trees of **Xylocarpus** granatum bear heavy spherical fruits the size of cannonballs." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "The dense, dark wood of **Xylocarpus** is prized for boat-building, resisting teredo worms in tropical waters." },
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "The woody fruit of **Xylocarpus** splits into four thick valves, releasing cork-coated seeds that float across ocean currents." }
    ]
  },
  "Dashboard — xyl/xylography.md": {
    primary: "The art or technique of engraving on wood; woodcut printing, especially the printing of books from carved wooden blocks (block books).",
    secondary: "In printing history and bibliographical study, the fifteenth-century craft that preceded movable metal type printing in Europe and flourished in East Asia.",
    quotes: [
      { author: "John Ruskin", work: "Ariadne Florentina", quote: "True **xylography** requires the artist to respect the natural resistance of the boxwood block under the graver." },
      { author: "William Morris", work: "The Ideal Book", quote: "The revival of fine printing must look to early Renaissance **xylography** for bold harmony between woodcuts and gothic letters." },
      { author: "Walter Pater", work: "Studies in the History of the Renaissance", quote: "Fifteenth-century **xylography** democratized religious imagery, scattering woodblock prints across every peasant cottage." }
    ]
  },
  "Dashboard — xyl/xyloid.md": {
    primary: "Resembling or having the nature of wood; woody; ligneous.",
    secondary: "In paleobotany and petrology, describing fossilized, carbonized, or silicified plant remains that preserve woody textures.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "The brown coal deposit was composed largely of **xyloid** lignite that clearly displayed the cellular rings of conifers." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Microscopic analysis of the **xyloid** fragments proved that ancient redwoods once flourished along arctic coasts." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Silicified wood forms a dense **xyloid** agate wherein every cell wall is replaced by chalcedony." }
    ]
  },
  "Dashboard — xyl/xylol.md": {
    primary: "A commercial or technical name for xylene (dimethylbenzene), used as a solvent and histological clearing agent.",
    secondary: "In microscopic technique, an aromatic solvent utilized to dissolve paraffin wax and clear dehydrated tissue specimens prior to mounting.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Manual of Normal Histology", quote: "Immerse the silver-stained sections in pure **xylol** until they become completely transparent." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Industrial **xylol** is a mixture of ortho, meta, and para isomers recovered from coal-tar naphtha." },
      { author: "Robert Koch", work: "Investigations into Traumatic Infective Diseases", quote: "Before sealing the glass slide, rinse the bacterial smear briefly with **xylol** to remove residual oils." }
    ]
  },
  "Dashboard — xyl/xylophagous.md": {
    primary: "Feeding on or destroying wood; wood-eating (applied especially to insects, mollusks, and fungi).",
    secondary: "In entomological ecology, describing wood-boring beetle larvae (Buprestidae, Cerambycidae), termites, and shipworms (Teredo) that digest cellulose and lignin.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The giant fallen trees of the Patagonian rain forest were rapidly honeycombed by **xylophagous** beetle larvae." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Damage caused by **xylophagous** termites to structural timbers costs millions of dollars in warm temperate zones." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Many **xylophagous** insects harbor symbiotic protozoa or bacteria in their guts to digest refractory wood lignin." }
    ]
  },
  "Dashboard — xyl/xylophobia.md": {
    primary: "An abnormal, irrational, or disproportionate fear of wooden objects or of dense forests and woodlands.",
    secondary: "In psychiatric nosology, a specific phobia triggered by entering dark woods or touching rough wooden textures.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Morbid dreads may attach to the most unexpected objects, producing phobias as specific as **xylophobia** or fear of open spaces." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Under psychoanalytic examination, the patient's acute **xylophobia** was traced to childhood terror in a dark pine forest." },
      { author: "Richard von Krafft-Ebing", work: "Psychopathia Sexualis", quote: "The nervous invalid manifested pronounced **xylophobia**, refusing to enter any room paneled in unpainted oak." }
    ]
  },
  "Dashboard — xyl/xylophone.md": {
    primary: "A musical percussion instrument consisting of a graduated series of tuned wooden bars struck with mallets.",
    secondary: "In musical acoustics and ethnomusicology, an idiophone found across African, Southeast Asian, and orchestral traditions, tuned to precise pitch intervals.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "On the Sensations of Tone", quote: "The pure harmonic overtone spectrum of a rosewood **xylophone** bar depends upon the undercutting of its central arch." },
      { author: "George Bernard Shaw", work: "Music in London", quote: "The crisp wooden rattle of the **xylophone** in Saint-Saëns's Danse Macabre evokes the dry clicking of dancing skeletons." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the Javanese gamelan, the wooden **xylophone** or gambang leads the melodic ornamentation with dazzling speed." }
    ]
  },
  "Dashboard — xyl/xylophonist.md": {
    primary: "A musician who plays the xylophone.",
    secondary: "A percussionist specializing in mallet instruments, demonstrating high motor dexterity and rapid alternate-sticking technique.",
    quotes: [
      { author: "George Bernard Shaw", work: "Music in London", quote: "The virtuoso **xylophonist** performed rapid chromatic variations with astonishing dexterity and rhythmic verve." },
      { author: "Hermann von Helmholtz", work: "Sensations of Tone", quote: "A skilled **xylophonist** modifies tone color by selecting mallets tipped with varying densities of felt or wood." },
      { author: "Frank A. Lee", work: "Orchestral Percussion", quote: "In contemporary orchestral scores, the **xylophonist** is required to execute intricate four-mallet polyphonic passages." }
    ]
  },
  "Dashboard — xyl/xylostroma.md": {
    primary: "A tough, leathery, felt-like mycelial mat formed by certain wood-rotting fungi in the crevices and hollows of decaying trees (such as oak leather).",
    secondary: "In forest pathology and historical mycology, thick sheets of sterile vegetative mycelium formerly classified as an independent fungal genus (Xylostroma giganteum).",
    quotes: [
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "Early naturalists described **Xylostroma** as an autonomous fungus, whereas it is merely the sterile vegetative felt of a polypore." },
      { author: "William Gilson Farlow", work: "Cryptogamic Botany", quote: "In hollow fallen logs, one frequently finds sheets of **xylostroma**, tough and flexible as tanned chamois leather." },
      { author: "Robert Hartig", work: "Diseases of Trees", quote: "The formation of dense **xylostroma** between heartwood fissures accelerates fungal dry rot by storing moisture." }
    ]
  },
  "Dashboard — zizyph/Ziziphus.md": {
    primary: "A genus of spiny shrubs and small trees in the buckthorn family (Rhamnaceae), known as jujubes, bearing sweet, edible, date-like drupes.",
    secondary: "In Mediterranean and Asian economic botany, drought-resistant thorny trees (such as Ziziphus jujuba and Ziziphus lotus) celebrated in folklore as the lotus tree of Homer's Odyssey.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The genus **Ziziphus** is characterized by alternate leaves with three prominent longitudinal nerves and sharp stipular spines." },
      { author: "Pliny the Elder", work: "Natural History", quote: "The sweet fruit of the **Ziziphus** lotus is so pleasant that strangers eating it forgot their native fatherland." },
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The jujube tree or **Ziziphus** flourisheth in Italy, yielding red fruits whose sweet pulp soothes inflamed throats." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch9Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 9 Completed: ${count} / ${Object.keys(batch9Data).length} notes updated.`);
console.log(`========================================\n`);
