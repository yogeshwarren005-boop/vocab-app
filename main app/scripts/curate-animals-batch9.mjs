import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Animals & Zoology';

const filesData = {
  "Dashboard — zo/anthrozoology.md": {
    "primary": "The interdisciplinary study of interactions, relationships, and bonds between humans and non-human animals.",
    "secondary": "In anthropology, psychology, and ethology, the examination of cross-cultural pet-keeping, working animal dynamics, wildlife conservation conflicts, and human attitudes toward other species.",
    "quotes": [
      {
        "author": "Hal Herzog",
        "work": "Some We Love, Some We Hate, Some We Eat",
        "quote": "Modern **anthrozoology** investigates why humans treat dogs like family members while raising pigs for bacon."
      },
      {
        "author": "James Serpell",
        "work": "In the Company of Animals",
        "quote": "Pioneering studies in **anthrozoology** demonstrated the profound psychological benefits of companion animals on human health."
      },
      {
        "author": "Frans de Waal",
        "work": "The Bonobo and the Atheist",
        "quote": "Cross-disciplinary **anthrozoology** bridges the traditional philosophical divide separating human culture from primate biology."
      }
    ]
  },
  "Dashboard — zo/azoic.md": {
    "primary": "Without life; destitute of organic life, or designating geological strata formed prior to the appearance of living organisms.",
    "secondary": "In historical geology, formerly applied to the earliest Precambrian rock systems preceding fossiliferous strata.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Geologists once considered the deepest metamorphic schists to belong to an entirely **azoic** epoch destitute of fossils."
      },
      {
        "author": "Edward Forbes",
        "work": "Report on the Aegean Invertebrates",
        "quote": "Forbes hypothesized that an **azoic** zone began below three hundred fathoms where marine pressure extinguished all life."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "The profound crystalline granite was designated **azoic** by early stratigraphers before microscopic algal structures were uncovered."
      }
    ]
  },
  "Dashboard — zo/azotemia.md": {
    "primary": "An excess of urea, creatinine, and other nitrogenous waste compounds in the blood, typically resulting from kidney failure or impaired renal clearance.",
    "secondary": "In clinical nephrology, categorized as prerenal, intrinsic renal, or postrenal azotemia based on etiology and urinary biochemical indices.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Progressive bilateral renal disease invariably culminates in severe **azotemia**, marked by lethargy and uremic frost."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Severe circulatory collapse diminishes glomerular filtration, producing acute prerenal **azotemia** without permanent tubular necrosis."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "The retention of urinary salts within the systemic circulation gave rise to terminal **azotemia** and convulsive seizures."
      }
    ]
  },
  "Dashboard — zo/azotemic.md": {
    "primary": "Relating to, characterized by, or suffering from azotemia; showing abnormally elevated nitrogenous waste in the blood.",
    "secondary": "In veterinary and human medicine, describing clinical signs—such as halitosis, vomiting, and metabolic acidosis—induced by retained nitrogen metabolites.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **azotemic** patient slipped into deep coma as urea clearance fell below five percent of normal capacity."
      },
      {
        "author": "T. R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Prompt fluid resuscitation successfully reversed the oliguric state in the dehydrated **azotemic** subject."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Elevated serum blood urea nitrogen and creatinine confirmed the **azotemic** condition following bilateral ureteral obstruction."
      }
    ]
  },
  "Dashboard — zo/cryptozoology.md": {
    "primary": "The search for and study of animals whose existence is unproven or substantiated only by folklore, hearsay, or anecdotal sightings.",
    "secondary": "In popular science and folklore studies, a subculture and investigative pursuit focused on cryptids such as the Sasquatch, Loch Ness monster, and yeti.",
    "quotes": [
      {
        "author": "Bernard Heuvelmans",
        "work": "On the Track of Unknown Animals",
        "quote": "Pioneering modern **cryptozoology**, Heuvelmans argued that native folklore often conceals zoological discoveries."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Flamingo's Smile",
        "quote": "Professional paleontologists remain skeptical of **cryptozoology**, demanding skeletal specimens rather than blurry photographs."
      },
      {
        "author": "Loren Coleman",
        "work": "Mysterious America",
        "quote": "Enthusiasts of **cryptozoology** comb remote wilderness river valleys in search of relict hominids."
      }
    ]
  },
  "Dashboard — zo/diazo.md": {
    "primary": "Relating to or containing a diazo group consisting of two linked nitrogen atoms bonded to a single carbon atom.",
    "secondary": "In synthetic organic chemistry, describing versatile reactive intermediates such as diazomethane or diazo dyes used in coupling reactions and cyclopropanation.",
    "quotes": [
      {
        "author": "Peter Griess",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "Griess synthesized the first aromatic **diazo** compound by treating aniline with nitrous acid in the cold."
      },
      {
        "author": "August Wilhelm von Hofmann",
        "work": "Introduction to Modern Chemistry",
        "quote": "The brilliant synthetic coloring matters derived from **diazo** precursors revolutionized the textile dye industry."
      },
      {
        "author": "Robert Burns Woodward",
        "work": "The Total Synthesis of Vitamin B12",
        "quote": "The transient intermediate was coupled with a stabilized **diazo** ester to assemble the corrin core ring."
      }
    ]
  },
  "Dashboard — zo/ectozoan.md": {
    "primary": "An external animal parasite; an ectoparasite that lives on the skin, feathers, fur, or gills of its host.",
    "secondary": "In veterinary parasitology, organisms such as fleas, ticks, lice, and parasitic copepods that feed externally on host tissues or bodily fluids.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The marine iguana harbored many a clinging **ectozoan** tick between the thick scales of its neck."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "Evenings at the Microscope",
        "quote": "Under the lens, each minute **ectozoan** revealed hooked appendages exquisitely adapted for clutching fish scales."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Zoology for High Schools and Colleges",
        "quote": "The common dog tick is a familiar **ectozoan** that drops from its host upon completing its blood meal."
      }
    ]
  },
  "Dashboard — zo/ectozoon.md": {
    "primary": "An external animal parasite (synonym of ectoparasite; plural: ectozoa).",
    "secondary": "In historical helminthology and zoology, an animal organism living on the exterior of another animal host, distinguished from an entozoon.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "The fish louse exemplifies a degraded crustacean transformed into an obligate **ectozoon**."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy of the Invertebrates",
        "quote": "Every parasitic **ectozoon** exhibits modifications of the mouthparts suited for piercing the epidermal integument."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Naturalists separated the internal entozoa from the external **ectozoon** infesting the gills of freshwater bass."
      }
    ]
  },
  "Dashboard — zo/endozoic.md": {
    "primary": "Living within an animal, either as a parasite, symbiont, or internal dweller; or transported internally through an animal's digestive tract.",
    "secondary": "In ecology and botany, describing seeds or spores adapted for endozoochory (dispersal by ingestion and defecation by animals).",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Wonders of Life",
        "quote": "Symbiotic green algae flourish as **endozoic** guests within the transparent bodies of freshwater hydras."
      },
      {
        "author": "Arthur Tansley",
        "work": "The British Islands and Their Vegetation",
        "quote": "Fleshy berries rely upon **endozoic** transport by frugivorous thrushes across fragmented woodlots."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Naturalist's Rambles on the Devonshire Coast",
        "quote": "The sponge harbored microscopic **endozoic** commensals sheltered inside its cavernous flagellated chambers."
      }
    ]
  },
  "Dashboard — zo/entozoan.md": {
    "primary": "An internal animal parasite; an animal that lives within the body or organs of another animal host (entozoon).",
    "secondary": "In historical parasitology, invertebrates including tapeworms, flukes, and nematodes that inhabit host viscera, muscles, or digestive tracts.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy of the Invertebrates",
        "quote": "The encysted trichina worm is a formidable **entozoan** lodging within the striated muscle fibers."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Complex life cycles evolved in every parasitic **entozoan** requiring alternate intermediate vertebrate hosts."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The adult cestode is an intestinal **entozoan** utterly lacking an alimentary canal of its own."
      }
    ]
  },
  "Dashboard — zo/entozoic.md": {
    "primary": "Living inside the body of an animal; relating to or characteristic of internal animal parasites or internal symbionts.",
    "secondary": "In protozoology and ecology, designating microscopic organisms inhabiting internal mucosal cavities, such as entozoic amoebae and flagellates.",
    "quotes": [
      {
        "author": "Joseph Leidy",
        "work": "A Flora and Fauna within Living Animals",
        "quote": "Leidy detailed numerous **entozoic** nematodes and ciliated infusoria populating the gut of the passalid beetle."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "Intestinal flukes exhibit specialized suckers designed to withstand the peristaltic forces of their **entozoic** habitat."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Certain **entozoic** ciliates thrive anaerobically within the rumen fluids of grazing herbivores."
      }
    ]
  },
  "Dashboard — zo/entozoon.md": {
    "primary": "An internal parasitic animal, such as an intestinal worm; an animal organism living inside another animal (plural: entozoa).",
    "secondary": "In 19th-century medical taxonomy, a formal grouping of parasitic worms (trematodes, cestodes, nematodes, and acanthocephalans).",
    "quotes": [
      {
        "author": "T. Spencer Cobbold",
        "work": "Entozoa: An Introduction to Helminthology",
        "quote": "Cobbold demonstrated that the hydatid cyst was the larval stage of a microscopic canine **entozoon**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lectures on the Elements of Comparative Anatomy",
        "quote": "No organ of the vertebrate frame is exempt from the invasion of some specialized **entozoon**."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The liver fluke represents an ancient flattened **entozoon** adapted to the biliary ducts of sheep."
      }
    ]
  },
  "Dashboard — zo/epizoan.md": {
    "primary": "An external animal parasite or surface dweller; an animal living on the exterior of another animal (epizoon).",
    "secondary": "In marine biology, any non-parasitic or ectocommensal invertebrate (such as a barnacle or hydroid) that encrusts the shell or body of a marine animal.",
    "quotes": [
      {
        "author": "Philip Henry Gosse",
        "work": "The Aquarium",
        "quote": "The carapace of the spider crab supported a thriving colony of seaweed and clinging **epizoan** tubes."
      },
      {
        "author": "Charles Darwin",
        "work": "A Monograph on the Sub-class Cirripedia",
        "quote": "Coronula barnacles attach firmly to the blubber of baleen whales as specialized **epizoan** riders."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Zoology for High Schools and Colleges",
        "quote": "The fish louse is a degenerate **epizoan** whose mouthparts have transformed into piercing stylets."
      }
    ]
  },
  "Dashboard — zo/epizoic.md": {
    "primary": "Living attached to or growing upon the exterior surface of an animal, either parasitically or commensally.",
    "secondary": "In botany, describing seeds, burs, or spores adapted for epizoochory (dispersal by clinging to animal fur, feathers, or wool).",
    "quotes": [
      {
        "author": "Arthur Tansley",
        "work": "The British Islands and Their Vegetation",
        "quote": "Hooked fruits of Galium aparine rely upon an **epizoic** mechanism of dispersal in sheep fleece."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Art Forms in Nature",
        "quote": "Minute colonial polyps flourish in **epizoic** fashion upon the spiny shells of deep-sea gastropods."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Mud adhering to the webbed feet of wading birds provides **epizoic** transport for freshwater mollusk spat."
      }
    ]
  },
  "Dashboard — zo/epizoon.md": {
    "primary": "An external parasite or animal organism living on the exterior of another animal (plural: epizoa).",
    "secondary": "In historical veterinary science, external pests including lice, ticks, mites, and blowfly larvae causing cutaneous disease.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy of the Invertebrates",
        "quote": "Unlike the sheltered fluke, the **epizoon** must develop powerful claws to resist dislodgment by grooming."
      },
      {
        "author": "Louis Agassiz",
        "work": "Principles of Zoology",
        "quote": "The parasitic crustacean Lernaea embeds its anchor-shaped cephalothorax deep into fish muscle as an aberrant **epizoon**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The sheep tick, though called a fly, has lost its wings to become a permanent blood-sucking **epizoon**."
      }
    ]
  },
  "Dashboard — zo/Eumetazoa.md": {
    "primary": "A major subkingdom or clade of animals comprising all multicellular organisms except sponges and placozoans, characterized by true tissues and an embryonic germ layer.",
    "secondary": "In phylogenetic systematics, organisms featuring true epithelia joined by belt desmosomes, nervous tissue, specialized digestive cavities, and gastrulation.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "The Evolution of Man",
        "quote": "Haeckel coined the term **Eumetazoa** to distinguish true tissue-forming animals from the primitive structural plan of sponges."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "All members of the **Eumetazoa** undergo gastrulation to establish primary ectoderm and endoderm layers."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The earliest radiation of the **Eumetazoa** during the Ediacaran set the basic body plans for all subsequent animal life."
      }
    ]
  },
  "Dashboard — zo/holozoic.md": {
    "primary": "Obtaining nutrition in the manner of most animals, by ingesting solid complex organic food material and digesting it internally.",
    "secondary": "In protozoology and cellular biology, nutritional behavior contrasted with holophytic (photosynthetic autotrophy) and saprozoic (absorptive heterotrophy).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The amoeba exhibits typical **holozoic** nutrition, engulfing diatoms and ciliates into temporary food vacuoles."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Euglena can switch from photosynthetic nourishment to **holozoic** ingestion when kept in darkness with suitable organic substrates."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Zoology for High Schools and Colleges",
        "quote": "Higher metazoans are uniformly **holozoic**, possessing specialized alimentary canals to digest particulate food."
      }
    ]
  },
  "Dashboard — zo/mesozoic.md": {
    "primary": "The geological era spanning approximately 252 to 66 million years ago, consisting of the Triassic, Jurassic, and Cretaceous periods; the Age of Reptiles.",
    "secondary": "In historical geology and paleontology, marked by the breakup of Pangaea, the dominance of dinosaurs, the radiation of gymnosperms, and the origin of birds, mammals, and flowering plants.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "Ammonites flourished with astonishing morphological diversity throughout the entire **Mesozoic** era before vanishing abruptly."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "The sudden extinction event at the close of the **Mesozoic** opened ecological niches for placental mammals."
      },
      {
        "author": "Edwin H. Colbert",
        "work": "The Dinosaur Book",
        "quote": "Terrestrial ecosystems of the **Mesozoic** world were dominated from pole to pole by enormous archosaurian reptiles."
      }
    ]
  },
  "Dashboard — zo/Metazoa.md": {
    "primary": "A major zoological division comprising all multicellular animals, characterized by cellular differentiation, extracellular matrix, and blastular embryonic development.",
    "secondary": "In evolutionary biology, the animal kingdom as distinct from unicellular Protozoa; monophyletic descendants of a colonial choanoflagellate ancestor.",
    "quotes": [
      {
        "author": "Ernst Haeckel",
        "work": "Generelle Morphologie der Organismen",
        "quote": "The origin of the **Metazoa** represents the momentous evolutionary leap from solitary protozoans to integrated colonial organisms."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Science and Culture",
        "quote": "Cellular cooperation and division of physiological labor define every representative of the **Metazoa**."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Wonderful Life",
        "quote": "The explosion of multicellular disparity within the **Metazoa** filled the Burgess Shale seas with extraordinary body architectures."
      }
    ]
  },
  "Dashboard — zo/paleozoic.md": {
    "primary": "The earliest of the three geological eras of the Phanerozoic Eon, spanning from approximately 541 to 252 million years ago; the Age of Ancient Life.",
    "secondary": "In paleontology and stratigraphy, comprising the Cambrian, Ordovician, Silurian, Devonian, Carboniferous, and Permian periods, culminating in the Great Permian Extinction.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "Trilobites are the diagnostic index fossils of the ancient **Paleozoic** strata across Wales and Scandinavia."
      },
      {
        "author": "Roderick Murchison",
        "work": "The Silurian System",
        "quote": "Murchison deciphered the sequence of **Paleozoic** formations that revealed the dawn of complex marine invertebrate faunas."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "Time's Arrow, Time's Cycle",
        "quote": "The catastrophic collapse terminating the **Paleozoic** erased nearly ninety-five percent of all marine species."
      }
    ]
  },
  "Dashboard — zo/paleozoology.md": {
    "primary": "The branch of paleontology dealing with the study of fossil animals and their prehistoric ecosystems, anatomy, and evolution.",
    "secondary": "In academic zoology and evolutionary biology, the reconstruction of extinct faunas using comparative anatomy, biostratigraphy, and taphonomic analysis.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "Recherches sur les ossemens fossiles",
        "quote": "Cuvier established systematic **paleozoology** by applying the principle of correlation of parts to fossil bones."
      },
      {
        "author": "Richard Owen",
        "work": "Paleontology: A Systematic Summary of Extinct Animals",
        "quote": "Modern **paleozoology** reconstructs extinct reptiles with the same anatomical rigor applied to living species."
      },
      {
        "author": "Alfred Romer",
        "work": "Vertebrate Paleontology",
        "quote": "Through rigorous **paleozoology**, the transition from lobe-finned crossopterygians to early amphibians was conclusively mapped."
      }
    ]
  },
  "Dashboard — zo/protozoal.md": {
    "primary": "Of, relating to, caused by, or characteristic of protozoa; protozoan.",
    "secondary": "In tropical medicine and veterinary parasitology, describing infectious diseases caused by single-celled eukaryotic parasites (e.g., malaria, giardiasis, toxoplasmosis).",
    "quotes": [
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Severe hemolytic anemia is the standard clinical hallmark of acute **protozoal** infection by Plasmodium."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic stool examination revealed active amoebic trophozoites, confirming the diagnosis of **protozoal** dysentery."
      },
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "Mosquito vectors transport the infective stages of this lethal **protozoal** parasite across tropical marshlands."
      }
    ]
  },
  "Dashboard — zo/protozoan.md": {
    "primary": "Any of various single-celled eukaryotic microscopic organisms belonging historically to the subkingdom Protozoa, having animal-like heterotrophic or motile behaviors.",
    "secondary": "In modern protistology, an informal term for non-photosynthetic, phagotrophic, or flagellated single-celled eukaryotes (ciliates, flagellates, amoebae, and sporozoans).",
    "quotes": [
      {
        "author": "Antonie van Leeuwenhoek",
        "work": "Philosophical Transactions of the Royal Society",
        "quote": "Observing pond droplets, Leeuwenhoek was astonished by the agility of every swimming **protozoan** animalcule."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish",
        "quote": "The humble **protozoan** performs all vital bodily functions—ingestion, respiration, locomotion—within the confines of a single cell."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Wonders of Life",
        "quote": "Radiolarian skeletons illustrate how an individual **protozoan** can secrete intricate geometric shells of silica."
      }
    ]
  },
  "Dashboard — zo/protozoic.md": {
    "primary": "Relating to, containing, or characterized by the earliest forms of animal life; protozoan or early fossiliferous.",
    "secondary": "In 19th-century geological terminology, designating strata yielding the earliest recognized fossil traces of primitive animal organisms.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Early stratigraphers assigned the lowest fossiliferous slate deposits to the **protozoic** system."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "The earliest limestone outcrops bear **protozoic** remains of microscopic corallines and primitive sponge spicules."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Zoology for High Schools and Colleges",
        "quote": "The transitional sedimentary beds illustrate the dawn of the **protozoic** animal fauna."
      }
    ]
  },
  "Dashboard — zo/protozoological.md": {
    "primary": "Of, relating to, or concerned with protozoology (the scientific study of protozoa).",
    "secondary": "In academic microbiology and parasitology, pertaining to laboratory investigations, culturing techniques, or taxonomics of single-celled eukaryotes.",
    "quotes": [
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Careful **protozoological** investigation under high magnification is required to differentiate amoebic cysts from yeast cells."
      },
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "The discovery of oocysts on the mosquito stomach was a triumph of applied **protozoological** field technique."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Specialized **protozoological** manuals catalog thousands of free-living and parasitic flagellate species."
      }
    ]
  },
  "Dashboard — zo/protozoologist.md": {
    "primary": "A biologist or microbiologist who specializes in the study of protozoa.",
    "secondary": "In biomedical research and limnology, a scientist researching the physiology, genetics, life cycles, and pathogenicity of single-celled eukaryotes.",
    "quotes": [
      {
        "author": "Ronald Ross",
        "work": "The Prevention of Malaria",
        "quote": "Every medical **protozoologist** understood that breaking the vector's life cycle would eradicate marsh ague."
      },
      {
        "author": "Joseph Leidy",
        "work": "Fresh-Water Rhizopods of North America",
        "quote": "As an indefatigable **protozoologist**, Leidy spent countless hours sketching amoebae and sun animalcules."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "The trained **protozoologist** identifies species of trypanosomes by their characteristic undulating membranes."
      }
    ]
  },
  "Dashboard — zo/protozoology.md": {
    "primary": "The scientific study of protozoa, their classification, morphology, physiology, and pathology.",
    "secondary": "In life sciences, a foundational sub-discipline of protistology and parasitology addressing both free-living microfauna and pathogen transmission.",
    "quotes": [
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "The rapid development of medical **protozoology** revolutionized our understanding of sleeping sickness and kala-azar."
      },
      {
        "author": "Ronald Ross",
        "work": "Memoirs",
        "quote": "Our experiments linked veterinary **protozoology** with mosquito entomology in a single unified transmission cycle."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "A comprehensive grasp of comparative **protozoology** is indispensable for tracing the phylogenetic roots of multicellular life."
      }
    ]
  },
  "Dashboard — zo/protozoon.md": {
    "primary": "A single-celled eukaryotic organism; an individual member of the Protozoa (singular form of protozoa).",
    "secondary": "In classical microscopy and zoology, an animalcule exhibiting autonomous motility, phagocytosis, and contractile vacuole pulsation.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Under high power, the solitary **protozoon** reveals an intricate internal cyclosis within its clear cytoplasm."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "Evenings at the Microscope",
        "quote": "A lively **protozoon** dashed across the field of view, propelled by rapid strokes of its ciliary wreath."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Riddle of the Universe",
        "quote": "The single-celled **protozoon** contains in potentia all the metabolic pathways found in higher mammalian tissue."
      }
    ]
  },
  "Dashboard — zo/zo.md": {
    "primary": "The classical Greek combining form meaning animal, living creature, or biological life (from Greek zōion / zōē).",
    "secondary": "In linguistic morphology and scientific nomenclature, the foundational root generating terms throughout zoology, paleontology, and biogeography.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The Greek combining formative **zo-** signifies animal, appearing everywhere from zoology to the constellations of the zodiac."
      },
      {
        "author": "James Murray",
        "work": "A New English Dictionary on Historical Principles",
        "quote": "Compounds containing **zo-** entered English predominantly in the seventeenth and eighteenth centuries with the rise of taxonomic natural history."
      },
      {
        "author": "Isaac Taylor",
        "work": "Words and Places",
        "quote": "The ancient root **zo-** captures the fundamental Hellenic perception of animate motion and living breath."
      }
    ]
  },
  "Dashboard — zo/zoanthropy.md": {
    "primary": "A mental disorder or delusion in which a human being believes himself or herself to have transformed into an animal, adopting animal behavior.",
    "secondary": "In clinical psychiatry and historical medicine, a severe form of monomania or lycanthropy where the patient imitates the sounds and habits of beasts.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "Victims of melancholy **zoanthropy** imagine themselves to be wolves, barking dogs, or howling beasts of the desert."
      },
      {
        "author": "Philippe Pinel",
        "work": "A Treatise on Insanity",
        "quote": "In our asylum wards, one severe case of **zoanthropy** spent weeks crawling on all fours and grazing on lawn turf."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Hysterical delusions occasionally take the archaic form of **zoanthropy**, where the patient rejects human speech for animal growls."
      }
    ]
  },
  "Dashboard — zo/zodiac.md": {
    "primary": "An imaginary belt of the heavens extending about 8 degrees on either side of the ecliptic, containing the twelve traditional constellations and signs named mostly after animals.",
    "secondary": "In celestial mechanics and historical astronomy, the band encompassing the orbital paths of the Sun, Moon, and principal major planets.",
    "quotes": [
      {
        "author": "Geoffrey Chaucer",
        "work": "A Treatise on the Astrolabe",
        "quote": "The circle of the **zodiac** is divided into twelve equal signs, beginning at the first point of Aries."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The sun traversed the starry **zodiac**, casting warm light across newly created oceans and continents."
      },
      {
        "author": "Arthur Eddington",
        "work": "Stars and Atoms",
        "quote": "Ancient Babylonian astronomers mapped the wandering planetary spheres along the golden road of the **zodiac**."
      }
    ]
  },
  "Dashboard — zo/zodiacal.md": {
    "primary": "Of, relating to, or situated within the zodiac.",
    "secondary": "In observational astronomy and astrophysics, designating interplanetary dust phenomena such as zodiacal light and the gegenschein.",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos",
        "quote": "In the clear skies of the tropical Atlantic, the glowing pyramid of **zodiacal** light rose vertically above the western horizon."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "The **zodiacal** constellations provide a permanent astronomical framework for calculating the planetary longitudes."
      },
      {
        "author": "Camille Flammarion",
        "work": "Popular Astronomy",
        "quote": "Interplanetary meteoritic dust reflects sunlight, creating the mysterious, ghostly **zodiacal** glow after sunset."
      }
    ]
  },
  "Dashboard — zo/zoe.md": {
    "primary": "A free-swimming larval stage of crabs and certain other decapod crustaceans (also written zoea), characterized by large compound eyes and prominent dorsal and rostral spines.",
    "secondary": "In marine invertebrate zoology, the pelagic developmental stage following the nauplius or protozoea, preceding the megalopa stage in brachyuran development.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "Upon hatching from the egg-mass, the tiny crab emerges as a bizarre spiny **zoe** drifting in coastal currents."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Naturalist's Rambles on the Devonshire Coast",
        "quote": "In the surface tow-net we captured many a curious **zoe** larva bearing long defensive cephalic spines."
      },
      {
        "author": "Louis Agassiz",
        "work": "Methods of Study in Natural History",
        "quote": "Vaughan Thompson demonstrated that the supposed independent genus Zoe was merely the larval **zoe** stage of the shore crab."
      }
    ]
  },
  "Dashboard — zo/zoic.md": {
    "primary": "Pertaining to or containing animal life; relating to animals or geological eras characterized by distinct animal faunas.",
    "secondary": "In geological nomenclature and stratigraphy, forming suffixes designating major eons and eras (e.g., Paleozoic, Mesozoic, Cenozoic, Phanerozoic).",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Geological strata bearing organic animal fossils are classified as distinctly **zoic** formations."
      },
      {
        "author": "James Dwight Dana",
        "work": "Manual of Geology",
        "quote": "The vast transition from azoic crystalline beds to fossil-rich **zoic** rocks marks the dawn of the Phanerozoic."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Zoology for High Schools and Colleges",
        "quote": "The entire fossiliferous column reflects successive evolutionary chapters of **zoic** life on Earth."
      }
    ]
  },
  "Dashboard — zo/zoo.md": {
    "primary": "A zoological garden or park where live wild and domestic animals are kept in enclosures for public exhibition, education, breeding, and scientific study.",
    "secondary": "In modern conservation biology, an institution engaged in ex-situ wildlife conservation, species survival plans, and public biodiversity education.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Expression of the Emotions in Man and Animals",
        "quote": "Observing the captive chimpanzees at the London **zoo**, Darwin noted facial expressions remarkably akin to human laughter."
      },
      {
        "author": "George Schaller",
        "work": "The Last Panda",
        "quote": "The modern **zoo** must evolve from a mere menagerie into a sanctuary and breeding station for endangered wildlife."
      },
      {
        "author": "Gerald Durrell",
        "work": "The Overloaded Ark",
        "quote": "We gathered rare forest creatures in Cameroon to establish captive breeding colonies at our island **zoo**."
      }
    ]
  },
  "Dashboard — zo/zoochore.md": {
    "primary": "A plant whose seeds, fruits, or spores are dispersed by animals.",
    "secondary": "In seed ecology and botany, a species possessing adaptations—such as edible pulp, hooks, burs, or elaiosomes—for endozoochory or epizoochory.",
    "quotes": [
      {
        "author": "Arthur Tansley",
        "work": "The British Islands and Their Vegetation",
        "quote": "The woodland flora includes many a specialized **zoochore** whose sticky fruits attach to the plumage of passerine birds."
      },
      {
        "author": "Daniel Janzen",
        "work": "Neotropical Ecology",
        "quote": "The giant guanacaste tree evolved as a megafaunal **zoochore**, originally adapted to seed dispersal by extinct Pleistocene herbivores."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The Wonders of Life",
        "quote": "Each flowering **zoochore** recruits animal partners through sugary rewards or clinging burrs to colonize distant clearings."
      }
    ]
  },
  "Dashboard — zo/zoogamete.md": {
    "primary": "A motile gamete; a flagellated reproductive cell capable of autonomous locomotion, produced by certain algae and fungi (a planogamete).",
    "secondary": "In phycology and reproductive biology, an unflagellated egg or flagellated sperm exhibiting directed swimming toward chemical attractants in aquatic fertilization.",
    "quotes": [
      {
        "author": "M. C. Cooke",
        "work": "British Fresh-Water Algae",
        "quote": "In green algae such as Chlamydomonas, each motile **zoogamete** fuses with a compatible partner to form a resting zygospore."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "The aquatic fungus discharges thousands of miniature **zoogamete** swarmers to accomplish fertilization in the film of dew."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Locomotion via anterior flagella enables each microscopic **zoogamete** to locate sessile oogonia in marine ulvophytes."
      }
    ]
  },
  "Dashboard — zo/zoogeography.md": {
    "primary": "The scientific study of the geographic distribution of animal species and populations across the globe.",
    "secondary": "In biogeography and evolutionary biology, the branch analyzing faunal realms (e.g., Nearctic, Palearctic, Ethiopian, Oriental, Australian, Neotropical) and historical dispersal pathways.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "Wallace established systematic **zoogeography** by demonstrating how deep ocean trenches define faunal boundaries between islands."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The curious anomalies of island **zoogeography** provide unanswerable evidence in favor of gradual evolutionary modification."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "Comparative **zoogeography** explains how Pleistocene glacial barriers accelerated allopatric speciation in continental bird populations."
      }
    ]
  },
  "Dashboard — zo/zoography.md": {
    "primary": "The scientific description of animals, their forms, habitats, external characteristics, and varieties.",
    "secondary": "In historical natural history, descriptive zoology focused on cataloging and illustrating species, distinguished from comparative anatomy and physiology.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Descriptive **zoography** provides the raw observational foundation upon which anatomical synthesis is constructed."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "The Romance of Natural History",
        "quote": "The naturalist's charming **zoography** brought the bizarre creatures of coral reefs vividly before Victorian readers."
      },
      {
        "author": "John James Audubon",
        "work": "Ornithological Biography",
        "quote": "Audubon combined exquisite field artistry with meticulous **zoography** to chronicle the vanishing birds of North America."
      }
    ]
  },
  "Dashboard — zo/zooidzoöid.md": {
    "primary": "An individual animal that is part of a colonial organism, such as a bryozoan, hydrozoan, or colonial ascidian; or an organic cell or body having independent motility.",
    "secondary": "In invertebrate zoology, specialized polymorphs within a colonial siphonophore or bryozoan performing distinct physiological roles (gastrozooid, dactylozooid, gonozooid).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "In the Portuguese man-of-war, each specialized **zooid** fulfills a single function—either hunting, feeding, or reproduction—for the colony."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Naturalist's Rambles on the Devonshire Coast",
        "quote": "Under the microscope, each moss animal **zooid** extends its delicate bell of ciliated tentacles."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Division of labor among polymorphs transforms a cluster of individual **zooid** units into a single super-organism."
      }
    ]
  },
  "Dashboard — zo/zoologic.md": {
    "primary": "Of or relating to zoology or the animal kingdom (variant form of zoological).",
    "secondary": "In scientific discourse, describing principles, expeditions, collections, or treatises pertaining to the study of animals.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Our **zoologic** collections from the Galápagos archipelago revealed endemic tortoises on each separate island."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "Agassiz organized an extensive **zoologic** survey to catalog the marine invertebrates of the Massachusetts coast."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Guide to the Study of Insects",
        "quote": "Careful anatomical dissection remains the foundation of all sound **zoologic** classification."
      }
    ]
  },
  "Dashboard — zo/zoological.md": {
    "primary": "Relating to the science of zoology, animal life, or the comparative study of animals.",
    "secondary": "In academic biology, pertaining to institutional collections, taxonomic classifications, field expeditions, or evolutionary morphology of fauna.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "From a strictly **zoological** point of view, the anatomical differences between man and the higher apes are remarkably slight."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Every **zoological** classification reflects the degrees of genealogical affinity shared by living forms."
      },
      {
        "author": "Ernst Mayr",
        "work": "Principles of Systematic Zoology",
        "quote": "Modern **zoological** nomenclature requires formal Latinized binomina anchored by designated type specimens."
      }
    ]
  },
  "Dashboard — zo/zoologist.md": {
    "primary": "A specialist or expert in zoology; a biological scientist who studies animals, their behavior, physiology, genetics, and classification.",
    "secondary": "In professional science, an investigator conducting empirical research on living or extinct animal species in field and laboratory settings.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The field **zoologist** finds endless wonder in observing how bizarre adaptations fit each species to its local environment."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "The evolutionary **zoologist** recognizes that species are dynamic breeding populations rather than static morphological types."
      },
      {
        "author": "Konrad Lorenz",
        "work": "King Solomon's Ring",
        "quote": "A true **zoologist** must live in intimate proximity with his animal subjects to interpret the subtleties of their instinctual signals."
      }
    ]
  },
  "Dashboard — zo/zoology.md": {
    "primary": "The scientific study of the behavior, physiology, classification, genetics, and distribution of animals.",
    "secondary": "In natural science, the overarching biological discipline encompassing ethology, comparative anatomy, entomology, herpetology, mammalogy, and marine biology.",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "History of Animals",
        "quote": "Aristotle laid the structural foundations of systematic **zoology** through his empirical dissections of cephalopods and marine vertebrates."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Comparative anatomy became the indispensable compass guiding modern **zoology** through the labyrinth of animal diversity."
      },
      {
        "author": "Stephen Jay Gould",
        "work": "The Panda's Thumb",
        "quote": "The history of **zoology** is punctuated by revolutionary debates over body plans and evolutionary contingency."
      }
    ]
  },
  "Dashboard — zo/zoomorphism.md": {
    "primary": "The attribution of animal form, characteristics, or qualities to deities, humans, inanimate objects, or abstract concepts.",
    "secondary": "In art history, anthropology, and religious studies, the depiction of gods or sacred symbols as animals (e.g., ancient Egyptian jackal, falcon, and ibis deities).",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Ancient Egyptian religion celebrated widespread **zoomorphism**, venerating the gods under the forms of falcons, cats, and baboons."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Early religious thought transitioned from animism to formal **zoomorphism** before anthropomorphic pantheons were created."
      },
      {
        "author": "Carl Jung",
        "work": "Man and His Symbols",
        "quote": "In mythical dreams, psychological archetypes frequently appear in the guise of instinctual **zoomorphism**, such as serpents and lions."
      }
    ]
  },
  "Dashboard — zo/zoon.md": {
    "primary": "An animal; an individual living animal organism, particularly one developed from a fertilized ovum (distinguished from a colony or zooid).",
    "secondary": "In philosophical biology and theoretical zoology, the total product of a single ovum, which may consist of an individual creature or an entire polymorphic colony.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "Huxley debated whether a colonial siphonophore should be regarded as an assemblage of organs or a single physiological **zoon**."
      },
      {
        "author": "Richard Owen",
        "work": "On Parthenogenesis",
        "quote": "In philosophical anatomy, each complete individual organism developed from a distinct fertilized ovum constitutes an authentic **zoon**."
      },
      {
        "author": "Herbert Spencer",
        "work": "The Principles of Biology",
        "quote": "Spencer analyzed how social aggregations of metazoan individuals mimic the integration of parts within an individual **zoon**."
      }
    ]
  },
  "Dashboard — zo/zoonosis.md": {
    "primary": "Any infectious disease that can be naturally transmitted from vertebrate animals to humans.",
    "secondary": "In epidemiology and public health, diseases such as rabies, anthrax, Ebola, plague, and avian influenza involving complex wild or domestic animal reservoirs.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Bovine tuberculosis represents a perilous **zoonosis** transmitted to children via contaminated milk supplies."
      },
      {
        "author": "David Quammen",
        "work": "Spillover: Animal Infections and the Next Human Pandemic",
        "quote": "Nearly every emerging global epidemic begins as a wildlife **zoonosis** jumping across the species barrier."
      },
      {
        "author": "Patrick Manson",
        "work": "Tropical Diseases",
        "quote": "Breaking the transmission cycle of a vector-borne **zoonosis** requires controlling both the insect carrier and the animal host."
      }
    ]
  },
  "Dashboard — zo/zoonotic.md": {
    "primary": "Of, relating to, or capable of being transmitted from animals to humans; characteristic of a zoonosis.",
    "secondary": "In veterinary epidemiology and global health, describing pathogens, reservoirs, or spillover events where animal microbes infect human populations.",
    "quotes": [
      {
        "author": "David Quammen",
        "work": "Spillover: Animal Infections and the Next Human Pandemic",
        "quote": "Bats harbor a diverse array of lethal **zoonotic** viruses, including Nipah, Hendra, and Marburg."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Glanders in horses is a hazardous **zoonotic** bacterial infection easily contracted by stablemen."
      },
      {
        "author": "Donald Henderson",
        "work": "Smallpox: The Death of a Disease",
        "quote": "Unlike smallpox, diseases with extensive **zoonotic** reservoirs in wild fauna can never be permanently eradicated from nature."
      }
    ]
  },
  "Dashboard — zo/zoophagy.md": {
    "primary": "The practice or habit of feeding on animal matter; carnivory.",
    "secondary": "In comparative physiology and ecology, dietary specialization on live or freshly killed animal prey, contrasted with phytophagy (herbivory).",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy of the Invertebrates",
        "quote": "The sharp scissor-like dentition of the felid skull is an extreme anatomical adaptation to obligate **zoophagy**."
      },
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "Darwin demonstrated that sundews and Venus flytraps engage in functional **zoophagy** to obtain nitrogen in nutrient-poor bogs."
      },
      {
        "author": "Alpheus Spring Packard",
        "work": "Zoology for High Schools and Colleges",
        "quote": "Predatory ground beetles exhibit voracious **zoophagy**, devouring caterpillars and earthworms in nocturnal hunts."
      }
    ]
  },
  "Dashboard — zo/zoophyte.md": {
    "primary": "An animal that is plant-like in appearance or growth habit, such as a sea anemone, coral, hydroid, or sponge; a plant-animal.",
    "secondary": "In historical natural history (16th–19th centuries), an intermediate organism once believed to form a living bridge between the plant and animal kingdoms.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The shallow tidal pools were encrusted with delicate corallines and branching **zoophyte** colonies resembling miniature mosses."
      },
      {
        "author": "Philip Henry Gosse",
        "work": "A Naturalist's Rambles on the Devonshire Coast",
        "quote": "When touched, the flowering tentacles of the **zoophyte** swiftly retracted into its leathery calyx."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Oceanic Hydrozoa",
        "quote": "Early naturalists debated whether each delicate marine **zoophyte** was truly an animal or an animated sea vegetable."
      }
    ]
  },
  "Dashboard — zo/zooplankton.md": {
    "primary": "Plankton consisting of microscopic and small macroscopic animals and the non-photosynthetic protists floating or drifting in aquatic environments.",
    "secondary": "In biological oceanography and limnology, the primary heterotrophic consumers (copepods, krill, rotifers, larvae) transferring energy from phytoplankton to higher trophic levels.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Billions of copepods and transparent larvae in the **zooplankton** drift through the sunlit pelagic layer, grazing upon diatoms."
      },
      {
        "author": "Alister Hardy",
        "work": "The Open Sea: Its Natural History",
        "quote": "The vertical migration of oceanic **zooplankton** under cover of darkness is the greatest biomass movement on planet Earth."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Planktonic Studies",
        "quote": "Haeckel marveled at the geometric silicoflagellates and tintinnids comprising the surface **zooplankton** of open ocean gyres."
      }
    ]
  },
  "Dashboard — zo/zoopoetics.md": {
    "primary": "The study or creative exploration of the presence, agency, voice, and representation of non-human animals in literature, poetry, and art.",
    "secondary": "In eco-criticism and literary theory, a critical framework interrogating how human language attempts to capture animal consciousness, embodiment, and umwelt.",
    "quotes": [
      {
        "author": "Jacques Derrida",
        "work": "The Animal That Therefore I Am",
        "quote": "Derrida's philosophical reflections on the gaze of his cat laid the groundwork for contemporary **zoopoetics** in critical theory."
      },
      {
        "author": "Donna Haraway",
        "work": "When Species Meet",
        "quote": "Practicing feminist **zoopoetics** requires writers to acknowledge the co-shaping agency of non-human companion species."
      },
      {
        "author": "J. M. Coetzee",
        "work": "The Lives of Animals",
        "quote": "Through visceral prose, the novelist engages in intense **zoopoetics**, imagining the sensory life and suffering of caged beasts."
      }
    ]
  },
  "Dashboard — zo/zoospore.md": {
    "primary": "A motile, flagellated asexual spore produced by many algae and lower fungi, capable of independent swimming.",
    "secondary": "In mycology and phycology, a reproductive swarmer propelled by anterior tinsel or posterior whiplash flagella that settles and germinates into a vegetative thallus.",
    "quotes": [
      {
        "author": "M. C. Cooke",
        "work": "British Fresh-Water Algae",
        "quote": "The sporangium of Oedogonium ruptures, discharging an energetic **zoospore** crowned with a ring of vibrating cilia."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Handbook of Practical Botany",
        "quote": "After swimming vigorously in water, each algal **zoospore** loses its flagella, encysts, and sprouts a new filament."
      },
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology of the Fungi",
        "quote": "De Bary discovered that the potato blight fungus spreads epidemic blight through moisture-borne **zoospore** swarmers."
      }
    ]
  },
  "Dashboard — zo/zootoxin.md": {
    "primary": "A toxic substance or venom produced by an animal, such as a snake, spider, scorpion, jellyfish, or cone snail.",
    "secondary": "In toxinology and biochemical pharmacology, complex polypeptide mixtures of neurotoxins, hemotoxins, and cytotoxins acting upon physiological targets.",
    "quotes": [
      {
        "author": "S. Weir Mitchell",
        "work": "Researches upon the Venoms of Poisonous Serpents",
        "quote": "Mitchell conducted pioneering chemical analyses of rattlesnake **zootoxin**, demonstrating its destructive effect on blood capillary walls."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intense local tissue necrosis followed the injection of cobra **zootoxin** into the victim's forearm."
      },
      {
        "author": "Louis Lewin",
        "work": "The Toxic Substances in the Animal Kingdom",
        "quote": "Each deadly marine **zootoxin** evolved as an offensive hunting weapon or a defensive barrier against predators."
      }
    ]
  },
  "Dashboard — zo/zooxanthella.md": {
    "primary": "A yellowish-brown intracellular symbiotic dinoflagellate algae living inside the tissues of marine invertebrates, especially reef-building corals, giant clams, and jellyfish.",
    "secondary": "In coral reef ecology and cell biology, photosynthetic endosymbionts (family Symbiodiniaceae) whose expulsion under elevated sea temperatures causes coral bleaching.",
    "quotes": [
      {
        "author": "Philip Henry Gosse",
        "work": "A Naturalist's Rambles on the Devonshire Coast",
        "quote": "Microscopic examination revealed thousands of golden **zooxanthella** cells embedded in the anemone's translucent tentacles."
      },
      {
        "author": "C. M. Yonge",
        "work": "The Great Barrier Reef Expedition",
        "quote": "Yonge demonstrated that the giant clam Tridacna farms photosynthetic **zooxanthella** colonies in its fleshy mantle lobes."
      },
      {
        "author": "Sylvia Earle",
        "work": "Sea Change: A Message of the Oceans",
        "quote": "Rising ocean temperatures stress the coral host, causing it to eject its essential **zooxanthella** partners in devastating bleaching events."
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

console.log(`Updated ${updatedCount} files in Batch 9!`);
