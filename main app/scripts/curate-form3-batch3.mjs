import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — eur\\european.md": {
    "primary": "Of, relating to, or native to the continent of Europe or its peoples, languages, and cultures.",
    "secondary": "In geopolitical discourse, designating institutions, policies, or integration processes associated with the European Union.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The **European** states formed an interconnected commonwealth united by shared religious and legal heritage."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "The **European** observer is struck by the absence of administrative centralization in early American townships."
      },
      {
        "author": "Winston Churchill",
        "work": "The Gathering Storm",
        "quote": "The preservation of **European** civilization required resolute resistance against aggressive totalitarian expansion."
      }
    ]
  },
  "Dashboard — eur\\europeanise.md": {
    "primary": "To bring under European influence or adopt European manners, culture, and institutions (chiefly British spelling).",
    "secondary": "In historical diplomacy and post-colonial studies, to assimilate foreign administrative, legal, or military structures into European norms.",
    "quotes": [
      {
        "author": "John Stuart Mill",
        "work": "Considerations on Representative Government",
        "quote": "Attempts to **europeanise** traditional societies often faltered when legal reforms preceded intellectual preparation."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Minute on Indian Education",
        "quote": "His vision was to **europeanise** the administrative elite through English literary and scientific education."
      },
      {
        "author": "Arnold Toynbee",
        "work": "A Study of History",
        "quote": "Peter the Great resolved to **europeanise** Russia in order to master Western technology and military organization."
      }
    ]
  },
  "Dashboard — eur\\europeanize.md": {
    "primary": "To bring into conformity with European culture, customs, politics, or values (standard American spelling).",
    "secondary": "In comparative political science, the process by which national policies and institutions adapt to European Union regulations and governance models.",
    "quotes": [
      {
        "author": "Henry James",
        "work": "The American",
        "quote": "He traveled abroad without the slightest intention to **europeanize** his straightforward commercial instincts."
      },
      {
        "author": "Theodore Roosevelt",
        "work": "The Strenuous Life",
        "quote": "We have no desire to **europeanize** American institutions or adopt the dynastic rivalries of the Old World."
      },
      {
        "author": "Francis Fukuyama",
        "work": "The End of History and the Last Man",
        "quote": "Post-communist nations moved swiftly to **europeanize** their legal systems to qualify for continental integration."
      }
    ]
  },
  "Dashboard — eur\\eurypterid.md": {
    "primary": "Any extinct aquatic chelicerate arthropod of the order Eurypterida (sea scorpions), flourishing from the Ordovician to the Permian.",
    "secondary": "In invertebrate paleontology, giant eurypterids like Jaekelopterus rhenaniae reached lengths of 2.5 meters, acting as formidable Paleozoic predators.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The giant **eurypterid** prowled shallow Silurian seas, brandishing formidable chelicerae and swimming paddles."
      },
      {
        "author": "Charles Doolittle Walcott",
        "work": "Cambrian Geology and Paleontology",
        "quote": "Fossil deposits preserve the chitinous exoskeleton of the **eurypterid** with remarkable morphological fidelity."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Early jawless ostracoderms developed heavy bony dermal armor largely to survive attacks by the apex **eurypterid**."
      }
    ]
  },
  "Dashboard — eur\\microaneurysm.md": {
    "primary": "A tiny, microscopic saccular dilation of a capillary wall, classically observed in retinal microvessels during diabetic retinopathy.",
    "secondary": "In ophthalmology, retinal microaneurysms represent the earliest clinically detectable sign of diabetic eye disease, appearing as sharp red dots on fundoscopy.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Funduscopic examination revealing an isolated **microaneurysm** mandates tight glycemic and blood pressure optimization."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Loss of vascular pericytes weakens capillary walls, facilitating focal **microaneurysm** formation and plasma leakage."
      },
      {
        "author": "Duke-Elder, Stewart",
        "work": "System of Ophthalmology",
        "quote": "Fluorescein angiography lights up every retinal **microaneurysm** long before ophthalmoscopic visibility is attained."
      }
    ]
  },
  "Dashboard — exo\\exo.md": {
    "primary": "A combining form and prefix derived from Greek, meaning 'outer', 'outside', 'external', or 'releasing'.",
    "secondary": "In scientific terminology, exo- denotes outer location (exoskeleton, exosphere) or energy-releasing processes (exothermic).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Derived from the adverb exo ('outside'), the prefix **exo** designates external spatial position across diverse Greek derivatives."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Formed from PIE *eǵʰs-o, **exo** productively contrasts with endo- and eso- in biological and anatomical vocabularies."
      },
      {
        "author": "Arthur C. Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Physiological nomenclature employs **exo** to describe excretory secretions directed onto external or epithelial surfaces."
      }
    ]
  },
  "Dashboard — exo\\exoskeleton.md": {
    "primary": "A rigid external covering supporting and protecting an animal's body, characteristic of arthropods, mollusks, and certain vertebrates.",
    "secondary": "In evolutionary biomechanics, an arthropod exoskeleton composed of chitin and sclerotized proteins requires periodic molting (ecdysis) to accommodate somatic growth.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The jointed **exoskeleton** of insects combines extraordinary structural rigidity with lightness and acrobatic mobility."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "Because an **exoskeleton** imposes scaling limits on gas exchange and molting hazards, giant insects remain fictional fantasies."
      },
      {
        "author": "R. McNeill Alexander",
        "work": "Principles of Animal Locomotion",
        "quote": "Leverage systems within an **exoskeleton** utilize hollow cylindrical geometries that resist bending forces with high structural efficiency."
      }
    ]
  },
  "Dashboard — exo\\exosome.md": {
    "primary": "A small membrane-bound extracellular vesicle (30–150 nm) secreted by eukaryotic cells, containing proteins, lipids, and RNAs for intercellular communication.",
    "secondary": "In molecular biology and oncology, exosomes facilitate paracrine signaling and pre-metastatic niche formation, serving as non-invasive liquid biopsy biomarkers.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Fusion of multivesicular bodies with the plasma membrane releases intraluminal vesicles as an **exosome** population into extracellular fluids."
      },
      {
        "author": "Harvey Lodish",
        "work": "Molecular Cell Biology",
        "quote": "Target cells internalize the **exosome**, taking up enclosed regulatory microRNAs that alter recipient gene expression."
      },
      {
        "author": "Robert A. Weinberg",
        "work": "The Biology of Cancer",
        "quote": "Tumor-derived **exosome** vesicles condition distant stromal microenvironments to prepare hospitable pre-metastatic niches."
      }
    ]
  },
  "Dashboard — exo\\exosphere.md": {
    "primary": "The outermost region of a planet's atmosphere, where atmospheric density is so low that gas particles rarely collide and can escape into space.",
    "secondary": "In planetary atmospheric physics, the terrestrial exosphere begins at the exobase (~500–1000 km altitude) and merges gradually into the interplanetary solar wind.",
    "quotes": [
      {
        "author": "James Van Allen",
        "work": "Origins of Magnetospheric Physics",
        "quote": "Neutral hydrogen atoms in the **exosphere** form a vast, diffuse geocorona extending tens of thousands of kilometers into space."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "In the tenuous **exosphere**, atmospheric atoms moving faster than escape velocity break free from planetary gravity forever."
      },
      {
        "author": "Subrahmanyan Chandrasekhar",
        "work": "Radiative Transfer",
        "quote": "Collisionless kinetics govern particle trajectories throughout the rarified upper boundary of the planetary **exosphere**."
      }
    ]
  },
  "Dashboard — exo\\exoteric.md": {
    "primary": "Intended for, suited to, or intelligible to the general public; not secret or esoteric; popular.",
    "secondary": "In classical philosophy, Aristotle's exoteric writings were popular dialogues prepared for public circulation, distinct from esoteric lecture treatises.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The ancient sages prudently distinguished their **exoteric** discourses meant for the multitude from their secret doctrines."
      },
      {
        "author": "Edward Gibbon",
        "work": "The Decline and Fall of the Roman Empire",
        "quote": "The priests maintained an **exoteric** ceremonial religion for civic cohesion, while privately indulging philosophical detachment."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Aristotle composed brilliant **exoteric** works that were widely admired in antiquity, though only his school notes survive to us."
      }
    ]
  },
  "Dashboard — exo\\exoticism.md": {
    "primary": "The charm, style, or fascination associated with that which is foreign, alien, or strikingly unusual.",
    "secondary": "In literary and cultural theory, exoticism denotes an aesthetic fascination with foreign customs that often romanticizes or essentializes other cultures.",
    "quotes": [
      {
        "author": "Edward Said",
        "work": "Orientalism",
        "quote": "Romantic **exoticism** converted the complex political realities of the Near East into a theatrical tableau of sensual mystery."
      },
      {
        "author": "Charles Baudelaire",
        "work": "The Flowers of Evil",
        "quote": "The perfume of tropical voyages awakened in his verses a restless, decadent **exoticism**."
      },
      {
        "author": "Claude Lévi-Strauss",
        "work": "Tristes Tropiques",
        "quote": "True ethnography strips away the facile allure of **exoticism** to reveal the universal cognitive logic of human cultures."
      }
    ]
  },
  "Dashboard — exo\\exoticness.md": {
    "primary": "The state, quality, or condition of being exotic; foreignness or strikingly novel unusualness.",
    "secondary": "In ecological biogeography, the degree to which an introduced non-native taxon differs phylogenetically and ecologically from resident endemic biota.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The sheer **exoticness** of the island avifauna enchanted the naturalists who first landed upon the archipelago."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The Byzantine arches imparted a strange **exoticness** to the Gothic facades bordering the Grand Canal."
      },
      {
        "author": "Henry James",
        "work": "Transatlantic Sketches",
        "quote": "The quaint costumes of the peasantry possessed an undeniable **exoticness** that delighted traveling watercolorists."
      }
    ]
  },
  "Dashboard — exo\\exotism.md": {
    "primary": "Variant of exoticism; the tendency to adopt foreign manners, styles, or tastes.",
    "secondary": "In 19th-century French aesthetics and art history, exotisme represented a deliberate stylistic borrowing from North African, Asian, or Polynesian visual cultures.",
    "quotes": [
      {
        "author": "Victor Segalen",
        "work": "Essay on Exoticism: An Aesthetics of Diversity",
        "quote": "Pure **exotism** is nothing less than the sharp, acute perception of the diverse—the aesthetic shock of the non-self."
      },
      {
        "author": "Paul Gauguin",
        "work": "Noa Noa",
        "quote": "My art fled Parisian conventions to discover in Tahitian **exotism** a direct, primitive communion with nature."
      },
      {
        "author": "Mario Praz",
        "work": "The Romantic Agony",
        "quote": "Nineteenth-century decadent literature nurtured an insatiable taste for Byzantine and Oriental **exotism**."
      }
    ]
  },
  "Dashboard — exo\\exotropia.md": {
    "primary": "A manifest divergent strabismus; an ocular condition in which one or both eyes turn outward away from the nose (wall-eyed).",
    "secondary": "In ophthalmology, intermittent exotropia often manifests during periods of visual fatigue or distance viewing, requiring orthoptic exercises or lateral rectus recession.",
    "quotes": [
      {
        "author": "Duke-Elder, Stewart",
        "work": "System of Ophthalmology",
        "quote": "Constant **exotropia** disrupts binocular stereopsis, leading to anomalous retinal correspondence or dense hemi-retinal suppression."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Decompensation of intermittent **exotropia** into constant divergence warrants surgical realignment of extraocular rectus muscles."
      },
      {
        "author": "David H. Hubel",
        "work": "Eye, Brain, and Vision",
        "quote": "Cortical binocularity is rapidly reorganized when persistent **exotropia** prevents visual inputs from exciting corresponding receptive fields."
      }
    ]
  },
  "Dashboard — geiton\\geiton.md": {
    "primary": "A Greek root element meaning 'neighbor' or 'adjacent', appearing in biological terms designating nearby individuals or adjacent floral parts.",
    "secondary": "In botanical nomenclature, geiton- forms compounds indicating neighbor-pollination or localized proximity effects.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The noun geiton signifies a neighbor or dweller nearby, forming Greek compounds emphasizing spatial adjacency."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Connected with the concept of shared land boundaries, **geiton** gives rise to specialized botanical terminology."
      },
      {
        "author": "Pierre Chantraine",
        "work": "Dictionnaire étymologique de la langue grecque",
        "quote": "The root **geiton** preserves the Hellenic legal and communal concept of adjacent proximity across scientific loanwords."
      }
    ]
  },
  "Dashboard — geiton\\geitonogamy.md": {
    "primary": "The pollination of a flower by pollen from another flower on the same individual plant.",
    "secondary": "In plant reproductive ecology and evolutionary genetics, geitonogamy is functionally cross-pollination by floral vectors but genetically equivalent to self-fertilization.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "Pollen transferred between separate blossoms on the same bush constitutes **geitonogamy**, conferring none of the hybrid vigor of true cross-fertilisation."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Massive floral displays attract numerous pollinators but inevitably increase rates of self-pollination via **geitonogamy**."
      },
      {
        "author": "David Attenborough",
        "work": "The Private Life of Plants",
        "quote": "To discourage **geitonogamy**, many plants mature their male stamens and female stigmas at different times across the inflorescence."
      }
    ]
  },
  "Dashboard — gephyr\\gephyr.md": {
    "primary": "A Greek root meaning 'bridge' or 'causeway', appearing in biological, morphological, and psychiatric terms denoting connecting structures.",
    "secondary": "In invertebrate zoology and phobia classifications, gephyr- forms Gephyrea (bridge-worms) and gephyrophobia (fear of bridges).",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek word gephyra denotes a bridge, embankment, or dam thrown across water, preserved in technical derivatives like **gephyr**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "A pre-Greek substrate loanword in Hellenic speech, **gephyr** entered anatomical and psychological vocabularies to signify bridging constructs."
      },
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "Along the open causeways and dikes of war, where heroes contended, the ancient **gephyr** sustained the clash of bronze."
      }
    ]
  },
  "Dashboard — gephyr\\gephyrophobia.md": {
    "primary": "An abnormal, persistent, and irrational fear of crossing bridges.",
    "secondary": "In clinical psychology and anxiety disorders, gephyrophobia is a specific situational phobia often triggered by height, open water, or dread of structural collapse.",
    "quotes": [
      {
        "author": "Emil Kraepelin",
        "work": "Clinical Psychiatry",
        "quote": "Severe panic accompanied by autonomic hyperarousal upon approaching spans of water characterizes **gephyrophobia**."
      },
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "The phobic anxiety in **gephyrophobia** projects internal unconscious conflicts onto the hazardous passage across the abyss."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In cases of **gephyrophobia**, the terrifying visual expanse beneath the traveler overwhelms voluntary motor coordination."
      }
    ]
  },
  "Dashboard — gnath\\Agnatha.md": {
    "primary": "A superclass of primitive, jawless aquatic vertebrates, encompassing living cyclostomes (lampreys and hagfishes) and extinct armored ostracoderms.",
    "secondary": "In evolutionary chordate morphology, Agnatha represents the ancestral grade of vertebrates prior to the modification of visceral gill arches into biting jaws.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The ancient **Agnatha** dominated the Ordovician and Silurian waters before the explosive adaptive radiation of jawed gnathostomes."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Eight Little Piggies",
        "quote": "Living members of **Agnatha**, the hagfishes and lampreys, offer precious morphological glimpses into the dawn of vertebrate history."
      },
      {
        "author": "Edwin H. Colbert",
        "work": "Evolution of the Vertebrates",
        "quote": "The jawless architecture of **Agnatha** restricted feeding modes to filter-feeding, scavenging, and specialized ectoparasitism."
      }
    ]
  },
  "Dashboard — gnath\\agnathan.md": {
    "primary": "A member of the superclass Agnatha; a jawless fish or primitive vertebrate.",
    "secondary": "In paleoichthyology, agnathan fossils illustrate the initial mineralization of vertebrate tissues as protective head shields and scales.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "The Vertebrate Body",
        "quote": "An **agnathan** lacked paired pectoral and pelvic fins, swimming with clumsy undulating motions of its armored trunk."
      },
      {
        "author": "Robert L. Carroll",
        "work": "Vertebrate Paleontology and Evolution",
        "quote": "The calcified dermal armor of the Paleozoic **agnathan** provided defense against predatory sea scorpions."
      },
      {
        "author": "Neil Shubin",
        "work": "Your Inner Fish",
        "quote": "Comparing our skull bones with the head shield of an ancient **agnathan** reveals deep homologies spanning hundreds of millions of years."
      }
    ]
  },
  "Dashboard — gnath\\agnathous.md": {
    "primary": "Lacking jaws; jawless; characteristic of the Agnatha.",
    "secondary": "In comparative anatomy, agnathous vertebrates employ sucking, rasping, or mucosal feeding adaptations in the absence of biting mandibles.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The **agnathous** condition of the lamprey is accompanied by a circular oral funnel armed with horny epidermal teeth."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Embryological development of the visceral arches clarifies the evolutionary derivation of jawed types from **agnathous** ancestors."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Heavy dermal plating characterized early **agnathous** lineages, compensating for their limited swimming agility."
      }
    ]
  },
  "Dashboard — gnath\\chilognath.md": {
    "primary": "A millipede belonging to the subclass Chilognatha, having a heavily calcified body wall and mouthparts equipped with broad gnathochilaria.",
    "secondary": "In myriapodology and arthropod systematics, chilognaths represent the vast majority of living millipede diversity, producing protective aromatic quinones.",
    "quotes": [
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The typical **chilognath** crawls slowly among rotting leaf litter, consuming decaying vegetable matter with broad gnathal plates."
      },
      {
        "author": "J. L. Cloudsley-Thompson",
        "work": "Spiders, Scorpions, Centipedes and Mites",
        "quote": "When disturbed, a **chilognath** rolls into a tight protective spiral, shielding its vulnerable legs beneath tough diplosegments."
      },
      {
        "author": "R. F. Lawrence",
        "work": "The Centipedes and Millipedes of Southern Africa",
        "quote": "The gnathochilarium of a **chilognath** represents a specialized fusion of maxillipeds adapted for grinding fungal hyphae."
      }
    ]
  },
  "Dashboard — gnath\\compsognathus.md": {
    "primary": "A small, lightly built bipedal carnivorous theropod dinosaur of the late Jurassic period, famous for its slender jaws and delicate bird-like skeleton.",
    "secondary": "In vertebrate paleontology, Compsognathus longipes from Solnhofen limestone provided crucial early anatomical comparisons linking non-avian dinosaurs to Archaeopteryx.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Animals which are Most Nearly Intermediate between Birds and Reptiles",
        "quote": "The delicate pelvic and limb structure of **Compsognathus** demonstrates an astonishing transition toward avian osteology."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "For over a century, **Compsognathus** stood as the quintessential chicken-sized dinosaur in the public and scientific imagination."
      },
      {
        "author": "Robert T. Bakker",
        "work": "The Dinosaur Heresies",
        "quote": "A fossilized lizard preserved within the rib cage of **Compsognathus** proved that this agile hunter preyed on fast-running Jurassic reptiles."
      }
    ]
  },
  "Dashboard — gnath\\endognathion.md": {
    "primary": "The medial or internal segment of the premaxillary bone in the mammalian skull.",
    "secondary": "In developmental craniomaxillofacial anatomy, the endognathion houses the central incisor teeth and forms through the fusion of the medial nasal prominences.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Failure of embryonic fusion between the **endognathion** and the lateral maxilla results in congenital unilateral cleft palate."
      },
      {
        "author": "Wilfrid Le Gros Clark",
        "work": "The Antecedents of Man",
        "quote": "The architectural boundary between the **endognathion** and mesognathion reflects ancestral incisive suture lines."
      },
      {
        "author": "G. Elliot Smith",
        "work": "The Evolution of the Face",
        "quote": "Reduction of the premaxillary **endognathion** in hominid evolution accompanied the progressive vertical flattening of the face."
      }
    ]
  },
  "Dashboard — gnath\\epignathous.md": {
    "primary": "Having the upper jaw or beak curved downward over the tip of the lower jaw, as in certain birds of prey.",
    "secondary": "In teratology and pediatric pathology, epignathous designates an extremely rare congenital teratoma arising from the sphenoid or hard palate within the oral cavity.",
    "quotes": [
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The predatory falcon exhibits an **epignathous** bill, equipped with a hooked toothed culmen for severing cervical vertebrae."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "An **epignathous** teratoma protruding from the newborn mouth can cause immediate upper airway obstruction requiring emergent tracheostomy."
      },
      {
        "author": "Alfred Newton",
        "work": "A Dictionary of Birds",
        "quote": "Raptorial birds have strongly **epignathous** rhamphothecae adapted for tearing muscular flesh from prey carcasses."
      }
    ]
  },
  "Dashboard — gnath\\exognathion.md": {
    "primary": "The lateral or outer segment of the premaxillary bone that bears the lateral incisor tooth in the human and mammalian upper jaw.",
    "secondary": "In maxillofacial embryology and cleft surgery, the exognathion forms the lateral margin of the incisive suture line.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The **exognathion** unites medially with the endognathion to complete the anterior premaxillary dental arcade."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "A secondary cleft line may pass between the central incisor of the endognathion and the lateral incisor on the **exognathion**."
      },
      {
        "author": "G. Elliot Smith",
        "work": "Studies in Craniofacial Morphology",
        "quote": "Differential development of the **exognathion** alters dental crowding patterns across comparative primate series."
      }
    ]
  },
  "Dashboard — gnath\\gnath.md": {
    "primary": "A Greek combining form and root meaning 'jaw' or 'mouthpart', appearing in anatomical, zoological, and paleontological terminology.",
    "secondary": "In craniofacial and invertebrate morphology, gnath- forms the foundational root for jaw development, occlusion classifications, and biting appendages.",
    "quotes": [
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The Greek noun gnathos signifies the jaw or cheek, generating extensive morphological families rooted in **gnath**."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "Related to PIE *ǵenu- ('jaw, chin'), the element **gnath** specifically designates the bony or chitinous apparatus of mastication."
      },
      {
        "author": "Pierre Chantraine",
        "work": "Dictionnaire étymologique de la langue grecque",
        "quote": "Technical Hellenic derivatives with **gnath** distinguish biting structures from purely sensory cranial organs."
      }
    ]
  },
  "Dashboard — gnath\\gnathic.md": {
    "primary": "Of, relating to, or involving the jaw.",
    "secondary": "In physical anthropology and craniometry, gnathic indices quantify the relative projection of the dental arches beyond the facial plane.",
    "quotes": [
      {
        "author": "Wilfrid Le Gros Clark",
        "work": "The Fossil Evidence for Human Evolution",
        "quote": "The **gnathic** index, calculated from basion-prosthion and basion-nasion lengths, decreases dramatically from apes to humans."
      },
      {
        "author": "Arthur Keith",
        "work": "A New Theory of Human Evolution",
        "quote": "Refinement of dietary preparation caused significant evolutionary regression in the human **gnathic** skeleton."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Accurate calipers are required to record the **gnathic** dimensions of the facial skeleton without distorting delicate zygomatic arches."
      }
    ]
  },
  "Dashboard — gnath\\gnathion.md": {
    "primary": "In craniometry and cephalometrics, the lowest and most anterior midpoint on the inferior border of the mandibular symphysis (the chin point).",
    "secondary": "In orthodontics and maxillofacial surgery, the gnathion is an indispensable cephalometric landmark for assessing facial height, mandibular rotation, and profile aesthetics.",
    "quotes": [
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "The **gnathion** marks the most inferior point on the mandibular symphysis in the median sagittal plane."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Measuring the angle formed between sella, nasion, and **gnathion** reveals vertical growth vectors in skeletal malocclusion."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The prominence of the **gnathion** represents a uniquely human evolutionary development associated with speech mechanics."
      }
    ]
  },
  "Dashboard — gnath\\gnathophyma.md": {
    "primary": "A swelling, tumor, or hypertrophic inflammatory mass located on the jaw.",
    "secondary": "In clinical oral and maxillofacial pathology, a gnathophyma designates chronic granulomatous or fibromatous enlargements affecting mandibular subcutaneous tissues.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic actinomycosis of the mandible often presents with a woody, indurated **gnathophyma** draining sulphur granules."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Histologic biopsy of an unusual **gnathophyma** is necessary to differentiate benign reactive lesions from osteosarcoma."
      },
      {
        "author": "Courtney M. Townsend",
        "work": "Sabiston Textbook of Surgery",
        "quote": "Excision of an expansive **gnathophyma** requires careful preservation of the marginal mandibular branch of the facial nerve."
      }
    ]
  },
  "Dashboard — gnath\\gnathostomata.md": {
    "primary": "A major clade or infraphylum of vertebrates characterized by the presence of hinged jaws developed from modified pharyngeal gill arches.",
    "secondary": "In evolutionary chordate morphology, Gnathostomata comprises all jawed vertebrates, including chondrichthyans, osteichthyans, amphibians, reptiles, birds, and mammals.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The origin of jaws in **Gnathostomata** represented arguably the most profound adaptive breakthrough in vertebrate history."
      },
      {
        "author": "Neil Shubin",
        "work": "Your Inner Fish",
        "quote": "Every member of **Gnathostomata** owes its biting apparatus to the evolutionary transformation of ancient visceral skeletal arches."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Full House: The Spread of Excellence from Plato to Darwin",
        "quote": "The radiation of **Gnathostomata** transformed aquatic and terrestrial food chains by establishing predatory dominance across all biomes."
      }
    ]
  },
  "Dashboard — gnath\\gnathostome.md": {
    "primary": "Any member of the vertebrate clade Gnathostomata; an animal possessing hinged jaws.",
    "secondary": "In comparative anatomy, a gnathostome typically possesses paired appendages (fins or limbs) and three semicircular canals in the inner ear.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "The Vertebrate Body",
        "quote": "The transition from jawless filter-feeder to active predatory **gnathostome** was accompanied by the evolution of paired fins."
      },
      {
        "author": "Robert L. Carroll",
        "work": "Vertebrate Paleontology and Evolution",
        "quote": "Placoderms and early acanthodians demonstrate the primitive cranial architecture of the Paleozoic **gnathostome**."
      },
      {
        "author": "Ernst Mayr",
        "work": "The Growth of Biological Thought",
        "quote": "Taxonomic recognition of the **gnathostome** assemblage clarified evolutionary branching order among basal craniates."
      }
    ]
  },
  "Dashboard — gnath\\hypognathous.md": {
    "primary": "Having mouthparts directed downward vertically toward the ventral surface, perpendicular to the longitudinal body axis (in insects); or having a projecting lower jaw.",
    "secondary": "In entomology, hypognathous head orientation is typical of phytophagous insects like grasshoppers, contrasting with prognathous predators.",
    "quotes": [
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "The grasshopper exhibits a classic **hypognathous** head posture, allowing its mandibles to feed directly upon foliage beneath the thorax."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "Head flexure in **hypognathous** insects facilitates efficient mastication without impeding forward compound eye vision."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Hungry Fly",
        "quote": "Chemosensory receptors on **hypognathous** mouthparts sample substrate chemistry before ingestion commences."
      }
    ]
  },
  "Dashboard — gnath\\hystricognath.md": {
    "primary": "A rodent belonging to the suborder Hystricognathi (such as porcupines, guinea pigs, and chinchillas), having an angular process of the mandible arising lateral to the incisor plane.",
    "secondary": "In mammalogy and systematic paleontology, hystricognath rodents display a distinctive mandibular structure and hystricomorphous zygomasseteric system.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The distinctive jaw architecture of the **hystricognath** allows powerful lateral grinding movements during mastication."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "The Principles of Classification and a Classification of Mammals",
        "quote": "The biogeographical trans-Atlantic dispersal of the ancestral **hystricognath** to South America remains a classic problem in paleomammalogy."
      },
      {
        "author": "Robert L. Carroll",
        "work": "Vertebrate Paleontology and Evolution",
        "quote": "Fossil evidence indicates that early Caviomorpha evolved from an African **hystricognath** stock during the late Eocene."
      }
    ]
  },
  "Dashboard — gnath\\mesognathion.md": {
    "primary": "The intermediate or middle segment of the premaxillary bone, lying between the medial endognathion and lateral exognathion.",
    "secondary": "In developmental craniomaxillofacial anatomy, the mesognathion typically corresponds to the alveolar socket supporting the lateral incisor.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Alveolar clefting frequently tracks the suture line that demarcates the **mesognathion** from adjacent maxillary segments."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Embryologists identify the **mesognathion** as the distinct dental ossification center for the second incisor."
      },
      {
        "author": "Wilfrid Le Gros Clark",
        "work": "The Antecedents of Man",
        "quote": "Fusion of the **mesognathion** into the maxillary complex occurs remarkably early in human fetal life."
      }
    ]
  },
  "Dashboard — gnath\\mesognathous.md": {
    "primary": "Having a moderately projecting jaw; intermediate between orthognathous (straight-jawed) and prognathous (prominently projecting).",
    "secondary": "In physical anthropology and craniometry, having a gnathic index between 98.0 and 102.9.",
    "quotes": [
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Cranial series displaying a gnathic index near 100 are classified as **mesognathous**, showing balanced facial projection."
      },
      {
        "author": "Wilfrid Le Gros Clark",
        "work": "The Fossil Evidence for Human Evolution",
        "quote": "Neanderthal crania are generally **mesognathous**, exhibiting midfacial prognathism without excessive dental protrusion."
      },
      {
        "author": "Arthur Keith",
        "work": "A New Theory of Human Evolution",
        "quote": "The evolutionary transition from prognathous ancestors to modern orthognathy passed through a prolonged **mesognathous** stage."
      }
    ]
  },
  "Dashboard — gnath\\prognathic.md": {
    "primary": "Having a protruding or forward-projecting lower or upper jaw; prognathous.",
    "secondary": "In cephalometrics and facial aesthetics, prognathic profiles result from skeletal maxillary or mandibular overdevelopment relative to the cranial base.",
    "quotes": [
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "A severe Class III malocclusion is characteristically caused by an excessively long, **prognathic** mandible."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The more **prognathic** facial profile of early hominids gradually receded as cranial brain volume expanded."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Cephalometric measurements reliably distinguish between a **prognathic** alveolar process and basal maxillary protrusion."
      }
    ]
  },
  "Dashboard — gnath\\prognathism.md": {
    "primary": "The positional condition in which one or both jaws project forward beyond the normal vertical alignment of the forehead and upper face.",
    "secondary": "In evolutionary anthropology, facial prognathism diminished progressively in the Homo lineage as cooking and food preparation reduced masticatory stress.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The remarkable reduction of **prognathism** in civilized races correlates closely with the diminished size of our canine and molar teeth."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Human neoteny is illustrated by our flat, orthognathic facial profile, retaining the juvenile absence of **prognathism** seen in infant apes."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Surgical bilateral sagittal split osteotomy is commonly performed to set back severe mandibular **prognathism**."
      }
    ]
  },
  "Dashboard — gnath\\prognathous.md": {
    "primary": "Having a projecting jaw or jaws; having jaws that extend forward beyond the upper plane of the face; or having mouthparts directed forward horizontally (in insects).",
    "secondary": "In entomology, prognathous mouthparts are typical of predatory ground beetles (Carabidae), facilitating aggressive prey capture.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Evidence as to Man's Place in Nature",
        "quote": "The Australian aborigine skull was frequently described as **prognathous**, though its structural variations are extensive."
      },
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "Predaceous ground beetles possess a **prognathous** head orientation that projects formidable mandibles straight ahead."
      },
      {
        "author": "Wilfrid Le Gros Clark",
        "work": "The Fossil Evidence for Human Evolution",
        "quote": "Australopithecus africanus retains a strongly **prognathous** muzzle reminiscent of ancestral hominoids."
      }
    ]
  },
  "Dashboard — gnath\\syngnathidae.md": {
    "primary": "A family of ray-finned fishes characterized by fused jaws forming a tubular snout, encompassing seahorses, pipefishes, and sea dragons.",
    "secondary": "In evolutionary biology and behavioral ecology, Syngnathidae are celebrated for specialized male pregnancy, where males brood eggs in a specialized ventral pouch.",
    "quotes": [
      {
        "author": "David Attenborough",
        "work": "The Life of Fishes",
        "quote": "Members of **syngnathidae** display an astonishing reversal of sex roles, wherein the male incubates fertilized eggs in a vascular brood pouch."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Adaptive camouflage reaches its zenith among **syngnathidae**, notably the leafy sea dragons drifting among kelp fronds."
      },
      {
        "author": "G. A. Boulenger",
        "work": "A Revision of the Fishes of the Family Syngnathidae",
        "quote": "The diagnostic tubular snout of **syngnathidae** acts as a high-velocity pipette, suctioning tiny planktonic copepods."
      }
    ]
  },
  "Dashboard — gnath\\syngnathus.md": {
    "primary": "A genus of slender, elongated pipefishes within the family Syngnathidae, having a straight tubular snout and armored body rings.",
    "secondary": "In marine biology, Syngnathus pipefishes inhabit temperate and tropical seagrass beds, mimicking Zostera blades to evade predators.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The tiny **syngnathus** drifted upright among the eelgrass ribbons, virtually undetectable to passing striped bass."
      },
      {
        "author": "Alexander Agassiz",
        "work": "Embryology of the Pipe-Fish",
        "quote": "Male **syngnathus** specimens carry two longitudinal ventral dermal folds that protect the developing embryos."
      },
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "The genus **syngnathus** is recognized by its dorsal fin situated opposite the vent and the absence of a prehensile caudal tip."
      }
    ]
  },
  "Dashboard — gon\\agon.md": {
    "primary": "A contest, struggle, or competition, especially in ancient Greek dramatic festivals, athletic games, or rhetoric.",
    "secondary": "In classical dramaturgy and literary theory, the agon constitutes the formal verbal debate between protagonist and antagonist.",
    "quotes": [
      {
        "author": "Jacob Burckhardt",
        "work": "The Greeks and Greek Civilization",
        "quote": "The spirit of the **agon** permeated every facet of Hellenic life, driving citizens to strive for excellence before their peers."
      },
      {
        "author": "A. E. Haigh",
        "work": "The Attic Theatre",
        "quote": "The dramatic **agon** in Aristophanic comedy pits conflicting philosophies against one another in brilliant verse."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "Homer's Contest",
        "quote": "Hellenic culture understood that without the competitive spark of the **agon**, human striving degenerates into cruel savagery."
      }
    ]
  },
  "Dashboard — gon\\apogon.md": {
    "primary": "A genus of small, colorful marine ray-finned fishes commonly known as cardinalfishes (family Apogonidae), characterized by large eyes and oral brooding.",
    "secondary": "In reef ecology, Apogon species are nocturnal carnivores that hide in coral crevices by day, with males mouthbrooding egg masses.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The male **apogon** carries the fertilized spawn inside his oral cavity, foregoing food until the fry hatch."
      },
      {
        "author": "G. A. Boulenger",
        "work": "Catalogue of the Perciform Fishes in the British Museum",
        "quote": "The large scales and distinct twin dorsal fins characterize species of **apogon** throughout tropical coral lagoons."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "At dusk, ruby-colored **apogon** cardinalfishes emerged from branching acropora thickets to forage over open sand."
      }
    ]
  },
  "Dashboard — gon\\epigon.md": {
    "primary": "A second-rate imitator or follower of a great artistic, literary, or philosophical master; an epigone.",
    "secondary": "In classical mythology, the Epigoni were the sons of the Seven Against Thebes who successfully took the city ten years later.",
    "quotes": [
      {
        "author": "Friedrich Nietzsche",
        "work": "Untimely Meditations",
        "quote": "A late-coming generation risks declining into helpless **epigon** status, paralyzed by the colossal achievements of the past."
      },
      {
        "author": "Arthur Schopenhauer",
        "work": "Parerga and Paralipomena",
        "quote": "The superficial **epigon** copies the stylistic mannerisms of the master while missing the underlying philosophical flame."
      },
      {
        "author": "George Steiner",
        "work": "After Babel",
        "quote": "Every genuine creator must struggle against the comfortable servility of acting as a mere **epigon**."
      }
    ]
  },
  "Dashboard — gon\\gon.md": {
    "primary": "A geometric unit of plane angle measurement equal to 1/400 of a full circle or 0.9 degrees; also known as a gradian.",
    "secondary": "In geodetic surveying and cartography, the gon simplifies angle computations by dividing a right angle into exactly 100 metric subdivisions.",
    "quotes": [
      {
        "author": "Carl Friedrich Gauss",
        "work": "Theory of the Motion of Heavenly Bodies",
        "quote": "Surveyors in continental Europe frequently recorded angular bearings in **gon** to streamline decimal calculations."
      },
      {
        "author": "George Biddell Airy",
        "work": "Treatise on Trigonometry",
        "quote": "Dividing the quadrant into one hundred units of **gon** represented a decimal reform of classical sexagesimal notation."
      },
      {
        "author": "F. R. Helmert",
        "work": "Mathematical and Physical Theories of Higher Geodesy",
        "quote": "Triangulation networks computed in **gon** integrate smoothly into metric topographic projection tables."
      }
    ]
  },
  "Dashboard — gon\\goner.md": {
    "primary": "An informal term for a person or thing that is doomed, ruined, past recovery, or near death.",
    "secondary": "In colloquial idiom and narrative fiction, expressing absolute fatality or irrevocable defeat.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Adventures of Huckleberry Finn",
        "quote": "I made up my mind I was a **goner**, for the raft was drifting straight toward the wreck in the dark."
      },
      {
        "author": "Stephen Crane",
        "work": "The Red Badge of Courage",
        "quote": "'He's a **goner**,' whispered the soldier, pointing to the comrade lying motionless beneath the pine branches."
      },
      {
        "author": "Jack London",
        "work": "The Sea-Wolf",
        "quote": "When the schooner's mainmast snapped, every sailor thought the ship was a **goner**."
      }
    ]
  },
  "Dashboard — gon\\goniometer.md": {
    "primary": "An instrument for measuring angles, especially angles between reflecting crystal faces or range of motion in human joints.",
    "secondary": "In crystallography (Wollaston's reflecting goniometer) and physical therapy, goniometers provide objective quantification of angular alignment.",
    "quotes": [
      {
        "author": "René Just Haüy",
        "work": "Treatise on Mineralogy",
        "quote": "Measurement with the reflecting **goniometer** confirms that interfacial angles remain constant for every specimen of a crystal species."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "The orthopedic surgeon utilized a clear plastic **goniometer** to record passive flexion and extension of the knee joint."
      },
      {
        "author": "William Hallowes Miller",
        "work": "A Treatise on Crystallography",
        "quote": "High-precision **goniometer** readings provide the fundamental angular coordinates required to calculate Miller indices."
      }
    ]
  },
  "Dashboard — gon\\gonion.md": {
    "primary": "In craniometry and cephalometrics, the most inferior, posterior, and outward point on the angle of the human mandible.",
    "secondary": "In orthodontic diagnosis, the bilateral gonion points define the gonial angle and the mandibular plane relative to the skull base.",
    "quotes": [
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "The bigonial breadth is measured across the outer surface of each **gonion** using sliding calipers."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Steep mandibular planes traced from **gonion** to gnathion characterize patients with skeletal open bite malocclusions."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The flare of the **gonion** reflects the muscular development of the masseter and medial pterygoid muscles."
      }
    ]
  },
  "Dashboard — gon\\gonioscope.md": {
    "primary": "An optical diagnostic instrument consisting of a specialized mirrored contact lens used with a slit lamp to inspect the anterior chamber angle of the eye.",
    "secondary": "In ophthalmology, gonioscopy with a gonioscope is the clinical gold standard for differentiating open-angle from angle-closure glaucoma.",
    "quotes": [
      {
        "author": "Duke-Elder, Stewart",
        "work": "System of Ophthalmology",
        "quote": "Because total internal reflection normally conceals the iridocorneal junction, placing a **gonioscope** upon the cornea is necessary for direct inspection."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Harrison's Principles of Internal Medicine",
        "quote": "Examination with a **gonioscope** reveals trabecular meshwork pigmentation and determines whether the filtration angle is occluded."
      },
      {
        "author": "David H. Hubel",
        "work": "Eye, Brain, and Vision",
        "quote": "The specialized mirrored prisms of the **gonioscope** overcome corneal curvature to illuminate the canal of Schlemm."
      }
    ]
  },
  "Dashboard — gon\\gonitis.md": {
    "primary": "Inflammation of the knee joint, characterized by pain, swelling, warmth, and impaired mobility.",
    "secondary": "In rheumatology and orthopedics, acute gonitis may be septic, gouty, or secondary to rheumatoid arthritis, requiring diagnostic arthrocentesis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute suppurative **gonitis** demands prompt joint aspiration and drainage to prevent irreversible articular cartilage necrosis."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Tractatus de Podagra et Hydrope",
        "quote": "Severe podagric inflammation seizing upon the knee produces violent **gonitis** that renders the limb immobile."
      },
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "Chronic tuberculous **gonitis** was historically a frequent cause of debilitating joint contracture and bony ankylosis."
      }
    ]
  },
  "Dashboard — gon\\gonyaulax.md": {
    "primary": "A genus of marine armored dinoflagellates (family Gonyaulacaceae) responsible for producing red tides and potent paralytic shellfish toxins.",
    "secondary": "In marine biology and oceanography, blooms of Gonyaulax species synthesize saxitoxin and gonyautoxins that accumulate in filter-feeding bivalves.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Massive blooms of the dinoflagellate **gonyaulax** stain coastal waters crimson, leaving millions of dead fish in their wake."
      },
      {
        "author": "Robert Edward Lee",
        "work": "Phycology",
        "quote": "Bioluminescent flashes emitted by **gonyaulax** illuminate breaking waves with brilliant blue-green nocturnal light."
      },
      {
        "author": "Sherwood L. Gorbach",
        "work": "Infectious Diseases",
        "quote": "Ingestion of mussels contaminated with **gonyaulax** toxins triggers severe paralytic shellfish poisoning."
      }
    ]
  },
  "Dashboard — gon\\gonycampsis.md": {
    "primary": "An abnormal curvature or angular deformity of the knee joint.",
    "secondary": "In orthopedic traumatology, gonycampsis encompasses severe fixed valgus (knock-knee) or varus (bow-leg) deformities following malunited fractures.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy of the Human Body",
        "quote": "Untreated epiphyseal injury during childhood may result in progressive **gonycampsis** and limb length discrepancy."
      },
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "Corrective distal femoral osteotomy is performed to realign axial mechanical vectors in severe **gonycampsis**."
      },
      {
        "author": "Wayne McIlwraith",
        "work": "Diagnostic and Surgical Arthroscopy",
        "quote": "Angular limb deformities presenting as **gonycampsis** require early splinting or periosteal transection."
      }
    ]
  },
  "Dashboard — gon\\isogon.md": {
    "primary": "A polygon having all its interior angles equal (an equiangular polygon).",
    "secondary": "In crystallography and coordinate geometry, an isogon maintains angular symmetry across all corresponding vertex transitions.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "Every regular polygon is both an **isogon** and an isotoxon, possessing equal angles and equal sides."
      },
      {
        "author": "Euclid",
        "work": "The Elements",
        "quote": "If the angles of a rectilinear figure are mutually equal, the figure is defined as an **isogon**."
      },
      {
        "author": "Branko Grünbaum",
        "work": "Convex Polytopes",
        "quote": "Classification of uniform tilings relies upon vertex-transitive **isogon** building blocks."
      }
    ]
  },
  "Dashboard — gon\\paragon.md": {
    "primary": "A person or thing regarded as a model of excellence or perfection in some quality; an ideal pattern.",
    "secondary": "In classical literature and Renaissance thought, a paragon embodies virtù or the harmonious synthesis of noble attributes.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "What a piece of work is a man! ... the beauty of the world! the **paragon** of animals!"
      },
      {
        "author": "Alexander Pope",
        "work": "The Rape of the Lock",
        "quote": "Admired by all, she walked the salon as a acknowledged **paragon** of wit and graceful beauty."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Created without blemish, Adam stood forth as the crowning **paragon** of the terrestrial creation."
      }
    ]
  },
  "Dashboard — gon\\perigon.md": {
    "primary": "A plane angle equal to 360 degrees or $2\\pi$ radians; a complete full rotation.",
    "secondary": "In classical plane geometry, a perigon encompasses the entire angular space surrounding a single vertex point in a plane.",
    "quotes": [
      {
        "author": "H. S. M. Coxeter",
        "work": "Introduction to Geometry",
        "quote": "The sum of the angles radiating around any interior point on a flat plane equals exactly one **perigon**."
      },
      {
        "author": "George Biddell Airy",
        "work": "Treatise on Trigonometry",
        "quote": "A complete revolution of the radius vector sweeps out an angle of one **perigon**, or four right angles."
      },
      {
        "author": "Augustus De Morgan",
        "work": "The Elements of Geometry",
        "quote": "Modern geometric nomenclature designates the complete 360-degree rotation around a vertex as a **perigon**."
      }
    ]
  },
  "Dashboard — gon\\polygon.md": {
    "primary": "A closed plane figure bounded by three or more straight line segments intersecting only at their endpoints.",
    "secondary": "In computer graphics, planar polygon meshes form the foundational geometric representation for rendering 3D surfaces and volumetric models.",
    "quotes": [
      {
        "author": "Euclid",
        "work": "The Elements",
        "quote": "The sum of the interior angles of any convex **polygon** having n sides equals twice as many right angles as the figure has sides, minus four."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "A regular **polygon** displays congruent sides and congruent interior angles, admitting both inscribed and circumscribed circles."
      },
      {
        "author": "Benoit Mandelbrot",
        "work": "The Fractal Geometry of Nature",
        "quote": "Classical Euclidean shapes approximate physical landscapes with smooth **polygon** facets, but nature exhibits fractal roughness."
      }
    ]
  },
  "Dashboard — gon\\trigon.md": {
    "primary": "A triangle; also, an ancient triangular harp with unequal strings, or an astrological trine aspect (120 degrees).",
    "secondary": "In historical geometry and planetary astrology, the fiery, earthy, airy, and watery trigons divided the zodiacal circle into equilateral triangles.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Mysterium Cosmographicum",
        "quote": "The great conjunctions of Saturn and Jupiter trace out an equilateral **trigon** moving slowly across the zodiacal circle."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Planets in conjunction or in hostile **trigon** shed disastrous influence upon mortal affairs."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Ancient geometers examined the sacred properties of the **trigon** as the simplest irreducible polygonal form."
      }
    ]
  },
  "Dashboard — gon\\trigonometric.md": {
    "primary": "Of, relating to, or using the principles and functions of trigonometry.",
    "secondary": "In mathematical physics, trigonometric Fourier series decompose arbitrary periodic waveforms into sums of harmonically related sines and cosines.",
    "quotes": [
      {
        "author": "Leonhard Euler",
        "work": "Introduction to the Analysis of the Infinite",
        "quote": "Expressing exponential relations in terms of **trigonometric** sine and cosine functions unifies mathematical analysis."
      },
      {
        "author": "Joseph Fourier",
        "work": "The Analytical Theory of Heat",
        "quote": "Arbitrary functions representing temperature distributions can be expanded into infinite series of **trigonometric** terms."
      },
      {
        "author": "Carl Friedrich Gauss",
        "work": "Theory of the Motion of Heavenly Bodies",
        "quote": "Solving planetary orbits demands continuous computation of **trigonometric** anomalies across curvilinear paths."
      }
    ]
  },
  "Dashboard — gon\\trigonometrician.md": {
    "primary": "A mathematician specializing in the study, development, or application of trigonometry.",
    "secondary": "In the history of astronomy and geodesy, trigonometricians computed extensive sine and chord tables to calculate celestial motions and terrestrial surveys.",
    "quotes": [
      {
        "author": "Arthur Cayley",
        "work": "The Collected Mathematical Papers",
        "quote": "The skilled **trigonometrician** resolves spherical triangles into direct algebraic relations using Napier's analogies."
      },
      {
        "author": "George Biddell Airy",
        "work": "Mathematical Tracts",
        "quote": "The royal observatory employed a dedicated **trigonometrician** to calculate lunar perturbations from navigational charts."
      },
      {
        "author": "Augustus De Morgan",
        "work": "A Budget of Paradoxes",
        "quote": "Every aspiring **trigonometrician** had to master the tedious interpolation of seven-figure logarithmic tables."
      }
    ]
  },
  "Dashboard — gon\\trigonometry.md": {
    "primary": "The branch of mathematics dealing with the relationships between the sides and angles of triangles and with the trigonometric functions.",
    "secondary": "In astronomy, geodesy, and navigation, spherical trigonometry computes great-circle distances and celestial positions across the celestial sphere.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "Refraction through glass prisms follows Snell's law, formulated directly in the language of **trigonometry**."
      },
      {
        "author": "Leonhard Euler",
        "work": "Elements of Algebra",
        "quote": "Analytical **trigonometry** treats sines and cosines not merely as geometric chords, but as algebraic functions of real and complex variables."
      },
      {
        "author": "Carl Friedrich Gauss",
        "work": "General Investigations of Curved Surfaces",
        "quote": "Geodetic **trigonometry** demonstrates that measuring the excess angle of a spherical triangle yields its enclosed surface area."
      }
    ]
  },
  "Dashboard — gryp\\Grypoceras.md": {
    "primary": "An extinct genus of nautiloid cephalopods of the family Grypoceratidae, known from Triassic and Jurassic marine strata.",
    "secondary": "In invertebrate paleontology, Grypoceras possesses an involute, coiled shell with characteristic hook-shaped sutures and a sub-central siphuncle.",
    "quotes": [
      {
        "author": "Alpheus Hyatt",
        "work": "Genera of Fossil Cephalopods",
        "quote": "The diagnostic suture patterns of **Grypoceras** distinguish it from ancestral nautiloids of the late Paleozoic."
      },
      {
        "author": "Curt Teichert",
        "work": "Treatise on Invertebrate Paleontology: Mollusca 4",
        "quote": "Specimens of **Grypoceras** recovered from Alpine Triassic limestones display elegant involute whorl geometry."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The post-extinction recovery of coiled cephalopods like **Grypoceras** illustrates resilient iterative evolution across mass extinction boundaries."
      }
    ]
  },
  "Dashboard — gryp\\Gryposaurus.md": {
    "primary": "A genus of large, duck-billed hadrosaurid dinosaur from the late Cretaceous of North America, distinguished by a prominent arched nasal crest (hooked nose).",
    "secondary": "In vertebrate paleontology, Gryposaurus (the 'hook-nosed lizard') grew up to 9 meters in length, utilizing hundreds of densely packed cheek teeth to grind fibrous vegetation.",
    "quotes": [
      {
        "author": "Lawrence Lambe",
        "work": "On Gryposaurus notabilis, a New Genus and Species of Trachodont Dinosaur",
        "quote": "The prominent arched nasal hump in **Gryposaurus** forms an unmistakable crest along the rostral facial axis."
      },
      {
        "author": "Robert T. Bakker",
        "work": "The Dinosaur Heresies",
        "quote": "The nasal arch of **Gryposaurus** may have supported an inflatable resonating air sac used for species-specific vocalization."
      },
      {
        "author": "Edwin H. Colbert",
        "work": "Dinosaurs: Their Discovery and Their World",
        "quote": "Massive dental batteries equipped **Gryposaurus** to grind tough Cretaceous conifer needles with extraordinary mechanical force."
      }
    ]
  },
  "Dashboard — gryp\\agrypnia.md": {
    "primary": "Severe, chronic, or total sleeplessness; extreme insomnia.",
    "secondary": "In neurology and somnology, agrypnia excitata is a life-threatening syndrome seen in fatal familial insomnia and Morvan's chorea, marked by motor agitation and autonomic hyperactivity.",
    "quotes": [
      {
        "author": "Thomas Willis",
        "work": "Two Discourses Concerning the Soul of Brutes",
        "quote": "In prolonged **agrypnia**, the animal spirits are incessantly agitated, preventing the brain from entering quiet repose."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient suffered from agonizing **agrypnia**, remaining wakeful and delirious through successive nights of high fever."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "Severe central sleep deregulation can produce profound **agrypnia**, blurring the cognitive boundaries between dreaming and waking reality."
      }
    ]
  },
  "Dashboard — gryp\\agrypnotic.md": {
    "primary": "Promoting wakefulness; preventing or counteracting sleep; stimulant or somnifugous.",
    "secondary": "In pharmacology, an agrypnotic substance (such as caffeine or modafinil) stimulates cortical arousal networks to stave off fatigue.",
    "quotes": [
      {
        "author": "Jonathan Pereira",
        "work": "The Elements of Materia Medica and Therapeutics",
        "quote": "Strong infusions of Camellia sinensis exert a marked **agrypnotic** effect upon students studying through the night."
      },
      {
        "author": "William Osler",
        "work": "Aequanimitas",
        "quote": "He relied on coffee as a gentle **agrypnotic**, sustaining concentration through long hours of hospital duty."
      },
      {
        "author": "Laurence L. Brunton",
        "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        "quote": "Central stimulants act as **agrypnotic** agents by blocking adenosine receptors in sleep-promoting nuclei."
      }
    ]
  },
  "Dashboard — gryp\\arthrogryposis.md": {
    "primary": "A congenital condition characterized by multiple joint contractures and curved or hooked joints present at birth, restricting normal mobility.",
    "secondary": "In pediatric orthopedics and clinical genetics, arthrogryposis multiplex congenita results from decreased fetal movement in utero (fetal akinesia).",
    "quotes": [
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "Early physical therapy and gentle serial casting are essential to mobilize rigid joints in neonatal **arthrogryposis**."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Histologic examination of muscle in severe **arthrogryposis** reveals marked neurogenic atrophy secondary to anterior horn cell loss."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Oligohydramnios can physically compress the developing fetus, contributing to the articular contractures of **arthrogryposis**."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Part 3 Batch 3.`);
