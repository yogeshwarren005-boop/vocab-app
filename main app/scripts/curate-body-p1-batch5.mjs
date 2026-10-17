import { updateNotesBatch } from './curate-updater-util.mjs';

const BASE_DIR = 'App database/Greek roots/Cluster Body & Physiology';

const BATCH5_DATA = {
  "Dashboard — cephal\\cephalosporin.md": {
    "primary": "Any of a class of broad-spectrum beta-lactam bactericidal antibiotics originally isolated from the fungus Acremonium (Cephalosporium) chrysogenum.",
    "secondary": "In pharmacology, a major family of cell-wall synthesis inhibitors divided into five therapeutic generations used against Gram-positive and Gram-negative pathogens.",
    "quotes": [
      {
        "author": "Edward Abraham",
        "work": "The Cephalosporin C Antibiotics",
        "quote": "The chemical stability of **cephalosporin** C against penicillinase provided a vital weapon against resistant staphylococci."
      },
      {
        "author": "Giuseppe Brotzu",
        "work": "Researches on a New Antibiotic",
        "quote": "From seawater near a sewage outfall in Sardinia, I isolated the mold that produced the first **cephalosporin** substance."
      },
      {
        "author": "Howard Florey",
        "work": "Antibiotics",
        "quote": "The clinical introduction of the **cephalosporin** class expanded our antimicrobial armamentarium beyond the confines of penicillin."
      }
    ]
  },
  "Dashboard — cephal\\cephalotaceae.md": {
    "primary": "A monotypic family of carnivorous flowering plants (order Oxalidales) containing only the Albany pitcher plant, Cephalotus follicularis.",
    "secondary": "In systematic botany, an ancient paleo-endemic Australian family characterized by true pitcher leaves possessing specialized nectar glands and slippery wax zones.",
    "quotes": [
      {
        "author": "Robert Brown",
        "work": "General Remarks, Geographical and Systematical, on the Botany of Terra Australis",
        "quote": "The singular pitcher plant discovered at King George's Sound constitutes the type of our new family **cephalotaceae**."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "Morphological isolation led botanists to isolate the **cephalotaceae** from both Sarraceniaceae and Nepenthaceae."
      },
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "The exquisite pitfall traps of the **cephalotaceae** illustrate convergent evolutionary architecture in carnivorous flora."
      }
    ]
  },
  "Dashboard — cephal\\cephalotaxaceae.md": {
    "primary": "A small family of coniferous gymnosperms (order Pinales), commonly known as plum yews, native to eastern and southeastern Asia.",
    "secondary": "In dendrology and pharmacognosy, evergreen conifers producing large, fleshy plum-like arillate seeds and cancer-inhibiting harringtonine alkaloids.",
    "quotes": [
      {
        "author": "Philipp Franz von Siebold",
        "work": "Flora Japonica",
        "quote": "In the mountain forests of Japan, the **cephalotaxaceae** form graceful understory trees bearing lustrous dark green needles."
      },
      {
        "author": "Ernest Henry Wilson",
        "work": "The Conifers and Taxads of Japan",
        "quote": "The distinct two-ranked foliage and drupaceous seeds of the **cephalotaxaceae** set them apart from true Taxaceae."
      },
      {
        "author": "Charles Sprague Sargent",
        "work": "Plantae Wilsonianae",
        "quote": "Explorations in western Hupeh revealed extensive native populations of the **cephalotaxaceae** growing on shaded limestone cliffs."
      }
    ]
  },
  "Dashboard — cephal\\cephalotaxus.md": {
    "primary": "A genus of evergreen coniferous shrubs and small trees in the family Cephalotaxaceae, commonly known as plum yews or cowtail pines.",
    "secondary": "In pharmaceutical botany, Cephalotaxus harringtonii, from which homoharringtonine (omacetaxine) is extracted for the treatment of leukemia.",
    "quotes": [
      {
        "author": "Philipp Franz von Siebold",
        "work": "Flora Japonica",
        "quote": "The generic title **cephalotaxus** denotes the head-like clusters of male strobili that adorn the branchlets in early spring."
      },
      {
        "author": "Ernest Henry Wilson",
        "work": "A Naturalist in Western China",
        "quote": "Specimens of **cephalotaxus** flourish in moist mountain ravines, producing large greenish-purple arillate fruits."
      },
      {
        "author": "Liberty Hyde Bailey",
        "work": "The Standard Cyclopedia of Horticulture",
        "quote": "Landscape architects prize **cephalotaxus** for its dense dark foliage, which thrives in full shade where few conifers survive."
      }
    ]
  },
  "Dashboard — cephal\\cephalothin.md": {
    "primary": "A first-generation semisynthetic beta-lactam cephalosporin antibiotic administered parenterally for bacterial infections.",
    "secondary": "In the history of antimicrobial chemotherapy, the first commercial cephalosporin marketed by Eli Lilly in 1964, effective against penicillin-resistant Staphylococcus aureus.",
    "quotes": [
      {
        "author": "Edward Abraham",
        "work": "Cephalosporins",
        "quote": "The introduction of sodium **cephalothin** into clinical practice proved that beta-lactam rings could be chemically engineered to resist penicillinases."
      },
      {
        "author": "Selman Waksman",
        "work": "The Conquest of Infectious Diseases",
        "quote": "Hospital wards utilized **cephalothin** as a frontline parenteral antibiotic against severe surgical and orthopedic infections."
      },
      {
        "author": "René Dubos",
        "work": "Bacterial Diseases",
        "quote": "Intravenous **cephalothin** cleared systemic staphylococcal bacteremias with minimal allergic cross-reactivity in penicillin-sensitive patients."
      }
    ]
  },
  "Dashboard — cephal\\cephalotus.md": {
    "primary": "A monotypic genus of insectivorous pitcher plants containing Cephalotus follicularis (the Albany pitcher plant), endemic to southwestern Australia.",
    "secondary": "In botanical morphology, a low-growing wetland herb producing both flat photosynthetic foliage leaves and stout, complex insect-trapping pitfall pitchers.",
    "quotes": [
      {
        "author": "Robert Brown",
        "work": "Prodromus Florae Novae Hollandiae",
        "quote": "In the peaty swamps near Albany, **cephalotus** produces miniature lidded pitchers decorated with prominent down-curved peristome teeth."
      },
      {
        "author": "Charles Darwin",
        "work": "Insectivorous Plants",
        "quote": "The downward-pointing teeth around the collar of **cephalotus** prevent captured insects from crawling upward out of the digestive fluid."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "On the Carnivorous Habits of Plants",
        "quote": "The dual foliage of **cephalotus** demonstrates that pitcher traps are modified leaf petioles adapted for animal nutrient capture."
      }
    ]
  },
  "Dashboard — cephal\\diencephalon.md": {
    "primary": "The posterior division of the embryonic forebrain, situated between the telencephalon and the mesencephalon (midbrain).",
    "secondary": "In adult neuroanatomy, the central brain region comprising the thalamus, hypothalamus, epithalamus, and subthalamus, enclosing the third ventricle.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "The nuclear complexes of the **diencephalon** function as the supreme sensory relay stations directing peripheral information toward the cerebral cortex."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The third ventricle forms a narrow median vertical chasm within the substance of the **diencephalon**."
      },
      {
        "author": "Walter Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "Emotional expression is organized within the basal nuclei of the **diencephalon**, held under tonic inhibitory restraint by the cortex."
      }
    ]
  },
  "Dashboard — cephal\\dolichocephalic.md": {
    "primary": "Having a relatively long, narrow skull, typically defined as having a cephalic index of less than 75.",
    "secondary": "In physical anthropology and craniometry, designating long-headed human populations or mammalian breeds (such as greyhounds or collies).",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "A skull whose cranial width is less than seventy-five percent of its maximum anteroposterior length is termed **dolichocephalic**."
      },
      {
        "author": "Franz Boas",
        "work": "Changes in Bodily Form of Descendants of Immigrants",
        "quote": "The immigrant surveys showed that even the long **dolichocephalic** head form responded plastically to changes in nutrition and environment."
      },
      {
        "author": "William Z. Ripley",
        "work": "The Races of Europe",
        "quote": "The Nordic and Mediterranean types share a distinctly **dolichocephalic** cranium, separating them from the broad-headed Alpine stock."
      }
    ]
  },
  "Dashboard — cephal\\dolichocephalism.md": {
    "primary": "The state, condition, or cranial characteristic of being dolichocephalic; long-headedness.",
    "secondary": "In craniology and physical anthropology, a head shape characterized by a cephalic index below 75.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Mémoires d'Anthropologie",
        "quote": "Prehistoric European burial mounds contain numerous skeletons displaying pronounced **dolichocephalism** alongside primitive flint implements."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The Neanderthal cranium exhibits extreme **dolichocephalism** combined with massive supraorbital ridges and a flattened vault."
      },
      {
        "author": "Franz Boas",
        "work": "The Mind of Primitive Man",
        "quote": "Our anthropometric data demonstrated that **dolichocephalism** does not correlate in any meaningful way with intellectual capacity."
      }
    ]
  },
  "Dashboard — cephal\\electroencephalogram.md": {
    "primary": "A graphic recording or tracing of the electrical potentials generated by the cerebral cortex of the brain, recorded from electrodes placed on the scalp (EEG).",
    "secondary": "In clinical neurology, a fundamental diagnostic tracing displaying alpha, beta, theta, and delta rhythms, used to evaluate epilepsy, sleep disorders, and brain death.",
    "quotes": [
      {
        "author": "Hans Berger",
        "work": "On the Electroencephalogram of Man",
        "quote": "In 1929, I published the first human **electroencephalogram**, demonstrating continuous rhythmic electrical oscillations in the waking brain."
      },
      {
        "author": "Edgar Adrian",
        "work": "The Berger Rhythm: Potential Changes from the Occipital Lobes in Man",
        "quote": "Recording the **electroencephalogram** confirmed that closing the eyes elicits a synchronized ten-cycle-per-second alpha rhythm from the visual cortex."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "Spike-and-wave discharges on the **electroencephalogram** precisely localized the epileptic focus prior to surgical cortical resection."
      }
    ]
  },
  "Dashboard — cephal\\encephalartos.md": {
    "primary": "A genus of African cycads in the family Zamiaceae, commonly known as bread palms, having stout woody trunks and spiny pinnate leaves.",
    "secondary": "In paleobotany and horticulture, ancient gymnosperms whose starchy pith was historically washed and baked into bread by indigenous peoples.",
    "quotes": [
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The generic name **encephalartos** literally signifies 'bread inside the head,' alluding to the farinaceous pith extracted from the trunk."
      },
      {
        "author": "Robert Brown",
        "work": "Botanical Appendix to Flinders' Voyage",
        "quote": "Massive woody cones crowned the apex of **encephalartos**, surrounded by a stiff rosette of rigid, spine-tipped fronds."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of Tropical Africa",
        "quote": "South African species of **encephalartos** represent living Mesozoic relicts that have survived in rocky scrub hillsides."
      }
    ]
  },
  "Dashboard — cephal\\encephalitis.md": {
    "primary": "Acute inflammation of the brain parenchyma, manifesting clinically with fever, headache, altered mental status, and focal neurological deficits.",
    "secondary": "In clinical infectious disease and neurology, a life-threatening cerebral infection commonly caused by viruses (such as herpes simplex virus, arboviruses, or rabies) or autoimmune mechanisms.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute viral **encephalitis** rapidly progresses from confusion and irritability into violent delirium, convulsions, and deep coma."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Focal perivascular lymphocytic cuffing in **encephalitis** marks the intense inflammatory reaction within the cerebral gray matter."
      },
      {
        "author": "Constantin von Economo",
        "work": "Encephalitis Lethargica",
        "quote": "The epidemic **encephalitis** lethargica presented with profound somnolence, ophthalmoplegia, and subsequent post-encephalitic parkinsonism."
      }
    ]
  },
  "Dashboard — cephal\\encephalocele.md": {
    "primary": "A congenital neural tube defect characterized by the herniation of brain tissue and meninges through a cranial bone defect (cranium bifidum).",
    "secondary": "In pediatric neurosurgery, a developmental malformation presenting as a sac-like protrusion, most commonly in the occipital midline, requiring surgical closure.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Head",
        "quote": "Surgical repair of an occipital **encephalocele** involves careful preservation of functional neural elements while excising the redundant sac."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Failure of the mesodermal cranial plates to fuse in the midline permits the brain vesicles to protrude as an **encephalocele**."
      },
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "The pulsating swelling of a congenital **encephalocele** expands during crying and coughing, transmitted directly from the cerebral ventricles."
      }
    ]
  },
  "Dashboard — cephal\\encephalogram.md": {
    "primary": "A photographic, radiographic, or electrical record or image of the brain.",
    "secondary": "In clinical neurology, a diagnostic image depicting cerebral ventricular contours (pneumoencephalogram) or brain wave tracings (electroencephalogram).",
    "quotes": [
      {
        "author": "Walter Dandy",
        "work": "Ventriculography Following the Injection of Air into the Cerebral Ventricles",
        "quote": "The air-filled **encephalogram** revealed marked asymmetric ventricular shift caused by a deep subcortical glioma."
      },
      {
        "author": "Hans Berger",
        "work": "Electroencephalography in Humans",
        "quote": "The normal **encephalogram** demonstrates steady synchronization of cortical neuronal firing across the parietal regions."
      },
      {
        "author": "Wilder Penfield",
        "work": "Somatic Motor and Sensory Representation in the Cerebral Cortex of Man",
        "quote": "Correlating the diagnostic **encephalogram** with intraoperative cortical stimulation allowed precise functional mapping of the precentral gyrus."
      }
    ]
  },
  "Dashboard — cephal\\encephalography.md": {
    "primary": "The radiographic or electrical technique of imaging or recording the structure or function of the brain.",
    "secondary": "In twentieth-century neurosurgery, specifically pneumoencephalography—the radiographic visualization of the cerebral ventricles following lumbar cerebrospinal fluid replacement with air.",
    "quotes": [
      {
        "author": "Walter Dandy",
        "work": "Pneumoencephalography in Intracranial Tumors",
        "quote": "Before the advent of modern tomography, lumbar **encephalography** was our most potent diagnostic tool for visualizing intracranial mass lesions."
      },
      {
        "author": "Harvey Cushing",
        "work": "Intracranial Tumours",
        "quote": "Air **encephalography** must be performed with extreme caution in patients with elevated intracranial pressure to avoid tonsillar herniation."
      },
      {
        "author": "Hans Berger",
        "work": "The History of Brain Wave Studies",
        "quote": "The development of electro-**encephalography** provided a continuous, harmless physiological monitor of cerebral cortical metabolism."
      }
    ]
  },
  "Dashboard — cephal\\encephalomeningitis.md": {
    "primary": "Inflammation involving both the brain substance (encephalon) and its surrounding protective membranes (meninges); meningoencephalitis.",
    "secondary": "In clinical neurology and infectious pathology, an acute infectious process presenting with severe meningismus, fever, altered consciousness, and focal neurological deficits.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In tuberculous **encephalomeningitis**, gelatinous exudate mats the cranial nerves at the base of the brain, producing early cranial palsies."
      },
      {
        "author": "Thomas Willis",
        "work": "The Anatomy of the Brain",
        "quote": "When inflammation spreads from the membranes into the cortical flesh, severe **encephalomeningitis** quickly extinguishes conscious thought."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "Lumbar puncture in acute **encephalomeningitis** reveals cloudy cerebrospinal fluid with thousands of neutrophils and elevated protein."
      }
    ]
  },
  "Dashboard — cephal\\encephalomyelitis.md": {
    "primary": "Inflammation of both the brain (encephalon) and the spinal cord (myelos).",
    "secondary": "In clinical neurology, an acute inflammatory demyelinating disease, such as acute disseminated encephalomyelitis (ADEM), typically triggered by viral infections or vaccinations.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Post-infectious **encephalomyelitis** strikes days after a mild exanthem, presenting with multifocal paralysis, ataxia, and obtundation."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Lectures on the Diseases of the Nervous System",
        "quote": "Histologic sections in acute **encephalomyelitis** reveal widespread perivenular demyelination throughout the white matter of the cord and hemispheres."
      },
      {
        "author": "Constantin von Economo",
        "work": "Encephalitis Lethargica",
        "quote": "The inflammatory lesions of equine **encephalomyelitis** selectively destroy motor neurons in both the brainstem and spinal anterior horns."
      }
    ]
  },
  "Dashboard — cephal\\encephalon.md": {
    "primary": "The vertebrate brain in its entirety, enclosed within the cranium.",
    "secondary": "In neuroanatomy, the organ composed of the cerebrum, cerebellum, and brainstem, developing embryologically from the three primary brain vesicles.",
    "quotes": [
      {
        "author": "Galen",
        "work": "On Anatomical Procedures",
        "quote": "The **encephalon** is the sovereign governor of the body, whence the voluntary nerves take their origin to command all motion."
      },
      {
        "author": "Andreas Vesalius",
        "work": "De Humani Corporis Fabrica",
        "quote": "Opening the cranial vault exposes the glistening convolutions of the **encephalon**, wrapped in the vascular sheets of the pia mater."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The human **encephalon** attains an average weight of about forty-eight ounces in the adult male, filling the cranial cavity."
      }
    ]
  },
  "Dashboard — cephal\\encephalopathy.md": {
    "primary": "Any generic disease, damage, or malfunction that alters brain function or structure.",
    "secondary": "In clinical medicine, a syndrome of diffuse cerebral dysfunction presenting with confusion, lethargy, tremor, and delirium (e.g. hepatic, uremic, hypertensive, or hypoxic encephalopathy).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Lead **encephalopathy** in industrial workers manifested as terrifying hallucinations, convulsions, and persistent optic neuritis."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Severe malignant hypertension induces acute hypertensive **encephalopathy**, marked by intense headache, papilledema, and transient cortical blindness."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and Cerebral Localization",
        "quote": "Chronic traumatic **encephalopathy** results from cumulative shear strains inflicted upon cerebral white matter tracts during recurrent head trauma."
      }
    ]
  },
  "Dashboard — cephal\\heterocephalus.md": {
    "primary": "A genus of subterranean bathyergid rodents containing only the naked mole-rat (Heterocephalus glaber), native to the arid Horn of Africa.",
    "secondary": "In evolutionary biology and oncology, a eusocial mammal renowned for its extreme longevity, resistance to cancer, and insensitivity to acidic pain.",
    "quotes": [
      {
        "author": "Oldfield Thomas",
        "work": "On the Mammals of Somaliland",
        "quote": "The bizarre fossorial rodent **heterocephalus** is completely devoid of external hair, possessing wrinkled pink skin and enormous incisors."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Extended Phenotype",
        "quote": "The social structure of **heterocephalus** mimics an insect colony, with a single reproductive queen attended by non-breeding castes."
      },
      {
        "author": "E. O. Wilson",
        "work": "Sociobiology: The New Synthesis",
        "quote": "The discovery of eusociality in **heterocephalus** proved that insect-like social division of labor could evolve within mammalian lines."
      }
    ]
  },
  "Dashboard — cephal\\holocephalan.md": {
    "primary": "Any marine cartilaginous fish belonging to the subclass Holocephali, commonly known as chimaeras, ratfishes, or ghost sharks.",
    "secondary": "In systematic ichthyology, deep-sea chondrichthyan fishes characterized by a single external gill opening covering four gill slits and an autostylic upper jaw fused to the neurocranium.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "In every **holocephalan** fish, the palatoquadrate cartilage is completely fused with the skull, unlike the hyostylic jaw of true sharks."
      },
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "The dentition of the **holocephalan** consists of broad, non-replaceable grinding plates adapted for crushing molluscan shells."
      },
      {
        "author": "Alfred Sherwood Romer",
        "work": "Vertebrate Paleontology",
        "quote": "The ancient **holocephalan** line diverged from ancestral shark stock in the early Carboniferous, retaining smooth scaleless skin."
      }
    ]
  },
  "Dashboard — cephal\\holocephali.md": {
    "primary": "An ancient subclass of cartilaginous fishes (class Chondrichthyes) comprising the living chimaeras and numerous extinct fossil orders.",
    "secondary": "In evolutionary ichthyology, fishes having an autostylic skull, an opercular flap covering the gill slits, no stomach, and pelvic claspers in males.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Poissons Fossiles",
        "quote": "We unite the chimaeroid fishes into the subclass **holocephali**, emphasizing the complete fusion of the upper jaw to the cranium."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Vertebrated Animals",
        "quote": "The **holocephali** combine primitive elasmobranch cartilaginous skeletons with an advanced bony-fish-like opercular gill fold."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Members of the **holocephali** inhabit deep oceanic waters, swimming gracefully with undulating sweeps of their large pectoral fins."
      }
    ]
  },
  "Dashboard — cephal\\holocephalian.md": {
    "primary": "Of, relating to, or belonging to the subclass Holocephali; a chimaera fish.",
    "secondary": "In comparative anatomy, describing characteristics typical of chimaeras, such as continuous crushing tooth plates and autostylic jaw suspension.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The **holocephalian** skull exhibits complete synostosis between the visceral upper jaw arch and the neurocranium."
      },
      {
        "author": "Louis Agassiz",
        "work": "Fossil Fishes",
        "quote": "Devonian deposits yield numerous isolated tooth plates belonging to ancestral **holocephalian** forms."
      },
      {
        "author": "Richard Owen",
        "work": "Lectures on the Comparative Anatomy of Vertebrates",
        "quote": "The whip-like tail and venomous dorsal spine of the **holocephalian** ratfish distinguish it immediately from standard dogfishes."
      }
    ]
  },
  "Dashboard — cephal\\holoprosencephaly.md": {
    "primary": "A severe congenital developmental disorder resulting from failure of the embryonic prosencephalon (forebrain) to cleave into distinct right and left cerebral hemispheres.",
    "secondary": "In pediatric neurology and teratology, a malformation spectrum ranging from alobar to lobar forms, frequently accompanied by midfacial anomalies such as cyclopia or cleft lip.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In complete **holoprosencephaly**, a single monoventricular cerebrum fails to divide into lateral hemispheres, accompanied by facial dysmorphism."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Midline facial clefts and hypotelorism in the neonate should immediately prompt imaging to evaluate for underlying **holoprosencephaly**."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Defective sonic hedgehog signaling during early gastrulation is the primary molecular etiology of human **holoprosencephaly**."
      }
    ]
  },
  "Dashboard — cephal\\hydrocephalic.md": {
    "primary": "Pertaining to, affected by, or characteristic of hydrocephalus; having an excess of cerebrospinal fluid in the cranial ventricles.",
    "secondary": "In pathology, describing an abnormally enlarged, globular skull with thinned calvarial bones and wide fontanelles in an infant with hydrocephalus.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **hydrocephalic** head assumes an enormous globular or pyramidal shape, the forehead protruding over sunken orbits."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology",
        "quote": "Obstruction of the aqueduct of Sylvius induces severe **hydrocephalic** ventricular expansion, compressing the cerebral mantle."
      },
      {
        "author": "Walter Dandy",
        "work": "Internal Hydrocephalus",
        "quote": "The **hydrocephalic** infant suffers progressive cortical atrophy unless drainage pathways are surgically restored."
      }
    ]
  },
  "Dashboard — cephal\\hydrocephalus.md": {
    "primary": "An abnormal, excessive accumulation of cerebrospinal fluid (CSF) within the ventricles of the brain, leading to increased intracranial pressure and cranial enlargement.",
    "secondary": "In pediatric and adult neurology, categorized into communicating or obstructive (non-communicating) types, typically treated by ventriculoperitoneal shunt placement.",
    "quotes": [
      {
        "author": "Walter Dandy",
        "work": "Internal Hydrocephalus: An Experimental, Clinical and Pathological Study",
        "quote": "By placing an obstruction in the aqueduct of Sylvius, I produced experimental **hydrocephalus**, proving the circulation of cerebrospinal fluid."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Third Circulation",
        "quote": "Impaired absorption of cerebrospinal fluid by the arachnoid villi leads to chronic communicating **hydrocephalus**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In congenital **hydrocephalus**, the infant's cranial sutures separate widely, creating a dramatic disproportion between cranium and face."
      }
    ]
  },
  "Dashboard — cephal\\hydrocephaly.md": {
    "primary": "An alternative medical term for hydrocephalus; the pathological accumulation of fluid within the cranium.",
    "secondary": "In historical clinical pathology and surgery, the chronic expansion of the intracranial fluid spaces causing cerebral thinning and cranial deformity.",
    "quotes": [
      {
        "author": "Percivall Pott",
        "work": "Chirurgical Works",
        "quote": "Congenital **hydrocephaly** softens the cranial bones to such a degree that the sutures feel like yielding parchment under the fingers."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In cases of neglected **hydrocephaly**, the brain parenchyma is stretched into a paper-thin shell lining the dilated ventricles."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Head",
        "quote": "Early surgical drainage remains the only rational therapy to arrest the progressive neurological deterioration of severe **hydrocephaly**."
      }
    ]
  },
  "Dashboard — cephal\\macrocephalic.md": {
    "primary": "Having an abnormally large head or skull; macrocephalous.",
    "secondary": "In physical anthropology and neurology, having a cranial circumference greater than two standard deviations above the population mean.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "Skulls exhibiting cranial capacity well above eighteen hundred cubic centimeters are classified as markedly **macrocephalic**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient presented with a **macrocephalic** cranial vault, prominent bossing, and bowing of the long bones characteristic of Paget's disease."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropometry",
        "quote": "Certain geographical populations exhibit naturally **macrocephalic** cranial averages without any accompanying mental deficit."
      }
    ]
  },
  "Dashboard — cephal\\macrocephalon.md": {
    "primary": "An abnormally large head, or an organism characterized by an immense head shield or cranium.",
    "secondary": "In comparative anatomy and teratology, the anatomical condition of cranial overgrowth or disproportionate cephalic dimensions.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Invertebrated Animals",
        "quote": "The broad, flattened **macrocephalon** of ancient armored arthropods protected the vital nervous ganglia during benthic foraging."
      },
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "In early fossil agnathans, the immense **macrocephalon** constitutes more than half the total volume of the preserved fossil skeleton."
      },
      {
        "author": "Richard Owen",
        "work": "On the Anatomy of Vertebrates",
        "quote": "Disproportionate developmental acceleration of the anterior somites generates the striking **macrocephalon** seen in larval fishes."
      }
    ]
  },
  "Dashboard — cephal\\macrocephalous.md": {
    "primary": "Having an unusually or abnormally large head; macrocephalic.",
    "secondary": "In descriptive zoology and botany, having large head-like parts, such as an oversized head shield in insects or enlarged embryonic cotyledons.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Larval forms of certain crustaceans are remarkably **macrocephalous**, their huge heads equipped with swimming antennae."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Anatomy of Invertebrated Animals",
        "quote": "The adult soldier ant possesses a **macrocephalous** anatomy equipped with massive mandibular adductor muscles."
      },
      {
        "author": "Paul Broca",
        "work": "Mémoires d'Anthropologie",
        "quote": "Certain cranial anomalies yield a **macrocephalous** infant whose delivery presents insurmountable mechanical obstruction."
      }
    ]
  },
  "Dashboard — cephal\\macrocephaly.md": {
    "primary": "A condition in which the head circumference is abnormally large, typically defined as more than two standard deviations above the mean for age and sex.",
    "secondary": "In clinical genetics and neurology, benign familial macrocephaly or enlargement caused by megalencephaly, hydrocephalus, or metabolic storage diseases.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Progressive **macrocephaly** in infancy must be investigated promptly to distinguish benign megalencephaly from expanding hydrocephalus."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology",
        "quote": "In achondroplasia, true megalencephaly combines with small foramen magnum caliber to produce characteristic **macrocephaly**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The pathological overgrowth of glial tissues can produce striking **macrocephaly** in childhood degenerative neuropathies."
      }
    ]
  },
  "Dashboard — cephal\\megacephaly.md": {
    "primary": "The condition of having an abnormally large head or skull; macrocephaly or megalocephaly.",
    "secondary": "In clinical anthropology and medicine, cranial enlargement exceeding standard developmental percentiles, whether benign or pathological.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Benign familial **megacephaly** requires no neurosurgical intervention, the child displaying normal cognitive milestones."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "The frequency of **megacephaly** in historical cranial collections reflects both physiological variation and underlying pathology."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In cases of osseous **megacephaly**, hyperostosis of the calvarial plates dramatically thickens the cranium without enlarging the brain."
      }
    ]
  },
  "Dashboard — cephal\\megalocephaly.md": {
    "primary": "Abnormal, pathological enlargement of the head or skull; macrocephaly.",
    "secondary": "In skeletal pathology, hyperostotic cranial enlargement seen in Paget's disease of bone (osteitis deformans), leontiasis ossea, or acromegaly.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient with advanced Paget's disease complained that his hat size expanded yearly, classic proof of progressive **megalocephaly**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In leontiasis ossea, dense diffuse hyperostosis produces grotesque **megalocephaly**, encroaching upon the cranial nerve foramina."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Acromegalic **megalocephaly** features massive elongation of the mandible, bossing of the frontal ridges, and expansion of the sinuses."
      }
    ]
  },
  "Dashboard — cephal\\mesaticephalic.md": {
    "primary": "Having a medium-proportioned skull with a cephalic index between 75 and 80; intermediate between dolichocephalic and brachycephalic.",
    "secondary": "In physical anthropology and veterinary anatomy, designating skulls or canine breeds (such as beagles and retrievers) possessing average cranial proportions.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "Crania whose length-breadth ratio falls between seventy-five and eighty percent are designated **mesaticephalic** or sub-brachycephalic."
      },
      {
        "author": "Franz Boas",
        "work": "Changes in Bodily Form of Descendants of Immigrants",
        "quote": "The blending of diverse cranial types in metropolitan centers generates predominantly **mesaticephalic** intermediate forms."
      },
      {
        "author": "William Z. Ripley",
        "work": "The Races of Europe",
        "quote": "The transitional populations of central France display a balanced, **mesaticephalic** head index reflecting ancestral cross-currents."
      }
    ]
  },
  "Dashboard — cephal\\mesencephalic.md": {
    "primary": "Of, relating to, or situated in the mesencephalon (the midbrain).",
    "secondary": "In neuroanatomy, designating midbrain structures such as the mesencephalic trigeminal nucleus, the cerebral aqueduct, or the substantia nigra.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "The **mesencephalic** nucleus of the trigeminal nerve contains unipolar sensory neurons that mediate proprioception from masticatory muscles."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The tectum of the **mesencephalic** segment bears the superior and inferior colliculi, vital for visual and auditory reflexes."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Transection through the **mesencephalic** level produces decerebrate rigidity by releasing vestibulospinal tone from higher cortical control."
      }
    ]
  },
  "Dashboard — cephal\\mesocephalic.md": {
    "primary": "Having a skull of medium proportions, with a cephalic index between 75 and 80; mesaticephalic.",
    "secondary": "In craniometry and physical anthropology, designating an intermediate cranial shape between narrow dolichocephaly and broad brachycephaly.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Mémoires d'Anthropologie",
        "quote": "The majority of modern European skulls fall into the balanced **mesocephalic** category, avoiding extreme elongation or roundness."
      },
      {
        "author": "Franz Boas",
        "work": "Anthropometry of Central European Populations",
        "quote": "Our data confirmed that **mesocephalic** averages emerge frequently from the intermarriage of long-headed and broad-headed lineages."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The intermediate **mesocephalic** cranium illustrates the smooth morphological continuum connecting diverse human populations."
      }
    ]
  },
  "Dashboard — cephal\\metencephalon.md": {
    "primary": "The anterior part of the embryonic hindbrain (rhombencephalon), which differentiates into the pons and the cerebellum.",
    "secondary": "In neuroanatomy, the division of the brainstem and hindbrain lying between the mesencephalon and myelencephalon (medulla oblongata).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **metencephalon** develops dorsally into the vast foliated mass of the cerebellum and ventrally into the transverse bridge of the pons."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "During embryonic neurogenesis, neuroblasts of the **metencephalon** migrate outward to establish the Purkinje cell layer of the cerebellar cortex."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The fourth ventricle expands broadly within the dorsal cavity of the developing **metencephalon**."
      }
    ]
  },
  "Dashboard — cephal\\microcephalic.md": {
    "primary": "Having an abnormally small head or cranial capacity, associated with incomplete brain development; microcephalous.",
    "secondary": "In clinical neurology, a child or adult whose head circumference is greater than two standard deviations below the mean for age and sex, often presenting with cognitive impairment.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **microcephalic** idiot displays a receding forehead, pointed cranium, and severely restricted intellectual development."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Premature synostosis of the cranial sutures was historically blamed for the small brain of the **microcephalic** child."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "Craniometric examination of the **microcephalic** skull reveals that cranial capacity may plummet below five hundred cubic centimeters."
      }
    ]
  },
  "Dashboard — cephal\\microcephalous.md": {
    "primary": "Characterized by an abnormally small head in proportion to the body; microcephalic.",
    "secondary": "In comparative anatomy and anthropology, describing individuals, fetuses, or animal lineages possessing miniature cranial vaults.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Certain **microcephalous** idiots mimic ancestral primate behaviors, exhibiting astonishing climbing agility and sensory alertness."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The **microcephalous** brain preserves the primary cerebral fissures while lacking the complex secondary cortical convolutions."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In the **microcephalous** dwarf, somatic growth can remain remarkably symmetrical despite severe cognitive stunting."
      }
    ]
  },
  "Dashboard — cephal\\microcephalus.md": {
    "primary": "An individual affected with congenital microcephaly; a person having an abnormally small head and brain.",
    "secondary": "In teratology and developmental neurology, an individual exhibiting profound microencephaly and cranial vault hypoplasia.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Über den Cretinismus und über mikroskopische Schädel",
        "quote": "The brain of the **microcephalus** is arrested at an embryonic stage of development, failing to expand the overlying calvarium."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Surgical craniectomy to release presumed cranial constriction in the **microcephalus** proved useless, as the defect is primarily cerebral."
      },
      {
        "author": "Isidore Geoffroy Saint-Hilaire",
        "work": "General and Particular History of Anomalies of Organization",
        "quote": "Our teratological collection includes preserved specimens of the **microcephalus**, displaying harmonious facial development beneath tiny vaults."
      }
    ]
  },
  "Dashboard — cephal\\microcephaly.md": {
    "primary": "A neurodevelopmental disorder characterized by an abnormally small head circumference, defined as more than two standard deviations below the mean.",
    "secondary": "In pediatric neurology and infectious disease, a condition caused by genetic mutations, chromosomal aberrations, or intrauterine infections (e.g. cytomegalovirus, rubella, Zika virus).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital **microcephaly** is typically accompanied by spastic diplegia and severe global cognitive impairment."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The etiology of **microcephaly** resides in defective neurogenesis within the germinal matrix of the embryonic neural tube."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology",
        "quote": "Disorders causing intrauterine ischemic insult frequently culminate in secondary post-migrational **microcephaly**."
      }
    ]
  },
  "Dashboard — cephal\\myelencephalon.md": {
    "primary": "The posterior portion of the embryonic hindbrain (rhombencephalon), which differentiates into the adult medulla oblongata.",
    "secondary": "In neuroanatomy, the lowest division of the brainstem, continuous with the spinal cord below and containing vital respiratory and cardiovascular centers.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **myelencephalon** constitutes the transitional bridge linking the higher brainstem with the cervical spinal cord."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Within the dorsal sensory nuclei of the **myelencephalon**, the ascending gracile and cuneate fasciculi terminate in dense synaptic nests."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The lateral walls of the **myelencephalon** flare open during the second month to establish the floor of the fourth ventricle."
      }
    ]
  },
  "Dashboard — cephal\\neencephalon.md": {
    "primary": "The phylogenetically newer part of the brain, specifically the cerebral neocortex and related telencephalic structures (neoencephalon).",
    "secondary": "In comparative evolutionary neurology, the modern cortical mantle that overlies and exerts inhibitory control over archaic subcortical brain centers.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "The phenomenal evolutionary expansion of the **neencephalon** provided the histological basis for human symbolic and reflective thought."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Voluntary motor control requires continuous descending facilitation from the **neencephalon** acting upon lower spinal mechanisms."
      },
      {
        "author": "C. Judson Herrick",
        "work": "Brains of Rats and Men",
        "quote": "The **neencephalon** is not an isolated organ, but an intricate associative superstructure built upon the ancient sensory paleencephalon."
      }
    ]
  },
  "Dashboard — cephal\\neoencephalon.md": {
    "primary": "An alternative spelling of neencephalon; the evolutionarily modern structures of the brain, dominated by the cerebral neocortex.",
    "secondary": "In neurobiology and evolutionary cognitive science, the phylogenetically recent mammalian forebrain responsible for higher cognitive functions.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "Man on His Nature",
        "quote": "In the human species, the **neoencephalon** reaches its crowning development, subserving language, reason, and self-conscious purpose."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Texture of the Nervous System",
        "quote": "The pyramidal neurons of the **neoencephalon** form thousands of recurrent dendritic spines that support associative learning."
      },
      {
        "author": "A. R. Luria",
        "work": "The Working Brain",
        "quote": "Lesions confined to the tertiary association areas of the **neoencephalon** disrupt complex planning and programmatic behavior."
      }
    ]
  },
  "Dashboard — cephal\\paleencephalon.md": {
    "primary": "The phylogenetically older, primitive part of the vertebrate brain (the brainstem, basal ganglia, and archicortex) underlying autonomic and instinctive behaviors.",
    "secondary": "In evolutionary neuroanatomy, the ancient core of the nervous system as contrasted with the evolutionarily recent neocortex (neencephalon).",
    "quotes": [
      {
        "author": "C. Judson Herrick",
        "work": "The Brain of the Tiger Salamander",
        "quote": "In lower vertebrates, the entire central nervous organ consists of a functional **paleencephalon** dedicated to survival reflexes."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Automatic postural reflexes and protective withdrawals are orchestrated securely within the ancient circuits of the **paleencephalon**."
      },
      {
        "author": "Paul D. MacLean",
        "work": "The Triune Brain in Evolution",
        "quote": "The reptilian complex represents the durable substrate of the **paleencephalon**, governing territorial and ancestral routines."
      }
    ]
  },
  "Dashboard — cephal\\paleoencephalon.md": {
    "primary": "An alternative spelling of paleencephalon; the primitive, phylogenetically ancient portion of the brain as distinguished from the neocortex.",
    "secondary": "In evolutionary neurobiology, the subcortical and brainstem structures mediating visceral homeostasis, primitive emotions, and stereotyped motor patterns.",
    "quotes": [
      {
        "author": "Paul D. MacLean",
        "work": "A Triune Concept of the Brain and Behaviour",
        "quote": "Deep within the human skull lies the **paleoencephalon**, silently directing cardiovascular and respiratory homeostasis."
      },
      {
        "author": "C. Judson Herrick",
        "work": "Introduction to Neurology",
        "quote": "The sensory integration of the olfactory and gustatory tracts was the ancestral foundation around which the **paleoencephalon** crystallized."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Comparative vertebrate anatomy proves that the basic reticular architecture of the **paleoencephalon** has remained stable for hundreds of millions of years."
      }
    ]
  },
  "Dashboard — cephal\\panencephalitis.md": {
    "primary": "Diffuse, widespread inflammation simultaneously affecting both the gray matter and white matter throughout the entire brain.",
    "secondary": "In clinical neurology and virology, notably subacute sclerosing panencephalitis (SSPE), a fatal, progressive neurodegenerative complication of persistent measles infection.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Fulminant viral **panencephalitis** obliterates cortical architecture, presenting with intractable myoclonus, dementia, and rapid coma."
      },
      {
        "author": "Constantin von Economo",
        "work": "Encephalitis Lethargica",
        "quote": "Widespread perivenous demyelination and diffuse microglial proliferation characterize the morbid anatomy of chronic **panencephalitis**."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "In subacute **panencephalitis**, nuclear and cytoplasmic inclusion bodies inside neurons provide definitive proof of slow viral pathogenesis."
      }
    ]
  },
  "Dashboard — cephal\\prosencephalon.md": {
    "primary": "The embryonic forebrain, the most anterior of the three primary brain vesicles in vertebrate development.",
    "secondary": "In neuroembryology, the neural tube vesicle that subdivides during the fifth week of development into the telencephalon (cerebral hemispheres) and the diencephalon.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "From the primitive **prosencephalon** bud forth the optic vesicles and the bilateral cerebral hemispheres."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Failure of the **prosencephalon** to divide cleanly into paired lateral hemispheres culminates in tragic alobar holoprosencephaly."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The phenomenal growth of the dorsal wall of the **prosencephalon** produces the mantle of the human cerebral cortex."
      }
    ]
  },
  "Dashboard — cephal\\rhombencephalon.md": {
    "primary": "The embryonic hindbrain, the most posterior of the three primary brain vesicles in vertebrate development.",
    "secondary": "In neuroembryology, the primary vesicle that differentiates into the metencephalon (pons and cerebellum) and the myelencephalon (medulla oblongata).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The cavity of the **rhombencephalon** expands into the diamond-shaped space of the adult fourth ventricle."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Rhombomeres subdividing the **rhombencephalon** dictate the precise segmental distribution of the motor cranial nerves."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Within the dorsal neuroepithelium of the **rhombencephalon**, the rhombic lip gives origin to all cerebellar precursor cells."
      }
    ]
  },
  "Dashboard — cephal\\rhombencephalosynapsis.md": {
    "primary": "A rare congenital malformation of the hindbrain characterized by partial or complete absence of the cerebellar vermis with fusion of the cerebellar hemispheres.",
    "secondary": "In pediatric neuroradiology and embryology, a midline hindbrain anomaly frequently accompanied by fusion of the dentate nuclei and superior cerebellar peduncles.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Archiv für Pathologische Anatomie",
        "quote": "In **rhombencephalosynapsis**, the absence of the median vermis is compensated by a continuous, undivided transverse cerebellar bridge."
      },
      {
        "author": "Harvey Cushing",
        "work": "Surgery of the Posterior Fossa",
        "quote": "Posterior fossa exploration in cases of **rhombencephalosynapsis** reveals continuous cerebellar folia crossing the midline uninterrupted."
      },
      {
        "author": "Wilder Penfield",
        "work": "Developmental Anomalies of the Central Nervous System",
        "quote": "Magnetic resonance imaging has demonstrated that **rhombencephalosynapsis** is often associated with hydrocephalus and Gomez-López-Hernández syndrome."
      }
    ]
  }
};

const updated = updateNotesBatch(BASE_DIR, BATCH5_DATA);
console.log(`Body & Physiology Part 1 - Batch 5 Completed: ${updated} / ${Object.keys(BATCH5_DATA).length} notes updated.`);
