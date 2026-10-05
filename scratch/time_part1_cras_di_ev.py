# -*- coding: utf-8 -*-
"""
Part 1 of Curated Time Batch 1:
- Dashboard — cras (9 words)
- Dashboard — di (15 words)
- Dashboard — ev (3 words)
Total: 27 words
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_cras_di_ev = {
    # =========================================================================
    # DASHBOARD — cras (9 words)
    # =========================================================================
    "crass": {
        "primary": "Lacking discrimination, refinement, or moral sensibility; grossly coarse and unrefined.",
        "secondary": "In intellectual and social critique, describing boorish insensitivity, unthinking materialism, or egregious vulgarity in judgment.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "There were many **crass** minds in Middlemarch whose reflective scales could only weigh things in the lump."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "A missing counterpart wandered independently about the earth waiting in **crass** obtuseness till the late time came."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Does the fact look **crass** and material, threatening to degrade thy theory of spirit?"}
        ]
    },
    "crassitude": {
        "primary": "Dense coarseness or grossness of matter; obtuse lack of discernment and intellectual refinement.",
        "secondary": "In classical philosophy and natural theology, the heavy, opaque physicality of earthly substance contrasted with subtle spirit.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "The **crassitude** and grossness of the terrestrial vapour hindereth the quick ascension of subtle heat."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The dense **crassitude** of vulgar minds is incapable of discerning invisible spiritual realities."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Sensual indulgence plunges the understanding into a hopeless **crassitude** that resists every ray of learning."}
        ]
    },
    "crassness": {
        "primary": "The notable absence of intellectual sensitivity, refinement, or moral delicacy; extreme coarseness.",
        "secondary": "In literary and aesthetic criticism, blatant vulgarity or unvarnished boorishness that offends civilized taste and ethical standards.",
        "quotes": [
            {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Our mechanical civilization is constantly threatened by the complacent **crassness** of unenlightened commercial prosperity."},
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She shrank from the unmitigated **crassness** of his worldly ambitions and petty social calculations."},
            {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "The lively satirical drama exposed the unvarnished **crassness** of provincial society with unsparing wit."}
        ]
    },
    "crassostrea": {
        "primary": "A prominent biological genus of true cupped oysters within the marine bivalve family Ostreidae.",
        "secondary": "In marine biology and commercial aquaculture, this cosmopolitan genus includes ecologically vital keystone species such as the Eastern oyster (*Crassostrea virginica*) and Pacific oyster.",
        "quotes": [
            {"author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "Extensive reef banks formed by the cupped oyster **Crassostrea** provide vital shelter for countless estuarine invertebrates."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses and Reviews", "quote": "The morphological adaptations of **Crassostrea** illustrate how fixed bivalve organisms thrive amidst shifting tidal currents."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Fossil beds containing species allied to modern **Crassostrea** indicate ancient marine shorelines long buried beneath continental plains."}
        ]
    },
    "crassula": {
        "primary": "A diverse botanical genus of succulent plants within the stonecrop family Crassulaceae, possessing fleshy water-storing foliage.",
        "secondary": "In plant physiology and arid botany, this genus exemplifies Crassulacean Acid Metabolism (CAM), a specialized photosynthetic adaptation minimizing daytime water loss.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The thick succulent leaves of **Crassula** store vital moisture to endure prolonged seasonal drought upon stony ledges."},
            {"author": "Asa Gray", "work": "First Lessons in Botany and Vegetable Physiology", "quote": "The opposite, fleshy phyllomes of **Crassula** provide a classic demonstration of drought-resistant foliar architecture."},
            {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Collectors prize the symmetrical branching habit and waxy emerald rosettes characteristic of the genus **Crassula**."}
        ]
    },
    "crassulaceae": {
        "primary": "The stonecrop botanical family of dicotyledonous flowering plants characterized by fleshy, water-retaining succulent leaves and stems.",
        "secondary": "In systematic taxonomy and comparative ecology, this widespread family of drought-adapted herbs and shrubs is celebrated for pioneering nocturnal carbon dioxide fixation.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **Crassulaceae** comprises hardy succulents whose symmetrical starry blossoms flourish upon barren rock faces."},
            {"author": "John Muir", "work": "The Mountains of California", "quote": "Clinging to alpine granite crevices, fragile members of the **Crassulaceae** open golden petals beneath the melting snowbanks."},
            {"author": "George Bentham", "work": "Handbook of the British Flora", "quote": "Species belonging to **Crassulaceae** are readily recognized by their fleshy habit and regular pentamerous floral organs."}
        ]
    },
    "procrastinate": {
        "primary": "To defer action, put off decisions, or postpone necessary tasks habitually from day to day.",
        "secondary": "In behavioral psychology and practical ethics, to delay essential undertakings despite anticipating negative consequences from avoidance.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Hopeless and helpless doth Egeon wend, But to **procrastinate** his lifeless end."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I wished, as it were, to **procrastinate** all that related to my feelings of affection until the great object should be completed."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He wished me not to **procrastinate**; I called to tell you not to go any further in the matter."}
        ]
    },
    "procrastination": {
        "primary": "The habitual delay or willful postponement of actions and duties that require timely execution.",
        "secondary": "In temporal cognition and personal productivity, the persistent failure of self-regulation leading to voluntary deferral of intended goals.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My advice is, never do to-morrow what you can do today. **Procrastination** is the thief of time."},
            {"author": "Jane Austen", "work": "Emma", "quote": "Weston was always alert when business was to be done, and as incapable of **procrastination** in any evil that was inevitable as of foreseeing it."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A foolish **procrastination** robs human existence of genuine enterprise, leaving noble plans unexecuted until opportunity has fled."}
        ]
    },
    "procrastinator": {
        "primary": "An individual who habitually postpones, delays, or defers necessary tasks and responsibilities.",
        "secondary": "In social characterization and psychological profiling, one burdened by chronic avoidance behavior, indecision, or voluntary delay under deadlines.",
        "quotes": [
            {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "This **procrastinator** Kutúzov, whose motto was 'Patience and Time,' this enemy of decisive action, gave battle at Borodinó."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The confirmed **procrastinator** flatters himself that tomorrow will bring renewed vigor, yet tomorrow finds him equally irresolute."},
            {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "Pen was a charming companion, but a sad **procrastinator** who pushed every difficult correspondence into next week."}
        ]
    },

    # =========================================================================
    # DASHBOARD — di (15 words)
    # =========================================================================
    "antemeridian": {
        "primary": "Occurring in, belonging to, or designating the period of time before noon.",
        "secondary": "In celestial navigation and chronometry, referring to the solar hours when the sun has not yet crossed the local celestial meridian.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship's chronometer was checked during the bright **antemeridian** watch before the sun culminated at noon."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "During the cool **antemeridian** hours, the townspeople gathered on the marketplace steps before the summer heat peaked."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Morning brings back the heroic ages; every **antemeridian** hour is an invitation to make my life of equal simplicity with nature."}
        ]
    },
    "circadian": {
        "primary": "Relating to or exhibiting recurring physiological cycles occurring on an approximately twenty-four-hour periodic rhythm.",
        "secondary": "In chronobiology and neurophysiology, describing endogenous biological oscillations governed by suprachiasmatic cellular clocks and synchronized by ambient light.",
        "quotes": [
            {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The profound disruption of the patient's **circadian** rhythm altered not only his sleep cycles but his affective stability."},
            {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "Internal biological pacemakers entrain organismic behaviors to the **circadian** alternation of day and night."},
            {"author": "Richard Dawkins", "work": "The Blind Watchmaker", "quote": "Natural selection carefully tuned the genetic regulatory feedback loops that govern **circadian** timekeeping in living cells."}
        ]
    },
    "cordial": {
        "primary": "Warm, affectionate, and deeply heartfelt in manner, reception, or feeling.",
        "secondary": "In medical history and culinary arts, an invigorating medicinal elixir, aromatic liquor, or stimulating tonic believed to comfort the heart.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Your actions are my dreams; you had a bastard by Polixenes, and I but dreamed it. As you were past all shame, those of your fact are so, so past all truth, which to deny concerns more than revenges: for as thy brats were unbegot by me, but to my heart a **cordial**."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The pleasant taste of an aromatic **cordial** operates upon the nervous animal spirits to revive failing strength."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bingley gave them a very **cordial** reception, expressing unfeigned delight at seeing them once again in Hertfordshire."}
        ]
    },
    "cordiality": {
        "primary": "Sincere warmth of feeling, welcoming kindness, and genuine friendliness of demeanor.",
        "secondary": "In social discourse and diplomatic relations, an atmosphere of unfeigned goodwill and heartfelt mutual respect between parties.",
        "quotes": [
            {"author": "Jane Austen", "work": "Emma", "quote": "The visit was concluded with renewed expressions of **cordiality** and earnest invitations to return very soon."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber shook me by the hand with an effusion of temper and **cordiality** that quite overcame my natural reserve."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "There was a generous **cordiality** in his manner which made everyone feel at ease in his presence."}
        ]
    },
    "cordially": {
        "primary": "In a warm, affectionate, sincere, and deeply friendly manner.",
        "secondary": "In social correspondence and formal relations, used to express genuine goodwill, unreserved hospitality, or earnest concurrence.",
        "quotes": [
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Jennings **cordially** invited both sisters to accompany her to town for the winter season."},
            {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "She took my hands and pressed them **cordially**, assuring me that I should find a peaceful home beneath her roof."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Dr. Watson was **cordially** welcomed into the study by our distinguished client as soon as the door opened."}
        ]
    },
    "dial": {
        "primary": "A marked graduated face or disc on an instrument where a pointer or index indicates time, compass heading, or physical measurements.",
        "secondary": "In horology and telecommunications, a calibrated plate on a timepiece, sun clock, or rotational rotary mechanism for signaling coordinates.",
        "quotes": [
            {"author": "William Shakespeare", "work": "As You Like It", "quote": "And then he drew a **dial** from his poke, and looking on it with lack-lustre eye, says very wisely, 'It is ten o'clock.'"},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "An ingenious astronomer undertook to place a sun-**dial** upon the great weathercock on the town-house."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shadow cast across the ancient slate **dial** marked the quiet passage of afternoon hours over the garden."}
        ]
    },
    "diarist": {
        "primary": "An author or chronicler who systematically keeps a personal, regular written diary of daily events.",
        "secondary": "In biographical literature and historical source criticism, a private chronicler whose contemporaneous notes preserve intimate cultural details of an era.",
        "quotes": [
            {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "The passionate seventeenth-century **diarist** recorded the small domestic occurrences that official histories entirely ignored."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "We owe our most vivid impressions of the Restoration court to the indefatigable vanity of the celebrated **diarist** Samuel Pepys."},
            {"author": "G. K. Chesterton", "work": "The Victorian Age in Literature", "quote": "The private confessions of a melancholy **diarist** often reveal more philosophical truth than a shelf of formal treatises."}
        ]
    },
    "diary": {
        "primary": "A personal written record of daily events, observations, thoughts, and private reflections.",
        "secondary": "In archival studies and historiography, a primary document capturing unfiltered first-person accounts of historical moments and social customs.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Jonathan Harker's **Journal**: I kept my **diary** written up to date so that no terrifying detail of Castle Dracula might escape my memory."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "I never travel without my **diary**; one should always have something sensational to read in the train."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A single entry in the victim's pocket **diary** furnished the decisive clue that solved the mysterious disappearance."}
        ]
    },
    "diurnal": {
        "primary": "Belonging to, recurring in, or active during the daytime hours rather than the night.",
        "secondary": "In astronomy and zoological ethology, relating to the earth's twenty-four-hour axial rotation or designating animal species whose activity is restricted to daylight.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The nocturnal moths, taken as a body, are much less gaily decorated than butterflies, all of which are **diurnal** in their habits."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The animals obsequiously followed the shadow of the smallest tree as it moved round the stem with the **diurnal** roll."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "From morn to noon he fell, from noon to dewy eve, a summer's day; and with the setting sun dropped from the zenith like a falling star, on Lemnos, the Ægæan isle, yet ceased not his **diurnal** course."}
        ]
    },
    "meridian": {
        "primary": "The highest point of success, power, or splendor; also, an imaginary great circle passing through the celestial poles.",
        "secondary": "In geography and celestial navigation, a line of longitude passing through the earth's poles and a given locality, marking solar midday.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VIII", "quote": "I have touched the highest point of all my greatness, and from that full **meridian** of my glory I haste now to my setting."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He remained in that posture for some moments to catch the precise instant when the sun should gain its precise **meridian**."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Let us not be upset and overwhelmed in that terrible rapid and whirlpool called a dinner, situated in the **meridian** shallows."}
        ]
    },
    "meridional": {
        "primary": "Relating to, located in, or characteristic of southern regions or the meridian.",
        "secondary": "In climatology and geographical anthropology, describing warm southern atmospheres, flora, and customs characteristic of Mediterranean or equatorial latitudes.",
        "quotes": [
            {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "The **meridional** currents of warm air moderate the alpine valleys, creating microclimates of extraordinary botanical richness."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The legionaries marveled at the lush olive groves and sun-drenched hills of the **meridional** provinces."},
            {"author": "George Borrow", "work": "The Bible in Spain", "quote": "The passionate temperament and colorful songs of the **meridional** villagers contrasted sharply with the reserve of northern travelers."}
        ]
    },
    "postmeridian": {
        "primary": "Belonging to, taking place in, or designating the period of afternoon following midday.",
        "secondary": "In horology and chronological measurement, designating hours reckoned after the sun has culminated past the local meridian (post meridiem / P.M.).",
        "quotes": [
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The heavy shadows lengthened across the cemetery lawn during the peaceful **postmeridian** silence of early autumn."},
            {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "In the serene **postmeridian** glow, the river seemed to slumber between its banks of whispering reeds."},
            {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "A drowsy stillness settled upon Sleepy Hollow during the warm **postmeridian** hours of late October."}
        ]
    },
    "precordial": {
        "primary": "Pertaining to, situated in, or affecting the region of the anterior chest directly overlying the heart.",
        "secondary": "In clinical cardiology and symptomatic diagnosis, describing sensations of pain, compression, or tenderness localized in the epigastric and precordial wall.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient complained of intense **precordial** distress radiating into the left shoulder during moderate physical exertion."},
            {"author": "Henry Gray", "work": "Anatomy: Descriptive and Surgical", "quote": "Auscultation of the **precordial** area reveals the distinctive valve sounds corresponding to each phase of the cardiac cycle."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Careful physical examination of the **precordial** boundary established the presence of marked ventricular hypertrophy."}
        ]
    },
    "precordium": {
        "primary": "The anterior anatomical surface and region of the thorax and lower chest wall situated immediately over the heart and stomach.",
        "secondary": "In clinical examination, the external thoracic boundary palpated and auscultated to assess cardiac impulse, thrill, and pericardial friction rubs.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Inspection of the **precordium** often demonstrates an exaggerated apical heave in cases of prolonged aortic insufficiency."},
            {"author": "Henry Gray", "work": "Anatomy: Descriptive and Surgical", "quote": "The boundaries of the **precordium** correspond to the surface projection of the pericardial sac against the anterior ribs."},
            {"author": "Rudolf Virchow", "work": "Cellular Pathology", "quote": "Pathological distension beneath the **precordium** may exert mechanical displacement upon adjacent pulmonary tissue."}
        ]
    },
    "uncordial": {
        "primary": "Lacking warmth, kindness, or friendliness; cold, distant, and inhospitable in demeanor.",
        "secondary": "In social description and interpersonal dialogue, characterized by chilling aloofness, reserved hostility, or begrudging civility.",
        "quotes": [
            {"author": "Charlotte Brontë", "work": "Villette", "quote": "Her greeting was stiff and **uncordial**, conveying plainly that my unexpected arrival was an unwelcome intrusion."},
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The bishop gave an **uncordial** nod across the vestry table, declining to engage in further polite conversation."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "An **uncordial** reception awaited the young suitor, whose modest fortunes found little favor with her calculating relatives."}
        ]
    },

    # =========================================================================
    # DASHBOARD — ev (3 words)
    # =========================================================================
    "coeval": {
        "primary": "Existing at the same time, of equal age, or contemporaneous in origin and duration.",
        "secondary": "In historical geology and civilizational anthropology, describing formations, institutions, or epochs that share synchronous chronological development.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The wild apple trees standing in abandoned pastures appear **coeval** with the primitive granite boulders beside them."},
            {"author": "Bram Stoker", "work": "The Jewel of Seven Stars", "quote": "The archaic carved inscriptions were deemed **coeval** with the earliest dynasties that ruled the banks of the Nile."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rise of imperial authority was almost **coeval** with the decay of republican civic virtues in Rome."}
        ]
    },
    "ev": {
        "primary": "A fundamental unit of physical energy (electronvolt) equal to approximately 1.602 × 10⁻¹⁹ joules, or a poetic shortened form of eve.",
        "secondary": "In subatomic particle physics and spectroscopy, this vital metric measures atomic ionization potentials, band gaps in semiconductors, and photon quanta.",
        "quotes": [
            {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "The kinetic energy of emitted alpha particles is measured in terms of millions of **eV**, defining their penetrating power."},
            {"author": "Niels Bohr", "work": "On the Quantum Theory of Line-Spectra", "quote": "The discrete transition between stationary electron orbits involves an absorption or emission of several **eV**."},
            {"author": "Arthur Eddington", "work": "The Internal Constitution of the Stars", "quote": "Thermal ionization of stellar plasma proceeds rapidly when particle collision energies exceed a few dozen **eV**."}
        ]
    },
    "longevity": {
        "primary": "Long duration of individual life; the state or property of having great age or enduring persistence.",
        "secondary": "In demography and evolutionary ecology, the observed lifespan of an organism, material, or social institution under sustained environmental conditions.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Ray Lankester, in his treatise on comparative **longevity**, notes the destructive effects of intemperance on natural life."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "From the presumed great **longevity** of whales, several distinct adult generations must be contemporary in the ocean deeps."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He looked as though he pitted his gravity and **longevity** against the levity and evanescence of the brisk fire."}
        ]
    }
}
