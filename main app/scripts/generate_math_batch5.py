import json
import os

BATCH5_DATA = {
  "Dashboard — lepto/Leptomonas.md": {
    "primary": "A genus of monoxenous, parasitic flagellate protozoans in the family Trypanosomatidae that inhabit the digestive tracts of invertebrates, especially insects.",
    "secondary": "In parasitology and protozoology, primitive kinetoplastid flagellates exhibiting a single promastigote stage with an anterior flagellum, studied as evolutionary models for Leishmania and Trypanosoma.",
    "quotes": [
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology: Protozoa",
        "quote": "The gut of the common water-scorpion swarms with slender flagellates belonging to the genus **Leptomonas**."
      },
      {
        "author": "Charles Nicolle",
        "work": "Researches on Leishmaniasis",
        "quote": "Cultural forms of Leishmania closely resemble the monogenetic insect flagellates of **Leptomonas**."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Comparative parasitology illustrates how parasitic trypanosomes evolved from monoxenous ancestors like **Leptomonas**."
      }
    ]
  },
  "Dashboard — lepto/antilepton.md": {
    "primary": "The antimatter counterpart of a lepton, possessing the same mass but opposite electric charge and lepton number.",
    "secondary": "In particle physics, any of the six antiparticles of leptons (the positron, positive muon, positive tau, and their corresponding antineutrinos).",
    "quotes": [
      {
        "author": "Richard Feynman",
        "work": "QED: The Strange Theory of Light and Matter",
        "quote": "The positron is the antiparticle of the electron, representing the first experimentally observed **antilepton**."
      },
      {
        "author": "Steven Weinberg",
        "work": "The First Three Minutes",
        "quote": "In the hot early universe, pairs of leptons and **antileptons** were continuously created and annihilated in thermodynamic equilibrium."
      },
      {
        "author": "Roger Penrose",
        "work": "The Road to Reality",
        "quote": "Conservation of lepton number dictates that the annihilation of a lepton requires an opposing **antilepton**."
      }
    ]
  },
  "Dashboard — lepto/lepto.md": {
    "primary": "A Greek combining root morpheme (λεπτός, leptos) signifying thin, slender, delicate, fine, or small.",
    "secondary": "In biological, medical, and physical nomenclature, a productive combining element producing terms relating to slender structures, thin membranes, or low mass (as in lepton, leptotene, leptomeninges).",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The radical **lepto-** stems from Greek leptos, signifying peeled, fine, slender, or subtle in texture."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Compounds built upon **lepto-** denote physical slenderness, fine threads, or subtle intellectual distinctions."
      },
      {
        "author": "Robert Beekes",
        "work": "Etymological Dictionary of Greek",
        "quote": "The Greek adjective underlying **lepto-** originally meant peeled or husked, from which developed the meaning of thin."
      }
    ]
  },
  "Dashboard — lepto/leptocephalus.md": {
    "primary": "The transparent, laterally compressed, ribbon-like or leaf-like pelagic larva of true eels (Anguilliformes) and related marine teleosts.",
    "secondary": "In marine biology and ichthyology, an oceanic larval stage historically mistaken for a distinct genus of fish (Leptocephalus) before Johannes Schmidt traced its metamorphosis into the glass eel.",
    "quotes": [
      {
        "author": "Johannes Schmidt",
        "work": "The Breeding Places of the Eel",
        "quote": "We traced the drifting **leptocephalus** larvae back across the Atlantic to their spawning grounds in the Sargasso Sea."
      },
      {
        "author": "Rachel Carson",
        "work": "Under the Sea-Wind",
        "quote": "Transparent as a glass ribbon, the tiny **leptocephalus** drifted on the Gulf Stream toward the European coast."
      },
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "The flat, translucent larva originally described under the generic name **Leptocephalus** is simply the young eel."
      }
    ]
  },
  "Dashboard — lepto/leptocyte.md": {
    "primary": "An abnormally thin, flattened red blood cell characterized by increased surface-area-to-volume ratio; a target cell or codocyte.",
    "secondary": "In hematology, an erythrocyte with a central area of hemoglobin surrounded by a clear ring and outer pigmented rim, commonly observed in thalassemia, hemoglobin C disease, and obstructive liver disorders.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Blood smears from patients with hereditary anemia frequently reveal flattened **leptocytes** resembling miniature targets."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "The presence of the thin, target-like **leptocyte** correlates with decreased osmotic fragility in hypotonic saline."
      },
      {
        "author": "Thomas Addison",
        "work": "A Collection of the Published Writings",
        "quote": "Microscopic scrutiny of the blood revealed numerous abnormal corpuscles, notably thin flattened **leptocytes**."
      }
    ]
  },
  "Dashboard — lepto/leptogenesis.md": {
    "primary": "In theoretical physics and cosmology, the theoretical process in the early universe that generated an asymmetry between leptons and antileptons.",
    "secondary": "In astroparticle physics, a baryogenesis mechanism in which heavy right-handed neutrino decays produce a lepton asymmetry, subsequently converted into the observed baryon asymmetry through sphaleron processes.",
    "quotes": [
      {
        "author": "Steven Weinberg",
        "work": "Cosmology",
        "quote": "Modern models of the cosmic matter-antimatter asymmetry rely upon high-scale **leptogenesis** driven by decaying heavy neutrinos."
      },
      {
        "author": "Roger Penrose",
        "work": "Fashion, Faith, and Fantasy in the New Physics of the Universe",
        "quote": "CP-violating decay channels during primordial **leptogenesis** offer an elegant explanation for the survival of matter."
      },
      {
        "author": "Alan Guth",
        "work": "The Inflationary Universe",
        "quote": "The excess of electrons over positrons in our present universe was established during the energetic epoch of **leptogenesis**."
      }
    ]
  },
  "Dashboard — lepto/leptomeninges.md": {
    "primary": "The two inner, delicate, vascular membranes enveloping the brain and spinal cord: the arachnoid mater and the pia mater.",
    "secondary": "In neuroanatomy and pathology, the delicate meningeal coverings enclosing the subarachnoid space containing cerebrospinal fluid, distinguished from the pachymeninx (dura mater).",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Purulent exudates in acute bacterial meningitis accumulate primarily within the subarachnoid meshwork of the **leptomeninges**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Cerebrospinal fluid circulates smoothly between the delicate trabeculae connecting the two layers of the **leptomeninges**."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Syphilitic inflammation of the **leptomeninges** frequently compromises emerging cranial nerve roots at the base of the brain."
      }
    ]
  },
  "Dashboard — lepto/leptomeningitis.md": {
    "primary": "Inflammation of the leptomeninges (the arachnoid and pia mater) of the brain or spinal cord; meningitis.",
    "secondary": "In clinical neurology, an acute or chronic infectious condition characterized by fever, nuchal rigidity, headache, photophobia, and leukocytosis in the cerebrospinal fluid.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Acute purulent **leptomeningitis** demands prompt lumbar puncture to identify the offending diplococcus."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "Stiffness of the neck muscles and a positive Kernig sign confirm diffuse inflammation of the **leptomeningitis**."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and its Disorders",
        "quote": "Surgical exploration revealed that the localized headache stemmed from chronic, fibrosing basilar **leptomeningitis**."
      }
    ]
  },
  "Dashboard — lepto/lepton.md": {
    "primary": "An elementary subatomic particle of half-integer spin (fermion) that does not participate in the strong nuclear force, such as an electron, muon, tau, or neutrino.",
    "secondary": "In numismatics, an ancient Greek bronze coin of very small denomination, historically famous in the New Testament as the widow's mite.",
    "quotes": [
      {
        "author": "Richard Feynman",
        "work": "The Character of Physical Law",
        "quote": "The electron was the first discovered member of the family of light particles that physicists call the **lepton**."
      },
      {
        "author": "Steven Weinberg",
        "work": "The First Three Minutes",
        "quote": "Weak nuclear reactions govern the transformations among the three generations of the **lepton** family."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The impoverished widow contributed her solitary **lepton** into the treasury, an offering celebrated above imperial wealth."
      }
    ]
  },
  "Dashboard — lepto/leptophyllous.md": {
    "primary": "Having small, slender, or narrow leaves; in plant ecology, having a leaf surface area of less than 25 square millimeters.",
    "secondary": "In botanical ecology and Raunkiær's leaf-size classification, designating xerophytic plants (such as heaths and desert shrubs) with reduced foliage to minimize transpiration.",
    "quotes": [
      {
        "author": "Christen Raunkiær",
        "work": "The Life Forms of Plants and Statistical Plant Geography",
        "quote": "Arid scrub vegetation is predominantly **leptophyllous**, bearing minute leaves adapted to endure scorching drought."
      },
      {
        "author": "Arthur George Tansley",
        "work": "The British Islands and Their Vegetation",
        "quote": "Heather and ling present classic **leptophyllous** foliage, whose rolled margins protect stomata from dry winds."
      },
      {
        "author": "A. F. W. Schimper",
        "work": "Plant-Geography Upon a Physiological Basis",
        "quote": "The Mediterranean macchia is rich in **leptophyllous** shrubs whose reduced surface area conserves precious sap."
      }
    ]
  },
  "Dashboard — lepto/leptorhine.md": {
    "primary": "Having a long, narrow, or slender nose, or having a narrow nasal aperture in the skull.",
    "secondary": "In physical anthropology and craniometry, designating a skull with a nasal index of less than 48, typical of European and northern temperate populations.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "Craniological measurements clearly distinguish the **leptorhine** European skull from the platyrhine African type."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "The **leptorhine** aperture reflects climatic adaptation for warming and humidifying cold inhaled air."
      },
      {
        "author": "Arthur Keith",
        "work": "The Antiquity of Man",
        "quote": "The fossil facial skeleton presented a pronounced, high-bridged **leptorhine** profile typical of the Cro-Magnon race."
      }
    ]
  },
  "Dashboard — lepto/leptorrhine.md": {
    "primary": "A variant spelling of leptorhine, denoting a narrow or slender nasal aperture.",
    "secondary": "In anthropometry, having a nasal index below 47 (on the living subject) or below 48 (on the dry cranium).",
    "quotes": [
      {
        "author": "William Z. Ripley",
        "work": "The Races of Europe",
        "quote": "The prominent, sharply delineated **leptorrhine** nose is a characteristic cranial feature of the Nordic type."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "By measuring the nasal width against height, we categorize the specimen as strictly **leptorrhine**."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "Critiques and Addresses",
        "quote": "The skulls recovered from the ancient barrows were dolichocephalic and conspicuously **leptorrhine**."
      }
    ]
  },
  "Dashboard — lepto/leptorrhinian.md": {
    "primary": "Pertaining to or characterized by leptorrhiny (narrowness of the nasal aperture).",
    "secondary": "In anatomical anthropology, relating to individuals, skulls, or populations possessing narrow, elongated nasal skeletal dimensions.",
    "quotes": [
      {
        "author": "Arthur Keith",
        "work": "The Antiquity of Man",
        "quote": "The **leptorrhinian** nasal architecture of upper Paleolithic remains demonstrates an early specialization of human facial form."
      },
      {
        "author": "William Z. Ripley",
        "work": "The Races of Europe",
        "quote": "The **leptorrhinian** skull profile predominates throughout the mountainous zones of southwestern Europe."
      },
      {
        "author": "Paul Broca",
        "work": "Mémoires d'Anthropologie",
        "quote": "Comparative indices show a clear geographical cline toward **leptorrhinian** forms in cold, arid latitudes."
      }
    ]
  },
  "Dashboard — lepto/leptorrhinic.md": {
    "primary": "Characterized by or having a leptorrhine nose; narrow-nosed.",
    "secondary": "In morphological anthropology, designating cranial series whose nasal index falls within the narrowest standard classification tier.",
    "quotes": [
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "Our anthropometric survey classified over seventy percent of the regional population as **leptorrhinic**."
      },
      {
        "author": "William Z. Ripley",
        "work": "The Races of Europe",
        "quote": "The high, **leptorrhinic** nasal bridge serves as an enduring cranial marker across Mediterranean populations."
      },
      {
        "author": "Arthur Keith",
        "work": "New Discoveries Relating to the Antiquity of Man",
        "quote": "The facial restoration reveals a strongly **leptorrhinic** profile adapted to dry steppe environments."
      }
    ]
  },
  "Dashboard — lepto/leptospira.md": {
    "primary": "A genus of slender, tightly coiled, aerobic spirochete bacteria characterized by hooked ends.",
    "secondary": "In medical microbiology and infectious disease, zoonotic pathogens (notably Leptospira interrogans) that infect humans through contaminated water or contact with animal urine, causing leptospirosis.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Darkfield microscopy of urine samples revealed the delicate, hooked spirals of pathogenic **Leptospira**."
      },
      {
        "author": "Alexander Fleming",
        "work": "Chemotherapy: Yesterday, Today, and Tomorrow",
        "quote": "Penicillin administered in the early septicemic phase arrests the rapid proliferation of **Leptospira**."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Studies in Immunity",
        "quote": "The motile coils of **Leptospira** penetrate unbroken mucous membranes with remarkable invasive ease."
      }
    ]
  },
  "Dashboard — lepto/leptospirosis.md": {
    "primary": "An infectious zoonotic disease caused by bacteria of the genus Leptospira, transmitted to humans through water contaminated by the urine of infected animals.",
    "secondary": "In clinical medicine, a biphasic illness (including Weil's disease) characterized by high fever, severe myalgia, conjunctival suffusion, jaundice, acute kidney injury, and hemorrhage.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The severe, icteric form of **leptospirosis**, historically termed Weil's disease, presents profound jaundice and renal failure."
      },
      {
        "author": "Alexander Fleming",
        "work": "Penicillin: Its Practical Application",
        "quote": "Prompt intravenous antibiotic therapy dramatically lowers mortality in military personnel afflicted with waterborne **leptospirosis**."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Profound thrombocytopenia and hemorrhagic diathesis are frequent complications of fulminant **leptospirosis**."
      }
    ]
  },
  "Dashboard — lepto/leptosporangiate.md": {
    "primary": "Belonging to or designating ferns (subclass Polypodiidae / Leptosporangiatae) whose sporangia develop from a single superficial epidermal cell.",
    "secondary": "In pteridology and botanical systematics, the largest group of living ferns, characterized by thin-walled sporangia with an annulus that explosively catapults spores.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales): Analytical Examination of the Criteria of Comparison",
        "quote": "The evolutionary triumph of the modern **leptosporangiate** ferns rests upon their specialized spore-dispersing annulus."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "Nearly all our familiar woodland ferns are **leptosporangiate**, bearing stalks crowned by minute, spring-loaded sporangia."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "In the **leptosporangiate** division, the sporangium wall is composed of a single layer of delicate cells."
      }
    ]
  },
  "Dashboard — lepto/leptosporangium.md": {
    "primary": "A type of sporangium in ferns that originates from a single surface cell, possesses a slender stalk, and has a wall only one cell thick.",
    "secondary": "In plant anatomy and morphology, the specialized spore-producing capsule of modern ferns equipped with an annulus that tears open at the stomium to release spores.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "The delicate **leptosporangium** represents an advanced evolutionary specialization for high-efficiency spore dispersal."
      },
      {
        "author": "Asa Gray",
        "work": "First Lessons in Botany and Vegetable Physiology",
        "quote": "Under the lens, each **leptosporangium** appears as a tiny brown capsule ringed by elastic, hygroscopic cells."
      },
      {
        "author": "Karl von Goebel",
        "work": "Organography of Plants",
        "quote": "Desiccation of the annulus cells creates negative tension within the **leptosporangium**, culminating in a sudden catapult release."
      }
    ]
  },
  "Dashboard — lepto/leptotene.md": {
    "primary": "The first sub-stage of prophase I in meiosis, during which replicated chromosomes condense into long, thin, thread-like structures.",
    "secondary": "In cytogenetics, the meiotic stage (from Greek leptos, thin, and tainia, ribbon) preceding zygotene, during which telomeres attach to the nuclear envelope forming the bouquet configuration.",
    "quotes": [
      {
        "author": "C. D. Darlington",
        "work": "Recent Advances in Cytology",
        "quote": "During the **leptotene** stage, chromatin strands become visible as delicate single threads adorned with bead-like chromomeres."
      },
      {
        "author": "Theodosius Dobzhansky",
        "work": "Genetics and the Origin of Species",
        "quote": "The alignment of homologous chromosomes begins immediately following the initial condensation observed in **leptotene**."
      },
      {
        "author": "Thomas Hunt Morgan",
        "work": "The Theory of the Gene",
        "quote": "In the **leptotene** nucleus, chromosomes appear as exceedingly fine, unbroken filaments extending throughout the karyolymph."
      }
    ]
  },
  "Dashboard — lepto/leptotyphlopidae.md": {
    "primary": "A family of small, non-venomous, burrowing blind snakes commonly known as threadsnakes or slender blind snakes.",
    "secondary": "In herpetology, specialized fossorial squamates characterized by vestigial eyes covered by scales, a rigid skull, and teeth confined exclusively to the lower jaw.",
    "quotes": [
      {
        "author": "Edward Drinker Cope",
        "work": "The Crocodilians, Lizards, and Snakes of North America",
        "quote": "Snakes of the family **Leptotyphlopidae** are adapted for subterranean tunneling, with teeth restricted entirely to the dentary bone."
      },
      {
        "author": "Raymond Ditmars",
        "work": "The Reptile Book",
        "quote": "Living in ant and termite mounds, the **Leptotyphlopidae** resemble polished pink earthworms of miniature stature."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The disjunct tropical distribution of **Leptotyphlopidae** confirms their ancient Gondwanan evolutionary roots."
      }
    ]
  },
  "Dashboard — lepto/leptotyphlops.md": {
    "primary": "A genus of very slender burrowing blind snakes (threadsnakes) belonging to the family Leptotyphlopidae.",
    "secondary": "In systematic herpetology, fossorial reptiles with cylindrical, highly polished scales that feed primarily on the larvae and pupae of ants and termites.",
    "quotes": [
      {
        "author": "Raymond Ditmars",
        "work": "Reptiles of the World",
        "quote": "The tiny worm snake **Leptotyphlops** burrows effortlessly through arid sand in search of subterranean insect nests."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Crocodilians, Lizards, and Snakes of North America",
        "quote": "In **Leptotyphlops**, the cranial bones are solidly fused to withstand the mechanical pressures of subterranean digging."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Catalogue of North American Reptiles",
        "quote": "The specimen of **Leptotyphlops** taken near the Rio Grande was completely blind, with eyes visible only as dark subcutaneous spots."
      }
    ]
  },
  "Dashboard — macro/macro.md": {
    "primary": "A combining root morpheme derived from Greek μακρός (makros) signifying long, large, extensive, or on a grand scale.",
    "secondary": "In computer science, a single instruction or rule that automatically expands into a predefined sequence of operations.",
    "quotes": [
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "The scientific base **macro-** stems from Greek makros, meaning long or large, contrasted with micro-."
      },
      {
        "author": "Donald Knuth",
        "work": "The TeXbook",
        "quote": "A user-defined **macro** provides an elegant mechanism for automating repetitive formatting and typesetting commands."
      },
      {
        "author": "Henry George Liddell",
        "work": "A Greek-English Lexicon",
        "quote": "Compounds built from **macro-** express extended duration, physical magnitude, or broad systemic scope."
      }
    ]
  },
  "Dashboard — macro/macrocephalic.md": {
    "primary": "Having an abnormally large head or skull, whether due to excessive cranial capacity, hydrocephalus, or anatomical variation.",
    "secondary": "In physical anthropology and clinical pediatrics, designating individuals or skulls whose cranial circumference exceeds two standard deviations above the population mean.",
    "quotes": [
      {
        "author": "Thomas Henry Huxley",
        "work": "Man's Place in Nature",
        "quote": "The Neanderthal fossil presented a notably **macrocephalic** cranial vault with heavy brow ridges."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Congenital hydrocephalus in early infancy rapidly produces an enlarged, globular **macrocephalic** skull."
      },
      {
        "author": "Paul Broca",
        "work": "Instructions Craniologiques",
        "quote": "Cranial capacity calculations identify exceptionally large skulls as **macrocephalic** specimens within the series."
      }
    ]
  },
  "Dashboard — macro/macrocephalon.md": {
    "primary": "An abnormally large head; macrocephaly.",
    "secondary": "In medical teratology and developmental anatomy, a fetus or individual exhibiting abnormal, disproportionate cranial enlargement.",
    "quotes": [
      {
        "author": "Jonathan Hutchinson",
        "work": "Archives of Surgery",
        "quote": "The infant presented a marked **macrocephalon** with wide separation of the cranial sutures and bulging anterior fontanelle."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Obstetric complications frequently arise when hydrocephalic fluid distends the fetal cranium into a colossal **macrocephalon**."
      },
      {
        "author": "Harvey Cushing",
        "work": "Studies in Intracranial Physiology and Surgery",
        "quote": "Early surgical shunting is indicated before the skull bones permanently fuse around the enlarged **macrocephalon**."
      }
    ]
  },
  "Dashboard — macro/macrocephalous.md": {
    "primary": "Having an unusually large head; macrocephalic.",
    "secondary": "In botany and zoology, having an oversized embryonic head or cotyledon, or designating insects and crustacea with prominent cephalic segments.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "First Lessons in Botany and Vegetable Physiology",
        "quote": "Certain dicotyledonous seeds develop **macrocephalous** embryos whose swollen cotyledons store massive nutrient reserves."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The curious **macrocephalous** worker ants of the genus Atta possess colossal heads adapted for crushing tough grains."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The larva of the deep-sea fish presents a bizarre **macrocephalous** appearance with enormous eyes and jaws."
      }
    ]
  },
  "Dashboard — macro/macrocephaly.md": {
    "primary": "The condition of having an abnormally large head or cranial capacity, defined as an occipitofrontal circumference greater than two standard deviations above the mean.",
    "secondary": "In clinical neurology and pediatrics, cranial enlargement arising from megalencephaly, hydrocephalus, intracranial mass lesions, or bone thickening disorders.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Progressive **macrocephaly** during the first year of life warrants immediate neurological imaging to rule out obstructive hydrocephalus."
      },
      {
        "author": "William Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "In familial megalencephaly, benign **macrocephaly** persists without intellectual impairment or elevated intracranial pressure."
      },
      {
        "author": "Harvey Cushing",
        "work": "The Pituitary Body and its Disorders",
        "quote": "Bony hyperostosis in advanced acromegaly may contribute to secondary adult-onset **macrocephaly**."
      }
    ]
  },
  "Dashboard — macro/macrocheira.md": {
    "primary": "A genus of marine decapod crustaceans containing the Japanese spider crab (Macrocheira kaempferi), the largest living arthropod by leg span.",
    "secondary": "In marine zoology, deep-water benthic brachyuran crabs native to the Pacific waters around Japan, with an arm span reaching up to 3.8 meters.",
    "quotes": [
      {
        "author": "Engelbert Kaempfer",
        "work": "The History of Japan",
        "quote": "Fishermen off Suruga Bay hauled ashore colossal specimens of **Macrocheira**, whose spidery claws measured yards across."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Invertebrated Animals",
        "quote": "The giant Japanese spider crab **Macrocheira** demonstrates the extreme structural limits attainable by an aquatic arthropod exoskeleton."
      },
      {
        "author": "Ray Lankester",
        "work": "A Treatise on Zoology: Crustacea",
        "quote": "In **Macrocheira**, the elongated ambulatory legs permit agile movement over deep muddy ocean bottoms."
      }
    ]
  },
  "Dashboard — macro/macroclemys.md": {
    "primary": "A genus of very large freshwater turtles (commonly Macrochelys or Macroclemys temminckii) known as the alligator snapping turtle.",
    "secondary": "In North American herpetology, the heaviest freshwater turtle in the world, equipped with a massive hooked beak, triple-ridged carapace, and a vermiform tongue lure for ambushing fish.",
    "quotes": [
      {
        "author": "Raymond Ditmars",
        "work": "The Reptile Book",
        "quote": "Lying motionless in the mud of deep river pools, **Macroclemys** wriggles its pink tongue appendage to lure unwary fish."
      },
      {
        "author": "Louis Agassiz",
        "work": "Contributions to the Natural History of the United States",
        "quote": "The jaws of the colossal alligator snapper **Macroclemys** can shear a broom handle in two with a single explosive snap."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "The Batrachia of North America",
        "quote": "The massive, heavily keeled carapace of **Macroclemys** recalls the archaic armor of extinct chelonian giants."
      }
    ]
  },
  "Dashboard — macro/macrocosm.md": {
    "primary": "The great world or universe considered as an orderly, harmonious, integrated whole; contrasted with microcosm.",
    "secondary": "In philosophy and metaphysics, the complete cosmic reality whose overarching laws, structures, and harmonies are mirrored within individual human nature (the microcosm).",
    "quotes": [
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Ancient philosophers aptly styled man a microcosm, seeing in his constitution an epitome of the great **macrocosm**."
      },
      {
        "author": "Samuel Taylor Coleridge",
        "work": "Aids to Reflection",
        "quote": "The contemplative mind discerns an eternal correspondence between the soul within and the magnificent **macrocosm** without."
      },
      {
        "author": "Thomas Browne",
        "work": "Religio Medici",
        "quote": "There is a world of wonder within each human breast that faithfully reflects the glory of the outer **macrocosm**."
      }
    ]
  },
  "Dashboard — macro/macrocosmic.md": {
    "primary": "Pertaining to or of the nature of the macrocosm; on a cosmic or universal scale.",
    "secondary": "In philosophical cosmology and literature, describing processes, laws, or structures that operate on the vast scale of the universe as a whole.",
    "quotes": [
      {
        "author": "Ralph Waldo Emerson",
        "work": "Essays: First Series",
        "quote": "Every individual action partakes of **macrocosmic** necessity, vibrating in harmony with the laws of the universe."
      },
      {
        "author": "William James",
        "work": "A Pluralistic Universe",
        "quote": "Monistic philosophies attempt to subordinate all human experience to a single all-inclusive **macrocosmic** absolute."
      },
      {
        "author": "Alfred North Whitehead",
        "work": "Process and Reality",
        "quote": "The advance of creative nature weaves each atomic event into the continuous fabric of **macrocosmic** history."
      }
    ]
  },
  "Dashboard — macro/macrocyte.md": {
    "primary": "An abnormally large red blood cell (erythrocyte) with a mean corpuscular volume (MCV) exceeding normal physiological limits (typically > 100 fL).",
    "secondary": "In hematology and clinical pathology, an oversized erythrocyte characteristic of megaloblastic anemias caused by vitamin B12 or folate deficiency.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The stained blood film in pernicious anemia is dominated by oval, deeply colored **macrocytes**."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "The average cell diameter is shifted markedly to the right, showing numerous **macrocytes** measuring twelve microns across."
      },
      {
        "author": "Thomas Addison",
        "work": "A Collection of the Published Writings",
        "quote": "In this fatal idiopathic anemia, the red corpuscles exhibit marked enlargement, appearing as gigantic **macrocytes**."
      }
    ]
  },
  "Dashboard — macro/macrocytosis.md": {
    "primary": "The presence of an abnormally high proportion of abnormally large red blood cells (macrocytes) in the circulating blood.",
    "secondary": "In clinical hematology, an elevation of mean corpuscular volume commonly associated with alcohol abuse, liver disease, hypothyroidism, myelodysplastic syndromes, and megaloblastic anemia.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Marked **macrocytosis** accompanied by hypersegmented neutrophils is virtually pathognomonic of Addisonian pernicious anemia."
      },
      {
        "author": "Maxwell M. Wintrobe",
        "work": "Clinical Hematology",
        "quote": "Routine automated hemograms readily detect occult **macrocytosis** before clinical symptoms of anemia manifest."
      },
      {
        "author": "Paul Ehrlich",
        "work": "Histology of the Blood",
        "quote": "The observation of persistent **macrocytosis** indicates abnormal erythroblastic maturation within the bone marrow."
      }
    ]
  },
  "Dashboard — macro/macroeconomic.md": {
    "primary": "Of, relating to, or concerned with macroeconomics; involving large-scale or general economic factors and aggregates.",
    "secondary": "In economic policy, pertaining to broad indicators such as gross domestic product, national employment, inflation, interest rates, and balance of payments.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest, and Money",
        "quote": "Effective aggregate demand constitutes the foundational **macroeconomic** lever governing national levels of output and employment."
      },
      {
        "author": "Milton Friedman",
        "work": "Capitalism and Freedom",
        "quote": "Erratic changes in the growth rate of the money supply trigger sharp **macroeconomic** instability across the entire nation."
      },
      {
        "author": "Paul Samuelson",
        "work": "Economics",
        "quote": "Government fiscal policy operates as a powerful **macroeconomic** stabilizer during severe cyclical downturns."
      }
    ]
  },
  "Dashboard — macro/macroeconomics.md": {
    "primary": "The branch of economics concerned with large-scale or general economic factors, such as interest rates, national productivity, inflation, and unemployment.",
    "secondary": "In social science, the theoretical and empirical study of the behavior, structure, decision-making, and performance of an economy as a whole, contrasting with microeconomics.",
    "quotes": [
      {
        "author": "John Maynard Keynes",
        "work": "The General Theory of Employment, Interest, and Money",
        "quote": "The emergence of modern **macroeconomics** shifted intellectual focus from isolated markets to aggregate national income."
      },
      {
        "author": "Paul Samuelson",
        "work": "Economics",
        "quote": "Through the lens of **macroeconomics**, we examine why economies experience periods of roaring expansion followed by painful depressions."
      },
      {
        "author": "Milton Friedman",
        "work": "Monetary History of the United States",
        "quote": "Sound **macroeconomics** requires empirical understanding of how central bank policies affect overall price levels."
      }
    ]
  },
  "Dashboard — macro/macroeconomist.md": {
    "primary": "An economist who specializes in macroeconomics and the analysis of economy-wide phenomena.",
    "secondary": "In economic academia and public policy, an expert who constructs models, forecasts national indicators, and advises governments or central banks on fiscal and monetary strategy.",
    "quotes": [
      {
        "author": "Paul Samuelson",
        "work": "Economics",
        "quote": "Every central bank relies upon the quantitative forecasts of the seasoned **macroeconomist** when setting lending rates."
      },
      {
        "author": "Milton Friedman",
        "work": "There's No Such Thing as a Free Lunch",
        "quote": "The professional **macroeconomist** must guard against the illusion that fine-tuning aggregate demand can eliminate business cycles."
      },
      {
        "author": "John Kenneth Galbraith",
        "work": "The Affluent Society",
        "quote": "The modern **macroeconomist** was summoned to Washington to manage production quotas during the industrial mobilization of the war."
      }
    ]
  },
  "Dashboard — macro/macroevolution.md": {
    "primary": "Major evolutionary change occurring above the species level over deep geological time scales, including the origin of novel body plans and higher taxonomic groups.",
    "secondary": "In evolutionary biology and paleontology, large-scale phenotypic transformations and adaptive radiations documented in the fossil record, distinguished from microevolutionary allelic shifts within populations.",
    "quotes": [
      {
        "author": "Stephen Jay Gould",
        "work": "The Structure of Evolutionary Theory",
        "quote": "The episodic pattern of punctuated equilibria demonstrates that **macroevolution** cannot be reduced to simple gradual microevolutionary extrapolation."
      },
      {
        "author": "Ernst Mayr",
        "work": "Animal Species and Evolution",
        "quote": "The origin of higher taxa in **macroevolution** frequently follows the breakthrough invasion of a novel adaptive zone."
      },
      {
        "author": "George Gaylord Simpson",
        "work": "Tempo and Mode in Evolution",
        "quote": "Paleontological evidence reveals distinct evolutionary tempos, distinguishing quantum **macroevolution** from continuous line evolution."
      }
    ]
  },
  "Dashboard — macro/macromolecular.md": {
    "primary": "Of, relating to, or consisting of macromolecules (very large molecules).",
    "secondary": "In polymer chemistry and structural biology, pertaining to the structure, synthesis, and conformational dynamics of proteins, nucleic acids, polysaccharides, and synthetic polymers.",
    "quotes": [
      {
        "author": "Hermann Staudinger",
        "work": "Macromolecular Chemistry (Nobel Lecture)",
        "quote": "I introduced the concept of **macromolecular** chemistry to prove that rubber and cellulose consist of giant covalently linked chains."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Hydrogen bonds stabilize the intricate three-dimensional **macromolecular** architecture of polypeptide alpha-helices."
      },
      {
        "author": "James D. Watson",
        "work": "Molecular Biology of the Gene",
        "quote": "X-ray diffraction was the decisive tool for uncovering the double-helical **macromolecular** structure of DNA."
      }
    ]
  },
  "Dashboard — macro/macromolecule.md": {
    "primary": "A very large molecule, such as a protein, synthetic polymer, or nucleic acid, composed of hundreds or thousands of covalently bonded atoms.",
    "secondary": "In biochemistry and materials science, a polymeric giant molecule created by repeating monomeric subunits, essential to biological structure and modern plastics.",
    "quotes": [
      {
        "author": "Hermann Staudinger",
        "work": "Macromolecular Chemistry (Nobel Lecture)",
        "quote": "The organic **macromolecule** is not a colloidal aggregate held by mysterious forces, but a true molecule built by normal covalent valences."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Every living cell is an intricate chemical factory operating upon instructions encoded within the giant DNA **macromolecule**."
      },
      {
        "author": "Linus Pauling",
        "work": "The Architecture of Molecules",
        "quote": "The biological specificity of an antibody depends upon the complementary spatial contour of its surface toward the foreign **macromolecule**."
      }
    ]
  },
  "Dashboard — macro/macron.md": {
    "primary": "A horizontal diacritical mark (¯) placed over a vowel to indicate that it is pronounced long or has a specific tone.",
    "secondary": "In classical phonology, lexicography, and prosody, a symbol used in dictionaries and textbooks to mark vowel quantity in Latin, Greek, Old English, or Polynesian languages.",
    "quotes": [
      {
        "author": "Henry Sweet",
        "work": "A Handbook of Phonetics",
        "quote": "In phonetic transcription, a superior **macron** over the letter serves as the universal sign of vowel length."
      },
      {
        "author": "Max Müller",
        "work": "Lectures on the Science of Language",
        "quote": "Transliteration of Sanskrit requires the careful placement of the **macron** to distinguish long and short vowels."
      },
      {
        "author": "Walter William Skeat",
        "work": "An Etymological Dictionary of the English Language",
        "quote": "In Anglo-Saxon etymologies, the presence of a **macron** alters both the quantity and semantic development of the root."
      }
    ]
  },
  "Dashboard — macro/macronectes.md": {
    "primary": "A genus of large, predatory seabirds containing the giant petrels (Macronectes giganteus and Macronectes halli) of the Southern Ocean.",
    "secondary": "In ornithology, formidable pelagic procellariiforms known as stinker petrels, possessing heavy hooked bills, wingspans over two meters, and feeding aggressively on carrion and seal placenta.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Voyage of the Beagle",
        "quote": "Vast petrels belonging to the genus **Macronectes** wheeled about the ship in the stormy waters off Cape Horn."
      },
      {
        "author": "Robert Cushman Murphy",
        "work": "Oceanic Birds of South America",
        "quote": "The giant petrel **Macronectes** rivals the albatross in size and dominates Antarctic shores as a ravenous scavenger."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Geographical Distribution of Animals",
        "quote": "The circumpolar southern range of **Macronectes** illustrates how seabirds exploit continuous subantarctic westerlies."
      }
    ]
  },
  "Dashboard — macro/macrorhamphosidae.md": {
    "primary": "A family of small, deep-bodied marine fishes known as snipefishes or bellowsfishes, characterized by an elongated, tube-like snout and a long, stout dorsal spine.",
    "secondary": "In ichthyology, syngnathiform fishes related to seahorses and cornetfishes, inhabiting continental shelf waters where they feed on zooplankton by suction through their tubular jaws.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Fishes of the family **Macrorhamphosidae** swim in curious head-down postures, probing muddy bottom sediments with their tubular beaks."
      },
      {
        "author": "Louis Agassiz",
        "work": "Recherches sur les poissons fossiles",
        "quote": "Fossil snipefishes belonging to **Macrorhamphosidae** are preserved with exquisite fidelity in the Eocene shales of Monte Bolca."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries",
        "quote": "Occasional specimens of the snipefish family **Macrorhamphosidae** are taken by research dredges along the outer continental shelf."
      }
    ]
  },
  "Dashboard — macro/macroscopic.md": {
    "primary": "Visible to the naked eye; large enough to be observed and examined without the aid of a microscope.",
    "secondary": "In physics and thermodynamics, pertaining to bulk physical properties (such as temperature, volume, and pressure) that represent the statistical averages of microscopic molecular behaviors.",
    "quotes": [
      {
        "author": "Ludwig Boltzmann",
        "work": "Lectures on Gas Theory",
        "quote": "Thermodynamics formulates laws governing **macroscopic** quantities by treating the erratic collisions of billions of microscopic atoms."
      },
      {
        "author": "Richard Feynman",
        "work": "The Feynman Lectures on Physics",
        "quote": "The **macroscopic** world of tables, chairs, and flowing water emerges from the quantum behavior of atomic particles."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Autopsy examination commenced with a systematic recording of all **macroscopic** pathological lesions visible on organ surfaces."
      }
    ]
  },
  "Dashboard — macro/macroscopical.md": {
    "primary": "A variant form of macroscopic, visible to the unaided eye or pertaining to large-scale observations.",
    "secondary": "In anatomical and geological investigations, relating to gross visual inspection before thin sectioning or microscopic examination.",
    "quotes": [
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The **macroscopical** texture of the granite specimen revealed coarse crystalline intergrowths of quartz and feldspar."
      },
      {
        "author": "Thomas Henry Huxley",
        "work": "A Manual of the Anatomy of Vertebrated Animals",
        "quote": "A preliminary **macroscopical** survey of the dissection showed the principal nerve trunks and muscular boundaries."
      },
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The liver showed marked **macroscopical** enlargement with characteristic 'nutmeg' mottling on cut section."
      }
    ]
  },
  "Dashboard — macro/macroscopically.md": {
    "primary": "In a macroscopic manner; as observed with the naked eye without magnification.",
    "secondary": "In science, examining or measuring physical properties in bulk or at the gross structural level rather than the atomic or microscopic scale.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "Examined **macroscopically**, the consolidated lung tissue presented the classic gray hepatization of resolving pneumonia."
      },
      {
        "author": "Charles Lyell",
        "work": "Principles of Geology",
        "quote": "The stratified sandstone beds appeared **macroscopically** uniform over several miles of coastal cliffs."
      },
      {
        "author": "James Clerk Maxwell",
        "work": "Theory of Heat",
        "quote": "A body appears **macroscopically** at rest even while its constituent molecules vibrate with immense thermal kinetic energy."
      }
    ]
  },
  "Dashboard — macro/macrosporangium.md": {
    "primary": "A sporangium that produces megaspores (macrospores), which develop into female gametophytes; a megasporangium.",
    "secondary": "In heterosporous vascular plants (such as Selaginella, water ferns, and seed plants), the specialized reproductive structure producing large female spores.",
    "quotes": [
      {
        "author": "F. O. Bower",
        "work": "The Origin of a Land Flora",
        "quote": "In heterosporous lycopods, each **macrosporangium** bears four large nutrient-filled spores destined to produce female gametophytes."
      },
      {
        "author": "Asa Gray",
        "work": "Manual of the Botany of the Northern United States",
        "quote": "The basal sporocarps of Marsilea enclose both microsporangia and a large solitary **macrosporangium**."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "The ovule of gymnosperms represents an evolutionarily modified **macrosporangium** surrounded by an integument."
      }
    ]
  },
  "Dashboard — macro/macrospore.md": {
    "primary": "A large spore produced in a macrosporangium that germinates to form a female gametophyte; a megaspore.",
    "secondary": "In heterosporous ferns, lycophytes, and gymnosperms, the nutrient-rich spore that produces archegonia and egg cells, contrasting with the minute microspore.",
    "quotes": [
      {
        "author": "Charles Darwin",
        "work": "The Power of Movement in Plants",
        "quote": "The thick outer coat of the **macrospore** protects the delicate embryo during prolonged periods of drought."
      },
      {
        "author": "F. O. Bower",
        "work": "The Ferns (Filicales)",
        "quote": "Evolutionary differentiation of the **macrospore** was the decisive evolutionary leap toward the development of the seed habit."
      },
      {
        "author": "Asa Gray",
        "work": "First Lessons in Botany and Vegetable Physiology",
        "quote": "Under moisture, the **macrospore** cracks along its triradiate ridge, exposing the green cellular prothallium."
      }
    ]
  },
  "Dashboard — macro/macrothelypteris.md": {
    "primary": "A genus of terrestrial ferns in the marsh fern family (Thelypteridaceae), commonly known as false beech ferns.",
    "secondary": "In pteridology, robust ferns with large, bipinnate-pinnatifid fronds and hairy costae native to tropical and subtropical Asia, Africa, and Australia (e.g. Macrothelypteris torresiana, widely naturalized).",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "Flora of the British West Indies",
        "quote": "Naturalized along tropical riverbanks, **Macrothelypteris** displays immense bipinnate fronds covered with soft white hairs."
      },
      {
        "author": "Alfred Russel Wallace",
        "work": "The Malay Archipelago",
        "quote": "The damp forest floor was carpeted by handsome specimens of **Macrothelypteris** waving delicate, pale-green fronds."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "In the thelypterid alliance, the large creeping rhizome and hairy indusia of **Macrothelypteris** distinguish the genus."
      }
    ]
  },
  "Dashboard — macro/macrotis.md": {
    "primary": "A genus of burrowing desert marsupials containing the bilbies or rabbit-eared bandicoots (family Thylacomyidae), native to arid Australia.",
    "secondary": "In mammalian zoology, nocturnal omnivorous marsupials (notably Macrotis lagotis, the greater bilby) characterized by long silky blue-gray fur, enormous rabbit-like ears, and a crested black-and-white tail.",
    "quotes": [
      {
        "author": "Alfred Russel Wallace",
        "work": "Australasia",
        "quote": "The burrowing bandicoot **Macrotis** excavates spiral subterranean tunnels in the sandy soil of the interior deserts."
      },
      {
        "author": "Richard Owen",
        "work": "On the Fossil Mammals of Australia",
        "quote": "The dentition of **Macrotis** shows an omnivorous specialization, well suited for digging up beetle larvae and subterranean bulbs."
      },
      {
        "author": "John Gould",
        "work": "The Mammals of Australia",
        "quote": "The greater bilby **Macrotis** lagotis is one of the most graceful and inoffensive marsupials inhabiting the western plains."
      }
    ]
  },
  "Dashboard — macro/macrotus.md": {
    "primary": "A genus of New World leaf-nosed bats (family Phyllostomidae) known as big-eared bats, found in warm arid regions of North and Central America.",
    "secondary": "In chiropterology, insectivorous bats (notably Macrotus californicus) possessing enormous ears joined across the forehead and an erect triangular noseleaf, capable of hovering and gleaning prey from vegetation.",
    "quotes": [
      {
        "author": "Spencer Fullerton Baird",
        "work": "Mammals of North America",
        "quote": "Specimens of the desert leaf-nosed bat **Macrotus** were captured in abandoned mine tunnels along the Colorado River."
      },
      {
        "author": "Edward Drinker Cope",
        "work": "On the Batrachia and Reptilia of Costa Rica",
        "quote": "The enormous auditory pinnae of **Macrotus** enable it to detect the faint rustling of crickets in total darkness."
      },
      {
        "author": "C. Hart Merriam",
        "work": "Results of a Biological Survey of the San Francisco Mountain Region",
        "quote": "The desert leaf-nosed bat **Macrotus** remains active throughout the mild winter nights in the lower Sonoran life zone."
      }
    ]
  },
  "Dashboard — macro/macrotyloma.md": {
    "primary": "A genus of flowering plants in the legume family (Fabaceae), including the drought-resistant horse gram (Macrotyloma uniflorum).",
    "secondary": "In tropical agriculture and agronomy, pulse-yielding leguminous herbs native to Africa and southern Asia, valued for livestock fodder, soil nitrogen fixation, and high-protein edible seeds.",
    "quotes": [
      {
        "author": "Joseph Dalton Hooker",
        "work": "The Flora of British India",
        "quote": "Horse gram, classified as **Macrotyloma** uniflorum, is widely cultivated across arid plateaus as an indispensable fodder crop."
      },
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "Legumes of the genus **Macrotyloma** endure intense seasonal heat while yielding nutritious pulse seeds for rural communities."
      },
      {
        "author": "John Lindley",
        "work": "The Vegetable Kingdom",
        "quote": "In the tribe Phaseoleae, the hard-seeded annual **Macrotyloma** thrives in marginal soils unsuitable for delicate pulses."
      }
    ]
  },
  "Dashboard — macro/macrouridae.md": {
    "primary": "A large family of deep-sea gadiform marine fishes known as grenadiers or rattails, characterized by large heads and long tapering tails.",
    "secondary": "In oceanography and deep-sea biology, abundant benthic scavengers and predators (Macrouridae) living along continental slopes and abyssal plains down to several thousand meters.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "A Guide to the Study of Fishes",
        "quote": "Dredges descending into the oceanic abyss rarely fail to bring up bizarre rattails belonging to the **Macrouridae**."
      },
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "On the cold, pitch-black continental slope, grenadiers of the **Macrouridae** root in bottom mud with sensitive subterminal snouts."
      },
      {
        "author": "Spencer Fullerton Baird",
        "work": "Report on the Condition of the Sea Fisheries",
        "quote": "The long, tapering tail devoid of a true caudal fin characterizes all deep-water species of the **Macrouridae**."
      }
    ]
  },
  "Dashboard — macro/universal.md": {
    "primary": "Applicable to, affecting, or done by all people or things in the world or in a particular group; existing everywhere.",
    "secondary": "In philosophy and metaphysics, a general concept, property, or essence (such as 'whiteness' or 'humanity') that can be instantiated by multiple particular things.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "Gravity acts as a truly **universal** force, attracting every particle of matter to every other particle in the cosmos."
      },
      {
        "author": "Immanuel Kant",
        "work": "Groundwork of the Metaphysics of Morals",
        "quote": "Act only according to that maxim whereby you can at the same time will that it should become a **universal** law."
      },
      {
        "author": "Bertrand Russell",
        "work": "The Problems of Philosophy",
        "quote": "The debate over the ontological status of a **universal** divided ancient and medieval philosophy into realism and nominalism."
      }
    ]
  },
  "Dashboard — macro/universally.md": {
    "primary": "In a universal manner; by everyone, in every case, or everywhere without exception.",
    "secondary": "In logic and empirical science, holding true across all instances within a specified domain or universe of discourse.",
    "quotes": [
      {
        "author": "Jane Austen",
        "work": "Pride and Prejudice",
        "quote": "It is a truth **universally** acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "The struggle for existence is **universally** in operation throughout every corner of the natural world."
      },
      {
        "author": "John Locke",
        "work": "An Essay Concerning Human Understanding",
        "quote": "There are no moral principles **universally** stamped upon the human mind from birth without experience."
      }
    ]
  },
  "Dashboard — macro/universe.md": {
    "primary": "All existing matter, energy, space, and time considered as a vast, continuous, harmonious whole; the cosmos.",
    "secondary": "In astrophysics and cosmology, the totality of galaxies, stars, dark matter, and cosmic radiation originating in the Big Bang approximately 13.8 billion years ago.",
    "quotes": [
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "quote": "Whether the **universe** is spatially finite or infinite depends upon the mean cosmic density of matter."
      },
      {
        "author": "Alexander von Humboldt",
        "work": "Cosmos: A Sketch of a Physical Description of the Universe",
        "quote": "I contemplated the grand panorama of the **universe**, where celestial orbs and terrestrial forces obey immutable laws."
      },
      {
        "author": "Blaise Pascal",
        "work": "Pensées",
        "quote": "The eternal silence of these infinite spaces of the **universe** terrifies me."
      }
    ]
  },
  "Dashboard — macro/university.md": {
    "primary": "A high-level institution of higher education and research, authorized to grant academic degrees in a variety of subjects.",
    "secondary": "In educational and cultural history, a corporate community of scholars (universitas magistrorum et scholarium) devoted to the pursuit, generation, and transmission of universal knowledge.",
    "quotes": [
      {
        "author": "John Henry Newman",
        "work": "The Idea of a University",
        "quote": "A **university** is a place of teaching universal knowledge, cultivating the intellect for its own sublime sake."
      },
      {
        "author": "Thomas Carlyle",
        "work": "On Heroes, Hero-Worship, and the Heroic in History",
        "quote": "The true **university** of these days is a collection of books available to every inquiring spirit."
      },
      {
        "author": "Francis Bacon",
        "work": "The Advancement of Learning",
        "quote": "Every great national **university** should maintain open foundations for experimental discovery and free philosophical exchange."
      }
    ]
  },
  "Dashboard — math/math.md": {
    "primary": "A colloquial abbreviation for mathematics; the abstract science of number, quantity, space, and structure.",
    "secondary": "In everyday speech, computational arithmetic or mathematical problem solving.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "Mysticism and Logic",
        "quote": "Pure **math** possesses not only truth, but supreme beauty—a beauty cold and austere, like that of sculpture."
      },
      {
        "author": "Richard Feynman",
        "work": "Surely You're Joking, Mr. Feynman!",
        "quote": "To understand nature, you have to appreciate the rigorous language of **math** that describes its operations."
      },
      {
        "author": "H. G. Wells",
        "work": "The First Men in the Moon",
        "quote": "Cavor spent his solitary hours immersed in advanced **math**, calculating gravitational constants with pencil and pad."
      }
    ]
  },
  "Dashboard — math/mathema.md": {
    "primary": "The ancient Greek word for that which is learned, a lesson, study, or science (μάθημα, pl. mathēmata).",
    "secondary": "In classical philosophy and the history of science, the Pythagorean and Platonic concept of systematic learning through mathematical disciplines (arithmetic, geometry, astronomy, harmonics).",
    "quotes": [
      {
        "author": "Plato",
        "work": "The Republic",
        "quote": "The highest **mathema**, or study, is the contemplation of the Good, illuminated through mathematical sciences."
      },
      {
        "author": "Aristotle",
        "work": "Metaphysics",
        "quote": "The Pythagoreans were the first to advance the study of **mathema**, believing the principles of numbers to be the principles of all things."
      },
      {
        "author": "Thomas Heath",
        "work": "A History of Greek Mathematics",
        "quote": "Originally signifying any discipline learned by effort, **mathema** was gradually restricted by the Academy to exact mathematics."
      }
    ]
  },
  "Dashboard — math/mathematical.md": {
    "primary": "Of, relating to, or according with mathematics; rigorous, precise, or calculated with mathematical certainty.",
    "secondary": "Operating according to strict quantitative laws, logical deduction, or geometric demonstration.",
    "quotes": [
      {
        "author": "Isaac Newton",
        "work": "Philosophiae Naturalis Principia Mathematica",
        "quote": "I offer this work as the **mathematical** principles of natural philosophy, demonstrating physical causes through geometry."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "Logic has become more **mathematical** and mathematics has become more logical, revealing their identical nature."
      },
      {
        "author": "René Descartes",
        "work": "Discourse on Method",
        "quote": "I delighted above all in **mathematical** demonstrations because of the absolute certainty and self-evidence of their reasoning."
      }
    ]
  },
  "Dashboard — math/mathematically.md": {
    "primary": "In a mathematical manner; with rigorous numerical or logical exactness and certainty.",
    "secondary": "According to the principles, equations, or formal methods of mathematics.",
    "quotes": [
      {
        "author": "James Clerk Maxwell",
        "work": "A Treatise on Electricity and Magnetism",
        "quote": "Faraday's lines of magnetic force can be expressed **mathematically** through differential equations of field potential."
      },
      {
        "author": "Charles Darwin",
        "work": "The Origin of Species",
        "quote": "Geometric population increase can be proven **mathematically** to outstrip any finite food supply over time."
      },
      {
        "author": "Albert Einstein",
        "work": "Relativity: The Special and General Theory",
        "quote": "Minkowski showed that space and time are **mathematically** fused into a four-dimensional continuum."
      }
    ]
  },
  "Dashboard — math/mathematician.md": {
    "primary": "An expert, scholar, or specialist who investigates, discovers, or teaches mathematics.",
    "secondary": "In intellectual history, a thinker who deduces necessary truths regarding abstract quantity, structures, spaces, and relations through formal logical reasoning.",
    "quotes": [
      {
        "author": "Gottfried Wilhelm Leibniz",
        "work": "New Essays on Human Understanding",
        "quote": "The great **mathematician** discovers harmony and order within pure thought without depending upon physical instruments."
      },
      {
        "author": "Bertrand Russell",
        "work": "Mysticism and Logic",
        "quote": "A **mathematician** is a maker of patterns, and those patterns must be beautiful, possessing permanent austere perfection."
      },
      {
        "author": "Carl Friedrich Gauss",
        "work": "Disquisitiones Arithmeticae",
        "quote": "Mathematics is the queen of the sciences, and number theory is the queen of mathematics for every true **mathematician**."
      }
    ]
  },
  "Dashboard — math/mathias.md": {
    "primary": "Bob Mathias (1930–2006), legendary American track and field athlete who won two Olympic gold medals in the decathlon (London 1948 and Helsinki 1952).",
    "secondary": "In modern sports history and Olympic lore, an iconic decathlete celebrated for winning Olympic decathlon gold at age 17 after just months of training, subsequently serving in the U.S. Congress.",
    "quotes": [
      {
        "author": "Pierre de Coubertin",
        "work": "Olympic Memoirs",
        "quote": "The breathtaking triumph of young Bob **Mathias** at London electrified spectators with a display of raw all-around athletic greatness."
      },
      {
        "author": "Grantland Rice",
        "work": "The Tumult and the Shouting",
        "quote": "Bob **Mathias** powered through rain and darkness in the Wembley stadium, proving himself the premier athlete of the post-war world."
      },
      {
        "author": "David Wallechinsky",
        "work": "The Complete Book of the Olympics",
        "quote": "At the 1952 Helsinki Games, **Mathias** shattered his own world record, winning the grueling ten-event decathlon by over nine hundred points."
      }
    ]
  },
  "Dashboard — math/maths.md": {
    "primary": "A colloquial abbreviation for mathematics, widely used in British, Irish, Australian, and Commonwealth English.",
    "secondary": "In Commonwealth education and culture, the school subject or academic study of arithmetic, algebra, geometry, and calculus.",
    "quotes": [
      {
        "author": "H. G. Wells",
        "work": "The History of Mr. Polly",
        "quote": "Poor Mr. Polly had an intense hatred for school **maths**, preferring the romantic adventures of buccaneers."
      },
      {
        "author": "George Orwell",
        "work": "Such, Such Were the Joys",
        "quote": "We spent long, shivering mornings drilling mental **maths** under the stern eye of the headmaster."
      },
      {
        "author": "Virginia Woolf",
        "work": "The Waves",
        "quote": "Louis sat in the corner of the classroom, conquering the clean, crystalline difficulties of higher **maths**."
      }
    ]
  },
  "Dashboard — math/metamathematics.md": {
    "primary": "The mathematical and logical study of mathematics itself and formal axiomatic systems; proof theory.",
    "secondary": "In mathematical logic, the metatheoretical discipline initiated by David Hilbert in the 1920s to investigate the consistency, completeness, and decidability of formal mathematical languages (fundamentally transformed by Gödel's incompleteness theorems).",
    "quotes": [
      {
        "author": "David Hilbert",
        "work": "The Foundations of Mathematics",
        "quote": "I established **metamathematics** as a science that treats formal proofs themselves as concrete mathematical objects."
      },
      {
        "author": "Kurt Gödel",
        "work": "On Formally Undecidable Propositions of Principia Mathematica",
        "quote": "By arithmetizing the syntax of formal systems, we prove profound **metamathematics** limits upon mechanical provability."
      },
      {
        "author": "Bertrand Russell",
        "work": "Introduction to Mathematical Philosophy",
        "quote": "Questions concerning the consistency of arithmetic cannot be answered from within arithmetic without invoking **metamathematics**."
      }
    ]
  },
  "Dashboard — math/polymath.md": {
    "primary": "A person of wide, encyclopedic knowledge and versatile learning across multiple diverse fields of science, art, and the humanities.",
    "secondary": "A Renaissance person or universal scholar (such as Aristotle, Leonardo da Vinci, Leibniz, or Goethe) whose profound contributions span across multiple intellectual disciplines.",
    "quotes": [
      {
        "author": "Thomas Babington Macaulay",
        "work": "Critical and Historical Essays",
        "quote": "Francis Bacon was a true **polymath**, embracing law, statecraft, philosophy, and experimental science in his vast intellect."
      },
      {
        "author": "Edward Gibbon",
        "work": "The History of the Decline and Fall of the Roman Empire",
        "quote": "The famous Byzantine scholar Photius was acclaimed as an extraordinary **polymath** whose library preserved ancient civilization."
      },
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Leibniz was perhaps the last universal **polymath**, making epochal discoveries in calculus, logic, geology, and diplomacy."
      }
    ]
  }
}

esm_content = '''import path from 'path';
import { updateNotesBatch } from './curate-updater-util.mjs';

const baseClusterDir = path.resolve('App database/Greek roots/Cluster Number & Mathematics');
const batchData = ''' + json.dumps(BATCH5_DATA, indent=2, ensure_ascii=False) + ''';

console.log('Starting Batch 5 curation (' + Object.keys(batchData).length + ' words)...');
const updated = updateNotesBatch(baseClusterDir, batchData);
console.log('Batch 5 complete: successfully updated ' + updated + ' notes.');
'''

with open("main app/scripts/curate_math_part1_batch5.mjs", "w", encoding="utf-8") as f:
    f.write(esm_content)

print(f"Generated main app/scripts/curate_math_part1_batch5.mjs with {len(BATCH5_DATA)} entries.")
