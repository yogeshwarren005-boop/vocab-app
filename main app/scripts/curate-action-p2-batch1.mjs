import { updateNotesBatch } from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Action';

const BATCH1_DATA = {
  "Dashboard — schiz\\schizoid.md": {
    "primary": "Exhibiting traits of social withdrawal, emotional detachment, aloofness, and introspective preoccupation without frank psychosis.",
    "secondary": "In psychoanalysis, pertaining to the fundamental split within the ego and defensive retreat into an internal world of fantasy.",
    "quotes": [
      {
        "author": "W. R. D. Fairbairn",
        "work": "Psychoanalytic Studies of the Personality",
        "quote": "The fundamental position of the **schizoid** individual is that his love is destructive to those he loves, compelling an inward retreat."
      },
      {
        "author": "Harry Guntrip",
        "work": "Schizoid Phenomena, Object-Relations, and the Self",
        "quote": "The ultimate **schizoid** defense is detachment from all emotional relationships in an effort to preserve personal integrity."
      },
      {
        "author": "Anthony Storr",
        "work": "Solitude: A Return to the Self",
        "quote": "Creative individuals often display **schizoid** characteristics, finding in solitary labor a refuge from interpersonal conflict."
      }
    ]
  },
  "Dashboard — schiz\\schizomycetes.md": {
    "primary": "In historical taxonomy, the class or division of unicellular fission fungi comprising bacteria that reproduce exclusively by transverse binary fission.",
    "secondary": "In bacteriological history, Ferdinand Cohn's foundational classification grouping micro-organisms capable of causing fermentation, putrefaction, and disease.",
    "quotes": [
      {
        "author": "Ferdinand Cohn",
        "work": "Researches on Bacteria",
        "quote": "Under the designation **schizomycetes** we unite those lowest plant-like forms whose multiplication proceeds through regular cellular division."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The microscopic agents of putrefaction belong predominantly to the **schizomycetes**, operating as indispensable scavengers in organic decay."
      },
      {
        "author": "William Bulloch",
        "work": "The History of Bacteriology",
        "quote": "Early nineteenth-century botanists grouped all bacterial organisms under the convenient rubric of **schizomycetes** before physiological traits were known."
      }
    ]
  },
  "Dashboard — schiz\\schizopetalon.md": {
    "primary": "A genus of Chilean annual herbs of the mustard family (Brassicaceae) distinguished by deeply cut, pinnatifid, or fringed white petals.",
    "secondary": "In horticultural botany, specifically denoting Schizopetalon walkeri, cultivated for its almond-scented night-blooming fringed blossoms.",
    "quotes": [
      {
        "author": "William Jackson Hooker",
        "work": "Botanical Magazine",
        "quote": "The pinnatifid structure of the corolla in **schizopetalon** imparts to the open blossom an exquisitely delicate, lacelike appearance."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Among cruciferous plants, few genera depart so remarkably from the standard four-petal pattern as does **schizopetalon** with its comb-like margins."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Amateur gardeners value **schizopetalon** for its unusual night-fragrance and intricate filigree petals that unfold at dusk."
      }
    ]
  },
  "Dashboard — schiz\\schizophragma.md": {
    "primary": "A genus of deciduous climbing woody vines in the hydrangea family (Hydrangeaceae), native to East Asia and climbing by aerial rootlets.",
    "secondary": "In dendrology and landscape architecture, climbing hydrangeas such as Schizophragma hydrangeoides bearing showy inflorescences with solitary enlarged sepals.",
    "quotes": [
      {
        "author": "Philipp Franz von Siebold",
        "work": "Flora Japonica",
        "quote": "Ascending the trunks of cryptomeria trees, **schizophragma** covers the bark with luxuriant foliage and broad corymbs of sterile bracts."
      },
      {
        "author": "Ernest Henry Wilson",
        "work": "A Naturalist in Western China",
        "quote": "In the damp mountain ravines of Hupeh, **schizophragma** clings tenaciously to sheer limestone cliffs, displaying great white sterile sepals."
      },
      {
        "author": "Charles Sprague Sargent",
        "work": "Trees and Shrubs",
        "quote": "The distinguishing character of **schizophragma** resides in the solitary ovate bract that subtends the peripheral sterile flowers of the cyme."
      }
    ]
  },
  "Dashboard — schiz\\schizophrenia.md": {
    "primary": "A severe chronic mental disorder characterized by disturbances in thought, perception, emotional responsiveness, and social functioning.",
    "secondary": "In historical psychiatry, Eugen Bleuler's conceptualization of a fundamental fragmentation and disharmony among psychic functions (the four A's).",
    "quotes": [
      {
        "author": "Eugen Bleuler",
        "work": "Dementia Praecox or the Group of Schizophrenias",
        "quote": "I call dementia praecox **schizophrenia** because the splitting of the different psychic functions is one of its most important characteristics."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "What Bleuler subsequently termed **schizophrenia** represents a tragic dissolution of emotional and volitional coherence in young adulthood."
      },
      {
        "author": "Karl Jaspers",
        "work": "General Psychopathology",
        "quote": "In **schizophrenia** we encounter a radical transformation of psychic life that defies intuitive empathic understanding."
      }
    ]
  },
  "Dashboard — schiz\\schizophrenic.md": {
    "primary": "Pertaining to, affected by, or characteristic of schizophrenia.",
    "secondary": "Describing contradictory, disjointed, or radically polarized qualities within a cultural, economic, or artistic system.",
    "quotes": [
      {
        "author": "R. D. Laing",
        "work": "The Divided Self",
        "quote": "The **schizophrenic** condition can be comprehended as an existential maneuver to survive in an unlivable interpersonal environment."
      },
      {
        "author": "Gregory Bateson",
        "work": "Steps to an Ecology of Mind",
        "quote": "Repeated exposure to contradictory double-bind communications fosters a distinctly **schizophrenic** pattern of defensive response."
      },
      {
        "author": "Fredric Jameson",
        "work": "Postmodernism, or, the Cultural Logic of Late Capitalism",
        "quote": "The breakdown of temporal continuity produces a **schizophrenic** experience of perpetual, disconnected presents."
      }
    ]
  },
  "Dashboard — schiz\\schizophyceae.md": {
    "primary": "The botanical taxonomic class encompassing the blue-green algae (cyanobacteria), characterized by reproduction by fission and lack of membrane-bound nuclei.",
    "secondary": "In evolutionary phycology, the primordial photosynthetic prokaryotes responsible for oxygenating the Earth's early atmosphere.",
    "quotes": [
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "The cellular simplicity of the **schizophyceae** clearly links them with the bacteria rather than the higher nucleated algae."
      },
      {
        "author": "F. E. Fritsch",
        "work": "The Structure and Reproduction of the Algae",
        "quote": "In the **schizophyceae**, vegetative division by fission is accompanied by a distinctive peripheral arrangement of photosynthetic lamellae."
      },
      {
        "author": "Lynn Margulis",
        "work": "Symbiosis in Cell Evolution",
        "quote": "Ancient members of the **schizophyceae** supplied the original plastid ancestors that transformed eukaryotic evolutionary pathways."
      }
    ]
  },
  "Dashboard — schiz\\schizophyta.md": {
    "primary": "An obsolete biological botanical division comprising unicellular prokaryotic organisms—namely bacteria and cyanobacteria—that multiply primarily by simple fission.",
    "secondary": "In late nineteenth-century phylogenetics, the primitive kingdom of anucleate plant organisms situated at the base of the tree of life.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The History of Creation",
        "quote": "We place the **schizophyta** at the root of organic creation as organisms devoid of organs and true nuclear structure."
      },
      {
        "author": "Julius von Sachs",
        "work": "Textbook of Botany",
        "quote": "Multiplication through transverse cleavage remains the sole mode of propagation observed across the entire group of the **schizophyta**."
      },
      {
        "author": "Charles Edwin Bessey",
        "work": "Botany for High Schools and Colleges",
        "quote": "The **schizophyta** exhibit the absolute minimum of morphological differentiation consistent with independent vital maintenance."
      }
    ]
  },
  "Dashboard — schiz\\schizopoda.md": {
    "primary": "An obsolete zoological order of small marine crustaceans possessing biramous, split-cleft thoracic limbs, formerly uniting mysids and euphausiids.",
    "secondary": "In carcinology, swimming malacostracan crustaceans exhibiting two-branched appendages adapted simultaneously for respiration and locomotion.",
    "quotes": [
      {
        "author": "G. O. Sars",
        "work": "Report on the Schizopoda Collected by H.M.S. Challenger",
        "quote": "The deep-sea dredging yielded abundant specimens of **schizopoda**, illustrating remarkable adaptations to abyssal pelagic zones."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The split-footed nature of the thoracic limbs gives the **schizopoda** their distinct taxonomic appellation."
      },
      {
        "author": "W. T. Calman",
        "work": "The Life of Crustacea",
        "quote": "Though modern taxonomists split the **schizopoda** into Mysida and Euphausiacea, their ecological roles as pelagic grazers remain intertwined."
      }
    ]
  },
  "Dashboard — schiz\\schizosaccharomyces.md": {
    "primary": "A genus of ascomycetous yeasts that reproduce by medial transverse fission rather than by budding.",
    "secondary": "In cell biology and genetics, the model organism Schizosaccharomyces pombe utilized to elucidate eukaryotic cell-cycle regulation and mitotic spindle dynamics.",
    "quotes": [
      {
        "author": "Paul Nurse",
        "work": "Cell Cycle Control in Fission Yeast",
        "quote": "By studying cell division mutants in **schizosaccharomyces**, we identified the universal kinase that triggers the onset of mitosis."
      },
      {
        "author": "J. Murdoch Mitchison",
        "work": "The Biology of the Cell Cycle",
        "quote": "The cylindrical geometry and constant diameter of **schizosaccharomyces** facilitate precise linear measurements of cellular growth."
      },
      {
        "author": "Urs Leupold",
        "work": "Genetics of Fission Yeast",
        "quote": "Genetic analysis in **schizosaccharomyces** provides an exquisite window into meiotic recombination and chromosome mechanics."
      }
    ]
  },
  "Dashboard — schiz\\schizosaccharomycetaceae.md": {
    "primary": "A family of yeasts within the order Schizosaccharomycetales characterized by reproduction by fission and formation of naked asci.",
    "secondary": "In systematic mycology, an early-diverging lineage of Taphrinomycotina separated from conventional budding yeasts by distinctive cell-wall polysaccharides and fission cytology.",
    "quotes": [
      {
        "author": "Alexandre Guilliermond",
        "work": "The Yeasts",
        "quote": "The family **schizosaccharomycetaceae** occupies an isolated position among ascomycetes due to its uncompromising reliance on transverse division."
      },
      {
        "author": "Cletus P. Kurtzman",
        "work": "The Yeasts: A Taxonomic Study",
        "quote": "Phylogenetic sequence comparisons place the **schizosaccharomycetaceae** near the ancient root of the modern ascomycete radiation."
      },
      {
        "author": "David Yarrow",
        "work": "Yeast Systematics",
        "quote": "Morphologically, the members of the **schizosaccharomycetaceae** lack pseudomycelium, persisting as solitary fission-divided rods."
      }
    ]
  },
  "Dashboard — schiz\\schizothymia.md": {
    "primary": "A psychological constitution characterized by introversion, emotional detachment, aloofness, and introspective reservedness within normal behavioral limits.",
    "secondary": "In Ernst Kretschmer's constitutional psychiatry, the healthy end of the personality continuum that predisposes toward schizophrenia in morbid manifestation.",
    "quotes": [
      {
        "author": "Ernst Kretschmer",
        "work": "Physique and Character",
        "quote": "Between the quiet, inward-looking genius and the eccentric hermit lies the vast psychological domain of **schizothymia**."
      },
      {
        "author": "Gordon Allport",
        "work": "Personality: A Psychological Interpretation",
        "quote": "Kretschmer contrasted cyclothymia with **schizothymia**, assigning the latter to lean leptosomic physiques prone to intellectual abstraction."
      },
      {
        "author": "William Sheldon",
        "work": "The Varieties of Temperament",
        "quote": "The cerebrotonic temperament mirrors many features originally assigned by German psychiatrists to **schizothymia**."
      }
    ]
  },
  "Dashboard — sci\\sciamachy.md": {
    "primary": "An act of fighting with a shadow; a mock contest, futile combat, or arguing against an imaginary or non-existent adversary.",
    "secondary": "In philosophical debate and polemical discourse, a pointless controversy wherein debaters attack constructed straw men rather than genuine tenets.",
    "quotes": [
      {
        "author": "John Cowper Powys",
        "work": "A Philosophy of Solitude",
        "quote": "Most of our frantic moral posturing is pure **sciamachy**, a breathless flailing at imaginary phantoms of our own conjuring."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Why spend your days in tedious **sciamachy** with phantom vices when direct virtue stands readily at hand?"
      },
      {
        "author": "William Hazlitt",
        "work": "Table-Talk",
        "quote": "The critic engaged in fierce **sciamachy** against obsolete doctrines resembles an armored knight battling windmill sails."
      }
    ]
  },
  "Dashboard — sci\\sciaphobia.md": {
    "primary": "An irrational, abnormal, and persistent fear of shadows.",
    "secondary": "In clinical psychopathology, an anxiety disorder manifesting as acute panic when confronted with silhouette projections or darkness-cast contours.",
    "quotes": [
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Childhood terrors frequently assume specific symbolic fixations, ranging from nyctophobia to an acute **sciaphobia**."
      },
      {
        "author": "G. Stanley Hall",
        "work": "Adolescence",
        "quote": "Primitive superstitions regarding disembodied spirits readily reinforce pathological **sciaphobia** in impressionable minds."
      },
      {
        "author": "George M. Beard",
        "work": "A Practical Treatise on Nervous Exhaustion",
        "quote": "The neurasthenic patient may develop peculiar dreads, including **sciaphobia**, where even his own shadow evokes involuntary tremor."
      }
    ]
  },
  "Dashboard — spad\\aspadana.md": {
    "primary": "The ancient Median and Achaemenid settlement and monumental audience hall or palace station located at modern Isfahan, Iran.",
    "secondary": "In ancient Near Eastern archaeology, a strategic crossroad city of antiquity situated on the central Iranian plateau along vital imperial trade routes.",
    "quotes": [
      {
        "author": "George Rawlinson",
        "work": "The Seven Great Monarchies of the Ancient Eastern World",
        "quote": "The name of modern Isfahan traces directly to the ancient **aspadana** recorded by Ptolemy as a royal Median settlement."
      },
      {
        "author": "A. T. Olmstead",
        "work": "History of the Persian Empire",
        "quote": "Persian caravans traversing the central deserts refreshed their cavalry mounts at the lush oasis pastures of **aspadana**."
      },
      {
        "author": "Ernst Herzfeld",
        "work": "Archaeological History of Iran",
        "quote": "Topographical surveys indicate that **aspadana** served as a major regional administrative garrison during late Achaemenid times."
      }
    ]
  },
  "Dashboard — spad\\epispadias.md": {
    "primary": "A rare congenital malformation in which the urethra terminates on the dorsal (upper) surface of the penis or clitoris.",
    "secondary": "In pediatric urology, a defect along the spectrum of bladder exstrophy caused by failure of midline closure of the lower abdominal wall and genital tubercle.",
    "quotes": [
      {
        "author": "Hugh Hampton Young",
        "work": "Practice of Urology",
        "quote": "Surgical repair of **epispadias** demands reconstructing the dorsal urethral plate while establishing dependable urinary continence."
      },
      {
        "author": "John W. Duckett",
        "work": "Pediatric Urology",
        "quote": "Unlike hypospadias, isolated **epispadias** involves dorsal curvature and profound alterations in pelvic floor anatomy."
      },
      {
        "author": "D. Innes Williams",
        "work": "Urology in Childhood",
        "quote": "The degree of dorsal clefting in **epispadias** correlates directly with the severity of accompanying pubic bone diastasis."
      }
    ]
  },
  "Dashboard — spad\\hypospadias.md": {
    "primary": "A common congenital malformation in which the external urethral orifice opens on the ventral (underside) aspect of the penis instead of at the tip of the glans.",
    "secondary": "In embryology, a developmental anomaly resulting from incomplete fusion of the urethral folds during the eighth to fourteenth weeks of gestation.",
    "quotes": [
      {
        "author": "Denis Browne",
        "work": "An Operation for Hypospadias",
        "quote": "The fundamental object in operations for **hypospadias** is to create a straight phallus with a terminal urinary meatus."
      },
      {
        "author": "Charles E. Horton",
        "work": "Plastic and Reconstructive Surgery of the Genital Area",
        "quote": "Accompanying chordee must be completely released prior to constructing the neourethra in severe forms of **hypospadias**."
      },
      {
        "author": "Frank Hinman Jr.",
        "work": "Atlas of Urosurgical Anatomy",
        "quote": "Ventral foreskin deficiency and hooded dorsal prepuce remain the classic external hallmarks of untreated **hypospadias**."
      }
    ]
  },
  "Dashboard — spad\\spade-like.md": {
    "primary": "Resembling a spade in broad, flat, or wedge-shaped contour.",
    "secondary": "In morphology, describing anatomical features such as incisors, snouts, or burrowing appendages modified into flattened digging blades.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The forelimbs of fossorial mammals have been transformed into stout, **spade-like** implements adapted for driving subterranean tunnels."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The broad flukes of the sperm whale terminated in a **spade-like** horizontal blade of immense propulsion."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "The Indian pointed out the **spade-like** imprint left by the moose's hoof in the soft swamp moss."
      }
    ]
  },
  "Dashboard — spad\\spade-shaped.md": {
    "primary": "Shaped like a spade; deltoid, cordate, or spatulate with a broad blade tapering toward a point or attachment.",
    "secondary": "In botany and zoology, denoting leaves or animal fins having a flattened triangular or rounded spatula outline.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The male bird displayed brilliant ornamental plumage ending in two **spade-shaped** tail feathers of iridescent green."
      },
      {
        "author": "William Beebe",
        "work": "Half Mile Down",
        "quote": "A bizarre bathypelagic creature drifted across the bathysphere window, flicking a **spade-shaped** caudal rudder."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "The plant sends up broad, **spade-shaped** leaves that catch the meltwater trickling from glacial moraines."
      }
    ]
  },
  "Dashboard — spad\\spade.md": {
    "primary": "A digging implement with a sharp, flat, rectangular metal blade and a long handle, operated by foot pressure for turning soil.",
    "secondary": "In cards, one of four suits in a standard deck characterized by a black, heart-shaped leaf emblem terminating in a small point and base stem.",
    "quotes": [
      {
        "author": "William Wordsworth",
        "work": "To the Spade of a Friend",
        "quote": "Spade! with which Henry delved the ground, with thee how cheerfully he turned the yielding sod!"
      },
      {
        "author": "Seamus Heaney",
        "work": "Death of a Naturalist",
        "quote": "Between my finger and my thumb the squat pen rests; snug as a gun. By God, the old man could handle a **spade**."
      },
      {
        "author": "John Ruskin",
        "work": "Sesame and Lilies",
        "quote": "Every honest laborer who thrusts his **spade** into the earth participates in the sacred duty of subduing nature."
      }
    ]
  },
  "Dashboard — spad\\spadefish.md": {
    "primary": "A deep-bodied, laterally compressed marine teleost fish of the family Ephippidae, particularly Chaetodipterus faber of the western Atlantic.",
    "secondary": "In marine biology, disk-shaped coastal and reef fishes possessing small terminal mouths, comb-like teeth, and steep dorsal profiles.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "Fishes",
        "quote": "The Atlantic **spadefish** is readily recognized by its compressed disk-like body and dark vertical juvenile banding."
      },
      {
        "author": "William Beebe",
        "work": "Beneath Tropic Seas",
        "quote": "A school of silvery **spadefish** hovered motionless above the coral reef, their steep profiles gleaming in the azure water."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "Around the submerged pilings, the **spadefish** foraged on hydroids and encrusting sponges swept by tidal currents."
      }
    ]
  },
  "Dashboard — spad\\spadefoot.md": {
    "primary": "A burrowing, nocturnal, toad-like amphibian belonging to the family Scaphiopodidae (or Pelobatidae), characterized by a keratinous spade on each hind foot.",
    "secondary": "In desert ecology, an explosive breeder that spends prolonged arid periods buried deep underground, emerging en masse following torrential rains.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Batrachia of North America",
        "quote": "The sharp horny blade of the metatarsal tubercle enables the **spadefoot** to vanish backward into sandy soil with incredible speed."
      },
      {
        "author": "Raymond B. Cowles",
        "work": "Desert Hour",
        "quote": "After the summer cloudburst, the dry arroyo echoed with the deafening courtship cries of the emerged **spadefoot**."
      },
      {
        "author": "Archie Carr",
        "work": "The Windward Road",
        "quote": "No creature exemplifies desert opportunism better than the **spadefoot**, completing metamorphosis within mere days of hatching."
      }
    ]
  },
  "Dashboard — spad\\spadeful.md": {
    "primary": "The amount of earth, coal, sand, or other loose material that can be held or lifted by a spade at one time.",
    "secondary": "A rough unit of manual excavation measurement signifying a single scoop turned during labor.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "With every heavy **spadeful** of rich loam turned, the earthy smell of autumn rose sharply into the morning air."
      },
      {
        "author": "George Eliot",
        "work": "Silas Marner",
        "quote": "He dug steadily until the last **spadeful** of gravel revealed the buried iron pot containing his hoarded gold."
      },
      {
        "author": "D. H. Lawrence",
        "work": "Sons and Lovers",
        "quote": "He flung a **spadeful** of slack onto the grate, watching the red coals blacken and then hiss with rising smoke."
      }
    ]
  },
  "Dashboard — spad\\spadework.md": {
    "primary": "Hard, laborious manual labor performed with a spade in digging or gardening.",
    "secondary": "Arduous, detailed, and indispensable preliminary investigation or organizational groundwork required to establish a larger enterprise.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "A Room of One's Own",
        "quote": "Centuries of thankless intellectual **spadework** were necessary before women could write poetry without social ridicule."
      },
      {
        "author": "George Orwell",
        "work": "The Road to Wigan Pier",
        "quote": "Before you can theorize about the working class, you must endure the unglamorous **spadework** of living in their cottages."
      },
      {
        "author": "H. G. Wells",
        "work": "The Outline of History",
        "quote": "A generation of field archaeologists had to finish their dusty **spadework** before the story of Sumer could be written."
      }
    ]
  },
  "Dashboard — spad\\spadix.md": {
    "primary": "A fleshy, thickened floral spike bearing small, crowded, petal-less flowers, typically enveloped by a leaf-like spathe (as in the arum family).",
    "secondary": "In reproductive morphology, the central columnar inflorescence of an aroid that often generates metabolic heat to volatilize floral scents.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "In the calla and Jack-in-the-pulpit, the tiny florets are densely packed along the erect fleshy axis of the **spadix**."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The spathe functions as an architectural protective shield sheltering the delicate blossoms clustering upon the **spadix**."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Cyclopedia of American Horticulture",
        "quote": "In Anthurium, the colorful waxy spathe contrasts vividly with the elongated, textured cylinder of the flowering **spadix**."
      }
    ]
  },
  "Dashboard — sphal\\asphalt.md": {
    "primary": "A dark brown or black viscous hydrocarbon liquid or semi-solid pitch found in natural deposits or obtained as a residue in petroleum refining.",
    "secondary": "A manufactured paving mixture composed of mineral aggregate cemented with bitumen, widely utilized for road construction and waterproofing.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "The Histories",
        "quote": "The builders of ancient Babylon bound together their baked bricks with mortar made of heated bubbling **asphalt**."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "From subterranean vaults arose fumes of sulfur and bituminous **asphalt**, paving the wide floor of Pandemonium."
      },
      {
        "author": "Lewis Mumford",
        "work": "The City in History",
        "quote": "The modern metropolis suffocates its living earth beneath an impermeable crust of concrete and black **asphalt**."
      }
    ]
  },
  "Dashboard — sphal\\asphaltic.md": {
    "primary": "Containing, consisting of, or having the chemical and physical characteristics of asphalt; bituminous.",
    "secondary": "In petroleum geology, denoting heavy crude oils that yield high percentages of solid bitumen and residual pitch upon fractional distillation.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Subterranean springs in Trinidad continuously discharge thick **asphaltic** pitch that solidifies into vast bituminous plains."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels",
        "quote": "The indigenous boatmen coated their canoes with native **asphaltic** gum obtained from coastal seepages."
      },
      {
        "author": "John Tyndall",
        "work": "Heat Considered as a Mode of Motion",
        "quote": "The radiation of heat through dark **asphaltic** varnishes illustrates the selective absorption spectra of complex hydrocarbons."
      }
    ]
  },
  "Dashboard — sphal\\sphalerite.md": {
    "primary": "The primary ore mineral of zinc, consisting of zinc sulfide (ZnS) in isometric crystals, commonly known as zinc blende.",
    "secondary": "In economic geology, a brittle sulfide mineral exhibiting resinous luster, perfect dodecahedral cleavage, and variable color due to iron substitution.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "A System of Mineralogy",
        "quote": "Because its deceptive appearance caused miners to mistake it for galena without yielding lead, the mineral was named **sphalerite** from the Greek for treacherous."
      },
      {
        "author": "René Just Haüy",
        "work": "Treatise on Mineralogy",
        "quote": "The cleavage directions of **sphalerite** reveal the flawless symmetry of its internal dodecahedral molecular lattice."
      },
      {
        "author": "Eduard Suess",
        "work": "The Face of the Earth",
        "quote": "Hydrothermal vein deposits frequently deposit galena in close association with dark iron-bearing **sphalerite**."
      }
    ]
  },
  "Dashboard — sphal\\sphaleron.md": {
    "primary": "A static, non-perturbative saddle-point solution of the electroweak field equations associated with baryon and lepton number violation.",
    "secondary": "In theoretical cosmology and particle physics, a finite-energy field configuration that mediates anomalous transitions across topological vacuum sectors at high temperatures.",
    "quotes": [
      {
        "author": "Frans Klinkhamer",
        "work": "A Saddle-Point Solution in the Standard Electroweak Theory",
        "quote": "We demonstrate the existence of a static, unstable field configuration—the **sphaleron**—representing the barrier top between topologically distinct vacua."
      },
      {
        "author": "Nicholas Manton",
        "work": "Topology in the Weinberg-Salam Model",
        "quote": "Thermal fluctuations in the primordial plasma can scale the **sphaleron** barrier, erasing preexisting baryon asymmetries."
      },
      {
        "author": "Valery Rubakov",
        "work": "Classical Theory of Gauge Fields",
        "quote": "At temperatures above the electroweak phase transition, **sphaleron** transitions occur unsuppressed, altering cosmic matter-antimatter ratios."
      }
    ]
  },
  "Dashboard — st\\acrostatic.md": {
    "primary": "Maintaining equilibrium or remaining stationary at extreme heights or upper atmospheric levels.",
    "secondary": "In aeronautics and meteorology, pertaining to aerostatic flotation or instrumentation stabilized within the stratosphere.",
    "quotes": [
      {
        "author": "Auguste Piccard",
        "work": "Between Earth and Sky",
        "quote": "Reaching our target ceiling, the spherical gondola settled into stable **acrostatic** balance above the turbulent troposphere."
      },
      {
        "author": "Svante Arrhenius",
        "work": "Worlds in the Making",
        "quote": "Microscopic spores may achieve **acrostatic** suspension in the highest planetary atmospheres before solar radiation pressure expels them."
      },
      {
        "author": "Theodore von Kármán",
        "work": "Aerodynamics",
        "quote": "Beyond dynamic lift boundaries, vehicles must rely on purely **acrostatic** displacement to hover in rarefied gas."
      }
    ]
  },
  "Dashboard — st\\actinostele.md": {
    "primary": "A type of protostele in vascular plants in which the central core of xylem has radiating ribs or lobes resembling a star in transverse section.",
    "secondary": "In plant anatomy, a primitive vascular cylinder found in primitive pteridophytes and lycophytes where phloem occupies the spaces between radiating xylem ridges.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The fluted xylem cylinder of the **actinostele** represents an evolutionary advance over the solid circular haplostele."
      },
      {
        "author": "Edward Charles Jeffrey",
        "work": "The Anatomy of Woody Plants",
        "quote": "In the fossil roots of early arborescent lycopods, transverse sections invariably reveal a well-defined star-like **actinostele**."
      },
      {
        "author": "Arthur Johnson Eames",
        "work": "Morphology of Vascular Plants",
        "quote": "The development of an **actinostele** vastly increases the contact surface between conducting tracheids and living phloem parenchyma."
      }
    ]
  },
  "Dashboard — st\\anastasis.md": {
    "primary": "A rising, restoration, or resurgence; specifically, the resurrection of Jesus Christ.",
    "secondary": "In Byzantine iconography and Eastern Christian theology, the depiction of the Harrowing of Hell, where Christ tramples the gates of death and raises Adam and Eve.",
    "quotes": [
      {
        "author": "Jaroslav Pelikan",
        "work": "The Spirit of Eastern Christendom",
        "quote": "In Eastern Orthodox liturgy, the feast of feasts is not simply Easter but the triumphant **anastasis** that shatters mortality."
      },
      {
        "author": "John Meyendorff",
        "work": "Byzantine Theology",
        "quote": "The great fresco of the **anastasis** at the Chora Monastery depicts Christ pulling humanity bodily from the tombs of Hades."
      },
      {
        "author": "Vladimir Lossky",
        "work": "The Mystical Theology of the Eastern Church",
        "quote": "Through the **anastasis**, human nature is ontologically renewed, releasing all creation from the bondage of decay."
      }
    ]
  },
  "Dashboard — st\\antistatic.md": {
    "primary": "Preventing, reducing, or eliminating the accumulation of static electricity and surface electrostatic charges.",
    "secondary": "In materials science and electronic packaging, denoting conductive or dissipative chemical coatings designed to protect sensitive semiconductor devices.",
    "quotes": [
      {
        "author": "Percy Bridgman",
        "work": "The Physics of High Pressure",
        "quote": "Treating the observation chamber with an **antistatic** layer prevented stray dielectric charges from deflecting the sensitive electrometer."
      },
      {
        "author": "Arthur von Hippel",
        "work": "Dielectrics and Waves",
        "quote": "The incorporation of hydrophilic quaternary ammonium salts imparts durable **antistatic** conductivity to synthetic polymer sheets."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "When synthetic garments rub together in dry air, only an **antistatic** rinse prevents that sharp crackle of spark discharges."
      }
    ]
  },
  "Dashboard — st\\apostate.md": {
    "primary": "A person who renounces, deserts, or completely abandons a religious faith, political allegiance, or moral cause.",
    "secondary": "Characterized by ideological defection or renunciation; renegade, traitorous, or heretical.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Emperor Julian earned the enduring title of **apostate** by attempting to resurrect pagan rituals over Christian dogma."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "So spake the Cherub, and on either side the war broke loose, while Satan stood as an **apostate** angel defying heaven."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Every dogmatic orthodoxy reserves its fiercest inquisitorial wrath not for the uninitiated pagan, but for the repentless **apostate**."
      }
    ]
  },
  "Dashboard — st\\astasia.md": {
    "primary": "Motor incoordination or psychogenic inability to stand upright, despite retaining normal muscular power when seated or lying down.",
    "secondary": "In clinical neurology, a dissociative or functional gait disturbance classically paired with abasia (astasia-abasia) as described by Paul Blocq.",
    "quotes": [
      {
        "author": "Paul Blocq",
        "work": "On an Affection Characterized by Astasia and Abasia",
        "quote": "The patient with **astasia** collapses instantly when placed on his feet, yet displays unimpaired strength in recumbency."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "We observed dramatic episodes of hysterical **astasia**, where the subject trembled violently without any organic lesion of the cord."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Functional **astasia** must be distinguished from cerebellar ataxia by the absence of true nystagmus and normal deep reflexes."
      }
    ]
  },
  "Dashboard — st\\astasis.md": {
    "primary": "Absence of stability or equilibrium; an unstable, fluctuating, or unsteady state.",
    "secondary": "In physical science and systems theory, a condition wherein restorative forces are completely neutralized, permitting free displacement.",
    "quotes": [
      {
        "author": "Lord Kelvin",
        "work": "Popular Lectures and Addresses",
        "quote": "A magnetic needle suspended at its neutral point experiences complete **astasis**, remaining indifferent to terrestrial flux."
      },
      {
        "author": "Ernst Mach",
        "work": "The Science of Mechanics",
        "quote": "Mechanical **astasis** indicates that the potential energy surface is entirely flat across small positional variations."
      },
      {
        "author": "Henri Poincaré",
        "work": "Science and Method",
        "quote": "When a dynamic system approaches the threshold of **astasis**, the slightest perturbation induces unpredictable trajectories."
      }
    ]
  },
  "Dashboard — st\\astatic.md": {
    "primary": "Having no tendency to take a fixed directional position or orientation; in neutral equilibrium regarding external fields.",
    "secondary": "In physics, designating an arrangement of magnetic needles (astatic couple) whose equal and opposite poles cancel Earth's magnetic influence.",
    "quotes": [
      {
        "author": "André-Marie Ampère",
        "work": "Memoir on the Mathematical Theory of Electrodynamic Phenomena",
        "quote": "By combining two parallel needles with opposing poles, Nobili constructed an **astatic** galvanometer of unprecedented sensitivity."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The deflection of the **astatic** needle demonstrated the existence of induced currents even in minute circuit loops."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "An **astatic** suspension eliminates the directive couple of the geomagnetic field, leaving the system subject only to torsion."
      }
    ]
  },
  "Dashboard — st\\astatine.md": {
    "primary": "A highly radioactive chemical element of the halogen group, having atomic number 85 and chemical symbol At, with no stable isotopes.",
    "secondary": "In nuclear radiochemistry, the heaviest known halogen, synthesized by alpha bombardment of bismuth-209, exhibiting metallic semi-conductive tendencies.",
    "quotes": [
      {
        "author": "Emilio Segrè",
        "work": "A Mind Always in Motion",
        "quote": "We christened the newly synthesized element 85 **astatine**, from the Greek word for unstable, to honor its fleeting half-life."
      },
      {
        "author": "Glenn T. Seaborg",
        "work": "Man-Made Transuranium Elements",
        "quote": "Because macroscopic quantities of **astatine** vaporize instantly from self-heating, its properties must be deduced from tracer experiments."
      },
      {
        "author": "Dale R. Corson",
        "work": "Artificially Produced Element 85",
        "quote": "The chemical behavior of **astatine** confirms its position in the halogen column while exhibiting noticeable electropositive metallicity."
      }
    ]
  },
  "Dashboard — st\\catastasis.md": {
    "primary": "The dramatic climax, heightening of tension, or central crisis of an ancient play immediately preceding the catastrophe.",
    "secondary": "In classical rhetoric, the exordium-following state of the question, or the establishment of the central thesis in formal oration.",
    "quotes": [
      {
        "author": "John Dryden",
        "work": "Of Dramatic Poesy: An Essay",
        "quote": "In the **catastasis**, the action is brought to its utmost fullness and fury, holding the spectator in breathless suspense."
      },
      {
        "author": "Samuel Johnson",
        "work": "Lives of the Most Eminent English Poets",
        "quote": "The dramatist managed his plot with such dexterity that the **catastasis** appeared the inevitable consequence of earlier acts."
      },
      {
        "author": "Julius Caesar Scaliger",
        "work": "Poetics",
        "quote": "Classical drama proceeds methodically from protasis through epitasis to the **catastasis**, before dissolving in the catastrophe."
      }
    ]
  },
  "Dashboard — st\\chronostasis.md": {
    "primary": "A temporal illusion in which the first duration observed after a rapid saccadic eye movement appears substantially extended.",
    "secondary": "In cognitive neuroscience, the stopped-clock illusion caused by neural backward masking and cortical time-calibration following visual suppression.",
    "quotes": [
      {
        "author": "Kielan Yarrow",
        "work": "Time Estimation and Saccadic Vision",
        "quote": "The phenomenon of **chronostasis** demonstrates that subjective time dilates to bridge the sensory void during saccadic eye movement."
      },
      {
        "author": "David Eagleman",
        "work": "Brain Time",
        "quote": "When you glance suddenly at a ticking second hand, **chronostasis** tricks your brain into believing the hand froze for an eternity."
      },
      {
        "author": "Patrick Haggard",
        "work": "Conscious Intention and Action",
        "quote": "Our perception of temporal flow is not a direct ticker-tape of reality, as illusions like **chronostasis** decisively prove."
      }
    ]
  },
  "Dashboard — st\\diastase.md": {
    "primary": "An enzyme mixture (chiefly amylase) found in germinating malt and saliva that hydrolyzes starches into soluble maltose and dextrin.",
    "secondary": "Historically, the first enzyme ever isolated and characterized, identified by Anselme Payen and Jean-François Persoz in 1833.",
    "quotes": [
      {
        "author": "Anselme Payen",
        "work": "Memoir on Diastase",
        "quote": "We gave the name **diastase** to this substance because it possesses the unique property of separating starch into soluble sugars."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Soluble ferments such as **diastase** act chemically upon carbohydrate substrates without requiring the direct presence of living yeast."
      },
      {
        "author": "Justus von Liebig",
        "work": "Animal Chemistry",
        "quote": "The transformation of vegetable starches into animal sugars is accelerated by natural catalytic ferments like **diastase**."
      }
    ]
  },
  "Dashboard — st\\diastasis.md": {
    "primary": "An abnormal separation or parting of two normally attached bones or muscle segments without actual fracture.",
    "secondary": "In cardiology and physiology, the quiescent middle phase of ventricular diastole between rapid ventricular filling and atrial systole.",
    "quotes": [
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "Violent trauma to the ankle frequently causes a complete **diastasis** of the inferior tibiofibular joint without bony fracture."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "In pregnancy, excessive intra-abdominal pressure may lead to permanent **diastasis** of the recti abdominis muscles."
      },
      {
        "author": "Astley Cooper",
        "work": "A Treatise on Dislocations and on Fractures of the Joints",
        "quote": "Epiphyseal **diastasis** in childhood must be managed with extreme gentleness to avoid arresting longitudinal bone growth."
      }
    ]
  },
  "Dashboard — st\\diastatic.md": {
    "primary": "Pertaining to, caused by, or possessing the enzymatic properties of diastase; capable of converting starch into sugar.",
    "secondary": "In brewing, distilling, and grain processing, denoting the enzymatic potency (diastatic power) of malted grains during the mashing process.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Beer",
        "quote": "The brewer relies entirely on the **diastatic** power of malted barley to convert unmalted starches into fermentable sugars."
      },
      {
        "author": "James Prescott Joule",
        "work": "Scientific Papers",
        "quote": "Thermal limits must be strictly observed during mashing, lest high temperatures destroy the **diastatic** activity of the liquor."
      },
      {
        "author": "William Henry Perkin",
        "work": "Industrial Chemistry",
        "quote": "Malt syrups are evaluated industrially by their **diastatic** capacity to liquefy thick starch pastes into transparent syrup."
      }
    ]
  },
  "Dashboard — st\\diasystem.md": {
    "primary": "A higher-level linguistic conceptual framework that abstracts and correlates the structural systems of several closely related dialects or languages.",
    "secondary": "In structural dialectology, Uriel Weinreich's model for mapping phonological and grammatical correspondences across divergent linguistic varieties.",
    "quotes": [
      {
        "author": "Uriel Weinreich",
        "work": "Is a Structural Dialectology Possible?",
        "quote": "A **diasystem** can be constructed by combining the discrete phonemic systems of two dialects into a single comparative formula."
      },
      {
        "author": "Roman Jakobson",
        "work": "Selected Writings: Word and Language",
        "quote": "Dialectological differences cease to appear chaotic once they are integrated into a comprehensive structural **diasystem**."
      },
      {
        "author": "William Labov",
        "work": "The Social Stratification of English in New York City",
        "quote": "The concept of the **diasystem** provided early fieldworkers with an elegant tool to formalize regional vowel shifts."
      }
    ]
  },
  "Dashboard — st\\ecstasy.md": {
    "primary": "An overwhelming state of intense emotion, transcendent joy, or mystic rapture that suspends ordinary conscious thought.",
    "secondary": "In religious mysticism and classical philosophy, a trance state in which the soul transcends the physical body to unite with the divine.",
    "quotes": [
      {
        "author": "Plotinus",
        "work": "The Enneads",
        "quote": "In this transcendent **ecstasy**, the soul casts off every earthly form and attains immediate mystical union with the One."
      },
      {
        "author": "Teresa of Ávila",
        "work": "The Interior Castle",
        "quote": "The soul in profound spiritual **ecstasy** feels itself completely dissolved in divine light and celestial sweetness."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "The hallmark of saintliness is the recurrent immersion in mystical **ecstasy**, where the boundaries of selfhood vanish."
      }
    ]
  },
  "Dashboard — st\\ecstatic.md": {
    "primary": "Characterized by, feeling, or expressing overwhelming rapturous joy or intense delight.",
    "secondary": "Relating to or absorbed in a mystical trance or state of religious ecstasy.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Nature",
        "quote": "Standing on the bare ground, my head bathed by the blithe air, I become an **ecstatic** transparent eyeball; I am nothing; I see all."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "In Dionysian rites, the celebrant experiences an **ecstatic** rupture of individuality, merging with the primal unity of existence."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "Prometheus Unbound",
        "quote": "The spirits of the air burst forth in **ecstatic** melodies that shook the ancient mountains with sublime joy."
      }
    ]
  },
  "Dashboard — st\\epistasis.md": {
    "primary": "The interaction between non-allelic genes whereby the phenotypic expression of one gene locus masks, inhibits, or alters the expression of another gene locus.",
    "secondary": "In evolutionary and statistical genetics, deviations from purely additive allelic effects in the determination of complex quantitative traits.",
    "quotes": [
      {
        "author": "William Bateson",
        "work": "Mendel's Principles of Heredity",
        "quote": "We may describe this phenomenon as **epistasis**, wherein one dominant factor completely obscures the outward effects of an independent gene."
      },
      {
        "author": "Ronald Fisher",
        "work": "The Genetical Theory of Natural Selection",
        "quote": "Although non-linear **epistasis** complicates simple selection models, additive variance remains the primary engine of evolutionary change."
      },
      {
        "author": "Sewall Wright",
        "work": "Evolution and the Genetics of Populations",
        "quote": "Complex adaptive landscapes are shaped largely by rugged peaks of **epistasis**, where specific gene combinations yield superior fitness."
      }
    ]
  },
  "Dashboard — st\\episteme.md": {
    "primary": "Scientific knowledge, systemic understanding, or principled philosophical knowledge (as contrasted with mere opinion or doxa).",
    "secondary": "In Michel Foucault's archaeology of knowledge, the unconscious cultural grid or historical a priori that grounds and conditions all discourse in a given epoch.",
    "quotes": [
      {
        "author": "Michel Foucault",
        "work": "The Order of Things",
        "quote": "The classical **episteme** organized all thought through representation, taxonomy, and the meticulous spatial arrangement of signs."
      },
      {
        "author": "Plato",
        "work": "The Republic",
        "quote": "The philosopher does not content himself with shadowy opinion, but pursues genuine **episteme** grounded in the immutable Forms."
      },
      {
        "author": "Aristotle",
        "work": "Nicomachean Ethics",
        "quote": "We possess **episteme** only when we understand the invariant causes and first principles from which a demonstration proceeds."
      }
    ]
  },
  "Dashboard — st\\epistemic.md": {
    "primary": "Of, relating to, or situated within the realm of knowledge, cognition, or the conditions of justification and belief.",
    "secondary": "In logic and philosophy of language, pertaining to modal operators expressing degrees of certainty, knowability, or probability.",
    "quotes": [
      {
        "author": "Willard Van Orman Quine",
        "work": "Word and Object",
        "quote": "Our theories face the tribunal of sensory experience not as isolated sentences, but as an interconnected **epistemic** web."
      },
      {
        "author": "Roderick Chisholm",
        "work": "Theory of Knowledge",
        "quote": "An **epistemic** principle establishes the rigorous criteria under which a person is justified in asserting that a belief is true."
      },
      {
        "author": "Alvin Goldman",
        "work": "Epistemology and Cognition",
        "quote": "Reliabilism argues that true beliefs possess genuine **epistemic** merit only if generated by truth-conducive cognitive mechanisms."
      }
    ]
  },
  "Dashboard — st\\epistemological.md": {
    "primary": "Relating to epistemology, the philosophical study of the origin, nature, validity, and limits of human knowledge.",
    "secondary": "Pertaining to the theoretical foundations, assumptions, and conceptual presuppositions that govern inquiry within a scientific discipline.",
    "quotes": [
      {
        "author": "Karl Popper",
        "work": "The Logic of Scientific Discovery",
        "quote": "The criterion of falsifiability provides an **epistemological** demarcation between empirical science and metaphysical speculation."
      },
      {
        "author": "Thomas Kuhn",
        "work": "The Structure of Scientific Revolutions",
        "quote": "A paradigm shift is never a mere accumulative addition, but an **epistemological** reordering of how scientists perceive reality."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Our **epistemological** inquiry demonstrates that space and time are not external objects, but pure forms of human sensible intuition."
      }
    ]
  },
  "Dashboard — st\\epistemologist.md": {
    "primary": "A philosopher or scholar who specializes in epistemology, investigating the nature, origins, criteria, and limits of knowledge.",
    "secondary": "A theorist dedicated to evaluating skepticism, justification, foundationalism, and cognitive truth claims.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "Human Knowledge: Its Scope and Limits",
        "quote": "The modern **epistemologist** must navigate between the paralyzing abyss of radical skepticism and the naivety of common sense."
      },
      {
        "author": "A. J. Ayer",
        "work": "Language, Truth, and Logic",
        "quote": "The traditional **epistemologist** erred whenever he sought to extract synthetic truths about reality from pure logical tautologies."
      },
      {
        "author": "Hilary Putnam",
        "work": "Reason, Truth and History",
        "quote": "Any reflective **epistemologist** must discard the myth of God's-eye perspective in favor of an internal, pragmatic realism."
      }
    ]
  },
  "Dashboard — st\\epistemology.md": {
    "primary": "The branch of philosophy that investigates the nature, origin, methods, presuppositions, and boundaries of human knowledge.",
    "secondary": "A philosophical theory or framework explaining how knowledge is acquired, justified, and demarcated from mere opinion or delusion.",
    "quotes": [
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Before embarking on lofty metaphysical speculations, sound **epistemology** demands that we take inventory of the mind's native powers."
      },
      {
        "author": "David Hume",
        "work": "An Enquiry Concerning Human Understanding",
        "quote": "Empirical **epistemology** teaches us to commit to the flames any volume containing neither abstract reasoning nor matters of fact."
      },
      {
        "author": "Ludwig Wittgenstein",
        "work": "On Certainty",
        "quote": "The game of doubting itself presumes a bedrock of certainty; **epistemology** begins where doubt can no longer meaningfully operate."
      }
    ]
  },
  "Dashboard — st\\eustasis.md": {
    "primary": "Worldwide, simultaneous changes in sea level caused by alterations in the absolute volume of ocean water or oceanic basin capacity.",
    "secondary": "In geology and oceanography, glacio-eustasy or tectono-eustasy driving global marine transgressions and regressions across geological time.",
    "quotes": [
      {
        "author": "Eduard Suess",
        "work": "The Face of the Earth",
        "quote": "We coin the term **eustasis** to designate those universal vertical oscillations of the sea surface that encompass all oceanic shores."
      },
      {
        "author": "Reginald Aldworth Daly",
        "work": "The Changing World of the Ice Age",
        "quote": "The growth and decay of continental ice sheets imposed massive glacio-eustatic **eustasis** on Pleistocene coastlines."
      },
      {
        "author": "Arthur Holmes",
        "work": "Principles of Physical Geology",
        "quote": "Sedimentary cyclothems record rhythmic marine transgressions driven by pulses of global **eustasis** throughout the Carboniferous period."
      }
    ]
  }
};

const updated = updateNotesBatch(BASE_DIR, BATCH1_DATA);
console.log(`Action Part 2 - Batch 1 Completed: ${updated} / ${Object.keys(BATCH1_DATA).length} notes updated.`);
