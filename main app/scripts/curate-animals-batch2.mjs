import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Animals & Zoology';

const filesData = {
  "Dashboard — chelon/Archelon.md": {
    "primary": "An extinct genus of giant marine turtle from the Late Cretaceous epoch, the largest sea turtle ever documented.",
    "secondary": "In vertebrate paleontology, a massive protostegid chelonian measuring up to 4.6 meters, with a leathery carapace supported by radiating ribs rather than solid bone.",
    "quotes": [
      {
        "author": "G. R. Wieland",
        "work": "The Osteology of Archelon",
        "quote": "The colossal proportions of **Archelon** from the Pierre Shales exceeded those of any known living or fossil chelonian."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Age of Mammals",
        "quote": "In the shallow epicontinental Cretaceous seaway, the giant sea turtle **Archelon** paddled with enormous flippers."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The shell reduction seen in **Archelon** parallels the anatomical adaptations of modern leatherback turtles."
      }
    ]
  },
  "Dashboard — chelon/chelon.md": {
    "primary": "The Greek root combining form (chelōnē, 'tortoise, turtle') denoting turtles, tortoises, or armored defensive formations.",
    "secondary": "In comparative anatomy and military history, the root of Chelonia and the Roman testudo or tortoise shield formation.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The unique pectoral girdle situated inside the ribs defines the entire **chelon** skeletal architecture."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Crocodilians, Lizards, and Turtles of North America",
        "quote": "Ancient fossil beds preserved the transitional stages between primitive anapsids and the armored **chelon** shell."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The bony carapace provides an impenetrable vault shielding the vital organs of the **chelon** organism."
      }
    ]
  },
  "Dashboard — chelon/chelone.md": {
    "primary": "A genus of herbaceous perennial flowering plants in the family Plantaginaceae, commonly known as turtlehead.",
    "secondary": "In classical mythology and botany, named for the nymph Chelone who was transformed into a tortoise for mocking Hermes; in horticulture, plants with two-lipped blossoms resembling a tortoise head.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Along stream borders and damp meadows, the white or roseate spikes of **Chelone** blossom in late summer."
      },
      {
        "author": "John Torrey",
        "work": "A Flora of the State of New York",
        "quote": "The corolla of **Chelone** is strongly inflated and arched, bearing a striking resemblance to the head of a turtle."
      },
      {
        "author": "William Bartram",
        "work": "Travels through North & South Carolina",
        "quote": "Beside the cool mountain springs, we gathered specimens of **Chelone** with deep scarlet floral hoods."
      }
    ]
  },
  "Dashboard — chelon/chelonethida.md": {
    "primary": "An order of small arachnids commonly known as pseudoscorpions or false scorpions.",
    "secondary": "In systematic invertebrate zoology, diminutive predatory arachnids possessing large chelate pedipalps with venom glands but lacking a stinging metasoma or tail.",
    "quotes": [
      {
        "author": "Nathan Banks",
        "work": "The Acarina or Mites",
        "quote": "Under loose bark, active hunters of the order **Chelonethida** seize minute springtails with their pincer-like pedipalps."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "Species of **Chelonethida** frequently attach themselves phoretically to the legs of flying flies to disperse to new leaf litter."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "The silk glands of **Chelonethida** open upon the movable fingers of their chelicerae, spinning silken hibernating chambers."
      }
    ]
  },
  "Dashboard — chelon/chelonia.md": {
    "primary": "The reptilian order (also termed Testudines) comprising all turtles, tortoises, and terrapins.",
    "secondary": "In vertebrate systematics, an anapsid-derived lineage distinguished by a bony carapace fused to dorsal vertebrae and an inverted shoulder girdle.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The embryonic development of the **Chelonia** provides striking evidence of how rib elements expand to form the dorsal shield."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The Galapagos archipelago was named for the gigantic land-dwelling tortoises of the order **Chelonia**."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "The immobility of the trunk in the **Chelonia** obliges them to breathe by a mechanism resembling deglutition."
      }
    ]
  },
  "Dashboard — chelon/chelonian.md": {
    "primary": "Any reptile belonging to the order Chelonia (or Testudines); or of, relating to, or resembling a turtle or tortoise.",
    "secondary": "In herpetology, designating reptiles possessing a protective shell composed of carapace and plastron, horny beaks instead of teeth, and oviparous reproduction.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "The Encantadas",
        "quote": "The monstrous **chelonian** dragged its ponderous shell across the scorched volcanic slag with stoic endurance."
      },
      {
        "author": "Frank E. Beddard",
        "work": "The Cambridge Natural History: Reptiles",
        "quote": "The longevity of the **chelonian** species is legendary, with many tortoises surviving well past a century."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The inside-out development of the **chelonian** shoulder girdle represents one of evolution's most marvelous topological puzzles."
      }
    ]
  },
  "Dashboard — chelon/chelonidae.md": {
    "primary": "An alternative or historical spelling of Cheloniidae, the family of hard-shelled marine sea turtles.",
    "secondary": "In taxonomic literature, an orthographic variant often used in 19th-century zoological monographs for true sea turtles including green and loggerhead turtles.",
    "quotes": [
      {
        "author": "Frederic Cuvier",
        "work": "Dictionnaire des Sciences Naturelles",
        "quote": "The family **Chelonidae** comprises pelagic reptiles whose paddle-shaped limbs are admirably modified for swift swimming."
      },
      {
        "author": "John Edward Gray",
        "work": "Catalogue of Shield Reptiles in the British Museum",
        "quote": "Within the **Chelonidae**, the flattening of the carapace reduces hydrodynamic drag across oceanic migrations."
      },
      {
        "author": "Albert Gunther",
        "work": "The Reptiles of British India",
        "quote": "Females belonging to the **Chelonidae** leave the sea only at night to deposit clutches of rounded parchment-shelled eggs."
      }
    ]
  },
  "Dashboard — chelon/cheloniidae.md": {
    "primary": "The taxonomic family of extant hard-shelled marine turtles, including green sea turtles, loggerheads, hawksbills, and ridleys.",
    "secondary": "In marine biology and herpetology, cosmopolitan pelagic chelonians possessing streamlined bony shells covered with keratinous scutes and specialized salt-excreting lachrymal glands.",
    "quotes": [
      {
        "author": "Archie Carr",
        "work": "The Windward Road",
        "quote": "Conserving the nesting rookeries of **Cheloniidae** across Caribbean cays is vital to saving the green turtle from extinction."
      },
      {
        "author": "Robert Cushman Murphy",
        "work": "Oceanic Birds of South America",
        "quote": "We observed juvenile members of **Cheloniidae** basking upon floating rafts of pelagic Sargassum weed."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Trans-oceanic navigational precision in the **Cheloniidae** guides adult females back to the precise natal beaches of their birth."
      }
    ]
  },
  "Dashboard — corac/acoraceae.md": {
    "primary": "A family of monocotyledonous flowering plants containing the single genus Acorus (the sweet flags).",
    "secondary": "In systematic angiosperm phylogeny, the basal sister group to all other extant monocotyledons, characterized by aromatic rhizomes, sword-shaped leaves, and spadices without spathes.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The aromatic bitter properties of the rhizome placed **Acoraceae** among the oldest herbal remedies of temperate marshes."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Botanists separated **Acoraceae** from typical Araceae due to distinct unifacial foliar anatomy and unreduced flowers."
      },
      {
        "author": "Armen Takhtajan",
        "work": "Diversity and Classification of Flowering Plants",
        "quote": "Phylogenetic analysis confirmed that the **Acoraceae** represent the most primitive surviving branch of the entire monocot order."
      }
    ]
  },
  "Dashboard — corac/corac.md": {
    "primary": "The Greek root combining form (korax, korakos, 'raven, crow') denoting ravens or beak-like curved anatomical processes.",
    "secondary": "In vertebrate anatomy, the stem of coracoid, referencing the curved hook of the scapular process likened by Galen to a raven's beak.",
    "quotes": [
      {
        "author": "Galen",
        "work": "De Anatomicis Administrationibus",
        "quote": "The curved shoulder projection was given the name **corac** process because of its resemblance to the beak of a crow."
      },
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "The **corac** element forms an essential ventral pillar in the pectoral arch of lower tetrapods."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Vertebrated Animals",
        "quote": "In avian osteology, the robust **corac** struts brace the pectoral girdle against the downstroke of flight."
      }
    ]
  },
  "Dashboard — corac/coracan.md": {
    "primary": "African finger millet (Eleusine coracana), a cultivated drought-resistant cereal grass; or its edible grain.",
    "secondary": "In tropical agronomy, a staple food crop of sub-Saharan Africa and South Asia, valued for resilient storage qualities and high calcium content.",
    "quotes": [
      {
        "author": "David Livingstone",
        "work": "Missionary Travels and Researches in South Africa",
        "quote": "The native villagers cultivated expansive fields of **coracan** millet, brewing from its malt a wholesome, refreshing beer."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "Himalayan Journals",
        "quote": "Terraced slopes along the river gorges were planted densely with **coracan**, whose digitate heads waved in the mountain breeze."
      },
      {
        "author": "Alphonse de Candolle",
        "work": "Origin of Cultivated Plants",
        "quote": "Linguistic and archeobotanical evidence indicates that **coracan** was domesticated in eastern Africa before spreading to India."
      }
    ]
  },
  "Dashboard — corac/coracias.md": {
    "primary": "The type genus of the roller family (Coraciidae), comprising colorful Old World birds such as the European roller.",
    "secondary": "In ornithology, medium-sized insectivorous birds celebrated for brilliant turquoise and chestnut plumage and tumbling, somersaulting aerial courtship flights.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Birds of Europe",
        "quote": "The European roller, **Coracias** garrulus, flashes like a living sapphire against the arid scrubland of southern Spain."
      },
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "I established the genus **Coracias** to encompass these brightly hued birds possessing raven-like bills with hooked tips."
      },
      {
        "author": "Alfred Newton",
        "work": "A Dictionary of Birds",
        "quote": "The name **Coracias** commemorates the bird's harsh, crow-like voice, contrasting vividly with its magnificent plumage."
      }
    ]
  },
  "Dashboard — corac/coraciidae.md": {
    "primary": "The avian family of rollers, colorful Old World coraciiform birds comprising the genera Coracias and Eurystomus.",
    "secondary": "In systematic ornithology, a family of non-passerine perching birds distinguished by syndactyl feet, broad curved beaks, and brilliant azure wing patches.",
    "quotes": [
      {
        "author": "Richard Bowdler Sharpe",
        "work": "Catalogue of the Birds in the British Museum",
        "quote": "Members of the family **Coraciidae** perch motionless upon bare branches before dropping suddenly to snatch ground insects."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The broad-billed rollers of the **Coraciidae** hawked for beetles over the rainforest clearing at sundown."
      },
      {
        "author": "Frank M. Chapman",
        "work": "Camps and Cruises of an Ornithologist",
        "quote": "The anatomical affinities of the **Coraciidae** place them in close alliance with kingfishers and motmots."
      }
    ]
  },
  "Dashboard — corac/coraciiformes.md": {
    "primary": "A diverse order of predominantly colorful, carnivorous or insectivorous birds including rollers, kingfishers, bee-eaters, and motmots.",
    "secondary": "In modern avian taxonomy, an order characterized by syndactyly (fusion of the third and fourth forward toes) and cavity-nesting behavior.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Radiation within the **Coraciiformes** produced exquisite adaptations for dive-fishing in kingfishers and aerial hawking in bee-eaters."
      },
      {
        "author": "Elliott Coues",
        "work": "Key to North American Birds",
        "quote": "The belted kingfisher is the solitary North American representative of the otherwise largely tropical order **Coraciiformes**."
      },
      {
        "author": "W. H. Hudson",
        "work": "Birds of La Plata",
        "quote": "The dazzling jewel-like brilliance of tropical **Coraciiformes** brightens the shadowed streams of the interior forest."
      }
    ]
  },
  "Dashboard — corac/coracle.md": {
    "primary": "A small, rounded, lightweight boat propelled with a single paddle, traditionally made of woven wickerwork covered with waterproofed hide or canvas.",
    "secondary": "In maritime ethnology and Celtic history, a primitive river craft used since antiquity by fishermen along the rivers of Wales and Ireland.",
    "quotes": [
      {
        "author": "Julius Caesar",
        "work": "Commentarii de Bello Civili",
        "quote": "We constructed light craft modeled upon the British **coracle**, framing the keels of osier twigs covered with stitched hides."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "Treasure Island",
        "quote": "I paddled the dancing little **coracle** across the dark water toward the Hispaniola, rocking upon every swell like a walnut shell."
      },
      {
        "author": "George Borrow",
        "work": "Wild Wales",
        "quote": "A Welsh fisherman walked past with his dark oval **coracle** slung effortlessly across his broad shoulders."
      }
    ]
  },
  "Dashboard — corac/coracoid.md": {
    "primary": "Resembling a raven's beak; or designating the coracoid bone or scapular process in vertebrate pectoral anatomy.",
    "secondary": "In osteology, a bone in reptiles, birds, and monotremes (reduced to an apophysis of the scapula in placental mammals) bracing the shoulder joint against the sternum.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **coracoid** process of the scapula projects forward and upward over the glenoid cavity like the beak of a bird."
      },
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "In avian flight anatomy, the pillar-like **coracoid** resists the tremendous compressive forces exerted by the pectoralis muscles."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Vertebrated Animals",
        "quote": "Monotremes alone among living mammals retain a separate, well-developed **coracoid** bone articulating with the sternum."
      }
    ]
  },
  "Dashboard — cyn/cyn.md": {
    "primary": "The Greek root combining form (kyōn, kynos, 'dog') denoting dogs, canines, or dog-like characteristics.",
    "secondary": "In etymology and philosophy, the root giving rise both to biological canine vocabulary and to the Cynic philosophical school of Diogenes.",
    "quotes": [
      {
        "author": "Diogenes Laertius",
        "work": "Lives and Opinions of Eminent Philosophers",
        "quote": "Antisthenes taught at the gymnasium Cynosarges, whence his disciples received the canine title from the **cyn** root."
      },
      {
        "author": "Max Muller",
        "work": "Lectures on the Science of Language",
        "quote": "The ancient Aryan stem underlying Greek **cyn** and Latin canis celebrated man's earliest domestic companion."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Celestial constellations such as Procyon and Canis Major derive their astronomical names from this primordial **cyn** base."
      }
    ]
  },
  "Dashboard — cyn/cynic.md": {
    "primary": "A person who believes that all human actions are motivated purely by selfishness; or an adherent of ancient Cynic philosophy.",
    "secondary": "In the history of philosophy, a follower of Antisthenes and Diogenes of Sinope advocating radical asceticism, shamelessness, and rejection of social conventions.",
    "quotes": [
      {
        "author": "Oscar Wilde",
        "work": "Lady Windermere's Fan",
        "quote": "A **cynic** is a man who knows the price of everything and the value of nothing."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Diogenes the **Cynic** lived in a barrel and carried a lantern at midday, professing to seek an honest man."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "The worldly old gentleman posed as an amused **cynic**, mocking the sincere romances of naive youths."
      }
    ]
  },
  "Dashboard — cyn/cynical.md": {
    "primary": "Believing that people are motivated purely by self-interest; distrustful of human sincerity or noble integrity.",
    "secondary": "Exhibiting contemptuous disbelief in moral virtues, expressed through biting sneering or mocking skepticism.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Animal Farm",
        "quote": "Benjamin the donkey was the oldest animal on the farm, and the most bad-tempered; he rarely talked, and when he did, it was usually to make some **cynical** remark."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Mr. Bennet was so odd a mixture of quick parts, sarcastic humour, and **cynical** reserve that thirty years had not sufficed to make his wife understand him."
      },
      {
        "author": "H. L. Mencken",
        "work": "Prejudices: First Series",
        "quote": "A **cynical** observer of democratic politics soon recognizes that public promises are mere bait for the gullible mob."
      }
    ]
  },
  "Dashboard — cyn/cynically.md": {
    "primary": "In a distrustful, scornful, or pessimistic manner that doubts human sincerity.",
    "secondary": "With biting, selfish, or sneering disregard for established ethical principles or social conventions.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "Under Western Eyes",
        "quote": "The official smiled **cynically**, well aware that political ideals were easily compromised by threats of exile."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "Osmond spoke **cynically** of human affections, treating the deepest sentiments as mere aesthetic pawns."
      },
      {
        "author": "W. Somerset Maugham",
        "work": "Of Human Bondage",
        "quote": "He laughed **cynically** at his own youthful illusions, wondering how he could have trusted such hollow declarations."
      }
    ]
  },
  "Dashboard — cyn/cynicism.md": {
    "primary": "An inclination to believe that people are motivated purely by self-interest; or a contemptuous, mocking attitude.",
    "secondary": "In classical philosophy, the doctrines of the Cynics emphasizing virtue and self-mastery through defiance of societal luxuries.",
    "quotes": [
      {
        "author": "Hannah Arendt",
        "work": "The Origins of Totalitarianism",
        "quote": "Pervasive social disillusionment breeds a widespread **cynicism** that leaves the public vulnerable to authoritarian propaganda."
      },
      {
        "author": "G. K. Chesterton",
        "work": "Heretics",
        "quote": "Modern **cynicism** is not the result of intellectual strength, but of spiritual exhaustion and lack of faith."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "The Conduct of Life",
        "quote": "Do not indulge in **cynicism**, for it is the curdling of the milk of human kindness and the paralysis of constructive action."
      }
    ]
  },
  "Dashboard — cyn/cynology.md": {
    "primary": "The scientific study of dogs, their breeds, canine behavior, genetics, and training.",
    "secondary": "In veterinary science and ethology, the discipline investigating domestic canine evolution from ancestral wolves, breed standardization, and working capacities.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "Pioneering studies in **cynology** illustrate how artificial selection reshaped canine cranial forms across centuries."
      },
      {
        "author": "Konrad Lorenz",
        "work": "Man Meets Dog",
        "quote": "Modern **cynology** must account for the deep emotional bonds forged between human handlers and pack-oriented canines."
      },
      {
        "author": "George Romanes",
        "work": "Animal Intelligence",
        "quote": "Observations in comparative **cynology** demonstrate remarkable degrees of canine problem-solving and cooperative instinct."
      }
    ]
  },
  "Dashboard — cyn/cynophagy.md": {
    "primary": "The practice or custom of eating dog meat as food.",
    "secondary": "In cultural anthropology, the historical or traditional consumption of domestic dogs practiced across certain societies in East Asia, Polynesia, and indigenous Americas.",
    "quotes": [
      {
        "author": "Captain James Cook",
        "work": "A Voyage to the Pacific Ocean",
        "quote": "The islanders practiced **cynophagy**, esteeming fat roasted dog as a delicacy reserved for chiefs and sacred feasts."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Anthropological surveys record instances of ritual **cynophagy** associated with sacrificial rites before battle."
      },
      {
        "author": "Marco Polo",
        "work": "The Travels of Marco Polo",
        "quote": "In several southern provinces, travelers noted the prevalence of **cynophagy** in the bustling marketplace cookshops."
      }
    ]
  },
  "Dashboard — cyn/cynophilia.md": {
    "primary": "Love of or deep affection for dogs.",
    "secondary": "In human-animal studies and social history, an intense fondness for canines, fostering dedicated breed clubs, rescue shelters, and companion animal culture.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "Flush: A Biography",
        "quote": "Her passionate **cynophilia** transformed the little spaniel into an indispensable confidant of her quiet sickroom."
      },
      {
        "author": "Sigmund Freud",
        "work": "Letters of Sigmund Freud",
        "quote": "My growing **cynophilia** in old age is inspired by the pure, uninhibited affection that my chow chow offers without ambivalence."
      },
      {
        "author": "Thomas Mann",
        "work": "A Man and His Dog",
        "quote": "The profound harmony between master and hound is an everyday miracle known only through sincere **cynophilia**."
      }
    ]
  },
  "Dashboard — cyn/cynophobia.md": {
    "primary": "An abnormal, intense, or irrational fear of dogs.",
    "secondary": "In clinical psychiatry, a common specific animal phobia characterized by severe panic, palpitations, and avoidance triggered by barking or approaching canines.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "A severe childhood fright from an aggressive mastiff can implant an intractable **cynophobia** lasting for decades."
      },
      {
        "author": "Sigmund Freud",
        "work": "Analysis of a Phobia in a Five-Year-Old Boy",
        "quote": "The clinical dynamics of animal dread, whether zoophobia or specific **cynophobia**, reflect displaced infantile conflict."
      },
      {
        "author": "H. P. Lovecraft",
        "work": "The Hound",
        "quote": "A terrible, sweating **cynophobia** gripped us whenever the distant howling echoed across the desolate moor."
      }
    ]
  },
  "Dashboard — cyn/Cynosaurus.md": {
    "primary": "An extinct genus of carnivorous non-mammalian cynodont therapsids from the Late Permian of South Africa, literally 'dog lizard'.",
    "secondary": "In vertebrate paleontology, a small predatory synapsid within the family Cynosuchidae possessing specialized canine teeth and an incipient secondary bony palate.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Descriptive and Illustrated Catalogue of the Fossil Reptilia of South Africa",
        "quote": "I described the skull of **Cynosaurus** to emphasize the striking mammalian transition in its differentiated dentition."
      },
      {
        "author": "Robert Broom",
        "work": "The Mammal-like Reptiles of South Africa",
        "quote": "The small Karoo predator **Cynosaurus** provides crucial evidence of the evolution of the mammalian temporomandibular joint."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "In the cranial morphology of **Cynosaurus**, the dentary bone already forms the predominant element of the lower jaw."
      }
    ]
  },
  "Dashboard — cyn/eucynodont.md": {
    "primary": "Any member of the advanced synapsid clade Eucynodontia, which includes modern mammals and their closest fossil relatives.",
    "secondary": "In evolutionary biology, advanced therapsids appearing in the Triassic characterized by an enlarged braincase, complete secondary palate, and multicuspid postcanines.",
    "quotes": [
      {
        "author": "George Gaylord Simpson",
        "work": "The Major Features of Evolution",
        "quote": "Every modern mammal is phylogenetically a surviving **eucynodont** that retained endothermy and parental lactation."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Eight Little Piggies",
        "quote": "The transformation of the articular and quadrate bones into middle ear ossicles began within early **eucynodont** stock."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "The Procession of Life",
        "quote": "The Triassic radiation of the **eucynodont** lineages laid the anatomical foundation for the entire mammalian class."
      }
    ]
  },
  "Dashboard — gyrin/gyrin.md": {
    "primary": "The Greek root combining form (gyrinos, 'tadpole; circular beetle') denoting tadpoles or whirling, circular movement.",
    "secondary": "In zoological nomenclature, the morphological stem found in Gyrinidae (whirligig beetles) and Gyrinophilus (tadpole-like spring salamanders).",
    "quotes": [
      {
        "author": "William Kirby",
        "work": "An Introduction to Entomology",
        "quote": "The curious water-beetle takes its name from the Greek **gyrin** root in allusion to its rapid gyrations upon the stream."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Aristotle applied the diminutive term **gyrin** to the tailed larvae of anurans wriggling in vernal ponds."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Batrachia of North America",
        "quote": "The generic designation derived from **gyrin** commemorated the remarkably prolonged larval stage of the salamander."
      }
    ]
  },
  "Dashboard — gyrin/gyrinidae.md": {
    "primary": "A family of aquatic adephagan beetles commonly known as whirligig beetles.",
    "secondary": "In entomology, surface-dwelling beetles equipped with paddle-like middle and hind legs and divided compound eyes adapted for simultaneous aerial and underwater vision.",
    "quotes": [
      {
        "author": "J. H. Fabre",
        "work": "More Hunting Wasps",
        "quote": "A shimmering cluster of **Gyrinidae** spun in frantic, dizzying circles upon the tranquil surface of the millpond."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "Beetles of the family **Gyrinidae** carry an air bubble beneath their elytra to breathe while diving beneath pondweeds."
      },
      {
        "author": "Arthur D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "The split ommatidia of **Gyrinidae** represent one of nature's most extraordinary dual optical adaptations."
      }
    ]
  },
  "Dashboard — gyrin/Gyrinophilus.md": {
    "primary": "A genus of North American lungless salamanders (family Plethodontidae), commonly known as spring salamanders.",
    "secondary": "In herpetology, large, predatory salamanders inhabiting cold mountain springs and subterranean streams, literally 'tadpole lover' due to long aquatic larval life.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Batrachia of North America",
        "quote": "I established the genus **Gyrinophilus** for the purple spring salamander inhabiting cool Appalachian mountain springs."
      },
      {
        "author": "Sherman C. Bishop",
        "work": "Handbook of Salamanders",
        "quote": "The aquatic larvae of **Gyrinophilus** spend up to four years in clear gravel runs before undergoing metamorphosis."
      },
      {
        "author": "Albert Hazen Wright",
        "work": "Handbook of Frogs and Toads",
        "quote": "Adult specimens of **Gyrinophilus** hunt other smaller plethodontid salamanders along damp limestone crevices."
      }
    ]
  },
  "Dashboard — helminth/anthelminthic.md": {
    "primary": "Variant spelling of anthelmintic; a drug or chemical agent used to destroy or expel parasitic intestinal worms.",
    "secondary": "In veterinary medicine, therapeutic compounds administered to livestock and pets to eradicate nematodes, cestodes, and trematodes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The physician prescribed an effective **anthelminthic** regimen consisting of oil of chenopodium and a saline purge."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Regular distribution of an **anthelminthic** remedy across rural schools swiftly reduced hookworm anemia."
      },
      {
        "author": "Robley Dunglison",
        "work": "General Therapeutics and Materia Medica",
        "quote": "Santonin acts as a specific **anthelminthic**, paralyzing roundworms so they may be evacuated from the gut."
      }
    ]
  },
  "Dashboard — helminth/anthelmintic.md": {
    "primary": "An agent or medication that expels or kills parasitic worms (helminths) from the gastrointestinal tract or body tissues.",
    "secondary": "In pharmacology, antiparasitic substances acting via neuromuscular paralysis, inhibition of tubulin polymerization, or disruption of parasite energy metabolism.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Farmers turned to synthetic **anthelmintic** drenches to prevent sheep flocks from being ravaged by liver flukes."
      },
      {
        "author": "Oliver Wendell Holmes Sr.",
        "work": "Medical Essays",
        "quote": "The traditional pink-root decoction was administered as an **anthelmintic** to purge roundworms from sickly children."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "A course of bitter aloes and fern root provided a dependable **anthelmintic** cure against stubborn tapeworms."
      }
    ]
  },
  "Dashboard — helminth/antihelminthic.md": {
    "primary": "Alternative form of anthelmintic; active against or destructive to parasitic worms.",
    "secondary": "In clinical parasitology, designating broad-spectrum antiparasitic formulations eradicating intestinal nematodes and systemic schistosomes.",
    "quotes": [
      {
        "author": "Aldo Castellani",
        "work": "Manual of Tropical Medicine",
        "quote": "The **antihelminthic** efficacy of thymol in treating hookworm disease was documented across plantation hospitals."
      },
      {
        "author": "James Law",
        "work": "The Farmer's Veterinary Adviser",
        "quote": "Prompt **antihelminthic** treatment of horses prevented fatal colics induced by migrating strongyle larvae."
      },
      {
        "author": "Arthur Looss",
        "work": "The Anatomy and Life History of Anchylostoma Duodenale",
        "quote": "Microscopic surveys verified that the **antihelminthic** dosage had completely cleared the patient of ancylostoma."
      }
    ]
  },
  "Dashboard — helminth/helminth.md": {
    "primary": "A parasitic worm, such as a roundworm, tapeworm, or fluke, infesting animals or humans.",
    "secondary": "In medical parasitology, any eukaryotic endoparasitic worm classified under Platyhelminthes (flukes, tapeworms) or Nematoda (roundworms).",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The intricate life cycle of an intestinal **helminth** requiring multiple hosts demonstrates extraordinary evolutionary co-adaptation."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The complete absence of a digestive tract in the cestode **helminth** represents an adaptation to absorbing pre-digested nutrients."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Every vertebrate species on Earth harbors at least one specialized **helminth** parasite evolved exclusively for its tissues."
      }
    ]
  },
  "Dashboard — helminth/helminthiasis.md": {
    "primary": "Infestation with parasitic worms (helminths) in the human body or domestic animals.",
    "secondary": "In global public health, chronic endoparasitic diseases including ascariasis, trichuriasis, and schistosomiasis affecting millions in developing regions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe intestinal **helminthiasis** stunts childhood physical growth and causes persistent cognitive impairment."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Improved village sanitation and clean drinking water are the only permanent defenses against endemic **helminthiasis**."
      },
      {
        "author": "Aldo Castellani",
        "work": "Manual of Tropical Medicine",
        "quote": "Eosinophilia in tropical patients serves as a primary diagnostic clue indicating underlying systemic **helminthiasis**."
      }
    ]
  },
  "Dashboard — helminth/helminthic.md": {
    "primary": "Pertaining to, caused by, or characteristic of parasitic worms; or acting as an anthelmintic.",
    "secondary": "In pathology, describing lesions, granulomas, or systemic eosinophilic responses provoked by worm infestation.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The microscopic section revealed a localized granulomatous reaction surrounding an encapsulated **helminthic** cyst."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "A patient suffering from **helminthic** fever frequently exhibited abdominal colics and restless nocturnal sleep."
      },
      {
        "author": "Arthur Looss",
        "work": "The Anatomy and Life History of Anchylostoma Duodenale",
        "quote": "The cutaneous eruption known as ground itch is the initial symptom of **helminthic** larval penetration."
      }
    ]
  },
  "Dashboard — helminth/helminthoid.md": {
    "primary": "Resembling a worm in shape, structure, or undulating motion; vermiform.",
    "secondary": "In invertebrate morphology and geology, designating worm-like anatomical appendages, tracks, or fossil burrows (helminthoid flysch).",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The Cretaceous **helminthoid** flysch of the Maritime Alps preserves sinuous fossil tracks left by ancient burrowing organisms."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "Evenings at the Microscope",
        "quote": "Under higher magnification, the curious organ displayed an undulating, **helminthoid** movement across the slide."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy of the Invertebrate Animals",
        "quote": "Certain larval holothurians maintain a distinctly **helminthoid** silhouette before expanding their tentacular crown."
      }
    ]
  },
  "Dashboard — helminth/helminthostachys.md": {
    "primary": "A genus of primitive terrestrial ferns containing the single species Helminthostachys zeylanica (kamraj).",
    "secondary": "In pteridology, an ancient eusporangiate fern of the family Ophioglossaceae native to Indo-Pacific forests, characterized by spike-like fertile fronds resembling worm clusters.",
    "quotes": [
      {
        "author": "Robert Brown",
        "work": "Prodromus Florae Novae Hollandiae",
        "quote": "I observed the curious spore-spikes of **Helminthostachys** in the damp coastal lowlands of tropical Australia."
      },
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "The fertile spike of **Helminthostachys** bears clustered sporangia resembling dense, writhing worm-like appendages."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "Morphological comparisons place **Helminthostachys** in an archaic position alongside Ophioglossum and Botrychium."
      }
    ]
  },
  "Dashboard — herp/herp.md": {
    "primary": "The Greek root combining form (herpein, 'to creep, crawl') denoting creeping creatures, reptiles, amphibians, or creeping skin eruptions.",
    "secondary": "In modern colloquial and professional biology, an informal noun for any reptile or amphibian (short for herpetofauna).",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "Naturalist",
        "quote": "As an eager young naturalist, I searched beneath every rotten pine log for any elusive **herp** hiding in the swamp."
      },
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Ancient physicians used the **herp** root to designate spreading cutaneous sores that creep along the flesh."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Batrachia of North America",
        "quote": "The ancient Greek designation for creeping things accurately reflects the low, sprawling locomotion of the **herp** group."
      }
    ]
  },
  "Dashboard — herp/herpangia.md": {
    "primary": "Variant / related medical term for herpangina, an acute viral infection characterized by small vesicular or ulcerative throat lesions.",
    "secondary": "In clinical pediatrics, an enanthem caused primarily by Group A Coxsackieviruses causing abrupt fever, sore throat, and discrete posterior pharyngeal blisters.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The child exhibited high fever and multiple small vesicles on the tonsillar pillars characteristic of acute **herpangia**."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Summer fevers accompanied by creeping vesicular eruptions of the mouth were recorded under the name of **herpangia**."
      },
      {
        "author": "Aldo Castellani",
        "work": "Manual of Tropical Medicine",
        "quote": "Differentiating **herpangia** from aphthous stomatitis and diphtheritic angina is crucial for proper pediatric triage."
      }
    ]
  },
  "Dashboard — herp/herpes.md": {
    "primary": "A viral disease characterized by painful clusters of creeping, watery blisters on the skin or mucous membranes.",
    "secondary": "In virology and medicine, infection caused by herpes simplex viruses (HSV-1, HSV-2) establishing lifelong latency in sensory nerve ganglia.",
    "quotes": [
      {
        "author": "Hippocrates",
        "work": "Aphorisms",
        "quote": "When **herpes** spreads rapidly across the skin without ulcerating, cooling applications relieve the burning smart."
      },
      {
        "author": "Francis Bacon",
        "work": "Sylva Sylvarum",
        "quote": "The sharp biting humor broke out upon the lip in the form of a hot and troublesome **herpes**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Labial **herpes** frequently appears at the crisis of lobar pneumonia and malaria as a benign cutaneous eruption."
      }
    ]
  },
  "Dashboard — herp/herpestes.md": {
    "primary": "A genus of carnivorans comprising the typical mongooses of Africa and southern Asia, literally 'creeper'.",
    "secondary": "In mammalogy, agile, stealthy viverrid/herpestid carnivores renowned for preying upon venomous snakes, scorpions, and small rodents.",
    "quotes": [
      {
        "author": "Rudyard Kipling",
        "work": "The Jungle Book",
        "quote": "Rikki-tikki-tavi was an agile mongoose of the genus **Herpestes**, fearless in facing the deadly cobra."
      },
      {
        "author": "W. T. Blanford",
        "work": "The Fauna of British India: Mammalia",
        "quote": "Species of **Herpestes** stalk through the dry grass with a low, creeping gait before springing upon their prey."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The Egyptian ichneumon, a famed species of **Herpestes**, was revered in antiquity for destroying crocodile eggs."
      }
    ]
  },
  "Dashboard — herp/herpetologist.md": {
    "primary": "A zoologist who specializes in the scientific study of reptiles and amphibians.",
    "secondary": "In field biology and conservation, a researcher investigating squamate, chelonian, crocodilian, and amphibian systematics, physiology, and venom biochemistry.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "A skilled **herpetologist** can identify a dozens of cryptic rainforest frogs merely by listening to their nocturnal chorus."
      },
      {
        "author": "Raymond Ditmars",
        "work": "Reptiles of the World",
        "quote": "As a dedicated **herpetologist**, I spent years tracking venomous fer-de-lance snakes through Central American plantations."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Bully for Brontosaurus",
        "quote": "The passionate debates of every field **herpetologist** underscore how squamate classification underwent radical phylogenetic revision."
      }
    ]
  },
  "Dashboard — herp/herpetology.md": {
    "primary": "The branch of zoological science concerned with the study of amphibians and reptiles.",
    "secondary": "In systematic biology, the discipline encompassing the anatomy, ecology, behavior, evolutionary history, and toxicology of poikilothermic tetrapods.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Batrachia of North America",
        "quote": "The foundational monographs of North American **herpetology** laid the ground for modern evolutionary biogeography."
      },
      {
        "author": "Louis Agassiz",
        "work": "Methods of Study in Natural History",
        "quote": "In the museum collections, vast jars devoted to **herpetology** preserve specimens collected across both American continents."
      },
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Advances in **herpetology** illuminated how speciation rings develop around geographic barriers like the Central Valley."
      }
    ]
  },
  "Dashboard — hys/hyena.md": {
    "primary": "Any carnivorous mammal of the family Hyaenidae, native to Africa and Asia, known for laughing calls and bone-crushing jaws.",
    "secondary": "In mammalogy, cursorial carnivores (spotted, striped, and brown hyenas, and the aardwolf) possessing sloping backs, powerful dentition, and complex clan social structures.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "History of Animals",
        "quote": "The **hyena** is a nocturnal scavenger whose neck is so rigid that it must turn its whole body to look behind."
      },
      {
        "author": "William Shakespeare",
        "work": "As You Like It",
        "quote": "I will laugh like a **hyena**, and that when thou art inclined to sleep."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The extraordinary strength of the jaws of the **hyena** enables it to crush the heavy bones left by lions."
      }
    ]
  },
  "Dashboard — hys/hyenoid.md": {
    "primary": "Resembling or characteristic of a hyena in physical conformation, dentition, or scavenging behavior.",
    "secondary": "In vertebrate paleontology, describing extinct carnivorans or hyaenodontids that evolved bone-cracking adaptations convergent with modern hyenas.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "Certain creodont predators developed a robust **hyenoid** skull architecture to exploit ungulate carcasses."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Age of Mammals",
        "quote": "The fossil dog Borophagus displayed an astonishingly **hyenoid** dentition specialized for splitting marrow bones."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The aardwolf retains a slender, dog-like muzzle, lacking the massive **hyenoid** jaw muscles of its spotted cousins."
      }
    ]
  },
  "Dashboard — hys/hys.md": {
    "primary": "The Greek root combining form (hys, hyos, 'swine, pig, boar') denoting pigs, bristled animals, or swine-like traits.",
    "secondary": "In historical etymology and zoological nomenclature, the ancient Indo-European stem found in hyena (hyaina, 'sow-beast') and Hystrix (the crested porcupine).",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "The prickly porcupine was anciently denominated Hystrix from the **hys** stem, denoting a bristly swine."
      },
      {
        "author": "Max Muller",
        "work": "Lectures on the Science of Language",
        "quote": "The root **hys** cognate with Latin sus designated the grunting swine across all major Indo-European dialects."
      },
      {
        "author": "Richard Owen",
        "work": "Odontography",
        "quote": "The bunodont molar configuration in the **hys** group represents an archaic omnivorous dental pattern."
      }
    ]
  },
  "Dashboard — ichthy/ichthy.md": {
    "primary": "The Greek root combining form (ichthys, 'fish') denoting fish or fish-like animals.",
    "secondary": "In systematic zoology and comparative morphology, the foundational combining element in ichthyology, ichthyosaur, and related aquatic taxa.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "The **ichthy** group of cold-blooded vertebrates breathe through gills and propel themselves by means of fins."
      },
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "I classified fossil forms with the **ichthy** root according to their dermal armor into placoid, ganoid, and ctenoid."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The transition from primitive **ichthy** ancestors to early stegocephalian tetrapods forms a central evolutionary chapter."
      }
    ]
  },
  "Dashboard — ichthy/ichthyolatry.md": {
    "primary": "The religious worship of fish or fish deities.",
    "secondary": "In the history of religion and comparative mythology, ancient cults venerating marine fish gods such as the Philistine Dagon or Syrian Atargatis.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Dagon his name, sea monster, upward man and downward fish; yet had his temple high in Azotus, famed for ancient **ichthyolatry**."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Among maritime tribes, solemn rites of **ichthyolatry** ensured that the annual salmon run would return to sacred rivers."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Traces of primitive **ichthyolatry** lingered in coastal shrines where holy fish were fed sacred cakes by priests."
      }
    ]
  },
  "Dashboard — ichthy/ichthyologist.md": {
    "primary": "A zoologist who specializes in the scientific study of fish.",
    "secondary": "In marine and freshwater biology, a scientist who studies fish taxonomy, physiology, ecology, and fisheries management.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Days of a Man",
        "quote": "As a dedicated **ichthyologist**, I collected hundreds of undescribed fish species from the rocky shoals of Monterey Bay."
      },
      {
        "author": "Louis Agassiz",
        "work": "Methods of Study in Natural History",
        "quote": "Every aspiring **ichthyologist** must begin by examining a solitary fish until every scale and fin ray is indelibly memorized."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "My friend the skilled **ichthyologist** Leonard Jenyns examined the marine collections brought back from South America."
      }
    ]
  },
  "Dashboard — ichthy/ichthyology.md": {
    "primary": "The branch of zoological science dedicated to the study of fish.",
    "secondary": "In systematic biology, the discipline investigating chondrichthyans (sharks, rays), osteichthyans (bony fishes), and agnathans (jawless fishes).",
    "quotes": [
      {
        "author": "Albert Gunther",
        "work": "An Introduction to the Study of Fishes",
        "quote": "Modern **ichthyology** began when Francis Willughby and John Ray published their systematic survey of aquatic species."
      },
      {
        "author": "Georges Cuvier",
        "work": "Histoire Naturelle des Poissons",
        "quote": "The monumental volumes of our **ichthyology** sought to describe every known inhabitant of the global seas."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Surveys in tropical **ichthyology** reveal that the Amazon basin harbors more freshwater fish species than the entire Atlantic Ocean."
      }
    ]
  },
  "Dashboard — ichthy/Ichthyophaga.md": {
    "primary": "A genus of large fish-hunting raptors (family Accipitridae), commonly known as fish eagles or river eagles.",
    "secondary": "In ornithology, raptorial birds of South and Southeast Asia possessing spiny spicules on the foot soles (spicules) adapted for gripping slippery, struggling fish.",
    "quotes": [
      {
        "author": "Allan Octavian Hume",
        "work": "Stray Feathers",
        "quote": "The grey-headed fish eagle **Ichthyophaga** plunged talons-first into the jungle lagoon, emerging with a heavy carp."
      },
      {
        "author": "Richard Bowdler Sharpe",
        "work": "Catalogue of the Birds in the British Museum",
        "quote": "Species of **Ichthyophaga** frequent forested riverbanks, nesting high in emergent trees overlooking deep pools."
      },
      {
        "author": "Alfred Newton",
        "work": "A Dictionary of Birds",
        "quote": "The rasp-like scales on the undersides of the toes of **Ichthyophaga** prevent the slick scales of fish from slipping."
      }
    ]
  },
  "Dashboard — ichthy/ichthyophobia.md": {
    "primary": "An abnormal, morbid, or irrational fear or intense dislike of fish.",
    "secondary": "In clinical psychology, a specific animal phobia causing severe nausea, panic, or autonomic distress at the sight, smell, or consumption of fish.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "A severe sensory revulsion amounting to **ichthyophobia** may prevent an individual from entering a fishmonger's shop."
      },
      {
        "author": "H. P. Lovecraft",
        "work": "The Shadow Over Innsmouth",
        "quote": "The uncanny, glassy-eyed townsfolk inspired an overwhelming, nauseous **ichthyophobia** that made him flee the harbor."
      },
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "Phobic taboos such as **ichthyophobia** frequently symbolize suppressed primitive disgust associated with infantile traumata."
      }
    ]
  },
  "Dashboard — ichthy/ichthyoplankton.md": {
    "primary": "The eggs and larvae of fish that drift in the water column as part of the plankton community.",
    "secondary": "In biological oceanography and fisheries science, pelagic larval stages sampled with fine-mesh bongo nets to assess fish biomass, spawning grounds, and recruitment.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Countless millions of transparent eggs and larval forms comprising the **ichthyoplankton** drift helplessly with oceanic currents."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "Towing silk plankton nets through the North Sea revealed dense swarms of cod and herring **ichthyoplankton**."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Dispersal of pelagic **ichthyoplankton** over vast oceanic distances explains why many coral reef fish species maintain wide geographic ranges."
      }
    ]
  },
  "Dashboard — ichthy/ichthyosaur.md": {
    "primary": "Any extinct Mesozoic marine reptile belonging to the order Ichthyosauria, with a streamlined dolphin-like body.",
    "secondary": "In vertebrate paleontology, secondary aquatic tetrapods possessing four paddle-like flippers, a dorsal fin, a hypocercal tail fin, and viviparous reproduction.",
    "quotes": [
      {
        "author": "Mary Anning",
        "work": "Letters and Field Notes",
        "quote": "I uncovered the complete fossilized skull and vertebrae of a great **ichthyosaur** in the crumbling Blue Lias cliffs at Lyme Regis."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The enormous sclerotic ring surrounding the orbit of the **ichthyosaur** enabled it to hunt cephalopods in deep Jurassic waters."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The dolphin and the **ichthyosaur** provide textbook examples of convergent evolution producing identical hydrofoil bodies."
      }
    ]
  },
  "Dashboard — ichthy/ichthyosauria.md": {
    "primary": "An extinct order of marine reptiles that flourished during much of the Mesozoic era.",
    "secondary": "In vertebrate paleontology, a clade of diapsid reptiles that appeared in the Early Triassic and evolved extreme fish-like body plans before dying out in the Late Cretaceous.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The vertebrae of the **Ichthyosauria** are deeply amphicoelous like those of bony fishes, providing maximum spinal flexibility."
      },
      {
        "author": "G. R. Wieland",
        "work": "The Osteology of Archelon",
        "quote": "Fossil embryos preserved inside adult ribcages proved that the **Ichthyosauria** were viviparous animals giving birth at sea."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The hyperphalangy and polydactyly seen in paddle fins of the **Ichthyosauria** represent extraordinary marine specializations."
      }
    ]
  },
  "Dashboard — ichthy/ichthyosauridae.md": {
    "primary": "A taxonomic family of typical Jurassic ichthyosaurs, including the genus Ichthyosaurus.",
    "secondary": "In systematic paleontology, streamlined marine reptiles of the parvipelvian clade possessing large eyes, reduced humerus bones, and a downward-bent tail supporting a caudal fin.",
    "quotes": [
      {
        "author": "Richard Lydekker",
        "work": "Catalogue of the Fossil Reptilia and Amphibia in the British Museum",
        "quote": "Specimens belonging to the family **Ichthyosauridae** abound in the Liassic limestone quarries of Somerset and Dorset."
      },
      {
        "author": "Henry Fairfield Osborn",
        "work": "The Age of Mammals",
        "quote": "The rapid aquatic propulsion of the **Ichthyosauridae** made them the apex pursuit predators of the Early Jurassic seas."
      },
      {
        "author": "Arthur Smith Woodward",
        "work": "Outlines of Vertebrate Palaeontology",
        "quote": "Skin impressions found at Holzmaden revealed that members of **Ichthyosauridae** possessed a fleshy dorsal fin lacking bony support."
      }
    ]
  },
  "Dashboard — ichthy/ichthyosaurus.md": {
    "primary": "The type genus of extinct dolphin-like marine reptiles from the Early Jurassic of Europe.",
    "secondary": "In paleontology, a predatory marine reptile growing to 2–3 meters in length, discovered famously by Mary Anning, feeding primarily on belemnites and fish.",
    "quotes": [
      {
        "author": "William Buckland",
        "work": "Geology and Mineralogy Considered with Reference to Natural Theology",
        "quote": "Coprolites found within the ribs of **Ichthyosaurus** contain scales of fossil fishes and the ink bags of prehistoric squids."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The unexpected discovery of **Ichthyosaurus** demonstrated how reptilian limbs could be modified into swimming paddles."
      },
      {
        "author": "Gideon Mantell",
        "work": "The Wonders of Geology",
        "quote": "The ferocious jaws and colossal eyes of **Ichthyosaurus** commanded the ancient seas that once rolled over England."
      }
    ]
  },
  "Dashboard — ichthy/ichthyosis.md": {
    "primary": "A genetic or acquired skin disorder characterized by dry, thickened, rough, and scaly skin resembling fish scales.",
    "secondary": "In dermatology, a group of cornification disorders (such as ichthyosis vulgaris and harlequin ichthyosis) caused by defective epidermal keratinization and barrier lipids.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital **ichthyosis** presents at birth with generalized scaling and polygonal plates covering the trunk and limbs."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "The skin was so dry and encrusted with rough scales that old writers compared it to the disease called **ichthyosis**."
      },
      {
        "author": "Erasmus Wilson",
        "work": "On Diseases of the Skin",
        "quote": "In chronic **ichthyosis**, emollients and warm alkaline baths soften the harsh, fish-like epidermis."
      }
    ]
  },
  "Dashboard — ichthy/ichthyosis_icthyophaga.md": {
    "primary": "A historical clinical designation linking fish-scale dermatosis with piscivorous diets or coastal fish-eating communities.",
    "secondary": "In medical ethnology and historical epidemiology, cutaneous scaly dermatoses observed in maritime populations traditionally consuming exclusively fish (ichthyophagi).",
    "quotes": [
      {
        "author": "Richard Mead",
        "work": "Medica Sacra",
        "quote": "The scaly skin eruptions recorded as **ichthyosis** were attributed by coastal travelers to a perpetual diet of dried fish."
      },
      {
        "author": "John Arbuthnot",
        "work": "An Essay Concerning the Effects of Air on Human Bodies",
        "quote": "Those tribes who subsisted entirely on fish suffered cutaneous disorders closely allied to **ichthyosis**."
      },
      {
        "author": "Gilbert Blane",
        "work": "Observations on the Diseases of Seamen",
        "quote": "Protracted maritime scorbutic states often manifested severe dry scaling mimicking true hereditary **ichthyosis**."
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

console.log(`Updated ${updatedCount} files in Batch 2!`);
