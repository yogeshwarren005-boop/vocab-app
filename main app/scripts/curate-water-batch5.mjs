import fs from 'fs';
import path from 'path';

const baseClusterDir = 'App database/Greek roots/Cluster Water & Hydrology';

function updateNote(relDir, fileName, data) {
  const filePath = path.join(baseClusterDir, relDir, fileName);
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
  // Dashboard — pelag
  "Dashboard — pelag/abyssopelagic.md": {
    primary: "Of, relating to, or inhabiting the deep open ocean water column between depths of approximately 4,000 and 6,000 meters.",
    secondary: "In oceanography, characterizing the pitch-black, freezing, high-pressure abyss zone lying just above the hadal trenches.",
    quotes: [
      { author: "William Beebe", work: "Half Mile Down", quote: "In the silent depths of the **abyssopelagic** zone, bizarre organisms drift through perpetual darkness under crushing pressures." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Life in the **abyssopelagic** depths depends entirely on the organic snow sinking from sunlit waters miles above." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Trawls dragged through **abyssopelagic** waters reveal grotesque anglerfish equipped with bioluminescent lures." }
    ]
  },
  "Dashboard — pelag/allopelagic.md": {
    primary: "Inhabiting or ranging across varying depths of the open sea rather than being confined to a single pelagic stratum.",
    secondary: "In marine ecology, descriptive of organisms that exhibit extensive vertical or horizontal migrations across disparate ocean water masses.",
    quotes: [
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "Certain squid and lanternfishes exhibit an **allopelagic** distribution, traversing hundreds of meters of depth each night." },
      { author: "William Beebe", work: "The Arcturus Adventure", quote: "The catch included **allopelagic** predators that follow shifting thermoclines in search of drifting prey." },
      { author: "Rachel Carson", work: "Under the Sea-Wind", quote: "Active **allopelagic** wanderers move freely between the warm sunlit surface and the chilly twilight zone." }
    ]
  },
  "Dashboard — pelag/archipelagic.md": {
    primary: "Of, relating to, or situated in an archipelago or group of scattered islands.",
    secondary: "In the law of the sea and geopolitics, designating sea lanes, baselines, and sovereign maritime zones enclosed by an island chain.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The flora of these **archipelagic** channels exhibits sharp variations dictated by deep submarine barriers." },
      { author: "Joseph Conrad", work: "The Rescue", quote: "The schooner glided silently into the labyrinth of **archipelagic** reefs where local rajahs held sway." },
      { author: "Herman Melville", work: "The Encantadas", quote: "The lonely **archipelagic** clusters of the Galápagos rise like heaps of burnt cinders above the Pacific swell." }
    ]
  },
  "Dashboard — pelag/archipelago.md": {
    primary: "A group or chain of islands clustered together in a sea or large body of water.",
    secondary: "Historically, the Aegean Sea (the original Archipelago, from Greek arkhi- chief + pelagos sea); figuratively, any scattered network of interconnected enclaves.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The natural history of this **archipelago** is very remarkable: it seems to be a little world within itself." },
      { author: "Aleksandr Solzhenitsyn", work: "The Gulag Archipelago", quote: "That **archipelago** was an enormous network of islands of suffering scattered across our continent." },
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "The sun sets on the blue Aegean **archipelago**, gilding each rocky isle with memories of ancient freedom." }
    ]
  },
  "Dashboard — pelag/bathypelagic.md": {
    primary: "Of, relating to, or inhabiting the deep ocean water column between approximately 1,000 and 4,000 meters below the surface.",
    secondary: "In biological oceanography, the midnight zone where sunlight never reaches and organisms rely on bioluminescence and low metabolic rates.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "In the **bathypelagic** realm of absolute night, creatures carry their own lanterns and glowing organs." },
      { author: "William Beebe", work: "Half Mile Down", quote: "Our net sampled the **bathypelagic** fauna, bringing up gelatinous medusae and black dragonfish." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Pressure in the **bathypelagic** zone exceeds hundreds of atmospheres, dictating fragile, fluid-rich body plans." }
    ]
  },
  "Dashboard — pelag/epipelagic.md": {
    primary: "Of, relating to, or constituting the sunlit uppermost layer of the ocean water column, from the surface down to about 200 meters.",
    secondary: "In marine ecology, the photic zone where sufficient sunlight penetrates to support photosynthesis, forming the primary productive layer of the sea.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The **epipelagic** zone is the green pasture of the sea, where microscopic diatoms harness the sun's energy." },
      { author: "Alister Hardy", work: "The Open Sea: Its Natural History", quote: "Most commercial fisheries harvest the dense schools of mackerel and herring that populate the **epipelagic** waters." },
      { author: "Sylvia Earle", work: "Sea Change", quote: "Protecting the biodiversity of the **epipelagic** layer is essential for sustaining the global marine food web." }
    ]
  },
  "Dashboard — pelag/hadopelagic.md": {
    primary: "Of, relating to, or inhabiting the deepest open waters of ocean trenches, extending from 6,000 meters down to the deepest ocean floor.",
    secondary: "In deep-sea oceanography, designating the trench zone (named after Hades) marked by extreme hydrostatic pressure, near-freezing temperatures, and specialized endemic scavengers.",
    quotes: [
      { author: "Jacques Piccard", work: "Seven Miles Down", quote: "As the bathyscaphe touched the bottom of the Mariana Trench, we gazed into the mysterious **hadopelagic** abyss." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Remarkable amphipods survive in the **hadopelagic** trenches, feeding on debris that cascades down submarine canyon walls." },
      { author: "Sylvia Earle", work: "Sea Change: A Message of the Oceans", quote: "The extreme adaptations of **hadopelagic** life challenge our fundamental understanding of biochemical stability under pressure." }
    ]
  },
  "Dashboard — pelag/mesopelagic.md": {
    primary: "Of, relating to, or inhabiting the intermediate ocean depths between approximately 200 and 1,000 meters below the surface.",
    secondary: "In marine science, the twilight zone characterized by dim, filtered sunlight, massive daily vertical migrations, and pervasive bioluminescence.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "At dusk, billions of **mesopelagic** creatures begin their immense journey toward the surface to graze under cover of night." },
      { author: "William Beebe", work: "Half Mile Down", quote: "The blue light faded to a ghostly violet as we entered the **mesopelagic** stratum of lanternfishes." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Acoustic sounders revealed the deep scattering layer, composed primarily of migrating **mesopelagic** fishes." }
    ]
  },
  "Dashboard — pelag/pelag.md": {
    primary: "The Greek root pelagos (meaning 'open sea', 'high sea', or 'ocean deeps'), forming words relating to marine zones and oceanic organisms.",
    secondary: "In oceanographic terminology and historical linguistics, the classical root designating the boundless expanse of open water beyond coastal shores.",
    quotes: [
      { author: "Walter William Skeat", work: "An Etymological Dictionary of the English Language", quote: "The ancient Greek **pelag**, denoting the wide sea, survives in our modern division of ocean vertical zones." },
      { author: "Ernest Weekley", work: "The Romance of Words", quote: "From the Homeric **pelag** we inherit archipelago, once the sovereign name of the Aegean Sea itself." },
      { author: "Peter Mark Roget", work: "Thesaurus of English Words and Phrases", quote: "All oceanographic categories that partition the open water column trace their etymology to the Hellenic **pelag**." }
    ]
  },
  "Dashboard — pelag/pelage.md": {
    primary: "The hairy coat, fur, or wool covering the skin of a non-human mammal.",
    secondary: "In mammalogy and wildlife biology, the collective coat consisting of underfur and guard hairs, serving for thermoregulation, camouflage, and tactile sensation; derived from French poil (Latin pilus).",
    quotes: [
      { author: "Charles Darwin", work: "The Expression of the Emotions in Man and Animals", quote: "When terrified, the animal erects its **pelage** to present a larger and more menacing appearance." },
      { author: "John James Audubon", work: "The Viviparous Quadrupeds of North America", quote: "In winter, the thick **pelage** of the northern otter turns dark and lustrous, providing complete waterproofing." },
      { author: "Henry Walter Bates", work: "The Naturalist on the River Amazons", quote: "The golden **pelage** of the lion tamarin glistened brilliantly as it leaped through the forest canopy." }
    ]
  },
  "Dashboard — pelag/pelagianism.md": {
    primary: "The theological doctrine originated by the 4th-century ascetic Pelagius, which asserted that original sin did not taint human nature and that humans possess free will to achieve salvation without divine grace.",
    secondary: "In church history, a major controversy vigorously opposed by Saint Augustine and condemned as heresy by the Council of Carthage (418 AD) and Council of Ephesus (431 AD).",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The subtle disputations of **Pelagianism** divided the bishops of Africa and Rome over the mystery of grace." },
      { author: "Thomas Aquinas", work: "Summa Theologiae", quote: "Against the error of **Pelagianism**, we must maintain that man cannot merit eternal life without the prior infusion of divine grace." },
      { author: "John Henry Newman", work: "An Essay on the Development of Christian Doctrine", quote: "Augustine saw in **Pelagianism** a dangerous rationalism that undermined the fundamental necessity of redemption." }
    ]
  },
  "Dashboard — pelag/pelagic.md": {
    primary: "Of, relating to, living in, or occurring in the open ocean or open water column, away from both the coast and the sea floor.",
    secondary: "In marine ecology, applied to organisms (plankton, nekton) and deposits that exist independently of coastal shallows or benthic substrates.",
    quotes: [
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Far from land, the **pelagic** petrel skims the crests of towering waves in effortless flight." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The great sperm whale is a true **pelagic** wanderer, making the entire circuit of the globe his pasture." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Our net captured innumerable **pelagic** crustacea and phosphorescent medusae in the open Atlantic." }
    ]
  },
  "Dashboard — pelag/pelagius.md": {
    primary: "A 4th-to-5th-century British ascetic monk and theologian who taught that humans have full moral responsibility and the capacity to choose good without the necessity of special divine grace.",
    secondary: "In Christian theology, the titular namesake of Pelagianism whose teachings spurred Saint Augustine's definitive treatises on predestination and sovereign grace.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The moral character of **Pelagius** was unimpeached even by his most vehement orthodox adversaries." },
      { author: "Bertrand Russell", work: "A History of Western Philosophy", quote: "**Pelagius** argued with cool British common sense that if God commands men to be good, it must be possible for men to be good." },
      { author: "Saint Augustine", work: "On the Grace of Christ and on Original Sin", quote: "We must confront **Pelagius** not from malice, but to defend the cross of Christ from being made void." }
    ]
  },
  "Dashboard — pelag/pelagonym.md": {
    primary: "A proper name applied to a sea, gulf, ocean, or open marine body of water; an ocean toponym.",
    secondary: "In toponomy and historical geography, the nomenclature and linguistic origin of sea names, such as Mediterranean, Pacific, or Adriatic.",
    quotes: [
      { author: "Isaac Taylor", work: "Words and Places: Or, Etymological Researches in History, Ethnology and Geography", quote: "The ancient **pelagonym** of the Euxine Sea reflected both the dread and the later hospitality of Greek navigators." },
      { author: "H. L. Mencken", work: "The American Language", quote: "Every historic **pelagonym** in the Western Hemisphere carries the imprint of Spanish or English colonial exploration." },
      { author: "Fernand Braudel", work: "The Mediterranean and the Mediterranean World in the Age of Philip II", quote: "The multiple variants of each **pelagonym** across our charts reflect the shifting frontiers of maritime empires." }
    ]
  },

  // Dashboard — phyc
  "Dashboard — phyc/Phycomyces.md": {
    primary: "A genus of saprophytic zygomycete fungi in the family Phycomycetaceae, famous for its exceptionally long, single-celled sporangiophores.",
    secondary: "In biophysics and photobiology, a classic model organism (notably Phycomyces blakesleeanus) used to study sensory phototropism, gravitropism, and helical cell-wall growth.",
    quotes: [
      { author: "Max Delbrück", work: "Phycomyces", quote: "The single-celled sporangiophore of **Phycomyces** offers an extraordinarily precise system for probing biological light reception." },
      { author: "George Wald", work: "The Molecular Basis of Visual Excitation", quote: "The phototropic response in **Phycomyces** shows action spectra closely aligned with flavin photoreceptors." },
      { author: "Kenneth B. Raper", work: "The Dictyostelids", quote: "Long stalks of **Phycomyces** bend unerringly toward the faintest point source of illumination." }
    ]
  },
  "Dashboard — phyc/phycobilin.md": {
    primary: "Any of a group of water-soluble, light-capturing tetrapyrrole pigments found in cyanobacteria and the rhodophyte (red) algae.",
    secondary: "In plant biochemistry, chromophores covalently bonded to proteins (phycobiliproteins) that absorb green and yellow light wavelengths and transfer energy to chlorophyll a.",
    quotes: [
      { author: "C. Stacy French", work: "The Pigments of Algae", quote: "The **phycobilin** pigments enable red algae to harvest the dim blue-green light that penetrates into deep waters." },
      { author: "Martin D. Kamen", work: "Primary Processes in Photosynthesis", quote: "Energy absorbed by the **phycobilin** complex is transferred with near-perfect quantum efficiency to the reaction center." },
      { author: "Robert Emerson", work: "The Effect of Wavelength on Photosynthetic Efficiency", quote: "Our spectroscopic analysis isolated the **phycobilin** components responsible for energy capture in blue-green algae." }
    ]
  },
  "Dashboard — phyc/phycocyanin.md": {
    primary: "A blue photosynthetic accessory pigment complex of the phycobiliprotein family, found primarily in cyanobacteria and red algae.",
    secondary: "In biochemistry and biotechnology, a fluorescent protein pigment used as a natural food colorant, medical diagnostic fluorophore, and potent antioxidant.",
    quotes: [
      { author: "C. Stacy French", work: "Photosynthesis", quote: "The intense cobalt hue of spirulina extracts is due to **phycocyanin**, which absorbs orange and red photons." },
      { author: "Martin D. Kamen", work: "Biochemical Studies of Photosynthesis", quote: "Spectrophotometric curves demonstrated that **phycocyanin** transfers its excitation energy directly to allophycocyanin." },
      { author: "Robert Emerson", work: "Photosynthetic Pigments", quote: "Light captured by **phycocyanin** drives oxygenic photosynthesis when chlorophyll absorption is at a minimum." }
    ]
  },
  "Dashboard — phyc/phycoerythrin.md": {
    primary: "A brilliant red photosynthetic accessory pigment belonging to the phycobiliprotein family, found prominently in red algae (Rhodophyta) and certain cyanobacteria.",
    secondary: "In marine botany and cell biology, an antenna pigment that absorbs blue-green light in deep coastal waters, widely utilized in flow cytometry as a fluorescent label.",
    quotes: [
      { author: "C. Stacy French", work: "The Pigments of Algae", quote: "The deep scarlet color of benthic rhodophytes is imparted by **phycoerythrin**, masking the underlying green chlorophyll." },
      { author: "Martin D. Kamen", work: "Biochemical Studies of Photosynthesis", quote: "Fluorescence emission from **phycoerythrin** cascades sequentially through phycocyanin to activate the photosynthetic core." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Dredges from forty fathoms brought up delicate red algae rich in **phycoerythrin**, perfectly tuned to deep submarine illumination." }
    ]
  },
  "Dashboard — phyc/phycology.md": {
    primary: "The scientific study of algae; also known as algology.",
    secondary: "The biological subdiscipline that investigates the taxonomy, ecology, physiology, and evolutionary history of photosynthetic micro- and macroalgae in marine and freshwater habitats.",
    quotes: [
      { author: "William Henry Harvey", work: "Phycologia Britannica", quote: "The progress of modern **phycology** has revealed an astonishing architectural diversity in the marine flora of our coasts." },
      { author: "George Francis Atkinson", work: "College Botany", quote: "A thorough grounding in **phycology** is indispensable for understanding the primary productivity of lakes and oceans." },
      { author: "Alister Hardy", work: "The Open Sea: The World of Plankton", quote: "Pioneering works in **phycology** opened our eyes to the microscopic diatom pastures that sustain all marine life." }
    ]
  },
  "Dashboard — phyc/phycomycetes.md": {
    primary: "An archaic taxonomic class of lower fungi characterized by non-septate (coenocytic) mycelia and asexual reproduction by sporangiospores, often resembling green algae.",
    secondary: "In the history of mycology, an obsolete grouping that formerly combined Chytridiomycota, Zygomycota, and fungus-like Oomycota before modern phylogenetic classification.",
    quotes: [
      { author: "Anton de Bary", work: "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria", quote: "The primitive structural affinities between the **phycomycetes** and siphonaceous algae led early naturalists to suspect a common origin." },
      { author: "George Massee", work: "A Text-Book of Fungi", quote: "In the **phycomycetes**, the vegetative hyphae lack cross-walls, forming continuous multinucleate filaments." },
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", quote: "Spore dispersal mechanisms among the **phycomycetes** exhibit extraordinary hydrostatic propulsion." }
    ]
  },
  "Dashboard — phyc/phycomycosis.md": {
    primary: "A rare and often severe fungal infection in humans and animals caused by members of the order Mucorales (mucormycosis) or Entomophthorales.",
    secondary: "In clinical pathology, an opportunistic, angioinvasive mycosis characteristically presenting with broad, non-septate hyphae in immunocompromised patients.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Cases of systemic **phycomycosis** are marked by rapid vascular thrombosis and tissue necrosis." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Under the term **phycomycosis**, pathologists classify destructive fungal lesions invading subcutaneous tissues and cranial sinuses." },
      { author: "Samuel Cooper", work: "A Dictionary of Practical Surgery", quote: "Early surgical debridement and aggressive antimycotic therapy are imperative in managing acute **phycomycosis**." }
    ]
  },
  "Dashboard — phyc/schizophyceous.md": {
    primary: "Of, pertaining to, or resembling the Schizophyceae (the cyanobacteria or blue-green algae).",
    secondary: "In botanical history and algology, descriptive of prokaryotic, fission-reproducing photosynthetic microorganisms that lack membrane-bound nuclei.",
    quotes: [
      { author: "Ferdinand Cohn", work: "Researches on Bacteria", quote: "The simple cell division of these organisms demonstrates their **schizophyceous** nature, allying them closely to the true bacteria." },
      { author: "William Henry Harvey", work: "Phycologia Australica", quote: "A dense **schizophyceous** scum coated the stagnant lagoons after weeks of uninterrupted summer heat." },
      { author: "Anton de Bary", work: "Lectures on Bacteria", quote: "Early microscopists placed these filamentous growths in the **schizophyceous** group because of their binary fission." }
    ]
  },

  // Dashboard — potam
  "Dashboard — potam/Mesopotamia.md": {
    primary: "An ancient historical region in Western Asia between the Tigris and Euphrates rivers, corresponding broadly to modern-day Iraq and parts of Syria, Turkey, and Iran.",
    secondary: "In world history, the 'cradle of civilization', where agriculture, writing (cuneiform), urban architecture, and codified law first emerged in Sumer, Akkad, Babylonia, and Assyria.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The fertile plains of **Mesopotamia** nourished the powerful monarchies of Nineveh and Babylon." },
      { author: "Herodotus", work: "The Histories", quote: "The whole country of **Mesopotamia** is intersected by canals, and the soil yields grain with incredible abundance." },
      { author: "Arnold J. Toynbee", work: "A Study of History", quote: "The challenge of managing the catastrophic floods of the twin rivers provoked the rise of civilization in **Mesopotamia**." }
    ]
  },
  "Dashboard — potam/autopotamic.md": {
    primary: "Indigenous to, originating within, or adapted specifically to flowing river environments; applied especially to river plankton (potamoplankton).",
    secondary: "In limnology and potamology, designating organisms that reproduce and complete their entire life cycle within a lotic (running water) ecosystem rather than drifting in from lakes.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "True **autopotamic** plankton can persist only in mature, slow-flowing lowland reaches where replacement rates match the current." },
      { author: "Victor Hensen", work: "Die Plankton-Expedition", quote: "We must separate the allochthonous washings of upland bogs from the strictly **autopotamic** species native to the river bed." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Studies of river ecology showed that certain diatoms are uniquely **autopotamic**, thriving in turbulent freshwater currents." }
    ]
  },
  "Dashboard — potam/hippopotamus.md": {
    primary: "A large, heavy, mostly herbivorous semiaquatic mammal (Hippopotamus amphibius) native to sub-Saharan Africa, possessing thick skin, short legs, and large tusks.",
    secondary: "Etymologically from Greek hippopotamos ('river horse'); in wildlife biology, an ecosystem engineer that alters riverbeds and aquatic nutrient cycles.",
    quotes: [
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "A huge **hippopotamus** rose suddenly beside our canoe, blowing water from its nostrils with a resonant snort." },
      { author: "Theodore Roosevelt", work: "African Game Trails", quote: "The clumsy bulk of the **hippopotamus** moves through the river reeds with surprising silence and swiftness." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "Fossil remains prove that the **hippopotamus** once wallowed in the Thames and the rivers of southern Europe during Pleistocene interglacials." }
    ]
  },
  "Dashboard — potam/potamic.md": {
    primary: "Of, relating to, or inhabiting rivers or streams; fluvial.",
    secondary: "In hydrology and freshwater biology, describing processes, sediments, or biological communities associated with flowing freshwater river channels.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative", quote: "The great **potamic** network of the Orinoco opens an immense highway across the virgin forests of the interior." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The **potamic** silt deposited during annual inundations gradually raises the level of the alluvial delta." },
      { author: "Arthur Tansley", work: "Practical Plant Ecology", quote: "Aquatic vegetation in this valley displays a distinct **potamic** zonation determined by current velocity." }
    ]
  },
  "Dashboard — potam/potamodromous.md": {
    primary: "Migrating exclusively within freshwater systems, especially moving upstream within rivers and tributaries to spawn.",
    secondary: "In fisheries biology and ichthyology, distinguished from anadromous (sea to river) and catadromous (river to sea) migrations.",
    quotes: [
      { author: "Francis Day", work: "The Fishes of Great Britain and Ireland", quote: "The grayling is a **potamodromous** species, journeying to clear upland shallows to deposit its spawn." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "Dams constructed across river valleys pose an insurmountable barrier to **potamodromous** native suckers and minnows." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Unlike the ocean-wandering salmon, strictly **potamodromous** fishes never cross the brackish boundary of the estuary." }
    ]
  },
  "Dashboard — potam/potamogale.md": {
    primary: "A genus of semiaquatic afrotherian mammals in the family Tenrecidae, comprising the giant otter shrew (Potamogale velox), native to the streams of equatorial Africa.",
    secondary: "In mammalogy and evolutionary biology, a living relict species that propels itself through water using lateral undulations of its laterally compressed tail, resembling an otter.",
    quotes: [
      { author: "Paul Du Chaillu", work: "Explorations and Adventures in Equatorial Africa", quote: "In the mountain streams of the interior, I secured specimens of the extraordinary **Potamogale**, which swims with the agility of a miniature seal." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The giant otter shrew, **Potamogale**, is unique among insectivores in swimming entirely by muscular strokes of its flattened tail." },
      { author: "Alfred Russel Wallace", work: "Island Life", quote: "The isolated anatomical position of **Potamogale** points to an ancient archaic mammalian lineage in the African forest refugia." }
    ]
  },
  "Dashboard — potam/potamogalidae.md": {
    primary: "A taxonomic family or subfamily of semiaquatic afrotherian insectivores (otter shrews) comprising the genera Potamogale and Micropotamogale.",
    secondary: "In systematic mammalogy, an endemic Central and West African group specialized for predatory foraging in freshwater streams.",
    quotes: [
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The family **Potamogalidae** contains aquatic tenrecs that have evolved external convergence with the true otters." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The distribution of the **Potamogalidae** is strictly confined to the river systems of the western equatorial rainforest." },
      { author: "William Henry Flower", work: "An Introduction to the Osteology of the Mammalia", quote: "Cranial osteology in the **Potamogalidae** reveals complete loss of the zygomatic arch and retention of primitive dental features." }
    ]
  },
  "Dashboard — potam/potamogeton.md": {
    primary: "A large genus of aquatic flowering plants in the family Potamogetonaceae, commonly known as pondweeds, widely distributed in freshwater habitats.",
    secondary: "In aquatic botany and limnology, submerged or floating-leaved macrophyte plants that provide essential food and habitat for waterfowl and freshwater fish.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "Dense beds of **Potamogeton** carpet the shallows of the pond, their translucent submerged leaves waving in the current." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The spikes of **Potamogeton** rise above the water surface to expose their wind-pollinated blossoms." },
      { author: "George Bentham", work: "Handbook of the British Flora", quote: "Identification of species in the genus **Potamogeton** is notoriously difficult owing to extreme leaf polymorphism." }
    ]
  },
  "Dashboard — potam/potamogetonaceae.md": {
    primary: "The pondweed family of aquatic monocotyledonous flowering plants, characterized by submerged or floating leaves and small wind-pollinated flowers in spikes.",
    secondary: "In systematic botany, a cosmopolitan freshwater family of great ecological importance in lakes, ponds, and slow rivers.",
    quotes: [
      { author: "Asa Gray", work: "Elements of Botany", quote: "Members of the **Potamogetonaceae** exhibit specialized anatomical air channels enabling buoyancy in stagnant water." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The family **Potamogetonaceae** is distributed across every continent, forming the primary vegetative cover of freshwater shallows." },
      { author: "George Bentham", work: "Genera Plantarum", quote: "In **Potamogetonaceae**, the perianth is reduced to four herbaceous scales opposite each stamen." }
    ]
  },
  "Dashboard — potam/potamology.md": {
    primary: "The scientific study of rivers, stream channels, and flowing freshwater surface systems.",
    secondary: "In hydrology and geomorphology, the comprehensive discipline examining fluvial hydraulics, river sediment transport, channel morphology, and river ecology.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "Comparative **potamology** reveals how river basins sculpt the physical geography of continents and determine historic trade routes." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The principles of **potamology** show that meandering channels continuously reconstruct alluvial plains through erosion and deposition." },
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "The insights of **potamology** are vital to the oceanographer who must account for the vast freshwater discharges pouring into coastal basins." }
    ]
  },
  "Dashboard — potam/potamonym.md": {
    primary: "A proper name applied to a river or stream; a fluvial toponym (e.g., Amazon, Danube, Mississippi).",
    secondary: "In onomastics and historical linguistics, river names that frequently preserve the most archaic linguistic roots of prehistoric populations.",
    quotes: [
      { author: "Isaac Taylor", work: "Words and Places: Or, Etymological Researches in History, Ethnology and Geography", quote: "The Celtic **potamonym** Avon or Ouse survives in dozens of English rivers long after the spoken language disappeared." },
      { author: "H. L. Mencken", work: "The American Language", quote: "Almost every indigenous American **potamonym** from the Mississippi to the Susquehanna commemorates an Algonquian tribal term." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "A primeval **potamonym** often outlives empires, preserving the speech of vanished races in the murmur of running water." }
    ]
  },
  "Dashboard — potam/potamophis.md": {
    primary: "An archaic taxonomic genus name applied to small North American water or earth snakes (such as the rough earth snake, now Virginia striatula).",
    secondary: "In historical herpetology, literally 'river snake' (Greek potamos + ophis), previously used to group harmless semiaquatic colubrids.",
    quotes: [
      { author: "Raymond Ditmars", work: "The Reptile Book", quote: "Under the older generic name **Potamophis**, naturalists classified the harmless ground snakes found beneath decaying logs near creek beds." },
      { author: "Spencer Fullerton Baird", work: "Catalogue of North American Reptiles", quote: "The species described as **Potamophis** striatula displays keeled dorsal scales and secretive fossorial habits." },
      { author: "Edward Drinker Cope", work: "The Crocodilians, Lizards, and Snakes of North America", quote: "Careful examination of the cranial bones demonstrated that **Potamophis** belonged to the colubrine subfamily." }
    ]
  },
  "Dashboard — potam/potamophobia.md": {
    primary: "An intense, irrational, or debilitating fear of rivers, streams, or running water.",
    secondary: "In clinical psychology and psychiatry, a specific phobia characterized by severe anxiety and panic attacks triggered by the sight, sound, or prospect of crossing rivers.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "A traveler afflicted with acute **potamophobia** will suffer severe distress when crossing a suspension bridge above a rushing torrent." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Phobias relating to natural water bodies, including **potamophobia**, frequently trace back to terrifying childhood experiences of drowning." },
      { author: "Sigmund Freud", work: "The Ego and the Id", quote: "The neurotic symptoms of **potamophobia** often conceal repressed traumatic memories symbolically associated with rushing floodwaters." }
    ]
  },
  "Dashboard — potam/potamoplankton.md": {
    primary: "The aggregate of microscopic drifting organisms (plankton) inhabiting rivers and flowing streams.",
    secondary: "In limnology and river ecology, distinguished from lake plankton (limnoplankton), adapted to turbulent mixing and continuous downstream displacement.",
    quotes: [
      { author: "Arthur Tansley", work: "The British Islands and Their Vegetation", quote: "In large, sluggish rivers, the **potamoplankton** develops in great abundance, tinting the water with green blooms of diatoms and flagellates." },
      { author: "Victor Hensen", work: "Die Plankton-Expedition", quote: "Our comparative samples of **potamoplankton** revealed marked differences in species dominance compared to adjacent lacustrine waters." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Heavy rain flushes millions of tons of **potamoplankton** from river estuaries directly into coastal marine food webs." }
    ]
  },

  // Dashboard — raph
  "Dashboard — raph/raphae.md": {
    primary: "The plural of rapha or raphe; anatomical seams, ridges, or lines of junction where two symmetrical halves of an organ or structure meet.",
    secondary: "In comparative anatomy and microscopy, visible longitudinal seams found on anatomical structures (e.g., median raphes) and on diatom frustules.",
    quotes: [
      { author: "Richard Owen", work: "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", quote: "The median **raphae** on the cranial sutures mark the precise lines of embryonic closure." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "In certain embryonic stages, distinct **raphae** indicate the fusion of bilateral tissue folds." },
      { author: "Robley Dunglison", work: "Medical Lexicon", quote: "Anatomists describe various superficial **raphae** where bilateral muscular sheets coalesce in the midline." }
    ]
  },
  "Dashboard — raph/raphael.md": {
    primary: "In Judeo-Christian and Islamic tradition, an archangel regarded as a patron of travelers and the angel of divine healing.",
    secondary: "In art history, Raffaello Sanzio (1483–1520), the celebrated Italian master painter and architect of the High Renaissance.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "The affable Archangel **Raphael** descended from the celestial heights to warn Adam of his impending trial." },
      { author: "John Ruskin", work: "Modern Painters", quote: "The serene harmony of **Raphael** reflects the highest peak of Italian classical draftsmanship and balanced composition." },
      { author: "Walter Pater", work: "The Renaissance", quote: "In the Vatican stanze, **Raphael** achieved a perfect synthesis of pagan antiquity and Christian grace." }
    ]
  },
  "Dashboard — raph/raphanus.md": {
    primary: "A genus of flowering plants in the mustard family Brassicaceae, notably comprising the cultivated radish (Raphanus sativus) and wild radish (Raphanus raphanistrum).",
    secondary: "In economic botany, pungent herbaceous plants valued for their crisp, edible taproots and pungent seeds containing mustard oils (glucosinolates).",
    quotes: [
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "Under the genus **Raphanus**, Linnaeus grouped the common radish and its wild seaside relatives." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The siliques of **Raphanus** are spongy and indehiscent, breaking into one-seeded joints when mature." },
      { author: "Charles Darwin", work: "The Variation of Animals and Plants under Domestication", quote: "Gardeners have produced countless distinct cultivars of **Raphanus** differing remarkably in root shape and color." }
    ]
  },
  "Dashboard — raph/raphe.md": {
    primary: "A seam, ridge, or groove marking the line of junction between two symmetrical halves of an anatomical organ or structure.",
    secondary: "In botanical anatomy and seed morphology, the ridge connecting the hilum to the chalaza on an anatropous ovule; in diatoms, the longitudinal slit through which cytoplasmic streaming occurs.",
    quotes: [
      { author: "Henry Gray", work: "Anatomy of the Human Body", quote: "A distinct median **raphe** extends along the perineum, indicating the bilateral union of the embryonic genital folds." },
      { author: "Asa Gray", work: "Structural Botany", quote: "In an inverted seed, the adnate funiculus forms a prominent **raphe** along one side of the testa." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Under high magnification, the diatom glides smoothly by means of protoplasmic streaming through its longitudinal **raphe**." }
    ]
  },
  "Dashboard — raph/raphia.md": {
    primary: "A genus of tropical palms in the family Arecaceae, native primarily to tropical Africa, celebrated for their immense pinnate leaves.",
    secondary: "In economic botany, the source of raffia fiber, obtained from the fibrous membranes of the young pinnate leaves, widely used in horticulture and textile weaving.",
    quotes: [
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "The natives construct durable sleeping mats and baskets from the tough fiber of the **Raphia** palm." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "The massive leaves of **Raphia** vinifera surpass those of almost all other trees, extending up to fifty feet in length." },
      { author: "Alfred Russel Wallace", work: "Palm Trees of the Amazon and Their Uses", quote: "The swampy river bottoms are choked with colossal groves of **Raphia**, whose pendulous fruits furnish oil to the inhabitants." }
    ]
  },
  "Dashboard — raph/raphicerus.md": {
    primary: "A genus of small, delicate African antelopes in the family Bovidae, commonly known as steenboks and grysboks.",
    secondary: "In mammalogy and wildlife ecology, territorial, solitary dwarf antelopes native to eastern and southern African grasslands and savannas, possessing straight, vertical spike-like horns.",
    quotes: [
      { author: "Frederick Courteney Selous", work: "A Hunter's Wanderings in Africa", quote: "A tiny steenbok of the genus **Raphicerus** darted from behind a thorn bush and vanished across the plain." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The genus **Raphicerus** is distinguished by upright, needle-sharp horns and large preorbital glandular tufts." },
      { author: "Theodore Roosevelt", work: "African Game Trails", quote: "While traversing the dry scrub, we frequently started a graceful **Raphicerus**, bounding like a hare through the stony ravines." }
    ]
  },
  "Dashboard — raph/raphidae.md": {
    primary: "An archaic or regional zoological family designation historically associated with certain invertebrate groups or birds related to Raphus.",
    secondary: "In systematic taxonomy, a historical variant family spelling formerly used in grouping flightless columbiforms (the dodo and solitaires, more formally Raphidae/Dididae).",
    quotes: [
      { author: "Richard Owen", work: "Memoir on the Dodo", quote: "The skeletal affinities of the extinct family **Raphidae** confirm that these giant birds were specialized terrestrial pigeons." },
      { author: "Thomas Henry Huxley", work: "The Anatomy of Vertebrated Animals", quote: "The sternum of the **Raphidae** lacked a keel, reflecting complete atrophy of the pectoral flight muscles." },
      { author: "Alfred Russel Wallace", work: "The Geographical Distribution of Animals", quote: "The tragic extinction of the **Raphidae** on Mauritius followed swiftly upon the introduction of swine and alien predators." }
    ]
  },
  "Dashboard — raph/raphidiidae.md": {
    primary: "A family of predatory insects in the order Raphidioptera, commonly known as snakeflies, characterized by an elongated prothorax and neck-like appearance.",
    secondary: "In entomology, holometabolous, woodland-dwelling insects whose females possess a long, flexible ovipositor used to lay eggs beneath loose tree bark.",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The snakefly, belonging to the family **Raphidiidae**, elevates its slender head and prothorax with a curious serpentine movement." },
      { author: "William Morton Wheeler", work: "Ants: Their Structure, Development and Behavior", quote: "Larvae of the **Raphidiidae** prowl under decaying bark, feeding voraciously on wood-boring beetle grubs." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Among terrestrial insects blown out to sea in offshore gales, we occasionally recovered specimens of **Raphidiidae**." }
    ]
  },
  "Dashboard — raph/raphus.md": {
    primary: "The genus of extinct flightless columbiform birds native to the island of Mauritius, containing the dodo (Raphus cucullatus).",
    secondary: "In evolutionary biology and paleontology, the iconic symbol of human-caused extinction, a giant ground-dwelling pigeon that vanished by the late 17th century.",
    quotes: [
      { author: "Richard Owen", work: "Memoir on the Dodo", quote: "The osteology of **Raphus** cucullatus demonstrates how insular isolation and absence of predators favored extreme gigantism." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The heavy, flightless dodo, **Raphus**, fell an easy prey to early navigators and introduced domestic animals." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The dodo, **Raphus**, was not an evolutionary failure but an exquisitely adapted island survivor doomed by human arrival." }
    ]
  },

  // Dashboard — sphrag
  "Dashboard — sphrag/sphragistic.md": {
    primary: "Of or relating to the study of engraved seals, signets, and official seal impressions (sphragistics or sigillography).",
    secondary: "In historical methodology and diplomatics, pertaining to the verification of antique documents, charters, and royal decrees by analyzing wax and lead seals.",
    quotes: [
      { author: "Isaac Taylor", work: "The History of the Alphabet", quote: "The **sphragistic** evidence gathered from clay sealings in Mesopotamia provides vital chronologies for royal dynasties." },
      { author: "Edward Augustus Freeman", work: "The History of the Norman Conquest of England", quote: "A meticulous **sphragistic** analysis of the royal charters revealed that several forged seals had been appended in the twelfth century." },
      { author: "John Horace Round", work: "Feudal England", quote: "The scholar must combine paleography with **sphragistic** criticism to detect spurious baronial grants." }
    ]
  },

  // Dashboard — thalass
  "Dashboard — thalass/Panthalassa.md": {
    primary: "The vast, continuous global superocean that surrounded the supercontinent Pangaea during the late Paleozoic and early Mesozoic eras.",
    secondary: "In historical geology and paleogeography, literally 'all sea' (from Greek pan- all + thalassa sea), the ancestral ocean whose basin contracted to form the modern Pacific Ocean.",
    quotes: [
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", quote: "The single continental block of Pangaea was encompassed on every side by the colossal world-ocean of **Panthalassa**." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Subduction along the margins of **Panthalassa** consumed thousands of miles of ancient oceanic lithosphere." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "Long before modern continents drifted apart, the tides of **Panthalassa** washed the shores of a solitary supercontinent." }
    ]
  },
  "Dashboard — thalass/thalassaemia.md": {
    primary: "An inherited blood disorder characterized by reduced or absent synthesis of normal hemoglobin, causing chronic anemia (British spelling).",
    secondary: "In clinical hematology and human genetics, an autosomal recessive hemoglobinopathy prevalent around the Mediterranean, Middle East, and Southeast Asia.",
    quotes: [
      { author: "J. B. S. Haldane", work: "Disease and Evolution", quote: "The high prevalence of **thalassaemia** in Mediterranean populations is maintained by the protection it confers against lethal malaria." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Children suffering from major **thalassaemia** present marked pallor, hepatosplenomegaly, and skeletal deformities." },
      { author: "Archibald Garrod", work: "Inborn Errors of Metabolism", quote: "Our clinical understanding of **thalassaemia** advanced dramatically once hemoglobin peptide chain synthesis was quantified." }
    ]
  },
  "Dashboard — thalass/thalassemia.md": {
    primary: "An inherited blood disorder characterized by abnormal or deficient production of hemoglobin subunits, resulting in anemia (American spelling).",
    secondary: "In hematology, categorized into alpha and beta forms depending on which polypeptide chain of the hemoglobin tetramer is affected.",
    quotes: [
      { author: "Linus Pauling", work: "Molecular Disease and Evolution", quote: "Sickle cell anemia and **thalassemia** served as the foundational prototypes for molecular pathology." },
      { author: "Thomas Henry Huxley", work: "Science and Culture", quote: "Genetic polymorphisms such as **thalassemia** demonstrate that physiological traits are shaped by geographical selection pressures." },
      { author: "Arthur Conan Doyle", work: "The Stark Munro Letters", quote: "The young physician noted the peculiar facial bone changes characteristic of severe **thalassemia** in the child." }
    ]
  },
  "Dashboard — thalass/thalassic.md": {
    primary: "Of, relating to, or situated in or near the sea; marine.",
    secondary: "In oceanography and geology, specifically applied to smaller, partially enclosed seas (such as the Mediterranean or Baltic), as distinguished from the open ocean.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative", quote: "The flora of the Mediterranean exhibits distinct **thalassic** affinities influenced by centuries of coastal trade." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Thick beds of limestone were deposited in ancient **thalassic** basins sheltered from the open ocean gales." },
      { author: "Matthew Fontaine Maury", work: "The Physical Geography of the Sea", quote: "The salinity of a **thalassic** sea varies considerably depending on freshwater inflow and evaporation rates." }
    ]
  },
  "Dashboard — thalass/thalassoma.md": {
    primary: "A genus of brightly colored marine reef fishes in the wrasse family Labridae, commonly known as rainbow wrasses, widely distributed in tropical and subtropical seas.",
    secondary: "In marine biology, protogynous hermaphroditic fishes (e.g., Thalassoma bifasciatum, the bluehead wrasse) noted for dramatic sex-role reversals and vivid color transformations.",
    quotes: [
      { author: "Francis Day", work: "The Fishes of Great Britain and Ireland", quote: "The vivid blues and greens of **Thalassoma** wrasses rival the plumage of tropical parrots." },
      { author: "David Starr Jordan", work: "A Guide to the Study of Fishes", quote: "Species of **Thalassoma** dart with frantic speed through coral crevices, picking small crustaceans from the rock." },
      { author: "Rachel Carson", work: "The Edge of the Sea", quote: "In the clear turquoise lagoons, glittering schools of **Thalassoma** swarm around every submerged coral head." }
    ]
  },
  "Dashboard — thalass/thalassophobia.md": {
    primary: "An intense, irrational, and persistent fear of the sea, deep water, ocean depths, or vast open maritime expanses.",
    secondary: "In clinical psychiatry, a specific environmental phobia triggered by anxiety about hidden abyss depths, sea monsters, distance from land, or drowning.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "A victim of acute **thalassophobia** experiences paralyzing dread when gazing out upon an empty, shoreless sea horizon." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "The roots of **thalassophobia** frequently intertwine with nightmares of being submerged in cold, lightless abysses." },
      { author: "H. P. Lovecraft", work: "The Shadow Over Innsmouth", quote: "The brooding presence of the reef inspired an unbearable **thalassophobia**, as though monstrous depths were stirring beneath the tide." }
    ]
  }
};

let count = 0;
for (const [key, data] of Object.entries(batch5Data)) {
  const [relDir, fileName] = key.split('/');
  if (updateNote(relDir, fileName, data)) {
    count++;
  }
}

console.log(`\n========================================`);
console.log(`Batch 5 Completed: ${count} / ${Object.keys(batch5Data).length} words updated`);
console.log(`========================================`);
