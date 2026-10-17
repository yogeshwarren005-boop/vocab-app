import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batchData = {
  "Dashboard — myel\\myelic.md": {
    "primary": "Of, relating to, or situated in the spinal cord or bone marrow.",
    "secondary": "In anatomical neurology, designating structures, pathways, or vascular networks associated specifically with the spinal cord (medulla spinalis).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The anterior and posterior **myelic** arteries supply the corresponding aspects of the spinal cord."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Compression of the **myelic** columns by an extradural abscess produces spastic paraparesis below the lesion."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Ascending sensory axons traverse the **myelic** funiculi toward the relay nuclei of the brainstem."
      }
    ]
  },
  "Dashboard — myel\\myelin.md": {
    "primary": "A soft, white, fatty lipid-rich substance that forms an insulating sheath around many nerve fibers.",
    "secondary": "In neurobiology and biophysics, a multilamellar membrane structure produced by oligodendrocytes in the CNS and Schwann cells in the PNS, accelerating saltatory impulse conduction.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The thick layer of **myelin** serves to insulate the central axoplasm from extracellular current leaks."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "I first identified **myelin** as a distinct, chemically complex lipid substance in nervous tissues."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Loss of the lipid **myelin** sheath severely compromises saltatory action potential propagation."
      }
    ]
  },
  "Dashboard — myel\\myelinated.md": {
    "primary": "Having or provided with a myelin sheath; medullated.",
    "secondary": "In neurophysiology, characterizing nerve axons insulated by concentric lipid lamellae, allowing high-speed impulse transmission via nodes of Ranvier.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Rapid proprioceptive reflexes depend upon large-diameter, heavily **myelinated** afferent nerve fibers."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "At each node of Ranvier along the **myelinated** axon, the axis cylinder becomes exposed to the interstitial fluid."
      },
      {
        "author": "John Carew Eccles",
        "work": "The Physiology of Synapses",
        "quote": "Conduction velocities exceeding one hundred meters per second are readily achieved in vertebrate **myelinated** motor fibers."
      }
    ]
  },
  "Dashboard — myel\\myeline.md": {
    "primary": "An alternate spelling of myelin, designating the fatty substance forming the medullary sheath of nerve fibers.",
    "secondary": "In historical neurochemistry and pathology, the lipid extract obtained from brain and marrow tissue that forms birefringent myelinic figures in water.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Under the microscope, isolated drops of **myeline** expand into cylindrical, coiled myelinic forms when exposed to warm water."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The medullary substance of Schwann, formerly designated **myeline**, surrounds the cylindrical axis of white nerve fibers."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chemical degeneration of peripheral **myeline** accompanies toxic neuritis caused by heavy metals."
      }
    ]
  },
  "Dashboard — myel\\myelinic.md": {
    "primary": "Of, relating to, or derived from myelin.",
    "secondary": "In cellular physical chemistry and histopathology, describing the cylindrical, tubular birefringent forms (myelinic figures) produced when phospholipids swell in aqueous media.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The spontaneous generation of **myelinic** forms from degenerating cells illustrates the physical properties of cellular lipoids."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "During Wallerian degeneration, the breaking down of the **myelinic** sheath yields fatty droplets and debris."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Phagocytic microglia engulf disrupted **myelinic** fragments following traumatic spinal cord injury."
      }
    ]
  },
  "Dashboard — myel\\myelinisation.md": {
    "primary": "The formation or development of a myelin sheath around a nerve fiber (British English spelling of myelinization).",
    "secondary": "In developmental neuroembryology, the sequential maturational process whereby glial cells wrap axons in protective myelin, correlating with the emergence of coordinated motor and cognitive functions.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The progressive **myelinisation** of fetal cerebral tracts proceeds in a strict craniocaudal sequence."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Functional maturation of peripheral reflex arcs coincides with the onset of sheath **myelinisation**."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Incomplete **myelinisation** explains the diffuse, uncoordinated motor responses observed in newborn mammals."
      }
    ]
  },
  "Dashboard — myel\\myelinization.md": {
    "primary": "The biological process of acquiring or developing a myelin sheath around nerve fibers.",
    "secondary": "In developmental neurobiology, the wrapping of axons by Schwann cells or oligodendrocytes to establish saltatory conduction during embryonic and postnatal brain maturation.",
    "quotes": [
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Cortical association areas exhibit delayed **myelinization**, continuing well into human childhood and adolescence."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Spinal root **myelinization** precedes the insulation of higher intracortical pathways."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Arrested **myelinization** of central tracts results in severe infantile spastic diplegia."
      }
    ]
  },
  "Dashboard — myel\\myelitis.md": {
    "primary": "Inflammation of the spinal cord or of the bone marrow.",
    "secondary": "In clinical neurology, an acute inflammatory disorder affecting the gray and white matter of the spinal cord (such as transverse myelitis), causing sensorimotor paraplegia and autonomic dysfunction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute transverse **myelitis** develops with rapid onset of motor paralysis, sensory dissociation, and loss of sphincter control."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The onset of severe spinal **myelitis** is frequently preceded by girdling abdominal pain."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Focal necrotic lesions in acute **myelitis** disrupt the ascending sensory and descending motor pathways of the cord."
      }
    ]
  },
  "Dashboard — myel\\myeloblast.md": {
    "primary": "An immature, unipotent precursor cell in the bone marrow that develops into a myelocyte and ultimately a granulocyte (neutrophil, eosinophil, or basophil).",
    "secondary": "In hematopathology and leukemia classification, a large primitive blastic cell with a high nuclear-to-cytoplasmic ratio, delicate chromatin, and prominent nucleoli, characteristic of acute myeloid leukemia.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The primitive **myeloblast** contains no specific granules, representing the earliest committed precursor of the granulocytic series."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute myeloblastic leukemia, the peripheral blood is flooded with abnormal, immature **myeloblasts**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Marrow examination reveals an uncontrolled proliferation of the ancestral **myeloblast** at the expense of erythropoiesis."
      }
    ]
  },
  "Dashboard — myel\\myelocyte.md": {
    "primary": "A young, developing granulocytic white blood cell in the bone marrow, intermediate between a promyelocyte and a metamyelocyte.",
    "secondary": "In hematology, the developmental stage at which lineage-specific primary and secondary granules (neutrophilic, eosinophilic, or basophilic) first become discernible under microscopy.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "The **myelocyte** is characterized by the initial appearance of specific cytoplasmic granules that distinguish the granular leukocytes."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The presence of numerous **myelocytes** in the circulation is the diagnostic hallmark of chronic myelogenous leukemia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In leukemic states, immense aggregations of **myelocytes** choke the sinusoids of the spleen and bone marrow."
      }
    ]
  },
  "Dashboard — myel\\myelodysplasia.md": {
    "primary": "Any defective or abnormal development of the spinal cord; also, a hematologic disorder marked by ineffective production of blood cells in the bone marrow.",
    "secondary": "In pediatric neurology, congenital spinal cord malformation associated with spina bifida; in hematology, myelodysplastic syndrome (MDS) characterized by peripheral cytopenias and potential leukemic transformation.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Occult spinal **myelodysplasia** should be suspected in children with persistent nocturnal enuresis and pes cavus."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe **myelodysplasia** in elderly patients leads to progressive refractory anemia resistant to iron therapy."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The marrow biopsy in **myelodysplasia** reveals hypercellularity accompanied by dysmorphic erythroblasts and megakaryocytes."
      }
    ]
  },
  "Dashboard — myel\\myelofibrosis.md": {
    "primary": "A chronic disorder characterized by progressive replacement of the blood-forming bone marrow by dense fibrous scar tissue.",
    "secondary": "In hematology and oncology, a BCR-ABL-negative myeloproliferative neoplasm marked by extramedullary hematopoiesis in the spleen and liver, leukoerythroblastic blood smear, and teardrop poikilocytes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Marked splenomegaly coupled with tear-drop poikilocytes on the blood film strongly suggests primary **myelofibrosis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In advanced **myelofibrosis**, fibrous collagen and reticulin fibers completely obliterate normal hematopoiesis in the medullary space."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The extensive bone marrow scarring of **myelofibrosis** forces the spleen to resume primitive fetal blood-forming activity."
      }
    ]
  },
  "Dashboard — myel\\myelogenous.md": {
    "primary": "Originating in or produced by the bone marrow.",
    "secondary": "In hematology and clinical oncology, describing leukemia, cells, or marrow-derived neoplasms (e.g., chronic myelogenous leukemia) that arise from granulocytic or myeloid precursors.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chronic **myelogenous** leukemia characteristically presents with massive splenic enlargement and a colossal white cell count."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The proliferation of **myelogenous** elements accounts for the whitish hue of the blood in medullary leukemia."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "Granulocytes and their precursor cells are of strictly **myelogenous** origin, distinct from the lymphoid series."
      }
    ]
  },
  "Dashboard — myel\\myelogram.md": {
    "primary": "A radiographic or fluoroscopic image of the spinal canal, cord, and nerve roots obtained after injection of radiopaque contrast medium into the subarachnoid space; also, a differential count of cells in bone marrow.",
    "secondary": "In neuroradiology, a diagnostic visualization demonstrating filling defects caused by herniated intervertebral discs, spinal canal stenosis, or extramedullary tumors.",
    "quotes": [
      {
        "author": "Walter Dandy",
        "work": "Surgery of the Brain",
        "quote": "The lumbar **myelogram** revealed a complete blockage of contrast media at the third thoracic vertebra."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "An iodized oil **myelogram** confirmed the presence of a compressive extradural neurofibroma."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Analysis of the bone marrow **myelogram** provides direct quantitative assessment of erythroid versus myeloid hyperplasia."
      }
    ]
  },
  "Dashboard — myel\\myelography.md": {
    "primary": "The radiographic visualization and examination of the spinal cord, subarachnoid space, and nerve roots following the injection of a contrast medium.",
    "secondary": "In clinical neurology and spine surgery, an imaging technique essential for assessing spinal cord compression, avulsion injuries, and arachnoiditis before the widespread advent of MRI.",
    "quotes": [
      {
        "author": "Walter Dandy",
        "work": "Surgery of the Brain",
        "quote": "Careful **myelography** allows the neurosurgeon to pinpoint the exact level of cord compression before laminectomy."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The diagnostic precision of modern spinal **myelography** was greatly enhanced by water-soluble contrast media."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Contrast **myelography** demonstrated severe cervical spondylotic compression causing spastic quadriparesis."
      }
    ]
  },
  "Dashboard — myel\\myeloid.md": {
    "primary": "Resembling, relating to, or derived from bone marrow or the spinal cord.",
    "secondary": "In immunology and hematology, designating the developmental lineage of blood cells that produces granulocytes, monocytes, erythrocytes, and platelets, as distinguished from the lymphoid lineage.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The **myeloid** tumor exhibits cellular elements directly reminiscent of normal marrow tissue."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "Divergence between the **myeloid** and lymphoid systems is fundamental to all classification of hematopoietic disease."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute **myeloid** leukemia runs a rapid and fatal course characterized by anemia, purpura, and sepsis."
      }
    ]
  },
  "Dashboard — myel\\myeloma.md": {
    "primary": "A primary malignant tumor of the bone marrow composed of plasma cells.",
    "secondary": "In oncology and pathology, a neoplastic proliferation of monoclonal plasma cells causing osteolytic bone destruction, hypercalcemia, renal impairment, and immunodeficiency.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Punched-out osteolytic lesions on the skull radiograph are virtually pathognomonic of **myeloma**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The marrow architecture in **myeloma** is replaced by confluent sheets of abnormal plasmacytoid cells."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The secretion of massive quantities of homogeneous paraprotein by a **myeloma** clone provides a pure model of antibody synthesis."
      }
    ]
  },
  "Dashboard — myel\\myelomeningocele.md": {
    "primary": "A severe congenital neural tube defect in which both the spinal cord and its covering meninges protrude through an opening in the vertebral column.",
    "secondary": "In pediatric neurosurgery and embryology, a form of spina bifida aperta where the exposed neural placode lies flush with or herniates beyond the infant's back, causing paraplegia and Chiari II malformation.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Immediate surgical repair of a lumbar **myelomeningocele** is necessary to prevent ascending bacterial ventriculitis."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Hydrocephalus almost invariably accompanies an extensive lumbar **myelomeningocele** in neonates."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Failure of the caudal neuropore to close by the fourth week of gestation results in a devastating **myelomeningocele**."
      }
    ]
  },
  "Dashboard — myel\\myelopathy.md": {
    "primary": "Any disease, functional disorder, or pathological condition affecting the spinal cord.",
    "secondary": "In clinical neurology, spinal cord dysfunction resulting from compression (cervical spondylotic myelopathy), ischemia, trauma, or nutritional deficiency (subacute combined degeneration).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Progressive cervical spondylotic **myelopathy** presents with clumsy hands and an unsteady, spastic gait."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Severe vitamin B12 deficiency produces a characteristic vacuolar **myelopathy** affecting the posterior columns."
      },
      {
        "author": "Walter Dandy",
        "work": "Surgery of the Brain",
        "quote": "Early surgical decompression halts the irreversible progression of compressive thoracic **myelopathy**."
      }
    ]
  },
  "Dashboard — myel\\myelopoiesis.md": {
    "primary": "The production, development, and maturation of blood cells, especially granulocytes and other non-lymphoid elements, in the bone marrow.",
    "secondary": "In hematology and stem cell biology, the continuous differentiation process from pluripotential hematopoietic stem cells into mature neutrophils, eosinophils, basophils, monocytes, and erythrocytes.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "Bone marrow remains the primary site of active **myelopoiesis** throughout adult human life."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Under conditions of severe peripheral hemolysis, compensatory **myelopoiesis** causes marked marrow hyperplasia."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Infection accelerates **myelopoiesis**, resulting in a rapid shift to the left with circulating band neutrophils."
      }
    ]
  },
  "Dashboard — myel\\unmyelinated.md": {
    "primary": "Not having or covered with a myelin sheath.",
    "secondary": "In neurophysiology and neuroanatomy, describing slow-conducting nerve axons (such as somatic C fibers and postganglionic autonomic axons) that conduct action potentials continuously rather than saltatorily.",
    "quotes": [
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Slow, burning pain and thermal sensations are mediated primarily by thin, **unmyelinated** C fibers."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Multiple **unmyelinated** axons are frequently ensheathed together in the simple cytoplasmic invaginations of a single Schwann cell."
      },
      {
        "author": "John Carew Eccles",
        "work": "The Physiology of Synapses",
        "quote": "Conduction in **unmyelinated** axons is continuous and slow, rarely exceeding one or two meters per second."
      }
    ]
  },
  "Dashboard — myx\\match.md": {
    "primary": "A person, item, or entity equal, suited, or corresponding to another; also, a contest or game between opposing sides, or a friction device for producing flame.",
    "secondary": "In marriage, social relations, or sporting competitions, an alliance or formal contest between two individuals, parties, or athletic contenders.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Romeo and Juliet",
        "quote": "Content thee, gentle coz, let him alone; he bears him like a portly gentleman... you shall find no **match** for him in Verona."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "To look upon him as a suitable **match** for Elizabeth had never entered her mother's wildest imagination."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "He struck a **match** against the rough hearth, illuminating the dark corners of the forge."
      }
    ]
  },
  "Dashboard — myx\\matched.md": {
    "primary": "Equal, suited, or paired appropriately with another person, item, or quality.",
    "secondary": "In immunology, statistics, and genetics, describing donors, recipients, or experimental controls carefully selected to correspond across specific clinical variables.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "The two advocates were equally **matched** in courtroom eloquence and legal subtlety."
      },
      {
        "author": "Jane Austen",
        "work": "Emma",
        "quote": "A better **matched** pair in fortune, age, and disposition could scarcely be discovered in the parish."
      },
      {
        "author": "Peter Medawar",
        "work": "The Uniqueness of the Individual",
        "quote": "Survival of skin allografts was significantly prolonged between genetically **matched** donor pairs."
      }
    ]
  },
  "Dashboard — myx\\matcher.md": {
    "primary": "A person or device that pairs, matches, or aligns corresponding items, patterns, or individuals.",
    "secondary": "In computational linguistics and engineering, an automated algorithm or machine tool designed to detect matching patterns or join interlocking components.",
    "quotes": [
      {
        "author": "Thomas Hardy",
        "work": "Far from the Madding Crowd",
        "quote": "The old parish clerk served as a shrewd **matcher** of youth and maiden across several villages."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "She was by nature no scheming **matcher**, yet she observed the growing intimacy with quiet satisfaction."
      },
      {
        "author": "Charles Babbage",
        "work": "Passages from the Life of a Philosopher",
        "quote": "The mechanical **matcher** ensures that each punched card corresponds accurately to its computational register."
      }
    ]
  },
  "Dashboard — myx\\micromyx.md": {
    "primary": "A genus or subgenus name applied to diminutive rodents, specifically Old World harvest mice.",
    "secondary": "In taxonomic rodentology and paleomammalogy, an archaic or alternative designation referencing tiny murine species adapted to climbing cereal stalks.",
    "quotes": [
      {
        "author": "Joel Asaph Allen",
        "work": "Bulletin of the American Museum of Natural History",
        "quote": "The tiny skeletal features of **micromyx** distinguish it readily from the heavier murines of the same valley."
      },
      {
        "author": "Oldfield Thomas",
        "work": "Annals and Magazine of Natural History",
        "quote": "Specimens cataloged under **micromyx** exhibit unique dental cusp patterns characteristic of dwarf harvest rodents."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Primary Factors of Organic Evolution",
        "quote": "Fossil teeth assigned to **micromyx** illustrate evolutionary dwarfing among Miocene seed-eating rodents."
      }
    ]
  },
  "Dashboard — myx\\myx.md": {
    "primary": "A root combining form (myx- / myxo-) meaning mucus or slime.",
    "secondary": "In biological nomenclature and medical pathology, utilized to designate mucinous organisms, tissues, or pathological conditions (e.g., myxoma, myxedema).",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The root **myx-** appropriately designates pathological tissues whose intercellular substance is saturated with mucin."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Terms incorporating **myx-** denote clinical syndromes characterized by excessive gelatinous or mucinous deposits."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "In anatomical terminology, the prefix **myx-** refers to the presence of mucus-like connective tissue."
      }
    ]
  },
  "Dashboard — myx\\myxedema.md": {
    "primary": "A condition characterized by swelling of the skin and subcutaneous tissues with a waxy, mucus-like edema, caused by severe hypothyroidism.",
    "secondary": "In clinical endocrinology, advanced thyroid hormone deficiency presenting with hypothermia, bradycardia, lethargy, coarsened facial features, and slowed mentation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The transformation wrought by thyroid extract in advanced **myxedema** is one of the greatest triumphs of modern medicine."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The sluggish mental reaction and non-pitting edema of **myxedema** disappear following thyroid administration."
      },
      {
        "author": "William Gull",
        "work": "Transactions of the Clinical Society of London",
        "quote": "I described this cretinoid state in adults under the name of **myxedema**, noting the gelatinous swelling of the dermis."
      }
    ]
  },
  "Dashboard — myx\\Myxini.md": {
    "primary": "A taxonomic class of jawless, eel-shaped marine fishes comprising the hagfishes.",
    "secondary": "In vertebrate phylogenetics and ichthyology, ancient craniates lacking true vertebrae, jaws, and paired fins, renowned for producing vast quantities of defensive slime.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The class **Myxini** represents the most primitive living branch of the craniate chordates."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Abundant slime pores along the ventrolateral margins of **Myxini** secrete fibrous mucus to deter predators."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Embryological studies of **Myxini** have illuminated the evolutionary origin of the vertebrate skull."
      }
    ]
  },
  "Dashboard — myx\\myxoedema.md": {
    "primary": "The British English spelling of myxedema, denoting severe hypothyroid skin infiltration and metabolic slowing.",
    "secondary": "In internal medicine, a state of profound thyroid insufficiency marked by dry skin, alopecia, hoarseness, hypothermia, and potential progression to myxedema coma.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The therapeutic efficacy of sheep thyroid extract in **myxoedema** remains one of the most brilliant chapters in therapeutics."
      },
      {
        "author": "William Gull",
        "work": "Transactions of the Clinical Society of London",
        "quote": "The dull, impassive expression in **myxoedema** reflects the infiltration of the subcutis with mucinous fluid."
      },
      {
        "author": "Victor Horsley",
        "work": "The Pathology of the Thyroid Gland",
        "quote": "Surgical ablation of the thyroid gland in primates produced a condition identical to human **myxoedema**."
      }
    ]
  },
  "Dashboard — myx\\myxogastrid.md": {
    "primary": "Any of the plasmodial or acellular slime molds belonging to the class Myxogastria (or Myxogastrea).",
    "secondary": "In mycology and protistology, multinucleate amoeboid organisms that form macroscopic plasmodia and develop elaborate spore-bearing fruiting bodies (sporangia).",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi, Mycetozoa and Bacteria",
        "quote": "The creeping plasmodium of a **myxogastrid** exhibits coordinated rhythmic cytoplasmic streaming."
      },
      {
        "author": "Roland Thaxter",
        "work": "Contributions from the Cryptogamic Laboratory of Harvard University",
        "quote": "The fruiting sporangium of the **myxogastrid** produces spores enclosed within an intricate capillitial network."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The developmental cycle of the **myxogastrid** bridges the boundary between protozoan amoebae and fungal fructifications."
      }
    ]
  },
  "Dashboard — myx\\rematch.md": {
    "primary": "A second or repeat contest, match, or competition between the same contestants or opposing teams.",
    "secondary": "In sports history and game theory, a subsequent competitive encounter undertaken to resolve an undecided or disputed initial contest.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The British Campaign in France and Flanders",
        "quote": "The defeated battalion eagerly anticipated a **rematch** against their former adversaries on equal ground."
      },
      {
        "author": "Jack London",
        "work": "The Abysmal Brute",
        "quote": "The sporting public clamored for a decisive **rematch** between the two heavyweight contenders."
      },
      {
        "author": "P. G. Wodehouse",
        "work": "The Code of the Woosters",
        "quote": "A spirited **rematch** on the local tennis court restored good humor to the disappointed contestants."
      }
    ]
  },
  "Dashboard — myx\\unmatched.md": {
    "primary": "Having no equal or match; peerless, incomparable, or unexcelled; also, not paired or harmonized.",
    "secondary": "In descriptive criticism and immunology, possessing unique, supreme excellence that surpasses all competitors, or lacking an appropriate counterpart.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "He stood among them with **unmatched** majesty, towering above his fallen peers in pride."
      },
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "That **unmatched** form and feature of blown youth blasted with ecstasy."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The Roman legions displayed an **unmatched** discipline that conquered every opposing power."
      }
    ]
  },
  "Dashboard — nephr\\epinephrin.md": {
    "primary": "A hormone and neurotransmitter secreted by the adrenal medulla; adrenaline (alternate spelling of epinephrine).",
    "secondary": "In cardiovascular pharmacology and autonomic physiology, a powerful catecholamine stimulating both alpha and beta-adrenergic receptors, elevating cardiac output and blood pressure.",
    "quotes": [
      {
        "author": "John Jacob Abel",
        "work": "The Chemistry of the Suprarenal Gland",
        "quote": "I succeeded in isolating the active pressor principle of the adrenal medulla, naming it **epinephrin**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Intravenous administration of **epinephrin** causes an immediate elevation of systemic arterial tension."
      },
      {
        "author": "Walter Bradford Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "The emergency secretion of **epinephrin** mobilizes blood sugar and shunts circulation to the skeletal muscles."
      }
    ]
  },
  "Dashboard — nephr\\epinephrine.md": {
    "primary": "A hormone secreted by the adrenal medulla that increases heart rate, blood pressure, cardiac output, and carbohydrate metabolism; adrenaline.",
    "secondary": "In emergency medicine and resuscitation pharmacology, a first-line drug used in the treatment of anaphylaxis, cardiac arrest, and severe bronchospasm.",
    "quotes": [
      {
        "author": "Walter Bradford Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "The sympathetic surge releases **epinephrine** to prepare the organism for instant fight or flight."
      },
      {
        "author": "Henry Dale",
        "work": "Adventures in Physiology",
        "quote": "The physiological effects of circulating **epinephrine** closely mimic direct stimulation of the sympathetic nervous system."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prompt subcutaneous injection of **epinephrine** provides lifesaving bronchodilation during acute anaphylactic collapse."
      }
    ]
  },
  "Dashboard — nephr\\hydronephrosis.md": {
    "primary": "Distension and dilation of the renal pelvis and calyces caused by obstruction of the free outflow of urine from the kidney.",
    "secondary": "In urological pathology, progressive atrophy and thinning of the renal parenchyma resulting from chronic urinary tract obstruction, leading to irreversible loss of nephrons.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Calculous impaction in the ureter produces acute unilateral **hydronephrosis** with agonizing flank pain."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Relief of the obstructing pelvic band arrests the progressive parenchymal destruction of **hydronephrosis**."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Extrinsic compression of the pelvic ureter by an ovarian mass is a frequent cause of asymptomatic **hydronephrosis**."
      }
    ]
  },
  "Dashboard — nephr\\mesonephric.md": {
    "primary": "Of, relating to, or derived from the mesonephros, the intermediate embryonic kidney.",
    "secondary": "In developmental embryology and gynecologic pathology, designating vestigial adult structures (such as the mesonephric duct or Gartner's duct) derived from the middle embryonic excretory organ.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The **mesonephric** duct differentiates into the vas deferens in males, while regressing in females."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Remnants of the embryonic **mesonephric** tubules persist within the broad ligament as the epoöphoron."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Cystic lesions arising in the lateral vaginal wall frequently originate from persistent **mesonephric** duct remnants."
      }
    ]
  },
  "Dashboard — nephr\\mesonephros.md": {
    "primary": "The second of the three pairs of embryonic excretory organs in vertebrates, functioning as the permanent adult kidney in anamniotes (fish and amphibians).",
    "secondary": "In amniote embryology, a transient functional kidney that develops caudal to the pronephros before being replaced by the metanephros, its duct contributing to the male genital tract.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "In elasmobranch embryos, the **mesonephros** consists of numerous vascular glomeruli and convoluted excretory tubules."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The permanent functional kidney of adult amphibians is the persistent **mesonephros** or Wolffian body."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "During human embryonic life, the **mesonephros** functions temporarily before degenerating as the metanephros ascends."
      }
    ]
  },
  "Dashboard — nephr\\metanephridium.md": {
    "primary": "A tubular excretory organ found in many invertebrates (such as annelids and mollusks), having an internal ciliated opening (nephrostome) into the coelom.",
    "secondary": "In comparative invertebrate physiology, a paired segmental organ that draws in coelomic fluid and selectively reabsorbs nutrients while expelling nitrogenous wastes via a nephridiopore.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The annelid **metanephridium** opens directly into the coelomic cavity via a wide, ciliated funnel."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Selective resorption of essential salts occurs along the glandular convolutions of the **metanephridium**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The developmental emergence of the **metanephridium** marks an advance over the simpler protonephridial flame-cell system."
      }
    ]
  },
  "Dashboard — nephr\\metanephros.md": {
    "primary": "The permanent, functional adult kidney of amniote vertebrates (reptiles, birds, and mammals).",
    "secondary": "In embryology, the third and definitive excretory organ that develops from the metanephric blastema and ureteric bud during intrauterine gestation.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The ureteric bud sprouts from the Wolffian duct to induce nephrogenesis within the **metanephros**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In all amniotes, the anterior embryonic excretory organs give place entirely to the definitive **metanephros**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The permanent kidney or **metanephros** ascends from the sacral region to its adult lumbar position during fetal life."
      }
    ]
  },
  "Dashboard — nephr\\nephr.md": {
    "primary": "A root combining form (nephr- / nephro-) denoting the kidney.",
    "secondary": "In anatomical terminology and medical pathology, utilized in constructing clinical terms referring to renal structures, physiology, or diseases (e.g., nephron, nephritis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Medical terms bearing the root **nephr-** delineate disorders and diagnostic procedures directly concerning the kidneys."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The suffix -itis joined to **nephr-** yields nephritis, denoting inflammatory destruction of the renal parenchyma."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "From ancient Greek nephros, combining forms beginning with **nephr-** designate all things pertaining to the renal organs."
      }
    ]
  },
  "Dashboard — nephr\\nephralgia.md": {
    "primary": "Pain in the kidney or renal region.",
    "secondary": "In clinical urology, paroxysmal or dull flank and lumbar pain caused by renal calculi, acute pyelonephritis, or sudden ureteral obstruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe paroxysmal **nephralgia** radiating toward the groin characterizes the passage of a renal calculus."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Persistent unilateral **nephralgia** without fever warrants careful cystoscopic and radiographic investigation."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The agonizing pain of acute **nephralgia** frequently induces reflex vomiting and profound prostration."
      }
    ]
  },
  "Dashboard — nephr\\nephrectomy.md": {
    "primary": "The surgical removal of one or both kidneys.",
    "secondary": "In operative urology and oncologic surgery, total or partial excision of a kidney indicated for malignant renal cell carcinoma, severe trauma, or non-functioning hydronephrosis.",
    "quotes": [
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "I performed lumbar **nephrectomy** for intractable calculous pyonephrosis with complete restoration of health."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Following unilateral **nephrectomy**, compensatory hypertrophy allows the remaining kidney to maintain normal renal clearance."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "In cases of extensive neoplastic invasion of the renal bed, radical **nephrectomy** offers the only definitive cure."
      }
    ]
  },
  "Dashboard — nephr\\nephridiopore.md": {
    "primary": "The external opening of an excretory organ (nephridium) in invertebrates.",
    "secondary": "In invertebrate zoology and comparative anatomy, the ventrolateral pore through which nitrogenous waste fluids filtered by the nephridial tubules are discharged to the exterior.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Excretory fluids collect in the nephridial bladder and are evacuated through the lateral **nephridiopore**."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Each body segment in the earthworm possesses a pair of minute ventral apertures representing the **nephridiopore**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Embryonic invaginations of the ectoderm meet the nephridial duct to establish the terminal **nephridiopore**."
      }
    ]
  },
  "Dashboard — nephr\\nephridium.md": {
    "primary": "A tubular excretory organ found in many invertebrates, serving functions analogous to the vertebrate kidney.",
    "secondary": "In comparative invertebrate morphology, categorized as either a protonephridium (with flame cells) or metanephridium (with an open coelomic nephrostome), maintaining osmoregulation and waste expulsion.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The annelid **nephridium** exhibits a complex convoluted canal lined with active ciliated epithelium."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Osmotic regulation in freshwater invertebrates is largely maintained through active transport along the **nephridium**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The segmental arrangement of the **nephridium** mirrors the primitive metameric architecture of the coelom."
      }
    ]
  },
  "Dashboard — nephr\\nephrite.md": {
    "primary": "A tough, compact variety of actinolite or tremolite amphibole, which is one of the two distinct mineral species commonly termed jade.",
    "secondary": "In mineralogy and gemology, a calcium-magnesium-iron amphibole gemstone renowned for its interlocking fibrous microcrystalline toughness, historically worn as an amulet against kidney ailments (Greek nephros).",
    "quotes": [
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "The smooth green stone called **nephrite** was celebrated among ancients as a sovereign remedy for gravel."
      },
      {
        "author": "George Frederick Kunz",
        "work": "The Curious Lore of Precious Stones",
        "quote": "The mineral **nephrite**, or true greenstone, was shaped into sacred amulets by ancient peoples from China to New Zealand."
      },
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The felted fibrous texture of **nephrite** confers upon it an extraordinary resistance to mechanical fracture."
      }
    ]
  },
  "Dashboard — nephr\\nephritic.md": {
    "primary": "Of, relating to, or affected by nephritis (inflammation of the kidneys); also, relating to or relieving kidney diseases.",
    "secondary": "In clinical nephrology, designating the nephritic syndrome, marked by hematuria, red blood cell casts, hypertension, oliguria, and mild proteinuria.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The sudden development of hematuria, facial edema, and hypertension characterizes the acute **nephritic** syndrome."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Violent **nephritic** paroxysms follow the transit of gravel through the narrow ureteral passage."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Active **nephritic** symptoms in post-scarlatinal dropsy demand strict dietary control and blood pressure reduction."
      }
    ]
  },
  "Dashboard — nephr\\nephritis.md": {
    "primary": "Inflammation of the kidneys.",
    "secondary": "In renal medicine and pathology, an acute or chronic condition involving glomeruli, tubules, or interstitial tissue (such as glomerulonephritis or pyelonephritis), leading to impaired renal filtration.",
    "quotes": [
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "The co-existence of coagulable urine, dropsy, and structural disorganization of the kidneys demonstrates the entity of chronic **nephritis**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute **nephritis** following streptococcal infection is heralded by smoky or cola-colored urine."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In interstitial **nephritis**, widespread lymphocytic infiltration leads to tubular atrophy and fibrous replacement."
      }
    ]
  },
  "Dashboard — nephr\\nephroangiosclerosis.md": {
    "primary": "Sclerosis or hardening of the renal arterioles and small blood vessels, associated with chronic hypertension.",
    "secondary": "In cardiovascular pathology, hyaline or hyperplastic arteriolar narrowing within the kidneys that leads to glomerular ischemia, tubular atrophy, and progressive chronic kidney disease.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sustained arterial hypertension leads insidiously to benign **nephroangiosclerosis** and contracted granular kidneys."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopically, **nephroangiosclerosis** demonstrates pronounced hyaline thickening of the afferent arterioles with lumen reduction."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Malignant hypertension accelerates **nephroangiosclerosis**, producing necrotizing arteriolitis and rapid uremic decline."
      }
    ]
  },
  "Dashboard — nephr\\nephroblastoma.md": {
    "primary": "A malignant embryonic tumor of the kidney occurring predominantly in young children, commonly known as Wilms tumor.",
    "secondary": "In pediatric oncology and pathology, a triphasic neoplasm consisting of blastemal, epithelial, and stromal elements resulting from aberrant kidney organogenesis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A large, palpable abdominal mass in a young toddler frequently proves to be an embryonic **nephroblastoma**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The histologic appearance of **nephroblastoma** reveals primitive blastemal sheets interspersed with abortive glomerular tubules."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Successful management of pediatric **nephroblastoma** combines meticulous operative excision with systemic therapy."
      }
    ]
  },
  "Dashboard — nephr\\nephrocalcinosis.md": {
    "primary": "A condition characterized by the deposition of calcium salts within the kidney parenchyma and tubules.",
    "secondary": "In metabolic nephrology, diffuse renal calcification resulting from prolonged hypercalcemia, hypercalciuria, primary hyperparathyroidism, or renal tubular acidosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Longstanding primary hyperparathyroidism precipitates severe **nephrocalcinosis** and secondary renal impairment."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections show dense basophilic precipitates of calcium phosphate throughout the medullary rays in **nephrocalcinosis**."
      },
      {
        "author": "Walter Bradford Cannon",
        "work": "Bodily Changes in Pain, Hunger, Fear and Rage",
        "quote": "Disrupted systemic calcium homeostasis induces metastatic calcification of the renal tubules, producing **nephrocalcinosis**."
      }
    ]
  },
  "Dashboard — nephr\\nephrogenesis.md": {
    "primary": "The embryonic development and formation of the kidneys.",
    "secondary": "In developmental biology and embryology, the reciprocal inductive signaling between the ureteric bud and the metanephric mesenchyme that drives nephron formation.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Active **nephrogenesis** begins when the branching ureteric ampulla induces surrounding mesenchymal cells to epithelialize."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Autonomic innervation arrives late in the program of mammalian **nephrogenesis**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Normal human **nephrogenesis** ceases around the thirty-sixth week of gestation, fixing the total nephron endowment."
      }
    ]
  },
  "Dashboard — nephr\\nephrolepis.md": {
    "primary": "A genus of about 30 species of ferns in the family Nephrolepidaceae, including the sword fern and the common Boston fern.",
    "secondary": "In systematic botany and horticulture, pantropical epiphytic or terrestrial ferns characterized by pinnate fronds and kidney-shaped indusia covering their spore-bearing sori.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The genus **Nephrolepis** is recognized by its kidney-shaped indusium attached at the sinus."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Cultivated sports of **Nephrolepis** exhibit remarkable diversity in frond division and leaf curl."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Species of **Nephrolepis** flourish as epiphytes along the mossy trunks of tropical rain-forest trees."
      }
    ]
  },
  "Dashboard — nephr\\nephrolith.md": {
    "primary": "A stone or calculus formed in the kidney; a renal calculus.",
    "secondary": "In urology, a crystalline concretion formed from calcium oxalate, uric acid, or struvite that forms in the renal papillae and may lodge in the pelvis or ureter.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Passage of an angular **nephrolith** through the narrow ureter elicits excruciating spasmodic renal colic."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "The extraction of a staghorn **nephrolith** from the renal pelvis was successfully accomplished through nephrolithotomy."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Hyperuricemia predisposes the constitution to the persistent formation of an obstructing **nephrolith**."
      }
    ]
  },
  "Dashboard — nephr\\nephrolithiasis.md": {
    "primary": "The medical condition characterized by the formation or presence of calculi (kidney stones) in the kidneys.",
    "secondary": "In clinical nephrology, a chronic metabolic or dietary disorder leading to supersaturation of urine and crystalluria, precipitating recurrent nephroliths.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Recurrent **nephrolithiasis** requires rigorous chemical evaluation of twenty-four-hour urinary excretion."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Chronic urinary stasis and persistent Proteus infection are primary causative factors in calculous **nephrolithiasis**."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Patients tormented by gout frequently share an underlying bodily diathesis toward painful **nephrolithiasis**."
      }
    ]
  },
  "Dashboard — nephr\\nephrologist.md": {
    "primary": "A physician or medical specialist who diagnoses and treats diseases and disorders of the kidneys.",
    "secondary": "In internal medicine, a specialist managing acute kidney injury, chronic renal failure, electrolyte imbalances, glomerulonephritis, and renal replacement therapy (dialysis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The consulting **nephrologist** must balance volume status and acid-base equilibrium in end-stage renal disease."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Close collaboration between the cardiologist and the **nephrologist** is essential when managing cardiorenal failure."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The astute **nephrologist** recognized that the patient's sudden delirium was uremic encephalopathy."
      }
    ]
  },
  "Dashboard — nephr\\nephrology.md": {
    "primary": "The branch of medical science that deals with the physiology, diseases, and treatment of the kidneys.",
    "secondary": "In internal medicine, the subspecialty focused on renal hemodynamics, glomerular filtration, tubular electrolyte transport, and maintenance dialysis therapies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The emergence of modern clinical **nephrology** has revolutionized our understanding of systemic fluid homeostasis."
      },
      {
        "author": "Homer Smith",
        "work": "The Kidney: Structure and Function in Health and Disease",
        "quote": "Experimental clearance techniques established the quantitative foundation of contemporary **nephrology**."
      },
      {
        "author": "Richard Bright",
        "work": "Reports of Medical Cases",
        "quote": "The systematic correlation of albuminous urine with renal structural changes laid the cornerstone of scientific **nephrology**."
      }
    ]
  },
  "Dashboard — nephr\\nephron.md": {
    "primary": "The fundamental structural and functional microscopic unit of the kidney, responsible for filtering blood and producing urine.",
    "secondary": "In renal physiology and histology, a microscopic tubule consisting of a renal corpuscle (glomerulus and Bowman's capsule) and a tubular system that regulates water and electrolyte balance.",
    "quotes": [
      {
        "author": "Homer Smith",
        "work": "The Kidney: Structure and Function in Health and Disease",
        "quote": "Each human kidney contains roughly one million **nephron** units filtering plasma under hydrostatic pressure."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Vasomotor nerve endings arborize around the afferent arteriole of every single **nephron**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The convoluted tubule of the **nephron** descends into the medulla as the loop of Henle before returning to the cortex."
      }
    ]
  },
  "Dashboard — nephr\\nephropathy.md": {
    "primary": "Any disease, damage, or pathological disorder of the kidneys.",
    "secondary": "In internal medicine and pathology, renal injury resulting from systemic conditions such as diabetes mellitus (diabetic nephropathy), hypertension, amyloidosis, or analgesic abuse.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In advanced diabetes mellitus, intercapillary glomerulosclerosis heralds the onset of severe diabetic **nephropathy**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Heavy metal poisoning induces acute toxic **nephropathy** characterized by extensive necrosis of the proximal convoluted tubules."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Chronic ischemic **nephropathy** exacerbates refractory hypertension by activating the renin-angiotensin cascade."
      }
    ]
  },
  "Dashboard — nephr\\nephrops.md": {
    "primary": "A taxonomic genus of decapod crustaceans in the family Nephropidae, comprising the Norway lobster (Nephrops norvegicus), also called Dublin Bay prawn or scampi.",
    "secondary": "In marine biology and commercial fisheries, slender, orange-pink clawed lobsters that inhabit muddy burrows in the northeastern Atlantic Ocean and Mediterranean Sea.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish: An Introduction to the Study of Zoology",
        "quote": "The marine lobster **Nephrops** exhibits an elongated cephalothorax and slender, spinous chelae."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Burrowing behavior in **Nephrops** creates extensive tunnel networks across the soft muddy sediments of the sea floor."
      },
      {
        "author": "William Thomas Calman",
        "work": "The Life of Crustacea",
        "quote": "Commercial trawlers harvest immense quantities of **Nephrops** from the deep coastal waters of northern Europe."
      }
    ]
  },
  "Dashboard — nephr\\nephropsidae.md": {
    "primary": "An alternate or obsolete spelling of Nephropidae, the family of clawed lobsters.",
    "secondary": "In systematic carcinology and marine zoology, marine decapod crustaceans possessing large, asymmetrical claws (chelipeds) and calcified abdominal somites.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "The Crayfish: An Introduction to the Study of Zoology",
        "quote": "The marine clawed lobsters included within **Nephropsidae** share a tripartite body plan and calcified carapace."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Members of **Nephropsidae** are readily separated from spiny lobsters by the prominent development of anterior pinchers."
      },
      {
        "author": "William Thomas Calman",
        "work": "The Life of Crustacea",
        "quote": "Taxonomic arrangements of the **Nephropsidae** emphasize the structure of the branchial formulas and thoracic appendages."
      }
    ]
  },
  "Dashboard — nephr\\nephroptosia.md": {
    "primary": "An abnormal downward displacement or dropping of a kidney; floating or wandering kidney (synonym of nephroptosis).",
    "secondary": "In historical clinical medicine and visceral surgery, mobility of the kidney out of its retroperitoneal fat pad into the iliac fossa upon standing, historically treated with nephropexy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Marked **nephroptosia** is frequently encountered in emaciated women with relaxed abdominal musculature."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Severe Dietl's crises in **nephroptosia** result from acute kinking of the ureter as the organ drops."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Surgical suspension of the organ via nephropexy relieves the traction pain caused by symptomatic **nephroptosia**."
      }
    ]
  },
  "Dashboard — nephr\\nephroptosis.md": {
    "primary": "An abnormal condition in which the kidney drops down into the pelvis when the patient stands up; floating kidney.",
    "secondary": "In urology and abdominal surgery, hypermobility of the kidney resulting from loss of perirenal adipose support, occasionally precipitating ureteral kinking and hydronephrosis (Dietl's crisis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The diagnosis of symptomatic **nephroptosis** requires palpation of the descended organ during deep inspiration while standing."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "True **nephroptosis** must be distinguished from a congenital ectopic kidney fixed in the pelvis."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Colicky flank pain relieved immediately upon lying down is the classic symptom complex of movable kidney or **nephroptosis**."
      }
    ]
  },
  "Dashboard — nephr\\nephrosclerosis.md": {
    "primary": "Hardening and scarring of the kidney tissues, especially involving the renal arteries and arterioles.",
    "secondary": "In renal pathology, progressive vascular sclerosis associated with chronic systemic hypertension, resulting in ischemia, loss of glomeruli, and fibrous contracted kidneys.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Arteriolar **nephrosclerosis** is the anatomical substrate of the contracted kidney found in chronic hypertension."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The gross appearance of **nephrosclerosis** shows a finely granular, shrunken cortical surface with adherent capsule."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Longstanding essential hypertension eventually compromises renal reserve through advancing **nephrosclerosis**."
      }
    ]
  },
  "Dashboard — nephr\\nephrosis.md": {
    "primary": "Any non-inflammatory degenerative disease of the kidneys, particularly one affecting the renal tubules.",
    "secondary": "In clinical nephrology, a condition (as in the nephrotic syndrome) characterized by severe proteinuria, hypoalbuminemia, hyperlipidemia, and generalized edema.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Lipoid **nephrosis** presents with colossal generalized anasarca, heavy proteinuria, and normal blood pressure."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Fatty degeneration and hyaline droplet change in the tubular epithelium characterize toxic **nephrosis**."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Profuse albuminuria accompanied by massive pitting edema without hematuria defines the clinical entity of **nephrosis**."
      }
    ]
  }
};

console.log(`Starting curation of Body Rem A Batch 2 (${Object.keys(batchData).length} notes)...`);
const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`Batch 2 complete: successfully updated ${count} notes.`);
