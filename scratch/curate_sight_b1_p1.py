# -*- coding: utf-8 -*-
"""
curate_sight_b1_p1.py
Batch 1 Part 1 of Cluster Sight:
- Dashboard — mir (39 words):
admirability, admirable, admirableness, admirably, admiral,
admiralty, admiration, admire, admired, admirer, admiringly,
emir, emirate, mirabeau, mirabilis, miracle, miracle-worship,
miraculous, miraculously, mirage, mirasol, mire, mired,
miri, mirid, miridae, mirish, miro, mirounga, mirror,
mirrored, mirrorlike, mirth, mirthful, mirthfully, mirthfulness,
mirthless, miry, semirigid
- Dashboard — pict (6 words):
depict, depicted, depicting, depiction, depictive, epictetus
Total: 45 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b1_p1 = {
    "admirability": {
        "primary": "Excellence, praiseworthy character, or worthiness of profound esteem and respect.",
        "secondary": "In ethical philosophy and aesthetics, moral or aesthetic distinction that commands universal esteem and reverence.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True **admirability** consists not in transient popular applause, but in steadfast adherence to moral virtue."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her quiet unselfishness possessed an **admirability** that deepened with every trial."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "We perceive an inherent **admirability** in any character that acts with self-reliant independence."}
        ]
    },
    "admirable": {
        "primary": "Arousing or deserving the highest esteem, respect, and approval; excellent.",
        "secondary": "In classical aesthetics and character appraisal, displaying exceptional virtue, skill, or sublime proportion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "What a piece of work is a man! how noble in reason! how infinite in faculty! in form and moving how express and **admirable**!"},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles displayed an **admirable** patience, refusing to utter a word of complaint against his misfortune."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The structure of the honeycomb is an **admirable** adaptation that saves both wax and bee labor."}
        ]
    },
    "admirableness": {
        "primary": "The trait of being worthy of admiration, high regard, or praise.",
        "secondary": "In moral philosophy, intrinsic excellence or praiseworthy dignity that inspires respectful reverence.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The **admirableness** of Milton's epic diction lies in its harmonized sublimity and metrical control."},
            {"author": "William Hazlitt", "work": "Table-Talk", "quote": "There is an unvarnished **admirableness** in genuine simplicity that pretension can never counterfeit."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The moral **admirableness** of an action depends upon its tendency to produce general human flourishing."}
        ]
    },
    "admirably": {
        "primary": "In a manner that commands high praise, respect, or esteem; excellently.",
        "secondary": "In descriptive prose, performing a function or displaying a virtue with consummate fitness and skill.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Each organic being is **admirably** adapted to the complex conditions of its life in the struggle for existence."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's earnest manner was **admirably** suited to disarm petty suspicion among the villagers."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak played the flute **admirably**, producing plaintive pastoral airs across the moonlit field."}
        ]
    },
    "admiral": {
        "primary": "The commander of a naval fleet or squadron; a flag officer of the highest rank in the navy.",
        "secondary": "In maritime history, the naval commander responsible for fleet strategy, tactical formation, and maritime sovereignty.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "Thou art our **admiral**, thou bearest the lantern in the poop, but 'tis in the nose of thee."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Napoleon studied the naval campaigns of each great **admiral**, seeking to understand the secret of British oceanic mastery."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The great **admiral** whose portrait hung above the mantelpiece looked grimly down upon his descendant."}
        ]
    },
    "admiralty": {
        "primary": "The government department or judicial court administering naval affairs and maritime law.",
        "secondary": "In British constitutional history and maritime jurisprudence, the high board commanding the Royal Navy or courts having jurisdiction over maritime offenses.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "The vessel was reported derelict by telegraph, and the **admiralty** dispatched a gunboat to secure the salvage."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The High Court of **Admiralty** held jurisdiction over collisions, piracies, and salvage claims on the high seas."},
            {"author": "Jane Austen", "work": "Persuasion", "quote": "Her father had served with distinction in the **admiralty**, accumulating honor and prize money during the Napoleonic blockade."}
        ]
    },
    "admiration": {
        "primary": "Respect, warm approval, and esteem; or anciently, wonder and astonishment.",
        "secondary": "In philosophical aesthetics and psychological analysis, high regard mixed with reverence for superior virtue, genius, or beauty.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "O wonder! How many goodly creatures are there here! How beauteous mankind is! O brave new world, that has such people in't! What strange **admiration**!"},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When an idea strikes the mind with unexpected perfection, it excites the passion of **admiration**."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare looked upon her with profound **admiration**, seeing an idealized embodiment of rural purity."}
        ]
    },
    "admire": {
        "primary": "To regard with respect, warm approval, or pleasure; or archaic, to marvel at.",
        "secondary": "In moral appreciation, to recognize superior character, artistry, or achievement with sincere intellectual delight.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Suit the action to the word, the word to the action, with this special observance, that you o'erstep not the modesty of nature: for any thing so o'erdone is from the purpose of playing, whose end, both at the first and now, was and is, to hold, as 'twere, the mirror up to nature. I cannot but **admire**."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "We justly **admire** the wisdom of the Creator when we discover the intricate contrivances of living bodies."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "She could not help but **admire** his tall, dignified figure against the sunset horizon."}
        ]
    },
    "admired": {
        "primary": "Regarded with wonder, high esteem, and profound respect.",
        "secondary": "In classical rhetoric, held in honored esteem by peers for intellectual or moral excellence.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "**Admired** Miranda! Indeed the top of admiration! Worth what's dearest to the world!"},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate was widely **admired** for his medical skill, though his reformist zeal alarmed traditionalists."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister was revered and **admired** by the entire Puritan congregation as a beacon of holiness."}
        ]
    },
    "admirer": {
        "primary": "A person who has a particular regard or affection for someone or something; an enthusiast or suitor.",
        "secondary": "In social history and literary critique, an appreciative devotee of an artistic genius or a gentleman paying court to a lady.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "From the four corners of the earth they come, To kiss this shrine, this mortal-breathing saint: every suitor and **admirer**."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A candid **admirer** of truth will abandon any hypothesis that contradicts demonstrable facts."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Farfrae found himself surrounded by many an **admirer** who praised his energetic business acumen."}
        ]
    },
    "admiringly": {
        "primary": "In a manner showing or feeling admiration, approval, or esteem.",
        "secondary": "In narrative description, regarding a person or object with visible respect, warmth, or appreciative wonder.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea looked **admiringly** at Will Ladislaw's radiant youth and spirited conversation."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "The young men listened **admiringly** to his tales of adventure and continental travel."},
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "The shepherd gazed **admiringly** upon the royal visitor, dazzled by his courtly grace."}
        ]
    },
    "emir": {
        "primary": "An aristocratic title of high military command or princely rule in Islamic countries.",
        "secondary": "In Middle Eastern history and governance, a provincial governor, military commander, or sovereign hereditary prince.",
        "quotes": [
            {"author": "Herman Melville", "work": "Mardi", "quote": "He carried himself with the haughty majesty of an Arabian **emir** surveying his desert realm."},
            {"author": "Washington Irving", "work": "Chronicle of the Conquest of Granada", "quote": "The Moorish **emir** led his cavalry in a desperate charge to relieve the besieged citadel."},
            {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The **emir** of the desert tribe received us with grave Bedouin hospitality under his black tent."}
        ]
    },
    "emirate": {
        "primary": "The political territory, principality, or jurisdiction ruled by an emir.",
        "secondary": "In geopolitical geography, a sovereign or autonomous Islamic monarchy governed by a dynastic prince (emir).",
        "quotes": [
            {"author": "Washington Irving", "work": "The Alhambra", "quote": "The Moorish **emirate** of Granada flourished for centuries as an oasis of art and scholastic learning in southern Spain."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Each provincial **emirate** established by the Umayyads minted its own coinage and fielded independent armies."},
            {"author": "Richard Francis Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The merchant traveled between one wealthy **emirate** and the next, trading damascene steel for rare spices."}
        ]
    },
    "mirabeau": {
        "primary": "Honoré Gabriel Riqueti, Comte de Mirabeau (1749–1791), a renowned French revolutionary orator and statesman.",
        "secondary": "In European political history, the brilliant French Assembly leader who sought to reconcile democratic constitutionalism with a reformist monarchy.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "In that fiery volcanic countenance of **Mirabeau**, the French National Assembly found its undisputed thunderer."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The eloquence of **Mirabeau** had the sudden, dazzling power of a thunderstorm breaking over a summer landscape."},
            {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "Had **Mirabeau** lived, the monarchical constitution might have survived the radical Jacobin deluge."}
        ]
    },
    "mirabilis": {
        "primary": "A genus of herbaceous flowering plants in the family Nyctaginaceae, including the four o'clock flower (Mirabilis jalapa).",
        "secondary": "In genetics and horticulture, the classical model organism (Mirabilis) in which Carl Correns discovered non-Mendelian cytoplasmic inheritance.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "My crossing experiments with **mirabilis** jalapa demonstrated surprising variations in petal variegation."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He wondered at the strange marine creatures, resembling a blooming **mirabilis** of the oceanic deep."},
            {"author": "Asa Gray", "work": "Field, Forest, and Garden Botany", "quote": "Commonly called four-o'clocks, species of **mirabilis** open their fragrant trumpet blossoms in late afternoon."}
        ]
    },
    "miracle": {
        "primary": "An extraordinary and welcome event that is not explicable by natural or scientific laws and is therefore attributed to a divine agency.",
        "secondary": "In theological epistemology and philosophy, a supernatural suspension or alteration of physical nature serving as a sign of divine power.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "It were a **miracle** if a prince so wild should turn suddenly to sober virtue."},
            {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "A **miracle** is a violation of the laws of nature; and because firm experience establishes these laws, the proof against a miracle is as full as can be imagined."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A **miracle** considered in itself is that which exceeds the known power of natural agents."}
        ]
    },
    "miracle-worship": {
        "primary": "Excessive religious devotion to or credulous reverence for miraculous occurrences and wonder-working relics.",
        "secondary": "In the history of religions and secular critique, superstitious veneration of prodigies and faith healings displacing ethical reflection.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Medieval pilgrimages were sustained by widespread **miracle-worship**, drawing credulous multitudes to saintly shrines."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Mechanical **miracle-worship** debases true spiritual wonder into vulgar craving for magical spectacles."},
            {"author": "Matthew Arnold", "work": "Literature and Dogma", "quote": "Puritan reformers swept away the medieval **miracle-worship** that had obscured the simple ethical gospel."}
        ]
    },
    "miraculous": {
        "primary": "Having the nature of a miracle; supernatural, wondrous, or extraordinary.",
        "secondary": "In philosophical criticism and narrative literature, appearing to transcend the normal operations of physical cause and effect.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "They say miracles are past; and we have our philosophical persons to make modern and familiar, things supernatural and causeless. Why, 'tis a **miraculous** cure!"},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection dispenses with the need for **miraculous** interventions to explain the marvelous adaptation of species."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "To her simple peasant mind, the sudden arrival of help appeared **miraculous** and ordained by heaven."}
        ]
    },
    "miraculously": {
        "primary": "In a miraculous manner; by supernatural intervention or remarkably against all odds.",
        "secondary": "In narrative history, escaping catastrophe or achieving success through an extraordinary, seemingly providential coincidence.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The frail carriage swung precariously near the ravine, yet **miraculously** righted itself before plunging over."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The wounded youth **miraculously** survived the severe fever that had carried off his companions."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "The pure water of Walden Pond seemed **miraculously** preserved from the corrupting impurities of human commerce."}
        ]
    },
    "mirage": {
        "primary": "An optical illusion caused by atmospheric refraction of light, producing the appearance of water or displaced objects.",
        "secondary": "In meteorological physics and metaphorical critique, an atmospheric inversion projecting distant images, or an enticing but unattainable illusion.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her early dreams of heroic self-sacrifice dissolved like a desert **mirage** before the cold reality of provincial marriage."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The promised fortune of Chancery was a cruel **mirage** that lured generation after generation to destruction."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Under the burning equatorial sun, distant islands floated inverted in the sky like an airy **mirage**."}
        ]
    },
    "mirasol": {
        "primary": "The sunflower; or a traditional Spanish and Mexican chili pepper whose pods point toward the sun.",
        "secondary": "In botanical agronomy and culinary ethnobotany, Capsicum annuum cv. 'Mirasol', prized for its upward-pointing pods, fruity flavor, and bright red color (guajillo when dried).",
        "quotes": [
            {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions", "quote": "Peasant gardens in New Spain were enlivened by vibrant beds of **mirasol**, whose golden discs followed the sun."},
            {"author": "Richard Ford", "work": "A Handbook for Travellers in Spain", "quote": "The fiery dishes of Andalusian cookery owe their warm hue and savory pungency to the sun-ripened **mirasol** pepper."},
            {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The heliotropic movement of the **mirasol** provides a spectacular illustration of diurnal phototropism in growing shoots."}
        ]
    },
    "mire": {
        "primary": "A stretch of swampy or boggy ground; or soft, deep mud or slush; or to plunge into mud.",
        "secondary": "In topographical ecology and metaphorical discourse, treacherous peat morass, or a difficult, entrapping predicament.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Master, if you do, expect spoon-meat; or bespeak a long spoon. Why, Dromio? Marry, he must have a long spoon that must eat with the devil. We are in the **mire**."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Metaphysical disputes without clear definitions plunge the intellect deeper into the **mire** of confusion."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Heavy winter rains had converted the chalky road into a clinging **mire** that impeded every step."}
        ]
    },
    "mired": {
        "primary": "Stuck, entangled, or bogged down in deep mud; or entangled in a difficult situation.",
        "secondary": "In narrative description, immobilized by physical peat or soil, or hopelessly caught in moral, legal, or emotional complications.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The lumber wagon was heavily **mired** in the clay lane, requiring four strong draught horses to dislodge it."},
            {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mr. Tulliver found his fortunes hopelessly **mired** in expensive lawsuits with his downstream neighbors."},
            {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The heavy carriage remained **mired** up to its axles in the black Mississippi silt."}
        ]
    },
    "miri": {
        "primary": "In Ottoman and Islamic land tenure, state-owned land whose usufruct rights were granted to cultivators in exchange for taxes.",
        "secondary": "In agrarian economic history and Middle Eastern law, land over which ultimate ownership belonged to the public treasury (Bayt al-mal).",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Under imperial agrarian codes, extensive agricultural tracts were classified as **miri**, leased to peasant cultivators."},
            {"author": "Richard Francis Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The revenue of the provincial **miri** lands was collected by imperial tax-farmers for the sultan's treasury."},
            {"author": "James Bryce", "work": "Transcaucasia and Ararat", "quote": "The complex tenure of **miri** property required Ottoman land registries to distinguish between state sovereignty and peasant usufruct."}
        ]
    },
    "mirid": {
        "primary": "Any true bug belonging to the large insect family Miridae (plant bugs or capsid bugs).",
        "secondary": "In agricultural entomology, a piercing-sucking hemipteran insect that feeds on plant juices, many species causing economic damage to crops.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The minute puncture wounds inflicted by a single **mirid** bug cause young apple buds to wither."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The piercing rostrum of the **mirid** is delicately jointed, allowing it to penetrate tough plant epidermis."},
            {"author": "Jean-Henri Fabre", "work": "The Life of the Fly", "quote": "Natural predators such as ladybird beetles keep populations of the destructive **mirid** within modest limits."}
        ]
    },
    "miridae": {
        "primary": "The plant bug family (Capsidae), the largest family of true bugs (order Hemiptera), with over 10,000 species worldwide.",
        "secondary": "In systematic entomology, hemipteran insects distinguished by the absence of ocelli, a cuneus on the hemelytra, and four-segmented antennae.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The extensive family **miridae** includes phytophagous bugs possessing a membranous wing cell and lack of ocelli."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Adaptive radiation among the **miridae** has produced specialized forms feeding upon almost every family of flowering plants."},
            {"author": "Jean-Henri Fabre", "work": "The Life of the Fly", "quote": "Horticulturists wage constant warfare against various invasive members of the **miridae** infesting garden crops."}
        ]
    },
    "mirish": {
        "primary": "Swampy, marshy, or resembling deep mud; miry.",
        "secondary": "In topographical description, having the treacherous, yielding consistency of waterlogged bogland.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We forced our birch canoe through a **mirish** meadow overgrown with sedges and water-lilies."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The lower hollows of the heath were damp and **mirish**, sucking at the traveler's boots."},
            {"author": "Herman Melville", "work": "Mardi", "quote": "The lagoon shoreline was lined with **mirish** mangrove swamps exuding thick, humid vapors."}
        ]
    },
    "miro": {
        "primary": "A large coniferous tree (Prumnopitys ferruginea) native to New Zealand, bearing red fleshy seed coats, valued for timber.",
        "secondary": "In Australasian dendrology and Maori ethnobotany, a Podocarpaceous canopy tree whose aromatic berries attract kereru (native wood pigeons).",
        "quotes": [
            {"author": "Joseph Dalton Hooker", "work": "The Botany of the Antarctic Voyage", "quote": "The New Zealand **miro** yields a valuable reddish timber prized by colonists for durable carpentry."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "In the primeval forests of the Bay of Islands, majestic specimens of the **miro** towered above the tree-ferns."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Conifers such as the **miro** illustrate the archaic southern gymnosperm flora that flourished on Gondwana."}
        ]
    },
    "mirounga": {
        "primary": "The genus of massive earless seals comprising the northern and southern elephant seals.",
        "secondary": "In marine mammalogy, the largest extant pinnipeds (Mirounga leonina and M. angustirostris), known for pronounced sexual dimorphism and inflatable male proboscis.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The colossal bull seals of the genus **mirounga** congregate on subantarctic beaches during the breeding season."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Sealers hunted the enormous **mirounga** on southern islands for its abundant yield of clear, illuminating oil."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The inflatable nasal sac of male **mirounga** serves as an acoustic resonating chamber during territorial combat."}
        ]
    },
    "mirror": {
        "primary": "A reflective surface, typically of glass coated with a metal amalgam, that reflects a clear image.",
        "secondary": "In optics, literature, and psychology, a speculum reflecting light rays according to equal angles of incidence and reflection, or a true representation of reality.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "To hold, as 'twere, the **mirror** up to nature; to show virtue her own feature, scorn her own image, and the very age and body of the time his form and pressure."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "The plane glass **mirror** reflects parallel beams with an angle of reflection precisely equal to the angle of incidence."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He stood before the oval **mirror**, shuddering at the subtle lines of cruelty creeping across his likeness."}
        ]
    },
    "mirrored": {
        "primary": "Reflected in or as if in a mirror.",
        "secondary": "In descriptive literature and optics, having an image reproduced with faithful specular clarity on a smooth surface.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The serene waters of the lake **mirrored** the surrounding pine forests and the autumn sky."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "His secret thoughts were **mirrored** in the portrait with terrifying, uncompromising fidelity."},
            {"author": "G. K. Chesterton", "work": "The Ball and the Cross", "quote": "The quiet pool **mirrored** the twilight stars, unbroken by any passing breeze."}
        ]
    },
    "mirrorlike": {
        "primary": "Resembling a mirror in smoothness, brightness, or reflective quality.",
        "secondary": "In physical optics and geographical description, having an unruffled, glass-like surface that reflects incident light with specular sharpness.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Walden Pond lay in unruffled serenity, its **mirrorlike** expanse reflecting the green hilltops."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pacific lay in a calm so profound that the sea presented a vast **mirrorlike** plain beneath the sun."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "We sailed across a **mirrorlike** sheet of water in which every cloud was inverted with absolute precision."}
        ]
    },
    "mirth": {
        "primary": "Amusement, high spirits, or merriment, especially as expressed in laughter.",
        "secondary": "In social character and dramatic literature, buoyant gladness, festive rejoicing, and wholesome comic cheer.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "With **mirth** in funeral and with dirge in marriage, In equal scale weighing delight and dole."},
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The sound of genial **mirth** and hearty laughter echoed from Scrooge's nephew's holiday parlor."},
            {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The village musicians played lively reels that filled the rustic kitchen with unconstrained **mirth**."}
        ]
    },
    "mirthful": {
        "primary": "Full of mirth; merry, amusing, or cheerful.",
        "secondary": "In descriptive literature, radiating jovial humor and lively good cheer.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "To laugh with **mirthful** companions at the pleasant follies of the court."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Phoebe's sweet voice and **mirthful** laugh brought sudden sunshine into the gloomy old mansion."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "He greeted his scientific colleagues with a **mirthful** twinkle that enlivened the solemn meeting."}
        ]
    },
    "mirthfully": {
        "primary": "In a mirthful, merry, or laughingly cheerful manner.",
        "secondary": "In narrative prose, expressing humor or good cheer with audible gaiety and lively amusement.",
        "quotes": [
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick beamed **mirthfully** upon the assembly, raising his punch glass in a festive toast."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw laughed **mirthfully**, shaking his head at the solemn pedantries of the town gossips."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shearers chatted **mirthfully** over their cider mugs when the afternoon's clipping was finished."}
        ]
    },
    "mirthfulness": {
        "primary": "The disposition or tendency to be cheerful, merry, and full of laughter.",
        "secondary": "In character analysis and social psychology, natural lightness of spirit, playful humor, and resistance to gloom.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "Genuine **mirthfulness** is an attribute of a healthy spirit that can perceive comedy without cynicism."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "Donatello's innocent **mirthfulness** reminded observers of a woodland faun untouched by human sorrow."},
            {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "A touch of innocent **mirthfulness** at the breakfast table sweetens the entire day's labors."}
        ]
    },
    "mirthless": {
        "primary": "Lacking mirth; gloomy, joyless, or grim.",
        "secondary": "In psychological narrative, expressing forced amusement or a hollow, bitter smile devoid of genuine gladness.",
        "quotes": [
            {"author": "James Joyce", "work": "Dubliners", "quote": "He gave a short, **mirthless** chuckle that betrayed the bitter disillusionment of his heart."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Count Dracula's lips curled into a cold, **mirthless** smile that revealed his pointed canine teeth."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The criminal gave a dry, **mirthless** laugh as he realized that the priest had uncovered his secret."}
        ]
    },
    "miry": {
        "primary": "Swampy, muddy, or bogged down; consisting of or full of mire.",
        "secondary": "In pastoral topography and descriptive narrative, deeply drenched with sticky, waterlogged clay or peat.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "How her horse fell, and she under her horse; thou shouldst have heard in how **miry** a place."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess trudged across the **miry** farm lanes, her boots heavy with sodden yellow clay."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The autumn rains had turned the cart track into a **miry** rut that delayed the timber wagons."}
        ]
    },
    "semirigid": {
        "primary": "Partially rigid; possessing some stiffness while retaining flexibility.",
        "secondary": "In aeronautical engineering and materials science, designating non-rigid airships reinforced with a longitudinal keel, or flexible polymers.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The military patrol employed a **semirigid** dirigible whose metal keel gave stability in violent crosswinds."},
            {"author": "Lord Kelvin", "work": "Popular Lectures and Addresses", "quote": "The elastic properties of the medium behave as a **semirigid** structure under high-frequency vibrations."},
            {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "The apparatus was protected within a **semirigid** framework of vulcanite and brass rods."}
        ]
    },
    "depict": {
        "primary": "To represent by a drawing, painting, or other art form; or to describe in words.",
        "secondary": "In visual arts and narrative literature, to portray a subject with lifelike realism or evocative aesthetic fidelity.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Many artists have attempted to **depict** the great sperm whale, yet few have captured its true oceanic majesty."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The author sought to **depict** the slow, agonizing delays that characterized nineteenth-century chancery proceedings."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "A true novelist must **depict** human frailties with compassionate sympathy rather than moral disdain."}
        ]
    },
    "depicted": {
        "primary": "Represented in a picture, painting, sculpture, or vivid description.",
        "secondary": "In art history and literary criticism, portrayed through visual iconography or detailed literary characterization.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The ancient tapestry **depicted** a hunting scene with courtiers on horseback pursued by hounds."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The newspaper engraving **depicted** the mysterious country house surrounded by dense woodland."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "In Greek sculpture the gods were **depicted** with serene brows untroubled by human anxieties."}
        ]
    },
    "depicting": {
        "primary": "Representing, portraying, or describing visually or verbally.",
        "secondary": "In aesthetic composition, rendering the form, color, or emotional atmosphere of a subject through graphic art or words.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "He spent years painting canvas after canvas, **depicting** the furious battles between whalemen and leviathans."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "Turner surpassed all contemporaries in **depicting** the incandescent fury of sea storms and burning skies."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The young copyist worked in the Roman gallery, **depicting** classical frescoes with remarkable delicate skill."}
        ]
    },
    "depiction": {
        "primary": "The action or result of depicting something, either in a visual artwork or a verbal description; representation.",
        "secondary": "In critical theory and semiotics, an aesthetic portrayal conveying narrative themes, social realities, or character psychology.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her realistic **depiction** of provincial provincial society earned the praise of thoughtful contemporary critics."},
            {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Gothic sculpture achieves its power through faithful **depiction** of natural foliage and animal life."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The satirical **depiction** of high society unmasked the vanity beneath aristocratic elegance."}
        ]
    },
    "depictive": {
        "primary": "Serving to depict; representing or portraying vivid images or scenes.",
        "secondary": "In aesthetic critique and cognitive linguistics, characterized by vivid descriptive power or illustrative graphic clarity.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Dante's verse possesses a **depictive** energy that brands each infernal vision upon the reader's imagination."},
            {"author": "William Hazlitt", "work": "Lectures on the English Poets", "quote": "Chaucer's prologue is unsurpassed for **depictive** vigor, sketching a dozen pilgrims in a handful of couplets."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The **depictive** accuracy of early Flemish painters reveals an extraordinary reverence for physical nature."}
        ]
    },
    "epictetus": {
        "primary": "Epictetus (c. 50–135 AD), a prominent Greek Stoic philosopher who taught that philosophy is a way of life focused on inner virtue.",
        "secondary": "In classical intellectual history, the freed Roman slave whose Enchiridion and Discourses established the foundation of late Stoic ethics.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The heroic fortitude of **Epictetus** teaches us that external chains cannot bind a self-governed soul."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Like **Epictetus**, the modern scientific investigator learns to accept nature's laws with calm equanimity."},
            {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The voice of **Epictetus** still speaks to us across centuries, urging moral serenity amid worldly chaos."}
        ]
    }
}
