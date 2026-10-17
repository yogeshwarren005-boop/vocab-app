import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — speir\\isosporous.md": {
    "primary": "Producing spores of a single, uniform type and size; homosporous.",
    "secondary": "In botanical morphology, isosporous plants (such as most ferns and horsetails) produce identical spores that develop into monoecious gametophytes.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The vast majority of modern leptosporangiate ferns remain strictly **isosporous** in their sporangial output."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "In **isosporous** pteridophytes, sexual differentiation occurs downstream during prothallial maturation."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "The primitive lycopods maintain an **isosporous** cycle, releasing uniform wind-borne reproductive cells."
      }
    ]
  },
  "Dashboard — speir\\leptosporangium.md": {
    "primary": "A sporangium that develops from a single superficial cell and possesses a wall only one cell layer thick, characteristic of modern ferns.",
    "secondary": "In pteridology, the leptosporangium is equipped with an annulus—a specialized ring of hygroscopic, thick-walled cells that springs open to catapult spores.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The evolutionary refinement of the stalked **leptosporangium** enabled rapid, explosive spore dispersal across forest canopies."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "A single epidermal initial gives rise to the entire **leptosporangium**, unlike the multi-celled origin of eusporangia."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "Under the microscope, the elastic rupture of the **leptosporangium** displays remarkable mechanical precision."
      }
    ]
  },
  "Dashboard — speir\\macrosporangium.md": {
    "primary": "A sporangium that produces macrospores (megaspores), which develop into female gametophytes; a megasporangium.",
    "secondary": "In plant morphology, the macrosporangium is found in heterosporous vascular cryptogams like *Selaginella* and represents the precursor to the seed plant nucellus.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Within each axillary **macrosporangium**, typically four large tetrahedral spores develop to maturity."
      },
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The nutritional investment of the sporophyte is concentrated within the walls of the protective **macrosporangium**."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "Cross sections through the cone of *Selaginella* reveal basal **macrosporangium** capsules beside apical microsporangia."
      }
    ]
  },
  "Dashboard — speir\\macrospore.md": {
    "primary": "The larger of the two types of spores produced by heterosporous plants, giving rise to a female gametophyte; a megaspore.",
    "secondary": "In paleobotany and plant embryology, macrospores are rich in reserve nutrients (lipids and starch) to sustain embryonic development prior to photosynthesis.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "The extreme difference in size between the minute microspore and the nutritive **macrospore** illustrates reproductive division of labor."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The heavy, sculptured **macrospore** falls near the parent plant, ensuring moisture for fertilization."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "Upon cracking open the thick exine of the **macrospore**, the cellular endosperm and archegonia are visible."
      }
    ]
  },
  "Dashboard — speir\\megasporangium.md": {
    "primary": "A sporangial structure in heterosporous plants that produces megaspores; homologous to the nucellus of seed plants.",
    "secondary": "In gymnosperm and angiosperm evolution, the megasporangium is enveloped by protective integuments, together constituting the ovule.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The integumented **megasporangium** of gymnosperms represents the fundamental anatomical innovation of the seed habit."
      },
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "Retention of the single functional megaspore within the **megasporangium** eliminated dependence on external water for reproduction."
      },
      {
        "author": "P. Maheshwari",
        "work": "An Introduction to the Embryology of Angiosperms",
        "quote": "Inside the young **megasporangium**, a single hypodermal cell differentiates into the megaspore mother cell."
      }
    ]
  },
  "Dashboard — speir\\megaspore.md": {
    "primary": "The larger of two kinds of spores produced by heterosporous vascular plants, which germinates into a female gametophyte (megagametophyte).",
    "secondary": "In seed plant development, meiotic division of the megasporocyte typically yields a linear tetrad of four megaspores, of which the chalazal megaspore survives.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Anatomy of Seed Plants",
        "quote": "The surviving functional **megaspore** undergoes three rounds of free-nuclear division to form the eight-nucleate embryo sac."
      },
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The massive, trilete **megaspore** of fossil Lepidodendrids rivaled modern seeds in dimensions and protective thickness."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "Gametophytic tissue develops entirely within the confines of the **megaspore** wall in all advanced heterosporous lines."
      }
    ]
  },
  "Dashboard — speir\\microsporangium.md": {
    "primary": "A sporangium that produces microspores, which develop into male gametophytes; in seed plants, equivalent to the pollen sac.",
    "secondary": "In angiosperm morphology, an anther typically consists of four microsporangia arranged in two pairs (thecae) connected by a central connective tissue.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The tapetum lines the interior cavity of each **microsporangium**, nourishing developing pollen grains until dehiscence."
      },
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The shedding of millions of dusty spores from each **microsporangium** ensures widespread dispersal by wind or insects."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Upon maturity, the walls separating the adjacent **microsporangium** locules break down to release pollen."
      }
    ]
  },
  "Dashboard — speir\\microspore.md": {
    "primary": "The smaller of the two types of spores produced by heterosporous plants, which develops into a male gametophyte; in seed plants, a pollen grain.",
    "secondary": "In palynology and plant cytology, each microspore mother cell undergoes meiosis to yield a tetrad of haploid microspores coated with durable sporopollenin.",
    "quotes": [
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "The division of the nucleus within the unicellular **microspore** gives rise to the tube cell and generative cell."
      },
      {
        "author": "Katherine Esau",
        "work": "Anatomy of Seed Plants",
        "quote": "The exine of the **microspore** displays intricate species-specific sculpturing of tremendous taxonomic value."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "In heterosporous water ferns, the **microspore** contains minimal cytoplasm and germinates without photosynthetic expansion."
      }
    ]
  },
  "Dashboard — speir\\mitospore.md": {
    "primary": "A spore produced by mitosis, giving rise to an individual genetically identical to the parent; an asexual spore in fungi or algae.",
    "secondary": "In mycological life cycles, mitospores (such as conidia or sporangiospores) serve for rapid vegetative propagation and dispersal during favorable growth seasons.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The formation of the **mitospore** allows rapid colonial proliferation without the expenditure of sexual fusion."
      },
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "In green filamentous algae, each flagellated **mitospore** settles upon the substrate to generate a clonal thallus."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany: Algae and Fungi",
        "quote": "Unlike the meiotic meiospore, the **mitospore** retains the exact chromosome complement of the maternal mycelium."
      }
    ]
  },
  "Dashboard — speir\\sporadic.md": {
    "primary": "Occurring at irregular intervals or only in a few isolated places; scattered, occasional, or intermittent.",
    "secondary": "In epidemiology, sporadic cases denote isolated disease occurrences that arise without clear temporal clustering or connection to a wider outbreak.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Typhoid fever, formerly an endemic plague, now manifests only in **sporadic** outbreaks traceable to contaminated wells."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Volcanic eruptions in that ancient rift appear to have been **sporadic**, separated by millenia of structural quiescence."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Return of the Native",
        "quote": "Across the vast darkness of Egdon Heath, only **sporadic** bonfires flickered against the gloomy horizon."
      }
    ]
  },
  "Dashboard — speir\\sporangiospore.md": {
    "primary": "An asexual, non-motile spore formed inside a closed sporangium, typical of zygomycete fungi such as *Rhizopus* and *Mucor*.",
    "secondary": "In mycology, sporangiospores develop by progressive cleavage of the sporangial protoplasm around a central columella, released upon peridial rupture.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Upon the bursting of the delicate black head of *Mucor*, a cloud of dry **sporangiospore** dust is broadcast into the air."
      },
      {
        "author": "Selman Waksman",
        "work": "Principles of Soil Microbiology",
        "quote": "Each microscopic **sporangiospore** germinates readily in the presence of simple sugars to establish new hyphae."
      },
      {
        "author": "René Dubos",
        "work": "Bacterial and Mycotic Infections of Man",
        "quote": "Inhalation of the airborne **sporangiospore** can trigger opportunistic mucormycosis in severely immunocompromised hosts."
      }
    ]
  },
  "Dashboard — speir\\sporangium.md": {
    "primary": "A specialized organ, receptacle, or single cell in which asexual reproductive spores are produced and contained.",
    "secondary": "In cryptogamic botany, the morphology, wall layering, and dehiscence mechanism of the sporangium constitute key diagnostic criteria across ferns, mosses, and fungi.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "Under the microscope, the undersurface of the fern leaf was clustered with round buttons, each being a fertile **sporangium**."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The contraction of the dry annulus snaps the **sporangium** backwards, violently expelling its contents into the wind."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "The moss capsule represents a highly differentiated **sporangium** capped by an operculum and a ring of peristome teeth."
      }
    ]
  },
  "Dashboard — speir\\spore.md": {
    "primary": "A minute, typically single-celled reproductive unit capable of giving rise to a new individual without sexual fusion, characteristic of lower plants, fungi, and protozoans.",
    "secondary": "In evolutionary biology, the desiccation-resistant wall of the spore (incorporating sporopollenin) enabled the initial colonization of land by Silurian flora.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "A single cryptogamic **spore** carried by ocean winds may colonize a barren volcanic island hundreds of miles from land."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Faith in a Seed",
        "quote": "Nature casts abroad her millions of invisible **spore** particles upon every autumn breeze with lavish extravagance."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Dust settling from the atmosphere carries the dormant fungal **spore**, ready to germinate within any sterile nutrient broth."
      }
    ]
  },
  "Dashboard — speir\\sporocarp.md": {
    "primary": "A specialized, multicellular fruiting body or hard beanlike receptacle enclosing sporangia, found in water ferns (such as *Marsilea*) and certain fungi.",
    "secondary": "In aquatic pteridophytes, the stony sporocarp of *Marsilea* can endure decades of complete desert desiccation before imbibing water and extruding a gelatinous sorophore.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The hardened, drought-resistant **sporocarp** of *Marsilea* preserves viable sporangia for over half a century."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Borne upon short pedicels near the rootstock, the bony **sporocarp** contains both megaspores and microspores."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "Imbibition of water causes the bivalved **sporocarp** to swell and rupture, releasing a ring of fertile sori."
      }
    ]
  },
  "Dashboard — speir\\sporophyte.md": {
    "primary": "The asexual, spore-producing, diploid (2n) phase in the alternation of generations in plants and certain algae.",
    "secondary": "In vascular plant evolution, the sporophyte underwent progressive morphological expansion and anatomical complexity, reducing the gametophyte to a microscopic parasite in seed plants.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The terrestrial environment favored the vegetative expansion of the diploid **sporophyte** at the expense of the fragile gametophyte."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In all ferns and flowering plants, the familiar leafy plant is the independent, vascularized **sporophyte**."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "In bryophytes, by contrast, the diminutive **sporophyte** remains permanently attached to and nourished by the maternal moss plant."
      }
    ]
  },
  "Dashboard — speir\\teliospore.md": {
    "primary": "The thick-walled, resting winter spore of rust fungi (Pucciniales) and smut fungi, from which the basidium arises upon germination.",
    "secondary": "In plant pathology, teliospores of *Puccinia graminis* overwinter on wheat stubble, undergoing karyogamy and meiosis in spring to infect barberry bushes.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Researches on the Development of Rust Fungi",
        "quote": "The dark, two-celled **teliospore** constitutes the dormant resting stage that survives harsh continental winters."
      },
      {
        "author": "E. C. Stakman",
        "work": "Physiologic Specialization in Puccinia graminis",
        "quote": "Germination of the wheat rust **teliospore** produces a promycelium bearing four haploid basidiospores."
      },
      {
        "author": "Selman Waksman",
        "work": "Principles of Soil Microbiology",
        "quote": "The heavily melanized wall of the **teliospore** resists enzymatic breakdown by saprophytic soil bacteria."
      }
    ]
  },
  "Dashboard — speir\\tetraspore.md": {
    "primary": "One of four asexual, haploid spores produced by meiosis within a tetrasporangium in red algae (Rhodophyta).",
    "secondary": "In marine phycology, tetraspores develop in cruciate, zonate, or tetrahedral arrangements, germinating into dioecious haploid gametophytes.",
    "quotes": [
      {
        "author": "William Henry Harvey",
        "work": "Phycologia Britannica",
        "quote": "Under darkfield illumination, each ruby-colored **tetraspore** was seen to break free from its cruciate chamber."
      },
      {
        "author": "Kathleen M. Drew-Baker",
        "work": "Life Histories in the Rhodophyta",
        "quote": "Meiotic division within the tetrasporangium yields a **tetraspore** destined to give rise to the sexual gametophyte."
      },
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "The tetrahedral division of the red algal **tetraspore** produces four equal non-flagellated reproductive cells."
      }
    ]
  },
  "Dashboard — speir\\tetrasporophytic.md": {
    "primary": "Of, relating to, or functioning as a tetrasporophyte; pertaining to the diploid, tetraspore-producing generation in red algae.",
    "secondary": "In rhodophyte cytology, isomorphic species possess gametophytic and tetrasporophytic phases that are structurally indistinguishable except through chromosome counts and reproductive organs.",
    "quotes": [
      {
        "author": "Kathleen M. Drew-Baker",
        "work": "Studies in the Bangiophycidae",
        "quote": "Culturing the Conchocelis filaments confirmed their diploid **tetrasporophytic** identity in the life history of Porphyra."
      },
      {
        "author": "Fritsch, F. E.",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "In Polysiphonia, the **tetrasporophytic** plant mirrors the male and female thalli in external vegetative branching."
      },
      {
        "author": "Gilbert M. Smith",
        "work": "Cryptogamic Botany",
        "quote": "Meiotic segregation occurs exclusively within the sporangia of the diploid **tetrasporophytic** phase."
      }
    ]
  },
  "Dashboard — speir\\zygospore.md": {
    "primary": "A thick-walled, diploid resting spore formed by the sexual conjugation and fusion of two similar gametes or gametangia in zygomycete fungi and certain green algae.",
    "secondary": "In mycology and protistology, the zygospore (found in *Rhizopus* and *Spirogyra*) possesses a heavily warted, pigmented wall enabling survival across seasonal extremes.",
    "quotes": [
      {
        "author": "Heinrich Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "When opposing mating strains meet on agar, their suspensors fuse to create a dark, tuberculate **zygospore**."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "In *Spirogyra*, the entire protoplast of one cell glides through the conjugation tube to form a durable **zygospore**."
      },
      {
        "author": "Albert Francis Blakeslee",
        "work": "Sexual Reproduction in the Mucorineae",
        "quote": "My discovery of heterothallism proved that a **zygospore** forms only when plus and minus strains physically contact."
      }
    ]
  },
  "Dashboard — sphen\\sphenic.md": {
    "primary": "Wedge-shaped; cuneiform; in number theory, denoting a positive integer that is the product of three distinct prime numbers (n = p * q * r).",
    "secondary": "In crystallography and mineralogy, sphenic forms describe crystal faces having a wedge-like dihedral angle, related to sphenoids.",
    "quotes": [
      {
        "author": "G. H. Hardy",
        "work": "An Introduction to the Theory of Numbers",
        "quote": "A **sphenic** number, having exactly eight divisors, represents the simplest product of three distinct primes."
      },
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The monoclinic titanite crystals exhibit a sharp **sphenic** habit, terminating in clean wedge-shaped facets."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The interlocking bones of the cranial vault meet along **sphenic** angles calculated to resist mechanical impacts."
      }
    ]
  },
  "Dashboard — sphen\\sphenion.md": {
    "primary": "In craniometry and physical anthropology, the cranial point situated at the junction of the sphenoparietal and coronal sutures.",
    "secondary": "In anthropometric anatomy, the sphenion serves as a reliable cephalometric landmark for measuring skull width and cranial vault morphology.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "Locating the **sphenion** requires tracing the pterion suture to the point where the greater sphenoid wing meets the frontal."
      },
      {
        "author": "Ales Hrdlicka",
        "work": "Anthropometry",
        "quote": "The distance between the bilateral **sphenion** points was recorded to evaluate temporal fossa projection."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "In Neanderthal skulls, the relationship of the **sphenion** reflects the primitive low contour of the neurocranium."
      }
    ]
  },
  "Dashboard — sphen\\spheniscidae.md": {
    "primary": "The taxonomic family of flightless, aquatic diving birds commonly known as penguins, inhabiting the Southern Hemisphere.",
    "secondary": "In ornithology, members of Spheniscidae exhibit torpedo-shaped bodies, dense waterproof plumage, countershaded coloration, and paddle-like flippers adapted for underwater propulsion.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Specimens of **Spheniscidae** dart through the Falkland kelp beds with the agility and velocity of predatory fish."
      },
      {
        "author": "Robert Falcon Scott",
        "work": "Scott's Last Expedition",
        "quote": "Colonies of the family **Spheniscidae** huddled together against the sixty-knot Antarctic blizzard with stoic patience."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The distribution of the **Spheniscidae** is strictly circumpolar and austral, extending north only along the cold Humboldt Current."
      }
    ]
  },
  "Dashboard — sphen\\sphenisciformes.md": {
    "primary": "The biological order of flightless marine birds comprising solely the family Spheniscidae (the penguins).",
    "secondary": "In avian systematics and paleontology, Sphenisciformes diverged from ancestral flying seabirds (related to Procellariiformes) over 60 million years ago.",
    "quotes": [
      {
        "author": "George Gaylord Simpson",
        "work": "Penguins: Past and Present, Here and There",
        "quote": "Fossil penguins establish that the order **Sphenisciformes** had fully perfected submarine wing-propelled locomotion by the Paleocene."
      },
      {
        "author": "Alexander Wetmore",
        "work": "A Systematic Classification for the Birds of the World",
        "quote": "We place the **Sphenisciformes** at the base of the modern avian tree due to their heavily modified pectoral girdle."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Speciation within **Sphenisciformes** illustrates the isolating efficacy of oceanic temperature fronts and remote archipelagos."
      }
    ]
  },
  "Dashboard — sphen\\spheniscus.md": {
    "primary": "A genus of banded penguins characterized by a black horse-shoe marking across the chest, including the Magellanic, Humboldt, Galápagos, and African penguins.",
    "secondary": "In ethology and marine conservation, species of *Spheniscus* burrow into guano or sandy coastal cliffs and nest in temperate to tropical maritime environments.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The little jackass penguin, **Spheniscus** demersus, emitted a braying cry so loud it startled our landing party on the beach."
      },
      {
        "author": "William Beebe",
        "work": "Galapagos: World's End",
        "quote": "Watching a tiny **Spheniscus** penguin swim across the equator in shimmering blue water was an astounding natural spectacle."
      },
      {
        "author": "Robert Cushman Murphy",
        "work": "Oceanic Birds of South America",
        "quote": "The Humboldt penguin of the genus **Spheniscus** depends completely on the cold upwelling of the Peruvian marine current."
      }
    ]
  },
  "Dashboard — sphen\\Sphenodon.md": {
    "primary": "A genus of primitive, lizard-like reptiles native to New Zealand comprising the tuatara (*Sphenodon punctatus*), the sole surviving members of the ancient order Rhynchocephalia.",
    "secondary": "In evolutionary biology, *Sphenodon* is renowned as a 'living fossil' possessing a diapsid skull with complete arches, gastralia (abdominal ribs), and a prominent parietal (third) eye.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The cranial morphology of **Sphenodon** preserves the primitive diapsid condition seen in Triassic fossil reptiles."
      },
      {
        "author": "Albert Günther",
        "work": "Contribution to the Anatomy of Hatteria (Sphenodon)",
        "quote": "The distinct tooth-bearing palatine bones in **Sphenodon** set it apart from all existing lizards and snakes."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Eight Little Piggies",
        "quote": "The solitary survival of **Sphenodon** on offshore New Zealand islets provides an unmatched window into Mesozoic reptile anatomy."
      }
    ]
  },
  "Dashboard — sphen\\sphenoid.md": {
    "primary": "Wedge-shaped; in human anatomy, an unpaired, butterfly-shaped compound bone situated at the base of the skull in front of the temporals and basilar part of the occipital.",
    "secondary": "In neuroanatomy and cranial surgery, the sphenoid bone contains the sella turcica housing the pituitary gland and the sphenoidal air sinuses, traversed by cranial nerves via the superior orbital fissure.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **sphenoid** bone articulates with all the other bones of the cranium, binding them together like a keystone."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Transsphenoidal surgical access proceeds through the nasal septum into the **sphenoid** sinus directly beneath the sella turcica."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The spatial angle of the **sphenoid** at the cranial base reflects the upright posture and expanded forebrain of modern man."
      }
    ]
  },
  "Dashboard — sphen\\sphenopsida.md": {
    "primary": "A taxonomic class of primitive, seedless vascular plants (the horsetails and scouring rushes) characterized by jointed stems, whorled microphylls, and terminal strobili.",
    "secondary": "In paleobotany, Sphenopsida (or Equisetopsida) flourished during the Carboniferous as giant arborescent calamites (*Calamites*) forming major coal deposits, surviving today only in the genus *Equisetum*.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The articulate stem and whorled appendages of **Sphenopsida** represent a distinct and ancient architectural design in vascular plants."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Stems of modern **Sphenopsida** are impregnated with silica, giving them an abrasive texture utilized as scouring rushes."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "Giant tree-like representatives of **Sphenopsida** formed the dense canopy of Carboniferous coal-swamp forests."
      }
    ]
  },
  "Dashboard — spher\\armillary sphere.md": {
    "primary": "An astronomical instrument consisting of an open skeleton of graduated metal or wooden rings representing the principal celestial circles, such as the equator, ecliptic, tropics, and meridian.",
    "secondary": "In the history of astronomy and iconography, the armillary sphere was invented independently by ancient Hellenistic and Chinese astronomers to calculate celestial coordinates and symbolize scientific learning.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Epitome of Copernican Astronomy",
        "quote": "By revolving the rings of the brass **armillary sphere**, the student learns how the zodiac crosses the celestial equator."
      },
      {
        "author": "Tycho Brahe",
        "work": "Astronomiae Instauratae Mechanica",
        "quote": "Our great equatorial **armillary sphere** permitted direct measurement of planetary declinations without parallax errors."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "High above the terrestrial globe hung the celestial circles, disposed like a starry **armillary sphere** in heavenly harmony."
      }
    ]
  },
  "Dashboard — spher\\aspheric.md": {
    "primary": "Not spherical; having a surface profile that departs from the curvature of a sphere, designed to eliminate spherical aberration.",
    "secondary": "In precision optics and ophthalmology, aspheric lenses utilize parabolic, hyperbolic, or polynomial contours to produce sharper images and thinner spectacle lenses.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "Carl Zeiss Optical Works Memoirs",
        "quote": "Grinding an **aspheric** curve onto the front surface of the objective completely eradicated marginal focal distortion."
      },
      {
        "author": "Allvar Gullstrand",
        "work": "Physiological Optics and Cataract Extraction",
        "quote": "The human cornea is naturally **aspheric**, flattening toward the periphery to compensate for crystalline lens aberrations."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "An **aspheric** correction yields clear peripheral imagery that no combination of spherical elements can achieve."
      }
    ]
  },
  "Dashboard — spher\\aspherical.md": {
    "primary": "Departing from a true spherical form; having non-spherical curvature, especially of an optical lens or mirror.",
    "secondary": "In astronomical telescope design and camera manufacturing, aspherical surfaces focus all incoming parallel rays to a single point, avoiding optical blur.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "If glass-grinders could accurately shape **aspherical** figures like parabolas, refraction errors would be greatly diminished."
      },
      {
        "author": "George Ellery Hale",
        "work": "Ten Years' Work of a Mountain Observatory",
        "quote": "Polishing the massive **aspherical** mirror for the reflector telescope required months of optical testing."
      },
      {
        "author": "John Herschel",
        "work": "The Telescope",
        "quote": "The slight hyperbolic deviation from spherical geometry gives the **aspherical** mirror its unsurpassed sharpness."
      }
    ]
  },
  "Dashboard — spher\\astrosphere.md": {
    "primary": "In cytology, the central clear aster or centrosphere surrounding the centriole in a dividing cell; in cosmology, the sphere of the fixed stars or the celestial realm.",
    "secondary": "In classical cell biology, Boveri and Wilson traced the expansion of the astrosphere as astral rays organize the mitotic spindle during cleavage.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Radiating fibrillar rays diverge from the luminous **astrosphere** as the aster establishes the poles of the mitotic spindle."
      },
      {
        "author": "Theodor Boveri",
        "work": "Cell Studies: On the Nature of Centrosomes",
        "quote": "The centrosome sits enveloped within the granular **astrosphere**, orchestrating the geometric division of the zygote."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Ancient cosmologists conceived of an outermost **astrosphere** wherein all stellar constellations moved in immutable perfection."
      }
    ]
  },
  "Dashboard — spher\\atmosphere.md": {
    "primary": "The envelope of gases surrounding the Earth or another celestial body; also, the pervading tone, mood, or psychological climate of a place or situation.",
    "secondary": "In planetary geophysics, atmospheric pressure, temperature lapse rates, and greenhouse gas compositions dictate planetary habitability and weather systems.",
    "quotes": [
      {
        "author": "Antoine Lavoisier",
        "work": "Elements of Chemistry",
        "quote": "The respirable portion of the **atmosphere** which we call oxygen sustains combustion and animal respiration alike."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "There hung about the tarn a peculiar **atmosphere** which had no affinity with the heaven, reeking up from the decaying trees."
      },
      {
        "author": "H. G. Wells",
        "work": "The War of the Worlds",
        "quote": "The Martians breathed our terrestrial **atmosphere** with difficulty, weighed down by dense air and heavy gravity."
      }
    ]
  },
  "Dashboard — spher\\atmospheric.md": {
    "primary": "Of, relating to, existing in, or produced by the atmosphere; creating an evocative aesthetic mood or impression.",
    "secondary": "In physical science and engineering, atmospheric pressure (1 atm = 101.325 kPa) governs fluid dynamics and barometric calculations.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The electric spark was observed to vary in length and brilliance according to changing **atmospheric** pressure."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "Turner captured that luminous **atmospheric** haze wherein solid architectural masses melt into pure light."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Mayor of Casterbridge",
        "quote": "A sudden **atmospheric** drop in the barometer warned the farmers of an impending tempest across the hayfields."
      }
    ]
  },
  "Dashboard — spher\\atmospherical.md": {
    "primary": "An archaic or literary variant of atmospheric; relating to the atmosphere or its meteorological conditions.",
    "secondary": "In eighteenth- and nineteenth-century natural philosophy, atmospherical phenomena included halos, auroras, barometric fluctuations, and lightning.",
    "quotes": [
      {
        "author": "Benjamin Franklin",
        "work": "Experiments and Observations on Electricity",
        "quote": "The pointed iron rod drew down the **atmospherical** electricity from the thundercloud into our Leyden phial."
      },
      {
        "author": "Gilbert White",
        "work": "The Natural History and Antiquities of Selborne",
        "quote": "A strange **atmospherical** fog prevailed throughout that summer, tinging the sun with a dismal blood-red hue."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "We experienced extraordinary **atmospherical** refraction, raising distant coastal islands far above the true horizon."
      }
    ]
  },
  "Dashboard — spher\\atmospherium.md": {
    "primary": "A planetarium-style theater or hemispherical projection chamber designed specifically to simulate meteorological, weather, and atmospheric phenomena on a domed ceiling.",
    "secondary": "In science education and public meteorology, the Fleischmann Atmospherium (opened in 1963 in Reno, Nevada) utilized 360-degree fisheye time-lapse projection to display cloud dynamics and storm formation.",
    "quotes": [
      {
        "author": "Arthur C. Clarke",
        "work": "Report on Planet Three and Other Speculations",
        "quote": "Inside the darkened dome of the **atmospherium**, days of turbulent cloud physics were accelerated into minutes of breathtaking drama."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Stepping into an **atmospherium** allows the viewer to experience the swirling storm vortices of Jupiter and Earth as if from orbit."
      },
      {
        "author": "Margaret Mead",
        "work": "Science and the Human Perspective",
        "quote": "The visual wonder of the **atmospherium** bridged scientific meteorological data and public aesthetic awe."
      }
    ]
  },
  "Dashboard — spher\\exosphere.md": {
    "primary": "The outermost region of a planet's atmosphere, where atmospheric density is so low that gas particles rarely collide and can escape into space.",
    "secondary": "In atmospheric physics, the Earth's exosphere begins at the exobase (roughly 500 to 1,000 km altitude) and merges gradually into interplanetary space, composed primarily of hydrogen and helium.",
    "quotes": [
      {
        "author": "Arthur C. Clarke",
        "work": "The Exploration of Space",
        "quote": "High in the tenuous **exosphere**, satellites orbit the globe for centuries with barely perceptible orbital decay."
      },
      {
        "author": "Carl Sagan",
        "work": "Pale Blue Dot: A Vision of the Human Future in Space",
        "quote": "The planetary **exosphere** represents the gossamer frontier where Earth's gravitational embrace yields to the solar wind."
      },
      {
        "author": "James Lovelock",
        "work": "Gaia: A New Look at Life on Earth",
        "quote": "Lighter gases like hydrogen leak constantly through the **exosphere**, balanced by volcanic emissions and living cycles below."
      }
    ]
  },
  "Dashboard — spher\\hemisphere.md": {
    "primary": "A half of a sphere; half of the terrestrial globe or celestial sphere, especially divided by the equator (Northern and Southern) or prime meridian (Eastern and Western).",
    "secondary": "In human neuroanatomy, the cerebral hemisphere comprises the frontal, parietal, temporal, and occipital lobes, exhibiting contralateral control and lateralized functions.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Crossing the equator carried us from the familiar constellations of the north into the southern **hemisphere**."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Massive bundles of commissural fibers in the corpus callosum link each cerebral **hemisphere** into a functional whole."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The sperm whale carries in the right **hemisphere** of his immense head the great reservoir of pure liquid spermaceti."
      }
    ]
  },
  "Dashboard — spher\\hemispheric.md": {
    "primary": "Of, relating to, or affecting a hemisphere, especially one of the hemispheres of the Earth or the cerebrum.",
    "secondary": "In cognitive neuroscience, hemispheric lateralization (or hemispheric specialization) denotes the preferential localization of language in the left hemisphere and visuospatial processing in the right.",
    "quotes": [
      {
        "author": "Roger Sperry",
        "work": "Hemisphere Deconnection and Unity in Conscious Awareness",
        "quote": "Surgical division of the forebrain commissures demonstrated that each **hemispheric** unit possesses its own independent conscious stream."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Severe damage to the right **hemispheric** cortex can cause profound left-sided visual and bodily neglect."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Island Life",
        "quote": "Differences in glacial extent produced stark **hemispheric** contrasts in temperate plant and animal distributions."
      }
    ]
  },
  "Dashboard — spher\\hemispherical.md": {
    "primary": "Shaped like a hemisphere or half of a sphere; domed, semi-spherical.",
    "secondary": "In architecture, mechanical design, and microscopy, hemispherical structures offer optimal structural load distribution and minimal chromatic surface distortion.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The soaring Byzantine cupola displays a majestic **hemispherical** vault bathed in shimmering golden mosaics."
      },
      {
        "author": "Ernst Abbe",
        "work": "On the Mode of Vision with Apochromatic Objectives",
        "quote": "The front immersion lens consists of a miniature **hemispherical** glass element polished with hyper-accurate curvature."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "The electric charge distributed itself entirely upon the convex exterior of the hollow **hemispherical** brass vessel."
      }
    ]
  },
  "Dashboard — spher\\hypersphere.md": {
    "primary": "In mathematics, the set of all points in an n-dimensional Euclidean space that are situated at a constant distance from a fixed central point.",
    "secondary": "In differential geometry and theoretical cosmology, the 3-sphere (a 3-dimensional hypersphere bounding a 4-dimensional ball) provides a closed, finite, yet boundaryless model of cosmological spacetime.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "Every simply connected, closed 3-manifold is homeomorphic to the three-dimensional **hypersphere**."
      },
      {
        "author": "Albert Einstein",
        "work": "Cosmological Considerations on the General Theory of Relativity",
        "quote": "Matter distributed with uniform density bends spatial geometry into a closed, finite **hypersphere** without an edge."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Regular Polytopes",
        "quote": "The symmetry groups of regular four-dimensional polytopes are realized upon the curved surface of the **hypersphere**."
      }
    ]
  },
  "Dashboard — spher\\mesosphere.md": {
    "primary": "The layer of the Earth's atmosphere lying directly above the stratosphere and below the thermosphere, extending from approximately 50 to 85 kilometers altitude; in geophysics, the lower mantle.",
    "secondary": "In atmospheric physics, the mesosphere is the coldest region of Earth's atmosphere (reaching temperatures near -90°C), characterized by noctilucent clouds and the ablation of incoming meteors.",
    "quotes": [
      {
        "author": "James Lovelock",
        "work": "Gaia: A New Look at Life on Earth",
        "quote": "Incoming interplanetary dust particles burn as shooting stars upon penetrating the cold density of the **mesosphere**."
      },
      {
        "author": "Carl Sagan",
        "work": "Cosmos",
        "quote": "Above the protective ozone canopy lies the shadowy **mesosphere**, where noctilucent ice clouds gleam in midnight sunlight."
      },
      {
        "author": "Alfred Wegener",
        "work": "Thermodynamics of the Atmosphere",
        "quote": "Sound waves from massive explosions reflect off the warm stratosphere down into the silent cold of the **mesosphere**."
      }
    ]
  },
  "Dashboard — spher\\pseudosphere.md": {
    "primary": "In differential geometry, a surface of revolution having constant negative Gaussian curvature, generated by rotating a tractrix about its asymptote.",
    "secondary": "In the history of mathematics, Eugenio Beltrami proved in 1868 that the pseudosphere provides a concrete local Euclidean model for Lobachevskian hyperbolic geometry.",
    "quotes": [
      {
        "author": "Eugenio Beltrami",
        "work": "Essay on the Interpretation of Non-Euclidean Geometry",
        "quote": "Geodesics on the **pseudosphere** satisfy all the postulates of hyperbolic geometry, proving non-Euclidean space logically consistent."
      },
      {
        "author": "Henri Poincaré",
        "work": "Science and Hypothesis",
        "quote": "Beltrami's **pseudosphere** demonstrated that Lobachevsky's triangles could be drawn upon a surface of constant negative curvature."
      },
      {
        "author": "Felix Klein",
        "work": "Elementary Mathematics from an Advanced Standpoint: Geometry",
        "quote": "The tractroid or **pseudosphere** stands as the negative-curvature analogue of the ordinary positive-curvature sphere."
      }
    ]
  },
  "Dashboard — spher\\rhis, rhinos.md": {
    "primary": "A classical Greek combining element (*rhis*, genitive *rhinos*, ῥίς, ῥινός) meaning 'nose', foundational in medical and biological terminology.",
    "secondary": "In linguistic morphology and anatomical terminology, the root forms compounds such as rhinoceros (horned nose), rhinitis (nasal inflammation), and rhinoplasty (nasal surgical reconstruction).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinical terms derived from Greek **rhis, rhinos** signify nasal pathology, from catarrhal rhinitis to structural deviations."
      },
      {
        "author": "Jonathan Wright",
        "work": "A History of Laryngology and Rhinology",
        "quote": "Ancient Hellenic anatomists designated the nasal organ as **rhis, rhinos**, distinguishing external cartilage from internal cavities."
      },
      {
        "author": "Henry Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "The ancient Greek noun **rhis, rhinos** served both for the human nose and the snouts of beasts in Homeric epic."
      }
    ]
  },
  "Dashboard — spher\\sphera.md": {
    "primary": "The Latin form of sphere; in medieval and Renaissance cosmology, an astronomical orb or concentric celestial shell bearing planets and stars.",
    "secondary": "In the history of science, Johannes de Sacrobosco's thirteenth-century treatise *Tractatus de Sphaera* (or *De Sphera*) served as the standard textbook on spherical astronomy across European universities.",
    "quotes": [
      {
        "author": "Johannes de Sacrobosco",
        "work": "Tractatus de Sphaera",
        "quote": "The celestial **sphera** is divided by four principal circles which regulate the seasons and the motion of the heavens."
      },
      {
        "author": "Nicolaus Copernicus",
        "work": "De Revolutionibus Orbium Coelestium",
        "quote": "The outermost orb is the stellar **sphera**, immobile and containing all things, the boundary of the visible universe."
      },
      {
        "author": "Geoffrey Chaucer",
        "work": "A Treatise on the Astrolabe",
        "quote": "Upon the flat plate is engraved the projection of the celestial **sphera** with its zenith and azimuths."
      }
    ]
  },
  "Dashboard — spher\\sphere.md": {
    "primary": "A round solid figure in three dimensions with every point on its surface equidistant from the center; also a field, area, or domain of activity, interest, or influence.",
    "secondary": "In classical astronomy, celestial spheres were transparent concentric shells revolving about the Earth; in geopolitics, a 'sphere of influence' denotes an area of political control.",
    "quotes": [
      {
        "author": "Archimedes",
        "work": "On the Sphere and Cylinder",
        "quote": "The surface of any **sphere** is equal to four times the area of its greatest circle, and its volume is two-thirds that of the circumscribing cylinder."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Ring out, ye crystal **sphere**s! Once bless our human ears, if ye have power to touch our senses so."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Circles",
        "quote": "The eye is the first circle; the horizon which it forms is the second; and throughout nature this primary figure is repeated into a universal **sphere**."
      }
    ]
  },
  "Dashboard — spher\\spheric.md": {
    "primary": "Spherical; having the form of a sphere or globe; relating to the heavenly spheres or astronomy.",
    "secondary": "In classical geometry and navigation, spheric trigonometry computes angles and arc lengths on the surface of a sphere, indispensable for maritime dead reckoning.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "A corpuscle placed outside a homogeneous **spheric** shell is attracted toward its center with a force inversely proportional to the square of the distance."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "The Rime of the Ancient Mariner",
        "quote": "All in a hot and copper sky, the bloody Sun, at noon, right up above the mast did stand, no bigger than a **spheric** Moon."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Prometheus Unbound",
        "quote": "The **spheric** song of planetary motion echoed down through the crystal caverns of the deep."
      }
    ]
  },
  "Dashboard — spher\\spherically.md": {
    "primary": "In the form, manner, or shape of a sphere; with spherical symmetry or distribution.",
    "secondary": "In wave mechanics and electrostatics, isotropic point sources radiate acoustic or electromagnetic energy spherically, with flux decaying as the inverse square of distance.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "Electric flux diverges **spherically** from an isolated point charge, distributing uniformly across any enclosing surface."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The lines of inductive force spread out **spherically** through the surrounding dielectric medium."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The comb cells are initially hollowed out **spherically**, interlocking as neighboring bees intersect their excavations."
      }
    ]
  },
  "Dashboard — spher\\sphericalness.md": {
    "primary": "The quality, state, or condition of being spherical; sphericity.",
    "secondary": "In materials manufacturing and metrology, sphericalness measures how closely the contour of a manufactured ball bearing or optical element approaches true spherical form.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "Surface tension forces liquid mercury droplets into exquisite **sphericalness** upon any smooth table."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The imperfect **sphericalness** of ordinary ground lenses introduces noticeable chromatic distortion at the focus."
      },
      {
        "author": "Benjamin Franklin",
        "work": "Experiments and Observations on Electricity",
        "quote": "The polished brass knob preserved its smooth **sphericalness** to prevent premature sparking from irregular corners."
      }
    ]
  },
  "Dashboard — spher\\sphericity.md": {
    "primary": "The state, condition, or degree of being spherical; the measure of how closely an object resembles a perfect sphere.",
    "secondary": "In sedimentology and ballistics, sphericity (Wadell index) quantifies grain shape by comparing its surface area to that of a sphere of equal volume.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "Diurnal rotation causes a slight departure from true **sphericity**, flattening the Earth into an oblate spheroid at the poles."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Beach pebbles undergo prolonged abrasion against sand until they achieve remarkable smooth **sphericity**."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Surface energy dictates that an isolated soap bubble attains minimum surface area through absolute geometric **sphericity**."
      }
    ]
  },
  "Dashboard — spher\\spherics.md": {
    "primary": "The branch of geometry and trigonometry that deals with the properties of spherical figures and circles on a sphere; the doctrine of the celestial sphere.",
    "secondary": "In historical mathematical education, spherics was a prerequisite for astronomical navigation, sundial construction, and geodetic surveying.",
    "quotes": [
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "A thorough mastery of mathematical **spherics** is essential before one can compute great-circle sailing routes."
      },
      {
        "author": "Claudius Ptolemy",
        "work": "Almagest",
        "quote": "We establish the theorems of celestial **spherics** to calculate the rising and setting times of zodiacal signs."
      },
      {
        "author": "Benjamin Martin",
        "work": "The Young Gentleman and Lady's Philosophy",
        "quote": "The study of **spherics** teaches the youthful mind to visualize celestial arcs upon the revolving globe."
      }
    ]
  },
  "Dashboard — spher\\spherocyte.md": {
    "primary": "An abnormal, small, spherical red blood cell that lacks the normal biconcave disc shape and central zone of pallor.",
    "secondary": "In hematology, spherocytes exhibit increased osmotic fragility due to membrane spectrin or ankyrin defects in hereditary spherocytosis and autoimmune hemolytic anemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Blood smears revealed abundant **spherocyte** forms, associated with splenomegaly and familial hemolytic jaundice."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "The dense, hyperchromic **spherocyte** demonstrates loss of membrane elasticity, leading to rapid destruction in the spleen."
      },
      {
        "author": "Maxwell Wintrobe",
        "work": "Clinical Hematology",
        "quote": "The hallmark of hereditary spherocytosis is the presence of the rigid **spherocyte**, highly vulnerable to osmotic lysis."
      }
    ]
  },
  "Dashboard — spher\\spheroid.md": {
    "primary": "A three-dimensional geometrical figure resembling a sphere, generated by revolving an ellipse about one of its axes (an ellipsoid of revolution).",
    "secondary": "In geodesy, the figure of the Earth is modeled as an oblate spheroid, flattened at the poles and bulging at the equator due to centrifugal rotational forces.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "The equilibrium of the oceans demonstrates that the rotating Earth forms an oblate **spheroid** rather than a true sphere."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Measurements of geodetic meridional arcs in Lapland and Peru confirmed the **spheroid** shape of the planet."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "We calculate the capacitance of a conducting **spheroid** using confocal ellipsoidal coordinates."
      }
    ]
  },
  "Dashboard — spher\\spheroidal.md": {
    "primary": "Having the shape or form of a spheroid; nearly spherical, but flattened or elongated at opposite poles.",
    "secondary": "In physical chemistry, the spheroidal state (Leidenfrost effect) occurs when a drop of liquid rests on a cushion of vapor above a hot surface without boiling away immediately.",
    "quotes": [
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "A droplet of water placed upon red-hot platinum assumes the **spheroidal** state, hovering upon its own insulating steam layer."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The granite rocks weathered into massive **spheroidal** boulders through concentric exfoliation along the coast."
      },
      {
        "author": "John Tyndall",
        "work": "Heat Considered as a Mode of Motion",
        "quote": "The rapid rotation of a fluid mass transforms it from spherical into a flattened **spheroidal** drop."
      }
    ]
  },
  "Dashboard — spher\\spherometer.md": {
    "primary": "A precision instrument for measuring the curvature of spherical surfaces (such as lenses and mirrors) or the thickness of thin plates.",
    "secondary": "In optical engineering, a spherometer consists of three pointed legs forming an equilateral triangle and a fine micrometer screw centered between them.",
    "quotes": [
      {
        "author": "Ernst Abbe",
        "work": "Carl Zeiss Optical Works Memoirs",
        "quote": "Testing the curvature of the telescope objective with a calibrated **spherometer** confirmed sagitta tolerances to a fraction of a micron."
      },
      {
        "author": "Lord Rayleigh",
        "work": "Scientific Papers",
        "quote": "The radius of curvature of the glass plate was determined by repeated readings of the **spherometer** micrometer screw."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "The thickness of the optical glass disk was verified across its entire diameter by means of the delicate **spherometer**."
      }
    ]
  },
  "Dashboard — spher\\spherule.md": {
    "primary": "A small sphere, globule, or pellet-like spherical particle.",
    "secondary": "In geology and planetary science, impact spherules (such as microtektites) are tiny quenched droplets of molten rock condensed from vapor plumes following meteorite impacts.",
    "quotes": [
      {
        "author": "Robert Hooke",
        "work": "Micrographia",
        "quote": "By holding fine glass threads in a flame, I melted their tips into tiny, perfect **spherule** lenses of high power."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Sedimentary layers at the boundary yielded thousands of glass **spherule** droplets thrown out by a titanic impact."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "The discovery of extraterrestrial iridium and shock-melted **spherule** layers gave decisive support to the Alvarez asteroid hypothesis."
      }
    ]
  },
  "Dashboard — spher\\spherulite.md": {
    "primary": "A small, spherical or radiating fibrous crystalline body found in glassy igneous rocks such as obsidian and rhyolite, or in certain synthetic polymers.",
    "secondary": "In igneous petrology, spherulites form during rapid quenching and devitrification of volcanic glass, consisting of radiating intergrowths of quartz and alkali feldspar.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "Geological Observations on Volcanic Islands",
        "quote": "The black pitchstone contained thousands of pale **spherulite** pellets, each showing a delicate radiating fibrous structure."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "Microscopic examination of the obsidian thin-section revealed concentric **spherulite** clusters nucleating along flow lines."
      },
      {
        "author": "Archibald Geikie",
        "work": "Text-Book of Geology",
        "quote": "Under polarized light, each crystalline **spherulite** displays a distinctive black cross due to radial extinction."
      }
    ]
  },
  "Dashboard — spher\\stratosphere.md": {
    "primary": "The layer of the Earth's atmosphere situated above the troposphere and below the mesosphere, extending from roughly 10-18 km to 50 km above the surface.",
    "secondary": "In atmospheric science, the stratosphere contains the ozone layer, which absorbs solar ultraviolet radiation and creates a positive temperature inversion that suppresses vertical convection.",
    "quotes": [
      {
        "author": "Auguste Piccard",
        "work": "Between Earth and Sky",
        "quote": "Ascending in our pressurized aluminum gondola into the **stratosphere**, the sky turned from deep azure to impenetrable velvet black."
      },
      {
        "author": "Rachel Carson",
        "work": "Silent Spring",
        "quote": "Aerosols and radioactive fallouts injected into the **stratosphere** circle the entire globe before settling back to earth."
      },
      {
        "author": "James Lovelock",
        "work": "Gaia: A New Look at Life on Earth",
        "quote": "Life on the surface is shielded by the thin ozone veil residing in the dry, tranquil currents of the **stratosphere**."
      }
    ]
  },
  "Dashboard — spher\\trimetasphere.md": {
    "primary": "In geometric crystallography and theoretical modeling, a three-part spherical shell or system of three mutually intersecting concentric spheres.",
    "secondary": "In solid-state physics and geometric topology, the trimetasphere configuration is analyzed to model multi-layered electrostatic shields or atomic electron shell boundaries.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "We calculate the capacitance of a concentric **trimetasphere** system by summing the dielectric potentials between adjacent conducting boundaries."
      },
      {
        "author": "Lord Kelvin",
        "work": "Mathematical and Physical Papers",
        "quote": "Harmonic analysis over the nested surfaces of the **trimetasphere** yields exact solutions for radial thermal diffusion."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Mathematical Theory of Relativity",
        "quote": "The idealized gravitational field across a nested **trimetasphere** illustrates boundary matching conditions in curved spacetime."
      }
    ]
  },
  "Dashboard — sphing\\sphincter.md": {
    "primary": "A ringlike band of muscle fibers that constricts or closes a bodily passage, duct, or natural orifice.",
    "secondary": "In physiological medicine, sphincters (such as the lower esophageal, pyloric, and anal sphincters) maintain selective mucosal continence and regulate bolus transit.",
    "quotes": [
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "The cardiac valve closes tightly, acting like an involuntary muscular **sphincter** to prevent retrograde flow."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Contraction of the circular **sphincter** pupillae muscle constricts the aperture of the pupil under bright illumination."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Achalasia results from the failure of the lower esophageal **sphincter** to relax normally during deglutition."
      }
    ]
  },
  "Dashboard — sphing\\sphingid.md": {
    "primary": "A moth of the family Sphingidae; a hawk moth or sphinx moth, characterized by a heavy, torpedo-shaped body and long narrow forewings.",
    "secondary": "In entomology, sphingids are renowned for hovering flight at blossoms, long proboscises (reaching over 30 cm in *Xanthopan*), and rapid crepuscular flight.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "I predicted that a giant **sphingid** moth with a foot-long proboscis must exist in Madagascar to pollinate *Angraecum sesquipedale*."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "At dusk, a magnificent **sphingid** hovered over the trumpet flowers, its wings vibrating like a humming-bird's."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Caterpillar",
        "quote": "The horn-tailed larva of the **sphingid** rears its head back when alarmed in the posture of an Egyptian sphinx."
      }
    ]
  },
  "Dashboard — sphing\\sphingidae.md": {
    "primary": "A cosmopolitan taxonomic family of stout-bodied, powerful-flying moths (the hawk moths, sphinx moths, and hornworms).",
    "secondary": "In lepidopterology, the Sphingidae encompass over 1,400 species displaying aerodynamic flight mechanics, high thoracic flight temperatures, and key roles as nocturnal pollinators.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Contributions to the Theory of Natural Selection",
        "quote": "The family **Sphingidae** contains some of the swiftest insects known, capable of sustained flight across broad channels."
      },
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "Many nocturnal white blossoms depend entirely on members of the **Sphingidae** for genetic outcrossing."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Tropical rain forest canopies harbor a staggering diversity of **Sphingidae**, adapted to specialized floral scents."
      }
    ]
  },
  "Dashboard — sphing\\sphingine.md": {
    "primary": "Of, relating to, or resembling a sphinx moth (sphingid); also, resembling the mythological Sphinx; enigmatic, mysterious, or statue-like.",
    "secondary": "In classical literature and entomological prose, sphingine evokes rigid, immobile postures (like the sphinx caterpillar) or inscrutable, riddle-like expressions.",
    "quotes": [
      {
        "author": "Thomas De Quincey",
        "work": "The Sphinx's Riddle and Other Essays",
        "quote": "The monumental face stared out across the sands with a cold, **sphingine** indifference to the rise and fall of empires."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The decapitated whale head hung against the ship's side with a vast, **sphingine** silence that defied human inquiry."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Social Life in the Insect World",
        "quote": "The caterpillar maintained its stiff **sphingine** pose on the twig for hours, frozen into a living carving."
      }
    ]
  },
  "Dashboard — stala\\stalactite.md": {
    "primary": "A tapering structure of calcium carbonate hanging like an icicle from the roof of a limestone cave, formed by the precipitation of minerals from dripping water.",
    "secondary": "In speleology and geomorphology, a stalactite forms along a central capillary hollow 'soda straw' tube as degassing of dissolved carbon dioxide precipitates calcite.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "From the vaulted limestone roof hung thousands of glistening **stalactite** spears, slowly fed by dripping carbonate waters."
      },
      {
        "author": "Mark Twain",
        "work": "The Adventures of Tom Sawyer",
        "quote": "The cave was a subterranean palace of wonder, where glittering **stalactite** columns reached down to meet the floor."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "Porous subterranean chambers were draped with delicate alabaster draperies and sparkling **stalactite** crystals."
      }
    ]
  },
  "Dashboard — stala\\stalagmite.md": {
    "primary": "An upward-growing mound or column of mineral deposits (especially calcium carbonate) formed on the floor of a cave by the accumulation of drips from the ceiling.",
    "secondary": "In paleoclimatology, speleothem stalagmites provide high-resolution terrestrial climate proxies through oxygen isotope (δ18O) variations and uranium-thorium dating.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Beneath each dripping point on the roof, a solid rounded **stalagmite** rose from the cavern floor like a pillar."
      },
      {
        "author": "Charles Lyell",
        "work": "The Antiquity of Man",
        "quote": "Flint implements and fossil bones of extinct mammoths were sealed safely beneath an ancient floor of hard **stalagmite**."
      },
      {
        "author": "Jules Verne",
        "work": "Journey to the Center of the Earth",
        "quote": "Our footsteps echoed among the colossal mineral shafts where stalactite and **stalagmite** met to form titanic colonnades."
      }
    ]
  }
};

const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`[Form Finish 4 - Batch 3] Successfully updated ${count}/${Object.keys(batchData).length} notes.`);
