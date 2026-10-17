import { updateNotesBatch } from './curate-updater-util.mjs';
import path from 'path';

const CLUSTER_DIR = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — clad\\cladogenesis.md": {
    "primary": "The evolutionary splitting of a parent species into two or more distinct descendant lineages.",
    "secondary": "In macroevolution and cladistics, lineage branching that generates biodiversity, in contrast to gradual phyletic change within a single unbranching lineage (anagenesis).",
    "quotes": [
      {
        "author": "Julian Huxley",
        "work": "Evolution: The Modern Synthesis",
        "quote": "Through repeated events of **cladogenesis**, an ancestral stock radiates into diverse ecological niches across an archipelago."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Geographic isolation serves as the indispensable physical catalyst for genuine evolutionary **cladogenesis**."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "The fossil record records long periods of stasis punctuated by rapid episodes of **cladogenesis**."
      }
    ]
  },
  "Dashboard — clad\\cladogram.md": {
    "primary": "A branching treelike diagram used in cladistics to show ancestral relations and genealogical affinities between taxa.",
    "secondary": "In phylogenetic systematics, a diagram that displays the topology of shared derived character states (synapomorphies) without implying evolutionary time or divergence rate.",
    "quotes": [
      {
        "author": "Willi Hennig",
        "work": "Phylogenetic Systematics",
        "quote": "A properly constructed **cladogram** depicts nested hierarchies of sister groups supported by derived character states."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "Every node on a **cladogram** represents a hypothetical speciation event connecting two sister lineages."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Blind Watchmaker",
        "quote": "By arranging anatomical features in an unambiguous **cladogram**, the biologist reconstructs the family tree of life."
      }
    ]
  },
  "Dashboard — clad\\cladonia.md": {
    "primary": "A widespread genus of cup and reindeer lichens in the family Cladoniaceae, characterized by hollow branching podetia.",
    "secondary": "In lichenology and polar ecology, fruticose lichens that form dense carpets in boreal tundra and provide the primary winter forage for caribou.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "The spongy floor of the spruce forest was carpeted with pale branching cushions of **Cladonia**."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "In high subarctic latitudes, vast plains are covered solely by species of **Cladonia**, sustaining immense herds of reindeer."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The scarlet-tipped apothecia of **Cladonia** cristatella gleam brightly upon rotting pine stumps in early spring."
      }
    ]
  },
  "Dashboard — clad\\cladoniaceae.md": {
    "primary": "A family of lichen-forming fungi in the order Lecanorales, characterized by a dimorphic thallus bearing upright stalks (podetia).",
    "secondary": "In systematic mycology, ascomycete lichens exhibiting a crustose or squamulose primary thallus surmounted by fruticose secondary structures.",
    "quotes": [
      {
        "author": "William Gilson Farlow",
        "work": "Notes on the Cryptogamic Flora of the White Mountains",
        "quote": "Specimens belonging to **Cladoniaceae** cover the granite slopes, anchored tenaciously against alpine gales."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Cyclopedia of American Agriculture",
        "quote": "In the subarctic biome, members of **Cladoniaceae** constitute the predominant ground vegetation across barren peatlands."
      },
      {
        "author": "John Merle Coulter",
        "work": "A Text-Book of Botany for Colleges and Universities",
        "quote": "The morphological complexity of **Cladoniaceae** illustrates the cooperative physiological balance achieved between fungus and alga."
      }
    ]
  },
  "Dashboard — clad\\cladophyll.md": {
    "primary": "A flattened, leaflike stem or branch that functions as a photosynthetic leaf.",
    "secondary": "In descriptive plant morphology, a cladode exhibiting foliar characteristics while bearing modified scale leaves, nodes, and buds along its margins.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The butcher's-broom produces what appears to be a stiff spiny leaf, which is in anatomical truth a modified **cladophyll**."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "In smilax and ornamental asparagus, each delicate green scale functioning as foliage is technically a **cladophyll**."
      },
      {
        "author": "John Muir",
        "work": "The Mountains of California",
        "quote": "Desert succulents conserve moisture by reducing true foliage and conducting transpiration through a fleshy **cladophyll**."
      }
    ]
  },
  "Dashboard — clad\\cladorhyncus.md": {
    "primary": "A genus of Australian wading birds in the family Recurvirostridae, represented by the banded stilt (Cladorhynchus leucocephalus).",
    "secondary": "In ornithology, nomadic shorebirds inhabiting ephemeral inland hypersaline lakes and breeding opportunistically following desert rain events.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Birds of Australia",
        "quote": "The banded stilt, described under **Cladorhynchus**, frequents the brackish lagoons of the southern interior in immense nomadic flocks."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "Australian saltpans harbor specialized avian forms such as **Cladorhynchus**, adapted to hyper-saline aquatic foraging."
      },
      {
        "author": "Gregory Mathews",
        "work": "The Birds of Australia: Volume III",
        "quote": "The long, slender bill and webbed front toes of **Cladorhynchus** distinguish it from other members of the stilt family."
      }
    ]
  },
  "Dashboard — clad\\cladrastis.md": {
    "primary": "A genus of deciduous leguminous trees in the pea family Fabaceae, commonly known as yellowwoods.",
    "secondary": "In dendrology and forestry, ornamental hardwood trees characterized by fragrant pendulous white blossoms, pinnate leaves, and bright yellow heartwood yielding a natural dye.",
    "quotes": [
      {
        "author": "Charles Sprague Sargent",
        "work": "The Silva of North America",
        "quote": "In early summer, the Kentucky yellowwood, **Cladrastis** kentukea, adorns limestone river bluffs with cascades of fragrant white petals."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Manual of Cultivated Plants",
        "quote": "Pioneer settlers extracted a vivid yellow dye from the freshly cut heartwood of **Cladrastis**."
      },
      {
        "author": "John Muir",
        "work": "A Thousand-Mile Walk to the Gulf",
        "quote": "I rested beneath a handsome **Cladrastis** on the riverbank, admiring its smooth bark and elegant foliage."
      }
    ]
  },
  "Dashboard — clad\\heterocladic.md": {
    "primary": "Characterized by or having branches of different types, forms, or structural orders.",
    "secondary": "In developmental bryology and morphology, describing plants or colonial organisms whose branching system comprises dimorphic or heteromorphic branch types.",
    "quotes": [
      {
        "author": "William Gilson Farlow",
        "work": "Marine Algae of New England",
        "quote": "The thallus exhibits a distinctly **heterocladic** habit, bearing short reproductive ramuli alongside long vegetative axes."
      },
      {
        "author": "Adolf Engler",
        "work": "Die Natürlichen Pflanzenfamilien",
        "quote": "In certain mosses, the stem exhibits **heterocladic** differentiation between spreading lateral shoots and flagelliform stolons."
      },
      {
        "author": "D'Arcy Wentworth Thompson",
        "work": "On Growth and Form",
        "quote": "Physical flow gradients induce **heterocladic** growth patterns in colonial hydroids facing asymmetric currents."
      }
    ]
  },
  "Dashboard — clad\\unclad.md": {
    "primary": "Not clothed; naked, bare, or stripped of covering.",
    "secondary": "In literary and descriptive style, exposed to view without embellishment, protective foliage, or architectural sheathing.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "So passd they naked on, nor shund the sight / Of God or Angel, for they thought no ill: / So hand in hand they passd, the loveliest pair / That ever since in loves imbraces met, / Adam the goodliest man of men since borne / His Sons, the fairest of her Daughters Eve, / Under a tuft of shadie arborous roof / In naked majesty stood **unclad**."
      },
      {
        "author": "Thomas Hardy",
        "work": "Under the Greenwood Tree",
        "quote": "The wintry branches stood stark and **unclad** against the cold grey sweep of the December sky."
      },
      {
        "author": "Walt Whitman",
        "work": "Leaves of Grass",
        "quote": "I bathe in the creek, rejoicing to stand clean and **unclad** beneath the open midday sun."
      }
    ]
  },
  "Dashboard — cleist\\cleist.md": {
    "primary": "A combining form derived from Greek kleistos, meaning closed, shut, or enclosed.",
    "secondary": "In botanical and zoological terminology, an affix denoting organs, flowers, or anatomical structures that remain permanently closed or seal off cavities.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "The Greek stem **cleist** designates closed floral structures that accomplish self-fertilization without ever expanding."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In morphological compounding, the prefix **cleist** denotes an organ or spore chamber that lacks a natural opening."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Morphologists use the root **cleist** to indicate structures sealed within an impenetrable membranous capsule."
      }
    ]
  },
  "Dashboard — cleist\\cleistes.md": {
    "primary": "A genus of terrestrial orchids in the family Orchidaceae, commonly called rosebud orchids or small spreading pogonias.",
    "secondary": "In systematic orchidology, bog-dwelling orchids native to the Americas bearing solitary, semi-tubular pink blossoms that appear partially closed.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Genera and Species of Orchidaceous Plants",
        "quote": "In **Cleistes**, the floral perianth forms a delicate tubular throat whose petals remain partially connivent."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Native to coastal pine savannahs, **Cleistes** divaricata enchants botanists with its slender purple-veined lip."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "A rare terrestrial orchid belonging to **Cleistes** was collected in the sphagnum meadows of the pine barrens."
      }
    ]
  },
  "Dashboard — cleist\\cleistocarp.md": {
    "primary": "A completely closed fruiting body or ascocarp that possesses no specialized aperture or ostiole for spore discharge.",
    "secondary": "In mycology and bryology, an ascocarp (cleistothecium) or moss capsule that ruptures irregularly or decays to liberate its spores.",
    "quotes": [
      {
        "author": "Miles Joseph Berkeley",
        "work": "Outlines of British Fungology",
        "quote": "In the powdery mildews, the **cleistocarp** forms a dark spherical vessel completely enclosing the asci until mechanical rupture."
      },
      {
        "author": "John Merle Coulter",
        "work": "Morphology of Gymnosperms and Cryptogams",
        "quote": "Spore dispersal from a **cleistocarp** depends on the gradual decay of the peridium rather than explosive dehiscence."
      },
      {
        "author": "William Gilson Farlow",
        "work": "Synoptic Flora of North American Fungi",
        "quote": "Appendages radiating from the outer wall of the **cleistocarp** anchor the fruiting body to host foliage."
      }
    ]
  },
  "Dashboard — cleist\\cleistogamic.md": {
    "primary": "Characterized by having flowers that do not open and are self-pollinated in the bud; cleistogamous.",
    "secondary": "In floral ecology, describing specialized reproductive structures adapted to ensure seed set under adverse environmental conditions without relying on insect pollinators.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "The tiny **cleistogamic** flowers of Viola odorata lie concealed beneath dead leaves, yielding seeds with extraordinary economy."
      },
      {
        "author": "Asa Gray",
        "work": "How Plants Behave",
        "quote": "Many wild legumes produce inconspicuous **cleistogamic** blossoms that fertilize themselves without waiting for honeybees."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Under low light conditions, impatiens switches from chasmogamic displays to prolific **cleistogamic** seed production."
      }
    ]
  },
  "Dashboard — cleist\\cleistogamous.md": {
    "primary": "Producing flowers that remain closed and are automatically self-fertilized within the bud.",
    "secondary": "In plant biology, designating a breeding system that provides guaranteed reproductive assurance at minimal energetic cost compared to open chasmogamous flowers.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "Plants bearing **cleistogamous** flowers economize their pollen to a wonderful degree, producing only a fraction of the grains found in ordinary blooms."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Faith in a Seed",
        "quote": "Beneath the showy spring petals of the violet lie hidden **cleistogamous** pods, steadily ripening plump seeds against the damp ground."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The evolution of **cleistogamous** reproduction in isolated plant populations safeguards locally adapted genotypes from swamping."
      }
    ]
  },
  "Dashboard — cleist\\cleistogamy.md": {
    "primary": "The condition of producing small, closed, self-fertilizing flowers that never open.",
    "secondary": "In evolutionary botany, a reproductive strategy that functions as a fail-safe mechanism to guarantee pollination when pollinators or weather conditions are unfavorable.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "The study of **cleistogamy** demonstrates that nature can resort to perpetual self-fertilization when cross-pollination becomes too hazardous."
      },
      {
        "author": "Asa Gray",
        "work": "Darwiniana: Essays and Reviews Pertaining to Darwinism",
        "quote": "In many woodland herbs, **cleistogamy** operates in autumn after the early insect-visited blossoms have completed their display."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "Adaptive flexibility is well illustrated by the coexistence of outcrossing and **cleistogamy** on the very same stem."
      }
    ]
  },
  "Dashboard — cleist\\cleistothecium.md": {
    "primary": "A completely closed, globose ascocarp lacking a specialized opening or ostiole, characteristic of powdery mildews.",
    "secondary": "In systematic mycology, a protective spherical fungal structure from which mature ascospores are liberated solely by mechanical rupture, weathering, or decay of the peridium wall.",
    "quotes": [
      {
        "author": "Miles Joseph Berkeley",
        "work": "Introduction to Cryptogamic Botany",
        "quote": "Under the microscope, each mature **cleistothecium** appears as a dark sphere adorned with bifurcated hooked appendages."
      },
      {
        "author": "William Gilson Farlow",
        "work": "The Gymnosporangia or Cedar-Apples of the United States",
        "quote": "During autumn the overwintering **cleistothecium** matures upon fallen leaves, safeguarding asci against freezing desiccation."
      },
      {
        "author": "John Merle Coulter",
        "work": "Morphology of Gymnosperms",
        "quote": "The enclosed architecture of the **cleistothecium** represents a distinct evolutionary departure from the open apothecium."
      }
    ]
  },
  "Dashboard — cleist\\enterocleisis.md": {
    "primary": "The closure, occlusion, or surgical obliteration of the intestinal lumen.",
    "secondary": "In gastroenterology and gastrointestinal surgery, pathological blockage or deliberate operative closure of a segment of intestine or an intestinal fistula.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic fibrotic strictures of the ileum occasionally produce insidious symptoms of complete **enterocleisis**."
      },
      {
        "author": "Sir Frederick Treves",
        "work": "Intestinal Obstruction: Its Varieties with Their Pathology, Diagnosis, and Treatment",
        "quote": "To remediate the persistent fecal fistula, the surgeon performed a formal **enterocleisis** to restore continuous mucosal continuity."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Cicatricial contraction following ulcerative enteritis may culminate in mechanical **enterocleisis**."
      }
    ]
  },
  "Dashboard — cleist\\kleisma.md": {
    "primary": "A minute musical microtonal interval equal to about 8.11 cents, defined by the frequency ratio 15625/15552.",
    "secondary": "In musical acoustics and tuning theory, the minute comma by which six minor thirds exceed an octave, or the difference between the diesis and five syntonic commas.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "On the Sensations of Tone as a Physiological Basis for the Theory of Music",
        "quote": "In subtle microtonal temperaments, the acoustic difference known as a **kleisma** marks the fine boundary of ear discrimination."
      },
      {
        "author": "Harry Partch",
        "work": "Genesis of a Music",
        "quote": "To accommodate just 53-tone scales, one must reckon with tiny pitch fractions such as the **kleisma**."
      },
      {
        "author": "John Rayleigh",
        "work": "The Theory of Sound",
        "quote": "The tiny acoustic interval of a **kleisma** demonstrates how compounding intervals generates residual discrepancies from pure octaves."
      }
    ]
  },
  "Dashboard — cleithr\\Clathrus.md": {
    "primary": "A genus of saprobic lattice stinkhorn fungi in the family Phallaceae, known for their hollow, basket-like, lattice-structured fruiting bodies.",
    "secondary": "In systematic mycology, fungi whose egg-like volva ruptures to expand into an intricate scarlet or orange latticed sphere coated with fetid gleba to attract flies.",
    "quotes": [
      {
        "author": "Miles Joseph Berkeley",
        "work": "Outlines of British Fungology",
        "quote": "The astonishing scarlet cage of **Clathrus** cancellatus resembles an intricate filigree sphere upon the woodland floor."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "In tropical humus we encountered a bizarre fungus of the genus **Clathrus**, whose bright lattice emitted a strong carrion stench."
      },
      {
        "author": "William Gilson Farlow",
        "work": "Notes on the Cryptogamic Flora of the White Mountains",
        "quote": "The polygonal meshwork characterizing **Clathrus** demonstrates an extraordinary mechanical design for expanding spore surfaces."
      }
    ]
  },
  "Dashboard — cleithr\\cleithr.md": {
    "primary": "A classical combining form derived from Greek kleithron, meaning a bar, bolt, key, or locked enclosure.",
    "secondary": "In comparative osteology and psychopathology, an affix designating locking skeletal girdle bones (cleithrum) or phobic dread of enclosed, locked spaces.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Archetype and Homologies of the Vertebrate Skeleton",
        "quote": "The anatomist derives the term from **cleithr**, signifying a locking bar that braces the pectoral girdle against lateral stress."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In osteological compounding, the root **cleithr** identifies the dermal brace anchoring the pectoral arch in teleost fishes."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The prefix **cleithr** designates that visceral terror of locked confinement which drives claustrophobic panic."
      }
    ]
  },
  "Dashboard — cleithr\\cleithrophobia.md": {
    "primary": "An abnormal, morbid, and irrational fear of being trapped, locked in, or enclosed in a confined space.",
    "secondary": "In clinical psychology and psychiatry, a specific phobic disorder triggered specifically by the actual physical lock or barrier preventing escape, distinguishing it from general claustrophobia.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In acute **cleithrophobia**, the mere click of a latch on a cellar door can induce sudden paroxysms of blind terror."
      },
      {
        "author": "Sigmund Freud",
        "work": "Inhibitions, Symptoms and Anxiety",
        "quote": "The psychic anxiety underlying **cleithrophobia** often traces to early childhood experiences of locked punishment."
      },
      {
        "author": "H. G. Wells",
        "work": "The Door in the Wall and Other Stories",
        "quote": "He felt a cold surge of **cleithrophobia** seize his chest as the heavy vault doors slowly swung shut."
      }
    ]
  },
  "Dashboard — cleithr\\cleithrum.md": {
    "primary": "A major membrane bone on each side of the pectoral girdle in bony fishes and early tetrapods.",
    "secondary": "In comparative vertebrate osteology, the large dermal bone that anchors the pectoral fin girdle to the skull via the supracleithrum, lost or vestigial in modern amniotes.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In teleostean fishes, the massive **cleithrum** constitutes the principal skeletal pillar supporting the base of the pectoral fin."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals",
        "quote": "The clavicle of higher vertebrates was long homologized with the fish **cleithrum**, until dermal girdle homologies were clarified."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "In primitive labyrinthodont amphibians, a prominent **cleithrum** still caps the dorsal tip of the scapulocoracoid."
      }
    ]
  },
  "Dashboard — coel\\blastocele.md": {
    "primary": "The fluid-filled cavity of a blastula; the blastocoel.",
    "secondary": "In developmental embryology, the primary segmentation cavity formed during early cleavage stages that separates the inner cell mass or blastoderm from outer blastomeres.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Repeated cleavage divisions produce a hollow spherical blastula enclosing a spacious **blastocele**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "During gastrulation, invaginating endodermal cells gradually obliterate the pre-existing **blastocele**."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Development of the Frog's Egg",
        "quote": "The eccentrically placed **blastocele** in the amphibian embryo occupies the animal hemisphere."
      }
    ]
  },
  "Dashboard — coel\\blastocoel.md": {
    "primary": "The central fluid-filled primary segmentation cavity of an early animal embryo at the blastula stage.",
    "secondary": "In developmental biology, the cavity that provides spatial room for cell migration during gastrulation and prevents premature inductive interactions between animal and vegetal cells.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The primary body cavity or **blastocoel** arises as a simple fluid space between dividing cleavage spheres."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "Cells inward migrating through the blastopore displace the **blastocoel** until only the archenteron remains."
      },
      {
        "author": "Sydney Brenner",
        "work": "Loose Ends",
        "quote": "Laser ablation of specific blastomeres within the nematode **blastocoel** revealed cell-autonomous fate specification."
      }
    ]
  },
  "Dashboard — coel\\blastocoele.md": {
    "primary": "The fluid-filled internal cavity of the blastula stage in early embryonic development; blastocoel.",
    "secondary": "In comparative embryology, the transient primary segmentation cavity that precedes the formation of the true coelom or archenteron.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The expansion of the **blastocoele** results from active fluid secretion by the enclosing envelope of blastodermic cells."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "In echinoderm gastrulation, mesenchyme cells detach and migrate actively through the jelly-like contents of the **blastocoele**."
      },
      {
        "author": "Hans Driesch",
        "work": "The Science and Philosophy of the Organism",
        "quote": "Isolated blastomeres of the sea urchin egg develop into harmonious dwarf blastulae enclosing a proportionate **blastocoele**."
      }
    ]
  },
  "Dashboard — coel\\blastocoelic.md": {
    "primary": "Of, relating to, or situated within the blastocoel of an embryo.",
    "secondary": "In cellular embryology, describing fluid, extracellular matrix molecules, or migrating primary mesenchyme cells located inside the blastocoel cavity.",
    "quotes": [
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Inheritance",
        "quote": "Fibronectin fibrils coating the **blastocoelic** wall provide physical tracks for inward migrating presumptive mesoderm."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "Comparative Embryology",
        "quote": "The **blastocoelic** fluid contains dissolved proteids that maintain osmotic turgor within the expanding blastosphere."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "Experimental Embryology",
        "quote": "Microinjection of signaling factors directly into the **blastocoelic** cavity alters ventral cell fates."
      }
    ]
  },
  "Dashboard — coel\\coel.md": {
    "primary": "A combining form derived from Greek koilos, meaning hollow, empty, or cavity.",
    "secondary": "In biological terminology and comparative anatomy, an affix denoting anatomical cavities, body spaces, or the embryonic coelom.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "From the Greek **coel**, signifying a hollow space, we coin terms for the primary and secondary cavities of living organisms."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The affix **coel** identifies anatomical excavations, whether embryonic blastocoels or the adult somatic coelom."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In phylogenetic terminology, **coel** distinguishes the genuine mesodermal body cavity from hemocoelic spaces."
      }
    ]
  },
  "Dashboard — coel\\coelacanth.md": {
    "primary": "A rare, ancient order of lobe-finned marine fishes with paired fleshy fins, once believed to have been extinct since the late Cretaceous.",
    "secondary": "In evolutionary biology and ichthyology, a renowned 'living fossil' (genus Latimeria) possessing a hollow cartilaginous spine and an intracranial joint, closely allied to tetrapod ancestors.",
    "quotes": [
      {
        "author": "J. L. B. Smith",
        "work": "Old Fourlegs: The Story of the Coelacanth",
        "quote": "I would not have been more astonished if I had met a living dinosaur walking down the street than I was when I saw that **coelacanth**."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "The discovery of a living **coelacanth** in 1938 was the greatest zoological sensation of the twentieth century."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "The **coelacanth** paddles its paired fleshy fins in an alternating gait reminiscent of a land vertebrate walking on four legs."
      }
    ]
  },
  "Dashboard — coel\\coelenterata.md": {
    "primary": "A traditional phylum or taxonomic group of aquatic invertebrates encompassing cnidarians (corals, sea anemones, jellyfish) and ctenophores.",
    "secondary": "In systematic invertebrate zoology, diploblastic metazoans possessing a single central digestive body cavity (coelenteron) that serves both digestive and circulatory functions.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "I proposed the division of **Coelenterata** to unite those radially symmetrical animals whose digestive cavity coincides with the general body space."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "The medusae and siphonophores belonging to **Coelenterata** display geometric radial symmetries of incomparable beauty."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Our investigations into **Coelenterata** prove that hydroids and acalephs are developmental phases of one unified plan of creation."
      }
    ]
  },
  "Dashboard — coel\\coelenterate.md": {
    "primary": "Any invertebrate animal belonging to the traditional phylum Coelenterata, such as a jellyfish, sea anemone, or coral.",
    "secondary": "In marine biology, a diploblastic radially symmetrical animal possessing specialized stinging cells (cnidocytes) and a gastrovascular cavity.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "A delicate, transparent **coelenterate** drifted past the ship, trailing long iridescent tentacles through the phosphorescent water."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "In every true **coelenterate**, the body consists of two cellular layers, ectoderm and endoderm, separated by a gelatinous mesoglea."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "The sea anemone is a sedentary **coelenterate** whose petal-like tentacles trap unwary shrimp upon the tidal ledge."
      }
    ]
  },
  "Dashboard — coel\\coelenteron.md": {
    "primary": "The central digestive cavity of a cnidarian or ctenophore, having a single opening that serves as both mouth and anus.",
    "secondary": "In comparative invertebrate anatomy, the gastrovascular cavity that carries out both enzymatic digestion and the circulatory distribution of nutrients.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Ingested food passes directly through the mouth into the spacious **coelenteron**, where extracellular digestion begins."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The primitive gut or **coelenteron** of the gastraea represents the ancestral prototype of all metazoan digestive tracts."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Flagellated gastrodermal cells lining the **coelenteron** maintain a steady current to circulate oxygen and chyme."
      }
    ]
  },
  "Dashboard — coel\\coeliac.md": {
    "primary": "Of, relating to, or located in the abdominal cavity.",
    "secondary": "In human anatomy and pathology, designating the coeliac trunk (artery), coeliac plexus, or coeliac disease (gluten-sensitive enteropathy).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **coeliac** artery arises from the anterior aspect of the abdominal aorta just below the aortic hiatus of the diaphragm."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Samuel Gee originally described the **coeliac** affliction as a chronic indigestion occurring in persons of all ages."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "Round the Red Lamp",
        "quote": "The surgeon traced the pulsation of the deep **coeliac** axis before placing his ligature with trembling precision."
      }
    ]
  },
  "Dashboard — coel\\coeloglossum.md": {
    "primary": "A genus of terrestrial orchids commonly known as frog orchids, now often classified within Dactylorhiza.",
    "secondary": "In botanical taxonomy, northern temperate meadow orchids characterized by a hollow, spurred labellum shaped like a tiny frog or tongue.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by which Orchids are Fertilised by Insects",
        "quote": "In **Coeloglossum** viride, the green labellum produces glistening droplets of nectar in a shallow furrow to attract small beetles."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Specimens of **Coeloglossum** were gathered on subalpine pasture slopes, their inconspicuous green flowers blending with surrounding grasses."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "Standard Cyclopedia of Horticulture",
        "quote": "The bracted frog orchid, **Coeloglossum** bracteatum, thrives in moist calcareous woodlands across the northern states."
      }
    ]
  },
  "Dashboard — coel\\coelogyne.md": {
    "primary": "A genus of epiphytic and lithophytic orchids native to tropical and subtropical Asia, characterized by pendulous clusters of fragrant blossoms.",
    "secondary": "In horticulture and systematic botany, pseudobulbous orchids possessing a deeply concave or hollow stigma and prominent hooded column.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Genera and Species of Orchidaceous Plants",
        "quote": "I established **Coelogyne** in allusion to the deeply excavated, cup-shaped stigma characteristic of the flower."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Massive clumps of white-flowered **Coelogyne** hung suspended from high forest branches like aromatic garlands."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Species of **Coelogyne** from Himalayan elevations require cool, humid greenhouse culture to bloom abundantly."
      }
    ]
  },
  "Dashboard — coel\\coelom.md": {
    "primary": "The principal fluid-filled body cavity in most triploblastic animals, situated between the body wall and the digestive canal.",
    "secondary": "In animal embryology and anatomy, a true body cavity completely lined by mesodermally derived epithelium (peritoneum).",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "The evolution of the true **coelom** liberated internal visceral organs to pulse and contract independently of somatic musculature."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In annelids, the spacious **coelom** is partitioned into segmental chambers by transverse muscular septa."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The origin of the triploblastic **coelom** represents one of the major architectural transitions in metazoan history."
      }
    ]
  },
  "Dashboard — coel\\coelomate.md": {
    "primary": "Any animal possessing a true coelom lined by mesodermal peritoneum.",
    "secondary": "In systematic zoology, triploblastic bilateral organisms (including mollusks, annelids, arthropods, echinoderms, and chordates) having a coelomic body plan.",
    "quotes": [
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In every advanced **coelomate** animal, internal organs are cushioned against mechanical shock within fluid-filled mesodermal spaces."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The Cambrian explosion witnessed the simultaneous emergence of virtually every major **coelomate** body architecture."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "A true **coelomate** displays compartmentalized organs suspended by double folds of peritoneal mesentery."
      }
    ]
  },
  "Dashboard — coel\\coelomic.md": {
    "primary": "Of, relating to, or situated within the coelom.",
    "secondary": "In comparative anatomy and physiology, describing the fluid, cellular lining, or circulating amoebocytes of the secondary body cavity.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The hydrostatic pressure of the **coelomic** fluid provides the essential hydraulic skeleton for earthworm burrowing."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "Primary germ cells migrate along the dorsal mesentery into the developing **coelomic** epithelium."
      },
      {
        "author": "William Morton Wheeler",
        "work": "Ants: Their Structure, Development and Behavior",
        "quote": "In insect metamorphosis, the ancestral **coelomic** cavities coalesce into an extensive open hemocoel."
      }
    ]
  },
  "Dashboard — coel\\coelophysis.md": {
    "primary": "A genus of small, slender, bipedal carnivorous theropod dinosaurs from the late Triassic period.",
    "secondary": "In vertebrate paleontology, an early fast-running dinosaur characterized by hollow, thin-walled limb bones and a narrow, sharply toothed skull.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Dinosauria of the Laramie and Trias",
        "quote": "I propose the name **Coelophysis** in reference to the hollow, bird-like character of its fossilized limb shafts."
      },
      {
        "author": "Edwin H. Colbert",
        "work": "The Little Dinosaurs of Ghost Ranch",
        "quote": "The extraordinary quarry at Ghost Ranch yielded hundreds of articulated skeletons of **Coelophysis** entombed in flash-flood silt."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Eight Little Piggies",
        "quote": "Colbert's meticulous reconstruction showed **Coelophysis** as an agile predator whose hollow bones foreshadowed avian skeletons."
      }
    ]
  },
  "Dashboard — coel\\coelostat.md": {
    "primary": "An astronomical apparatus comprising a plane mirror driven by clockwork to rotate once in 48 hours around an axis parallel to the Earth's axis, reflecting a motionless image of a star or the sun into a fixed telescope.",
    "secondary": "In solar physics and observational astronomy, a precision instrumentation system that tracks the sun continuously without requiring the movement of massive spectrographs or long-focus vertical solar telescopes.",
    "quotes": [
      {
        "author": "George Ellery Hale",
        "work": "The Study of Stellar Evolution",
        "quote": "The flat mirror of the **coelostat** turns slowly upon its polar axis, casting an unmoving beam of sunlight into the horizontal telescope."
      },
      {
        "author": "Arthur Eddington",
        "work": "Space, Time and Gravitation",
        "quote": "During the 1919 solar eclipse expedition, light from the corona was fed by a **coelostat** into the long-focus photographic cameras."
      },
      {
        "author": "Simon Newcomb",
        "work": "Popular Astronomy",
        "quote": "Using a **coelostat** permits the astronomer to employ bulky, temperature-controlled laboratory spectroscopes impossible to mount on moving tubes."
      }
    ]
  },
  "Dashboard — coel\\enterocoely.md": {
    "primary": "The developmental process by which the coelom arises as outpocketings or pouches from the embryonic archenteron (primitive gut).",
    "secondary": "In comparative embryology, a fundamental developmental pathway characteristic of deuterostomes (such as echinoderms and chordates), contrasting with schizocoely in protostomes.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "In amphioxus, the body cavity forms by **enterocoely**, wherein pouches of the archenteron pinch off to establish paired coelomic sacs."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "The occurrence of **enterocoely** across both echinoderms and primitive chordates provides compelling evidence of their deep genealogical affinity."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Deuterostome phylogeny rests firmly upon the embryological observation of tripartite **enterocoely** during early organogenesis."
      }
    ]
  },
  "Dashboard — coel\\pseudocoelomate.md": {
    "primary": "An invertebrate animal possessing a pseudocoel—a fluid-filled body cavity that is not entirely lined by mesoderm.",
    "secondary": "In systematic invertebrate zoology, an animal (such as a nematode, rotifer, or kinorhynch) having a body space derived directly from the embryonic blastocoel rather than true mesodermal tissue.",
    "quotes": [
      {
        "author": "Libbie Hyman",
        "work": "The Invertebrates: Acanthocephala, Aschelminthes, and Entoprocta",
        "quote": "A typical **pseudocoelomate** lacks visceral peritoneum, leaving internal organs bathed directly in fluid bounded by somatic muscle."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The simple wormlike habitus of the **pseudocoelomate** phyla represents an ancient, successful ecological compromise."
      },
      {
        "author": "Sydney Brenner",
        "work": "The Genetics of Caenorhabditis elegans",
        "quote": "Under differential interference contrast, the internal anatomy of this microscopic **pseudocoelomate** shines with crystal clarity."
      }
    ]
  },
  "Dashboard — coel\\schizocoelomate.md": {
    "primary": "Any animal whose coelom develops by schizocoely, through the splitting of solid masses of embryonic mesodermal tissue.",
    "secondary": "In comparative embryology, a classification grouping protostomes (such as annelids, arthropods, and mollusks) whose body cavity originates by cavitation of paired mesodermal bands.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "In every typical **schizocoelomate**, the primary mesoderm forms solid lateral cords which subsequently hollow out into segmented vesicles."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie",
        "quote": "The splitting of the mesoblastic blocks in a **schizocoelomate** stands in marked contrast to the outpocketing seen in enterocoelates."
      },
      {
        "author": "E. Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Annelid evolution clearly illustrates the **schizocoelomate** pattern of body cavity construction accompanied by homonomous metamery."
      }
    ]
  },
  "Dashboard — coel\\schizocoely.md": {
    "primary": "The embryonic process in which the coelom is formed by the splitting of solid blocks of mesodermal tissue.",
    "secondary": "In developmental biology, a diagnostic ontogenetic feature of protostome coelomates whereby cells proliferate from the 4d blastomere and delaminate to generate the peritoneal cavity.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The formation of the coelomic spaces by **schizocoely** reflects the intense local proliferation and separation of mesoblast cells."
      },
      {
        "author": "Edmund Beecher Wilson",
        "work": "The Cell in Development and Heredity",
        "quote": "In polychaete development, **schizocoely** proceeds with rigorous mathematical regularity following spiral cleavage."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Ontogeny and Phylogeny",
        "quote": "The divergence between enterocoely and **schizocoely** provided classical morphologists with their primary criterion for dividing the Animalia."
      }
    ]
  },
  "Dashboard — coel\\spongocoel.md": {
    "primary": "The large, central cavity of a sponge through which water flows before exiting via the osculum.",
    "secondary": "In invertebrate anatomy, the internal atrium (atrium spongiosum) lined in simple asconoid sponges by flagellated choanocytes that filter food particles from circulating water.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Water drawn through thousands of microscopic dermal pores pours into the spacious **spongocoel** before being ejected at the terminal osculum."
      },
      {
        "author": "Louis Agassiz",
        "work": "Methods of Study in Natural History",
        "quote": "The beating flagella lining the **spongocoel** generate an unceasing current vital for nutrition and respiration."
      },
      {
        "author": "Rachel Carson",
        "work": "The Edge of the Sea",
        "quote": "Within the sheltered chamber of the **spongocoel**, tiny commensal shrimps and brittle stars find sanctuary from shore predators."
      }
    ]
  },
  "Dashboard — cotyl\\cotyl.md": {
    "primary": "A combining form derived from Greek kotyle, meaning cup, small vessel, or cup-shaped socket.",
    "secondary": "In anatomical and botanical nomenclature, an affix designating cup-shaped structures such as the acetabular cotyloid cavity or embryonic seed leaves (cotyledons).",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "The Greek root **cotyl** designates a cup or vessel, describing the hollow, nourishing embryonic seed leaf."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Comparative anatomists employ the stem **cotyl** to denote deep articular cups such as the hip acetabulum."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "In morphological terminology, **cotyl** forms the base for classifying angiosperms by their seed-leaf architecture."
      }
    ]
  },
  "Dashboard — cotyl\\cotyledon.md": {
    "primary": "An embryonic leaf in seed-bearing plants, one or more of which are the first leaves to appear from a germinating seed.",
    "secondary": "In botany and physiology, a primary seed leaf storing or absorbing nutrients for the developing seedling; also in mammalian placentation, a functional vascular tuft or lobe.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "As germination proceeds, each **cotyledon** arches upward toward the light, executing delicate circumnutation movements."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Faith in a Seed",
        "quote": "The expanding **cotyledon** of the young pine thrusts aside the dry forest mulch like a green hand opening to the sun."
      },
      {
        "author": "John Ray",
        "work": "Historia Plantarum",
        "quote": "The fundamental division of flowering vegetation depends on whether the embryo bears a single **cotyledon** or two."
      }
    ]
  },
  "Dashboard — cotyl\\cotyloid.md": {
    "primary": "Cup-shaped; resembling a small cup or bowl.",
    "secondary": "In vertebrate osteology, designating cup-shaped anatomical depressions or sockets, particularly the acetabular cavity of the pelvic bone.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **cotyloid** notch at the inferior rim of the acetabulum transmits nutrient vessels to the femoral head ligament."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The hemispherical head of the femur fits neatly into the deep **cotyloid** socket of the innominate bone."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The fibrocartilaginous **cotyloid** ligament deepens the pelvic cup, securing joint articulation during locomotion."
      }
    ]
  },
  "Dashboard — cotyl\\cotyloidal.md": {
    "primary": "Pertaining to or shaped like a cotyloid cavity; cup-shaped.",
    "secondary": "In clinical orthopedics and morphology, of or relating to the acetabulum or its enclosing fibrocartilaginous rim.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Tuberculous coxitis often causes extensive erosion of the **cotyloidal** articular cartilage."
      },
      {
        "author": "Sir Frederick Treves",
        "work": "Surgical Applied Anatomy",
        "quote": "Dislocation of the hip requires manipulation to lever the femoral head back over the **cotyloidal** margin."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The transverse **cotyloidal** ligament bridges the gap across the lower notch of the pelvic socket."
      }
    ]
  },
  "Dashboard — cotyl\\dicotyledon.md": {
    "primary": "A flowering plant whose embryo typically bears two seed leaves or cotyledons.",
    "secondary": "In systematic botany, a traditional class of angiosperms (now understood to encompass basal angiosperms and eudicots) characterized by reticulate leaf venation, concentric vascular bundles, and floral parts in multiples of four or five.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The broad reticulated leaves of a **dicotyledon** contrast strikingly with the parallel-veined foliage of grasses."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Upon emerging from the seed coat, a **dicotyledon** displays two fleshy lobes that nourish the initial shoot."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The vast majority of deciduous forest trees across the globe belong structurally to the **dicotyledon** group."
      }
    ]
  },
  "Dashboard — cotyl\\dicotyledonous.md": {
    "primary": "Having two cotyledons or seed lobes in the embryo.",
    "secondary": "In botanical anatomy, describing plants exhibiting concentric woody rings with open vascular bundles and cambial secondary growth.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Aspects of Nature",
        "quote": "The great expanse of the temperate forest is dominated by stately **dicotyledonous** trees such as oak and chestnut."
      },
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "Every tender **dicotyledonous** seedling that poked its twin leaves through my bean-field soil was an invitation to work."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "A cross-section of a **dicotyledonous** stem reveals a distinct central pith surrounded by a cylinder of wood."
      }
    ]
  },
  "Dashboard — cotyl\\eudicotyledon.md": {
    "primary": "Any member of a major monophyletic clade of angiosperms whose pollen grains typically possess three apertures (tricolpate).",
    "secondary": "In modern phylogenetic angiosperm systematics (APG), the large monophyletic assemblage encompassing the vast majority of traditional dicotyledons, excluding primitive magnoliids and basal lines.",
    "quotes": [
      {
        "author": "Ernst Mayr",
        "work": "This Is Biology",
        "quote": "Cladistic analysis of pollen ultrastructure revealed that the true **eudicotyledon** lineage forms a strictly monophyletic group."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The recognition of the **eudicotyledon** clade revolutionized angiosperm taxonomy, separating tricolpate plants from ancient magnoliid grades."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Ancestor's Tale",
        "quote": "A familiar apple tree is a **eudicotyledon**, sharing tricolpate pollen with roses, buttercups, and sunflowers."
      }
    ]
  },
  "Dashboard — cotyl\\monocotyledon.md": {
    "primary": "A flowering plant whose embryo possesses a single cotyledon or seed leaf.",
    "secondary": "In systematic botany, an angiosperm lineage (including grasses, lilies, orchids, and palms) characterized by parallel leaf venation, scattered stem vascular bundles, and floral parts in multiples of three.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "In a germinating **monocotyledon** like oats, the solitary cotyledon forms a protective sheath known as the coleoptile."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The cereal grains upon which human civilization rests belong without exception to the great **monocotyledon** family of grasses."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions of America",
        "quote": "Giant palms rising above the tropical canopy demonstrate how a **monocotyledon** can achieve tree-like stature without secondary wood."
      }
    ]
  },
  "Dashboard — cotyl\\monocotyledonae.md": {
    "primary": "A major botanical taxon (class) comprising all monocotyledonous flowering plants.",
    "secondary": "In classical plant taxonomy, the group of angiosperms possessing a single seed lobe, scattered stele bundles, fibrous root systems, and trimerous flowers.",
    "quotes": [
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "Within the division Angiospermae, the class **Monocotyledonae** constitutes an extraordinarily uniform and natural evolutionary branch."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The **Monocotyledonae** include not only our humble pasture grasses but also the most magnificent and bizarre tropical orchids."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of Botany",
        "quote": "The embryo in **Monocotyledonae** remains undivided, sending up a single cylindrical green shoot upon germination."
      }
    ]
  },
  "Dashboard — cotyl\\monocotyledones.md": {
    "primary": "The plural taxonomic designation for monocotyledons in botanical classification.",
    "secondary": "In historical taxonomy (such as Jussieu's natural system), the primary division of angiosperm plants whose seeds contain only one cotyledon.",
    "quotes": [
      {
        "author": "Antoine Laurent de Jussieu",
        "work": "Genera Plantarum",
        "quote": "I established the primary division of **Monocotyledones** on the basis of embryo architecture and floral insertion."
      },
      {
        "author": "George Bentham",
        "work": "Genera Plantarum",
        "quote": "The **Monocotyledones** present an astonishing ecological range, from subaquatic duckweeds to massive columnar palms."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "In equatorial zones, the luxuriant growth of **Monocotyledones** gives tropical landscapes their distinctive majestic character."
      }
    ]
  },
  "Dashboard — cotyl\\monocotyledonous.md": {
    "primary": "Pertaining to, having, or resembling a single cotyledon in the seed.",
    "secondary": "In plant anatomy, characterizing plants that display parallel leaf veins, scattered vascular bundles, and adventitious fibrous roots.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Different Forms of Flowers on Plants of the Same Species",
        "quote": "Many **monocotyledonous** species, notably within the orchid family, have evolved the most intricate mechanisms for insect pollination."
      },
      {
        "author": "Henry David Thoreau",
        "work": "The Maine Woods",
        "quote": "Tall **monocotyledonous** rushes bordered the lake margin, shivering in the chilly north wind."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "A transverse cut through a **monocotyledonous** stalk shows vascular bundles distributed irregularly throughout the ground parenchyma."
      }
    ]
  },
  "Dashboard — cotyl\\tricotyledonous.md": {
    "primary": "Having or developing three cotyledons instead of the normal one or two.",
    "secondary": "In plant teratology and developmental genetics, describing seedling anomalies or gymnosperm embryos that produce three functional seed leaves.",
    "quotes": [
      {
        "author": "Hugo de Vries",
        "work": "The Mutation Theory",
        "quote": "Among several thousand germinating evening primroses, I discovered occasional **tricotyledonous** seedlings that bred true in successive generations."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants Under Domestication",
        "quote": "Horticultural records show that **tricotyledonous** variations appear intermittently in radishes, beans, and sycamores."
      },
      {
        "author": "Asa Gray",
        "work": "Botanical Text-Book",
        "quote": "Conifers frequently exhibit polycotyledony, but a strictly **tricotyledonous** angiosperm embryo is regarded as an abnormal deviation."
      }
    ]
  },
  "Dashboard — crepid\\crepid.md": {
    "primary": "A combining form derived from Greek krepis, meaning a boot, slipper, shoe, or architectural foundation.",
    "secondary": "In architectural terminology and classical archeology, a root denoting a raised stepped stone base or platform.",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "The Greek root **crepid** evokes the solid footstall or foundational shoe upon which the temple column firmly rests."
      },
      {
        "author": "Vitruvius",
        "work": "The Ten Books on Architecture",
        "quote": "Every temple requires a stepped base or **crepid** structure to elevate the sacred cella above the surrounding dust."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "In Hellenic design, the **crepid** platform unifies the peristyle with the rocky topography of the acropolis."
      }
    ]
  },
  "Dashboard — crepid\\crepidoma.md": {
    "primary": "The stepped architectural platform or stone base upon which the superstructure of a classical Greek temple stands.",
    "secondary": "In classical architecture, the substructure typically consisting of three stepped courses (the lower two forming the stereobate and the topmost being the stylobate).",
    "quotes": [
      {
        "author": "John Ruskin",
        "work": "The Seven Lamps of Architecture",
        "quote": "The massive marble blocks of the **crepidoma** lift the temple above ordinary soil, lending it an air of celestial detachment."
      },
      {
        "author": "William Morris",
        "work": "Hopes and Fears for Art",
        "quote": "Standing upon the ancient **crepidoma** of the Parthenon, one feels the serene rhythm of Hellenic geometry beneath one's feet."
      },
      {
        "author": "James Fergusson",
        "work": "A History of Architecture in All Countries",
        "quote": "To correct optical illusion, the horizontal lines of the **crepidoma** were subtly curved upward toward the center."
      }
    ]
  },
  "Dashboard — cross\\Crossopterygii.md": {
    "primary": "A taxonomic subclass or clade of lobe-finned bony fishes possessing paired, fleshy, lobed fins fringed with rays.",
    "secondary": "In vertebrate paleontology and evolutionary biology, sarcopterygian fishes (including coelacanths and rhipidistians) whose internal fin skeletal elements directly gave rise to tetrapod limbs.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Preliminary Essay on the Systematic Arrangement of the Fishes of the Devonian Epoch",
        "quote": "I established the order **Crossopterygii** to include those fishes having their paired fins fringed with rays around a central fleshy lobe."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The rhipidistian branch of **Crossopterygii** bridges the evolutionary transition from aquatic vertebrates to primitive land amphibians."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "Paleontologists recognized that the limb bones of our early terrestrial ancestors were already mapped out in the fins of Devonian **Crossopterygii**."
      }
    ]
  },
  "Dashboard — cross\\across.md": {
    "primary": "From one side to the other of a space, area, or boundary; in a crossing direction.",
    "secondary": "Extending from side to side; so as to intersect or form a cross with.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "A field of water betrays the spirit that is in the air, and ripples **across** the pond beneath the summer breeze."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "A shadow flitted **across** the captain's furrowed brow as he gazed silently toward the horizon."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "A beam of light swept **across** the darkened water, touching the bedroom window with cyclical brilliance."
      }
    ]
  },
  "Dashboard — cross\\cross.md": {
    "primary": "An upright post with a transverse beam, used in antiquity for execution, or an emblem thereof representing Christianity.",
    "secondary": "An intersection of two lines or paths; a hybrid organism produced by mating different varieties or species; or to traverse a boundary.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Upon the **cross** he hung, and by his death / Redeemed mankind from ancient misery."
      },
      {
        "author": "Charles Darwin",
        "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
        "quote": "A systematic **cross** between distinct individuals of the same species almost invariably imparts increased vigor and fertility to the offspring."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "The Rime of the Ancient Mariner",
        "quote": "Instead of the **cross**, the Albatross / About my neck was hung."
      }
    ]
  },
  "Dashboard — cross\\crosscheck.md": {
    "primary": "To verify or confirm figures, facts, or results by utilizing an alternative independent method, source, or record.",
    "secondary": "In computational validation and ice hockey, an independent corroboration of data points; in sports, an illegal check delivered using the shaft of the stick with both hands.",
    "quotes": [
      {
        "author": "Alan Turing",
        "work": "Computing Machinery and Intelligence",
        "quote": "The operator must **crosscheck** every logical deduction against intermediate mechanical tabulations."
      },
      {
        "author": "Carl Sagan",
        "work": "The Demon-Haunted World",
        "quote": "Skeptical inquiry demands that we **crosscheck** extraordinary claims against reproducible physical evidence."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Sign of the Four",
        "quote": "Holmes paused to **crosscheck** the footprints against the known gait of the fugitive before advancing."
      }
    ]
  },
  "Dashboard — cross\\crosscurrent.md": {
    "primary": "A water or air current that flows across the main flow of direction.",
    "secondary": "Figuratively, a conflicting tendency, opinion, or cultural influence running counter to the prevailing trend.",
    "quotes": [
      {
        "author": "Joseph Conrad",
        "work": "Typhoon",
        "quote": "A sudden violent **crosscurrent** caught the steamer's stern, throwing her off course into the churning trough."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "A strong mind steers steadily onward, ignoring the transient **crosscurrent** of public censure."
      },
      {
        "author": "Winston Churchill",
        "work": "The World Crisis",
        "quote": "Naval maneuvers in the North Sea were complicated by an unpredictable tidal **crosscurrent**."
      }
    ]
  },
  "Dashboard — cross\\crosscut.md": {
    "primary": "Made or directed across the grain or main flow; cut transversely.",
    "secondary": "A transverse cut, path, or saw designed to cut timber across the wood grain; figuratively, a shortcut across terrain.",
    "quotes": [
      {
        "author": "Henry David Thoreau",
        "work": "Walden",
        "quote": "With a keen **crosscut** saw, the woodman sliced the fallen pine trunk into even hearth logs."
      },
      {
        "author": "Thomas Hardy",
        "work": "The Woodlanders",
        "quote": "The rhythmic rasp of the **crosscut** echoed through the misty hazel coppice from sunrise to dusk."
      },
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The harpooneer made a swift **crosscut** through the tangle of hemp line to free the capsizing whaleboat."
      }
    ]
  }
};

const updated = updateNotesBatch(CLUSTER_DIR, batchData);
console.log(`[Batch 2] Successfully updated ${updated} of ${Object.keys(batchData).length} notes.`);
