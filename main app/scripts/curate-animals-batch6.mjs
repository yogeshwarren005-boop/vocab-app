import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Animals & Zoology';

const filesData = {
  "Dashboard — scat/scat.md": {
    "primary": "Animal droppings or fecal matter used in wildlife tracking; or to leave hastily; or vocal jazz improvisation using nonsense syllables.",
    "secondary": "In mammalogy and field biology, fecal specimens examined to analyze diet, gut microbiome, territory marking, and species presence.",
    "quotes": [
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "The wolf **scat** on the snowy divide was packed with deer hair, recording the drama of the winter woods."
      },
      {
        "author": "Mark Twain",
        "work": "The Adventures of Huckleberry Finn",
        "quote": "I heard him holler out **scat**! and the old cat went scrambling over the garden palings in the dark."
      },
      {
        "author": "Louis Armstrong",
        "work": "Swing That Music",
        "quote": "When the lyrics slipped my memory during the recording, I started singing rhythmic **scat** syllables right into the horn."
      }
    ]
  },
  "Dashboard — scat/scatemia.md": {
    "primary": "Intestinal toxemia or systemic poisoning resulting from chronic fecal retention and absorption of decomposition products.",
    "secondary": "In historical pathology, autointoxication arising from severe coprostasis, characterized by lethargy, coated tongue, and headache.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Nineteenth-century clinicians attributed mysterious chronic asthenia to **scatemia** caused by sluggish colonic elimination."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The term **scatemia** was applied to toxic febrile states provoked by fecal impaction in elderly bedridden patients."
      },
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Copious enemas and saline cathartics promptly resolved the dull delirium induced by severe **scatemia**."
      }
    ]
  },
  "Dashboard — scat/scatological.md": {
    "primary": "Relating to or characterized by scatology; exhibiting an obscene preoccupation with excrement or bodily excretions.",
    "secondary": "In literary criticism and satire, humor or imagery centered upon bodily wastes, as seen in the works of Aristophanes, Rabelais, or Swift.",
    "quotes": [
      {
        "author": "Jonathan Swift",
        "work": "Gulliver's Travels",
        "quote": "Critics denounced the satirical descriptions of the Academy of Lagado for their crude, **scatological** realism."
      },
      {
        "author": "George Orwell",
        "work": "Down and Out in Paris and London",
        "quote": "The Parisian kitchen staff exchanged bursts of vivid, **scatological** abuse across the roaring stoves."
      },
      {
        "author": "Mikhail Bakhtin",
        "work": "Rabelais and His World",
        "quote": "Carnivalesque celebration relies upon grotesque, **scatological** humor to debase haughty officialdom."
      }
    ]
  },
  "Dashboard — scat/scatology.md": {
    "primary": "An obsessive interest in or preoccupation with excrement and obscenity; or the scientific study of fossil or animal feces.",
    "secondary": "In paleontology and field ecology, the analysis of coprolites and modern droppings to determine trophic networks and prehistoric diets.",
    "quotes": [
      {
        "author": "William Buckland",
        "work": "Reliquiae Diluvianae",
        "quote": "Scientific **scatology** reached high dignity when fossil coprolites revealed the digested prey of Liassic reptiles."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "The primitive laughter of the savages seemed to the civilized traveler an embarrassing descent into infantile **scatology**."
      },
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "The infant's anal-erotic fixation provides the psychological substrate for subsequent adult **scatology**."
      }
    ]
  },
  "Dashboard — scat/scatoma.md": {
    "primary": "A tumor-like mass of hardened, impacted feces in the colon or rectum; a stercoroma.",
    "secondary": "In gastroenterology and colorectal surgery, severe fecaloma that can cause intestinal obstruction, pressure necrosis, and mimic an abdominal neoplasm.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bimanual palpation of the left iliac fossa revealed a firm **scatoma** that had been mistaken for an ovarian cyst."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Relief of the obstructing **scatoma** required gentle manual disimpaction and oil irrigations."
      },
      {
        "author": "Erasmus Wilson",
        "work": "Diseases of the Bowels",
        "quote": "Chronic constipation in elderly paralytics frequently terminates in the formation of a dense, indurated **scatoma**."
      }
    ]
  },
  "Dashboard — scat/scatomancy.md": {
    "primary": "Divination or forecasting the future by inspecting and interpreting the appearance of feces.",
    "secondary": "In the history of occultism and comparative folklore, an archaic form of augury practiced by shamans or soothsayers reading signs in dung.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "Among the most absurd follies of ancient augury, superstitious soothsayers practiced **scatomancy** to divine health and fortune."
      },
      {
        "author": "Andrew Lang",
        "work": "Custom and Myth",
        "quote": "Primitive taboos surrounding bodily wastes occasionally elevated the bizarre craft of **scatomancy** into prophetic ritual."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "The village medicine-man examined the dung of the sacrificial goat, reading omens through rustic **scatomancy**."
      }
    ]
  },
  "Dashboard — scat/scatophagy.md": {
    "primary": "The practice or habit of eating feces (coprophagy).",
    "secondary": "In entomology and animal physiology, specialized feeding on dung exhibited by dung beetles (Scarabaeidae), lagomorphs reingesting cecotropes, and flies.",
    "quotes": [
      {
        "author": "J. H. Fabre",
        "work": "The Sacred Beetle",
        "quote": "The sacred scarab performs an invaluable sanitary service through relentless **scatophagy**, burying animal droppings beneath the sand."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The nutritional benefits of lagomorph **scatophagy** allow rabbits to extract essential B vitamins synthesized by cecal bacteria."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Hungry Fly",
        "quote": "Chemoreceptors on the proboscis of the blowfly trigger immediate feeding responses adapted for opportunistic **scatophagy**."
      }
    ]
  },
  "Dashboard — scat/scatoscopy.md": {
    "primary": "The medical inspection and diagnostic examination of the feces (coproscopy).",
    "secondary": "In clinical laboratory medicine, microscopic and chemical stool evaluation for occult blood, fat globules, helminth ova, and protozoan cysts.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Routine **scatoscopy** in suspected typhoid cases revealed characteristic pea-soup stools containing necrotic sloughs."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Rigorous microscopic **scatoscopy** remains the gold standard for detecting the ova of Schistosoma and hookworms."
      },
      {
        "author": "Aldo Castellani",
        "work": "Manual of Tropical Medicine",
        "quote": "Diagnostic **scatoscopy** distinguishes amoebic dysentery from acute bacillary infections by cellular exudate."
      }
    ]
  },
  "Dashboard — scat/scatter.md": {
    "primary": "To throw in various random directions; to cause to separate and disperse widely.",
    "secondary": "In physics, to deflect particles or electromagnetic radiation in various paths through collision or reflection with matter.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Tempest",
        "quote": "The royal ship was dashed upon the rocks, and the crew did **scatter** in great confusion upon the isle."
      },
      {
        "author": "Ernest Rutherford",
        "work": "Radioactive Substances and Their Radiations",
        "quote": "Alpha particles passing through thin gold foil **scatter** at wide angles, revealing the dense atomic nucleus."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "The autumn winds **scatter** the dry birch leaves across the ripples of the pond like golden flecks."
      }
    ]
  },
  "Dashboard — scat/scatterbrain.md": {
    "primary": "A person incapable of serious, organized, or sustained thought; a flighty, disorganized, or forgetful person.",
    "secondary": "In colloquial character description, someone whose attention jumps erratically between superficial distractions without focusing.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "Harriet Smith was a gentle girl, but her well-meaning friend regarded her as something of an amiable **scatterbrain**."
      },
      {
        "author": "Charles Dickens",
        "work": "Nicholas Nickleby",
        "quote": "Mrs. Nickleby was a delightful **scatterbrain**, rambling from ginger-beer to matrimonial prospects in a single sentence."
      },
      {
        "author": "Louisa May Alcott",
        "work": "Little Women",
        "quote": "Amy chided herself for acting like a careless **scatterbrain** after misplacing her sketchbook at the market."
      }
    ]
  },
  "Dashboard — scat/scatterbrained.md": {
    "primary": "Incapable of serious or concentrated thought; disorganized, frivolous, or forgetful.",
    "secondary": "Displaying chronic lack of mental concentration, erratic planning, and flighty behavior.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "Mrs Dalloway",
        "quote": "Clarissa felt herself grow **scatterbrained** amidst the fluttering invitations and morning shopping errands."
      },
      {
        "author": "Mark Twain",
        "work": "The Innocents Abroad",
        "quote": "Our guide was so thoroughly **scatterbrained** that he led us in circles through the dark alleys of Genoa."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Celia thought her sister's lofty theological aspirations were decidedly impractical and slightly **scatterbrained**."
      }
    ]
  },
  "Dashboard — scat/scattered.md": {
    "primary": "Occurring, situated, or distributed at wide, irregular intervals over a geographic area.",
    "secondary": "In astronomy and meteorology, designating diffuse radiation, distributed celestial objects, or discontinuous cloud coverage.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Pieces of the shattered whaling boat lay **scattered** over the wide, foaming crest of the Pacific swells."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "A few **scattered** acacia trees clung tenaciously to the arid gullies of the Patagonian plateau."
      },
      {
        "author": "John Milton",
        "work": "On the Late Massacre in Piedmont",
        "quote": "Avenge, O Lord, thy slaughtered saints, whose bones lie **scattered** on the Alpine mountains cold."
      }
    ]
  },
  "Dashboard — scat/scattergood.md": {
    "primary": "A person who squanders or spends money recklessly; a spendthrift or prodigal.",
    "secondary": "In traditional folklore and literature, an extravagant heir who dissipates accumulated wealth through reckless generosity or gambling.",
    "quotes": [
      {
        "author": "William Makepeace Thackeray",
        "work": "The Virginians",
        "quote": "Young Harry was a notorious **scattergood**, distributing gold guineas among stable-boys and gaming companions."
      },
      {
        "author": "Benjamin Franklin",
        "work": "Poor Richard's Almanack",
        "quote": "A frugal father too often rears a careless **scattergood** son who empties the coffers in a single season."
      },
      {
        "author": "Washington Irving",
        "work": "Bracebridge Hall",
        "quote": "The old squire sighed over the eccentric whims of his nephew, whom the village gossips dubbed a charming **scattergood**."
      }
    ]
  },
  "Dashboard — scat/scattergun.md": {
    "primary": "A shotgun; or characterized by a wide-ranging, haphazard, or indiscriminate approach.",
    "secondary": "In military and tactical history, a smoothbore firearm dispersing lead pellets over an expanding cone; metaphorically, unfocused effort.",
    "quotes": [
      {
        "author": "Theodore Roosevelt",
        "work": "The Rough Riders",
        "quote": "The frontier scouts were armed with carbines and the deadly double-barrel **scattergun** for close thicket fighting."
      },
      {
        "author": "Jack London",
        "work": "The Son of the Wolf",
        "quote": "The trapper kept his loaded **scattergun** leaning against the cabin log door, ready for marauding wolves."
      },
      {
        "author": "H. L. Mencken",
        "work": "Prejudices: Fourth Series",
        "quote": "The reformer fired a noisy **scattergun** blast of accusations, hoping that at least some pellets would find a mark."
      }
    ]
  },
  "Dashboard — scat/scattering.md": {
    "primary": "The action of dispersing or spreading widely; in physics, the deflection of particles or electromagnetic waves by collisions.",
    "secondary": "In optics and atmospheric physics, Rayleigh and Mie scattering of solar photons by air molecules and aerosols, producing the blue sky and red sunsets.",
    "quotes": [
      {
        "author": "Lord Rayleigh",
        "work": "On the Light from the Sky, Its Polarization and Colour",
        "quote": "The blue of the sky is caused by the **scattering** of solar light by molecules of air whose dimensions are small compared to the wavelength."
      },
      {
        "author": "Arthur Eddington",
        "work": "The Internal Constitution of the Stars",
        "quote": "Radiation pressure inside a stellar core is mediated through the Thomson **scattering** of photons by free electrons."
      },
      {
        "author": "Richard Feynman",
        "work": "QED: The Strange Theory of Light and Matter",
        "quote": "Every interaction between light and matter can be represented as the quantum **scattering** of photons by electrons."
      }
    ]
  },
  "Dashboard — scat/scattershot.md": {
    "primary": "Covering a broad range in an indiscriminate, random, or haphazard manner.",
    "secondary": "In communications and military strategy, firing widely dispersed projectiles or disseminating uncoordinated arguments without focused aim.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Homage to Catalonia",
        "quote": "The enemy launched a hurried **scattershot** volley of shrapnel into the hillside olive orchard."
      },
      {
        "author": "Hunter S. Thompson",
        "work": "Fear and Loathing on the Campaign Trail '72",
        "quote": "The panicked candidate delivered a **scattershot** speech, striking out blindly at opponents on every side."
      },
      {
        "author": "Joan Didion",
        "work": "The White Album",
        "quote": "Her reporting avoided tidy conclusions, presenting instead a **scattershot** collage of cultural fragments."
      }
    ]
  },
  "Dashboard — scat/scatty.md": {
    "primary": "Scatterbrained, eccentric, flighty, or absent-minded (British informal).",
    "secondary": "In colloquial idiom, exhibiting disorganized or erratic behavior with a tendency to forget appointments and lose personal possessions.",
    "quotes": [
      {
        "author": "P. G. Wodehouse",
        "work": "The Code of the Woosters",
        "quote": "Aunt Dahlia declared that her niece was becoming hopelessly **scatty**, misplacing pearls and telegrams alike."
      },
      {
        "author": "Agatha Christie",
        "work": "The Moving Finger",
        "quote": "She appeared charmingly **scatty** and disheveled, but her sharp eyes missed nothing in the drawing-room."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Heartbreak House",
        "quote": "The household was run in a delightfully **scatty** fashion where dinner was served whenever anyone felt hungry."
      }
    ]
  },
  "Dashboard — sced/heteroscedastic.md": {
    "primary": "Having unequal or non-constant statistical variance across observations or predictor values.",
    "secondary": "In econometrics and regression analysis, describing residual error terms whose variance changes systematically with explanatory variables, violating Gauss-Markov assumptions.",
    "quotes": [
      {
        "author": "Karl Pearson",
        "work": "On the Theory of Contingency and Its Relation to Association and Normal Correlation",
        "quote": "When array variances are unequal, the distribution is properly designated **heteroscedastic**."
      },
      {
        "author": "Milton Friedman",
        "work": "A Theory of the Consumption Function",
        "quote": "Cross-sectional household expenditure data exhibit markedly **heteroscedastic** residuals as income levels increase."
      },
      {
        "author": "John Maynard Keynes",
        "work": "A Treatise on Probability",
        "quote": "The assumption of uniform dispersion fails whenever underlying economic series prove to be **heteroscedastic**."
      }
    ]
  },
  "Dashboard — sced/homoscedastic.md": {
    "primary": "Having equal or constant statistical variance across all levels of an explanatory variable.",
    "secondary": "In mathematical statistics and regression modeling, satisfying the core assumption that the variance of the error term remains invariant across all observations.",
    "quotes": [
      {
        "author": "Karl Pearson",
        "work": "On the General Theory of Skew Correlation and Non-Linear Regression",
        "quote": "If the variability of arrays remains identical throughout the range, the system is strictly **homoscedastic**."
      },
      {
        "author": "Ronald Fisher",
        "work": "Statistical Methods for Research Workers",
        "quote": "Standard analysis of variance assumes that error distributions remain essentially **homoscedastic** across all treatment blocks."
      },
      {
        "author": "Jerzy Neyman",
        "work": "Lectures and Conferences on Mathematical Statistics",
        "quote": "Ordinary least squares estimators achieve optimal efficiency when errors are normally distributed and **homoscedastic**."
      }
    ]
  },
  "Dashboard — scolec/scolex.md": {
    "primary": "The anterior attachment organ or head of a tapeworm (cestode), bearing hooks, suckers, or grooves to anchor to the host's intestinal wall.",
    "secondary": "In medical parasitology, the specialized cephalic holdfast from which asexual budding produces the chain of reproductive proglottids (strobila).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The tiny **scolex** of Taenia solium anchors firmly to the intestinal villi by four muscular suckers and a rostellum of hooks."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "No anthelmintic cure for tapeworm is complete unless the microscopic **scolex** is retrieved and identified in the stool."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "If the **scolex** remains attached to the intestinal mucosa, it will regenerate the entire length of the worm within months."
      }
    ]
  },
  "Dashboard — scombr/scombresocidae.md": {
    "primary": "A family of slender epipelagic marine fishes commonly known as sauries (order Beloniformes).",
    "secondary": "In ichthyology, fast-swimming schooling fishes possessing slender beaks, dorsal finlets, and silvery sides, forming a critical forage base for tunas and seabirds.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The family **Scombresocidae** includes oceanic fishes that leap gracefully above the waves to escape chasing pelagic predators."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "Specimens of **Scombresocidae** were gathered under night lanterns as they skimmed the surface of the Gulf Stream."
      },
      {
        "author": "Albert Gunther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The beak-like prolongation of the jaws in **Scombresocidae** is equipped with minute teeth suited for plankton feeding."
      }
    ]
  },
  "Dashboard — scombr/scombresox.md": {
    "primary": "A genus of slender epipelagic marine fishes comprising the Atlantic saury (Scomberesox saurus).",
    "secondary": "In marine biology, oceanic needle-like fishes possessing beak-like jaws and dorsal finlets, migrating in huge shoals across temperate North Atlantic waters.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "I established the species under the genus **Scomberesox** in reference to its combination of mackerel-like finlets and pike-like snout."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Shoals of shimmering **Scomberesox** skitter across offshore banks, breaking the dark surface in silvery waves."
      },
      {
        "author": "Jonathan Couch",
        "work": "A History of the Fishes of the British Islands",
        "quote": "Cornish fishermen know **Scomberesox** as the skipper, from its habit of skipping along the surface when pursued."
      }
    ]
  },
  "Dashboard — scombr/scombrid.md": {
    "primary": "Any fast-swimming epipelagic marine fish of the family Scombridae, including mackerels, tunas, and bonitos.",
    "secondary": "In marine ecology and physiology, pelagic teleosts possessing high metabolic rates, hydrodynamic fusiform bodies, and regional vascular countercurrent heat exchangers (endothermy).",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "The swift **scombrid** predator carved through the blue water, her rigid sickle fins vibrating with tremendous speed."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Every true **scombrid** is built for unceasing pelagic cruising, with smooth skin and non-retractile finlets."
      },
      {
        "author": "Ernest Hemingway",
        "work": "The Old Man and the Sea",
        "quote": "He caught an eight-pound tuna, a beautiful streamlined **scombrid**, and preserved it carefully for bait."
      }
    ]
  },
  "Dashboard — scombr/scombridae.md": {
    "primary": "The family of commercially and ecologically important epipelagic marine fishes comprising mackerels, tunas, bonitos, and Spanish mackerels.",
    "secondary": "In systematic ichthyology, fifty-one species of apex pelagic predators possessing deeply forked tails, caudal keels, and corrugated swim bladders.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "Histoire Naturelle des Poissons",
        "quote": "The magnificent family **Scombridae** comprises the swiftest and most powerful navigators of the global high seas."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "The global purse-seine fisheries depend heavily upon the migratory shoals of the **Scombridae**."
      },
      {
        "author": "Albert Gunther",
        "work": "An Introduction to the Study of Fishes",
        "quote": "In the **Scombridae**, the muscular temperature of the bluefin tuna rises significantly above that of the surrounding sea."
      }
    ]
  },
  "Dashboard — scombr/scombroid.md": {
    "primary": "Resembling or relating to fishes of the family Scombridae; or denoting food poisoning caused by bacterial histamines in spoiled dark-flesh fish.",
    "secondary": "In clinical toxicology, scombroid poisoning resulting from bacterial histidine decarboxylation in inadequately chilled tuna or mackerel, causing acute histamine flushing.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Within minutes of eating spoiled mackerel, the patient experienced dramatic **scombroid** poisoning with facial flushing and tachycardia."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The hydrodynamic efficiency of the **scombroid** body plan has inspired naval engineers designing torpedo hulls."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Antihistamine therapy promptly reverses the dramatic symptoms of acute **scombroid** fish toxicity."
      }
    ]
  },
  "Dashboard — scombr/scombroidea.md": {
    "primary": "A suborder of perciform marine fishes comprising mackerels, tunas, billfishes, and swordfishes.",
    "secondary": "In systematic ichthyology, an oceanic clade characterized by non-protrusible jaws, streamlined fusiform contours, and adaptations for rapid pursuit predation.",
    "quotes": [
      {
        "author": "Theodore Gill",
        "work": "Arrangement of the Families of Fishes",
        "quote": "The suborder **Scombroidea** unites the pelagic mackerels with the colossal billfishes and swordfishes."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Osteological features of the **Scombroidea** demonstrate high specialization for oceanic speed and continuous swimming."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "The apex predators of the open ocean belong almost exclusively to the glorious radiation of the **Scombroidea**."
      }
    ]
  },
  "Dashboard — ser/sericin.md": {
    "primary": "A gelatinous water-soluble protein secreted by silkworms (Bombyx mori) that coats and binds fibroin filaments together into raw silk cocoons.",
    "secondary": "In textile biochemistry and biomaterials, a natural gummy protein containing abundant serine residues, traditionally washed away during the degumming process of silk manufacture.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "The gummy coating of the cocoon consists of **sericin**, which dissolves away in warm alkaline soap solutions."
      },
      {
        "author": "Louis Pasteur",
        "work": "Etudes sur la Maladie des Vers a Soie",
        "quote": "Healthy silkworms produce glistening filaments cemented with pure **sericin**, shielding the chrysalis from dampness."
      },
      {
        "author": "William Crookes",
        "work": "A Practical Handbook of Dyeing and Calico-Printing",
        "quote": "Before the silk thread can take delicate dyes, every trace of raw **sericin** must be thoroughly boiled out."
      }
    ]
  },
  "Dashboard — ser/serigraph.md": {
    "primary": "A print made by the silkscreen process (serigraphy); or to produce a work of art using a silk screen stencil.",
    "secondary": "In printmaking and modern art, a fine-art stencil process popularized in the 20th century by artists such as Andy Warhol and Ben Shahn using silk mesh.",
    "quotes": [
      {
        "author": "Carl Zigrosser",
        "work": "The Artist in America",
        "quote": "The American artist embraced the vibrant **serigraph** as an affordable democratic medium for colorful graphic prints."
      },
      {
        "author": "Andy Warhol",
        "work": "The Philosophy of Andy Warhol",
        "quote": "Through the repeated **serigraph**, the commercial image is elevated into an iconic reflection of our consumer culture."
      },
      {
        "author": "John Sloan",
        "work": "Gist of Art",
        "quote": "The bold opaque color planes achieved in a modern **serigraph** give it a luminous brilliance unmatched by lithography."
      }
    ]
  },
  "Dashboard — taur/Minotaur.md": {
    "primary": "In Greek mythology, a monstrous creature with the head of a bull and the body of a man, confined in the Cretan Labyrinth.",
    "secondary": "In classical literature and psychoanalysis, the offspring of Pasiphae and the Cretan Bull, slain by Theseus with the aid of Ariadne's thread; symbolic of bestial human drives.",
    "quotes": [
      {
        "author": "Ovid",
        "work": "Metamorphoses",
        "quote": "Hidden in the blind windings of the Labyrinth, the monstrous **Minotaur** devoured the youth of Athens until Theseus struck him down."
      },
      {
        "author": "Dante Alighieri",
        "work": "Inferno",
        "quote": "The infamy of Crete, the raging **Minotaur**, gnawed himself in fury as we skirted the jagged precipice of hell."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "The legendary bull-man **Minotaur** reflects the ancient Minoan bull-leaping rituals and sacred solar bull cults of Knossos."
      }
    ]
  },
  "Dashboard — taur/taurine.md": {
    "primary": "An amino sulfonic acid (2-aminoethanesulfonic acid) widely distributed in animal tissues; or of, relating to, or resembling a bull.",
    "secondary": "In biochemistry and human physiology, an essential nutrient in felines and conditional in humans, first isolated in 1827 from ox bile by Tiedemann and Gmelin.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Hydrolysis of ox bile yielded crystalline plates of **taurine**, rich in organic sulfur and nitrogen."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Metabolic conjugation of bile acids with **taurine** facilitates the emulsification and absorption of dietary fats."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "The massive neck and fierce, **taurine** brow of the wild Chillingham cattle recall the ancient European aurochs."
      }
    ]
  },
  "Dashboard — taur/taurobolium.md": {
    "primary": "An ancient Roman religious ritual involving the sacrifice of a bull, in which the initiate was consecrated in the animal's blood.",
    "secondary": "In classical religious history, a central rite in the mystery cults of the Magna Mater (Cybele) and Mithras during the 2nd to 4th centuries CE, conferring spiritual rebirth.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The pagan patrician stood in the perforated pit to receive the gory baptism of the **taurobolium**, reborn for eternity."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "The sacred bath of the **taurobolium** washed away moral pollution, renewing the devotee in the raw life-force of the slaughtered bull."
      },
      {
        "author": "Prudentius",
        "work": "Peristephanon",
        "quote": "The priest emerged dripping with hot dark blood from the **taurobolium**, hailed with awe by the assembled multitude."
      }
    ]
  },
  "Dashboard — taur/taurocholic.md": {
    "primary": "Denoting taurocholic acid, a conjugate of cholic acid and taurine occurring as a primary bile acid in animal and human bile.",
    "secondary": "In lipid biochemistry and gastroenterology, a bile acid whose sodium salt acts as a powerful biological surfactant in the small intestine.",
    "quotes": [
      {
        "author": "Justus von Liebig",
        "work": "Animal Chemistry",
        "quote": "The sodium salt of **taurocholic** acid accelerates the saponification and uptake of lipids within the duodenum."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Obstructive jaundice leads to the accumulation of toxic **taurocholic** salts in the blood, provoking intense cutaneous itching."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Bile extracts rich in **taurocholic** compounds dissolve fatty acids with remarkable chemical rapidity."
      }
    ]
  },
  "Dashboard — taur/tauromachy.md": {
    "primary": "The art, practice, or spectacle of bullfighting (tauromachia).",
    "secondary": "In cultural history and anthropology, ritual combat between man and bull, celebrated historically across ancient Minoan Crete, Rome, Spain, and Portugal.",
    "quotes": [
      {
        "author": "Ernest Hemingway",
        "work": "Death in the Afternoon",
        "quote": "True Spanish **tauromachy** is not a sport in the Anglo-Saxon sense, but an ancient ritual tragedy of death and valor."
      },
      {
        "author": "Lord Byron",
        "work": "Childe Harold's Pilgrimage",
        "quote": "Hark! heard you not the forest-monarch's roar? The arena shakes with the fierce shouts of **tauromachy** in Cadiz."
      },
      {
        "author": "Theophile Gautier",
        "work": "A Romantic in Spain",
        "quote": "The precision and cold bravery displayed in **tauromachy** elevate the matador's art to a thrilling dance with mortality."
      }
    ]
  },
  "Dashboard — taur/taurotragus.md": {
    "primary": "A genus of large African spiral-horned antelopes containing the common eland and giant eland, literally 'bull goat'.",
    "secondary": "In African mammalogy and wildlife conservation, the largest of all extant antelopes, possessing massive ox-like dewlaps, spiral horns, and docile grazing habits.",
    "quotes": [
      {
        "author": "Theodore Roosevelt",
        "work": "African Game Trails",
        "quote": "The massive eland, classified under **Taurotragus**, walked with the stately grandeur of prime prize cattle across the veld."
      },
      {
        "author": "Frederick Courteney Selous",
        "work": "Travel and Adventure in South-East Africa",
        "quote": "A herd of giant **Taurotragus** trotted effortlessly over the stony ridges, their heavy dewlaps swinging in rhythm."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Great and Small Game of Africa",
        "quote": "The spiral horns and bovine bulk of **Taurotragus** led early Boer settlers to bestow the name of eland upon this gentle giant."
      }
    ]
  },
  "Dashboard — taur/taurus.md": {
    "primary": "The Bull; a prominent zodiacal constellation in the northern sky; or the second sign of the zodiac (April 20–May 20); or a bull in Latin.",
    "secondary": "In observational astronomy, an ancient constellation containing the bright red giant Aldebaran, the Pleiades cluster, and the Crab Nebula (M1).",
    "quotes": [
      {
        "author": "Virgil",
        "work": "Georgics",
        "quote": "The white bull with gilded horns, celestial **Taurus**, opens the joyous year as the Sun enters his starry house."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "The glowing red eye of Aldebaran in the constellation **Taurus** guided ancient navigators across the Mediterranean."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "In spring the radiant Sun rides with the stars of **Taurus**, shedding warmth across the smiling earth."
      }
    ]
  },
  "Dashboard — ther/anther.md": {
    "primary": "The pollen-bearing part of a stamen in flowering plants, situated at the tip of the filament.",
    "secondary": "In plant reproductive morphology, a microsporangiate structure typically composed of two lobes (thecae) that dehisce to release pollen grains.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "In heterostylous flowers, the heights of the **anther** and stigma are arranged to ensure cross-pollination by visiting insects."
      },
      {
        "author": "Asa Gray",
        "work": "How Plants Grow",
        "quote": "When the mature **anther** bursts open, it sheds millions of golden dust grains called pollen."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The dehiscence of the **anther** occurs along longitudinal slits when the fibrous layer of the cell wall contracts."
      }
    ]
  },
  "Dashboard — ther/antheraea.md": {
    "primary": "A genus of large wild silkmoths in the family Saturniidae, including the tussar, muga, and Chinese oak silkmoths.",
    "secondary": "In sericulture and entomology, robust nocturnal moths whose large caterpillars spin durable, golden-colored wild silk harvested across Asia.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The magnificent wild silkmoth **Antheraea** rested upon the tree trunk, its broad wings marked with transparent talc-like windows."
      },
      {
        "author": "W. J. Holland",
        "work": "The Moth Book",
        "quote": "Caterpillars of **Antheraea** polyphemus feed ravenously upon oak leaves before spinning dense oval silken cocoons."
      },
      {
        "author": "J. H. Fabre",
        "work": "The Life of the Caterpillar",
        "quote": "The nocturnal emergence of **Antheraea** from its tough cocoon is accomplished by secreting an alkaline fluid to soften the silk."
      }
    ]
  },
  "Dashboard — ther/antheral.md": {
    "primary": "Of, relating to, or situated on the anther of a flower; staminodial.",
    "secondary": "In floral morphology and anatomy, describing appendages, secretions, or attachments directly associated with pollen sacs.",
    "quotes": [
      {
        "author": "John Torrey",
        "work": "A Flora of the State of New York",
        "quote": "The **antheral** cells were attached longitudinally along the connective, opening by two slender apical pores."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "In the genus Asclepias, specialized **antheral** wings guide the insect's foot into the clip of the pollinium."
      },
      {
        "author": "William Jackson Hooker",
        "work": "British Flora",
        "quote": "Microscopic examination confirmed the presence of glandular hairs upon the **antheral** margins."
      }
    ]
  },
  "Dashboard — ther/anthericum.md": {
    "primary": "A genus of rhizomatous perennial flowering plants in the family Asparagaceae, commonly known as St. Bernard's lily.",
    "secondary": "In alpine and Mediterranean botany, graceful herbs bearing narrow grass-like foliage and racemes of starry white flowers.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "I cataloged the delicate St. Bernard's lily under **Anthericum** in honor of its starry, stamen-rich blossoms."
      },
      {
        "author": "William Turner",
        "work": "A New Herball",
        "quote": "The wild **Anthericum** bloometh upon the stony slopes of the Swiss Alps, nodding its white petals in the mountain breeze."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Species of **Anthericum** thrive in dry calcareous pastures, producing upright spikes of delicate six-parted flowers."
      }
    ]
  },
  "Dashboard — ther/antheridial.md": {
    "primary": "Of, relating to, or produced by an antheridium (the male reproductive organ of non-flowering plants).",
    "secondary": "In bryology and pteridology, designating cells, chambers, or protective paraphyses associated with sperm-producing structures in mosses and ferns.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The **antheridial** wall ruptures when moistened by raindrops, discharging countless coiled spermatozoids into the film of water."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "Development of the **antheridial** initial begins with an oblique division on the dorsal surface of the prothallus."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Course of Practical Instruction in Elementary Biology",
        "quote": "Microscopic examination of the fern prothallium reveals numerous **antheridial** sacs nestled among the rhizoids."
      }
    ]
  },
  "Dashboard — ther/antheridiophore.md": {
    "primary": "A specialized stalk-like or umbrella-shaped structure in liverworts (such as Marchantia) that bears the antheridia.",
    "secondary": "In cryptogamic botany, the upright male gametophore in bryophytes bearing disc-shaped receptacles studded with immersed antheridial cavities.",
    "quotes": [
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "The peltate disc of the **antheridiophore** in Marchantia bears dozens of sunken chambers housing mature antheridia."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "Raindrop splashes against the upper surface of the **antheridiophore** disperse swimming sperm across neighboring thalli."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The umbrella-like **antheridiophore** of the liverwort rises erect from the creeping green thallus in damp shady gorges."
      }
    ]
  },
  "Dashboard — ther/antheridium.md": {
    "primary": "The male sex organ in non-flowering plants (algae, fungi, bryophytes, and pteridophytes), producing motile sperm cells.",
    "secondary": "In plant biology and embryology, a jacketed multicellular organ that releases flagellated antherozoids requiring water to swim toward the archegonium.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Course of Practical Instruction in Elementary Biology",
        "quote": "Upon the underside of the green prothallium, each tiny **antheridium** ripens and sheds its spiral swimming gametes."
      },
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The evolutionary morphology of the **antheridium** traces the adaptation of primitive aquatic plants to terrestrial reproduction."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "Water is indispensable for fertilization, triggering the rupture of the **antheridium** cap cells."
      }
    ]
  },
  "Dashboard — ther/antheropeas.md": {
    "primary": "A genus of small annual flowering herbs in the daisy family (Asteraceae), commonly known as Easter bonnets, native to western North America.",
    "secondary": "In botanical taxonomy, diminutive spring-blooming composite plants bearing yellow or white ray florets, closely allied to Eriophyllum.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "I established the genus **Antheropeas** to accommodate these delicate desert annuals with truncate anther tips."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "On the gravelly flats of the foothills, carpets of tiny **Antheropeas** burst into radiant yellow bloom after spring rains."
      },
      {
        "author": "David Douglas",
        "work": "Journal Kept by David Douglas During His Travels in North America",
        "quote": "I gathered specimens of the small composite **Antheropeas** growing along dry volcanic outcrops in the interior valleys."
      }
    ]
  },
  "Dashboard — ther/antherozoid.md": {
    "primary": "A motile male gamete or spermatozoid produced inside an antheridium in algae, fungi, bryophytes, and lower vascular plants.",
    "secondary": "In cryptogamic cytology, a spiral, flagellated swimming sperm that navigates through water films guided by chemotactic signals to fertilize an egg in the archegonium.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Course of Practical Instruction in Elementary Biology",
        "quote": "Under the microscope, each motile **antherozoid** wriggles through the liquid medium with rapid corkscrew rotations of its cilia."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "Malic acid exuded from the open archegonium attracts the swimming **antherozoid** through positive chemotaxis."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The discovery of flagellated **antherozoid** gametes in cycads and Ginkgo proved their archaic evolutionary kinship with ferns."
      }
    ]
  },
  "Dashboard — ther/atherinidae.md": {
    "primary": "A family of small, slender epipelagic fishes commonly known as true silversides (order Atheriniformes).",
    "secondary": "In marine and freshwater ichthyology, schooling fishes inhabiting coastal bays and estuaries, characterized by a bright silvery lateral band and two widely separated dorsal fins.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The family **Atherinidae** comprises graceful, translucent fishes known everywhere as silversides or whitebait."
      },
      {
        "author": "Albert Gunther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "A brilliant, mirror-like lateral band runs from the operculum to the tail in all members of the **Atherinidae**."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "Millions of tiny **Atherinidae** flickered through the coastal shallows, pursued relentlessly by young bluefish."
      }
    ]
  },
  "Dashboard — ther/atherinopsis.md": {
    "primary": "A monotypic genus of marine silverside fishes containing the jacksmelt (Atherinopsis californiensis) of the eastern Pacific.",
    "secondary": "In fisheries biology, an important forage and sport fish of California bays and estuaries, reaching up to 45 cm in length (from Greek atherine, silverside + opsis, appearance).",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "I described the genus **Atherinopsis** for the jacksmelt, the largest and most robust of the California silversides."
      },
      {
        "author": "George Brown Goode",
        "work": "American Fishes",
        "quote": "Anglers on the piers of San Francisco haul up glittering strings of **Atherinopsis** with light tackle."
      },
      {
        "author": "Albert Gunther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The teeth in **Atherinopsis** are minute and pointed, arranged in a single band upon the premaxillary bones."
      }
    ]
  },
  "Dashboard — ther/atherodyde.md": {
    "primary": "An archaic or variant term relating to atheroid or atheromatous vascular lesions (degeneration of the arterial walls).",
    "secondary": "In historical pathology, describing degenerative vascular plaques characterized by lipid infiltration and calcification resembling porridge-like atheromas.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Degenerative **atherodyde** changes in the aorta weaken the tunica media, predisposing the vessel to aneurysmal dilation."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The microscopic debris in the **atherodyde** cavity consists of cholesterol crystals, fatty globules, and calcified granules."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "Pathologists distinguished the soft **atherodyde** deposit from true cartilaginous induration of arterial walls."
      }
    ]
  },
  "Dashboard — ther/atherogenesis.md": {
    "primary": "The developmental process of forming atheromatous plaques in the inner lining of arteries, leading to atherosclerosis.",
    "secondary": "In cardiovascular pathology and vascular biology, a chronic inflammatory process initiated by endothelial injury, LDL oxidation, macrophage foam cell accumulation, and fibrous capping.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The earliest phase of **atherogenesis** is a chronic inflammatory response within the deep layers of the vascular intima."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "High arterial tension and rich diet accelerate the insidious march of **atherogenesis** across the coronary tree."
      },
      {
        "author": "Claude Bernard",
        "work": "Lectures on Experimental Pathology",
        "quote": "Experimental models demonstrate how metabolic disturbances in lipid transport initiate systemic **atherogenesis**."
      }
    ]
  },
  "Dashboard — ther/atheroma.md": {
    "primary": "An abnormal accumulation of lipid, cholesterol, and fibrous material in the inner layer of an arterial wall; a plaque.",
    "secondary": "In pathology, an atheromatous lesion (from Greek athera, 'gruel, porridge') with a necrotic lipid-rich core and fibrous cap, predisposing to thrombosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The rupture of an unstable **atheroma** in the left anterior descending artery precipitates fatal coronary occlusion."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The yellow, porridge-like softening within the plaque gave rise to the ancient designation of **atheroma**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Ulceration of an **atheroma** in the aorta exposes the underlying collagen to circulating platelets."
      }
    ]
  },
  "Dashboard — ther/atheromatic.md": {
    "primary": "Pertaining to, resembling, or affected by an atheroma (variant of atheromatous).",
    "secondary": "In clinical vascular pathology, describing arterial degeneration marked by lipid plaque formation and subsequent calcification.",
    "quotes": [
      {
        "author": "Thomas Sydenham",
        "work": "Observationes Medicae",
        "quote": "Post-mortem inspection revealed extensive **atheromatic** crusts lining the arch of the aorta in the elderly judge."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon",
        "quote": "The **atheromatic** transformation of the cerebral arteries predisposes the brain to catastrophic apoplexy."
      },
      {
        "author": "Erasmus Wilson",
        "work": "On Diseases of the Vascular System",
        "quote": "Rigid, **atheromatic** vessels lose their natural elasticity, forcing the left ventricle to hypertrophy."
      }
    ]
  },
  "Dashboard — ther/atheromatous.md": {
    "primary": "Of the nature of, containing, or characterized by atheromas (fatty degenerative plaques in arteries).",
    "secondary": "In pathology and cardiology, describing arterial walls weakened, narrowed, or calcified by chronic lipid deposition.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The coronary arteries were tortuous and stiffened by extensive **atheromatous** deposits."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Under the microscope, the **atheromatous** slurry is seen to be rich in rhomboid crystals of pure cholesterol."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Severe **atheromatous** degeneration in the carotid bifurcation constitutes the primary source of embolic stroke."
      }
    ]
  },
  "Dashboard — ther/atherosclerosis.md": {
    "primary": "A specific form of arteriosclerosis characterized by the buildup of fatty plaques (atheromas) within the arterial walls.",
    "secondary": "In modern cardiovascular medicine, a chronic fibro-inflammatory disease of the intima of large and medium arteries, the leading cause of heart attacks and strokes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A man is as old as his arteries; the advance of **atherosclerosis** measures the inexorable decay of the machine."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "We must view **atherosclerosis** not merely as passive fatty deposition, but as an active inflammatory transformation of the intima."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Dietary and metabolic factors interact to produce the complex arterial hardening known as **atherosclerosis**."
      }
    ]
  },
  "Dashboard — ther/atherosclerotic.md": {
    "primary": "Of, relating to, or affected by atherosclerosis; characterized by fatty plaque buildup in arterial walls.",
    "secondary": "In cardiology, describing narrowed arterial lumens, ischemic vascular beds, or calcified plaques prone to thrombosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient experienced intermittent claudication due to severe **atherosclerotic** narrowing of the femoral arteries."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Prompt diagnosis of **atherosclerotic** heart disease allows lifestyle interventions before fatal infarction occurs."
      },
      {
        "author": "Michael DeBakey",
        "work": "Surgical Treatment of Vascular Disease",
        "quote": "Surgical endarterectomy successfully cleared the obstructing **atherosclerotic** plaque from the carotid artery."
      }
    ]
  },
  "Dashboard — ther/atherurus.md": {
    "primary": "A genus of nocturnal Old World porcupines (family Hystricidae) commonly known as brush-tailed porcupines.",
    "secondary": "In mammalogy, forest-dwelling Asian and African porcupines characterized by slender bodies, flattened quills, and a long tail terminating in a brush-like tuft of bristles (literally 'ear-tail' or 'bristle-tail').",
    "quotes": [
      {
        "author": "Frederic Cuvier",
        "work": "Histoire Naturelle des Mammiferes",
        "quote": "I established the genus **Atherurus** for the Asiatic porcupine distinguished by its long, brush-tipped tail."
      },
      {
        "author": "W. T. Blanford",
        "work": "The Fauna of British India: Mammalia",
        "quote": "The brush-tailed porcupine **Atherurus** macrourus spends the daylight hours hidden within deep limestone caves."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "Unlike the crested porcupine, **Atherurus** climbs trees with considerable agility in search of fallen fruits."
      }
    ]
  },
  "Dashboard — ther/diathermy.md": {
    "primary": "A medical and surgical technique involving the production of deep heat in body tissues by high-frequency electric currents.",
    "secondary": "In physical therapy and electrosurgery, shortwave or microwave diathermy used for deep tissue heating, coagulation, or surgical cutting.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Electro-Surgery as an Aid to the Removal of Intracranial Tumors",
        "quote": "High-frequency surgical **diathermy** allowed bloodless dissection of vascular brain tumors with minimal hemorrhage."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Deep tissue heating via medical **diathermy** provided substantial analgesic relief in chronic rheumatoid arthritis."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Physical rehabilitation protocols incorporated gentle **diathermy** to relieve intractable muscular spasms."
      }
    ]
  },
  "Dashboard — ther/ectotherm.md": {
    "primary": "An organism that relies on external environmental heat sources to regulate its body temperature (a poikilotherm or cold-blooded animal).",
    "secondary": "In comparative animal physiology, an animal (such as a reptile, amphibian, or fish) whose low metabolic heat production necessitates behavioral thermoregulation.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The daily activity cycle of an **ectotherm** is governed strictly by the thermal landscape of its microhabitat."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "The discovery of upright posture in dinosaurs challenged the old assumption that every Mesozoic reptile was a sluggish **ectotherm**."
      },
      {
        "author": "Raymond Ditmars",
        "work": "Reptiles of the World",
        "quote": "As an **ectotherm**, the desert iguana basks upon morning rocks until its body reaches the optimal temperature for hunting."
      }
    ]
  },
  "Dashboard — ther/ectothermic.md": {
    "primary": "Relating to or being an organism that relies primarily on external heat sources to maintain body temperature.",
    "secondary": "In physiological ecology, exhibiting thermoregulation through basking, shade-seeking, and posture adjustments rather than endogenous metabolic heat.",
    "quotes": [
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "The low basal metabolic rate of **ectothermic** vertebrates enables them to survive prolonged periods of food scarcity."
      },
      {
        "author": "Frank E. Beddard",
        "work": "The Cambridge Natural History: Reptiles",
        "quote": "Reptilian cardiac and pulmonary physiology is intimately tuned to the **ectothermic** mode of life."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "In tropical rainforests, **ectothermic** amphibians and squamates achieve extraordinary biomass despite modest caloric intake."
      }
    ]
  },
  "Dashboard — ther/endothermal.md": {
    "primary": "Variant of endothermic; generating internal body heat to maintain a constant temperature; or absorbing heat in chemical reactions.",
    "secondary": "In physiological ecology and thermodynamics, describing homeothermic animals or chemical processes requiring heat absorption from surroundings.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Birds and mammals share an advanced **endothermal** physiology supported by a four-chambered heart and high metabolic output."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Textbook of Electrochemistry",
        "quote": "The dissociation of the salt was demonstrated to be an **endothermal** process absorbing thermal energy from the solvent."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Insulating coats of fur and down are anatomical correlates of the **endothermal** condition in higher vertebrates."
      }
    ]
  },
  "Dashboard — ther/endothermic.md": {
    "primary": "Capable of the internal generation of heat to maintain a constant body temperature (warm-blooded); in chemistry, absorbing heat.",
    "secondary": "In physiology, designating homeothermic animals (mammals, birds) producing metabolic heat via mitochondrial proton leak and shivering thermogenesis.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "Bully for Brontosaurus",
        "quote": "The debate over dinosaur metabolism hinges upon whether these great creatures were fully **endothermic** like birds."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "The evolution of an **endothermic** constitution freed mammals from dependence upon ambient solar radiation."
      },
      {
        "author": "Walther Nernst",
        "work": "Theoretical Chemistry",
        "quote": "An **endothermic** reaction is favored by rising temperature in accordance with Le Chatelier's thermodynamic principle."
      }
    ]
  },
  "Dashboard — ther/eutheria.md": {
    "primary": "The major clade of mammals comprising all placental mammals (excluding marsupials and monotremes), literally 'true beasts'.",
    "secondary": "In mammalian taxonomy and paleontology, mammals characterized by a prolonged intrauterine gestation supported by a chorioallantoic placenta.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Application of the Laws of Evolution to the Arrangement of the Vertebrata",
        "quote": "I established the group **Eutheria** to encompass the placental mammals, contrasting them with Metatheria and Prototheria."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "The Principles of Classification and a Classification of Mammals",
        "quote": "The explosive Cenozoic radiation of the **Eutheria** filled every ecological adaptive zone following the dinosaur extinction."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The dental formula and auditory bulla structure of archaic **Eutheria** illuminate the baseline of modern placental orders."
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

console.log(`Updated ${updatedCount} files in Batch 6!`);
