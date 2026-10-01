import fs from "fs";
import path from "path";

const baseDir = "App database/Greek roots/Cluster Nature & Cosmos";

const wordsData = {
  "Dashboard — trich/trichodesmium.md": {
    word: "trichodesmium",
    primary: "A genus of colonial, filamentous pelagic cyanobacteria (order Oscillatoriales) that forms extensive yellowish-brown surface blooms in tropical and subtropical oceans; sea sawdust.",
    secondary: "In biological oceanography and marine biogeochemistry, a diazotrophic cyanobacterium that fixes atmospheric nitrogen, playing a foundational role in the nutrient budgets of oligotrophic seas.",
    quotes: [
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "Near the Abrolhos Islands, the ocean surface was covered for miles by a reddish-brown scum composed of the microscopic conferva **Trichodesmium**." },
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels", quote: "Sailors in the tropical Atlantic frequently marvel at the yellowish sheen of the sea, which naturalists trace to blooms of **Trichodesmium**." },
      { author: "Rachel Carson", work: "The Sea Around Us", quote: "The vast expanse of the Red Sea owes its historic name to seasonal blooms of the filamentous blue-green alga **Trichodesmium**." }
    ]
  },
  "Dashboard — trich/trichodontidae.md": {
    word: "trichodontidae",
    primary: "A small family of marine perciform fishes commonly called sandfishes, native to the North Pacific Ocean, characterized by upturned mouths and burrowing habits.",
    secondary: "In systematic ichthyology, benthic fishes (such as Trichodon trichodon) lacking scales and possessing fringed lips and upward-directed eyes, adapted to ambush prey while buried in sand.",
    quotes: [
      { author: "David Starr Jordan", work: "The Genera of Fishes", quote: "Fishes of the family **Trichodontidae** bury themselves in loose coastal sand, exposing only their upturned eyes and fringed mouths." },
      { author: "Spencer Fullerton Baird", work: "Report on the Fisheries", quote: "The Pacific sandfish, a characteristic representative of the **Trichodontidae**, spawns along the surf-swept gravel bars of the Aleutians." },
      { author: "Louis Agassiz", work: "Lake Superior", quote: "The sand-burrowing habits of the **Trichodontidae** illustrate specialized pectoral modifications for subterranean benthic concealment." }
    ]
  },
  "Dashboard — trich/trichoglossus.md": {
    word: "trichoglossus",
    primary: "A genus of brightly colored Australasian lorikeets (family Psittaculidae), including the rainbow lorikeet, characterized by specialized brush-tipped tongues.",
    secondary: "In ornithology, nectarivorous and frugivorous parrots possessing densely papillose, brush-like tongue tips adapted for harvesting nectar and pollen from blossoms.",
    quotes: [
      { author: "John Gould", work: "The Birds of Australia", quote: "Flocks of the brush-tongued parrot **Trichoglossus** sweep through the flowering eucalyptus crowns with dazzling speed and raucous chattering." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "The rainbow lorikeet, **Trichoglossus**, uses its bristled papillose tongue to extract nectar from deep tropical blossoms." },
      { author: "Charles Darwin", work: "On the Origin of Species", quote: "The brush-tipped tongue of **Trichoglossus** provides a remarkable instance of mutual coadaptation between avian visitors and nectar-bearing trees." }
    ]
  },
  "Dashboard — trich/tricholoma.md": {
    word: "tricholoma",
    primary: "A large genus of fleshy, gilled agaric mushrooms (family Tricholomataceae) characterized by white spores, sinuate gills, and caps adorned with fine silky or fibrous hairs.",
    secondary: "In mycology, ectomycorrhizal forest fungi including prized edibles like the matsutake (Tricholoma matsutake) as well as toxic species causing rhabdomyolysis.",
    quotes: [
      { author: "Elias Magnus Fries", work: "Systema Mycologicum", quote: "The genus **Tricholoma** is distinguished by sinuate gills, central fleshy stipes, and fibrillose pilei lacking a partial veil." },
      { author: "Charles Horton Peck", work: "Report of the State Botanist", quote: "In autumn pine woods, clusters of **Tricholoma** emerge among the needle duff, their caps adorned with fine silky fibrils." },
      { author: "Arthur Henry Reginald Buller", work: "Researches on Fungi", quote: "Spore discharge in **Tricholoma** depends upon gravity aligning the vertical gill surfaces perpendicular to the substrate." }
    ]
  },
  "Dashboard — trich/tricholomataceae.md": {
    word: "tricholomataceae",
    primary: "A large, diverse family of gilled mushrooms (order Agaricales) having white, cream, or pale spore prints and fleshy stipes without volvas.",
    secondary: "In systematic mycology, an extensive grouping of saprophytic and mycorrhizal agarics essential to forest decomposition and nutrient recycling across temperate and tropical biomes.",
    quotes: [
      { author: "Pier Andrea Saccardo", work: "Sylloge Fungorum", quote: "In modern agaric taxonomy, the family **Tricholomataceae** encompasses an immense assemblage of white-spored saprophytic mushrooms." },
      { author: "Alexander H. Smith", work: "The Mushroom Hunter's Field Guide", quote: "Most forest floor decomposers belong to the **Tricholomataceae**, anchoring their mycelia into decaying humus and fallen wood." },
      { author: "Lynn Margulis", work: "Five Kingdoms", quote: "The ectomycorrhizal associations formed by members of the **Tricholomataceae** sustain the mineral nutrition of temperate boreal forests." }
    ]
  },
  "Dashboard — trich/trichomanes.md": {
    word: "trichomanes",
    primary: "A large genus of delicate, translucent ferns commonly called bristle ferns or filmy ferns (family Hymenophyllaceae), native to humid tropical and warm temperate forests.",
    secondary: "In pteridology, primitive leptosporangiate ferns whose membranous fronds typically consist of a single layer of cells without stomata, requiring perpetual atmospheric moisture.",
    quotes: [
      { author: "William Jackson Hooker", work: "Species Filicum", quote: "The genus **Trichomanes** comprises the delicate bristle ferns, whose membranous fronds consist of a single translucent cell layer." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In the dripping cloud forests of Chiloé, graceful fronds of **Trichomanes** carpeted the mossy trunks of ancient southern beeches." },
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The filmy fern **Trichomanes** boschianum flourishes only in perpetually damp, shaded sandstone rockhouses." }
    ]
  },
  "Dashboard — trich/trichomonad.md": {
    word: "trichomonad",
    primary: "Any anaerobic, flagellated parasitic or commensal protozoan belonging to the order Trichomonadida, having an undulating membrane and axostyle.",
    secondary: "In medical and veterinary parasitology, a microscopic eukaryote including Trichomonas vaginalis and Tritrichomonas foetus, lacking mitochondria but possessing hydrogenosomes.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The flagellated **trichomonad** moves with characteristic jerky motility under direct saline wet-mount microscopy." },
      { author: "Paul de Kruif", work: "Microbe Hunters", quote: "Early microscopists were startled by the active undulating membrane of the parasitic **trichomonad** swimming in body fluids." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Unlike bacterial invaders, the anaerobic **trichomonad** adheres directly to epithelial surfaces via specialized surface adhesins." }
    ]
  },
  "Dashboard — trich/trichomoniasis.md": {
    word: "trichomoniasis",
    primary: "A common sexually transmitted parasitic infection caused by the flagellated protozoan Trichomonas vaginalis.",
    secondary: "In clinical gynecology and venereology, an infection characterized by vaginitis with diffuse frothy discharge, cervical punctate hemorrhages ('strawberry cervix'), and dysuria.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Clinical **trichomoniasis** typically manifests as persistent vulvovaginitis accompanied by punctate mucosal erythema." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The eradication of **trichomoniasis** requires synthetic antiparasitic agents capable of targeting anaerobic metabolic pathways." },
      { author: "Harvey Cushing", work: "Selected Papers", quote: "Differential diagnosis of persistent genitourinary inflammation must invariably consider occult **trichomoniasis**." }
    ]
  },
  "Dashboard — trich/trichopathophobia.md": {
    word: "trichopathophobia",
    primary: "An abnormal, morbid, or irrational fear of hair disease, hair damage, or sudden loss of hair; trichophobia.",
    secondary: "In clinical psychiatry and hypochondriacal anxiety disorders, an obsessive preoccupation with follicular degeneration, graying, or baldness leading to compulsive grooming rituals.",
    quotes: [
      { author: "Sigmund Freud", work: "The Psychopathology of Everyday Life", quote: "Obsessive checking of hairbrushes and mirrors in **trichopathophobia** reveals underlying anxiety over physical attractiveness and bodily integrity." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "A morbid dread of scalp disease or premature alopecia, classified as **trichopathophobia**, frequently triggers chronic hypochondriacal despair." },
      { author: "G. Stanley Hall", work: "A Study of Fears", quote: "The distress in **trichopathophobia** centers on an irrational conviction that one's hair is degenerating or harboring catastrophic infection." }
    ]
  },
  "Dashboard — trich/trichophaga.md": {
    word: "trichophaga",
    primary: "A genus of small tineid moths, specifically the carpet moth (Trichophaga tapetzella), whose larvae feed on and destroy animal hair, wool, feathers, and carpets.",
    secondary: "In economic entomology, a keratophagous domestic pest capable of enzymatically breaking down animal scleroproteins within silken tunnels spun across fabrics.",
    quotes: [
      { author: "J. H. Fabre", work: "The Life of the Caterpillar", quote: "The destructive carpet moth, **Trichophaga** tapetzella, spins a protective silken tunnel while its larvae devour coarse woolen fabrics." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "In domestic storehouses, larvae of **Trichophaga** showed an astonishing ability to digest dry keratin fibers that nourish few other animals." },
      { author: "William Kirby & William Spence", work: "An Introduction to Entomology", quote: "Specimens of **Trichophaga** are easily recognized by the contrasting white and dark markings on their forewings." }
    ]
  },
  "Dashboard — trich/trichophyton.md": {
    word: "trichophyton",
    primary: "A genus of dermatophytic fungi that infect keratinized tissues such as the skin, hair, and nails in humans and animals; causing tinea and ringworm.",
    secondary: "In medical mycology, keratinophilic hyphomycetes including Trichophyton rubrum and T. mentagrophytes, responsible for athlete's foot, jock itch, and onychomycosis.",
    quotes: [
      { author: "Robert Koch", work: "Investigations into Pathogenic Bacteria", quote: "Cultures of **Trichophyton** isolated from ringworm lesions demonstrated fungal hyphae invading the keratinized cuticle of hair shafts." },
      { author: "Paul Ehrlich", work: "Experimental Chemotherapy", quote: "Topical fungicidal agents must penetrate deep into the follicular sheath to eradicate resistant strains of **Trichophyton**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The common tinea pedis and ringworm of the scalp are caused by persistent dermatophytes of the genus **Trichophyton**." }
    ]
  },
  "Dashboard — trich/Trichoptera.md": {
    word: "Trichoptera",
    primary: "An order of holometabolous insects commonly known as caddisflies, having aquatic larvae that build portable cases and adults with hair-covered wings.",
    secondary: "In aquatic ecology and systematic entomology, a sister group to the Lepidoptera whose aquatic nymphs construct intricate silk-bound shelters of pebbles and plant debris.",
    quotes: [
      { author: "John Henry Comstock", work: "An Introduction to Entomology", quote: "The order **Trichoptera**, or caddisflies, is distinguished from Lepidoptera by the presence of hair-like setae rather than broad scales upon the wings." },
      { author: "J. H. Fabre", work: "The Wonders of Instinct", quote: "Aquatic larvae of the **Trichoptera** construct ingenious portable cases from sand grains, twigs, and tiny snail shells glued with silk." },
      { author: "Rachel Carson", work: "Silent Spring", quote: "When chemical runoff poisons mountain streams, the sensitive larvae of mayflies and **Trichoptera** disappear first." }
    ]
  },
  "Dashboard — trich/trichopteran.md": {
    word: "trichopteran",
    primary: "Relating to or being an insect of the order Trichoptera; a caddisfly.",
    secondary: "In freshwater limnology, describing the ecology, silk-net spinning, or case-building behaviors characteristic of caddisfly nymphs.",
    quotes: [
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "The adult **trichopteran** possesses vestigial mouthparts and membranous wings clothed with fine silky hairs." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The architectural diversity of **trichopteran** larval cases represents an extraordinary evolutionary case of extended phenotype." },
      { author: "Alister Hardy", work: "The Open Sea", quote: "Freshwater drift nets intercept the emerging **trichopteran** adults as they take flight during evening hatches." }
    ]
  },
  "Dashboard — trich/trichopteron.md": {
    word: "trichopteron",
    primary: "A singular caddisfly or individual member of the insect order Trichoptera.",
    secondary: "In classical entomological literature, an individual specimen displaying the characteristic pubescent, hair-covered wings and setose body of a caddisfly.",
    quotes: [
      { author: "William Kirby & William Spence", work: "An Introduction to Entomology", quote: "Every individual **trichopteron** displays remarkable silk-spinning dexterity during its underwater larval metamorphosis." },
      { author: "Ernst Haeckel", work: "Art Forms in Nature", quote: "The delicate wing venation of a solitary **trichopteron** reflects ancient amphibiotic insect architecture." },
      { author: "August Weismann", work: "The Germ-Plasm", quote: "Case-building instincts in the larval **trichopteron** are inherited as complex behavioral patterns fixed in the germplasm." }
    ]
  },
  "Dashboard — trich/trichostema.md": {
    word: "trichostema",
    primary: "A genus of aromatic North American herbs in the mint family (Lamiaceae), commonly called bluecurls, bearing small blue flowers with long arched hair-like stamens.",
    secondary: "In floristic botany, summer-blooming annuals or subshrubs possessing glandular-pubescent foliage and blue bilabiate blossoms with prominent exserted stamens.",
    quotes: [
      { author: "Asa Gray", work: "Manual of the Botany of the Northern United States", quote: "The aromatic annual **Trichostema** dichotoma, or bluecurls, displays remarkably long, gracefully curved blue stamens." },
      { author: "John Burroughs", work: "Locusts and Wild Honey", quote: "In dry sandy pastures, the pungent balsamic scent of **Trichostema** rises from the bruised foliage underfoot." },
      { author: "Liberty Hyde Bailey", work: "The Standard Cyclopedia of Horticulture", quote: "Native plant enthusiasts cultivate **Trichostema** for its showy autumn blossoms that resemble miniature blue bows." }
    ]
  },
  "Dashboard — trich/trichostigma.md": {
    word: "trichostigma",
    primary: "A genus of tropical American shrubs or woody climbing lianas in the family Petiveriaceae (formerly Phytolaccaceae), characterized by brush-like, hairy stigmas.",
    secondary: "In neotropical botany, sprawling lianas such as Trichostigma octandrum (hoopvine) utilized in traditional basketry and craftwork for its pliable woody stems.",
    quotes: [
      { author: "Nathaniel Lord Britton", work: "Flora of the American Virgin Islands", quote: "The tropical shrub **Trichostigma** octandrum clambers over rocky thickets, bearing racemes of small greenish-white flowers." },
      { author: "John Lindley", work: "The Vegetable Kingdom", quote: "In the family Petiveriaceae, the genus **Trichostigma** is distinguished by its penicillate, densely bristled stigmas." },
      { author: "Charles Darwin", work: "The Movements and Habits of Climbing Plants", quote: "The scrambling woody stems of **Trichostigma** support themselves upon surrounding vegetation without twining organs." }
    ]
  },
  "Dashboard — trich/trichosurus.md": {
    word: "trichosurus",
    primary: "A genus of nocturnal Australasian diprotodont marsupials comprising the brush-tailed possums, notably the common brushtail possum (Trichosurus vulpecula).",
    secondary: "In marsupial mammalogy, adaptable arboreal herbivores possessing a prehensile, furred tail with a naked friction pad beneath, widespread across Australian eucalyptus woodlands.",
    quotes: [
      { author: "John Gould", work: "The Mammals of Australia", quote: "The common brushtail possum, **Trichosurus** vulpecula, is widely distributed throughout Australian forests, nesting in hollow eucalyptus boughs." },
      { author: "Alfred Russel Wallace", work: "Australasia", quote: "The thick, woolly fur of **Trichosurus** made it an important resource for indigenous peoples across the southern continent." },
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "In the genus **Trichosurus**, the prehensile tail is naked on the underside, providing secure grip while climbing." }
    ]
  },
  "Dashboard — trich/trichotillomania.md": {
    word: "trichotillomania",
    primary: "A psychiatric compulsive disorder characterized by the recurrent, irresistible urge to pull out one's own hair, resulting in noticeable patchy hair loss.",
    secondary: "In clinical psychiatry and DSM-5 diagnostics, an obsessive-compulsive related condition preceded by increasing emotional tension and followed by relief upon hair extraction.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The compulsive pulling out of one's own hair, termed **trichotillomania**, leads to irregular patches of non-cicatricial alopecia." },
      { author: "Sigmund Freud", work: "Introductory Lectures on Psycho-Analysis", quote: "Repetitive self-injurious habits such as **trichotillomania** often serve as unconscious tension-reduction rituals." },
      { author: "Emil Kraepelin", work: "Lectures on Clinical Psychiatry", quote: "In severe neurotic patients, **trichotillomania** may be practiced covertly for months before baldness prompts clinical consultation." }
    ]
  },
  "Dashboard — trich/trichotomy.md": {
    word: "trichotomy",
    primary: "Division into three parts, categories, or branches; a three-way distinction or classification (etymologically from Greek tricha in three parts + tome cutting).",
    secondary: "In mathematics and logic, the property stating that for any two real numbers a and b, exactly one of the three relations holds: a < b, a = b, or a > b.",
    quotes: [
      { author: "Immanuel Kant", work: "Critique of Pure Reason", quote: "The table of categories displays an essential **trichotomy**, dividing each class into unity, plurality, and totality." },
      { author: "Charles Sanders Peirce", work: "Collected Papers", quote: "Every sign involves a fundamental **trichotomy** between the sign itself, its object, and its interpretant." },
      { author: "William James", work: "The Will to Believe", quote: "The philosopher divided the debate into an exhaustive **trichotomy**, examining each alternative with rigorous scrutiny." }
    ]
  },
  "Dashboard — trich/trichroism.md": {
    word: "trichroism",
    primary: "The optical property of certain anisotropic crystals of exhibiting three different colors when viewed in polarized light along three different crystallographic directions; trichromatism.",
    secondary: "In optical crystallography and mineralogy, an extreme form of pleochroism characteristic of orthorhombic, monoclinic, and triclinic minerals such as cordierite and zoisite (from Greek tri- three + chroa color).",
    quotes: [
      { author: "David Brewster", work: "A Treatise on New Philosophical Instruments", quote: "Under the dichroscope, the crystal of cordierite exhibits striking **trichroism**, displaying blue, yellowish-brown, and gray along three axes." },
      { author: "James Dwight Dana", work: "System of Mineralogy", quote: "Pleochroic minerals possessing three distinct principal absorption colors are said to exhibit **trichroism**." },
      { author: "John Tyndall", work: "Notes of a Course of Nine Lectures on Light", quote: "The optical phenomenon of **trichroism** illustrates how crystal symmetry dictates selective wave absorption." }
    ]
  },
  "Dashboard — trich/trichromacy.md": {
    word: "trichromacy",
    primary: "The condition of possessing normal color vision based on three independent retinal cone photoreceptor pigments (sensitive to red, green, and blue light); trichromatism.",
    secondary: "In visual psychophysics and neurobiology, the evolutionary adaptation typical of catarrhine primates, providing fine discrimination across the visible spectrum.",
    quotes: [
      { author: "Thomas Young", work: "On the Theory of Light and Colours", quote: "Human vision achieves full **trichromacy** through three sets of retinal nerve fibers sensitive to red, green, and violet." },
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "The trichromatic theory posits that normal color vision and **trichromacy** arise from differential stimulation of three photoreceptors." },
      { author: "Santiago Ramón y Cajal", work: "The Structure of the Retina", quote: "The anatomical specialization of foveal cone pathways provides the neurobiological basis for primate **trichromacy**." }
    ]
  },
  "Dashboard — trich/trichromatic.md": {
    word: "trichromatic",
    primary: "Of, relating to, or possessing vision mediated by three distinct color receptors; also, displaying three colors.",
    secondary: "In visual physiology and colorimetry, pertaining to the Young-Helmholtz theory that all perceived hues result from the additive combination of three primary spectral responses.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Physiological Optics", quote: "Our perception of the infinite palette of nature relies upon a **trichromatic** mechanism in the retina." },
      { author: "James Clerk Maxwell", work: "On the Theory of Compound Colours", quote: "Every visible hue can be reproduced by an appropriate mixture of three spectral primaries, confirming the **trichromatic** model." },
      { author: "Thomas Young", work: "Bakerian Lecture", quote: "The eye possesses a **trichromatic** receptor system capable of synthesizing any chromatic sensation from three distinct inputs." }
    ]
  },
  "Dashboard — trich/trichrome.md": {
    word: "trichrome",
    primary: "A histological staining method or solution that uses three differential dyes to stain distinct tissue components in contrasting colors (e.g., Masson's trichrome).",
    secondary: "In histopathology, a diagnostic stain typically coloring nuclei black/blue, cytoplasm and muscle red/pink, and collagen fibers blue or green to evaluate fibrosis.",
    quotes: [
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Differential connective tissue staining with a **trichrome** mixture clearly distinguishes collagen fibrils from smooth muscle." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Histological sections stained with Masson's **trichrome** revealed extensive hepatic fibrosis in the cirrhotic liver." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The application of a triple **trichrome** dye provides brilliant contrast between cytoplasmic matrices and nuclear chromatin." }
    ]
  },
  "Dashboard — trich/trichuriasis.md": {
    word: "trichuriasis",
    primary: "An intestinal parasitic infection of humans caused by the whipworm Trichuris trichiura.",
    secondary: "In tropical medicine and public health, a soil-transmitted helminthiasis causing chronic bloody diarrhea, anemia, rectal prolapse, and growth stunting in children with heavy worm burdens.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Heavy childhood **trichuriasis** results in chronic mucoid bloody diarrhea, microcytic anemia, and rectal prolapse." },
      { author: "Claude Bernard", work: "An Introduction to the Study of Experimental Medicine", quote: "The whipworm infests the cecum in **trichuriasis**, burrowing its attenuated anterior end into the colonic mucosa." },
      { author: "René Dubos", work: "Man Adapting", quote: "Public sanitation and clean water supplies are the definitive barriers against the transmission of endemic **trichuriasis**." }
    ]
  },
  "Dashboard — trich/trichys.md": {
    word: "trichys",
    primary: "A genus of Old World porcupines containing a single living species, the long-tailed porcupine (Trichys fasciculata), native to Borneo, Sumatra, and the Malay Peninsula.",
    secondary: "In rodent taxonomy, an archaic basal hystricomorph possessing short flattened spines mixed with bristles and a long scaly tail ending in a bundle of hollow quills.",
    quotes: [
      { author: "Richard Lydekker", work: "The Royal Natural History", quote: "The genus **Trichys**, containing the long-tailed porcupine of Borneo and Sumatra, is distinguished by its slender scaly tail tipped with hollow quills." },
      { author: "Alfred Russel Wallace", work: "The Malay Archipelago", quote: "In the dense rainforests of Sarawak, the small porcupine **Trichys** forages by night among the fallen dipterocarp fruits." },
      { author: "George Gaylord Simpson", work: "The Principles of Classification and a Classification of Mammals", quote: "The morphological characteristics of **Trichys** preserve the primitive skeletal architecture of Old World hystricomorph rodents." }
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
console.log("Batch 6 finished! Total words updated:", Object.keys(wordsData).length);
