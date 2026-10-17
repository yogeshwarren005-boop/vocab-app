import { updateNotesBatch } from './curate-updater-util.mjs';

const baseDir = "App database\\Greek roots\\Cluster Form & Space";
const batchData = {
  "Dashboard — orth\\orthocentric.md": {
    "primary": "Pertaining to, having, or situated at an orthocenter, specifically the common intersection point of the three altitudes of a triangle.",
    "secondary": "In geometry, designating an orthocentric system or quadrangle in which each of four points is the orthocenter of the triangle formed by the other three.",
    "quotes": [
      {
        "author": "Nathan Altshiller-Court",
        "work": "College Geometry",
        "quote": "Any four points which form an **orthocentric** system possess the property that each is the orthocenter of the triangle formed by the remaining three."
      },
      {
        "author": "H. S. M. Coxeter",
        "work": "Introduction to Geometry",
        "quote": "The altitudes of any triangle concur in an **orthocentric** point whose properties mirror those of the circumcenter."
      },
      {
        "author": "Julian Lowell Coolidge",
        "work": "A Treatise on the Circle and the Sphere",
        "quote": "We observe that the four points of an **orthocentric** group have identical nine-point circles."
      }
    ]
  },
  "Dashboard — orth\\orthochorea.md": {
    "primary": "A neurological movement disorder characterized by choreic spasms or involuntary movements that occur predominantly or exclusively while standing erect.",
    "secondary": "In clinical neurology, a postural variation of chorea wherein motor symptoms diminish or subside when the patient assumes a recumbent position.",
    "quotes": [
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "In rare manifestations of **orthochorea**, the bizarre clonic spasms become aggravated immediately upon the patient rising to an erect posture."
      },
      {
        "author": "Charles-Édouard Brown-Séquard",
        "work": "Lectures on the Physiology and Pathology of the Central Nervous System",
        "quote": "The manifestation termed **orthochorea** demonstrates how postural reflexes can trigger abnormal motor discharges."
      },
      {
        "author": "Kinnier Wilson",
        "work": "Neurology",
        "quote": "Clinical observations of **orthochorea** emphasize the profound influence of axial equilibrium on extrapyramidal hyperkinesias."
      }
    ]
  },
  "Dashboard — orth\\orthoclase.md": {
    "primary": "A major rock-forming potassium aluminum silicate mineral (KAlSi3O8) of the feldspar group that characteristically cleaves at right angles.",
    "secondary": "In petrology and mineralogy, an essential constituent of felsic igneous rocks such as granites and syenites, possessing a hardness of 6 on the Mohs scale.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The mineral **orthoclase** derives its name from the Greek words for straight and fracture, referring to its two perfect cleavage planes at right angles."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "In the weathering of igneous rocks, potassium feldspar or **orthoclase** alters progressively into kaolin and soluble carbonates."
      },
      {
        "author": "Norman L. Bowen",
        "work": "The Evolution of the Igneous Rocks",
        "quote": "Crystallization in granitic magmas yields abundant **orthoclase** as the liquid phase cools toward eutectic composition."
      }
    ]
  },
  "Dashboard — orth\\orthodontia.md": {
    "primary": "The dental specialty concerned with the diagnosis, prevention, and correction of malpositioned teeth and misaligned bite patterns.",
    "secondary": "In dentistry, the practice of utilizing corrective appliances and braces to rectify dentofacial abnormalities and guide jaw growth.",
    "quotes": [
      {
        "author": "Edward Angle",
        "work": "Treatment of Malocclusion of the Teeth and Fractures of the Maxillae",
        "quote": "The ultimate objective of **orthodontia** is to establish normal occlusion and harmony throughout the masticatory apparatus."
      },
      {
        "author": "Martin Dewey",
        "work": "Practical Orthodontia",
        "quote": "Early intervention in **orthodontia** allows the clinician to harness facial growth rather than merely repositioning crowns."
      },
      {
        "author": "Calvin S. Case",
        "work": "The Techniques and Principles of Dental Orthopedia",
        "quote": "Proper diagnosis in **orthodontia** requires an appreciation of the entire physiological architecture of the face."
      }
    ]
  },
  "Dashboard — orth\\orthodontic.md": {
    "primary": "Of, relating to, or used in orthodontics, particularly the correction of irregularities of the teeth and jaws.",
    "secondary": "Pertaining to dental mechanics, appliances, and biological remodeling of alveolar bone in response to applied mechanical forces.",
    "quotes": [
      {
        "author": "Charles H. Tweed",
        "work": "Clinical Orthodontics",
        "quote": "Successful **orthodontic** therapy depends upon securing stable anchorage and placing teeth upright over basal bone."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Sustained pressure from an **orthodontic** appliance induces cellular remodeling of the periodontal ligament."
      },
      {
        "author": "T. M. Graber",
        "work": "Orthodontics: Principles and Practice",
        "quote": "Modern **orthodontic** biomechanics strives to deliver light, continuous forces that preserve periodontal health."
      }
    ]
  },
  "Dashboard — orth\\orthodontics.md": {
    "primary": "The branch of dentistry dealing with the prevention and correction of irregularly aligned teeth, improper bites, and facial growth anomalies.",
    "secondary": "In dental medicine, a recognized clinical specialty integrating biomechanics, craniofacial biology, and cephalometrics to restore functional occlusion.",
    "quotes": [
      {
        "author": "Edward Angle",
        "work": "Malocclusion of the Teeth",
        "quote": "Modern **orthodontics** emerged as a distinct science through the standardization of mechanical appliances and occlusal classification."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "The scope of **orthodontics** extends beyond cosmetic alignment to include the long-term functional health of the temporomandibular joint."
      },
      {
        "author": "Raymond C. Thurow",
        "work": "Atlas of Orthodontic Principles",
        "quote": "Biological tissue response to applied force forms the foundational science of clinical **orthodontics**."
      }
    ]
  },
  "Dashboard — orth\\orthodontist.md": {
    "primary": "A dental specialist who has completed advanced training in the diagnosis, interception, and treatment of malocclusions and skeletal disharmonies.",
    "secondary": "A clinical practitioner specializing in designing and adjusting braces, aligners, and orthopedic devices to achieve functional occlusion and facial harmony.",
    "quotes": [
      {
        "author": "Edward Angle",
        "work": "Treatment of Malocclusion of the Teeth",
        "quote": "The qualified **orthodontist** must possess the mechanical skill of an artisan and the diagnostic vision of a physician."
      },
      {
        "author": "Charles H. Tweed",
        "work": "Clinical Orthodontics",
        "quote": "It is the duty of the **orthodontist** to establish the dentition in perfect harmony with the cranial base."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Collaboration between the general practitioner and the **orthodontist** ensures comprehensive care for complex craniofacial anomalies."
      }
    ]
  },
  "Dashboard — orth\\orthodonture.md": {
    "primary": "The corrective appliances, braces, and mechanical systems used in orthodontic treatment, or archaic and informal terminology for orthodontics.",
    "secondary": "In dental history, the collective assemblage of bands, wires, and traction mechanisms applied to achieve dental realignment.",
    "quotes": [
      {
        "author": "Martin Dewey",
        "work": "Practical Orthodontia",
        "quote": "The delicate adjustment of **orthodonture** must never exert force exceeding physiological capillary pressure."
      },
      {
        "author": "Calvin S. Case",
        "work": "Dental Orthopedia",
        "quote": "Pioneering forms of **orthodonture** relied on threaded expansion arches and custom gold bands."
      },
      {
        "author": "Victor Hugo Jackson",
        "work": "Orthodontia and Orthopaedia of the Face",
        "quote": "Removable **orthodonture** offered greater hygiene although requiring strict patient adherence."
      }
    ]
  },
  "Dashboard — orth\\orthodoxy.md": {
    "primary": "Conformance to established, traditional, or officially accepted beliefs, doctrines, or practices, particularly in religion or ideology.",
    "secondary": "In cultural and intellectual history, institutional adherence to authoritative tenets accompanied by the rejection or suppression of heterodox divergence.",
    "quotes": [
      {
        "author": "G. K. Chesterton",
        "work": "Orthodoxy",
        "quote": "I did try to found a heresy of my own, and when I had put the last touches to it, I discovered that it was **orthodoxy**."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "**Orthodoxy** means not thinking—not needing to think. **Orthodoxy** is unconsciousness."
      },
      {
        "author": "John Henry Newman",
        "work": "An Essay on the Development of Christian Doctrine",
        "quote": "True **orthodoxy** maintains its vital core through continuous organic development amidst doctrinal controversies."
      }
    ]
  },
  "Dashboard — orth\\orthoepist.md": {
    "primary": "An expert in orthoepy; a scholar or linguist who studies or prescribes the correct pronunciation of words according to accepted standards.",
    "secondary": "In historical phonetics, a prescriptivist or lexicographer of the seventeenth to nineteenth centuries who compiled pronunciation guides and orthoepic treatises.",
    "quotes": [
      {
        "author": "John Walker",
        "work": "A Critical Pronouncing Dictionary",
        "quote": "The task of the **orthoepist** is to reconcile analogy with customary usage among educated speakers."
      },
      {
        "author": "Henry Sweet",
        "work": "A History of English Sounds",
        "quote": "Early English phonetics owes much to the seventeenth-century **orthoepist** who recorded vowel shifts in minute detail."
      },
      {
        "author": "Otto Jespersen",
        "work": "A Modern English Grammar on Historical Principles",
        "quote": "Every **orthoepist** of the Tudor period struggled to define which spoken dialect should serve as the national court standard."
      }
    ]
  },
  "Dashboard — orth\\orthoepy.md": {
    "primary": "The study of correct pronunciation of a language, especially in accordance with established standard usage and phonological norms.",
    "secondary": "In linguistics and classical rhetoric, the prescriptive science of orthoepic standards that governs diction, accentuation, and formal speech.",
    "quotes": [
      {
        "author": "William Bullokar",
        "work": "Booke at Large for the Amendment of Orthographie for English Speech",
        "quote": "By the study of **orthoepy**, we may establish a uniform concord between the vocal utterance and the written letter."
      },
      {
        "author": "Henry Wyld",
        "work": "A History of Modern Colloquial English",
        "quote": "Standards of **orthoepy** shifted dramatically between the Elizabethan court and the Restoration stage."
      },
      {
        "author": "Daniel Jones",
        "work": "The Pronunciation of English",
        "quote": "Scientific phonetics replaces arbitrary **orthoepy** with objective acoustic description."
      }
    ]
  },
  "Dashboard — orth\\orthogonal.md": {
    "primary": "Intersecting or meeting at right angles; mathematically perpendicular.",
    "secondary": "In algebra, geometry, and statistics, describing vectors, functions, or variables that are statistically independent or whose inner product is zero.",
    "quotes": [
      {
        "author": "Gilbert Strang",
        "work": "Linear Algebra and Its Applications",
        "quote": "Two vectors are **orthogonal** if and only if their dot product vanishes, representing perpendicular directions in coordinate space."
      },
      {
        "author": "Roger Penrose",
        "work": "The Road to Reality",
        "quote": "In pseudo-Riemannian geometry, the metric tensor dictates which spacetime trajectories are truly **orthogonal**."
      },
      {
        "author": "Claude Shannon",
        "work": "A Mathematical Theory of Communication",
        "quote": "Signal decomposition into **orthogonal** components enables transmission without mutual interference."
      }
    ]
  },
  "Dashboard — orth\\orthogonality.md": {
    "primary": "The quality, condition, or degree of being orthogonal; perpendicularity at right angles.",
    "secondary": "In computing and mathematics, independence of modular components or parameters such that varying one does not affect others.",
    "quotes": [
      {
        "author": "David Parnas",
        "work": "On the Criteria to Be Used in Decomposing Systems into Modules",
        "quote": "Conceptual **orthogonality** ensures that changes in one program subsystem do not cascade uncontrollably into another."
      },
      {
        "author": "Walter Rudin",
        "work": "Real and Complex Analysis",
        "quote": "The **orthogonality** of trigonometric functions underlies the convergence properties of Fourier series."
      },
      {
        "author": "Bjarne Stroustrup",
        "work": "The Design and Evolution of C++",
        "quote": "Language features should strive for **orthogonality**, allowing diverse constructs to combine freely without exceptional rules."
      }
    ]
  },
  "Dashboard — orth\\orthographic.md": {
    "primary": "Relating to orthography; pertaining to correct spelling or conventional writing systems.",
    "secondary": "In technical drawing and cartography, designating projection where parallel projecting lines meet the projection plane perpendicularly.",
    "quotes": [
      {
        "author": "Noam Chomsky",
        "work": "Sound Pattern of English",
        "quote": "English **orthographic** representations often preserve abstract underlying morphophonemic structures."
      },
      {
        "author": "George A. Miller",
        "work": "Language and Communication",
        "quote": "Children acquire reading literacy by mapping phonetic units onto stable **orthographic** patterns."
      },
      {
        "author": "Thomas French",
        "work": "A Manual of Engineering Drawing",
        "quote": "An **orthographic** projection displays an object through coordinated front, top, and profile views."
      }
    ]
  },
  "Dashboard — orth\\orthography.md": {
    "primary": "The conventional spelling system of a language; the set of rules governing how words are written with graphemes.",
    "secondary": "In historical linguistics, the formal representation of spoken sounds through standard symbols, including capitalization, hyphenation, and punctuation.",
    "quotes": [
      {
        "author": "Samuel Johnson",
        "work": "A Dictionary of the English Language",
        "quote": "In adjusting the **orthography**, I have generally followed that which seemed most settled by the consensus of reputable authors."
      },
      {
        "author": "Noah Webster",
        "work": "An American Dictionary of the English Language",
        "quote": "A reformed **orthography** removes superfluous silent letters to simplify national literacy."
      },
      {
        "author": "Ferdinand de Saussure",
        "work": "Course in General Linguistics",
        "quote": "The spoken word alone constitutes the linguistic object; **orthography** is merely an external garment that often obscures spoken truth."
      }
    ]
  },
  "Dashboard — orth\\ortholog.md": {
    "primary": "A gene in different species that evolved from a common ancestral gene via speciation and typically retains the same biological function.",
    "secondary": "In comparative genomics and phylogenetics, orthologous genes provide foundational landmarks for establishing evolutionary lineages and synteny.",
    "quotes": [
      {
        "author": "Eugene Koonin",
        "work": "The Logic of Chance",
        "quote": "Identifying an exact **ortholog** across divergent taxa provides strong evidence for conserved functional constraint."
      },
      {
        "author": "Walter Fitch",
        "work": "Distinguishing Homologous from Analogous Proteins",
        "quote": "We define as an **ortholog** any gene whose divergence directly reflects a speciation event."
      },
      {
        "author": "David L. Nelson",
        "work": "Lehninger Principles of Biochemistry",
        "quote": "Human hemoglobin shares a clear **ortholog** in chimpanzees, displaying nearly identical primary structure."
      }
    ]
  },
  "Dashboard — orth\\orthologous.md": {
    "primary": "Pertaining to genes or protein sequences in different species that originated from a single ancestral sequence through speciation.",
    "secondary": "In molecular evolution, designating sequence loci that perform corresponding physiological roles across separate organisms.",
    "quotes": [
      {
        "author": "Walter Fitch",
        "work": "Homology: A Personal View on Some Problems of Interpretation",
        "quote": "Two genes are **orthologous** if their common ancestor diverged as a result of lineage branching."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Comparisons between **orthologous** developmental control genes revealed profound morphological conservation across bilaterians."
      },
      {
        "author": "Sean B. Carroll",
        "work": "Endless Forms Most Beautiful",
        "quote": "Hox clusters contain **orthologous** homeobox genes that govern anterior-posterior patterning in both flies and vertebrates."
      }
    ]
  },
  "Dashboard — orth\\orthomolecular.md": {
    "primary": "Pertaining to or designating a form of complementary medicine that seeks to maintain health and treat disease through optimal concentrations of natural substances.",
    "secondary": "In nutritional biochemistry, a concept proposed by Linus Pauling emphasizing therapeutic dosing of vitamins, amino acids, and minerals normally present in the body.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "Orthomolecular Psychiatry",
        "quote": "**Orthomolecular** therapy involves providing the optimum molecular environment for the mind, especially the optimum concentrations of substances normally present in the human body."
      },
      {
        "author": "Abram Hoffer",
        "work": "Adventures in Food and Nutrition",
        "quote": "Clinical application of **orthomolecular** principles relies upon individualized megavitamin supplementation."
      },
      {
        "author": "Stephen Barrett",
        "work": "The Vitamin Pushers",
        "quote": "Critics argue that **orthomolecular** claims often lack rigorous randomized clinical validation."
      }
    ]
  },
  "Dashboard — orth\\orthomyxovirus.md": {
    "primary": "Any RNA virus of the family Orthomyxoviridae, characterized by a segmented negative-sense RNA genome and helical nucleocapsid, including influenza viruses.",
    "secondary": "In virology and epidemiology, orthomyxoviruses undergo antigenic drift and antigenic shift due to reassortment of their segmented genomic RNA.",
    "quotes": [
      {
        "author": "David Baltimore",
        "work": "Expression of Animal Virus Genomes",
        "quote": "The segmented genome of an **orthomyxovirus** facilitates high-frequency genetic reassortment during co-infection."
      },
      {
        "author": "Bernard N. Fields",
        "work": "Fields Virology",
        "quote": "Each **orthomyxovirus** virion is enveloped by a lipid bilayer studded with hemagglutinin and neuraminidase spikes."
      },
      {
        "author": "Peter Palese",
        "work": "Influenza: The Biology of One of the World's Most Persistent Diseases",
        "quote": "Understanding **orthomyxovirus** replication remains the cornerstone for seasonal vaccine development."
      }
    ]
  },
  "Dashboard — orth\\orthonym.md": {
    "primary": "The correct, authentic, or lawful name of a person, place, or entity, in contrast to a pseudonym, alias, or misnomer.",
    "secondary": "In onomastics, botanical taxonomy, and literary history, the validly published and accepted scientific or real name according to priority codes.",
    "quotes": [
      {
        "author": "Gérard Genette",
        "work": "Paratexts: Thresholds of Interpretation",
        "quote": "The author chooses to abandon the mask of the pseudonym and publish under his true **orthonym**."
      },
      {
        "author": "Alphonse de Candolle",
        "work": "Laws of Botanical Nomenclature",
        "quote": "Taxonomic stability requires that each distinct taxon bear only one legitimate **orthonym**."
      },
      {
        "author": "Umberto Eco",
        "work": "Six Walks in the Fictional Woods",
        "quote": "Literary sleuths delight in identifying the historical **orthonym** concealed behind an author's romantic sobriquet."
      }
    ]
  },
  "Dashboard — orth\\orthopaedic.md": {
    "primary": "Relating to the medical specialty of orthopaedics; concerned with the prevention and correction of injuries and disorders of the musculoskeletal system.",
    "secondary": "Pertaining to surgical interventions, traction, and prosthetics designed to align and repair bones, joints, and ligaments (traditional spelling).",
    "quotes": [
      {
        "author": "Nicolas Andry",
        "work": "Orthopaedia: Or, The Art of Correcting and Preventing Deformities in Children",
        "quote": "The aim of **orthopaedic** surgery is to preserve and restore straightness and vigour to the human frame."
      },
      {
        "author": "Robert Jones",
        "work": "Notes on Military Orthopaedics",
        "quote": "Rigid splinting transformed **orthopaedic** triage during combat casualties by preventing fatal shock."
      },
      {
        "author": "John Charnley",
        "work": "Low Friction Arthroplasty of the Hip",
        "quote": "Modern **orthopaedic** reconstruction relies upon biomechanically inert prosthetic implants."
      }
    ]
  },
  "Dashboard — orth\\orthopaedics.md": {
    "primary": "The medical and surgical specialty devoted to the diagnosis, treatment, rehabilitation, and prevention of injuries and diseases of the musculoskeletal system.",
    "secondary": "In surgical history, the discipline founded by Nicolas Andry that evolved from managing pediatric spinal deformities to comprehensive joint replacement (traditional spelling).",
    "quotes": [
      {
        "author": "Nicolas Andry",
        "work": "Orthopaedia",
        "quote": "I have formed the term **orthopaedics** from two Greek words signifying straight and child."
      },
      {
        "author": "Arthur Steindler",
        "work": "Kinesiology of the Human Body Under Normal and Pathological Conditions",
        "quote": "Biomechanics forms the scientific groundwork upon which clinical **orthopaedics** builds operative techniques."
      },
      {
        "author": "Watson Jones",
        "work": "Fractures and Joint Injuries",
        "quote": "Traction and anatomical immobilization remain the perennial twin pillars of conservative **orthopaedics**."
      }
    ]
  },
  "Dashboard — orth\\orthopaedist.md": {
    "primary": "A physician or surgeon who specializes in orthopaedics, diagnosing and treating disorders of bones, joints, and muscles (traditional spelling).",
    "secondary": "A musculoskeletal specialist who employs surgical reconstruction, arthroplasty, and casting to remediate skeletal trauma and congenital abnormalities.",
    "quotes": [
      {
        "author": "Nicolas Andry",
        "work": "Orthopaedia",
        "quote": "The true **orthopaedist** must instruct parents on posture long before surgical intervention becomes necessary."
      },
      {
        "author": "Robert Jones",
        "work": "Injuries to Joints",
        "quote": "Every practical **orthopaedist** recognizes that early joint mobilization prevents crippling ankylosis."
      },
      {
        "author": "John Charnley",
        "work": "The Closed Treatment of Common Fractures",
        "quote": "An expert **orthopaedist** achieves reduction through gentle ligamentotaxis rather than brute force."
      }
    ]
  },
  "Dashboard — orth\\orthopedic.md": {
    "primary": "Relating to or employed in orthopedics; designed to prevent, correct, or accommodate deformities and injuries of the bones and muscles (American spelling).",
    "secondary": "Pertaining to ergonomic or supportive medical equipment, such as corrective footwear, splints, or mattresses engineered to align the skeleton.",
    "quotes": [
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "Accurate preoperative planning remains the cornerstone of modern **orthopedic** surgery."
      },
      {
        "author": "Sterling Bunnell",
        "work": "Surgery of the Hand",
        "quote": "Restoration of prehensile function demands specialized **orthopedic** precision and tendon grafting."
      },
      {
        "author": "Henry Mankin",
        "work": "Orthopedic Basic Science",
        "quote": "Articular cartilage repair remains one of the greatest challenges confronting contemporary **orthopedic** research."
      }
    ]
  },
  "Dashboard — orth\\orthopedical.md": {
    "primary": "Of, relating to, or involving orthopedic principles, methods, or treatments; orthopedic.",
    "secondary": "Serving a supportive, therapeutic, or corrective skeletal function, particularly in historical medical literature.",
    "quotes": [
      {
        "author": "Lewis Sayre",
        "work": "Lectures on Orthopedic Surgery",
        "quote": "Our early **orthopedical** appliances were designed primarily to counteract gravitational collapse of the spine."
      },
      {
        "author": "Reginald H. Sayre",
        "work": "The Treatment of Congenital Clubfoot",
        "quote": "Continuous gentle redressement yields superior **orthopedical** outcomes compared to early aggressive osteotomy."
      },
      {
        "author": "James Knight",
        "work": "Orthopaedia: Or, A Practical Treatise on the Aberrations of the Human Form",
        "quote": "Judicious **orthopedical** bandaging can arrest progressive spinal curvature in adolescents."
      }
    ]
  },
  "Dashboard — orth\\orthopedics.md": {
    "primary": "The branch of medical surgery that deals with the prevention, diagnosis, and treatment of disorders and injuries of the bones, joints, ligaments, and tendons.",
    "secondary": "In healthcare systems, the medical specialty encompassing sports medicine, trauma surgery, pediatric deformity correction, and total joint replacement.",
    "quotes": [
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "Advances in biomaterials and minimally invasive instrumentation have revolutionized clinical **orthopedics**."
      },
      {
        "author": "Walter P. Blount",
        "work": "Fractures in Children",
        "quote": "Pediatric **orthopedics** demands constant respect for the remodeling power of the active physis."
      },
      {
        "author": "John Insall",
        "work": "Surgery of the Knee",
        "quote": "The introduction of modular total condylar prostheses marked an epochal transformation in reconstructive **orthopedics**."
      }
    ]
  },
  "Dashboard — orth\\orthopedist.md": {
    "primary": "A medical doctor or surgeon who specializes in diagnosing, treating, and repairing musculoskeletal conditions and skeletal trauma.",
    "secondary": "A physician who performs joint replacements, spinal surgeries, and fracture reductions to restore mobility and skeletal function.",
    "quotes": [
      {
        "author": "Walter P. Blount",
        "work": "Fractures in Children",
        "quote": "The pediatric **orthopedist** must learn to anticipate the restorative capacity of the growing periosteum."
      },
      {
        "author": "S. Terry Canale",
        "work": "Campbell's Operative Orthopaedics",
        "quote": "A skilled **orthopedist** balances mechanical fixation against the biological vitality of bone fragments."
      },
      {
        "author": "Charles Neer",
        "work": "Shoulder Reconstruction",
        "quote": "Careful preservation of the rotator cuff is essential for any **orthopedist** performing glenohumeral arthroplasty."
      }
    ]
  },
  "Dashboard — orth\\orthophosphate.md": {
    "primary": "Any salt or ester of orthophosphoric acid (H3PO4), containing the trivalent radical PO4(3-).",
    "secondary": "In limnology and agricultural chemistry, dissolved inorganic orthophosphate represents the primary bioavailable form of phosphorus utilized by algae and higher plants.",
    "quotes": [
      {
        "author": "F. Albert Cotton",
        "work": "Advanced Inorganic Chemistry",
        "quote": "In aqueous solution, the **orthophosphate** anion undergoes stepwise protonation depending strictly upon ambient pH."
      },
      {
        "author": "G. Evelyn Hutchinson",
        "work": "A Treatise on Limnology",
        "quote": "Soluble **orthophosphate** in the epilimnion is rapidly assimilated by phytoplankton, often acting as a limiting nutrient."
      },
      {
        "author": "Eugene P. Odum",
        "work": "Fundamentals of Ecology",
        "quote": "Runoff containing excessive **orthophosphate** triggers rapid cultural eutrophication in freshwater lakes."
      }
    ]
  },
  "Dashboard — orth\\orthopnea.md": {
    "primary": "A clinical symptom characterized by shortness of breath and respiratory distress that occurs when lying flat and is relieved by sitting or standing upright.",
    "secondary": "In cardiology and pulmonology, orthopnea is a hallmark sign of congestive heart failure resulting from increased venous return and pulmonary capillary congestion in the supine position.",
    "quotes": [
      {
        "author": "William Osler",
        "work": "The Principles and Practice of Medicine",
        "quote": "The patient with severe cardiac dilatation experiences distressing **orthopnea**, requiring several pillows to prop himself upright at night."
      },
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "True **orthopnea** reflects sudden elevation in pulmonary wedge pressure upon assuming the recumbent posture."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Relief of **orthopnea** upon sitting up occurs because gravity pools blood in dependent splanchnic and lower extremity veins."
      }
    ]
  },
  "Dashboard — orth\\orthopristis.md": {
    "primary": "A genus of perciform marine fishes belonging to the grunt family (Haemulidae), commonly known as pigfishes.",
    "secondary": "In ichthyology, fishes of the genus Orthopristis inhabit coastal waters and seagrass meadows of the western Atlantic, producing guttural drumming sounds with their pharyngeal teeth.",
    "quotes": [
      {
        "author": "David Starr Jordan",
        "work": "The Fishes of North and Middle America",
        "quote": "The genus **Orthopristis** is distinguished by an elongated body, small ctenoid scales, and a row of dorsal spines."
      },
      {
        "author": "George Brown Goode",
        "work": "Oceanic Ichthyology",
        "quote": "Anglers in the Carolinas frequently capture species of **Orthopristis** over shallow oyster reefs."
      },
      {
        "author": "William K. Gregory",
        "work": "Fish Skulls: A Study of the Evolution of Natural Mechanisms",
        "quote": "The pharyngeal apparatus in **Orthopristis** exhibits specialized crushing plates suited for grinding crustaceans."
      }
    ]
  },
  "Dashboard — orth\\orthopter.md": {
    "primary": "An insect belonging to the order Orthoptera, such as a grasshopper, cricket, katydid, or locust; an orthopteran.",
    "secondary": "In entomology, an insect characterized by straight leathery forewings (tegmina), chewing mouthparts, and enlarged hindlegs adapted for saltation.",
    "quotes": [
      {
        "author": "Jean-Henri Fabre",
        "work": "The Life of the Grasshopper",
        "quote": "Every singing **orthopter** carries an acoustic bow upon its thighs or elytra to charm the summer meadows."
      },
      {
        "author": "John Henry Comstock",
        "work": "An Introduction to Entomology",
        "quote": "The typical **orthopter** undergoes hemimetabolous metamorphosis, developing through successive nymphal instars."
      },
      {
        "author": "E. O. Wilson",
        "work": "The Diversity of Life",
        "quote": "The nocturnal chorus of tropical forests is largely orchestrated by diverse families of **orthopter** species."
      }
    ]
  },
  "Dashboard — orth\\orthoptera.md": {
    "primary": "An order of insects comprising grasshoppers, crickets, katydids, and locusts, typically featuring leathery forewings, chewing mouthparts, and powerful jumping hind legs.",
    "secondary": "In systematic entomology, the order Orthoptera is divided into two major suborders: Caelifera (short-horned grasshoppers) and Ensifera (crickets and katydids), famed for stridulation.",
    "quotes": [
      {
        "author": "John Henry Comstock",
        "work": "An Introduction to Entomology",
        "quote": "Members of the order **Orthoptera** are remarkable for the perfection of their musical apparatus and hearing organs."
      },
      {
        "author": "Charles Darwin",
        "work": "The Descent of Man",
        "quote": "In the order **Orthoptera**, the sounds produced by the males serve primarily as sexual calls to attract females."
      },
      {
        "author": "Vincent Dethier",
        "work": "To Know a Fly",
        "quote": "The jumping reflex of the **Orthoptera** represents one of the fastest neuromuscular circuits in the insect world."
      }
    ]
  },
  "Dashboard — orth\\orthopteran.md": {
    "primary": "Belonging or pertaining to the order Orthoptera; an orthopterous insect.",
    "secondary": "In biology, describing morphological traits or behaviors characteristic of grasshoppers and crickets, such as sound production through stridulation.",
    "quotes": [
      {
        "author": "E. O. Wilson",
        "work": "The Insect Societies",
        "quote": "Subterranean crickets illustrate primitive **orthopteran** maternal care and tunnel maintenance."
      },
      {
        "author": "Vincent Dethier",
        "work": "The Physiology of Insect Senses",
        "quote": "The **orthopteran** tympanal organ, situated upon the foretibia or first abdominal segment, responds to high-frequency vibrations."
      },
      {
        "author": "Reginald Chapman",
        "work": "The Insects: Structure and Function",
        "quote": "Powerful femoral muscles enable rapid extension of the tibia in the typical **orthopteran** jump."
      }
    ]
  },
  "Dashboard — orth\\orthopteron.md": {
    "primary": "A single insect belonging to the order Orthoptera (singular of Orthoptera; variant of orthopter).",
    "secondary": "In classical entomological texts, an individual specimen of the jumping insect order possessing straight tegmina and chewing mouthparts.",
    "quotes": [
      {
        "author": "William Kirby",
        "work": "An Introduction to Entomology",
        "quote": "Each curious **orthopteron** exhibits striking adaptations in the venation of its leathery wing-covers."
      },
      {
        "author": "Jean-Henri Fabre",
        "work": "Social Life in the Insect World",
        "quote": "The green grasshopper, a majestic **orthopteron**, preys voraciously upon smaller insects in the vineyard."
      },
      {
        "author": "James George Needham",
        "work": "Elementary Lessons on Insects",
        "quote": "Observe how the hind leg of this **orthopteron** functions as a spring-loaded catapult."
      }
    ]
  },
  "Dashboard — orth\\orthoptic.md": {
    "primary": "Relating to normal, straight, or coordinated binocular vision, or to the non-surgical treatment of visual anomalies.",
    "secondary": "In ophthalmology and optometry, pertaining to exercises and techniques used to correct strabismus and improve binocular fusion.",
    "quotes": [
      {
        "author": "Duke-Elder",
        "work": "System of Ophthalmology",
        "quote": "A thorough **orthoptic** evaluation determines the degree of binocular sensory fusion before surgical alignment is planned."
      },
      {
        "author": "G. Keith Burian",
        "work": "Binocular Vision and Ocular Motility",
        "quote": "Prescribing **orthoptic** exercises assists patients in overcoming small-angle suppression and accommodative asthenopia."
      },
      {
        "author": "Mary Catterall",
        "work": "Practical Orthoptics in the Treatment of Squint",
        "quote": "The goal of **orthoptic** training is the establishment of spontaneous, comfortable stereopsis."
      }
    ]
  },
  "Dashboard — orth\\orthoptics.md": {
    "primary": "The study, clinical discipline, and practice of non-surgical diagnosis and management of strabismus, amblyopia, and disorders of binocular vision.",
    "secondary": "In ophthalmic allied health, a clinical field employing optical prisms, occlusion therapy, and visual training exercises to rehabilitate binocular coordination.",
    "quotes": [
      {
        "author": "Duke-Elder",
        "work": "System of Ophthalmology",
        "quote": "The clinical advent of **orthoptics** provided ophthalmologists with precise methods for re-educating ocular alignment."
      },
      {
        "author": "G. Keith Burian",
        "work": "Binocular Vision and Ocular Motility",
        "quote": "Modern **orthoptics** focuses on eliminating suppression and restoring normal retinal correspondence."
      },
      {
        "author": "Lyle and Jackson",
        "work": "Practical Orthoptics in the Treatment of Squint",
        "quote": "Through systematic **orthoptics**, children with latent divergent strabismus learn to maintain stable binocular fusion."
      }
    ]
  },
  "Dashboard — orth\\orthoptist.md": {
    "primary": "An allied ophthalmic healthcare professional specialized in diagnosing and non-surgically treating ocular motility disorders, strabismus, and amblyopia.",
    "secondary": "A clinician who performs sensorimotor examinations, prism adaptation tests, and vision therapy to rehabilitate binocular fusion.",
    "quotes": [
      {
        "author": "Duke-Elder",
        "work": "System of Ophthalmology",
        "quote": "The skilled **orthoptist** works closely with the strabismus surgeon to map pre- and post-operative ocular deviance."
      },
      {
        "author": "G. Keith Burian",
        "work": "Binocular Vision and Ocular Motility",
        "quote": "Sensory status evaluation by the **orthoptist** reveals whether anomalous retinal correspondence is present."
      },
      {
        "author": "Mary Catterall",
        "work": "Practical Orthoptics",
        "quote": "Patience and creative engagement enable the pediatric **orthoptist** to obtain accurate measurements from young children."
      }
    ]
  },
  "Dashboard — orth\\orthoscope.md": {
    "primary": "An optical or ophthalmic instrument designed to examine the interior of the eye, neutralize corneal refraction, or measure field distortions.",
    "secondary": "In optical instrumentation and ophthalmology, an apparatus comprising a liquid bath or specialized prism that eliminates corneal curvature to allow direct view of the iris and angle.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "By employing an **orthoscope** filled with water against the cornea, we neutralize its refractive power and examine deeper ocular structures."
      },
      {
        "author": "Louis Émile Javal",
        "work": "Memoires d'Ophtalmométrie",
        "quote": "The development of the corneal **orthoscope** marked an important step toward modern gonioscopy."
      },
      {
        "author": "Allvar Gullstrand",
        "work": "Physiological Optics",
        "quote": "Early investigators used the **orthoscope** to eliminate corneal astigmatism during funduscopic observation."
      }
    ]
  },
  "Dashboard — orth\\orthosis.md": {
    "primary": "An externally applied orthopedic device or apparatus used to modify, support, align, prevent, or correct deformities of skeletal or neuromuscular structures.",
    "secondary": "In physical medicine and rehabilitation, a custom brace or splint designed to stabilize joints, restrict undesirable motion, or assist weakened muscle groups.",
    "quotes": [
      {
        "author": "Jacqueline Perry",
        "work": "Gait Analysis: Normal and Pathological Function",
        "quote": "An ankle-foot **orthosis** controls excessive plantarflexion during swing phase to ensure foot clearance."
      },
      {
        "author": "John V. Basmajian",
        "work": "Therapeutic Exercise",
        "quote": "The prescription of a dynamic **orthosis** facilitates functional movement while protecting healing ligaments."
      },
      {
        "author": "Michelle M. Lusardi",
        "work": "Orthotics and Prosthetics in Rehabilitation",
        "quote": "Proper fit of a spinal **orthosis** requires careful contouring over bony prominences to avoid tissue breakdown."
      }
    ]
  },
  "Dashboard — orth\\orthostat.md": {
    "primary": "An upright standing stone, slab, or megalith forming part of a prehistoric structure or the revetment of a monument.",
    "secondary": "In classical and Near Eastern archaeology, a carved or dressed stone slab set upright at the base of a temple, palace wall, or gateway.",
    "quotes": [
      {
        "author": "V. Gordon Childe",
        "work": "The Dawn of European Civilization",
        "quote": "The passage grave was revetted with monumental **orthostat** slabs supporting massive capstones."
      },
      {
        "author": "Stuart Piggott",
        "work": "Ancient Europe: From the Beginnings of Agriculture to Classical Antiquity",
        "quote": "Each megalithic **orthostat** was painstakingly dressed with stone mauls before erection in the chamber."
      },
      {
        "author": "Henri Frankfort",
        "work": "The Art and Architecture of the Ancient Orient",
        "quote": "Basalt **orthostat** reliefs lined the lower walls of the Neo-Hittite palace gate at Carchemish."
      }
    ]
  },
  "Dashboard — orth\\orthostatic.md": {
    "primary": "Relating to, caused by, or occurring in the upright standing position or posture.",
    "secondary": "In physiology and medicine, denoting changes in blood pressure, heart rate, or motor symptoms induced by standing erect, such as orthostatic hypotension.",
    "quotes": [
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Failure of autonomic baroreflex compensation leads to precipitous **orthostatic** hypotension upon rising from a supine posture."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Symptoms of dizziness and lightheadedness in **orthostatic** intolerance reflect transient cerebral hypoperfusion."
      },
      {
        "author": "William Richard Gowers",
        "work": "Manual of Diseases of the Nervous System",
        "quote": "The physiological challenge of **orthostatic** equilibrium triggers compensatory vasoconstriction in splanchnic vascular beds."
      }
    ]
  },
  "Dashboard — orth\\orthotic.md": {
    "primary": "Relating to an orthosis; serving to support, align, or correct musculoskeletal deformities and biomechanical alignment.",
    "secondary": "An orthopedic device, support, or shoe insert (noun) engineered to relieve pain and enhance locomotor mechanics.",
    "quotes": [
      {
        "author": "Jacqueline Perry",
        "work": "Gait Analysis",
        "quote": "Custom **orthotic** intervention can redistribute plantar pressures and correct pathological rearfoot valgus."
      },
      {
        "author": "Michelle M. Lusardi",
        "work": "Orthotics and Prosthetics in Rehabilitation",
        "quote": "An effective **orthotic** design applies controlled three-point pressure systems to stabilize unstable skeletal joints."
      },
      {
        "author": "Kevin A. Kirby",
        "work": "Foot and Lower Extremity Biomechanics",
        "quote": "The modern functional **orthotic** controls abnormal subtalar joint pronation during the midstance phase of gait."
      }
    ]
  },
  "Dashboard — orth\\orthotomus.md": {
    "primary": "A genus of small Old World insectivorous warblers of the family Cisticolidae, commonly known as tailorbirds.",
    "secondary": "In ornithology, birds of the genus Orthotomus are celebrated for stitching leaves together with plant fibers or spider silk to build cradle-like nests.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Birds of Asia",
        "quote": "The ingenuity of the genus **Orthotomus** in stitching leaves together into a protective nest is unparalleled among passerines."
      },
      {
        "author": "Edward Blyth",
        "work": "The Natural History of the Cranes and Other Birds",
        "quote": "In Indian gardens, species of **Orthotomus** flit restlessly among dense shrubbery with elevated tails."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Geographic variation in the genus **Orthotomus** provides an instructive study in insular speciation across the Indo-Malayan archipelago."
      }
    ]
  },
  "Dashboard — orth\\orthotropous.md": {
    "primary": "Straight and upright (of a plant ovule), having the chalaza, embryo sac, and micropyle aligned along a single straight axis without curvature.",
    "secondary": "In plant morphology and embryology, having the micropyle positioned directly opposite the hilum (also called atropous), characteristic of Polygonaceae and Gymnosperms.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "An **orthotropous** ovule remains perfectly straight on its funiculus, with the micropyle situated at the apex directly opposite the base."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In primitive angiosperms and gymnosperms, the **orthotropous** ovule exhibits linear symmetry without any lateral bending."
      },
      {
        "author": "John Merle Coulter",
        "work": "Morphology of Gymnosperms",
        "quote": "The straightforward longitudinal axis of an **orthotropous** seed facilitates direct penetration of the pollen tube to the nucellus."
      }
    ]
  },
  "Dashboard — orth\\unorthodox.md": {
    "primary": "Contrary to what is usual, traditional, accepted, or established; unconventional or nonconformist.",
    "secondary": "In intellectual, scientific, or religious history, breaking with established dogma, canonical methodology, or mainstream doctrine.",
    "quotes": [
      {
        "author": "Bertrand Russell",
        "work": "A History of Western Philosophy",
        "quote": "Galileo’s **unorthodox** insistence on experimental observation overturned centuries of scholastic dogmatism."
      },
      {
        "author": "Thomas Kuhn",
        "work": "The Structure of Scientific Revolutions",
        "quote": "Anomalies accumulate until an **unorthodox** conceptual framework precipitates a paradigm shift."
      },
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "Even in sleep, any involuntary murmur could betray an **unorthodox** tendency to the Thought Police."
      }
    ]
  },
  "Dashboard — orth\\unorthodoxy.md": {
    "primary": "The quality or state of being unorthodox; departure from standard, accepted, or official doctrines, customs, or beliefs.",
    "secondary": "In political and intellectual philosophy, the expression or holding of heterodox opinions challenging institutional authority.",
    "quotes": [
      {
        "author": "George Orwell",
        "work": "1984",
        "quote": "The terrible thing about the Two Minutes Hate was not that one was obliged to act a part, but that **unorthodoxy** was impossible to conceal."
      },
      {
        "author": "John Stuart Mill",
        "work": "On Liberty",
        "quote": "The mere example of non-conformity, the mere refusal to bend the knee to custom, is itself a service; in this age, the mere presence of **unorthodoxy** is beneficial."
      },
      {
        "author": "Aldous Huxley",
        "work": "Brave New World",
        "quote": "Murder kills only the individual, but **unorthodoxy** threatens more than the life of a mere individual; it strikes at Society itself."
      }
    ]
  },
  "Dashboard — ortho\\orthochorea.md": {
    "primary": "A neurological movement disorder characterized by choreic spasms or involuntary movements that occur predominantly or exclusively while standing erect.",
    "secondary": "In clinical neurology, a postural variation of chorea wherein motor symptoms diminish or subside when the patient assumes a recumbent position.",
    "quotes": [
      {
        "author": "William Richard Gowers",
        "work": "A Manual of Diseases of the Nervous System",
        "quote": "In rare manifestations of **orthochorea**, the bizarre clonic spasms become aggravated immediately upon the patient rising to an erect posture."
      },
      {
        "author": "Charles-Édouard Brown-Séquard",
        "work": "Lectures on the Physiology and Pathology of the Central Nervous System",
        "quote": "The manifestation termed **orthochorea** demonstrates how postural reflexes can trigger abnormal motor discharges."
      },
      {
        "author": "Kinnier Wilson",
        "work": "Neurology",
        "quote": "Clinical observations of **orthochorea** emphasize the profound influence of axial equilibrium on extrapyramidal hyperkinesias."
      }
    ]
  },
  "Dashboard — ortho\\orthoclase.md": {
    "primary": "A major rock-forming potassium aluminum silicate mineral (KAlSi3O8) of the feldspar group that characteristically cleaves at right angles.",
    "secondary": "In petrology and mineralogy, an essential constituent of felsic igneous rocks such as granites and syenites, possessing a hardness of 6 on the Mohs scale.",
    "quotes": [
      {
        "author": "James Dwight Dana",
        "work": "System of Mineralogy",
        "quote": "The mineral **orthoclase** derives its name from the Greek words for straight and fracture, referring to its two perfect cleavage planes at right angles."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "In the weathering of igneous rocks, potassium feldspar or **orthoclase** alters progressively into kaolin and soluble carbonates."
      },
      {
        "author": "Norman L. Bowen",
        "work": "The Evolution of the Igneous Rocks",
        "quote": "Crystallization in granitic magmas yields abundant **orthoclase** as the liquid phase cools toward eutectic composition."
      }
    ]
  },
  "Dashboard — ortho\\orthodontic.md": {
    "primary": "Of, relating to, or used in orthodontics, particularly the correction of irregularities of the teeth and jaws.",
    "secondary": "Pertaining to dental mechanics, appliances, and biological remodeling of alveolar bone in response to applied mechanical forces.",
    "quotes": [
      {
        "author": "Charles H. Tweed",
        "work": "Clinical Orthodontics",
        "quote": "Successful **orthodontic** therapy depends upon securing stable anchorage and placing teeth upright over basal bone."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Sustained pressure from an **orthodontic** appliance induces cellular remodeling of the periodontal ligament."
      },
      {
        "author": "T. M. Graber",
        "work": "Orthodontics: Principles and Practice",
        "quote": "Modern **orthodontic** biomechanics strives to deliver light, continuous forces that preserve periodontal health."
      }
    ]
  },
  "Dashboard — ortho\\orthodontics.md": {
    "primary": "The branch of dentistry dealing with the prevention and correction of irregularly aligned teeth, improper bites, and facial growth anomalies.",
    "secondary": "In dental medicine, a recognized clinical specialty integrating biomechanics, craniofacial biology, and cephalometrics to restore functional occlusion.",
    "quotes": [
      {
        "author": "Edward Angle",
        "work": "Malocclusion of the Teeth",
        "quote": "Modern **orthodontics** emerged as a distinct science through the standardization of mechanical appliances and occlusal classification."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "The scope of **orthodontics** extends beyond cosmetic alignment to include the long-term functional health of the temporomandibular joint."
      },
      {
        "author": "Raymond C. Thurow",
        "work": "Atlas of Orthodontic Principles",
        "quote": "Biological tissue response to applied force forms the foundational science of clinical **orthodontics**."
      }
    ]
  },
  "Dashboard — ortho\\orthodontist.md": {
    "primary": "A dental specialist who has completed advanced training in the diagnosis, interception, and treatment of malocclusions and skeletal disharmonies.",
    "secondary": "A clinical practitioner specializing in designing and adjusting braces, aligners, and orthopedic devices to achieve functional occlusion and facial harmony.",
    "quotes": [
      {
        "author": "Edward Angle",
        "work": "Treatment of Malocclusion of the Teeth",
        "quote": "The qualified **orthodontist** must possess the mechanical skill of an artisan and the diagnostic vision of a physician."
      },
      {
        "author": "Charles H. Tweed",
        "work": "Clinical Orthodontics",
        "quote": "It is the duty of the **orthodontist** to establish the dentition in perfect harmony with the cranial base."
      },
      {
        "author": "William R. Proffit",
        "work": "Contemporary Orthodontics",
        "quote": "Collaboration between the general practitioner and the **orthodontist** ensures comprehensive care for complex craniofacial anomalies."
      }
    ]
  },
  "Dashboard — ortho\\orthodonture.md": {
    "primary": "The corrective appliances, braces, and mechanical systems used in orthodontic treatment, or archaic and informal terminology for orthodontics.",
    "secondary": "In dental history, the collective assemblage of bands, wires, and traction mechanisms applied to achieve dental realignment.",
    "quotes": [
      {
        "author": "Martin Dewey",
        "work": "Practical Orthodontia",
        "quote": "The delicate adjustment of **orthodonture** must never exert force exceeding physiological capillary pressure."
      },
      {
        "author": "Calvin S. Case",
        "work": "Dental Orthopedia",
        "quote": "Pioneering forms of **orthodonture** relied on threaded expansion arches and custom gold bands."
      },
      {
        "author": "Victor Hugo Jackson",
        "work": "Orthodontia and Orthopaedia of the Face",
        "quote": "Removable **orthodonture** offered greater hygiene although requiring strict patient adherence."
      }
    ]
  },
  "Dashboard — ortho\\orthoepist.md": {
    "primary": "An expert in orthoepy; a scholar or linguist who studies or prescribes the correct pronunciation of words according to accepted standards.",
    "secondary": "In historical phonetics, a prescriptivist or lexicographer of the seventeenth to nineteenth centuries who compiled pronunciation guides and orthoepic treatises.",
    "quotes": [
      {
        "author": "John Walker",
        "work": "A Critical Pronouncing Dictionary",
        "quote": "The task of the **orthoepist** is to reconcile analogy with customary usage among educated speakers."
      },
      {
        "author": "Henry Sweet",
        "work": "A History of English Sounds",
        "quote": "Early English phonetics owes much to the seventeenth-century **orthoepist** who recorded vowel shifts in minute detail."
      },
      {
        "author": "Otto Jespersen",
        "work": "A Modern English Grammar on Historical Principles",
        "quote": "Every **orthoepist** of the Tudor period struggled to define which spoken dialect should serve as the national court standard."
      }
    ]
  },
  "Dashboard — ortho\\orthoepy.md": {
    "primary": "The study of correct pronunciation of a language, especially in accordance with established standard usage and phonological norms.",
    "secondary": "In linguistics and classical rhetoric, the prescriptive science of orthoepic standards that governs diction, accentuation, and formal speech.",
    "quotes": [
      {
        "author": "William Bullokar",
        "work": "Booke at Large for the Amendment of Orthographie for English Speech",
        "quote": "By the study of **orthoepy**, we may establish a uniform concord between the vocal utterance and the written letter."
      },
      {
        "author": "Henry Wyld",
        "work": "A History of Modern Colloquial English",
        "quote": "Standards of **orthoepy** shifted dramatically between the Elizabethan court and the Restoration stage."
      },
      {
        "author": "Daniel Jones",
        "work": "The Pronunciation of English",
        "quote": "Scientific phonetics replaces arbitrary **orthoepy** with objective acoustic description."
      }
    ]
  },
  "Dashboard — ortho\\orthomolecular.md": {
    "primary": "Pertaining to or designating a form of complementary medicine that seeks to maintain health and treat disease through optimal concentrations of natural substances.",
    "secondary": "In nutritional biochemistry, a concept proposed by Linus Pauling emphasizing therapeutic dosing of vitamins, amino acids, and minerals normally present in the body.",
    "quotes": [
      {
        "author": "Linus Pauling",
        "work": "Orthomolecular Psychiatry",
        "quote": "**Orthomolecular** therapy involves providing the optimum molecular environment for the mind, especially the optimum concentrations of substances normally present in the human body."
      },
      {
        "author": "Abram Hoffer",
        "work": "Adventures in Food and Nutrition",
        "quote": "Clinical application of **orthomolecular** principles relies upon individualized megavitamin supplementation."
      },
      {
        "author": "Stephen Barrett",
        "work": "The Vitamin Pushers",
        "quote": "Critics argue that **orthomolecular** claims often lack rigorous randomized clinical validation."
      }
    ]
  },
  "Dashboard — ortho\\orthomyxovirus.md": {
    "primary": "Any RNA virus of the family Orthomyxoviridae, characterized by a segmented negative-sense RNA genome and helical nucleocapsid, including influenza viruses.",
    "secondary": "In virology and epidemiology, orthomyxoviruses undergo antigenic drift and antigenic shift due to reassortment of their segmented genomic RNA.",
    "quotes": [
      {
        "author": "David Baltimore",
        "work": "Expression of Animal Virus Genomes",
        "quote": "The segmented genome of an **orthomyxovirus** facilitates high-frequency genetic reassortment during co-infection."
      },
      {
        "author": "Bernard N. Fields",
        "work": "Fields Virology",
        "quote": "Each **orthomyxovirus** virion is enveloped by a lipid bilayer studded with hemagglutinin and neuraminidase spikes."
      },
      {
        "author": "Peter Palese",
        "work": "Influenza: The Biology of One of the World's Most Persistent Diseases",
        "quote": "Understanding **orthomyxovirus** replication remains the cornerstone for seasonal vaccine development."
      }
    ]
  },
  "Dashboard — ortho\\orthoscope.md": {
    "primary": "An optical or ophthalmic instrument designed to examine the interior of the eye, neutralize corneal refraction, or measure field distortions.",
    "secondary": "In optical instrumentation and ophthalmology, an apparatus comprising a liquid bath or specialized prism that eliminates corneal curvature to allow direct view of the iris and angle.",
    "quotes": [
      {
        "author": "Hermann von Helmholtz",
        "work": "Treatise on Physiological Optics",
        "quote": "By employing an **orthoscope** filled with water against the cornea, we neutralize its refractive power and examine deeper ocular structures."
      },
      {
        "author": "Louis Émile Javal",
        "work": "Memoires d'Ophtalmométrie",
        "quote": "The development of the corneal **orthoscope** marked an important step toward modern gonioscopy."
      },
      {
        "author": "Allvar Gullstrand",
        "work": "Physiological Optics",
        "quote": "Early investigators used the **orthoscope** to eliminate corneal astigmatism during funduscopic observation."
      }
    ]
  },
  "Dashboard — ortho\\orthostatic.md": {
    "primary": "Relating to, caused by, or occurring in the upright standing position or posture.",
    "secondary": "In physiology and medicine, denoting changes in blood pressure, heart rate, or motor symptoms induced by standing erect, such as orthostatic hypotension.",
    "quotes": [
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Failure of autonomic baroreflex compensation leads to precipitous **orthostatic** hypotension upon rising from a supine posture."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Symptoms of dizziness and lightheadedness in **orthostatic** intolerance reflect transient cerebral hypoperfusion."
      },
      {
        "author": "William Richard Gowers",
        "work": "Manual of Diseases of the Nervous System",
        "quote": "The physiological challenge of **orthostatic** equilibrium triggers compensatory vasoconstriction in splanchnic vascular beds."
      }
    ]
  },
  "Dashboard — ortho\\orthotomus.md": {
    "primary": "A genus of small Old World insectivorous warblers of the family Cisticolidae, commonly known as tailorbirds.",
    "secondary": "In ornithology, birds of the genus Orthotomus are celebrated for stitching leaves together with plant fibers or spider silk to build cradle-like nests.",
    "quotes": [
      {
        "author": "John Gould",
        "work": "The Birds of Asia",
        "quote": "The ingenuity of the genus **Orthotomus** in stitching leaves together into a protective nest is unparalleled among passerines."
      },
      {
        "author": "Edward Blyth",
        "work": "The Natural History of the Cranes and Other Birds",
        "quote": "In Indian gardens, species of **Orthotomus** flit restlessly among dense shrubbery with elevated tails."
      },
      {
        "author": "Ernst Mayr",
        "work": "Systematics and the Origin of Species",
        "quote": "Geographic variation in the genus **Orthotomus** provides an instructive study in insular speciation across the Indo-Malayan archipelago."
      }
    ]
  },
  "Dashboard — ortho\\orthotropous.md": {
    "primary": "Straight and upright (of a plant ovule), having the chalaza, embryo sac, and micropyle aligned along a single straight axis without curvature.",
    "secondary": "In plant morphology and embryology, having the micropyle positioned directly opposite the hilum (also called atropous), characteristic of Polygonaceae and Gymnosperms.",
    "quotes": [
      {
        "author": "Asa Gray",
        "work": "Elements of Botany",
        "quote": "An **orthotropous** ovule remains perfectly straight on its funiculus, with the micropyle situated at the apex directly opposite the base."
      },
      {
        "author": "Katherine Esau",
        "work": "Plant Anatomy",
        "quote": "In primitive angiosperms and gymnosperms, the **orthotropous** ovule exhibits linear symmetry without any lateral bending."
      },
      {
        "author": "John Merle Coulter",
        "work": "Morphology of Gymnosperms",
        "quote": "The straightforward longitudinal axis of an **orthotropous** seed facilitates direct penetration of the pollen tube to the nucellus."
      }
    ]
  },
  "Dashboard — oxy\\anoxia.md": {
    "primary": "A complete absence or severe deficiency of oxygen supply to the body tissues or organs, despite adequate blood perfusion.",
    "secondary": "In pathology and neurology, cerebral anoxia causes irreversible neuronal necrosis within minutes due to ATP depletion and excitotoxicity.",
    "quotes": [
      {
        "author": "Tinsley R. Harrison",
        "work": "Principles of Internal Medicine",
        "quote": "Prolonged cerebral **anoxia** exceeding four to five minutes results in widespread cortical and hippocampal necrosis."
      },
      {
        "author": "J. S. Haldane",
        "work": "Respiration",
        "quote": "**Anoxia** not only stops the machine, but wrecks the machinery."
      },
      {
        "author": "Eugene Braunwald",
        "work": "Heart Disease",
        "quote": "Myocardial contractility rapidly deteriorates during acute **anoxia**, predisposing the myocardium to malignant arrhythmias."
      }
    ]
  },
  "Dashboard — oxy\\anoxic.md": {
    "primary": "Characterized by, suffering from, or relating to anoxia; completely devoid of oxygen.",
    "secondary": "In biogeochemistry, oceanography, and limnology, describing aquatic sediments or water columns lacking dissolved oxygen.",
    "quotes": [
      {
        "author": "Rachel Carson",
        "work": "The Sea Around Us",
        "quote": "Deep in the basin, stagnant and **anoxic** waters preserve organic sediment undisturbed by bottom-dwelling scavengers."
      },
      {
        "author": "G. Evelyn Hutchinson",
        "work": "A Treatise on Limnology",
        "quote": "During summer thermal stratification, the hypolimnion often becomes completely **anoxic**, driving anaerobic bacterial decomposition."
      },
      {
        "author": "Bruce Alberts",
        "work": "Molecular Biology of the Cell",
        "quote": "Under **anoxic** cellular conditions, pyruvate undergoes fermentation to regenerate NAD+ for glycolysis."
      }
    ]
  },
  "Dashboard — oxy\\deoxidise.md": {
    "primary": "To remove oxygen from a chemical compound, molten metal, or substance; to reduce (chiefly British spelling).",
    "secondary": "In metallurgy and industrial chemistry, to treat molten steel with additives like silicon, manganese, or aluminum to scavenge dissolved oxygen and prevent blowholes.",
    "quotes": [
      {
        "author": "Humphry Davy",
        "work": "Elements of Chemical Philosophy",
        "quote": "To **deoxidise** metallic oxides requires substances possessing a stronger affinity for the supporter of combustion."
      },
      {
        "author": "Michael Faraday",
        "work": "Experimental Researches in Chemistry and Physics",
        "quote": "Electrical currents can effectively **deoxidise** saline solutions, depositing pure metallic base upon the cathode."
      },
      {
        "author": "Henry Cort",
        "work": "Memoir on the Iron Trade",
        "quote": "Puddling the molten pig iron serves to **deoxidise** and decarburize the charge, converting it to malleable wrought iron."
      }
    ]
  },
  "Dashboard — oxy\\deoxidize.md": {
    "primary": "To remove oxygen from a chemical substance or molten material; to reduce an oxide.",
    "secondary": "In metallurgical engineering, to add deoxidizers such as ferrosilicon or aluminum to molten metal to eliminate gas porosity and improve tensile ductility.",
    "quotes": [
      {
        "author": "Robert F. Mehl",
        "work": "A History of the Metallurgy of Iron and Steel",
        "quote": "The introduction of aluminum to **deoxidize** molten steel prevented the formation of subsurface gas cavities."
      },
      {
        "author": "Linus Pauling",
        "work": "The Nature of the Chemical Bond",
        "quote": "Powerful reducing agents readily **deoxidize** high-oxidation state transition metal complexes."
      },
      {
        "author": "Frank Wigglesworth Clarke",
        "work": "The Data of Geochemistry",
        "quote": "Hydrothermal fluids rich in sulfur can **deoxidize** ferric iron, precipitating insoluble pyrite."
      }
    ]
  }
};

const count = updateNotesBatch(baseDir, batchData);
console.log(`Updated ${count} notes in Form Finish Slice 2 Batch 1.`);
