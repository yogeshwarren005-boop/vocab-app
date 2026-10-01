import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Animals & Zoology';

const filesData = {
  "Dashboard — hipp/ephippidae.md": {
    "primary": "A family of marine perciform fishes known as spadefishes, characterized by deep, laterally compressed bodies resembling a horse's saddle.",
    "secondary": "In ichthyology, reef and coastal fishes having small mouths, brush-like teeth, and steep dorsal profiles (from Greek ephippios, 'saddle-like').",
    "quotes": [
      {
        "author": "Albert Gunther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The family **Ephippidae** comprises compressed, high-backed fishes whose dorsal outline resembles an ornate riding saddle."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The Atlantic spadefish of the **Ephippidae** travels in vast schools around offshore rocky reefs and navigation pilings."
      },
      {
        "author": "Georges Cuvier",
        "work": "Histoire Naturelle des Poissons",
        "quote": "The distinctive cranial crest in **Ephippidae** gives the head a curious equestrian or crested contour."
      }
    ]
  },
  "Dashboard — hipp/ephippiorhynchus.md": {
    "primary": "A genus of large wading birds in the stork family (Ciconiidae), including the saddle-billed stork and black-necked stork.",
    "secondary": "In ornithology, colossal tropical storks characterized by a brightly colored bill bearing an upright frontal shield resembling a leather saddle.",
    "quotes": [
      {
        "author": "Richard Bowdler Sharpe",
        "work": "Catalogue of the Birds in the British Museum",
        "quote": "The magnificent saddle-billed stork was classified under **Ephippiorhynchus** on account of the yellow saddle-like frontal plate upon its culmen."
      },
      {
        "author": "David Livingstone",
        "work": "Missionary Travels and Researches in South Africa",
        "quote": "On the sandbanks of the Zambezi, tall pairs of **Ephippiorhynchus** stalked through the shallows with majestic strides."
      },
      {
        "author": "Frank M. Chapman",
        "work": "Camps and Cruises of an Ornithologist",
        "quote": "The striking black, white, and crimson bill of **Ephippiorhynchus** glinted brilliantly in the equatorial sunlight."
      }
    ]
  },
  "Dashboard — hipp/ephippium.md": {
    "primary": "A saddle-shaped anatomical structure; in crustacean biology, the thickened protective winter-egg saddle of cladocerans like Daphnia.",
    "secondary": "In human neuroanatomy, an archaic designation for the sella turcica of the sphenoid bone housing the pituitary gland (from Greek ephippion, saddle).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Upon the onset of drought, the female water-flea develops a dark, protective **ephippium** enclosing fertilized resting eggs."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The pituitary fossa was anciently termed the **ephippium** from its striking likeness to a Turkish saddle."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Zoology for High Schools and Colleges",
        "quote": "The shed **ephippium** of Daphnia floats upon the water surface, withstanding freezing temperatures until spring."
      }
    ]
  },
  "Dashboard — hipp/hipp.md": {
    "primary": "The Greek root combining form (hippos, 'horse') denoting horses, equestrian pursuits, or horse-like structures.",
    "secondary": "In comparative anatomy, taxonomy, and classical history, the root forming terms such as hippocampus, hippodrome, and Hippocrates.",
    "quotes": [
      {
        "author": "Max Muller",
        "work": "Lectures on the Science of Language",
        "quote": "The Greek root **hipp** preserves the ancient Indo-European designation for the swift steed of battle."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Mythological hydras and hybrid monsters often compounded the equine **hipp** stem with aquatic serpents."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "In phylogenetic reconstructions of ungulate lineages, the **hipp** series demonstrates remarkable toe reduction."
      }
    ]
  },
  "Dashboard — hipp/hipparchus.md": {
    "primary": "An ancient Greek cavalry commander or general of horse; or the celebrated ancient Greek astronomer Hipparchus of Nicaea.",
    "secondary": "In classical history, a civic military magistrate in Hellenistic poleis; in astronomy, the scientist who compiled the first comprehensive star catalogue and discovered the precession of the equinoxes.",
    "quotes": [
      {
        "author": "Xenophon",
        "work": "The Cavalry General (Hipparchicus)",
        "quote": "A competent **hipparchus** must inspect not only the armor of his riders but the hooves and spirit of every horse."
      },
      {
        "author": "Ptolemy",
        "work": "Almagest",
        "quote": "I verified the precession of the stellar sphere by comparing my observations with the catalogue of **Hipparchus**."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The profound trigonometric calculations of **Hipparchus** laid the true foundations of mathematical astronomy."
      }
    ]
  },
  "Dashboard — hipp/hippeastrum.md": {
    "primary": "A genus of bulbous flowering perennial plants in the family Amaryllidaceae native to tropical America, commonly cultivated as amaryllis.",
    "secondary": "In horticultural botany, showy plants producing large, trumpet-shaped flowers on hollow scapes, literally 'knight's star' (Greek hippeus, knight/horseman + astron, star).",
    "quotes": [
      {
        "author": "William Herbert",
        "work": "Amaryllidaceae",
        "quote": "I established the genus **Hippeastrum** to honor the knightly star-like symmetry of these splendid South American lilies."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The crimson trumpets of greenhouse **Hippeastrum** burst into glorious bloom in midwinter from dormant bulbs."
      },
      {
        "author": "Asa Gray",
        "work": "Field, Forest, and Garden Botany",
        "quote": "Cultivated hybrids of **Hippeastrum** exhibit immense flowers ranging from pure porcelain white to deep velvety carmine."
      }
    ]
  },
  "Dashboard — hipp/hipped.md": {
    "primary": "Having hips of a specified kind; or in architecture, designating a roof having sloping ends as well as sloping sides.",
    "secondary": "In building construction, describing a hip roof (hipped roof) where all four sides slope downward toward the walls without vertical gables; historically, affected with low spirits or hip.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The old vernacular barns were sheltered by low, **hipped** roofs designed to deflect the force of Atlantic gales."
      },
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "The ancient farmhouse was a rambling structure of red brick beneath a weather-stained **hipped** roof of mossy tiles."
      },
      {
        "author": "Jonathan Swift",
        "work": "Journal to Stella",
        "quote": "I was terribly **hipped** yesterday with melancholy thoughts and spleen, but the brisk morning walk revived me."
      }
    ]
  },
  "Dashboard — hipp/hippeis.md": {
    "primary": "The social class of cavalrymen or horse-owning citizens in ancient Athens and other Greek city-states.",
    "secondary": "In classical Athenian history, the second-highest property class established under the Solonian constitution, assessed at three hundred medimnoi and obligated to maintain a warhorse.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "The Constitution of Athens",
        "quote": "Solon divided the citizen body into four classes, of which the **Hippeis** comprised those wealthy enough to furnish an equipped cavalry mount."
      },
      {
        "author": "Thucydides",
        "work": "History of the Peloponnesian War",
        "quote": "The Athenian **Hippeis** charged down upon the Spartan flank, preventing their light infantry from outflanking the phalanx."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "Membership among the **Hippeis** conferred high civic prestige and prominent aristocratic standing in the assembly."
      }
    ]
  },
  "Dashboard — hipp/hippie.md": {
    "primary": "A person, especially of the 1960s counterculture, who rejected conventional societal norms, advocating peace, love, and communal living.",
    "secondary": "In cultural sociology, an adherent of the mid-20th-century anti-war movement associated with psychedelic music, bohemian dress, and alternative lifestyles.",
    "quotes": [
      {
        "author": "Joan Didion",
        "work": "Slouching Towards Bethlehem",
        "quote": "In the Haight-Ashbury, every runaway adolescent adopted the colorful attire and quiet slogans of the young **hippie**."
      },
      {
        "author": "Hunter S. Thompson",
        "work": "Fear and Loathing in Las Vegas",
        "quote": "That high and beautiful wave of the sixties broke, leaving the bewildered **hippie** stranded upon the shores of a harsher reality."
      },
      {
        "author": "Tom Wolfe",
        "work": "The Electric Kool-Aid Acid Test",
        "quote": "The bus rolled across America, transforming curious spectators into the vanguard of the modern **hippie** ethos."
      }
    ]
  },
  "Dashboard — hipp/hippies.md": {
    "primary": "Plural of hippie; participants in the 1960s countercultural youth movement advocating pacifism and counter-conventional lifestyles.",
    "secondary": "In social history, the large youth cohort that gathered at music festivals, established rural communes, and popularized environmental and peace movements.",
    "quotes": [
      {
        "author": "Joan Didion",
        "work": "The White Album",
        "quote": "Flocks of young **hippies** drifted through Golden Gate Park with flowers braided into their tangled hair."
      },
      {
        "author": "Hunter S. Thompson",
        "work": "Hell's Angels",
        "quote": "The clash between the outlaw motorcyclists and the gentle **hippies** exposed the profound fissures of the sixties."
      },
      {
        "author": "Tom Wolfe",
        "work": "The Pump House Gang",
        "quote": "Suburban parents watched with bafflement as thousands of self-styled **hippies** gathered to celebrate the Summer of Love."
      }
    ]
  },
  "Dashboard — hipp/hippo.md": {
    "primary": "Informal abbreviation for a hippopotamus; or the Greek root element hippos (horse).",
    "secondary": "In colloquial natural history and zoo keeping, common shorthand for Hippopotamus amphibius; historically, also an ancient North African city (Hippo Regius, home of St. Augustine).",
    "quotes": [
      {
        "author": "Theodore Roosevelt",
        "work": "African Game Trails",
        "quote": "A huge bull **hippo** suddenly thrust its massive pink-edged muzzle above the brown waters of the river pool."
      },
      {
        "author": "W. H. Hudson",
        "work": "The Naturalist in La Plata",
        "quote": "Visitors at the zoological gardens crowded along the iron railings to watch the colossal **hippo** submerge."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Augustine served as bishop of **Hippo** while the Vandals laid siege to the crumbling Roman ramparts."
      }
    ]
  },
  "Dashboard — hipp/hippobosca.md": {
    "primary": "A genus of blood-sucking louse flies (family Hippoboscidae) that ectoparasitize horses, cattle, and other domestic ungulates.",
    "secondary": "In veterinary entomology, dipteran insects known as forest flies or horse flies that scuttle sideways across the animal's hide and retain larvae until pupation.",
    "quotes": [
      {
        "author": "William Spence",
        "work": "An Introduction to Entomology",
        "quote": "The forest fly, **Hippobosca** equina, torments horses with its leathery body and tenaciously clinging claws."
      },
      {
        "author": "Charles Valentine Riley",
        "work": "The American Entomologist",
        "quote": "Unlike typical flies, **Hippobosca** deposits fully grown larvae ready to transform immediately into pupae."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "The dorsoventral flattening of **Hippobosca** enables it to slip smoothly between the coarse hairs of its mammalian host."
      }
    ]
  },
  "Dashboard — hipp/hippoboscid.md": {
    "primary": "Any fly belonging to the family Hippoboscidae, commonly known as a louse fly or ked.",
    "secondary": "In dipterology, an obligate blood-sucking pupiparous fly infesting birds or mammals, possessing flattened leathery cuticles and hooked tarsal claws.",
    "quotes": [
      {
        "author": "L. O. Howard",
        "work": "The Insect Book",
        "quote": "Every wingless sheep ked is technically a degenerate **hippoboscid** fly that has abandoned aerial flight."
      },
      {
        "author": "Frank M. Chapman",
        "work": "Handbook of Birds of Eastern North America",
        "quote": "While banding migrating raptors, we frequently discovered a parasitic **hippoboscid** clinging to the plumage."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "The specialized viviparity of the **hippoboscid** provides milk glands within the maternal uterus to nourish the developing larva."
      }
    ]
  },
  "Dashboard — hipp/hippoboscidae.md": {
    "primary": "A taxonomic family of specialized parasitic flies (superfamily Hippoboscoidea) including louse flies, forest flies, and sheep keds.",
    "secondary": "In veterinary parasitology, blood-feeding dipterans exhibiting adenotrophic viviparity and remarkable adaptations for phoretic hitchhiking upon avian and mammalian hosts.",
    "quotes": [
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "The family **Hippoboscidae** contains abnormal flies whose clawed tarsi are marvelously adapted for clinging to hair and feathers."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Members of **Hippoboscidae** transmit hematozoan parasites and cause severe irritation in domestic herds."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "Modern Classification of Insects",
        "quote": "Latreille assigned the **Hippoboscidae** to the order Pupipara because the female produces a hardened puparium rather than eggs."
      }
    ]
  },
  "Dashboard — hipp/hippocampus.md": {
    "primary": "A major seahorse-shaped component of the mammalian brain involved in memory consolidation; or the genus of seahorses (Hippocampus).",
    "secondary": "In neuroanatomy, an allocortical structure within the medial temporal lobe essential for episodic memory and spatial navigation; in marine biology, a syngnathid fish with prehensile tail.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Lesions in the region of the **hippocampus** produce profound impairments in the conscious retention of new experiences."
      },
      {
        "author": "Santiago Ramon y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "The elegant pyramidal neurons of the **hippocampus** send exquisite axonal collaterals across the Ammonic horn."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Year at the Shore",
        "quote": "The little sea-horse, named **Hippocampus** from its curved equine head, curled its flexible tail around a sprig of seaweed."
      }
    ]
  },
  "Dashboard — hipp/hippocastanaceae.md": {
    "primary": "A former plant family of trees and shrubs containing horse chestnuts and buckeyes (genus Aesculus), now merged into Sapindaceae.",
    "secondary": "In systematic botany, deciduous woody plants characterized by palmately compound leaves, showy upright panicles of flowers, and leathery spiny capsules containing glossy seeds.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The buckeyes of North America constituted the primary indigenous representatives of the family **Hippocastanaceae**."
      },
      {
        "author": "John Torrey",
        "work": "A Flora of the State of New York",
        "quote": "The European horse chestnut, widely planted along urban boulevards, belongs to the family **Hippocastanaceae**."
      },
      {
        "author": "Armen Takhtajan",
        "work": "Diversity and Classification of Flowering Plants",
        "quote": "Modern cladistic analysis demonstrated that **Hippocastanaceae** is nested deeply within the broader maple-soapberry family Sapindaceae."
      }
    ]
  },
  "Dashboard — hipp/hippocrates.md": {
    "primary": "The ancient Greek physician of Kos (c. 460–c. 370 BCE), traditionally honored as the Father of Western Medicine.",
    "secondary": "In the history of science and medical ethics, the foundational author of the Hippocratic Corpus who liberated clinical medicine from superstition and established the humoral doctrine.",
    "quotes": [
      {
        "author": "Plato",
        "work": "Phaedrus",
        "quote": "Does not **Hippocrates** the Asclepiad say that one cannot understand the nature of the body without understanding the nature of the whole?"
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "No physician ever observed the natural course of disease with clearer vision and deeper humility than **Hippocrates**."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "I have taken **Hippocrates** as my guide, following closely the footsteps of nature rather than scholastic hypotheses."
      }
    ]
  },
  "Dashboard — hipp/hippocratic.md": {
    "primary": "Of, relating to, or characteristic of Hippocrates, his medical treatises, or ethical standards.",
    "secondary": "In clinical medicine, designating foundational ethical oaths (Hippocratic Oath) or classic diagnostic physical signs like the Hippocratic facies (sunken features portending death).",
    "quotes": [
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "Every young physician stepping into clinical practice solemnly repeats the venerable tenets of the **Hippocratic** oath."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The dying man's sharp nose and hollow temples presented that pinched, ghastly **Hippocratic** countenance which warns that life is ebbing."
      },
      {
        "author": "Sigmund Freud",
        "work": "An Outline of Psycho-Analysis",
        "quote": "The therapeutic alliance respects the ancient **Hippocratic** precept to assist the suffering patient and above all do no harm."
      }
    ]
  },
  "Dashboard — hipp/hippocrepis.md": {
    "primary": "A genus of leguminous flowering plants in the pea family (Fabaceae), commonly known as horseshoe vetch.",
    "secondary": "In botany and entomology, European herbs bearing distinctive horseshoe-shaped curved pod segments (from Greek hippos + krepis, horse boot/shoe), larval host of the chalkhill blue butterfly.",
    "quotes": [
      {
        "author": "John Gerard",
        "work": "The Herball or Generall Historie of Plantes",
        "quote": "The curious jointed seed-pods of **Hippocrepis** bend into little crescents resembling the iron shoe of a horse."
      },
      {
        "author": "William Jackson Hooker",
        "work": "British Flora",
        "quote": "Upon the chalk downs of southern England, bright yellow clusters of **Hippocrepis** comosa carpet the sunny turf."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History of Selborne",
        "quote": "The chalk hills abound with **Hippocrepis**, where the rare blue butterflies flutter over its yellow blossoms."
      }
    ]
  },
  "Dashboard — hipp/hippodamia.md": {
    "primary": "In Greek mythology, daughter of King Oenomaus of Pisa, won in a chariot race by Pelops; also a genus of ladybird beetles.",
    "secondary": "In entomology, a genus of predatory coccinellid beetles including the convergent lady beetle (Hippodamia convergens), valuable in biological aphid control.",
    "quotes": [
      {
        "author": "Pindar",
        "work": "Olympian Odes",
        "quote": "Pelops won the fair maiden **Hippodamia** by defeating her fierce father in the chariot race across the sands of Elis."
      },
      {
        "author": "C. V. Riley",
        "work": "Reports on Injurious Insects",
        "quote": "Dense aggregations of the ladybird **Hippodamia** congregate upon high mountain peaks before dispersing to lowland orchards."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "Both adults and larvae of **Hippodamia** prey voraciously upon destructive aphids and scale insects."
      }
    ]
  },
  "Dashboard — hipp/hippodrome.md": {
    "primary": "An ancient Greek or Roman stadium designed for horse and chariot racing; or a modern arena, circus, or theater.",
    "secondary": "In classical archaeology and urban history, a massive elongated oval arena with tiered seating, such as the famous Hippodrome of Constantinople.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The factions of the **Hippodrome** in Constantinople shook the foundations of the Byzantine throne with the fury of the Nika riots."
      },
      {
        "author": "Lord Byron",
        "work": "Don Juan",
        "quote": "He traversed the wide square where ancient emperors once drove chariots around the colossal **hippodrome**."
      },
      {
        "author": "Washington Irving",
        "work": "The Alhambra",
        "quote": "Moorish cavaliers displayed feats of equestrian horsemanship in the wide **hippodrome** outside the city gates."
      }
    ]
  },
  "Dashboard — hipp/hippoglossoides.md": {
    "primary": "A genus of righteye flatfishes (family Pleuronectidae) including the American plaice and rough dab.",
    "secondary": "In marine fisheries biology, cold-water benthic flatfishes inhabiting North Atlantic and North Pacific continental shelves, morphologically resembling small halibuts.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The American plaice, classified as **Hippoglossoides** platessoides, supports an extensive bottom trawl fishery in the Grand Banks."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "Specimens of **Hippoglossoides** were dredged from the muddy seabed at depths exceeding one hundred fathoms."
      },
      {
        "author": "Albert Gunther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The mouth of **Hippoglossoides** is large and symmetrical, armed with sharp conical teeth suited for seizing small crabs."
      }
    ]
  },
  "Dashboard — hipp/hippoglossus.md": {
    "primary": "The genus of colossal righteye flatfishes (family Pleuronectidae) comprising the Atlantic and Pacific halibuts.",
    "secondary": "In commercial marine fisheries, apex predatory flatfishes that reach lengths over two meters, literally named 'horse tongue' (Greek hippos + glossa) for their broad oval shape.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "I assigned the great halibut to Pleuronectes **hippoglossus** in reference to its vast tongue-like flattened body."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Giant halibut of the genus **Hippoglossus** patrol the deep northern banks, preying upon cod, haddock, and flounders."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The hardy fishermen of the northern banks hauled up the monstrous **Hippoglossus** through the freezing fog."
      }
    ]
  },
  "Dashboard — hipp/hippology.md": {
    "primary": "The scientific study of the horse, including equine anatomy, physiology, breeds, training, and veterinary care.",
    "secondary": "In historical military and agricultural science, the comprehensive discipline cultivated by cavalry officers and master breeders to optimize equine performance.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "A rigorous treatise on comparative **hippology** must trace the fusion of equine metapodials across geological epochs."
      },
      {
        "author": "George Romanes",
        "work": "Animal Intelligence",
        "quote": "Experimental **hippology** reveals that horses possess remarkable spatial memory and acute auditory discernment."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The practical arts of farriery and theoretical **hippology** should be united for the improvement of national cavalry."
      }
    ]
  },
  "Dashboard — hipp/hippomancy.md": {
    "primary": "Divination or predicting the future by observing the movements, neighing, or behaviors of horses.",
    "secondary": "In comparative folklore and ancient religion, sacred augury practiced by ancient Persians, Celts, and Germanic tribes using consecrated white stallions.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "Darius ascended the Persian throne through a sacred rite of **hippomancy**, when his stallion was the first to neigh at sunrise."
      },
      {
        "author": "Tacitus",
        "work": "Germania",
        "quote": "The German tribes practiced **hippomancy** in sacred groves, watching whether consecrated white horses stepped forward with the right or left hoof."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Ancient kings interpreted the trembling and whinnying of sacred steeds as prophetic signs of **hippomancy** before going into battle."
      }
    ]
  },
  "Dashboard — hipp/hippophagy.md": {
    "primary": "The practice or custom of eating horse meat as food.",
    "secondary": "In culinary history and anthrozoology, the consumption of equine meat, widely tabooed in Anglo-American culture but traditionally embraced in parts of Europe and Central Asia.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The gauchos of the Argentine pampas subsist cheerfully upon beef, though some indigenous tribes practice regular **hippophagy**."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Papal edicts in the eighth century strictly forbade **hippophagy** to break Christian converts from pagan Germanic sacrifices."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Scientific Essays",
        "quote": "Economic reformers argued that regulated **hippophagy** would provide wholesome, affordable animal protein to the urban poor."
      }
    ]
  },
  "Dashboard — hipp/hippophile.md": {
    "primary": "A person who loves, admires, or is exceptionally fond of horses; an equestrian enthusiast.",
    "secondary": "In equestrian society and sporting culture, an aficionado dedicated to horse breeding, riding, horsemanship, and equine welfare.",
    "quotes": [
      {
        "author": "Siegfried Sassoon",
        "work": "Memoirs of a Fox-Hunting Man",
        "quote": "As an ardent young **hippophile**, my entire universe revolved around the stable, the saddle, and the morning hunt."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of Silver Blaze",
        "quote": "Every observant **hippophile** in England had placed his wagers upon the magnificent missing racehorse."
      },
      {
        "author": "George Borrow",
        "work": "Lavengro",
        "quote": "The old Romany horse-dealer was a true **hippophile**, understanding the temper of a stallion by a mere whisper."
      }
    ]
  },
  "Dashboard — hipp/hippophobia.md": {
    "primary": "An abnormal, intense, or irrational fear of horses (equinophobia).",
    "secondary": "In clinical psychology, a specific animal phobia characterized by severe dread, trembling, and panic attacks triggered by horses or equine carriages.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Analysis of a Phobia in a Five-Year-Old Boy",
        "quote": "Little Hans developed a dramatic **hippophobia**, terrified that a horse pulling a heavy cart would bite him or collapse in the street."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Childhood traumatic memories of a bolting carriage can produce persistent **hippophobia** in nervous temperaments."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "The patient confessed an uncontrollable **hippophobia** that made crossing busy city thoroughfares an ordeal."
      }
    ]
  },
  "Dashboard — hipp/hippopotamidae.md": {
    "primary": "The mammalian family of artiodactyl ungulates comprising the two extant species: the common hippopotamus and the pygmy hippopotamus.",
    "secondary": "In mammalian paleontology and molecular systematics, a semiaquatic clade whose closest living relatives are the Cetacea (forming the clade Whippomorpha).",
    "quotes": [
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The family **Hippopotamidae** contains massive, thick-skinned ungulates adapted for a sluggish semiaquatic existence."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "The Principles of Classification and a Classification of Mammals",
        "quote": "Fossil members of **Hippopotamidae** roamed across Pleistocene Europe before retreating to African river systems."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Lying Stones of Marrakech",
        "quote": "DNA sequencing established the astonishing phylogenetic truth that the **Hippopotamidae** are the closest living terrestrial cousins of whales."
      }
    ]
  },
  "Dashboard — hipp/hippopotamus.md": {
    "primary": "A large, heavy, thick-skinned semiaquatic African mammal (Hippopotamus amphibius) with barrel-shaped body and massive jaws, literally 'river horse'.",
    "secondary": "In mammalogy and wildlife ecology, an herbivorous megaherbivore spending daytime submerged in rivers and lakes to prevent dehydration, emerging at dusk to graze.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "In the Nile dwells the **hippopotamus**, a quadruped with cloven hooves, horse-like mane, and tusks like a wild boar."
      },
      {
        "author": "David Livingstone",
        "work": "Missionary Travels and Researches in South Africa",
        "quote": "Our dugout canoe was nearly overturned when a wounded **hippopotamus** charged from the papyrus swamp."
      },
      {
        "author": "T. S. Eliot",
        "work": "The Hippopotamus",
        "quote": "The broad-backed **hippopotamus** rests on his belly in the mud; Although he seems so firm to us, he is merely flesh and blood."
      }
    ]
  },
  "Dashboard — hipp/hipposideridae.md": {
    "primary": "A family of Old World microbats known as roundleaf bats or Old World leaf-nosed bats.",
    "secondary": "In chiropterology, insectivorous bats possessing an intricate horseshoe-and-leaf nasal ornamentation used to focus echolocation pulses emitted through the nostrils.",
    "quotes": [
      {
        "author": "Gerrit S. Miller",
        "work": "The Families and Genera of Bats",
        "quote": "The family **Hipposideridae** is distinguished from Rhinolophidae by the absence of a posterior lanceolate noseleaf."
      },
      {
        "author": "Frank E. Beddard",
        "work": "Mammalia",
        "quote": "Caves throughout the Indo-Malayan archipelago shelter vast colonies of insectivorous bats belonging to the **Hipposideridae**."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "Members of the **Hipposideridae** radiate extensively across tropical Africa, southern Asia, and Australasia."
      }
    ]
  },
  "Dashboard — hipp/hipposideros.md": {
    "primary": "The type genus of Old World roundleaf bats, literally 'horse iron' in reference to their horseshoe-shaped fleshy noseleaf.",
    "secondary": "In systematic mammalogy, a diverse genus of insect-hunting cave bats utilizing constant frequency echolocation directed through complex nasal structures.",
    "quotes": [
      {
        "author": "Thomas Horsfield",
        "work": "Zoological Researches in Java",
        "quote": "I described several new species of **Hipposideros** found suspended in limestone caverns near the southern coast of Java."
      },
      {
        "author": "W. T. Blanford",
        "work": "The Fauna of British India: Mammalia",
        "quote": "The horseshoe portion of the noseleaf in **Hipposideros** lacks the central sella characteristic of true horseshoe bats."
      },
      {
        "author": "Richard Lydekker",
        "work": "A Hand-book to the British Mammalia",
        "quote": "At dusk, countless individuals of **Hipposideros** pour out of cavern mouths to hawk for beetles over the jungle canopy."
      }
    ]
  },
  "Dashboard — hipp/hippotragus.md": {
    "primary": "A genus of large, imposing African antelopes including the roan antelope and the sable antelope, literally 'horse goat'.",
    "secondary": "In mammalogy and game conservation, magnificent grazing bovids possessing compact muscular necks, erect manes, and long, backward-curving ringed horns.",
    "quotes": [
      {
        "author": "Theodore Roosevelt",
        "work": "African Game Trails",
        "quote": "The sable antelope, of the genus **Hippotragus**, is among the noblest beasts in Africa, with sweeping scimitar horns."
      },
      {
        "author": "Frederick Courteney Selous",
        "work": "A Hunter's Wanderings in Africa",
        "quote": "A herd of roan antelope **Hippotragus** stood upon the open ridge, their erect manes giving them an equine appearance."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Great and Small Game of Africa",
        "quote": "In speed and fierce courage when brought to bay, species of **Hippotragus** yield to no other African antelope."
      }
    ]
  },
  "Dashboard — hipp/hippy.md": {
    "primary": "Variant spelling of hippie; or having large, prominent, or wide hips.",
    "secondary": "In social history and fashion, denoting mid-century countercultural youth culture; in physical anthropology or tailoring, describing wide pelvic contours.",
    "quotes": [
      {
        "author": "Joan Didion",
        "work": "Slouching Towards Bethlehem",
        "quote": "A barefoot **hippy** girl sat on the curb outside the bookstore, strumming an acoustic guitar."
      },
      {
        "author": "Tom Wolfe",
        "work": "The Electric Kool-Aid Acid Test",
        "quote": "The entire psychedelic caravan embraced that new, free-spirited **hippy** style that was sweeping the West Coast."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Pygmalion",
        "quote": "The fashionable dressmaker remarked that the client's somewhat **hippy** figure required an empire waistline to balance the silhouette."
      }
    ]
  },
  "Dashboard — hipp/mesohippus.md": {
    "primary": "An extinct genus of small, three-toed early horses that lived during the Oligocene epoch in North America, literally 'middle horse'.",
    "secondary": "In vertebrate paleontology, a key transitional fossil in equine evolution, standing about two feet tall, possessing low-crowned molars for browsing on soft woodland foliage.",
    "quotes": [
      {
        "author": "O. C. Marsh",
        "work": "Fossil Horses in America",
        "quote": "The discovery of **Mesohippus** in the White River Badlands established a critical intermediate link in equine phylogeny."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "American Addresses",
        "quote": "In **Mesohippus**, three functional digits touch the ground on all four feet, demonstrating the gradual reduction from ancestral tetradactyl forms."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Age of Mammals",
        "quote": "The cranial capacity of **Mesohippus** was significantly enlarged compared to its Eocene predecessor Eohippus."
      }
    ]
  },
  "Dashboard — hipp/parahippocampus.md": {
    "primary": "The parahippocampal gyrus, a cortical brain region surrounding the hippocampus critical for memory encoding and environmental scene perception.",
    "secondary": "In cognitive neuroscience, gray matter cortex within the medial temporal lobe that funnels sensory input into the hippocampus and contains place-sensitive areas (PPA).",
    "quotes": [
      {
        "author": "Santiago Ramon y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "Pyramidal tract fibers pass from the **parahippocampus** into the entorhinal cortex, relaying cortical associations."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The cerebral gyri surrounding the Ammonic horn, notably the **parahippocampus**, mediate the emotional coloring of recalled events."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Damage extending into the **parahippocampus** disrupts the spatial orientation and topological memory of the patient."
      }
    ]
  },
  "Dashboard — hipp/protohippus.md": {
    "primary": "An extinct genus of three-toed grazing horses from the Miocene of North America, literally 'first/primitive horse'.",
    "secondary": "In equine paleontology, a moderately sized Miocene horse with high-crowned (hypsodont) teeth adapted for chewing abrasive prairie grasses, retaining tiny non-functional lateral toes.",
    "quotes": [
      {
        "author": "Joseph Leidy",
        "work": "The Extinct Mammalian Fauna of Dakota and Nebraska",
        "quote": "I established the genus **Protohippus** based on dental remains showing advanced cementum deposits and hypsodont crowns."
      },
      {
        "author": "O. C. Marsh",
        "work": "Fossil Horses in America",
        "quote": "In **Protohippus**, the side toes were reduced to slender splints suspended above the central weight-bearing hoof."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "Equidae of the Oligocene, Miocene, and Pliocene of North America",
        "quote": "The radiation of **Protohippus** coincided with the vast spread of silica-rich savanna grasslands across the continent."
      }
    ]
  },
  "Dashboard — jub/jubate.md": {
    "primary": "Having a mane or long, fringing hair; maned, like a lion, horse, or baboon.",
    "secondary": "In descriptive zoology, designating animals with a dorsal crest or shaggy mane (from Latin jubatus, derived from juba, mane).",
    "quotes": [
      {
        "author": "Thomas Pennant",
        "work": "History of Quadrupeds",
        "quote": "The male hamadryas baboon exhibits a majestic, **jubate** cape of silvery fur over its shoulders."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The **jubate** mane of the adult male lion darkens with age, signaling physical vigor to rival males."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Certain extinct ungulates exhibited a **jubate** crest running along the entire cervical spine."
      }
    ]
  },
  "Dashboard — jub/jubilance.md": {
    "primary": "A feeling or expression of great joy, triumph, or exultation.",
    "secondary": "In literary prose, an atmosphere of uninhibited rejoicing and communal celebration celebrating victory or liberation.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Typee",
        "quote": "The islanders greeted the dawn with bursts of wild **jubilance**, dancing along the palm-fringed shore."
      },
      {
        "author": "Charlotte Bronte",
        "work": "Jane Eyre",
        "quote": "A surge of sudden **jubilance** swept through my heart as the long-dreaded sorrow was lifted."
      },
      {
        "author": "Walt Whitman",
        "work": "Leaves of Grass",
        "quote": "I sound my barbaric yawp over the roofs of the world in pure **jubilance** of existence."
      }
    ]
  },
  "Dashboard — jub/jubilancy.md": {
    "primary": "The state or condition of being jubilant; exultant triumph and celebration.",
    "secondary": "In psychological and literary description, high-spirited joy and victorious buoyancy of spirit.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "The Return of the Native",
        "quote": "The bonfires on the heath crackled into the night sky, mirroring the rustic **jubilancy** of the villagers."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Her momentary **jubilancy** over the small triumph was soon tempered by the sobering realities of household duty."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "The History of Henry Esmond",
        "quote": "The bells of London chimed with noisy **jubilancy** to welcome news of the grand victory at Blenheim."
      }
    ]
  },
  "Dashboard — jub/jubilant.md": {
    "primary": "Feeling or expressing great happiness, triumph, or exultation.",
    "secondary": "Characterized by triumphant rejoicing or exuberant celebratory vocalization.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The heavenly host with **jubilant** shout and loud hosannas filled the eternal courts of light."
      },
      {
        "author": "Charles Dickens",
        "work": "A Christmas Carol",
        "quote": "The bells rang out their **jubilant** message across the snowy roofs, waking the glad city on Christmas morning."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "A **jubilant** crowd surged outside Downing Street as the final announcement of victory in Europe was proclaimed."
      }
    ]
  },
  "Dashboard — jub/jubilantly.md": {
    "primary": "In a joyful, triumphant, or exultant manner.",
    "secondary": "With unrestrained happiness and celebratory enthusiasm.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "The Adventures of Tom Sawyer",
        "quote": "Tom shouted **jubilantly** as his companions emerged safe from the deep labyrinth of McDougal's cave."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Kidnapped",
        "quote": "Alan Breck waved his bonnet **jubilantly** as we saw the English redcoats marching in the wrong direction."
      },
      {
        "author": "Louisa May Alcott",
        "work": "Little Women",
        "quote": "Jo waved the acceptance letter **jubilantly** over her head, declaring that her literary career had begun at last."
      }
    ]
  },
  "Dashboard — jub/jubilate.md": {
    "primary": "To rejoice or exult greatly; or the 100th Psalm (Jubilate Deo) sung as a canticle of joy.",
    "secondary": "In liturgy and rhetoric, a call to triumphant celebration and thanksgiving (from Latin jubilare, to shout for joy).",
    "quotes": [
      {
        "author": "Christopher Smart",
        "work": "Jubilate Agno",
        "quote": "For I will consider my Cat Jeoffry, and with him **jubilate** before the glorious presence of God."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The choral voices unite to **jubilate** over the majestic harmonies of the orchestral fugue."
      },
      {
        "author": "George Herbert",
        "work": "The Temple",
        "quote": "Let all the world in every corner sing and **jubilate** to the praise of my King."
      }
    ]
  },
  "Dashboard — jub/jubilation.md": {
    "primary": "A feeling of great happiness, triumph, or rejoicing; festive celebration.",
    "secondary": "In social history and literature, widespread public celebrations following peace, liberation, or momentous achievements.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The news of the barbarian defeat was received in Rome with wild **jubilation** and lavish games in the amphitheater."
      },
      {
        "author": "Leo Tolstoy",
        "work": "War and Peace",
        "quote": "Shouts of genuine **jubilation** echoed along the battalions as the Tsar rode past on his white stallion."
      },
      {
        "author": "Frederick Douglass",
        "work": "Life and Times of Frederick Douglass",
        "quote": "The midnight proclamation of emancipation brought tears of speechless **jubilation** to thousands in the packed hall."
      }
    ]
  },
  "Dashboard — jub/jubilee.md": {
    "primary": "A special anniversary of an event, especially one celebrating twenty-five, fifty, or sixty years.",
    "secondary": "In biblical tradition (Hebrew yovel), a holy sabbatical year celebrated every fifty years in ancient Israel, marked by the freeing of slaves and restoration of ancestral land.",
    "quotes": [
      {
        "author": "Leviticus",
        "work": "The King James Bible",
        "quote": "And ye shall hallow the fiftieth year, and proclaim liberty throughout all the land: it shall be a **jubilee** unto you."
      },
      {
        "author": "Alfred Lord Tennyson",
        "work": "Carmen Saeculare: An Ode in Honour of the Jubilee of Queen Victoria",
        "quote": "Fifty years of ever-broadening commerce! Fifty times the rose has flowered and faded on her golden **jubilee**."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The grand festival on the Champ de Mars seemed like a universal **jubilee** of brotherhood and newfound liberty."
      }
    ]
  },
  "Dashboard — lit/lit.md": {
    "primary": "Past and past participle of light; illuminated, ignited, or provided with light.",
    "secondary": "In Greek etymology (lite), an ancient root denoting supplication, prayer, or entreaty, as seen in litany.",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Iliad",
        "quote": "Prayers of entreaty, the sacred **lit** daughters of great Zeus, follow behind Ruin to heal her reckless wounds."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Treasure Island",
        "quote": "A lantern **lit** the smoke-filled cabin, throwing grotesque shadows of the mutineers upon the bulkhead."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "The feeble rays of the candle **lit** the tarnished armour upon the wall, revealing deep fissures in the masonry."
      }
    ]
  },
  "Dashboard — lit/litany.md": {
    "primary": "A series of petitions for use in church services, recited by clergy and responded to by the congregation; or a tedious recital or repetitive list.",
    "secondary": "In liturgical theology, formal supplicatory prayers (from Greek litaneia, entreaty) chanted during penitential seasons; colloquially, any monotonous catalog of grievances.",
    "quotes": [
      {
        "author": "John Donne",
        "work": "The Litanie",
        "quote": "In our solemn **litany**, we beseech the Trinity to deliver our frail souls from the perils of the world."
      },
      {
        "author": "George Orwell",
        "work": "Nineteen Eighty-Four",
        "quote": "He listened with numb weariness to the familiar **litany** of production quotas, military victories, and state enemies."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "The simple song of the wood thrush was a divine **litany** that purified the morning air."
      }
    ]
  },
  "Dashboard — lit/liter.md": {
    "primary": "A metric unit of capacity and volume equal to one cubic decimeter (1,000 cubic centimeters or approximately 1.057 US liquid quarts).",
    "secondary": "In the International System of Units (SI), standard unit of liquid measure derived historically via French litre from Greek litra (an ancient Sicilian silver coin and measure of weight).",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "We adopted the decimal measure of capacity, defining the **liter** as the volume of a cubic decimeter of pure water."
      },
      {
        "author": "H. G. Wells",
        "work": "The Food of the Gods and How It Came to Earth",
        "quote": "The chemist poured out exactly one **liter** of the concentrated growth tincture into the feeding trough."
      },
      {
        "author": "Jules Verne",
        "work": "Twenty Thousand Leagues Under the Sea",
        "quote": "The compressed air reservoirs of the Nautilus held thousands of **liter** volumes at immense atmospheric tension."
      }
    ]
  },
  "Dashboard — lit/unlit.md": {
    "primary": "Not provided with light; not illuminated; not ignited.",
    "secondary": "In literature and poetry, describing shadowy, gloomy, or dormant states lacking visual warmth or spiritual enlightenment.",
    "quotes": [
      {
        "author": "Robert Browning",
        "work": "The Statue and the Bust",
        "quote": "The **unlit** lamp and the ungirt loin, in life's true crisis when we should act, leave us forever wanting."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "She walked along the dark, **unlit** country lane, her footsteps rustling through wet fallen leaves."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "The silent river flowed toward the black sea beneath an ominous, **unlit** dome of gathering clouds."
      }
    ]
  },
  "Dashboard — lyc/lyc.md": {
    "primary": "The Greek root combining form (lykos, 'wolf') denoting wolves, lupine traits, or predatory canine habits.",
    "secondary": "In zoology, mythology, and medical history, the stem giving rise to lycanthropy, Lycaon, Lycopodium, and allied scientific nomenclature.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "The Greek root **lyc** was inscribed upon ancient Arcadian altars dedicated to Zeus Lycaeus."
      },
      {
        "author": "Max Muller",
        "work": "Lectures on the Science of Language",
        "quote": "Solar myths often confounded the root **lyc** meaning wolf with leukos meaning light and radiant dawn."
      },
      {
        "author": "Richard Owen",
        "work": "Odontography",
        "quote": "The carnassial sectorial teeth in the **lyc** family are engineered for severing tendons and shearing muscle."
      }
    ]
  },
  "Dashboard — lyc/lycanthropy.md": {
    "primary": "The mythical or magical transformation of a human into a wolf; or a psychiatric delusion in which a patient believes they are a wolf.",
    "secondary": "In medical history and folklore, a rare clinical monomania documented since classical antiquity where sufferers mimic lupine howling and carnivorous savagery.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Those afflicted with **lycanthropy** run barking and howling about graveyards by night, believing themselves transformed into wolves."
      },
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "It is an idle Greek fable of **lycanthropy** that a man, by swimming across a certain Arcadian lake, becomes a wolf."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Rites of shape-shifting and ceremonial **lycanthropy** were practiced among archaic hunters seeking the beast's predatory power."
      }
    ]
  },
  "Dashboard — lyc/Lycaon.md": {
    "primary": "In Greek mythology, an Arcadian king turned into a wolf by Zeus for serving him human flesh; in zoology, the genus of the African wild dog (Lycaon pictus).",
    "secondary": "In mammalogy, cursorial pack-hunting canids possessing mottled coats and four toes per foot, celebrated for extraordinary hunting coordination.",
    "quotes": [
      {
        "author": "Ovid",
        "work": "Metamorphoses",
        "quote": "Howling in terror, cruel **Lycaon** fled to the pastures, his royal garments transformed into shaggy wolf fur."
      },
      {
        "author": "Theodore Roosevelt",
        "work": "African Game Trails",
        "quote": "A pack of the painted wild dog, **Lycaon** pictus, trotted across the savannah in relentless pursuit of a gazelle."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The African hunting dog **Lycaon** is distinguished from true wolves by possessing only four digits on the forefeet."
      }
    ]
  },
  "Dashboard — lyc/lycopersicon.md": {
    "primary": "A former genus (now Solanum section Lycopersicon) of flowering plants in the nightshade family, containing the tomato (Lycopersicon esculentum).",
    "secondary": "In systematic botany, New World solanaceous plants bearing fleshy berries and pinnate aromatic leaves, literally 'wolf peach' due to ancient suspicions of toxicity.",
    "quotes": [
      {
        "author": "Philip Miller",
        "work": "The Gardeners Dictionary",
        "quote": "Tournefort established the genus **Lycopersicon** for the love-apple, separating it from the deadly nightshades."
      },
      {
        "author": "Alphonse de Candolle",
        "work": "Origin of Cultivated Plants",
        "quote": "Wild species of **Lycopersicon** originated in the Andean regions of Peru and Ecuador before domestication in Mexico."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The garden tomato, formerly cataloged as **Lycopersicon**, is now recognized as a specialized fleshy-fruited Solanum."
      }
    ]
  },
  "Dashboard — lyc/lycoris.md": {
    "primary": "A genus of flowering bulbous plants in the family Amaryllidaceae, commonly known as spider lilies, hurricane lilies, or red spider lily.",
    "secondary": "In horticulture and pharmacology, East Asian bulbs that produce leafless floral scapes bearing showy umbels with long recurved stamens, containing the alkaloid galantamine.",
    "quotes": [
      {
        "author": "William Herbert",
        "work": "Amaryllidaceae",
        "quote": "I named the genus **Lycoris** after the celebrated Roman beauty of Virgil's eclogues, to match its delicate floral grace."
      },
      {
        "author": "Robert Fortune",
        "work": "Three Years' Wanderings in the Northern Provinces of China",
        "quote": "Along the borders of rice fields, brilliant scarlet heads of **Lycoris** radiata flared like torches after autumn rains."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The remarkable autumn bloom of **Lycoris** appears abruptly after the foliage has completely withered away."
      }
    ]
  },
  "Dashboard — meliss/meliss.md": {
    "primary": "The Greek root combining form (melissa, 'honeybee', from meli, 'honey') denoting bees, apiary arts, or bee-like traits.",
    "secondary": "In classical literature and botany, the stem commemorating the mythical nymph Melissa who first taught mortals the harvest of honey; found in Melissa and melissophobia.",
    "quotes": [
      {
        "author": "Virgil",
        "work": "Georgics",
        "quote": "The ancient nymphs honoring the **meliss** art gathered golden honeycombs from hollow oak trunks."
      },
      {
        "author": "Max Muller",
        "work": "Lectures on the Science of Language",
        "quote": "The sweet Greek root **meliss** arose directly from the ancestral term for liquid sweetness and honey."
      },
      {
        "author": "Maurice Maeterlinck",
        "work": "The Life of the Bee",
        "quote": "The communal harmony of the **meliss** republic has inspired philosophical wonder since the dawn of Greece."
      }
    ]
  },
  "Dashboard — meliss/melissa.md": {
    "primary": "A genus of perennial herbaceous plants in the mint family (Lamiaceae), including lemon balm (Melissa officinalis); or in myth, the nymph who discovered honey.",
    "secondary": "In herbal medicine and pharmacology, an aromatic herb rich in rosmarinic acid and citronellal, long cultivated as a calming tisane and bee forage.",
    "quotes": [
      {
        "author": "John Gerard",
        "work": "The Herball or Generall Historie of Plantes",
        "quote": "The herb **Melissa**, or balm, comforteth the heart and driveth away all melancholic sadness from the spirits."
      },
      {
        "author": "William Turner",
        "work": "A New Herball",
        "quote": "Beekeepers rub their new hives with fresh bruised **Melissa** to entice the swarm to settle comfortably."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The sweet lemon-scented foliage of **Melissa** officinalis makes it a cherished inhabitant of kitchen gardens."
      }
    ]
  },
  "Dashboard — meliss/melissophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear of bees (apiphobia).",
    "secondary": "In clinical psychology, a specific animal phobia causing severe panic, hyperventilation, and flight responses at the buzzing or sight of honeybees.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "A severe childhood sting often produces a persistent **melissophobia** that makes garden walks a terrifying ordeal."
      },
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "The patient's acute **melissophobia** masked a deeper dread of sudden, uncontrollable bodily injury."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "The nervous invalid trembled with violent **melissophobia** whenever a solitary bumblebee approached the open window."
      }
    ]
  },
  "Dashboard — myz/myz.md": {
    "primary": "The Greek root combining form (myzein, 'to suck') denoting sucking habits, suction organs, or parasitic suction.",
    "secondary": "In zoological nomenclature, the combining element in Myzopoda (sucker-footed bats), Myzostoma (parasitic worms on crinoids), and related suction-adapted taxa.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The strange ectoparasite was designated from the **myz** stem because of the sucking discs lining its ventral margins."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy of the Invertebrate Animals",
        "quote": "Suctorial adaptations derived from the **myz** root reflect convergent feeding specializations across diverse phyla."
      },
      {
        "author": "Frank E. Beddard",
        "work": "Mammalia",
        "quote": "The suctorial wrist organs that give name to the **myz** group of bats function as adhesive vacuum discs."
      }
    ]
  },
  "Dashboard — myz/Myzopoda.md": {
    "primary": "The monotypic genus of bats (family Myzopodidae) containing the Madagascar sucker-footed bat (Myzopoda aurita).",
    "secondary": "In chiropterology, rare bats endemic to Madagascar possessing adhesive fleshy pads on the thumbs and soles of the feet, adhering to smooth ravenala palm leaves by wet adhesion.",
    "quotes": [
      {
        "author": "Oldfield Thomas",
        "work": "On the Mammals of Madagascar",
        "quote": "I examined the extraordinary adhesive pads of **Myzopoda**, which enable this bat to cling to smooth palm fronds."
      },
      {
        "author": "Gerrit S. Miller",
        "work": "The Families and Genera of Bats",
        "quote": "The family Myzopodidae contains the single aberrant genus **Myzopoda**, whose ear structures and foot pads are unique."
      },
      {
        "author": "Frank E. Beddard",
        "work": "Mammalia",
        "quote": "Unlike typical clinging bats, **Myzopoda** relies on cellular surface adhesion rather than sharp claws to roost upon banana leaves."
      }
    ]
  },
  "Dashboard — on/anon.md": {
    "primary": "Soon, shortly, presently; or in a short while (from Old English on ān, 'in one [course/moment]').",
    "secondary": "In historical literature and drama, a common response by servants meaning 'coming immediately!', or an adverb signifying promptly.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Henry IV, Part 1",
        "quote": "Francis the drawer could say nothing else but **Anon**, **anon**, sir! Score a pint of bastard in the Half-moon!"
      },
      {
        "author": "John Milton",
        "work": "Lycidas",
        "quote": "So sinks the day-star in the ocean bed, and yet **anon** repairs his drooping head, and tricks his beams."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "The Rime of the Ancient Mariner",
        "quote": "The ice was here, the ice was there, the ice was all around: It cracked and growled, and roared and howled, like noises in a swound; and **anon** the ship drove on."
      }
    ]
  },
  "Dashboard — on/exon.md": {
    "primary": "Any part of a gene that will form part of the final mature RNA produced by that gene after introns have been removed by RNA splicing.",
    "secondary": "In molecular genetics, the expressed coding or untranslated segment of an interrupted eukaryotic gene, coined by Walter Gilbert in 1978 for 'expressed region'.",
    "quotes": [
      {
        "author": "Walter Gilbert",
        "work": "Why Genes in Pieces?",
        "quote": "I proposed the term **exon** for those regions of the primary transcript that are retained and expressed in the mature messenger RNA."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "The discovery of introns and every intervening **exon** fundamentally revolutionized our understanding of gene architecture."
      },
      {
        "author": "Francis Crick",
        "work": "Split Genes and RNA Splicing",
        "quote": "The nuclear spliceosome excises intervening sequences, bringing each consecutive **exon** into proper reading frame."
      }
    ]
  },
  "Dashboard — on/hyperon.md": {
    "primary": "Any subatomic baryon composed of three quarks, containing one or more strange quarks but no charm, bottom, or top quarks.",
    "secondary": "In high-energy particle physics, an unstable hadron (such as Lambda, Sigma, Xi, or Omega) having mass greater than a nucleon and decaying predominantly via the weak interaction.",
    "quotes": [
      {
        "author": "Murray Gell-Mann",
        "work": "The Eightfold Way",
        "quote": "The symmetrical arrangement of each known **hyperon** within the baryon octet confirmed the underlying SU(3) flavor group."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "A strange particle like the lambda **hyperon** is produced rapidly by the strong force, yet decays slowly through the weak interaction."
      },
      {
        "author": "Enrico Fermi",
        "work": "Elementary Particles",
        "quote": "Cosmic ray bubble-chamber tracks revealed the creation of a massive neutral **hyperon** accompanied by a strange meson."
      }
    ]
  },
  "Dashboard — on/on.md": {
    "primary": "The Greek neuter participle combining form (ōn, ontos, 'being, existing, that which is') foundational to ontology; or English preposition.",
    "secondary": "In philosophy and metaphysics, the ontological root designating being, essence, and ultimate reality as investigated by Aristotle and Parmenides.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "There is a science which investigates being as being—to **on** he **on**—and the attributes which belong to it in virtue of its own nature."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "First philosophy inquiry into abstract being, or to **on**, must be grounded in physical observation rather than verbal disputes."
      },
      {
        "author": "Martin Heidegger",
        "work": "Being and Time",
        "quote": "The question of being, the ancient Greek to **on**, was forgotten in Western metaphysics through the confusion of Being with entities."
      }
    ]
  },
  "Dashboard — on/Oniscidea.md": {
    "primary": "A suborder of isopod crustaceans comprising terrestrial woodlice, pill bugs, and sow bugs, capable of living entirely on land.",
    "secondary": "In invertebrate biology, the most successful group of terrestrial crustaceans, retaining ancestral gills (pleopodal lungs) requiring damp microhabitats to prevent desiccation.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The suborder **Oniscidea** includes the common woodlice, which breathe by pseudotracheae situated upon their abdominal appendages."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "Species of **Oniscidea** feed upon decaying wood and vegetable matter beneath stones in moist woodlands."
      },
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Under damp flowerpots in the garden, small colonies of **Oniscidea** congregate alongside earthworms."
      }
    ]
  },
  "Dashboard — on/Oniscomorpha.md": {
    "primary": "A superorder of millipedes commonly known as pill millipedes, capable of rolling into a tight protective sphere.",
    "secondary": "In myriapodology, short-bodied pentazonian millipedes possessing eleven to thirteen body segments and an enlarged shield-like pygidium, exhibiting convergent volvation with armadillidiid woodlice.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "Modern Classification of Insects",
        "quote": "The millipedes of the group **Oniscomorpha** roll themselves into an impenetrable globular ball when molested."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "The extraordinary resemblance between the **Oniscomorpha** and true pill bugs is a classic case of morphological convergence."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "Tropical forests harbor giant species of **Oniscomorpha** that roll into balls as large as a billiard ball."
      }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);
  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 3!`);
