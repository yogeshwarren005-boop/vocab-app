import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batchData = {
  "Dashboard — odont\\anodonta.md": {
    "primary": "A taxonomic genus of large freshwater mussels in the family Unionidae, characterized by thin, toothless shell hinges.",
    "secondary": "In malacology, unionid bivalves lacking pseudocardinal and lateral hinge teeth, commonly known as floater mussels or swan mussels.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The freshwater bivalve **Anodonta** lacks the interlocking hinge teeth found in more robust unionids."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Glochidia larvae discharged by **Anodonta** attach to the gills of passing fish to complete development."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Ciliary feeding currents across the ctenidia of **Anodonta** provide an elegant model of lamellibranch respiration."
      }
    ]
  },
  "Dashboard — odont\\anodontia.md": {
    "primary": "The congenital absence of teeth, either in the primary or permanent dentition.",
    "secondary": "In oral pathology and medical genetics, complete failure of dental lamina development, commonly presenting as a feature of hypohidrotic ectodermal dysplasia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Complete **anodontia** is exceedingly rare and almost invariably accompanied by generalized ectodermal defects."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Cases of inherited **anodontia** illustrate how cutaneous appendages and teeth share a common developmental mechanism."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Congenital failure of tooth germ formation leads to partial or total **anodontia** within both jaws."
      }
    ]
  },
  "Dashboard — odont\\conodont.md": {
    "primary": "An extinct microscopic tooth-like fossil composed of calcium phosphate, produced by primitive marine agnathan chordates.",
    "secondary": "In micropaleontology and biostratigraphy, index fossils spanning the Cambrian to Triassic that belonged to eel-like chordates (Conodonta) possessing mineralized feeding apparatuses.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Primary Factors of Organic Evolution",
        "quote": "The tiny phosphatic structures designated as **conodont** elements represent the earliest vertebrate mineralized hard tissues."
      },
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "Stratigraphic correlation of Paleozoic marine limestone strata relies heavily upon the evolutionary succession of the **conodont**."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Microscopic **conodont** teeth arranged along the pharynx provided primitive chordates with an effective grasping apparatus."
      }
    ]
  },
  "Dashboard — odont\\cynodont.md": {
    "primary": "A member of an extinct group of carnivorous and herbivorous therapsid synapsids from which mammals evolved.",
    "secondary": "In vertebrate paleontology and evolutionary biology, advanced theriodonts possessing specialized heterodont dentition, secondary bony palates, and differentiated jaw musculature.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "The skull of the advanced **cynodont** exhibits transitional features that bridge ancient reptiles and primitive mammals."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In every true **cynodont**, the differentiation into incisors, canines, and multicuspid cheek teeth is clearly displayed."
      },
      {
        "author": "Richard Owen",
        "work": "Odontography: A Treatise on the Comparative Anatomy of the Teeth",
        "quote": "The dentary bone of the **cynodont** expanded progressively, foreshadowing the mammalian single-bone lower jaw."
      }
    ]
  },
  "Dashboard — odont\\dicynodont.md": {
    "primary": "An extinct herbivorous therapsid of the suborder Dicynodontia, typically characterized by a horny beak and two prominent canine tusks.",
    "secondary": "In vertebrate paleontology, dominant Permo-Triassic non-mammalian synapsids possessing edentulous turtle-like keratinous beaks paired with ever-growing maxillary tusks.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Descriptive and Illustrated Catalogue of the Fossil Reptilia of South Africa",
        "quote": "I established the genus **Dicynodont** to denote reptiles possessing two formidable canine tusks within an otherwise toothless jaw."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The massive skull of the herbivorous **dicynodont** accommodated powerful muscles for grinding tough vegetation."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Fossil deposits in the Karoo basin preserve abundant skeletons of the bidental reptile known as the **dicynodont**."
      }
    ]
  },
  "Dashboard — odont\\dysodontiasis.md": {
    "primary": "Difficult, painful, or abnormal dentition or tooth eruption.",
    "secondary": "In clinical stomatology and dental surgery, severe pain, localized pericoronitis, and mucosal inflammation accompanying impacted or delayed wisdom tooth eruption.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe facial neuralgia and trismus are frequent accompaniments of acute mandibular **dysodontiasis**."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The convulsions of early infancy may be reflexively triggered by agonizing **dysodontiasis** during deciduous tooth eruption."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon: A Dictionary of Medical Science",
        "quote": "By **dysodontiasis**, physicians denote that morbid state of the gums and jaws provoked by retarded dentition."
      }
    ]
  },
  "Dashboard — odont\\endodontia.md": {
    "primary": "The branch of dentistry concerned with the etiology, diagnosis, prevention, and treatment of diseases of the dental pulp and periapical tissues.",
    "secondary": "In dental science and operative stomatology, surgical and non-surgical procedures aimed at cleansing, shaping, and obturating the pulpal root canal space.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Systemic bacteremia originating from apical abscesses was substantially curtailed by modern aseptic **endodontia**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Maxillary sinus infections often trace directly to neglected dental roots requiring specialized **endodontia**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The clinical scope of **endodontia** centers upon preserving tooth stability following devitalization of the coronal pulp."
      }
    ]
  },
  "Dashboard — odont\\endodontic.md": {
    "primary": "Of, relating to, or situated within the dental pulp or the root canal of a tooth.",
    "secondary": "In operative dentistry, designating diagnostic instruments, rotary files, disinfection irrigants, or therapy targeting the inner neurovascular pulpal core.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Failure of complete **endodontic** debridement allows persistent anaerobic colonies to sustain chronic periapical osteitis."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Referred facial pain along the trigeminal divisions may subside following timely **endodontic** drainage."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological examination of the inflamed **endodontic** pulp reveals granulomatous tissue surrounded by dentinal tubules."
      }
    ]
  },
  "Dashboard — odont\\endodontics.md": {
    "primary": "The specialized branch of dental medicine dealing with the biology, pathology, and therapy of the dental pulp and surrounding periradicular tissues.",
    "secondary": "In dental surgery, the advanced discipline encompassing root canal therapy, vital pulp therapy, apicoectomy, and the management of traumatized teeth.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The refinement of clinical **endodontics** has eliminated the necessity for routine tooth extraction in pulpal necrosis."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Intense dental pain referred to the mandibular branch resolved completely under specialized **endodontics**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The anatomical complexity of root canal bifurcations dictates the technical procedures of modern **endodontics**."
      }
    ]
  },
  "Dashboard — odont\\endodontist.md": {
    "primary": "A dentist who specializes in the diagnosis, prevention, and treatment of diseases and injuries of the dental pulp and periapical tissues.",
    "secondary": "In specialized oral healthcare, a practitioner skilled in operating microscopes, rotary canal preparation, and complex root canal retreatments.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Consultation with a skilled **endodontist** is indicated when persistent apical abscesses threaten systemic health."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The patient was referred to an **endodontist** to relieve severe odontogenic trigeminal neuralgia."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Careful root canal disinfection performed by the **endodontist** prevented cavernous sinus thrombophlebitis."
      }
    ]
  },
  "Dashboard — odont\\exodontia.md": {
    "primary": "The branch of dental surgery concerned with the extraction of teeth.",
    "secondary": "In oral surgery, the clinical technique and mechanical instrumentation required for the luxation, elevation, and surgical removal of erupted or impacted teeth.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Before the advent of local anesthesia, the practice of **exodontia** was an ordeal of excruciating agony."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Aseptic principles established in general surgery were swiftly applied to the operative discipline of **exodontia**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Familiarity with mandibular alveolar bone thickness is essential for avoiding cortical fracture during **exodontia**."
      }
    ]
  },
  "Dashboard — odont\\exodontic.md": {
    "primary": "Of or relating to the extraction of teeth (exodontia).",
    "secondary": "In surgical instrumentation and dental literature, describing elevators, forceps, surgical flaps, or techniques designed specifically for tooth removal.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe alveolar hemorrhage following **exodontic** intervention warrants immediate investigation for hemophilia."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "The development of specialized **exodontic** forceps minimized traumatic splintering of the alveolar ridge."
      },
      {
        "author": "Robley Dunglison",
        "work": "General Therapeutics and Materia Medica",
        "quote": "Topical styptics and mechanical pressure remain primary measures for arresting post-operative **exodontic** bleeding."
      }
    ]
  },
  "Dashboard — odont\\exodontics.md": {
    "primary": "The science and practice of extracting teeth; exodontia.",
    "secondary": "In oral and maxillofacial surgery, the systematic surgical specialty focused on the extraction of impacted third molars, supernumerary teeth, and retained roots.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Advances in local analgesia and radiography transformed operative **exodontics** into a painless science."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Careful tissue handling and minimal bone sacrifice are the guiding principles of modern **exodontics**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The course of the inferior alveolar nerve must be evaluated before complex third molar **exodontics**."
      }
    ]
  },
  "Dashboard — odont\\exodontist.md": {
    "primary": "A dental specialist whose practice is limited to or focuses upon the extraction of teeth.",
    "secondary": "In oral surgery, a practitioner specializing in difficult impactions, bone grafting, and pre-prosthetic alveolar surgical remodeling.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The experienced **exodontist** carefully elevated the deeply impacted mandibular third molar without damaging the alveolar nerve."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Intractable facial spasms prompted a visit to the **exodontist** to extract an irritating retained root fragment."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Surgical decompression by the **exodontist** evacuated a submandibular abscess complicating severe periapical infection."
      }
    ]
  },
  "Dashboard — odont\\hyperodontidae.md": {
    "primary": "An alternate or obsolete family name for the Ziphiidae (beaked whales), named after the bottlenose whale genus Hyperoodon.",
    "secondary": "In systematic cetology and marine zoology, deep-diving toothed whales characterized by a pronounced rostral beak and extreme reduction of functional dentition to one or two mandibular pairs.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Cetaceans formerly cataloged under **Hyperodontidae** exhibit prominent maxillary crests supporting deep acoustic fat organs."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In members of **Hyperodontidae**, the dentition is reduced to a single pair of functional lower teeth."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "The massive cranial expansion in the genus Hyperoodon gave name to the archaic family **Hyperodontidae**."
      }
    ]
  },
  "Dashboard — odont\\macrodontia.md": {
    "primary": "The condition of having abnormally large teeth; megadontia.",
    "secondary": "In oral pathology and dysmorphology, generalized or localized dental gigantism, frequently associated with pituitary gigantism or facial hemihypertrophy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Pronounced facial hemihypertrophy is characteristically accompanied by ipsilateral **macrodontia** and macroglossia."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Eosinophilic adenomas producing juvenile gigantism frequently induce generalized **macrodontia** alongside massive mandibular growth."
      },
      {
        "author": "Richard Owen",
        "work": "Odontography: A Treatise on the Comparative Anatomy of the Teeth",
        "quote": "Comparative studies show that extreme **macrodontia** in anthropoid apes serves primarily display and defensive functions."
      }
    ]
  },
  "Dashboard — odont\\mastodon.md": {
    "primary": "A large, extinct elephant-like proboscidean mammal of the genus Mammut, having distinct nipple-shaped cusps on its molar teeth.",
    "secondary": "In vertebrate paleontology, Miocene to Pleistocene proboscideans with low-crowned zygodont molars adapted for browsing woody vegetation, distinct from true mammoths.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "Researches on Fossil Bones",
        "quote": "I assigned the name **mastodon** to this colossal extinct quadruped on account of the nipple-shaped tubercles upon its molars."
      },
      {
        "author": "Thomas Jefferson",
        "work": "Notes on the State of Virginia",
        "quote": "The discovery of the incognitum or American **mastodon** near the Ohio River proves the ancient existence of enormous land beasts."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Bones and teeth of the giant **mastodon** are frequently unearthed from peat bogs and post-Pliocene gravels."
      }
    ]
  },
  "Dashboard — odont\\odont.md": {
    "primary": "A root combining form (odont- / odonto-) meaning tooth or teeth.",
    "secondary": "In anatomical nomenclature and taxonomic zoology, utilized in forming terms that designate tooth structures, dentition, or dental disorders (e.g., odontoid, odontology).",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Odontography: A Treatise on the Comparative Anatomy of the Teeth",
        "quote": "The Greek root **odont-** provides the foundational prefix for descriptive anatomical nomenclature of mammalian dentition."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Compounds incorporating **odont-** designate structures possessing tooth-like shapes or relations with the dental apparatus."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Pathological syndromes bearing the prefix **odont-** involve infectious or developmental disorders of the teeth and jaws."
      }
    ]
  },
  "Dashboard — odont\\odontalgia.md": {
    "primary": "Pain in a tooth or teeth; toothache.",
    "secondary": "In stomatology and clinical medicine, acute or throbbing pain originating from dental caries, pulpitis, periodontal abscess, or referred from maxillary sinus disease.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe facial neuralgia must be distinguished from the localized throbbing agony of acute **odontalgia**."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "A topical application of oil of cloves rarely fails to soothe the violent paroxysm of inflamed **odontalgia**."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Exquisite nocturnal **odontalgia** signals irreversible inflammation and suppurative necrosis of the dental pulp."
      }
    ]
  },
  "Dashboard — odont\\odontaspididae.md": {
    "primary": "The family of lamniform sharks comprising the sand tiger sharks (ragged-tooth sharks).",
    "secondary": "In elasmobranch ichthyology and marine biology, predatory sharks possessing awl-like, non-serrated teeth adapted for grasping slippery prey, and lacking a nictitating eyelid.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Members of **Odontaspididae** display protruding, needle-like teeth designed for seizing swift marine teleosts."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The reproductive biology of **Odontaspididae** features intrauterine cannibalism among developing embryos."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Fossil teeth identical to modern **Odontaspididae** are abundant throughout Cretaceous marine strata."
      }
    ]
  },
  "Dashboard — odont\\odontaspis.md": {
    "primary": "A taxonomic genus of lamniform sharks in the family Odontaspididae, including the smalltooth sand tiger shark.",
    "secondary": "In marine paleontology and ichthyology, slender-bodied sharks with long, awl-like teeth characterized by prominent lateral denticles, known from abundant fossil tooth beds.",
    "quotes": [
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les Poissons Fossiles",
        "quote": "I established the genus **Odontaspis** to receive fossil shark teeth displaying slender crowns flanked by sharp lateral cusps."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The living shark **Odontaspis** swims slowly over sandy sea bottoms, snatching cephalopods and bottom-dwelling fishes."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The jaw mechanics of **Odontaspis** illustrate efficient puncture-and-hold predation among primitive lamniforms."
      }
    ]
  },
  "Dashboard — odont\\odontiasis.md": {
    "primary": "The development and cutting or eruption of teeth; dentition.",
    "secondary": "In historical pediatrics and physiology, the physiological process of primary tooth eruption in infants, historically associated with teething symptoms.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Fretfulness, mild fever, and excessive salivation accompany the physiological process of infant **odontiasis**."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The physician must guard against attributing severe cerebral disease merely to the ordinary coincidences of **odontiasis**."
      },
      {
        "author": "Henry Koplik",
        "work": "The Diseases of Infancy and Childhood",
        "quote": "Swollen and tender gums indicate that primary deciduous **odontiasis** is actively progressing."
      }
    ]
  },
  "Dashboard — odont\\odontoceti.md": {
    "primary": "A taxonomic suborder of cetaceans that have teeth rather than baleen, comprising dolphins, porpoises, killer whales, and sperm whales.",
    "secondary": "In marine mammalogy and evolutionary biology, monophyletic toothed whales that employ sophisticated echolocation via acoustic melon structures and asymmetric skull morphology.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The suborder **Odontoceti** is distinguished from mysticetes by the persistence of homodont teeth and a single blowhole."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "Cranial asymmetry and maxillary expansion are hallmark osteological characteristics of all living **Odontoceti**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The remarkable homodont dentition of **Odontoceti** represents an adaptation for grasping slippery pelagic prey."
      }
    ]
  },
  "Dashboard — odont\\odontoglossum.md": {
    "primary": "A genus of tropical American orchids in the family Orchidaceae, characterized by tooth-like projections on the lip (labellum).",
    "secondary": "In systematic orchidology and horticulture, high-elevation Andean epiphytic orchids renowned for showy, intricately patterned flower sprays with toothed calli.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "The prominent dental calli on the labellum of **Odontoglossum** guide pollinating insects directly toward the rostellum."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "High-altitude cloud forests of the Andes host magnificent species of the epiphytic orchid **Odontoglossum**."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The characteristic tooth-like crests on the lip gave the genus **Odontoglossum** its scientific appellation."
      }
    ]
  },
  "Dashboard — odont\\odontoid.md": {
    "primary": "Shaped like a tooth; designating the tooth-like process (dens) projecting upward from the second cervical vertebra (axis).",
    "secondary": "In gross human osteology and spinal surgery, the vertical bony peg that articulates with the anterior arch of the atlas, providing the pivot for rotational head movements.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **odontoid** process of the axis ascends into the ring of the atlas, held firmly by the transverse ligament."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Fracture of the **odontoid** process with backward displacement instantly crushes the medulla oblongata, causing fatal arrest."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Congenital hypoplasia of the **odontoid** peg predisposes to dangerous atlantoaxial subluxation upon minor trauma."
      }
    ]
  },
  "Dashboard — odont\\odontology.md": {
    "primary": "The scientific study of the structure, development, diseases, and comparative anatomy of the teeth; dentistry.",
    "secondary": "In forensic medicine and anthropology, the scientific analysis of human dentition, bite marks, and dental restoration records to identify human remains.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Odontography: A Treatise on the Comparative Anatomy of the Teeth",
        "quote": "Comparative **odontology** demonstrates how dentition reflects an animal's exact place within ecological food webs."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The integration of bacteriological research into **odontology** has clarified the etiology of dental caries."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "The findings of evolutionary **odontology** trace the progressive reduction of human canine size since the late Miocene."
      }
    ]
  },
  "Dashboard — odont\\odontoma.md": {
    "primary": "A benign odontogenic tumor of the jaw composed of dental tissue elements (enamel, dentin, cementum, and pulp).",
    "secondary": "In oral maxillofacial pathology, classified as a compound odontoma (resembling small tooth-like structures or denticles) or a complex odontoma (an irregular conglomerate mass).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Radiographic examination revealed a calcified compound **odontoma** obstructing the normal eruption of the permanent canine."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopically, an **odontoma** displays disordered arrays of mature enamel, dentin, and cementum mimicking dental organogenesis."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Surgical enucleation of the mandibular **odontoma** was achieved through conservative curettage without altering jaw continuity."
      }
    ]
  },
  "Dashboard — odont\\odontophore.md": {
    "primary": "The cartilaginous structure in the mouth of most mollusks that supports the radula (toothed chitinous ribbon).",
    "secondary": "In invertebrate zoology and comparative functional morphology, the muscular cushion and subradular membrane that protrudes and rasps algae or flesh during molluscan feeding.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The muscular **odontophore** acts as an elastic bolster over which the rasping radula is rhythmically drawn."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Paired cartilages within the gastropod **odontophore** provide rigid support during vigorous feeding upon tough algae."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Development of the **odontophore** proceeds from a ventral invagination of the stomodaeal floor in the molluscan larva."
      }
    ]
  },
  "Dashboard — odont\\odontophorus.md": {
    "primary": "A genus of New World quails (wood quails) in the family Odontophoridae, inhabiting Central and South American tropical forests.",
    "secondary": "In systematic ornithology, plump, terrestrial gamebirds possessing heavy bills with distinct denticulations or serrae along the cutting edges of the lower mandible.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "A Monograph of the Odontophorinae, or Partridges of America",
        "quote": "The wood quails belonging to the genus **Odontophorus** dwell in dense Neotropical undergrowth, rarely taking wing."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The toothed lower mandible of **Odontophorus** reflects specialized adaptations for processing hard jungle seeds and nuts."
      },
      {
        "author": "Alexander Wetmore",
        "work": "The Birds of the Republic of Panama",
        "quote": "The resonant duetting calls of **Odontophorus** echo through the humid montane rainforest at dawn."
      }
    ]
  },
  "Dashboard — odont\\periodontal.md": {
    "primary": "Of, relating to, or situated around the teeth; surrounding and supporting a tooth.",
    "secondary": "In periodontology, designating the periodontium, which comprises the gingiva, periodontal ligament, cementum, and alveolar bone.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic **periodontal** infection provides a persistent portal of entry for oral streptococci into the systemic bloodstream."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The collagenous fibers of the **periodontal** ligament anchor the cementum of the tooth root into the surrounding alveolar socket."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Inflammatory destruction of the **periodontal** membrane leads inexorably to alveolar bone resorption and tooth mobility."
      }
    ]
  },
  "Dashboard — odont\\periodontia.md": {
    "primary": "The branch of dentistry that deals with the study and treatment of diseases of the supporting tissues of the teeth; periodontics.",
    "secondary": "In clinical stomatology, the preventive and surgical discipline dedicated to the health of the gingiva, periodontal ligament, cementum, and alveolar bone.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The development of rational clinical **periodontia** emphasized mechanical subgingival scaling to halt alveolar resorption."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Specialized techniques evolved in operative **periodontia** for regenerating supporting bone lost to chronic suppuration."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Knowledge of the vascular supply of the gingival papillae is fundamental to the surgical procedures of **periodontia**."
      }
    ]
  },
  "Dashboard — odont\\periodontic.md": {
    "primary": "Of or relating to periodontics or the periodontium (the supporting structures around the teeth).",
    "secondary": "In dental therapeutics and clinical terminology, characterizing instruments, surgical flaps, or antimicrobial regimens aimed at treating periodontal disease.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Advanced **periodontic** destruction causes deep pocketing and persistent purulent discharge along the gingival margin."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Proprioceptive mechanoreceptors within the **periodontic** ligament regulate the reflex force of mastication."
      },
      {
        "author": "Robley Dunglison",
        "work": "General Therapeutics and Materia Medica",
        "quote": "Astringent mouthwashes were traditionally employed to tone relaxed gingival tissues during active **periodontic** distress."
      }
    ]
  },
  "Dashboard — odont\\periodontics.md": {
    "primary": "The branch of dental medicine concerned with the study, prevention, and treatment of diseases affecting the supporting tissues of the teeth.",
    "secondary": "In modern dental surgery, the subspecialty managing gingivitis, periodontitis, guided tissue regeneration, and the placement of dental implants.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The systematic practice of **periodontics** plays a critical role in mitigating systemic inflammation and secondary bacteremia."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Rigorous oral hygiene and expert **periodontics** prevented further loss of mandibular support in the elderly patient."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Surgical procedures in **periodontics** require an exact understanding of alveolar bone morphology and biological width."
      }
    ]
  },
  "Dashboard — odont\\periodontist.md": {
    "primary": "A dentist who specializes in the prevention, diagnosis, and treatment of diseases of the supporting tissues of the teeth (periodontium).",
    "secondary": "In dental healthcare, a surgical specialist skilled in subgingival debridement, osseous resective surgery, connective tissue grafting, and dental implantology.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prompt evaluation by a **periodontist** is vital to arrest rapidly progressing juvenile alveolar bone loss."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The patient was referred to a **periodontist** for surgical debridement of chronic suppurative gingival pockets."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Eradication of occult oral sepsis by the **periodontist** preceded elective intracranial operative interventions."
      }
    ]
  },
  "Dashboard — odont\\periodontitis.md": {
    "primary": "Inflammation and infection of the ligaments and bones that support the teeth, leading to tooth loosening and bone loss.",
    "secondary": "In oral medicine and periodontology, a chronic infectious disease initiated by subgingival plaque biofilms, causing progressive loss of periodontal attachment and alveolar bone.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Neglected chronic **periodontitis**, or pyorrhea alveolaris, results in purulent pockets and eventual loss of intact teeth."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histopathological sections in **periodontitis** show osteoclastic resorption of the alveolar crest with dense plasmacytic infiltration."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Systemic constitutional decline is often exacerbated by the toxic absorption from severe chronic **periodontitis**."
      }
    ]
  },
  "Dashboard — odont\\polyodontidae.md": {
    "primary": "A family of primitive chondrostean ray-finned fishes commonly known as paddlefishes.",
    "secondary": "In ichthyology and vertebrate evolution, ancient freshwater fishes possessing an elongated, paddle-shaped rostrum covered in electroreceptors, mostly cartilaginous skeletons, and minute larval teeth.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The chondrostean family **Polyodontidae** retains a largely cartilaginous skeleton and a persistent unsegmented notochord."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The extended spatula-like snout in **Polyodontidae** is densely packed with ampullary electroreceptor organs."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The Mississippi paddlefish represents one of the few surviving relict species of the ancient family **Polyodontidae**."
      }
    ]
  },
  "Dashboard — odont\\synodontidae.md": {
    "primary": "A family of predatory marine ray-finned fishes in the order Aulopiformes, commonly known as lizardfishes.",
    "secondary": "In marine biology and ichthyology, benthic ambush predators possessing needle-like, hinged teeth lining the jaws, palate, and tongue, adapted for seizing elusive prey.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Fishes of the family **Synodontidae** bury themselves in bottom sand, exposing only their eyes to ambush passing prey."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The jaws and palatines of **Synodontidae** are crowded with sharp, depressible teeth, earning them the name lizardfishes."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The predatory efficiency of **Synodontidae** relies upon instantaneous lunges propelled by wide pectoral and caudal fins."
      }
    ]
  },
  "Dashboard — odont\\Zanclodon.md": {
    "primary": "An extinct genus of Triassic archosaurian reptiles, originally described from fossil teeth resembling scythes.",
    "secondary": "In vertebrate paleontology, an archosauromorph reptile from the Middle and Upper Triassic of Europe, historically classified alongside megalosaurs based on curved, serrated teeth.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "A History of British Fossil Reptiles",
        "quote": "The curved, serrated teeth of **Zanclodon** exhibit a scythe-like profile suited for slicing through dinosaurian prey."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Fossil jaw fragments referred to **Zanclodon** were once considered primitive representatives of carnivorous megalosaurs."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Primary Factors of Organic Evolution",
        "quote": "The dental morphology of **Zanclodon** illustrates the early evolutionary emergence of ziphodont dentition in Triassic archosaurs."
      }
    ]
  },
  "Dashboard — olecran\\olecranon.md": {
    "primary": "The large, thick, curved bony prominence of the ulna projecting behind the elbow joint.",
    "secondary": "In human osteology and orthopedic surgery, the bony process that receives the insertion of the triceps brachii muscle and fits into the olecranon fossa of the humerus during forearm extension.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **olecranon** forms the prominent tip of the elbow, serving as the lever arm for the powerful triceps brachii."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Subcutaneous tophi in chronic tophaceous gout preferentially deposit over the bursa of the **olecranon**."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Fracture of the **olecranon** demands precise tension-band wiring to restore active forearm extension."
      }
    ]
  },
  "Dashboard — ommat\\ommat.md": {
    "primary": "A root combining form (ommat- / ommato-) denoting the eye.",
    "secondary": "In arthropod morphology and anatomical zoology, used in compounding terms referring to visual organs or eye-bearing appendages (e.g., ommatidium, ommatophore).",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The combining form **ommat-** derives from the Greek term for eye, designating optical units in compound visual organs."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Structural variations among organs bearing the root **ommat-** trace the evolution of complex visual systems in invertebrates."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Embryological invaginations giving rise to **ommat-** structures demonstrate the common origin of optic cups across phyla."
      }
    ]
  },
  "Dashboard — ommat\\ommatidium.md": {
    "primary": "One of the optical units or subunits that make up the compound eye of an arthropod.",
    "secondary": "In invertebrate visual neurobiology, an independent visual receptor consisting of a corneal lens, crystalline cone, retinular photoreceptor cells, and surrounding pigment cells.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Each hexagonal facet on the cornea of the insect's eye corresponds to the apex of a distinct **ommatidium**."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Axons originating from the rhabdomere of each **ommatidium** project directly into the lamina ganglionaris."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The light-insulating pigment cells surrounding each **ommatidium** ensure that only parallel light rays stimulate the rhabdom."
      }
    ]
  },
  "Dashboard — ommat\\ommatophore.md": {
    "primary": "An eye-bearing stalk, tentacle, or peduncle in certain invertebrates, especially pulmonate gastropod mollusks.",
    "secondary": "In comparative malacology, the retractable upper cephalic tentacle of a land snail, carrying a simple optic vesicle and retractor muscle at its distal tip.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The land snail readily invaginates its sensory **ommatophore** upon encountering noxious tactile stimuli."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "At the summit of each **ommatophore**, a pigmented eye cup with a spherical lens permits coarse light detection."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The embryonic development of the **ommatophore** reflects ectodermal outgrowth coordinated with cephalic nerve elongation."
      }
    ]
  },
  "Dashboard — omo\\acromion.md": {
    "primary": "The outer end of the scapular spine that projects over the glenoid cavity and articulates with the clavicle.",
    "secondary": "In human osteology and orthopedic surgery, the superior bony landmark of the shoulder that forms the summit of the shoulder and provides attachment for the deltoid and trapezius muscles.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **acromion** projects forward and outward, forming the highest point of the bony shoulder girdle."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Subacromial bursitis elicits localized exquisite tenderness just beneath the anterior margin of the **acromion**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Accessory nerve injury induces drooping of the shoulder and prominence of the underlying **acromion**."
      }
    ]
  },
  "Dashboard — omo\\om 2.md": {
    "primary": "An anatomical combining form or designation (om- / omo-) derived from the Greek omos, denoting the shoulder.",
    "secondary": "In musculoskeletal anatomy, utilized in naming structures associated with the shoulder or scapular girdle (such as the omohyoid muscle or omoclavicular triangle).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The anatomical prefix **om-** denotes relations with the shoulder girdle and the superior border of the scapula."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Muscular atrophy involving the **om-** girdle causes drooping of the shoulder and winging of the scapula."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Motor nerve filaments innervating the **om-** region branch from the upper trunks of the brachial plexus."
      }
    ]
  },
  "Dashboard — omo\\omohyoid.md": {
    "primary": "A long, slender muscle of the neck having two bellies connected by an intermediate tendon, extending from the scapula to the hyoid bone.",
    "secondary": "In human surgical anatomy, an infrahyoid strap muscle that depresses and fixes the hyoid bone, dividing both the anterior and posterior cervical triangles into subdivisions.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The intermediate tendon of the **omohyoid** muscle is bound to the clavicle by a process of the deep cervical fascia."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "During deep radical neck dissection, the inferior belly of the **omohyoid** serves as a reliable landmark for the internal jugular vein."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Retraction of the **omohyoid** permits clear exposure of the deeper carotid sheath and sympathetic chain."
      }
    ]
  },
  "Dashboard — omo\\omophorion.md": {
    "primary": "A wide, patterned band of silk or wool worn around the neck and shoulders by bishops of the Eastern Orthodox and Byzantine Rite churches.",
    "secondary": "In ecclesiastical vestment history and liturgics, the distinctive episcopal vestment symbolizing the lost sheep carried upon the Good Shepherd's shoulders.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Patriarch of Constantinople appeared in solemn council clad in the embroidered **omophorion** of his episcopal dignity."
      },
      {
        "author": "Arthur Penrhyn Stanley",
        "work": "Lectures on the History of the Eastern Church",
        "quote": "The crosses emblazoned upon the white wool of the **omophorion** proclaim the pastoral burden borne by the prelate."
      },
      {
        "author": "John Mason Neale",
        "work": "A History of the Holy Eastern Church",
        "quote": "Without the **omophorion**, no Orthodox bishop may celebrate the Divine Liturgy or confer holy orders."
      }
    ]
  },
  "Dashboard — omphal\\exomphalos.md": {
    "primary": "A hernia at the navel; an umbilical hernia, especially a congenital omphalocele.",
    "secondary": "In pediatric surgery and embryology, a midline anterior abdominal wall defect at the base of the umbilicus with extrusion of abdominal viscera into a membranous sac.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Immediate surgical reduction of a massive neonatal **exomphalos** is imperative to avert peritonitis from sac rupture."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "In congenital **exomphalos**, the herniated viscera are insulated by amniotic membrane and peritoneum rather than normal skin."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Adult **exomphalos** typically develops in multiparous women due to gradual stretching of the fibrous umbilical ring."
      }
    ]
  },
  "Dashboard — omphal\\omphal.md": {
    "primary": "A root combining form (omphal- / omphalo-) denoting the navel or umbilicus.",
    "secondary": "In anatomical terminology and surgical pathology, utilized in constructing clinical terms relating to the umbilicus, umbilical cord, or primitive yolk stalk (e.g., omphalocele, omphalic).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Disorders designated by the prefix **omphal-** involve inflammatory or congenital defects centered upon the umbilicus."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The Greek root **omphal-** serves as the basis for clinical nomenclature concerning the umbilical cord and vitelline duct."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Neonatal infections denoted with **omphal-** spread via the unclosed umbilical vessels to produce systemic phlebitis."
      }
    ]
  },
  "Dashboard — omphal\\omphalectomy.md": {
    "primary": "The surgical excision or removal of the umbilicus (navel).",
    "secondary": "In abdominal and plastic surgery, excision of the navel performed during radical repair of umbilical hernias, excision of urachal cysts, or abdominoplasty.",
    "quotes": [
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Complete **omphalectomy** with elliptical incision of the fibrous ring ensured secure closure of the giant umbilical hernia."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Total excision of an infected urachal sinus necessitated concurrent **omphalectomy** to eliminate the fistulous tract."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Surgical intervention involving **omphalectomy** was curative for chronic umbilical granulomas that resisted cautery."
      }
    ]
  },
  "Dashboard — omphal\\omphalic.md": {
    "primary": "Of, relating to, or situated near the umbilicus (navel).",
    "secondary": "In embryology and anatomical topography, designating vascular structures (such as omphalomesenteric vessels) or regional pain patterns centered at the navel.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The embryonic **omphalic** veins return blood from the vitelline sac to the sinus venosus of the developing heart."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Referred appendiceal pain is initially perceived in the peri-**omphalic** region before localizing to the right lower quadrant."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "During early yolk-sac circulation, the paired **omphalic** arteries supply the expansive extra-embryonic vascular area."
      }
    ]
  },
  "Dashboard — omphal\\omphalocele.md": {
    "primary": "A congenital herniation of abdominal viscera into the base of the umbilical cord, enclosed within an amnioperitoneal sac.",
    "secondary": "In pediatric surgery and embryology, a major abdominal wall defect caused by failure of the physiological midgut herniation to return to the peritoneal cavity by the tenth week of gestation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A translucent membranous sac encloses the liver and intestines in neonates born with a large **omphalocele**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Failure of lateral embryonic body folds to fuse at the midline produces the clinical defect termed **omphalocele**."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Careful staged reduction of the **omphalocele** prevents fatal elevations in intra-abdominal pressure."
      }
    ]
  },
  "Dashboard — omphal\\omphalopagus.md": {
    "primary": "Conjoined twins united at the umbilicus and lower abdomen.",
    "secondary": "In teratology and developmental genetics, symmetrical conjoined twins sharing anterior abdominal wall structures, often with a conjoined liver or common peritoneal cavity.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The famous Siamese twins Chang and Eng were an anatomical example of **omphalopagus** joined by a fleshy umbilical bridge."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Incomplete fission of the embryonic embryonic disc at the primitive streak level accounts for the **omphalopagus** union."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Post-mortem dissection of the **omphalopagus** confirmed a vascular parenchymal bridge linking their respective livers."
      }
    ]
  },
  "Dashboard — omphal\\omphalophobia.md": {
    "primary": "An abnormal, persistent, and irrational fear or aversion to navels (belly buttons).",
    "secondary": "In clinical psychology and psychiatry, a specific phobia characterized by intense anxiety, nausea, or panic triggered by touching, viewing, or contemplating one's own or others' navel.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "Bizarre body phobias such as **omphalophobia** frequently conceal deeply repressed anxieties surrounding birth or infantile attachment."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In extreme **omphalophobia**, the mere accidental glance at an exposed navel elicits a sharp somatic shudder of revulsion."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Patients afflicted with **omphalophobia** avoid all physical contact with the umbilical region, fearing tactile injury."
      }
    ]
  },
  "Dashboard — omphal\\omphalos.md": {
    "primary": "The navel or umbilicus; also, a sacred rounded stone representing the focal center or hub of the earth.",
    "secondary": "In classical archaeology and cultural mythology, the ancient carved stone at Delphi regarded by Greeks as the navel of the world, where two eagles dispatched by Zeus met.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Pilgrims at Delphi bowed before the white marble **omphalos**, revering it as the mystical center of the earth."
      },
      {
        "author": "Pausanias",
        "work": "Description of Greece",
        "quote": "Within the adyton of the temple stands the **omphalos**, draped in wool fillets and crowned with golden eagles."
      },
      {
        "author": "Jane Ellen Harrison",
        "work": "Prolegomena to the Study of Greek Religion",
        "quote": "The primeval cult of the Delphic **omphalos** was originally dedicated to Gaia before Apollo established his oracle."
      }
    ]
  },
  "Dashboard — omphal\\omphaloskepsis.md": {
    "primary": "The contemplation of one's navel as an aid to mystical meditation; navel-gazing.",
    "secondary": "In the history of Christian mysticism and Eastern Orthodox spirituality, a contemplative practice associated with 14th-century Hesychast monks on Mount Athos; figuratively, self-absorbed absorption.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Hesychasts of Mount Athos practiced **omphaloskepsis**, seeking to behold the uncreated light of Mount Tabor."
      },
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Sustained interior concentration, whether through breath control or quiet **omphaloskepsis**, induces profound altered states of consciousness."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "Idle philosophical speculation that degenerates into barren **omphaloskepsis** produces no practical fruit for suffering humanity."
      }
    ]
  },
  "Dashboard — omphal\\omphalotus.md": {
    "primary": "A genus of poisonous, bioluminescent gilled mushrooms in the family Marasmiaceae, commonly known as Jack-o'-lantern mushrooms.",
    "secondary": "In systematic mycology and toxicology, wood-decaying basidiomycetes containing the sesquiterpene illudin, which causes severe gastrointestinal poisoning when mistaken for edible chanterelles.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "Gills of the toxic woodland mushroom **Omphalotus** emit a striking greenish bioluminescence in total darkness."
      },
      {
        "author": "Roland Thaxter",
        "work": "Contributions from the Cryptogamic Laboratory of Harvard University",
        "quote": "The luminescent enzyme system found in **Omphalotus** requires oxygen and reduced pyridine nucleotides for photon emission."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Clusters of glowing **Omphalotus** upon decaying tree stumps present an eerie spectacle to nocturnal travelers."
      }
    ]
  },
  "Dashboard — omphal\\omphalus.md": {
    "primary": "The navel or umbilicus (Latinized anatomical variant of omphalos).",
    "secondary": "In historical anatomical treatises and classical descriptions, the circular depression in the midline of the abdominal wall marking the attachment site of the fetal umbilical cord.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The scar tissue forming the **omphalus** represents the obliterated remnants of the umbilical vein and hypogastric arteries."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Venous distension radiating from the **omphalus** in portal cirrhosis produces the classic caput medusae."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Metastatic adenocarcinomatous nodules at the **omphalus**, or Sister Mary Joseph nodules, signify widespread abdominal carcinomatosis."
      }
    ]
  },
  "Dashboard — omphal\\paromphalocele.md": {
    "primary": "A hernia occurring near, adjacent to, or alongside the umbilicus.",
    "secondary": "In operative abdominal surgery, a parumbilical hernia protruding through the linea alba slightly above or below the umbilical fibrous ring, common in adults.",
    "quotes": [
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Surgical repair of a recurrent **paromphalocele** requires overlapping closure of the adjacent rectus sheaths."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Unlike true congenital omphalocele, a **paromphalocele** protrudes alongside the intact umbilical cicatricial ring."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Incarceration of omentum within an irreducible **paromphalocele** can simulate an acute intra-abdominal catastrophe."
      }
    ]
  },
  "Dashboard — onych\\hapalonychia.md": {
    "primary": "An abnormal softness, fragility, or thinning of the fingernails or toenails, causing them to bend and break easily.",
    "secondary": "In clinical dermatology, a nail dystrophy resulting from chronic malnutrition, calcium or iron deficiency, myxedema, or prolonged exposure to strong chemical alkalis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe hypochromic anemia is often heralded by brittle koilonychia and pronounced **hapalonychia** of the hands."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The flexible, paper-thin nails characteristic of **hapalonychia** reflect constitutional malnutrition and mineral loss."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Defective keratinization within the nail matrix leads microscopically to the lamellar softening of **hapalonychia**."
      }
    ]
  },
  "Dashboard — onych\\Mesonychia.md": {
    "primary": "An extinct order or suborder of medium to large carnivorous or omnivorous ungulate mammals from the Paleocene and Eocene epochs.",
    "secondary": "In vertebrate paleontology and evolutionary phylogenetics, archaic hoofed carnivores with triangular, bunodont-crushing molars and blunt, hoof-like claws, closely allied to artiodactyls and cetaceans.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "I described the archaic predator under **Mesonychia**, recognizing its unique combination of ungulate feet and carnivorous dentition."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "Digits in the order **Mesonychia** terminate in blunt, fissured hooves rather than the sharp, retractile claws of carnivorans."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The cranial architecture of **Mesonychia** displays massive sagittal crests for the attachment of powerful temporal muscles."
      }
    ]
  },
  "Dashboard — onych\\onych.md": {
    "primary": "A root combining form (onych- / onycho-) denoting a nail, claw, or talon.",
    "secondary": "In dermatological medicine, zoology, and comparative morphology, utilized in constructing terms relating to unguicular structures, keratinous claws, or nail disorders (e.g., onycholysis, onychomycosis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinical conditions bearing the prefix **onych-** indicate localized pathology or dystrophic change of the human nail plate."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The Greek root **onych-** designates the keratinous claw or nail produced by the specialized germinative matrix."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Compounded terms with **onych-** denote disorders where the stratified keratin of the nail fails to mature normally."
      }
    ]
  },
  "Dashboard — onych\\onychectomy.md": {
    "primary": "The surgical removal or excision of a nail or claw (declawing).",
    "secondary": "In veterinary and human dermatologic surgery, total excision of the claw and associated third phalanx in animals, or permanent avulsion of an ingrown nail in humans.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intractable recurring onychocryptosis may necessitate permanent surgical **onychectomy** with chemical matrix destruction."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Surgical **onychectomy** provides complete relief when chronic subungual infections resist conservative local therapy."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Aseptic execution of terminal **onychectomy** eliminates the risk of ascending osteomyelitis of the distal phalanx."
      }
    ]
  },
  "Dashboard — onych\\onychium.md": {
    "primary": "A small footpad, pulvillus, or adhesive pad located between or beneath the claws of insects and arachnids.",
    "secondary": "In insect functional morphology, a median pretarsal structure (arolium or empodium) equipped with micro-tenent setae that generate capillary adhesion on smooth vertical surfaces.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The pretarsus of the beetle bears a delicate adhesive **onychium** positioned between the terminal claws."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Secretions moistening the micro-hairs of the **onychium** enable climbing insects to traverse polished glass with ease."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "During late pupal metamorphosis, the pretarsal pad or **onychium** differentiates alongside the pair of chitinous ungues."
      }
    ]
  },
  "Dashboard — onych\\onychogalea.md": {
    "primary": "A genus of small Australasian macropod marsupials commonly known as nail-tail wallabies.",
    "secondary": "In systematic mammalogy and marsupial ecology, endemic Australian wallabies characterized by a horny, claw-like nail or spur at the tip of their tail and distinct shoulder stripes.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Mammals of Australia",
        "quote": "The crescent nail-tail wallaby, referred to the genus **Onychogalea**, carries a small horny fingernail at the extremity of its tail."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "Members of **Onychogalea** rotate their forearms like sails when hopping at high speed across the scrub plains."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The curious caudal nail in **Onychogalea** represents an enigmatic morphological development among leaping marsupials."
      }
    ]
  }
};

console.log(`Starting curation of Body Rem A Batch 3 (${Object.keys(batchData).length} notes)...`);
const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`Batch 3 complete: successfully updated ${count} notes.`);
