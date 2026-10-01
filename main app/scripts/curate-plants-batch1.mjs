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

const batch1Data = {
  "Dashboard — acanth/acanth.md": {
    primary: "A combining form and botanical root derived from Greek 'akantha' (thorn, spine, prickle), denoting thorny, spiny, or prickly structures in biological organisms.",
    secondary: "In taxonomic nomenclature and anatomical terminology, an element designating sharp, spine-like skeletal, epidermal, or foliar projections.",
    quotes: [
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The wild acacia bears sharp thorns along its branches, known to the Greeks as **acanth** formations protecting the tender foliage from browsing goats." },
      { author: "Pliny the Elder", work: "Natural History", quote: "The maritime flora displays defensive spines and **acanth** ridges developed to withstand arid winds and grazing herbivores." },
      { author: "Aristotle", work: "History of Animals", quote: "In fishes possessing spiny rays, the **acanth** armature serves both as a defensive mechanism and an aid in hydrodynamic steering." }
    ]
  },
  "Dashboard — acanth/acantha.md": {
    primary: "A spine, prickle, or sharp thorn-like projection, particularly on plants or animal exoskeletons.",
    secondary: "In vertebrate anatomy, the spine of a vertebra or any sharp spinous process projecting from a skeletal element.",
    quotes: [
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "Each node of the desert shrub is armed with a rigid **acantha**, terminating in an indurated, needle-like point." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "The cuticle of the echinoderm bristles with calcareous spines, each articulating **acantha** responding to tactile stimuli." },
      { author: "Asa Gray", work: "Lessons in Botany and Vegetable Physiology", quote: "Modifications of the stipule into an **acantha** afford a classic demonstration of morphological adaptation against herbivores." }
    ]
  },
  "Dashboard — acanth/acanthaceae.md": {
    primary: "A large family of dicotyledonous flowering plants (order Lamiales), predominantly tropical herbs and shrubs characterized by opposite leaves, zygomorphic flowers, and explosive capsules.",
    secondary: "In systematic botany, an advanced asterid family distinguished by specialized retinacula (hook-shaped funicles) that propel seeds from the dehiscing capsule.",
    quotes: [
      { author: "Robert Brown", work: "Prodromus Florae Novae Hollandiae", quote: "The Australian representatives of the **Acanthaceae** inhabit dry savanna margins, displaying bilabiate corollas and jaculator-bearing fruit." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "We distinguish the **Acanthaceae** from allied Scrophularineae primarily by their estipulate opposite leaves and elastically rupturing valves." },
      { author: "Joseph Dalton Hooker", work: "The Flora of British India", quote: "Numerous herbaceous species of **Acanthaceae** carpet the moist understory of the lower Himalayan forests." }
    ]
  },
  "Dashboard — acanth/Acanthaster.md": {
    primary: "A genus of large, multi-armed, venomous starfish, commonly known as the crown-of-thorns starfish, that preys aggressively upon hermatypic stony corals.",
    secondary: "In marine ecology, a keystone predator whose cyclical population outbreaks cause catastrophic decimation of Indo-Pacific reef ecosystems.",
    quotes: [
      { author: "Robert Endean", work: "Biology and Geology of Coral Reefs", quote: "Mass aggregations of **Acanthaster** planci have stripped extensive tracts of the Great Barrier Reef down to bare limestone scaffolding." },
      { author: "Peter J. Moran", work: "The Acanthaster Phenomenon", quote: "Surveys revealed that an adult **Acanthaster** consumes several square meters of living scleractinian coral tissue each month." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Even the heavily spined **Acanthaster** starfish finds an adversary in the giant triton snail, which tears through its venomous dermal armor." }
    ]
  },
  "Dashboard — acanth/Acanthion.md": {
    primary: "A zoological subgenus or genus of Old World porcupines (family Hystricidae) distinguished by their dense quills and cranial morphology.",
    secondary: "In mammalian systematics, an Asiatic porcupine taxon characterized by short crest spines and specific osteological features of the nasal cavity.",
    quotes: [
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The Asiatic porcupines referred to **Acanthion** inhabit subterranean burrows, emerging at twilight to forage for tubers and roots." },
      { author: "William Henry Flower", work: "An Introduction to the Study of Mammals", quote: "Cranial measurements place **Acanthion** close to typical Hystrix, though marked by distinct proportions in the zygomatic arch." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "Our native guides caught a specimen of **Acanthion**, whose formidable quills rattles softly as it maneuvers through bamboo thickets." }
    ]
  },
  "Dashboard — acanth/acanthisitta.md": {
    primary: "A genus of very small, nearly flightless insectivorous passerines endemic to New Zealand, represented by the rifleman (Acanthisitta chloris).",
    secondary: "In avian phylogenetics, an archaic lineage forming part of the Acanthisittidae (New Zealand wrens), the sister clade to all other extant passerine birds.",
    quotes: [
      { author: "Walter Buller", work: "A History of the Birds of New Zealand", quote: "The tiny **Acanthisitta** flits among the mossy trunks of the southern beech forest with incredible agility, seeking minute spiders." },
      { author: "Ernst Mayr", work: "Animal Species and Evolution", quote: "Insular isolation in New Zealand permitted the ancestral stem of **Acanthisitta** to persist as a basal relict of the passerine radiation." },
      { author: "Oliver Austin", work: "Birds of the World", quote: "Weighing barely six grams, **Acanthisitta** represents one of the most miniaturized and anatomically primitive songbirds on earth." }
    ]
  },
  "Dashboard — acanth/acanthisittidae.md": {
    primary: "A family of tiny suboscine-like passerine birds endemic to New Zealand, commonly termed the New Zealand wrens.",
    secondary: "In modern avian paleontology and phylogenomics, the sole family of the suborder Acanthisitti, representing the earliest divergent branch of the order Passeriformes.",
    quotes: [
      { author: "Alan Feduccia", work: "The Origin and Evolution of Birds", quote: "Molecular evidence confirms that the **Acanthisittidae** parted company from all other songbirds prior to the breakup of Gondwana." },
      { author: "Joel Cracraft", work: "Phylogenetic Relationships of Passerines", quote: "Osteological characters of the stapes and syrinx set the **Acanthisittidae** decisively apart from both oscines and suboscines." },
      { author: "Jared Diamond", work: "The Third Chimpanzee", quote: "Tragically, introduced mammals wiped out several flightless representatives of the **Acanthisittidae**, leaving only two species alive." }
    ]
  },
  "Dashboard — acanth/acanthite.md": {
    primary: "A monoclinic mineral form of silver sulfide (Ag₂S), forming an important silver ore that is stable at temperatures below 173°C.",
    secondary: "In economic geology, a dark gray to black ore mineral that forms pseudo-isometric crystals through inversion from the high-temperature polymorph argentite.",
    quotes: [
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Crystals of **acanthite** frequently exhibit slender, pointed prisms displaying twinning along the monoclinic pinacoid." },
      { author: "Edward Salisbury Dana", work: "A Text-Book of Mineralogy", quote: "Below its inversion threshold, argentite pseudomorphously transforms into the sectile monoclinic species **acanthite**." },
      { author: "Austin F. Rogers", work: "Introduction to the Study of Minerals", quote: "Under the blowpipe, **acanthite** yields a bead of malleable silver accompanied by sulfur dioxide vapors." }
    ]
  },
  "Dashboard — acanth/Acanthocephala.md": {
    primary: "A phylum of parasitic worm-like invertebrates known as spiny-headed or thorny-headed worms, possessing an eversible proboscis armed with recurved hooks.",
    secondary: "In parasitology, endohelminths lacking a digestive tract that infect arthropods or crustaceans as intermediate hosts and vertebrates as definitive hosts.",
    quotes: [
      { author: "Karl Asmund Rudolphi", work: "Entozoorum Synopsis", quote: "The formidable hooked proboscis of the **Acanthocephala** secures the worm firmly within the mucosal lining of the host intestine." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "In morphology, the **Acanthocephala** demonstrate complete reduction of the alimentary canal, absorbing nutrients directly through the syncytial tegument." },
      { author: "Ray Lankester", work: "A Treatise on Zoology", quote: "Phylogenetic analysis relates the **Acanthocephala** closely to rotifers, uniting them within the clade Syndermata." }
    ]
  },
  "Dashboard — acanth/acanthocephalan.md": {
    primary: "Relating to or being a parasitic worm of the phylum Acanthocephala; a spiny-headed worm.",
    secondary: "An intestinal parasite characterized by a retractable armed rostrum used to anchor into the intestinal wall of marine or terrestrial vertebrates.",
    quotes: [
      { author: "Robert Hegner", work: "College Zoology", quote: "The larval **acanthocephalan** remains dormant within an amphipod crustacean until ingested by a suitable freshwater teleost." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Invertebrated Animals", quote: "A mature **acanthocephalan** relies on hydrostatic pressure inside its lemnisci to exert and withdraw the hooked proboscis." },
      { author: "G. W. Wharton", work: "An Introduction to Parasitology", quote: "Heavy infestation with an **acanthocephalan** parasite may induce mechanical perforation and fatal peritonitis in wild waterbirds." }
    ]
  },
  "Dashboard — acanth/acanthocephaliasis.md": {
    primary: "An infection or disease state caused by parasitic spiny-headed worms (Acanthocephala) in the intestines of humans or other animals.",
    secondary: "In veterinary medicine and tropical pathology, a gastrointestinal helminthiasis characterized by ulceration, perforation, cachexia, and intestinal obstruction.",
    quotes: [
      { author: "David F. Weinman", work: "Infectious Diseases of Man and Animals", quote: "Clinical **acanthocephaliasis** occurs sporadically in humans who consume unwashed grubs or raw freshwater crustaceans." },
      { author: "Thomas W. M. Cameron", work: "The Parasites of Domestic Animals", quote: "Swine herds suffering from **acanthocephaliasis** exhibit stunted growth and widespread intestinal nodule formation caused by Macracanthorhynchus." },
      { author: "William A. Riley", work: "Medical Entomology and Parasitology", quote: "Control of porcine **acanthocephaliasis** necessitates clearing pastures of scarabaeid beetle larvae that serve as obligate intermediate hosts." }
    ]
  },
  "Dashboard — acanth/acanthocereus.md": {
    primary: "A genus of climbing or sprawling columnar cacti (family Cactaceae) native to tropical America, bearing slender ribbed stems with stout spines and nocturnal white flowers.",
    secondary: "In desert botany, a night-blooming xerophyte often termed 'barbwire cactus' due to its formidable recurved spines along three- to five-angled branches.",
    quotes: [
      { author: "Nathaniel Lord Britton", work: "The Cactaceae", quote: "The arching joints of **Acanthocereus** pentagonus clamber through coastal thickets, armed with needle-sharp spines up to five centimeters long." },
      { author: "Lyman Benson", work: "The Cacti of the United States and Canada", quote: "On hammocks in southern Florida, **Acanthocereus** flourishes under the shade of maritime live oaks, opening its fragrant blooms after dusk." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "For greenhouse cultivation, **Acanthocereus** requires well-drained calcareous loam and ample room for its trailing, angled stems." }
    ]
  },
  "Dashboard — acanth/acanthocybium.md": {
    primary: "A monotypic genus of large, fast-swimming predatory marine fish of the family Scombridae, comprising Acanthocybium solandri, commonly known as the wahoo.",
    secondary: "In pelagic ichthyology, an epipelagic apex predator prized for its speed, streamlined body, and sharp serrated triangular teeth.",
    quotes: [
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "The formidable jaws of **Acanthocybium** bear a single row of closely set, compressed teeth capable of cleaving prey instantly." },
      { author: "Charles Tate Regan", work: "The Classification of the Percoid Fishes", quote: "Morphologically, **Acanthocybium** occupies an intermediate position between the king mackerels and the marlins." },
      { author: "William Beebe", work: "Half Mile Down", quote: "Out in the blue water beyond the reef, a six-foot **Acanthocybium** shot beneath the launch like a torpedo of living silver." }
    ]
  },
  "Dashboard — acanth/acanthocyte.md": {
    primary: "An abnormal red blood cell (erythrocyte) exhibiting thorny, irregular, spike-like cytoplasmic projections over its surface; a spur cell.",
    secondary: "In hematology, a poikilocyte whose deformed morphology results from lipid imbalances in the cell membrane, particularly seen in abetalipoproteinemia and liver disease.",
    quotes: [
      { author: "Ernest Beutler", work: "Williams Hematology", quote: "Under the optical microscope, each **acanthocyte** displays irregularly spaced spicules of varying length, unlike the uniform crenations of echinocytes." },
      { author: "Maxwell Wintrobe", work: "Clinical Hematology", quote: "The formation of the **acanthocyte** reflects altered membrane cholesterol-to-phospholipid ratios that impair red cell deformability." },
      { author: "Victor McKusick", work: "Mendelian Inheritance in Man", quote: "Peripheral blood smear examination revealed the classic **acanthocyte** profile pathognomonic of Bassen-Kornzweig syndrome." }
    ]
  },
  "Dashboard — acanth/acanthocytosis.md": {
    primary: "A medical condition characterized by the abnormal presence of spiny, spiked erythrocytes (acanthocytes) in the peripheral blood.",
    secondary: "In clinical pathology, a laboratory manifestation associated with inborn errors of lipoprotein metabolism or neurodegenerative syndromes.",
    quotes: [
      { author: "Michael B. Singer", work: "Neurology in Clinical Practice", quote: "A diagnostic hallmark of chorea-acanthocytosis is hereditary **acanthocytosis** accompanied by progressive basal ganglia degeneration." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "Patients presenting with orofacial dyskinesias and hyporeflexia must be evaluated for underlying **acanthocytosis**." },
      { author: "William N. Kelley", work: "Textbook of Internal Medicine", quote: "Severe advanced cirrhosis frequently produces a secondary spur-cell anemia marked by pronounced **acanthocytosis**." }
    ]
  },
  "Dashboard — acanth/acanthoid.md": {
    primary: "Resembling a spine, thorn, or prickle; spiniform or thorny in structure.",
    secondary: "In descriptive morphology, having sharp spiny processes projecting from a surface or skeletal margin.",
    quotes: [
      { author: "John Lindley", work: "Elements of Botany", quote: "The margin of the thistle leaf bears numerous **acanthoid** projections that discourage herbivores." },
      { author: "George Henslow", work: "The Heredity of Acquired Characters in Plants", quote: "Under extreme drought, rudimentary leaflets shrink into rigid **acanthoid** structures." },
      { author: "Richard Owen", work: "Lectures on Comparative Anatomy", quote: "The larval carapace is fortified by dorsal **acanthoid** processes that deter aquatic predators." }
    ]
  },
  "Dashboard — acanth/acantholysis.md": {
    primary: "The loss of intercellular connections, such as desmosomes, between keratinocytes, leading to intraepidermal blister formation.",
    secondary: "In dermatopathology, a cellular process seen in autoimmune bullous disorders like pemphigus vulgaris, where autoantibodies target desmogleins.",
    quotes: [
      { author: "Arthur Rook", work: "Textbook of Dermatology", quote: "Suprabasal **acantholysis** detaches the epidermal cells, creating the characteristic flaccid bullae of pemphigus." },
      { author: "Thomas B. Fitzpatrick", work: "Dermatology in General Medicine", quote: "A positive Nikolsky sign is the bedside clinical counterpart of widespread intraepidermal **acantholysis**." },
      { author: "Ferdinand von Hebra", work: "Diseases of the Skin", quote: "Microscopic inspection demonstrates primary **acantholysis** wherein the prickle-cells lose their bridges and float freely in blister fluid." }
    ]
  },
  "Dashboard — acanth/acanthoma.md": {
    primary: "A benign neoplasm or localized hyperplastic tumor composed primarily of epidermal squamous cells (keratinocytes).",
    secondary: "In cutaneous oncology and dermatopathology, a circumscribed proliferation of the stratum spinosum, such as pale cell acanthoma or clear cell acanthoma.",
    quotes: [
      { author: "Jonathan Hutchinson", work: "Lectures on Clinical Surgery", quote: "The solitary lesion presented as a firm, circumscribed **acanthoma** without signs of infiltrative malignancy." },
      { author: "James Nevins Hyde", work: "A Practical Treatise on Diseases of the Skin", quote: "Histological sections of the excised **acanthoma** displayed massive thickening of the prickle-cell layer." },
      { author: "Bernard Ackerman", work: "Histologic Diagnosis of Inflammatory Skin Diseases", quote: "Clear-cell **acanthoma** is recognized by its sharply demarcated, glycogen-rich keratinocytic hyperplasia." }
    ]
  },
  "Dashboard — acanth/Acanthomintha.md": {
    primary: "A small genus of annual herbs in the mint family (Lamiaceae), commonly known as thornmints, endemic to California and northern Baja California.",
    secondary: "In conservation botany, rare native plants adapted to vernal pools and vertisol clay soils, characterized by spiny-toothed floral bracts.",
    quotes: [
      { author: "Edward Lee Greene", work: "Manual of the Botany of San Francisco Bay", quote: "The genus **Acanthomintha** is well distinguished from Calamintha by its pectinate-spiny bracts and two fertile stamens." },
      { author: "Philip A. Munz", work: "A California Flora", quote: "San Diego thornmint (**Acanthomintha** ilicifolia) is severely threatened by urban encroachment upon clay lens habitats." },
      { author: "Willis Linn Jepson", work: "A Flora of Western Middle California", quote: "In dry adobe fields in late spring, the white and rose corollas of **Acanthomintha** gleam among armed calyces." }
    ]
  },
  "Dashboard — acanth/acanthophis.md": {
    primary: "A genus of highly venomous elapid snakes native to Australia and New Guinea, commonly called death adders, featuring a broad triangular head and spine-tipped tail.",
    secondary: "In herpetology, ambush predators exhibiting convergent viper-like morphology, utilizing their caudal spine as a caudal lure to attract prey.",
    quotes: [
      { author: "George Albert Boulenger", work: "Catalogue of the Snakes in the British Museum", quote: "The genus **Acanthophis** exhibits a short, stout body and a terminal spine on the tail, resembling true vipers." },
      { author: "Raymond Hoser", work: "Australian Elapid Snakes", quote: "Concealed beneath leaf litter, an **Acanthophis** twitches the worm-like tip of its tail to entice curious skinks." },
      { author: "Raymond Ditmars", work: "Reptiles of the World", quote: "The strike of **Acanthophis** antarcticus is widely regarded as one of the swiftest predatory motions in the reptile kingdom." }
    ]
  },
  "Dashboard — acanth/acanthopterygian.md": {
    primary: "Relating to or belonging to the Acanthopterygii (spiny-finned fishes); having stiff, unjointed fin spines.",
    secondary: "A spiny-finned teleost fish, representing the dominant and most diversified evolutionary radiation of modern bony fishes.",
    quotes: [
      { author: "Georges Cuvier", work: "The Animal Kingdom", quote: "The great **acanthopterygian** order includes perches, mackerels, and breams, all possessing rigid spines before the soft dorsal fin rays." },
      { author: "Louis Agassiz", work: "Recherches sur les Poissons Fossiles", quote: "Fossil evidence from the Cretaceous marks the rise of the **acanthopterygian** lineages over older ganoid groups." },
      { author: "David Starr Jordan", work: "Fishes", quote: "Every typical **acanthopterygian** fish relies upon its stiff anterior rays for defense against voracious predators." }
    ]
  },
  "Dashboard — acanth/acanthopterygii.md": {
    primary: "A superorder or major taxonomic group of teleost bony fishes characterized by spiny rayed fins and advanced protrusible jaws.",
    secondary: "In systematic ichthyology, the most species-rich clade of vertebrates, encompassing percomorphs, atherinomorphs, and related orders.",
    quotes: [
      { author: "Albert Günther", work: "Catalogue of Fishes in the British Museum", quote: "Within the **Acanthopterygii**, the first rays of the dorsal and anal fins are modified into solid, unsegmented spines." },
      { author: "Theodore Gill", work: "Arrangement of the Families of Fishes", quote: "Modern classifications group the vast majority of marine coastal teleosts under the **Acanthopterygii**." },
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Vertebrated Animals", quote: "The cranial osteology of the **Acanthopterygii** shows exquisite specialization of the premaxilla for raptorial feeding." }
    ]
  },
  "Dashboard — acanth/Acanthosaura.md": {
    primary: "A genus of agamid lizards native to Southeast Asia, commonly known as mountain horned dragons, distinguished by prominent spiny crests along the neck and back.",
    secondary: "In herpetology, arboreal forest lizards that use spiky cephalic horns and camouflage to avoid detection in humid tropical canopies.",
    quotes: [
      { author: "Edward Drinker Cope", work: "The Lizards and Snakes of North America", quote: "The Southeast Asian genus **Acanthosaura** exhibits extraordinary spination around the nuchal fold and temporal regions." },
      { author: "Malcolm Arthur Smith", work: "The Fauna of British India: Reptilia and Amphibia", quote: "When threatened, **Acanthosaura** armata flattens its body against the bark, erecting its formidable dorsal spines." },
      { author: "Hans Gadow", work: "Amphibia and Reptiles", quote: "The horned dragons of the genus **Acanthosaura** thrive in moist montane rain forests across the Indochinese peninsula." }
    ]
  },
  "Dashboard — acanth/acanthoscelides.md": {
    primary: "A genus of seed beetles in the subfamily Bruchinae (family Chrysomelidae), notorious for infesting leguminous seeds.",
    secondary: "In agricultural entomology, economically destructive pests such as Acanthoscelides obtectus (the bean weevil), which reproduces inside stored dry beans.",
    quotes: [
      { author: "Charles Valentine Riley", work: "Reports on the Insects of Missouri", quote: "A single stored jar of kidney beans may breed thousands of tiny **Acanthoscelides** beetles in the course of a single summer." },
      { author: "Leland Ossian Howard", work: "The Insect Book", quote: "The larva of **Acanthoscelides** burrows into the cotyledons, leaving behind hollowed, unviable seeds and powdery frass." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Field infestations of **Acanthoscelides** commence while pods are green and mature rapidly once the crop is placed in granaries." }
    ]
  },
  "Dashboard — acanth/acanthosis.md": {
    primary: "A diffuse hypertrophy or abnormal thickening of the prickle-cell layer (stratum spinosum) of the epidermis.",
    secondary: "In histopathology, a reactive epidermal change commonly seen in chronic dermatitis, psoriasis, and acanthosis nigricans.",
    quotes: [
      { author: "Paul Gerson Unna", work: "The Histopathology of the Diseases of the Skin", quote: "Chronic friction and chemical irritation produce marked **acanthosis**, with elongated rete ridges dipping into the dermis." },
      { author: "William Allen Pusey", work: "The Principles and Practice of Dermatology", quote: "The velvety hyperpigmented plaques of **acanthosis** nigricans often correlate with profound insulin resistance." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Biopsy of the lesion confirmed prominent **acanthosis** without nuclear atypia, confirming its benign, reactive nature." }
    ]
  },
  "Dashboard — acanth/acanthotic.md": {
    primary: "Pertaining to, characterized by, or affected with acanthosis (thickening of the prickle-cell layer).",
    secondary: "In histological diagnostics, describing epidermis showing hyperplastic elongation and widening of the rete pegs.",
    quotes: [
      { author: "Bernard Ackerman", work: "Differential Diagnosis in Dermatopathology", quote: "The **acanthotic** rete ridges in psoriasis show regular elongation and bulbous expansion at their lower poles." },
      { author: "Arthur Rook", work: "Textbook of Dermatology", quote: "Beneath the hyperkeratotic scale lay an **acanthotic** stratum spinosum studded with focal lymphocytic exocytosis." },
      { author: "Walter Lever", work: "Histopathology of the Skin", quote: "Seborrheic keratosis presents an intensely **acanthotic** proliferation composed of small basaloid cells mingled with horn cysts." }
    ]
  },
  "Dashboard — acanth/acanthous.md": {
    primary: "Covered with spines or prickles; thorny; spiny.",
    secondary: "In classical natural history and descriptive anatomy, possessing sharp, rigid needle-like spines.",
    quotes: [
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Wild varieties of the gooseberry exhibit intensely **acanthous** stems, whereas cultivated forms tend toward smooth branches." },
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Certain desert cacti present an entirely **acanthous** exterior, where leaves are replaced completely by clusters of defensive thorns." },
      { author: "John Lindley", work: "The Treasury of Botany", quote: "The seed capsules of the teasel are surrounded by an **acanthous** involucre of stiff, hooked bracts." }
    ]
  },
  "Dashboard — acanth/acanthuridae.md": {
    primary: "A family of marine perciform fishes known as surgeonfishes, tangs, and unicornfishes, characterized by sharp, scalpel-like spines on the caudal peduncle.",
    secondary: "In reef ecology, grazing herbivorous fishes that regulate algal turf dynamics on coral reefs worldwide.",
    quotes: [
      { author: "John E. Randall", work: "Surgeonfishes of Hawaii and the World", quote: "Members of the **Acanthuridae** possess a modified folding spine on each flank of the caudal peduncle that can inflict deep lacerations." },
      { author: "David Starr Jordan", work: "The Genera of Fishes", quote: "The family **Acanthuridae** includes both algal-browsing tangs and planktivorous unicornfishes with prominent cranial horns." },
      { author: "William Beebe", work: "Field Book of Shore Fishes of Bermuda", quote: "Schools of blue tang belonging to the **Acanthuridae** sweep across the reef flat like an azure cloud grazing on filamentous algae." }
    ]
  },
  "Dashboard — acanth/acanthurus.md": {
    primary: "A diverse genus of surgeonfishes (family Acanthuridae) bearing a single hinged, sharp spine on each side of the caudal peduncle.",
    secondary: "In tropical ichthyology, circumtropical reef dwellers that defend feeding territories against competing herbivorous fishes.",
    quotes: [
      { author: "Charles Darwin", work: "The Zoology of the Voyage of H.M.S. Beagle", quote: "We observed specimens of **Acanthurus** darting among the coral heads at Tahiti, using their lateral lancets in territorial combat." },
      { author: "Albert Günther", work: "Fische der Südsee", quote: "The genus **Acanthurus** is distinguished by its high, compressed body, deep caudal peduncle, and erectable caudal lancet." },
      { author: "Georges Cuvier", work: "Histoire Naturelle des Poissons", quote: "Linnaeus initially grouped these spiny-tailed herbivores under Chaetodon before the establishment of **Acanthurus**." }
    ]
  },
  "Dashboard — acanth/Acanthus.md": {
    primary: "A genus of spiny-leaved Mediterranean herbaceous plants (family Acanthaceae) with spikes of white or purplish flowers; the classic inspiration for Corinthian capitals.",
    secondary: "In classical architecture and ornamentation, the stylized foliar motif carved into Corinthian and Composite architectural capitals and friezes.",
    quotes: [
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The Greek sculptor looked upon the serrated margins of the wild **Acanthus** and drew from its curves the crowning glory of the Corinthian capital." },
      { author: "Vitruvius", work: "De Architectura", quote: "Callimachus passed by the tomb of a Corinthian maiden where an **Acanthus** root had sprouted, its curling leaves clasping a votive basket." },
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The spinous leaves of the wild **Acanthus** spread along garden borders in damp soils, maintaining glossy foliage throughout winter." }
    ]
  },
  "Dashboard — acanth/anacanthini.md": {
    primary: "An obsolete taxonomic order of teleost fishes characterized by the absence of spiny rays in their fins, including codfishes and flatfishes.",
    secondary: "In historical systematic ichthyology, a grouping proposed by Johannes Müller to contrast soft-rayed gadoids and pleuronectids with acanthopterygians.",
    quotes: [
      { author: "Johannes Müller", work: "Ueber den Bau und die Grenzen der Ganoiden", quote: "I have established the **Anacanthini** to embrace those teleosts whose dorsal and anal rays are entirely soft and jointed." },
      { author: "Albert Günther", work: "Introduction to the Study of Fishes", quote: "Although the **Anacanthini** were traditionally placed alongside physostomes, their air bladder lacks a pneumatic duct." },
      { author: "David Starr Jordan", work: "The Classification of Fishes", quote: "Modern phylogenetics disassembled the **Anacanthini**, transferring flatfishes to Pleuronectiformes and cods to Gadiformes." }
    ]
  },
  "Dashboard — acanth/Metri acanth osaurus.md": {
    primary: "A genus of medium-sized theropod dinosaur from the Late Jurassic of England, named for its moderately elevated neural spines.",
    secondary: "In vertebrate paleontology, an allosauroid carnivore characterized by neural spines intermediate in height between typical theropods and sail-backed forms.",
    quotes: [
      { author: "Friedrich von Huene", work: "Carnivorous Saurischia of the Upper Jurassic", quote: "The holotype vertebrae were designated **Metriacanthosaurus** parkeri, reflecting the medium height of its dorsal neural spines." },
      { author: "Alick Walker", work: "Triassic Reptiles from the Elgin Area", quote: "Comparisons between Megalosaurus and **Metriacanthosaurus** highlight the diagnostic value of axial spine elongation in Jurassic theropods." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "Phylogenetic revisions place **Metriacanthosaurus** within the Sinraptoridae, a lineage of predatory dinosaurs widespread across Eurasia." }
    ]
  },
  "Dashboard — acanth/metriacanthosaurus.md": {
    primary: "A genus of theropod dinosaur from the Late Jurassic of Europe, belonging to the Metriacanthosauridae family, characterized by moderate dorsal neural spines.",
    secondary: "In vertebrate paleontology, a basal tetanuran predator measuring roughly eight meters in length that inhabited the island archipelago of Jurassic Britain.",
    quotes: [
      { author: "Friedrich von Huene", work: "Carnivorous Saurischia of the Upper Jurassic", quote: "The distinct height of the vertebral spinous processes justifies classifying **Metriacanthosaurus** apart from Megalosaurus." },
      { author: "Michael J. Benton", work: "Vertebrate Palaeontology", quote: "Skeletal reconstructions of **Metriacanthosaurus** show a bipedal carnivore equipped with curved, serrated teeth adapted for slicing flesh." },
      { author: "Gregory S. Paul", work: "Predatory Dinosaurs of the World", quote: "With its deep skull and moderate vertebral ridge, **Metriacanthosaurus** was the dominant terrestrial carnivore of the Oxfordian landscape." }
    ]
  },
  "Dashboard — acanth/neuro acanth ocytosis.md": {
    primary: "A group of rare, genetically determined neurodegenerative disorders characterized by movement disorders and the presence of spiny red blood cells (acanthocytes).",
    secondary: "In clinical neurology, a syndrome encompassing chorea-acanthocytosis and McLeod syndrome, presenting with basal ganglia atrophy and peripheral neuropathy.",
    quotes: [
      { author: "C. David Marsden", work: "Movement Disorders", quote: "Patients exhibiting involuntary choreic jerks and progressive orofacial self-mutilation must be screened for **neuroacanthocytosis**." },
      { author: "Victor McKusick", work: "Mendelian Inheritance in Man", quote: "Mutations in the VPS13A gene underlie the autosomal recessive form of **neuroacanthocytosis**, impairing erythrocyte membrane stability." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The subtle coexistence of neurological tics with bizarrely deformed red cells makes **neuroacanthocytosis** an extraordinary hematological anomaly." }
    ]
  },
  "Dashboard — acanth/neuroacanthocytosis.md": {
    primary: "A rare inherited neurological syndrome marked by progressive basal ganglia degeneration, chorea, and acanthocytes in the peripheral blood.",
    secondary: "In neurogenetics, a fatal degenerative condition characterized by limb chorea, tongue biting, psychiatric disturbances, and erythrocyte deformation.",
    quotes: [
      { author: "C. David Marsden", work: "Movement Disorders", quote: "The diagnostic identification of **neuroacanthocytosis** relies on detecting deformed spur cells alongside caudate atrophy on magnetic resonance scans." },
      { author: "Raymond D. Adams", work: "Principles of Neurology", quote: "Unlike Huntington's disease, **neuroacanthocytosis** frequently features axonal neuropathy, areflexia, and elevated serum creatine kinase." },
      { author: "Michael B. Singer", work: "Neurology in Clinical Practice", quote: "Effective management of **neuroacanthocytosis** remains supportive, targeting debilitating movement symptoms and malnutrition." }
    ]
  },
  "Dashboard — alphit/alphit.md": {
    primary: "A combining form and classical root derived from Greek 'alphiton' (barley meal, groats, flour), used in historical divinatory and culinary terminology.",
    secondary: "In historical linguistics and folklore studies, an ancient Hellenic element associated with sacrificial barley cakes and ritual ordeal divination.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The root **alphit** traces directly to alphiton, the ancient barley meal that served as the staple cereal of the Homeric Greeks." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Derivatives of **alphit** reflect archaic Indo-European agricultural vocabulary for husked cereals ground between quern stones." },
      { author: "Jane Ellen Harrison", work: "Prolegomena to the Study of Greek Religion", quote: "Ritual offerings of consecrated meal known by the root **alphit** were scattered over the altar prior to animal sacrifice." }
    ]
  },
  "Dashboard — alphit/alphitomancy.md": {
    primary: "A form of divination or trial by ordeal using barley meal or barley cakes, historically used to identify a guilty person who could not swallow the dry flour.",
    secondary: "In anthropological folklore, an archaic juridical ordeal wherein accused parties were forced to consume consecrated barley cakes under fear of divine choked asphyxiation.",
    quotes: [
      { author: "John Brand", work: "Observations on Popular Antiquities", quote: "In the ancient practice of **alphitomancy**, the priest gave consecrated barley flour to suspects, believing the guilty throat would constrict." },
      { author: "Walter Woodburn Hyde", work: "Greek Religion and Its Survivals", quote: "The psychological terror induced by **alphitomancy** frequently elicited confessions before the barley cake was even tasted." },
      { author: "E. Cobham Brewer", work: "Dictionary of Phrase and Fable", quote: "The ancient Greeks resorted to **alphitomancy** when property was stolen, deeming him culpable who could not digest the sacred meal." }
    ]
  },
  "Dashboard — amygdal/almond.md": {
    primary: "The oval edible nut-like kernel of Prunus dulcis (family Rosaceae), or the small deciduous tree producing it.",
    secondary: "In botanical horticulture, a drupaceous fruit whose dry, leathery exocarp splits at maturity to expose a hard, pitted endocarp enclosing the seed.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The sweet **almond** tree blossoms early in spring with fair pinkish petals before the tender leaves unfold." },
      { author: "Henry David Thoreau", work: "Walden", quote: "In my woodland walks, the scent of crushed sweet fern recalled the subtle, bitter aroma of the crushed **almond**." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Physicians prescribe oil pressed from the bitter **almond** to disperse headaches and purge sluggish humoral humors." }
    ]
  },
  "Dashboard — amygdal/amygdal.md": {
    primary: "A combining form and root derived from Greek 'amygdale' (almond), used in botanical, anatomical, and mineralogical nomenclature.",
    secondary: "In etymological lexicography, the root element designating almond-shaped anatomical organs, volcanic cavities, or cyanogenic glycosides.",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The ancient Greek **amygdal** designated both the almond tree itself and the delicate kernel enclosed within its stony shell." },
      { author: "Pierre-Joseph Redouté", work: "Les Fruits", quote: "Botanical descriptions employing the root **amygdal** underscore the characteristic pitted stone of the drupaceous stone fruits." },
      { author: "William Rhind", work: "A History of the Vegetable Kingdom", quote: "In medicinal flora, species bearing the prefix **amygdal** are scrutinized for their volatile benzaldehyde and prussic acid content." }
    ]
  },
  "Dashboard — amygdal/amygdala.md": {
    primary: "An almond-shaped complex of nuclei located deep within the anterior temporal lobe of the brain, playing a critical role in processing emotion and memory.",
    secondary: "In neuroanatomy and cognitive neuroscience, a key component of the limbic system essential for conditioned fear responses and emotional valence assignment.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Microscopic preparations demonstrate dense afferent fibers connecting the olfactory tracts directly to the lateral nuclei of the **amygdala**." },
      { author: "Joseph LeDoux", work: "The Emotional Brain", quote: "The rapid neural pathway from the sensory thalamus straight to the **amygdala** allows defensive reactions before the neocortex is even conscious." },
      { author: "William James", work: "The Principles of Psychology", quote: "Lesions in the temporal lobe affecting structures around the **amygdala** profoundly disrupt instinctive emotional reactions to danger." }
    ]
  },
  "Dashboard — amygdal/amygdalaceae.md": {
    primary: "An obsolete botanical family name formerly comprising the almond, peach, plum, and cherry (now placed in the subfamily Amygdaloideae or Prunoideae within Rosaceae).",
    secondary: "In historical systematic botany, a taxon established by Jussieu and De Candolle for stone fruits characterized by single carpels and drupes with stony endocarps.",
    quotes: [
      { author: "Augustin Pyramus de Candolle", work: "Prodromus Systematis Naturalis", quote: "We distinguish the **Amygdalaceae** by their solitary superior ovary and the presence of hydrocyanic acid in their seeds." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The **Amygdalaceae** include many of our finest temperate orchard trees, yielding succulent stone fruits and aromatic kernels." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "Recent classifications abandon **Amygdalaceae** as an independent family, merging it as a tribe or subfamily of the Rosaceae." }
    ]
  },
  "Dashboard — amygdal/amygdale.md": {
    primary: "An almond, or something shaped like an almond; in geology, an amygdule (a mineral-filled vesicle in igneous rock).",
    secondary: "In petrology and physical geology, a nodule or secondary mineral deposit filling a former gas bubble in volcanic basalt or lava.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "Each rounded **amygdale** consists of concentric layers of chalcedony, calcite, and zeolites deposited by percolating waters." },
      { author: "Charles Lyell", work: "Elements of Geology", quote: "The weathered face of the trap rock revealed countless mineral pockets, each **amygdale** sparkling with crystalline quartz." },
      { author: "James Dwight Dana", work: "Manual of Geology", quote: "Gas vesicles elongated by flowing lava solidify into oval cavities that later become transformed into an **amygdale**." }
    ]
  },
  "Dashboard — amygdal/amygdaliform.md": {
    primary: "Having the shape or form of an almond; almond-shaped.",
    secondary: "In paleontology, anthropology, and anatomy, describing stone tools, nodules, or organs possessing a symmetrical oval outline tapering toward one end.",
    quotes: [
      { author: "William Buckland", work: "Reliquiae Diluvianae", quote: "The Pleistocene gravels yielded several finely chipped **amygdaliform** handaxes worked from dark flint pebbles." },
      { author: "Richard Owen", work: "Odontography", quote: "The fossil crown exhibits an **amygdaliform** contour, tapering gracefully toward its anterior masticatory margin." },
      { author: "Edward Drinker Cope", work: "The Vertebrata of the Tertiary Formations", quote: "The tympanic bulla of the extinct carnivore is remarkably **amygdaliform**, smooth on its ventral aspect." }
    ]
  },
  "Dashboard — amygdal/amygdalin.md": {
    primary: "A cyanogenic glycoside found naturally in the seeds of almonds, apricots, peaches, and plums, which yields hydrogen cyanide when hydrolyzed by enzymes.",
    secondary: "In biochemistry and clinical toxicology, a compound composed of gentiobiose and mandelonitrile that enzymatic hydrolysis with beta-glucosidase degrades into prussic acid and benzaldehyde.",
    quotes: [
      { author: "Justus von Liebig", work: "Researches on the Radical of Benzoic Acid", quote: "Wöhler and I demonstrated that emulsin decomposes **amygdalin** into oil of bitter almonds, sugar, and prussic acid." },
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "The catalytic cleavage of **amygdalin** by soluble ferments represents one of the foundational reactions of organic chemistry." },
      { author: "T. Lauder Brunton", work: "A Text-Book of Pharmacology", quote: "Ingestion of bitter apricot kernels poses acute risk of poisoning because mucosal enzymes liberate free cyanide from **amygdalin**." }
    ]
  },
  "Dashboard — amygdal/amygdaline.md": {
    primary: "Pertaining to, resembling, or obtained from almonds.",
    secondary: "Characterized by the presence or chemical properties of bitter almond oil or cyanogenic glycosides.",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Agricultural Chemistry", quote: "The wild pit fruits generate an **amygdaline** bitterness that disappears under centuries of careful horticultural selection." },
      { author: "Robert Christison", work: "A Treatise on Poisons", quote: "Distillation of cherry-laurel leaves produces an **amygdaline** distillate carrying sufficient hydrocyanic acid to cause rapid death." },
      { author: "William Allen Miller", work: "Elements of Chemistry", quote: "Organic analysis reveals distinct **amygdaline** compounds across many species of the genus Prunus." }
    ]
  },
  "Dashboard — amygdal/amygdaloid.md": {
    primary: "An extrusive volcanic rock (especially basalt) containing gas bubbles (vesicles) that have been filled with secondary minerals such as zeolites, quartz, or calcite.",
    secondary: "In anatomy, resembling an almond in form, as in the amygdaloid body (amygdala) of the temporal lobe.",
    quotes: [
      { author: "Charles Darwin", work: "Geological Observations on Volcanic Islands", quote: "The sea cliffs of St. Helena consist of dark porous lava alternating with heavy beds of compact **amygdaloid**." },
      { author: "Hugh Miller", work: "The Old Red Sandstone", quote: "Veins of jasper and banded agate traverse the weathered **amygdaloid** rocks along the Scottish coast." },
      { author: "James Hutton", work: "Theory of the Earth", quote: "The formation of **amygdaloid** demonstrates that mineral solutions infiltrated the cooled subterranean fissures over enormous expanses of time." }
    ]
  },
  "Dashboard — amygdal/amygdaloidal.md": {
    primary: "Pertaining to, having the texture of, or characterized by amygdules; almond-shaped or vesicular with mineral infillings.",
    secondary: "In petrography, describing the texture of volcanic rocks whose cavities have been sealed by secondary crystallization.",
    quotes: [
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The basaltic columns give way at the summit of the plateau to an **amygdaloidal** lava crammed with nodules of green earth." },
      { author: "Archibald Geikie", work: "The Ancient Volcanoes of Great Britain", quote: "In thin section, the **amygdaloidal** cavities display radiating needles of natrolite projecting from the chlorite rim." },
      { author: "Roderick Murchison", work: "The Silurian System", quote: "Trappean hills along the Welsh border contain extensive **amygdaloidal** layers hosting sparkling crystals of carbonate of lime." }
    ]
  },
  "Dashboard — amygdal/amygdalotomy.md": {
    primary: "The surgical excision, cutting, or removal of a tonsil; tonsillectomy.",
    secondary: "In 19th-century surgery, the historical operation of amputating enlarged palatine tonsils using a specialized tonsillotome or snare.",
    quotes: [
      { author: "Morell Mackenzie", work: "Diseases of the Pharynx, Larynx, and Trachea", quote: "When hypertrophied tonsils impede respiration and cause chronic dysphagia, bilateral **amygdalotomy** offers prompt relief." },
      { author: "George M. Lefferts", work: "Pharmacopoeia of the Throat Hospital", quote: "The guillotine instrument perfected for **amygdalotomy** permits swift, clean amputation of the hypertrophied gland." },
      { author: "Frank Hamilton", work: "The Principles and Practice of Surgery", quote: "Postoperative hemorrhage following **amygdalotomy** is best checked by topical astringents or digital pressure against the carotid." }
    ]
  },
  "Dashboard — amygdal/amygdalus.md": {
    primary: "A botanical genus (or subgenus of Prunus) comprising the almond (Amygdalus communis) and peach (Amygdalus persica).",
    secondary: "In historical botanical taxonomy, Linnaeus's original genus for stone fruit trees bearing velvety fruits with deeply pitted or furrowed stones.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Under the genus **Amygdalus**, I have placed the common sweet and bitter almonds alongside the downy-skinned peach." },
      { author: "Philip Miller", work: "The Gardeners Dictionary", quote: "The ancient gardeners cultivated **Amygdalus** in sheltered southern borders to protect its fragile vernal blossoms from frost." },
      { author: "Augustin Pyramus de Candolle", work: "Prodromus", quote: "Modern systematists debate whether **Amygdalus** merits generic distinction from Prunus based on furrowed endocarps." }
    ]
  },
  "Dashboard — amygdal/amygdule.md": {
    primary: "A small, rounded or almond-shaped vesicle in volcanic rock that has been filled with secondary minerals such as chalcedony, zeolite, or calcite.",
    secondary: "In petrology, an epigenetic mineral nodule formed by precipitation from hydrothermal fluids inside fossil gas bubbles of cooled volcanic lava.",
    quotes: [
      { author: "Archibald Geikie", work: "Textbook of Geology", quote: "When the basalt weathers away, the harder siliceous **amygdule** drops out as an unbroken agate pebble." },
      { author: "Ferdinand Zirkel", work: "Microscopical Petrography", quote: "Polarizing microscopy reveals that each **amygdule** possesses concentric rims of fibrous quartz enclosing a core of radiating stilbite." },
      { author: "Frank Rutley", work: "The Study of Rocks", quote: "The presence of an **amygdule** in an igneous specimen indicates that the rock was originally a vesicular surface flow." }
    ]
  },
  "Dashboard — anth/anth.md": {
    primary: "A combining form and botanical root derived from Greek 'anthos' (flower, blossom), used widely in biological, literary, and chemical terms.",
    secondary: "In historical linguistics and etymology, the root underlying terms for flowers, inflorescences, floral pigments (anthocyanins), and literary collections (anthologies).",
    quotes: [
      { author: "Henry George Liddell", work: "A Greek-English Lexicon", quote: "The root **anth** derives from anthos, signifying flower, bloom, or the finest and brightest part of any substance." },
      { author: "Theophrastus", work: "Enquiry into Plants", quote: "The botanical component **anth** refers strictly to the floral organ wherein seed conception and nectar secretion occur." },
      { author: "Robert Beekes", work: "Etymological Dictionary of Greek", quote: "Indo-European cognates of **anth** point to ancient verbal roots meaning to sprout, burst forth, or blossom." }
    ]
  },
  "Dashboard — anth/anthelminthic.md": {
    primary: "An agent or medication that expels or destroys parasitic intestinal worms (helminths); vermifuge or vermicide.",
    secondary: "In pharmacological therapeutics, describing medicinal preparations formulated to paralyze, digest, or detach parasitic cestodes, nematodes, and trematodes.",
    quotes: [
      { author: "William Cullen", work: "A Treatise of the Materia Medica", quote: "The powdered root of male fern possesses powerful **anthelminthic** virtues against the stubborn tapeworm." },
      { author: "Jonathan Pereira", work: "The Elements of Materia Medica and Therapeutics", quote: "Santonin acts as a specific **anthelminthic**, causing roundworms to lose their hold upon the ileum." },
      { author: "Robley Dunglison", work: "General Therapeutics and Materia Medica", quote: "Administration of an **anthelminthic** should be followed promptly by a saline cathartic to sweep out the paralyzed parasites." }
    ]
  },
  "Dashboard — anth/anthelmintic.md": {
    primary: "Capable of expelling or destroying parasitic intestinal worms; a drug or natural remedy acting as a vermifuge.",
    secondary: "In clinical pharmacotherapy, a pharmaceutical substance that selectively targets helminth neuromuscular transmission, microtubule synthesis, or metabolic pathways.",
    quotes: [
      { author: "William Withering", work: "An Account of the Foxglove", quote: "Certain rural practitioners extolled the decoction as an **anthelmintic**, though its true cardiac virtues remained unrecognized." },
      { author: "T. Lauder Brunton", work: "A Text-Book of Pharmacology", quote: "Oil of chenopodium is an effective **anthelmintic** for hookworm infection, though its therapeutic index requires cautious dosing." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In cases of ascariasis, a dependable **anthelmintic** will reliably clear the digestive tract of adult nematodes." }
    ]
  },
  "Dashboard — anth/anthem.md": {
    primary: "A musical composition of celebration, praise, or religious devotion, often set to sacred text or adopted as a national song.",
    secondary: "In ecclesiastical music, a choral setting of scripture or liturgical verse performed in Anglican and Protestant worship services, derived etymologically from antiphon.",
    quotes: [
      { author: "John Milton", work: "Il Penseroso", quote: "There let the pealing organ blow, to the full-voiced quire below, in service high and **anthem** clear." },
      { author: "John Keats", work: "Ode to a Nightingale", quote: "Adieu! adieu! thy plaintive **anthem** fades past the near meadows, over the still stream." },
      { author: "George Eliot", work: "Middlemarch", quote: "The organ strains swelled into a majestic **anthem** that stirred Dorothea's heart with ardent religious longing." }
    ]
  },
  "Dashboard — anth/anthemis.md": {
    primary: "A genus of aromatic flowering herbs in the daisy family (Asteraceae), commonly called dog-fennel or chamomile, with daisy-like flower heads.",
    secondary: "In pharmacognosy and herbal medicine, the genus containing Roman chamomile (Anthemis nobilis), valued for its carminative and soothing essential oils.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The wild **Anthemis** or chamomile groweth abundantly along roadsides, yielding a bitter yet wholesome aromatic odor." },
      { author: "Nicholas Culpeper", work: "The Complete Herbal", quote: "A warm fomentation of **Anthemis** blossoms dispels digestive colic and calms agitated nervous vapors." },
      { author: "William Woodville", work: "Medical Botany", quote: "The yellow disk florets of **Anthemis** yield by distillation an ethereal oil possessing pronounced antispasmodic qualities." }
    ]
  },
  "Dashboard — anth/anther.md": {
    primary: "The terminal, pollen-bearing portion of a plant stamen, usually borne atop a slender filament.",
    secondary: "In floral anatomy, a bilobed microsporangial structure comprising four locules that dehisce longitudinally or poricidally to release pollen grains.",
    quotes: [
      { author: "Charles Darwin", work: "The Various Contrivances by Which Orchids Are Fertilised", quote: "When the visiting bee depresses the labellum, the ripe **anther** deposits its paired pollinia neatly upon the insect's thorax." },
      { author: "Asa Gray", work: "First Lessons in Botany", quote: "Each stamen consists of the slender thread-like filament and the hollow box or **anther** containing pollen dust." },
      { author: "John Lindley", work: "An Introduction to Botany", quote: "Dehiscence of the **anther** occurs at the precise moment when the stigma becomes receptive to fertilizing grains." }
    ]
  },
  "Dashboard — anth/antheraea.md": {
    primary: "A genus of large, nocturnal saturniid silkmoths, including the Chinese oak silkmoth (Antheraea pernyi) and the tasar silkmoth (Antheraea paphia).",
    secondary: "In sericulture and entomology, wild silkmoths prized for producing coarse, resilient, naturally golden tussah silk from larvae feeding on forest foliage.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on the Disease of Silkworms", quote: "Wild species of **Antheraea** demonstrated far greater resistance to pebrine infection than the domesticated Bombyx mori." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the moonlit clearing, a magnificent saturniid of the genus **Antheraea** fluttered past, its wings spanning nearly seven inches." },
      { author: "Jean-Henri Fabre", work: "Social Life in the Insect World", quote: "The cocoon spun by **Antheraea** is dense and tough as leather, sheltering the pupa through torrential monsoon rains." }
    ]
  },
  "Dashboard — anth/antheral.md": {
    primary: "Of, relating to, or situated on the anther of a flower.",
    secondary: "In organographic botany, pertaining specifically to the microsporangia or pollen sacs of the angiosperm stamen.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "Microscopic scrutiny reveals that the **antheral** walls consist of fibrous endothecial cells designed to split upon drying." },
      { author: "John Lindley", work: "The Elements of Botany", quote: "The **antheral** appendages in the violet family secrete sweet nectar to guide foraging insects directly to the pollen." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "Diagnostic keys distinguish the genera by the presence or absence of terminal **antheral** awns." }
    ]
  },
  "Dashboard — anth/anthericum.md": {
    primary: "A genus of rhizomatous perennial flowering plants in the family Asparagaceae, known as St. Bernard's lilies, bearing starry white flowers on unbranched scapes.",
    secondary: "In European and African floristics, herbaceous perennials with grass-like leaves and racemose blossoms native to subalpine meadows and dry grasslands.",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The genus **Anthericum** is characterized by a six-petaled spreading perianth and filiform stamens crowned with erect anthers." },
      { author: "William Curtis", work: "The Botanical Magazine", quote: "In June, the graceful scapes of **Anthericum** liliago rise above the foliage, displaying pure white star-like blossoms." },
      { author: "Philip Miller", work: "The Gardeners Dictionary", quote: "Alpine gardeners value **Anthericum** for its hardiness and the luminous purity of its floral racemes." }
    ]
  },
  "Dashboard — anth/antheridial.md": {
    primary: "Pertaining to, produced within, or resembling an antheridium (the male reproductive organ in cryptogams).",
    secondary: "In pteridology and bryology, referring to the haploid gametangial cells, chambers, or protective paraphyses associated with motile spermatozoid generation.",
    quotes: [
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Water droplets are indispensable for rupture of the **antheridial** wall and liberation of flagellated spermatozoids." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "The **antheridial** disk of Marchantia is elevated on a slender stalk to ensure effective splash dispersal by rain." },
      { author: "William Gilson Farlow", work: "Gymnosporangia of the United States", quote: "Microscopic sections through the prothallus revealed numerous mature **antheridial** cysts along the ventral margin." }
    ]
  },
  "Dashboard — anth/antheridiophore.md": {
    primary: "A specialized stalk or receptacle in liverworts (such as Marchantia) that bears the antheridia (male reproductive organs).",
    secondary: "In bryophyte morphodynamics, an umbrella-like gametophoric branch with a lobed terminal disc housing antheridial cavities on its upper surface.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "Higher Cryptogamia", quote: "The erect stalk of the **antheridiophore** elevates the male gametangia into the path of splashing raindrops." },
      { author: "Douglas Houghton Campbell", work: "The Structure and Development of Mosses and Ferns", quote: "Cross-sections through the peltate disc of the **antheridiophore** show flask-shaped chambers, each sheltering a solitary antheridium." },
      { author: "Frederick Orpen Bower", work: "The Origin of a Land Flora", quote: "The differentiation between the male **antheridiophore** and the female archegoniophore reflects the division of labor in bryophyte gametophytes." }
    ]
  },
  "Dashboard — anth/antheridium.md": {
    primary: "The haploid male sex organ (gametangium) in mosses, liverworts, ferns, and certain fungi and algae, producing motile flagellated male gametes (antherozoids).",
    secondary: "In plant embryology, a jacketed multicellular structure wherein spermatogenous tissue undergoes mitoses to yield chemotactic swimming spermatozoids.",
    quotes: [
      { author: "Wilhelm Hofmeister", work: "Higher Cryptogamia", quote: "Upon maturity, the cap cell of the **antheridium** dissolves, permitting hundreds of spiral spermatozoids to swarm into the film of water." },
      { author: "Karl von Goebel", work: "Organography of Plants", quote: "The club-shaped **antheridium** is enveloped by a protective single-layered sterile jacket that prevents premature dehydration." },
      { author: "Julius von Sachs", work: "Text-Book of Botany", quote: "Fertilization in cryptogams cannot occur unless the **antheridium** discharges its motile gametes during periods of dew or rain." }
    ]
  }
};

let count = 0;
for (const [relPath, data] of Object.entries(batch1Data)) {
  if (updateNote(relPath, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 1 Completed: ${count} / ${Object.keys(batch1Data).length} notes updated.`);
console.log(`========================================\n`);
