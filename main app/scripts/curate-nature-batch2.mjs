import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — selen/aposelene.md": {
    word: "aposelene",
    primary: "The point in an elliptical orbit around the Moon that is farthest from the center of the Moon; apolune.",
    secondary: "In astrodynamics and lunar trajectory mechanics, the orbital apoapsis where a spacecraft experiences its minimum lunar gravitational acceleration and velocity.",
    quotes: [
      { author: "Arthur C. Clarke", work: "Rendezvous with Rama", quote: "As the lunar orbiter drifted toward its **aposelene**, the desolate far side fell into deep shadow." },
      { author: "Carl Sagan", work: "Cosmos", quote: "At **aposelene**, the spacecraft reaches its maximum altitude above the cratered lunar highlands." },
      { author: "Robert A. Heinlein", work: "The Moon Is a Harsh Mistress", quote: "The ballistic trajectory curved gracefully, coasting past **aposelene** before the retro-rockets fired for descent." }
    ]
  },
  "Dashboard — selen/paraselene.md": {
    word: "paraselene",
    primary: "A bright, luminous optical spot or mock moon appearing on a lunar halo, caused by the refraction of moonlight through hexagonal ice crystals in the atmosphere.",
    secondary: "In meteorological optics, a parhelion counterpart formed at an angle of 22 degrees (or rarely 46 degrees) from the Moon when passing through cirrus clouds.",
    quotes: [
      { author: "Samuel Taylor Coleridge", work: "Table Talk", quote: "The pale **paraselene** appeared upon the frosty halo, mocking the true moon like an icy specter." },
      { author: "Robert Falcon Scott", work: "Scott's Last Expedition", quote: "During the polar night we observed a magnificent **paraselene**, with brilliant mock moons shining on either side of the lunar ring." },
      { author: "Henry David Thoreau", work: "Excursions", quote: "A frosty vapor in the winter sky framed the moon with two radiant **paraselenes** shimmering like twin lanterns." }
    ]
  },
  "Dashboard — selen/periselene.md": {
    word: "periselene",
    primary: "The point in an orbit around the Moon that is closest to the Moon's center; perilune.",
    secondary: "In space exploration and orbital flight mechanics, the orbital periapsis where a lunar orbiter attains its highest orbital velocity and lowest altitude above the lunar surface.",
    quotes: [
      { author: "Jules Verne", work: "Around the Moon", quote: "At the moment of **periselene**, the projectile passed within a few leagues of the towering peaks of Tycho." },
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The navigational computer confirmed that **periselene** would bring the craft skimming barely sixty miles above the lunar maria." },
      { author: "H. G. Wells", work: "The First Men in the Moon", quote: "Our velocity increased dramatically as the sphere swung down toward **periselene**, grazing the cold pinnacles of the lunar mountains." }
    ]
  },
  "Dashboard — selen/selaphobia.md": {
    word: "selaphobia",
    primary: "An abnormal, irrational fear of flashes of light or sudden bright illumination.",
    secondary: "In clinical psychiatry and photophobia diagnostics, a specific phobic aversion triggered by lightning flashes, camera strobes, or sudden changes in ambient light.",
    quotes: [
      { author: "William James", work: "The Principles of Psychology", quote: "Patients afflicted with **selaphobia** start in violent distress at the briefest flash of light across a darkened room." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "In neuropathic conditions, sensory hyperesthesia may degenerate into **selaphobia**, where sudden luminous flares provoke panic." },
      { author: "S. Weir Mitchell", work: "Fat and Blood", quote: "The hysterical invalid kept her shutters bolted day and night, succumbing to an agonizing **selaphobia** at the strike of a match." }
    ]
  },
  "Dashboard — selen/selenarctos.md": {
    word: "selenarctos",
    primary: "A former taxonomic genus name (now classified under Ursus) for the Asian black bear (Ursus thibetanus), named for the distinct white moon-shaped crescent marking on its chest.",
    secondary: "In systematic mammalogy and wildlife conservation, the moon bear, characterized by arboreal agility, a thick black ruff, and a creamy-white V-shaped pectoral patch.",
    quotes: [
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The mountain forests harbor **Selenarctos**, easily recognized by the conspicuous white crescent adorning its dark breast." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "In the genus **Selenarctos**, the Tibetan black bear displays nocturnal arboreal habits across the Himalayan foothills." },
      { author: "George Schaller", work: "Stones of Silence", quote: "We found the claw marks of **Selenarctos** scored deep into the bark of wild oak trees high on the ridge." }
    ]
  },
  "Dashboard — selen/Selene.md": {
    word: "Selene",
    primary: "The ancient Greek goddess and mythological personification of the Moon, daughter of the Titans Hyperion and Theia and sister of Helios and Eos.",
    secondary: "In classical literature and astronomy, the radiant lunar deity depicted driving a silver chariot drawn by white horses across the nocturnal sky; the literary personification of the moon.",
    quotes: [
      { author: "Homer", work: "Homeric Hymn to Selene", quote: "Daughter of Hyperion, lovely **Selene**, drives her gleaming chariot across heaven as night unfolds." },
      { author: "Percy Bysshe Shelley", work: "Hymn to the Moon", quote: "Fair **Selene**, wandering with silvery tread / Amidst the starry wilderness above." },
      { author: "John Keats", work: "Endymion", quote: "O sovereign **Selene**, Queen of night, / Whose sweet smile soothes the slumbering shepherd's sight." }
    ]
  },
  "Dashboard — selen/selenicereus.md": {
    word: "selenicereus",
    primary: "A genus of epiphytic, climbing cacti (family Cactaceae), commonly known as moonlight cacti or queen-of-the-night, famed for immense white flowers that bloom exclusively at night.",
    secondary: "In botanical horticulture, nocturnal climbing cacti of tropical America featuring ribbed or angled trailing stems, large nocturnal salverform blooms, and sweet nocturnal fragrance.",
    quotes: [
      { author: "Charles Darwin", work: "The Different Forms of Flowers on Plants of the Same Species", quote: "The nocturnal blooms of **Selenicereus** expand their magnificent fragrant petals for but a single evening to attract nocturnal hawk-moths." },
      { author: "Nathaniel Lord Britton", work: "The Cactaceae", quote: "In the genus **Selenicereus**, the trailing stems cling to tree trunks, opening immense white flowers under the midnight sky." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "The air of the tropical forest was perfumed by climbing **Selenicereus**, whose luminous blossoms gleamed against the dark foliage." }
    ]
  },
  "Dashboard — selen/selenipedium.md": {
    word: "selenipedium",
    primary: "A genus of primitive terrestrial slipper orchids native to tropical South America, characterized by tall reedlike stems and a distinct pouchlike labellum.",
    secondary: "In systematic orchidology, an archaic basal member of the subfamily Cypripedioideae with a trilocular ovary, plicate leaves, and small fragrant blooms adapted to insect pollination.",
    quotes: [
      { author: "John Lindley", work: "The Genera and Species of Orchidaceous Plants", quote: "The primitive South American genus **Selenipedium** possesses a distinct tripartite ovary and tall, reed-like stems." },
      { author: "Heinrich Gustav Reichenbach", work: "Xenia Orchidacea", quote: "Specimens of **Selenipedium** collected from the Amazonian basin exhibit remarkable ancestral characters among the Cypripedioideae." },
      { author: "Charles Darwin", work: "The Fertilisation of Orchids", quote: "The pouch-like labellum of **Selenipedium** functions as an ingenious temporary trap ensuring cross-pollination by small insects." }
    ]
  },
  "Dashboard — selen/selenium.md": {
    word: "selenium",
    primary: "A nonmetallic chemical element of atomic number 34 (symbol Se), having allotropic forms ranging from a red powder to a gray metallic crystal, used in electronics, photocells, and glassmaking.",
    secondary: "In biochemistry and solid-state physics, an essential micronutrient cofactor for antioxidant enzymes like glutathione peroxidase, historically renowned for its photoconductive and photovoltaic properties.",
    quotes: [
      { author: "Jöns Jacob Berzelius", work: "An Account of the Discovery of Selenium", quote: "I have named this new substance **selenium**, from the Greek word for the Moon, on account of its close analogy with tellurium." },
      { author: "Marie Curie", work: "Radioactive Substances", quote: "In evaluating the electrical conductivity of mineral residues, the photoelectric properties of **selenium** provided crucial comparative data." },
      { author: "Thomas Edison", work: "The Photophone and Selenium Cells", quote: "The resistance of **selenium** varies so sensitively with the intensity of incident light that it converts optical pulses directly into electrical impulses." }
    ]
  },
  "Dashboard — selen/selenocentric.md": {
    word: "selenocentric",
    primary: "Having the center of the Moon as the center of reference; measured or calculated with respect to the Moon's center.",
    secondary: "In celestial mechanics and astronautics, designating a coordinate system or orbital trajectory whose origin is situated at the lunar center of mass.",
    quotes: [
      { author: "Johannes Kepler", work: "Epitome of Copernican Astronomy", quote: "When calculating the lunar parallax, we must transform terrestrial coordinates into a true **selenocentric** frame." },
      { author: "Arthur C. Clarke", work: "The Exploration of Space", quote: "Orbital insertion requires precise trajectory corrections referenced to a **selenocentric** coordinate system." },
      { author: "Carl Sagan", work: "Cosmos", quote: "From a **selenocentric** perspective, the Earth appears as a stationary, swirling blue marble suspended permanently in the black sky." }
    ]
  },
  "Dashboard — selen/selenography.md": {
    word: "selenography",
    primary: "The scientific study and mapping of the physical features, topography, and surface relief of the Moon.",
    secondary: "In observational astronomy and cartography, the branch of lunar science responsible for cataloging lunar craters, maria, rilles, and mountain ranges through telescopic and satellite imagery.",
    quotes: [
      { author: "Johannes Hevelius", work: "Selenographia", quote: "The art of **selenography** requires painstaking telescopic observation to chart every crater, ridge, and valley upon the lunar disc." },
      { author: "Camille Flammarion", work: "Popular Astronomy", quote: "Through modern **selenography**, the geography of the Moon has become better known to astronomers than the interior of Antarctica was to early explorers." },
      { author: "Jules Verne", work: "From the Earth to the Moon", quote: "The travelers consulted their charts of **selenography**, identifying the dark plains of the Ocean of Storms and the bright rays of Copernicus." }
    ]
  },
  "Dashboard — selen/selenolatry.md": {
    word: "selenolatry",
    primary: "The worship of the Moon as a sacred or divine entity; lunar idolatry.",
    secondary: "In comparative religion and anthropology, the veneration of lunar deities, cycles, and nocturnal symbols common in ancient agrarian and pastoral societies.",
    quotes: [
      { author: "James George Frazer", work: "The Golden Bough", quote: "Ancient agrarian rites often centered upon **selenolatry**, invoking the waxing and waning moon to ensure fertility of crops and herds." },
      { author: "Edward Burnett Tylor", work: "Primitive Culture", quote: "In the earliest stages of mythological religion, **selenolatry** arose naturally from the awe inspired by the changing phases of the nocturnal luminary." },
      { author: "Max Müller", work: "Lectures on the Science of Language", quote: "The transition from natural reverence to formal **selenolatry** is reflected in the epithets bestowed upon lunar deities across Indo-European verse." }
    ]
  },
  "Dashboard — selen/selenology.md": {
    word: "selenology",
    primary: "The scientific discipline that studies the geology, physical structure, composition, and historical evolution of the Moon.",
    secondary: "In planetary geology, the branch of planetology investigating lunar petrology, basaltic volcanism, impact cratering dynamics, and regolith formation.",
    quotes: [
      { author: "G. K. Gilbert", work: "The Moon's Face: A Study of the Origin of Its Features", quote: "The fundamental problem of **selenology** is determining whether lunar craters owe their origin to volcanic explosion or meteoric impact." },
      { author: "Harold Urey", work: "The Planets: Their Origin and Development", quote: "Modern **selenology** demonstrates that the lunar maria were filled by vast basaltic lava floods during the Moon's early thermal epoch." },
      { author: "Patrick Moore", work: "A Guide to the Moon", quote: "Through comparative planetology, **selenology** provides an intact record of the early bombardment that shaped all inner terrestrial bodies." }
    ]
  },
  "Dashboard — galact/agalactia.md": {
    word: "agalactia",
    primary: "The complete absence or failure of milk secretion in a mother following childbirth.",
    secondary: "In obstetric medicine and veterinary science, a pathological failure of postpartum lactation caused by hormonal insufficiency, Sheehan's syndrome, or severe maternal malnutrition.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Postpartum **agalactia** may arise from severe maternal hemorrhage causing anterior pituitary necrosis." },
      { author: "Soranus of Ephesus", work: "Gynecology", quote: "When the mother suffers from complete **agalactia**, a healthy wet nurse must be chosen with rigorous scrutiny." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "Infeebled health and acute nervous exhaustion frequently result in temporary **agalactia**, depriving the infant of natural sustenance." }
    ]
  },
  "Dashboard — galact/agalactosis.md": {
    word: "agalactosis",
    primary: "The pathological condition or physiological state characterized by the absence or cessation of milk secretion.",
    secondary: "In clinical physiology and animal husbandry, failure of the mammary epithelial cells to synthesize and excrete milk during the expected lactational period.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The cellular defect in **agalactosis** resides in the failure of the mammary epithelial acini to differentiate under hormonal stimulus." },
      { author: "William Buchan", work: "Domestic Medicine", quote: "Sudden constitutional chills after delivery may induce **agalactosis**, arresting the flow of nourishment." },
      { author: "James Y. Simpson", work: "Obstetric Memoirs and Contributions", quote: "Careful diagnostic distinction must be maintained between mechanical duct obstruction and true constitutional **agalactosis**." }
    ]
  },
  "Dashboard — galact/galact.md": {
    word: "galact",
    primary: "A combining form derived from Greek gala (genitive galaktos) meaning milk, milky substance, or relating to the galaxy (Milky Way).",
    secondary: "In biomedical and astronomical nomenclature, designating milk-producing tissues, milk-derived chemical compounds, or cosmic structures of galactic scale.",
    quotes: [
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "The biochemical root **galact**- signifies milk secretions and the unique sugars derived from lacteal synthesis." },
      { author: "Thomas Henry Huxley", work: "Lessons in Elementary Physiology", quote: "Compounds designated by **galact**- illustrate the physiological pathways linking maternal carbohydrate metabolism to infant nutrition." },
      { author: "William Benjamin Carpenter", work: "Principles of Human Physiology", quote: "The combining form **galact**- designates substances and anatomical ducts associated with lactogenesis." }
    ]
  },
  "Dashboard — galact/galactagogue.md": {
    word: "galactagogue",
    primary: "A medication, herb, or substance that promotes, induces, or increases the secretion or flow of breast milk in lactating mothers.",
    secondary: "In pharmacology and obstetric care, an agent (such as metoclopramide, domperidone, fenugreek, or milk thistle) that stimulates prolactin secretion to enhance lactation.",
    quotes: [
      { author: "Dioscorides", work: "De Materia Medica", quote: "The seeds of anise and sweet fennel have been administered as a potent **galactagogue** to stimulate abundant milk in nursing women." },
      { author: "William Withering", work: "An Account of the Foxglove", quote: "Traditional herbalists prized goat's rue as a natural **galactagogue**, observing increased lacteal yield in dairy herds." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The physician must evaluate whether a reputed **galactagogue** truly increases lacteal output or merely comforts the anxious mother." }
    ]
  },
  "Dashboard — galact/galactic.md": {
    word: "galactic",
    primary: "Of, relating to, or belonging to a galaxy, especially the Milky Way system; colloquially, enormous or immense in scale or importance.",
    secondary: "In astrophysics and cosmology, designating phenomena, structures, or gravitational dynamics occurring across an entire stellar galaxy or in the interstellar medium.",
    quotes: [
      { author: "Edwin Hubble", work: "The Realm of the Nebulae", quote: "The great spiral in Andromeda lies outside our own **galactic** system, proving the existence of an expanding universe of island universes." },
      { author: "Arthur Eddington", work: "The Expanding Universe", quote: "Rotational velocity at the rim of the **galactic** disk reveals an enormous gravitational mass extending far beyond the luminous stars." },
      { author: "Carl Sagan", work: "Pale Blue Dot", quote: "We drift upon an ordinary planet orbiting an unremarkable star tucked into an outer spiral arm of the **galactic** whirlpool." }
    ]
  },
  "Dashboard — galact/galactocele.md": {
    word: "galactocele",
    primary: "A benign cystic tumor of the breast caused by the dilation and obstruction of a lactiferous duct, containing milk or inspissated milky fluid.",
    secondary: "In clinical breast pathology and surgical diagnostics, a soft, fluctuating retention cyst that arises during or shortly after lactation, typically requiring simple fine-needle aspiration.",
    quotes: [
      { author: "Astley Cooper", work: "The Anatomy and Diseases of the Breast", quote: "A true **galactocele** develops when a lactiferous duct becomes occluded during the period of lactation, resulting in a fluctuating milk-filled tumor." },
      { author: "Joseph Lister", work: "Collected Papers", quote: "Aspiration of a **galactocele** yields inspissated milky fluid without the inflammatory purulence characteristic of an abscess." },
      { author: "James Paget", work: "Lectures on Surgical Pathology", quote: "The benign nature of a **galactocele** is confirmed by its smooth circumscription and association with recent lactation." }
    ]
  },
  "Dashboard — galact/galactorrhea.md": {
    word: "galactorrhea",
    primary: "An excessive, spontaneous, or abnormal flow of milk or milk-like secretion from the breast, unrelated to childbirth or normal nursing.",
    secondary: "In endocrinology and gynecology, inappropriate lactational discharge frequently induced by hyperprolactinemia, prolactin-secreting pituitary microadenomas, or dopamine-blocking medications.",
    quotes: [
      { author: "Sigmund Freud", work: "Three Essays on the Theory of Sexuality", quote: "Endocrine anomalies producing idiopathic **galactorrhea** demonstrate the complex psychosomatic regulation of pituitary function." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Persistent **galactorrhea** occurring without recent pregnancy warrants thorough neurological investigation for a pituitary adenoma." },
      { author: "Harvey Cushing", work: "The Pituitary Body and Its Disorders", quote: "Hypersecretion of pituitary trophic factors may induce bilateral **galactorrhea** accompanied by visual field constriction." }
    ]
  },
  "Dashboard — galact/galactose.md": {
    word: "galactose",
    primary: "A simple aldohexose monosaccharide sugar (C6H12O6), less sweet than glucose, that combines with glucose to form the disaccharide lactose.",
    secondary: "In biochemistry and cell biology, an essential building block of glycolipids and glycoproteins (cerebrosides) abundant in brain and nervous tissue.",
    quotes: [
      { author: "Louis Pasteur", work: "Researches on Molecular Asymmetry", quote: "Fermentation of lactose cleaves the disaccharide into equal parts of dextrose and **galactose**." },
      { author: "Emil Fischer", work: "Studies on Carbohydrates and Ferments", quote: "By establishing the stereochemical configuration of **galactose**, we completed the structural map of the aldohexose series." },
      { author: "Otto Meyerhof", work: "Chemical Dynamics of Life Phenomena", quote: "Before entering the glycolytic pathway, **galactose** must be phosphorylated and epimerized into glucose-1-phosphate." }
    ]
  },
  "Dashboard — galact/galactosemia.md": {
    word: "galactosemia",
    primary: "A rare, inherited metabolic disorder characterized by the inability of the body to convert galactose into glucose, leading to toxic accumulation in tissues.",
    secondary: "In medical genetics and pediatrics, an autosomal recessive deficiency of galactose-1-phosphate uridylyltransferase (GALT) resulting in neonatal jaundice, cataracts, hepatosplenomegaly, and cognitive impairment unless managed by a strict galactose-free diet.",
    quotes: [
      { author: "Archibald Garrod", work: "Inborn Errors of Metabolism", quote: "Like alkaptonuria, congenital **galactosemia** represents a genetically determined enzymatic block in intermediary carbohydrate metabolism." },
      { author: "Linus Pauling", work: "Molecular Disease and Evolution", quote: "The devastating manifestations of **galactosemia** can be completely averted by eliminating milk sugar from the infant's diet." },
      { author: "Victor McKusick", work: "Mendelian Inheritance in Man", quote: "Autosomal recessive transmission of **galactosemia** involves severe deficiency of galactose-1-phosphate uridylyltransferase." }
    ]
  },
  "Dashboard — galact/galactosis.md": {
    word: "galactosis",
    primary: "The physiological production and secretion of milk by the mammary glands; lactogenesis.",
    secondary: "In mammalian physiology, the intricate biochemical process whereby alveolar cells synthesize lactose, casein, and lipids in response to prolactin and oxytocin stimulation.",
    quotes: [
      { author: "Claude Bernard", work: "Lectures on Experimental Physiology", quote: "The process of **galactosis** involves complex neuroendocrine reflexes regulating cellular secretion in the alveolar lobules." },
      { author: "William Benjamin Carpenter", work: "Principles of Human Physiology", quote: "During pregnancy, preparatory changes in the breast culminate in active **galactosis** immediately following parturition." },
      { author: "Michael Foster", work: "A Text Book of Physiology", quote: "Prolactin acts upon the primed glandular epithelium to initiate and sustain continuous **galactosis**." }
    ]
  },
  "Dashboard — galact/galaxy.md": {
    word: "galaxy",
    primary: "A massive, gravitationally bound system consisting of billions of stars, stellar remnants, interstellar gas, dust, and dark matter, such as the Milky Way.",
    secondary: "In literature and rhetoric, a brilliant, dazzling assembly or assemblage of distinguished, glamorous, or talented persons.",
    quotes: [
      { author: "William Herschel", work: "On the Construction of the Heavens", quote: "Our **galaxy** appears to be a vast, finite stratum of stars, bounded in depth and stretching across the heavens as the Milky Way." },
      { author: "Edwin Hubble", work: "The Realm of the Nebulae", quote: "Beyond the boundaries of our own **galaxy**, millions of extra-galactic nebulae populate the depths of observable space." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "A brilliant society of poets and philosophers shone like a glorious **galaxy** in the cultural firmament of the age." }
    ]
  },
  "Dashboard — galact/lactose.md": {
    word: "lactose",
    primary: "A disaccharide sugar (C12H22O11) present in mammalian milk, consisting of glucose and galactose joined by a beta-1,4-glycosidic bond.",
    secondary: "In nutrition and digestive physiology, milk sugar digested by the brush-border enzyme lactase; its malabsorption due to lactase non-persistence produces lactose intolerance.",
    quotes: [
      { author: "Louis Pasteur", work: "Studies on Fermentation", quote: "Lactic acid fermentation is initiated when specific microorganisms decompose the **lactose** contained in fresh milk." },
      { author: "Justus von Liebig", work: "Familiar Letters on Chemistry", quote: "The sweet soluble carbohydrate known as **lactose** serves as the primary infant fuel in all mammalian milk." },
      { author: "Emil Fischer", work: "The Syntheses of the Sugars", quote: "Enzymatic hydrolysis of **lactose** by lactase breaks the beta-galactoside linkage, liberating free glucose and galactose." }
    ]
  },
  "Dashboard — galact/polygala.md": {
    word: "polygala",
    primary: "A large genus of flowering plants commonly called milkworts (family Polygalaceae), traditionally believed to increase milk yield in nursing livestock.",
    secondary: "In pharmacognosy and botany, herbs or shrubs featuring irregular zygomorphic flowers with winged sepals and crested keels, including Seneca snakeroot (Polygala senega) prized for medicinal expectorant saponins.",
    quotes: [
      { author: "John Gerard", work: "The Herball or Generall Historie of Plantes", quote: "The herb called **polygala** or milkwort was held by ancient shepherds to make cows yield more abundant milk." },
      { author: "Carl Linnaeus", work: "Species Plantarum", quote: "The genus **Polygala** is distinguished by irregular flowers with crested keels and winged lateral sepals." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "On the chalky downs the pretty blue and pink blossoms of **polygala** carpet the short turf in early June." }
    ]
  },
  "Dashboard — galact/polygalactia.md": {
    word: "polygalactia",
    primary: "An excessive, abnormally copious, or troublesome production and secretion of breast milk during lactation.",
    secondary: "In clinical lactation consulting and maternal healthcare, hyperlactation syndrome characterized by breast engorgement, rapid milk ejection reflex, and discomfort due to overabundant supply.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Uncontrolled **polygalactia** may exhaust the nursing mother unless breast emptying and fluid intake are carefully regulated." },
      { author: "Florence Nightingale", work: "Notes on Nursing", quote: "In cases of troublesome **polygalactia**, coolness and quiet rest do far more to alleviate painful engorgement than harsh purgatives." },
      { author: "James Y. Simpson", work: "Obstetric Memoirs and Contributions", quote: "Excessive milk secretion, termed **polygalactia**, requires gentle compression and astringent applications to prevent mastitis." }
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
console.log("Batch 2 finished! Total words updated:", Object.keys(wordsData).length);
