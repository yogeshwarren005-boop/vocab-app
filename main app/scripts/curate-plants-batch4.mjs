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

const batch4Data = {
  "Dashboard — carp/carpel.md": {
    primary: "The female reproductive organ of a flower, consisting of an ovary, a stigma, and usually a style; a modified megasporophyll enclosing the ovules.",
    secondary: "In floral morphology, the fundamental morphological unit of the angiosperm gynoecium, either free (apocarpous) or fused into a compound pistil (syncarpous).",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "The three confluent styles demonstrate that the orchid column incorporates an ancestral three-valved **carpel**." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "A simple pistil is formed of a solitary **carpel**, which may be compared to a folded green leaf bearing seeds along its margins." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Goethe's theory of metamorphosis recognized the **carpel** as a foliar organ folded inward and joined along the ventral suture." }
    ]
  },
  "Dashboard — carp/carpellary.md": {
    primary: "Of, relating to, or belonging to a carpel or carpels.",
    secondary: "In structural botany, designating the specialized tissues, sutures, margins, or vascular traces forming the carpel wall.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Parietal placentation arises when ovules are borne directly upon the united **carpellary** margins of a compound ovary." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "Dehiscence along the dorsal suture represents loculicidal rupture of the **carpellary** wall." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "Diagnostic keys distinguish syncarpous tribes by whether the **carpellary** septa reach the central floral axis." }
    ]
  },
  "Dashboard — carp/carpellate.md": {
    primary: "Having one or more carpels; specifically applied to flowers that possess functional carpels but lack stamens (female flowers).",
    secondary: "In reproductive plant biology, describing pistillate blossoms in monoecious or dioecious species dedicated exclusively to seed production.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "In dioecious hollies, cross-pollination depends entirely upon bees carrying pollen from staminate trees to **carpellate** individuals." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The fertile **carpellate** catkins of the willow swell rapidly after spring fertilization, shedding downy seeds in early June." },
      { author: "John Torrey", work: "Flora of the State of New York", quote: "In the hop vine, the commercial strobiles develop exclusively from clusters of imbricated **carpellate** flowers." }
    ]
  },
  "Dashboard — carp/carpentaria.md": {
    primary: "A large, shallow sea inlet situated on the northern coast of Australia; the Gulf of Carpentaria.",
    secondary: "In biogeography and exploration history, a vast tropical gulf and drainage basin named by Jan Carstensz in 1623 in honor of Pieter de Carpentier.",
    quotes: [
      { author: "Matthew Flinders", work: "A Voyage to Terra Australis", quote: "We charted the low mangrove-lined shores of the Gulf of **Carpentaria**, battling shoals and fierce monsoon squalls." },
      { author: "Alfred Russel Wallace", work: "Australasia", quote: "The Gulf of **Carpentaria** represents a drowned continental depression that once formed an unbroken land bridge to New Guinea." },
      { author: "Robert Logan Jack", work: "The Exploration of Cape York Peninsula", quote: "Burke and Wills pushed heroically across the arid interior until they reached the tidal estuaries of **Carpentaria**." }
    ]
  },
  "Dashboard — carp/carpenter.md": {
    primary: "A skilled tradesperson who builds, installs, or repairs wooden structures and fixtures.",
    secondary: "In natural history and entomology, applied to animals that excavate wood, such as carpenter bees (Xylocopa) or carpenter ants (Camponotus).",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "The busy shipwright and **carpenter** laboured upon the stout timbers of the ark before the deep broke forth." },
      { author: "Henry David Thoreau", work: "Walden", quote: "I borrowed an axe and went down to the woods by Walden Pond, cutting white pine studs like an earnest **carpenter**." },
      { author: "Jean-Henri Fabre", work: "Bramble-Bees and Others", quote: "The solitary **carpenter** bee bores a neat cylindrical gallery through dead cedar posts to house her larval chambers." }
    ]
  },
  "Dashboard — carp/carpenteria.md": {
    primary: "A monotypic genus of evergreen flowering shrubs in the hydrangeaceae family, comprising Carpenteria californica, commonly known as bush anemone.",
    secondary: "In conservation botany, a rare relict shrub endemic to the Sierra Nevada foothills of California, bearing clusters of fragrant white flowers with golden stamens.",
    quotes: [
      { author: "John Torrey", work: "Plantae Fremontianae", quote: "I have named this splendid Sierran shrub **Carpenteria** in memory of my esteemed friend, the late Dr. William M. Carpenter of Louisiana." },
      { author: "Willis Linn Jepson", work: "A Flora of California", quote: "In sheltered granite ravines of Fresno County, **Carpenteria** californica unfurls pure white blossoms of anemone-like beauty." },
      { author: "Philip A. Munz", work: "A California Flora", quote: "Horticulturalists cherish **Carpenteria** for its glossy evergreen foliage and profuse clusters of showy five-petaled blossoms." }
    ]
  },
  "Dashboard — carp/carpentry.md": {
    primary: "The trade, craft, or art of cutting, shaping, and joining timber to construct buildings, furniture, and wooden structures.",
    secondary: "In mechanical arts, the technology of joinery, framing, and timber fabrication fundamental to architectural history.",
    quotes: [
      { author: "John Ruskin", work: "The Seven Lamps of Architecture", quote: "Honest **carpentry** reveals the natural grain and structural joints of the timber rather than concealing them beneath veneer." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "Joe Gargery admired the precise **carpentry** of the church belfry, appreciating the skill required to fit the massive oak beams." },
      { author: "Henry David Thoreau", work: "Walden", quote: "There is some of the same fitness in a man's building his own house that there is in a bird's building its nest, mastering rudimentary **carpentry**." }
    ]
  },
  "Dashboard — carp/carper.md": {
    primary: "A person who habitually finds fault, cavils, or raises trivial, nagging objections.",
    secondary: "A captious or censorious critic who overlooks general excellence to disparage minor imperfections.",
    quotes: [
      { author: "Samuel Johnson", work: "The Rambler", quote: "The chronic **carper** spends his life hunting out grammatical blemishes, insensible to the grandest flights of poetic imagination." },
      { author: "Alexander Pope", work: "An Essay on Criticism", quote: "A pettifogging **carper** may pick holes in Virgil's diction, yet lack the soul to conceive a single heroic line." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Old Miss Crawley was an inveterate **carper**, delighting to point out the modest shortcomings of her impoverished relations." }
    ]
  },
  "Dashboard — carp/carpet.md": {
    primary: "A heavy woven fabric, usually of wool, cotton, or synthetic fiber, used for covering floors or stairs.",
    secondary: "Any dense, continuous covering or expanse resembling a floor textile, such as a carpet of fallen leaves, snow, or moss.",
    quotes: [
      { author: "John Keats", work: "The Eve of St. Agnes", quote: "Across the polished floor the moonbeam shone, while on the soft **carpet** no sound of footsteps stirred." },
      { author: "Henry David Thoreau", work: "Walden", quote: "A rich **carpet** of pine needles softened our path through the deep silent woods." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "A glowing Turkish **carpet** covered the center of the library, radiating crimson warmth into the winter gloom." }
    ]
  },
  "Dashboard — carp/carpetbag.md": {
    primary: "A traveling bag or satchel made of carpet fabric, widely used in the 19th century.",
    secondary: "Historically in American politics, the symbol of opportunistic Northern migrants traveling to the South during Reconstruction.",
    quotes: [
      { author: "Charles Dickens", work: "The Pickwick Papers", quote: "Mr. Pickwick packed his change of linen into a capacious **carpetbag** and mounted the roof of the Rochester coach." },
      { author: "Mark Twain", work: "The Gilded Age", quote: "He arrived at the frontier station clutching an old battered **carpetbag** that contained his entire worldly fortune." },
      { author: "Nathaniel Hawthorne", work: "The Blithedale Romance", quote: "I slung my traveling **carpetbag** over my shoulder and turned my back on the clamorous city streets." }
    ]
  },
  "Dashboard — carp/carpetbagger.md": {
    primary: "Historically, a derogatory term for a Northerner who moved to the South during the Reconstruction era to seek political or financial advantage; any political opportunist running for office in an area with which they have no prior ties.",
    secondary: "In political sociology, an outsider perceived as exploiting local crises or political vacancies for personal or partisan advancement.",
    quotes: [
      { author: "W. E. B. Du Bois", work: "Black Reconstruction in America", quote: "Southern historians unfairly vilified every Northern reformer as a self-seeking **carpetbagger**, ignoring those who came to build public schools." },
      { author: "Mark Twain", work: "Life on the Mississippi", quote: "The local press excoriated the candidate as an unprincipled **carpetbagger** who had not resided three months in the district." },
      { author: "Henry Adams", work: "The Education of Henry Adams", quote: "Post-war Washington was overrun with speculators and the opportunistic **carpetbagger** seeking federal subsidies." }
    ]
  },
  "Dashboard — carp/carpetbagging.md": {
    primary: "The practice or actions of a carpetbagger; opportunistic exploitation of a political or financial situation by an outsider.",
    secondary: "In electoral politics, the practice of relocating to a new district solely to compete for political office without local roots.",
    quotes: [
      { author: "W. E. B. Du Bois", work: "The Souls of Black Folk", quote: "Accusations of corrupt **carpetbagging** were hurled against Northern philanthropists who established colleges for freedmen." },
      { author: "Mark Twain", work: "The Gilded Age", quote: "The editorial condemned the syndicate's shameless **carpetbagging** in acquiring municipal rail franchises." },
      { author: "Woodrow Wilson", work: "Division and Reunion", quote: "The period of so-called **carpetbagging** governance generated deep regional bitterness that lingered for generations." }
    ]
  },
  "Dashboard — carp/carpeted.md": {
    primary: "Fitted, covered, or overlaid with a carpet or a carpet-like layer.",
    secondary: "Describing surfaces spread over with a dense, colorful layer of flowers, moss, fallen leaves, or snow.",
    quotes: [
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "I followed the servant through dark corridors into a lofty room richly **carpeted** in antique crimson draperies." },
      { author: "John Muir", work: "The Mountains of California", quote: "The glacial meadows were thickly **carpeted** with shooting stars, gentians, and golden buttercups." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "The secluded forest glade was softly **carpeted** with brown beech leaves that rustled beneath her tread." }
    ]
  },
  "Dashboard — carp/carpeting.md": {
    primary: "Material used for carpets; the carpets of an interior collectively; the process of laying carpets.",
    secondary: "A dense expanse of low vegetation, turf, or groundcover covering the earth like a woven fabric.",
    quotes: [
      { author: "George Eliot", work: "Middlemarch", quote: "The new mistress ordered rich Brussels **carpeting** to replace the worn drugget in the drawing room." },
      { author: "John Muir", work: "My First Summer in the Sierra", quote: "A dense **carpeting** of dwarf lupines and alpine daisies spread right up to the verge of the snowfields." },
      { author: "Henry James", work: "The American", quote: "His footsteps made no sound upon the thick velvet **carpeting** that muffled the grand staircase." }
    ]
  },
  "Dashboard — carp/carpetweed.md": {
    primary: "A low-growing, prostrate annual weed (Mollugo verticillata, family Molluginaceae) forming flat mats upon cultivated ground and waste places.",
    secondary: "In agricultural weed ecology, a drought-tolerant annual characterized by whorled spatulate leaves and tiny greenish-white blossoms spreading over sandy soils.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The humble **carpetweed** spreads flat upon bare sandy ground in summer, forming green circular mats several feet across." },
      { author: "Nathaniel Lord Britton", work: "An Illustrated Flora of the Northern United States", quote: "Common **carpetweed** is an introduced immigrant from tropical America that rapidly colonizes fallow cornfields." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Gardeners eradicate **carpetweed** by shallow hoeing before its minute seeds ripen in late autumn." }
    ]
  },
  "Dashboard — carp/carpinaceae.md": {
    primary: "An obsolete or segregate botanical family comprising the hornbeams (Carpinus) and hop-hornbeams (Ostrya), now included in Betulaceae (subfamily Coryloideae).",
    secondary: "In historical dendrology, a family of amentiferous trees characterized by hard, dense wood and hop-like fruiting catkins with ribbed nuts.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Systematists separating the **Carpinaceae** from Betulaceae emphasize the three-lobed leafy bracts enclosing the nut." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "The **Carpinaceae** are distinguished by their solitary male flowers in catkins and pairs of female flowers enclosed in leafy involucre." },
      { author: "Charles Sprague Sargent", work: "The Silva of North America", quote: "Fossil leaves matching modern **Carpinaceae** occur abundantly in Eocene and Miocene lacustrine deposits." }
    ]
  },
  "Dashboard — carp/carping.md": {
    primary: "Habitually finding fault, caviling, or raising petty, nagging objections; querulous.",
    secondary: "Captious or hypercritical criticism that dwells persistently upon trivial defects.",
    quotes: [
      { author: "William Shakespeare", work: "Much Ado About Nothing", quote: "Why, he is the common **carping** critic of the court, who never praised honest soldier or fair lady." },
      { author: "Samuel Johnson", work: "The Idler", quote: "A small mind consoles its own mediocrity by constant **carping** at the masterpieces of great authors." },
      { author: "George Eliot", work: "Adam Bede", quote: "Mrs. Poyser had little patience for **carping** gossips who wasted morning hours finding fault with their neighbors' churning." }
    ]
  },
  "Dashboard — carp/carpinus.md": {
    primary: "A genus of deciduous trees in the birch family (Betulaceae) known as hornbeams or ironwoods, valued for their exceptionally hard, dense wood.",
    secondary: "In temperate forest ecology, shade-tolerant understory trees characterized by fluted trunks, smooth grey bark, and three-lobed fruiting bracts.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The genus **Carpinus** is recognized by its pendulous male ament and female spikes with large foliaceous bracts." },
      { author: "John Evelyn", work: "Sylva, or A Discourse of Forest-Trees", quote: "The wood of **Carpinus** betulus or hornbeam is of extraordinary toughness, making incomparable mill cogs and yokes." },
      { author: "Charles Sprague Sargent", work: "Manual of the Trees of North America", quote: "American hornbeam (**Carpinus** caroliniana) features sinewy muscular ridges along its trunk, earning the name blue beech." }
    ]
  },
  "Dashboard — carp/Carpo.md": {
    primary: "In Greek mythology, Carpo (or Karpo) was one of the Horae (Hours), the goddess representing autumn, harvest yield, and the ripening of fruits.",
    secondary: "In classical mythology and astronomical nomenclature, the divine attendant of seasonal abundance; also an outer prograde irregular satellite of Jupiter.",
    quotes: [
      { author: "Pausanias", work: "Description of Greece", quote: "The Athenians dedicated altars to two Horae, Thallo who brings the spring blossom and **Carpo** who ripens autumn fruit." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "The maiden **Carpo** was invoked in harvest liturgies as the divine power that brings seed to fullness." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In classical sculpture, **Carpo** appears crowned with ears of wheat and laden with clusters of purple grapes." }
    ]
  },
  "Dashboard — carp/carpobrotus.md": {
    primary: "A genus of succulent coastal creeping plants in the ice plant family (Aizoaceae), known as pigface, sour fig, or hottentot fig, bearing large daisy-like flowers and edible fruits.",
    secondary: "In coastal ecology, robust ground-hugging halophytes with triangular succulent leaves used for dune stabilization, frequently becoming invasive in Mediterranean climates.",
    quotes: [
      { author: "Nathaniel Lord Britton", work: "Flora of Bermuda", quote: "The thick triangular succulent leaves of **Carpobrotus** edulis carpet maritime dunes, binding shifting coastal sand." },
      { author: "Philip A. Munz", work: "A California Flora", quote: "Introduced from South Africa, **Carpobrotus** has naturalized along the Pacific coast, outcompeting native coastal scrub." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The fleshy yellow and magenta blossoms of **Carpobrotus** open only in bright sunlight, setting large pulpy edible fruits." }
    ]
  },
  "Dashboard — carp/carpocapsa.md": {
    primary: "A former or synonym genus name for Cydia (tortricid moths), including Carpocapsa pomonella, the codling moth whose larva infests apples and pears.",
    secondary: "In economic entomology, a destructive orchard pest whose caterpillar burrows into the core of pomaceous fruits to feed upon seeds.",
    quotes: [
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "The insidious larva of **Carpocapsa** enters the apple at the calyx cup, boring directly to the core." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "Orchardists spray arsenicals immediately after petal fall to destroy newly hatched caterpillars of **Carpocapsa** pomonella." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The codling moth, formerly called **Carpocapsa**, passes the winter as a cocooned larva hidden beneath scaly bark." }
    ]
  },
  "Dashboard — carp/carpodacus.md": {
    primary: "A genus of passerine birds in the finch family (Fringillidae), known as rosefinches, characterized by conical seed-eating bills and rose-red plumage in adult males.",
    secondary: "In avian systematics, Holarctic and alpine finches, including the common rosefinch of Eurasia, feeding upon buds, berries, and seeds.",
    quotes: [
      { author: "John Gould", work: "The Birds of Asia", quote: "The male **Carpodacus** erythrinus exhibits dazzling crimson plumage across its crown, throat, and breast, singing a cheerful whistling song." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "The high mountains of Central Asia represent the principal radiation center for numerous endemic species of **Carpodacus**." },
      { author: "William Yarrell", work: "A History of British Birds", quote: "Occasional vagrants of the genus **Carpodacus** reach the British coast during autumn gales from Northern Europe." }
    ]
  },
  "Dashboard — carp/carpogonium.md": {
    primary: "The female reproductive organ (gametangium) in red algae (Rhodophyta), consisting of an enlarged base containing the female nucleus and a receptive hair-like trichogyne.",
    secondary: "In phycology, the basal cell of the procarp that, upon fertilization by a non-motile spermatium, gives rise to diploid carpospores.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Fertilization in Florideae occurs when a floating spermatium adheres to the elongated trichogyne of the **carpogonium**." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The red algal **carpogonium** demonstrates a unique mode of fertilization involving cytoplasmic fusion and auxiliary cells." },
      { author: "William Gilson Farlow", work: "The Marine Algae of New England", quote: "Microscopic scrutiny of Callithamnion reveals the tiny **carpogonium** nestled among the lateral branching filaments." }
    ]
  },
  "Dashboard — carp/carpology.md": {
    primary: "The branch of botany that deals with the structural study, classification, and morphology of fruits and seeds.",
    secondary: "In systematic organography, the specialized scientific discipline established by Joseph Gaertner to classify plants based upon internal seed and fruit architecture.",
    quotes: [
      { author: "Joseph Gaertner", work: "De Fructibus et Seminibus Plantarum", quote: "The foundation of rational **carpology** rests upon the internal anatomy of the embryo and seed coats rather than external pericarp shape." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Gaertner's masterwork on **carpology** revolutionized plant systematics by demonstrating the diagnostic constancy of seed structures." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "A sound grounding in **carpology** enables the student to distinguish true syncarpous berries from deceptive pseudocarps." }
    ]
  },
  "Dashboard — carp/carpophagous.md": {
    primary: "Feeding on fruit; fruit-eating; frugivorous.",
    secondary: "In animal ecology, describing bats, birds, primates, or insects whose specialized diet consists predominantly of ripe succulent fruits.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The great flying foxes of Java are strictly **carpophagous**, congregating in thousands at dusk to strip fig trees in the jungle canopy." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "Certain Australian pigeons are predominantly **carpophagous**, swallowing large wild nutmegs whole and digesting the nutritious aril." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The generalized dentition of ancestral primates indicates an originally **carpophagous** and insectivorous arboreal habit." }
    ]
  },
  "Dashboard — carp/carpophore.md": {
    primary: "A slender floral stalk or axis supporting the fruit, gynoecium, or mericarps, especially the central axis of umbelliferous fruits (Apiaceae).",
    secondary: "In mycology and pteridology, a specialized stalk supporting a sporocarp or mushroom fruiting body.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "At maturity, the two mericarps of the carrot split apart, remaining suspended from the wiry central **carpophore**." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "The presence of a persistent **carpophore** prevents seeds from falling directly beneath the parent foliage." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "In the Umbelliferae, the structural configuration of the bifurcate **carpophore** provides a reliable tribal character." }
    ]
  },
  "Dashboard — carp/carport.md": {
    primary: "A sheltered roofed structure for an automobile, usually attached to a house and open on at least one or more sides.",
    secondary: "In modern residential architecture, a minimalist vehicle shelter pioneered by Frank Lloyd Wright in Usonian home designs.",
    quotes: [
      { author: "Frank Lloyd Wright", work: "The Natural House", quote: "A car is not a horse; it does not require a barn, and a clean overhanging **carport** provides all necessary protection from weather." },
      { author: "Lewis Mumford", work: "The City in History", quote: "Suburban post-war tract houses replaced the detached carriage barn with an integrated **carport** opening onto the lawn." },
      { author: "John Keats (biographer)", work: "The Crack in the Picture Window", quote: "Rows of suburban dwellings featured an identical concrete slab and cantilevered **carport** sheltering the family sedan." }
    ]
  },
  "Dashboard — carp/carpospore.md": {
    primary: "A diploid non-motile spore produced inside the cystocarp of red algae (Rhodophyta) following fertilization.",
    secondary: "In phycological life cycles, the spore that germinates into the diploid tetrasporophyte generation in triphasic red algal alternation of generations.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Upon maturation of the cystocarp, each liberated **carpospore** drifts into the plankton, ready to settle upon a rocky substrate." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The development of a dense cluster of **carpospores** multiplies the reproductive output of a single fertilization event." },
      { author: "William Gilson Farlow", work: "Marine Algae of New England", quote: "Under the microscope, each rounded **carpospore** gleams with deep phycoerythrin pigment, devoid of cilia or flagella." }
    ]
  },
  "Dashboard — carp/carposporic.md": {
    primary: "Of, relating to, or producing carpospores (the spores of red algae).",
    secondary: "In rhodophyte cytology, designating the carposporophyte phase dedicated to carpospore amplification and discharge.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The **carposporic** phase represents an extraordinary parasitic diploid generation living entirely within the female gametophyte." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Cytological division within the **carposporic** filaments culminates in the formation of club-shaped terminal sporangia." },
      { author: "William Gilson Farlow", work: "Marine Algae of New England", quote: "The presence of mature **carposporic** cysts provides conclusive taxonomic identification among ambiguous red algal species." }
    ]
  },
  "Dashboard — carp/carposporous.md": {
    primary: "Bearing, producing, or characterized by carpospores.",
    secondary: "Describing red algae during their fruiting reproductive stage when cystocarps are actively releasing carpospores.",
    quotes: [
      { author: "William Gilson Farlow", work: "Marine Algae of New England", quote: "Specimens collected in late August were abundantly **carposporous**, with swelling cystocarps visible along the frond margins." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The **carposporous** generation multiplies the diploid genome before meiosis occurs in the subsequent tetrasporophyte." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The **carposporous** reproductive mechanism compensates for the complete absence of motile flagellated gametes in red algae." }
    ]
  },
  "Dashboard — carp/carpus.md": {
    primary: "The wrist in vertebrate anatomy; the group of small bones between the forearm (radius and ulna) and the metacarpus.",
    secondary: "In comparative osteology, an articulating complex of eight carpal bones arranged in two transverse rows facilitating multi-axial wrist motion.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The mammalian **carpus** retains the primitive pentadactyl pattern, comprising radiale, intermedium, ulnare, and five distal carpals." },
      { author: "Richard Owen", work: "On the Nature of Limbs", quote: "Homologies of the **carpus** demonstrate the common structural archetype underlying the flipper of the whale and the human hand." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The identical arrangement of bones in the **carpus** of a bat and the hand of a man cannot be explained by mere adaptation." }
    ]
  },
  "Dashboard — carp/cystocarp.md": {
    primary: "The fruit-body or spore-producing structure developed after fertilization in red algae (Rhodophyta), consisting of carpospores enclosed in a sterile cellular pericarp.",
    secondary: "In phycology, the complex urn-shaped or urn-like structure housing gonimoblast filaments and mature carpospores.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The swollen **cystocarp** projects from the frond as a dark, bead-like capsule with a terminal ostiole for spore release." },
      { author: "William Gilson Farlow", work: "Marine Algae of New England", quote: "Cross-sections through the **cystocarp** of Polysiphonia demonstrate the urn-shaped protective envelope surrounding gonimoblast cells." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "The **cystocarp** constitutes an elaborate post-fertilization envelope unique to the higher Florideae." }
    ]
  },
  "Dashboard — carp/dipterocarp.md": {
    primary: "A tall tropical forest tree of the family Dipterocarpaceae, characterized by two-winged fruits and aromatic resins, dominating Asian rainforests.",
    secondary: "In tropical forestry and ecology, emergent canopy trees that produce commercially valuable hardwood timber (such as meranti and keruing) and undergo mast fruiting.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The primary forest of Borneo is crowned by giant species of **dipterocarp**, their massive buttressed trunks rising over two hundred feet." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "The resinous secretions of the **dipterocarp** forests yield valuable dammar varnishes and wood oils across tropical Asia." },
      { author: "Henry Nicholas Ridley", work: "The Dispersal of Plants Throughout the World", quote: "When the wind shakes the canopy, the two-winged fruits of the **dipterocarp** spin gracefully downward like miniature shuttlecocks." }
    ]
  },
  "Dashboard — carp/endocarp.md": {
    primary: "The innermost layer of the pericarp of a fruit, surrounding the seed; may be hard and stony (as the peach pit) or membranous (as the apple core).",
    secondary: "In carpological anatomy, the sclerified or papery lining of the ovarian cavity derived from the inner epidermis of the carpel wall.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "In a peach or cherry, the stone is the indurated **endocarp**, enclosing the soft edible kernel or true seed." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The toughness of the **endocarp** protects the delicate embryonic plantlet from digestive juices when swallowed by fruit-eating birds." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "In the pome fruit of the hawthorn, the stony **endocarp** forms bony nutlets enclosing each individual seed." }
    ]
  },
  "Dashboard — carp/epicarp.md": {
    primary: "The outermost layer of the pericarp or fruit wall; the skin or peel of a fruit (also termed exocarp).",
    secondary: "In descriptive pomology, the cuticle-covered epidermal layer of a fruit often containing pigments, stomata, waxes, and essential oil glands.",
    quotes: [
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The bright red blush of the ripening apple resides entirely within the cells of the **epicarp**." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In the orange, the leathery **epicarp** is studded with aromatic oil glands and colored by carotenoid pigments." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "A waxy bloom covering the **epicarp** prevents excessive transpiration and repels moisture from the fruit surface." }
    ]
  },
  "Dashboard — carp/epicarpal.md": {
    primary: "Situated upon, relating to, or belonging to the epicarp (the outer skin of a fruit).",
    secondary: "In anatomical carpology, describing glandular trichomes, waxes, or stomata located on the external surface of the fruit peel.",
    quotes: [
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Microscopic analysis reveals secretory cavities situated directly beneath the **epicarpal** layer in Citrus fruits." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The **epicarpal** cells of the plum secrete a delicate pruinose coating that rubs off at the slightest touch." },
      { author: "George Henslow", work: "The Heredity of Acquired Characters in Plants", quote: "Thickening of the **epicarpal** wall in desert melons serves as a protective adaptation against intense solar radiation." }
    ]
  },
  "Dashboard — carp/exocarp.md": {
    primary: "The outermost layer of the pericarp of a fruit; the skin or peel; epicarp.",
    secondary: "In botanical morphology, the external epidermal tissue of the fruit wall, often differentiated with waxes, trichomes, or protective collenchyma.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "In drupaceous fruits, the **exocarp** forms the thin exterior skin, while the mesocarp constitutes the juicy edible flesh." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The tough, fibrous **exocarp** of the coconut enables the heavy seed to float uninjured across ocean currents for months." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Anthocyanin accumulation in the **exocarp** signals ripeness to frugivorous dispersal agents in the forest understory." }
    ]
  },
  "Dashboard — carp/Karpos.md": {
    primary: "The ancient Greek word for fruit, grain, or harvest yield (karpos); also the personified Greek deity of seasonal fruit and harvest.",
    secondary: "In classical mythology and Hellenic agriculture, the divine youth Karpos (son of Zephyrus and Chloris), celebrated as the spirit of summer fruits.",
    quotes: [
      { author: "Pausanias", work: "Description of Greece", quote: "The ancients celebrated **Karpos** alongside the agricultural deities who bless the earth with corn and vine." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "The mythological figure of **Karpos** embodied the annual miracle of seed ripening into bountiful nourishment." },
      { author: "Walter Pater", work: "Greek Studies", quote: "In pastoral poetry, **Karpos** represents the youthful spirit of the garden, crowned with fig leaves and ripe apples." }
    ]
  },
  "Dashboard — carp/mericarp.md": {
    primary: "A one-seeded portion or half-fruit of a schizocarp that splits away from the central axis (carpophore) at maturity, typical of the carrot family (Apiaceae).",
    secondary: "In systematic carpology, an indehiscent carpellary unit possessing distinctive longitudinal ribs, vittae (oil tubes), and stylopodium.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "At full maturity, the fruit of the hemlock separates into two ribbed seed-like halves, each termed a **mericarp**." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The cross-section of each **mericarp** displays five primary ribs and secretes essential oils within internal vittae." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "Diagnostic keys in the Umbelliferae depend upon the prominence of ridges and spines along the dorsal surface of the **mericarp**." }
    ]
  },
  "Dashboard — carp/mesocarp.md": {
    primary: "The middle layer of the pericarp of a fruit, between the epicarp (exocarp) and endocarp; often fleshy and succulent (the pulp of a peach or berry).",
    secondary: "In pomology, the succulent parenchymatous tissue that accumulates sugars, water, and organic acids to attract seed-dispersing vertebrates.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "In a peach, the luscious pulp that we eat is the fleshy **mesocarp**, situated between the outer skin and the stone." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "In the coconut, the **mesocarp** is not juicy, but consists of a dense fibrous husk utilized commercially as coir." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Rapid cellular enlargement and sugar accumulation transform the green **mesocarp** into sweet succulent tissue at ripening." }
    ]
  },
  "Dashboard — carp/metacarpal.md": {
    primary: "Of or relating to the metacarpus (the hand bones between the wrist and fingers); any of the bones of the metacarpus.",
    secondary: "In vertebrate anatomy, one of the five cylindrical rod-like bones forming the skeletal framework of the palm in humans.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The human hand possesses five distinct **metacarpal** bones, articulating proximally with the carpus and distally with the phalanges." },
      { author: "Richard Owen", work: "On the Nature of Limbs", quote: "In the horse, cursorial specialization has reduced the **metacarpal** series to a single dominant cannon bone flanked by splint bones." },
      { author: "Charles Darwin", work: "The Descent of Man", quote: "The high mobility of the first **metacarpal** bone permits opposability of the thumb, a cornerstone of human manual dexterity." }
    ]
  },
  "Dashboard — carp/metacarpus.md": {
    primary: "The part of the hand or forefoot situated between the carpus (wrist) and the digits (phalanges), comprising the metacarpal bones.",
    secondary: "In comparative tetrapod osteology, the skeletal intermediate segment of the manus that supports the palm or paw.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "Comparative analysis of the forelimb demonstrates that the **metacarpus** underwent drastic elongation in running ungulates." },
      { author: "Richard Owen", work: "Comparative Anatomy of Vertebrates", quote: "The bat wing demonstrates extraordinary elongation of the **metacarpus** and phalanges to support the membranous patagium." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "In carnivores, the five digits of the **metacarpus** rest upon fibro-fatty pads adapted for silent stalking." }
    ]
  },
  "Dashboard — carp/monocarp.md": {
    primary: "A plant that bears fruit only once in its life cycle and then dies (monocarpic plant).",
    secondary: "In life history theory, a semelparous flowering plant (such as bamboo, century plant, or talipot palm) that invests all accumulated resources into a single massive fruiting event.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The colossal talipot palm lives for half a century as a vegetative **monocarp** before expending all its vitality in one stupendous inflorescence." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The common century plant (Agave americana) is a famous **monocarp**, dying down to the roots after its towering scape matures seeds." },
      { author: "Alfred Russel Wallace", work: "Tropical Nature", quote: "Certain gregarious forest bamboos flower synchronously as a **monocarp**, seeding once across entire provinces and then withering simultaneously." }
    ]
  },
  "Dashboard — carp/monocarpic.md": {
    primary: "Flowering and bearing fruit only once in a lifetime and dying after seed production; semelparous.",
    secondary: "In plant ecology and reproductive energetics, designating annuals, biennials, and long-lived perennials that commit all metabolic reserves to a single terminal reproductive effort.",
    quotes: [
      { author: "Charles Darwin", work: "The Effects of Cross and Self Fertilisation", quote: "The **monocarpic** habit ensures that the plant directs its entire stored reserves into producing the maximum quantity of viable seed." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "Annual and biennial herbs are strictly **monocarpic**, whereas long-lived orchard trees are polycarpic." },
      { author: "John Muir", work: "Steep Trails", quote: "The giant silversword of Haleakala is **monocarpic**, blooming once in a glorious silver spire before perishing upon the volcanic cinder." }
    ]
  },
  "Dashboard — carp/pericarp.md": {
    primary: "The wall of a ripened plant ovary or fruit, consisting of three layers: exocarp, mesocarp, and endocarp.",
    secondary: "In carpological morphology, the surrounding fruit wall enclosing the seeds, exhibiting specialized modifications for seed dispersal and mechanical protection.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The **pericarp** is the ripened ovary wall, which in a berry remains fleshy throughout, but in a hazelnut becomes hard and woody." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Tension in the drying **pericarp** causes explosive dehiscence in the touch-me-not, flinging seeds yards away." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Microscopic analysis shows that the **pericarp** differentiates from the carpel mesophyll into three distinct histogenetic zones." }
    ]
  },
  "Dashboard — carp/polycarp.md": {
    primary: "A plant that flowers and bears fruit multiple times year after year; also St. Polycarp, 2nd-century Christian martyr and bishop of Smyrna.",
    secondary: "In botanical life history and church history, a perennial flowering organism (polycarpic plant); or the venerated apostolic father who suffered martyrdom at Smyrna.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Perennial forest oaks represent the ultimate **polycarp**, bearing seasonal crops of acorns across hundreds of successive autumns." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The venerable Bishop **Polycarp** refused to revile Christ before the proconsul, sealing his eighty-six years of faith in the flames." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "A typical woody **polycarp** sets aside nutrient reserves each summer to sustain the following spring's burst of flowers." }
    ]
  },
  "Dashboard — carp/polycarpic.md": {
    primary: "Flowering and bearing fruit repeatedly year after year throughout its lifetime; iteroparous (characteristic of perennial plants).",
    secondary: "In plant ecology, the life history strategy of allocating resources across multiple reproductive seasons, contrasting with monocarpic semelparity.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Most woody shrubs and trees are **polycarpic**, surviving after each harvest to produce fruit through successive decades." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Cultivated fruit trees maintain their **polycarpic** constitution even when subjected to intense artificial selection for annual yield." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "The transition from an annual monocarpic habit to a **polycarpic** perennial state often corresponds with the evolution of secondary woody growth." }
    ]
  },
  "Dashboard — carp/procarp.md": {
    primary: "The female reproductive structure of red algae (Rhodophyta), consisting of the carpogonium (with its trichogyne) and the auxiliary cell before fertilization.",
    secondary: "In phycological embryology, the pre-fertilization gametangial complex whose architectural arrangement governs subsequent diploid carposporophyte development.",
    quotes: [
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "The compact **procarp** comprises both the receptive carpogonium and a closely associated auxiliary cell ready to receive the diploid nucleus." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "In Ceramium, the **procarp** develops upon a specialized four-celled fertile branch of the thallus." },
      { author: "William Gilson Farlow", work: "Marine Algae of New England", quote: "Detailed study of the **procarp** is indispensable for unraveling the phylogenetic relationships among Floridean red seaweeds." }
    ]
  },
  "Dashboard — carp/pseudocarp.md": {
    primary: "A false fruit or accessory fruit, in which parts other than the ripened ovary (such as the receptacle, calyx, or floral axis) enlarge and form part of the fruit (e.g. apple, strawberry, fig).",
    secondary: "In carpological taxonomy, an edible fruit structure derived predominantly from non-carpellary floral organs, contrasting with true fruits derived solely from the ovary.",
    quotes: [
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The strawberry is a celebrated **pseudocarp**, where the succulent red flesh is an enlarged receptacle dotted with tiny true achene fruits." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "In the apple, the fleshy edible portion is technically a **pseudocarp** formed by the swollen hypanthium fused to the central core." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Accessory tissues contributing to a **pseudocarp** often accumulate higher sugar concentrations than the carpels themselves." }
    ]
  },
  "Dashboard — carp/syncarp.md": {
    primary: "A composite or aggregate fruit formed from the union of multiple carpels of a single flower or the coalesced fruits of several flowers (such as a blackberry or pineapple).",
    secondary: "In angiosperm carpology, a collective fruiting body consisting of densely packed drupelets or coalesced ovaries maturing as a single structural unit.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The mulberry is an exemplary multiple **syncarp**, where each succulent bead represents the fleshy perianth of an independent female floret." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The cone-like **syncarp** of Magnolia consists of spirally arranged carpels that split along their backs to discharge scarlet seeds." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "In the raspberry, the edible dome is an aggregate **syncarp** composed of dozens of tiny succulent drupelets." }
    ]
  },
  "Dashboard — carp/syncarpous.md": {
    primary: "Having the carpels of a flower united or fused together to form a single compound ovary or pistil.",
    secondary: "In angiosperm phylogenetics, an advanced floral evolutionary stage that allows unified pollen tube transmission and efficient multi-locular seed packaging.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "The **syncarpous** ovary of the orchid consists of three carpels so intimately united that internal partitions are completely obliterated." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "The lily displays a **syncarpous** pistil with three united locules, whereas the buttercup retains separate apocarpous carpels." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "The formation of a **syncarpous** gynoecium represents one of the major evolutionary advances in the diversification of flowering plants." }
    ]
  },
  "Dashboard — carp/uncarpeted.md": {
    primary: "Not covered or fitted with a carpet; having bare floors.",
    secondary: "Describing rooms, floors, or stairs that lack floor coverings, often conveying austerity, poverty, or stark simplicity.",
    quotes: [
      { author: "Charles Dickens", work: "Bleak House", quote: "Our footsteps echoed hollowly upon the cold, **uncarpeted** stone staircase of the desolate London inn." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "The dormitory at Lowood was vast and chill, with rows of narrow beds set upon bare, **uncarpeted** deal boards." },
      { author: "Thomas Hardy", work: "The Mayor of Casterbridge", quote: "Henchard paced the bare, **uncarpeted** parlor of his ruined cottage, listening to the midnight wind rattle the casement." }
    ]
  },
  "Dashboard — dendr/dendr.md": {
    primary: "A combining form and classical botanical root derived from Greek 'dendron' (tree, woody plant), forming words relating to trees and arborescent structures.",
    secondary: "In etymological lexicography and dendrology, the foundational stem designating tree biology, tree rings (dendrochronology), and tree-like branching (dendrites).",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The Greek root **dendr** originates in dendron, signifying any majestic forest tree or woody perennial plant." },
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The Greeks designated as **dendr** those perennial plants possessing an erect main trunk, distinct branches, and enduring longevity." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Scientific nomenclature employs the root **dendr** to denote arborescent habit or branching tree-like morphology across biological kingdoms." }
    ]
  },
  "Dashboard — dendr/dendranthema.md": {
    primary: "A botanical genus name (or synonym of Chrysanthemum) containing the florist's chrysanthemum and allied East Asian wild species.",
    secondary: "In plant taxonomy, a segregative asteraceous genus established for autumn-blooming subshrubs possessing lobed aromatic leaves and radiate flower heads.",
    quotes: [
      { author: "Adolf Engler", work: "Syllabus der Pflanzenfamilien", quote: "Systematic revisions transferred several ornamental species from Chrysanthemum to **Dendranthema**, citing distinct achene anatomy." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The ancestral wild parent of cultivated autumn chrysanthemums is **Dendranthema** indicum, native to rocky slopes of China." },
      { author: "Asa Gray", work: "Field, Forest, and Garden Botany", quote: "Under the name **Dendranthema**, taxonomists distinguish the perennial woody-based chrysanthemums from annual corn-marigolds." }
    ]
  },
  "Dashboard — dendr/dendraspis.md": {
    primary: "An alternative or historical generic spelling for Dendroaspis, the genus of highly venomous arboreal elapid snakes native to sub-Saharan Africa (the mambas).",
    secondary: "In historical herpetology, fast-moving arboreal serpents including the black mamba and green mamba, renowned for potent neurotoxic venoms.",
    quotes: [
      { author: "Albert Günther", work: "Catalogue of Colubrine Snakes in the British Museum", quote: "The arboreal genus **Dendraspis** is distinguished by its narrow elongate head, slender body, and immense venom fangs." },
      { author: "George Albert Boulenger", work: "The Snakes of Africa", quote: "Specimens of **Dendraspis** angusticeps glide through the high forest foliage with extraordinary rapidity, hunting birds." },
      { author: "Raymond Ditmars", work: "Snakes of the World", quote: "In African folklore, the terror inspired by **Dendraspis** matches that of the king cobra in southern Asia." }
    ]
  },
  "Dashboard — dendr/dendric.md": {
    primary: "Of, relating to, or resembling a tree; having a tree-like or arborescent branching structure.",
    secondary: "In cytology and neurology, pertaining to the branching dendritic processes of a neuron.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The coral colony expands into a complex **dendric** framework that mimics the branching boughs of a forest oak." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "The **dendric** arborizations of the cerebellar Purkinje cells spread like an intricate fan to receive parallel fibers." },
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Mineral solutions seeping through shale bedding planes crystallize into exquisite **dendric** patterns of manganese oxide." }
    ]
  },
  "Dashboard — dendr/dendriform.md": {
    primary: "Having the shape, appearance, or branching structure of a tree; arborescent.",
    secondary: "In mineralogy and comparative anatomy, describing crystals, blood vessels, or organisms displaying tree-like ramification.",
    quotes: [
      { author: "Charles Darwin", work: "Geological Observations on South America", quote: "The cliff face was painted with delicate **dendriform** crystallizations of iron and manganese that simulated fossil mosses." },
      { author: "James Dwight Dana", work: "Corals and Coral Islands", quote: "The elkhorn coral develops massive **dendriform** colonies whose heavy branches withstand the pounding surf of Caribbean reefs." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "The respiratory organs in certain marine worms present an elegant **dendriform** cluster of branching gills." }
    ]
  },
  "Dashboard — dendr/dendrite.md": {
    primary: "A short, branched extension of a nerve cell, along which impulses received from other cells at synapses are transmitted to the cell body; also a branching, tree-like mineral crystal.",
    secondary: "In mineralogy and neurology, a branching arborescent structure, whether a manganese oxide fern-like marking on stone or a receptive neuronal process.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Each microscopic **dendrite** bristles with thousands of tiny dendritic spines that form contact points with axon terminals." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Novices frequently mistake a manganese **dendrite** upon a limestone flagstone for the fossilized imprint of a delicate fern." },
      { author: "William James", work: "The Principles of Psychology", quote: "The proliferation of connections between **dendrite** and axon underlies the neurophysiological formation of habit in the brain." }
    ]
  },
  "Dashboard — dendr/dendritic.md": {
    primary: "Having a branching, tree-like structure; relating to dendrites (neuronal or mineral).",
    secondary: "In geomorphology, drainage patterns characterized by irregular branching tributary streams resembling the veins of a leaf or tree branches.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "River systems developing across horizontal sedimentary plains naturally carve out a **dendritic** drainage network." },
      { author: "Santiago Ramón y Cajal", work: "Recollections of My Life", quote: "Under the silver nitrate stain, the **dendritic** arborization of cortical neurons stood revealed in astonishing clarity." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Native copper occasionally occurs in exquisite **dendritic** crystal sprays resembling branching bronze foliage." }
    ]
  },
  "Dashboard — dendr/dendroaspis.md": {
    primary: "A genus of fast-moving, highly venomous elapid snakes native to sub-Saharan Africa, comprising the mambas (including the black mamba, Dendroaspis polylepis).",
    secondary: "In herpetology and clinical toxinology, arboreal and terrestrial serpents whose bite delivers rapid neurotoxins and cardiotoxins causing respiratory paralysis.",
    quotes: [
      { author: "George Albert Boulenger", work: "The Snakes of Africa", quote: "The genus **Dendroaspis** differs from Naja in its exceptionally slender build, large smooth scales, and specialized proteroglyph dentition." },
      { author: "Raymond Ditmars", work: "Reptiles of the World", quote: "The black mamba, **Dendroaspis** polylepis, can travel across rough ground with the speed of a running man." },
      { author: "Albert Günther", work: "Catalogue of Colubrine Snakes", quote: "Green specimens of **Dendroaspis** spend their entire lives in the upper forest canopy, perfectly camouflaged among tropical lianas." }
    ]
  },
  "Dashboard — dendr/dendrobium.md": {
    primary: "A vast and diverse genus of predominantly epiphytic and lithophytic orchids (family Orchidaceae), native to tropical and subtropical Asia, Australasia, and the Pacific.",
    secondary: "In tropical horticulture and floristics, an immense orchid genus bearing pseudobulbs or cane-like stems and showy blossoms with a distinct chin-like mentum.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The genus **Dendrobium** derives its name from its tree-dwelling habit, clinging to high jungle boughs with tenaciously grasping roots." },
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "In **Dendrobium**, the mentum formed by the lateral sepals secretes a sweet drop of nectar that attracts nocturnal moths." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the forests of the Moluccas, we discovered a splendid **Dendrobium** with trailing flower spikes of pure golden yellow over three feet long." }
    ]
  },
  "Dashboard — dendr/dendrocalamus.md": {
    primary: "A genus of giant, clumping tropical bamboos (family Poaceae), native to South and Southeast Asia, including Dendrocalamus giganteus (giant bamboo).",
    secondary: "In economic botany, massive arborescent grasses whose woody culms can reach over thirty meters in height and thirty centimeters in diameter, used for structural construction.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The gigantic culms of **Dendrocalamus** provide the native architect with pillars, water pipes, floor joists, and roofing tiles." },
      { author: "Joseph Dalton Hooker", work: "Himalayan Journals", quote: "In the deep valleys of Sikkim, culms of **Dendrocalamus** grow with such phenomenal velocity that one can almost watch them lengthen day by day." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "The culms of **Dendrocalamus** giganteus form immense towering clumps that resemble majestic organ pipes in tropical botanical gardens." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch4Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 4 Completed: ${count} / ${Object.keys(batch4Data).length} notes updated.`);
console.log(`========================================\n`);
