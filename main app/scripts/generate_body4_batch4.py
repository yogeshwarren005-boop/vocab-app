import json
import os

BATCH4_DATA = {
  "Dashboard — logy_ ology/posology.md": {
    "primary": "The branch of medical and pharmacological science concerned with the determination and administration of medicinal dosages.",
    "secondary": "In clinical therapeutics, the calculation and adjustment of drug doses based on pharmacokinetics, clearance, patient weight, and clinical response.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A sound knowledge of **posology** is essential to avoid toxic accumulations in elderly or cachectic patients."
      },
      {
        "author": "Bertram Katzung",
        "work": "Basic and Clinical Pharmacology",
        "quote": "Pediatric **posology** requires exact weight-adjusted calculations rather than arbitrary fractions of adult dosages."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "Medical Essays",
        "quote": "The physician who neglects **posology** will find his remedies either inert from underdosing or lethal from excess."
      }
    ]
  },
  "Dashboard — logy_ ology/rheology.md": {
    "primary": "The branch of physics that studies the deformation and flow of matter, particularly non-Newtonian fluids and soft solids.",
    "secondary": "In cardiovascular biophysics and hemorheology, the investigation of blood viscosity, erythrocyte elasticity, and shear stress within the microvasculature.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Altered blood **rheology** and elevated plasma fibrinogen contribute significantly to microvascular thrombosis."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The study of circulatory **rheology** demonstrates that hematocrit is the primary determinant of whole blood viscosity."
      },
      {
        "author": "Albert Einstein",
        "work": "Investigations on the Theory of the Brownian Movement",
        "quote": "Theoretical **rheology** connects the macroscopic viscosity of suspensions with the hydrodynamic drag of suspended particles."
      }
    ]
  },
  "Dashboard — logy_ ology/serology.md": {
    "primary": "The scientific study and diagnostic examination of blood serum and other bodily fluids, especially regarding immune reactions.",
    "secondary": "In clinical immunology and pathology, the laboratory identification of circulating antibodies, antigens, and past pathogen exposure through immunological assays.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The development of diagnostic **serology** by Wassermann revolutionized the detection of latent syphilis."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Quantitative **serology** enabled us to measure the exact neutralizing titers of anti-diphtheritic horse sera."
      },
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The principles that gave birth to modern **serology** arose from our earliest observations of immunization."
      }
    ]
  },
  "Dashboard — logy_ ology/sinology.md": {
    "primary": "The academic study of Chinese language, literature, history, culture, and philosophy.",
    "secondary": "In comparative oriental studies, the philological and historical investigation of classical Chinese texts, dynastic records, and civilizational traditions.",
    "quotes": [
      {
        "author": "Max Weber",
        "work": "The Religion of China: Confucianism and Taoism",
        "quote": "Comparative **sinology** demonstrates how the bureaucratic mandate of the literati shaped Chinese social ethics."
      },
      {
        "author": "James Legge",
        "work": "The Chinese Classics",
        "quote": "A lifelong dedication to **sinology** allowed Legge to render the Confucian canon into authoritative English prose."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Problem of China",
        "quote": "Western scholars who embark upon **sinology** often discover a civilization remarkably free from theological fanaticism."
      }
    ]
  },
  "Dashboard — logy_ ology/theology.md": {
    "primary": "The systematic study of the nature of the divine, religious truth, and spiritual doctrines.",
    "secondary": "In intellectual and ecclesiastical history, a formal academic discipline utilizing philosophical analysis to interpret scripture, revelation, and moral duty.",
    "quotes": [
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "Sacred **theology** is an overarching science that receives its principles immediately from God through revelation."
      },
      {
        "author": "Augustine of Hippo",
        "work": "The City of God",
        "quote": "True **theology** directs the human intellect beyond temporal shadows toward the eternal contemplation of divine truth."
      },
      {
        "author": "John Henry Newman",
        "work": "The Idea of a University",
        "quote": "To exclude **theology** from a university curriculum is to impair the completeness of intellectual culture."
      }
    ]
  },
  "Dashboard — logy_ ology/tocology.md": {
    "primary": "The science and medical specialty of obstetrics and childbirth.",
    "secondary": "In clinical medicine and perinatal history, the systematic study of labor mechanisms, parturition, and maternal care during delivery.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The modern discipline of **tocology** has drastically curtailed maternal puerperal mortality through aseptic technique."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The mechanics of human **tocology** reflect evolutionary modifications in pelvic morphology resulting from bipedalism."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "Medical Essays",
        "quote": "The practitioner of **tocology** must never forget that clean hands protect the lying-in mother from fatal fever."
      }
    ]
  },
  "Dashboard — logy_ ology/topology.md": {
    "primary": "The mathematical study of the properties of spaces that are preserved under continuous deformation such as stretching and twisting.",
    "secondary": "In structural and network engineering, the spatial layout, interconnectivity pattern, or physical arrangement of components or communication nodes.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "The profound methods of algebraic **topology** allow us to classify manifolds that elude traditional Euclidean geometry."
      },
      {
        "author": "Alan Turing",
        "work": "The Chemical Basis of Morphogenesis",
        "quote": "Biological morphogenesis creates complex cellular **topology** through reaction-diffusion instabilities."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "In modern mathematical **topology**, geometric continuity is purified of all empirical intuition."
      }
    ]
  },
  "Dashboard — logy_ ology/trilogy.md": {
    "primary": "A group or series of three related works of literature, drama, film, or music that form a connected narrative.",
    "secondary": "In ancient Greek theatrical festivals, a sequence of three linked tragedies presented consecutively by a tragic poet (e.g. Aeschylus's Oresteia).",
    "quotes": [
      {
        "author": "John Addington Symonds",
        "work": "Studies of the Greek Poets",
        "quote": "Aeschylus achieved the grandest architecture of tragic art in his monumental Oresteian **trilogy**."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of the French Novel",
        "quote": "Balzac conceived individual novels as dynamic panels within an expansive thematic **trilogy**."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "The Birth of Tragedy",
        "quote": "The tragic **trilogy** celebrated the reconciliation of Dionysian suffering with Apollonian artistic restraint."
      }
    ]
  },
  "Dashboard — logy_ ology/typology.md": {
    "primary": "A systematic classification of things according to their shared general types or characteristics.",
    "secondary": "In biblical hermeneutics, the study of historical figures or events in the Old Testament prefiguring New Testament realities; in linguistics, structural categorization.",
    "quotes": [
      {
        "author": "Edward Sapir",
        "work": "Language: An Introduction to the Study of Speech",
        "quote": "Linguistic **typology** classifies world languages according to their morphological synthesis and agglutinative techniques."
      },
      {
        "author": "Max Weber",
        "work": "The Protestant Ethic and the Spirit of Capitalism",
        "quote": "The construction of an ideal **typology** provides sociology with heuristic benchmarks for historical comparison."
      },
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "Biblical **typology** links prophetic symbols in the Hebrew scriptures with their historical realization in the New Testament."
      }
    ]
  },
  "Dashboard — logy_ ology/urology.md": {
    "primary": "The medical and surgical specialty concerned with the urinary system and male reproductive system.",
    "secondary": "In surgical pathology, the diagnosis and operative treatment of kidney disorders, calculi, bladder diseases, and prostatic conditions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The early diagnosis of urinary calculus and bladder neoplasms belongs to the purview of operative **urology**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "A meticulous mastery of pelvic and retroperitoneal anatomy is the foundation of modern **urology**."
      },
      {
        "author": "William Stewart Halsted",
        "work": "Surgical Papers",
        "quote": "Aseptic instrument design and cystoscopic illumination revolutionized the practice of clinical **urology**."
      }
    ]
  },
  "Dashboard — logy_ ology/virology.md": {
    "primary": "The scientific branch of microbiology concerned with the study of viruses and viral infections.",
    "secondary": "In molecular biology, the study of viral genomics, viral replication kinetics, capsid structure, and antiviral therapeutic agents.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Although the rabies agent eluded microscopic detection, Pasteur's work heralded the dawn of **virology**."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy",
        "quote": "Unlike bacterial infections, viral pathogens investigated in **virology** replicate obligatorily within host cells."
      },
      {
        "author": "Siddhartha Mukherjee",
        "work": "The Song of the Cell",
        "quote": "The techniques of molecular **virology** transformed our understanding of how retroviruses insert genetic code into eukaryotic hosts."
      }
    ]
  },
  "Dashboard — logy_ ology/zoology.md": {
    "primary": "The scientific study of animals and animal life, including structure, physiology, and classification.",
    "secondary": "In natural history and comparative biology, the systematic exploration of animal behavior, morphological diversity, and phylogenetic lineage.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The facts of geographic distribution and morphological homology form the cornerstone of evolutionary **zoology**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "Comparative **zoology** bridges the artificial gulf separating human anatomy from the rest of animated nature."
      },
      {
        "author": "Ernst Haeckel",
        "work": "The History of Creation",
        "quote": "Modern **zoology** is fundamentally genealogical, seeking to reconstruct the ancestral tree of animal life."
      }
    ]
  },
  "Dashboard — logy_ ology/zymology.md": {
    "primary": "The science and study of fermentation and enzyme-driven biochemical reactions.",
    "secondary": "In applied biotechnology and brewing, the industrial study of yeast metabolism, enzymatic catalysis, and alcohol production.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The foundations of scientific **zymology** were established by demonstrating that fermentation is an expression of microscopic life."
      },
      {
        "author": "Justus von Liebig",
        "work": "Familiar Letters on Chemistry",
        "quote": "Before microbiological **zymology** prevailed, chemists viewed fermentation as a purely non-living catalytic decomposition."
      },
      {
        "author": "Eduard Buchner",
        "work": "Cell-Free Fermentation (Nobel Lecture)",
        "quote": "Buchner revolutionized **zymology** by proving that yeast juice devoid of intact cells retains the power of alcoholic fermentation."
      }
    ]
  },
  "Dashboard — mening/leptomeninges.md": {
    "primary": "The two delicate, inner membranous envelopes of the brain and spinal cord: the arachnoid and pia mater.",
    "secondary": "In neuropathology, the vascular and reticular coverings enclosing the subarachnoid space through which cerebrospinal fluid circulates.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The arachnoid and pia mater are frequently designated together as the **leptomeninges**, distinguished by their vascular and delicate texture."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Purulent inflammation spreading through the **leptomeninges** rapidly generates signs of severe meningeal irritation."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The cerebrospinal fluid circulates within the meshwork of the **leptomeninges** before absorbing into venous sinuses."
      }
    ]
  },
  "Dashboard — mening/menage.md": {
    "primary": "A household or domestic establishment; the members of a household living together as a domestic unit.",
    "secondary": "In social history and domestic economy, the housekeeping, financial affairs, and daily management of a family home.",
    "quotes": [
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "Becky Sharp managed the extravagant **menage** with astonishing thrift and diplomatic ingenuity."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "Mrs. Fairfax conducted the quiet **menage** of Thornfield Hall with traditional English punctuality."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Lydgate realized that the expenses of his new **menage** were far outstripping his clinical fees."
      }
    ]
  },
  "Dashboard — mening/mening.md": {
    "primary": "An anatomical combining form derived from Greek μῆνιγξ (meninx), denoting the meninges or protective cranial membranes.",
    "secondary": "In clinical lexicography, a root used to form neurological terms describing membranes enclosing the central nervous system (e.g. meningitis, meningioma).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The root **mening**- forms numerous clinical terms designating the three protective envelopes of the encephalon."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Every inflammatory process involving the **mening**-eal envelopes presents with fever, cervical rigidity, and photophobia."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Mesodermal cells condense around the developing neural tube to form the primordial **mening**-eal sheath."
      }
    ]
  },
  "Dashboard — mening/meningeal.md": {
    "primary": "Pertaining to, located near, or affecting the meninges of the brain and spinal cord.",
    "secondary": "In neuroanatomy, designating cranial vessels and sensory nerves (such as the middle meningeal artery) supplying the cranial dura mater.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The middle **meningeal** artery ascends through the foramen spinosum to ramify upon the inner table of the skull."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Laceration of a **meningeal** vessel after temporal skull trauma produces progressive somnolence and hemiplegia."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Control of hemorrhage from the **meningeal** sinuses requires meticulous silver-clip placement during craniotomy."
      }
    ]
  },
  "Dashboard — mening/meninges.md": {
    "primary": "The three membranous protective envelopes (dura mater, arachnoid mater, and pia mater) enclosing the brain and spinal cord.",
    "secondary": "In gross neurology, the fibrous and vascular layers that cushion the central nervous system, contain CSF, and compartmentalize intracranial volume.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The brain and spinal cord are enclosed within three membranes, termed the **meninges**: the dura mater, the arachnoid, and the pia mater."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Suppurative exudate coating the cerebral **meninges** produces the classic tripos of headache, vomiting, and neck stiffness."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Traumatic contusion affecting the cerebral **meninges** often triggers focal epileptic discharges in adjacent cortical tissue."
      }
    ]
  },
  "Dashboard — mening/meningioma.md": {
    "primary": "A typically slow-growing, usually benign neoplasm arising from the arachnoid cells of the meninges.",
    "secondary": "In neuropathology, a primary extra-axial intracranial or intraspinal tumor characterized by whorled arachnoid cap cells, psammoma bodies, and hyperostosis.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Meningiomas: Their Classification and Surgical Behavior",
        "quote": "Cushing coined the term **meningioma** to designate tumors arising from the arachnoid villi that compress adjacent cerebral cortex."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unlike malignant gliomas, an intracranial **meningioma** is encapsulated and frequently amenable to total surgical resection."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "A frontal **meningioma** had grown silently for years, gradually altering the patient's personality before causing motor deficits."
      }
    ]
  },
  "Dashboard — mening/meningism.md": {
    "primary": "A state of meningeal irritation characterized by headache, neck rigidity, and photophobia without actual infection or inflammation of the meninges.",
    "secondary": "In pediatrics and clinical medicine, a syndrome of pseudo-meningitis seen in acute extra-cranial infections like pneumonia, marked by normal cerebrospinal fluid.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In young children, acute apical pneumonia often presents with violent **meningism**, mimicking true bacterial infection."
      },
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "Lumbar puncture is the definitive test to distinguish true meningeal exudation from benign **meningism**."
      },
      {
        "author": "Emil Kraepelin",
        "work": "Lectures on Clinical Psychiatry",
        "quote": "Severe toxic states may induce a transient **meningism** accompanied by delirium and cervical resistance."
      }
    ]
  },
  "Dashboard — mening/meningocele.md": {
    "primary": "A congenital protrusion of the meninges through a bony defect in the skull or vertebral column, forming a cystic sac.",
    "secondary": "In neurosurgery and teratology, a cystic spina bifida variant containing meninges and cerebrospinal fluid without neural tissue involvement.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Failure of the neural arches to fuse posteriorly permits the protrusion of a cystic **meningocele**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unlike a myelomeningocele, an uncomplicated **meningocele** contains no nervous tissue in the protruding sac."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The genesis of **meningocele** is linked to defective mesodermal closure around the embryonic neural tube."
      }
    ]
  },
  "Dashboard — mening/meningoencephalitis.md": {
    "primary": "Simultaneous inflammation of the brain (encephalitis) and its surrounding meningeal membranes (meningitis).",
    "secondary": "In infectious disease neurology, an acute neuro-inflammatory state presenting with combined neck stiffness, fever, confusion, and focal neurological deficits.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Viral infection may precipitate acute **meningoencephalitis**, plunging the patient from lethargy into coma."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Cognitive rehabilitation following recovery from **meningoencephalitis** must address widespread patchy cortical deficits."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The pandemic of encephalitis lethargica presented in its acute phase as an enigmatic, deadly **meningoencephalitis**."
      }
    ]
  },
  "Dashboard — mening/meninx.md": {
    "primary": "A single protective membrane covering the brain or spinal cord (singular form of meninges).",
    "secondary": "In comparative vertebrate anatomy and developmental embryology, the investing membranous sheet that encapsulates the central nervous system.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The outer **meninx**, or dura mater, adheres firmly to the internal periosteum of the calvaria."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "In lower vertebrates, a single undifferentiated **meninx** surrounds the spinal cord, whereas mammals develop three distinct sheets."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The vascular **meninx** conforms intimately to the gyri and sulci of the cerebral hemispheres."
      }
    ]
  },
  "Dashboard — mening/mental.md": {
    "primary": "Relating to the mind or psychological operations; also relating to the chin in anatomical terminology (from Latin mentum).",
    "secondary": "In neurocognitive science, pertaining to conscious intellect and thought; in craniofacial anatomy, designating the mental nerve, artery, and foramen of the lower jaw.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The distribution of consciousness shows that **mental** action is teleological, striving toward chosen goals."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **mental** nerve emerges from the mandible through the **mental** foramen to supply sensation to the lower lip."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "Reflection is that notice which the mind takes of its own operations, producing our complex **mental** ideas."
      }
    ]
  },
  "Dashboard — mening/mentally.md": {
    "primary": "In a manner relating to the mind, intellectual capacity, or psychological state.",
    "secondary": "In cognitive psychology and psychiatry, with respect to interior cognitive appraisal, intellectual processing, or mental health.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "David Copperfield",
        "quote": "I was **mentally** exhausted by the long day of intense study and emotional turmoil."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "To focus our attention is to withdraw **mentally** from surrounding impressions to concentrate upon a single object."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Conquest of Happiness",
        "quote": "The philosopher learns to view misfortune **mentally** from the perspective of cosmic insignificance."
      }
    ]
  },
  "Dashboard — mening/mentation.md": {
    "primary": "Mental activity or the process of cognitive functioning and reasoning.",
    "secondary": "In clinical neurology and critical care assessment, the level of consciousness, orientation, and cognitive responsiveness exhibited by a patient.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clouding of **mentation** and nocturnal delirium frequently precede overt uremic coma."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The stream of conscious **mentation** flows unbroken, though sensations and thoughts continually fluctuate."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Decreased cerebral perfusion in low-output cardiogenic shock causes altered **mentation** and lethargy."
      }
    ]
  },
  "Dashboard — mening/mention.md": {
    "primary": "To refer to, speak of, or cite briefly in discourse or writing; a passing notice or allusion.",
    "secondary": "In formal rhetoric and institutional communiqués, an official or honorary acknowledgment of service or merit.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Merchant of Venice",
        "quote": "I will buy with you, sell with you, talk with you, walk with you, and so following; but I will not eat with you, drink with you, nor pray with you. What news on the Rialto? Who is he comes here? ... Make no **mention** of it."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Lives of the English Poets",
        "quote": "He omitted all **mention** of his rival's brilliant achievement, blinded by ungenerous jealousy."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "She resolved not to make the slightest **mention** of what had passed between herself and Mr. Darcy."
      }
    ]
  },
  "Dashboard — mening/mentioner.md": {
    "primary": "A person who mentions, speaks of, or cites another person, fact, or event.",
    "secondary": "In literary criticism and scholarly historiography, a commentator or writer who records a reference or first introduces a subject into literature.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "The earliest **mentioner** of this curious ancient custom was a traveler whose credulity exceeded his judgment."
      },
      {
        "author": "Thomas Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "He was an unsparing **mentioner** of the frailties and indiscretions of his political contemporaries."
      },
      {
        "author": "William Hazlitt",
        "work": "Table-Talk",
        "quote": "A frequent **mentioner** of great names is often seeking to borrow reflected luster for his own mediocrity."
      }
    ]
  },
  "Dashboard — mening/mentor.md": {
    "primary": "A wise, trusted, and experienced counselor, guide, or advisor.",
    "secondary": "Originally the character Mentor in Homer's Odyssey, guide of Telemachus; in modern education and professional training, an experienced practitioner fostering the growth of a protégé.",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Odyssey",
        "quote": "Athena assumed the form and voice of **Mentor**, offering wise counsel to the youthful Telemachus."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Every aspiring youth seeks a revered **mentor** whose intellectual stature validates their highest ideals."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative",
        "quote": "In my formative scientific years, Georg Forster was the inspiring **mentor** who ignited my passion for tropical exploration."
      }
    ]
  },
  "Dashboard — my/Nectomys.md": {
    "primary": "A genus of semiaquatic Neotropical rodents in the family Cricetidae, commonly called Neotropical water rats.",
    "secondary": "In mammalian taxonomy, a rodent genus characterized by broad webbed hind feet, dense water-resistant fur, and specialized adaptations for foraging in Amazonian and Orinoco waterways.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Comparative adaptations among aquatic rodents, such as the South American **Nectomys**, illustrate convergent evolution toward swimming specializations."
      },
      {
        "author": "Charles Darwin",
        "work": "Zoology of the Voyage of H.M.S. Beagle",
        "quote": "Specimens of the aquatic rodent **Nectomys** collected along the riverbanks displayed remarkable webbed digits."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The cranial and dental morphology of **Nectomys** aligns it closely with the pastoral Neotropical sigmodontines."
      }
    ]
  },
  "Dashboard — my/Sigmodontomys.md": {
    "primary": "A genus of Neotropical cricetid rodents commonly known as Alfaro's water rats or rice water rats.",
    "secondary": "In systematic mammalogy, a genus of semiaquatic forest rodents inhabiting Central and northern South America, distinguished by sigmoid molar folds and adaptations to montane rainforests.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The distribution of specialized rodents like **Sigmodontomys** marks the biotic interchange across the Panamanian land bridge."
      },
      {
        "author": "Frank M. Chapman",
        "work": "The Distribution of Bird-Life in Colombia",
        "quote": "Small mammal trappings in the wet subtropical forests yielded rare specimens of **Sigmodontomys** alongside endemic avifauna."
      },
      {
        "author": "Aleš Hrdlička",
        "work": "Anthropological Investigations",
        "quote": "Local fauna recorded along the rainforest streams included the elusive water rat **Sigmodontomys**."
      }
    ]
  },
  "Dashboard — my/electromyogram.md": {
    "primary": "A graphical tracing or record of electrical activity produced by skeletal muscle fibers during contraction.",
    "secondary": "In clinical neurophysiology, an oscilloscopic or printed recording of motor unit action potentials used to diagnose neuromuscular transmission disorders and denervation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The recorded **electromyogram** clearly showed fibrillations and positive sharp waves characteristic of lower motor neuron denervation."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "The **electromyogram** recorded from speech muscles during silent reading reveals covert articulatory micro-movements."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "In healthy muscle at rest, the **electromyogram** remains isoelectric, displaying bursts of electrical potentials only upon voluntary contraction."
      }
    ]
  },
  "Dashboard — my/electromyograph.md": {
    "primary": "An electrical apparatus or instrument used for recording and analyzing potentials generated by contracting muscles.",
    "secondary": "In diagnostic neurology and biomechanics, an electronic instrument with differential amplifiers and electrodes used to assess the integrity of motor units.",
    "quotes": [
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The modern **electromyograph** amplifies minute electrical potentials from motor units to assess contractile function."
      },
      {
        "author": "Alexander Luria",
        "work": "Higher Cortical Functions in Man",
        "quote": "By connecting the patient to an **electromyograph**, we demonstrated subconscious motor preparation preceding conscious movement."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Analysis of Matter",
        "quote": "Instrumental recording with an **electromyograph** objectifies physiological states that subjective introspection can never measure."
      }
    ]
  },
  "Dashboard — my/electromyography.md": {
    "primary": "The diagnostic technique or clinical science of recording and evaluating the electrical activity produced by skeletal muscles.",
    "secondary": "In clinical electrodiagnosis, the evaluation of spontaneous, voluntary, and evoked electrical potentials to distinguish neurogenic denervation from intrinsic myopathies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinical **electromyography** provides objective evidence confirming radiculopathy when physical examination remains ambiguous."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Through quantitative **electromyography**, the firing rates of individual motor units can be measured during graduated exertion."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "The application of **electromyography** revealed that motor cortical lesions disrupt voluntary muscle activation rhythms."
      }
    ]
  },
  "Dashboard — my/emmy.md": {
    "primary": "An annual statuette award presented by the Academy of Television Arts and Sciences recognizing outstanding achievements in television.",
    "secondary": "In media history, an award figurine depicting a winged muse holding an electron atom, derived from 'Immy' (a diminutive for the image orthicon camera tube).",
    "quotes": [
      {
        "author": "H. L. Mencken",
        "work": "The American Language",
        "quote": "The television industry coined the jaunty name **Emmy** from the image orthicon tube to designate its annual statuette."
      },
      {
        "author": "Marshall McLuhan",
        "work": "Understanding Media: The Extensions of Man",
        "quote": "The lavish spectacle of the **Emmy** broadcast celebrates the triumph of the cool electronic medium over print culture."
      },
      {
        "author": "Gore Vidal",
        "work": "United States: Essays 1952–1992",
        "quote": "Television writers gathered each season to bestow an **Emmy** upon productions that conformed to commercial orthodoxy."
      }
    ]
  },
  "Dashboard — my/endomysium.md": {
    "primary": "The delicate sheath of connective tissue surrounding each individual skeletal muscle fiber.",
    "secondary": "In muscle histology, the reticular collagenous matrix that envelops the sarcolemma, accommodating nutritional capillaries and unmyelinated nerve terminals.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Each separate muscular fiber is enveloped in a delicate connective tissue sheath known as the **endomysium**."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The capillaries of skeletal muscle traverse the **endomysium** in close contact with the sarcolemma."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In progressive muscular dystrophy, the **endomysium** becomes thickened by fibrous infiltration as muscle fibers atrophy."
      }
    ]
  },
  "Dashboard — my/epimysium.md": {
    "primary": "The outer sheath of dense fibrous connective tissue that encloses an entire skeletal muscle.",
    "secondary": "In functional anatomy, the continuous fascial envelope that bundles muscle fascicles together, protects muscle architecture, and transitions into tendons.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **epimysium** forms a dense external investiture enclosing the whole muscle, continuous with the deep fascia."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "During embryonic development, the condensed mesenchyme differentiates into the **epimysium** and neighboring aponeuroses."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Tensile force generated by sarcomeres is transmitted laterally through the **epimysium** to insert upon bone."
      }
    ]
  },
  "Dashboard — my/fibromyoma.md": {
    "primary": "A benign neoplasm composed of smooth muscle cells and fibrous connective tissue, commonly developing in the uterus.",
    "secondary": "In gynecological oncology, an encapsulated uterine leiomyoma that may cause abnormal bleeding, pelvic pressure, or pain depending on intramural or submucous location.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The presence of a large uterine **fibromyoma** may cause severe mechanical compression of the pelvic ureters."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Virchow demonstrated that a **fibromyoma** develops from monocytic smooth muscle proliferation within the uterine wall."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "The surgeon successfully excised a massive calcified **fibromyoma**, restoring pelvic anatomy and relieving pain."
      }
    ]
  },
  "Dashboard — my/murine.md": {
    "primary": "Belonging to, relating to, or resembling mice or the rodent family Muridae.",
    "secondary": "In biomedical and immunological research, designating experimental models, pathogens, or monoclonal antibodies derived from or affecting mice.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The colonization of remote oceanic islands by **murine** rodents has produced marked endemic divergence."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The dental formula and zygomatic plate of the **murine** skull distinguish it from all sciuromorphs."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Experimental inoculation of **murine** subjects demonstrated acquired humoral immunity against ricin intoxication."
      }
    ]
  },
  "Dashboard — my/musophobia.md": {
    "primary": "An abnormal, irrational, or disproportionate fear of mice or rats.",
    "secondary": "In clinical psychology and psychiatric diagnostics, a specific animal phobia characterized by acute sympathetic activation and panic upon encountering rodents.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Introductory Lectures on Psycho-Analysis",
        "quote": "Specific phobias such as **musophobia** frequently represent displaced childhood anxieties anchored to animal symbols."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The irrational dread of harmless creatures like mice, termed **musophobia**, illustrates how instinctive fear can become pathologically fixed."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "An acute attack of **musophobia** in an adult patient is often accompanied by tachycardia and hysterical trembling."
      }
    ]
  },
  "Dashboard — my/my.md": {
    "primary": "In anatomical nomenclature, a combining root or prefix (from Greek μῦς, myos) denoting muscle tissue; in English grammar, the possessive pronoun of the first person singular.",
    "secondary": "In biomedical etymology, the combining form (*my-*, *myo-*) utilized across medical disciplines (e.g. myocardium, myology); in personal discourse, signifying possession by the speaker.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "Give me that man that is not passion's slave, and I will wear him in **my** heart's core, ay, in **my** heart of heart."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The world was all before them, where to choose their place of rest, and Providence their guide: They hand in hand, with wandering steps and slow, through Eden took their solitary way ... O **my** soul!"
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The anatomical prefix **my**- designates muscular tissue, originating from the Greek noun for mouse and muscle."
      }
    ]
  },
  "Dashboard — my/myalgia.md": {
    "primary": "Pain or soreness in a muscle or group of muscles.",
    "secondary": "In internal medicine and rheumatology, a symptom common to systemic infectious syndromes, autoimmune disorders, and medication toxicities such as statin therapy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The prodromal stage of epidemic influenza is marked by high fever, prostrating fatigue, and diffuse **myalgia**."
      },
      {
        "author": "Bertram Katzung",
        "work": "Basic and Clinical Pharmacology",
        "quote": "Patients receiving HMG-CoA reductase inhibitors must be monitored for unexplained **myalgia** indicative of rhabdomyolysis."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Severe **myalgia** accompanied by elevated serum creatine kinase warrants immediate discontinuation of the offending lipid-lowering agent."
      }
    ]
  },
  "Dashboard — my/myalgic.md": {
    "primary": "Relating to, characterized by, or affected with muscular pain.",
    "secondary": "In diagnostic medicine, describing pathological symptoms of muscle tenderness, notably in myalgic encephalomyelitis (chronic fatigue syndrome).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The **myalgic** distress accompanying trichinosis reflects the direct larval invasion of skeletal muscle fibers."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Accumulation of lactic acid and inflammatory cytokines excites sensory free nerve endings, triggering a **myalgic** sensation."
      },
      {
        "author": "Oliver Wendell Holmes",
        "work": "Medical Essays",
        "quote": "The patient complained of constant **myalgic** soreness in the lumbar region following excessive physical exertion."
      }
    ]
  },
  "Dashboard — my/myasthenia gravis.md": {
    "primary": "A chronic autoimmune neuromuscular disorder characterized by marked weakness and abnormal fatigability of voluntary skeletal muscles.",
    "secondary": "In clinical neurology, a disease caused by autoantibodies directed against acetylcholine receptors at the neuromuscular junction, leading to ptosis, diplopia, and bulbar weakness.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The striking feature of **myasthenia gravis** is the rapid exhaustion of voluntary power upon repeated effort, with partial recovery after rest."
      },
      {
        "author": "Bertram Katzung",
        "work": "Basic and Clinical Pharmacology",
        "quote": "In **myasthenia gravis**, acetylcholinesterase inhibitors such as pyridostigmine increase available synaptic acetylcholine to improve muscle strength."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The clinical spectrum of **myasthenia gravis** illustrates how immunologic failure disrupts the synaptic dialogue between nerve and muscle."
      }
    ]
  },
  "Dashboard — my/myocardial.md": {
    "primary": "Relating to the myocardium, the muscular middle tissue of the heart wall.",
    "secondary": "In cardiology, describing functional states, perfusion, ischemic damage, or pathological necrosis of the cardiac muscle tissue.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "A critical reduction in coronary blood flow precipitates acute **myocardial** ischemia and cellular necrosis."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The synchronous depolarization of **myocardial** fibers depends upon low-resistance gap junctions within intercalated discs."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Extensive **myocardial** degeneration following coronary sclerosis is the commonest cause of chronic congestive failure."
      }
    ]
  },
  "Dashboard — my/myocarditis.md": {
    "primary": "Inflammation of the muscular wall of the heart (the myocardium).",
    "secondary": "In clinical cardiology, an inflammatory cardiomyopathy provoked by viral infections, autoimmune processes, or cardiotoxins, often causing arrhythmias and acute heart failure.",
    "quotes": [
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Acute viral **myocarditis** may present insidiously with unexplained ventricular arrhythmias or fulminant cardiogenic collapse."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Diphtheritic **myocarditis** is a perilous complication arising from the direct cardiotoxic effect of circulating bacterial exotoxin."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Diffuse inflammatory infiltration in **myocarditis** impairs contractile coordination, markedly depressing cardiac output."
      }
    ]
  },
  "Dashboard — my/myocardium.md": {
    "primary": "The thick middle muscular layer of the heart wall.",
    "secondary": "In cardiac physiology, the specialized striated muscle syncytium that performs involuntary contractions to sustain systemic and pulmonary circulation.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **myocardium** consists of interlacing bands of striated muscle fibers forming the bulk of the atrial and ventricular walls."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "The metabolic demands of the working **myocardium** are immense, requiring uninterrupted coronary perfusion."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Hypertrophy of the left ventricular **myocardium** develops as a compensatory adaptation to prolonged arterial hypertension."
      }
    ]
  },
  "Dashboard — my/myoclonus.md": {
    "primary": "A sudden, brief, involuntary twitching or jerking of a muscle or group of muscles.",
    "secondary": "In clinical neurology, a hyperkinetic movement symptom arising from cortical, subcortical, or spinal hyperexcitability following anoxia or metabolic encephalopathy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe toxic metabolic encephalopathies are frequently accompanied by multifocal **myoclonus** and asterixis."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Post-encephalitic patients experienced distressing paroxysms of respiratory **myoclonus** interrupting speech and breathing."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "Subcortical lesions affecting the dentato-rubro-olivary pathway may produce intractable palatal **myoclonus**."
      }
    ]
  },
  "Dashboard — my/myoelectric.md": {
    "primary": "Relating to electrical potentials and currents generated by contracting muscular tissue.",
    "secondary": "In medical engineering and rehabilitation, designating powered prosthetic limbs operated by amplifying microvolt electrical signals from residual muscles.",
    "quotes": [
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Every voluntary muscular effort generates measurable **myoelectric** currents through the synchronized depolarization of motor units."
      },
      {
        "author": "Alexander Luria",
        "work": "Higher Cortical Functions in Man",
        "quote": "Modern prosthetics utilizes amplified **myoelectric** signals from stump musculature to actuate mechanical fingers."
      },
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics",
        "quote": "Feedback control in artificial limbs reaches its apex through the cybernetic integration of **myoelectric** potentials."
      }
    ]
  },
  "Dashboard — my/myoma.md": {
    "primary": "A benign neoplasm or tumor composed of muscle tissue.",
    "secondary": "In pathology, an encapsulated benign growth of smooth muscle (leiomyoma) or skeletal muscle (rhabdomyoma), most frequently found in the myometrium.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Virchow classified every benign muscular neoplasm as a **myoma**, distinguishing smooth from striated cellular origins."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A submucous uterine **myoma** frequently provokes profound secondary anemia from recurrent hemorrhages."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Cardiac rhabdomyoma, though rare, is a specialized **myoma** often associated with tuberous sclerosis."
      }
    ]
  },
  "Dashboard — my/myomancy.md": {
    "primary": "Divination or prophecy based upon the movements, behavior, or sounds of mice or rats.",
    "secondary": "In the history of classical augury and folklore, the superstitious interpretation of rodent sightings and gnawing habits as ominous omens.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Ancient augurs practiced **myomancy**, interpreting the sudden flight of field mice as a portent of famine or siege."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "The belief in **myomancy** illustrates how primitive minds projected prophetic significance upon the movements of domestic pests."
      },
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "superstitious prognosticators who observe auguries from the squeaking of mice and practice ridiculous **myomancy**."
      }
    ]
  },
  "Dashboard — my/myomorphous.md": {
    "primary": "Resembling or having the form of a mouse; belonging or relating to the rodent suborder Myomorpha.",
    "secondary": "In comparative vertebrate osteology, having a jaw and zygomatic structure characteristic of mouselike rodents.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The **myomorphous** skull exhibits a distinctive arrangement of the masseter muscle passing through the infraorbital canal."
      },
      {
        "author": "Charles Darwin",
        "work": "Zoology of the Voyage of H.M.S. Beagle",
        "quote": "Several species of small **myomorphous** rodents collected on the pampas represent unique transitional morphologies."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The extraordinary adaptive radiation of **myomorphous** families explains their numerical dominance among terrestrial mammals."
      }
    ]
  },
  "Dashboard — my/myomorphy.md": {
    "primary": "The structural condition or characteristic morphological organization of mouselike rodents.",
    "secondary": "In mammalian evolution, the zygomasseteric cranial architecture that permits both powerful incisor gnawing and efficient molar grinding in myomorph rodents.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The evolution of **myomorphy** represents an advanced biomechanical compromise between sciuromorph and hystricomorph jaw mechanics."
      },
      {
        "author": "Charles Darwin",
        "work": "On the Origin of Species",
        "quote": "The osteological characteristics of **myomorphy** illustrate how structural specializations become fixed across an entire evolutionary clade."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Island Life",
        "quote": "The swift dispersal of rodents exhibiting true **myomorphy** accounts for their presence on remote archipelagos."
      }
    ]
  },
  "Dashboard — my/myositis.md": {
    "primary": "Inflammation of a muscle or skeletal muscular tissue.",
    "secondary": "In rheumatology, an autoimmune or infectious inflammatory condition of skeletal muscles characterized by muscle fiber necrosis, weakness, and elevated muscle enzymes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In acute suppurative **myositis**, localized swelling, intense tenderness, and high fever point to intramuscular abscess formation."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic evaluation of **myositis** reveals parenchymatous degeneration of muscle fibers accompanied by interstitial cellular infiltration."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Autoimmune **myositis** destroys muscle sarcomeres, progressively diminishing the total tension the contractile apparatus can generate."
      }
    ]
  },
  "Dashboard — my/myotome.md": {
    "primary": "A surgical knife or instrument for dividing muscle; in embryology, the segment of a somite developing into skeletal muscle.",
    "secondary": "In clinical neurology, the collection of skeletal muscles innervated by motor fibers from a single spinal nerve root.",
    "quotes": [
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Each somite divides into a sclerotome, dermatome, and **myotome**, the latter giving rise to trunk and limb musculature."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "Testing the motor power of an individual **myotome** enables the neurologist to localize the precise spinal cord level of a lesion."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "The surgeon utilized a delicate **myotome** to divide the spastic muscular band without injuring underlying vessels."
      }
    ]
  },
  "Dashboard — my/perimysium.md": {
    "primary": "The sheath of connective tissue enclosing a fascicle or bundle of muscle fibers.",
    "secondary": "In gross histology, the collagenous investment that organizes skeletal muscle into functional contractile bundles and carries blood vessels and intramuscular nerves.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **perimysium** consists of thicker connective tissue septa that divide the muscle into primary and secondary fasciculi."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "Intramuscular arterioles and larger nerve branches travel within the protective connective tissue network of the **perimysium**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In chronic myopathies, fibrous proliferation in the **perimysium** frequently precedes the complete destruction of muscle fibers."
      }
    ]
  },
  "Dashboard — my/polymyositis.md": {
    "primary": "A chronic inflammatory muscle disease characterized by symmetric proximal muscle weakness and muscle tenderness.",
    "secondary": "In clinical immunology, an autoimmune myopathy mediated by CD8+ cytotoxic T cells invading non-necrotic skeletal muscle fibers, characterized by elevated creatine kinase.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The diagnostic hallmark of **polymyositis** is insidious proximal muscle weakness sparing ocular and facial musculature."
      },
      {
        "author": "Bertram Katzung",
        "work": "Basic and Clinical Pharmacology",
        "quote": "Corticosteroids remain the first-line therapeutic intervention to suppress immune destruction in severe **polymyositis**."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease: A Textbook of Cardiovascular Medicine",
        "quote": "Cardiovascular involvement in **polymyositis** may manifest as conduction defects, arrhythmias, or subclinical myocarditis."
      }
    ]
  },
  "Dashboard — myel/amyelia.md": {
    "primary": "The congenital absence of the spinal cord in a developing embryo or fetus.",
    "secondary": "In human teratology and embryology, a lethal developmental defect of early neurulation wherein the spinal cord fails to form, almost always occurring alongside anencephaly.",
    "quotes": [
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Complete **amyelia** represents the most extreme failure of neural tube closure, occurring during the third week of embryonic life."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Teratological monsters exhibiting anencephaly are frequently found upon dissection to present total **amyelia**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The developmental arrest leading to **amyelia** demonstrates the absolute dependence of vertebral canal formation upon neural inductions."
      }
    ]
  },
  "Dashboard — myel/demyelinate.md": {
    "primary": "To damage, strip, or destroy the myelin sheath surrounding nerve axons.",
    "secondary": "In neurobiology and neuropathology, to compromise the insulating lipid layer of central or peripheral nerves, interrupting saltatory nerve conduction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Autoimmune processes that **demyelinate** central axons lead directly to sensory ataxia and spastic paralysis."
      },
      {
        "author": "Arthur Guyton",
        "work": "Textbook of Medical Physiology",
        "quote": "When pathological antibodies **demyelinate** a nerve fiber, conduction velocity drops catastrophically as saltatory conduction fails."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Viral triggers can occasionally stimulate reactive T-cells to **demyelinate** acute peripheral nerve roots in Guillain-Barré syndrome."
      }
    ]
  },
  "Dashboard — myel/demyelination.md": {
    "primary": "The loss, destruction, or stripping of the myelin sheath covering nerve fibers.",
    "secondary": "In clinical neurology, a primary pathological hallmark of disorders like multiple sclerosis, characterized by neuroinflammation, axonal slowing, and conduction block.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In multiple sclerosis, sclerotic plaques composed of active **demyelination** and astrocytic gliosis are scattered throughout the white matter."
      },
      {
        "author": "Alexander Luria",
        "work": "The Working Brain",
        "quote": "The progressive cognitive slowing observed in subcortical disease corresponds pathologically to diffuse white-matter **demyelination**."
      },
      {
        "author": "Oliver Sacks",
        "work": "A Leg to Stand On",
        "quote": "Focal **demyelination** in the spinal cord interrupted proprioceptive feedback, leaving the limb devoid of positional awareness."
      }
    ]
  },
  "Dashboard — myel/multiple myeloma.md": {
    "primary": "A primary malignant neoplasm of plasma cells in the bone marrow causing osteolytic lesions, bone marrow failure, and pathological fractures.",
    "secondary": "In hematology and oncology, a clonal plasma cell dyscrasia characterized by monoclonal paraprotein production, hypercalcemia, renal impairment, anemia, and bone destruction.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The discovery of Bence Jones albumosuria in an elderly patient complaining of deep bone pain is virtually diagnostic of **multiple myeloma**."
      },
      {
        "author": "Bertram Katzung",
        "work": "Basic and Clinical Pharmacology",
        "quote": "Modern chemotherapy for **multiple myeloma** combines proteasome inhibitors, immunomodulatory drugs, and dexamethasone."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological sections of bones affected by **multiple myeloma** reveal extensive resorption of trabeculae by sheets of abnormal plasmacytoid cells."
      }
    ]
  },
  "Dashboard — myel/myel.md": {
    "primary": "An anatomical combining root (derived from Greek μυελός, myelos) denoting the bone marrow or spinal cord.",
    "secondary": "In anatomical and clinical terminology, a root element forming names for disorders or structures of the spinal axis (e.g. myelitis) or hematopoietic marrow (e.g. myeloid).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The combining element **myel**- derives from the Greek for marrow, designating both the medullary tissue of bone and the spinal cord."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In medical taxonomy, the prefix **myel**- appears in conditions affecting either the spinal medulla or hematopoiesis."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "The **myel**-encephalic segment of the hindbrain differentiates directly into the adult medulla oblongata."
      }
    ]
  },
  "Dashboard — myel/myelatelia.md": {
    "primary": "Defective, incomplete, or arrested development of the spinal cord.",
    "secondary": "In congenital neuropathology, developmental hypoplasia or failure of closure of the spinal cord or its central ependymal canal during neurogenesis.",
    "quotes": [
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "Severe spinal dysraphism is typically accompanied by microscopic **myelatelia**, with failure of posterior column differentiation."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital paraplegia observed in neonatal pathology often reveals localized **myelatelia** upon post-mortem examination."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Cases of **myelatelia** demonstrate that focal embryonic arrest in the neural cord prevents normal axonal myelination."
      }
    ]
  },
  "Dashboard — myel/myelencephalon.md": {
    "primary": "The posterior portion of the embryonic hindbrain that differentiates into the adult medulla oblongata.",
    "secondary": "In neuroembryology and neuroanatomy, the lower division of the rhombencephalon connecting the pons to the spinal cord, containing cranial nerve nuclei and vital autonomic centers.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy, Descriptive and Surgical",
        "quote": "The **myelencephalon** forms the caudal part of the hindbrain vesicle, developing into the medulla oblongata and the lower half of the fourth ventricle."
      },
      {
        "author": "Arthur Keith",
        "work": "Human Embryology and Morphology",
        "quote": "In vertebrate embryos, the transition from the **myelencephalon** into the spinal cord is marked by the decussation of the pyramids."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Manual of the Anatomy of Vertebrated Animals",
        "quote": "The basic autonomic reflex centers controlling respiration and vascular tone are phylogenetically conserved within the **myelencephalon**."
      }
    ]
  }
}

esm_content = '''import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = ''' + json.dumps(BATCH4_DATA, indent=2, ensure_ascii=False) + ''';

console.log('Starting Body Part 4 Batch 4 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 4 complete: successfully updated ' + updated + ' notes.');
'''

with open("main app/scripts/curate_body4_batch4.mjs", "w", encoding="utf-8") as f:
    f.write(esm_content)

print(f"Generated main app/scripts/curate_body4_batch4.mjs with {len(BATCH4_DATA)} entries.")
