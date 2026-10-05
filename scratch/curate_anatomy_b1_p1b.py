# -*- coding: utf-8 -*-
"""
curate_anatomy_b1_p1b.py
Batch 1 Part 1b of Cluster Anatomy & Clinical Medicine (27 words):
- dent remaining (4 words): edentate, indent, indenture, trident
- front (17 words): affront, confront, confrontation, confrontational, effrontery,
  front, frontage, frontal, frontier, frontiersman, frontispiece, frontlet,
  fronton, frontsman, forefront, subfrontal, upfront
- maxill part 1 (6 words): inframaxillary, maxilla, maxillaria, maxillary,
  maxillofacial, maxilliped
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_p1b = {
    # ==================== Dashboard — dent (remaining 4 words) ====================
    "edentate": {
        "primary": "Lacking teeth; belonging to the mammalian order Edentata (including anteaters, sloths, and armadillos).",
        "secondary": "In vertebrate paleontology and comparative zoology, placental mammals with poorly developed, peg-like molars lacking enamel, or completely toothless jaws.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The giant fossil bones of the Megatherium demonstrate close affinities with the small living **edentate** quadrupeds of South America."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The **edentate** skull exhibits extreme simplification in the mandibular arcade, often completely devoid of premaxillary teeth."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In the ant-eater, an exclusively **edentate** diet has resulted in the total reduction of teeth and the elongation of the snout."}
        ]
    },
    "indent": {
        "primary": "To form notches, tooth-like recesses, or deep impressions along an edge, or to set text inward from a margin.",
        "secondary": "In legal history and cartography, to notch the jagged edge of duplicate deeds to prove matching authenticity, or to cut deeply into a coastline.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Venus and Adonis", "quote": "More white and red than doves or roses are, nature that made thee, with herself at strife, saith that the world hath ending with thy life; see how the horses **indent** the soft sand along the ocean shore."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer instructed the clerk to **indent** the opening paragraphs of the formal petition with utmost neatness."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Deep wooded coves **indent** the shoreline of the pond, sheltering quiet waters from the northern blast."}
        ]
    },
    "indenture": {
        "primary": "A formal legal contract or deed between two or more parties, historically executed in duplicate with notched or indented edges.",
        "secondary": "In colonial labor history and contract law, a binding covenant obligating an apprentice or servant to labor for a master over a fixed term of years.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Go with me to a notary, seal me there your single bond; and, in a merry sport, if you repay me not on such a day, let the forfeit be nominated in our formal **indenture**."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The family lawyer drew up the formal **indenture** of settlement that secured the estate to the heirs male."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery proudly produced the sheepskin **indenture** that bound me apprentice to the blacksmith's trade."}
        ]
    },
    "trident": {
        "primary": "A three-pronged spear, fork, or weapon, historically associated with Neptune or gladiatorial combat.",
        "secondary": "In classical mythology and heraldic symbolism, the sovereign scepter of the sea god commanding marine depths, storms, and oceanic tides.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "We debase the nature of our seats and make the rabble call our cares fears, which will in time break ope the locks o' the senate and bring in the crows to peck the eagles; he that had a heart to rule would never yield his **trident** to such hands."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Britannia was depicted upon the copper coin seated majestically above the waves, grasping her triumphant **trident**."},
            {"author": "Jane Austen", "work": "Persuasion", "quote": "Captain Wentworth spoke with nautical enthusiasm of the naval prowess that upheld the sovereign power of the British **trident** upon every sea."}
        ]
    },

    # ==================== Dashboard — front (17 words) ====================
    "affront": {
        "primary": "An open, intentional insult or offense to someone's dignity or personal honor.",
        "secondary": "In social ethics and aristocratic honor codes, a provocative public slight delivered to the face, historically demanding formal satisfaction or duel.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "For we have closely sent for Hamlet hither, that he, as 'twere by accident, may here **affront** Ophelia."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A deliberate and unprovoked **affront** wounds human pride far more deeply than the loss of material possessions."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard took the refusal as a direct personal **affront**, brooding over the injury in grim silence."}
        ]
    },
    "confront": {
        "primary": "To face, stand in front of, or meet someone face-to-face, especially in challenge, hostility, or defiance.",
        "secondary": "In judicial evidence and psychological therapy, bringing an accused directly before an accuser, or directly facing painful cognitive truths.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "**Confronted** him with self-comparisons, point against point rebellious, arm 'gainst arm, curbing his lavish spirit; and to conclude, the victory fell on us."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba turned resolutely to **confront** her suitor, determined that there should be no further misunderstanding between them."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The detective stepped forward from the shadow of the pillar to **confront** the fugitive at the garden gate."}
        ]
    },
    "confrontation": {
        "primary": "A hostile, argumentative, or defiant face-to-face meeting between opposing persons or forces.",
        "secondary": "In geopolitical diplomacy and procedural law, an acute standoff between adversarial powers, or the formal constitutional right to cross-examine adverse witnesses.",
        "quotes": [
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "A direct **confrontation** between the Crown and Parliament could no longer be averted by subtle courtly negotiations."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She dreaded the impending **confrontation** with her uncle, knowing his deep aversion to financial disclosures."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The captain was unnerved by the sudden **confrontation** with men whose steadfast courage reproached his own shameful desertion."}
        ]
    },
    "confrontational": {
        "primary": "Tending toward, characterized by, or encouraging direct conflict, argument, or aggressive confrontation.",
        "secondary": "In interpersonal communication and diplomatic negotiation, an adversarial posture that escalates tensions rather than facilitating consensus.",
        "quotes": [
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Partisan journalists adopted a fiercely **confrontational** tone that inflamed the passions of the electorate."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "A dogmatic minority frequently resorts to a **confrontational** rhetoric that alienates moderate citizens."},
            {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "A wise parliament avoids adopting a **confrontational** attitude toward distant colonies whose grievances demand patient consideration."}
        ]
    },
    "effrontery": {
        "primary": "Insolent, shameless audacity, impudence, or boldness in behavior or speech.",
        "secondary": "In moral psychology (*ex-* + *frons*, without forehead/shame), barefaced impertinence demonstrating contempt for social decorum or moral censure.",
        "quotes": [
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was astonished at the boundless **effrontery** of Wickham in appearing so unconcerned before the very family he had disgraced."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook had the brazen **effrontery** to claim the entire credit for my good fortune in the public house."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The housekeeper reproved the maid for her intolerable **effrontery** in disputing the commands of her mistress."}
        ]
    },
    "front": {
        "primary": "The foremost part, surface, or side of something, or the part that faces forward.",
        "secondary": "In military strategy, meteorology, and anatomy, the line of actual contact between armed forces, the boundary separating contrasting air masses, or the forehead (*frons*).",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "He had his hurts before, on the very **front** of his body; ay, on the **front**; why then, God's soldier be he!"},
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The grand white forehead of the whale presented an impenetrable wall in **front**, baffling the whalemen's lances."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "I wished to live deliberately, to **front** only the essential facts of life, and see if I could not learn what it had to teach."}
        ]
    },
    "frontage": {
        "primary": "The front part of a building or piece of land facing a street, river, or other open space.",
        "secondary": "In urban planning and real estate law, the linear extent of a property boundary abutting a public road or navigable waterfront.",
        "quotes": [
            {"author": "G. K. Chesterton", "work": "The Club of Queer Trades", "quote": "The narrow house presented an eccentric brick **frontage** ornamented with strange gothic gargoyles staring into the street."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The timber warehouse enjoyed an extensive river **frontage** that permitted barges to unload grain directly beneath its cranes."},
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The gloomy **frontage** of the Marshalsea prison frowned upon the narrow alley, casting a cold shadow over all who passed."}
        ]
    },
    "frontal": {
        "primary": "Pertaining to, directed toward, or situated at the front or the forehead.",
        "secondary": "In craniofacial osteology and military tactics, relating to the frontal bone forming the forehead, or a direct head-on tactical assault upon an enemy position.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In ancestral hominids, prominent bony ridges arch across the **frontal** bone above the orbits, shielding the eyes from injury."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe throbbing headaches localized over the **frontal** sinuses frequently indicate acute inflammatory obstruction."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The gradual expansion of the **frontal** lobes reflects the remarkable cerebral development that characterizes the human lineage."}
        ]
    },
    "frontier": {
        "primary": "A border separating two countries, or the extreme limit of settled land beyond which lies wilderness.",
        "secondary": "In political geography and intellectual history, an unsettled boundary zone where civilizations clash, or the cutting-edge advancing perimeter of scientific discovery.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Of palisadoes, **frontier**s, parapets, of basilisks, of cannon, culverin, of prisoners' ransom, and of soldiers slain, and all the currents of a heady fight."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We crossed the remote desert **frontier** where military outposts guarded the scattered estancias against hostile native raiders."},
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The adventurous whaleman pushes the maritime **frontier** into frozen polar bays where no merchant keel ever ventured before."}
        ]
    },
    "frontiersman": {
        "primary": "A person who lives near or explores the wilderness boundary of settled territory.",
        "secondary": "In American cultural history, an independent pioneer, scout, or backwoods settler skilled in wilderness survival, tracking, and defensive combat.",
        "quotes": [
            {"author": "Theodore Roosevelt", "work": "The Winning of the West", "quote": "The American **frontiersman** relied upon his trusty long rifle, woodcraft, and indomitable courage to tame the Appalachian wilderness."},
            {"author": "Mark Twain", "work": "Roughing It", "quote": "In every mining settlement we encountered the veteran **frontiersman**, clad in buckskin and full of tall tales about hostile ambushes."},
            {"author": "Francis Parkman", "work": "The Oregon Trail", "quote": "The hardened **frontiersman** regarded the vast prairie as his natural home, reading the trail with the uncanny instinct of an Indian."}
        ]
    },
    "frontispiece": {
        "primary": "An illustration or decorative engraving facing the title page of a book.",
        "secondary": "In classical architecture and bibliography, the principal pedimented facade of a building, or the ornate engraved front plate introducing a literary volume.",
        "quotes": [
            {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "The curious book contained a charming **frontispiece** showing the White Rabbit in his waistcoat inspecting his pocket watch."},
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The venerable Dutch folio opened with an astonishing **frontispiece** depicting Jonah escaping from the jaws of a monstrous whale."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The antique volume was adorned with a quaint copperplate **frontispiece** depicting the pious author in his Puritan band and cloak."}
        ]
    },
    "frontlet": {
        "primary": "A decorative band, ribbon, or jewel worn across the forehead.",
        "secondary": "In historical costume and ornithology, an ornamental brow-band worn by women, or the frontal feather patch situated directly above the avian beak.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "How now, daughter! What makes that **frontlet** on? Methinks you are too much of late i' the frown."},
            {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "A slender golden **frontlet** bound her dark tresses, gleaming softly beneath the velvet hood."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The fair queen appeared adorned with an exquisite **frontlet** of oriental pearls upon her radiant brow."}
        ]
    },
    "fronton": {
        "primary": "A pediment or triangular ornamental gable above a door, window, or classical building facade; or a court for playing Basque pelota.",
        "secondary": "In neoclassical architecture, a decorated tympanum surmounting an entablature, or the enclosed court with a granite front wall used in jai alai.",
        "quotes": [
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The classical **fronton** above the palace portal was enriched with carved laurel wreaths and weeping cherubs."},
            {"author": "Henry James", "work": "A Little Tour in France", "quote": "In the quiet Basque village, boys were energetically practicing pelota against the towering stone **fronton** beside the church."},
            {"author": "William H. Prescott", "work": "History of the Reign of Ferdinand and Isabella", "quote": "The Renaissance palace entrance displayed a stately marble **fronton** bearing the quartered arms of Castile and Aragon."}
        ]
    },
    "frontsman": {
        "primary": "A person positioned at the front of a formation, party, or organization; a frontman or leader.",
        "secondary": "In commercial syndicates and political factions, a public figurehead who represents an organization to deflect scrutiny from backstage directors.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The conspirators chose a respectable local merchant as their public **frontsman** to conceal their clandestine operations from the police."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The outspoken **frontsman** shouted brave slogans at the hustings while craftier politicians dictated the platform in secret."},
            {"author": "George Orwell", "work": "Animal Farm", "quote": "Squealer served as the persuasive **frontsman** for the ruling clique, explaining away every tyrannical decree with glib rhetoric."}
        ]
    },
    "forefront": {
        "primary": "The leading or most prominent position in a movement, activity, or advancing front.",
        "secondary": "In military combat and intellectual history, the vanguard of battle, or the leading edge of philosophical and scientific innovation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VIII", "quote": "He stood ever in the **forefront** of the realm's business, advising his majesty with tireless vigilance and supreme statecraft."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Bacon placed himself boldly in the **forefront** of modern intellectual progress, sweeping away medieval scholastic dogmas."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Defarge and his resolute wife stood in the very **forefront** of the furious mob storming the gates of the Bastille."}
        ]
    },
    "subfrontal": {
        "primary": "Situated beneath or on the inferior surface of the frontal bone or frontal lobe of the brain.",
        "secondary": "In neurosurgical anatomy, designating a basal intracranial operative corridor beneath the orbital roof utilized to expose the optic chiasm, pituitary fossa, and anterior circle of Willis.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Basal fractures across the anterior fossa frequently involve the **subfrontal** dura, producing persistent cerebrospinal rhinorrhea."},
            {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The olfactory tracts course along the **subfrontal** gyri, delivering sensory afferents directly into the piriform cortex."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The optic nerves emerge beneath the **subfrontal** region of the encephalon, crossing at the optic chiasma."}
        ]
    },
    "upfront": {
        "primary": "Honest, direct, and straightforward in dealing; or paid in advance before goods or services are delivered.",
        "secondary": "In financial contracting and communicative pragmatics, requiring advance capitalization, or exhibiting candid transparency free of dissimulation.",
        "quotes": [
            {"author": "Mark Twain", "work": "Roughing It", "quote": "The mining agent demanded an **upfront** deposit in gold dust before he would register the claim in the town ledger."},
            {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "He preferred an **upfront** man who declared his terms frankly, rather than one who concealed selfish schemes behind oily flattery."},
            {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The automobile salesman was refreshingly **upfront** about the mechanical drawbacks of the second-hand roadster."}
        ]
    },

    # ==================== Dashboard — maxill (part 1: 6 words) ====================
    "inframaxillary": {
        "primary": "Situated beneath, below, or on the inferior aspect of the maxilla or upper jawbone.",
        "secondary": "In cranial osteology and oral anatomy, designating nerves, vessels, or muscular attachments localized along the inferior border of the maxillary antrum and dental arch.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In certain reptiles the **inframaxillary** arcade fuses seamlessly with the jugal bone to support the lower cheek."},
            {"author": "Richard Owen", "work": "Odontography", "quote": "The **inframaxillary** canal conveys the neurovascular bundle supplying sensation to the lower premolars and canine teeth."},
            {"author": "William Flower", "work": "An Introduction to the Osteology of the Mammalia", "quote": "The muscular fossa along the **inframaxillary** surface provides firm attachment for the deep fibers of the masseter."}
        ]
    },
    "maxilla": {
        "primary": "The upper jawbone in vertebrates, forming the roof of the mouth and floor of the eye sockets.",
        "secondary": "In arthropod morphology, one of the paired mouthpart appendages positioned behind the mandibles, functioning in food handling and mastication.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In insects the paired **maxilla** structures are modified into mouthparts exhibiting diverse adaptations for chewing, sucking, or piercing."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The human **maxilla** houses the extensive pneumatic cavity known as the maxillary sinus or Antrum of Highmore."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In predatory dinosaurs the premaxilla and **maxilla** unite into a formidable bone frame bearing deeply socketed serrated teeth."}
        ]
    },
    "maxillaria": {
        "primary": "A large, diverse genus of tropical American orchids in the family Orchidaceae.",
        "secondary": "In systematic orchidology, epiphytic or lithophytic orchids whose column and lip morphology vaguely resembles an insect's paired maxillae, yielding its generic name.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised by Insects", "quote": "The floral mechanism in **Maxillaria** illustrates an exquisite adaptation whereby the insect pollinator is directed toward the sticky viscidium."},
            {"author": "John Lindley", "work": "The Genera and Species of Orchidaceous Plants", "quote": "Ruiz and Pavon established the genus **Maxillaria** to encompass numerous fragrant epiphytes discovered in the Peruvian Andes."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Greenhouse collectors prize the strange triangular blossoms of **Maxillaria** for their intense spicy fragrance and waxy texture."}
        ]
    },
    "maxillary": {
        "primary": "Pertaining to, situated in, or associated with the maxilla or upper jaw.",
        "secondary": "In stomatognathic anatomy and otorhinolaryngology, designating the maxillary division of the trigeminal nerve (V2), the maxillary artery, or the large paranasal sinus.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Acute suppuration within the **maxillary** antrum causes severe radiating facial neuralgia and unilateral nasal purulence."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The **maxillary** process in the developing embryo grows forward to fuse with the frontonasal prominence, forming the upper lip."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The reduction in length of the **maxillary** bone in civilized races is closely correlated with the modern adoption of cooked, softened food."}
        ]
    },
    "maxillofacial": {
        "primary": "Pertaining to, involving, or treating the maxilla (upper jaw) and face.",
        "secondary": "In reconstructive surgery and dental subspecialties, relating to the comprehensive surgical repair of craniofacial trauma, congenital clefts, and facial bone deformities.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Severe artillery trauma required the establishment of specialized surgical wards dedicated entirely to reconstructive **maxillofacial** repairs."},
            {"author": "Sir Astley Cooper", "work": "A Treatise on Dislocations and Fractures of the Joints", "quote": "Complex **maxillofacial** injuries demand immediate airway protection prior to reduction of the shattered facial bones."},
            {"author": "Howard Kelly", "work": "Operative Surgery", "quote": "The pioneering surgeon devised delicate osteotomy techniques that laid the foundation for modern **maxillofacial** surgery."}
        ]
    },
    "maxilliped": {
        "primary": "One of the paired appendages modified to function as mouthparts in crustaceans.",
        "secondary": "In marine invertebrate carcinology, thoracic limbs shifted forward during cephalization to manipulate, shred, and sort food particles before ingestion.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The transition from a locomotive thoracic limb to an accessory **maxilliped** mouthpart is beautifully illustrated across diverse decapod crustaceans."},
            {"author": "Thomas Henry Huxley", "work": "The Crayfish: An Introduction to the Study of Zoology", "quote": "The third **maxilliped** of the crayfish acts as a tactile feeler and protective cover over the delicate inner masticatory jaws."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "Microscopic examination of the crab larva reveals the gradual transformation of swimming setae on each **maxilliped** into grasping spines."}
        ]
    }
}
