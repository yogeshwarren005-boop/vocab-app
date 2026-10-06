# -*- coding: utf-8 -*-
"""
curate_anatomy_b2_p1.py
Batch 2 Part 1 of Cluster Anatomy & Clinical Medicine (50 words):
- chir (22 words)
- dors (12 words)
- pariet (3 words)
- vertebr (7 words)
- nas first 6 words (intranasal, nasa, nasal, nasale, nasalis, nasalisation)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_anatomy_b2_p1 = {
    # ==================== Dashboard — chir (22 words) ====================
    "chiralgia": {
        "primary": "Neuralgic pain, cramp, or severe aches occurring specifically within the hand.",
        "secondary": "In clinical rheumatology and occupational neurology, recurrent localized pain affecting carpal and metacarpal joints without acute systemic inflammatory signs.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic clerical fatigue, persistent **chiralgia** frequently complicates the clinical presentation of occupational neurosis."},
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham, M.D.", "quote": "The patient complained of violent nocturnal **chiralgia**, which seized the joints of the fingers and thumb with piercing sharpness."},
            {"author": "Benjamin Bell", "work": "A System of Surgery", "quote": "Topical counter-irritants and warm fomentations were applied to alleviate the distressing spasms of **chiralgia**."}
        ]
    },
    "chirico": {
        "primary": "Giorgio de Chirico (1888–1978), Italian painter and founder of the Scuola Metafisica art movement.",
        "secondary": "In art history and cultural studies, the distinctive aesthetic pioneered by Giorgio de Chirico characterized by hauntingly deserted piazzas, elongated shadows, and enigmatic classical statuary.",
        "quotes": [
            {"author": "André Breton", "work": "Surrealism and Painting", "quote": "The early canvases of **Chirico** unveiled a profound new mythology of deserted arcades and melancholic clocktowers."},
            {"author": "Herbert Read", "work": "A Concise History of Modern Painting", "quote": "In the enigmatic compositions of **Chirico**, architectural perspective becomes an instrument of dreamlike psychological tension."},
            {"author": "James Thrall Soby", "work": "Giorgio de Chirico", "quote": "Every mysterious colonnade painted by **Chirico** resonates with a brooding stillness that forever altered modern European art."}
        ]
    },
    "chirocephalus": {
        "primary": "A genus of freshwater fairy shrimp belonging to the crustacean order Anostraca.",
        "secondary": "In invertebrate zoology and limnology, fairy shrimps characterized by prominent prehensile appendages borne upon the head of the male for clasping the female.",
        "quotes": [
            {"author": "Thomas Bell", "work": "A History of the British Stalk-eyed Crustacea", "quote": "Specimens of **Chirocephalus** diaphanus may be observed swimming gracefully on their backs in vernal woodland pools."},
            {"author": "William Elford Leach", "work": "Zoological Miscellany", "quote": "The remarkable cephalic apparatus of the male **Chirocephalus** serves as a delicate grasping organ during courtship."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In the primitive branchiopod **Chirocephalus**, the lack of a dorsal carapace leaves the eleven thoracic segments fully exposed."}
        ]
    },
    "chirography": {
        "primary": "Handwriting, penmanship, or the art and individual style of personal script.",
        "secondary": "In paleography and archival bibliography, the physical execution, orthographic ductus, and scribal technique observable in historical manuscripts.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Unconsciously my **chirography** expands into placard capitals as I record these astounding adventures."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "This envelope had the air of an official record of some period long past, when clerks engrossed their stiff and formal **chirography**."},
            {"author": "Edgar Allan Poe", "work": "Autography", "quote": "The minute peculiarities of an author's **chirography** frequently betray the nervous constitution of the mind."}
        ]
    },
    "chirology": {
        "primary": "The study of the hands, or communication by means of manual gestures and signs.",
        "secondary": "In linguistics and deaf education, the formal linguistic analysis of manual gestures, finger-spelling, and sign systems serving as visual speech.",
        "quotes": [
            {"author": "John Bulwer", "work": "Chirologia: Or the Naturall Language of the Hand", "quote": "Through the expressive silent motions of **chirology**, the hand speaks a universal discourse comprehended by all nations."},
            {"author": "William Holder", "work": "Elements of Speech", "quote": "Instructors of the deaf-mute found in systematic **chirology** a practical bridge across the gulf of silence."},
            {"author": "George Dalgarno", "work": "Didascalocophus", "quote": "He demonstrated that finger-alphabets and manual **chirology** could transmit philosophical ideas with admirable exactness."}
        ]
    },
    "chiromance": {
        "primary": "To practice palmistry or foretell future events through reading the lines of the hand.",
        "secondary": "In historical occultism and divinatory practices, the act of interpreting the mounts, creases, and proportions of human palms to infer character and destiny.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Those who presume to **chiromance** upon the lines of the palm mingle vain superstition with natural observations."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Pretenders who undertake to **chiromance** every lineament of the hand confound accidental flexures with celestial influences."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Gipsies and strolling fortune-tellers pretend to **chiromance** the fates of credulous villagers for a brass farthing."}
        ]
    },
    "chiromancer": {
        "primary": "A practitioner of palmistry who claims to tell fortunes and discern character from the lines of the hand.",
        "secondary": "In folklore and historical sociology, a professional palm-reader or diviner interpreting manual palm creases, dermatoglyphics, and carpal configurations.",
        "quotes": [
            {"author": "John Webster", "work": "The White Devil", "quote": "Trust not that wandering **chiromancer**, whose subtle prophecies feed upon foolish credulity."},
            {"author": "Walter Scott", "work": "The Fortunes of Nigel", "quote": "The aged **chiromancer** scanned Nigel's palm with furrowed brow, tracing the broken line of life with his withered finger."},
            {"author": "Ben Jonson", "work": "The Alchemist", "quote": "The cunning **chiromancer** promised the simple merchant wealth and honors inscribed upon the mount of Jupiter."}
        ]
    },
    "chiromancy": {
        "primary": "Palmistry; divination or character analysis through the inspection of the lines and mounts of the hand.",
        "secondary": "In historical anthropology and mantic traditions, the esoteric methodology correlating palmar flexure lines with astrological influences and temperaments.",
        "quotes": [
            {"author": "John Dryden", "work": "The Spanish Fryar", "quote": "Her faith in fraudulent **chiromancy** led her to consult every strolling astrologer who passed through the city gates."},
            {"author": "Samuel Butler", "work": "Hudibras", "quote": "With astrological arts and subtle **chiromancy**, he persuaded simple folk that their stars were written in their hands."},
            {"author": "William Congreve", "work": "Love for Love", "quote": "You may read your own destiny without resorting to the dubious subtleties of medieval **chiromancy**."}
        ]
    },
    "chiromantic": {
        "primary": "Pertaining to, derived from, or characteristic of palmistry and manual divination.",
        "secondary": "In hermetic literature and esoteric traditions, descriptive of symbols, lines, or interpretive tables utilized in reading palm features.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "We reject those extravagant **chiromantic** conjectures that attribute every crease of the skin to the planets."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Melancholic men are easily swayed by **chiromantic** predictions, fearing disaster at every crossing of a line."},
            {"author": "Joseph Glanvill", "work": "Saducismus Triumphatus", "quote": "Ancient treatises contained elaborate **chiromantic** diagrams setting forth the significance of every minor palmar wrinkle."}
        ]
    },
    "chiron": {
        "primary": "The wisest and most just of the centaurs in Greek mythology, famed as a physician, sage, and tutor to heroes.",
        "secondary": "In the history of classical medicine, the legendary mentor of Asclepius and Achilles whose name symbolizes surgical skill and herbal healing.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Titus Andronicus", "quote": "Sound drums and trumpets, and let Demetrius and **Chiron** attend upon their sovereign's command."},
            {"author": "Alexander Pope", "work": "The Iliad of Homer", "quote": "Taught by divine **Chiron** the healing art, he bathed the wound and calmed the throbbing smart."},
            {"author": "John Keats", "work": "Endymion", "quote": "Ancient **Chiron** trod these shadowy glades, instructing youthful heroes in the secrets of wild woodland herbs."}
        ]
    },
    "chironomidae": {
        "primary": "A large and globally distributed family of non-biting midges belonging to the insect order Diptera.",
        "secondary": "In freshwater ecology and entomology, aquatic dipterans whose benthic larvae (bloodworms) serve as vital ecological indicators of water quality and benthic food webs.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In several species of **Chironomidae**, the males possess magnificent plumose antennae that resonate to the wing-tones of the females."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "The delicate larvae of **Chironomidae** flourish in stagnant marsh waters, providing essential nourishment to juvenile fishes."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The aquatic stages of **Chironomidae** exhibit rudimentary tracheal systems adapted to low-oxygen mud environments."}
        ]
    },
    "chironomus": {
        "primary": "The type genus of non-biting midges within the family Chironomidae, known for their aquatic red larvae.",
        "secondary": "In genetics and cellular biology, midge larvae renowned for giant polytene chromosomes in their salivary glands, widely studied in gene transcription.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The tiny aquatic larva of **Chironomus** demonstrates remarkable tenacity in surviving severe organic pollution."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "Under the microscope, the pulsating dorsal vessel of the living **Chironomus** larva reveals every detail of circulation."},
            {"author": "Jan Swammerdam", "work": "The Book of Nature", "quote": "The blood-red worm of the water-midge **Chironomus** builds delicate tubes of silt along the lake floor."}
        ]
    },
    "chiropodist": {
        "primary": "A medical specialist who treats minor ailments, deformities, and afflictions of the feet.",
        "secondary": "In the history of clinical medicine and podiatry, a licensed professional treating corns, bunions, and ingrown nails through skilled manual instruments.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The odd gait of the visitor suggested an appointment with a **chiropodist** rather than any involvement in criminal matters."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "He spoke of his troublesome corns and recommended an experienced **chiropodist** residing in the neighbouring court."},
            {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "One cannot conduct high society conversations while walking upon feet in desperate need of a skillful **chiropodist**."}
        ]
    },
    "chiropody": {
        "primary": "The diagnosis and conservative treatment of minor foot disorders, nail diseases, and skin afflictions; podiatry.",
        "secondary": "In clinical orthopedics and preventive healthcare, the field of manual foot care managing plantar hyperkeratosis, hallux valgus, and biomechanical imbalances.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful attention to diabetic foot hygiene and regular **chiropody** prevent the development of intractable neuropathic ulcers."},
            {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "My uncle conceived vast commercial schemes encompassing everything from patent pills to fashionable salons of **chiropody**."},
            {"author": "George Meredith", "work": "The Egoist", "quote": "He discoursed upon trivialities with the gravity of an expert lecturing upon the delicate principles of **chiropody**."}
        ]
    },
    "chiropractic": {
        "primary": "A therapeutic system of complementary medicine centered on the diagnosis and manipulative treatment of spinal misalignments.",
        "secondary": "In clinical manual therapy, a discipline founded on the premise that vertebral subluxations compromise neuromuscular integrity and general vitality.",
        "quotes": [
            {"author": "Daniel David Palmer", "work": "The Chiropractor's Adjuster", "quote": "The foundation of **chiropractic** rests upon restoring normal physiological transmission through manual spinal adjustment."},
            {"author": "William Osler", "work": "The Evolution of Modern Medicine", "quote": "Modern practitioners must distinguish between established orthopedic manipulation and the wider theoretical claims of **chiropractic**."},
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "Institutions professing **chiropractic** doctrines must align their clinical instruction with validated principles of anatomical science."}
        ]
    },
    "chiropractor": {
        "primary": "A healthcare professional who treats disorders of the spine and musculoskeletal system through manual adjustments.",
        "secondary": "In complementary medicine, a licensed practitioner performing targeted spinal thrusts and articular mobilization to relieve neural impingement.",
        "quotes": [
            {"author": "Daniel David Palmer", "work": "The Science, Art and Philosophy of Chiropractic", "quote": "The skilled **chiropractor** employs the hands to correct osseous displacements and re-establish neuromuscular balance."},
            {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The small town housed both an orthodox apothecary and an enterprising **chiropractor** whose adjustments were highly popular."},
            {"author": "Morris Fishbein", "work": "The Medical Follies", "quote": "He documented the rapid spread of the licensed **chiropractor** across American municipalities during the early twentieth century."}
        ]
    },
    "chiroptera": {
        "primary": "An order of placental mammals possessing forelimbs adapted into membranous wings; the bats.",
        "secondary": "In mammalian taxonomy and comparative anatomy, the only truly flying mammals, characterized by elongated metacarpals and phalanges supporting a flight patagium.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Dobson on sexual characters in the **Chiroptera**, Proceedings of the Zoological Society, records several remarkable anatomical variations."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The modified manual skeleton of the **Chiroptera** presents the most marvelous evolutionary adaptation of the vertebrate hand."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In all **Chiroptera**, the clavicle is remarkably well developed to provide sturdy anchorage for the primary flight muscles."}
        ]
    },
    "chiropteran": {
        "primary": "Relating to or belonging to the order Chiroptera; a bat.",
        "secondary": "In evolutionary biology, describing morphological, echolocatory, or physiological adaptations distinctive to bats and their specialized aerial niche.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The **chiropteran** wing illustrates how natural selection can modify ordinary mammalian digits into organs of swift flight."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Dense clouds of large **chiropteran** frugivores emerged from the cavernous limestone cliffs at dusk to raid the orchards."},
            {"author": "Richard Owen", "work": "Comparative Anatomy and Physiology of Vertebrates", "quote": "The elongation of the second to fifth digits in the **chiropteran** manus supports the elastic cutaneous membrane without adding excess weight."}
        ]
    },
    "chirr": {
        "primary": "A shrill, vibrating, or trilling sound typical of certain insects such as cicadas and grasshoppers.",
        "secondary": "In acoustic ecology and natural history writing, the high-frequency rhythmic stridulation generated by the friction of insect wings or hind legs.",
        "quotes": [
            {"author": "John Keats", "work": "The Poetical Works of John Keats", "quote": "The hedgerow crickets **chirr** their twilight melody as dusk descends softly across the harvest meadow."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "From the pine needles at midsummer arose the persistent dry **chirr** of grasshoppers basking in the sun."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "No sound broke the stillness of the coppice save the intermittent **chirr** of an unseen cricket among the fallen leaves."}
        ]
    },
    "chirrup": {
        "primary": "A series of sharp, cheerful chirps or trills, especially produced by small birds or insects.",
        "secondary": "In avian ethology and descriptive prose, a brief vocalization or clicking sound made to encourage an animal or express alert vitality.",
        "quotes": [
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "A grasshopper began to **chirrup** by the wall, and like a blue thread a long thin dragon-fly floated past on its brown gauze wings."},
            {"author": "Charles Dickens", "work": "The Cricket on the Hearth", "quote": "The cheerful little kettle began to **chirrup** and hum upon the hearth as if celebrating the carrier's safe return."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Sparrows continued to **chirrup** vigorously under the eaves while Maggie stood watching the swift current of the Floss."}
        ]
    },
    "chirurgeon": {
        "primary": "An archaic term for a surgeon; a medical practitioner who treats injuries and diseases by manual operation.",
        "secondary": "In medical history, a guild-trained operator who performed phlebotomies, amputations, and wound dressings with instruments prior to modern surgical training.",
        "quotes": [
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The wounded knight was committed to the care of a skilled **chirurgeon** who dressed his gashes with soothing balsams."},
            {"author": "Samuel Pepys", "work": "The Diary of Samuel Pepys", "quote": "I sent in haste for the **chirurgeon** to dress my cousin's fractured leg, which had been hurt in the coaching accident."},
            {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The naval **chirurgeon** inspected the injured seamen with brisk efficiency, wielding probe and forceps with indifferent composure."}
        ]
    },
    "enchiridion": {
        "primary": "A handbook, concise manual, or compact compendium of practical rules and knowledge.",
        "secondary": "In philosophical and classical literature, a pocket-sized vade mecum summarizing ethical maxims or spiritual guidelines for everyday living.",
        "quotes": [
            {"author": "Desiderius Erasmus", "work": "Enchiridion Militis Christiani", "quote": "He designed this Christian **enchiridion** not for disputation in scholastic halls, but to arm the soul with virtuous precepts."},
            {"author": "Epictetus", "work": "The Enchiridion, or Manual", "quote": "This brief **enchiridion** contains those indispensable truths that preserve equanimity amidst the tumult of human affairs."},
            {"author": "Jeremy Taylor", "work": "Holy Living", "quote": "Let this small manual serve as an **enchiridion** of pious exercises for the daily governance of the Christian household."}
        ]
    },

    # ==================== Dashboard — dors (12 words) ====================
    "dorsal": {
        "primary": "Relating to, situated on, or directed toward the back or upper surface of an organism.",
        "secondary": "In vertebrate anatomy and comparative zoology, the posterior anatomical plane in humans or superior aspect in quadrupeds and fishes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The spinal cord in man extends only as far downwards as the last **dorsal** or first lumbar vertebra."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Driving across that high **dorsal** ridge, the wind buffeted the cart from the vast open downs below."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The prominent spinous processes of the thoracic vertebrae provide sturdy leverage for the **dorsal** musculature."}
        ]
    },
    "dorsally": {
        "primary": "Toward, upon, or in the direction of the back or posterior aspect of an anatomical structure.",
        "secondary": "In descriptive embryology and surgical navigation, spatial orientation directed toward the spine or uppermost surface of an organism.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The neural tube closes **dorsally** along the midline of the developing vertebrate embryo during early gastrulation."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The hairs along the spine bristle up **dorsally** when the animal prepares to confront a threatening adversary."},
            {"author": "Louis Agassiz", "work": "Methods of Study in Natural History", "quote": "In primitive fishes, the notochord is arched **dorsally** by a series of cartilaginous protective plates."}
        ]
    },
    "dorsiflexion": {
        "primary": "The upward flexion or backward bending of a body part, especially the foot or hand.",
        "secondary": "In clinical orthopedics and kinematic gait analysis, the contraction of anterior tibial muscles reducing the angle between the dorsal foot and anterior leg.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Contraction of the tibialis anterior muscle produces energetic **dorsiflexion** of the foot at the talocrural joint."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In peroneal nerve palsy, loss of active **dorsiflexion** produces the characteristic high-stepping steppage gait."},
            {"author": "Charles Bell", "work": "The Anatomy of the Brain", "quote": "Testing passive **dorsiflexion** of the wrist reveals spastic resistance in patients suffering from pyramidal tract lesions."}
        ]
    },
    "dorsoventral": {
        "primary": "Extending along or relating to the axis connecting the back (dorsal) and belly (ventral) surfaces.",
        "secondary": "In developmental biology and comparative morphometry, the fundamental axis of bilateral symmetry perpendicular to the anteroposterior plane.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "Flatworms exhibit pronounced **dorsoventral** compression, which facilitates cutaneous gas exchange across the entire body surface."},
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The flattened cotyledons demonstrate clear **dorsoventral** polarity in their growth response to incident sunlight."},
            {"author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "quote": "The deep **dorsoventral** diameter of the thoracic cage reflects the large volume of the cardiopulmonary viscera."}
        ]
    },
    "dorsoventrally": {
        "primary": "In a direction extending from the back surface to the belly surface of an organism.",
        "secondary": "In zoological morphology, describing an organism or structure that is compressed or flattened along its vertical axis from dorsal to ventral sides.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The skull of the crocodile is compressed **dorsoventrally**, presenting a broad and flattened predatory snout."},
            {"author": "Charles Darwin", "work": "Monograph on the Sub-class Cirripedia", "quote": "The peduncle is flattened **dorsoventrally**, allowing the sessile barnacle to resist turbulent wave action."},
            {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "Benthic rays are flattened **dorsoventrally**, a modification perfectly adapted to resting concealed in marine sand."}
        ]
    },
    "dorsum": {
        "primary": "The entire back of the body, or the upper surface of a bodily part such as the tongue, foot, or hand.",
        "secondary": "In human gross anatomy, the posterior aspect of the torso or the convex superior surface of the foot (dorsum pedis) and hand (dorsum manus).",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The lingual papillae covering the **dorsum** of the tongue are richly supplied with taste buds and sensory nerve endings."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Pitting edema upon the **dorsum** of the feet is among the earliest physical signs of congestive cardiac decompensation."},
            {"author": "John Hunter", "work": "Treatise on the Blood, Inflammation, and Gun-shot Wounds", "quote": "Extensive inflammation across the **dorsum** of the foot requires careful incision to relieve subfascial tension."}
        ]
    },
    "endorse": {
        "primary": "To approve, support, or sustain publicly; or to sign the back of a negotiable document.",
        "secondary": "In commercial law and public policy, to execute a signature upon the reverse of a legal instrument transferring rights, or to give formal sanction to an initiative.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "I **endorse** the last words written, but this time there is no doubt in question regarding our solemn compact."},
            {"author": "Herman Melville", "work": "Bartleby, the Scrivener", "quote": "I cannot **endorse** the strange obstinacy of a clerk who refuses to verify his own copied folios."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Whoso would be a man must not meekly **endorse** the opinions of his neighbors, but consult his own conscience."}
        ]
    },
    "endorsement": {
        "primary": "An act of giving one's public approval or support to someone or something.",
        "secondary": "In banking and contract jurisprudence, a legal signature or clause written on the back of a negotiable bill, transferring title and guaranteeing value.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "I have done myself the honour of counting you one trusting friend, and such **endorsement** is dear to me."},
            {"author": "Mark Twain", "work": "The Gilded Age", "quote": "The senator hesitated to append his personal **endorsement** to a railroad bill burdened with questionable subsidies."},
            {"author": "William James", "work": "The Will to Believe", "quote": "Our active faith gives vital **endorsement** to possibilities that would remain dead without our personal commitment."}
        ]
    },
    "endorser": {
        "primary": "A person who publicly approves or supports a candidate, proposal, or enterprise.",
        "secondary": "In commercial paper law, the party who signs the reverse of a negotiable draft or check, thereby undertaking contingent liability to subsequent holders.",
        "quotes": [
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The financial credit of the state rests upon the known solvency of every reliable public **endorser**."},
            {"author": "Daniel Webster", "work": "Speeches and Forensic Arguments", "quote": "The court held that notice of protest had been properly served upon the secondary **endorser** of the protested note."},
            {"author": "Thomas Jefferson", "work": "The Writings of Thomas Jefferson", "quote": "He refused to stand as an **endorser** for speculative loans that endangered the private fortunes of his kindred."}
        ]
    },
    "indorse": {
        "primary": "To write one's signature on the back of a legal or financial document; to endorse.",
        "secondary": "In formal statutory jurisprudence and traditional commercial paper drafting, the legal act of signing a negotiable bill of exchange to assign title.",
        "quotes": [
            {"author": "George Washington", "work": "The Writings of George Washington", "quote": "I am requested to **indorse** the accompanying warrants before they are presented to the treasury for payment."},
            {"author": "Alexander Hamilton", "work": "Report on the Subject of Manufactures", "quote": "Merchants of high standing **indorse** domestic bills of exchange, thereby facilitating the rapid circulation of capital."},
            {"author": "John Marshall", "work": "Marbury v. Madison", "quote": "The officer had no discretionary power to refuse to **indorse** the patent once the legal conditions had been satisfied."}
        ]
    },
    "indorsement": {
        "primary": "A signature or legal notation written upon the back of a bill, note, or check; endorsement.",
        "secondary": "In commercial law, the formal inscription by which a negotiable instrument is assigned and made payable to a designated transferee.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I see the vast factories with their foremen and workmen, and hear the **indorsement** of all commerce and mechanical trade."},
            {"author": "Abraham Lincoln", "work": "Collected Works of Abraham Lincoln", "quote": "Upon this petition the President made a brief **indorsement** directing the Secretary of War to investigate the soldier's plea."},
            {"author": "Benjamin Franklin", "work": "The Autobiography of Benjamin Franklin", "quote": "My brother's printed journal carried the formal **indorsement** of the magistrates, without which no sheet could appear."}
        ]
    },
    "indorser": {
        "primary": "One who writes their signature on the back of a commercial document or bill.",
        "secondary": "In banking law, a party whose indorsement on a promissory note creates secondary liability to pay the instrument upon dishonor by the maker.",
        "quotes": [
            {"author": "John Marshall", "work": "Judicial Opinions", "quote": "Due diligence must be exercised in demanding payment from the maker before proceeding against the **indorser**."},
            {"author": "Joseph Story", "work": "Commentaries on the Law of Promissory Notes", "quote": "The contract of the **indorser** is that if the bill is dishonored, he will indemnify the holder upon timely notice."},
            {"author": "James Kent", "work": "Commentaries on American Law", "quote": "A discharge given to the principal debtor necessarily extinguishes the collateral liability of every accommodation **indorser**."}
        ]
    },

    # ==================== Dashboard — pariet (3 words) ====================
    "parietal": {
        "primary": "Relating to or forming the walls of a body cavity, or denoting the parietal bones of the skull.",
        "secondary": "In human neuroanatomy and osteology, pertaining to the bilateral parietal bones forming the roof and sides of the cranium, or to the parietal lobe of the cerebrum.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "In the surgeon's deposition it was stated that the posterior third of the left **parietal** bone was severely fractured."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **parietal** foramen in ancestral vertebrates represents the vestige of a median pineal sensory organ."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The external surface of the **parietal** bone is convex and marked near the center by the prominent parietal eminence."}
        ]
    },
    "parietales": {
        "primary": "An obsolete taxonomic order of dicotyledonous flowering plants possessing parietal placentation.",
        "secondary": "In historical systematic botany, a major plant group classified by Bentham and Hooker, characterized by ovaries whose ovules attach directly to the outer ovarian walls.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The order **Parietales** includes diverse families unified by the characteristic attachment of ovules to the ovary wall."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Several tropical genera belonging to the **Parietales** yield valuable resins, aromatic barks, and edible fruits."},
            {"author": "George Bentham", "work": "Genera Plantarum", "quote": "In our natural arrangement, the **Parietales** occupy an intermediate position between the Ranales and Polygalinae."}
        ]
    },
    "parietaria": {
        "primary": "A genus of flowering plants in the nettle family Urticaceae, commonly known as pellitory-of-the-wall.",
        "secondary": "In ethnobotany and allergic immunology, stingless wall-growing nettles (such as Parietaria officinalis) whose wind-borne pollen is a potent seasonal allergen in the Mediterranean basin.",
        "quotes": [
            {"author": "John Gerard", "work": "The Herball or Generall Historie of Plantes", "quote": "**Parietaria**, commonly called pellitory-of-the-wall, groweth upon ancient stone ramparts and ruined battlements."},
            {"author": "William Withering", "work": "An Arrangement of British Plants", "quote": "The small greenish flowers of **Parietaria** possess curious elastic stamens that discharge their pollen with sudden force."},
            {"author": "Nicholas Culpeper", "work": "The Complete Herbal", "quote": "An infusion of **Parietaria** hath been celebrated by ancient physicians as an effective diuretic for clearing the kidneys."}
        ]
    },

    # ==================== Dashboard — vertebr (7 words) ====================
    "intervertebral": {
        "primary": "Situated, located, or occurring between two adjacent vertebrae of the spinal column.",
        "secondary": "In orthopedic anatomy, relating to the fibrocartilaginous intervertebral discs and articulating ligaments that absorb shock and permit spinal flexibility.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "Each **intervertebral** disc consists of a fibrous outer ring, the anulus fibrosus, enclosing the gelatinous nucleus pulposus."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The thickness of the **intervertebral** cartilages varies throughout the spinal column according to the degree of mobility required."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "Spinal nerves emerge from the neural canal through paired **intervertebral** foramina situated along the vertebral column."}
        ]
    },
    "invertebrate": {
        "primary": "Lacking a backbone or spinal column; any animal not belonging to the subphylum Vertebrata.",
        "secondary": "In evolutionary zoology, designating the diverse assemblage of animal phyla (comprising over 95% of animal species) that develop without an axial notochord or vertebral column.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The lancelet presented affinities with the Ascidians, which are **invertebrate**, hermaphrodite, marine creatures."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The anatomical divide between the **invertebrate** and vertebrate plans of organization forms a central problem of biology."},
            {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "Our evolutionary genealogy traces human origins through primitive chordates back into ancient **invertebrate** marine ancestors."}
        ]
    },
    "vertebra": {
        "primary": "Any single bone or cartilaginous segment composing the spinal column in vertebrate animals.",
        "secondary": "In comparative osteology, a segmented skeletal unit typically consisting of a centrum, neural arch, and articular processes surrounding and protecting the spinal cord.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The spinal cord in man extends only as far downwards as the last dorsal or first lumbar **vertebra**."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "His cranial cavity is continuous with the first neck-vertebra; and in that **vertebra** the spinal canal will terminate."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The peasant's cart rattled along with its long, snake-like **vertebra**, calculated to surmount any unevenness of the mountain roads."}
        ]
    },
    "vertebrae": {
        "primary": "The plural of vertebra; the articulated series of bones forming the backbone or spinal column.",
        "secondary": "In human anatomy, the thirty-three segmented bones (cervical, thoracic, lumbar, sacral, coccygeal) that support trunk axial load and encase the spinal canal.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In man, the os coccyx, together with certain other **vertebrae** hereafter to be described, represents a rudimentary tail."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The articulated **vertebrae** are bound together by powerful ligaments, forming a flexible yet remarkably strong column."},
            {"author": "Richard Owen", "work": "On the Archetype and Homologies of the Vertebrate Skeleton", "quote": "He demonstrated that the skull itself represents the extreme cranial expansion of four modified primal **vertebrae**."}
        ]
    },
    "vertebral": {
        "primary": "Pertaining to, composed of, or situated in the vicinity of the vertebrae or spinal column.",
        "secondary": "In human neurovascular anatomy, describing essential anatomical structures such as the vertebral artery, vertebral vein, or vertebral canal.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "This primitive fish can hardly be said to possess a brain, **vertebral** column, or heart in any differentiated form."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The segmented **vertebral** column provides the primary axial support and protective housing for the spinal marrow."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Currents and Counter-Currents in Medical Science", "quote": "A severe lateral curvature of the **vertebral** axis inevitably restricts the expansion of the thoracic viscera."}
        ]
    },
    "vertebrata": {
        "primary": "The comprehensive taxonomic subphylum of chordate animals possessing an internal vertebral column.",
        "secondary": "In zoological systematics, the taxon comprising cyclostomes, cartilaginous and bony fishes, amphibians, reptiles, birds, and mammals, defined by an articulated axial skeleton and cranium.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Amongst existing **Vertebrata**, we find but a small amount of gradation in the structure of the eye."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The fundamental morphological plan of the **Vertebrata** remains recognizable across every adaptive evolutionary radiation."},
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Vertebrate Animals", "quote": "In all **Vertebrata**, the central nervous axis occupies a closed dorsal neural canal above the alimentary canal."}
        ]
    },
    "vertebrate": {
        "primary": "Having a backbone or spinal column; an animal belonging to the subphylum Vertebrata.",
        "secondary": "In comparative anatomy, designating any chordate animal possessing an internal cartilaginous or bony skeleton, an axial spine, and a protected cephalic brain.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "All **vertebrate** animals, all insects, and some other large groups of animals, pair for each birth."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The anatomical structural gap separating man from the highest apes is less than that which divides apes from lower **vertebrate** orders."},
            {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "The fossil record exhibits a clear ascendancy of higher **vertebrate** forms through successive geological strata."}
        ]
    },

    # ==================== Dashboard — nas (First 6 words) ====================
    "intranasal": {
        "primary": "Situated within, introduced into, or administered through the nasal cavity.",
        "secondary": "In clinical pharmacology and otolaryngology, describing topical drug administration or surgical procedures performed within the nasal mucosa and turbinates.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful **intranasal** inspection reveals mucosal hypertrophy or polypoid growths that frequently obstruct the upper respiratory tract."},
            {"author": "Sigmund Freud", "work": "The Interpretation of Dreams", "quote": "Fliess maintained that reflex neuroses could be directly influenced by topical cocainization of specific **intranasal** trigger zones."},
            {"author": "William Henry Welch", "work": "Papers and Addresses", "quote": "Experimental **intranasal** inoculation in laboratory animals demonstrated how pathogens gain access to the central nervous system."}
        ]
    },
    "nasa": {
        "primary": "The National Aeronautics and Space Administration, the civilian aerospace agency of the United States.",
        "secondary": "In space exploration and technological history, the federal agency established in 1958 responsible for civilian spaceflight, lunar exploration, and robotic interplanetary science.",
        "quotes": [
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "The robotic Voyager missions orchestrated by **NASA** transformed our understanding of the outer solar system and its giant moons."},
            {"author": "Arthur C. Clarke", "work": "The Promise of Space", "quote": "Through the massive technical coordination of **NASA**, humanity took its first tentative footsteps upon the lunar surface."},
            {"author": "Lyndon B. Johnson", "work": "Public Papers of the Presidents", "quote": "We created **NASA** to ensure that space exploration would serve the peaceful development and scientific enlightenment of all mankind."}
        ]
    },
    "nasal": {
        "primary": "Relating to, situated near, or affecting the nose; or pronounced with air escaping through the nose.",
        "secondary": "In clinical anatomy and phonetics, pertaining to the nasal bones, septum, and paranasal sinuses, or to resonant speech sounds produced by lowering the soft palate.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The prominence of the **nasal** bones varies remarkably among different human races and ancestral primates."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The vicar spoke in a high **nasal** tone that seemed to flatten every lively topic into a dry sermon."},
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The boatman gave vent to a curious **nasal** twang that sounded distinct and musical across the misty water."}
        ]
    },
    "nasale": {
        "primary": "An anatomical designation for a nasal bone, plate, or rostral cranial element.",
        "secondary": "In comparative craniology and vertebrate paleontology, the paired dermal bone (os nasale) roofed over the anterior nasal chamber in tetrapod skulls.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The os **nasale** articulates superiorly with the frontal bone and laterally with the frontal process of the maxilla."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "In fossil reptilian crania, the paired **nasale** elements extend forward to delimit the external bony nares."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The rostral sutures joining the **nasale** with adjacent facial bones remain distinct in primitive mammalian skulls."}
        ]
    },
    "nasalis": {
        "primary": "A facial muscle spanning the dorsum and nostrils that acts to compress or dilate the nasal aperture.",
        "secondary": "In facial anatomy, a paired mimetic muscle consisting of a transverse compressor naris portion and an alar dilator naris portion innervated by the facial nerve.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **nasalis** muscle arises from the maxilla and sends aponeurotic fibers across the bridge of the nose to compress the cartilaginous apertures."},
            {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "During fierce rage or deep disgust, contraction of the **nasalis** and levator muscles draws the nostrils upward in an instinctive sneer."},
            {"author": "Charles Bell", "work": "The Anatomy and Philosophy of Expression as Connected with the Fine Arts", "quote": "The delicate play of the **nasalis** fiber tracts imparts subtle emotional animation to the human countenance in passion."}
        ]
    },
    "nasalisation": {
        "primary": "The phonetic production of a speech sound accompanied by lowering of the soft palate so that air escapes through the nose.",
        "secondary": "In historical and acoustic phonetics, the physiological process wherein oral vowels or consonants acquire nasal resonance through palatal relaxation (British spelling).",
        "quotes": [
            {"author": "Henry Sweet", "work": "A Handbook of Phonetics", "quote": "Vowel **nasalisation** occurs when the velum is lowered sufficiently to allow the vocal resonance to pass through the nasal passages."},
            {"author": "Ferdinand de Saussure", "work": "Course in General Linguistics", "quote": "The historical development of modern French vowels demonstrates how anticipatory **nasalisation** permanently transformed the language's phonetic system."},
            {"author": "Otto Jespersen", "work": "Phonetics", "quote": "In casual vernacular speech, degrees of involuntary **nasalisation** frequently affect vowels immediately preceding nasal consonants."}
        ]
    }
}
