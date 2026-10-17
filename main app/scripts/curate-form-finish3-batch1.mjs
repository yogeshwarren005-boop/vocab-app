import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — plat\\platonic.md": {
    "primary": "Of, relating to, or characteristic of the Greek philosopher Plato, his doctrines, or his philosophical system.",
    "secondary": "In psychology and ethics, designating an affectionate or spiritual relationship between persons that is devoid of sexual or sensual desire.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Out of Plato come all things that are still written and debated among men of thought; he represents the pure **platonic** intellect."
      },
      {
        "author": "Walter Pater",
        "work": "Plato and Platonism",
        "quote": "The essence of the **platonic** method lies in dialectical questioning that refines our grasp of transcendental reality."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Christian theology absorbed a profound **platonic** strain through Augustine and early Patristic thought."
      }
    ]
  },
  "Dashboard — plat\\platonism.md": {
    "primary": "The philosophical doctrine of Plato and his successors, positing that abstract universal Forms possess objective and immutable reality beyond the sensible world.",
    "secondary": "In the philosophy of mathematics, the ontological thesis that mathematical entities exist independently of human minds and physical space-time.",
    "quotes": [
      {
        "author": "Alfred North Whitehead",
        "work": "Process and Reality",
        "quote": "The safest general characterization of the European philosophical tradition is that it consists of a series of footnotes to **platonism**."
      },
      {
        "author": "Willard Van Orman Quine",
        "work": "From a Logical Point of View",
        "quote": "Classical mathematics is committed to ontological **platonism** through its bound variables quantifying over sets."
      },
      {
        "author": "Kurt Gödel",
        "work": "What is Cantor's Continuum Problem?",
        "quote": "Classes and concepts may be conceived as real objects, establishing a defensible foundation for mathematical **platonism**."
      }
    ]
  },
  "Dashboard — plat\\platonist.md": {
    "primary": "An adherent, student, or scholar of Plato's philosophy and the doctrine of ideal Forms.",
    "secondary": "A thinker or writer whose intellectual worldview prioritizes transcendent ideals and metaphysical archetypes over material phenomena.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick; or, The Whale",
        "quote": "Beware of such an one, I say; your whales must be seen before they can be killed; and this sunken-eyed young **platonist** will tow you ten wakes round the world."
      },
      {
        "author": "Sydney Waterlow",
        "work": "Shelley",
        "quote": "A poet who is also a **platonist** is likely to exalt his office, striving to lead mankind nearer to eternal ideal beauty."
      },
      {
        "author": "George Santayana",
        "work": "The Life of Reason",
        "quote": "Every idealist is at heart an instinctive **platonist**, seeking order amid the mutability of temporal life."
      }
    ]
  },
  "Dashboard — plat\\platonistic.md": {
    "primary": "Relating to, resembling, or exhibiting the principles and characteristics of Platonism.",
    "secondary": "In epistemological and aesthetic theory, reflecting an idealizing tendency that looks to metaphysical paradigms rather than empirical observation.",
    "quotes": [
      {
        "author": "Charles Sanders Peirce",
        "work": "Collected Papers",
        "quote": "Scholastic realism embraced a decidedly **platonistic** attitude toward the ontological status of universals."
      },
      {
        "author": "William James",
        "work": "The Meaning of Truth",
        "quote": "Pragmatism stands in stark opposition to those **platonistic** habits of mind that view truth as static contemplation."
      },
      {
        "author": "C. I. Lewis",
        "work": "Mind and the World-Order",
        "quote": "The conceptual framework includes an element that critics might label **platonistic** in its devotion to a priori categories."
      }
    ]
  },
  "Dashboard — plat\\plattdeutsch.md": {
    "primary": "Low German; a group of West Germanic dialects spoken in northern Germany and parts of the eastern Netherlands.",
    "secondary": "In historical linguistics, the Germanic varieties that did not undergo the High German consonant shift, retaining unshifted voiceless stops.",
    "quotes": [
      {
        "author": "Jacob Grimm",
        "work": "Deutsche Grammatik",
        "quote": "The geographic boundaries between High German and **plattdeutsch** illustrate the phonetic impact of the second sound shift."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "In northern provinces, the common speech preserved **plattdeutsch** idioms that reflect an archaic Germanic syntax."
      },
      {
        "author": "Theodor Fontane",
        "work": "Effi Briest",
        "quote": "The old coachman spoke in broad **plattdeutsch**, his sentences rolling with northern cadence and earthy humor."
      }
    ]
  },
  "Dashboard — plat\\platte.md": {
    "primary": "A broad, shallow river in Nebraska flowing into the Missouri River, historically vital to westward overland trails.",
    "secondary": "In geographical and historical narratives, an emblem of the vast alluvial plains and braided stream morphology of the American West.",
    "quotes": [
      {
        "author": "Francis Parkman",
        "work": "The Oregon Trail",
        "quote": "At length we reached the **platte**, whose broad and turbid current rolled sluggishly through the boundless prairie."
      },
      {
        "author": "Washington Irving",
        "work": "The Adventures of Captain Bonneville",
        "quote": "The expedition encamped along the valley of the **platte**, where islands of cottonwood dotted the shallow waters."
      },
      {
        "author": "John C. Frémont",
        "work": "Report of the Exploring Expedition",
        "quote": "We traced the southern fork of the **platte**, noting the shifting sandbars and sparse riparian timber."
      }
    ]
  },
  "Dashboard — plat\\plattensee.md": {
    "primary": "The German name for Lake Balaton, a large, shallow freshwater lake in western Hungary.",
    "secondary": "In European physical geography and limnology, the largest freshwater lake in Central Europe, noted for its extensive silty bed and mild microclimate.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "The shallow basin of the **plattensee** modifies the thermal currents and atmospheric moisture of the Hungarian plains."
      },
      {
        "author": "Karl Baedeker",
        "work": "Austria-Hungary Handbook",
        "quote": "Excursionists frequent the scenic shores of the **plattensee**, renowned for its medicinal baths and vineyards."
      },
      {
        "author": "John Paget",
        "work": "Hungary and Transylvania",
        "quote": "The silver expanse of the **plattensee** stretched before us, bordered by basaltic hills and ancient volcanic cones."
      }
    ]
  },
  "Dashboard — plat\\platy.md": {
    "primary": "Having a flat, plate-like, or tabular structure or appearance.",
    "secondary": "In petrology and pedology, describing mineral crystals or soil peds that are thin and laterally extended in horizontal planes.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "The mineral aggregates exhibit a distinct **platy** habit, cleaving readily along basal planes into thin laminae."
      },
      {
        "author": "Leonard Baver",
        "work": "Soil Physics",
        "quote": "Compacted subsoils frequently develop a **platy** structure that impedes downward percolation of gravitational water."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The fissile shale splits into **platy** fragments under the persistent action of subaerial weathering."
      }
    ]
  },
  "Dashboard — plat\\platycephalidae.md": {
    "primary": "A family of marine scorpaeniform fishes, commonly known as flatheads, possessing an exceptionally depressed head and body.",
    "secondary": "In ichthyology, benthic ambush predators of the Indo-West Pacific, characterized by cryptic coloration and upward-directed eyes.",
    "quotes": [
      {
        "author": "Albert Günther",
        "work": "Catalogue of the Fishes in the British Museum",
        "quote": "The **platycephalidae** inhabit sandy bottoms, their flattened crania allowing them to bury themselves beneath the sediment."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Fishes of the family **platycephalidae** are prized as food fishes in Australian waters and across the eastern tropics."
      },
      {
        "author": "Theodore Gill",
        "work": "Arrangement of the Families of Fishes",
        "quote": "In any natural systematic scheme, the family **platycephalidae** occupies a specialized branch of craniate scorpaenoids."
      }
    ]
  },
  "Dashboard — plat\\platycerium.md": {
    "primary": "A genus of epiphytic ferns in the family Polypodiaceae, commonly known as staghorn or elkhorn ferns.",
    "secondary": "In horticultural botany, tropical epiphytes characterized by two distinct frond types: sterile basal nest fronds and fertile antler-like foliage fronds.",
    "quotes": [
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "The magnificent fronds of **platycerium** cling to forest barks, collecting falling debris within their basal shields."
      },
      {
        "author": "David Fairchild",
        "work": "The World Was My Garden",
        "quote": "Giant specimens of **platycerium** hung suspended from the tropical trees like verdant chandeliers."
      },
      {
        "author": "George Nicholson",
        "work": "The Illustrated Dictionary of Gardening",
        "quote": "Cultivators prize **platycerium** for its dramatic bifurcated leaves resembling the antlers of a stag."
      }
    ]
  },
  "Dashboard — plat\\platyctenea.md": {
    "primary": "An order of ctenophores (comb jellies) that are highly flattened along the oral-aboral axis and adapted to a benthic or creeping lifestyle.",
    "secondary": "In marine invertebrate zoology, organisms that largely reduce their ciliated comb rows in adult stages, adopting sessile or epizoic habits upon corals and echinoderms.",
    "quotes": [
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Protozoa through Ctenophora",
        "quote": "The benthic members of **platyctenea** have abandoned pelagic swimming in favor of creeping upon creeping soles."
      },
      {
        "author": "Alfred Goldsborough Mayor",
        "work": "Ctenophores of the Atlantic Coast of North America",
        "quote": "The anatomical transitions observed in **platyctenea** bridge typical pelagic comb jellies and planar forms."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Development of the Ctenophore Egg",
        "quote": "Embryological cleavage in **platyctenea** confirms their close phylogenetic alignment with tentaculate ctenophores."
      }
    ]
  },
  "Dashboard — plat\\platyctenean.md": {
    "primary": "Of, relating to, or belonging to the Platyctenea, an order of dorsoventrally compressed benthic ctenophores.",
    "secondary": "In marine biology, designating any ctenophore that displays secondary adaptation to creeping or parasitic association on benthic substrates.",
    "quotes": [
      {
        "author": "Robert D. Barnes",
        "work": "Invertebrate Zoology",
        "quote": "The bizarre **platyctenean** morphology superficially resembles that of polyclad flatworms due to extreme flattening."
      },
      {
        "author": "Richard C. Brusca",
        "work": "Invertebrates",
        "quote": "A specialized **platyctenean** species uses retractable tentacles to capture small crustaceans while clinging to alcyonarian soft corals."
      },
      {
        "author": "Thomas Cavalier-Smith",
        "work": "A Revised Six-Kingdom System of Life",
        "quote": "The sedentary lifestyle of the **platyctenean** group represents a notable evolutionary reversal of ancestral ctenophore locomotion."
      }
    ]
  },
  "Dashboard — plat\\platyhelminth.md": {
    "primary": "Any member of the phylum Platyhelminthes, comprising dorsoventrally flattened, bilaterally symmetrical unsegmented worms.",
    "secondary": "In parasitology and invertebrate zoology, acoelomate organisms lacking circulatory and respiratory systems, including planarians, trematodes, and cestodes.",
    "quotes": [
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The typical **platyhelminth** exhibits flame cells that mediate osmoregulation within its parenchymatous mesoderm."
      },
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Platyhelminthes and Rhynchocoela",
        "quote": "No free-living **platyhelminth** possesses an anus; undigested particulate matter must be expelled through the pharyngeal orifice."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "Early morphologists debated whether the primitive **platyhelminth** represented the root ancestor of all triploblastic animals."
      }
    ]
  },
  "Dashboard — plat\\platyhelminthes.md": {
    "primary": "The taxonomic phylum of invertebrate animals consisting of the flatworms, characterized by bilateral symmetry and a triploblastic, acoelomate body plan.",
    "secondary": "In systematic zoology, an extensive animal phylum divided into Turbellaria, Monogenea, Trematoda, and Cestoda, possessing complex reproductive systems.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "The phylum **platyhelminthes** encompasses diverse parasitic lineages that have evolved intricate multi-host life cycles."
      },
      {
        "author": "Edward O. Wilson",
        "work": "The Diversity of Life",
        "quote": "In moist forest litter and ocean sediments, **platyhelminthes** constitute a vital component of micro-invertebrate fauna."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "The flattened geometry of **platyhelminthes** maximizes surface area for diffusion in the total absence of vascular pumps."
      }
    ]
  },
  "Dashboard — plat\\platylobium.md": {
    "primary": "A genus of leguminous shrubs in the pea family (Fabaceae), endemic to eastern and southern Australia, commonly known as flat-peas.",
    "secondary": "In systematic botany, characterized by opposite leaves, solitary pea-shaped flowers, and distinctly flattened, winged legume pods.",
    "quotes": [
      {
        "author": "George Bentham",
        "work": "Flora Australiensis",
        "quote": "The genus **platylobium** is distinguished from Bossiaea by its winged, compressed pod and peculiar calyx structure."
      },
      {
        "author": "Ferdinand von Mueller",
        "work": "Fragmenta Phytographiae Australiae",
        "quote": "We observed bright yellow blossoms of **platylobium** expanding along the sandy ridges of Victoria."
      },
      {
        "author": "Joseph Maiden",
        "work": "The Forest Flora of New South Wales",
        "quote": "In heathland formations, **platylobium** forms attractive understory bushes with papilionaceous corollas."
      }
    ]
  },
  "Dashboard — plat\\platymiscium.md": {
    "primary": "A genus of neotropical trees in the legume family (Fabaceae), yielding heavy, dense timber known commercially as macawood or granadillo.",
    "secondary": "In forestry and wood anatomy, prized for its high dimensional stability, dark variegated heartwood, and resonant qualities in musical instrument making.",
    "quotes": [
      {
        "author": "Samuel J. Record",
        "work": "Timbers of Tropical America",
        "quote": "The lustrous wood of **platymiscium** takes a high polish and resists insect attack with exceptional durability."
      },
      {
        "author": "Paul C. Standley",
        "work": "Trees and Shrubs of Mexico",
        "quote": "Species of **platymiscium** grow in the deciduous and evergreen lowland forests of Central and South America."
      },
      {
        "author": "Julian A. Steyermark",
        "work": "Flora of the Venezuelan Guayana",
        "quote": "Specimens of **platymiscium** along the riparian corridors produce handsome clusters of papilionaceous flowers."
      }
    ]
  },
  "Dashboard — plat\\platypoecilus.md": {
    "primary": "A former genus name for small freshwater livebearing fishes of Central America, now classified within the genus Xiphophorus (the platy).",
    "secondary": "In genetics and evolutionary biology, a historical model organism used extensively to study sex determination, melanoma development, and pigmentation genetics.",
    "quotes": [
      {
        "author": "Charles Tate Regan",
        "work": "A Revision of the Poeciliid Fishes",
        "quote": "The species formerly grouped under **platypoecilus** lack the caudal sword feature characteristic of male swordtails."
      },
      {
        "author": "Myron Gordon",
        "work": "The Genetics of Fish",
        "quote": "Cross-breeding experiments between **platypoecilus** and swordtails revealed inherited macromelanophore patterns prone to malignant transformation."
      },
      {
        "author": "William T. Innes",
        "work": "Exotic Aquarium Fishes",
        "quote": "Known to every hobbyist as the platy, **platypoecilus** exhibits a delightful spectrum of cultivated color variations."
      }
    ]
  },
  "Dashboard — plat\\platypus.md": {
    "primary": "A semi-aquatic, egg-laying mammal (Ornithorhynchus anatinus) of eastern Australia, possessing a duck-like bill, webbed feet, and a beaver-like tail.",
    "secondary": "In evolutionary biology, an archaic monotreme that produces milk without nipples, detects prey via electroreception, and features venomous ankle spurs in males.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "A little time before it was dark, I was lucky enough to see two of the famous **platypus** swimming and diving in the creek."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The paradoxical combination of avian and reptilian skeletal characters in the **platypus** astonished early European anatomists."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Classification and Distribution of the Mammalia",
        "quote": "The oviparous habits of the **platypus** demonstrate its survival as an ancient offshoot of proto-mammalian lineage."
      }
    ]
  },
  "Dashboard — plat\\platyrhine.md": {
    "primary": "Having a broad, flat nose or flattened nasal apertures.",
    "secondary": "In physical anthropology and primatology, designating primates of the New World (Platyrrhini), characterized by widely separated nostrils that open sideways.",
    "quotes": [
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "The **platyrhine** skull differs conspicuously from that of Old World primates in the conformation of the nasal septa."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Facial development in early human embryos briefly passes through a broad, **platyrhine** phase before nasal elevation."
      },
      {
        "author": "William King Gregory",
        "work": "Our Face from Fish to Man",
        "quote": "South American monkeys belong exclusively to the **platyrhine** division of the anthropoid stock."
      }
    ]
  },
  "Dashboard — plat\\platyrhinian.md": {
    "primary": "Pertaining to or possessing broad, flattened nasal characteristics.",
    "secondary": "In comparative craniometry, relating to a skull exhibiting a high nasal index indicating wide nasal bones.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The anatomical distinctions between catarrhine and **platyrhinian** forms underscore a deep geographic bifurcation in primate ancestry."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "In standardized craniometric surveys, a nasal index exceeding 53 denotes a distinctly **platyrhinian** nasal aperture."
      },
      {
        "author": "Earnest Hooton",
        "work": "Up from the Ape",
        "quote": "Certain equatorial populations exhibit **platyrhinian** features that facilitate thermal and moisture exchange in humid climates."
      }
    ]
  },
  "Dashboard — plat\\platyrrhine.md": {
    "primary": "A primate belonging to the New World group Platyrrhini; or relating to this broad-nosed subdivision.",
    "secondary": "In evolutionary primatology, New World monkeys possessing three premolars in each quadrant and frequently prehensile tails.",
    "quotes": [
      {
        "author": "George Gaylord Simpson",
        "work": "The Principles of Classification and a Classification of Mammals",
        "quote": "The **platyrrhine** radiation in South America occurred in geographical isolation from the catarrhines of the Old World."
      },
      {
        "author": "Colin Groves",
        "work": "Primate Taxonomy",
        "quote": "Every known **platyrrhine** monkey shares a specialized tympanic ring fused directly to the petrosal bone."
      },
      {
        "author": "Matt Cartmill",
        "work": "The Human Lineage",
        "quote": "Fossil evidence suggests the ancestral **platyrrhine** arrived in the neotropics via trans-Atlantic sweepstakes rafting in the Oligocene."
      }
    ]
  },
  "Dashboard — plat\\Platyrrhini.md": {
    "primary": "The infraorder or parvorder of anthropoid primates native to Central and South America, characterized by nostrils separated by a broad nasal septum.",
    "secondary": "In systematic mammalogy, comprising five extant families: Callitrichidae, Cebidae, Aotidae, Pitheciidae, and Atelidae.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The History of Creation",
        "quote": "The divergent cranial structures of the **Platyrrhini** confirm that New World monkeys followed an independent evolutionary trajectory."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Within the order Primates, the **Platyrrhini** retain the primitive condition of three premolar teeth per quadrant."
      },
      {
        "author": "Robert Broom",
        "work": "The Origin of the Human Skeleton",
        "quote": "Cranial morphology in the **Platyrrhini** displays marked specialization for arboreal life in dense tropical canopies."
      }
    ]
  },
  "Dashboard — plat\\platyrrhinian.md": {
    "primary": "Pertaining or belonging to the Platyrrhini; having broad-spaced nostrils facing laterally.",
    "secondary": "In physical anthropology and zoology, characterizing the cranial or dental traits unique to South American simians.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Odontography; or, a Treatise on the Comparative Anatomy of the Teeth",
        "quote": "The dental formula of the **platyrrhinian** monkey typically includes thirty-six teeth, preserving extra bicuspids."
      },
      {
        "author": "W. L. H. Duckworth",
        "work": "Morphology and Anthropology",
        "quote": "Comparative analysis reveals that the **platyrrhinian** orbit is separated from the temporal fossa by a complete bony septum."
      },
      {
        "author": "Grafton Elliot Smith",
        "work": "The Evolution of Man",
        "quote": "The cerebral fissures of the **platyrrhinian** brain demonstrate unique cortical folding patterns among arboreal primates."
      }
    ]
  },
  "Dashboard — plat\\platyrrhinic.md": {
    "primary": "Characteristic of or having a platyrrhine nose; possessing a broad nasal aperture.",
    "secondary": "In anthropometric and forensic osteology, describing a skeletal skull with a nasal breadth that is wide relative to its height.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Mémoires d'anthropologie",
        "quote": "Skulls classified as **platyrrhinic** exhibit an index indicating nasal aperture breadth greater than half the nasal height."
      },
      {
        "author": "Arthur Keith",
        "work": "A New Theory of Human Evolution",
        "quote": "The transition from a narrow to a **platyrrhinic** facial morphology is influenced by respiratory adaptation to tropical conditions."
      },
      {
        "author": "Franz Boas",
        "work": "Race, Language and Culture",
        "quote": "Variations between leptorrhinic and **platyrrhinic** skull forms must be analyzed in conjunction with developmental plasticity."
      }
    ]
  },
  "Dashboard — plat\\platysma.md": {
    "primary": "A broad, thin sheet of muscle lying superficial to the deep cervical fascia on either side of the neck.",
    "secondary": "In human surgical anatomy, an expressive muscle innervated by the cervical branch of the facial nerve, acting to depress the mandible and tense the skin of the neck.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **platysma** arises from the fascia covering the upper part of the pectoral and deltoid muscles and ascends across the clavicle."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Beneath the subcutaneous fat of the throat spreads the thin fleshy membrane known as the **platysma** myoides."
      },
      {
        "author": "Frank H. Netter",
        "work": "Atlas of Human Anatomy",
        "quote": "In facial rejuvenation and neck dissection, meticulous re-approximation of the severed **platysma** borders ensures smooth contours."
      }
    ]
  },
  "Dashboard — plat\\platystemon.md": {
    "primary": "A genus of annual wildflowers in the poppy family (Papaveraceae), native to western North America, containing the single species Platystemon californicus (cream cups).",
    "secondary": "In botanical morphology, distinguished by its flattened stamens and a compound ovary consisting of multiple carpels that separate at maturity into one-seeded joints.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Synoptical Flora of North America",
        "quote": "The delicate yellow petals and dilated stamens of **platystemon** brighten the gravelly hills of California each spring."
      },
      {
        "author": "Willis Linn Jepson",
        "work": "A Flora of Western Middle California",
        "quote": "In open coastal grasslands, **platystemon** flowers carpet wide swaths with nodding cream-colored blossoms."
      },
      {
        "author": "LeRoy Abrams",
        "work": "Illustrated Flora of the Pacific States",
        "quote": "The linear carpels of **platystemon** disarticulate transversely when dry, dispersing seeds through mechanical rupture."
      }
    ]
  },
  "Dashboard — plat\\Platyzoa.md": {
    "primary": "A proposed major group or clade of protostome animals including flatworms, rotifers, and gastrotrichs.",
    "secondary": "In phylogenetics, a taxonomic assemblage characterized by a non-coelomate or pseudocoelomate body plan and lack of a complex circulatory system.",
    "quotes": [
      {
        "author": "Thomas Cavalier-Smith",
        "work": "A Revised Six-Kingdom System of Life",
        "quote": "The clade **Platyzoa** unites flatworms and gnathiferans into a coherent assemblage within the spiral-cleaving animals."
      },
      {
        "author": "Kenneth M. Halanych",
        "work": "The New View of Animal Phylogeny",
        "quote": "Molecular analyses utilizing ribosomal RNA sequences provided initial support for the monophyly of **Platyzoa**."
      },
      {
        "author": "Gonzalo Giribet",
        "work": "Assembling the Protostome Tree of Life",
        "quote": "Subsequent phylogenomic data have challenged the cohesion of **Platyzoa**, suggesting certain lineages belong closer to Lophotrochozoa."
      }
    ]
  },
  "Dashboard — plat\\replacement.md": {
    "primary": "The action, process, or instance of substituting one person, object, or concept in place of another.",
    "secondary": "In geology and mineralogy, metasomatic replacement wherein one mineral dissolved by hydrothermal fluid is simultaneously replaced by another.",
    "quotes": [
      {
        "author": "Waldemar Lindgren",
        "work": "Mineral Deposits",
        "quote": "Metasomatic **replacement** involves the simultaneous capillary solution and deposition of minerals by circulating subterranean solutions."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "In every country, new species are introduced by natural selection, leading to the gradual **replacement** of ancestral forms."
      },
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The annual fund destined for the **replacement** of fixed capital must constantly draw upon the gross revenue of society."
      }
    ]
  },
  "Dashboard — pole\\antimonopoly.md": {
    "primary": "Opposed to monopolies or monopolistic economic practices; supporting legal regulation to foster competitive markets.",
    "secondary": "In political economy and jurisprudence, designating legislation or social movements aimed at curbing trust formations and excessive market concentration.",
    "quotes": [
      {
        "author": "Ida Tarbell",
        "work": "The History of the Standard Oil Company",
        "quote": "An intense **antimonopoly** sentiment swept across independent producers whose transport rates had been dictated by the trust."
      },
      {
        "author": "Louis Brandeis",
        "work": "Other People's Money and How the Bankers Use It",
        "quote": "Effective **antimonopoly** regulation must prohibit interlocking directorates that suppress open commercial competition."
      },
      {
        "author": "John Kenneth Galbraith",
        "work": "American Capitalism: The Concept of Countervailing Power",
        "quote": "The traditional American **antimonopoly** tradition seeks to enforce competitive dispersion by legal decree."
      }
    ]
  },
  "Dashboard — pole\\apolemia.md": {
    "primary": "A genus of pelagic siphonophores (colonial hydrozoans) forming extraordinarily long, ribbon-like colonies in open oceanic waters.",
    "secondary": "In marine biology, fragile siphonophores composed of coordinated nectophores and stinging zooids capable of stretching dozens of meters in deep waters.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Report on the Siphonophorae Collected by H.M.S. Challenger",
        "quote": "The polymorphic colonies of **apolemia** drift through the pelagic abyss, trailing extended batteries of urticating tentacles."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "In living specimens of **apolemia**, each individual polyp performs a dedicated nutritional or locomotive function."
      },
      {
        "author": "Carl Chun",
        "work": "Die Siphonophoren der Plankton-Expedition",
        "quote": "Deep-sea dredging operations captured magnificent fragments of **apolemia**, revealing complex colonial budding."
      }
    ]
  },
  "Dashboard — pole\\duopoly.md": {
    "primary": "A market condition or industry structure in which only two suppliers or sellers dominate the market for a commodity or service.",
    "secondary": "In microeconomic game theory, an oligopolistic model wherein two competing firms determine price and output strategies based on mutual anticipation.",
    "quotes": [
      {
        "author": "Antoine Augustin Cournot",
        "work": "Researches into the Mathematical Principles of the Theory of Wealth",
        "quote": "In the case of a **duopoly**, each proprietor adjusts his output on the assumption that his rival's production remains constant."
      },
      {
        "author": "Joseph Schumpeter",
        "work": "Capitalism, Socialism and Democracy",
        "quote": "A stable **duopoly** may temporarily avoid ruinous price-cutting through unspoken consensus or differentiated branding."
      },
      {
        "author": "Joan Robinson",
        "work": "The Economics of Imperfect Competition",
        "quote": "Price determination under conditions of **duopoly** remains inherently indeterminate without assumptions regarding rival reactions."
      }
    ]
  },
  "Dashboard — pole\\monopolist.md": {
    "primary": "A person, corporation, or entity that possesses, controls, or seeks to obtain an exclusive monopoly in a given market.",
    "secondary": "In political economy, an agent with the power to restrict output in order to sell at a price significantly exceeding marginal cost.",
    "quotes": [
      {
        "author": "Adam Smith",
        "work": "The Wealth of Nations",
        "quote": "The **monopolist**, by keeping the market constantly understocked, sells his commodities much above their natural price."
      },
      {
        "author": "David Ricardo",
        "work": "Principles of Political Economy and Taxation",
        "quote": "Commodities which are subject to a monopoly are not regulated by the cost of production; the **monopolist** governs supply at will."
      },
      {
        "author": "John Stuart Mill",
        "work": "Principles of Political Economy",
        "quote": "Whenever an enterprise falls into the hands of a single private **monopolist**, the public interest demands statutory limitation."
      }
    ]
  },
  "Dashboard — pole\\monopolistic.md": {
    "primary": "Having the nature or characteristics of a monopoly; possessing or aiming at exclusive market dominance.",
    "secondary": "In industrial economics, designating market structures—such as monopolistic competition—where firms sell differentiated products with slight pricing power.",
    "quotes": [
      {
        "author": "Edward Chamberlin",
        "work": "The Theory of Monopolistic Competition",
        "quote": "Under **monopolistic** competition, product differentiation grants each vendor a tiny insulated realm of price control."
      },
      {
        "author": "Thorstein Veblen",
        "work": "The Theory of Business Enterprise",
        "quote": "Modern corporate strategy increasingly pivots on securing **monopolistic** advantages over strategic resource channels."
      },
      {
        "author": "Paul Sweezy",
        "work": "The Theory of Capitalist Development",
        "quote": "The growth of industrial trusts fosters **monopolistic** price structures that inhibit competitive market clearance."
      }
    ]
  },
  "Dashboard — pole\\monopolization.md": {
    "primary": "The act, process, or practice of obtaining exclusive possession or control of a market, commodity, or sphere of activity.",
    "secondary": "In antitrust law, the unlawful acquisition or maintenance of monopoly power through anticompetitive, predatory, or exclusionary conduct.",
    "quotes": [
      {
        "author": "William Howard Taft",
        "work": "The Anti-Trust Act and the Supreme Court",
        "quote": "Section two of the statute expressly prohibits every contract, combination, or conspiracy tending toward the **monopolization** of interstate trade."
      },
      {
        "author": "Richard Posner",
        "work": "Antitrust Law",
        "quote": "To prove illegal **monopolization**, the plaintiff must establish possession of monopoly power coupled with exclusionary business conduct."
      },
      {
        "author": "Alfred Chandler",
        "work": "The Visible Hand: The Managerial Revolution in American Business",
        "quote": "The rapid **monopolization** of refining infrastructure enabled standard managerial practices to dominate national distribution."
      }
    ]
  },
  "Dashboard — pole\\monopolize.md": {
    "primary": "To obtain, secure, or exercise exclusive control or possession of a commodity, service, or market.",
    "secondary": "In interpersonal or social contexts, to dominate conversation, attention, or resources to the exclusion of others.",
    "quotes": [
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "In democratic societies, when a few men attempt to **monopolize** public honors, the multitude quickly reasserts its claims."
      },
      {
        "author": "Karl Marx",
        "work": "Capital: A Critique of Political Economy",
        "quote": "Giant industrial combinations strive to **monopolize** whole spheres of production, centralizing capital into fewer hands."
      },
      {
        "author": "Theodore Roosevelt",
        "work": "The Strenuous Life",
        "quote": "We do not wish to destroy corporations, but we insist that no single enterprise shall **monopolize** the necessities of life."
      }
    ]
  },
  "Dashboard — pole\\monopolizer.md": {
    "primary": "One who monopolizes; a person or commercial entity that acquires exclusive control of a trade, commodity, or conversation.",
    "secondary": "In legal and economic history, an individual who corners the market by engrossing, regrating, or forestalling vital provisions.",
    "quotes": [
      {
        "author": "Thomas More",
        "work": "Utopia",
        "quote": "The rich **monopolizer** hoards corn until scarcity inflates the price, enriching himself upon the misery of the commonwealth."
      },
      {
        "author": "Jeremy Bentham",
        "work": "Defense of Usury",
        "quote": "Public prejudice routinely casts the speculative merchant as an extortionate **monopolizer** regardless of the service he renders."
      },
      {
        "author": "Thomas Jefferson",
        "work": "Writings of Thomas Jefferson",
        "quote": "I hope we shall crush in its birth the aristocracy of our monied corporations, lest the corporate **monopolizer** dictate our laws."
      }
    ]
  },
  "Dashboard — pole\\oligopolist.md": {
    "primary": "A seller, producer, or firm operating in an oligopolistic market characterized by a small number of dominant competitors.",
    "secondary": "In industrial economics, a market participant whose pricing and production decisions explicitly depend upon the anticipated strategies of rival firms.",
    "quotes": [
      {
        "author": "William Fellner",
        "work": "Competition Among the Few: Oligopoly and Similar Market Structures",
        "quote": "An **oligopolist** realizes that an aggressive reduction in price will instantly provoke retaliatory cuts from his few competitors."
      },
      {
        "author": "George Stigler",
        "work": "The Theory of Price",
        "quote": "The fundamental dilemma confronting the **oligopolist** is whether to engage in tacit collusion or risk independent rivalry."
      },
      {
        "author": "Paul Samuelson",
        "work": "Economics: An Introductory Analysis",
        "quote": "Because every **oligopolist** watches his neighbors keenly, price stability often prevails even when market demand fluctuates."
      }
    ]
  },
  "Dashboard — pole\\oligopoly.md": {
    "primary": "A market condition or economic structure in which a market or industry is dominated by a small number of large sellers or producers.",
    "secondary": "In economic theory, an industry structure where high barriers to entry allow existing firms to earn supernormal profits through strategic interdependence.",
    "quotes": [
      {
        "author": "Joseph Stiglitz",
        "work": "Principles of Microeconomics",
        "quote": "In an **oligopoly**, each enterprise must consider how its competitors will respond before altering its output or price."
      },
      {
        "author": "F. M. Scherer",
        "work": "Industrial Market Structure and Economic Performance",
        "quote": "The degree of seller concentration determines whether an **oligopoly** behaves like an overt cartel or a fiercely competitive arena."
      },
      {
        "author": "Edward Chamberlin",
        "work": "The Theory of Monopolistic Competition",
        "quote": "Mutual dependence recognized among vendors is the defining hallmark of pure **oligopoly**."
      }
    ]
  },
  "Dashboard — pole\\pole.md": {
    "primary": "A long, slender, cylindrical piece of wood, metal, or other material, typically erected vertically to provide support or suspension.",
    "secondary": "In physics and geography, either of the two extreme points of an axis of rotation, or either of the two opposed terminals of a magnet or electric cell.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden; or, Life in the Woods",
        "quote": "I planted a tall bean-**pole** in the garden, watching the tendrils climb spirally toward the morning light."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Electricity",
        "quote": "The magnetic force concentrates with intense vigor at each **pole** of the bar, manifesting opposite polarities."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "Lines of induction issue from the positive **pole** and curve gracefully through space toward the negative terminal."
      }
    ]
  },
  "Dashboard — pole\\poleax.md": {
    "primary": "A medieval European staff weapon or battle-axe combining an axe blade, hammerhead, and spear point on a long shaft.",
    "secondary": "A heavy butcher's tool with a spiked or blunt head historically used to stun livestock prior to slaughter.",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "The Canterbury Tales: The Knight's Tale",
        "quote": "With mace and **poleax** the fierce knights struck, while sparks flew from their battered helmets."
      },
      {
        "author": "Sir Walter Scott",
        "work": "Ivanhoe",
        "quote": "The stalwart yeoman wielded his heavy **poleax**, beating back the men-at-arms at the castle gate."
      },
      {
        "author": "Howard Pyle",
        "work": "The Merry Adventures of Robin Hood",
        "quote": "He grasped the stout **poleax** firmly, ready to defend the bridge against all comers."
      }
    ]
  },
  "Dashboard — pole\\poleaxe.md": {
    "primary": "A variant spelling of poleax, designating a combination axe-hammer polearm used by medieval and Renaissance knights.",
    "secondary": "To strike, fell, or knock down with or as if with a heavy poleaxe; to stun or overwhelm completely.",
    "quotes": [
      {
        "author": "Thomas Malory",
        "work": "Le Morte d'Arthur",
        "quote": "Sir Lancelot drew his **poleaxe** and smote the knight through helm and shield down to the earth."
      },
      {
        "author": "Robert Louis Stevenson",
        "work": "The Black Arrow",
        "quote": "The shock of the iron-shod **poleaxe** echoed through the timbered hall as the battle raged."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The White Company",
        "quote": "With his mighty **poleaxe**, the veteran archer held the narrow stairway against a dozen assailants."
      }
    ]
  },
  "Dashboard — pole\\polemical.md": {
    "primary": "Of, relating to, or involving strongly critical, controversial, or disputatious argument or writing.",
    "secondary": "In literary criticism and rhetoric, characterized by aggressive partisan advocacy aimed at dismantling an opponent's doctrine.",
    "quotes": [
      {
        "author": "Friedrich Nietzsche",
        "work": "On the Genealogy of Morality",
        "quote": "This small book contains three **polemical** essays designed to uncover the psychological roots of modern asceticism."
      },
      {
        "author": "Matthew Arnold",
        "work": "Culture and Anarchy",
        "quote": "The noisy, **polemical** tone of theological debates often obscures the calm pursuit of sweet reasonableness."
      },
      {
        "author": "Bertrand Russell",
        "work": "Sceptical Essays",
        "quote": "In political discourse, honest factual analysis is too frequently replaced by passionate, **polemical** rhetoric."
      }
    ]
  },
  "Dashboard — pole\\polemically.md": {
    "primary": "In a polemical manner; by means of controversial, passionate, or disputatious argument.",
    "secondary": "In rhetorical analysis, adopting an aggressive or adversarial stance rather than a neutral or expository tone.",
    "quotes": [
      {
        "author": "Søren Kierkegaard",
        "work": "Concluding Unscientific Postscript to Philosophical Fragments",
        "quote": "The author proceeds **polemically** against the speculative systematizers who confuse objective knowledge with inward faith."
      },
      {
        "author": "C. S. Lewis",
        "work": "The Abolition of Man",
        "quote": "I am arguing not **polemically** for an individual point of view, but on behalf of traditional moral valuation."
      },
      {
        "author": "Jürgen Habermas",
        "work": "The Philosophical Discourse of Modernity",
        "quote": "He formulated his thesis **polemically** to shake the complacency of prevailing sociological paradigms."
      }
    ]
  },
  "Dashboard — pole\\polemicise.md": {
    "primary": "To engage in polemics or controversial argumentation; to write or argue in a disputatious manner (British spelling).",
    "secondary": "In political and literary journalism, to take up the pen aggressively against an ideological adversary.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "Essays",
        "quote": "He did not hesitate to **polemicise** against the dogmas of orthodox political parties whenever intellectual honesty required it."
      },
      {
        "author": "Christopher Hitchens",
        "work": "Letters to a Young Contrarian",
        "quote": "To **polemicise** effectively, one must study the strongest arguments of one's opponent and strike at their core."
      },
      {
        "author": "E. P. Thompson",
        "work": "The Poverty of Theory",
        "quote": "We must openly **polemicise** against structuralist abstractions that reduce human agency to passive effect."
      }
    ]
  },
  "Dashboard — pole\\polemicist.md": {
    "primary": "A person who writes or argues in a passionate, controversial, or polemical manner; a skilled disputant.",
    "secondary": "In intellectual history, an author renowned for attacking established orthodoxy, dogmas, or rival philosophical schools.",
    "quotes": [
      {
        "author": "H. L. Mencken",
        "work": "Prejudices: First Series",
        "quote": "The brilliant **polemicist** cares far less for converting the dullard than for exposing the absurdity of his shibboleths."
      },
      {
        "author": "Jonathan Swift",
        "work": "A Tale of a Tub",
        "quote": "Every partisan pamphlet proclaimed its author a consummate **polemicist** ready to demolish all theological opponents."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Prefaces",
        "quote": "A dramatist must at times become a fearless **polemicist**, using the stage to puncture moral hypocrisies."
      }
    ]
  },
  "Dashboard — pole\\polemicize.md": {
    "primary": "To engage in verbal or written controversy; to argue disputatiously against a position or opponent.",
    "secondary": "In philosophy and critical theory, to direct critical discourse explicitly toward refuting another's conceptual paradigm.",
    "quotes": [
      {
        "author": "Karl Marx",
        "work": "The Poverty of Philosophy",
        "quote": "Throughout these chapters we **polemicize** against Proudhon's economic contradictions and utopian illusions."
      },
      {
        "author": "Walter Benjamin",
        "work": "The Arcades Project",
        "quote": "The critic's duty is not simply to classify, but to **polemicize** against the reification of historical consciousness."
      },
      {
        "author": "Theodor Adorno",
        "work": "Minima Moralia: Reflections from Damaged Life",
        "quote": "To write philosophy today means to **polemicize** against the totalizing claims of the culture industry."
      }
    ]
  },
  "Dashboard — pole\\polemics.md": {
    "primary": "The practice or art of engaging in aggressive verbal or written controversy and disputation.",
    "secondary": "In theology and intellectual history, a branch of discourse dedicated to the systematic defense of doctrine against heresy or dissent.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Areopagitica",
        "quote": "Truth needs no policies, no stratagems, nor licensing to make her victorious in the open field of **polemics**."
      },
      {
        "author": "Immanuel Kant",
        "work": "Critique of Pure Reason",
        "quote": "Reason has no need for censorship, since the **polemics** of reason serve to awaken philosophy from dogmatic slumber."
      },
      {
        "author": "William Hazlitt",
        "work": "Table-Talk; or, Original Essays",
        "quote": "The bitter **polemics** of sectarian pamphleteers frequently consume the very charity they profess to defend."
      }
    ]
  },
  "Dashboard — pole\\polemise.md": {
    "primary": "A variant spelling of polemicise; to engage in public argument or write controversial essays.",
    "secondary": "In rhetorical contexts, to direct critical commentary against opposing aesthetic or literary movements.",
    "quotes": [
      {
        "author": "Virginia Woolf",
        "work": "The Common Reader",
        "quote": "When Victorian reviewers began to **polemise** over morality in art, they often overlooked the beauty of style."
      },
      {
        "author": "Terry Eagleton",
        "work": "Literary Theory: An Introduction",
        "quote": "Critical theorists frequently **polemise** over the social function of art in contemporary culture."
      },
      {
        "author": "Raymond Williams",
        "work": "Keywords: A Vocabulary of Culture and Society",
        "quote": "Scholars continue to **polemise** over the political implications embedded in the vocabulary of democracy."
      }
    ]
  },
  "Dashboard — pole\\polemist.md": {
    "primary": "A person skilled in or given to polemics; a disputant or controversial writer (variant of polemicist).",
    "secondary": "In literary history, an essayist whose work is distinguished by vigorous ideological debate and satirical attack.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Biographia Literaria",
        "quote": "The eager **polemist** often mistakes the heat of personal resentment for the divine warmth of truth."
      },
      {
        "author": "Thomas De Quincey",
        "work": "Confessions of an English Opium-Eater and Other Writings",
        "quote": "In every scholarly contest, this formidable **polemist** brought forth an armory of classical quotations."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Our wandering philosopher turned **polemist**, battering the hollow conventions of dandified society."
      }
    ]
  },
  "Dashboard — pole\\polemize.md": {
    "primary": "To carry on polemical warfare or disputes; to engage in controversial debate (variant of polemicize).",
    "secondary": "In scholarly and methodological discourse, to contest theoretical foundations through vigorous written critique.",
    "quotes": [
      {
        "author": "William James",
        "work": "Pragmatism: A New Name for Some Old Ways of Thinking",
        "quote": "It is futile to **polemize** indefinitely about abstract concepts when practical consequences decide the issue."
      },
      {
        "author": "Max Weber",
        "work": "The Methodology of the Social Sciences",
        "quote": "Sociologists must not merely **polemize** against competing ideologies, but maintain rigorous value-neutral analysis."
      },
      {
        "author": "John Dewey",
        "work": "Logic: The Theory of Inquiry",
        "quote": "Philosophers spend centuries attempting to **polemize** over dualisms that inquiry dissolves into functional distinctions."
      }
    ]
  },
  "Dashboard — pole\\polemoniaceae.md": {
    "primary": "A family of flowering plants in the order Ericales, commonly known as the phlox family.",
    "secondary": "In systematic botany, comprising herbs, shrubs, and small trees characterized by five-lobed corollas, five stamens, and a three-locular ovary.",
    "quotes": [
      {
        "author": "John Torrey",
        "work": "Flora of the State of New York",
        "quote": "The family **polemoniaceae** includes the popular garden phloxes as well as wild Jacob's ladder."
      },
      {
        "author": "Nathaniel Lord Britton",
        "work": "An Illustrated Flora of the Northern United States and Canada",
        "quote": "Members of **polemoniaceae** are predominantly North American, flourishing across western montane and prairie habitats."
      },
      {
        "author": "Arthur Cronquist",
        "work": "An Integrated System of Classification of Flowering Plants",
        "quote": "In floral morphology, **polemoniaceae** exhibit regular, bisexual blossoms with twisted aestivation in the bud."
      }
    ]
  },
  "Dashboard — pole\\polemoniaceous.md": {
    "primary": "Of, relating to, or belonging to the botanical family Polemoniaceae.",
    "secondary": "In descriptive floristics, exhibiting the structural characteristics—such as a three-parted style and capsular fruit—of the phlox family.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The collected specimen exhibits unmistakable **polemoniaceous** affinities in its tubular corolla and tripartite stigma."
      },
      {
        "author": "Charles Sprague Sargent",
        "work": "The Silva of North America",
        "quote": "Few species among the **polemoniaceous** genera achieve arborescent stature, remaining mostly herbaceous perennials."
      },
      {
        "author": "John Kunkel Small",
        "work": "Flora of the Southeastern United States",
        "quote": "Along coastal sand dunes, several **polemoniaceous** species produce vibrant terminal cymes throughout the summer."
      }
    ]
  },
  "Dashboard — pole\\polemoniales.md": {
    "primary": "An order of dicotyledonous flowering plants in traditional botanical classification systems, containing Polemoniaceae and allied families.",
    "secondary": "In historical taxonomy, an ordinal grouping roughly equivalent to the modern order Solanales or expanded Ericales in phylogenetic classifications.",
    "quotes": [
      {
        "author": "George Bentham",
        "work": "Genera Plantarum",
        "quote": "Under the order **polemoniales**, botanists grouped sympetalous families characterized by hypogynous stamens alternating with corolla lobes."
      },
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "The systematic placement of **polemoniales** connected primitive tubiflorous dicotyledons with advanced campanulate forms."
      },
      {
        "author": "Robert F. Thorne",
        "work": "Classification and Geography of the Flowering Plants",
        "quote": "Comparative serological studies helped realign the heterogeneous components traditionally assigned to the **polemoniales**."
      }
    ]
  },
  "Dashboard — pole\\polemonium.md": {
    "primary": "A genus of flowering plants in the family Polemoniaceae, commonly known as Jacob's ladder, bearing pinnate leaves and bell-shaped blue or purple flowers.",
    "secondary": "In horticulture and alpine floras, cold-tolerant perennial herbs prized for rock gardens and woodland borders.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Under the genus **polemonium**, we include the classical Greek plant renowned for its pinnate foliage resembling a ladder."
      },
      {
        "author": "John Gerard",
        "work": "The Herball or Generall Historie of Plantes",
        "quote": "The blue flowers of **polemonium** open gracefully in midsummer, adorning gardens with upright sprays of azure bells."
      },
      {
        "author": "William Robinson",
        "work": "The English Flower Garden",
        "quote": "Few hardy perennials equal **polemonium** for naturalizing beneath deciduous shade trees and along moist borders."
      }
    ]
  },
  "Dashboard — pole\\polenta.md": {
    "primary": "A traditional northern Italian dish of boiled coarsely ground yellow or white cornmeal, served hot as porridge or cooled and sliced.",
    "secondary": "In culinary history, an ancient staple dating back to Roman barley or spelt pulmentum, transformed in modern times by maize cultivation.",
    "quotes": [
      {
        "author": "Pellegrino Artusi",
        "work": "Science in the Kitchen and the Art of Eating Well",
        "quote": "In the northern provinces, steaming **polenta** forms the daily bread of the peasant table, poured onto wooden platters."
      },
      {
        "author": "Elizabeth David",
        "work": "Italian Food",
        "quote": "A dish of golden **polenta** topped with stewed wild mushrooms is one of the great autumnal consolations of Lombardy."
      },
      {
        "author": "Ernest Hemingway",
        "work": "A Farewell to Arms",
        "quote": "We sat by the hearth in the inn, eating hot **polenta** and roast hare while the mountain wind rattled the shutters."
      }
    ]
  },
  "Dashboard — pole\\poler.md": {
    "primary": "A person who propels or steers a boat using a pole, especially in shallow or sluggish waters.",
    "secondary": "A draft horse or mule hitched beside the pole (wagon tongue) of a vehicle, bearing steering and braking loads.",
    "quotes": [
      {
        "author": "Mark Twain",
        "work": "Life on the Mississippi",
        "quote": "The weary keelboat **poler** threw his whole weight against the ash shaft, thrusting the heavy craft upstream against the eddy."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "Our Indian guide, an expert **poler**, guided the birch canoe through boiling rapids where oars were useless."
      },
      {
        "author": "Willa Cather",
        "work": "My Ántonia",
        "quote": "The team labored through the mud, the heavy wheel-horse and his sturdy **poler** straining together under the harness."
      }
    ]
  },
  "Dashboard — pole\\polestar.md": {
    "primary": "The North Star (Polaris); the prominent star located closest to the north celestial pole.",
    "secondary": "Something that serves as a guiding principle, beacon, or lodestar directing moral conduct or navigation.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick; or, The Whale",
        "quote": "Look at the needle; it is fixed true to the **polestar**, holding its eternal heading while our canvas strains in the gale."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Self-Reliance",
        "quote": "Let a man keep his eye on his own **polestar**, steering steadfastly without reference to the fluctuating applause of crowds."
      },
      {
        "author": "John Keats",
        "work": "Bright Star! Would I Were Steadfast as Thou Art",
        "quote": "Watching the sleepless **polestar** suspended aloft in lone splendor, gazing over the dark waters of the nocturnal world."
      }
    ]
  },
  "Dashboard — pomph\\podopompholyx.md": {
    "primary": "A vesicular dermatological eruption or form of eczema affecting exclusively or predominantly the soles and edges of the feet.",
    "secondary": "In clinical dermatology, a manifestation of dyshidrotic eczema characterized by deep-seated, pruritic 'tapioca-like' vesicles on the plantar surfaces.",
    "quotes": [
      {
        "author": "Jonathan Hutchinson",
        "work": "Lectures on Clinical Surgery",
        "quote": "In chronic **podopompholyx**, the symmetrical eruption of tense bullae across the soles causes severe pain upon walking."
      },
      {
        "author": "William Allen Pusey",
        "work": "The Principles and Practice of Dermatology",
        "quote": "Topical drying agents and rest are indispensable in managing acute recurrent **podopompholyx** in warm climates."
      },
      {
        "author": "Thomas Bateman",
        "work": "A Practical Synopsis of Cutaneous Diseases",
        "quote": "The plantar vesicle outbreak termed **podopompholyx** displays little tendency to spontaneous suppuration unless secondarily infected."
      }
    ]
  },
  "Dashboard — pomph\\pompholyx.md": {
    "primary": "Dyshidrotic eczema; an acute or recurrent inflammatory skin condition characterized by tiny, intensely itchy blisters on the palms and soles.",
    "secondary": "In historical dermatology, any sudden eruption of vesicular bullae without primary erythema, often triggered by stress, sweating, or contact allergens.",
    "quotes": [
      {
        "author": "Tilbury Fox",
        "work": "Skin Diseases: Their Description, Pathology, Diagnosis, and Treatment",
        "quote": "I proposed the term **pompholyx** for that distressing affection wherein clear sago-grain vesicles erupt along the sides of the fingers."
      },
      {
        "author": "Robert Willan",
        "work": "On Cutaneous Diseases",
        "quote": "The transparent bullae of **pompholyx** arise suddenly without antecedent fever, drying into thin brownish crusts."
      },
      {
        "author": "Jean-Louis Alibert",
        "work": "Monographie des dermatoses",
        "quote": "Vesicular eruptions conforming to **pompholyx** demand soothing emollients rather than aggressive mercurial salves."
      }
    ]
  },
  "Dashboard — prefix\\Examples.md": {
    "primary": "Instances, models, or cases that serve to illustrate, explain, or exemplify a general principle, rule, or category.",
    "secondary": "In pedagogical and rhetorical traditions, concrete representative specimens utilized to establish precedent or provide moral and instructional guidance.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "In the discovery of sciences, we must not rely solely on abstract axioms but test them perpetually against living **examples**."
      },
      {
        "author": "Samuel Johnson",
        "work": "A Dictionary of the English Language (Preface)",
        "quote": "I have extracted illuminating **examples** from our best writers to fix the pronunciation and illustrate the varied significations of words."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Clear **examples** assist the mind in grasping complex ideas far more readily than lengthy formal definitions."
      }
    ]
  },
  "Dashboard — prefix\\prefix.md": {
    "primary": "An affix attached to the beginning of a word, base, or stem to modify its grammatical function or lexical meaning.",
    "secondary": "In morphology and historical linguistics, a bound morpheme that alters semantic valence or creates derivative lexical categories.",
    "quotes": [
      {
        "author": "Otto Jespersen",
        "work": "A Modern English Grammar on Historical Principles",
        "quote": "The negative **prefix** un- combines with adjectives of native and foreign origin with exceptional productivity."
      },
      {
        "author": "Leonard Bloomfield",
        "work": "Language",
        "quote": "When a bound form precedes the root in word-formation, we classify it structurally as a **prefix**."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The psychological association between a **prefix** and its root contributes to the syntagmatic solidarity of compound terms."
      }
    ]
  },
  "Dashboard — prefix\\prefixation.md": {
    "primary": "The morphological process of forming new words by attaching a prefix to a root, base, or stem.",
    "secondary": "In structural and comparative linguistics, an affixation process contrasting with suffixation and infixation, often altering word meaning without changing lexical class.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Languages differ fundamentally in whether they rely upon **prefixation** or suffixation to express relational concepts."
      },
      {
        "author": "Laurie Bauer",
        "work": "English Word-Formation",
        "quote": "Unlike suffixation, derivational **prefixation** in English rarely changes the word class of the underlying base."
      },
      {
        "author": "Noam Chomsky",
        "work": "The Morphophonemics of Modern Hebrew",
        "quote": "Morphological rules governing **prefixation** interact directly with stem vocalism and syllabic weight."
      }
    ]
  },
  "Dashboard — proter\\isoproterenol.md": {
    "primary": "A synthetic sympathomimetic medication that acts as a potent, non-selective beta-adrenergic receptor agonist.",
    "secondary": "In clinical pharmacology and cardiology, an intravenous catecholamine analog used to treat severe bradycardia, heart block, and historically refractory bronchospasm.",
    "quotes": [
      {
        "author": "Raymond P. Ahlquist",
        "work": "A Study of the Adrenotropic Receptors",
        "quote": "The remarkable potency of **isoproterenol** in relaxing bronchial musculature provided key evidence for distinct beta-receptor mediation."
      },
      {
        "author": "Louis S. Goodman",
        "work": "The Pharmacological Basis of Therapeutics",
        "quote": "Administration of **isoproterenol** produces positive inotropic and chronotropic cardiac responses accompanied by peripheral vasodilation."
      },
      {
        "author": "Earl W. Sutherland",
        "work": "The Biological Role of Adenosine-3',5'-Phosphate",
        "quote": "Stimulation of myocardial tissue with **isoproterenol** markedly accelerates the intracellular synthesis of cyclic AMP."
      }
    ]
  },
  "Dashboard — proter\\metaproterenol.md": {
    "primary": "A synthetic beta-2 adrenergic receptor agonist medication used primarily as a bronchodilator in the treatment of asthma and COPD.",
    "secondary": "In clinical pharmacology, a resorcinol derivative (also known as orciprenaline) possessing longer duration of action and greater cardiac safety than isoproterenol.",
    "quotes": [
      {
        "author": "Alfred Goodman Gilman",
        "work": "Goodman & Gilman's The Pharmacological Basis of Therapeutics",
        "quote": "The substitution of a resorcinol ring in **metaproterenol** renders it resistant to catechol-O-methyltransferase degradation."
      },
      {
        "author": "Reuben M. Cherniack",
        "work": "Respiration in Health and Disease",
        "quote": "Inhaled **metaproterenol** rapidly relieves bronchoconstriction by promoting smooth muscle relaxation across the bronchial tree."
      },
      {
        "author": "John A. Nadel",
        "work": "Textbook of Respiratory Medicine",
        "quote": "For acute reversible airway obstruction, aerosolized **metaproterenol** provides prompt symptomatic relief with moderate beta-selectivity."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 3 Batch 1.`);
