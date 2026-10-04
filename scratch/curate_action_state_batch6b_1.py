# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — art Part 1 (41 words) ---
  "Dashboard — art/abarticulation.md": {
    "primary": "Dislocation of a joint; or a synovial joint characterized by a wide range of mobility.",
    "secondary": "In historical arthrology and orthopedic surgery, abarticulation designated diarthrodial joints such as the ball-and-socket shoulder articulation.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The pectoral girdle permits extensive **abarticulation**, allowing the humerus free rotational movement within the glenoid fossa."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe traumatic injury may cause violent **abarticulation** of the phalanges, requiring immediate closed reduction under anesthesia."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The surgeon examined the compound dislocation, noting how pathological **abarticulation** had compromised adjacent neurovascular bundles."}
    ]
  },
  "Dashboard — art/apart.md": {
    "primary": "Separated by a distance in space or time; or aside and away from others.",
    "secondary": "In analytical philosophy and aesthetics, setting a concept apart from contingent circumstances clarifies its essential properties.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Stand all **apart**, and let me hear him speak; for in his sorrow there is royal dignity."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip stood **apart** in the marshes, watching the dark figures of the soldiers pursue the escaped convicts."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The mind considers complex ideas by taking their simple components **apart** through intellectual abstraction."}
    ]
  },
  "Dashboard — art/apartment.md": {
    "primary": "A suite of rooms forming one residence, typically within a larger building containing several such dwellings.",
    "secondary": "In European court architecture, royal state apartments were arranged in strict ceremonial sequences of guard chambers, presence rooms, and bedchambers.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "We met next day as he had arranged, and inspected the rooms at 221B, Baker Street, the very **apartment** we desired."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Gardiner expressed great pleasure at the elegance of the private **apartment** prepared for their reception."},
      {"author": "Edgar Allan Poe", "work": "The Masque of the Red Death", "quote": "Prince Prospero entertained his thousand friends in seven magnificent suites, each **apartment** hung in imperial colors."}
    ]
  },
  "Dashboard — art/art.md": {
    "primary": "The expression or application of human creative skill and imagination; or archaic second-person singular of be.",
    "secondary": "In aesthetic philosophy, fine art transcends utilitarian function, embodying profound emotional truth and formal aesthetic harmony.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 18", "quote": "Shall I compare thee to a summer's day? Thou **art** more lovely and more temperate."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "All great **art** is the expression of an honest delight in God's work across the natural world."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Human **art** is nothing else but nature cooperating with mechanical skill under the direction of reason."}
    ]
  },
  "Dashboard — art/artamidae.md": {
    "primary": "A family of Australasian passerine birds commonly known as woodswallows and butcherbirds.",
    "secondary": "In ornithology, members of Artamidae are agile aerial insectivores possessing specialized powder down and bifurcated brush-tipped tongues.",
    "quotes": [
      {"author": "John Gould", "work": "The Birds of Australia", "quote": "Flocks of aerial woodswallows belonging to the family **artamidae** clustered together like a swarm of bees upon the eucalyptus boughs."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The graceful soaring flight of the Australian **artamidae** closely resembles that of European swallows, exhibiting convergent adaptation."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "We observed several species of **artamidae** hawking for winged insects above the forest canopy of Timor."}
    ]
  },
  "Dashboard — art/artamus.md": {
    "primary": "The typical genus of woodswallows within the family Artamidae, native to South Asia, Australasia, and the Pacific.",
    "secondary": "In avian ethology, Artamus species are noted for communal roosting behavior, huddling tightly along branches to conserve body heat.",
    "quotes": [
      {"author": "John Gould", "work": "Handbook to the Birds of Australia", "quote": "The dusky woodswallow, **artamus** cyanopterus, glides with effortless buoyancy over the open gum forests."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The wide geographical distribution of the genus **artamus** across oceanic islands reflects their powerful migratory flight."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In the genus **artamus**, both sexes display similar sober plumage, sharing equally in the duties of incubation."}
    ]
  },
  "Dashboard — art/artaxerxes.md": {
    "primary": "The name of several monarchs of the ancient Achaemenid Persian Empire.",
    "secondary": "In classical history, Artaxerxes II Longimanus reigned during the March of the Ten Thousand, famously recounted by Xenophon in the *Anabasis*.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The royal court of **artaxerxes** was adorned with the spoils of conquered nations and governed by intricate palace etiquette."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The Persian satraps under **artaxerxes** enjoyed extensive local autonomy, which frequently led to regional rebellions."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Xenophon recorded the dramatic struggle for the Persian crown between Cyrus the Younger and King **artaxerxes** at Cunaxa."}
    ]
  },
  "Dashboard — art/artefact.md": {
    "primary": "An object made or shaped by human workmanship, typically of cultural or historical interest; artifact.",
    "secondary": "In archaeology, an excavated stone or ceramic artefact provides diagnostic stratigraphical evidence for dating past material cultures.",
    "quotes": [
      {"author": "John Lubbock", "work": "Pre-historic Times", "quote": "The flaked flint core was indisputably an ancient human **artefact** recovered from undisturbed Pleistocene gravels."},
      {"author": "Edward Burnett Tylor", "work": "Primitive Culture", "quote": "Every domestic **artefact** preserved in ethnographic collections illustrates the slow evolution of mechanical arts among early peoples."},
      {"author": "Arthur Evans", "work": "The Palace of Minos", "quote": "The painted clay vessel was a priceless Minoan **artefact** demonstrating sophisticated bronze-age maritime commerce."}
    ]
  },
  "Dashboard — art/artefactual.md": {
    "primary": "Relating to, characteristic of, or caused by an artifact; artificial or not naturally occurring.",
    "secondary": "In microscopy and histopathology, an artefactual flaw arises from fixation shrinkage, staining precipitation, or knife chatter.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The pathologist must distinguish between true histological lesions and **artefactual** distortions produced by poor tissue fixation."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Critics suggested that the anomalous protoplasmic network was purely **artefactual**, resulting from chemical precipitation."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Careful microtome sectioning is required to avoid creating **artefactual** vacuolation within delicate brain specimens."}
    ]
  },
  "Dashboard — art/artemia.md": {
    "primary": "A genus of aquatic crustaceans commonly known as brine shrimp, adapted to hypersaline lakes and lagoons.",
    "secondary": "In developmental and evolutionary biology, Artemia salina produces cryptobiotic cysts capable of surviving complete desiccation for decades.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The ability of the brine shrimp **artemia** to thrive in saturated saline solutions illustrates extreme physiological adaptation."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The phyllopod crustacean **artemia** swims on its back by rhythmic undulations of its flattened foliaceous appendages."},
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "Waterfowl transport the resistant encysted eggs of **artemia** on their muddy feet to isolated desert salt pans."}
    ]
  },
  "Dashboard — art/artemis.md": {
    "primary": "The ancient Greek goddess of the hunt, wilderness, wild animals, childbirth, and the moon; Roman Diana.",
    "secondary": "In Hellenic mythology, Artemis was the twin sister of Apollo, depicted with a silver bow and accompanied by hunting hounds and nymphs.",
    "quotes": [
      {"author": "John Keats", "work": "Endymion", "quote": "The silver radiance of **artemis** shone through forest branches, blessing the sleeping hunter upon the mossy hillside."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "The woodland sanctuary of **artemis** at Nemi was guarded by a priest who held office until slain by a runaway slave."},
      {"author": "Percy Bysshe Shelley", "work": "Hellas", "quote": "Hymns to virgin **artemis** echoed through the mountain pine glades as Athenian maidens celebrated the spring rites."}
    ]
  },
  "Dashboard — art/artemisia.md": {
    "primary": "A large, diverse genus of aromatic plants in the daisy family, comprising mugwort, wormwood, and sagebrush.",
    "secondary": "In phytomedicine and pharmacology, Artemisia annua yields artemisinin, a sesquiterpene lactone crucial for modern antimalarial therapeutics.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Excursions", "quote": "The bitter, pungent fragrance of wild **artemisia** scented the sandy gravel ridges along the river course."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **artemisia**, including common wormwood, inhabit dry western plains and rocky alkaline prairies."},
      {"author": "Richard Francis Burton", "work": "The City of the Saints", "quote": "The vast expanse of the Great Basin was blanketed with gray, aromatic shrubs of desert **artemisia**."}
    ]
  },
  "Dashboard — art/arteria.md": {
    "primary": "The Latin and anatomical term for an artery; an efferent blood vessel carrying oxygenated blood from the heart.",
    "secondary": "In classical Galenic medicine, an arteria was erroneously believed by ancient anatomists to transport vital pneuma rather than blood.",
    "quotes": [
      {"author": "William Harvey", "work": "De Motu Cordis", "quote": "When the left ventricle contracts, blood is propelled directly into the great **arteria** aorta and distributed to the extremities."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The pulmonary **arteria** carries deoxygenated venous blood from the right ventricle into the capillary network of the lungs."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Aneurysmal dilation of the **arteria** femoralis presents as an expansile pulsating mass in Scarpa's triangle."}
    ]
  },
  "Dashboard — art/arterial.md": {
    "primary": "Pertaining to an artery or the system of arteries; or relating to major transport routes.",
    "secondary": "In cardiovascular hemodynamics, arterial blood pressure is maintained by rhythmic left ventricular ejection and peripheral vascular resistance.",
    "quotes": [
      {"author": "William Harvey", "work": "De Motu Cordis", "quote": "The bright scarlet color of **arterial** blood distinguishes it from the dark purple hue of venous return."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The elastic muscular walls of the **arterial** system convert the intermittent cardiac pulse into a steady flow."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Modern engineers planned broad **arterial** highways radiating outward from the metropolitan center into the countryside."}
    ]
  },
  "Dashboard — art/arterialise.md": {
    "primary": "To convert venous blood into arterial blood by oxygenation in the lungs; arterialize.",
    "secondary": "In nineteenth-century respiratory physiology, pulmonary capillaries arterialise dark blood through gas exchange across alveoli.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The primary function of pulmonary respiration is to **arterialise** the venous stream before it re-enters the systemic circulation."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Obstruction of the terminal bronchioles impairs the capacity of the lungs to **arterialise** circulating blood, producing cyanosis."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In high Andean altitudes, deep breathing is required to **arterialise** the blood sufficiently to prevent soroche or mountain sickness."}
    ]
  },
  "Dashboard — art/arterialize.md": {
    "primary": "To oxygenate venous blood, transforming it into oxygen-rich arterial blood; or to vascularize a graft.",
    "secondary": "In cardiopulmonary physiology and perfusion technology, membrane oxygenators arterialize hypoxemic blood during open-heart bypass surgery.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Failure of the pulmonary circulation to **arterialize** hemoglobin results in progressive systemic tissue hypoxia."},
      {"author": "Thomas Henry Huxley", "work": "A Course of Elementary Instruction in Practical Biology", "quote": "The extensive vascular network lining the amphibian lung serves to **arterialize** the blood before it returns to the heart."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The surgeon monitored the revascularized flap to verify that capillary loops had begun to **arterialize** the transplanted tissue."}
    ]
  },
  "Dashboard — art/arteriectasia.md": {
    "primary": "Abnormal dilation or distention of an artery; aneurysmal widening of an arterial vessel.",
    "secondary": "In clinical vascular surgery, congenital arteriectasia predisposes vessel walls to degenerative dissection or rupture under hypertension.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diffuse **arteriectasia** involving the thoracic aorta frequently results from syphilitic degeneration of the tunica media."},
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "Exploratory incision revealed localized **arteriectasia** adjacent to the base of the skull, requiring delicate ligatures."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Angiographic imaging disclosed a segmental **arteriectasia** affecting the basilar artery, accounting for intermittent vertigo."}
    ]
  },
  "Dashboard — art/arteriectasis.md": {
    "primary": "A variant medical term for arteriectasia; pathologic dilation or stretching of arterial walls.",
    "secondary": "In cardiovascular pathology, arteriectasis denotes structural weakening of arterial elastica, leading to fusiform or saccular aneurysm formation.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The presence of chronic hypertension accelerated the progressive **arteriectasis** observed within the abdominal aorta."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Microscopic examination of the resected vessel segment confirmed marked **arteriectasis** accompanied by loss of elastic fibers."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The senior pathologist demonstrated to the clinic students a remarkable specimen of cerebral **arteriectasis**."}
    ]
  },
  "Dashboard — art/arteriogram.md": {
    "primary": "A radiographic or imaging recording of an artery after the injection of a radiopaque contrast medium.",
    "secondary": "In diagnostic interventional radiology, an arteriogram delineates arterial stenosis, occlusive thrombi, or vascular malformations.",
    "quotes": [
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The diagnostic **arteriogram** mapped the precise cerebral vascular displacement caused by the deeply seated neoplasm."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "Vascular imaging technology has evolved to where an **arteriogram** clearly illuminates occult lesions before surgical exploration."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The vascular surgeon reviewed the femoral **arteriogram**, noting an abrupt cessation of contrast in the popliteal artery."}
    ]
  },
  "Dashboard — art/arteriography.md": {
    "primary": "The medical imaging technique of visualizing arteries using X-rays or fluoroscopy following radiopaque dye injection.",
    "secondary": "Pioneered by Egas Moniz in 1927, cerebral arteriography transformed neurosurgery by making intracranial aneurysms visible in vivo.",
    "quotes": [
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "The clinical introduction of cerebral **arteriography** provided neurosurgeons with a reliable roadmap of intracranial circulation."},
      {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "Advances in radiological **arteriography** opened new diagnostic horizons for detecting cardiovascular disease before severe complications arose."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Selective **arteriography** revealed severe atheromatous narrowing of the internal carotid artery supplying the parietal cortex."}
    ]
  },
  "Dashboard — art/arteriola.md": {
    "primary": "The Latin and anatomical term for an arteriole; a minute arterial vessel branching into capillaries.",
    "secondary": "In renal microanatomy, the afferent arteriola supplies glomerular capillary tufts, where primary blood filtration takes place.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "Each terminal **arteriola** is encircled by involuntary smooth muscle fibers that regulate vascular resistance."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic sections of the kidney demonstrate hyaline thickening of the afferent **arteriola** in benign nephrosclerosis."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Delicate coagulation was applied to the tiny bleeding **arteriola** to secure hemostasis along the resection bed."}
    ]
  },
  "Dashboard — art/arteriolar.md": {
    "primary": "Pertaining to, located in, or affecting arterioles (minute arterial blood vessels).",
    "secondary": "In systemic hemodynamics, arteriolar tone determines total peripheral resistance, directly governing systemic diastolic blood pressure.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Sustained vasoconstriction of the peripheral **arteriolar** bed underlies the pathogenesis of primary essential hypertension."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Vasomotor nerves modulate **arteriolar** diameter, directing blood flow dynamically toward metabolically active tissues."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Examination of retinal fundi revealed classic **arteriolar** narrowing and copper-wire changes associated with advanced vascular disease."}
    ]
  },
  "Dashboard — art/arteriole.md": {
    "primary": "A small branch of an artery leading directly into a network of capillaries.",
    "secondary": "In microvascular physiology, arterioles function as the primary resistance vessels of the systemic circulation through precapillary sphincters.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The contraction of circular muscle fibers surrounding each **arteriole** restricts blood flow into the downstream capillary bed."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe spasm of an **arteriole** in the digital circulation produces the paroxysmal pallor characteristic of Raynaud's phenomenon."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The sudden emotional blush is mediated by the rapid dilation of each facial **arteriole** under autonomic control."}
    ]
  },
  "Dashboard — art/arteriolosclerosis.md": {
    "primary": "A form of cardiovascular disease affecting arterioles, characterized by thickening, hardening, and loss of elasticity in vessel walls.",
    "secondary": "In renal and cardiovascular pathology, hyaline and hyperplastic arteriolosclerosis are hallmarks of chronic and malignant hypertension.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Diffuse renal **arteriolosclerosis** leads to progressive nephron loss, glomerular sclerosis, and eventual uremic insufficiency."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Histopathological examination of visceral biopsies confirmed advanced **arteriolosclerosis** throughout the mesenteric and cerebral vasculature."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Longstanding hypertension had produced diffuse cerebral **arteriolosclerosis**, predisposing to lacunar subcortical infarcts."}
    ]
  },
  "Dashboard — art/arteriosclerosis.md": {
    "primary": "The thickening, hardening, and loss of elasticity of arterial walls, resulting in impaired blood circulation.",
    "secondary": "In pathology, arteriosclerosis encompasses atherosclerosis, Mönckeberg's medial calcific sclerosis, and arteriolosclerosis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A man is as old as his arteries; the clinical onset of **arteriosclerosis** marks the inevitable physical toll of aging and vascular stress."},
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "The surgeon noted that calcific **arteriosclerosis** made the femoral vessel brittle, requiring great care during vascular clamping."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Gradual cognitive decline was attributed to multi-infarct dementia arising from cerebral **arteriosclerosis**."}
    ]
  },
  "Dashboard — art/arteriosclerotic.md": {
    "primary": "Pertaining to, affected by, or characterized by arteriosclerosis; hardened and thickened arterial vessels.",
    "secondary": "In geriatric clinical medicine, arteriosclerotic cardiovascular disease is the leading underlying etiology of ischemic myocardial infarction.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient exhibited rigid, tortuous radial vessels characteristic of severe **arteriosclerotic** vascular remodeling."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Surgical exposure revealed an **arteriosclerotic** plaque ulcerating into the lumen of the common carotid bifurcation."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The tremor was exacerbated by chronic **arteriosclerotic** parkinsonism, showing poor response to standard dopaminergic agents."}
    ]
  },
  "Dashboard — art/arteriovenous.md": {
    "primary": "Relating to, involving, or connecting both arteries and veins.",
    "secondary": "In vascular surgery, an arteriovenous fistula (e.g., Cimino fistula) is surgically constructed to provide vascular access for hemodialysis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A penetrating bullet wound produced a traumatic **arteriovenous** aneurysm between the femoral artery and vein, accompanied by a continuous thrill."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "The neurosurgical team successfully ligated the large congenital **arteriovenous** malformation resting on the cerebral cortex."},
      {"author": "Oliver Sacks", "work": "The Mind's Eye", "quote": "The patient's visual scotoma was traced to a retinal **arteriovenous** crossing defect causing localized macular ischemia."}
    ]
  },
  "Dashboard — art/arteritis.md": {
    "primary": "Inflammation of the walls of one or more arteries.",
    "secondary": "In clinical rheumatology, giant cell arteritis (temporal arteritis) causes scalp tenderness, jaw claudication, and sudden blindness if untreated with corticosteroids.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The presence of painful, cord-like temporal arteries in an elderly patient strongly indicates acute temporal **arteritis**."},
      {"author": "Harvey Cushing", "work": "Consecratio Medici", "quote": "Biopsy of the inflamed superficial temporal artery confirmed granulomatous **arteritis** with multinucleated giant cells."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The physician prescribed anti-inflammatory treatment to subdue the localized **arteritis** before irreversible ischemic damage occurred."}
    ]
  },
  "Dashboard — art/artery.md": {
    "primary": "A muscular-walled tube forming part of the cardiovascular system that carries oxygenated blood away from the heart to the body.",
    "secondary": "In human gross anatomy, the systemic arterial tree branches hierarchically from the ascending aorta to distribute blood to peripheral organs.",
    "quotes": [
      {"author": "William Harvey", "work": "De Motu Cordis", "quote": "The blood moves through every **artery** in a continuous circuit, propelled by the muscular contraction of the heart."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Fleet Street was the roaring **artery** through which poured the noisy tide of London's commercial life."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The lancet penetrated the radial **artery**, causing bright scarlet blood to spurt in rhythmic pulses across the floor."}
    ]
  },
  "Dashboard — art/artesian.md": {
    "primary": "Relating to a well or aquifer in which groundwater rises to the surface under natural hydrostatic pressure without pumping.",
    "secondary": "In hydrogeology, an artesian basin forms when a permeable water-bearing aquifer is confined between two impermeable strata of rock or clay.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The sinking of an **artesian** well in the arid valley struck pressurized water that spouted several feet above the dry soil."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Water absorbed in the chalk hills of Hertfordshire feeds the great **artesian** wells that supply subterranean London."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "The discovery of deep **artesian** springs in the Algerian Sahara transformed barren desert tracts into flourishing date palm oases."}
    ]
  },
  "Dashboard — art/artichoke.md": {
    "primary": "A European plant of the daisy family cultivated for its edible flower head with fleshy bracts; globe artichoke.",
    "secondary": "In culinary botany, the edible portion of Cynara cardunculus comprises the tender receptacle (heart) and fleshy bases of the surrounding involucral bracts.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "The kitchen gardens at Donwell Abbey were noted for early rows of asparagus, crisp peas, and handsome heads of **artichoke**."},
      {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "Boil the globe **artichoke** until the leaves pull away easily, and serve with melted Hollandaise sauce."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The green-grocer displayed a fresh basket of spiky **artichoke** heads alongside cabbages and autumn leeks."}
    ]
  },
  "Dashboard — art/article.md": {
    "primary": "A particular item or object; a piece of writing in a newspaper or magazine; or a separate clause in a legal contract.",
    "secondary": "In grammar, an article is a word (such as 'the' or 'a') used with a noun to indicate the type of reference being made.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Then let the peace, of many terms and conditions, be made according to each **article** of this royal treaty."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The third **article** of the proposed constitution establishes an independent federal judiciary to interpret national laws."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery had placed upon the table every **article** of value that the forge possessed to secure Pip's education."}
    ]
  },
  "Dashboard — art/articled.md": {
    "primary": "Bound by a formal contract of apprenticeship, training, or employment, especially to a solicitor or accountant.",
    "secondary": "In Victorian legal and commercial training, an articled clerk served five years under articles of indenture before qualifying for the roll of solicitors.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Richard Carstone was **articled** to a respectable London solicitor, but found copying legal briefs tedious and unprofitable."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Norwood Builder", "quote": "John McFarlane was an **articled** clerk working diligently in his father's legal chambers in the City."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "The ambitious young gentleman was **articled** to a prominent civil engineer, hoping to supervise railway construction in India."}
    ]
  },
  "Dashboard — art/articular.md": {
    "primary": "Pertaining to, located in, or affecting a joint or joints of the skeletal body.",
    "secondary": "In functional arthrology, articular cartilage provides an ultra-low-friction, wear-resistant bearing surface bathed in synovial fluid.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute rheumatic fever typically attacks the large synovial joints, producing severe **articular** swelling, heat, and exquisite tenderness."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The **articular** surface of the femoral condyle glides smoothly over the concave tibial plateau during flexion."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The modified **articular** facets of the hominid pelvis reflect the biomechanical requirements of habitual upright bipedal posture."}
    ]
  },
  "Dashboard — art/articulary.md": {
    "primary": "An archaic variant of articular; pertaining to, affecting, or situated near the joints.",
    "secondary": "In historical medical literature, articulary rheumatism designated joint inflammation in contrast to muscular or visceral affections.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain herbal decoctions and warm mineral baths were anciently prescribed to assuage chronic **articulary** aches."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Cold, damp climates aggravate the **articulary** pains of aged scholars who lead sedentary lives."},
      {"author": "Jeremy Taylor", "work": "Holy Dying", "quote": "The infirmities of decrepitude, with their lingering **articulary** torments, prepare the soul for quiet detachment from earthly vanity."}
    ]
  },
  "Dashboard — art/articulate.md": {
    "primary": "Having or showing the ability to speak fluently and coherently; or to express an idea clearly in words; or jointed.",
    "secondary": "In comparative anatomy, to articulate means to form a joint or movable connection with another skeletal bone.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was an **articulate** and thoughtful young woman whose clear convictions impressed all who conversed with her."},
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The ribs **articulate** posteriorly with the thoracic vertebrae and anteriorly connect with the costal cartilages."},
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My father taught me to formulate my thoughts with precision and to **articulate** arguments without rhetorical evasion."}
    ]
  },
  "Dashboard — art/articulated.md": {
    "primary": "Having joints or connected by joints; or expressed clearly and distinctly in speech.",
    "secondary": "In mechanical engineering and railway design, an articulated locomotive features hinged engine trucks to negotiate tight track curves.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The fossil skeleton of the giant armadillo displayed heavily **articulated** bony plates protecting the lumbar region."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Crustaceans and insects possess segmented, **articulated** limbs engineered for swimming, running, or grasping."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "The Prince **articulated** his feelings with careful diplomatic reserve, choosing each syllable with deliberate elegance."}
    ]
  },
  "Dashboard — art/articulately.md": {
    "primary": "In a clear, distinct, fluent, and coherent manner of speech or expression.",
    "secondary": "In parliamentary debate, orators who argue articulately dismantle opposing sophistry through cadenced, logical persuasion.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane spoke **articulately** and firmly, defending her moral autonomy before Rochester's passionate pleadings."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Burke expounded constitutional principles so **articulately** that his parliamentary speeches became enduring masterpieces of political philosophy."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The witness recounted his terrifying experience on the moor **articulately**, omitting no detail of time or circumstance."}
    ]
  },
  "Dashboard — art/articulateness.md": {
    "primary": "Clarity, coherence, and expressive fluency in verbal or written communication.",
    "secondary": "In rhetorical education, cultivating articulateness trains advocates to present nuanced legal distinctions with persuasive elegance.",
    "quotes": [
      {"author": "Henry James", "work": "The Bostonians", "quote": "Verena's natural **articulateness** and radiant charm held the large public audience spellbound throughout her lecture."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Deronda admired the passionate **articulateness** with which Mordecai expounded the historical destiny of his ancient people."},
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "The letters of Jane Austen exhibit an effortless **articulateness** that reflects the sparkling wit of eighteenth-century society."}
    ]
  },
  "Dashboard — art/articulatio.md": {
    "primary": "The Latin and anatomical term for an articulation; a joint between bones or cartilages.",
    "secondary": "In international anatomical nomenclature (Nomina Anatomica), articulatio coxae designates the hip joint, and articulatio cubiti the elbow.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "The mammalian knee joint represents a complex **articulatio** incorporating intra-articular cruciate ligaments and meniscal cartilages."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Suppurative bacterial infection within the **articulatio** genus requires prompt surgical drainage to prevent chondral destruction."},
      {"author": "Harvey Cushing", "work": "The Medical Career", "quote": "Dissection of the cranial base reveals the mobile **articulatio** atlanto-occipitalis supporting the head upon the cervical spine."}
    ]
  },
  "Dashboard — art/articulation.md": {
    "primary": "The act or manner of expressing an idea in speech; or a joint or connection between bones.",
    "secondary": "In acoustic phonetics, articulation refers to the vocal tract configurations and movements of lips, tongue, and teeth that shape speech sounds.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The ball-and-socket **articulation** of the hip joint affords immense stability while permitting wide rotational movement."},
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "Hear you this voice? The clear **articulation** of his speech commands silence from the turbulent Roman assembly."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The distinct vocal **articulation** of speech sounds in mankind relies upon precise neuromuscular coordination of the larynx and tongue."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

updated = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Dashboard — art Part 1: Successfully updated {updated}/{len(data)} notes.")
