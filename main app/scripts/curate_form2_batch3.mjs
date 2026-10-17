import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — cross\\crosse.md": {
    "primary": "A hooked stick with an oval network pocket used in lacrosse, or an ecclesiastical pastoral crook.",
    "secondary": "In sporting history and ethnography, the traditional curved racket originally developed by North American indigenous nations for the ball-and-stick game of lacrosse.",
    "quotes": [
      {
        "author": "George Catlin",
        "work": "Letters and Notes on the Manners, Customs, and Condition of the North American Indians",
        "quote": "Each Choctaw warrior held his webbed **crosse** poised in readiness as the ball was tossed high into the air."
      },
      {
        "author": "Francis Parkman",
        "work": "The Conspiracy of Pontiac",
        "quote": "Under cover of a spirited game with the netted **crosse**, the warriors drew near the gates of Fort Michilimackinac."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "Our guide pointed out ash saplings seasoned specifically to fashion the bent frame of a hunter's **crosse**."
      }
    ]
  },
  "Dashboard — cross\\crossed.md": {
    "primary": "Traversed, passed over, intersected, or placed transversely.",
    "secondary": "Thwarted or opposed in purpose; or produced by the hybridization of different strains or varieties.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Romeo and Juliet",
        "quote": "A pair of star-**crossed** lovers take their life, whose misadventured piteous overthrows do with their death bury their parents' strife."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "When two distinct varieties of pigeons are **crossed**, the ancestral rock pigeon plumage frequently reappears in the progeny."
      },
      {
        "author": "Joseph Conrad",
        "work": "Heart of Darkness",
        "quote": "We sat in silence while darkness fell, and shadows **crossed** the glassy surface of the Thames."
      }
    ]
  },
  "Dashboard — cross\\crossing.md": {
    "primary": "The act of traversing an intersection, body of water, or boundary; an intersection where paths or roads meet.",
    "secondary": "In genetics and agriculture, the deliberate interbreeding or hybridization of two distinct varieties, strains, or species.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "The **crossing** of two flowers belonging to different plants almost invariably yields larger and more robust seedlings."
      },
      {
        "author": "Mark Twain",
        "work": "Life on the Mississippi",
        "quote": "A Mississippi pilot must know every shifting sandbar and treacherous river **crossing** in pitch darkness."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "Footsteps mingle at the crowded street **crossing**, weaving fleeting patterns on the pavement."
      }
    ]
  },
  "Dashboard — cross\\crossly.md": {
    "primary": "In an irritable, petulant, ill-tempered, or peevish manner.",
    "secondary": "In an intersecting or transverse direction; contrarily or transversely.",
    "quotes": [
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "Bessie spoke **crossly** to the children when they disrupted her mending by the parlor hearth."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "Mrs. Bennet replied **crossly** that nobody in the house showed the least sympathy for her poor nerves."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Pip was answered **crossly** whenever he ventured to inquire into the mysterious benefactor's designs."
      }
    ]
  },
  "Dashboard — cross\\crossopterygian.md": {
    "primary": "Pertaining to or belonging to the Crossopterygii, the clade of lobe-finned bony fishes.",
    "secondary": "In vertebrate paleontology and evolutionary morphology, describing sarcopterygian fishes possessing lobed fins supported by skeletal elements homologous to tetrapod limbs.",
    "quotes": [
      {
        "author": "Alfred Romer",
        "work": "The Vertebrate Body",
        "quote": "The ancestral Devonian **crossopterygian** possessed internal nostrils and limb bones directly ancestral to amphibians."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Hen's Teeth and Horse's Toes",
        "quote": "The enduring anatomical architecture of the **crossopterygian** fin illustrates how ancient structures preadapt organisms for land life."
      },
      {
        "author": "J. L. B. Smith",
        "work": "Old Fourlegs",
        "quote": "Every museum curator recognized the famous five-lobed tail of the **crossopterygian** coelacanth as a priceless relic."
      }
    ]
  },
  "Dashboard — cross\\crossover.md": {
    "primary": "The act, process, or instance of passing from one style, category, or sphere to another.",
    "secondary": "In genetics, the reciprocal exchange of genetic material between non-sister chromatids during meiotic prophase I (crossing over).",
    "quotes": [
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Mechanism of Mendelian Heredity",
        "quote": "A single **crossover** event between homologous chromosome strands alters the linkage values of adjacent genes."
      },
      {
        "author": "Barbara McClintock",
        "work": "A Cytological and Genetical Study of Multiple Allelomorphs in Maize",
        "quote": "Physical evidence of chromosomal **crossover** was confirmed by tracking morphological knobs under the microscope."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "Chromosomal inversions suppress effective **crossover** recombination, preserving co-adapted gene complexes in wild populations."
      }
    ]
  },
  "Dashboard — cross\\crossroad.md": {
    "primary": "A road that intersects another main road, or a minor connecting road linking two primary highways.",
    "secondary": "A point of intersection; figuratively, a crucial turning point or decisive juncture demanding an irrevocable choice.",
    "quotes": [
      {
        "author": "Robert Frost",
        "work": "Mountain Interval",
        "quote": "Two paths met at the lone **crossroad**, where the traveler paused before deciding which course to pursue."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "She waited in the gathering dusk by the lonely **crossroad**, listening anxiously for the rumble of the carrier's wagon."
      },
      {
        "author": "William Faulkner",
        "work": "Light in August",
        "quote": "A dilapidated store stood at the dusty **crossroad**, serving as the silent social hub for neighboring tenant farmers."
      }
    ]
  },
  "Dashboard — cross\\crossroads.md": {
    "primary": "An intersection where two or more roads cross each other.",
    "secondary": "A pivotal crisis or critical turning point in life, history, or strategy where a crucial decision must be made.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Modern civilization stands at a historic **crossroads**, choosing between democratic equality in freedom or equal servitude."
      },
      {
        "author": "Winston Churchill",
        "work": "The Second World War: Their Finest Hour",
        "quote": "The nation had reached a desperate **crossroads** where steadfast endurance was the only alternative to extinction."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Dorothea found herself standing at the spiritual **crossroads** of her youth, uncertain which duty commanded her conscience."
      }
    ]
  },
  "Dashboard — cross\\crossruff.md": {
    "primary": "A play in bridge or whist where partners alternate trumping cards in each other's void suits.",
    "secondary": "In contract bridge tactics, an offensive strategy designed to maximize trick counts by executing consecutive trumps from both hands.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Murders in the Rue Morgue",
        "quote": "An accomplished card player anticipates the devastating execution of a **crossruff** by tracking discards with microscopic vigilance."
      },
      {
        "author": "Somerset Maugham",
        "work": "Cakes and Ale",
        "quote": "The vicar was triumphant when he established a neat **crossruff**, scooping up four unexpected tricks before his opponents realized their peril."
      },
      {
        "author": "Ian Fleming",
        "work": "Moonraker",
        "quote": "Bond timed the **crossruff** flawlessly, depriving Drax of his lingering club honors at the decisive rubber."
      }
    ]
  },
  "Dashboard — cross\\crosstalk.md": {
    "primary": "Unwanted electrical or electromagnetic interference between adjacent signal paths or communication channels.",
    "secondary": "In communications and biochemistry, mutual conversational banter; or the cross-activation between distinct biochemical signaling pathways in a cell.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Shielding and signal multiplexing are engineered to minimize **crosstalk** between adjacent telephone transmission pairs."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "Spurious **crosstalk** within neural circuits can degrade sensory fidelity and induce feedback instability."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "Intricate **crosstalk** between kinase cascades ensures that the cell integrates multiple extracellular growth signals."
      }
    ]
  },
  "Dashboard — cross\\crosstie.md": {
    "primary": "A transverse timber, concrete, or steel sleeper laid beneath railroad rails to maintain track gauge and distribute load.",
    "secondary": "In civil and mechanical engineering, any transverse structural brace or tie that secures parallel members against lateral displacement.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "We do not ride on the railroad; it rides upon us. Did you ever think what those sleepers are that underlie the railroad? Each one is a man, an Irishman, or a Yankee man. The rails are laid on them, and they are covered with sand, and the cars run smoothly over them. Every **crosstie** is a human life laid down."
      },
      {
        "author": "Walt Whitman",
        "work": "To a Locomotive in Winter",
        "quote": "Fierce-throated beauty! Roll through the gale, jarring each sturdy **crosstie** beneath thy ponderous driving wheels."
      },
      {
        "author": "John Steinbeck",
        "work": "The Grapes of Wrath",
        "quote": "Men walked the railway line, stepping from one creosoted **crosstie** to the next in their trek toward California."
      }
    ]
  },
  "Dashboard — cross\\crosstown.md": {
    "primary": "Extending, traveling, or situated across a town or city, typically perpendicular to the principal avenues.",
    "secondary": "In urban transportation, designating transit routes, buses, or expressways that connect opposite city districts across the urban core.",
    "quotes": [
      {
        "author": "Lewis Mumford",
        "work": "The Culture of Cities",
        "quote": "A congested metropolis requires efficient **crosstown** arterials to relieve pressure on radiating radial avenues."
      },
      {
        "author": "E. B. White",
        "work": "Here Is New York",
        "quote": "Taking a **crosstown** bus in midtown Manhattan during the midday rush can be slower than traveling by foot."
      },
      {
        "author": "John Dos Passos",
        "work": "Manhattan Transfer",
        "quote": "The clanging yellow streetcar rattled along the **crosstown** tracks, carrying commuters toward the East River docks."
      }
    ]
  },
  "Dashboard — cross\\uncross.md": {
    "primary": "To change from a crossed position to an open or parallel one; to separate things that are crossed.",
    "secondary": "To undo or reverse an intersection, crossing, or folded bodily posture.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "Mr. Knightley shifted in his armchair and began to **uncross** his legs as the conversation took a more serious turn."
      },
      {
        "author": "Henry James",
        "work": "The Portrait of a Lady",
        "quote": "She watched him deliberately **uncross** his arms and lean forward to inspect the contested miniature."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Lydgate paused to **uncross** his hands from behind his back before offering his clinical opinion."
      }
    ]
  },
  "Dashboard — cross\\uncrossed.md": {
    "primary": "Not crossed, traversed, or intersected; not folded across.",
    "secondary": "Not opposed or thwarted; in genetics, purebred or unhybridized.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "The **uncrossed** parental stock produced seeds with notably lower germination vitality than the outbred hybrids."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "Vast leagues of **uncrossed** ocean stretched out toward the Antarctic ice sheet in unmapped desolation."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Mayor of Casterbridge",
        "quote": "Henchard strode through the gates with his formidable will still **uncrossed** by any rival authority."
      }
    ]
  },
  "Dashboard — crypt\\apocrypha.md": {
    "primary": "Biblical writings not accepted into the canonical authorized Jewish or Protestant scriptures, included in the Septuagint and Vulgate.",
    "secondary": "Writings, narratives, or statements of dubious authenticity, uncertain authority, or spurious authorship.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Critical scholarship separates authentic history from the fabulous fables and ecclesiastical **apocrypha** of dark ages."
      },
      {
        "author": "John Milton",
        "work": "Areopagitica",
        "quote": "The fathers of the church read the ancient **apocrypha** with discerning wisdom, extracting virtue without superstition."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "Many popular anecdotes regarding Dryden belong properly to literary **apocrypha**, lacking contemporary testimony."
      }
    ]
  },
  "Dashboard — crypt\\apocryphal.md": {
    "primary": "Of doubtful authenticity or questionable veracity, although widely circulated as true.",
    "secondary": "In textual criticism, pertaining to, resembling, or belonging to the biblical Apocrypha.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The historian must cautiously discard the **apocryphal** marvels invented by credulous monks centuries after the event."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "The narrative of King Alfred burning the cakes remains delightfully memorable, however **apocryphal** its origin."
      },
      {
        "author": "David Hume",
        "work": "An Enquiry Concerning Human Understanding",
        "quote": "Miracles alleged in remote antiquity resting upon **apocryphal** testimony cannot establish philosophical conviction."
      }
    ]
  },
  "Dashboard — crypt\\archaeocryptography.md": {
    "primary": "The study, decipherment, and analysis of ancient ciphers, hidden inscriptions, and historical cryptographic texts.",
    "secondary": "In historical epigraphy and forensic archaeology, the methodological reconstruction of obsolete code systems and steganographic inscriptions found on ancient artifacts.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Pioneering work in **archaeocryptography** unlocked the Spartan scytale and early Mesopotamian secret cuneiform tablets."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "Techniques from modern **archaeocryptography** prove that even monoalphabetic substitutions in forgotten languages surrender to frequency analysis."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "The analytical discipline required for **archaeocryptography** mirrors that needed to break mechanized polyalphabetic rotors."
      }
    ]
  },
  "Dashboard — crypt\\crypt.md": {
    "primary": "An underground chamber, vault, or chapel, especially beneath the floor of a church, commonly used as a burial place.",
    "secondary": "In human and vertebrate anatomy, a small tubular glandular pit or recess, such as the crypts of Lieberkühn in the intestinal mucosa.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Cask of Amontillado",
        "quote": "We passed through a range of low arches, descended, passed on, and descending again, arrived at a deep **crypt**."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The somber Norman **crypt** supported the massive piers above with subterranean solidity."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Deep within each mucosal **crypt** of the small intestine, specialized secretory cells produce digestive enzymes."
      }
    ]
  },
  "Dashboard — crypt\\cryptacanthodes.md": {
    "primary": "A genus of elongated, burrowing marine fishes known as wrymouths, belonging to the family Cryptacanthodidae.",
    "secondary": "In marine ichthyology, benthic North Atlantic and Pacific fishes characterized by a sharp upturned mouth, eel-like body, and habit of excavating mud burrows.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The wrymouth, **Cryptacanthodes** maculatus, conceals its elongated body in complex subterranean galleries on muddy bottoms."
      },
      {
        "author": "Henry Bryant Bigelow",
        "work": "Fishes of the Gulf of Maine",
        "quote": "Trawl hauls from soft silt occasionally bring up specimens of **Cryptacanthodes**, snapping their oblique jaws with ferocity."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries",
        "quote": "Fishermen frequently encounter the spotted wrymouth, **Cryptacanthodes**, hiding inside submerged lobster pots."
      }
    ]
  },
  "Dashboard — crypt\\cryptanalysis.md": {
    "primary": "The art and science of analyzing and deciphering encrypted information without access to the secret key.",
    "secondary": "In computational mathematics and national intelligence, the mathematical techniques used to break cryptographic algorithms and uncover underlying plaintext.",
    "quotes": [
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Mathematical **cryptanalysis** enables the analyst to deduce rotor wirings through statistical weighting of probable cribs."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "Theoretical **cryptanalysis** evaluates how much ciphertext is required before a unique decipherment becomes mathematically certain."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Bletchley Park transformed **cryptanalysis** from a solitary puzzle-solving art into a massive mechanized factory of intellect."
      }
    ]
  },
  "Dashboard — crypt\\cryptanalyst.md": {
    "primary": "A specialist trained in cryptanalysis who deciphers secret codes and ciphers without prior knowledge of the key.",
    "secondary": "In intelligence and cybersecurity, a mathematician or computer scientist who evaluates the security of cryptographic ciphers or recovers plaintext.",
    "quotes": [
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "The **cryptanalyst** relies upon consistent operator errors and stereotypic message headings to insert the fatal wedge."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "William Friedman demonstrated how a dedicated **cryptanalyst** could reconstruct the Purple cipher machine without ever seeing it."
      },
      {
        "author": "Claude Shannon",
        "work": "The Mathematical Theory of Communication",
        "quote": "From the viewpoint of the **cryptanalyst**, every encrypted communication presents a noisy statistical puzzle."
      }
    ]
  },
  "Dashboard — crypt\\cryptanalytic.md": {
    "primary": "Pertaining to, involving, or utilizing the principles of cryptanalysis.",
    "secondary": "In computational information theory, describing methodologies (such as linear or differential attacks) deployed to assess or break cryptosystems.",
    "quotes": [
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Our mechanical Bombe executed rapid **cryptanalytic** searches across thousands of possible wheel combinations every minute."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The breaking of the Zimmermann Telegram stands as one of the most consequential **cryptanalytic** triumphs in modern history."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "A cipher possessing an infinite unicity distance resists every conceivable **cryptanalytic** approach."
      }
    ]
  },
  "Dashboard — crypt\\cryptanalytics.md": {
    "primary": "The techniques, operations, and analytical procedures employed in cryptanalysis.",
    "secondary": "In cybersecurity and military communications, the systematic quantitative processes applied to intercept, parse, and decipher encrypted transmissions.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Modern **cryptanalytics** blends high-speed digital computation with profound theorems from algebraic number theory."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "The mathematical foundation of **cryptanalytics** requires calculating conditional entropy across expanding message sequences."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Without rigorous **cryptanalytics**, the stream of military teleprinter traffic would remain an impenetrable wall of noise."
      }
    ]
  },
  "Dashboard — crypt\\crypteia.md": {
    "primary": "An ancient Spartan institution and secret police force in which young men carried out covert surveillance and killings of Helots.",
    "secondary": "In classical Greek history and political philosophy, a brutal state-sponsored survival rite of passage designed to terrorize the subjugated agricultural population.",
    "quotes": [
      {
        "author": "Plutarch",
        "work": "Life of Lycurgus",
        "quote": "In the operation of the **Crypteia**, the magistrates dispatched the most discreet youths into the countryside armed with daggers."
      },
      {
        "author": "Plato",
        "work": "Laws",
        "quote": "The arduous training of the **Crypteia** inures young citizens to extreme endurance, wandering barefoot in winter without bedding."
      },
      {
        "author": "George Grote",
        "work": "A History of Greece",
        "quote": "Spartan terror was institutionalized through the **Crypteia**, maintaining perpetual vigilance over a restless slave caste."
      }
    ]
  },
  "Dashboard — crypt\\cryptical.md": {
    "primary": "Mysterious, obscure, or occult in meaning; enigmatic; cryptographic.",
    "secondary": "In natural history and zoology, serving to conceal or hide, as in cryptic camouflage or coloration.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Gold-Bug",
        "quote": "The parchment revealed a series of **cryptical** characters drawn with sympathetic ink that vanished as the paper cooled."
      },
      {
        "author": "Sir Thomas Browne",
        "work": "Pseudodoxia Epidemica",
        "quote": "The ancient Egyptians shadowed their sacred truths beneath **cryptical** hieroglyphs inaccessible to the vulgar crowd."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Return of the Native",
        "quote": "His silence conveyed a **cryptical** reproach that wounded Eustacia more deeply than any overt criticism."
      }
    ]
  },
  "Dashboard — crypt\\cryptically.md": {
    "primary": "In a cryptic, enigmatic, obscure, or secretive manner.",
    "secondary": "So as to disguise meaning or avoid detection, whether verbally or through concealing coloration.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Dancing Men",
        "quote": "The drawings were inscribed **cryptically** in chalk upon the sundial, defying the comprehension of all who saw them."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "Marlow paused and smiled **cryptically**, as though recalling an incident too subtle for blunt narration."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Darwinism",
        "quote": "The nightjar rests **cryptically** upon fallen bark, its mottled plumage merging seamlessly with lichens."
      }
    ]
  },
  "Dashboard — crypt\\cryptobiosis.md": {
    "primary": "A state of suspended animation in an organism in response to extreme environmental stress, in which all measurable metabolic processes cease.",
    "secondary": "In physiology and extremophile biology, a reversible metabolic standstill (such as anhydrobiosis, cryobiosis, or osmobiosis) seen in tardigrades, nematodes, and brine shrimp cysts.",
    "quotes": [
      {
        "author": "Leeuwenhoek",
        "work": "Letters to the Royal Society",
        "quote": "Upon adding water to dry dust, rotifers revived from dormant **cryptobiosis** and swam with vigor as if newly born."
      },
      {
        "author": "Ernst Mayr",
        "work": "The Growth of Biological Thought",
        "quote": "The phenomenon of **cryptobiosis** challenges our philosophical definitions of life by demonstrating that metabolic arrest is fully reversible."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Eight Little Piggies",
        "quote": "Tardigrades survive exposure to the vacuum of space while locked in the desiccated stasis of **cryptobiosis**."
      }
    ]
  },
  "Dashboard — crypt\\cryptobiotic.md": {
    "primary": "Of, relating to, or capable of existing in a state of cryptobiosis.",
    "secondary": "In soil ecology and microbiology, describing biological crusts composed of cyanobacteria, lichens, and mosses that survive prolonged desiccation.",
    "quotes": [
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "Arid desert plateaus are stabilized by fragile **cryptobiotic** soil crusts that prevent wind erosion."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "Microscopic **cryptobiotic** organisms endure months of parching equatorial drought before sudden rains awaken them."
      },
      {
        "author": "Aldo Leopold",
        "work": "A Sand County Almanac",
        "quote": "Careless steps across the dunes destroy the delicate **cryptobiotic** mantle that took centuries to mature."
      }
    ]
  },
  "Dashboard — crypt\\cryptobranchidae.md": {
    "primary": "A family of exceptionally large, aquatic, paedomorphic salamanders commonly known as giant salamanders.",
    "secondary": "In systematic herpetology, basal urodele amphibians (including the North American hellbender and Asian giant salamanders) that retain gill slits or skin folds for cutaneous respiration in cold, swift streams.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Manual of the Vertebrate Animals of the Northern United States",
        "quote": "Members of **Cryptobranchidae** inhabit rocky mountain rivers, breathing predominantly through wrinkled lateral folds of vascular skin."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The retention of larval gill apertures in **Cryptobranchidae** exemplifies ancestral paedomorphic persistence in modern amphibia."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Fossil giants related to living **Cryptobranchidae** date back to the Jurassic, exhibiting remarkably conservative skeletal morphology."
      }
    ]
  },
  "Dashboard — crypt\\cryptobranchus.md": {
    "primary": "A genus of giant North American aquatic salamanders comprising the hellbender (Cryptobranchus alleganiensis).",
    "secondary": "In herpetology, a large, dorsoventrally flattened stream salamander with fleshy, highly vascularized skin folds used for cutaneous oxygen uptake.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "The formidable water-dog of the Ohio River, designated **Cryptobranchus**, lurks under flat submerged slabs of limestone."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Iconographic Encyclopaedia of Science, Literature, and Art",
        "quote": "The broad, depressed head and wrinkled cutaneous flaps of **Cryptobranchus** equip it perfectly for bottom-dwelling life in turbulent waters."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "In **Cryptobranchus**, fertilization remains external, an ancient reproductive trait conserved from primitive aquatic ancestors."
      }
    ]
  },
  "Dashboard — crypt\\cryptocercidae.md": {
    "primary": "A family of subsocial, wingless, wood-eating roaches comprising the solitary genus Cryptocercus.",
    "secondary": "In entomology and evolutionary systematics, primitive roaches whose mutualistic gut flagellates and social behavior establish them as the sister group to termites (Isoptera).",
    "quotes": [
      {
        "author": "William Morton Wheeler",
        "work": "The Social Insects: Their Origin and Evolution",
        "quote": "The close phylogenetic tie between termites and cockroaches is demonstrated by the wood-boring roaches of **Cryptocercidae**."
      },
      {
        "author": "Edward O. Wilson",
        "work": "Sociobiology: The New Synthesis",
        "quote": "Subsocial parent-offspring care and cellulose-digesting symbiotes make **Cryptocercidae** a living window into termite origins."
      },
      {
        "author": "Ernst Mayr",
        "work": "The Growth of Biological Thought",
        "quote": "Taxonomists placed **Cryptocercidae** at the base of dictyopteran evolution, bridging solitary blattodeans and eusocial termites."
      }
    ]
  },
  "Dashboard — crypt\\cryptocercus.md": {
    "primary": "A genus of wingless, wood-feeding roaches commonly known as brown-hooded cockroaches.",
    "secondary": "In insect physiology and evolutionary biology, a xylophagous insect living inside rotting logs, dependent on protozoan endosymbionts to digest wood.",
    "quotes": [
      {
        "author": "William Morton Wheeler",
        "work": "Social Life Among the Insects",
        "quote": "In mountain forests of the Appalachians, colonies of **Cryptocercus** excavate extensive galleries inside decaying hemlock logs."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "Young nymphs of **Cryptocercus** acquire their indispensable cellulose-digesting flagellates by direct proctodeal feeding from their parents."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The parallel speciation of symbiotic hypermastigotes inside the gut of **Cryptocercus** mirrors the divergence of the host roach."
      }
    ]
  },
  "Dashboard — crypt\\cryptochrome.md": {
    "primary": "A class of flavoprotein photoreceptors sensitive to blue light, found in plants, insects, and animals.",
    "secondary": "In chronobiology and sensory physiology, pigments that regulate circadian rhythms in plants and animals and mediate magnetoreception in migrating birds.",
    "quotes": [
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends: Selected Writings",
        "quote": "Identification of **cryptochrome** confirmed how blue wavelengths reset the molecular oscillator in circadian entrainment."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Extended Phenotype",
        "quote": "Migratory songbirds apparently perceive the Earth's geomagnetic lines using quantum spin chemistry mediated by retinal **cryptochrome**."
      },
      {
        "author": "Francis Crick",
        "work": "What Mad Pursuit",
        "quote": "The light-induced electron transfers inside **cryptochrome** bridge molecular biophysics and organismal behavioral timing."
      }
    ]
  },
  "Dashboard — crypt\\cryptococcosis.md": {
    "primary": "A subacute or chronic infectious disease caused by encapsulated yeast-like fungi of the genus Cryptococcus.",
    "secondary": "In infectious disease and medical mycology, an opportunistic infection (primarily Cryptococcus neoformans) that manifests typically as fatal subacute meningitis in immunocompromised patients.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In cerebral **cryptococcosis**, examination of cerebrospinal fluid with India ink reveals budding yeast cells ringed by voluminous clear capsules."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The mucopolysaccharide capsule characterizing the yeast in **cryptococcosis** shields the organism against phagocytic destruction."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumors",
        "quote": "Granulomatous lesions of **cryptococcosis** may clinically simulate an expanding intracranial neoplasm before culture verification."
      }
    ]
  },
  "Dashboard — crypt\\cryptocoryne.md": {
    "primary": "A genus of aquatic and amphibious flowering plants in the arum family Araceae, native to tropical streams of South and Southeast Asia.",
    "secondary": "In systematic botany and aquarium horticulture, perennial aquatic herbs known as water trumpets, characterized by a spiral-twisted spathe enclosing a concealed spadix.",
    "quotes": [
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Aquarists prize the submerged foliage of **Cryptocoryne** for its graceful bronze hues and tolerance of shaded aquatic conditions."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Along shaded jungle rivulets of Borneo, lush patches of **Cryptocoryne** carpeted the gravel banks beneath clear flowing water."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The inflorescence of **Cryptocoryne** is enclosed within a tubular spathe, concealing the minute blossoms in a basal kettle."
      }
    ]
  },
  "Dashboard — crypt\\cryptogam.md": {
    "primary": "A plant or plant-like organism that reproduces by spores rather than seeds, lacking conspicuous flowers or stamens.",
    "secondary": "In classical botanical systematics, any member of the traditional group Cryptogamia, comprising ferns, mosses, algae, and fungi.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Systema Naturae",
        "quote": "The **cryptogam** conceals its nuptials in darkness, producing minute dust-like spores without the display of floral petals."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Every fern, horsetail, and humble moss is structurally a **cryptogam**, reproducing by microscopic dust-like spores."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Views of Nature",
        "quote": "High on Andean volcanic summits, the final pioneers of vegetation belong to the hardy **cryptogam** tribes of lichens and mosses."
      }
    ]
  },
  "Dashboard — crypt\\cryptogamia.md": {
    "primary": "The 24th and final class in the Linnaean sexual system of plant classification, encompassing plants with concealed reproductive organs.",
    "secondary": "In historical taxonomy, a vast non-flowering assemblage embracing ferns, mosses, liverworts, lichens, algae, and fungi.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Genera Plantarum",
        "quote": "In the class **Cryptogamia**, the stamens and pistils are either too minute to be detected or entirely hidden from sight."
      },
      {
        "author": "John Ray",
        "work": "The Wisdom of God Manifested in the Works of the Creation",
        "quote": "Even in the obscure realms of **Cryptogamia**, the Divine Architect has provided exquisite mechanisms for propagation."
      },
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "Microscopic discoveries gradually dismembered the artificial class **Cryptogamia**, segregating fungi and algae from vascular archegoniates."
      }
    ]
  },
  "Dashboard — crypt\\cryptogamic.md": {
    "primary": "Of, relating to, or characteristic of cryptogams; reproducing by spores without flowers.",
    "secondary": "In floristics, describing the lower non-seed floras (mosses, liverworts, ferns, algae) of a biome.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "The damp northern forest floor supported a luxuriant **cryptogamic** growth of emerald mosses and delicate liverworts."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "On the bleak rocks of Tierra del Fuego, **cryptogamic** plants formed the solitary living tapestry across granite cliffs."
      },
      {
        "author": "William Gilson Farlow",
        "work": "Marine Algae of New England",
        "quote": "The coastal tidepools exhibit an astonishing diversity of **cryptogamic** life, from microscopic diatoms to giant kelps."
      }
    ]
  },
  "Dashboard — crypt\\cryptogamous.md": {
    "primary": "Having concealed reproductive organs; reproducing by spores rather than flowers and seeds; cryptogamic.",
    "secondary": "In descriptive botanical morphology, describing plants that do not produce true seeds or pollen tubes.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "Massive tree ferns presented a splendid specimen of **cryptogamous** vegetation flourishing under tropical mist."
      },
      {
        "author": "John Muir",
        "work": "My First Summer in the Sierra",
        "quote": "Moist rock crevices were cushioned with **cryptogamous** tapestries of green mosses glistening with spray."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The study of **cryptogamous** botany demands patient exploration with compound achromatic lenses."
      }
    ]
  },
  "Dashboard — crypt\\cryptogenic.md": {
    "primary": "Of obscure, hidden, or unknown cause or origin, especially said of a disease.",
    "secondary": "In clinical etiology, designating pathologies such as cryptogenic organizing pneumonia, stroke, or cirrhosis where diagnostic workup reveals no identifiable agent.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cases of severe pyemia arising without an identifiable external wound or focus were historically termed **cryptogenic** septicemia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The label **cryptogenic** merely confesses the temporary limitation of our microscopic and bacteriological methods."
      },
      {
        "author": "Sir Thomas Watson",
        "work": "Lectures on the Principles and Practice of Physic",
        "quote": "The clinician must not rest satisfied with a diagnosis of **cryptogenic** fever until every latent visceral abscess has been excluded."
      }
    ]
  },
  "Dashboard — crypt\\cryptogram.md": {
    "primary": "A text or message written in code or cipher.",
    "secondary": "In recreational linguistics and historical cryptology, an encrypted puzzle or secret writing whose meaning is concealed by substitution or transposition.",
    "quotes": [
      {
        "author": "Edgar Allan Poe",
        "work": "The Gold-Bug",
        "quote": "It may well be doubted whether human ingenuity can construct a **cryptogram** which human ingenuity cannot resolve."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventure of the Dancing Men",
        "quote": "Holmes arranged the slips of paper, studying the enigmatic dancing stick-figures of the **cryptogram** with keen absorption."
      },
      {
        "author": "Jules Verne",
        "work": "Journey to the Center of the Earth",
        "quote": "Professor Lidenbrock paced the floor in agitation, determined to decipher the runic **cryptogram** of Arne Saknussemm."
      }
    ]
  },
  "Dashboard — crypt\\cryptogramma.md": {
    "primary": "A small genus of ferns in the family Pteridaceae, commonly known as rock brakes or parsley ferns.",
    "secondary": "In pteridology, small saxicolous ferns native to alpine and arctic scree slopes, characterized by marked dimorphism between vegetative and fertile fronds.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The delicate parsley fern, **Cryptogramma** stelleri, roots in shaded fissures of moist limestone cliffs."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "High among the granite talus of the Sierra Nevada, tough little tufts of **Cryptogramma** brave the frost."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Species of **Cryptogramma** require cool, alpine rockery conditions with immaculate drainage to flourish in cultivation."
      }
    ]
  },
  "Dashboard — crypt\\cryptogrammataceae.md": {
    "primary": "A former or segregate family of leptosporangiate ferns containing the genus Cryptogramma.",
    "secondary": "In systematic pteridology, a taxon erected for rock-brake ferns displaying distinct frond dimorphism, now usually subsumed under Pteridaceae.",
    "quotes": [
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "Characters of spore ornamentation and marginal indusia justified the provisional separation of **Cryptogrammataceae**."
      },
      {
        "author": "John Merle Coulter",
        "work": "Morphology of Gymnosperms and Cryptogams",
        "quote": "Ferns assigned to **Cryptogrammataceae** demonstrate marked adaptations to saxicolous alpine habitats."
      },
      {
        "author": "William Gilson Farlow",
        "work": "Notes on North American Pteridophytes",
        "quote": "Frond dimorphism remains the most conspicuous morphological criterion uniting the genera of **Cryptogrammataceae**."
      }
    ]
  },
  "Dashboard — crypt\\cryptograph.md": {
    "primary": "A secret text or cipher; also a mechanical device, apparatus, or system used for enciphering and deciphering communications.",
    "secondary": "In cryptographic history, an instrument such as the Wheatstone cryptograph that encrypts plaintext into polyalphabetic cipher.",
    "quotes": [
      {
        "author": "Charles Babbage",
        "work": "Passages from the Life of a Philosopher",
        "quote": "I constructed a mechanical **cryptograph** designed to scramble printed characters according to predetermined wheel teeth."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Wheatstone exhibited his revolving **cryptograph** at the Royal Society, demonstrating rapid cipher substitution."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "Essays on Secret Writing",
        "quote": "The cunning artisan who frames an elaborate **cryptograph** often forgets that linguistic redundancy inevitably exposes his secret."
      }
    ]
  },
  "Dashboard — crypt\\cryptographer.md": {
    "primary": "A person who designs, constructs, or practices secret codes and ciphers; an expert in cryptography.",
    "secondary": "In computer science and intelligence, a theorist who formulates mathematical algorithms to safeguard communication against eavesdropping.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The skilled **cryptographer** builds his cipher on the assumption that the enemy already knows the mechanism but lacks the key."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "The task of the **cryptographer** is to maximize equivocation so that ciphertext provides no statistical leverage."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Every working **cryptographer** learns to look for human laziness in repetitive message prefixes."
      }
    ]
  },
  "Dashboard — crypt\\cryptographic.md": {
    "primary": "Pertaining to, written in, or characteristic of cryptography or secret ciphers.",
    "secondary": "In information security, describing mathematical primitives such as hash functions, public-key algorithms, and block ciphers.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "A robust **cryptographic** system achieves perfect secrecy only when the key space equals or exceeds the message entropy."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "The German military relied upon the Enigma machine under the mistaken conviction of its unbreakable **cryptographic** strength."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The advent of radio communications elevated **cryptographic** security into a matter of national survival."
      }
    ]
  },
  "Dashboard — crypt\\cryptographical.md": {
    "primary": "Relating to cryptography; cryptographic.",
    "secondary": "In historical and mathematical texts, of or relating to the technical methods and systems of enciphering messages.",
    "quotes": [
      {
        "author": "Charles Babbage",
        "work": "Passages from the Life of a Philosopher",
        "quote": "My early investigations into **cryptographical** puzzles aided me considerably in designing the mechanical calculating engine."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Diplomatic pouches across seventeenth-century Europe were subjected to relentless **cryptographical** interception."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "A Few Words on Secret Writing",
        "quote": "No **cryptographical** mystery can withstand methodical frequency analysis when sufficient text is supplied."
      }
    ]
  },
  "Dashboard — crypt\\cryptographically.md": {
    "primary": "In a cryptographic manner; by means of secret codes, ciphers, or encryption.",
    "secondary": "In cybersecurity, using mathematically secure cryptographic algorithms to protect data integrity and authenticity.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "Transmissions that are **cryptographically** secure must display the statistical randomness of white noise to an interceptor."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The telegram was **cryptographically** scrambled before being transmitted over transatlantic cables."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "By operating **cryptographically** upon daily cipher traffic, our team reconstructed changing naval call signs."
      }
    ]
  },
  "Dashboard — crypt\\cryptography.md": {
    "primary": "The practice and study of techniques for secure communication in the presence of adversarial third parties; secret writing.",
    "secondary": "In computer science and mathematics, the discipline encompassing data encryption, digital signatures, hash functions, and authentication protocols.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "The virtues required in **cryptography** are three: that they be easy to write, that they be difficult to decipher, and that they be devoid of suspicion."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "The fundamental problem of **cryptography** is that of transmitting a secret message over an insecure communication channel."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Gold-Bug",
        "quote": "Circumstances led me to give particular attention to the fascinating curiosities of **cryptography**."
      }
    ]
  },
  "Dashboard — crypt\\cryptologic.md": {
    "primary": "Pertaining to cryptology, the combined science of cryptography and cryptanalysis.",
    "secondary": "In military intelligence and signals intelligence, relating to the intercept, protection, and breaking of communications.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The battle of Midway was decided before the first carrier sailed, thanks to brilliant **cryptologic** breakthroughs."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "The daily rotor alignment posed a formidable **cryptologic** obstacle requiring specialized mechanical computation."
      },
      {
        "author": "Claude Shannon",
        "work": "The Mathematical Theory of Communication",
        "quote": "Shannon's classic 1945 memorandum laid the quantitative foundation for modern **cryptologic** evaluation."
      }
    ]
  },
  "Dashboard — crypt\\cryptological.md": {
    "primary": "Of or relating to cryptology or the scientific investigation of secret codes and ciphers.",
    "secondary": "In the history of espionage, describing analytical systems and mathematical protocols developed to secure or intercept state secrets.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Major nations established dedicated **cryptological** bureaus whose existence was concealed from the public."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "Our **cryptological** successes against naval codes directly shortened the duration of the European conflict."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "The statistical structure of human language constitutes the fundamental basis for all **cryptological** exploitation."
      }
    ]
  },
  "Dashboard — crypt\\cryptologist.md": {
    "primary": "An expert in cryptology who studies, creates, or deciphers codes and secret communications.",
    "secondary": "In signals intelligence, a specialist combining skills in mathematics, linguistics, and computer science to analyze secure communications.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "William Friedman, regarded as the dean of American cryptology, trained a generation of **cryptologist** pioneers."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "A patient **cryptologist** tracks subtle variations in operator habits to isolate recurring keystroke patterns."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "A Few Words on Secret Writing",
        "quote": "The enthusiastic **cryptologist** takes delight in peeling away layered substitutions to lay bare the author's hidden thought."
      }
    ]
  },
  "Dashboard — crypt\\cryptology.md": {
    "primary": "The overall scientific study of secret codes, encompassing both cryptography (creating codes) and cryptanalysis (breaking codes).",
    "secondary": "In communications and military intelligence, the comprehensive mathematical discipline governing the security and decryption of information systems.",
    "quotes": [
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "Modern **cryptology** was born when mathematical statistical analysis replaced intuitive guesswork in code-breaking."
      },
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "Information theory transformed **cryptology** from an empirical trade into an exact branch of applied probability."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "The progress of mechanized **cryptology** showed that calculating engines could outstrip human calculation in combinatorial deduction."
      }
    ]
  },
  "Dashboard — crypt\\cryptomeria.md": {
    "primary": "A monotypic genus of majestic evergreen coniferous trees in the cypress family Cupressaceae, commonly known as Japanese cedar or Sugi (Cryptomeria japonica).",
    "secondary": "In forestry and arboriculture, an ancient timber and sacred temple tree native to Japan, characterized by fragrant reddish-brown bark, spiraled awl-shaped needles, and soft, durable wood.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "Ancient avenues of towering **Cryptomeria** lead pilgrims through misty mountain ravines toward the shrines of Nikko."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "The Japanese cedar, **Cryptomeria** japonica, forms an imposing pyramidal tree whose foliage turns bronze-purple in winter frost."
      },
      {
        "author": "Charles Sprague Sargent",
        "work": "Forest Flora of Japan",
        "quote": "No tree in the Japanese archipelago yields more valuable or aromatic lumber than the revered **Cryptomeria**."
      }
    ]
  },
  "Dashboard — crypt\\cryptomonad.md": {
    "primary": "Any member of the phylum Cryptophyta, comprising single-celled biflagellate photosynthetic or heterotrophic algae.",
    "secondary": "In protistology and evolutionary cell biology, unicellular flagellates possessing ejectisomes, flattened cells, and a nucleomorph representing the vestigial nucleus of an engulfed red algal endosymbiont.",
    "quotes": [
      {
        "author": "Lynn Margulis",
        "work": "Symbiosis in Cell Evolution",
        "quote": "The tiny **cryptomonad** flagellate contains a nucleomorph between its four plastid membranes, conclusive proof of secondary endosymbiosis."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "Under darkfield illumination, a swimming **cryptomonad** darts with breathtaking agility, propelled by unequal flagella."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology: Part I",
        "quote": "The distinctive gullet and discharging ejectisomes of each **cryptomonad** serve both for food capture and rapid escape."
      }
    ]
  },
  "Dashboard — crypt\\cryptophyceae.md": {
    "primary": "The principal taxonomic class of biflagellate unicellular algae within the phylum Cryptophyta, commonly known as cryptophytes.",
    "secondary": "In aquatic biology and phycology, photosynthetic microalgae harboring phycobiliproteins, chlorophylls a and c, and a vestigial eukaryotic nucleomorph inside the plastid.",
    "quotes": [
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "The class **Cryptophyceae** embraces asymmetric motile unicells distinguished by a longitudinal ventral furrow."
      },
      {
        "author": "Lynn Margulis",
        "work": "Five Kingdoms",
        "quote": "Plastids in **Cryptophyceae** trace their origin to an ancient engulfed red alga whose remnant nucleus persists as a nucleomorph."
      },
      {
        "author": "William Gilson Farlow",
        "work": "The Marine Algae of New England",
        "quote": "Dense populations of **Cryptophyceae** contribute significantly to the primary productivity of chilly coastal estuaries."
      }
    ]
  },
  "Dashboard — crypt\\cryptophyta.md": {
    "primary": "A phylum or division of largely photosynthetic, eukaryotic, single-celled flagellates known as cryptomonads.",
    "secondary": "In protist evolution, a distinct algal lineage characterized by a periplast, ejectisomes, flattened cell morphology, and complex quadri-membranous plastids derived from red algae.",
    "quotes": [
      {
        "author": "Lynn Margulis",
        "work": "Symbiosis in Cell Evolution",
        "quote": "Members of **Cryptophyta** offer an irreplaceable snapshot of eukaryotic evolution frozen in the act of secondary plastid acquisition."
      },
      {
        "author": "Ernst Mayr",
        "work": "This Is Biology",
        "quote": "The unexpected cellular complexity of **Cryptophyta** upset traditional two-kingdom classifications of animals and plants."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The classification of **Cryptophyta** was established based upon the arrangement of flagella and the morphology of the cytopharynx."
      }
    ]
  },
  "Dashboard — crypt\\cryptophyte.md": {
    "primary": "A plant whose perennating buds survive unfavorable seasons buried beneath the soil surface or submerged under water.",
    "secondary": "In plant ecology (Raunkiær's life-form system), geophytes, helophytes, and hydrophytes (such as bulbs, tubers, and aquatic rhizomes) whose renewal buds are protected underground.",
    "quotes": [
      {
        "author": "Christen Raunkiær",
        "work": "The Life Forms of Plants and Statistical Plant Geography",
        "quote": "In harsh arid or frozen climates, a **cryptophyte** survives extreme seasons by burying its renewal buds deep in subterranean humus."
      },
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "The common potato and wild lily illustrate the habit of a **cryptophyte**, drawing upon subterranean food stores when spring arrives."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "On the steppes, vast numbers of **cryptophyte** species send forth sudden glorious carpets of blossoms after the first rains."
      }
    ]
  },
  "Dashboard — crypt\\cryptoprocta.md": {
    "primary": "A genus of solitary, carnivorous euplerid mammals endemic to Madagascar, containing the fossa (Cryptoprocta ferox).",
    "secondary": "In mammalian zoology and island biogeography, the apex mammalian predator of Madagascar, combining felid-like retractile claws with viverrid dentition and skeletal adaptations for arboreal agility.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Island Life",
        "quote": "Madagascar's peculiar fauna includes **Cryptoprocta**, a formidable carnivore uniting characters of cats and civets in isolation."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The fossa, known to science as **Cryptoprocta** ferox, hunts lemurs through the forest canopy with astonishing acrobatic speed."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The skull and dental apparatus of **Cryptoprocta** illustrate how convergent selection can mold a viverrid into a cat-like hunter."
      }
    ]
  },
  "Dashboard — crypt\\cryptorchidism.md": {
    "primary": "The medical condition in which one or both testes fail to descend normally into the scrotum before birth.",
    "secondary": "In clinical urology and pediatric endocrinology, the failure of testicular descent from the abdominal cavity through the inguinal canal, predisposing to infertility and germ-cell neoplasia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Uncorrected **cryptorchidism** carries an elevated risk of malignant degeneration in adult life, warranting timely orchidopexy."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Arrest of the gubernaculum testis during the seventh month of fetal development results in congenital **cryptorchidism**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Rudimentary organs and developmental arrests like **cryptorchidism** reveal the complex evolutionary history of mammalian morphology."
      }
    ]
  },
  "Dashboard — crypt\\cryptorchidy.md": {
    "primary": "The state or condition of having undescended testicles; cryptorchidism.",
    "secondary": "In veterinary medicine and animal husbandry, a congenital developmental defect wherein one or both testicles remain retained in the abdomen or inguinal ring.",
    "quotes": [
      {
        "author": "Sir Frederick Hobday",
        "work": "Castration of Cryptorchid Horses and the Ovariotomy of Troublesome Mares",
        "quote": "Equine **cryptorchidy** presents a difficult surgical challenge, requiring deep abdominal exploration to locate the retained organ."
      },
      {
        "author": "William Youatt",
        "work": "The Horse",
        "quote": "Horses suffering from unilateral **cryptorchidy** are notoriously vicious and unmanageable unless skillfully operated upon."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections in cases of **cryptorchidy** demonstrate progressive atrophy of the spermatogenic seminiferous tubules."
      }
    ]
  },
  "Dashboard — crypt\\cryptorchism.md": {
    "primary": "A congenital condition marked by the failure of one or both testicles to descend into the scrotum; cryptorchidism.",
    "secondary": "In comparative pathology and clinical genetics, developmental arrest of testicular migration along the inguinal trajectory.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Early surgical intervention for **cryptorchism** preserves spermatogenesis and minimizes the future risk of testicular torsion."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "Breeders of domestic dogs observe that **cryptorchism** occurs with surprising frequency in closely inbred strains."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "When the testis lodges within the inguinal canal, the condition of **cryptorchism** is readily palpated during clinical examination."
      }
    ]
  },
  "Dashboard — crypt\\cryptosystem.md": {
    "primary": "A complete suite of cryptographic algorithms, protocols, hardware, and key management systems necessary to implement secure communications.",
    "secondary": "In computer science and modern cryptography, a mathematical system consisting of plaintext space, ciphertext space, key generation algorithms, and encryption/decryption functions.",
    "quotes": [
      {
        "author": "Claude Shannon",
        "work": "Communication Theory of Secrecy Systems",
        "quote": "A mathematically sound **cryptosystem** must ensure that decryption remains computationally infeasible even if the eavesdropper knows the entire algorithm."
      },
      {
        "author": "Alan Turing",
        "work": "Turing's Treatise on the Enigma",
        "quote": "The vulnerability of the Enigma **cryptosystem** stemmed not from the rotors alone, but from procedural flaws in daily key distribution."
      },
      {
        "author": "David Kahn",
        "work": "The Codebreakers",
        "quote": "The development of the RSA public-key **cryptosystem** revolutionized digital commerce by solving the ancient key-exchange dilemma."
      }
    ]
  },
  "Dashboard — crypt\\cryptotermes.md": {
    "primary": "A genus of drywood termites in the family Kalotermitidae, notable for nesting inside dry, sound wood without contact with the soil.",
    "secondary": "In structural entomology and tropical ecology, wood-destroying social insects characterized by phragmotic soldiers possessing a plug-like, truncated head used to block gallery entrances.",
    "quotes": [
      {
        "author": "William Morton Wheeler",
        "work": "The Social Insects: Their Origin and Evolution",
        "quote": "The soldier of **Cryptotermes** possesses a heavily sclerotized, shovel-shaped head perfectly fashioned to plug the nest burrow against invading ants."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Insect Societies",
        "quote": "Colonies of **Cryptotermes** thrive inside dry furniture and structural rafters, extracting every trace of metabolic moisture from dry wood."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Wooden bungalows in the tropics suffer silent devastation from **Cryptotermes**, reducing solid timber to paper-thin shells."
      }
    ]
  }
};

const updated = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`[Batch 3] Successfully updated ${updated} of ${Object.keys(batchData).length} notes.`);
