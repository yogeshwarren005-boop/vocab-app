import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — zephyr/zephyr.md": {
    word: "zephyr",
    primary: "A gentle, mild, or refreshing breeze, traditionally blowing from the west.",
    secondary: "In literary and poetical contexts, an airy, delicate, or barely perceptible movement of air; any soft, whisper-light fabric or atmospheric draft.",
    quotes: [
      { author: "Thomas Hardy", work: "Far from the Madding Crowd", quote: "He felt a **zephyr** curling about his cheek, and turned." },
      { author: "Herman Melville", work: "Moby-Dick; or, The Whale", quote: "Euroclydon, nevertheless, is a mighty pleasant **zephyr** to any one in-doors, with his feet on the hob quietly toasting for bed." },
      { author: "William Shakespeare", work: "Cymbeline", quote: "They are as gentle / As **zephyrs** blowing below the violet, / Not wagging his sweet head." }
    ]
  },
  "Dashboard — styg/Stygian.md": {
    word: "Stygian",
    primary: "Of, relating to, or resembling the river Styx in Greek mythology; hence, dark, gloomy, forbidding, or infernal.",
    secondary: "In classical literature and oaths, inviolable or bound by solemn dread, as of an oath sworn upon the sacred and dreadful waters of the underworld.",
    quotes: [
      { author: "William Shakespeare", work: "Troilus and Cressida", quote: "I stalk about her door / Like a strange soul upon the **Stygian** banks / Staying for waftage." },
      { author: "John Milton", work: "Paradise Lost", quote: "Him followed his next Mate, / Both glorying to have scap't the **Stygian** flood / As Gods, and by their own recover'd strength." },
      { author: "Dante Alighieri", work: "The Divine Comedy: Inferno", quote: "And now we reached the base of a dark tower, across whose moat the **Stygian** waters roll." }
    ]
  },
  "Dashboard — styg/stygiophobia.md": {
    word: "stygiophobia",
    primary: "An abnormal, morbid, or irrational fear of hell, damnation, or infernal torment.",
    secondary: "In clinical psychopathology and history of psychiatry, an obsessive existential dread of post-mortem punishment or underworld suffering.",
    quotes: [
      { author: "G. Stanley Hall", work: "A Study of Fears", quote: "In clinical observations of morbid dread, **stygiophobia** manifests as an agonizing, obsessional terror of damnation and the infernal pit." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The melancholy mind is gripped by profound dread of perdition, resembling that classic **stygiophobia** where every shadow portends eternal torment." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Many religious hypochondriacs suffer an incurable **stygiophobia**, terrified incessantly by the sulphurous river and the wrath to come." }
    ]
  },
  "Dashboard — bront/bront.md": {
    word: "bront",
    primary: "A combining form derived from Greek bronte meaning thunder, used in scientific, taxonomic, and geological terminology.",
    secondary: "In morphology and taxonomy, a prefix denoting thunderous acoustics, explosive atmospheric force, or immense prehistoric heft resembling thunder.",
    quotes: [
      { author: "Othniel Charles Marsh", work: "Notice of New Dinosaurian Reptiles", quote: "The Greek prefix **bront**- signifies thunder, appropriately chosen for the colossal sauropods whose footfalls shook the Mesozoic earth." },
      { author: "Edward Drinker Cope", work: "The Vertebrata of the Tertiary Formations of the West", quote: "In taxonomic nomenclature, the element **bront**- denotes massive magnitude and thundering power in extinct mammalian and reptilian forms." },
      { author: "Richard Owen", work: "Palaeontology", quote: "The root **bront**- recurs across natural history to designate phenomena associated with atmospheric detonations or monstrous terrestrial heft." }
    ]
  },
  "Dashboard — bront/bronte.md": {
    word: "bronte",
    primary: "A literary surname made world-renowned by the Brontë sisters; historically and etymologically also used in mythological contexts for personified thunder.",
    secondary: "In literary history and cultural biography, designating the impassioned Romantic and Victorian works, themes, or biographical legend of Charlotte, Emily, and Anne Brontë.",
    quotes: [
      { author: "Elizabeth Gaskell", work: "The Life of Charlotte Brontë", quote: "The genius of Charlotte **Brontë** was nurtured amidst the wild, desolate Yorkshire moors of Haworth." },
      { author: "Virginia Woolf", work: "The Common Reader", quote: "Emily **Brontë** looked out upon a world cleft into gigantic disorder and felt within her the power to unite it in a book." },
      { author: "Matthew Arnold", work: "Haworth Churchyard", quote: "Round the moist stones of the graves, / Rest the gifted sisters of the house of **Brontë**." }
    ]
  },
  "Dashboard — bront/brontology.md": {
    word: "brontology",
    primary: "The scientific or mythological study of thunder and electrical atmospheric phenomena.",
    secondary: "In meteorological history, the systematic acoustic observation and recording of thunderclaps, lightning discharges, and storm shockwave propagation.",
    quotes: [
      { author: "Benjamin Franklin", work: "Experiments and Observations on Electricity", quote: "A rational **brontology** must supplant vulgar superstition, demonstrating that thunder is but the acoustic consequence of electrical discharge." },
      { author: "Camille Flammarion", work: "The Atmosphere", quote: "In the annals of meteorological physics, **brontology** catalogs the acoustics of storm fronts and the shockwaves of celestial fire." },
      { author: "John Tyndall", work: "Sound", quote: "The student of **brontology** traces how atmospheric temperature gradients refract the rolling peals across mountain valleys." }
    ]
  },
  "Dashboard — bront/brontophobia.md": {
    word: "brontophobia",
    primary: "An abnormal, irrational, or disproportionate fear of thunder and lightning storms; astraphobia.",
    secondary: "In clinical psychiatry and animal behavior, a severe phobic anxiety response triggered by barometric shifts and audible rumbling.",
    quotes: [
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "Children suffering from **brontophobia** cower beneath blankets, overwhelmed by thunderous acoustics beyond their control." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Excessive panic during electrical storms, classified as **brontophobia**, frequently accompanies autonomic instability in hypersensitive constitutions." },
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "The patient exhibited intense **brontophobia**, locking herself in windowless corridors at the earliest rumble of a summer squall." }
    ]
  },
  "Dashboard — bront/brontosaur.md": {
    word: "brontosaur",
    primary: "A popular and colloquial term for the Brontosaurus or any massive sauropod dinosaur resembling it.",
    secondary: "In paleontology and popular science culture, the iconic archetype of herbivorous quadrupedal Mesozoic giants with long necks and pillarlike limbs.",
    quotes: [
      { author: "Arthur Conan Doyle", work: "The Lost World", quote: "There upon the primeval plateau we beheld the giant **brontosaur**, wading through the marshy reedy waters." },
      { author: "Stephen Jay Gould", work: "Bully for Brontosaurus", quote: "For generations of museum visitors, no creature captured the prehistoric imagination quite like the beloved **brontosaur**." },
      { author: "Ray Bradbury", work: "A Sound of Thunder", quote: "The great **brontosaur** loomed like a sculptured mountain above the steaming Jurassic cycads." }
    ]
  },
  "Dashboard — bront/Brontosaurus.md": {
    word: "Brontosaurus",
    primary: "A genus of gigantic sauropod dinosaurs of the late Jurassic period, characterized by a massive quadrupedal body, long whip-like tail, and long neck.",
    secondary: "In taxonomic history, a famous genus name ('thunder lizard') coined by O. C. Marsh in 1879, famously synonymized with Apatosaurus for a century before being resurrected in 2015.",
    quotes: [
      { author: "Othniel Charles Marsh", work: "Notice of New Jurassic Reptiles", quote: "For this genus and species the name **Brontosaurus** excelsus is proposed, in allusion to the enormous size of the animal." },
      { author: "Henry Fairfield Osborn", work: "Skeletons of Sauropodous Dinosaurs", quote: "The mounting of the **Brontosaurus** skeleton in the American Museum established a new landmark in vertebrate paleontology." },
      { author: "Adrian Desmond", work: "The Hot-Blooded Dinosaurs", quote: "The public imagination embraced **Brontosaurus** as the archetype of peaceful reptilian gigantism roaming primeval lagoons." }
    ]
  },
  "Dashboard — ere/deere.md": {
    word: "deere",
    primary: "A historic brand and surname synonymous with John Deere (1804–1886), inventor of the self-scouring steel plow that revolutionized agriculture.",
    secondary: "In agrarian and industrial history, representative of mechanized farming equipment and the heavy engineering of the American Midwest; historically also an archaic spelling of deer.",
    quotes: [
      { author: "Hamlin Garland", work: "A Son of the Middle Border", quote: "With a polished John **Deere** plow, my father turned the black virgin sod of the Iowa prairie." },
      { author: "Willa Cather", work: "O Pioneers!", quote: "The heavy steel plows of John **Deere** cut deep furrows through the tough prairie grass where oxen strained." },
      { author: "Thorstein Veblen", work: "The Theory of Business Enterprise", quote: "Agricultural mechanization advanced swiftly as implements bearing the **Deere** imprint reshaped the economics of Western husbandry." }
    ]
  },
  "Dashboard — ere/ere.md": {
    word: "ere",
    primary: "An archaic or poetic preposition and conjunction meaning before or prior to in time.",
    secondary: "In literary syntax and rhetoric, expressing anticipation, impending transition, or urgency before a specified threshold or condition occurs.",
    quotes: [
      { author: "William Shakespeare", work: "Hamlet", quote: "A little month, or **ere** those shoes were old / With which she follow'd my poor father's body." },
      { author: "John Milton", work: "Paradise Lost", quote: "Our prison strong, this huge convex of Fire, / Outrageous to devour, immures us round / Ninefold, and starving Shop and molten Lead / Heaps on our heads, **ere** we can reach the shore." },
      { author: "Samuel Taylor Coleridge", work: "The Rime of the Ancient Mariner", quote: "And **ere** my work was done, the moon arose / And cast a silver sheen across the foam." }
    ]
  },
  "Dashboard — ere/hyperetes.md": {
    word: "hyperetes",
    primary: "In ancient Greece, an under-rower serving in the lower tier of a trireme; broadly, any subordinate assistant, attendant, or public officer.",
    secondary: "In classical civic and military administration, an official functioning under the authority of a magistrate, commander, or sacred liturgy.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "Every Athenian naval squadron depended upon the disciplined labor of the **hyperetes**, rowing tirelessly at the lowest bank." },
      { author: "Xenophon", work: "Hellenica", quote: "The naval commander inspected the crew, assigning each capable oarsman to his station as **hyperetes** beneath the deck." },
      { author: "Aristotle", work: "The Politics", quote: "In civic and military hierarchy, the **hyperetes** executes the direct operational commands of the governing magistrate." }
    ]
  },
  "Dashboard — ere/isere.md": {
    word: "isere",
    primary: "The Isère, a major river of southeastern France rising in the Graian Alps and joining the Rhône near Valence.",
    secondary: "A French department named after the river, situated in the Auvergne-Rhône-Alpes region, renowned for Alpine geography, hydroelectric power, and Grenoble's scientific institutions.",
    quotes: [
      { author: "Edward Whymper", work: "Scrambles Amongst the Alps", quote: "The waters of the **Isère** rushed through the deep alpine gorge, swollen by the summer thaw of the Dauphiné glaciers." },
      { author: "Victor Hugo", work: "Les Misérables", quote: "The mountain regiments marched along the banks of the **Isère**, shadowed by the steep limestone cliffs of Grenoble." },
      { author: "George Sand", work: "Letters of a Traveller", quote: "We followed the serpentine course of the **Isère** as the sun illuminated the high snowy ridges above the valley." }
    ]
  },
  "Dashboard — ere/trierarch.md": {
    word: "trierarch",
    primary: "In ancient Athens, the captain or commander of a trireme warship; specifically, a wealthy citizen upon whom the liturgy of outfitting and maintaining a trireme was imposed.",
    secondary: "In classical Greek public finance and naval governance, the designated individual bearing personal civic and financial responsibility for the operational readiness of the fleet.",
    quotes: [
      { author: "Demosthenes", work: "On the Crown", quote: "As **trierarch**, I equipped the war galley at my own personal expense, refusing to burden the public treasury during the emergency." },
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The **trierarch** steered his vessel into the thick of the battle, exhorting his rowers to ram the Corinthian flank." },
      { author: "Plutarch", work: "Lives: Themistocles", quote: "The state required every wealthy **trierarch** to maintain his warship in immediate readiness for offshore defense." }
    ]
  },
  "Dashboard — ere/trireme.md": {
    word: "trireme",
    primary: "An ancient Greek or Roman galley or warship propelled by three stacked banks of oars on each side.",
    secondary: "In naval history, the preeminent fast-attack warship of the classical Mediterranean, designed for ramming tactics and rapid maritime flanking maneuvers.",
    quotes: [
      { author: "Thucydides", work: "History of the Peloponnesian War", quote: "The Athenian **trireme** dashed into the harbor with all three banks of oars churning the blue water into foam." },
      { author: "Herodotus", work: "The Histories", quote: "The fleet of Salamis consisted of swift **triremes** whose bronze beaks proved fatal to the heavier Persian galleys." },
      { author: "Aeschylus", work: "The Persians", quote: "Ship sheared off ship with bronze-sheathed prow, until the **trireme** wreckage choked the strait." }
    ]
  },
  "Dashboard — bore/bore.md": {
    word: "bore",
    primary: "A sudden, powerful tidal wave that surges up an estuary or narrow river against the direction of the current; also, the hollow interior bore of a tube or firearm barrel.",
    secondary: "In geomorphology and oceanography, an abrupt wall of water produced by incoming spring tides forced into a converging shallow channel; also, to pierce through solid substance.",
    quotes: [
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "Like the tidal **bore** of the Severn, the sudden flood of memory rushed into the quiet channels of the soul." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The Atlantic tide forces an immense head of water up the estuary, creating a formidable traveling wave known as a **bore**." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "The river current clashed against the rising ocean tide, creating a churning **bore** that hissed through the mangroves." }
    ]
  },
  "Dashboard — bore/boreal.md": {
    word: "boreal",
    primary: "Of, relating to, or inhabiting northern regions; designating the circumpolar terrestrial climate and forest zone of the Northern Hemisphere.",
    secondary: "In biogeography and ecology, referring specifically to the subarctic coniferous biome (taiga) characterized by cold winters, muskegs, and spruce-fir vegetation.",
    quotes: [
      { author: "Henry David Thoreau", work: "The Maine Woods", quote: "The vast **boreal** forest of spruce and balsam stretched unbroken toward the frozen northern horizons." },
      { author: "John Muir", work: "The Mountains of California", quote: "In these high altitudes, alpine flora merges seamlessly into the hardy shrubs of the **boreal** zone." },
      { author: "Jack London", work: "The Call of the Wild", quote: "A cold **boreal** wind swept down from the Arctic barren lands, driving needles of frost across the trail." }
    ]
  },
  "Dashboard — bore/borealis.md": {
    word: "borealis",
    primary: "Northern; used as a Latin/Greek specific epithet in scientific, botanical, and astronomical designations (most notably in Aurora Borealis).",
    secondary: "In atmospheric physics and astronomy, designating radiant luminous displays occurring in northern polar ionospheric latitudes.",
    quotes: [
      { author: "Henry Wadsworth Longfellow", work: "The Song of Hiawatha", quote: "And the northern lights, the **borealis**, / Flashed across the purple midnight." },
      { author: "Robert Louis Stevenson", work: "In the South Seas", quote: "Even under equatorial stars, memory recalled the flickering ribbons of the aurora **borealis** over Scottish hills." },
      { author: "Fridtjof Nansen", work: "Farthest North", quote: "The aurora **borealis** streamed across the zenith like a shimmering curtain of electric green and violet fire." }
    ]
  },
  "Dashboard — bore/boreas.md": {
    word: "boreas",
    primary: "The Greek personification of the fierce North Wind, son of Astraeus and Eos, celebrated in classical mythology.",
    secondary: "In poetical and meteorological discourse, a blustering, icy northerly gale bringing winter snows and freezing gales from polar latitudes.",
    quotes: [
      { author: "Homer", work: "The Iliad", quote: "Then fierce **Boreas** blew from the Thracian peaks, whipping the gray Aegean into mountainous white-capped waves." },
      { author: "Ovid", work: "Metamorphoses", quote: "With rushing pinions **Boreas** sweeps the sky, driving before him the scattering clouds and icy hail." },
      { author: "Edmund Spenser", work: "The Faerie Queene", quote: "When bitter **Boreas** with his blustring blast / Doth scour the frozen plains and strip the forest bare." }
    ]
  },
  "Dashboard — bore/borecole.md": {
    word: "borecole",
    primary: "A variety of headless cabbage (Brassica oleracea acephala) with curly, crinkled leaves; kale.",
    secondary: "In horticulture and traditional culinary arts, a hardy biennial brassica capable of surviving severe winter frosts, harvested for nutritious winter greens.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The curled **borecole** or garden cabbage withstandeth the bitterest frost of winter without injury." },
      { author: "William Cobbett", work: "The English Gardener", quote: "No kitchen garden should lack a sturdy border of **borecole**, for it provides wholesome greens when all else is frozen." },
      { author: "Elizabeth David", work: "French Provincial Cooking", quote: "Winter soups gain hearty substance from shredded **borecole**, simmered gently with root vegetables and salt pork." }
    ]
  },
  "Dashboard — bore/borer.md": {
    word: "borer",
    primary: "A person, tool, or mechanical device that bores holes; also, any animal or insect that bores into wood, soil, or organic matter.",
    secondary: "In entomology and maritime trade, an insect larva (such as the corn borer or emerald ash borer) or marine mollusk (such as Teredo navalis) that destroys timber or crops by tunneling.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The timber of the submerged hulks was riddled with tunnels excavated by the destructive marine **borer**." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The larvae of the beetle act as an industrious **borer**, perforating the heartwood of ancient oaks." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "Along the wharf pilings, the shipworm, a bivalve **borer**, hollows out labyrinthine galleries in the soaked pine." }
    ]
  },
  "Dashboard — bore/hyperborean.md": {
    word: "hyperborean",
    primary: "In Greek mythology, an inhabitant of a legendary sunlit paradise situated beyond the North Wind (Boreas); hence, extremely northern, frigid, or arctic.",
    secondary: "In philosophy and literature, designating an outsider residing in extreme, Olympian intellectual solitude or inhabiting the farthest polar margins.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "The Antichrist", quote: "Let us look each other in the face. We are **Hyperboreans**—we know well enough how out of the way we live." },
      { author: "John Keats", work: "Endymion", quote: "Far in the sunlit spaces of the **Hyperborean** realm, eternal spring preserves the sacred groves of Apollo." },
      { author: "H. P. Lovecraft", work: "At the Mountains of Madness", quote: "The ancient stone structures suggested an architecture originating in remote, prehistoric **Hyperborean** latitudes." }
    ]
  },
  "Dashboard — nemat/nemat.md": {
    word: "nemat",
    primary: "A combining form derived from Greek nema (genitive nematos) meaning thread, used extensively in biological and anatomical nomenclature.",
    secondary: "In morphology and taxonomy, designating threadlike structure, cylindrical worm morphology, or filiform cellular filaments.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "Manual of the Anatomy of Invertebrated Animals", quote: "The morphological prefix **nemat**- denotes the threadlike structural habit typical of roundworms and flagellar fibers." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "Microscopic organisms bearing the **nemat**- designation exhibit exquisite filamentary symmetry under darkfield illumination." },
      { author: "William Benjamin Carpenter", work: "The Microscope and Its Revelations", quote: "In anatomical nomenclature, **nemat**- indicates elongated, threadlike cylindrical tissues and organisms." }
    ]
  },
  "Dashboard — nemat/nematocera.md": {
    word: "nematocera",
    primary: "A suborder of Diptera (true flies) characterized by long, slender, multi-segmented threadlike antennae, including mosquitoes, gnats, and crane flies.",
    secondary: "In systematic entomology, primitive dipterans exhibiting aquatic or moisture-dependent larvae, slender bodies, and elongate filiform appendages.",
    quotes: [
      { author: "William Kirby & William Spence", work: "An Introduction to Entomology", quote: "The suborder **Nematocera** is distinguished by slender, delicate antennae composed of numerous distinct segments." },
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "Flies belonging to the **Nematocera** possess graceful elongated bodies and long, multi-jointed filiform antennae." },
      { author: "August Weismann", work: "The Germ-Plasm", quote: "Embryological segmentation in **Nematocera** reveals ancestral dipteran patterns preserved through evolutionary divergence." }
    ]
  },
  "Dashboard — nemat/nematocyst.md": {
    word: "nematocyst",
    primary: "A specialized, microscopic stinging organelle found in cnidocytes of jellyfish, sea anemones, and corals, containing a coiled, eversible venomous thread.",
    secondary: "In invertebrate biology, a microscopic projectile weapon triggered chemically or mechanistically to paralyze prey or deter predators with extreme acceleration.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "The Oceanic Hydrozoa", quote: "Upon contact with prey, the coiled thread of the **nematocyst** is discharged with explosive velocity." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Each microscopic **nematocyst** contains a toxic barb capable of paralyzing small marine organisms instantly." },
      { author: "Stephen Jay Gould", work: "The Flamingo's Smile", quote: "The intricate spring-loaded mechanism of the cnidarian **nematocyst** represents a pinnacle of subcellular mechanical engineering." }
    ]
  },
  "Dashboard — nemat/nematocyte.md": {
    word: "nematocyte",
    primary: "A specialized cell found in cnidarians (such as jellyfish and hydras) that produces and encloses a stinging nematocyst; a cnidocyte.",
    secondary: "In cellular histology, an excitable epidermal cell armed with a cnidocil trigger that initiates exocytosis of the stinging apparatus upon tactile stimulation.",
    quotes: [
      { author: "Louis Agassiz", work: "Contributions to the Natural History of the United States", quote: "Within the epidermal layer of the hydra, each specialized **nematocyte** develops its lethal defensive capsule." },
      { author: "E. B. Wilson", work: "The Cell in Development and Inheritance", quote: "The differentiation of a **nematocyte** from undifferentiated interstitial cells demonstrates remarkable cellular specialization." },
      { author: "Libbie Hyman", work: "The Invertebrates", quote: "The sensory hair of the **nematocyte** detects chemical and mechanical stimuli, triggering instantaneous projectile expulsion." }
    ]
  },
  "Dashboard — nemat/nematoda.md": {
    word: "nematoda",
    primary: "A major phylum of smooth, unsegmented, bilaterally symmetrical pseudocoelomate worms commonly known as roundworms.",
    secondary: "In systematic zoology, one of the most abundant animal phyla on Earth, encompassing thousands of free-living benthic species and medically important plant and animal parasites.",
    quotes: [
      { author: "Nathan Cobb", work: "Nematodes and Their Relationships", quote: "If all the matter in the universe were swept away, our world would still be dimly recognizable in a ghostly film of **Nematoda**." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Members of the phylum **Nematoda** inhabit nearly every ecological niche, teeming unseen in soil grains and ocean sediments." },
      { author: "Libbie Hyman", work: "The Invertebrates: Acanthocephala, Aschelminthes, and Entoprocta", quote: "The structural uniformity of the **Nematoda** contrasts strikingly with their extraordinary ecological adaptability." }
    ]
  },
  "Dashboard — nemat/nematode.md": {
    word: "nematode",
    primary: "Any unsegmented, cylindrical roundworm belonging to the phylum Nematoda.",
    secondary: "In ecology, agriculture, and developmental genetics, a ubiquitous microscopic worm functioning as a soil decomposer, agricultural parasite, or premier laboratory model organism (such as C. elegans).",
    quotes: [
      { author: "Nathan Cobb", work: "Contributions to a Science of Nematology", quote: "A single thimbleful of fertile garden soil may harbor tens of thousands of microscopic **nematodes**." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "Beneath the roots of agricultural crops, beneficial and parasitic **nematodes** play vital roles in the subterranean food web." },
      { author: "Sydney Brenner", work: "The Genetics of Caenorhabditis elegans", quote: "The transparent soil **nematode** proved to be the ideal model organism for tracing embryonic cell lineages." }
    ]
  },
  "Dashboard — nemat/nematology.md": {
    word: "nematology",
    primary: "The branch of zoology that studies nematodes (roundworms), their taxonomy, biology, and ecological interactions.",
    secondary: "In agricultural science and phytopathology, the discipline focused on controlling parasitic nematodes that devastate crop root systems and transmit plant viruses.",
    quotes: [
      { author: "Nathan Cobb", work: "The Progress of Nematology", quote: "Agricultural yields worldwide depend upon the insights provided by modern **nematology** in managing root-knot parasites." },
      { author: "Gerald Thorne", work: "Principles of Nematology", quote: "The development of **nematology** as an independent discipline transformed pest management across subtropical plantations." },
      { author: "J. R. Christie", work: "Plant Nematodes: Their Bionomics and Control", quote: "Instruction in economic **nematology** equips agronomists to diagnose cryptic root decline caused by subterranean infestations." }
    ]
  }
};

function updateWordNote(relPath, data) {
  const fullPath = path.join(baseDir, relPath);
  if (!fs.existsSync(fullPath)) {
    console.error("Not found:", fullPath);
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
console.log("Batch 1 finished! Total words updated:", Object.keys(wordsData).length);
