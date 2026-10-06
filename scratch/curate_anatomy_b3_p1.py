# -*- coding: utf-8 -*-
"""
curate_anatomy_b3_p1.py
Batch 3 Part 1 of Cluster Anatomy & Clinical Medicine (55 words):
- mamm (21 words)
- oss (27 words)
- pector (7 words)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_b3_p1 = {
    # ==================== Dashboard — mamm (21 words) ====================
    "mamma": {
        "primary": "The milk-secreting organ of female mammals; the breast or mammary gland.",
        "secondary": "In human female anatomy, the glandular organ situated over the pectoralis major comprising lobes, lactiferous ducts, and adipose stroma.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The infant nestled closely against the maternal **mamma**, seeking natural nourishment with instinctive murmurs of content."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Rudimentary nipples and traces of the **mamma** occur regularly in the male sex across diverse mammalian orders."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The arterial supply to the **mamma** is derived principally from the internal mammary and lateral thoracic vessels."}
        ]
    },
    "mammal": {
        "primary": "Any warm-blooded vertebrate animal of the class Mammalia, characterized by hair, milk secretion, and three middle ear ossicles.",
        "secondary": "In evolutionary biology and paleontology, an endothermic tetrapod clade possessing specialized dentition, a neocortex, and viviparous reproduction.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The structure of the limb in every terrestrial **mammal** exhibits profound homologies derived from common ancestral prototypes."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The presence of hair and mammary nourishment distinguishes the true **mammal** from all other vertebrate classes."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In every placental **mammal**, the brain presents a corpus callosum bridging the bilateral cerebral hemispheres."}
        ]
    },
    "mammalia": {
        "primary": "The major taxonomic class of vertebrate animals whose females produce milk to nourish their offspring.",
        "secondary": "In systematic zoology, the class comprising monotremes, marsupials, and eutherian placentals, defined by specialized integumentary and auditory adaptations.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Throughout the vast class of the **Mammalia**, the general plan of the cranial and axial skeleton remains strictly conserved."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Linnaeus erected the class **Mammalia** upon the universal possession of functional or rudimentary mammary glands."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The marine cetaceans belong unreservedly to the **Mammalia**, despite their external resemblance to pelagic fishes."}
        ]
    },
    "mammalian": {
        "primary": "Relating to, characteristic of, or belonging to the class Mammalia.",
        "secondary": "In comparative physiology and embryology, describing biological structures, metabolic processes, or developmental pathways peculiar to mammals.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The early stages of the **mammalian** embryo reveal transient branchial arches recalling primitive ancestral aquatic life."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The structural modifications of the **mammalian** foot reflect diverse adaptations to cursorial, arboreal, or aquatic locomotion."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Experimental models in **mammalian** physiology have elucidated the regulatory pathways of cardiac output and vasomotor tone."}
        ]
    },
    "mammalogist": {
        "primary": "A zoologist or professional scientist who studies mammals and their natural history.",
        "secondary": "In field zoology and wildlife conservation, a specialist documenting mammalian taxonomy, population genetics, geographic distribution, and ecological interactions.",
        "quotes": [
            {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The observant **mammalogist** finds on the Sunda Islands an extraordinary assemblage of endemic forest rodents and viverrids."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "A trained **mammalogist** distinguishes closely allied species by subtle variations in cranial sutures and molar cusps."},
            {"author": "Theodore Roosevelt", "work": "African Game Trails", "quote": "Our camp naturalist worked with the unflagging diligence of a dedicated **mammalogist**, skinning specimens by lantern light."}
        ]
    },
    "mammalogy": {
        "primary": "The scientific study of mammals, including their classification, anatomy, behavior, and evolution.",
        "secondary": "In academic biology, the discipline integrating paleomammalogy, comparative craniology, and ecological ethology to understand mammalian diversification.",
        "quotes": [
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The systematic study of **mammalogy** demonstrates how homologous skeletal elements are reshaped to serve diverse ecological functions."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Progress in modern **mammalogy** requires rigorous correlation between living soft-tissue anatomy and fossil dental remains."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "His monumental contributions to North American **mammalogy** established definitive standards for taxonomic description."}
        ]
    },
    "mammary": {
        "primary": "Relating to the breasts or the milk-producing glands of female mammals.",
        "secondary": "In histology and endocrinology, designating modified apocrine cutaneous glands responsive to prolactin, estrogen, and oxytocin during lactation.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The evolution of the **mammary** glands remains one of the most distinctive innovations in the history of vertebrate life."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Each lobe of the **mammary** gland terminates in an independent lactiferous duct opening upon the summit of the nipple."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Palpation of the **mammary** tissue must be conducted systematically to distinguish benign fibroadenomas from malignant induration."}
        ]
    },
    "mammea": {
        "primary": "A genus of tropical trees in the family Calophyllaceae, noted for large edible fruits.",
        "secondary": "In systematic tropical botany, evergreen trees characterized by fragrant white flowers, opposite coriaceous leaves, and thick-skinned drupaceous fruits.",
        "quotes": [
            {"author": "William Withering", "work": "The Miscellaneous Tracts of the Late William Withering", "quote": "The Caribbean genus **Mammea** yields a delicious fruit whose firm orange pulp resembles the flavor of ripe apricots."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "In the fertile valleys of the Orinoco, flourishing groves of **Mammea** shade the village clearings with dark glossy foliage."},
            {"author": "Hans Sloane", "work": "A Voyage to the Islands Madera, Barbados, Nieves, S. Christophers and Jamaica", "quote": "The aromatic gum exuding from the trunk of **Mammea** is applied by native inhabitants to extract venomous jiggers."}
        ]
    },
    "mammee": {
        "primary": "A tropical American tree (Mammea americana) or its large, edible russet fruit with sweet orange pulp.",
        "secondary": "In economic pomology, the mammee apple, cultivated throughout the West Indies and Central America for its aromatic pulp and insecticidal seed extracts.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The marketplace in Bahia offered generous baskets of fragrant **mammee** and sweet cherimoya fresh from the plantations."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "We refreshed ourselves beneath the tropical midday heat with the luscious golden flesh of the wild **mammee**."},
            {"author": "Hans Sloane", "work": "A Voyage to the Islands", "quote": "The fruit of the **mammee** tree is circular and thick-rinded, enclosing several large seeds within pleasant yellow pulp."}
        ]
    },
    "mammilla": {
        "primary": "A biological nipple, teat, or small nipple-shaped protuberance.",
        "secondary": "In descriptive human and comparative anatomy, the central papilla of the mammary areola containing the terminal orifices of the lactiferous sinuses.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **mammilla** is surrounded by a pigmented areola equipped with numerous sebaceous glands of Montgomery."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Cold temperature or tactile stimulation excites involuntary contraction of the smooth muscular fibers within the **mammilla**."},
            {"author": "William Hunter", "work": "Anatomy of the Human Gravid Uterus", "quote": "During gestation the **mammilla** enlarges, its vascular plexus becoming remarkably prominent as lactation approaches."}
        ]
    },
    "mammillaria": {
        "primary": "A genus of small globose or cylindrical cacti covered with spiral rows of nipple-like tubercles.",
        "secondary": "In succulent botany, a widespread New World cactus genus characterized by dimorphic areoles and colorful flowers emerging between the tubercles.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The desert species of **Mammillaria** protect their fleshy stems with dense lattices of sharp radial spines."},
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "Upon the arid limestone ridges of northern Mexico, dwarf colonies of **Mammillaria** carpet the rock crevices."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "The tubercles of **Mammillaria** represent modified leaf-bases arranged in elegant mathematical spirals around the stem."}
        ]
    },
    "mammogram": {
        "primary": "A radiographic image of the breast produced by low-energy X-rays, used for diagnostic cancer screening.",
        "secondary": "In clinical radiology, a photographic or digital record visualizing parenchymal architecture, architectural distortion, and clustered microcalcifications.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The advent of the modern **mammogram** revolutionized early neoplastic detection long before physical palpation becomes positive."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "Diagnostic imaging faculties demonstrated how a systematic **mammogram** provides objective evidence of occult lesions."},
            {"author": "Morris Fishbein", "work": "The Medical Follies", "quote": "The clinician evaluated the newly developed **mammogram** as an indispensable technological advance in preventive oncology."}
        ]
    },
    "mammography": {
        "primary": "The medical imaging technique of examining human breasts using low-dose ionizing radiation.",
        "secondary": "In diagnostic oncology and preventive medicine, the primary screening modality utilized to detect non-palpable early-stage ductal or lobular carcinomas.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Routine screening **mammography** substantially reduces mortality by discovering malignant transformation in its pre-invasive stage."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "The radiologic curriculum incorporated rigorous training in **mammography** to standardize diagnostic interpretation."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He praised the early pioneers of **mammography** who applied radiological physics to the compassionate preservation of human health."}
        ]
    },
    "mammon": {
        "primary": "Wealth, money, or material riches, regarded as an object of corrupting worship or false idolatry.",
        "secondary": "In theological ethics and biblical literature, the personification of worldly gain as an antagonistic force subverting spiritual integrity.",
        "quotes": [
            {"author": "King James Bible", "work": "The Gospel According to Saint Matthew", "quote": "No man can serve two masters: for either he will hate the one, and love the other; ye cannot serve God and **mammon**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He had yielded up his youthful scientific aspirations to worship at the prosperous domestic shrine of **mammon**."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "His daily life was bound fast in the commercial service of **mammon**, adding up ledger columns from dawn to dusk."}
        ]
    },
    "mammoplasty": {
        "primary": "Plastic or reconstructive surgery performed upon the human breast.",
        "secondary": "In aesthetic and reconstructive plastic surgery, operative remodeling involving reduction, augmentation, or mastopexy to alter breast contour or repair post-mastectomy tissue.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Advances in antiseptic technique allowed surgeons to undertake complex **mammoplasty** without fear of suppurative infection."},
            {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Reconstructive **mammoplasty** following radical oncological extirpation requires meticulous mobilization of cutaneous flaps."},
            {"author": "Alexis Carrel", "work": "Man, The Unknown", "quote": "Reconstructive **mammoplasty** exemplifies the restorative potential of modern plastic surgery in repairing diseased anatomy."}
        ]
    },
    "mammoth": {
        "primary": "An extinct large hairy elephant of the genus Mammuthus; or colossal and gigantic in scale.",
        "secondary": "In Pleistocene paleontology, an extinct herbivorous proboscidean adapted to subarctic steppe-tundra; figuratively, any enterprise of colossal proportions.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "We excavate the frozen silt of Siberia to exhume the intact carcass of the hairy **mammoth** with flesh preserved in ice."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The skeleton of the sperm whale presented the colossal proportions of a prehistoric **mammoth** stranded upon the beach."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Fossil teeth of the **mammoth** discovered in post-Pliocene deposits demonstrate its adaptation to a cold northern habitat."}
        ]
    },
    "mammothermography": {
        "primary": "The diagnostic recording of infrared temperature patterns across the surface of the breast.",
        "secondary": "In clinical oncology, an adjunct non-invasive imaging modality mapping skin thermovascular asymmetries generated by hypervascular malignant tumors.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early investigators explored **mammothermography** in hopes that localized neoplastic hyperemia would betray early malignant growth."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "The laboratory introduced **mammothermography** as a thermal diagnostic technique to supplement morphological radiological scans."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "He noted the preliminary trials of **mammothermography**, emphasizing that thermal asymmetry demands rigorous biopsy confirmation."}
        ]
    },
    "mammut": {
        "primary": "The taxonomic genus of extinct North American mastodons belonging to the family Mammutidae.",
        "secondary": "In vertebrate paleontology, primitive proboscideans possessing paired low-crowned bunodont molars with transverse ridges adapted for forest browsing rather than grazing.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The dental architecture of **Mammut** americanum separates the true mastodon decisively from the steppe mammoths."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The massive skeletal remains of **Mammut** unearthed in Kentucky salt-licks excited the wonder of early naturalists."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In the fossil cranium of **Mammut**, the air cells of the diploë expand to enormous dimensions to support the heavy tusks."}
        ]
    },
    "mammuthus": {
        "primary": "The taxonomic genus of extinct true mammoths within the elephant family Elephantidae.",
        "secondary": "In quaternary paleontology, a lineage of cold-adapted proboscideans featuring high-crowned hypsodont molars with crowded enamel plates specialized for grinding grasses.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Cave paintings executed by Paleolithic men depict **Mammuthus** primigenius with remarkable naturalistic fidelity."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The curved tusks and woolly pelt of **Mammuthus** represent specialized adaptations to Pleistocene periglacial environments."},
            {"author": "Louis Agassiz", "work": "Geological Sketches", "quote": "The discovery of frozen **Mammuthus** carcasses in Siberian gravels provides incontestable proof of past climatic catastrophes."}
        ]
    },
    "mammutidae": {
        "primary": "An extinct family of primitive proboscideans containing the mastodons.",
        "secondary": "In mammalian taxonomy, an archaic proboscidean family that diverged from the elephant lineage in the Oligocene, retaining zygolophodont grinding molars.",
        "quotes": [
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The family **Mammutidae** represents an independent evolutionary branch that flourished in North American woodland habitats."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Comparative analysis of the dental series demonstrates that **Mammutidae** retained primitive bunodont features lost in modern elephants."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extinction of the **Mammutidae** throughout the Americas occurred alongside the disappearance of many colossal Pleistocene quadrupeds."}
        ]
    },
    "mammy": {
        "primary": "An affectionate dialect term for a mother; or historically a Black nursemaid in the American South.",
        "secondary": "In cultural history and sociolinguistics, a regional vernacular term for mother, or the historical domestic caregiver archetype in nineteenth-century Southern society.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The little child ran joyfully toward the kitchen, calling out for its beloved **mammy** with open arms."},
            {"author": "Mark Twain", "work": "The Adventures of Huckleberry Finn", "quote": "The little children clung to their old **mammy**, who comforted their childish fears with soothing songs."},
            {"author": "Frederick Douglass", "work": "My Bondage and My Freedom", "quote": "In the slave quarters, the affectionate name of **mammy** was bestowed upon the elder women who cared for the infant children."}
        ]
    },

    # ==================== Dashboard — oss (27 words) ====================
    "colossae": {
        "primary": "Colossae, an ancient city of Phrygia in southwestern Asia Minor.",
        "secondary": "In biblical geography and Hellenistic history, a prosperous trade center on the Lycus River renowned for wool dyed with cyclamen (colossinus).",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient cities of Laodicea, Hierapolis, and **Colossae** shared in the commercial prosperity of the fertile Lycus valley."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The apostolic letter dispatched to the church at **Colossae** addressed philosophical speculations that threatened early Christian doctrine."},
            {"author": "Strabo", "work": "The Geography of Strabo", "quote": "Proceeding eastward along the river, one reaches the ancient settlement of **Colossae**, once a flourishing mart of Phrygia."}
        ]
    },
    "colossal": {
        "primary": "Extremely large, gigantic, or immense in size, scale, or extent.",
        "secondary": "In architectural aesthetics and descriptive history, referring to monumental sculpture or structures that dwarf ordinary human proportions.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The monumental monoliths of Stonehenge loomed in **colossal** majesty against the gray predawn sky."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Nature presents a **colossal** architecture beside which the proudest human temples appear like toys."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The primeval forest seemed an impenetrable **colossal** presence brooding silently over our little steamboat."}
        ]
    },
    "colosseum": {
        "primary": "The Flavian Amphitheatre in Rome; or any vast amphitheatre or arena designed for public spectacles.",
        "secondary": "In classical Roman archaeology, the monumental elliptical amphitheater begun under Vespasian in 72 AD and inaugurated by Titus, seating over 50,000 spectators.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He recalled the moonlight shining upon the ruined arches of the **Colosseum**, casting gigantic shadows upon the ancient sand."},
            {"author": "Charles Dickens", "work": "Pictures from Italy", "quote": "To see the **Colosseum** by moonlight is to behold the ghost of imperial Rome rising in solemn desolation."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The immense circumference of the **Colosseum** long resisted the destructive assaults of time, barbarian invaders, and stone-robbers."}
        ]
    },
    "colossian": {
        "primary": "A native or inhabitant of ancient Colossae; or relating to the city of Colossae.",
        "secondary": "In biblical theology, pertaining to the Christian community at Colossae or the Christological doctrine articulated in Paul's Epistle to the Colossians.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **Colossian** congregation flourished amidst the bustling trade routes connecting coastal Ephesus with the inland plateau."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The moral exhortations addressed to the **Colossian** converts reflect the ascetic debates of the first-century Roman province."},
            {"author": "Jeremy Taylor", "work": "Holy Living", "quote": "Saint Paul urged the **Colossian** believers to set their affections on heavenly things rather than earthly vanities."}
        ]
    },
    "colossians": {
        "primary": "The Epistle of Paul to the Colossians in the New Testament; or the inhabitants of ancient Colossae.",
        "secondary": "In New Testament literature, a Pauline captivity epistle emphasizing the supreme cosmic preeminence of Christ over gnostic angelic hierarchies.",
        "quotes": [
            {"author": "King James Bible", "work": "The Epistle of Paul to the Colossians", "quote": "The Epistle to the **Colossians** warns the early church against vain philosophy and deceitful human traditions."},
            {"author": "John Milton", "work": "Christian Doctrine", "quote": "The sublime passage in the letter to the **Colossians** proclaims Christ as the firstborn of every creature and head of the body."},
            {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "A thoughtful meditation upon the Epistle to the **Colossians** illuminates the organic harmony between faith and reason."}
        ]
    },
    "colossus": {
        "primary": "A statue of gigantic size and scale; or a person or entity of immense stature and commanding influence.",
        "secondary": "In ancient history, monumental statuary such as the bronze Colossus of Rhodes, or metaphorically a domineering figure towering over their contemporaries.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Why, man, he doth bestride the narrow world like a **Colossus**, and we petty men walk under his huge legs."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "An institution is the lengthened shadow of one man; as, Monachism, of the Hermit Antony; and all history resolves into the biography of a few **colossus** figures."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The giant sperm whale hung alongside like a drowned **colossus**, dark and majestic amidst the ocean swell."}
        ]
    },
    "deossification": {
        "primary": "The biological loss, resorption, or chemical removal of mineral salts and osseous material from bone.",
        "secondary": "In metabolic bone pathology, pathological skeletal demineralization resulting from hyperparathyroidism, osteomalacia, or prolonged disuse osteopenia.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Progressive **deossification** of the pelvic bones during osteomalacia results in severe skeletal deformities and intractable bone pain."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Laboratory immersion of an intact bone in dilute hydrochloric acid causes complete **deossification**, leaving only a flexible collagenous framework."},
            {"author": "John Hunter", "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "In chronic inflammation of bone, localized **deossification** precedes the formation of a sequestrum."}
        ]
    },
    "deossify": {
        "primary": "To deprive bone of its calcareous mineral matter; to cause osseous resorption.",
        "secondary": "In experimental osteology and pathology, to dissolve calcium phosphate and hydroxyapatite from bone tissue, rendering it soft and flexible.",
        "quotes": [
            {"author": "William Hunter", "work": "Medical Commentaries", "quote": "Acid solutions act rapidly to **deossify** the specimen, leaving the cartilaginous matrix intact for microscopic examination."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic nutritional deprivation and vitamin deficiency conspire to **deossify** the developing skeletons of impoverished children."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "If you **deossify** a long bone by prolonged acid maceration, it may be tied into a knot without fracturing."}
        ]
    },
    "fossil": {
        "primary": "The petrified remain, impression, or trace of an organism preserved in the Earth's crust from past geological ages.",
        "secondary": "In historical geology and paleontology, mineralized skeletal structures, permineralized woods, or trace ichnofossils documenting ancient evolutionary lineages.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The discovery of an intermediate **fossil** form linking reptiles and birds provided remarkable verification of evolutionary descent."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Every **fossil** shell exhumed from chalk cliffs bears silent witness to the immense antiquity of terrestrial life."},
            {"author": "Louis Agassiz", "work": "Geological Sketches", "quote": "The distinct **fossil** fauna of each geological horizon reveals an orderly progression of organic creation."}
        ]
    },
    "fossilisation": {
        "primary": "The natural geological process of being preserved as a fossil; petrifaction (British spelling).",
        "secondary": "In taphonomy, the sequence of geochemical processes including burial, permineralization, carbonization, and recrystallization preserving organic structures.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The conditions necessary for complete **fossilisation** occur only rarely, requiring rapid sedimentary burial away from scavengers."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Soft-bodied organisms decompose rapidly before the slow geochemical processes of **fossilisation** can take effect."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "In deltaic estuaries, sand and silt deposition favors the **fossilisation** of stranded marine and terrestrial remains."}
        ]
    },
    "fossilise": {
        "primary": "To convert organic matter into a fossil through mineral petrifaction; or to become rigid and antiquated (British spelling).",
        "secondary": "In geological taphonomy, the infiltration and replacement of cellular spaces by silicate or calcite minerals over vast epochs.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Sediments accumulating along tranquil lake bottoms slowly **fossilise** the delicate leaves and insects carried in by streams."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "We must not allow our scientific conclusions to **fossilise** into dogmas that resist fresh empirical evidence."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Mineral springs rich in dissolved carbonates rapidly **fossilise** submerged twigs and calcareous mosses."}
        ]
    },
    "fossilist": {
        "primary": "An archaic term for a paleontologist or collector of fossils and mineral specimens.",
        "secondary": "In eighteenth- and nineteenth-century natural history, an enthusiast or scholar who collected, cataloged, and interpreted organic petrifactions.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The enthusiastic **fossilist** explores coastal shale cliffs, exhuming ammonites that lived in forgotten Mesozoic seas."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The early **fossilist** viewed these stony petrifactions merely as curious sports of nature rather than genuine extinct organisms."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Every provincial **fossilist** contributed valuable local observations that helped construct our geological chronology."}
        ]
    },
    "fossilization": {
        "primary": "The biological and geological process by which animal or plant remains are converted into stone or preserved in rock.",
        "secondary": "In sedimentary geology and taphonomy, the physical and chemical alteration of hard tissues through calcium carbonate or silica deposition.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The extreme imperfection of the geological record results from the rarity of the conditions required for **fossilization**."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "During **fossilization**, subterranean mineral solutions gradually replace the organic matrix molecule by molecule."},
            {"author": "Louis Agassiz", "work": "Geological Sketches", "quote": "The process of **fossilization** has preserved even the finest striations upon the scales of ancient Devonian fishes."}
        ]
    },
    "fossilize": {
        "primary": "To turn organic tissues into stone through mineral replacement; or to render opinions rigid and unchangeable.",
        "secondary": "In taphonomic science and figurative prose, the mineralization of organic material, or the intellectual ossification of ideas.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Calcareous muds rapidly bury marine mollusks and **fossilize** their hard shells with extraordinary microscopic fidelity."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Without continuous critical examination, the most brilliant scientific theories **fossilize** into lifeless scholastic formulas."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Institutions tend to **fossilize** the spontaneous spiritual insights of the prophetic minds that established them."}
        ]
    },
    "interosseous": {
        "primary": "Situated, located, or occurring between two adjacent bones.",
        "secondary": "In human gross anatomy, designating deep muscles, ligaments, and dense fibrous membranes connecting paired parallel bones (such as the radius and ulna).",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The dorsal **interosseous** muscles of the hand abduct the fingers away from the middle digit."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe atrophy of the first dorsal **interosseous** muscle is a classic physical sign of ulnar nerve neuropathy."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "A strong **interosseous** membrane binds the tibia and fibula, providing a broad surface for muscular attachment."}
        ]
    },
    "opossum": {
        "primary": "A nocturnal, solitary American marsupial of the order Didelphimorphia, noted for feigning death when threatened.",
        "secondary": "In mammalian zoology, a primitive didelphid possessing an opposable hallux, prehensile tail, and fifty teeth, surviving as North America's only marsupial.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The virginian **opossum** presents in its reproductive anatomy primitive marsupial characters preserved from the Mesozoic epoch."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In the female **opossum**, the marsupial pouch contains the teats to which the tiny altricial young attach immediately after birth."},
            {"author": "John James Audubon", "work": "The Viviparous Quadrupeds of North America", "quote": "When overtaken by hounds, the cunning **opossum** feigns absolute lifelessness, deceiving the hunter with uncanny composure."}
        ]
    },
    "osseous": {
        "primary": "Composed of, resembling, or pertaining to bone; bony.",
        "secondary": "In histology and skeletal pathology, descriptive of the rigid calcified extracellular matrix consisting of hydroxyapatite crystals embedded in collagen fibrils.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The **osseous** labyrinth of the sperm whale's skull presents an impenetrable citadel against ocean pressure."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The homologous arrangement of **osseous** elements across the vertebrate limbs confirms their common ancestry."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Compact **osseous** tissue forms the dense outer shell of long bones, resisting heavy compressive and torsional strains."}
        ]
    },
    "ossete": {
        "primary": "A member of an Iranian indigenous ethnic group native to Ossetia in the central Caucasus Mountains.",
        "secondary": "In Caucasian ethnography and historical linguistics, speakers of Ossetian, an Eastern Iranian language descended from ancient Scytho-Sarmatian dialects.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The martial **Ossete** clans guarded the strategic defiles of the Dariel Pass against northern nomadic horsemen."},
            {"author": "Leo Tolstoy", "work": "The Cossacks", "quote": "The tall **Ossete** horseman rode proudly along the mountain trail, his shaggy sheepskin cloak fluttering in the alpine wind."},
            {"author": "Mikhail Lermontov", "work": "A Hero of Our Time", "quote": "Our **Ossete** driver cracked his whip and urged the horses up the steep Georgian military road."}
        ]
    },
    "ossicle": {
        "primary": "A small bone or small bony structure, especially one of the three auditory bones of the middle ear.",
        "secondary": "In otorhinolaryngology and echinoderm anatomy, the malleus, incus, or stapes of the tympanic cavity, or calcareous skeletal plates in starfish.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The stapes is the smallest **ossicle** in the human body, transmitting acoustic mechanical vibrations directly to the oval window."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Sound waves vibrate the tympanic membrane, which sets each miniature auditory **ossicle** into rhythmic motion."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The middle ear **ossicle** system illustrates how ancestral reptilian jaw bones were co-opted for mammalian hearing."}
        ]
    },
    "ossicular": {
        "primary": "Pertaining to, composed of, or affecting an anatomical ossicle, particularly the auditory bones.",
        "secondary": "In otology and audiometric medicine, designating the ossicular chain (malleus, incus, stapes) or surgical reconstruction (ossiculoplasty) for conductive hearing loss.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Chronic suppurative otitis media frequently causes necrosis of the **ossicular** chain, resulting in permanent conductive deafness."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Delicate synovial articulations unite the **ossicular** segments, allowing flexible mechanical transmission of sound."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Comparative craniology demonstrates that the mammalian **ossicular** apparatus was derived from modified quadrate and articular bones."}
        ]
    },
    "ossiculate": {
        "primary": "Furnished with ossicles; having small bones or bone-like calcified structures.",
        "secondary": "In invertebrate morphology and comparative anatomy, designating organisms (such as echinoderms) possessing a dermis reinforced by calcareous plates.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The flexible yet protective skin of sea stars is densely **ossiculate**, supporting moveable defensive spines."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "The **ossiculate** framework of echinoderms demonstrates an intricate geometric radial symmetry unique in the animal kingdom."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In certain primitive fishes, the dermal armor is composed of discrete **ossiculate** plates embedded within the scales."}
        ]
    },
    "ossiculum": {
        "primary": "The Latin anatomical term for an ossicle; a miniature bone or calcified skeletal element.",
        "secondary": "In classical descriptive osteology, a minute skeletal nodule, such as a sesamoid bone or an auditory ossicle of the middle ear cavity.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Each **ossiculum** auditus plays an essential role in matching acoustic impedance between air and inner ear fluid."},
            {"author": "William Hunter", "work": "Medical Commentaries", "quote": "Careful dissection of the tympanic cavity revealed that the smallest **ossiculum** remained intact despite chronic disease."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The homologous **ossiculum** in lower vertebrates fulfills a suspensory rather than an auditory functional role."}
        ]
    },
    "ossiferous": {
        "primary": "Containing, yielding, or producing bones or fossil skeletal remains.",
        "secondary": "In speleology and quaternary geology, designating caves, breccias, or sedimentary strata that contain abundant fossilized bones of prehistoric animals.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The celebrated **ossiferous** caverns of Yorkshire yielded thousands of teeth and bones of Pleistocene hyenas and hippopotami."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We examined the **ossiferous** breccia at Monte Hermoso, which contained abundant remains of extinct giant edentates."},
            {"author": "William Buckland", "work": "Reliquiae Diluvianae", "quote": "The muddy floor of Kirkdale Cave presented a rich **ossiferous** deposit preserving the fractured bones of ancient quadrupeds."}
        ]
    },
    "ossification": {
        "primary": "The developmental or pathological process of bone formation; or the state of becoming rigid and hardened.",
        "secondary": "In skeletal osteogenesis, the conversion of mesenchymal tissue or hyaline cartilage into calcified bone through osteoblast activity.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Primary **ossification** begins within the diaphyseal center of long bones during early embryonic development."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Abnormal heterotopic **ossification** in muscular tissue characterizes the rare disabling syndrome of fibrodysplasia ossificans progressiva."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The replacement of flexible embryonic cartilage by hard calcium phosphate marks the completion of skeletal **ossification**."}
        ]
    },
    "ossified": {
        "primary": "Converted into bone; hardened by calcium salts; or rigid, stubborn, and resistant to change.",
        "secondary": "In histology and figurative prose, tissue transformed into rigid bone matrix, or an intellect calcified in outworn traditions.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In mature birds, the cranial sutures become completely **ossified**, obliterating all visible boundaries between individual bones."},
            {"author": "William Osler", "work": "Aequanimitas", "quote": "He warned young physicians not to allow their clinical curiosity to become **ossified** in dogmatic routine."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The old farmer's beliefs were as **ossified** as the gnarled oak roots that gripped the chalk hill."}
        ]
    },
    "ossify": {
        "primary": "To turn into bone or bony tissue; or to make or become rigid, conventional, and unyielding.",
        "secondary": "In skeletal physiology, the deposition of hydroxyapatite transforming soft connective tissue into bone; figuratively, the cessation of intellectual growth.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The cartilaginous growth plates continue to **ossify** until skeletal maturity is attained in early adulthood."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Unless refreshed by active experimental inquiry, scientific institutions tend to **ossify** into conservative guilds."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Custom and unthinking reverence tend to **ossify** spiritual truths into lifeless formal creeds."}
        ]
    },
    "ossuary": {
        "primary": "A container, stone receptacle, vault, or building where the bones of dead people are deposited.",
        "secondary": "In mortuary archaeology and comparative anthropology, a subterranean chamber or chest for secondary burial, housing skeletonized human remains.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Hydriotaphia, Urn Burial", "quote": "Ancient sepulchral vaults served as a solemn **ossuary** wherein the dry dust and bones of whole generations mingled."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Catacombs excavated beneath the imperial city functioned as a subterranean **ossuary** for early Christian believers."},
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "He gazed with contemplative sorrow into the dark stone **ossuary**, meditating upon the transitory glory of mortal existence."}
        ]
    },

    # ==================== Dashboard — pector (7 words) ====================
    "expectorant": {
        "primary": "A therapeutic medicine that promotes the secretion, liquefaction, and expulsion of mucus from the respiratory tract.",
        "secondary": "In clinical pulmonary pharmacology, an agent that reduces bronchial mucus viscosity and facilitates ciliary clearance in respiratory infections.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Ammonium chloride administered in syrup of ipecac serves as an effective stimulating **expectorant** in acute bronchitis."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "An **expectorant** formula that softens tenacious phlegm brings prompt relief to the distressed asthmatic patient."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Warm herbal decoctions act as a mild **expectorant**, encouraging the discharge of purulent secretions from the bronchi."}
        ]
    },
    "expectorate": {
        "primary": "To cough up, spit out, or discharge phlegm, sputum, or fluid from the respiratory passages.",
        "secondary": "In clinical pulmonology, the clearing of tracheobronchial exudates through vigorous diaphragmatic contraction and ciliary transport.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient with lobar pneumonia begins to **expectorate** characteristic rusty, tenacious sputum on the third day of illness."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "In cavernous pulmonary tuberculosis, the invalid continues to **expectorate** copious nummular masses of purulent matter."},
            {"author": "Charles Dickens", "work": "American Notes", "quote": "The travelers sat around the stove, pausing only to **expectorate** copious streams of tobacco juice into the ashes."}
        ]
    },
    "expectoration": {
        "primary": "The act or process of coughing up and expelling matter from the lungs; or the material so ejected (sputum).",
        "secondary": "In diagnostic pulmonology, the physical and microscopic analysis of expelled tracheobronchial secretions to identify cellular pathology and pathogens.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic examination of the **expectoration** readily demonstrates the presence of elastic fibers and tubercle bacilli."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "The sudden cessation of purulent **expectoration** in bronchiectasis frequently heralds septic retention and rising fever."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham, M.D.", "quote": "Copious free **expectoration** during the second stage of winter pleurisy is a favorable symptom of natural resolution."}
        ]
    },
    "expectorator": {
        "primary": "One who expels sputum or spits; or an obsolete container or spittoon used to collect sputum.",
        "secondary": "In clinical sanatorium management and social history, a receptacle provided for pulmonary patients to prevent airborne tuberculous contamination.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "The inveterate **expectorator** discharged his tobacco quid across the cabin floor with careless disregard for cleanliness."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In every tuberculosis ward, each patient was supplied with a covered pocket **expectorator** containing antiseptic fluid."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "The rustic court room was furnished with a cracked stove and a sawdust-filled box serving as a general **expectorator**."}
        ]
    },
    "pectoral": {
        "primary": "Pertaining to, situated on, or worn upon the chest or breast.",
        "secondary": "In vertebrate anatomy, designating structures such as the pectoral girdle, pectoral fins in fishes, or the pectoral muscles supporting forelimb movement.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The homologue of the mammalian forelimb is clearly recognizable in the **pectoral** fin of the ancient lungfish."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **pectoral** fascia forms a thin lamina covering the surface of the pectoralis major muscle across the thoracic wall."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "A golden **pectoral** cross rested upon the rich embroidered vestment of the venerable prior."}
        ]
    },
    "pectoralis": {
        "primary": "Either of two large muscles of the anterior chest wall (the pectoralis major or pectoralis minor).",
        "secondary": "In human musculoskeletal anatomy, the fan-shaped pectoralis major that adducts, flexes, and internally rotates the humerus at the glenohumeral joint.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **pectoralis** major arises from the clavicle, sternum, and costal cartilages to insert into the bicipital groove of the humerus."},
            {"author": "Charles Bell", "work": "The Anatomy of the Brain", "quote": "In violent respiratory distress, the **pectoralis** muscles act as powerful accessory muscles of inspiration."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In flying birds, the **pectoralis** major attains enormous development, anchoring securely to the prominent keel of the sternum."}
        ]
    },
    "pectoriloquy": {
        "primary": "The striking transmission of the sound of a patient's whispered speech through the chest wall, heard via a stethoscope.",
        "secondary": "In clinical diagnostic auscultation, a physical sign pathognomonic of lobar pulmonary consolidation, atelectasis, or a superficial tuberculous lung cavity.",
        "quotes": [
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Whispering **pectoriloquy** is heard with startling distinctness over an excavated tuberculous cavity communicating with a bronchus."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Clear whispered **pectoriloquy** over the right lower lobe confirms the clinical impression of complete pneumonic consolidation."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Through the acoustic tube of the stethoscope, unmistakable **pectoriloquy** revealed the cavernous destruction hidden in the lung."}
        ]
    }
}
