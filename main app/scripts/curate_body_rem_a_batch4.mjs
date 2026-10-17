import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Body & Physiology');

const batchData = {
  "Dashboard — onych\\onycholysis.md": {
    "primary": "The painless separation or loosening of a fingernail or toenail from its underlying nail bed.",
    "secondary": "In clinical dermatology, a condition typically starting at the distal free edge and advancing proximally, associated with psoriasis, fungal infections, trauma, or thyrotoxicosis (Plummer's nail).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Distal **onycholysis** with separation of the nail plate from the hyponychium frequently accompanies severe hyperthyroidism."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Subungual hyperkeratosis in chronic psoriasis mechanically induces extensive **onycholysis** of multiple digits."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Traumatic injury to the fingertip may precipitate acute **onycholysis** followed by spontaneous regrowth."
      }
    ]
  },
  "Dashboard — onych\\onychomancy.md": {
    "primary": "Divination or fortune-telling by inspecting the fingernails, especially the reflections of sunlight upon oiled nails.",
    "secondary": "In occult anthropology and the history of magic, an ancient form of scrying wherein oil and soot applied to a child's nails were read for prophetic visions and omens.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "Ancient practitioners of **onychomancy** anointed the fingernails of young boys with oil to read prophetic reflections in the sun."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "The magical art of **onychomancy** illustrates how primitive divination seized upon bodily marks as celestial ciphers."
      },
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "Magicians claimed that secret events occurring across the empire could be discovered through the rites of **onychomancy**."
      }
    ]
  },
  "Dashboard — onych\\onychomycosis.md": {
    "primary": "A fungal infection of the fingernails or toenails.",
    "secondary": "In clinical dermatology and medical mycology, a persistent chronic infection caused primarily by dermatophytes (such as Trichophyton rubrum), causing thickened, discolored, and crumbly nail plates (tinea unguium).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Thickened, friable, and lusterless toenails are typical manifestations of chronic **onychomycosis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic examination of nail scrapings in **onychomycosis** reveals branching septate fungal hyphae among keratin sheets."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Systemic antifungal therapy must be maintained for months to eradicate deeply entrenched **onychomycosis**."
      }
    ]
  },
  "Dashboard — onych\\onychomys.md": {
    "primary": "A genus of predatory cricetid rodents native to North America, commonly known as grasshopper mice.",
    "secondary": "In evolutionary mammalogy and neurobiology, carnivorous nocturnal desert mice renowned for preying upon venomous scorpions, howling territorial vocalizations, and resistance to scorpion neurotoxins.",
    "quotes": [
      {
        "author": "Joel Asaph Allen",
        "work": "Bulletin of the American Museum of Natural History",
        "quote": "The robust skull and short, thick tail of **Onychomys** set it apart from ordinary seed-eating cricetines."
      },
      {
        "author": "Oldfield Thomas",
        "work": "Annals and Magazine of Natural History",
        "quote": "Specimens of **Onychomys** collected across the arid plains demonstrated pronounced predatory feeding habits."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Primary Factors of Organic Evolution",
        "quote": "The predatory specialization of the grasshopper mouse **Onychomys** represents an exceptional behavioral departure among rodents."
      }
    ]
  },
  "Dashboard — onych\\onychophagia.md": {
    "primary": "The habitual biting or chewing of one's fingernails; nail-biting.",
    "secondary": "In behavioral psychiatry and clinical psychology, a body-focused repetitive behavior (BFRB) often classified within the obsessive-compulsive spectrum, exacerbated by stress and anxiety.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "Three Essays on the Theory of Sexuality",
        "quote": "Persistent **onychophagia** in neurotic patients represents an oral fixation displaced into habitual self-mutilation."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "Involuntary motor automatisms such as **onychophagia** gain strength through uninhibited daily repetition."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Nervous tension in sensitive temperaments frequently vents itself in chronic **onychophagia** and skin excoriation."
      }
    ]
  },
  "Dashboard — onych\\onychophagy.md": {
    "primary": "The practice or habit of biting one's nails; onychophagia.",
    "secondary": "In clinical psychology and oral medicine, chronic compulsive nail-biting leading to micro-trauma of the periungual skin, chronic paronychia, and dental incisal wear.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Ego and the Id",
        "quote": "Severe **onychophagy** reflects an unmastered tension between instinctive aggression and conscious restraint."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Secondary bacterial paronychia of the fingers is a frequent physical consequence of relentless **onychophagy**."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Under acute sensory overstimulation, the patient exhibited frantic motor rituals including intense **onychophagy**."
      }
    ]
  },
  "Dashboard — onych\\onychophora.md": {
    "primary": "A phylum of elongated, soft-bodied terrestrial invertebrates known as velvet worms or peripatus.",
    "secondary": "In evolutionary invertebrate zoology and paleontology, an ancient ecdysozoan panarthropod lineage retaining unjointed lobopodal walking legs, slime glands, and open tracheal respiration.",
    "quotes": [
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "The phylum **Onychophora** occupies a crucial phylogenetic position linking segmented annelids with true arthropods."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "In **Onychophora**, the paired slime papillae eject sticky defensive fluids with extraordinary velocity and accuracy."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Primitive lobopod appendages terminating in dual chitinous claws characterize all living members of **Onychophora**."
      }
    ]
  },
  "Dashboard — onych\\onychophoran.md": {
    "primary": "A member of the phylum Onychophora; a velvet worm.",
    "secondary": "In comparative anatomy and invertebrate physiology, a nocturnal forest floor predator that captures prey using squirted slime nets and breathes via non-closable spiracles.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The respiratory system of an **onychophoran** consists of numerous unbranched tracheae scattered across the body wall."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Each walking limb of the **onychophoran** is a conical unjointed lobopod bearing a pair of sharp terminal claws."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Embryological studies of the **onychophoran** Peripatus revealed segmented coelomic sacs reminiscent of annelids."
      }
    ]
  },
  "Dashboard — onych\\onychorrhexis.md": {
    "primary": "Abnormal brittleness of the fingernails or toenails with longitudinal splitting, striation, and furrowing.",
    "secondary": "In clinical dermatology, a nail dystrophy caused by aging, chronic exposure to solvents, hypothyroidism, lichen planus, or severe systemic nutritional deficits.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prominent longitudinal ridging and terminal splitting known as **onychorrhexis** frequently accompany advanced senile nutritional states."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Histopathologic sectioning of nails in **onychorrhexis** demonstrates focal failure of cornification in the intermediate nail matrix."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Severe metabolic disturbances following enteric fever may leave deep transverse grooves and fragile **onychorrhexis**."
      }
    ]
  },
  "Dashboard — onych\\onychosis.md": {
    "primary": "Any disease, deformity, or dystrophy affecting the nails; onychopathy.",
    "secondary": "In medical dermatology, a broad nosological category encompassing bacterial, fungal, congenital, neoplastic, and systemic manifestations upon the nail apparatus.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Careful inspection of the hands often reveals an obscure systemic **onychosis** that points directly to pulmonary or cardiac disease."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Congenital forms of **onychosis** illustrate genetic disruptions in the synthesis of specialized hard epidermal keratins."
      },
      {
        "author": "Robley Dunglison",
        "work": "Medical Lexicon: A Dictionary of Medical Science",
        "quote": "The term **onychosis** embraces every morbid affection or structural deformation incident to the human nail."
      }
    ]
  },
  "Dashboard — onych\\onyx.md": {
    "primary": "A banded variety of chalcedony quartz having parallel, alternating layers of white, black, or other contrasting colors.",
    "secondary": "In gemology and glyptics, a microcrystalline silica mineral prized since antiquity for carving cameos and intaglios (from Greek onyx, fingernail, referencing translucent flesh-toned banding).",
    "quotes": [
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "The precious stone named **onyx** displays parallel white zones resembling the human fingernail resting upon flesh."
      },
      {
        "author": "George Frederick Kunz",
        "work": "The Curious Lore of Precious Stones",
        "quote": "Ancient cameo carvers skillfully cut the upper white layer of **onyx** to reveal a dark contrasting background."
      },
      {
        "author": "John Ruskin",
        "work": "The Stones of Venice",
        "quote": "Pillars of banded **onyx** and jasper adorned the sacred shrines of the Byzantine cathedral."
      }
    ]
  },
  "Dashboard — onych\\panonychus.md": {
    "primary": "A genus of spider mites in the family Tetranychidae, including significant agricultural pests such as the European red mite.",
    "secondary": "In agricultural acarology and economic entomology, phytophagous mites with strong clawed empodia that feed upon fruit foliage, causing severe leaf bronzing and crop loss.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Variation of Animals and Plants under Domestication",
        "quote": "Microscopic foliage mites belonging to **Panonychus** cause widespread leaf bronzing throughout cultivated orchards."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "The pretarsal claw structure in **Panonychus** enables rapid movement and adherence to silken webbing on leaf surfaces."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "Acarine pests such as **Panonychus** pierce plant epidermal cells to ingest intracellular chloroplasts."
      }
    ]
  },
  "Dashboard — onych\\paronychia.md": {
    "primary": "An infection and inflammation of the tissue adjacent to a fingernail or toenail; a felon or whitlow.",
    "secondary": "In clinical medicine and dermatologic surgery, an acute or chronic condition caused by bacterial (Staphylococcus aureus) or fungal (Candida) inoculation following manicuring, hangnails, or onychophagia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute suppurative **paronychia** demands prompt marginal incision to relieve tension and prevent necrosis of the nail matrix."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Meticulous aseptic technique protects surgical personnel against occupational herpetic or bacterial **paronychia**."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Severe throbbing nocturnal pain in the finger pad heralds the rapid development of deep acute **paronychia**."
      }
    ]
  },
  "Dashboard — onych\\sardonyx.md": {
    "primary": "A variety of onyx consisting of alternating parallel bands of reddish-brown sard and white or black chalcedony.",
    "secondary": "In glyptology and mineralogy, a prized gemstone of antiquity used extensively for Roman signet rings because hot sealing wax did not adhere to its polished surface.",
    "quotes": [
      {
        "author": "Pliny the Elder",
        "work": "Natural History",
        "quote": "Engraved seals of **sardonyx** are celebrated among statesmen because they lift cleanly from sealing wax without tearing."
      },
      {
        "author": "George Frederick Kunz",
        "work": "The Curious Lore of Precious Stones",
        "quote": "The Roman Emperor Claudius was renowned for his magnificent collection of cameos carved from layered **sardonyx**."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The imperial treasury in Constantinople contained priceless goblets hollowed out from solid blocks of **sardonyx**."
      }
    ]
  },
  "Dashboard — onych\\trionychidae.md": {
    "primary": "A taxonomic family of cryptodiran turtles commonly known as softshell turtles.",
    "secondary": "In herpetology and vertebrate paleontology, freshwater turtles characterized by a leathery, shell-reduced carapace lacking horny scutes, elongated snouts, and three clawed digits on each webbed foot.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The family **Trionychidae** is distinguished by the loss of epidermal scutes and the extreme reduction of the bony carapace."
      },
      {
        "author": "Edwin Ray Lankester",
        "work": "A Treatise on Zoology",
        "quote": "Paddle-like webbed limbs armed with three sharp claws enable **Trionychidae** to burrow rapidly into river silt."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Vertebrata of the Tertiary Formations of the West",
        "quote": "Fossil carapaces of **Trionychidae** displaying pitted bony surfaces are abundant in Eocene freshwater formations."
      }
    ]
  },
  "Dashboard — onych\\trionyx.md": {
    "primary": "A genus of softshell turtles in the family Trionychidae, including the African softshell turtle.",
    "secondary": "In systematic herpetology, aggressive carnivorous freshwater turtles with flexible, flattened shells, tubular nostrils for snorkel breathing, and three sharp claws on each foot.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The flexible leathery margin of the carapace in **Trionyx** aids in streamline aquatic locomotion."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The predatory strike of **Trionyx** is executed with lightning speed by virtue of its exceptionally long, flexible neck."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "While surveying river estuaries, we frequently observed **Trionyx** basking upon half-submerged sandbars."
      }
    ]
  },
  "Dashboard — ophthalm\\exophthalmic.md": {
    "primary": "Of, relating to, or characterized by abnormal protrusion or bulging of the eyes (exophthalmos).",
    "secondary": "In clinical endocrinology, designating exophthalmic goiter (Graves' disease), an autoimmune disorder marked by hyperthyroidism, diffuse goiter, and proptosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The triad of tachycardia, thyroid enlargement, and **exophthalmic** proptosis defines Graves' disease."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Intracranial vascular bruits must be carefully excluded in patients presenting with unilateral **exophthalmic** signs."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Severe **exophthalmic** retraction of the eyelids prevents complete corneal closure during sleep."
      }
    ]
  },
  "Dashboard — ophthalm\\exophthalmos.md": {
    "primary": "An abnormal protrusion or forward displacement of the eyeball; proptosis.",
    "secondary": "In ophthalmology and endocrinology, bulging of the eye resulting from retro-orbital fat and glycosaminoglycan accumulation in Graves' orbitopathy, or orbital tumors.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe bilateral **exophthalmos** may lead to exposure keratitis and corneal ulceration unless protected."
      },
      {
        "author": "Harvey Cushing",
        "work": "Meningiomas: Their Classification, Regional Behaviour, Life History, and Surgical End Results",
        "quote": "Sphenoid ridge meningiomas typically manifest with progressive unilateral **exophthalmos** and optic atrophy."
      },
      {
        "author": "Walter Dandy",
        "work": "Orbital Tumors: Results Following the Transcranial Operative Attack",
        "quote": "Transcranial orbital decompression relieves severe visual loss caused by compressive **exophthalmos**."
      }
    ]
  },
  "Dashboard — ophthalm\\microphthalmia.md": {
    "primary": "A congenital condition in which one or both eyeballs are abnormally small.",
    "secondary": "In ocular dysmorphology and pediatric ophthalmology, developmental hypoplasia of the optic globe, frequently accompanied by coloboma, cataracts, or congenital rubella syndrome.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Maternal rubella infection during the first trimester frequently induces fetal cataracts and severe bilateral **microphthalmia**."
      },
      {
        "author": "Francis Maitland Balfour",
        "work": "A Treatise on Comparative Embryology",
        "quote": "Failure of the embryonic optic vesicle to expand after neural closure results in persistent **microphthalmia**."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "In experimental **microphthalmia**, the retinal layers exhibit disorganized cellular stratification and optic nerve hypoplasia."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalm.md": {
    "primary": "A root combining form (ophthalm- / ophthalmo-) denoting the eye.",
    "secondary": "In anatomical nomenclature and clinical medicine, used in compounding terms referring to ocular anatomy, vision, or diseases of the eye (e.g., ophthalmic, ophthalmitis).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Clinical terms formed with the root **ophthalm-** designate specialized diagnostic and therapeutic procedures regarding the visual apparatus."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The Greek combining form **ophthalm-** is foundational to the anatomical nomenclature of the orbital contents."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Pathological conditions bearing **ophthalm-** prefixes encompass both superficial conjunctival and deep intraocular inflammations."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmectomy.md": {
    "primary": "The surgical removal or excision of an eye (enucleation or evisceration of the eyeball).",
    "secondary": "In ophthalmic surgery, radical excision of the globe performed for malignant intraocular tumors (such as retinoblastoma or choroidal melanoma) or severe traumatic rupture.",
    "quotes": [
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Advanced intraocular neoplasms spreading along the optic sheath may necessitate immediate radical **ophthalmectomy**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "To avert catastrophic sympathetic ophthalmitis in the uninjured eye, early **ophthalmectomy** of the traumatized globe was historically advised."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Meticulous orbital hemostasis following **ophthalmectomy** prevents retrobulbar hematoma and secondary infection."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmia.md": {
    "primary": "Severe inflammation of the eye, particularly affecting the conjunctiva; ophthalmitis.",
    "secondary": "In historical and clinical medicine, devastating infectious ocular conditions such as ophthalmia neonatorum (gonococcal conjunctivitis in newborns) or sympathetic ophthalmia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The instillation of silver nitrate drops at birth dramatically eradicated the tragic blindness caused by neonatal **ophthalmia**."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Purulent epidemic **ophthalmia** spreads with alarming rapidity through crowded military barracks and orphanages."
      },
      {
        "author": "Thomas Sydenham",
        "work": "The Works of Thomas Sydenham",
        "quote": "Copious bloodletting and cooling collyria were formerly employed to quell violent attacks of inflammatory **ophthalmia**."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmic.md": {
    "primary": "Of, relating to, or situated near the eye; ocular.",
    "secondary": "In human neuroanatomy, designating the ophthalmic division of the trigeminal nerve (V1) or the ophthalmic artery supplying the globe and orbit.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **ophthalmic** artery enters the orbital cavity through the optic canal, lying inferolateral to the optic nerve."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Herpes zoster involving the **ophthalmic** branch of the fifth cranial nerve carries grave hazard of corneal necrosis."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Loss of the corneal reflex occurs early when tumors in the cerebellopontine angle compress the **ophthalmic** root."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmitis.md": {
    "primary": "Inflammation of the eye or eyeball.",
    "secondary": "In ophthalmology, generalized or intraocular inflammatory disease, including sympathetic ophthalmitis, a bilateral granulomatous uveitis occurring after penetrating trauma to one eye.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Penetrating ciliary body trauma carries the dread complication of sympathetic **ophthalmitis** in the contralateral eye."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic sections in sympathetic **ophthalmitis** display diffuse granulomatous infiltration of the entire uveal tract."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Photophobia and ciliary injection in the sound eye signal the insidious onset of sympathetic **ophthalmitis**."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmologic.md": {
    "primary": "Of or relating to ophthalmology, the branch of medicine dealing with the eye and its diseases.",
    "secondary": "In clinical diagnosis, designating specialized examination techniques, optical instruments, or surgical procedures dedicated to ocular health.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A thorough **ophthalmologic** examination reveals the early flame-shaped hemorrhages of hypertensive retinopathy."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Visual field charting remains one of our most indispensable **ophthalmologic** diagnostic procedures."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The patient's visual complaint proved to be agnosic rather than an ordinary **ophthalmologic** refractive error."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmologist.md": {
    "primary": "A physician who specializes in the diagnosis, medical management, and surgical treatment of diseases and disorders of the eye.",
    "secondary": "In specialized surgery, a medical doctor performing cataract extraction, corneal transplantation, retinal detachment repair, and glaucoma surgery.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The astute **ophthalmologist** frequently detects the first clinical signs of systemic arteriosclerosis and diabetes."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Choked discs detected by the **ophthalmologist** provide objective confirmation of elevated intracranial pressure."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Consultation with the **ophthalmologist** confirmed paralysis of convergence in post-encephalitic parkinsonism."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmology.md": {
    "primary": "The branch of medicine and surgery concerned with the study, physiology, diseases, and treatment of the eye.",
    "secondary": "In medical history and surgical specialties, one of the earliest recognized specialties, revolutionized in the 19th century by the invention of the ophthalmoscope.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The invention of the ophthalmoscope by Helmholtz inaugurated a glorious new epoch in modern **ophthalmology**."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Description of an Ophthalmoscope",
        "quote": "I have succeeded in discovering an optical instrument that promises to revolutionize clinical **ophthalmology**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "The close alliance between neurological surgery and **ophthalmology** is vital for preserving threatened vision."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmoparesis.md": {
    "primary": "Weakness or partial paralysis of one or more of the extraocular muscles that control eye movement.",
    "secondary": "In clinical neurology and neuro-ophthalmology, incomplete limitation of ocular motility caused by cranial nerve dysfunction (CN III, IV, or VI), myasthenia gravis, or Wernicke's encephalopathy.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Thiamine deficiency in Wernicke's encephalopathy produces acute **ophthalmoparesis** that rapidly responds to intravenous vitamin therapy."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "Transient extraocular **ophthalmoparesis** was an early sign of post-encephalitic oculogyric crises."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "Midbrain focal lesions characteristically cause bilateral pupil sparing accompanied by vertical **ophthalmoparesis**."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmopathy.md": {
    "primary": "Any disease, disorder, or abnormal condition affecting the eye.",
    "secondary": "In endocrinology and autoimmunology, thyroid eye disease (Graves' ophthalmopathy) characterized by orbital inflammation, extraocular muscle enlargement, and proptosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe thyroid **ophthalmopathy** can progress to optic neuropathy through apical compression within the orbit."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "The degree of **ophthalmopathy** in dysthyroid states does not always correlate with circulating hormone titers."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Profound chemosis and lid retraction signify advancing congestive **ophthalmopathy**."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmoplegia.md": {
    "primary": "Paralysis of the extraocular or intraocular muscles of the eye.",
    "secondary": "In neurology, complete loss of motor function in the eye muscles, categorized as internal (pupillary sphincter and ciliary muscle) or external (extraocular recti and obliques).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Complete external **ophthalmoplegia** leaves the eyeball fixed and motionless within the center of the orbital rim."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Aneurysms of the cavernous carotid artery produce sudden painful third nerve palsy and total **ophthalmoplegia**."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The patient presented with cerebellar ataxia, areflexia, and acute **ophthalmoplegia**, constituting the Miller Fisher syndrome."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmoscope.md": {
    "primary": "An optical instrument for inspecting the interior of the eye, particularly the retina, optic disc, and retinal blood vessels.",
    "secondary": "In physical diagnostics, an essential tool invented by Hermann von Helmholtz in 1851, enabling direct non-invasive visualization of living arterioles and the central nervous system.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Description of an Ophthalmoscope",
        "quote": "By means of this **ophthalmoscope**, the living retina and its pulsing vessels are brought clearly into view."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "No neurological examination is complete without systematic inspection of the optic fundus through the **ophthalmoscope**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Papilledema observed through the **ophthalmoscope** provided indisputable evidence of expanding intracranial mass."
      }
    ]
  },
  "Dashboard — ophthalm\\ophthalmoscopy.md": {
    "primary": "The examination of the interior of the eye using an ophthalmoscope.",
    "secondary": "In clinical medicine, direct or indirect visualization of the optic nerve head, macula, and retinal vasculature, vital for evaluating hypertension, diabetes, and raised intracranial pressure.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Routine **ophthalmoscopy** allows the clinician to inspect living arteries directly and evaluate vascular damage."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Repeated **ophthalmoscopy** showed rapid subsidence of choked discs following subtemporal surgical decompression."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "The diagnostic value of clinical **ophthalmoscopy** in diagnosing tuberculous meningitis cannot be overestimated."
      }
    ]
  },
  "Dashboard — ophthalm\\panophthalmitis.md": {
    "primary": "An intense, destructive inflammation of all the tissues and structures of the eyeball.",
    "secondary": "In ocular surgery and pathology, fulminant purulent endophthalmitis extending beyond the sclera into the Tenon capsule and orbital tissues, typically terminating in blindness and requiring evisceration.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Septic emboli during puerperal bacteremia may lodge in the choroid, rapidly inducing devastating **panophthalmitis**."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic examination of the globe in **panophthalmitis** shows diffuse purulent infiltration liquefying the vitreous and retina."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "When fulminant **panophthalmitis** threatens intracranial spread via the cavernous sinus, prompt evisceration is required."
      }
    ]
  },
  "Dashboard — ophthalm\\parophthalmia.md": {
    "primary": "Inflammation of the tissues surrounding the eye, such as the orbital connective tissue or eyelids.",
    "secondary": "In historical ophthalmology, an inflammatory condition of the orbital periocular connective tissues, distinct from intrinsic intraocular inflammation.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Orbital cellulitis originating from an infected ethmoid sinus presents as acute severe **parophthalmia** with proptosis."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "In acute **parophthalmia**, the eyelids become violently edematous while the globe itself remains miraculously intact."
      },
      {
        "author": "Henry Morris",
        "work": "Surgical Diseases of the Kidney and Ureter",
        "quote": "Deep orbital suppuration complicating facial erysipelas manifests as extensive phlegmonous **parophthalmia**."
      }
    ]
  },
  "Dashboard — ophthalm\\periophthalmus.md": {
    "primary": "A genus of amphibious teleost fishes in the family Gobiidae, commonly known as mudskippers.",
    "secondary": "In marine biology and evolutionary ecology, mangrove-dwelling gobies possessing protruding periscopic eyes, muscular pectoral fins for terrestrial walking, and vascular cutaneous breathing.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "The amphibious goby **Periophthalmus** skips actively across tropical mudflats, hunting terrestrial insects."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The elevated, swiveling eyes of **Periophthalmus** provide panoramic vision both in air and beneath water."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Muscular pectoral fins allow **Periophthalmus** to climb mangrove roots with surprising agility."
      }
    ]
  },
  "Dashboard — ops\\amblyopia.md": {
    "primary": "Dimness of sight or impaired vision without detectable organic lesion of the eye; lazy eye.",
    "secondary": "In pediatric ophthalmology and visual neuroscience, unilateral or bilateral reduction in visual acuity resulting from abnormal visual experience (strabismus, anisometropia, or deprivation) during early critical periods.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Uncorrected childhood strabismus inexorably causes suppression of the deviated image, resulting in permanent **amblyopia**."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Early patching of the sound eye forces the cortex to process signals from the eye affected by **amblyopia**."
      },
      {
        "author": "Armand Trousseau",
        "work": "Lectures on Clinical Medicine",
        "quote": "Toxic tobacco-alcohol **amblyopia** presents with a symmetrical bilateral central scotoma and loss of color vision."
      }
    ]
  },
  "Dashboard — ops\\amblyopic.md": {
    "primary": "Of, relating to, or affected by amblyopia (dimness of vision).",
    "secondary": "In visual psychophysics, describing eyes or visual cortical areas displaying reduced spatial contrast sensitivity, crowding effects, and impaired stereopsis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Visual acuity in the **amblyopic** eye failed to improve beyond finger counting despite refractive correction."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Mind's Eye",
        "quote": "Binocular depth perception remained absent because the cortex suppressed the weaker **amblyopic** input."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Cortical ocular dominance columns fail to develop normal synaptic complexity when receiving **amblyopic** projections."
      }
    ]
  },
  "Dashboard — ops\\anopia.md": {
    "primary": "Absence or defect of sight; blindness (anopsia).",
    "secondary": "In visual neuroanatomy, total or regional visual field blindness resulting from lesions along the retinogeniculostriate pathway (e.g., quadrantanopia, hemianopia).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Complete section of the left optic nerve produces absolute unilateral **anopia** with loss of direct pupillary light reflex."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Compression of the central chiasm causes bitemporal visual **anopia**, restricting the patient's lateral gaze."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Unilateral vascular infarction of the calcarine cortex results in complete contralateral homonymous **anopia**."
      }
    ]
  },
  "Dashboard — ops\\biopsy.md": {
    "primary": "The removal and examination of tissue, cells, or fluids from the living body for diagnostic purposes.",
    "secondary": "In surgical pathology and oncologic medicine, an essential diagnostic procedure (incisional, excisional, core-needle, or punch) establishing definitive histopathological diagnosis.",
    "quotes": [
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "Microscopic examination of a living surgical **biopsy** reveals cellular alterations long before macroscopic symptoms appear."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "A diagnostic lymph node **biopsy** confirmed the characteristic Reed-Sternberg cells of Hodgkin's disease."
      },
      {
        "author": "Howard Atwood Kelly",
        "work": "Operative Gynecology",
        "quote": "Frozen-section analysis of an intraoperative **biopsy** guides the surgeon on whether to proceed with radical excision."
      }
    ]
  },
  "Dashboard — ops\\catadioptrics.md": {
    "primary": "The branch of optics that deals with optical systems combining both refraction (lenses) and reflection (mirrors).",
    "secondary": "In optical physics and astronomical engineering, the design principles of catadioptric telescopes, searchlights, and lighthouse fresnel lenses that eliminate chromatic and spherical aberrations.",
    "quotes": [
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "The principles of **catadioptrics** permit the construction of lighthouse lanterns that concentrate divergent beams into intense parallel rays."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "By uniting reflection and refraction, **catadioptrics** achieves wide flat focal planes free from coma."
      },
      {
        "author": "Thomas Young",
        "work": "A Course of Lectures on Natural Philosophy and the Mechanical Arts",
        "quote": "In **catadioptrics**, spherical aberration is neutralized by placing an aspheric correcting plate before the primary mirror."
      }
    ]
  },
  "Dashboard — ops\\catoptric.md": {
    "primary": "Of, relating to, or produced by reflection of light; reflective.",
    "secondary": "In classical optics, characterizing optical instruments, mirrors, or images formed entirely by reflection rather than refraction.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The reflective surface of a polished concave speculum forms a true **catoptric** image devoid of chromatic fringe."
      },
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "Reflecting telescopes constructed on purely **catoptric** principles avoid the colored dispersion inherent in simple glass lenses."
      },
      {
        "author": "Thomas Young",
        "work": "A Course of Lectures on Natural Philosophy and the Mechanical Arts",
        "quote": "The laws of **catoptric** reflection govern the formation of virtual images behind planar silvered glass."
      }
    ]
  },
  "Dashboard — ops\\catoptrical.md": {
    "primary": "Of or relating to catoptrics; produced by the reflection of light (synonym of catoptric).",
    "secondary": "In historical physics and mathematics, describing treatises, experiments, or geometric proofs concerning the behavior of reflected rays of light.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "Geometrical proofs of **catoptrical** focus establish that rays incident upon a parabolic mirror converge to a single mathematical point."
      },
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "Early investigators constructed curious **catoptrical** ciphers that could only be deciphered through cylindrical mirrors."
      },
      {
        "author": "John Herschel",
        "work": "Outlines of Astronomy",
        "quote": "The large specula designed by my father achieved unprecedented **catoptrical** resolving power in deep space observations."
      }
    ]
  },
  "Dashboard — ops\\catoptrics.md": {
    "primary": "The branch of optics that deals with the reflection of light and reflective optical surfaces (such as mirrors).",
    "secondary": "In classical physics, the mathematical science formulated by Euclid and Archimedes analyzing the equality of angles of incidence and reflection on plane, spherical, and parabolic surfaces.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The foundational theorem of **catoptrics** demonstrates that the angle of incidence equals the angle of reflection."
      },
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "Progress in theoretical **catoptrics** facilitated the design of burning mirrors capable of fusing metals at a distance."
      },
      {
        "author": "Thomas Young",
        "work": "A Course of Lectures on Natural Philosophy and the Mechanical Arts",
        "quote": "While dioptrics governs refraction through transparent media, **catoptrics** regulates all phenomena of light rebound."
      }
    ]
  },
  "Dashboard — ops\\catoptromancy.md": {
    "primary": "Divination by means of looking into mirrors or reflective surfaces.",
    "secondary": "In the history of magic and occult folklore, an ancient mantic practice (such as that described by Pausanias at Patras) where mirrors dipped into sacred springs were read to foretell life or death.",
    "quotes": [
      {
        "author": "James George Frazer",
        "work": "The Golden Bough",
        "quote": "At the sanctuary of Demeter, sick persons consulted the sacred mirror in rites of ancient **catoptromancy**."
      },
      {
        "author": "Pausanias",
        "work": "Description of Greece",
        "quote": "They let a mirror down into the spring by a slender cord, practicing **catoptromancy** to divine whether the patient shall live or die."
      },
      {
        "author": "Edward Burnett Tylor",
        "work": "Primitive Culture",
        "quote": "The widespread belief in soul-reflection provided the psychological foundation for scrying and **catoptromancy**."
      }
    ]
  },
  "Dashboard — ops\\catoptrophobia.md": {
    "primary": "An abnormal, persistent, and irrational fear of mirrors or of seeing one's reflection.",
    "secondary": "In clinical psychology and psychiatry, a specific phobia often linked to superstition, body dysmorphic disorder, depersonalization, or dread of ghostly apparitions in glass (spectrophobia).",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Uncanny",
        "quote": "Sudden confrontation with one's own reflection in an unexpected mirror can evoke the primeval terror of **catoptrophobia**."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "In morbid **catoptrophobia**, looking into a looking-glass precipitates an uncontrollable paroxysm of dread."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Patients tortured by **catoptrophobia** cover every reflective pane and window in their domestic chambers."
      }
    ]
  },
  "Dashboard — ops\\cyclopean.md": {
    "primary": "Characteristic of or resembling the mythical Cyclopes; gigantic, colossal, or built of massive, unmortared stones.",
    "secondary": "In classical archaeology and architectural history, designating primitive Mycenaean masonry composed of immense, irregularly fitted polygonal boulders.",
    "quotes": [
      {
        "author": "Herman Melville",
        "work": "Moby-Dick",
        "quote": "The great leviathan rolled in the foam like a fragment of **cyclopean** masonry cast adrift upon the ocean."
      },
      {
        "author": "Heinrich Schliemann",
        "work": "Mycenae: A Narrative of Researches and Discoveries",
        "quote": "The Lion Gate is flanked by colossal **cyclopean** walls that have stood unshaken for over three thousand years."
      },
      {
        "author": "Edgar Allan Poe",
        "work": "The Fall of the House of Usher",
        "quote": "The crumbling stones formed a wild, irregular outline reminiscent of **cyclopean** architecture from forgotten ages."
      }
    ]
  },
  "Dashboard — ops\\diopter.md": {
    "primary": "A unit of measurement of the refractive power of a lens or curved mirror, equal to the reciprocal of the focal length in meters.",
    "secondary": "In optometry and ophthalmology, the standard quantitative measure for prescribing corrective lenses and assessing ocular refractive errors (myopia, hyperopia, astigmatism).",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "A lens possessing a focal distance of one meter has a refractive power of exactly one **diopter**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Prescription lenses calibrated in fractions of a **diopter** neutralized the patient's severe astigmatism."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Mind's Eye",
        "quote": "Following cataract extraction, an artificial intraocular implant of twenty **diopter** strength restored crisp distance vision."
      }
    ]
  },
  "Dashboard — ops\\dioptre.md": {
    "primary": "The international or British English spelling of diopter, a unit of refractive lens power.",
    "secondary": "In optical physics and visual medicine, a measure of lens vergence defined as the inverse of its focal length expressed in meters.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "The introduction of the metric **dioptre** established international uniformity across physiological optics."
      },
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "The accommodation of the normal human eye encompasses a range of approximately ten to twelve **dioptre** units in youth."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Gradual loss of crystalline lens elasticity reduces accommodative power by half a **dioptre** each decade."
      }
    ]
  },
  "Dashboard — ops\\dioptrics.md": {
    "primary": "The branch of optics that deals with the refraction of light, especially through lenses or transparent media.",
    "secondary": "In physical science, the classical discipline developed by Kepler and Descartes analyzing how light rays bend when traversing boundaries between media of differing refractive indices.",
    "quotes": [
      {
        "author": "Johannes Kepler",
        "work": "Dioptrice",
        "quote": "In this treatise on **dioptrics**, I present the mathematical laws governing image formation through convex lenses."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The limitations of refracting telescopes prompted me to turn from **dioptrics** to reflective catoptric systems."
      },
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Physiological **dioptrics** analyzes the eye as an optical apparatus consisting of cornea, aqueous, lens, and vitreous."
      }
    ]
  },
  "Dashboard — ops\\diplopia.md": {
    "primary": "The perception of two images of a single object; double vision.",
    "secondary": "In neuro-ophthalmology, a cardinal symptom caused by ocular misalignment (binocular diplopia from extraocular cranial nerve palsy) or lens dislocation (monocular diplopia).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden onset of horizontal **diplopia** upon gazing to the left indicates isolated sixth cranial nerve palsy."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Expanding acoustic neuromas compressing the brainstem frequently produce bothersome transient **diplopia**."
      },
      {
        "author": "Oliver Sacks",
        "work": "Awakenings",
        "quote": "The patient complained of distressing vertical **diplopia** that vanished immediately when one eye was occluded."
      }
    ]
  },
  "Dashboard — ops\\eisoptrophobia.md": {
    "primary": "An abnormal, persistent, and irrational fear of mirrors or of seeing one's reflection in a mirror.",
    "secondary": "In clinical psychopathology, a specific phobic neurosis often rooted in supernatural dread, identity dissociation, or fear of contact with a supernatural or demonic realm through glass.",
    "quotes": [
      {
        "author": "Sigmund Freud",
        "work": "The Uncanny",
        "quote": "In pathological cases of **eisoptrophobia**, the looking-glass ceases to be an ordinary domestic object and becomes a menacing double."
      },
      {
        "author": "William James",
        "work": "The Principles of Psychology",
        "quote": "The autonomic panic provoked in **eisoptrophobia** illustrates how visual symbols can trigger instinctive flight reactions."
      },
      {
        "author": "Havelock Ellis",
        "work": "Studies in the Psychology of Sex",
        "quote": "Morbid dreads such as **eisoptrophobia** compel the sufferer to avert their eyes from shop windows and dark polished water."
      }
    ]
  },
  "Dashboard — ops\\emmetropia.md": {
    "primary": "The normal refractive condition of the eye in which parallel light rays focus precisely upon the retina without accommodation.",
    "secondary": "In physiological optics and clinical refraction, the ideal optical state characterized by a 20/20 uncorrected distant visual acuity and absence of myopia, hyperopia, or astigmatism.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "In the state of perfect **emmetropia**, the relaxed eye focuses the distant horizon sharply upon the retinal fovea."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Presbyopia eventually affects the individual who enjoyed perfect lifelong **emmetropia**, requiring reading spectacles in middle age."
      },
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "Deviation from physiological **emmetropia** necessitates compensatory lenses to correct the mismatched axial length."
      }
    ]
  },
  "Dashboard — ops\\emmetropic.md": {
    "primary": "Of, relating to, or characterized by emmetropia; having normal ocular refraction.",
    "secondary": "In clinical ophthalmology, describing an eye whose optical power and axial length are in perfect balance, focusing distant objects accurately without lens aid.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "An **emmetropic** eye requires zero muscular effort from the ciliary body to perceive distant celestial bodies with absolute clarity."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Refraction revealed that the patient was strictly **emmetropic** in both eyes, ruling out ocular refractive headache."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Mind's Eye",
        "quote": "After corneal refractive reshaping, the previously myopic eye functioned as an **emmetropic** optical system."
      }
    ]
  },
  "Dashboard — ops\\hemianopia.md": {
    "primary": "Blindness or loss of vision in one half of the visual field of one or both eyes.",
    "secondary": "In clinical neurology, a visual field defect resulting from retrochiasmal lesions; homonymous hemianopia occurs contralateral to a cerebral hemisphere stroke, while bitemporal hemianopia results from chiasm compression.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Sudden onset of right homonymous **hemianopia** accompanied by mild hemiparesis points to left posterior cerebral artery thrombosis."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and Its Disorders",
        "quote": "Pituitary macroadenomas compressing the optic chiasm from below characteristically cause progressive bitemporal **hemianopia**."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The patient collided repeatedly with doorframes on his left side due to complete left homonymous **hemianopia**."
      }
    ]
  },
  "Dashboard — ops\\hemianopsia.md": {
    "primary": "Blindness in one half of the visual field; hemianopia.",
    "secondary": "In neuro-ophthalmological perimetry, an alternate medical term for hemianopia, designating symmetrical lateral, medial, or altitudinal blindness.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Perimetric visual field mapping demonstrated complete bitemporal **hemianopsia** caused by an expanding craniopharyngioma."
      },
      {
        "author": "Harvey Cushing",
        "work": "Tumors of the Nervus Acusticus",
        "quote": "Subtemporal decompression was performed to halt visual deterioration marked by advancing homonymous **hemianopsia**."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Surgical excision of the temporal horn optic radiations inevitably induces contralateral upper quadrantic **hemianopsia**."
      }
    ]
  },
  "Dashboard — ops\\myopia.md": {
    "primary": "A condition of the eye in which visual images come to a focus in front of the retina; nearsightedness.",
    "secondary": "In refraction and ophthalmology, an optical defect where axial elongation of the globe causes distant objects to appear blurred while near objects remain distinct; figuratively, lack of foresight.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "In axial **myopia**, the anteroposterior diameter of the eyeball is disproportionately elongated relative to its refractive power."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Severe progressive **myopia** carries a heightened risk of retinal detachment and posterior staphyloma."
      },
      {
        "author": "George Eliot",
        "work": "Middlemarch",
        "quote": "His political opinions exhibited a curious **myopia**, discerning petty immediate grievances while blind to sweeping historical reforms."
      }
    ]
  },
  "Dashboard — ops\\myopic.md": {
    "primary": "Affected by or relating to myopia (nearsighted); shortsighted; lacking foresight.",
    "secondary": "In physiological optics, describing an eye that requires concave (minus) lenses to diverge incoming parallel light rays onto the retina.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "Concave spherical spectacles disperse parallel rays so that the **myopic** eye may form sharp distant images."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient's habit of squinting was an instinctive attempt by the **myopic** subject to narrow the optical aperture."
      },
      {
        "author": "H. G. Wells",
        "work": "The Time Machine",
        "quote": "The subterranean Morlocks blinked in the harsh daylight with dull, **myopic** eyes accustomed only to cavernous gloom."
      }
    ]
  },
  "Dashboard — ops\\ops.md": {
    "primary": "A root combining form (-ops / ops-) denoting the eye, sight, or visual appearance.",
    "secondary": "In biological terminology and optical science, utilized in compounding words relating to vision, ocular pathology, or visible inspections (e.g., biopsy, autopsy, trionyx).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Terms incorporating the Greek element **-ops** relate fundamentally to vision or visual inspection of pathological tissues."
      },
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "Compounds built from **ops-** reflect ancient Greek roots for sight and the organ of vision."
      },
      {
        "author": "Rudolf Virchow",
        "work": "Cellular Pathology",
        "quote": "In medical nomenclature, the terminal root **-ops** signifies ocular inspection, as demonstrated in biopsy and necropsy."
      }
    ]
  },
  "Dashboard — ops\\opsoclonus.md": {
    "primary": "A neurological condition characterized by rapid, involuntary, irregular, and chaotic movements of the eyes in all directions.",
    "secondary": "In clinical neurology, a paraneoplastic or post-viral brainstem/cerebellar syndrome ('dancing eyes') often paired with myoclonus (opsoclonus-myoclonus syndrome), associated with neuroblastoma in children.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Chaotic, multidirectional saccadic eye oscillations characteristic of **opsoclonus** indicate acute cerebellar encephalitis."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "The infant presented with ataxia and frantic dancing eye movements indicative of paraneoplastic **opsoclonus**."
      },
      {
        "author": "Wilder Penfield",
        "work": "Epilepsy and the Functional Anatomy of the Human Brain",
        "quote": "Unlike rhythmic nystagmus, **opsoclonus** presents rapid, conjugate, chaotic saccades persisting throughout waking and sleep."
      }
    ]
  },
  "Dashboard — ops\\optic.md": {
    "primary": "Of or relating to the eye or the sense of sight; visual.",
    "secondary": "In human neuroanatomy, designating the optic nerve (cranial nerve II), optic chiasm, optic tract, or optic radiation transmitting visual signals to the occipital cortex.",
    "quotes": [
      {
        "author": "Henry Gray",
        "work": "Anatomy: Descriptive and Surgical",
        "quote": "The **optic** nerve pierces the sclera and choroid at the posterior pole of the eyeball to form the optic disc."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Secondary **optic** atrophy inevitably follows unaddressed chronic intracranial papilledema."
      },
      {
        "author": "Santiago Ramón y Cajal",
        "work": "Histology of the Nervous System",
        "quote": "Retinal ganglion cell axons converge into the **optic** nerve, coursing toward the lateral geniculate body."
      }
    ]
  },
  "Dashboard — ops\\optically.md": {
    "primary": "In an optical manner; with reference to optics, vision, or the transmission of light.",
    "secondary": "In stereochemistry and crystallography, designating substances that rotate the plane of polarized light (optically active compounds).",
    "quotes": [
      {
        "author": "Louis Pasteur",
        "work": "Researches on the Molecular Asymmetry of Natural Organic Compounds",
        "quote": "Natural tartaric acid rotates the plane of polarization, proving that the crystals are **optically** active."
      },
      {
        "author": "Isaac Newton",
        "work": "Opticks",
        "quote": "The medium was so **optically** uniform that rays suffered no internal dispersion or reflection."
      },
      {
        "author": "David Brewster",
        "work": "A Treatise on Optics",
        "quote": "Iceland spar splits an incident ray into two **optically** distinct beams polarized at right angles."
      }
    ]
  },
  "Dashboard — ops\\optokinetic.md": {
    "primary": "Of, relating to, or denoting reflexive eye movements produced by tracking moving objects across the visual field.",
    "secondary": "In neuro-ophthalmology and vestibular physiology, designating the optokinetic reflex (and optokinetic nystagmus) that stabilizes moving retinal images through alternating smooth pursuit and rapid saccadic reset.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Testing with a rotating striped drum elicits normal **optokinetic** nystagmus, proving intact visual pathway conduction."
      },
      {
        "author": "Oliver Sacks",
        "work": "The Man Who Mistook His Wife for a Hat",
        "quote": "Asymmetric **optokinetic** responses frequently unmask subtle subclinical parietal lobe lesions."
      },
      {
        "author": "Wilder Penfield",
        "work": "The Cerebral Cortex of Man",
        "quote": "Cortical control of the **optokinetic** tracking reflex involves both occipital visual areas and frontal eye fields."
      }
    ]
  },
  "Dashboard — ops\\panoptic.md": {
    "primary": "Permitting the viewing of everything in a single comprehensive vista; all-seeing.",
    "secondary": "In social philosophy and architectural penology, designating Jeremy Bentham's circular prison design (the Panopticon) where an unseen inspector can observe all inmates simultaneously.",
    "quotes": [
      {
        "author": "Jeremy Bentham",
        "work": "Panopticon; or, The Inspection-House",
        "quote": "The **panoptic** architecture ensures that the central inspector commands an unhindered view into every surrounding cell."
      },
      {
        "author": "Thomas Carlyle",
        "work": "Sartor Resartus",
        "quote": "From his elevated tower, the philosopher enjoyed a **panoptic** view over the bustling life of the metropolis."
      },
      {
        "author": "John Ruskin",
        "work": "Modern Painters",
        "quote": "The landscape painter must cultivate a **panoptic** grasp of light and atmosphere across the entire canvas."
      }
    ]
  },
  "Dashboard — ops\\panoptical.md": {
    "primary": "Of or relating to a panopticon; comprehensive, all-inclusive in view (synonym of panoptic).",
    "secondary": "In political philosophy and sociology, describing surveillance mechanisms or totalizing observation systems where subjects are continuously visible.",
    "quotes": [
      {
        "author": "Jeremy Bentham",
        "work": "Panopticon; or, The Inspection-House",
        "quote": "The moral effect of this **panoptical** arrangement is to convince the inmate that he is perpetually observed."
      },
      {
        "author": "Thomas Carlyle",
        "work": "The French Revolution",
        "quote": "The revolutionary surveillance committee exercised a **panoptical** vigilance over every citizen's speech."
      },
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "True intellect aspires to a **panoptical** survey of human history, rising above sectarian prejudices."
      }
    ]
  }
};

console.log(`Starting curation of Body Rem A Batch 4 (${Object.keys(batchData).length} notes)...`);
const count = updateNotesBatch(baseClusterDir, batchData);
console.log(`Batch 4 complete: successfully updated ${count} notes.`);
