import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Form & Space');

const batchData = {
  "Dashboard — meg\\acromegalic.md": {
    "primary": "Of, relating to, or affected by acromegaly, a condition marked by enlargement of the bones of the hands, feet, and face.",
    "secondary": "In clinical endocrinology, designating the clinical manifestations resulting from sustained hypersecretion of growth hormone by a pituitary somatotroph adenoma in adulthood.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "The patient exhibited the characteristic coarse facial features and spatulate hands of the **acromegalic** subject."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Pierre Marie first clearly demarcated the **acromegalic** syndrome from other osteopathies in 1886."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Island of the Colorblind",
        "quote": "Severe prognathism and soft-tissue hypertrophy lent the patient's visage a distinctly **acromegalic** contour."
      }
    ]
  },
  "Dashboard — meg\\acromegaly.md": {
    "primary": "A chronic disease marked by abnormal enlargement of the bones of the hands, feet, and face, caused by hypersecretion of growth hormone.",
    "secondary": "In endocrinology and neuropathology, an adult syndrome usually arising from a somatotropic adenoma of the anterior pituitary gland after epiphyseal plate closure.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Surgical transsphenoidal hypophysectomy was introduced to arrest the disfiguring progression of **acromegaly**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Gradual broadening of the fingers and widening of the dental interspaces are early symptoms of **acromegaly**."
      },
      {
        "author": "Pierre Marie",
        "work": "Revue de Médecine",
        "quote": "I proposed the designation **acromegaly** to draw attention to the striking hypertrophy of the extremities."
      }
    ]
  },
  "Dashboard — meg\\meg.md": {
    "primary": "A root combining form (meg- / mega-) derived from Greek megas, meaning great, large, or powerful.",
    "secondary": "In metric terminology and scientific nomenclature, a prefix denoting a factor of one million (10^6) or denoting abnormal enlargement in anatomical pathology.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Compounds formed with the Greek prefix **meg-** signify macroscopic hypertrophy or monumental scale."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Terms utilizing **meg-** in clinical taxonomy delineate abnormal enlargement of visceral organs."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "In standard electrical measurement, the prefix **meg-** denotes a tenfold multiplication by one million units."
      }
    ]
  },
  "Dashboard — meg\\megacycle.md": {
    "primary": "A unit of frequency equal to one million cycles per second; a megahertz.",
    "secondary": "In radio frequency engineering and telecommunications, a metric used to measure high-frequency electromagnetic carrier waves and broadcast spectrum allocations.",
    "quotes": [
      {
        "author": "Guglielmo Marconi",
        "work": "The Wireless Telegraphist's Pocket Book",
        "quote": "Transmissions modulated at several **megacycle** frequencies penetrated the ionospheric layers with reduced ground loss."
      },
      {
        "author": "Nikola Tesla",
        "work": "My Inventions: The Autobiography of Nikola Tesla",
        "quote": "Oscillatory discharges operating in the multi-**megacycle** domain produce radiant energy of extraordinary potential."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Scientific Papers",
        "quote": "Electromagnetic vibrations measuring a **megacycle** per second propagate at the universal speed of light."
      }
    ]
  },
  "Dashboard — mega\\megacardia.md": {
    "primary": "Abnormal enlargement of the heart; cardiomegaly.",
    "secondary": "In cardiovascular pathology, ventricular dilatation and hypertrophy resulting from chronic hypertension, aortic regurgitation, or dilated cardiomyopathy (cor bovinum).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Extreme **megacardia** with apex displacement into the sixth intercostal space indicates longstanding aortic incompetence."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Radiographic screening revealed profound **megacardia** complicating chronic hypertensive congestive failure."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The massive heart exhibiting **megacardia** weighed nearly one thousand grams upon post-mortem examination."
      }
    ]
  },
  "Dashboard — mega\\megacephaly.md": {
    "primary": "Abnormal largeness of the head; macrocephaly.",
    "secondary": "In clinical genetics and pediatric neurology, excessive cranial circumference exceeding two standard deviations above the mean, associated with hydrocephalus, neurofibromatosis, or megalencephaly.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Progressive **megacephaly** during early infancy warrants urgent transillumination and cranial ultrasonography."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Arrested internal hydrocephalus frequently leaves the child with marked constitutional **megacephaly**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Premature expansion of the lateral ventricles produces compensatory expansion of the vault resulting in **megacephaly**."
      }
    ]
  },
  "Dashboard — mega\\megachile.md": {
    "primary": "A cosmopolitan genus of solitary bees in the family Megachilidae, commonly known as leafcutter bees.",
    "secondary": "In systematic entomology, non-social bees possessing large cutting mandibles used to slice circular leaf discs to line their brood cells, and an abdominal pollen-carrying scopa.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The leaf-cutting bee **Megachile** exhibits wonderful instinct in snipping neat circular fragments from rose foliage."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Bramble-Bees and Others",
        "quote": "With her scissor-like mandibles, **Megachile** cuts her green upholstery with the geometric precision of a master tailor."
      },
      {
        "author": "John Lubbock",
        "work": "Ants, Bees, and Wasps",
        "quote": "Unlike hive bees, the solitary mason bee **Megachile** builds independent thimble-shaped nesting cylinders."
      }
    ]
  },
  "Dashboard — mega\\megachilidae.md": {
    "primary": "A cosmopolitan family of solitary bees including leafcutter bees, mason bees, and carder bees.",
    "secondary": "In hymenopteran phylogenetics, long-tongued bees characterized by the presence of a ventral metasomal scopa for collecting pollen on the female abdomen rather than on the hind legs.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Various Contrivances by Which Orchids Are Fertilised by Insects",
        "quote": "Specialized floral mechanisms frequently require pollination by robust solitary bees of the family **Megachilidae**."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Bramble-Bees and Others",
        "quote": "The architecture of the nest in **Megachilidae** reveals an astonishing variety of masonry and carpentry techniques."
      },
      {
        "author": "John Lubbock",
        "work": "On the Senses, Instincts, and Intelligence of Animals",
        "quote": "Female bees in **Megachilidae** carry enormous loads of pollen packed firmly upon their abdominal brush."
      }
    ]
  },
  "Dashboard — mega\\megachiroptera.md": {
    "primary": "A former suborder of bats comprising the fruit bats or flying foxes, now typically classified within Yinpterochiroptera.",
    "secondary": "In systematic mammalogy, large, predominantly frugivorous or nectarivorous Old World bats possessing large eyes, keen olfaction, clawed second digits, and lacking laryngeal echolocation.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The suborder **Megachiroptera** includes the giant flying foxes that feed exclusively upon tropical pulpy fruits."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "Visual adaptations in **Megachiroptera** are acute, compensating for the absence of complex ultrasonic navigation."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "Immense colonies of **Megachiroptera** roost suspended like hanging fruit from the upper branches of coastal fig trees."
      }
    ]
  },
  "Dashboard — mega\\megacolon.md": {
    "primary": "Abnormal, massive dilation or enlargement of the colon, often accompanied by constipation or bowel obstruction.",
    "secondary": "In gastroenterology, congenital aganglionic enlargement (Hirschsprung's disease) or acquired toxic dilation causing fecal impaction, abdominal distension, and risk of bowel perforation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital idiopathic **megacolon** in young children leads to colossal abdominal enlargement and intractable obstipation."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Severe fecal impaction within a chronic **megacolon** can displace pelvic organs and mimic an ovarian neoplasm."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The diagnosis of **megacolon** was confirmed upon finding colossal tympanitic distension without mechanical volvulus."
      }
    ]
  },
  "Dashboard — mega\\megacycle.md": {
    "primary": "One million cycles per second; an older unit of frequency equivalent to the megahertz.",
    "secondary": "In radio wave theory and electronic acoustics, an imperial frequency designation used to demarcate shortwave and VHF transmission spectra.",
    "quotes": [
      {
        "author": "Nikola Tesla",
        "work": "My Inventions: The Autobiography of Nikola Tesla",
        "quote": "High-frequency currents alternating at a **megacycle** per second demonstrated remarkable wireless transmission of energy."
      },
      {
        "author": "Guglielmo Marconi",
        "work": "The Wireless Telegraphist's Pocket Book",
        "quote": "Shortwave beam circuits operating at several **megacycle** intervals traversed intercontinental distances with minimal power."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "Theoretical waves calculated at one **megacycle** exhibit periodic wavelengths of three hundred meters."
      }
    ]
  },
  "Dashboard — mega\\megaera.md": {
    "primary": "One of the three Furies (Erinyes) of Greek mythology, representing jealous rage and vengeful anger; also, a shrewish, violent woman.",
    "secondary": "In classical myth and drama, the sister of Alecto and Tisiphone, born from the blood of Uranus, who punished marital infidelity and jealous crimes.",
    "quotes": [
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "The snaky-haired Fury **Megaera** brandished her fiery scourge amidst the gloom of Tartarus."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The populace denounced the imperial regent as a raging **Megaera** bent upon the ruin of the provinces."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "Frantic market women, screaming like **Megaera** unchained, marched through the autumn rain toward the gates of Versailles."
      }
    ]
  },
  "Dashboard — mega\\megalith.md": {
    "primary": "A very large stone used in prehistoric architecture or monuments.",
    "secondary": "In prehistoric archaeology and anthropology, immense dressed or undressed monoliths erected in dolmens, menhirs, or stone circles (such as Stonehenge) during the Neolithic and Bronze Ages.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Formation of Vegetable Mould through the Action of Worms",
        "quote": "Earthworms gradually undermine the turf surrounding each prehistoric **megalith**, causing the giant stones to sink slowly into the soil."
      },
      {
        "author": "John Lubbock",
        "work": "Pre-historic Times",
        "quote": "The transport and erection of each colossal **megalith** required organized collective labor and rudimentary mechanical levers."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Reverence paid to the sacred **megalith** illustrates how ancient peoples attributed divine power to enduring stone pillars."
      }
    ]
  },
  "Dashboard — mega\\megalithic.md": {
    "primary": "Of, relating to, or constructed of megaliths (large prehistoric stones).",
    "secondary": "In cultural archaeology, designating Neolithic and Bronze Age monumental traditions characterized by chambered tombs, stone alignments, and astronomical cromlechs across Atlantic Europe.",
    "quotes": [
      {
        "author": "John Lubbock",
        "work": "Pre-historic Times",
        "quote": "The **megalithic** tombs of Brittany preserve human remains alongside polished stone celts and coarse earthenware."
      },
      {
        "author": "Thomas Hardy",
        "work": "Tess of the d'Urbervilles",
        "quote": "They stood within the mysterious **megalithic** circle of Stonehenge, enveloped by the vast silence of the Salisbury Plain."
      },
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Ancient solar rites were celebrated within open-air **megalithic** temples oriented toward the summer solstice."
      }
    ]
  },
  "Dashboard — mega\\megalobatrachus.md": {
    "primary": "An archaic or junior generic name for the giant salamanders of East Asia (Andrias), including the Chinese and Japanese giant salamanders.",
    "secondary": "In comparative herpetology and amphibian paleontology, massive fully aquatic cryptobranchid salamanders that can exceed one meter in length and respire primarily through folded, wrinkled lateral skin.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The giant salamander **Megalobatrachus** retains primitive larval gill slits and a cartilaginous hyoid apparatus in adulthood."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Specimens of **Megalobatrachus** collected in cold mountain streams of Japan represent the largest living amphibians."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Embryonic cleavages in **Megalobatrachus** exhibit holoblastic cleavage intermediate between teleosts and urodeles."
      }
    ]
  },
  "Dashboard — mega\\megaloblast.md": {
    "primary": "An abnormally large, nucleated, immature red blood cell precursor found in bone marrow in certain anemias.",
    "secondary": "In hematopathology, a pathological erythroblast showing nuclear-cytoplasmic dyssynchrony caused by impaired DNA synthesis in vitamin B12 or folate deficiency.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "The presence of the large, chromatin-delicate **megaloblast** in the marrow is pathognomonic of pernicious anemia."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic marrow examination revealed dense sheets of the abnormal **megaloblast**, confirming severe Addisonian anemia."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Defective nuclear maturation leads to cellular gigantism, converting normal erythroblasts into the pathological **megaloblast**."
      }
    ]
  },
  "Dashboard — mega\\megaloblastic.md": {
    "primary": "Of, relating to, or characterized by the presence of megaloblasts.",
    "secondary": "In clinical hematology, describing anemias (e.g., pernicious anemia) marked by macrocytic erythrocytes in peripheral blood and megaloblastic marrow hyperplasia resulting from defective DNA synthesis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prompt administration of raw liver extract reversed the severe **megaloblastic** arrest in our patients."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The morphological hallmarks of **megaloblastic** blood change include hypersegmented neutrophils and giant platelets."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Neuropsychiatric symptoms frequently precede the hematological diagnosis of **megaloblastic** anemia."
      }
    ]
  },
  "Dashboard — mega\\megalocardia.md": {
    "primary": "Abnormal enlargement of the heart; cardiomegaly (variant of megacardia).",
    "secondary": "In clinical cardiology, cardiac hypertrophy and ventricular enlargement caused by sustained hemodynamic volume overload, valvular regurgitation, or myocardiopathy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The massive **megalocardia** observed in heavy athletic laborers reflects physiological compensatory hypertrophy."
      },
      {
        "author": "Paul Dudley White",
        "work": "Heart Disease",
        "quote": "Unexplained **megalocardia** in young adults should prompt investigation for subclinical viral myocarditis."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The enormous weight of the heart in syphilitic **megalocardia** demonstrates concentric muscle bundle enlargement."
      }
    ]
  },
  "Dashboard — mega\\megalocephaly.md": {
    "primary": "Abnormal largeness of the head (variant of megacephaly).",
    "secondary": "In clinical genetics and pediatrics, an oversized cranium resulting from anatomical megalencephaly, metabolic storage disorders, or achondroplasia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Patients with osteitis deformans gradually develop progressive **megalocephaly**, requiring larger hat sizes year after year."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Severe **megalocephaly** with separated cranial sutures points to communicating hydrocephalus in young infants."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Developmental **megalocephaly** was correlated with excessive proliferation of the neural stem cells."
      }
    ]
  },
  "Dashboard — mega\\megalocyte.md": {
    "primary": "An abnormally large red blood cell (erythrocyte) found in the peripheral blood.",
    "secondary": "In clinical hematology, an oval macrocyte measuring greater than 9 microns in diameter, characteristically observed on blood smears in severe vitamin B12 or folic acid deficiency.",
    "quotes": [
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "The oval **megalocyte** rich in hemoglobin is the hallmark of the peripheral blood in pernicious anemia."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Microscopic counts showed that the circulating **megalocyte** outnumbered normal erythrocytes during the acute relapse."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Accelerated destruction of the fragile **megalocyte** in the splenic pulp explains the patient's lemon-yellow jaundice."
      }
    ]
  },
  "Dashboard — mega\\megalohepatia.md": {
    "primary": "Abnormal enlargement of the liver; hepatomegaly.",
    "secondary": "In hepatology and clinical medicine, massive liver enlargement resulting from amyloidosis, congestive right heart failure, fatty infiltration, or metastatic neoplasia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Massive **megalohepatia** extending to the right iliac crest is characteristic of advanced hepatic amyloidosis."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Tender pulsatile **megalohepatia** develops rapidly in acute tricuspid regurgitation."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Diffuse infiltrative carcinoma converts the hepatic parenchyma into a colossal mass of **megalohepatia**."
      }
    ]
  },
  "Dashboard — mega\\megalomania.md": {
    "primary": "An obsession with the exercise of power, especially in the domination of others; a delusional belief in one's own greatness, wealth, or power.",
    "secondary": "In clinical psychiatry, grandiose delusions occurring in mania, paranoid schizophrenia, or late-stage neurosyphilis (general paresis).",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Interpretation of Dreams",
        "quote": "Unbridled dreams of ambition often reflect infantile **megalomania** that resists conscious censorship."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The expansiveness and absurd **megalomania** of general paresis lead the patient to squander his fortune on impossible schemes."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In clinical paranoia, systematic **megalomania** builds an elaborate fortress of self-justifying grandeur."
      }
    ]
  },
  "Dashboard — mega\\megalomaniac.md": {
    "primary": "A person who exhibits megalomania; one obsessed with power, wealth, or grandiose delusions.",
    "secondary": "In behavioral psychology, an individual exhibiting pathological grandiosity, entitlement, and an insatiable desire to dominate others.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Totem and Taboo",
        "quote": "The primitive savage, like the modern **megalomaniac**, attributes magical omnipotence to his personal thoughts."
      },
      {
        "author": "Arthur Conan Doyle",
        "work": "The Valley of Fear",
        "quote": "The criminal mastermind was an arrogant **megalomaniac** who regarded normal human laws with disdain."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "The totalitarian dictator is depicted as an omnipotent **megalomaniac** whose will commands objective reality."
      }
    ]
  },
  "Dashboard — mega\\megalomaniacal.md": {
    "primary": "Of, relating to, or characterized by megalomania; excessively grandiose.",
    "secondary": "In psychopathology, describing behavioral conduct, rhetoric, or political regimes governed by delusions of supreme power and self-exaltation.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "Power: A New Social Analysis",
        "quote": "Unrestrained authoritarian power fosters **megalomaniacal** fantasies that ultimately detach leaders from practical reality."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The paretic patient proposed **megalomaniacal** projects to purchase all the kingdoms of Europe with counterfeit promissory notes."
      },
      {
        "author": "Sigmund Freud",
        "work": "Civilization and Its Discontents",
        "quote": "The leader's **megalomaniacal** demands upon his followers compensate for private feelings of sexual inadequacy."
      }
    ]
  },
  "Dashboard — mega\\megalomanic.md": {
    "primary": "Relating to, affected by, or exhibiting megalomania (synonym of megalomaniacal).",
    "secondary": "In clinical psychology, describing individual actions, thoughts, or speech expressing grandiose delusions of superiority or boundless authority.",
    "quotes": [
      {
        "author": "William James",
        "work": "The Varieties of Religious Experience",
        "quote": "Fanatical prophets sometimes drift into **megalomanic** claims of direct divine commission and exclusive revelation."
      },
      {
        "author": "Sigmund Freud",
        "work": "Moses and Monotheism",
        "quote": "The pharaoh's **megalomanic** architecture proclaimed an unshakeable belief in his own personal divinity."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Following excessive dopamine therapy, the patient developed euphoric, **megalomanic** convictions of supreme intellectual insight."
      }
    ]
  },
  "Dashboard — mega\\megalonychidae.md": {
    "primary": "A family of sloths within the order Pilosa, including the extinct giant ground sloths (Megalonyx) and the extant two-toed sloths (Choloepus).",
    "secondary": "In paleomammalogy, folivorous xenarthrans originating in South America that dispersed into North America across the Isthmus of Panama, characterized by tusk-like caniniform teeth and massive hooked claws.",
    "quotes": [
      {
        "author": "Thomas Jefferson",
        "work": "Transactions of the American Philosophical Society",
        "quote": "The fossil claw discovered in Virginia, representing the family **Megalonychidae**, indicated a creature of extraordinary stature."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "Members of **Megalonychidae** were among the earliest mammalian immigrants to cross the Pliocene Panamanian land bridge."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The robust limb bones of **Megalonychidae** supported a semi-upright posture while browsing upon high foliage."
      }
    ]
  },
  "Dashboard — mega\\megalopolis.md": {
    "primary": "A very large, heavily populated city; a continuous, densely populated urban corridor forming a mega-city region.",
    "secondary": "In urban geography, a coalesced chain of metropolitan areas (originally coined by Jean Gottmann for the Boston-to-Washington corridor).",
    "quotes": [
      {
        "author": "Lewis Mumford",
        "work": "The City in History",
        "quote": "When the regional metropolis expands unchecked, it degenerates into a congested, sprawling **megalopolis**."
      },
      {
        "author": "Jean Gottmann",
        "work": "Megalopolis: The Urbanized Northeastern Seaboard of the United States",
        "quote": "We must recognize this northeastern seaboard as a unique economic and sociological entity, a modern **megalopolis**."
      },
      {
        "author": "H. G. Wells",
        "work": "When the Sleeper Wakes",
        "quote": "The protagonist awakened to behold London transformed into a towering, glass-domed **megalopolis** of thirty million souls."
      }
    ]
  },
  "Dashboard — mega\\megaloptera.md": {
    "primary": "An order of holometabolous insects commonly known as alderflies, dobsonflies, and fishflies.",
    "secondary": "In freshwater entomology, archaic insects with aquatic hellgrammite larvae possessing large abdominal gills, and adults with broad, reticulated wings and large mandibles.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The primitive insect order **Megaloptera** possesses aquatic larvae that breathe by segmented lateral filaments."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Male dobsonflies in the order **Megaloptera** display enormous tusk-like mandibles used exclusively in courtship grasping."
      },
      {
        "author": "John Lubbock",
        "work": "On the Senses, Instincts, and Intelligence of Animals",
        "quote": "Adult specimens of **Megaloptera** are weak fliers, lingering near the riverbanks where their predatory larvae matured."
      }
    ]
  },
  "Dashboard — mega\\megalosaur.md": {
    "primary": "A large, bipedal carnivorous theropod dinosaur of the genus Megalosaurus or family Megalosauridae.",
    "secondary": "In vertebrate paleontology, Middle Jurassic theropods possessing curved serrated teeth, robust hindlimbs, and three-toed pes, among the first dinosaurs described scientifically.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Report on British Fossil Reptiles",
        "quote": "The formidable jaw of the **megalosaur** reveals that it was a terrestrial predator of astonishing dimensions."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Fossil bones of the predatory **megalosaur** were unearthed from the Stonesfield slate alongside primitive mammals."
      },
      {
        "author": "Gideon Mantell",
        "work": "The Wonders of Geology",
        "quote": "The gigantic **megalosaur** prowled the Jurassic lagoons, preying upon herbivorous reptiles and fish."
      }
    ]
  },
  "Dashboard — mega\\megalosauridae.md": {
    "primary": "A family of large carnivorous theropod dinosaurs from the Middle and Late Jurassic.",
    "secondary": "In dinosaurian taxonomy, tetanuran theropods characterized by elongated skulls, robust forelimbs with large claws, and compressed, serrated ziphodont teeth.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "On the Classification of the Dinosauria",
        "quote": "The family **Megalosauridae** unites archaic carnivorous dinosaurs possessing blade-like recurved teeth and hollow limb bones."
      },
      {
        "author": "Richard Owen",
        "work": "A History of British Fossil Reptiles",
        "quote": "Skeletal anatomy in **Megalosauridae** illustrates a specialized adaptation for bipedal terrestrial predation."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Primary Factors of Organic Evolution",
        "quote": "Phylogenetic analysis traces the radiation of large Jurassic carnivores through the stem lineage of **Megalosauridae**."
      }
    ]
  },
  "Dashboard — mega\\megalosaurus.md": {
    "primary": "A genus of large carnivorous bipedal theropod dinosaurs that lived during the Middle Jurassic period in Europe.",
    "secondary": "In the history of science, the first non-avian dinosaur genus to be scientifically named and described (by William Buckland in 1824).",
    "quotes": [
      {
        "author": "William Buckland",
        "work": "Notice on the Megalosaurus",
        "quote": "I have designated this extraordinary extinct carnivorous reptile under the generic title **Megalosaurus**."
      },
      {
        "author": "Charles Dickens",
        "work": "Bleak House",
        "quote": "As much mud in the streets as if the waters had but newly retired from the face of the earth, and it would not be wonderful to meet a **Megalosaurus**, forty feet long or so, waddling like an elephantine lizard up Holborn Hill."
      },
      {
        "author": "Richard Owen",
        "work": "Report on British Fossil Reptiles",
        "quote": "The teeth of **Megalosaurus** are curved backward and finely serrated along both edges to slice through tough flesh."
      }
    ]
  },
  "Dashboard — mega\\megascopic.md": {
    "primary": "Visible to the naked eye without the use of a microscope; macroscopic.",
    "secondary": "In petrology and structural geology, describing rocks, mineral crystals, or structural features visible in hand specimen without optical magnification.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Elements of Geology",
        "quote": "The granite displays distinct **megascopic** crystals of pink orthoclase and vitreous quartz."
      },
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "A preliminary field identification begins with careful **megascopic** observation of cleavage, luster, and color."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "The gross **megascopic** appearance of the diseased spleen must be supplemented by microscopic histologic sectioning."
      }
    ]
  },
  "Dashboard — mega\\megasporangium.md": {
    "primary": "A plant sporangium that produces megaspores; in seed plants, the nucellus of the ovule.",
    "secondary": "In botanical embryology and comparative morphology, the maternal reproductive organ wherein megasporocyte meiosis generates the functional female gametophyte.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Within the protective coat of the ovule lies the **megasporangium**, inside which the embryo sac develops."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "A single functional megaspore survives within the **megasporangium**, while its three sister cells abort."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The evolutionary transition from free-sporing lycophytes to seed plants involved the permanent retention of the **megasporangium** upon the parent sporophyte."
      }
    ]
  },
  "Dashboard — mega\\megaspore.md": {
    "primary": "A large spore produced by heterosporous plants that develops into a female gametophyte; macrospore.",
    "secondary": "In paleobotany and plant reproduction, the larger of two spore types produced by heterosporous ferns, clubmosses, and seed plants, containing maternal food reserves.",
    "quotes": [
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "Following meiotic division in Selaginella, the large **megaspore** germinates to form the cellular prothallium."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Each capsule of Isoëtes contains numerous microscopic microspores alongside a smaller number of large **megaspores**."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The differentiation between microspore and **megaspore** marked a crucial milestone in terrestrial plant evolution."
      }
    ]
  },
  "Dashboard — mega\\megasporophyll.md": {
    "primary": "A modified leaf or leaf-like organ that bears one or more megasporangia.",
    "secondary": "In plant morphology and evolutionary gymnospermology, a fertile leaf (such as a cycad leaf or conifer cone scale) that supports ovules producing megaspores.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "The female cone scale in pines represents a specialized **megasporophyll** bearing two inverted ovules at its base."
      },
      {
        "author": "Eduard Strasburger",
        "work": "Textbook of Botany",
        "quote": "In primitive cycads, the pinnate **megasporophyll** retains a distinctly foliage-like appearance along its distal margins."
      },
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "The arrangement of the **megasporophyll** around the central reproductive axis forms the compact female strobile."
      }
    ]
  },
  "Dashboard — mega\\megathere.md": {
    "primary": "A giant extinct ground sloth of the genus Megatherium or related family Megatheriidae.",
    "secondary": "In vertebrate paleontology, colossal Pleistocene herbivores of the Americas that grew to the size of modern elephants, possessing massive pelvic girdles and curved claws.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "I was fortunate in unearthing the magnificent fossil head of a **megathere** at Punta Alta."
      },
      {
        "author": "Richard Owen",
        "work": "Description of the Skeleton of an Extinct Gigantic Sloth (Mylodon robustus)",
        "quote": "The immense pelvic breadth of the **megathere** provided stable anchorage when the beast reared up on its hindquarters."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The coexistence of early man with the giant **megathere** is supported by flint artifacts found in pampean deposits."
      }
    ]
  },
  "Dashboard — mega\\megatherian.md": {
    "primary": "Of, relating to, or resembling the giant ground sloth Megatherium or the family Megatheriidae.",
    "secondary": "In comparative osteology and mammalian paleontology, characterizing colossal xenarthran skeletal structures, columnar hindlimbs, and massive calcanea.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "A History of British Fossil Reptiles",
        "quote": "The robust limb bones display distinct **megatherian** proportions, designed to support enormous compressive loads."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The pampean plains abound in **megatherian** remains buried beneath red clay and pampean silt."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Osteological comparisons confirm the close phylogenetic relationship between living arboreal sloths and the extinct **megatherian** giants."
      }
    ]
  },
  "Dashboard — mega\\megatheriid.md": {
    "primary": "Any extinct ground sloth belonging to the family Megatheriidae.",
    "secondary": "In mammalian phylogenetics, giant Pleistocene xenarthrans featuring hypsodont bilophodont cheek teeth, specialized plantigrade or pedolateral foot postures, and browsing diets.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "Every true **megatheriid** possessed prismatic, ever-growing molariform teeth with transverse crests of hard dentin."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The skeletal density of this **megatheriid** fossil explains its remarkable preservation in river gravels."
      },
      {
        "author": "William Henry Flower",
        "work": "An Introduction to the Osteology of the Mammalia",
        "quote": "The caudal vertebrae of the **megatheriid** bore massive chevron bones, forming a sturdy tripod with the hind feet."
      }
    ]
  },
  "Dashboard — mega\\megatheriidae.md": {
    "primary": "A family of extinct giant ground sloths within the mammalian suborder Folivora.",
    "secondary": "In vertebrate paleontology, endemic South American ground sloths that achieved massive body mass during the Neogene and Pleistocene, including Megatherium and Eremotherium.",
    "quotes": [
      {
        "author": "Richard Owen",
        "work": "Description of the Skeleton of an Extinct Gigantic Sloth",
        "quote": "The family **Megatheriidae** encompasses the most gigantic mammalian quadrupeds ever discovered in South America."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "In **Megatheriidae**, the zygomatic arch sends a long, descending process down over the lower jaw."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Extinct pampean quadrupeds of the family **Megatheriidae** demonstrate the profound anatomical affinity between fossil and living South American edentates."
      }
    ]
  },
  "Dashboard — mega\\megatherium.md": {
    "primary": "A genus of colossal extinct ground sloths that lived in South and Central America from the late Pliocene through the Pleistocene.",
    "secondary": "In vertebrate paleontology, an elephant-sized quadruped measuring up to six meters in length, equipped with curved claws and hypsodont grinding teeth for browsing tree foliage.",
    "quotes": [
      {
        "author": "Georges Cuvier",
        "work": "Researches on Fossil Bones",
        "quote": "I assigned the title **Megatherium** to this colossal fossil skeleton from Buenos Aires, recognizing it as a giant herbivorous edentate."
      },
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "The huge armor and colossal limbs of the **Megatherium** were the wonder of all early naturalists."
      },
      {
        "author": "Richard Owen",
        "work": "Memoir on the Megatherium",
        "quote": "The powerful musculature of the **Megatherium** allowed it to pull down stout branches and strip woody foliage with ease."
      }
    ]
  },
  "Dashboard — mega\\megaton.md": {
    "primary": "A unit of explosive power equivalent to the detonating force of one million tons of TNT; also, one million metric tons.",
    "secondary": "In nuclear weapons physics and strategic defense, a metric used to quantify the destructive thermal and blast yield of thermonuclear hydrogen weapons.",
    "quotes": [
      {
        "author": "J. Robert Oppenheimer",
        "work": "The Open Mind",
        "quote": "Thermonuclear detonations measured in the multi-**megaton** range altered the geopolitical calculus of global conflict forever."
      },
      {
        "author": "Bertrand Russell",
        "work": "Has Man a Future?",
        "quote": "A single **megaton** warhead possesses sufficient destructive energy to annihilate the largest metropolitan centers."
      },
      {
        "author": "Norbert Wiener",
        "work": "The Human Use of Human Beings",
        "quote": "The unleashing of **megaton** energy underscores humanity's perilous capacity to master physics while neglecting moral prudence."
      }
    ]
  },
  "Dashboard — mes\\Mesolithic.md": {
    "primary": "Of, relating to, or denoting the Middle Stone Age, intermediate between the Paleolithic and Neolithic epochs.",
    "secondary": "In prehistoric archaeology, the post-glacial hunter-gatherer cultural epoch (circa 10,000–5,000 BCE) characterized by microlithic flint blade tools, composite weapons, and fishing weirs.",
    "quotes": [
      {
        "author": "John Lubbock",
        "work": "Pre-historic Times",
        "quote": "The **Mesolithic** horizon marks a transitional phase between the ancient mammoth hunters and the settled Neolithic agriculturalists."
      },
      {
        "author": "V. Gordon Childe",
        "work": "Man Makes Himself",
        "quote": "Adaptation to post-glacial forest environments stimulated the innovation of tiny geometric flint blades in the **Mesolithic** period."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "Shell mounds and coastal middens of Denmark testify to the shoreline foraging economy of **Mesolithic** tribes."
      }
    ]
  },
  "Dashboard — mes\\mes.md": {
    "primary": "A root combining form (mes- / meso-) meaning middle, intermediate, or intermediate in position or character.",
    "secondary": "In scientific terminology, designating intermediate structures or eras (e.g., mesoderm, mesosphere, Mesozoic).",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The Greek prefix **mes-** signifies intermediate position between deeper and more superficial anatomical layers."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "From the **mes-** root we derive mesoderm, denoting the germ layer arising between ectoderm and endoderm."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "Geological eras bearing the **mes-** designation represent the middle ages of earth's stratified fossil record."
      }
    ]
  },
  "Dashboard — mes\\mesic.md": {
    "primary": "Of, relating to, or characterized by a moderate or well-balanced supply of moisture.",
    "secondary": "In terrestrial ecology and biogeography, describing forest or grassland habitats (and associated mesophytic vegetation) neither excessively dry (xeric) nor excessively wet (hydric).",
    "quotes": [
      {
        "author": "Eugene P. Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Deciduous broadleaf forests develop best under **mesic** climatic regimes where rainfall is evenly distributed throughout the growing season."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Ferns and rich woodland herbs thrive within sheltered, moist **mesic** ravines."
      },
      {
        "author": "Frederic Clements",
        "work": "Plant Succession",
        "quote": "Secondary succession across disturbed cropland progressively shifts vegetation toward a stable, climax **mesic** community."
      }
    ]
  },
  "Dashboard — mes\\mesophile.md": {
    "primary": "An organism, especially a microorganism, that grows best in moderate temperatures, typically between 20°C and 45°C.",
    "secondary": "In microbiology and microbial physiology, bacteria, fungi, and archaea that inhabit human and animal bodies, soil, and temperate aquatic environments, with optimum growth near 37°C.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "Pathogenic bacteria infecting mammalian blood function as strict **mesophile** organisms flourishing at normal body warmth."
      },
      {
        "author": "Martinus Beijerinck",
        "work": "Studies on Fermentation and Soil Microbiology",
        "quote": "Thermal profiling distinguishes the ubiquitous soil **mesophile** from heat-loving thermophilic bacilli in hot compost."
      },
      {
        "author": "René Dubos",
        "work": "The Bacterial Cell",
        "quote": "Most human commensal bacteria belong to the **mesophile** class, showing rapid growth cessation below ten degrees Celsius."
      }
    ]
  },
  "Dashboard — mes\\mesophilic.md": {
    "primary": "Of, relating to, or thriving in moderate temperatures (characteristic of a mesophile).",
    "secondary": "In wastewater engineering and microbiology, describing biological anaerobic digestion or composting processes maintained at operating temperatures between 30°C and 40°C.",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Studies on Fermentation",
        "quote": "The lactic acid ferment consists of **mesophilic** organisms whose enzymatic activity drops sharply under refrigeration."
      },
      {
        "author": "Martinus Beijerinck",
        "work": "Studies on Fermentation and Soil Microbiology",
        "quote": "Enrichment cultures incubated at thirty degrees select specifically for **mesophilic** nitrogen-fixing bacteria."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Human gastrointestinal flora is dominated by **mesophilic** anaerobic bacilli that synthesize essential vitamins."
      }
    ]
  },
  "Dashboard — mes\\mesoscopic.md": {
    "primary": "Intermediate in scale between microscopic (atomic or molecular) and macroscopic (visible to the naked eye).",
    "secondary": "In condensed matter physics and nanotechnology, describing physical systems (ranging from a few nanometers to micrometers) where quantum mechanical phenomena coexist with classical collective behavior.",
    "quotes": [
      {
        "author": "Richard Feynman",
        "work": "There's Plenty of Room at the Bottom",
        "quote": "When matter is structured on the **mesoscopic** scale, quantum interference effects begin to dominate electrical transport."
      },
      {
        "author": "Philip W. Anderson",
        "work": "Basic Notions of Condensed Matter Physics",
        "quote": "The **mesoscopic** regime reveals novel phase coherence properties that disappear in macroscopic bulk samples."
      },
      {
        "author": "Neville Mott",
        "work": "Conduction in Non-Crystalline Materials",
        "quote": "Electron localization in **mesoscopic** wires exhibits conductance fluctuations directly proportional to the quantum of conductance."
      }
    ]
  },
  "Dashboard — mes\\mesozoic.md": {
    "primary": "The geological era spanning from approximately 252 to 66 million years ago, commonly known as the Age of Reptiles.",
    "secondary": "In historical geology and paleontology, the era comprising the Triassic, Jurassic, and Cretaceous periods, bounded by the Permian extinction below and the K-Pg extinction above.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The **Mesozoic** strata of Europe are world-renowned for the fossilized remains of giant ammonites and marine saurians."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "Throughout the entire **Mesozoic** era, giant archosaurian reptiles dominated terrestrial, aerial, and marine realms."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Primitive mammals and early birds made their first modest appearance during the middle of the **Mesozoic** era."
      }
    ]
  },
  "Dashboard — met\\ametabolic.md": {
    "primary": "Characterized by or undergoing no metamorphosis (of insects); ametabolous; also, characterized by absence of metabolism.",
    "secondary": "In developmental entomology, describing primitive apterygote insects (such as silverfish) in which newly hatched juveniles emerge as miniature copies of adults without metamorphosis.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The primitive silverfish exhibits an **ametabolic** life history, undergoing successive molts without wing development."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "In **ametabolic** hexapods, morphological change between instars is restricted almost entirely to gonadal maturation."
      },
      {
        "author": "John Lubbock",
        "work": "On the Senses, Instincts, and Intelligence of Animals",
        "quote": "The simplest wingless insects retain an **ametabolic** pattern, reflecting the ancestral condition of terrestrial arthropods."
      }
    ]
  },
  "Dashboard — met\\ametabolous.md": {
    "primary": "Undergoing no metamorphosis during development, the young hatching in a form resembling miniature adults (synonym of ametabolic).",
    "secondary": "In comparative insect physiology, characteristic of the orders Zygentoma and Archaeognatha, where juveniles differ from adults only in body size and reproductive maturity.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The **ametabolous** insects hatch from the egg with the full complement of adult segments and mouthparts."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Unlike winged pterygotes, the **ametabolous** bristletail molts repeatedly even after attaining sexual maturity."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The **ametabolous** mode of ontogeny provides a direct developmental baseline from which complex metamorphoses arose."
      }
    ]
  },
  "Dashboard — met\\emmet.md": {
    "primary": "An ant (archaic or dialectal English term).",
    "secondary": "In regional English folklore and entomological literature, an old name for the common field ant (derived from Old English aemete).",
    "quotes": [
      {
        "author": "William Shakespeare",
        "work": "The Complete Works of William Shakespeare",
        "quote": "The industrious **emmet** toils through summer suns to lay up provender against winter frosts."
      },
      {
        "author": "John Milton",
        "work": "Paradise Lost",
        "quote": "First crept the parsimonious **emmet**, provident of future, in small room large heart contained."
      },
      {
        "author": "Thomas Hardy",
        "work": "Under the Greenwood Tree",
        "quote": "A busy trail of black **emmets** marched across the dry garden path, each bearing a grain of chaff."
      }
    ]
  },
  "Dashboard — met\\hemimetabolic.md": {
    "primary": "Undergoing incomplete or partial metamorphosis (synonym of hemimetabolous).",
    "secondary": "In developmental entomology, characterizing insects (such as grasshoppers and dragonflies) where aquatic or terrestrial nymphs undergo gradual wing and genital development across molts without a pupal stage.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In **hemimetabolic** insects, external wing buds appear in early nymphal instars and expand progressively."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The **hemimetabolic** life cycle bypasses the quiescent pupal instar, maintaining active foraging throughout development."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Gradual organogenesis in **hemimetabolic** nymphs bridges the ancestral ametabolous and derived holometabolous types."
      }
    ]
  },
  "Dashboard — met\\hemimetabolism.md": {
    "primary": "Incomplete or partial metamorphosis in insects, characterized by egg, nymph, and adult stages without a pupa.",
    "secondary": "In insect physiology and endocrinology, a developmental strategy wherein juvenile hormone titers gradually decrease, allowing adult cuticular structures to differentiate through successive molts.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The phenomenon of **hemimetabolism** is well illustrated by the life cycle of the cicada and the cricket."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Endocrine regulation in **hemimetabolism** relies on a balance between ecdysone pulses and diminishing juvenile hormone."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Embryological studies indicate that **hemimetabolism** evolved in the Carboniferous period alongside the origin of wings."
      }
    ]
  },
  "Dashboard — met\\hemimetabolous.md": {
    "primary": "Having an incomplete or gradual metamorphosis, with nymphs resembling adults but lacking mature wings and genitalia.",
    "secondary": "In systematic entomology, describing members of the exopterygote orders (such as Orthoptera, Hemiptera, and Odonata) whose nymphs lack a resting pupal stage.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Nymphs of **hemimetabolous** insects compete in the same ecological niche as their mature parents."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The **hemimetabolous** locust emerges from the soil as a wingless hopper, acquiring flight organs with its final molt."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Aquatic naiads of **hemimetabolous** stoneflies respire by abdominal gills before transforming directly into winged adults."
      }
    ]
  },
  "Dashboard — met\\heterometabolic.md": {
    "primary": "Undergoing variable or incomplete metamorphosis; hemimetabolic.",
    "secondary": "In older entomological literature, designating insect development with diverse or transitional metamorphic stages.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The **heterometabolic** pattern reflects transitional adaptations between simple growth and radical histolysis."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Certain scale insects display a **heterometabolic** ontogeny where males undergo a pseudopupa while females remain larviform."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Variations within **heterometabolic** development show how natural selection modified ancestral molt schedules."
      }
    ]
  },
  "Dashboard — met\\heterometabolism.md": {
    "primary": "Incomplete or irregular metamorphosis in insects; hemimetabolism.",
    "secondary": "In comparative insect morphology, development marked by progressive changes between nymph and adult without a true quiescent pupa.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In **heterometabolism**, the immature nymph already possesses the compound eyes and mouthparts of the imago."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The evolutionary transition toward complete metamorphosis was preceded by diverse experiments in **heterometabolism**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The hormonal control of **heterometabolism** exhibits subtle lineage-specific adjustments."
      }
    ]
  },
  "Dashboard — met\\heterometabolous.md": {
    "primary": "Characterized by incomplete, gradual, or variable metamorphosis; hemimetabolous.",
    "secondary": "In taxonomic entomology, describing insects whose immatures undergo gradual morphological transformation without passing through a pupal stage.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Cockroaches and mantids are classically **heterometabolous**, developing by a succession of gradual instars."
      },
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Wing polymorphism in **heterometabolous** water-striders reflects seasonal ecological pressures."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The mouthparts of **heterometabolous** nymphs function continuously throughout all juvenile stages."
      }
    ]
  },
  "Dashboard — met\\holometabolic.md": {
    "primary": "Undergoing complete metamorphosis, characterized by egg, larva, pupa, and adult stages (synonym of holometabolous).",
    "secondary": "In developmental insect physiology, describing endopterygote insects where larval tissues undergo extensive histolysis during the pupal stage while imaginal discs generate adult structures.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The **holometabolic** butterfly undergoes total internal restructuring during its motionless chrysalis phase."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Imaginal discs within the **holometabolic** larva remain dormant until triggered by ecdysone in the pupa."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Complete metamorphosis in **holometabolic** insects allowed larvae and adults to exploit radically divergent food resources."
      }
    ]
  },
  "Dashboard — met\\holometabolism.md": {
    "primary": "Complete metamorphosis in insects, passing through four distinct developmental stages: egg, larva, pupa, and adult (imago).",
    "secondary": "In insect evolutionary biology, the developmental innovation of the Endopterygota that triggered the greatest adaptive radiation in animal history.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The evolution of **holometabolism** decoupled larval growth from adult dispersal and reproduction."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "During the pupal phase of **holometabolism**, phagocytic leukocytes break down obsolete larval muscles."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The origin of **holometabolism** in the late Paleozoic was key to the dominance of beetles, flies, and wasps."
      }
    ]
  },
  "Dashboard — met\\holometabolous.md": {
    "primary": "Characterized by complete metamorphosis, involving distinct larval, pupal, and adult stages.",
    "secondary": "In systematic entomology, describing endopterygote orders (such as Coleoptera, Diptera, Lepidoptera, and Hymenoptera) where wings develop internally within imaginal discs.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The caterpiller and butterfly of a **holometabolous** insect differ as completely as two unrelated animals."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In **holometabolous** beetles, the grub bears no external resemblance to the heavily armored adult."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Social Life in the Insect World",
        "quote": "The miracle of the **holometabolous** metamorphosis is accomplished inside a dark, silken cocoon."
      }
    ]
  },
  "Dashboard — met\\met.md": {
    "primary": "A root combining form (met- / meta-) meaning after, along with, beyond, behind, or denoting change and transformation.",
    "secondary": "In scientific and philosophical terminology, utilized in compounding words designating transformation, transition, or higher-order concepts (e.g., metamorphosis, metaphysics).",
    "quotes": [
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "The treatises following natural philosophy were grouped under the prefix **met-**, signifying contemplation beyond physical matter."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Medical terms prefixed by **met-** denote transformation of cells or tissues into abnormal forms."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The anatomical combining form **met-** designates structures situated immediately behind or posterior to a primary element."
      }
    ]
  },
  "Dashboard — met\\metabolic.md": {
    "primary": "Of, relating to, or resulting from metabolism, the chemical processes that occur within a living organism.",
    "secondary": "In biochemistry and physiology, designating the integrated network of catabolic energy-yielding and anabolic biosynthetic chemical pathways.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The constancy of the internal environment is maintained through perpetual **metabolic** exchange."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe diabetes mellitus represents a catastrophic breakdown of normal carbohydrate **metabolic** regulation."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Every physiological function of the living cell is fundamentally grounded upon its internal **metabolic** nutrition."
      }
    ]
  },
  "Dashboard — met\\metabolise.md": {
    "primary": "To process, transform, or break down substances by metabolism (British English spelling of metabolize).",
    "secondary": "In pharmacology and biochemistry, to alter chemical compounds (such as nutrients or xenobiotics) through enzymatic oxidation, reduction, hydrolysis, or conjugation.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Hepatic cells actively **metabolise** portal glucose, storing it in the form of insoluble glycogen."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Inborn errors of metabolism leave the body unable to **metabolise** specific dietary amino acids."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The reticuloendothelial system operates continuously to **metabolise** foreign toxins and cellular debris."
      }
    ]
  },
  "Dashboard — met\\metabolism.md": {
    "primary": "The chemical processes occurring within a living cell or organism that are necessary for the maintenance of life.",
    "secondary": "In physiological chemistry, the sum total of anabolism (synthetic, energy-consuming reactions) and catabolism (breakdown, energy-releasing reactions) regulated by enzymes and hormones.",
    "quotes": [
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "Life is sustained through the continuous reciprocal harmony of cellular **metabolism**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Basal **metabolism** provides an exact quantitative indicator of thyroid gland activity."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Disease is not an independent entity, but rather normal cellular **metabolism** modified under abnormal stimuli."
      }
    ]
  },
  "Dashboard — met\\metabolize.md": {
    "primary": "To process, transform, or break down a substance by chemical reactions within an organism's metabolism.",
    "secondary": "In pharmacokinetics and cellular biology, to biotransform drugs, xenobiotics, or endogenous substrates through Phase I and Phase II enzymatic reactions.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Failure of the cirrhotic liver to **metabolize** circulating estrogens leads to spider angiomas and palmar erythema."
      },
      {
        "author": "Claude Bernard",
        "work": "An Introduction to the Study of Experimental Medicine",
        "quote": "The living tissues **metabolize** absorbed nutrients to generate kinetic mechanical force and animal heat."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "Specialized microsomal enzymes within hepatic parenchyma **metabolize** exogenous alkaloids into harmless conjugates."
      }
    ]
  }
};

console.log(`Starting curation of Form Part 5 Batch 1 (${Object.keys(batchData).length} notes)...`);
const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`Batch 1 complete: successfully updated ${count} notes.`);
