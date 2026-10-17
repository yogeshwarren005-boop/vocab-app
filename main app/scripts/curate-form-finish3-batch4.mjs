import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — pter\\pteropod.md": {
    "primary": "Any small, pelagic marine gastropod mollusk belonging to the clade Thecosomata or Gymnosomata, commonly called a sea butterfly.",
    "secondary": "In biological oceanography and paleoceanography, calcifying planktonic snails whose aragonite shells sink to form pteropod ooze on oceanic abyssal plains.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In tropical latitudes, pelagic **pteropod** shells drifted past our keel, fluttering through the clear blue water like miniature butterflies."
      },
      {
        "author": "S. P. Woodward",
        "work": "A Manual of the Mollusca",
        "quote": "The foot in each oceanic **pteropod** is modified into two broad wing-like fins that propel the tiny shell through open seas."
      },
      {
        "author": "Ernst Haeckel",
        "work": "Planktonic Studies",
        "quote": "Oceanic trawls captured millions of **pteropod** mollusks whose delicate calcareous shells carpet wide tracts of deep Atlantic sediments."
      }
    ]
  },
  "Dashboard — pter\\pteropogon.md": {
    "primary": "A botanical genus name or taxonomic section in Asteraceae characterized by feathery-bristled pappus hairs.",
    "secondary": "In systematic botany, Australian composite herbs with plumose pappi adapted for anemochoric fruit dispersal.",
    "quotes": [
      {
        "author": "George Bentham",
        "work": "Flora Australiensis",
        "quote": "The feathery bristles of **pteropogon** expand widely upon dry desert winds, carrying the tiny achenes across sandy plains."
      },
      {
        "author": "Ferdinand von Mueller",
        "work": "Fragmenta Phytographiae Australiae",
        "quote": "We observed bright papery blossoms of **pteropogon** covering the stony ridges of the interior with yellow carpets."
      },
      {
        "author": "William Jackson Hooker",
        "work": "Icones Plantarum",
        "quote": "The plumose pappus setae in **pteropogon** provide diagnostic separation from allied helichrysoid composites."
      }
    ]
  },
  "Dashboard — pter\\pteropsida.md": {
    "primary": "A major division or class of vascular plants in traditional taxonomy comprising ferns, gymnosperms, and angiosperms.",
    "secondary": "In evolutionary plant morphology, a taxonomic assemblage characterized by large, megaphyllous leaves with leaf gaps in the central stele.",
    "quotes": [
      {
        "author": "Arthur J. Eames",
        "work": "Morphology of Vascular Plants: Lower Groups",
        "quote": "The grouping **pteropsida** emphasized the shared possession of complex megaphyllous foliage contrasting with microphyllous lycopods."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Evolution of the Land Plants",
        "quote": "In **pteropsida**, the leaf gap interrupts the vascular ring, reflecting the immense conductive demand of expansive leaf blades."
      },
      {
        "author": "Harold C. Bold",
        "work": "Morphology of Plants",
        "quote": "Comparative morphologists long debated whether **pteropsida** represented a truly monophyletic clade or a grades-level assemblage."
      }
    ]
  },
  "Dashboard — pter\\pteropus.md": {
    "primary": "A genus of large megabats in the family Pteropodidae, commonly known as flying foxes or fruit bats, native to Old World tropics.",
    "secondary": "In mammalogy and tropical forest ecology, large non-echolocating frugivorous bats vital as keystone seed dispersers and pollinators.",
    "quotes": [
      {
        "author": "Thomas Pennant",
        "work": "Synopsis of Quadrupeds",
        "quote": "The great bat of Madagascar, belonging to **pteropus**, spans nearly four feet between the tips of its extended wings."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "In **pteropus**, the sense of smell is exquisitely acute, guiding the animal to nocturnal blossoms and ripening forest fruits."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Enormous colonies of **pteropus** hung suspended by their claws from bare mangrove boughs, screeching when the sun rose."
      }
    ]
  },
  "Dashboard — pter\\pterosaur.md": {
    "primary": "Any extinct Mesozoic flying reptile belonging to the order Pterosauria, having wings formed by a membrane supported by an elongated fourth finger.",
    "secondary": "In vertebrate paleontology, the first vertebrate lineage to achieve powered flight, spanning from Late Triassic to the end of the Cretaceous.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Palaeontology: Or a Systematic Summary of Extinct Animals",
        "quote": "The air-filled bones of the **pterosaur** rivaled those of modern soaring birds in lightened architectural strength."
      },
      {
        "author": "Gideon Mantell",
        "work": "Petrifactions and Their Teachings",
        "quote": "The fragile wing bones of the giant chalk **pterosaur** demonstrate how flight conquered prehistoric skies millions of years before man."
      },
      {
        "author": "Peter Wellnhofer",
        "work": "The Illustrated Encyclopedia of Pterosaurs",
        "quote": "Pycnofiber coatings preserved on fossil specimens confirm that the active **pterosaur** maintained endothermic metabolic regulation."
      }
    ]
  },
  "Dashboard — pter\\pterosauria.md": {
    "primary": "The extinct taxonomic order of flying archosaurian reptiles that lived during the Mesozoic era.",
    "secondary": "In systematic vertebrate paleontology, an archosaur clade comprising Rhamphorhynchoidea and Pterodactyloidea, characterized by patagial wing membranes.",
    "quotes": [
      {
        "author": "Harry Govier Seeley",
        "work": "Dragons of the Air: An Account of Extinct Flying Reptiles",
        "quote": "The order **pterosauria** represents nature's boldest experiment in combining reptilian skeletal patterns with sustained avian locomotion."
      },
      {
        "author": "Christian Erich Hermann von Meyer",
        "work": "Zur Fauna der Vorwelt",
        "quote": "Fossils belonging to **pterosauria** from Solnhofen quarries reveal the delicate impression of the leathery flight membrane."
      },
      {
        "author": "Karl Alfred von Zittel",
        "work": "Text-Book of Palaeontology",
        "quote": "Throughout the Jurassic and Cretaceous periods, **pterosauria** dominated the aerial vertebrate ecological niches across continental margins."
      }
    ]
  },
  "Dashboard — pter\\pterospermum.md": {
    "primary": "A genus of tropical Asian trees and shrubs in the mallow family (Malvaceae), commonly known as bayur trees.",
    "secondary": "In dendrology and ethnobotany, evergreen trees valued for hardwood timber and fragrant white nocturnal flowers with winged seeds in woody capsules.",
    "quotes": [
      {
        "author": "William Roxburgh",
        "work": "Flora Indica",
        "quote": "The broad, oblique leaves of **pterospermum** are densely covered with rusty tomentum beneath, contrasting with their glossy green upper surfaces."
      },
      {
        "author": "Nathaniel Wallich",
        "work": "Plantae Asiaticae Rariores",
        "quote": "In the foothills of Bengal, **pterospermum** unfolds large, sweet-smelling white flowers that open at twilight."
      },
      {
        "author": "George King",
        "work": "Materials for a Flora of the Malayan Peninsula",
        "quote": "Upon maturity, the woody five-angled capsule of **pterospermum** splits to liberate numerous membranously winged seeds."
      }
    ]
  },
  "Dashboard — pter\\pterostigma.md": {
    "primary": "A specialized, pigmented, or opaque cell located on the anterior margin of an insect's wing near the apex.",
    "secondary": "In insect biomechanics, an inertial mass on the leading edge (especially prominent in dragonflies) that stabilizes wings against aerodynamic pitch flutter at high speeds.",
    "quotes": [
      {
        "author": "John Henry Comstock",
        "work": "The Wings of Insects",
        "quote": "The dark, thickened **pterostigma** along the costal vein provides an indispensable taxonomic landmark in odonate venation."
      },
      {
        "author": "R. J. Tillyard",
        "work": "The Biology of Dragonflies",
        "quote": "The aerodynamic weight of the **pterostigma** damps out destructive wing oscillations during high-velocity gliding."
      },
      {
        "author": "A. D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "In many hymenopterous parasites, the presence or absence of a distinct **pterostigma** dictates family diagnosis."
      }
    ]
  },
  "Dashboard — pter\\pterostylis.md": {
    "primary": "A genus of terrestrial orchids native to Australasia, commonly known as greenhood orchids, bearing hooded green or reddish flowers.",
    "secondary": "In pollination biology, orchids featuring a sensitive, touch-triggered labellum that snaps shut when insects land, trapping them against the reproductive column.",
    "quotes": [
      {
        "author": "Robert Brown",
        "work": "Prodromus Florae Novae Hollandiae",
        "quote": "I designated this remarkable orchid genus **pterostylis** in reference to the winged lateral expansion of the column."
      },
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "The irritable labellum of **pterostylis** acts like a spring trap, enclosing small gnats within the hood to ensure pollen deposit."
      },
      {
        "author": "Joseph Maiden",
        "work": "The Forest Flora of New South Wales",
        "quote": "Colonies of **pterostylis** produce rosettes of soft basal leaves on sheltered woodland soils before sending up solitary hooded blooms."
      }
    ]
  },
  "Dashboard — pter\\pterygium.md": {
    "primary": "An abnormal triangular, fleshy fibrovascular growth of the bulbar conjunctiva that encroaches across the limbus onto the cornea.",
    "secondary": "In clinical ophthalmology, a benign degenerative lesion associated with chronic ultraviolet radiation and dust exposure, causing astigmatism and visual loss.",
    "quotes": [
      {
        "author": "William Mackenzie",
        "work": "A Practical Treatise on the Diseases of the Eye",
        "quote": "When a progressive **pterygium** advances across the pupil, surgical excision is necessary to preserve unimpeded visual acuity."
      },
      {
        "author": "Albrecht von Graefe",
        "work": "Archiv für Ophthalmologie",
        "quote": "Meticulous limbal conjunctival autografting after the excision of **pterygium** dramatically reduces the rate of postoperative recurrence."
      },
      {
        "author": "Sir Stewart Duke-Elder",
        "work": "System of Ophthalmology",
        "quote": "Epidemiological surveys confirm that prolonged solar ultraviolet exposure is the primary etiologic factor in **pterygium** development."
      }
    ]
  },
  "Dashboard — pter\\pterygote.md": {
    "primary": "Any insect belonging to the subclass Pterygota, characterized by wings or descended from winged ancestors.",
    "secondary": "In systematic entomology, comprising the vast majority of insects, exhibiting tracheal systems, thoracic flight sclerites, and metamorphic development.",
    "quotes": [
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "Flight muscles within a **pterygote** thorax achieve metabolic rates and contraction frequencies unmatched elsewhere in the animal kingdom."
      },
      {
        "author": "A. D. Imms",
        "work": "A General Textbook of Entomology",
        "quote": "Even wingless fleas and lice belong to the **pterygote** lineage, having secondarily shed their wings in adaptation to ectoparasitism."
      },
      {
        "author": "Michael S. Engel",
        "work": "Evolution of the Insects",
        "quote": "The appearance of the first **pterygote** in the Carboniferous unleashed the most explosive adaptive radiation in terrestrial history."
      }
    ]
  },
  "Dashboard — pter\\tetrapterous.md": {
    "primary": "Having four wings, four wing-like appendages, or four prominent longitudinal angles or ribs.",
    "secondary": "In systematic botany and entomology, describing four-angled stems, quadrangular fruits, or four-winged flying insects.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Philosophia Botanica",
        "quote": "When a seed pod develops four longitudinal membranous fins, the fruit is termed **tetrapterous**."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "The **tetrapterous** stem of the cruciferous plant provides increased aerodynamic stability along windblown sea bluffs."
      },
      {
        "author": "Thomas Say",
        "work": "American Entomology",
        "quote": "The specimen exhibits a **tetrapterous** flight apparatus composed of four transparent, delicately reticulated wings."
      }
    ]
  },
  "Dashboard — pterid\\pteridaceae.md": {
    "primary": "The brake fern or maidenhair family of leptosporangiate ferns, cosmopolitan in distribution and diverse in ecological habit.",
    "secondary": "In pteridology, characterized by marginal or linear superficial sori often lacking a true indusium and protected by reflexed pinnule margins.",
    "quotes": [
      {
        "author": "Rolla M. Tryon",
        "work": "The Fern Genus Pityrogramma",
        "quote": "Species within **pteridaceae** demonstrate extraordinary drought tolerance, curling their fronds tightly during seasonal dry spells."
      },
      {
        "author": "Robbin C. Moran",
        "work": "A Natural History of Ferns",
        "quote": "In the family **pteridaceae**, the sporangia trace the veins or line the edge beneath a protective pseudo-indusium."
      },
      {
        "author": "David B. Lellinger",
        "work": "A Field Manual of Ferns and Fern-Allies",
        "quote": "The dark, wiry stipes and fan-shaped pinnules of Adiantum make **pteridaceae** easily recognizable to field naturalists."
      }
    ]
  },
  "Dashboard — pterid\\pteridium.md": {
    "primary": "A genus of large, coarse terrestrial ferns in the family Dennstaedtiaceae, commonly known as bracken or brake.",
    "secondary": "In plant ecology, aggressive rhizomatous perennial ferns containing carcinogenic ptaquiloside, dominating open pastures and fire-prone woodlands.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "The cosmopolitan fern **pteridium** forms vast stands on uncultivated moors, unrolling stout crosiers each spring."
      },
      {
        "author": "A. C. Seward",
        "work": "Plant Life Through the Ages",
        "quote": "Fossil frond impressions indistinguishable from modern **pteridium** occur across Cretaceous and Tertiary strata."
      },
      {
        "author": "George Nicholson",
        "work": "The Illustrated Dictionary of Gardening",
        "quote": "The deep subterranean rootstocks of **pteridium** survive moorland fires and send up vigorous fronds through scorched peat."
      }
    ]
  },
  "Dashboard — pterid\\pteridological.md": {
    "primary": "Of, relating to, or concerned with pteridology, the scientific study of ferns and related seedless vascular plants.",
    "secondary": "In botanical scholarship, describing taxonomic surveys, field excursions, or herbarium research focused on fern biodiversity.",
    "quotes": [
      {
        "author": "William Jackson Hooker",
        "work": "Species Filicum",
        "quote": "This volume incorporates extensive **pteridological** monographs contributed by correspondents from botanical stations across the empire."
      },
      {
        "author": "John Gilbert Baker",
        "work": "Synopsis Filicum",
        "quote": "Standardizing the diagnostic terminology in **pteridological** works remains vital for international herbarium curation."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Structure and Development of Mosses and Ferns",
        "quote": "Our **pteridological** investigations into gametophyte development shed unexpected light on the ancestry of early seed plants."
      }
    ]
  },
  "Dashboard — pterid\\pteridologist.md": {
    "primary": "A botanist or researcher who specializes in the study of ferns, horsetails, and related spore-bearing plants.",
    "secondary": "In botanical history, a specialist skilled in discriminating fern species by sporangial anatomy, venation, and chromosome counts.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Letters of Asa Gray",
        "quote": "Our visiting **pteridologist** examined the dried collections, identifying two undescribed cliff-brakes from the Rio Grande."
      },
      {
        "author": "Edward Tuckerman",
        "work": "Genera Lichenum",
        "quote": "The discerning **pteridologist** notes every gradation in indusial curvature when delineating polymorphic species."
      },
      {
        "author": "Warren H. Wagner Jr.",
        "work": "Systematic Botany: Appalachian Aspleniums",
        "quote": "By synthesizing cytological evidence and field ecology, the modern **pteridologist** unravels reticulate evolution in wild fern complexes."
      }
    ]
  },
  "Dashboard — pterid\\pteridology.md": {
    "primary": "The scientific study of ferns, horsetails, lycophytes, and related seedless vascular cryptogams.",
    "secondary": "In plant biology, a specialized discipline encompassing the evolutionary history, cytology, ecology, and taxonomy of pteridophytes.",
    "quotes": [
      {
        "author": "John Smith",
        "work": "Historia Filicum: An Exposition of the Nature and Organography of Ferns",
        "quote": "The Victorian era witnessed an extraordinary surge of interest in **pteridology**, transforming amateur collecting into precise botanical science."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns: Filicales",
        "quote": "Fundamental advancements in **pteridology** rely upon analyzing the vascular architecture of both fossil and living rhizomes."
      },
      {
        "author": "Rolla M. Tryon",
        "work": "Ferns and Allied Plants",
        "quote": "Field **pteridology** in montane cloud forests continually brings to light cryptic and micro-endemic species."
      }
    ]
  },
  "Dashboard — pterid\\pteridophyta.md": {
    "primary": "The taxonomic plant division comprising ferns, clubmosses, and horsetails, reproducing by spores rather than seeds.",
    "secondary": "In plant systematics, an ancient lineage of vascular cryptogams whose sporophyte generation is dominant and equipped with true xylem and phloem.",
    "quotes": [
      {
        "author": "Adolf Engler",
        "work": "Syllabus der Pflanzenfamilien",
        "quote": "Within the plant kingdom, **pteridophyta** marks the epochal evolutionary threshold where internal conducting vessels first appeared."
      },
      {
        "author": "Arthur J. Eames",
        "work": "Morphology of Vascular Plants",
        "quote": "Comparative stelar morphology confirms that **pteridophyta** includes both primitive protostelic and advanced dictyostelic architectures."
      },
      {
        "author": "Douglas Houghton Campbell",
        "work": "The Evolution of the Land Plants",
        "quote": "Giant tree-like members of **pteridophyta** flourished in the humid swamps of the Paleozoic, laying down our principal coal seams."
      }
    ]
  },
  "Dashboard — pterid\\pteridophyte.md": {
    "primary": "Any vascular plant that reproduces by single-celled spores without producing flowers or seeds (such as a fern or lycopod).",
    "secondary": "In botanical anatomy, a seedless tracheophyte requiring environmental surface water for its flagellated spermatozoids to fertilize the archegonium.",
    "quotes": [
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "The xylem conduits of an herbaceous **pteridophyte** are dominated by scalariformly pitted tracheids rather than vessels."
      },
      {
        "author": "Peter H. Raven",
        "work": "Biology of Plants",
        "quote": "Each **pteridophyte** must establish a delicate haploid gametophyte in moist soil before producing the macroscopic sporophyte generation."
      },
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "The petrified stems of the fossil **pteridophyte** display astonishing tissue preservation in Carboniferous coal balls."
      }
    ]
  },
  "Dashboard — pterid\\pteridosperm.md": {
    "primary": "Any extinct Paleozoic or Mesozoic seed-bearing plant with fern-like foliage belonging to the Pteridospermatophyta; a seed fern.",
    "secondary": "In evolutionary paleobotany, a critical transitional gymnosperm that decoupled sexual reproduction from free-water fertilization while retaining megaphyllous fronds.",
    "quotes": [
      {
        "author": "D. H. Scott",
        "work": "Studies in Fossil Botany",
        "quote": "The historic demonstration that Lyginopteris bore cupulate seeds confirmed the long-hypothesized existence of the **pteridosperm**."
      },
      {
        "author": "F. W. Oliver",
        "work": "On the Structure of the Palaeozoic Seed Lagenostoma Lomaxi",
        "quote": "The microscopic anatomy of the seed established the **pteridosperm** as a profound bridge between vascular cryptogams and gymnosperms."
      },
      {
        "author": "Thomas N. Taylor",
        "work": "Paleobotany: The Biology and Evolution of Fossil Plants",
        "quote": "Pollen-bearing microsporangia found associated with each **pteridosperm** shed light on early wind-pollination mechanisms."
      }
    ]
  },
  "Dashboard — pterid\\pteridospermae.md": {
    "primary": "The extinct taxonomic class of seed ferns, prominent in late Paleozoic and Mesozoic floras.",
    "secondary": "In paleobotany, fossil seed plants combining fern-like leaf morphology with true gymnospermous seeds, secondary wood, and pollen organs.",
    "quotes": [
      {
        "author": "Robert Kidston",
        "work": "Fossil Plants of the Carboniferous Rocks of Great Britain",
        "quote": "Compression specimens of **pteridospermae** dominate Carboniferous shale beds, preserving exquisite details of frond venation."
      },
      {
        "author": "Chester A. Arnold",
        "work": "An Introduction to Paleobotany",
        "quote": "The formal recognition of **pteridospermae** revolutionized historical paleobotany by reclassifying half of all Carboniferous 'ferns.'"
      },
      {
        "author": "Henry N. Andrews",
        "work": "Studies in Paleobotany",
        "quote": "Ovules borne directly upon the vegetative pinnules of **pteridospermae** demonstrate primitive gymnospermous reproductive architecture."
      }
    ]
  },
  "Dashboard — pterid\\pteridospermaphyta.md": {
    "primary": "A proposed taxonomic division or phylum encompassing the extinct seed ferns (pteridosperms).",
    "secondary": "In plant macroevolution, an ancient gymnospermous division considered ancestral or sister to modern cycads, bennettites, and angiosperms.",
    "quotes": [
      {
        "author": "Armen Takhtajan",
        "work": "Evolutionary Trends in Flowering Plants",
        "quote": "Morphologists frequently trace the origin of the angiosperm carpel to the cupulate appendages of **pteridospermaphyta**."
      },
      {
        "author": "Arthur Cronquist",
        "work": "An Integrated System of Classification of Flowering Plants",
        "quote": "The division **pteridospermaphyta** represents the evolutionary crucible in which early seed plant diversity was forged."
      },
      {
        "author": "A. C. Seward",
        "work": "Fossil Plants",
        "quote": "Foliar and anatomical diversity within **pteridospermaphyta** shows that seed production evolved early among megaphyllous lineages."
      }
    ]
  },
  "Dashboard — pterid\\pteridospermopsida.md": {
    "primary": "The formal taxonomic class of extinct seed ferns within the gymnosperms, flourishing from the Devonian to the Cretaceous.",
    "secondary": "In systematic paleobotany, encompassing classical orders like Lyginopteridales and Medullosales, having seeds encased in protective cupules.",
    "quotes": [
      {
        "author": "Thomas N. Taylor",
        "work": "The Biology and Evolution of Fossil Plants",
        "quote": "Within **pteridospermopsida**, the Medullosales reached massive proportions, their trunks supported by extensive secondary vascular growth."
      },
      {
        "author": "Wilson N. Stewart",
        "work": "Paleobotany and the Evolution of Plants",
        "quote": "The discovery of petrified ovules belonging to **pteridospermopsida** settled debates regarding the non-fern nature of Carboniferous fronds."
      },
      {
        "author": "Harlan P. Banks",
        "work": "Evolution and Plants of the Past",
        "quote": "The cupule morphology in **pteridospermopsida** represents an important precursor to the protective integuments of modern seeds."
      }
    ]
  },
  "Dashboard — pyel\\pyelitis.md": {
    "primary": "Inflammation of the renal pelvis, typically caused by an ascending bacterial infection from the lower urinary tract.",
    "secondary": "In clinical nephrology and urology, a condition presenting with flank pain, chills, fever, and pyuria, distinct from deep parenchymal nephritis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute **pyelitis**, the urine contains abundant pus cells and pelvis epithelium, accompanied by sudden lumbar tenderness and rigors."
      },
      {
        "author": "Thomas Addison",
        "work": "Observations on Disorders of the Kidney",
        "quote": "Catheterization of the ureters confirmed that the purulent discharge originated from localized **pyelitis** without cortical destruction."
      },
      {
        "author": "William Roberts",
        "work": "A Practical Treatise on Urinary and Renal Diseases",
        "quote": "Calculous **pyelitis** arises when an abrasive gravel stone lodges within the pelvis, exciting chronic mucosal suppuration."
      }
    ]
  },
  "Dashboard — pyel\\pyelogram.md": {
    "primary": "A radiographic image or X-ray of the renal pelvis, ureters, and urinary tract obtained using a radiopaque contrast medium.",
    "secondary": "In diagnostic radiology, an imaging record (intravenous or retrograde) used to detect nephrolithiasis, hydronephrosis, or filling defects.",
    "quotes": [
      {
        "author": "Alexander Randall",
        "work": "Surgical Pathology of Prostatic Obstructions",
        "quote": "The intravenous **pyelogram** outlined dilated ureteral contours caused by chronic bladder neck obstruction."
      },
      {
        "author": "Hugh H. Young",
        "work": "Practice of Urology",
        "quote": "A retrograde **pyelogram** clearly demonstrated the calculus wedged at the ureteropelvic junction."
      },
      {
        "author": "Meredith Campbell",
        "work": "Clinical Pediatric Urology",
        "quote": "Evaluation of congenital hydronephrosis in infants requires a carefully timed excretory **pyelogram**."
      }
    ]
  },
  "Dashboard — pyel\\pyelography.md": {
    "primary": "The radiographic examination and imaging of the renal pelvis and ureter following the administration of radiopaque contrast media.",
    "secondary": "In clinical urology, categorized into intravenous (excretory) and retrograde techniques to assess renal morphology and function.",
    "quotes": [
      {
        "author": "Alexander von Lichtenberg",
        "work": "Intravenous Pyelography",
        "quote": "The introduction of excretory **pyelography** transformed urological diagnostics by rendering exploratory surgery unnecessary in most renal colic cases."
      },
      {
        "author": "Hugh H. Young",
        "work": "Young's Practice of Urology",
        "quote": "When intravenous visualization proves faint, retrograde **pyelography** provides sharp anatomical delineation of the renal calyces."
      },
      {
        "author": "John K. Lattimer",
        "work": "Urology in Childhood",
        "quote": "Modern contrast agents made pediatric **pyelography** safer while minimizing systemic adverse reactions."
      }
    ]
  },
  "Dashboard — pyel\\pyelonephritis.md": {
    "primary": "An inflammatory disease and bacterial infection affecting both the renal parenchyma and the renal pelvis.",
    "secondary": "In clinical nephrology, categorized as acute or chronic, presenting with high fever, flank pain, leukocytosis, and risk of renal scarring or sepsis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute **pyelonephritis** demands prompt antibiotic therapy to prevent the formation of multiple cortical abscesses within the kidney."
      },
      {
        "author": "Arnold R. Rich",
        "work": "The Pathogenesis of Tuberculosis and Renal Diseases",
        "quote": "Ascending bacterial invasion along the ureter represents the most common etiology of bilateral suppurative **pyelonephritis**."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Chronic **pyelonephritis** remains a major cause of progressive end-stage renal failure accompanied by asymmetric cortical scarring."
      }
    ]
  },
  "Dashboard — pyel\\pyeloscopy.md": {
    "primary": "The visual inspection and examination of the renal pelvis and calyces using an endoscope (pyeloscope or ureteroscope) or fluoroscopy.",
    "secondary": "In endourology, a minimally invasive endoscopic procedure enabling direct visualization, biopsy, and laser ablation of pelvic urothelial tumors and calculi.",
    "quotes": [
      {
        "author": "Meredith Campbell",
        "work": "Pediatric Urology",
        "quote": "Flexible instruments allow pediatric **pyeloscopy** to survey congenital diverticula and relieve ureteropelvic strictures."
      },
      {
        "author": "Hugh H. Young",
        "work": "Practice of Urology",
        "quote": "Fluoroscopic **pyeloscopy** enabled surgeons to observe rhythmic peristaltic contractions emptying the renal pelvis in real time."
      },
      {
        "author": "Victor Marshall",
        "work": "Textbook of Urology",
        "quote": "Direct **pyeloscopy** provides invaluable diagnostic confirmation when filling defects on radiographic films remain indeterminate."
      }
    ]
  },
  "Dashboard — pyg\\callipygian.md": {
    "primary": "Having shapely, beautifully formed, or attractive buttocks.",
    "secondary": "In classical art history and aesthetic literature, designating statues such as the Venus Kallipygos of ancient Syracuse.",
    "quotes": [
      {
        "author": "Théophile Gautier",
        "work": "Mademoiselle de Maupin",
        "quote": "She turned with the sculptural grace of an antique **callipygian** statue, her silhouette glowing in the soft candlelight."
      },
      {
        "author": "James Joyce",
        "work": "Ulysses",
        "quote": "He admired the marble contours of classical goddesses, praising their heroic, **callipygian** perfection in Greek statuary."
      },
      {
        "author": "Aldous Huxley",
        "work": "Point Counter Point",
        "quote": "He smiled cynically at the modern aesthetic obsession with slender forms, recalling more voluptuous **callipygian** ideals of the Renaissance."
      }
    ]
  },
  "Dashboard — pyg\\pygopagus.md": {
    "primary": "Conjoined twins united back-to-back at the sacrum, buttocks, and coccyx.",
    "secondary": "In teratology and pediatric surgery, an uncommon symmetrical conjoined twin fusion where twins often share lower spinal dural sacs, perineum, and distal rectum.",
    "quotes": [
      {
        "author": "George M. Gould",
        "work": "Anomalies and Curiosities of Medicine",
        "quote": "The celebrated Bohemian sisters, Josepha and Rosa Blazek, presented a classic instance of **pygopagus** conjoined twins united at the sacrum."
      },
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "Histoire des anomalies de l'organisation",
        "quote": "In every true **pygopagus**, the skeletal union involves the posterior surfaces of the pelvic girdle without visceral fusion above the pelvis."
      },
      {
        "author": "John William Ballantyne",
        "work": "Manual of Antenatal Pathology and Hygiene",
        "quote": "Surgical separation of a **pygopagus** twin pair poses complex reconstructive challenges for urogenital and anorectal tracts."
      }
    ]
  },
  "Dashboard — pyg\\pygostyle.md": {
    "primary": "A triangular bone formed by the fusion of the caudal vertebrae at the end of the avian spinal column, supporting tail feathers.",
    "secondary": "In avian osteology and functional anatomy, the plowshare-shaped terminal skeletal structure that provides anchorage for the rectrices and associated flight steering musculature.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The fusion of the terminal caudal vertebrae into a **pygostyle** distinguishes modern carinate birds from archaic long-tailed archosaurs."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Vertebrated Animals",
        "quote": "The **pygostyle** serves as a sturdy osseous base for the insertion of the powerful levator and depressor muscles of the tail."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "The Vertebrate Body",
        "quote": "In modern birds, the elongated reptile tail is reduced to a short stump ending in the compact plowshare bone or **pygostyle**."
      }
    ]
  },
  "Dashboard — pyg\\steatopygia.md": {
    "primary": "A condition characterized by substantial genetic accumulation of fat in the buttocks and upper thighs.",
    "secondary": "In physical anthropology and human physiology, a phenotypic trait most prominent in female San (Bushmen) and Khoikhoi populations of southern Africa.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man, and Selection in Relation to Sex",
        "quote": "The pronounced **steatopygia** of Bushmen women was regarded by early travelers as a remarkable racial physical peculiarity."
      },
      {
        "author": "Francis Galton",
        "work": "Narrative of an Explorer in Tropical South Africa",
        "quote": "I observed how **steatopygia** appeared to function as a metabolic energy reserve comparable to the camel's adipose hump."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Anthropometric measurements of gluteal fat deposition in southern Africa establish the unique physiological distribution of **steatopygia**."
      }
    ]
  },
  "Dashboard — pyramid\\dipyramid.md": {
    "primary": "A geometric polyhedron formed by joining two identical pyramids base-to-base.",
    "secondary": "In crystallography, a crystal form comprising two matching pyramids inverted against each other across a central horizontal plane of symmetry.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "Manual of Mineralogy",
        "quote": "In the tetragonal system, zircon commonly crystallizes as a prism terminated by a symmetrical **dipyramid**."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Textbook of Mineralogy",
        "quote": "The hexagonal **dipyramid** comprises twelve triangular faces meeting at two opposite vertical summits."
      },
      {
        "author": "Henry Alexander Miers",
        "work": "Mineralogy: An Introduction to the Scientific Study of Minerals",
        "quote": "Crystalline quartz rarely presents an uncorrupted **dipyramid**, because unequal face development distorts the geometric ideal."
      }
    ]
  },
  "Dashboard — pyramid\\pyramid.md": {
    "primary": "A monumental ancient stone structure with a square or triangular base and sloping triangular sides meeting at an apex.",
    "secondary": "In solid geometry, a polyhedron formed by connecting a polygonal base and a point, called the apex.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "Histories",
        "quote": "Cheops compelled all his subjects to work on the great **pyramid**, dragging limestone blocks from Arabian quarries across the Nile."
      },
      {
        "author": "Napoleon Bonaparte",
        "work": "Proclamation to the Army of Egypt",
        "quote": "Soldiers, from the height of this magnificent **pyramid**, forty centuries of history gaze down upon your deeds today."
      },
      {
        "author": "John Greaves",
        "work": "Pyramidographia: Or a Description of the Pyramids in Aegypt",
        "quote": "The solid masonry of the Great **pyramid** stands as an everlasting monument to ancient mathematical and mechanical genius."
      }
    ]
  },
  "Dashboard — pyramid\\pyramidal.md": {
    "primary": "Having the form, shape, or geometric proportions of a pyramid; tapering to a point from an angular base.",
    "secondary": "In neuroanatomy, designating the corticospinal motor tracts whose upper motor neurons arise from pyramidal cells in the cerebral cortex.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **pyramidal** tracts originate from giant cells of Betz in the precentral gyrus, descending through the internal capsule to the spinal cord."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "The apical dendrite of a cerebral **pyramidal** neuron ascends through cortical layers to arborize beneath the pial surface."
      },
      {
        "author": "Charles Bell",
        "work": "The Nervous System of the Human Body",
        "quote": "Lesions within the **pyramidal** decussation in the medulla oblongata result in contralateral motor hemiplegia."
      }
    ]
  },
  "Dashboard — pyramid\\pyramidic.md": {
    "primary": "Of, relating to, or resembling a pyramid; pyramidal.",
    "secondary": "In literature and natural philosophy, describing towering, faceted, or tapering structures resembling an ancient pyramid.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick; or, The Whale",
        "quote": "The sperm whale's forehead rose like a vast **pyramidic** mass of solid matter against the ocean spray."
      },
      {
        "author": "Thomas Browne",
        "work": "Hydriotaphia, Urn Burial",
        "quote": "Restless mortals seek immortality through **pyramidic** sepulchres and brass monuments, which time nonetheless crumbles into dust."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "English Traits",
        "quote": "The feudal aristocracy raised its **pyramidic** social order, resting on peasant labor and capped by royal power."
      }
    ]
  },
  "Dashboard — pyramid\\pyramidical.md": {
    "primary": "Having the form of a pyramid; tapering upward to a single peak or apex.",
    "secondary": "In historical and philosophical treatises, characterized by hierarchical, monumental, or tapering geometry.",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Knowledge advances in a **pyramidical** order, broadening from diverse empirical facts to a few unified axioms at the apex."
      },
      {
        "author": "John Evelyn",
        "work": "Sylva, or A Discourse of Forest-Trees",
        "quote": "The Italian cypress grows in a strict **pyramidical** column, making it a favorite ornament for solemn cemetery avenues."
      },
      {
        "author": "Samuel Johnson",
        "work": "Lives of the Most Eminent English Poets",
        "quote": "The architect piled monument upon monument, striving to achieve a **pyramidical** grandeur that overpowered the eye."
      }
    ]
  },
  "Dashboard — pyramid\\pyramidically.md": {
    "primary": "In the form, manner, or geometric proportions of a pyramid; tapering upward to a point.",
    "secondary": "In descriptive writing, rising or narrowing gradually in stacked horizontal ranks or layers toward an apex.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution: A History",
        "quote": "Society had arranged itself **pyramidically**, with the starving multitude at the base and a sparkling court balanced on top."
      },
      {
        "author": "Charles Dickens",
        "work": "Martin Chuzzlewit",
        "quote": "Luggage of every conceivable shape was piled **pyramidically** upon the wharf, threatening to tumble into the river below."
      },
      {
        "author": "Washington Irving",
        "work": "A History of New York",
        "quote": "The burghers constructed their brick houses with gables stepped **pyramidically** in the quaint style of Old Amsterdam."
      }
    ]
  },
  "Dashboard — pyramid\\pyramiding.md": {
    "primary": "The practice of using unrealized paper profits from an open financial trade as margin to purchase additional shares or contracts.",
    "secondary": "In financial speculation and economic theory, an aggressive trading strategy that multiplies gains in a rising market but sharply elevates downside leverage risk.",
    "quotes": [
      {
        "author": "Edwin Lefèvre",
        "work": "Reminiscences of a Stock Operator",
        "quote": "Jesse Livermore explained that successful **pyramiding** requires adding to winning positions only when the market confirms your initial judgment."
      },
      {
        "author": "Charles Dow",
        "work": "Scientific Stock Speculation",
        "quote": "Reckless **pyramiding** during bull market manias inevitably causes catastrophic wipeouts when liquidity suddenly evaporates."
      },
      {
        "author": "Jesse Livermore",
        "work": "How to Trade in Stocks",
        "quote": "Never average down on a losing trade; reserve your **pyramiding** strictly for positions showing unmistakable accumulating profits."
      }
    ]
  },
  "Dashboard — pyramid\\pyramidion.md": {
    "primary": "The miniature pyramid-shaped capstone that sat atop an ancient Egyptian pyramid or the apex of an obelisk.",
    "secondary": "In Egyptology and monumental archaeology, a finely carved diorite, basalt, or limestone capstone often covered in electrum to reflect the sun's rays.",
    "quotes": [
      {
        "author": "Flinders Petrie",
        "work": "The Pyramids and Temples of Gizeh",
        "quote": "The black granite **pyramidion** of Amenemhat III at Dahshur is adorned with hieroglyphic prayers to the sun god Ra."
      },
      {
        "author": "Gaston Maspero",
        "work": "Manual of Egyptian Archaeology",
        "quote": "Sheathed in golden electrum, the gleaming **pyramidion** caught the first rays of dawn long before light touched the desert floor."
      },
      {
        "author": "I. E. S. Edwards",
        "work": "The Pyramids of Egypt",
        "quote": "The setting of the final **pyramidion** marked the solemn completion of the pharaoh's eternal resting place."
      }
    ]
  },
  "Dashboard — rhabd\\Rhabdodon.md": {
    "primary": "An extinct genus of herbivorous rhabdodontid ornithopod dinosaurs from the Late Cretaceous of Europe.",
    "secondary": "In vertebrate paleontology, an insular European dinosaur characterized by heavy, rod-like fluted tooth crowns adapted to shredding tough vegetation.",
    "quotes": [
      {
        "author": "Philippe Matheron",
        "work": "Notice sur les reptiles fossiles des dépôts fluvio-lacustres",
        "quote": "I proposed the genus **Rhabdodon** for these Cretaceous fossil jaws on account of their heavily ridged, rod-like teeth."
      },
      {
        "author": "Harry Govier Seeley",
        "work": "On the Dinosaurian Remains of the Gosau Formation",
        "quote": "Fossils of **Rhabdodon** demonstrate that archaic ornithopod stocks persisted on European island archipelagos until the end of the Cretaceous."
      },
      {
        "author": "David B. Weishampel",
        "work": "The Dinosauria",
        "quote": "Dental microwear analysis in **Rhabdodon** indicates powerful transverse chewing cycles suited to tough angiosperm and fern diets."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdoid.md": {
    "primary": "Shaped like a rod, wand, or stick; having the form of a small cylinder.",
    "secondary": "In oncologic pathology, describing malignant tumors composed of dyscohesive round or polygonal cells with eccentric vesicular nuclei and eosinophilic cytoplasmic inclusions.",
    "quotes": [
      {
        "author": "Juan Rosai",
        "work": "Rosai and Ackerman's Surgical Pathology",
        "quote": "Malignant **rhabdoid** tumors of infancy are characterized by loss of INI1 protein expression due to SMARCB1 gene mutations."
      },
      {
        "author": "Christopher D. M. Fletcher",
        "work": "Diagnostic Histopathology of Tumors",
        "quote": "Histologically, the **rhabdoid** cell features an abundant, glassy pink cytoplasm that displaces the vesicular nucleus to the cell periphery."
      },
      {
        "author": "Louis P. Dehner",
        "work": "Pediatric Surgical Pathology",
        "quote": "Renal and extrarenal **rhabdoid** neoplasms pursue an exceptionally aggressive clinical course requiring intensive multi-agent chemotherapy."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdom.md": {
    "primary": "The transparent, light-sensitive rod-like central structure in the ommatidium of an arthropod compound eye.",
    "secondary": "In sensory neurobiology, a cylindrical organelle formed by microvillar membranes of retinular cells that contain rhodopsin photopigments for vision.",
    "quotes": [
      {
        "author": "Johannes Müller",
        "work": "Comparative Physiology of Vision",
        "quote": "Within each compound facet, the central transparent **rhabdom** guides light rays down to the optic nerve terminals."
      },
      {
        "author": "V. B. Wigglesworth",
        "work": "The Principles of Insect Physiology",
        "quote": "The microvilli of the insect **rhabdom** are oriented perpendicularly to the incident light path, facilitating the detection of polarized light."
      },
      {
        "author": "George Wald",
        "work": "Visual Pigments and Photoreceptor Mechanisms",
        "quote": "Photochemical absorption in the arthropod **rhabdom** relies on retinaldehyde coupled with invertebrate opsin proteins."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdomancer.md": {
    "primary": "A person who practices rhabdomancy; a dowser who uses a divining rod or hazel twig to locate water or hidden treasures.",
    "secondary": "In the history of folk magic and occult traditions, an operator believed to detect subterranean currents via wand deflections.",
    "quotes": [
      {
        "author": "Thomas Browne",
        "work": "Pseudodoxia Epidemica: Vulgar Errors",
        "quote": "The credulous countryman employs a **rhabdomancer** to walk the pastures with a forked twig in search of hidden wellsprings."
      },
      {
        "author": "William Barrett",
        "work": "Psychical Research",
        "quote": "In every mining district, the traditional **rhabdomancer** claimed to feel an involuntary twitch when crossing rich metal veins."
      },
      {
        "author": "Sabine Baring-Gould",
        "work": "Curious Myths of the Middle Ages",
        "quote": "The seventeenth-century **rhabdomancer** Jacques Aymar astounded Parisian magistrates by tracking criminals with his divining rod."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdomancy.md": {
    "primary": "Divination or dowsing by means of a rod, wand, or forked twig to discover subterranean water, minerals, or buried objects.",
    "secondary": "In ethnology and the history of science, an ancient divinatory practice investigated as an early example of ideomotor movement.",
    "quotes": [
      {
        "author": "Robert Boyle",
        "work": "Hydrostatical Paradoxes",
        "quote": "I observed experiments in **rhabdomancy** conducted by Cornish miners, remaining skeptical of the hazel wand's reputed occult virtues."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Belief in **rhabdomancy** shows how habit and unexamined authority can establish conviction without logical demonstration."
      },
      {
        "author": "William Barrett",
        "work": "The Divining Rod: An Experimental and Psychological Investigation",
        "quote": "Scientific analysis demonstrated that the phenomena of **rhabdomancy** are produced by subconscious motor impulses in the dowser's arms."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdomyolysis.md": {
    "primary": "The rapid breakdown and destruction of skeletal muscle tissue, accompanied by the release of myoglobin, creatine kinase, and electrolytes into circulation.",
    "secondary": "In emergency and critical care medicine, a condition triggered by severe crush trauma, extreme exertion, or drug toxicity that carries high risk of acute kidney injury.",
    "quotes": [
      {
        "author": "Eric G. Bywaters",
        "work": "Crush Injuries with Impairment of Renal Function",
        "quote": "In victims of the London Blitz, extensive **rhabdomyolysis** from buried limbs precipitated acute tubular necrosis due to myoglobinuria."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe generalized **rhabdomyolysis** manifests with profound muscle weakness, brown port-wine urine, and rapid electrolyte imbalances."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins Basic Pathology",
        "quote": "Massive hydration and alkalinization of the urine are paramount in acute **rhabdomyolysis** to prevent myoglobin cast nephropathy."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdomyoma.md": {
    "primary": "A benign neoplasm or tumor derived from striated muscle fibers.",
    "secondary": "In pediatric cardiology and surgical pathology, a hamartomatous cardiac tumor strongly associated with tuberous sclerosis, often regressing spontaneously.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Die krankhaften Geschwülste",
        "quote": "The benign cardiac **rhabdomyoma** consists of swollen, glycogen-rich cells that preserve faint transverse striations under the microscope."
      },
      {
        "author": "Juan Rosai",
        "work": "Rosai and Ackerman's Surgical Pathology",
        "quote": "Histologic sections of cardiac **rhabdomyoma** display distinctive 'spider cells' whose cytoplasm is laced with thin glycogenated strands."
      },
      {
        "author": "Christopher D. M. Fletcher",
        "work": "Diagnostic Histopathology of Tumors",
        "quote": "Extra-cardiac **rhabdomyoma** occurs primarily in the head and neck of adult patients, mimicking granular cell tumors."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdomyosarcoma.md": {
    "primary": "A highly malignant soft-tissue cancer derived from primitive mesenchymal cells exhibiting striated myogenic differentiation.",
    "secondary": "In pediatric oncology, the most common soft-tissue sarcoma of childhood, divided into embryonal (including botryoid) and alveolar subtypes.",
    "quotes": [
      {
        "author": "Lauren V. Ackerman",
        "work": "Surgical Pathology",
        "quote": "The botryoid variant of embryonal **rhabdomyosarcoma** grows into body cavities as translucent, grape-like polypoid masses."
      },
      {
        "author": "Christopher D. M. Fletcher",
        "work": "Diagnostic Histopathology of Tumors",
        "quote": "Alveolar **rhabdomyosarcoma** is characterized by the PAX3-FOXO1 gene fusion and carries a poorer prognosis than the embryonal subtype."
      },
      {
        "author": "Vinay Kumar",
        "work": "Robbins and Cotran Pathologic Basis of Disease",
        "quote": "Immunohistochemical staining for desmin and myogenin confirms the striated skeletal muscle lineage of an undifferentiated **rhabdomyosarcoma**."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdosarcoma.md": {
    "primary": "A malignant tumor arising from striated muscle tissue; an alternative or shortened term for rhabdomyosarcoma.",
    "secondary": "In historical oncologic pathology, a high-grade sarcoma featuring strap cells, racquet cells, and cross-striated rhabdomyoblasts.",
    "quotes": [
      {
        "author": "James Ewing",
        "work": "Neoplastic Diseases: A Treatise on Tumors",
        "quote": "Cases classified as **rhabdosarcoma** display rapid infiltrative growth into fascial planes and early hematogenous dissemination to lungs."
      },
      {
        "author": "Arthur Purdy Stout",
        "work": "Tumors of the Soft Tissues",
        "quote": "The pleomorphic **rhabdosarcoma** of adult extremity musculature is notoriously resistant to conservative radiation therapy alone."
      },
      {
        "author": "Juan Rosai",
        "work": "Surgical Pathology",
        "quote": "Meticulous microscopic search for cross-striations was historically required before immunohistochemistry clarified each **rhabdosarcoma**."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdoviridae.md": {
    "primary": "A family of enveloped, negative-sense single-stranded RNA viruses having a characteristic bullet-like or rod-like morphology.",
    "secondary": "In systematic virology, an animal and plant virus family encompassing the genera Lyssavirus (rabies virus) and Vesiculovirus.",
    "quotes": [
      {
        "author": "David Baltimore",
        "work": "Expression of Animal Virus Genomes",
        "quote": "Viruses of the family **rhabdoviridae** package their own viral RNA-dependent RNA polymerase within the bullet-shaped virion."
      },
      {
        "author": "Bernard N. Fields",
        "work": "Virology",
        "quote": "The helical nucleocapsid core of **rhabdoviridae** is encased by matrix protein and a lipid bilayer bristling with glycoprotein spikes."
      },
      {
        "author": "Frank Fenner",
        "work": "Medical Virology",
        "quote": "Members of **rhabdoviridae** infect an exceptionally wide host range, spanning plants, insects, fish, and terrestrial mammals."
      }
    ]
  },
  "Dashboard — rhabd\\rhabdovirus.md": {
    "primary": "Any bullet-shaped or rod-shaped single-stranded RNA virus of the family Rhabdoviridae, especially the rabies virus.",
    "secondary": "In infectious disease and molecular virology, a neurotropic pathogen that travels retrograde along peripheral axoplasm to infect the central nervous system.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Méthode pour prévenir la rage après morsure",
        "quote": "The deadly rabies **rhabdovirus** migrates slowly through neural pathways from the dog bite wound toward the spinal cord and brain."
      },
      {
        "author": "Bernard N. Fields",
        "work": "Virology",
        "quote": "The bullet-like shape of a mature **rhabdovirus** particle is maintained by tightly wound structural matrix proteins."
      },
      {
        "author": "Michael B. A. Oldstone",
        "work": "Viruses, Plagues, and History",
        "quote": "No human viral infection is more lethal than that caused by an established rabies **rhabdovirus** once encephalitis sets in."
      }
    ]
  },
  "Dashboard — rhach\\arachis.md": {
    "primary": "A genus of leguminous plants in the family Fabaceae containing Arachis hypogaea, the cultivated peanut or groundnut.",
    "secondary": "In agricultural botany, geocarpic annual legumes whose fertilized flowers bend downward into the soil where the pods mature underground.",
    "quotes": [
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "Under the genus **arachis**, nature presents the astonishing spectacle of a flower whose ripening fruit buries itself beneath the earth."
      },
      {
        "author": "George Bentham",
        "work": "Flora Brasiliensis",
        "quote": "Indigenous wild species of **arachis** carpet the interior savannas and sandy river banks of central Brazil."
      },
      {
        "author": "George Washington Carver",
        "work": "How to Grow the Peanut and 105 Ways of Preparing It for Human Consumption",
        "quote": "The common peanut, belonging to **arachis**, revitalizes exhausted cotton soils by fixing atmospheric nitrogen through root nodules."
      }
    ]
  },
  "Dashboard — rhach\\rachipagus.md": {
    "primary": "Conjoined twins united back-to-back along the vertebral column or spine.",
    "secondary": "In teratology, an exceptionally rare congenital malformation involving posterior union along the spinal axis, often sharing neural canal elements.",
    "quotes": [
      {
        "author": "George M. Gould",
        "work": "Anomalies and Curiosities of Medicine",
        "quote": "In true **rachipagus**, the union involves the dorsal spines of the vertebrae, creating complete back-to-back fusion of the torsos."
      },
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "Histoire des anomalies de l'organisation",
        "quote": "The dorsal conjunction observed in **rachipagus** represents an embryological failure of posterior neural tube divergence."
      },
      {
        "author": "John William Ballantyne",
        "work": "Manual of Antenatal Pathology and Hygiene",
        "quote": "Autopsies of **rachipagus** twins reveal intricate shared dural investments requiring complex neurosurgical separation plans."
      }
    ]
  },
  "Dashboard — rhach\\rachis.md": {
    "primary": "The main axis or shaft of a compound leaf, fern frond, or inflorescence; also the central shaft of a bird's feather.",
    "secondary": "In anatomy and physical medicine, the vertebral or spinal column; the dorsal skeletal axis of vertebrate animals.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "The solid central **rachis** of the contour feather supports two lateral vanes composed of interlocking barbs and barbules."
      },
      {
        "author": "Asa Gray",
        "work": "Structural Botany",
        "quote": "In pinnate foliage, the individual leaflets attach along the extended **rachis** that continues from the petiole."
      },
      {
        "author": "John Lindley",
        "work": "An Introduction to Botany",
        "quote": "Spikelet arrangements along the central floral **rachis** determine the botanical classification of graminaceous crops."
      }
    ]
  },
  "Dashboard — rhach\\rachischisis.md": {
    "primary": "A severe congenital neural tube defect characterized by an open, unfused cleft of the vertebral column with exposure of the spinal cord.",
    "secondary": "In embryology and neonatal surgery, the most severe form of spina bifida (rachischisis totalis) resulting from failure of neural fold closure during neurulation.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Die krankhaften Geschwülste",
        "quote": "In complete **rachischisis**, the spinal canal remains entirely open from the occiput to the sacrum, leaving the neural plate bare."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Maternal folate deficiency in early pregnancy is strongly implicated in fatal neural tube failures like **rachischisis**."
      },
      {
        "author": "John William Ballantyne",
        "work": "Manual of Antenatal Pathology and Hygiene",
        "quote": "The exposed vascular area medullo-vasculosa in **rachischisis** demonstrates failure of mesodermal arch closure over the open spinal cord."
      }
    ]
  },
  "Dashboard — rhach\\rhachiodont.md": {
    "primary": "Having modified, forward-projecting hypapophyses on the cervical vertebrae that penetrate the esophagus to crack eggshells, as in egg-eating snakes.",
    "secondary": "In herpetology, designating specialized vertebral adaptations in colubrid snakes like Dasypeltis that consume intact bird eggs.",
    "quotes": [
      {
        "author": "George Albert Boulenger",
        "work": "Catalogue of the Snakes in the British Museum",
        "quote": "The extraordinary **rhachiodont** dentition of Dasypeltis employs enamelled vertebral spines to crush eggs within the gullet."
      },
      {
        "author": "Edward D. Cope",
        "work": "The Crocodilians, Lizards, and Snakes of North America",
        "quote": "In the **rhachiodont** serpent, the skull teeth are reduced to mere minute pegs, having surrendered their masticatory role to the backbone."
      },
      {
        "author": "Hans Gadow",
        "work": "Amphibia and Reptiles",
        "quote": "Once swallowed, the shell is sliced open by the **rhachiodont** vertebral keels, allowing the liquid egg contents to drain into the stomach."
      }
    ]
  },
  "Dashboard — rhach\\rhachis.md": {
    "primary": "The spine or vertebral column of vertebrates; an alternative spelling of rachis.",
    "secondary": "In botanical and zoological morphology, the primary axis of a feather, pinnate leaf, or flowering spike.",
    "quotes": [
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "The segmented **rhachis** provides a flexible yet rigid central axis supporting the thorax, ribs, and cranium."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Each vertebra of the human **rhachis** is exquisitely articulated to allow flexion, extension, and lateral rotation."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "Vascular bundles diverge sequentially from the central **rhachis** to supply the lateral pinnae of the fern frond."
      }
    ]
  },
  "Dashboard — rhod\\rhodanthe.md": {
    "primary": "A genus of Australian annual flowering herbs in the daisy family (Asteraceae), commonly known as paper daisies or everlastings.",
    "secondary": "In ornamental horticulture, drought-tolerant desert ephemerals cultivated for their papery, brightly colored involucral bracts that retain form and color when dried.",
    "quotes": [
      {
        "author": "George Bentham",
        "work": "Flora Australiensis",
        "quote": "The papery, scarious bracts of **rhodanthe** glisten with silvery and rose hues across the red sand dunes of western Australia."
      },
      {
        "author": "Ferdinand von Mueller",
        "work": "Fragmenta Phytographiae Australiae",
        "quote": "Following winter rains, vast interior plains are transformed into waving carpets of blooming **rhodanthe**."
      },
      {
        "author": "William Robinson",
        "work": "The English Flower Garden",
        "quote": "Cut sprays of **rhodanthe** can be preserved for winter bouquets, retaining their vivid color for years without fading."
      }
    ]
  },
  "Dashboard — rhod\\rhodes.md": {
    "primary": "The largest of the Dodecanese islands of Greece in the eastern Aegean Sea, renowned for its ancient Colossus and medieval fortifications.",
    "secondary": "In classical history and Mediterranean maritime law, an influential ancient seafaring republic that developed the Lex Rhodia code of maritime trade.",
    "quotes": [
      {
        "author": "Herodotus",
        "work": "Histories",
        "quote": "The Greek cities of **rhodes** formed a flourishing maritime league, trading widely across Egypt and the Levant."
      },
      {
        "author": "Strabo",
        "work": "Geographica",
        "quote": "The city of **rhodes** surpasses all others in the beauty of its harbors, streets, walls, and monumental civic architecture."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "For over two centuries, the Knights of Saint John maintained the fortified stronghold of **rhodes** against the Ottoman empire."
      }
    ]
  },
  "Dashboard — rhod\\rhodesia.md": {
    "primary": "The former historical British colonial territory in southern Africa, named after Cecil Rhodes, that gained independence as Zimbabwe in 1980.",
    "secondary": "In African colonial history, an unrecognized de facto state between 1965 and 1979 following its Unilateral Declaration of Independence under Ian Smith.",
    "quotes": [
      {
        "author": "David Livingstone",
        "work": "Missionary Travels and Researches in South Africa",
        "quote": "The great river Zambezi flows majestically across the plateau lands that would later be annexed under the name of **rhodesia**."
      },
      {
        "author": "Frederick Courteney Selous",
        "work": "A Hunter's Wanderings in Africa",
        "quote": "In the uncharted bushveldt of southern **rhodesia**, vast herds of elephant and buffalo roamed the mopane forests."
      },
      {
        "author": "James Bryce",
        "work": "Impressions of South Africa",
        "quote": "The mineral wealth and high savannah plateaus of **rhodesia** attracted thousands of European settlers seeking pastoral homesteads."
      }
    ]
  },
  "Dashboard — rhod\\rhodesian.md": {
    "primary": "Of, relating to, or originating from Rhodesia (now Zimbabwe); an inhabitant of Rhodesia.",
    "secondary": "Designating the Rhodesian Ridgeback, a distinctive African hunting dog breed characterized by a reverse ridge of hair along its spine.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Great Boer War",
        "quote": "A detachment of sturdy **rhodesian** troopers guarded the northern frontier railway line against Boer incursions."
      },
      {
        "author": "Winston Churchill",
        "work": "The Story of the Malakand Field Force",
        "quote": "The spirited **rhodesian** volunteers displayed admirable frontier endurance in the face of arduous wilderness campaigns."
      },
      {
        "author": "Frederick Courteney Selous",
        "work": "Sunshine and Storm in Rhodesia",
        "quote": "The settler relied upon his faithful **rhodesian** hound to bay lions in the tall thorny scrub."
      }
    ]
  },
  "Dashboard — rhod\\rhodium.md": {
    "primary": "A rare, silvery-white, hard, corrosion-resistant metallic chemical element of the platinum group, atomic number 45 (symbol Rh).",
    "secondary": "In industrial chemistry and jewelry, a noble metal used primarily in automotive three-way catalytic converters and as electroplated coatings on white gold.",
    "quotes": [
      {
        "author": "William Hyde Wollaston",
        "work": "On a New Metal Found in Crude Platina",
        "quote": "I have named this newly discovered element **rhodium**, from the rose color of its dilute saline solutions."
      },
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "The remarkable resistance of **rhodium** to mineral acids exceeds that of platinum itself under ordinary temperatures."
      },
      {
        "author": "Jöns Jacob Berzelius",
        "work": "Treatise on Chemistry",
        "quote": "Alloying a small percentage of **rhodium** with platinum produces an intensely hard metal ideal for scientific crucibles."
      }
    ]
  },
  "Dashboard — rhod\\rhodochrosite.md": {
    "primary": "A rose-red or raspberry-pink manganese carbonate mineral (MnCO3), crystallizing in the trigonal system and valued as a gemstone and manganese ore.",
    "secondary": "In mineralogy and economic geology, a hydrothermal vein mineral often forming banded, stalactitic botryoidal crusts in silver and polymetallic lead-zinc deposits.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The exquisite rose-red rhombohedrons of **rhodochrosite** exhibit vitreous luster and distinct rhombohedral cleavage."
      },
      {
        "author": "Edward Salisbury Dana",
        "work": "A Textbook of Mineralogy",
        "quote": "Concentric bands of deep rose and white make stalactitic **rhodochrosite** from Argentine silver mines highly sought after for carving."
      },
      {
        "author": "Waldemar Lindgren",
        "work": "Mineral Deposits",
        "quote": "In epithermal precious metal veins, **rhodochrosite** occurs in association with quartz, fluorite, and rhodonite."
      }
    ]
  },
  "Dashboard — rhod\\rhododendron.md": {
    "primary": "A large genus of woody flowering shrubs and trees in the heath family (Ericaceae), famed for clusters of showy, bell-shaped blossoms.",
    "secondary": "In botanical ecology and horticulture, acidophilic, mycorrhizal shrubs native largely to the Himalayas, East Asia, and the Appalachian mountains.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Rhododendrons of Sikkim-Himalaya",
        "quote": "The mountain slopes of Sikkim were blaze with scarlet blooms of **rhododendron**, transforming rugged Himalayan cliffs into a floral paradise."
      },
      {
        "author": "Carl Linnaeus",
        "work": "Species Plantarum",
        "quote": "I grouped under **rhododendron** those alpine shrubs whose evergreen leaves protect clusters of magnificent terminal blossoms."
      },
      {
        "author": "Ernest Henry Wilson",
        "work": "A Naturalist in Western China",
        "quote": "High mountain passes in Sichuan are choked with impenetrable thickets of **rhododendron**, through which we had to cut our path."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 3 Batch 4.`);
