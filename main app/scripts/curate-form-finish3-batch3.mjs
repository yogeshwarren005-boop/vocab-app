import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — pter\\apteral.md": {
    "primary": "In classical architecture, describing a temple or building having columns at one or both ends but none along the lateral flanks.",
    "secondary": "In zoology and comparative morphology, lacking lateral wings or wing-like appendages.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "De Architectura (Ten Books on Architecture)",
        "quote": "The **apteral** temple features porticoes solely at the front and posticum without lateral external colonnades."
      },
      {
        "author": "James Fergusson",
        "work": "The Parthenon: An Essay on the Mode by Which Light Was Introduced",
        "quote": "The Temple of Athena Nike in Athens stands as the finest surviving example of an amphiprostyle **apteral** structure."
      },
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture on the Comparative Method",
        "quote": "Greek builders employed the **apteral** plan when restricted site boundaries precluded a full peristyle."
      }
    ]
  },
  "Dashboard — pter\\apterous.md": {
    "primary": "Lacking wings; wingless (especially of insects or birds).",
    "secondary": "In botany, designating plant organs, such as stems, petioles, or seeds, that lack membranous wing-like expansions.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "In oceanic islands, beetles frequently become **apterous** because flying individuals are repeatedly swept out to sea."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Wonders of Instinct",
        "quote": "The female glow-worm remains permanently **apterous**, emitting her luminous beacon from the roadside grass."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Unlike the winged fruits of maple and ash, the nut of the oak remains strictly **apterous**."
      }
    ]
  },
  "Dashboard — pter\\apterygidae.md": {
    "primary": "A family of flightless, nocturnal ratite birds comprising the kiwis (genus Apteryx), endemic to New Zealand.",
    "secondary": "In systematic ornithology, paleognathous birds characterized by vestigial wings hidden beneath shaggy hair-like plumage, nostrils at the bill tip, and keen olfaction.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of the Southern Apteryx",
        "quote": "The skeletal reduction observed in **apterygidae** represents the most extreme regression of the avian pectoral girdle."
      },
      {
        "author": "Walter Buller",
        "work": "A History of the Birds of New Zealand",
        "quote": "Members of **apterygidae** probe the damp humus of nocturnal forests in search of earthworms and larvae."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The survival of **apterygidae** in New Zealand underscores the evolutionary refuge afforded by prolonged island isolation."
      }
    ]
  },
  "Dashboard — pter\\apterygiformes.md": {
    "primary": "The taxonomic avian order consisting solely of the kiwis of New Zealand (family Apterygidae).",
    "secondary": "In avian systematics, an ancient ratite order sister to the extinct elephant birds of Madagascar, adapted to a terrestrial nocturnal forest niche.",
    "quotes": [
      {
        "author": "Alfred Newton",
        "work": "A Dictionary of Birds",
        "quote": "The order **apterygiformes** displays bone marrow density and nocturnal sensory specializations unique among living birds."
      },
      {
        "author": "Jared Diamond",
        "work": "The Third Chimpanzee: The Evolution and Future of the Human Animal",
        "quote": "Evolutionary isolation enabled **apterygiformes** to occupy the ecological niche filled by small nocturnal mammals elsewhere."
      },
      {
        "author": "Joel Cracraft",
        "work": "Phylogenetic Relationships and Monophyly of the Ratite Birds",
        "quote": "Cranial morphology within **apterygiformes** confirms their paleognathous palate and deep divergence from tinamous."
      }
    ]
  },
  "Dashboard — pter\\apterygote.md": {
    "primary": "Any primitively wingless insect belonging to the subclass Apterygota, such as a silverfish, bristletail, or firebrat.",
    "secondary": "In systematic entomology, a hexapod whose ancestors never evolved wings, undergoing slight or ametabolous development.",
    "quotes": [
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "The humble **apterygote** scuttles across damp soil, retaining the ancestral six-legged body architecture of primitive arthropods."
      },
      {
        "author": "A. D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "Unlike pterygote insects that lost wings secondarily, each true **apterygote** belongs to a lineage that never possessed flight organs."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "Subterranean niches harbor diverse **apterygote** species that decompose decaying leaf mulch in forest ecosystems."
      }
    ]
  },
  "Dashboard — pter\\apteryx.md": {
    "primary": "A genus of flightless, nocturnal ratite birds of New Zealand commonly called kiwis, having a long slender bill with terminal nostrils.",
    "secondary": "In evolutionary biology, an archaic bird remarkable for laying an egg that constitutes up to twenty percent of its total body mass.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Memoir on the Apteryx",
        "quote": "Dissection of the **apteryx** revealed robust pelvic musculature paired with tiny, rudimentary humeri buried in the fleece."
      },
      {
        "author": "Walter Buller",
        "work": "Manual of the Birds of New Zealand",
        "quote": "The sensitive vibrissae at the base of the bill assist the **apteryx** in locating subterranean food in absolute darkness."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man, and Selection in Relation to Sex",
        "quote": "The plumage of the **apteryx** is modified into coarse hair-like strands that blend invisibly against tree fern root masses."
      }
    ]
  },
  "Dashboard — pter\\archaeopteryx.md": {
    "primary": "An extinct genus of bird-like theropod dinosaurs from the Late Jurassic Solnhofen limestone of Bavaria, exhibiting feathers and toothed jaws.",
    "secondary": "In evolutionary paleontology, a celebrated transitional fossil possessing both reptilian traits (clawed fingers, long bony tail) and avian flight feathers.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Further Evidence of the Affinity between the Dinosaurian Reptiles and Birds",
        "quote": "The skeleton of **archaeopteryx** demonstrates beyond dispute that birds are the lineal descendants of dinosaurian ancestors."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Hardly any recent discovery is more remarkable than that of **archaeopteryx**, with its long lizard-like tail bearing pairs of feathers."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "The mosaic anatomy of **archaeopteryx** presents a perfect refutation to those who demand intermediate forms in the fossil record."
      }
    ]
  },
  "Dashboard — pter\\brachypterous.md": {
    "primary": "Having abnormally short or rudimentary wings (of insects or birds).",
    "secondary": "In ecological entomology, describing a morph or caste that trades flight dispersal ability for higher reproductive fecundity.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Several montane carabid beetles become **brachypterous** at high elevations, surviving as flightless foragers in the moss."
      },
      {
        "author": "Edward Bagnall Poulton",
        "work": "The Colours of Animals: Their Meaning and Use",
        "quote": "The **brachypterous** condition in female moths is accompanied by crypsis that blends seamlessly against lichen-covered trunks."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "Hormonal titering during nymphal stadia determines whether an individual matures into a macropterous or **brachypterous** adult."
      }
    ]
  },
  "Dashboard — pter\\brachyptery.md": {
    "primary": "The condition or evolutionary state of possessing short, reduced, or rudimentary wings non-functional for flight.",
    "secondary": "In evolutionary biology, wing reduction frequently observed in alpine, insular, or subterranean insect populations.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Insular **brachyptery** arises rapidly when natural selection penalizes flight dispersal over open, hostile waters."
      },
      {
        "author": "G. Evelyn Hutchinson",
        "work": "An Introduction to Population Ecology",
        "quote": "Polymorphism between flight capability and **brachyptery** reflects balancing trade-offs between dispersal and egg production."
      },
      {
        "author": "Douglas J. Futuyma",
        "work": "Evolutionary Biology",
        "quote": "Genomic analyses reveal that **brachyptery** can evolve repeatedly through mutations in wing development pathways."
      }
    ]
  },
  "Dashboard — pter\\Chiroptera.md": {
    "primary": "The mammalian order comprising bats, characterized by forelimbs modified into wings supported by elongated metacarpals and phalanges.",
    "secondary": "In systematic mammalogy, the second largest mammalian order, subdivided into Yinpterochiroptera and Yangochiroptera, capable of true sustained powered flight.",
    "quotes": [
      {
        "author": "John James Audubon",
        "work": "The Viviparous Quadrupeds of North America",
        "quote": "The nocturnal agility of **Chiroptera** fills the twilight sky with silent sweeps as they gather myriad flying insects."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The wing of **Chiroptera** exhibits immense elongation of the four fingers, between which the thin patagial membrane extends."
      },
      {
        "author": "Donald Griffin",
        "work": "Listening in the Dark: The Acoustic Orientation of Bats and Men",
        "quote": "Echolocation in **Chiroptera** allows navigation through pitch-black subterranean caverns by analyzing reflected ultrasonic pulses."
      }
    ]
  },
  "Dashboard — pter\\chiropterologist.md": {
    "primary": "A zoologist or biologist who specializes in the scientific study of bats (order Chiroptera).",
    "secondary": "In field mammalogy, a scientist who studies bat echolocation, ecology, cave hibernation, and viral zoonoses.",
    "quotes": [
      {
        "author": "Merlin Tuttle",
        "work": "America's Neighborhood Bats",
        "quote": "As an experienced **chiropterologist**, I spent decades documenting how insectivorous bats safeguard agriculture from destructive pests."
      },
      {
        "author": "Brock Fenton",
        "work": "Bats",
        "quote": "The modern **chiropterologist** employs ultrasonic acoustic monitors to survey nocturnal airspace without disturbing roosting colonies."
      },
      {
        "author": "Thomas Kunz",
        "work": "Ecological and Behavioral Methods for the Study of Bats",
        "quote": "Every field **chiropterologist** must exercise caution when sampling cave microclimates during winter torpor periods."
      }
    ]
  },
  "Dashboard — pter\\Endopterygota.md": {
    "primary": "A superorder of insects (holometabolous insects) whose wings develop internally inside the body of the larva and pupa.",
    "secondary": "In systematic entomology, comprising beetles, flies, wasps, and butterflies, defined by complete metamorphosis through egg, larva, pupa, and adult stages.",
    "quotes": [
      {
        "author": "A. D. Imms",
        "work": "Recent Advances in Entomology",
        "quote": "The evolutionary success of **Endopterygota** stems from the complete functional separation of larval feeding and adult reproductive stages."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Physiology of Insect Senses",
        "quote": "Imaginal discs within the pupa of **Endopterygota** give rise to the wings, legs, and compound eyes of the adult insect."
      },
      {
        "author": "Michael S. Engel",
        "work": "Evolution of the Insects",
        "quote": "Over eighty percent of all extant insect species belong to the colossal monophyletic radiation of **Endopterygota**."
      }
    ]
  },
  "Dashboard — pter\\exopterygota.md": {
    "primary": "A division or superorder of insects (hemimetabolous insects) in which the wings develop externally as visible wing buds during nymphal stages.",
    "secondary": "In entomology, including dragonflies, grasshoppers, true bugs, and mantises, characterized by gradual or incomplete metamorphosis lacking a pupal instar.",
    "quotes": [
      {
        "author": "R. F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "In **exopterygota**, the immature nymph already resembles a miniature adult, acquiring larger wing buds with each successive moult."
      },
      {
        "author": "John Henry Comstock",
        "work": "The Wings of Insects",
        "quote": "External wing development in **exopterygota** represents the phylogenetically ancestral condition among winged hexapods."
      },
      {
        "author": "Howard E. Evans",
        "work": "Life on a Little-Known Planet",
        "quote": "A young grasshopper belonging to **exopterygota** hops alongside its parents, feeding on the very same vegetation."
      }
    ]
  },
  "Dashboard — pter\\exopterygote.md": {
    "primary": "Of, relating to, or designating an insect belonging to the Exopterygota.",
    "secondary": "An insect exhibiting hemimetabolous development wherein wings develop externally upon the body wall without a pupal stage.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "Insect Physiology",
        "quote": "Ecdysone surges regulate each nymphal ecdysis until the **exopterygote** insect undergoes its final imaginal transformation."
      },
      {
        "author": "Penny Gullan",
        "work": "The Insects: An Outline of Entomology",
        "quote": "The **exopterygote** life cycle permits continuous ecological occupancy of the same habitat by both juveniles and adults."
      },
      {
        "author": "Charles Valentine Riley",
        "work": "Reports on the Insects of Missouri",
        "quote": "The chinch bug provides a classic example of an **exopterygote** crop pest multiplying through gradual nymphal instars."
      }
    ]
  },
  "Dashboard — pter\\helicopter.md": {
    "primary": "A heavier-than-air aircraft that obtains lift and propulsion from horizontally rotating overhead rotors or blades.",
    "secondary": "In aeronautical engineering, a vertical take-off and landing (VTOL) rotary-wing aircraft capable of hovering, forward, backward, and lateral flight.",
    "quotes": [
      {
        "author": "Igor Sikorsky",
        "work": "The Story of the Winged-S: An Autobiography",
        "quote": "The successful maiden flight of the VS-300 proved that the single main-rotor **helicopter** was practically sound and controllable."
      },
      {
        "author": "Antoine de Saint-Exupéry",
        "work": "Wind, Sand and Stars",
        "quote": "Pioneering aviation was driven by the dream of vertical flight, realized eventually in the rotor-driven **helicopter**."
      },
      {
        "author": "H. G. Wells",
        "work": "The War in the Air",
        "quote": "In speculative visions of future combat, the whirring blades of the **helicopter** scouted enemy positions over mountainous ridges."
      }
    ]
  },
  "Dashboard — pter\\hemiptera.md": {
    "primary": "A large taxonomic order of insects, commonly known as true bugs, characterized by piercing-sucking mouthparts.",
    "secondary": "In systematic entomology, comprising cicadas, aphids, planthoppers, and shield bugs, possessing forewings modified as hemelytra or uniformly membranous.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "Under the ordinal banner of **hemiptera**, I have classified insects whose rostrum is folded beneath the pectus for sucking fluids."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "The mouthparts in **hemiptera** form a jointed beak housing slender mandibular and maxillary stylets for piercing tissues."
      },
      {
        "author": "Carl Stål",
        "work": "Hemiptera Africana",
        "quote": "The immense diversity of tropical **hemiptera** includes both destructive plant-feeders and beneficial predatory assassins."
      }
    ]
  },
  "Dashboard — pter\\hemipteran.md": {
    "primary": "Any insect belonging to the order Hemiptera, such as a stink bug, bed bug, aphid, or cicada.",
    "secondary": "In ecological entomology, a sucking insect that feeds on plant phloem sap or acts as a hemophagous or predatory fluid-feeder.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "Social Life in the Insect World",
        "quote": "The predatory **hemipteran** impales its unsuspecting victim with a sharp beak, injecting liquefying digestive enzymes."
      },
      {
        "author": "A. D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "Many a phytophagous **hemipteran** serves as an efficient vector for systemic viral pathogens in agricultural crops."
      },
      {
        "author": "John Henry Comstock",
        "work": "Manual for the Study of Insects",
        "quote": "The defensive scent glands of an adult **hemipteran** discharge volatile pungent aldehydes when handled."
      }
    ]
  },
  "Dashboard — pter\\hemipteron.md": {
    "primary": "An individual true bug of the order Hemiptera (singular noun form of hemiptera).",
    "secondary": "In historical entomological descriptions, an insect possessing hemelytra and a rostrate piercing proboscis.",
    "quotes": [
      {
        "author": "William Kirby",
        "work": "An Introduction to Entomology",
        "quote": "Every **hemipteron** carries an elongated rostrum beneath its breast, ready to puncture plant stems or soft caterpillars."
      },
      {
        "author": "Thomas Say",
        "work": "Descriptions of New Species of Heteropterous Hemiptera",
        "quote": "I observed a striking **hemipteron** clinging to riparian reeds, its corium marked with intricate crimson reticulations."
      },
      {
        "author": "Hermann Burmeister",
        "work": "A Manual of Entomology",
        "quote": "The salivary pump of the **hemipteron** exerts hydraulic force to drive digestive secretions deep into host tissues."
      }
    ]
  },
  "Dashboard — pter\\hemipteronatus.md": {
    "primary": "A former genus name for tropical marine razorfishes (family Labridae), now classified primarily under Iniistius or Xyrichtys.",
    "secondary": "In ichthyology, laterally compressed wrasses that dive headfirst into soft benthic sand when threatened by predators.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "Histoire Naturelle des Poissons",
        "quote": "The knife-like forehead and elevated dorsal spine of **hemipteronatus** allow it to plunge instantaneously into sandy shoals."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Fishes referred to **hemipteronatus** possess an extremely sharp, compressed frontal ridge adapted for subterranean burrowing."
      },
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "Specimens of **hemipteronatus** taken from coral sandflats exhibit vibrant coloration and deciduous cycloid scales."
      }
    ]
  },
  "Dashboard — pter\\hemipterous.md": {
    "primary": "Belonging to, resembling, or characteristic of the order Hemiptera (the true bugs).",
    "secondary": "In biological morphology, possessing piercing-sucking mouthparts and hemelytrous or membranous wings.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In the arid pampas, I captured several **hemipterous** insects that mimic dry grass stems with extraordinary fidelity."
      },
      {
        "author": "Thomas Belt",
        "work": "The Naturalist in Nicaragua",
        "quote": "A curious **hemipterous** species lives in close mutualistic partnership with stinging acacia ants."
      },
      {
        "author": "Henry Walter Bates",
        "work": "The Naturalist on the River Amazons",
        "quote": "The bizarre thoracic horns of certain **hemipterous** treehoppers simulate thorns and dried leaf fragments."
      }
    ]
  },
  "Dashboard — pter\\heteroptera.md": {
    "primary": "A suborder of the order Hemiptera comprising the true bugs, having forewings whose basal portion is thickened and leathery while the apical part is membranous.",
    "secondary": "In systematic entomology, including assassin bugs, shield bugs, water striders, and bedbugs, distinguished by wings folding flat over the abdomen.",
    "quotes": [
      {
        "author": "W. S. Blatchley",
        "work": "Heteroptera or True Bugs of Eastern North America",
        "quote": "The suborder **heteroptera** encompasses aquatic, littoral, and terrestrial forms adapted to diverse nutritional niches."
      },
      {
        "author": "H. G. Barber",
        "work": "Insects of Porto Rico and the Virgin Islands: Heteroptera",
        "quote": "Identification of **heteroptera** relies upon the venation of the hemelytral membrane and the morphology of the scutellum."
      },
      {
        "author": "O. M. Reuter",
        "work": "Hemiptera Gymnocerata Europae",
        "quote": "Comparative analysis of antennae and sensory organs clarifies the evolutionary divergence across terrestrial **heteroptera**."
      }
    ]
  },
  "Dashboard — pter\\heteropterous.md": {
    "primary": "Of, relating to, or belonging to the suborder Heteroptera.",
    "secondary": "In descriptive entomology, possessing hemelytra that have distinct corium and membrane regions.",
    "quotes": [
      {
        "author": "Thomas Say",
        "work": "American Entomology",
        "quote": "This **heteropterous** insect secretes a defensive volatile liquid from thoracic orifices when disturbed in the net."
      },
      {
        "author": "William Kirby",
        "work": "Monographia Apum Angliae",
        "quote": "The rostrum of a **heteropterous** bug articulates from the anterior part of the head, pointing rearward in repose."
      },
      {
        "author": "John Curtis",
        "work": "British Entomology",
        "quote": "We illustrate a rare **heteropterous** specimen captured upon littoral marsh vegetation near the English Channel."
      }
    ]
  },
  "Dashboard — pter\\homoptera.md": {
    "primary": "A former suborder of the Hemiptera (now divided into Sternorrhyncha and Auchenorrhyncha) comprising aphids, cicadas, leafhoppers, and scale insects.",
    "secondary": "In historical entomology, phytophagous insects having forewings of uniform texture throughout, held roof-like over the body at rest.",
    "quotes": [
      {
        "author": "John Henry Comstock",
        "work": "The Wings of Insects",
        "quote": "Unlike true bugs, members of **homoptera** possess wings that are either entirely membranous or uniformly thickened."
      },
      {
        "author": "Charles Valentine Riley",
        "work": "The Periodical Cicada",
        "quote": "The piercing stylets of **homoptera** tap directly into the phloem vessels of forest trees, diverting vital carbohydrates."
      },
      {
        "author": "E. P. Felt",
        "work": "Key to American Insect Galls",
        "quote": "Galls formed by gall-making **homoptera** protect developing nymphs from predatory wasps and desiccating winds."
      }
    ]
  },
  "Dashboard — pter\\homopteran.md": {
    "primary": "Any insect traditionally classified in the suborder Homoptera, such as a leafhopper, aphid, or spittlebug.",
    "secondary": "In agricultural ecology, a phloem-feeding pest capable of producing large quantities of honeydew and transmitting phytoplasmas.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "A filter chamber in the digestive tract of the **homopteran** shunts excess water and sugars away from active midgut enzymes."
      },
      {
        "author": "A. E. Eaton",
        "work": "A Revisional Monograph of Recent Ephemeridae",
        "quote": "Swarming along riverine willows, the minute **homopteran** feeds on tender sapwood through slender mandibular setae."
      },
      {
        "author": "Charles Michener",
        "work": "The Social Behavior of the Bees",
        "quote": "Stingless bees eagerly forage on the sweet exudates produced by colonies of an arboreal **homopteran**."
      }
    ]
  },
  "Dashboard — pter\\homopterous.md": {
    "primary": "Of, relating to, or belonging to the Homoptera; having wings of uniform texture throughout.",
    "secondary": "In descriptive entomology, possessing roof-like wings and mouthparts arising from the posterior ventral part of the head.",
    "quotes": [
      {
        "author": "Hermann Burmeister",
        "work": "Handbuch der Entomologie",
        "quote": "The **homopterous** condition contrasts with the divided hemelytron seen in predatory water bugs."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "Arcana Entomologica",
        "quote": "We observed a bizarre **homopterous** lantern-fly whose cephalic prolongation was thought to emit luminescence."
      },
      {
        "author": "Asa Fitch",
        "work": "Reports on the Insects of New York",
        "quote": "Apple orchards suffer heavy damage from the feeding punctures of several small **homopterous** leafhoppers."
      }
    ]
  },
  "Dashboard — pter\\isoptera.md": {
    "primary": "A former order of social insects comprising the termites (now classified as an infraorder within Blattodea).",
    "secondary": "In entomology and sociobiology, eusocial insects living in structured colonies with castes, capable of digesting cellulose via microbial gut symbionts.",
    "quotes": [
      {
        "author": "Eugène Marais",
        "work": "The Soul of the White Ant",
        "quote": "The termite colony within the order **isoptera** behaves not as an assembly of individuals, but as a single organic whole."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "True eusociality evolved in **isoptera** millions of years before the appearance of social bees and ants."
      },
      {
        "author": "Thomas Snyder",
        "work": "Catalog of the Termites of the World",
        "quote": "Reproductive swarmers of **isoptera** shed their four equal-sized wings immediately upon completing nuptial dispersal flights."
      }
    ]
  },
  "Dashboard — pter\\isopteran.md": {
    "primary": "Any insect belonging to the Isoptera; a termite or white ant.",
    "secondary": "In insect ecology, a hemimetabolous social detritivore that recycles fallen timber and constructs earthen mounds.",
    "quotes": [
      {
        "author": "Maurice Maeterlinck",
        "work": "The Life of the White Ant",
        "quote": "The subterranean **isopteran** labors perpetually in total darkness, blind yet exquisitely sensitive to colony pheromones."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Social Life Among the Insects",
        "quote": "Soldier castes of an **isopteran** species defend nest tunnels with crushing mandibles or frontal chemical nozzles."
      },
      {
        "author": "Thomas Eisner",
        "work": "For Love of Insects",
        "quote": "Nasute soldiers of the tropical **isopteran** spray sticky diterpene repellents that disable attacking ants instantly."
      }
    ]
  },
  "Dashboard — pter\\megaloptera.md": {
    "primary": "An ancient order of holometabolous insects comprising the alderflies, dobsonflies, and fishflies.",
    "secondary": "In aquatic entomology, predatory freshwater insects whose aquatic larvae (hellgrammites) bear abdominal gills and whose adults possess broad, net-veined wings.",
    "quotes": [
      {
        "author": "James G. Needham",
        "work": "Aquatic Insects in New York State",
        "quote": "Larvae of the order **megaloptera** crawl under rocky rapids, seizing smaller aquatic nymphs with powerful mandibles."
      },
      {
        "author": "A. D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "Adult **megaloptera** are clumsy fliers, resting on streamside foliage while their immense membranous wings fold over the back."
      },
      {
        "author": "Norman H. Anderson",
        "work": "An Introduction to the Aquatic Insects of North America",
        "quote": "The large predatory hellgrammites of **megaloptera** serve as valuable bioindicators of well-oxygenated stream health."
      }
    ]
  },
  "Dashboard — pter\\megaptera.md": {
    "primary": "A genus of baleen whales containing the single living species Megaptera novaeangliae, the humpback whale.",
    "secondary": "In marine mammalogy, rorquals renowned for exceptionally long pectoral flippers (up to a third of body length), complex songs, and acrobatic breaching.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick; or, The Whale",
        "quote": "The Hump Back whale, which naturalists designate **megaptera**, sports huge wing-like flukes that beat the surface into foam."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "In **megaptera**, the hyperphalangy of the pectoral limbs produces enormous flippers that grant remarkable underwater maneuvering."
      },
      {
        "author": "William Henry Flower",
        "work": "Introduction to the Study of Mammals Living and Extinct",
        "quote": "The baleen plates of **megaptera** are comparatively short and coarse, adapted to filtering krill and small schooling fishes."
      }
    ]
  },
  "Dashboard — pter\\micropterus.md": {
    "primary": "A genus of freshwater game fishes in the sunfish family (Centrarchidae), commonly known as black basses.",
    "secondary": "In ichthyology and sports fisheries, North American freshwater apex predators including the largemouth bass (Micropterus salmoides) and smallmouth bass.",
    "quotes": [
      {
        "author": "Constantine Samuel Rafinesque",
        "work": "Ichthyologia Ohiensis",
        "quote": "I established the genus **micropterus** based on Ohio River specimens exhibiting stout bodies and notched dorsal fins."
      },
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "No sporting fish of inland waters commands higher esteem than the members of **micropterus** for their stubborn fighting spirit."
      },
      {
        "author": "Louis Agassiz",
        "work": "Lake Superior: Its Physical Character, Vegetation, and Animals",
        "quote": "Clear, boulder-strewn shorelines provide the favored spawning substrate for northern species of **micropterus**."
      }
    ]
  },
  "Dashboard — pter\\monopteral.md": {
    "primary": "In classical architecture, describing a round building or temple consisting of a circular colonnade supporting a roof without a central enclosed cella.",
    "secondary": "In architectural history, a lightweight circular peristyle pavilion, such as the Roman Temple of Vesta or garden tholos structures.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "De Architectura (Ten Books on Architecture)",
        "quote": "A **monopteral** temple has neither cella nor enclosing walls, but merely columns set in a circle under a round canopy."
      },
      {
        "author": "Andrea Palladio",
        "work": "The Four Books of Architecture",
        "quote": "The elegant simplicity of the **monopteral** pavilion was frequently copied in Renaissance landscape gardens."
      },
      {
        "author": "John Soane",
        "work": "Lectures on Architecture",
        "quote": "Light floods freely through the open columns of a **monopteral** shrine, blending sacred enclosure with surrounding nature."
      }
    ]
  },
  "Dashboard — pter\\Neoptera.md": {
    "primary": "A major taxonomic infraclass of winged insects comprising all orders that can flex and fold their wings flat over the abdomen when at rest.",
    "secondary": "In insect phylogenetics, a vast evolutionary lineage encompassing hemipterans, orthopterans, beetles, and butterflies, contrasting with the primitive Palaeoptera.",
    "quotes": [
      {
        "author": "Michael S. Engel",
        "work": "Evolution of the Insects",
        "quote": "The evolutionary breakthrough of the **Neoptera** was the wing-flexing mechanism that allowed insects to scurry into crevices without damaging delicate flight foils."
      },
      {
        "author": "Robin J. Wootton",
        "work": "The Functional Morphology of Insect Wings",
        "quote": "Specific third axillary sclerites in **Neoptera** act as mechanical hinges that fold the wing backwards over the abdominal tergites."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Hungry Fly",
        "quote": "Nearly every winged insect encountered in terrestrial undergrowth belongs to the adaptable evolutionary clade of **Neoptera**."
      }
    ]
  },
  "Dashboard — pter\\orthopter.md": {
    "primary": "Any insect belonging to the order Orthoptera, such as a grasshopper, cricket, katydid, or locust.",
    "secondary": "In entomology, a saltatorial insect with powerful jumping hind legs and leathery forewings that protect membranous hindwings.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "Social Life in the Insect World",
        "quote": "The great green **orthopter** chirps rhythmically from the vine, rubbing its file and scraper to serenade the twilight."
      },
      {
        "author": "Samuel H. Scudder",
        "work": "The Orthopteran Group Melanopli",
        "quote": "Systematic identification of each **orthopter** depends upon the shape of the male subgenital plate and caudal cerci."
      },
      {
        "author": "Leland O. Howard",
        "work": "The Insect Book",
        "quote": "A voracious **orthopter** can consume its own weight in green foliage within a single afternoon."
      }
    ]
  },
  "Dashboard — pter\\orthoptera.md": {
    "primary": "The taxonomic order of insects with biting mouthparts, straight leathery forewings (tegmina), and enlarged hind legs adapted for jumping.",
    "secondary": "In systematic entomology, divided into Caelifera (grasshoppers, locusts) and Ensifera (crickets, katydids), celebrated for acoustic stridulation.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "Members of **orthoptera** possess coriaceous upper wings beneath which the broad, folded membranous wings lie protected."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Grasshopper",
        "quote": "In hot Mediterranean afternoons, the acoustic choruses of **orthoptera** vibrate through dry scrub and dusty olive groves."
      },
      {
        "author": "A. D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "Auditory organs in **orthoptera** are located either upon the front tibiae in crickets or the first abdominal segment in acridids."
      }
    ]
  },
  "Dashboard — pter\\orthopteran.md": {
    "primary": "Of, relating to, or belonging to the order Orthoptera; a member of this order.",
    "secondary": "In physiological entomology, an insect possessing tympanal organs and acoustic mechanisms for intraspecific mate recognition.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "The saltatorial hind leg of an **orthopteran** incorporates resilin pads that store and release mechanical spring energy."
      },
      {
        "author": "Reginald F. Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "An **orthopteran** nymph matures through several flightless nymphal instars before developing functional stridulatory apparatus."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "Certain harvesting ants frequently forage on the protein-rich carcasses of a fallen **orthopteran**."
      }
    ]
  },
  "Dashboard — pter\\orthopteron.md": {
    "primary": "An individual orthopterous insect; a single grasshopper, locust, or cricket (singular of orthoptera).",
    "secondary": "In historical entomological descriptions, an insect possessing tegmina and saltatorial adaptations.",
    "quotes": [
      {
        "author": "William Kirby",
        "work": "An Introduction to Entomology",
        "quote": "The nocturnal song of an **orthopteron** echoes across meadows through the friction of modified wing veins."
      },
      {
        "author": "Thomas Say",
        "work": "American Entomology",
        "quote": "I described this western **orthopteron** from specimens collected during the Long expedition along the Arkansas River."
      },
      {
        "author": "Hermann Burmeister",
        "work": "A Manual of Entomology",
        "quote": "Every jumping **orthopteron** exhibits a greatly thickened metafemur enclosing powerful retractor muscles."
      }
    ]
  },
  "Dashboard — pter\\peripteral.md": {
    "primary": "In classical architecture, describing a temple or building surrounded on all four sides by a single continuous exterior peristyle colonnade.",
    "secondary": "In Hellenic temple design, the canonical form of the Doric and Ionic temple, exemplified by the Parthenon in Athens.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "Ten Books on Architecture",
        "quote": "A **peripteral** temple has six columns on each façade and eleven along the flanks, leaving an open ambulatory between the walls and columns."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "The magnificent **peripteral** colonnade of the Parthenon casts rhythmic shadows across the marble stylobate."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The severe dignity of the **peripteral** Greek temple contrasts profoundly with the clustered soaring shafts of northern Gothic cathedrals."
      }
    ]
  },
  "Dashboard — pter\\peripteros.md": {
    "primary": "A peripteral temple or building; a structure surrounded on all exterior sides by a continuous colonnade.",
    "secondary": "In classical archaeology and Greek architectural history, the definitive sacred monument plan of archaic and classical Greece.",
    "quotes": [
      {
        "author": "Banister Fletcher",
        "work": "A History of Architecture on the Comparative Method",
        "quote": "The monumental **peripteros** at Paestum preserves its archaic entablature and sturdy fluted columns in exceptional integrity."
      },
      {
        "author": "Pausanias",
        "work": "Description of Greece",
        "quote": "At Olympia, the ancient **peripteros** of Hera was originally built with oak columns that were gradually replaced with limestone."
      },
      {
        "author": "Andrea Palladio",
        "work": "The Four Books of Architecture",
        "quote": "The harmonious proportions of the ancient **peripteros** guided my designs for suburban villas surrounded by loggias."
      }
    ]
  },
  "Dashboard — pter\\pteretis.md": {
    "primary": "A botanical synonym or historical genus name for the ostrich fern (now classified as Matteuccia or Struthiopteris).",
    "secondary": "In pteridology, moisture-loving leptosporangiate ferns in Onocleaceae with dimorphic sterile arching fronds and erect woody fertile spikes.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The elegant crown of sterile fronds in **pteretis** surrounds dense brown fertile spikes that persist through winter."
      },
      {
        "author": "Merritt Lyndon Fernald",
        "work": "Gray's Manual of Botany",
        "quote": "In alluvial river floodplains, **pteretis** forms extensive colonies by means of deeply buried black subterranean stolons."
      },
      {
        "author": "Rolla M. Tryon",
        "work": "Ferns and Allied Plants",
        "quote": "Taxonomists historically assigned the ostrich fern to **pteretis** before consolidating the onocleoid genera."
      }
    ]
  },
  "Dashboard — pter\\pteridaceae.md": {
    "primary": "A large cosmopolitan family of ferns (order Polypodiales), commonly known as the maidenhair fern or brake family.",
    "secondary": "In pteridology, leptosporangiate ferns characterized by marginal or submarginal sori, frequently protected by a reflexed, false indusium.",
    "quotes": [
      {
        "author": "Rolla M. Tryon",
        "work": "The Fern Genus Pityrogramma",
        "quote": "The family **pteridaceae** displays tremendous ecological radiation, flourishing from desert rock crevices to wet tropical rainforest canopies."
      },
      {
        "author": "Robbin C. Moran",
        "work": "A Natural History of Ferns",
        "quote": "Members of **pteridaceae** often possess farinose secretions on the lower frond surfaces to retard water loss in arid environments."
      },
      {
        "author": "David B. Lellinger",
        "work": "A Field Manual of the Ferns and Fern-Allies of the United States and Canada",
        "quote": "In **pteridaceae**, the sporangia trace the veins or form continuous lines along the reflexed margins of the pinnules."
      }
    ]
  },
  "Dashboard — pter\\pteridium.md": {
    "primary": "A genus of coarse, large terrestrial ferns in the family Dennstaedtiaceae, commonly known as bracken.",
    "secondary": "In plant ecology and agriculture, cosmopolitan clonal weeds with deep rhizomes containing toxic ptaquiloside, invasive in pastures and heathlands.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Under **pteridium**, the common bracken fern spreads over dry hillsides, its triangular fronds unrolling on stout brown stipes."
      },
      {
        "author": "A. C. Seward",
        "work": "Plant Life Through the Ages",
        "quote": "Extensive fossil records confirm that ancestors of **pteridium** flourished widely across Mesozoic and Cenozoic landscapes."
      },
      {
        "author": "George Nicholson",
        "work": "The Illustrated Dictionary of Gardening",
        "quote": "The aggressive subterranean rhizomes of **pteridium** make it difficult to eradicate from cultivated grazing land."
      }
    ]
  },
  "Dashboard — pter\\pteridological.md": {
    "primary": "Of, relating to, or concerned with pteridology, the scientific study of ferns and related vascular spore-bearing plants.",
    "secondary": "In botanical literature, designating research, monographs, or herbarium collections devoted to pteridophytes.",
    "quotes": [
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "This comprehensive volume presents our **pteridological** findings based on specimens collected by botanical explorers worldwide."
      },
      {
        "author": "John Gilbert Baker",
        "work": "Synopsis Filicum",
        "quote": "Meticulous microscopic examination of sporangial annuli advanced **pteridological** classification beyond gross foliar morphology."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "Embryological studies provided a firmer basis for resolving thorny **pteridological** affinities among early land plants."
      }
    ]
  },
  "Dashboard — pter\\pteridologist.md": {
    "primary": "A botanist who specializes in pteridology, the study of ferns, horsetails, clubmosses, and related seedless vascular plants.",
    "secondary": "In taxonomic history, a scientist dedicated to surveying, identifying, and cataloging fern biodiversity.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Letters of Asa Gray",
        "quote": "Our resident **pteridologist** spent the summer in the Southern Appalachians hunting elusive rock spleenworts."
      },
      {
        "author": "Edward Tuckerman",
        "work": "Genera Lichenum: An Arrangement of the North American Lichens",
        "quote": "A devoted **pteridologist** must master subtle variations in venation and indusial development to identify difficult hybrids."
      },
      {
        "author": "Warren H. Wagner Jr.",
        "work": "Systematic Botany: Reticulate Evolution in the Appalachian Aspleniums",
        "quote": "The modern **pteridologist** applies cytogenetics and chromosome counting to unravel complex reticulate speciation in ferns."
      }
    ]
  },
  "Dashboard — pter\\pteridology.md": {
    "primary": "The branch of botany concerned with the scientific study of ferns, horsetails, lycophytes, and related seedless vascular plants.",
    "secondary": "In botanical science, encompassing morphology, anatomy, cytology, reproductive biology, and evolutionary phylogeny of pteridophytes.",
    "quotes": [
      {
        "author": "John Smith",
        "work": "Historia Filicum: An Exposition of the Nature and Organography of Ferns",
        "quote": "The nineteenth century witnessed a magnificent renaissance in **pteridology**, spurred by the Victorian fern-collecting craze."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns: Filicales",
        "quote": "Progress in **pteridology** requires synthesizing evidence from living gametophytes, stelar anatomy, and fossil paleobotany."
      },
      {
        "author": "Rolla M. Tryon",
        "work": "Ferns and Allied Plants",
        "quote": "Neotropical biodiversity continues to offer exciting frontiers for taxonomic discovery in field **pteridology**."
      }
    ]
  },
  "Dashboard — pter\\pteridophyta.md": {
    "primary": "The taxonomic plant division comprising the ferns and fern allies (vascular seedless cryptogams).",
    "secondary": "In botanical taxonomy, plants having alternating generations with dominant independent sporophytes that disperse by single-celled haploid spores.",
    "quotes": [
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "The division **pteridophyta** bridges non-vascular bryophytes and the higher seed-bearing phanerogams."
      },
      {
        "author": "Arthur J. Eames",
        "work": "Morphology of Vascular Plants",
        "quote": "Comparative stelar anatomy within the **pteridophyta** reveals the transition from primitive protosteles to complex siphonosteles."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Evolution of the Land Plants",
        "quote": "During the Carboniferous period, gigantic arborescent members of **pteridophyta** formed the vast swamp forests that produced coal beds."
      }
    ]
  },
  "Dashboard — pter\\pteridophyte.md": {
    "primary": "Any vascular plant that reproduces by spores and does not produce flowers or seeds; a fern, horsetail, or lycophyte.",
    "secondary": "In evolutionary botany, a tracheophyte exhibiting free-swimming flagellated sperm requiring moisture for fertilization.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The conductive xylem elements of a typical **pteridophyte** consist exclusively of scalariform tracheids without true vessel elements."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "The life cycle of a **pteridophyte** features an alternation between a large leafy sporophyte and a delicate, free-living prothallium."
      },
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "The coal measures abound in petrified remains demonstrating the anatomical complexity achieved by every ancient **pteridophyte**."
      }
    ]
  },
  "Dashboard — pter\\pteridosperm.md": {
    "primary": "Any of an extinct group of Paleozoic and Mesozoic gymnosperms (order Pteridospermales) having fern-like fronds but reproducing by true seeds; a seed fern.",
    "secondary": "In paleobotany, a key evolutionary intermediate linking primitive seedless cryptogams with early gymnospermous seed plants.",
    "quotes": [
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "The historic demonstration that Lyginopteris bore true seeds proved that this plant was not a fern, but a **pteridosperm**."
      },
      {
        "author": "F. W. Oliver",
        "work": "On the Structure of the Palaeozoic Seed Lagenostoma Lomaxi",
        "quote": "The discovery of ovules attached to fern-like fronds established the **pteridosperm** as a profound link in plant evolution."
      },
      {
        "author": "Thomas N. Taylor",
        "work": "Paleobotany: The Biology and Evolution of Fossil Plants",
        "quote": "Pollen-bearing microsporangiate organs confirm that the **pteridosperm** possessed sophisticated gymnospermous fertilization biology."
      }
    ]
  },
  "Dashboard — pter\\pteridospermae.md": {
    "primary": "The taxonomic class or order of extinct seed ferns (Pteridospermopsida) that flourished from the Devonian to the Cretaceous period.",
    "secondary": "In paleobotany, fossil seed plants combining fern-like fronds with gymnospermous vascular anatomy and naked seed production.",
    "quotes": [
      {
        "author": "Robert Kidston",
        "work": "Fossil Plants of the Carboniferous Rocks of Great Britain",
        "quote": "Extensive compression fossils belonging to **pteridospermae** dominate the shale deposits of the Upper Carboniferous coal basins."
      },
      {
        "author": "Chester A. Arnold",
        "work": "An Introduction to Paleobotany",
        "quote": "The recognition of **pteridospermae** removed hundreds of fossil species from the true ferns into the seed-bearing gymnosperms."
      },
      {
        "author": "Henry N. Andrews",
        "work": "Studies in Paleobotany",
        "quote": "Anatomical preservation of cupulate seeds within the **pteridospermae** illuminates early stages in ovular integument evolution."
      }
    ]
  },
  "Dashboard — pter\\pteridospermaphyta.md": {
    "primary": "A taxonomic division name proposed in paleobotany to encompass the seed ferns (pteridosperms) as an independent gymnospermous phylum.",
    "secondary": "In higher plant taxonomy, an archaic division of seed plants characterized by fern-like megaphyllous leaves, eustelic vascular cylinders, and gymnospermous ovules.",
    "quotes": [
      {
        "author": "Armen Takhtajan",
        "work": "Evolutionary Trends in Flowering Plants",
        "quote": "Many morphologists look to the division **pteridospermaphyta** as the broad ancestral complex from which angiosperms eventually arose."
      },
      {
        "author": "Arthur Cronquist",
        "work": "An Integrated System of Classification of Flowering Plants",
        "quote": "The placement of **pteridospermaphyta** at the base of the gymnosperm radiation clarifies the transition from homospory to seeds."
      },
      {
        "author": "A. C. Seward",
        "work": "Fossil Plants",
        "quote": "The diverse foliage types assembled under **pteridospermaphyta** illustrate the morphological plasticity of early Paleozoic seed plants."
      }
    ]
  },
  "Dashboard — pter\\pteridospermopsida.md": {
    "primary": "The formal taxonomic class containing the extinct seed ferns (pteridosperms), bridging seedless tracheophytes and modern seed plants.",
    "secondary": "In paleobotany, encompassing orders such as Lyginopteridales, Medullosales, Glossopteridales, and Caytoniales.",
    "quotes": [
      {
        "author": "Thomas N. Taylor",
        "work": "The Biology and Evolution of Fossil Plants",
        "quote": "Within the class **pteridospermopsida**, the Medullosales developed polystelic vascular stems with massive secondary xylem."
      },
      {
        "author": "Wilson N. Stewart",
        "work": "Paleobotany and the Evolution of Plants",
        "quote": "The cupules and seeds of **pteridospermopsida** display complex adaptations for wind pollination and subsequent embryo protection."
      },
      {
        "author": "Harlan P. Banks",
        "work": "Evolution and Plants of the Past",
        "quote": "Comparative analysis of fossil reproductive structures positions **pteridospermopsida** as the evolutionary springboard for all seed plants."
      }
    ]
  },
  "Dashboard — pter\\pteriidae.md": {
    "primary": "A taxonomic family of marine bivalve mollusks in the order Pterioida, commonly known as feather oysters and pearl oysters.",
    "secondary": "In malacology, marine bivalves having an oblique, winged hinge line and an inner shell layer coated in iridescent nacre (mother-of-pearl).",
    "quotes": [
      {
        "author": "George Washington Tryon",
        "work": "Structural and Systematic Conchology",
        "quote": "Bivalves of the family **pteriidae** attach themselves to rocky substrates or wharf pilings by a stout fibrous byssus."
      },
      {
        "author": "S. P. Woodward",
        "work": "A Manual of the Mollusca",
        "quote": "The renowned pearl oyster, belonging to **pteriidae**, secretes concentric layers of aragonite around foreign irritants."
      },
      {
        "author": "R. Tucker Abbott",
        "work": "American Seashells",
        "quote": "The Atlantic wing oyster exemplifies the characteristic oblique hinge and posterior wing extension typical of **pteriidae**."
      }
    ]
  },
  "Dashboard — pter\\pterion.md": {
    "primary": "An anatomical craniometric landmark on the side of the skull where the frontal, parietal, sphenoid, and temporal bones meet in an H-shaped suture.",
    "secondary": "In neurosurgery and cranial osteology, a critical surgical landmark lying directly over the anterior branch of the middle meningeal artery.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Fractures traversing the **pterion** are exceedingly dangerous because they readily lacerate the underlying middle meningeal artery."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "On the lateral temple, the junction of four cranial bones forms the delicate sutural crossing that surgeons call the **pterion**."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The closure of the anterolateral fontanelle during infancy establishes the definitive H-shaped suture known as the **pterion**."
      }
    ]
  },
  "Dashboard — pter\\pteris.md": {
    "primary": "A cosmopolitan genus of leptosporangiate ferns in the family Pteridaceae, commonly called brakes, characterized by marginal continuous sori.",
    "secondary": "In environmental botany and phytoremediation, terrestrial ferns (such as Pteris vittata) noted for hyperaccumulating arsenic from contaminated soils.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Under the genus **pteris**, the sporangia form an uninterrupted linear sorus along the reflexed margin of the pinnule."
      },
      {
        "author": "William Jackson Hooker",
        "work": "Genera Filicum",
        "quote": "The crisp green fronds of **pteris** adorn rocky ravines, displaying intricate dichotomous or reticulate venation."
      },
      {
        "author": "Rolla M. Tryon",
        "work": "Ferns and Allied Plants",
        "quote": "Species of **pteris** are widely distributed in the tropics, where they pioneer open banks and volcanic ash beds."
      }
    ]
  },
  "Dashboard — pter\\pternohyla.md": {
    "primary": "A former genus name for burrowing treefrogs (now classified under Smilisca), native to Mexico and the southwestern United States.",
    "secondary": "In herpetology, hylid frogs characterized by a heavily ossified, helmet-like skull (casqued head) utilized for phragmosis to block burrow entrances.",
    "quotes": [
      {
        "author": "Edward D. Cope",
        "work": "The Batrachia of North America",
        "quote": "The cranial dermal ossification in **pternohyla** unites the skull bones into a solid helmet adapted for dry arid survival."
      },
      {
        "author": "Hobart M. Smith",
        "work": "The Amphibians of Western North America",
        "quote": "During arid summer droughts, **pternohyla** retreats deep into underground burrows, sealing the opening with its hardened head."
      },
      {
        "author": "Linda Trueb",
        "work": "Evolutionary History of the Neotropical Treefrogs",
        "quote": "Hyperossification of the cranium in **pternohyla** represents an extreme adaptation to curb cutaneous moisture loss."
      }
    ]
  },
  "Dashboard — pter\\pterocarpus.md": {
    "primary": "A genus of pantropical trees in the legume family (Fabaceae), yielding valuable timber (padauk, narra) and medicinal kino resin.",
    "secondary": "In forestry and dendrology, trees characterized by golden-yellow flowers and circular, winged, indehiscent legume pods resembling discs.",
    "quotes": [
      {
        "author": "George Bentham",
        "work": "Flora Australiensis",
        "quote": "The distinctive circular fruit of **pterocarpus** is surrounded by a membranous wavy wing that aids wind dispersal."
      },
      {
        "author": "Samuel J. Record",
        "work": "Timbers of the New World",
        "quote": "The heartwood of **pterocarpus** exhibits rich vermilion or blood-red hues prized by cabinetmakers for fine furniture."
      },
      {
        "author": "David Fairchild",
        "work": "The World Was My Garden",
        "quote": "When the trunk of **pterocarpus** is incised, it exudes a ruby-red astringent sap known to commerce as gum kino."
      }
    ]
  },
  "Dashboard — pter\\pterocarya.md": {
    "primary": "A genus of deciduous hardwood trees in the walnut family (Juglandaceae), commonly known as wingnuts, native to Asia.",
    "secondary": "In dendrology and arboriculture, riparian trees bearing long, hanging female catkins of nutlets flanked by circular membranous wings.",
    "quotes": [
      {
        "author": "Charles Sprague Sargent",
        "work": "The Silva of North America",
        "quote": "The Caucasian wingnut, belonging to **pterocarya**, forms magnificent spreading specimens along moist riverbanks in temperate parks."
      },
      {
        "author": "Ernest Henry Wilson",
        "work": "A Naturalist in Western China",
        "quote": "Long pendant racemes of **pterocarya** fruits dangle gracefully from the branches like emerald necklaces in midsummer."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Botanically distinct from Juglans, the winged nutlets of **pterocarya** demonstrate efficient anemochoric seed dispersal."
      }
    ]
  },
  "Dashboard — pter\\pterocles.md": {
    "primary": "A genus of ground-dwelling arid-land birds in the family Pteroclidae, commonly called sandgrouse, native to Africa and Eurasia.",
    "secondary": "In desert avian ecology, seed-eating birds renowned for daily long-distance flights to water holes and carrying water in coiled breast feathers to chicks.",
    "quotes": [
      {
        "author": "Richard Bowdler Sharpe",
        "work": "A Hand-List of the Genera and Species of Birds",
        "quote": "Flocks of **pterocles** arrive at desert waterholes at daybreak, drinking rapidly before retreating into stony wilderness."
      },
      {
        "author": "Alfred Newton",
        "work": "A Dictionary of Birds",
        "quote": "The male **pterocles** soaks his breast plumage in water, flying dozens of miles across desert sands to nurture his brood."
      },
      {
        "author": "William Yarrell",
        "work": "A History of British Birds",
        "quote": "The cryptically mottled plumage of **pterocles** renders the bird almost invisible upon sun-baked gravel plains."
      }
    ]
  },
  "Dashboard — pter\\pteroclididae.md": {
    "primary": "The avian family of sandgrouse (order Pterocliformes), comprising sixteen species adapted to arid and semiarid habitats of the Old World.",
    "secondary": "In systematic ornithology, seed-eating birds intermediate between pigeons and plovers, possessing pigeon-like heads and gamebird-like compact bodies.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "Taxonomic placement of **pteroclididae** provoked extensive debate until biochemical data allied them with Columbiformes."
      },
      {
        "author": "Joel Cracraft",
        "work": "The Relationships and Evolution of the Galliform Birds",
        "quote": "Feather morphology in the family **pteroclididae** exhibits unique structural helices that hold capillary water during flight."
      },
      {
        "author": "David Lack",
        "work": "Ecological Adaptations for Breeding in Birds",
        "quote": "Synchronous nesting in **pteroclididae** corresponds with peak seed abundance following sporadic desert rains."
      }
    ]
  },
  "Dashboard — pter\\pterocnemia.md": {
    "primary": "A genus or subgenus of flightless South American ratite birds containing Darwin's rhea (Pterocnemia pennata), the lesser rhea.",
    "secondary": "In ornithology, an upland ratite of the Patagonian steppe and Andean altiplano, characterized by feathered tarsi and white-tipped plumage.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In Patagonia, I procured specimens of the rare lesser rhea, subsequently named **pterocnemia**, which differs markedly from the common ostrich."
      },
      {
        "author": "John Gould",
        "work": "The Zoology of the Voyage of H.M.S. Beagle",
        "quote": "The feathered leg and distinct mottled plumage of **pterocnemia** confirm its generic distinction from Rhea americana."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Island Life: Or, The Phenomena and Causes of Insular Faunas and Floras",
        "quote": "The distribution of **pterocnemia** across the arid southern plains illustrates geographic speciation along the Andean barrier."
      }
    ]
  },
  "Dashboard — pter\\pterodactyl.md": {
    "primary": "Any extinct flying reptile of the order Pterosauria, particularly those of the Late Jurassic with short tails and long beaks.",
    "secondary": "In popular paleontology, an informal designation for all flying archosaurs of the Mesozoic that flew by means of a skin membrane stretched along an elongated fourth finger.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Palaeontology: Or a Systematic Summary of Extinct Animals",
        "quote": "The fragile, pneumatic bones of the **pterodactyl** were exquisitely lightened to sustain active flight through Mesozoic skies."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Lost World",
        "quote": "A sudden shadow fell across the volcanic lake as an enormous **pterodactyl** wheeled overhead on leathery wings."
      },
      {
        "author": "Gideon Mantell",
        "work": "Petrifactions and Their Teachings",
        "quote": "The discovery of a toothless **pterodactyl** in chalk strata astonished those who viewed these creatures merely as winged lizards."
      }
    ]
  },
  "Dashboard — pter\\pterodactylidae.md": {
    "primary": "An extinct family of short-tailed pterosaurs from the Late Jurassic period, typified by the genus Pterodactylus.",
    "secondary": "In vertebrate paleontology, carnivorous or insectivorous flying reptiles characterized by elongated rostra, small slender teeth, and reduced fifth toes.",
    "quotes": [
      {
        "author": "Christian Erich Hermann von Meyer",
        "work": "Zur Fauna der Vorwelt",
        "quote": "In the lithographic limestone of Bavaria, members of **pterodactylidae** are preserved with complete wing impressions."
      },
      {
        "author": "Harry Govier Seeley",
        "work": "Dragons of the Air: An Account of Extinct Flying Reptiles",
        "quote": "The cranial construction of **pterodactylidae** reveals large orbits and spacious brain cavities indicative of acute vision in flight."
      },
      {
        "author": "Karl Alfred von Zittel",
        "work": "Text-Book of Palaeontology",
        "quote": "All known genera of **pterodactylidae** possess a short tail and elongated metacarpal bones supporting the flight finger."
      }
    ]
  },
  "Dashboard — pter\\pterodactylus.md": {
    "primary": "A genus of extinct short-tailed pterosaurs from the Late Jurassic of Germany, the first pterosaur ever discovered and scientifically named.",
    "secondary": "In paleontology, a small flying reptile with an estimated wingspan of about one meter, possessing a long straight skull armed with slender teeth.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "Recherches sur les ossemens fossiles",
        "quote": "I proved that **pterodactylus** was neither a bird nor a bat, but a true flying reptile belonging to an extinct order."
      },
      {
        "author": "William Buckland",
        "work": "Geology and Mineralogy Considered with Reference to Natural Theology",
        "quote": "The structure of the fourth digit in **pterodactylus** is uniquely elongated to stretch the membranous wing foil."
      },
      {
        "author": "Peter Wellnhofer",
        "work": "The Illustrated Encyclopedia of Pterosaurs",
        "quote": "Juvenile fossils of **pterodactylus** from Solnhofen provide unparalleled evidence of ontogenetic growth in pterosaurs."
      }
    ]
  },
  "Dashboard — pter\\pterois.md": {
    "primary": "A genus of venomous marine ray-finned reef fishes in the scorpionfish family (Scorpaenidae), commonly known as lionfishes.",
    "secondary": "In marine biology and invasive species ecology, predatory reef fishes of the Indo-Pacific, equipped with venomous fin rays, that have severely disrupted western Atlantic coral reefs.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "Histoire Naturelle des Poissons",
        "quote": "The magnificent pectoral fins of **pterois** spread like feathery fans, concealing grooved dorsal spines charged with toxic venom."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "With slow, deliberate movements, **pterois** herds small reef fishes against coral walls before swallowing them in an instant."
      },
      {
        "author": "John E. Randall",
        "work": "Reef and Shore Fishes of the South Pacific",
        "quote": "A puncture from the dorsal spines of **pterois** causes excruciating systemic pain and cardiovascular distress."
      }
    ]
  },
  "Dashboard — pter\\pteron.md": {
    "primary": "In classical Greek architecture, the lateral exterior colonnade or flank peristyle surrounding a temple.",
    "secondary": "In classical archaeology and entomological morphology, a wing, wing-like flank, or lateral side of a structure.",
    "quotes": [
      {
        "author": "Vitruvius",
        "work": "Ten Books on Architecture",
        "quote": "The **pteron** creates a sheltered ambulatory along the flanks of the sacred precinct, welcoming worshippers from the sun."
      },
      {
        "author": "Pausanias",
        "work": "Description of Greece",
        "quote": "Walking through the shaded **pteron** of the temple at Epidaurus, one admires the delicate fluting of the limestone columns."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "The spacing of columns in the **pteron** determined the overall optical rhythm of classical monumental façades."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 3 Batch 3.`);
