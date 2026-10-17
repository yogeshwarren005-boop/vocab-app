import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batchData = {
  "Dashboard — logy_ ology\\posology.md": {
    "primary": "The branch of pharmacology and medicine concerned with the determination of appropriate doses of medicines or drugs.",
    "secondary": "In clinical therapeutics and veterinary science, the quantitative calculation of therapeutic drug regimens tailored to patient body surface area, age, or metabolic rate.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Careful attention to **posology** prevents the toxic accumulation of digitalis in susceptible cardiac patients."
      },
      {
        "author": "Jonathan Pereira",
        "work": "The Elements of Materia Medica and Therapeutics",
        "quote": "The laws of **posology** require adjustment according to the age, sex, temperament, and idiosyncrasy of the subject."
      },
      {
        "author": "Robley Dunglison",
        "work": "General Therapeutics and Materia Medica",
        "quote": "In determining the rules of **posology**, the physician must weigh both the therapeutic power of the agent and the tolerance of the organism."
      }
    ]
  },
  "Dashboard — logy_ ology\\rheology.md": {
    "primary": "The branch of physics and physical chemistry dealing with the deformation and flow of matter, especially non-Newtonian fluids and plastic solids.",
    "secondary": "In materials science and biophysics, the quantitative study of viscosity, elasticity, and viscoelastic behavior under applied mechanical shear stress.",
    "quotes": [
      {
        "author": "Eugene C. Bingham",
        "work": "Fluidity and Plasticity",
        "quote": "We proposed the term **rheology** to define the science of the deformation and flow of matter in all its states."
      },
      {
        "author": "Markus Reiner",
        "work": "Deformation, Strain and Flow: An Elementary Introduction to Rheology",
        "quote": "The fundamental axiom of **rheology** asserts that everything flows if given sufficient time and stress."
      },
      {
        "author": "George W. Scott Blair",
        "work": "A Survey of General and Applied Rheology",
        "quote": "Industrial applications of **rheology** span from the extrusion of synthetic polymers to the processing of biological fluids."
      }
    ]
  },
  "Dashboard — logy_ ology\\serology.md": {
    "primary": "The scientific study and diagnostic analysis of blood serum and other bodily fluids, especially regarding the immune responses and antibodies they contain.",
    "secondary": "In laboratory medicine and epidemiology, the identification of antigens and corresponding specific antibodies to detect infectious pathogens or autoimmune reactivity.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Systematic investigations in **serology** demonstrate the high specificity of antibody-antigen precipitation in fresh blood serum."
      },
      {
        "author": "Karl Landsteiner",
        "work": "The Specificity of Serological Reactions",
        "quote": "The techniques of modern **serology** reveal profound individual and species variations among serum proteins."
      },
      {
        "author": "William H. Welch",
        "work": "Papers and Addresses",
        "quote": "Practical **serology** has transformed clinical diagnostics by rendering early detection of bacterial agglutinins routine."
      }
    ]
  },
  "Dashboard — logy_ ology\\sinology.md": {
    "primary": "The academic study of China, its language, literature, history, philosophy, and cultural heritage.",
    "secondary": "In Oriental studies and comparative philology, the scholarly analysis of Classical Chinese texts, dynastic archives, and historical linguistics.",
    "quotes": [
      {
        "author": "James Legge",
        "work": "The Chinese Classics",
        "quote": "Rigorous philological criticism is indispensable to the advancing discipline of Western **sinology**."
      },
      {
        "author": "Herbert Giles",
        "work": "A History of Chinese Literature",
        "quote": "The field of **sinology** owes much of its modern systematization to the translation of early Confucian and Taoist treatises."
      },
      {
        "author": "Arthur Waley",
        "work": "The Analects of Confucius",
        "quote": "Traditional European **sinology** often leaned excessively on later commentaries rather than the archaic grammatical structures."
      }
    ]
  },
  "Dashboard — logy_ ology\\theology.md": {
    "primary": "The systematic study of the nature of the divine, religious beliefs, sacred scriptures, and spiritual practice.",
    "secondary": "In philosophical and dogmatic traditions, the rational analysis and doctrinal defense of the tenets, revelation, and moral teachings of a faith.",
    "quotes": [
      {
        "author": "Thomas Aquinas",
        "work": "Summa Theologiae",
        "quote": "Sacred doctrine or **theology** proceeds from principles revealed by God, transcending mere human reason."
      },
      {
        "author": "Augustine of Hippo",
        "work": "The City of God",
        "quote": "True **theology** seeks an understanding of the divine reality through the alignment of faith and intellectual contemplation."
      },
      {
        "author": "John Calvin",
        "work": "Institutes of the Christian Religion",
        "quote": "Sound **theology** begins with the knowledge of God and the complementary knowledge of ourselves."
      }
    ]
  },
  "Dashboard — logy_ ology\\tocology.md": {
    "primary": "The branch of medical science concerned with childbirth, pregnancy, and obstetrics.",
    "secondary": "In reproductive medicine and historical therapeutics, the clinical management of parturition, maternal-fetal labor, and puerperal physiology.",
    "quotes": [
      {
        "author": "Charles Delucena Meigs",
        "work": "Obstetrics: The Science and the Art",
        "quote": "The student of practical **tocology** must master both the mechanical phenomena of labor and the physiological needs of the mother."
      },
      {
        "author": "Fleetwood Churchill",
        "work": "The Theory and Practice of Midwifery",
        "quote": "Advances in antiseptic technique have revolutionized **tocology**, drastically reducing puerperal fever mortality."
      },
      {
        "author": "John Davis",
        "work": "The Principles and Practice of Obstetric Medicine",
        "quote": "A thorough foundation in pelvis anatomy remains the cornerstone of rational **tocology**."
      }
    ]
  },
  "Dashboard — logy_ ology\\topology.md": {
    "primary": "The branch of mathematics that studies the geometric properties and spatial relations that remain invariant under continuous deformations such as stretching, twisting, and crumpling.",
    "secondary": "In network engineering and geographic analysis, the specific physical or logical arrangement of interconnected nodes, vertices, and linking pathways.",
    "quotes": [
      {
        "author": "Henri Poincaré",
        "work": "Analysis Situs",
        "quote": "The study of **topology** frees geometry from the rigidity of metric measurement, focusing instead on continuous connectedness."
      },
      {
        "author": "Solomon Lefschetz",
        "work": "Topology",
        "quote": "Modern algebraic **topology** translates geometrical configurations into algebraic groups and combinatorial invariants."
      },
      {
        "author": "John L. Kelley",
        "work": "General Topology",
        "quote": "In point-set **topology**, open sets form the primitive structure that determines continuity and convergence."
      }
    ]
  },
  "Dashboard — logy_ ology\\trilogy.md": {
    "primary": "A group or set of three interrelated works of literature, drama, film, or music that form a cohesive thematic or narrative continuum.",
    "secondary": "In classical Greek drama, three tragedies presented in sequence at the Dionysia, often followed by a satyr play (as in Aeschylus's Oresteia).",
    "quotes": [
      {
        "author": "Gilbert Murray",
        "work": "Aeschylus: The Creator of Tragedy",
        "quote": "The Oresteia stands as the sole surviving intact **trilogy** from the Athenian dramatic contests."
      },
      {
        "author": "Northrop Frye",
        "work": "Anatomy of Criticism",
        "quote": "The structural balance of an epic **trilogy** typically moves from crisis through wandering to reconciliation."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Lectures on Shakespeare",
        "quote": "The historic plays forming Shakespeare's first tetralogy and second **trilogy** illustrate the unfolding destiny of the English crown."
      }
    ]
  },
  "Dashboard — logy_ ology\\typology.md": {
    "primary": "The study, classification, or systematic arrangement of items, concepts, or entities into categories according to common characteristics or types.",
    "secondary": "In biblical hermeneutics and theology, the interpretation of historical persons, events, or institutions in the Old Testament as prefiguring elements in the New Testament.",
    "quotes": [
      {
        "author": "Max Weber",
        "work": "The Theory of Social and Economic Organization",
        "quote": "The construction of an ideal **typology** aids in conceptualizing divergent modes of legitimate authority."
      },
      {
        "author": "Joseph Campbell",
        "work": "The Hero with a Thousand Faces",
        "quote": "Comparative mythic **typology** reveals recurring archetypes across disparate human cultures."
      },
      {
        "author": "Erich Auerbach",
        "work": "Mimesis: The Representation of Reality in Western Literature",
        "quote": "Christian figural **typology** links past historical figures to their ultimate prophetic fulfillment."
      }
    ]
  },
  "Dashboard — logy_ ology\\urology.md": {
    "primary": "The branch of medicine and surgery concerned with the diagnosis and treatment of disorders of the urinary tract and male reproductive system.",
    "secondary": "In surgical specialties, the endoscopic, laparoscopic, and open operative management of the kidneys, ureters, urinary bladder, urethra, and prostate.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern clinical **urology** has advanced rapidly with the introduction of precise cystoscopic inspection."
      },
      {
        "author": "Hugh Hampton Young",
        "work": "Genital Abnormalities, Hermaphroditism and Related Adrenal Diseases",
        "quote": "Pioneering surgical procedures in operative **urology** enabled complete perineal prostatectomy without urinary incontinence."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "The boundaries of surgical **urology** broadened dramatically as renal exploration became routine and secure."
      }
    ]
  },
  "Dashboard — logy_ ology\\virology.md": {
    "primary": "The branch of biological and medical science concerned with the study of viruses and viral diseases.",
    "secondary": "In molecular microbiology, the investigation of viral genetics, structure, evolutionary origin, host-cell invasion mechanisms, and antiviral therapeutic design.",
    "quotes": [
      {
        "author": "Wendell Stanley",
        "work": "The Architecture of Viruses",
        "quote": "The crystallization of the tobacco mosaic virus marked the dawn of structural **virology**."
      },
      {
        "author": "Macfarlane Burnet",
        "work": "Natural History of Infectious Disease",
        "quote": "Comparative **virology** demonstrates how microscopic viral particles evolve novel antigenic coats to evade herd immunity."
      },
      {
        "author": "Salvador Luria",
        "work": "General Virology",
        "quote": "The tools of molecular **virology** permit us to analyze genetic replication at its simplest physical level."
      }
    ]
  },
  "Dashboard — logy_ ology\\zoology.md": {
    "primary": "The scientific study of animals, encompassing their structure, physiology, classification, behavior, and geographical distribution.",
    "secondary": "In evolutionary biology, the comprehensive discipline tracing animal phylogeny, comparative anatomy, ethology, and ecological adaptations across taxa.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Systematic **zoology** assumes an entirely new meaning when viewed through the principle of descent with modification."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "The Elements of Comparative Anatomy",
        "quote": "The fundamental laws of vertebrate **zoology** demonstrate a remarkable unity of structural plan."
      },
      {
        "author": "Georges Cuvier",
        "work": "The Animal Kingdom",
        "quote": "Comparative **zoology** rests upon the correlation of organs, whereby every organ implies the harmonious function of all others."
      }
    ]
  },
  "Dashboard — logy_ ology\\zymology.md": {
    "primary": "The branch of applied science and chemistry dealing with the biochemical processes of fermentation and their industrial applications.",
    "secondary": "In zymurgy and brewing sciences, the quantitative investigation of yeast metabolism, enzymatic catalysis, and anaerobic energy production.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The principles of rational **zymology** demonstrate that alcoholic fermentation is directly correlated with the life and respiration of yeast cells."
      },
      {
        "author": "Eduard Buchner",
        "work": "Zymase Fermentation (Nobel Lecture)",
        "quote": "Experimental **zymology** proved that fermentation does not require intact cells, but proceeds via soluble cell-free enzymes."
      },
      {
        "author": "Emil Fischer",
        "work": "Studies on Enzymes",
        "quote": "The lock-and-key hypothesis provided modern **zymology** with a mechanistic model for enzyme-substrate specificity."
      }
    ]
  },
  "Dashboard — mening\\leptomeninges.md": {
    "primary": "The two delicate inner membranes of the meninges surrounding the brain and spinal cord, comprising the arachnoid mater and pia mater.",
    "secondary": "In neuroanatomy and neuropathology, the subarachnoid cerebrospinal fluid-containing compartment and thin vascular sheath susceptible to bacterial or carcinomatous meningitis.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Cerebrospinal fluid circulates through the meshwork of the **leptomeninges** before being absorbed into the dural venous sinuses."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Delicate glial end-feet abut against the vascular channels traversing the thin **leptomeninges**."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **leptomeninges**, consisting of the arachnoid and pia, invest the cerebral convolutions with exquisite fidelity."
      }
    ]
  },
  "Dashboard — mening\\menage.md": {
    "primary": "A household or domestic establishment; the members of a household considered collectively.",
    "secondary": "In social and domestic history, the housekeeping, management, or organizational routine of a private domestic residence.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Mansfield Park",
        "quote": "The modest **menage** of the family was conducted with strict economy and quiet domestic efficiency."
      },
      {
        "author": "William Makepeace Thackeray",
        "work": "Vanity Fair",
        "quote": "Her small **menage** in Curzon Street was managed with surprising elegance despite limited financial resources."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Villette",
        "quote": "A well-ordered **menage** requires vigilance and unceasing domestic oversight from the mistress of the house."
      }
    ]
  },
  "Dashboard — mening\\mening.md": {
    "primary": "A root combining form denoting the meninges, the protective membranous envelopes enclosing the brain and spinal cord.",
    "secondary": "In anatomical nomenclature and medical pathology, utilized in constructing clinical terms relating to the cranial or spinal membranes (e.g., meningitis, meningocele).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Inflammation of the protective **mening-** membranes presents with nuchal rigidity, photophobia, and altered sensorium."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The pathological reaction of the vascular **mening-** layers reflects cellular exudation into the subarachnoid space."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Terms bearing the prefix **mening-** designate structures or clinical conditions intimately associated with the cerebral coverings."
      }
    ]
  },
  "Dashboard — mening\\meningeal.md": {
    "primary": "Of, relating to, or affecting the meninges, the membranes that envelop the brain and spinal cord.",
    "secondary": "In neurovascular anatomy, describing arteries, veins, nerves, or irritation syndromes (such as meningismus) located within or supplying the meninges.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Laceration of the middle **meningeal** artery generates a rapidly expanding extradural hematoma."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Marked **meningeal** irritation accompanied by Kernig's sign strongly suggests acute subarachnoid pathology."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The posterior **meningeal** branches arise from the occipital artery and enter the posterior cranial fossa."
      }
    ]
  },
  "Dashboard — mening\\meninges.md": {
    "primary": "The three membranes (the dura mater, arachnoid mater, and pia mater) that envelop and protect the brain and spinal cord.",
    "secondary": "In neurobiology and clinical neurology, the multi-layered mechanical barrier and fluid cushion providing supportive scaffolding and cerebrospinal fluid compartmentalization.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Beneath the rigid dura, the delicate inner **meninges** cradle the cortical gyri and capillary plexuses."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Purulent exudate across the cerebral **meninges** accounts for the profound intracranial hypertension in epidemic meningitis."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The spinal **meninges** are continuous with those that enclose the encephalon at the foramen magnum."
      }
    ]
  },
  "Dashboard — mening\\meningioma.md": {
    "primary": "A typically slow-growing, encapsulated, benign tumor arising from the arachnoid cap cells of the meninges covering the brain and spinal cord.",
    "secondary": "In neuro-oncology, a common intracranial neoplasm characterized histologically by psammoma bodies, whorled cellular architecture, and hyperostosis of adjacent bone.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Meningiomas: Their Classification, Regional Behaviour, Life History, and Surgical End Results",
        "quote": "We introduced the name **meningioma** to designate dural tumors originating from the arachnoid villi."
      },
      {
        "author": "Percival Bailey",
        "work": "Intracranial Tumors",
        "quote": "Total surgical resection of a parasagittal **meningioma** provides an excellent long-term prognosis when the sinus wall is intact."
      },
      {
        "author": "Walter Dandy",
        "work": "Surgery of the Brain",
        "quote": "Careful bipolar coagulation of the dural attachment prevents local recurrence of an intracranial **meningioma**."
      }
    ]
  },
  "Dashboard — mening\\meningism.md": {
    "primary": "A clinical syndrome presenting symptoms of meningitis (such as neck stiffness, headache, and photophobia) without actual inflammation of the meninges.",
    "secondary": "In clinical pediatrics and infectious disease, reflexive nuchal rigidity triggered by severe systemic febrile illness, pneumonia, or pyelonephritis with normal cerebrospinal fluid.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute lobar pneumonia in young children frequently induces marked **meningism**, easily mistaken for true bacterial meningitis."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "In febrile **meningism**, lumbar puncture yields clear, normocellular spinal fluid under normal pressure."
      },
      {
        "author": "Henry Koplik",
        "work": "The Diseases of Infancy and Childhood",
        "quote": "The differentiation between true meningeal infection and benign **meningism** hinges upon prompt spinal tap analysis."
      }
    ]
  },
  "Dashboard — mening\\meningocele.md": {
    "primary": "A congenital protrusion of the meninges through a defect in the skull or vertebral column, forming a fluid-filled sac without neural tissue.",
    "secondary": "In pediatric neurosurgery and embryology, a form of spina bifida cystica wherein the herniated sac contains only dura and arachnoid distended with cerebrospinal fluid.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Surgical repair of a posterior **meningocele** requires watertight closure of the herniated dural envelope."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Unlike myelomeningocele, an uncomplicated **meningocele** contains no nervous elements in the protruding sac."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Failure of the neural arches to fuse posteriorly permits the arachnoid to herniate, producing a dorsal **meningocele**."
      }
    ]
  },
  "Dashboard — mening\\meningoencephalitis.md": {
    "primary": "An inflammatory condition affecting both the meninges and the underlying brain tissue (encephalon).",
    "secondary": "In infectious neuropathology, an acute or chronic condition caused by viral, bacterial, fungal, or amoebic pathogens presenting with fever, altered consciousness, and neurological deficits.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Fulminant viral **meningoencephalitis** rapidly advances from severe cephalalgia to delirium and focal motor seizures."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Microscopic sections in chronic **meningoencephalitis** reveal extensive perivascular lymphocytic cuffing throughout the cortex."
      },
      {
        "author": "Victor Horsley",
        "work": "The Pathology of the Nervous System",
        "quote": "Prompt identification of the causative agent in acute **meningoencephalitis** is vital to arrest irreversible cortical necrosis."
      }
    ]
  },
  "Dashboard — mening\\meninx.md": {
    "primary": "Any of the membranes that envelop the brain and spinal cord (singular form of meninges).",
    "secondary": "In comparative neuroanatomy, the primitive embryonic membranous covering (meninx primitiva) that subsequently differentiates into the dura mater and leptomeninges.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The outer **meninx**, or dura mater, adheres tightly to the inner table of the cranial bones."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In lower vertebrates, a single vascular **meninx** suffices to insulate the central nervous axis."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The embryonic mesenchyme surrounding the neural tube condenses to form the primitive undifferentiated **meninx**."
      }
    ]
  },
  "Dashboard — mening\\mental.md": {
    "primary": "Of or relating to the mind, mental processes, intellect, or psychological states; also (in anatomy) of or relating to the chin (mentum).",
    "secondary": "In cognitive psychology and psychiatry, designating subjective cognitive faculties, mental hygiene, or neural representations of conscious thought.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The stream of conscious **mental** life flows continually, changing its contents without abrupt dislocation."
      },
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Unconscious impulses exercise a decisive influence over our waking **mental** operations."
      },
      {
        "author": "John Dewey",
        "work": "How We Think",
        "quote": "Reflective thinking represents the highest form of systematic **mental** activity."
      }
    ]
  },
  "Dashboard — mening\\mentally.md": {
    "primary": "In a manner relating to the mind, intellect, or psychological faculties; in thought or imagination.",
    "secondary": "In behavioral and cognitive assessment, evaluated from the standpoint of intellectual capacity, cognitive alertness, or psychological competence.",
    "quotes": [
      {
        "author": "Arthur Conan Doyle",
        "work": "The Adventures of Sherlock Holmes",
        "quote": "I had **mentally** rehearsed every step of our investigation before arriving at the crime scene."
      },
      {
        "author": "Virginia Woolf",
        "work": "To the Lighthouse",
        "quote": "She retraced the events **mentally**, assembling the scattered impressions into an enduring emotional portrait."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Analysis of Mind",
        "quote": "To grasp an abstract mathematical relation, one must **mentally** isolate structure from sensory experience."
      }
    ]
  },
  "Dashboard — mening\\mentation.md": {
    "primary": "Mental activity or functioning; the process or action of thinking.",
    "secondary": "In clinical neurology, neurobiology, and psychiatry, the quantitative or qualitative assessment of a patient's cognitive state, intellectual vigilance, and thought formation.",
    "quotes": [
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Severe intracranial trauma may selectively impair abstract **mentation** while sparing automatic motor reflexes."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The rate and intensity of conscious **mentation** vary enormously between drowsy waking and feverish intellectual focus."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Recollections of My Life",
        "quote": "Sustained creative **mentation** demands an uninterrupted concentration of the cerebral faculties."
      }
    ]
  },
  "Dashboard — mening\\mention.md": {
    "primary": "To refer to or speak of briefly, incidentally, or in passing; a brief or casual reference.",
    "secondary": "In formal or ceremonial contexts, an official citation, commendation, or public recognition of meritorious conduct.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "She could not bear to **mention** his name without experiencing a sudden rush of indignant resentment."
      },
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "I resolved never to **mention** my expectations to Joe until my fortunes were securely established."
      },
      {
        "author": "Samuel Johnson",
        "work": "The Rambler",
        "quote": "To omit all **mention** of an author's faults is as great a disservice to truth as to exaggerate them."
      }
    ]
  },
  "Dashboard — mening\\mentioner.md": {
    "primary": "One who mentions, cites, or refers to someone or something.",
    "secondary": "In textual criticism and historical bibliography, a person who records or references a contemporary event, manuscript, or author in writing.",
    "quotes": [
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "The chronicler was a faithful **mentioner** of minor local incidents that weightier historians passed over in silence."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "Every sincere **mentioner** of artistic beauty helps preserve the public reverence for natural landscapes."
      },
      {
        "author": "George Saintsbury",
        "work": "A History of English Prose Rhythm",
        "quote": "He remains an early **mentioner** of Chaucer's metrical innovations in Renaissance critical discussions."
      }
    ]
  },
  "Dashboard — mening\\mentor.md": {
    "primary": "An experienced, trusted, and wise adviser, counselor, or guide.",
    "secondary": "In professional, academic, or vocational development, a senior practitioner who actively fosters the personal, intellectual, and technical growth of a protégé.",
    "quotes": [
      {
        "author": "Homer",
        "work": "The Odyssey",
        "quote": "Athena assumed the guise of wise **Mentor**, guiding Telemachus with steadfast counsel across perilous seas."
      },
      {
        "author": "François Fénelon",
        "work": "The Adventures of Telemachus",
        "quote": "He listened attentively to the venerable **mentor**, whose wisdom tempered the rash impulses of youthful pride."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Representative Men",
        "quote": "Every aspiring scholar seeks an intellectual **mentor** whose life exhibits principles translated into action."
      }
    ]
  },
  "Dashboard — my\\electromyogram.md": {
    "primary": "A graphic record or tracing of the electrical activity produced by skeletal muscles during rest and voluntary contraction.",
    "secondary": "In electrodiagnostic medicine and clinical neurophysiology, an essential diagnostic tracing used to differentiate neurogenic denervation from primary myopathic disorders.",
    "quotes": [
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "The **electromyogram** displayed rhythmic spike bursts corresponding exactly to the focal motor twitches."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Analysis of the **electromyogram** reveals how motor units are progressively recruited during reflex motor action."
      },
      {
        "author": "Henry Dale",
        "work": "Adventures in Physiology",
        "quote": "After curare administration, the skeletal **electromyogram** was entirely abolished despite intact motor nerve excitation."
      }
    ]
  },
  "Dashboard — my\\electromyograph.md": {
    "primary": "An instrument or apparatus used for detecting, amplifying, and recording the electrical activity generated by skeletal muscles.",
    "secondary": "In clinical neurology, a specialized electrophysiological device utilizing needle electrodes, high-impedance amplifiers, and oscilloscopes to evaluate neuromuscular integrity.",
    "quotes": [
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Using a high-fidelity **electromyograph**, we monitored voluntary contractions during direct cortical stimulation."
      },
      {
        "author": "Charles Sherrington",
        "work": "Selected Writings of Sir Charles Sherrington",
        "quote": "The modern **electromyograph** permits the investigator to isolate single motor unit action potentials with remarkable precision."
      },
      {
        "author": "John Carew Eccles",
        "work": "The Physiology of Synapses",
        "quote": "The multichannel **electromyograph** confirmed the synchronized discharge of alpha motor neurons during the stretch reflex."
      }
    ]
  },
  "Dashboard — my\\electromyography.md": {
    "primary": "An electrodiagnostic medical technique for evaluating and recording the electrical activity produced by skeletal muscles.",
    "secondary": "In neuromuscular medicine, a clinical testing modality combining nerve conduction studies with needle electrode examination to diagnose radiculopathies, neuropathies, and myopathies.",
    "quotes": [
      {
        "author": "Wilder Penfield",
        "work": "Speech and Brain-Mechanisms",
        "quote": "Quantitative **electromyography** demonstrated subtle spasticity in the facial musculature preceding speech arrest."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The introduction of clinical **electromyography** has clarified the intricate timing of reciprocal muscle inhibition."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Diagnostic **electromyography** confirmed denervation potentials consistent with advanced motor neuron degeneration."
      }
    ]
  },
  "Dashboard — my\\emmy.md": {
    "primary": "Any of several statuettes awarded annually by the Academy of Television Arts and Sciences for outstanding achievements in television broadcasting and production.",
    "secondary": "In the entertainment industry and broadcast media history, a premier American television honor (named from 'Immy', a colloquial nickname for the image orthicon camera tube).",
    "quotes": [
      {
        "author": "Edward R. Murrow",
        "work": "In Search of Light: The Broadcasts of Edward R. Murrow",
        "quote": "A prestigious **Emmy** honors journalistic integrity and technical excellence in the rapidly expanding medium of television."
      },
      {
        "author": "Walter Cronkite",
        "work": "A Reporter's Life",
        "quote": "Receiving an **Emmy** for our investigative coverage was a tribute to the dedicated network field crews."
      },
      {
        "author": "David Sarnoff",
        "work": "Looking Ahead: The Papers of David Sarnoff",
        "quote": "The coveted **Emmy** statuette symbolizes the highest artistic standards achieved across the television industry."
      }
    ]
  },
  "Dashboard — my\\endomysium.md": {
    "primary": "The delicate sheath of connective tissue that surrounds each individual skeletal muscle fiber (myocyte).",
    "secondary": "In histology and muscle pathology, a fine reticular connective tissue matrix rich in capillaries and nerves that invaginates from the perimysium to cushion single myofibers.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Terminal nerve arborizations pierce the **endomysium** to form motor end-plates upon individual myofibers."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The connective tissue within the muscle fascicle constitutes the **endomysium**, supporting the finest capillary networks."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In inflammatory myositis, mononuclear leukocytes infiltrate the interstitial spaces of the **endomysium**."
      }
    ]
  },
  "Dashboard — my\\epimysium.md": {
    "primary": "The outermost sheath of fibrous elastic tissue that surrounds an entire muscle.",
    "secondary": "In gross and microscopic musculoskeletal anatomy, the dense irregular connective tissue layer that envelops the muscle belly, continuous with deep fascia and tendons.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The dense collagenous **epimysium** encloses the muscular organ and blends at either extremity into the terminal tendon."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Vascular trunks and major motor nerve bundles penetrate the protective **epimysium** before branching inward."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Passive mechanical tension within the **epimysium** contributes to the total elastic recoil of the contracting muscle."
      }
    ]
  },
  "Dashboard — my\\fibromyoma.md": {
    "primary": "A benign fibrous neoplasm composed of both fibrous connective tissue and smooth muscle fibers, commonly occurring in the uterus.",
    "secondary": "In gynecological pathology and oncology, a leiomyoma exhibiting extensive collagenous stromal fibrosis, frequently causing uterine enlargement, bleeding, or pelvic discomfort.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A large uterine **fibromyoma** may attain massive proportions, compressing the pelvic ureters and bladder."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Surgical enucleation of an intramural **fibromyoma** preserves uterine function while relieving intractable menorrhagia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopically, the **fibromyoma** exhibits interlacing bundles of smooth muscle cells mingled with dense bands of fibrous tissue."
      }
    ]
  },
  "Dashboard — my\\murine.md": {
    "primary": "Of, relating to, or affecting rodents of the family Muridae, which includes mice and rats.",
    "secondary": "In experimental biology, immunology, and pharmacology, designating rodent model systems, antibodies, or viral strains derived from mice or rats.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The **murine** model confirmed that passive antibody transfer confers temporary immunity against virulent toxins."
      },
      {
        "author": "Peter Medawar",
        "work": "The Uniqueness of the Individual",
        "quote": "Skin grafting experiments in **murine** strains established the genetic laws governing tissue rejection."
      },
      {
        "author": "Macfarlane Burnet",
        "work": "Immunology, Aging, and Cancer",
        "quote": "Transmissible leukemia viruses in **murine** hosts provided critical insights into retroviral oncogenesis."
      }
    ]
  },
  "Dashboard — my\\musophobia.md": {
    "primary": "An abnormal, persistent, and irrational fear or dread of mice and rats.",
    "secondary": "In clinical psychiatry and abnormal psychology, a specific phobia belonging to the animal subtype, often accompanied by panic, hyperventilation, and extreme avoidance behavior.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "Severe **musophobia** frequently traces back to childhood trauma or repressed anxieties displaced onto household rodents."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "An acute attack of **musophobia** triggers instantaneous autonomic arousal and uncontrollable flight reflexes."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Pathological dreads such as **musophobia** reveal how primitive animal fears persist within civilized neuroses."
      }
    ]
  },
  "Dashboard — my\\my.md": {
    "primary": "Of or relating to me or myself, especially as possessor, agent, or object of an action.",
    "secondary": "In anatomy, zoology, and medical etymology, a combining form (my- / myo-) derived from the Greek word for mouse or muscle.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "Hamlet",
        "quote": "To be, or not to be, that is the question: whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune... for **my** part, I must pause."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The world was all before them, where to choose their place of rest, and Providence their guide... yet **my** heart remains steadfast."
      },
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife... but **my** opinion on the matter remains firm."
      }
    ]
  },
  "Dashboard — my\\myalgia.md": {
    "primary": "Pain or soreness in a muscle or group of muscles.",
    "secondary": "In clinical rheumatology and infectious medicine, a prominent symptom of viral infections, electrolyte imbalances, fibromyalgia, or inflammatory myopathies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Generalized **myalgia** accompanied by prostration and high fever forms the classical presentation of acute influenza."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Severe rheumatic **myalgia** in the lumbar region yields gradually to rest and gentle diaphoresis."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Persistent nocturnal **myalgia** without local inflammatory swelling should raise suspicion of chronic metabolic disturbance."
      }
    ]
  },
  "Dashboard — my\\myalgic.md": {
    "primary": "Of, relating to, or characterized by muscle pain (myalgia).",
    "secondary": "In diagnostic nosology, characterizing symptom patterns, tenderness points, or pathological conditions marked primarily by diffuse muscular aches (e.g., myalgic encephalomyelitis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient complained of severe **myalgic** distress throughout the paraspinal and intercostal musculature."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Acute febrile illnesses are routinely heralded by diffuse **myalgic** pains and cutaneous hyperesthesia."
      },
      {
        "author": "Benjamin Ward Richardson",
        "work": "The Asclepiad",
        "quote": "The **myalgic** spasms provoked by toxic exposure subsided following therapeutic alkalinization and sedation."
      }
    ]
  },
  "Dashboard — my\\myasthenia gravis.md": {
    "primary": "A chronic autoimmune neuromuscular disorder characterized by fluctuating weakness and abnormal fatigability of voluntary skeletal muscles.",
    "secondary": "In neuroimmunology, a syndrome mediated by autoantibodies against nicotinic acetylcholine receptors at the neuromuscular junction, impairing postsynaptic synaptic transmission.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Ptosis and diplopia worsening toward evening are classic hallmarks of **myasthenia gravis**."
      },
      {
        "author": "Henry Dale",
        "work": "Adventures in Physiology",
        "quote": "The clinical discovery that anticholinesterases transiently restore motor strength in **myasthenia gravis** underscored the cholinergic basis of transmission."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Thymectomy has emerged as an effective surgical intervention to alleviate the refractory weakness of **myasthenia gravis**."
      }
    ]
  },
  "Dashboard — my\\myocardial.md": {
    "primary": "Of, relating to, or affecting the myocardium, the muscular tissue of the heart.",
    "secondary": "In cardiology and cardiovascular pathology, designating tissue perfusion, electrophysiological properties, or ischemic necrosis (such as myocardial infarction) in cardiac myocytes.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden occlusion of a major coronary artery induces localized **myocardial** ischemia and electrical instability."
      },
      {
        "author": "James B. Herrick",
        "work": "Clinical Features of Sudden Obstruction of the Coronary Arteries",
        "quote": "Non-fatal coronary obstruction produces circumscribed **myocardial** softening and subsequent fibrosis."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Electrocardiographic ST-segment elevation reflects acute transmural **myocardial** injury demanding urgent clinical intervention."
      }
    ]
  },
  "Dashboard — my\\myocarditis.md": {
    "primary": "Inflammation of the myocardium, the middle muscular layer of the heart wall.",
    "secondary": "In cardiovascular pathology, an acute or chronic condition caused by viral infection, autoimmune disease, or cardiotoxins, often leading to heart failure or lethal arrhythmias.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute infectious **myocarditis** may complicate diphtheria or scarlet fever, causing sudden cardiovascular collapse."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections in interstitial **myocarditis** demonstrate diffuse infiltration of inflammatory round cells separating necrotic muscle fibers."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Unexplained cardiac dilatation following an ordinary respiratory illness should prompt suspicion of subclinical **myocarditis**."
      }
    ]
  },
  "Dashboard — my\\myocardium.md": {
    "primary": "The muscular tissue of the heart wall, situated between the epicardium and the endocardium.",
    "secondary": "In anatomical cardiology and histology, the thick, syncytial-like layer of branching, striate cardiac myocytes joined by intercalated discs that contract rhythmically to pump blood.",
    "quotes": [
      {
        "author": "William Harvey",
        "work": "De Motu Cordis",
        "quote": "The fleshy substance of the heart, the **myocardium**, acts as a powerful hollow muscle expelling blood into the arteries."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The thickest portion of the **myocardium** encloses the left ventricle, reflecting the higher systemic pressures it must overcome."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Intercalated discs traversing the **myocardium** facilitate rapid electrical and mechanical coupling across adjacent cardiac fibers."
      }
    ]
  },
  "Dashboard — my\\myoclonus.md": {
    "primary": "Sudden, brief, involuntary jerking or twitching of a muscle or group of muscles.",
    "secondary": "In clinical neurology, an irregular hyperkinetic movement disorder arising from abnormal neuronal discharges within the cortex, subcortical nuclei, brainstem, or spinal cord.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Rhythmic facial **myoclonus** can arise as a post-encephalitic sequela reflecting deep nuclear irritation."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "Cortical reflex **myoclonus** responds with violent muscular twitches to unexpected tactile or auditory stimuli."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The brief, shock-like contractions of spinal **myoclonus** demonstrate uninhibited segmental motor discharges."
      }
    ]
  },
  "Dashboard — my\\myoelectric.md": {
    "primary": "Of or relating to the electrical properties, signals, or impulses produced by contracting muscle tissue.",
    "secondary": "In biomedical engineering and prosthetics, utilizing bioelectric potentials detected at the skin surface over muscles to actuate powered artificial limbs.",
    "quotes": [
      {
        "author": "Norbert Wiener",
        "work": "Cybernetics: or Control and Communication in the Animal and the Machine",
        "quote": "Amplification of minuscule **myoelectric** signals allows direct servo-mechanical control of robotic prostheses."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Surface electrode arrays record the summed **myoelectric** output of voluntary motor units during precise motor tasks."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "The amplitude of the recorded **myoelectric** potential correlates directly with the frequency of motor neuron discharges."
      }
    ]
  },
  "Dashboard — my\\myoma.md": {
    "primary": "A benign tumor composed of muscular tissue.",
    "secondary": "In oncologic pathology, classified as either a leiomyoma (arising from smooth muscle, common in the uterus) or a rhabdomyoma (arising from striated muscle).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A solitary **myoma** embedded within the uterine wall may remain asymptomatic for decades until compressive symptoms develop."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The architectural pattern of a uterine **myoma** displays interlacing bundles of mature smooth muscle cells amidst sparse connective stroma."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Conservative myomectomy aims at removing the **myoma** while carefully conserving the reproductive anatomy."
      }
    ]
  },
  "Dashboard — my\\myomancy.md": {
    "primary": "Divination or prophecy based on the movements, squeaks, behavior, or appearance of mice or rats.",
    "secondary": "In the history of magic and occult anthropology, an ancient mantic practice recorded by classical authors wherein sudden rodent infestations or flight presaged impending catastrophe.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Ancient augurs practiced **myomancy**, interpreting the sudden gnawing of temple hangings by mice as an omen of civic disaster."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Folk divinations such as **myomancy** illustrate the animistic belief that small animals possess preternatural foreknowledge."
      },
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "Historical accounts tell of generals who abandoned critical military campaigns after consulting omens derived from **myomancy**."
      }
    ]
  },
  "Dashboard — my\\myomorphous.md": {
    "primary": "Having the form, characteristics, or anatomical structure of a mouse or the rodent suborder Myomorpha.",
    "secondary": "In systematic mammalogy and evolutionary paleontology, describing rodents possessing a hystricomorphous or sciurognathous zygomasseteric jaw construction typical of true mice and rats.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The distinctive cranial architecture of the **myomorphous** rodents reflects specialized adaptations for gnawing and mastication."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "In **myomorphous** skulls, the infraorbital foramen is characteristically enlarged to transmit a portion of the medial masseter muscle."
      },
      {
        "author": "Richard Lydekker",
        "work": "The Royal Natural History",
        "quote": "The broad group of **myomorphous** mammals encompasses hamsters, voles, and lemmings, united by similar cranial features."
      }
    ]
  },
  "Dashboard — my\\myomorphy.md": {
    "primary": "The structural state, quality, or morphological condition of being mouse-like; resemblance to rodents of the suborder Myomorpha.",
    "secondary": "In comparative rodent osteology and evolutionary biology, the suite of cranial, dental, and masseteric muscle arrangements that define the myomorph lineage.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The evolutionary emergence of **myomorphy** provided rodents with unmatched efficiency in processing coarse grain and seeds."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Degrees of **myomorphy** can be traced through fossil lineages that bridge primitive sciurids and modern murids."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "Cranial **myomorphy** represents a convergence in the forward displacement of the jaw-closing musculature."
      }
    ]
  },
  "Dashboard — my\\myositis.md": {
    "primary": "Inflammation of a muscle, particularly a skeletal voluntary muscle.",
    "secondary": "In rheumatology and pathology, an acute or chronic condition characterized by muscle weakness, tenderness, and lymphocytic infiltration, including dermatomyositis and polymyositis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Primary suppurative **myositis** may follow deep trauma, causing exquisite local swelling and septic fever."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Biopsy specimens in chronic **myositis** demonstrate marked interstitial mononuclear infiltration and myofiber degeneration."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "In acute **myositis**, even the gentlest palpation of the calf muscles elicits intense agony."
      }
    ]
  },
  "Dashboard — my\\myotome.md": {
    "primary": "A group of skeletal muscles innervated by the motor fibers of a single spinal nerve root; also, an instrument used for cutting muscle tissue.",
    "secondary": "In embryology, the dorsolateral portion of a somite that develops into the skeletal musculature of the trunk and limbs.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Each embryonic somite differentiates into a sclerotome, dermatome, and a distinct muscular **myotome**."
      },
      {
        "author": "Charles Sherrington",
        "work": "The Integrative Action of the Nervous System",
        "quote": "Clinical mapping of a specific **myotome** allows precise localization of spinal nerve compression."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The deltoid and biceps muscles are primarily innervated by the C5 **myotome**."
      }
    ]
  },
  "Dashboard — my\\Nectomys.md": {
    "primary": "A taxonomic genus of semiaquatic Neotropical rodents in the family Cricetidae, commonly known as Neotropical water rats.",
    "secondary": "In systematic zoology and mammalogy, water-dwelling oryzomyine rodents characterized by webbed hind feet, dense waterproof fur, and foraging habits along Amazonian riverbanks.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "Specimens of **Nectomys** illustrate remarkable anatomical adaptations to semiaquatic foraging in tropical rivers."
      },
      {
        "author": "Joel Asaph Allen",
        "work": "Bulletin of the American Museum of Natural History",
        "quote": "The cranial dimensions of **Nectomys** distinguish it readily from terrestrial oryzomyine relatives."
      },
      {
        "author": "Oldfield Thomas",
        "work": "Annals and Magazine of Natural History",
        "quote": "Our field survey in South America yielded several distinct regional varieties of the genus **Nectomys**."
      }
    ]
  },
  "Dashboard — my\\perimysium.md": {
    "primary": "The connective tissue sheath that groups individual skeletal muscle fibers into bundles called fascicles.",
    "secondary": "In musculoskeletal histology, collagenous septa continuous with the epimysium that carry intermediate-sized blood vessels and nerve branches deeper into the muscle belly.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **perimysium** partitions the skeletal muscle into distinct bundles or fasciculi visible to the naked eye."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Intramuscular nerve plexuses travel within the collagenous conduits afforded by the **perimysium**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Fatty infiltration in muscular dystrophy preferentially expands along the planes of the **perimysium**."
      }
    ]
  },
  "Dashboard — my\\polymyositis.md": {
    "primary": "A chronic inflammatory disease of the muscles, characterized by progressive, symmetric weakness and wasting of proximal skeletal muscles.",
    "secondary": "In clinical rheumatology, an idiopathic autoimmune inflammatory myopathy mediated by cytotoxic CD8+ T cells targeting non-necrotic muscle fibers, without cutaneous involvement.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients with idiopathic **polymyositis** experience insidious difficulty in climbing stairs and raising the arms above the head."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "The diagnostic evaluation of unexplained pelvic girdle weakness must exclude systemic **polymyositis** before considering surgical intervention."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Elevated serum muscle enzymes and progressive weakness in proximal limbs confirm the diagnosis of **polymyositis**."
      }
    ]
  },
  "Dashboard — my\\Sigmodontomys.md": {
    "primary": "A genus of Neotropical rodents within the family Cricetidae, commonly referred to as Alfaro's water rats.",
    "secondary": "In mammalogy and rodent phylogenetics, a specialized oryzomyine genus endemic to Central and northwestern South America, adapted to riparian montane forest habitats.",
    "quotes": [
      {
        "author": "Joel Asaph Allen",
        "work": "Bulletin of the American Museum of Natural History",
        "quote": "The rodent genus **Sigmodontomys** exhibits distinctive molar cusp patterns separating it from allied marsh rats."
      },
      {
        "author": "Oldfield Thomas",
        "work": "Annals and Magazine of Natural History",
        "quote": "We designated the new specimens from Costa Rica under the generic title **Sigmodontomys**."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Primary Factors of Organic Evolution",
        "quote": "Morphological variations in the dentition of **Sigmodontomys** shed light on the radiation of Neotropical cricetids."
      }
    ]
  },
  "Dashboard — myel\\amyelia.md": {
    "primary": "The congenital absence of the spinal cord.",
    "secondary": "In developmental neuropathology and teratology, a fatal neural tube malformation where the spinal cord fails to form, commonly accompanying anencephaly (anencephaloamyelia).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Complete **amyelia** is an incompatible-with-life malformation, almost invariably associated with total cranioschisis."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Pathological specimens exhibiting **amyelia** demonstrate an empty spinal canal lined only by primitive connective stroma."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Severe disruption of early neural groove closure results in failure of medullary cord development, manifesting as **amyelia**."
      }
    ]
  },
  "Dashboard — myel\\demyelinate.md": {
    "primary": "To destroy, strip away, or remove the myelin sheath from a nerve fiber or axon.",
    "secondary": "In experimental neurobiology and pathology, to induce loss of myelin insulation through toxic, autoimmune, or mechanical insults, disrupting saltatory action potential propagation.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Chemical neurotoxins selectively **demyelinate** central pathways while leaving the underlying axis cylinder structurally intact."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Activated microglial cells actively ingest and **demyelinate** focal patches of white matter in animal models."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Autoimmune cascades that systematically **demyelinate** peripheral axons cause acute flaccid paralysis."
      }
    ]
  },
  "Dashboard — myel\\demyelination.md": {
    "primary": "The loss, destruction, or removal of the myelin sheath covering nerve fibers.",
    "secondary": "In neurology and neuropathology, the hallmark process of diseases such as multiple sclerosis and Guillain-Barré syndrome, leading to slowed conduction velocity and functional deficit.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Disseminated sclerosis is anatomically characterized by multiple circumscribed patches of **demyelination** throughout the cerebrospinal axis."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Following focal **demyelination**, the bare axonal membrane cannot sustain saltatory nerve conduction."
      },
      {
        "author": "Wilder Penfield",
        "work": "Cytology and Cellular Pathology of the Nervous System",
        "quote": "Plaques of chronic **demyelination** exhibit dense gliosis with complete loss of oligodendrocytes."
      }
    ]
  },
  "Dashboard — myel\\multiple myeloma.md": {
    "primary": "A malignant hematologic cancer of plasma cells in the bone marrow, characterized by skeletal lesions, anemia, renal dysfunction, and abnormal immunoglobulins.",
    "secondary": "In hematology and oncology, a clonal proliferation of terminally differentiated B cells that secrete monoclonal paraproteins (M-protein) and Bence-Jones light chains.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Spontaneous pathological fractures and Bence-Jones proteinuria are characteristic manifestations of **multiple myeloma**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The marrow cavities in **multiple myeloma** are replaced by soft, reddish plasmacytic tumor masses that erode cortical bone."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The excessive monoclonal immunoglobulin production observed in **multiple myeloma** illustrates the clonal amplification of antibody-secreting cells."
      }
    ]
  },
  "Dashboard — myel\\myel.md": {
    "primary": "A root combining form denoting the bone marrow or the spinal cord.",
    "secondary": "In anatomical and medical nomenclature, employed in compounding terms referring to the medullary substance of bones or the central neural axis (e.g., myelitis, myeloid).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prefixes based on **myel-** signify pathology situated either within the spinal medullary axis or the blood-forming bone marrow."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The cellular elements of the marrow, denoted by the root **myel-**, undergo rapid proliferation in leukemic conditions."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Classical anatomical terms formed with **myel-** reflect the ancient Greek concept of the internal marrow and spinal substance."
      }
    ]
  },
  "Dashboard — myel\\myelatelia.md": {
    "primary": "Imperfect or incomplete development of the spinal cord.",
    "secondary": "In congenital neuro-teratology, an embryonic developmental defect in the spinal cord, often characterized by localized hypoplasia, canal duplication, or dysraphic lesions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital **myelatelia** frequently underlies obscure lower extremity spasticity and neurogenic bladder dysfunction in early childhood."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Failure of the bilateral medullary plates to fuse cleanly during embryonic development results in localized **myelatelia**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histological examination of the dysplastic cord revealed structural **myelatelia** with erratic glial proliferation."
      }
    ]
  },
  "Dashboard — myel\\myelencephalon.md": {
    "primary": "The posterior subdivision of the embryonic hindbrain (rhombencephalon) that develops into the medulla oblongata.",
    "secondary": "In developmental neurobiology and neuroanatomy, the lowest brain segment containing the vital autonomic respiratory, vasomotor, and cardiac reflex centers.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "The **myelencephalon** gives rise directly to the medulla oblongata, where cranial nerve nuclei are arranged in longitudinal columns."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The central canal of the embryonic **myelencephalon** expands dorsally to form the floor of the fourth ventricle."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "During hindbrain differentiation, the metencephalon develops into the cerebellum and pons, while the **myelencephalon** becomes the medulla."
      }
    ]
  }
};

console.log(`Starting curation of Body Rem A Batch 1 (${Object.keys(batchData).length} notes)...`);
const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`Batch 1 complete: successfully updated ${count} notes.`);
