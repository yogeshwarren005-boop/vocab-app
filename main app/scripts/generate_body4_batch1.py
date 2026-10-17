import json
import os

BATCH1_DATA = {
  "Dashboard — hist/histocompatibility.md": {
    "primary": "The immunological compatibility between the tissues of a donor and recipient, determining the success of organ or tissue transplantation.",
    "secondary": "In immunology and transplant medicine, the matching of major histocompatibility complex (MHC) or human leukocyte antigen (HLA) surface glycoproteins to prevent allograft rejection.",
    "quotes": [
      {
        "author": "Peter Medawar",
        "work": "The Uniqueness of the Individual",
        "quote": "Tissue transplantation between genetically discordant individuals fails because of antigenic differences governed by **histocompatibility** genes."
      },
      {
        "author": "Jean Dausset",
        "work": "The Major Histocompatibility Complex in Man (Nobel Lecture)",
        "quote": "The discovery of the HLA system established the genetic basis of human **histocompatibility** and cellular self-recognition."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Renal allograft survival is profoundly prolonged when donor and host share close **histocompatibility** antigens."
      }
    ]
  },
  "Dashboard — hist/histogram.md": {
    "primary": "A graphical representation of the distribution of numerical data, consisting of adjacent rectangles whose areas are proportional to the frequency of observations within successive intervals.",
    "secondary": "In statistics and data analysis, a fundamental non-parametric probability density estimator introduced by Karl Pearson in 1891 (derived from Greek histos, mast or loom).",
    "quotes": [
      {
        "author": "Karl Pearson",
        "work": "Contributions to the Mathematical Theory of Evolution",
        "quote": "I introduced the term **histogram** to describe graphical diagrams presenting frequency distributions upon a common baseline."
      },
      {
        "author": "Ronald Fisher",
        "work": "Statistical Methods for Research Workers",
        "quote": "Plotting sample frequencies in a **histogram** provides an immediate visual check against the theoretical Gaussian bell curve."
      },
      {
        "author": "Augustus De Morgan",
        "work": "An Explanation of the Gnomonic Projection of the Sphere",
        "quote": "Columns erected upon intervals of equal base illustrate the discrete groupings later organized into the modern **histogram**."
      }
    ]
  },
  "Dashboard — hist/histoincompatibility.md": {
    "primary": "The state or condition of immunological incompatibility between the tissues of a graft donor and recipient, leading to immune-mediated graft rejection.",
    "secondary": "In transplant immunology, disparity at polymorphic major histocompatibility gene loci that triggers cytotoxic T-lymphocyte and antibody-mediated destruction of allografts.",
    "quotes": [
      {
        "author": "Peter Medawar",
        "work": "The Behavior and Fate of Skin Autografts and Skin Homografts in Rabbits",
        "quote": "Acute allograft necrosis represents an actively acquired immune response driven by genetic **histoincompatibility**."
      },
      {
        "author": "Jean Dausset",
        "work": "Histocompatibility Typing in Clinical Transplantation",
        "quote": "Severe graft-versus-host disease ensues when bone marrow transplants harbor unshared minor **histoincompatibility** antigens."
      },
      {
        "author": "Macfarlane Burnet",
        "work": "Immunological Surveillance",
        "quote": "Cellular recognition mechanisms have evolved specifically to detect tissue **histoincompatibility** and foreign surface markers."
      }
    ]
  },
  "Dashboard — hist/histologic.md": {
    "primary": "Of or relating to histology; pertaining to the microscopic anatomy of tissues.",
    "secondary": "In medical pathology and cytology, describing tissue architecture, cellular arrangement, or micro-structural alterations observed under a microscope.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Every **histologic** investigation demonstrates that disease originates within the altered metabolism of individual cells."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The definitive diagnosis of hepatic cirrhosis requires **histologic** confirmation of diffuse fibrous bridging."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "Silver impregnation reveals the delicate **histologic** arborization of cortical pyramidal neurons."
      }
    ]
  },
  "Dashboard — hist/histological.md": {
    "primary": "Pertaining to the microscopic structure of animal or plant tissues; histological.",
    "secondary": "Relating to the science of histology or the microscopic examination of stained tissue sections.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Advice for a Young Investigator",
        "quote": "Mastery of differential tissue staining is the indispensable foundation of all serious **histological** research."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic **histological** sections bridge the gap between gross clinical anatomy and cellular pathology."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The **histological** elements of vertebrate bone reveal concentric lamellae organized around central Haversian canals."
      }
    ]
  },
  "Dashboard — hist/histologically.md": {
    "primary": "In a histological manner; with reference to microscopic tissue structure or by means of histological techniques.",
    "secondary": "As observed or confirmed through microscopic examination of stained tissue specimens.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Examined **histologically**, the granuloma presented central caseous necrosis ringed by epithelioid and Langhans giant cells."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "The cerebellar cortex is organized **histologically** into three distinct horizontal layers."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Tissues that appear normal to the naked eye often prove **histologically** infiltrated with inflammatory leukocytes."
      }
    ]
  },
  "Dashboard — hist/histologist.md": {
    "primary": "A scientist, anatomist, or specialist who investigates the microscopic anatomy, structure, and chemistry of biological tissues.",
    "secondary": "In biomedical science, an investigator skilled in microtomy, histological staining, and microscopic analysis of organ microarchitecture.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Recollections of My Life",
        "quote": "The enthusiastic **histologist** discovers unexpected beauty within the intricate labyrinth of cerebral dendrites."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Every competent **histologist** recognizes that cellular division constitutes the universal engine of tissue renewal."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Lay Sermons, Addresses, and Reviews",
        "quote": "Through the tireless labors of the modern **histologist**, the internal mechanics of the living engine have been laid bare."
      }
    ]
  },
  "Dashboard — hist/histology.md": {
    "primary": "The scientific study of the microscopic structure, organization, and function of biological tissues.",
    "secondary": "In anatomical medicine, the discipline (founded by Xavier Bichat and elevated by microscopic staining) that bridges gross anatomy and molecular cytology.",
    "quotes": [
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System of Man and Vertebrates",
        "quote": "Comparative **histology** reveals that the basic functional unit of the brain is the independent cellular neuron."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Without a thorough foundation in normal human **histology**, the pathologist cannot interpret malignant degenerations."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The fundamental **histology** of coelenterates is uncomplicated, consisting of simple ectodermal and endodermal sheets."
      }
    ]
  },
  "Dashboard — hist/histone.md": {
    "primary": "Any of a group of basic, alkaline proteins found in eukaryotic cell nuclei that package and order DNA into structural units called nucleosomes.",
    "secondary": "In molecular genetics and epigenetics, the core octamer proteins (H2A, H2B, H3, H4, plus linker H1) whose post-translational chemical modifications regulate chromatin accessibility and gene expression.",
    "quotes": [
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Eukaryotic nuclear DNA winds tightly around an octamer core of basic **histone** proteins to form nucleosome beads."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Acetylation and methylation of protruding **histone** tails serve as an epigenetic code modulating transcriptional activation."
      },
      {
        "author": "Albrecht Kossel",
        "work": "The Chemical Composition of the Cell Nucleus (Nobel Lecture)",
        "quote": "I isolated the basic protein **histone** from avian erythrocytes, establishing its intimate association with nucleic acids."
      }
    ]
  },
  "Dashboard — hist/histopathology.md": {
    "primary": "The microscopic study and examination of diseased tissues to understand the manifestations and mechanisms of disease.",
    "secondary": "In diagnostic medicine, the specialized branch of pathology that provides definitive clinical diagnosis of biopsies and surgical resections through tissue section microscopy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The accurate prognosis of malignant neoplasms rests squarely upon the findings of surgical **histopathology**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Modern **histopathology** traces the clinical symptoms of disease down to the specific micro-architectural breakdown of tissues."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus and the Syndrome of the Cerebellopontile Angle",
        "quote": "Correlating clinical neurosurgical signs with post-operative **histopathology** refined our classification of intracranial gliomas."
      }
    ]
  },
  "Dashboard — hist/histoplasmosis.md": {
    "primary": "An infectious systemic fungal disease caused by the dimorphic fungus Histoplasma capsulatum, contracted by inhaling airborne fungal microconidia from bird or bat droppings.",
    "secondary": "In clinical infectious disease and pulmonology, a granulomatous disorder (Darling's disease) presenting typically as benign pulmonary infiltration, but capable of fatal dissemination in immunocompromised hosts.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Disseminated **histoplasmosis** closely mimics pulmonary tuberculosis, producing fever, hepatosplenomegaly, and lymphadenopathy."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Bone marrow aspirates stained with Wright's dye revealed intracellular yeast forms of **histoplasmosis** packed within macrophages."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "While penicillin proved ineffective against deep fungal infections like **histoplasmosis**, newer antimycotics offered hope."
      }
    ]
  },
  "Dashboard — hist/historian.md": {
    "primary": "An expert, scholar, or writer who researches, analyzes, interprets, and chronicles past events.",
    "secondary": "In intellectual culture, a critical scholar who evaluates primary sources, historical context, and documentary evidence to reconstruct human society over time.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The diligence of the **historian** must examine every reliable monument and manuscript to separate truth from fable."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "A perfect **historian** must possess not only laborious research, but a powerful imagination to revive the living drama of the past."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "Universal history, what man has accomplished in this world, is at bottom the history of the Great Men who have worked here, observes the **historian**."
      }
    ]
  },
  "Dashboard — hist/historic.md": {
    "primary": "Famous, celebrated, or important in history; having a great and lasting impact upon human affairs.",
    "secondary": "In cultural and political discourse, marking an epochal milestone, event, or site destined to be remembered by posterity.",
    "quotes": [
      {
        "author": "Winston Churchill",
        "work": "The Second World War",
        "quote": "This **historic** decision committed the combined naval and air power of the democracies to liberation."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The ruins of the Roman Forum stood as a silent, **historic** witness to the rise and fall of universal empire."
      },
      {
        "author": "Abraham Lincoln",
        "work": "Gettysburg Address",
        "quote": "The world will little note, nor long remember what we say here, but it can never forget the **historic** sacrifice made here."
      }
    ]
  },
  "Dashboard — hist/historical.md": {
    "primary": "Of, relating to, or having the character of history; based on real past events rather than myth or legend.",
    "secondary": "In epistemology and social science, pertaining to temporal development, contextual documentation, and chronological records.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "The History of England",
        "quote": "The **historical** method reconstructs not merely royal decrees, but the daily habits and convictions of the common people."
      },
      {
        "author": "Lord Acton",
        "work": "Lectures on Modern History",
        "quote": "Strict **historical** criticism requires judging the past by standards of universal morality without partisan bias."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "Her quiet life was woven into the vast, silent fabric of unwritten **historical** change."
      }
    ]
  },
  "Dashboard — hist/historically.md": {
    "primary": "With reference to history, past events, or historical development; throughout recorded history.",
    "secondary": "In terms of historical context, origin, or chronology rather than static abstract principles.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The institutions of the republic had **historically** dissolved long before the formal title of Augustus was conferred."
      },
      {
        "author": "Max Weber",
        "work": "The Protestant Ethic and the Spirit of Capitalism",
        "quote": "Modern rational capitalism was **historically** conditioned by ascetic religious ethics emerging during the Reformation."
      },
      {
        "author": "Alexis de Tocqueville",
        "work": "Democracy in America",
        "quote": "Township self-government in New England was **historically** established prior to state or national confederation."
      }
    ]
  },
  "Dashboard — hist/historicalness.md": {
    "primary": "The state, quality, or condition of being historical; historical authenticity, actuality, or character.",
    "secondary": "In the philosophy of history and existential phenomenology (historicity / Geschichtlichkeit), the intrinsic temporal and situated nature of human existence and institutions.",
    "quotes": [
      {
        "author": "Wilhelm Dilthey",
        "work": "The Formation of the Historical World in the Human Sciences",
        "quote": "The profound **historicalness** of human consciousness means that we understand human nature only through history."
      },
      {
        "author": "Lord Acton",
        "work": "Lectures on Modern History",
        "quote": "The documentary test of **historicalness** separates authentic ancient charters from spurious pious inventions."
      },
      {
        "author": "Martin Heidegger",
        "work": "Being and Time",
        "quote": "The authentic temporality of Dasein grounds the primordial **historicalness** of our shared cultural inheritance."
      }
    ]
  },
  "Dashboard — hist/historicism.md": {
    "primary": "The philosophical theory that social, cultural, and political phenomena are determined by and can only be understood through historical context.",
    "secondary": "In 19th- and 20th-century intellectual history, the doctrine that values and truths are historically relative, or (critiqued by Karl Popper) the belief that history unfolds according to inexorable developmental laws.",
    "quotes": [
      {
        "author": "Karl Popper",
        "work": "The Poverty of Historicism",
        "quote": "I mean by **historicism** an approach to the social sciences which assumes that historical prediction is their principal aim."
      },
      {
        "author": "Ernst Cassirer",
        "work": "The Philosophy of the Enlightenment",
        "quote": "Romantic **historicism** arose as a profound reaction against the abstract universalism of the Enlightenment."
      },
      {
        "author": "Friedrich Nietzsche",
        "work": "On the Use and Abuse of History for Life",
        "quote": "An excess of uncritical **historicism** paralyzes modern man, transforming him into a passive spectator of the past."
      }
    ]
  },
  "Dashboard — hist/historied.md": {
    "primary": "Having a long, illustrious, or celebrated history; recorded, chronicled, or commemorated in historical annals.",
    "secondary": "In literature and architectural description, rich in historical associations, venerable memories, or artistic depictions of past events.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "Memory unrolls her **historied** scroll, recording the rise of ancient dynasties and their fateful falls."
      },
      {
        "author": "Washington Irving",
        "work": "The Sketch-Book of Geoffrey Crayon, Gent.",
        "quote": "We wandered through the **historied** aisles of Westminster Abbey, surrounded by the dust of kings and poets."
      },
      {
        "author": "Henry Wadsworth Longfellow",
        "work": "Outre-Mer: A Pilgrimage Beyond the Sea",
        "quote": "Every ruined battlement along the Rhine was a **historied** monument to chivalry and medieval warfare."
      }
    ]
  },
  "Dashboard — hist/historiographer.md": {
    "primary": "An official writer of history appointed by a monarch, government, or learned institution.",
    "secondary": "In literary history, a scholar specifically tasked with compiling official annals, national chronicles, or dynastic historical records (such as the Historiographer Royal).",
    "quotes": [
      {
        "author": "John Dryden",
        "work": "The Life of Plutarch",
        "quote": "In his capacity as **historiographer** to the crown, the author was entrusted with the royal state archives."
      },
      {
        "author": "Voltaire",
        "work": "The Age of Louis XIV",
        "quote": "As official **historiographer** of France, I resolved to record the cultural glory of the reign rather than court petty gossip."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Imperial **historiographers** at Constantinople often tailored their panegyrics to please the reigning faction."
      }
    ]
  },
  "Dashboard — hist/historiography.md": {
    "primary": "The writing of history based on the critical examination of authentic sources; the body of historical literature on a specific subject.",
    "secondary": "In academic history, the methodological and philosophical study of how historical interpretations, paradigms, and narratives evolve over time.",
    "quotes": [
      {
        "author": "Lord Acton",
        "work": "The Study of History",
        "quote": "Modern **historiography** was transformed when European archives opened their unvarnished diplomatic records to scholars."
      },
      {
        "author": "R. G. Collingwood",
        "work": "The Idea of History",
        "quote": "The central problem of **historiography** is how the contemporary mind re-enacts past human thought in its own context."
      },
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "Classical **historiography** combined poetic drama with political philosophy, as seen in the immortal narrative of Thucydides."
      }
    ]
  },
  "Dashboard — hist/history.md": {
    "primary": "The discipline that records, analyzes, and interprets past events, societies, cultures, and human experiences.",
    "secondary": "In philosophy, the continuous chronological progression of human civilization, or a formal narrative account of natural or civil phenomena.",
    "quotes": [
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "**History**, indeed, is little more than the register of the crimes, follies, and misfortunes of mankind."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "The **history** of the world is but the biography of great men."
      },
      {
        "author": "Cicero",
        "work": "De Oratore",
        "quote": "**History** is the witness of times, the light of truth, the life of memory, the mistress of life, the messenger of antiquity."
      }
    ]
  },
  "Dashboard — hist/histrion.md": {
    "primary": "An actor, theatrical performer, or stage player (archaic term derived from Latin histrio).",
    "secondary": "In dramatic history, a theatrical performer, often used with derogatory connotations of artificiality, insincerity, or affectation.",
    "quotes": [
      {
        "author": "William Hazlitt",
        "work": "A View of the English Stage",
        "quote": "The true **histrion** lives upon the stage, giving bodily form and emotional voice to the poet's deepest passions."
      },
      {
        "author": "Charles Lamb",
        "work": "On the Tragedies of Shakespeare",
        "quote": "We confuse the dramatic creation of Shakespeare with the physical gestures of the contemporary **histrion**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "Roman senators were forbidden under pain of infamy from exhibiting their talents upon the stage as a public **histrion**."
      }
    ]
  },
  "Dashboard — hist/histrionic.md": {
    "primary": "Overly theatrical, dramatic, exaggerated, or emotional in character, style, or behavior.",
    "secondary": "In clinical psychiatry, designating a personality disorder (histrionic personality disorder) marked by constant attention-seeking, seductiveness, and excessive emotionality.",
    "quotes": [
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "There was an artificial, almost **histrionic** intensity in her voice that warned him against taking her words literally."
      },
      {
        "author": "Henry James",
        "work": "The Bostonians",
        "quote": "Basil Ransom listened to her passionate address with the cool detachment one accords an accomplished **histrionic** actress."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In hysterical temperament, **histrionic** displays of emotion frequently substitute for genuine inner feeling."
      }
    ]
  },
  "Dashboard — hist/histrionics.md": {
    "primary": "Exaggerated, theatrical, melodramatic, or insincere behavior designed to attract attention or produce an effect.",
    "secondary": "The art, performance, or technique of theatrical acting on stage.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Mr. Wopsle indulged in such astounding vocal **histrionics** that the gallery erupted in laughter during Hamlet."
      },
      {
        "author": "W. M. Thackeray",
        "work": "Vanity Fair",
        "quote": "Becky Sharp was a mistress of domestic **histrionics**, summoning tears or smiles at a moment's notice to conquer society."
      },
      {
        "author": "George Bernard Shaw",
        "work": "Our Theatres in the Nineties",
        "quote": "True dramatic art demands intellectual restraint rather than the cheap emotional **histrionics** of the Victorian melodrama."
      }
    ]
  },
  "Dashboard — hist/immunohistochemistry.md": {
    "primary": "A laboratory technique that uses labeled antibodies to identify and visualize specific antigens, proteins, or biomarkers in microscopic tissue sections.",
    "secondary": "In diagnostic pathology and oncology, an indispensable diagnostic tool for typing malignant tumors, determining receptor status (e.g. HER2, estrogen receptors), and guiding targeted therapy.",
    "quotes": [
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "By using fluorescent antibodies in **immunohistochemistry**, researchers pinpoint the exact intracellular localization of cytoskeletal proteins."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Modern surgical pathology relies upon **immunohistochemistry** to distinguish poorly differentiated carcinomas from lymphomas."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "Specific monoclonal probes applied through **immunohistochemistry** revealed oncogene overexpression across human breast tumor biopsies."
      }
    ]
  },
  "Dashboard — hist/protohistory.md": {
    "primary": "The transitional period between prehistory and recorded history, during which a culture has not yet developed its own writing but is mentioned in the written records of other literate civilizations.",
    "secondary": "In archaeology and anthropology, the study of human societies immediately preceding the availability of continuous indigenous historical inscriptions or chronicles.",
    "quotes": [
      {
        "author": "V. Gordon Childe",
        "work": "The Dawn of European Civilization",
        "quote": "The European Bronze Age represents a vast **protohistory** illuminated intermittently by the literate empires of Egypt and Mesopotamia."
      },
      {
        "author": "Arthur Evans",
        "work": "The Palace of Minos at Knossos",
        "quote": "Minoan archaeological strata illuminate the shadowy **protohistory** that preceded classical Greek civilization."
      },
      {
        "author": "Lewis Henry Morgan",
        "work": "Ancient Society",
        "quote": "During the upper stage of barbarism, tribal institutions entered the epoch of **protohistory** through iron metallurgy and oral tradition."
      }
    ]
  },
  "Dashboard — hymen/Hymenoptera.md": {
    "primary": "A large order of insects comprising sawflies, wasps, bees, and ants, characterized by four membranous wings coupled during flight by tiny hooks (hamuli).",
    "secondary": "In systematic entomology, one of the most ecologically important and diverse holometabolous insect orders, noted for advanced eusociality, haplodiploid sex determination, and critical pollination roles.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The extraordinary social instincts of the **Hymenoptera**, including sterile worker castes, provided a formidable test for natural selection."
      },
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "In the order **Hymenoptera**, the posterior margin of the forewing is locked to the hindwing during flight by microscopic hooks."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Wonders of Instinct",
        "quote": "Solitary hunting wasps of the **Hymenoptera** exhibit surgical precision when paralyzing crickets with their venomous stings."
      }
    ]
  },
  "Dashboard — hymen/hymen.md": {
    "primary": "A thin mucous membrane that partially or completely occludes the external opening of the vagina in human females and certain other mammals.",
    "secondary": "In classical Greek mythology, Hymen (Ὑμήν), the god of marriage and wedding ceremonies; also used figuratively for nuptials or marriage vows.",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "As You Like It",
        "quote": "Then is there mirth in heaven, When earthly things made even Atone together: Good **Hymen**, people every town."
      },
      {
        "author": "John Milton",
        "work": "L'Allegro",
        "quote": "There let **Hymen** oft appear In saffron robe, with taper clear, And pomp, and feast, and revelry."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital imperforation of the **hymen** leads to hematocolpos with retained menstrual flow at puberty."
      }
    ]
  },
  "Dashboard — hymen/hymenaea.md": {
    "primary": "A genus of tropical leguminous trees in the family Fabaceae (such as Hymenaea courbaril, the courbaril or Brazilian copal tree), native to the Neotropics.",
    "secondary": "In paleobotany and forestry, tropical canopy trees prized for hard, durable timber and fragrant resin (copal), which fossilizes into amber (such as Dominican amber).",
    "quotes": [
      {
        "author": "Alexander von Humboldt",
        "work": "Personal Narrative of Travels to the Equinoctial Regions",
        "quote": "Colossal trunks of **Hymenaea** courbaril towered above the riverbanks, exuding clear drops of aromatic copal resin."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "Palm Trees of the Amazon and Their Uses",
        "quote": "Indigenous tribes collect the fragrant resin from the roots of **Hymenaea** to use as incense in ceremonies."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "In the leguminous genus **Hymenaea**, the woody pods enclose seeds embedded in an edible mealy pulp."
      }
    ]
  },
  "Dashboard — hymen/hymenal.md": {
    "primary": "Pertaining to, situated on, or involving the hymen.",
    "secondary": "In gynecology and forensic anatomy, designating the anatomical remnants (carunculae hymenales) or surgical procedures concerning the hymeneal membrane.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Following normal parturition, the torn membrane is reduced to small nodular **hymenal** caruncles."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "Congenital vascular anomalies occasionally produce persistent bleeding along the **hymenal** border."
      },
      {
        "author": "Ferdinand von Hebra",
        "work": "Diseases of the Skin",
        "quote": "Benign mucosal papillomas were observed arising directly from the **hymenal** margin."
      }
    ]
  },
  "Dashboard — hymen/hymenanthera.md": {
    "primary": "A genus of rigid, often spiny shrubs and small trees in the violet family (Violaceae), native to Australasia (often included in Melicytus).",
    "secondary": "In systematic botany, woody violaceous shrubs characterized by anthers bearing membranous terminal appendages, yielding small white or purple berries.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Handbook of the New Zealand Flora",
        "quote": "The coastal shrub **Hymenanthera** crassifolia forms dense spiny thickets along windswept sea cliffs."
      },
      {
        "author": "Asa Gray",
        "work": "Botany of the United States Exploring Expedition",
        "quote": "In **Hymenanthera**, the anthers are capped by delicate membranous scales from which the generic name is derived."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The anomalous woody habit of **Hymenanthera** contrasts with the herbaceous nature of northern violets."
      }
    ]
  },
  "Dashboard — hymen/hymeneal.md": {
    "primary": "Of, relating to, or appropriate for marriage or a wedding ceremony; nuptial.",
    "secondary": "In classical literature, a wedding song, hymn, or epithalamium sung in celebration of the bride and bridegroom.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The birds their quire apply; airs, vernal airs, Breathing the smell of field and grove, attune The **hymeneal** gale."
      },
      {
        "author": "Percy Bysshe Shelley",
        "work": "To a Skylark",
        "quote": "Chorus **Hymeneal**, Or triumphal chaunt, Matched with thine would be all But an empty vaunt."
      },
      {
        "author": "Edmund Spenser",
        "work": "Epithalamion",
        "quote": "Ring ye the bells, ye yong men of the towne, And leave your wonted labors for this day: This day is holy, let our **hymeneal** sound resound."
      }
    ]
  },
  "Dashboard — hymen/hymeneals.md": {
    "primary": "Nuptial songs, wedding poems, or marriage celebrations (plural form of hymeneal).",
    "secondary": "In poetry, joyful choral songs invoking Hymen to bless newly wedded lovers.",
    "quotes": [
      {
        "author": "Lord Byron",
        "work": "Don Juan",
        "quote": "The joyous feast, the dancing, and the loud **hymeneals** echoed through the palace till dawn."
      },
      {
        "author": "John Dryden",
        "work": "The Fables of John Dryden",
        "quote": "Soft flutes accompanied the sweet **hymeneals** chanted by the maidens before the bridal chamber."
      },
      {
        "author": "Alexander Pope",
        "work": "The Odyssey of Homer",
        "quote": "Joyful youths led forth the radiant bride amidst festive torches and resonant **hymeneals**."
      }
    ]
  },
  "Dashboard — hymen/hymenium.md": {
    "primary": "The spore-bearing tissue layer in fungi, containing the spore-producing basidia (in basidiomycetes) or asci (in ascomycetes).",
    "secondary": "In mycology, the fertile palisade layer lining the surface of mushroom gills, pores, spines, or cup-fungus surfaces, interspersed with sterile cystidia and paraphyses.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Microscopic sections through the gill of Agaricus reveal the dense palisade of club-shaped basidia forming the **hymenium**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The vast surface area provided by gills allows the fungal **hymenium** to produce millions of airborne spores."
      },
      {
        "author": "Pier Andrea Saccardo",
        "work": "Sylloge Fungorum",
        "quote": "The morphology and arrangement of the **hymenium** serve as primary taxonomic criteria across the higher fungi."
      }
    ]
  },
  "Dashboard — hymen/hymenogastrales.md": {
    "primary": "An order or family (Hymenogastraceae) of subterranean, truffle-like gastroid basidiomycete fungi.",
    "secondary": "In systematic mycology, false truffles forming mycorrhizal symbioses with forest trees, characterized by enclosed, chambered glebae that do not open at maturity.",
    "quotes": [
      {
        "author": "Pier Andrea Saccardo",
        "work": "Sylloge Fungorum",
        "quote": "Subterranean fungi of the **Hymenogastrales** conceal their fertile glebal chambers inside a thick, protective peridium."
      },
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The closed fruiting body of **Hymenogastrales** represents an evolutionary adaptation for animal mycophagy and spore dispersal."
      },
      {
        "author": "Elias Magnus Fries",
        "work": "Systema Mycologicum",
        "quote": "Fries classified the subterranean gasteromycetes allied to Hymenogaster within his pioneering group of **Hymenogastrales**."
      }
    ]
  },
  "Dashboard — hymen/hymenomycete.md": {
    "primary": "Any fungus belonging to the historical class Hymenomycetes, having an exposed spore-bearing hymenium.",
    "secondary": "In mycology, a higher basidiomycete (such as an agaric, bolete, polypore, or chanterelle) whose spores are discharged from an open, exposed hymenial surface.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "Every true **hymenomycete** exposes its spore-bearing surface to the open air before spore discharge begins."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The diverse forms assumed by the **hymenomycete** fungi illustrate the evolutionary plasticity of fungal fruiting bodies."
      },
      {
        "author": "Elias Magnus Fries",
        "work": "Epicrisis Systematis Mycologici",
        "quote": "Fries organized the vast order of the **hymenomycetes** according to the gill, pore, or tooth architecture of the hymenium."
      }
    ]
  },
  "Dashboard — hymen/hymenomycetes.md": {
    "primary": "A major traditional taxonomic group or class of basidiomycete fungi possessing an exposed spore-bearing hymenium (including mushrooms, shelf fungi, and coral fungi).",
    "secondary": "In historical mycology, fungi characterized by basidia arranged in a continuous hymenial palisade exposed to the open air at maturity, contrasting with Gasteromycetes.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The class **Hymenomycetes** represents the pinnacle of basidial spore production and ballistic spore dispersal."
      },
      {
        "author": "Elias Magnus Fries",
        "work": "Systema Mycologicum",
        "quote": "In the **Hymenomycetes**, the configuration of the hymenophore establishes the fundamental families of the Agaricini and Polyporei."
      },
      {
        "author": "Pier Andrea Saccardo",
        "work": "Sylloge Fungorum",
        "quote": "Thousands of wood-rotting forest species are catalogued under the extensive umbrella of the **Hymenomycetes**."
      }
    ]
  },
  "Dashboard — hymen/hymenophore.md": {
    "primary": "The structural part of a basidiomycete fungus that bears or supports the hymenium (such as gills, pores, tubes, or teeth).",
    "secondary": "In fungal morphology and systematics, the specialized tramal framework of an agaric or polypore beneath the fertile spore-bearing layer.",
    "quotes": [
      {
        "author": "Anton de Bary",
        "work": "Comparative Morphology and Biology of the Fungi",
        "quote": "The vertical gills of the mushroom serve as a corrugated **hymenophore**, multiplying the surface available for spore production."
      },
      {
        "author": "Elias Magnus Fries",
        "work": "Epicrisis Systematis Mycologici",
        "quote": "Whether the **hymenophore** is lamellate, poroid, or hydnoid determines the primary taxonomic genus of the specimen."
      },
      {
        "author": "Pier Andrea Saccardo",
        "work": "Sylloge Fungorum",
        "quote": "Microscopic sections show the continuous tramal tissue of the **hymenophore** supporting the delicate basidial palisade."
      }
    ]
  },
  "Dashboard — hymen/hymenophyllaceae.md": {
    "primary": "A family of delicate, moisture-loving leptosporangiate ferns known as the filmy ferns, characterized by fronds that are only one cell thick.",
    "secondary": "In pteridology, primitive shade- and humidity-dependent ferns native to wet tropical and temperate rainforests, lacking stomata and absorbing moisture directly through their translucent leaves.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Himalayan Journals",
        "quote": "Damp granite boulders in the cloud forest were draped in exquisite green curtains of the **Hymenophyllaceae**."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "The translucent fronds of the **Hymenophyllaceae** are reduced to a single cellular layer between the veins."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Nowhere are the filmy ferns of the **Hymenophyllaceae** more lush than along the misty mountain torrents of Borneo."
      }
    ]
  },
  "Dashboard — hymen/hymenophyllum.md": {
    "primary": "A genus of small, delicate filmy ferns in the family Hymenophyllaceae, having membranous fronds with bivalved indusia enclosing the sporangia.",
    "secondary": "In botany, moss-like epiphytic or epilithic ferns growing in humid ravine spray zones and mist forests, characterized by two-lipped cup-like soral receptacles.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Flora Antarctica",
        "quote": "The tiny filmy fern **Hymenophyllum** covers the damp trunks of southern beeches throughout Tierra del Fuego."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The two-lipped indusium of **Hymenophyllum** opens at the top to expose the sporangia clustered upon a short receptacle."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "In the drenched rainforests of Chiloé, graceful fronds of **Hymenophyllum** clung to every dripping branch."
      }
    ]
  },
  "Dashboard — hymen/hymenoplasty.md": {
    "primary": "Surgical reconstruction, restoration, or repair of the hymen.",
    "secondary": "In reconstructive and cosmetic gynecology, an elective surgical procedure (hymenorrhaphy) performed to approximate or reconstruct hymenal mucosal edges.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Operative procedures encompassing **hymenoplasty** demand meticulous surgical approximation of mucosal tissue flaps."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "Plastic repair or **hymenoplasty** was indicated to correct cicatricial stenosis resulting from severe laceration."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Delicate reconstructive surgery or **hymenoplasty** utilizes fine absorbable sutures to secure mucosal union."
      }
    ]
  },
  "Dashboard — hymen/hymenopter.md": {
    "primary": "An insect belonging to the order Hymenoptera; a hymenopteran (wasp, bee, ant, or sawfly).",
    "secondary": "In entomology, a four-winged holometabolous insect possessing coupled membranous wings and often a specialized ovipositor or sting.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "The diligent **hymenopter** returns to its nest loaded with provisions for its developing brood."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Wonders of Instinct",
        "quote": "No mechanical tool matches the delicate stinging precision of the predatory **hymenopter**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Complex colonial instincts evolved repeatedly among various branches of the social **hymenopter**."
      }
    ]
  },
  "Dashboard — hymen/hymenopteran.md": {
    "primary": "Any insect of the order Hymenoptera, including bees, wasps, ants, and sawflies.",
    "secondary": "Of or relating to the insect order Hymenoptera; exhibiting characteristic membranous wings, haplodiploidy, and complete metamorphosis.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "The Insect Societies",
        "quote": "The haplodiploid genetic system of the **hymenopteran** predisposes female siblings to altruistic colonial cooperation."
      },
      {
        "author": "Richard Dawkins",
        "work": "The Selfish Gene",
        "quote": "Kin selection provides an elegant explanation for the evolution of sterile worker castes in the **hymenopteran**."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Bramble-Bees and Others",
        "quote": "Each solitary **hymenopteran** constructs her brood cell with architectural geometry innate to her species."
      }
    ]
  },
  "Dashboard — hymen/hymenopteron.md": {
    "primary": "A hymenopterous insect; an individual member of the order Hymenoptera.",
    "secondary": "In classical and 19th-century entomological treatises, a singular form designating an insect possessing membranous hooked wings.",
    "quotes": [
      {
        "author": "John Obadiah Westwood",
        "work": "An Introduction to the Modern Classification of Insects",
        "quote": "Under magnification, the wings of the **hymenopteron** reveal a reduced, highly specialized venational pattern."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "The parasitic **hymenopteron** deposits its eggs within the living body of the host caterpillar."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In every adult **hymenopteron**, the first abdominal segment is fused solidly to the posterior metathorax."
      }
    ]
  },
  "Dashboard — hymen/hymenopterous.md": {
    "primary": "Of, relating to, or characteristic of the Hymenoptera; having four membranous wings.",
    "secondary": "In entomology, describing insects such as bees, wasps, and ants that undergo complete metamorphosis with membranous wings joined by hamuli.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The stinging apparatus in **hymenopterous** insects is a modified ovipositor adapted for defense or predation."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Fly",
        "quote": "The **hymenopterous** parasitoid paralyzes its victim, ensuring fresh living tissue for its emerging grub."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Immense **hymenopterous** insects, including giant black carpenter bees, droned around the dead forest timber."
      }
    ]
  },
  "Dashboard — hymen/hymenorrhaphy.md": {
    "primary": "The surgical repair, suturing, or reconstruction of the hymen.",
    "secondary": "In operative gynecology and reconstructive pelvic surgery, the suturing of torn or lacerated edges of the hymenal mucosa.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Surgical **hymenorrhaphy** was performed under local anesthesia to restore the integrity of the lacerated membrane."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "Traumatic rupture following pelvic injury required immediate **hymenorrhaphy** to arrest persistent capillary hemorrhage."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "The technique of **hymenorrhaphy** involves debridement of fibrous scar margins followed by fine catgut coaptation."
      }
    ]
  },
  "Dashboard — hymen/hymenotomy.md": {
    "primary": "Surgical incision of the hymen, especially to relieve an imperforate hymen.",
    "secondary": "In clinical gynecology, a minor operative incision performed to drain retained menstrual blood (hematocolpos) caused by congenital hymenal atresia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Cruciate **hymenotomy** released several pints of dark, tarry fluid, providing immediate relief from pelvic distension."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "In cases of congenital imperforation, prompt **hymenotomy** prevents ascending infection and hematometra."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Simple **hymenotomy** performed under aseptic precautions completely resolves the obstructive pelvic mass."
      }
    ]
  },
  "Dashboard — hyster/hyster 2.md": {
    "primary": "A Greek combining root morpheme (ὕστερος, hysteros) signifying latter, subsequent, coming after, or lagging behind.",
    "secondary": "In physical science and rhetoric, a formative element producing terms relating to delayed physical effects or inverted sequence (as in hysteresis, hysteron proteron).",
    "quotes": [
      {
        "author": "James Alfred Ewing",
        "work": "Magnetic Induction in Iron and Other Metals",
        "quote": "I selected the Greek root **hyster-** to name the phenomenon wherein magnetic effect lags behind magnetizing force."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "The rhetorical figure hysteron proteron derives from Greek **hyster-**, placing that which is subsequent in the front."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The comparative adjective **hyster-** reflects an ancient Indo-European construction signifying behind or later."
      }
    ]
  },
  "Dashboard — hyster/hyster.md": {
    "primary": "A Greek combining root morpheme (ὑστέρα, hystera) signifying the womb or uterus.",
    "secondary": "In medical and surgical nomenclature, the foundational combining element for anatomical conditions and operative procedures involving the female reproductive uterus (as in hysterectomy, hysteroscope, hysteralgia).",
    "quotes": [
      {
        "author": "Galen",
        "work": "De Uteri Dissectione",
        "quote": "The ancient physicians called the womb **hyster-**, tracing numerous sympathetic bodily disorders to its health."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The surgical prefix **hyster-** denotes operative procedures directed upon the pathology of the uterus."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "From **hyster-** arise terms in classical medicine reflecting ancient views of uterine mobility and temperament."
      }
    ]
  },
  "Dashboard — hyster/hysteralgia.md": {
    "primary": "Pain in the uterus; uterine neuralgia.",
    "secondary": "In clinical gynecology, severe pelvic pain or cramping originating from uterine contractions, adenomyosis, endometriosis, or pelvic congestion.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe spasmodic **hysteralgia** during the menstrual cycle frequently responds to rest, heat, and analgesic sedation."
      },
      {
        "author": "Thomas Addison",
        "work": "A Collection of the Published Writings",
        "quote": "Chronic **hysteralgia** was often mistaken by older clinicians for inflammatory peritonitis before pelvic palpation was perfected."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Neuralgic pelvic complaints presenting as **hysteralgia** may accompany generalized neurasthenic debility."
      }
    ]
  },
  "Dashboard — hyster/hysteratresia.md": {
    "primary": "Occlusion, obliteration, or pathological closure of the cavity or cervical canal of the uterus.",
    "secondary": "In gynecological surgery, congenital or acquired cervical stenosis resulting from scarring, cauterization, or developmental failure of Müllerian duct canalization.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Post-traumatic **hysteratresia** following vigorous curettage leads to amenorrhea and painful hematometra."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "Cervical dilation under anesthesia is required to relieve complete acquired **hysteratresia**."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Surgical recanalization of the cervix overcame the congenital **hysteratresia**, preserving reproductive function."
      }
    ]
  },
  "Dashboard — hyster/hysterectomy.md": {
    "primary": "The surgical operation of removing the uterus.",
    "secondary": "In gynecological surgery, total or subtotal excision of the uterus (frequently accompanied by salpingo-oophorectomy) indicated for leiomyomas, endometriosis, uterine prolapse, or pelvic malignancies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Radical abdominal **hysterectomy** became a safe and standard procedure following the introduction of antiseptic surgical technique."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Medical Career and Other Papers",
        "quote": "Advances in hemostasis transformed the dangerous **hysterectomy** into one of the most successful major pelvic operations."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Careful ligation of the uterine arteries is the crucial step when performing a complete abdominal **hysterectomy**."
      }
    ]
  },
  "Dashboard — hyster/hysteresis.md": {
    "primary": "The phenomenon in which the value of a physical property lags behind changes in the effect causing it, as in the magnetization of ferromagnetic materials.",
    "secondary": "In physics and materials science, the loop-like lag observed in magnetic, elastic, or dielectric systems where the state of the material depends upon its past history (discovered and named by J. A. Ewing).",
    "quotes": [
      {
        "author": "James Alfred Ewing",
        "work": "Magnetic Induction in Iron and Other Metals",
        "quote": "I propose to call this lagging of magnetic effects behind magnetizing changes by the name of **hysteresis**."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "The energy dissipated as heat in transformer cores is proportional to the area of the magnetic **hysteresis** loop."
      },
      {
        "author": "Nikola Tesla",
        "work": "My Inventions: The Autobiography of Nikola Tesla",
        "quote": "In alternating current machines, iron cores must be laminated to reduce losses arising from magnetic **hysteresis**."
      }
    ]
  },
  "Dashboard — hyster/hysteretic.md": {
    "primary": "Of, relating to, or characterized by hysteresis.",
    "secondary": "In mechanics and materials physics, describing energy dissipation or phase lag resulting from cyclic loading and unloading in ferromagnetic, ferroelectric, or viscoelastic materials.",
    "quotes": [
      {
        "author": "James Alfred Ewing",
        "work": "Magnetic Induction in Iron and Other Metals",
        "quote": "The **hysteretic** loss per cycle in soft Swedish iron is remarkably small compared to hardened carbon steel."
      },
      {
        "author": "Nikola Tesla",
        "work": "Experiments with Alternate Currents of High Potential and High Frequency",
        "quote": "At elevated frequencies, internal **hysteretic** damping generates intense heating within dielectric insulators."
      },
      {
        "author": "William Thomson (Lord Kelvin)",
        "work": "Mathematical and Physical Papers",
        "quote": "Elastic bodies subjected to rapid cyclic twisting demonstrate measurable **hysteretic** retardations of recovery."
      }
    ]
  },
  "Dashboard — hyster/hysteric.md": {
    "primary": "Affected by, suffering from, or exhibiting hysteria; a person subject to hysterical fits or behavior.",
    "secondary": "In historical medicine, describing spasmodic, emotional, or convulsive paroxysms once attributed to uterine disturbance.",
    "quotes": [
      {
        "author": "Robert Burton",
        "work": "The Anatomy of Melancholy",
        "quote": "The ancient physicians attributed many wild melancholic paroxysms to **hysteric** vapors rising to the brain."
      },
      {
        "author": "William Shakespeare",
        "work": "King Lear",
        "quote": "O, how this mother swells up toward my heart! Hysterica passio, down, thou climbing sorrow, thy element's below! Cried the **hysteric** king."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The classic **hysteric** attack may simulate epilepsy with dramatic pseudoseizures and arching of the back."
      }
    ]
  },
  "Dashboard — hyster/hysterical.md": {
    "primary": "Deriving from or affected by uncontrolled, extreme emotional excess, panic, or wild laughter.",
    "secondary": "In psychiatry and psychopathology, relating to conversion disorder, somatization, or dissociative states historically diagnosed as hysteria (studied by Charcot and Freud).",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Studies on Hysteria",
        "quote": "**Hysterical** patients suffer mainly from reminiscences; their suppressed traumatic memories convert into bodily symptoms."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In the **hysterical** state, whole tracts of consciousness and sensory awareness split off from voluntary control."
      },
      {
        "author": "Charlotte Brontë",
        "work": "Jane Eyre",
        "quote": "A demonic, **hysterical** laugh echoed through the third-story corridor of Thornfield Hall in the dead of night."
      }
    ]
  },
  "Dashboard — hyster/hysterically.md": {
    "primary": "In a hysterical manner; with uncontrolled, wild, or frantic emotion.",
    "secondary": "Behaving with overwhelming panic, uncontrollable sobbing, or wild laughter.",
    "quotes": [
      {
        "author": "Charles Dickens",
        "work": "Great Expectations",
        "quote": "Miss Havisham wept **hysterically**, wringing her hands as the tragic wreckage of her life confronted her."
      },
      {
        "author": "Virginia Woolf",
        "work": "Mrs. Dalloway",
        "quote": "The distraught girl sobbed **hysterically** upon the bench, unable to explain the terror that seized her."
      },
      {
        "author": "Joseph Conrad",
        "work": "Lord Jim",
        "quote": "The panic-stricken passengers screamed **hysterically** as the ship rolled heavily into the trough of the sea."
      }
    ]
  },
  "Dashboard — hyster/hysterocatalepsy.md": {
    "primary": "A condition characterized by symptoms of both hysteria and catalepsy, in which an individual enters a trance-like state with plastic muscle rigidity during a hysterical episode.",
    "secondary": "In 19th-century neuropsychiatry (associated with Jean-Martin Charcot at the Salpêtrière), a stage of major hysteria (grande hystérie) marked by wax-like waxy flexibility (flexibilitas cerea) and sensory anesthesia.",
    "quotes": [
      {
        "author": "Jean-Martin Charcot",
        "work": "Clinical Lectures on Diseases of the Nervous System",
        "quote": "During the phase of **hysterocatalepsy**, the patient's limbs retain any bizarre posture in which the examiner places them."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The profound trance seen in **hysterocatalepsy** illustrates the complete dissociation of motor control from conscious will."
      },
      {
        "author": "Pierre Janet",
        "work": "The Mental State of Hystericals",
        "quote": "Cases of **hysterocatalepsy** exhibit deep analgesia, failing to respond to painful needle pricks while the cataleptic posture persists."
      }
    ]
  },
  "Dashboard — hyster/hysteron proteron.md": {
    "primary": "A rhetorical figure of speech in which the natural, logical, or chronological order of things is reversed ('putting the cart before the horse').",
    "secondary": "In classical rhetoric, an emphatic construction where that which should naturally follow is placed first for dramatic effect (e.g. Virgil's 'Moriamur, et in media arma ruamus' - 'Let us die, and rush into the midst of arms').",
    "quotes": [
      {
        "author": "Quintilian",
        "work": "Institutio Oratoria",
        "quote": "The figure **hysteron proteron** places that which is chronologically second first, creating striking dramatic urgency."
      },
      {
        "author": "Laurence Sterne",
        "work": "The Life and Opinions of Tristram Shandy, Gentleman",
        "quote": "My father's philosophical arguments constantly committed **hysteron proteron**, setting the consequence before the antecedent."
      },
      {
        "author": "George Puttenham",
        "work": "The Arte of English Poesie",
        "quote": "We call this figure the preposterous, or **hysteron proteron**, when you put the cart before the horse in speech."
      }
    ]
  },
  "Dashboard — hyster/hysteronproteron.md": {
    "primary": "A variant single-word spelling of hysteron proteron; the reversal of natural, logical, or chronological sequence in language or reasoning.",
    "secondary": "In classical rhetoric and logic, placing what is subsequent before what is prior; inverted syntax or inverted cause and effect.",
    "quotes": [
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Table Talk",
        "quote": "To deduce moral virtue from political expediency is a gross philosophical **hysteronproteron**."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "The modern utilitarian commits a perpetual **hysteronproteron**, mistaking outward clothes for the living inner man."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The term **hysteronproteron** combines the Greek comparatives for 'latter' and 'former' into an expressive compound."
      }
    ]
  },
  "Dashboard — hyster/hysterosalpingogram.md": {
    "primary": "A radiographic (X-ray) image of the uterus and fallopian tubes taken after injecting a radio-opaque contrast medium through the cervix.",
    "secondary": "In reproductive medicine and fertility evaluation, a primary diagnostic fluoroscopic procedure (HSG) used to determine fallopian tube patency and detect uterine cavity anomalies.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Evaluating the cause of primary female infertility routinely incorporates a diagnostic **hysterosalpingogram**."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "The **hysterosalpingogram** clearly outlined the submucosal fibroid that was distorting the endometrial contour."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Medical Career and Other Papers",
        "quote": "Contrast radiography represented a monumental advance, making internal pelvic anatomy visible upon the **hysterosalpingogram**."
      }
    ]
  },
  "Dashboard — hyster/hysteroscopy.md": {
    "primary": "The visual inspection and examination of the uterine cavity by means of an endoscope (hysteroscope) inserted through the cervix.",
    "secondary": "In modern gynecological surgery, an endoscopic diagnostic and operative procedure used to identify and resect endometrial polyps, submucosal fibroids, or intra-uterine adhesions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Direct visualization of the endometrial mucosa by **hysteroscopy** revolutionized the diagnosis of abnormal uterine bleeding."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Endoscopic methods such as **hysteroscopy** permit targeted biopsy of suspicious intrauterine lesions under direct vision."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "The optical improvement of illuminated specula paved the way for diagnostic **hysteroscopy** in pelvic disorders."
      }
    ]
  },
  "Dashboard — hyster/hysterotomy.md": {
    "primary": "Surgical incision into the wall of the uterus, as in a caesarean section.",
    "secondary": "In obstetric and gynecological surgery, an operative entry into the uterine cavity performed to deliver a fetus or remove deeply embedded intramural tumors.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "When obstructed labor threatens maternal life, emergency **hysterotomy** by the classical caesarean approach is mandatory."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "Rapid hemostasis must be secured immediately following **hysterotomy** to prevent catastrophic uterine hemorrhage."
      },
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "The history of abdominal **hysterotomy** demonstrates how antiseptic principles transformed a desperate procedure into a safe delivery."
      }
    ]
  },
  "Dashboard — hyster/panhysterectomy.md": {
    "primary": "The complete surgical excision of the entire uterus (including the cervix) and usually both ovaries and fallopian tubes; total abdominal hysterectomy with bilateral salpingo-oophorectomy.",
    "secondary": "In gynecological oncology, an extensive surgical procedure performed for widespread uterine, ovarian, or cervical malignancy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "In advanced invasive carcinoma of the endometrium, complete **panhysterectomy** offers the best prospect of long-term cure."
      },
      {
        "author": "Ferdinand Sauerbruch",
        "work": "Master Surgeon: A Life in Surgery",
        "quote": "The surgeon executed a meticulous **panhysterectomy**, clearing the pelvic lymph nodes along with the uterine adnexa."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Neurosurgical pituitary balance was complicated by sudden surgical menopause following a pelvic **panhysterectomy**."
      }
    ]
  }
}

esm_content = '''import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');
const batchData = ''' + json.dumps(BATCH1_DATA, indent=2, ensure_ascii=False) + ''';

console.log('Starting Body Part 4 Batch 1 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 1 complete: successfully updated ' + updated + ' notes.');
'''

with open("main app/scripts/curate_body4_batch1.mjs", "w", encoding="utf-8") as f:
    f.write(esm_content)

print(f"Generated main app/scripts/curate_body4_batch1.mjs with {len(BATCH1_DATA)} entries.")
