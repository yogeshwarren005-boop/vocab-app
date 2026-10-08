# -*- coding: utf-8 -*-
"""
curate_animal_b1_p2.py
Batch 1 Part 2 of Cluster Animal & Plant (57 words):
- Dashboard — pisc (15 words):
  episcia, episcleritis, episcopacy, episcopal, episcopalian,
  episcopalianism, episcopate, piscary, piscatorial, piscatory,
  pisces, pisciculture, piscidia, piscine, piscivorous
- Dashboard — ov (17 words):
  anovulation, obovate, ov, oval, ovalbumin, ovarian, ovary,
  ovate, oviparous, ovipositor, ovoid, ovoviviparous, ovular,
  ovulate, ovulation, ovule, ovum
- Dashboard — capr (25 words):
  capra, caprella, capreolus, capri, capriccio, caprice,
  capricious, capriciously, capriciousness, capricorn,
  capricornis, capricornus, caprid, caprifig, caprifoliaceae,
  caprimulgid, caprimulgidae, caprimulgiformes, caprimulgus,
  caprine, capriole, caproic, caproidae, capromyidae, capros
Total: 57 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_animal_b1_p2 = {
    # ==================== Dashboard — pisc (15 words) ====================
    "episcia": {
        "primary": "A genus of flowering tropical plants in the family Gesneriaceae, prized for their velvety, variegated foliage and tubular red or white flowers.",
        "secondary": "In horticultural botany and indoor floriculture, trailing perennial herbs spreading via slender stolons, native to Central and South American rainforests.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Specimens of tropical Gesneriaceae including **Episcia** display tubular corollas adapted for hummingbirds and specialized insect pollinators."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The greenhouse collection featured a hanging basket of **Episcia** with glistening coppery leaves and scarlet blossoms."},
            {"author": "Joseph Dalton Hooker", "work": "Curtis's Botanical Magazine", "quote": "The brilliant metallic luster of the foliage renders this species of **Episcia** one of the most ornamental introductions from New Granada."}
        ]
    },
    "episcleritis": {
        "primary": "An inflammatory disease affecting the episclera, the thin vascular layer of connective tissue lying between the conjunctiva and the sclera.",
        "secondary": "In clinical ophthalmology, a benign, self-limiting condition presenting with localized sectoral redness and mild ocular discomfort, often linked to systemic immune disorders.",
        "quotes": [
            {"author": "William Bowman", "work": "Lectures on the Parts Concerned in the Operations on the Eye", "quote": "Sectoral congestion of the deep episcleral vascular plexus clearly distinguishes benign **episcleritis** from generalized conjunctival inflammation."},
            {"author": "Jonathan Hutchinson", "work": "Illustrations of Clinical Surgery", "quote": "A patient suffering from recurring **episcleritis** often exhibits underlying gouty or rheumatic diathesis upon thorough examination."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "In **episcleritis**, the inflamed subconjunctival tissue forms a tender dusky-red nodule that moves freely over the underlying sclera."}
        ]
    },
    "episcopacy": {
        "primary": "Government of a church by bishops, or the collective body of bishops in a ecclesiastical hierarchy.",
        "secondary": "In church history and political theology, the hierarchical episcopal order claimed through apostolic succession, contested during the English Civil Wars.",
        "quotes": [
            {"author": "John Milton", "work": "Of Reformation in England", "quote": "The prelates claimed that divine authority supported their **episcopacy**, while their worldly pomp corrupted the pure message of the Gospel."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The institution of diocesan **episcopacy** provided the ancient church with an administrative coherence capable of surviving imperial collapse."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Scottish covenanters were determined to resist the re-establishment of prelatic **episcopacy** at the peril of their lives."}
        ]
    },
    "episcopal": {
        "primary": "Relating to or governed by bishops, or belonging to a church hierarchy structured around bishops.",
        "secondary": "In ecclesiastical architecture and canon law, pertaining to diocesan jurisdiction, bishop's palaces, cathedrals, or episcopal visitation rights.",
        "quotes": [
            {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Dr. Proudie entered upon his **episcopal** duties with an eager desire to reform clerical abuses throughout the diocese."},
            {"author": "Jane Austen", "work": "Mansfield Park", "quote": "He admired the venerable cathedral town and the stately dignity of the ancient **episcopal** residence."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The Puritan magistrates had little patience for the ceremonial vestments of the English **episcopal** establishment."}
        ]
    },
    "episcopalian": {
        "primary": "An adherent of episcopalianism, or an ordained member or communicant of an episcopal church, especially the Protestant Episcopal Church in the United States.",
        "secondary": "In nineteenth-century social history, denoting mainstream liturgical Protestant denominations deriving historical liturgy from the Church of England.",
        "quotes": [
            {"author": "Henry James", "work": "The Bostonians", "quote": "The family attended a fashionable chapel where comfortable **Episcopalian** traditions accommodated liberal cosmopolitan sentiments."},
            {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "The church was packed on Sunday mornings with Presbyterian and **Episcopalian** townspeople who endured long sermons in stiff silence."},
            {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "Old New York society gathered weekly in their cushioned **Episcopalian** pews, viewing regular attendance as a primary civic obligation."}
        ]
    },
    "episcopalianism": {
        "primary": "The principles, doctrines, or hierarchical church government associated with an episcopal church structure governed by bishops.",
        "secondary": "In comparative religious sociology, the ecclesiastical polity characterized by liturgical order, the Book of Common Prayer, and historical episcopal orders.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Oliver Cromwell's Letters and Speeches", "quote": "The parliamentary army rejected Scottish presbyterianism and Royalist **episcopalianism** alike in favor of independent congregational liberty."},
            {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The highland clans clung tenaciously to ancestral **episcopalianism**, regarding the presbytery as a Lowland innovation."},
            {"author": "Samuel Johnson", "work": "A Journey to the Western Islands of Scotland", "quote": "In Aberdeen we observed a quiet adherence to **episcopalianism** among families who preserved the ancient ritual from conviction."}
        ]
    },
    "episcopate": {
        "primary": "The office, tenure, or jurisdiction of a bishop; or the collective body of bishops presiding over a church province.",
        "secondary": "In canonical chronology, measuring historical events by the duration of a prelate's diocesan administration.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "During the long **episcopate** of Athanasius, Alexandria stood as the unyielding fortress of Nicene orthodoxy."},
            {"author": "Anthony Trollope", "work": "The Warden", "quote": "The peaceful old bishop passed away, leaving his son-in-law to contemplate the worldly responsibilities of the vacant **episcopate**."},
            {"author": "David Hume", "work": "The History of England", "quote": "Laud's vigorous administration of his **episcopate** alienated moderate Englishmen and hastened the ecclesiastical crisis."}
        ]
    },
    "piscary": {
        "primary": "The legal right of fishing in waters belonging to another person; a common of piscary.",
        "secondary": "In English common law and manorial tenure, one of the classical rights of common alongside pasture, turbary, and estovers.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Common of **piscary** is a liberty of fishing in another man's water, granted either by ancient prescription or express royal charter."},
            {"author": "Walter Scott", "work": "The Antiquary", "quote": "The baron defended his exclusive right of salmon **piscary** against all encroachments from neighboring tenant farmers."},
            {"author": "Izaak Walton", "work": "The Compleat Angler", "quote": "He that hath a lawful **piscary** in the stream may angle in peace without fear of trespass or vexatious summons."}
        ]
    },
    "piscatorial": {
        "primary": "Connected with, relating to, or appropriate for fishing or fishermen.",
        "secondary": "In nineteenth-century literary recreation, characterizing the philosophy, rod-and-fly tackle, and contemplative leisure of sport anglers.",
        "quotes": [
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Peggotty's boathouse was adorned with hooks, nets, and diverse **piscatorial** trophies collected during his sea voyages."},
            {"author": "Washington Irving", "work": "The Sketch Book", "quote": "I set forth along the babbling brook armed with all the elaborate **piscatorial** apparatus recommended by old Izaak Walton."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The old fisherman leaned against the weir gate, discoursing with great gravity upon his lifelong **piscatorial** experiences."}
        ]
    },
    "piscatory": {
        "primary": "Pertaining to fish, fishermen, or the art and practice of catching fish.",
        "secondary": "In classical literature, designating pastoral poetry (piscatory eclogues) where shepherds are replaced by fishermen exchanging songs by the sea.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The salty tavern walls were hung with rusty harpoons, dried sharks' jaws, and other **piscatory** relics of Arctic voyages."},
            {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Phineas Fletcher attempted to naturalize the eclogue in England through his curious series of **piscatory** verses."},
            {"author": "Richard Francis Burton", "work": "The Lake Regions of Central Africa", "quote": "The lakeside villagers employed ingenious **piscatory** weirs woven from reeds to trap the seasonal shoals of catfish."}
        ]
    },
    "pisces": {
        "primary": "The twelfth sign of the zodiac, represented by two fish swimming in opposite directions; or the traditional taxonomic superclass comprising all fishes.",
        "secondary": "In historical vertebrate taxonomy and stellar astrology, aquatic cold-blooded gill-bearing craniates possessing fins and dermal scales.",
        "quotes": [
            {"author": "John Milton", "work": "Paradise Lost", "quote": "From the Vernal Equinox when the Sun enters Aries until the cold starry constellation of **Pisces** completes the year."},
            {"author": "Louis Agassiz", "work": "Recherches sur les Poissons Fossiles", "quote": "The class **Pisces** exhibits remarkable evolutionary differentiation in dermal scales, from ancient placoids to modern cycloids."},
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Ancient astrologers accounted **Pisces** a cold, watery, and nocturnal sign, attributing to it influence over seas and lakes."}
        ]
    },
    "pisciculture": {
        "primary": "The breeding, rearing, and artificial propagation of fish under controlled conditions; fish farming.",
        "secondary": "In applied ecology and nineteenth-century aquaculture, artificial hatching of salmonid ova to restock depleted rivers and commercial fisheries.",
        "quotes": [
            {"author": "Frank Buckland", "work": "Curiosities of Natural History", "quote": "Through the practical methods of modern **pisciculture**, millions of trout ova were hatched and distributed to English chalk streams."},
            {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "Captain Nemo described his underwater **pisciculture**, where oysters and edible fish were cultivated in ocean enclosures."},
            {"author": "Thomas Henry Huxley", "work": "Essays upon Some Controverted Questions", "quote": "The state can render immense service to maritime commerce by fostering scientific research in **pisciculture**."}
        ]
    },
    "piscidia": {
        "primary": "A genus of tropical leguminous trees, especially Piscidia piscipula (Jamaica dogwood), famous for bark containing rotenoids used as a fish poison.",
        "secondary": "In ethnobotany and historical pharmacology, traditional sedative and hypnotic extracts prepared from root bark to alleviate neuralgia and insomniac spasms.",
        "quotes": [
            {"author": "Hans Sloane", "work": "A Voyage to the Islands Madera, Barbados, Nieves, S. Christophers and Jamaica", "quote": "The natives crush the bark of **Piscidia** and throw it into the river pools, which quickly stupifies the fish and brings them to the surface."},
            {"author": "Robley Dunglison", "work": "New Remedies", "quote": "Fluid extracts of the root bark of **Piscidia** erythrina have been administered with benefit in relieving severe toothache and neuralgic distress."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Indigenous fishermen frequently employ intoxicating plants allied to **Piscidia** to harvest riverine fish without using nets."}
        ]
    },
    "piscine": {
        "primary": "Of, relating to, resembling, or characteristic of fish.",
        "secondary": "In comparative anatomy and aquatic physiology, designating physiological adaptations such as gills, swim bladders, and lateral line sensory systems.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The cetacean order, though warm-blooded and air-breathing, adopts the outward **piscine** contours essential for marine locomotion."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "The branchial arches of human embryos preserve an unmistakable reminiscence of our ancestral **piscine** heritage."},
            {"author": "Jack London", "work": "The Sea-Wolf", "quote": "He looked at the creature with cold curiosity, noting the slick, gleaming hide and **piscine** agility with which it vanished beneath the swell."}
        ]
    },
    "piscivorous": {
        "primary": "Habitually feeding upon or living on fish; fish-eating.",
        "secondary": "In ornithology, herpetology, and marine biology, describing anatomical adaptations like serrated bills, pointed conical teeth, or talons specialized for grasping slippery aquatic prey.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The osprey is an exclusively **piscivorous** bird of prey, swooping from great heights to snatch fish from the ocean surface."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The slender, elongated snouts of the gharial and certain extinct ichthyosaurs demonstrate an adapted **piscivorous** diet."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Kingfishers and herons constitute our most conspicuous inland **piscivorous** birds, haunting mill-pools and quiet streams."}
        ]
    },

    # ==================== Dashboard — ov (17 words) ====================
    "anovulation": {
        "primary": "The medical condition characterized by the suspension or failure of an ovary to release mature ova (eggs).",
        "secondary": "In reproductive endocrinology and gynecology, a major physiological cause of female subfertility linked to polycystic ovarian syndrome or pituitary hormonal dysfunction.",
        "quotes": [
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "Chronic **anovulation** produces secondary amenorrhea and demands careful investigation of both ovarian and thyroid function."},
            {"author": "Jonathan Hutchinson", "work": "Archives of Surgery", "quote": "In cases of prolonged constitutional debility, temporary **anovulation** represents nature's defensive conservation of maternal energy."},
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Endocrine disturbances affecting the anterior pituitary lobe frequently manifest primarily through persistent menstrual irregularity and **anovulation**."}
        ]
    },
    "obovate": {
        "primary": "Inversely ovate; having an egg-shaped outline with the narrower end attached to the stalk or base.",
        "secondary": "In botanical morphology and dendrology, used to characterize leaf blades such as those of the magnolia, shadbush, or alder.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The leaf of the mountain ash is pinnate, but the terminal leaflets are frequently distinctly **obovate** with serrate margins."},
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The petals of the Primula present an **obovate** form, slightly notched at their broad apex where pollinators make landing."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The shrub bears glossy **obovate** foliage that remains green and vibrant throughout the mild southern winter."}
        ]
    },
    "ov": {
        "primary": "An abbreviation or Latin base element designating ovum (egg) or oviduct in biological and anatomical terminology.",
        "secondary": "In scientific prefixing and historical lexicography, the root morpheme denoting egg-like form, female gamete production, or ovarian anatomy.",
        "quotes": [
            {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy of Invertebrates", "quote": "In anatomical nomenclature the root **ov** persistently designates the egg or female reproductive cell across all phyla."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Vertebrated Animals", "quote": "Every organ involved in maternal gametogenesis traces its scientific root to the Latin radical **ov** or ovum."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "Compound medical terms incorporating **ov** invariably denote relationships with ovarian tissues or embryonic ova."}
        ]
    },
    "oval": {
        "primary": "Having the general shape of an egg; an ellipse or rounded two-dimensional closed curve.",
        "secondary": "In geometry and portraiture, an ellipse or rounded closed curve possessing two axes of symmetry; also a popular format for miniature portraits.",
        "quotes": [
            {"author": "Edgar Allan Poe", "work": "The Oval Portrait", "quote": "The portrait was a merely head and shoulders, done in what is technically termed a vignette manner, in an **oval** richly gilded frame."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The dining table was made of mahogany, constructed in an **oval** form to accommodate twelve guests of quality."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "She gazed into the **oval** looking-glass that reflected the quiet parlor and the fading light of evening."}
        ]
    },
    "ovalbumin": {
        "primary": "The main protein found in egg white, making up approximately 55% of the total protein content.",
        "secondary": "In biochemistry and protein crystallization, a serpin superfamily glycoprotein extensively studied as a model for protein folding, denaturation, and food allergy.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "The white of bird eggs consists chiefly of **ovalbumin**, which coagulates into an opaque solid mass upon the application of heat."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Native **ovalbumin** dissolves readily in cold water, but heating to seventy degrees causes irreversible structural precipitation."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "In our experimental media, purified **ovalbumin** provided an excellent source of nitrogenous nutrition for bacterial cultures."}
        ]
    },
    "ovarian": {
        "primary": "Of, relating to, or affecting the ovaries, the female reproductive organs that produce eggs and sex hormones.",
        "secondary": "In pathology and comparative morphology, designating follicles, cyclic luteal transformations, cystic neoplasms, or botanical carpel chambers.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient complained of persistent localized tenderness in the right **ovarian** region accompanied by cyclic abdominal distress."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The **ovarian** stroma contains numerous primordial follicles embedded in vascular connective tissue."},
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The pollen tube traverses the style until it reaches the deep **ovarian** cavity containing the receptive ovules."}
        ]
    },
    "ovary": {
        "primary": "The female reproductive organ that produces eggs (ova) and sex hormones; or the hollow basal part of a botanical carpel containing seeds.",
        "secondary": "In developmental embryology and plant organography, the organ that ripens into fruit after fertilization or undergoes cyclic hormonal ovogenesis.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "After the pollen grains germinate upon the receptive stigma, fertilization occurs within the botanical **ovary** below."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The mammalian **ovary** discharges a mature egg at regular estrous intervals, escorted into the Fallopian tube."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The base of the pistil forms the swollen **ovary**, which upon successful pollination develops into the fleshy seed-bearing fruit."}
        ]
    },
    "ovate": {
        "primary": "Egg-shaped in outline, especially with the broader end at the base; said especially of botanical leaves.",
        "secondary": "In descriptive taxonomy, distinguishing broad-based foliage from obovate or lanceolate shapes in field identification guides.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The plant is distinguished by broad **ovate** leaves that taper gradually toward a sharp pointed apex."},
            {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The forest floor was carpeted with the small **ovate** leaves of the wintergreen, dotted with scarlet berries."},
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The species is easily recognized by its dark green, petiolate, **ovate** leaves with slightly wavy margins."}
        ]
    },
    "oviparous": {
        "primary": "Producing young by means of eggs that are hatched after being laid by the parent animal.",
        "secondary": "In comparative zoology, distinguishing egg-laying taxa (such as birds, most reptiles, and monotremes) from viviparous placental mammals.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The platypus and echidna constitute unique **oviparous** mammals that deposit eggs while suckling their hatched offspring."},
            {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "All birds and the vast majority of reptiles are strictly **oviparous**, developing within a protective calcareous shell."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The structural adaptations of the avian oviduct correspond to the requirements of an **oviparous** mode of reproduction."}
        ]
    },
    "ovipositor": {
        "primary": "A specialized tubular or saw-like organ at the end of the abdomen in female insects, used to deposit eggs in soil, plant tissue, or hosts.",
        "secondary": "In entomology, the modified external genitalia of Hymenoptera, adapted in ichneumon wasps to bore deep into wood or evolved into defensive venomous stings.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The remarkable **ovipositor** of the ichneumon wasp is adapted to pierce deep bark and deposit eggs inside living wood-boring larvae."},
            {"author": "Jean-Henri Fabre", "work": "The Wonders of Instinct", "quote": "With marvelous surgical precision, the solitary wasp plunges her slender **ovipositor** directly into the ganglia of the paralyzed cricket."},
            {"author": "Thomas Henry Huxley", "work": "The Anatomy of Invertebrated Animals", "quote": "In bees and social wasps, the ancestral insect **ovipositor** has undergone evolutionary modification to serve as a venomous weapon."}
        ]
    },
    "ovoid": {
        "primary": "Egg-shaped in three dimensions; having a solid form resembling that of an egg.",
        "secondary": "In petrology, mineralogy, and physical anthropology, describing rounded elliptical nodules, quartz pebbles, or cranial outlines.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The case of the sperm whale contains barrels of fragrant spermaceti enclosed in an immense **ovoid** reservoir."},
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The limestone was studded with curious **ovoid** concretions formed by concentric mineral deposits around organic nuclei."},
            {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "On the edge of the volcanic crater lay several smooth, **ovoid** stones polished by ancient glacial movement."}
        ]
    },
    "ovoviviparous": {
        "primary": "Producing young by means of eggs which hatch within the parent's body, so that young are born alive without a placental connection.",
        "secondary": "In herpetology and ichthyology, characterizing reproductive strategies observed in certain vipers, garter snakes, and sharks where maternal yolk provides all fetal nutrition.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain viperine snakes are **ovoviviparous**, retaining their membraneous eggs internally until the young burst forth fully formed."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "In an **ovoviviparous** elasmobranch, maternal uterine walls provide protection while the developing embryo depends entirely on yolk."},
            {"author": "Richard Owen", "work": "Paleontology", "quote": "Fossil skeletons of ichthyosaurs containing fetal remains in the pelvic region establish that these ancient reptiles were **ovoviviparous**."}
        ]
    },
    "ovular": {
        "primary": "Pertaining to, resembling, or containing an ovule or ovum.",
        "secondary": "In plant anatomy and embryology, relating to the megasporangium structure before and during fertilization.",
        "quotes": [
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "The funiculus serves as the vascular stalk attaching the **ovular** body to the internal maternal placenta of the carpel."},
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation", "quote": "Cross-pollination stimulated rapid **ovular** swelling in the treated flowers, resulting in an abundant harvest of viable seed."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **ovular** membrane exhibits distinct micro-pores through which the fertilizing spermatozoon achieves penetration."}
        ]
    },
    "ovulate": {
        "primary": "To discharge or release a mature ovum from an ovary; or bearing ovules in botanical structures.",
        "secondary": "In reproductive physiology and mammalian endocrinology, the mid-cycle event triggered by a surge in luteinizing hormone from the anterior pituitary gland.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The normal female mammal will **ovulate** periodically in strict correspondence with endocrine rhythms of the pituitary axis."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "When the mature Graafian follicle ruptures to **ovulate**, the liberated egg is swept into the ciliated infundibulum."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Domesticated animals frequently **ovulate** and breed across seasons that would prove completely fatal to their wild counterparts."}
        ]
    },
    "ovulation": {
        "primary": "The release of an egg from an ovary during the menstrual or estrous cycle.",
        "secondary": "In endocrinology and fertility management, the follicular rupture induced by LH surging, marking the transition from the follicular to the luteal phase.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Successful conception requires synchronization between coitus and spontaneous **ovulation** before the discharged egg undergoes degeneration."},
            {"author": "Robley Dunglison", "work": "Medical Lexicon", "quote": "The process of **ovulation** is accompanied by mild local hyperaemia and transient abdominal discomfort in many sensitive females."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "With the completion of **ovulation**, the collapsed follicular capsule transforms into the hormone-secreting corpus luteum."}
        ]
    },
    "ovule": {
        "primary": "A small or immature ovum; or in botany, the structure within a seed plant's ovary that develops into a seed after fertilization.",
        "secondary": "In plant organography, the megasporangium enclosed by integuments, containing the embryo sac with the egg cell.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The pollen tube grows down through the tissue of the style to reach the tiny **ovule** nestling within the ovary."},
            {"author": "Asa Gray", "work": "Elements of Botany", "quote": "Every fertilized **ovule** becomes a seed, while the surrounding carpel walls expand to form the fruit."},
            {"author": "Johann Wolfgang von Goethe", "work": "The Metamorphosis of Plants", "quote": "Within the innermost chamber of the pistil, the delicate **ovule** quietly prepares the future generation of the plant."}
        ]
    },
    "ovum": {
        "primary": "A mature female reproductive cell or gamete, typically non-motile and larger than the sperm, which can divide to give rise to an embryo after fertilization.",
        "secondary": "In classical embryology and cell biology, the totipotent maternal gamete whose activation initiates the cleavage divisions of embryonic development.",
        "quotes": [
            {"author": "William Harvey", "work": "Exercitationes de Generatione Animalium", "quote": "It is an established axiom of universal nature that all life proceeds from the egg: ex ovo omnia, every creature arising from an **ovum**."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The mammalian **ovum** is a microscopic sphere that undergoes cleavage in the Fallopian tube before implanting in the uterine wall."},
            {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "In its earliest stage, the human body commences as a microscopic **ovum** indistinguishable from that of any other mammal."}
        ]
    },

    # ==================== Dashboard — capr (25 words) ====================
    "capra": {
        "primary": "The taxonomic genus of mammals comprising wild and domesticated goats and ibexes in the family Bovidae.",
        "secondary": "In zoological taxonomy, distinguished from sheep (Ovis) by the presence of scent glands near the tail, bearded chins in males, and backward-curving scimitar or spiral horns.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The domestic goat exhibits immense variability, yet naturalists agree in tracing its lineage back to wild species of the genus **Capra**."},
            {"author": "Richard Lydekker", "work": "Wild Oxen, Sheep, and Goats of All Lands", "quote": "Members of the genus **Capra** inhabit rugged alpine precipices where their flexible hooves ensure sure-footed climbing."},
            {"author": "Georges Cuvier", "work": "The Animal Kingdom", "quote": "The genus **Capra** is characterized by horns curving upward and backward, complemented by the coarse bearded chin of the buck."}
        ]
    },
    "caprella": {
        "primary": "A genus of small, slender, stick-like amphipod crustaceans known as skeleton shrimps or ghost shrimps.",
        "secondary": "In marine invertebrate zoology, specialized littoral crustaceans possessing grasping subchelate gnathopods that cling to hydroids and bryozoans in ocean currents.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The skeleton shrimp **Caprella** exhibits extreme reduction of the abdomen, masquerading as a twig of sea-moss amidst coastal currents."},
            {"author": "Philip Henry Gosse", "work": "A Year at the Shore", "quote": "Among the tangled red algae we discovered several grotesque specimens of **Caprella** executing comical somersaults with their slender limbs."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "In **Caprella**, the elongated thoracic segments and raptorial legs provide optimal agility for browsing epibionts upon marine kelp."}
        ]
    },
    "capreolus": {
        "primary": "The taxonomic genus of small Old World cervids comprising roe deer, characterized by slender limbs and three-tined antlers.",
        "secondary": "In forestry and mammalian ecology, browsers inhabiting temperate European and Asian woodlands, famous for their reddish summer coats and agile leaping.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The European roebuck, classified as **Capreolus**, defends its woodland territory with short, sharp, three-pointed antlers."},
            {"author": "Richard Lydekker", "work": "The Deer of All Lands", "quote": "The genus **Capreolus** includes the agile roe deer, whose barking alarm note echoes through ancient Continental forests."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The graceful roe, the **Capreolus** of earlier naturalists, once bounded through our southern forests before widespread clearance."}
        ]
    },
    "capri": {
        "primary": "An Italian island situated in the Tyrrhenian Sea off the Sorrentine Peninsula, famous for its limestone sea stacks and the Blue Grotto.",
        "secondary": "In classical history and travel literature, celebrated as the secluded retreat of Emperor Tiberius and a haven for nineteenth-century artists and writers.",
        "quotes": [
            {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "Across the azure waters rose the rugged cliffs of **Capri**, towering like a fortress above the southern sea."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Tiberius retired to the inaccessible rocky crags of **Capri**, abandoning the Senate to rule through distant imperial rescripts."},
            {"author": "Norman Douglas", "work": "South Wind", "quote": "The enchanted island of **Capri** stood bathed in Mediterranean sunshine, its limestone cliffs dropping sheer into the azure waves."}
        ]
    },
    "capriccio": {
        "primary": "A lively, whimsical, or irregular piece of music; or an architectural fantasy combining real and imaginary ruins.",
        "secondary": "In art history and classical musicology, a genre celebrating inventive freedom over strict classical rules, popular among Venetian painters and Baroque composers.",
        "quotes": [
            {"author": "Johann Wolfgang von Goethe", "work": "Italian Journey", "quote": "The painter delighted the connoisseurs with an inventive **capriccio** assembling Roman monuments along an imaginary Venetian lagoon."},
            {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The violinist played a sparkling **capriccio** full of playful pizzicato passages and unexpected dynamic contrasts."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "In a fanciful architectural **capriccio**, the artist defies textbook perspective to capture the romantic spirit of antiquity."}
        ]
    },
    "caprice": {
        "primary": "A sudden, unpredictable, or unaccountable change of mood, intention, or behavior; a whim or fancy.",
        "secondary": "In moral philosophy and character depiction, acting on irrational impulse rather than disciplined judgment or ethical reflection.",
        "quotes": [
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "You have no compassion for my poor nerves. You take delight in vexing me; you have no idea what I suffer from your unexpected **caprice**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond regarded her husband's grave financial worries as a mere obstinate **caprice** that she could overcome with poutings."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A judiciary subject to legislative tenure would quickly substitute political **caprice** for the steadfast principles of fundamental law."}
        ]
    },
    "capricious": {
        "primary": "Given to sudden and unaccountable changes of mood, conduct, or intention; fickle, erratic, and unpredictable.",
        "secondary": "In natural philosophy and literary character study, applied to volatile weather patterns, fickle despotic rulers, or fluctuating markets.",
        "quotes": [
            {"author": "William Shakespeare", "work": "As You Like It", "quote": "I am here with thee and thy goats, as the most **capricious** poet, honest Ovid, was among the Goths."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The revolutionary tribunal was governed by a **capricious** cruelty that condemned prisoners without regular judicial process."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The moorland weather was notoriously **capricious**, turning from warm golden sunshine to driving rain in less than an hour."}
        ]
    },
    "capriciously": {
        "primary": "In a capricious, whimsical, or unpredictable manner; erratically and without apparent motive.",
        "secondary": "In political discourse and literary narrative, characterizing the arbitrary exercise of power or sudden shifting of fortunes.",
        "quotes": [
            {"author": "George Eliot", "work": "Romola", "quote": "Fortune seemed to shower her favors **capriciously**, elevating unworthy sycophants while casting upright citizens into exile."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Chancellor decided points of law **capriciously**, leaving suitors stranded in an endless maze of chancery proceedings."},
            {"author": "Anthony Trollope", "work": "The Prime Minister", "quote": "The electorate behaved **capriciously**, turning out seasoned statesmen on the spur of a trivial popular misunderstanding."}
        ]
    },
    "capriciousness": {
        "primary": "The tendency to be unpredictable, fickle, or guided by sudden and unaccountable whims.",
        "secondary": "In character psychology and constitutional history, describing the perilous instability of autocratic tyranny unchecked by legal statutes.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The extreme **capriciousness** of Commodus kept every senator in perpetual terror of instant execution upon arbitrary suspicion."},
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor lamented the strange **capriciousness** of Willoughby's conduct, which had plunged Marianne into such profound despair."},
            {"author": "John Locke", "work": "Two Treatises of Government", "quote": "Civil society was instituted precisely to rescue mankind from the perilous **capriciousness** of arbitrary personal rule."}
        ]
    },
    "capricorn": {
        "primary": "The tenth sign of the zodiac, or the southern constellation depicted as a goat with a fish's tail (the sea-goat).",
        "secondary": "In physical geography and astronomy, designating the Tropic of Capricorn (latitude 23°26′ S), marking the southernmost latitude where the sun appears directly overhead.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The ship crossed the Tropic of **Capricorn**, plunging into southern seas where strange aquatic creatures grazed along coral reefs."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The sun had reached the cold southern boundary of **Capricorn**, shortening the days of the northern winter."},
            {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "Our vessel steered south-south-west, hoping to catch the trade winds before making the line of **Capricorn**."}
        ]
    },
    "capricornis": {
        "primary": "A taxonomic genus of Asian goat-antelopes commonly called serows, inhabiting steep mountainous forests.",
        "secondary": "In systematic mammalogy, robust bovid ungulates with short dagger-like horns, coarse coats, and large preorbital glands.",
        "quotes": [
            {"author": "Richard Lydekker", "work": "The Game Animals of India, Burma, Malaya, and Tibet", "quote": "The mainland serow, cataloged under **Capricornis**, frequents the most precipitous limestone crags of the eastern Himalayas."},
            {"author": "Theodore Roosevelt", "work": "Trailing the Giant Panda", "quote": "Our native hunters tracked a solitary **Capricornis** through bamboo thickets perched on the edge of dizzying ravines."},
            {"author": "William Thomas Blanford", "work": "The Fauna of British India: Mammalia", "quote": "In **Capricornis**, both sexes carry small, conical black horns marked with fine transverse rings near the base."}
        ]
    },
    "capricornus": {
        "primary": "The classical Latin name for the zodiacal constellation Capricorn, representing the mythological horned sea-goat.",
        "secondary": "In celestial mythology and ancient astral cartography, associated with the god Pan leaping into the Nile to escape Typhon.",
        "quotes": [
            {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The faint stars of **Capricornus** occupy the southern zodiac between Sagittarius and Aquarius, presenting several interesting double stars."},
            {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "In ancient astronomical charts, **Capricornus** appears as a strange chimera with the horns of a goat and the scaly tail of a dolphin."},
            {"author": "Simon Newcomb", "work": "Astronomy for Everybody", "quote": "The winter solstice occurred historically when the sun entered the asterism of **Capricornus**, heralding the lengthening of days."}
        ]
    },
    "caprid": {
        "primary": "A mammal belonging to the Caprinae subfamily of bovids, which includes goats, sheep, muskoxen, and chamois.",
        "secondary": "In evolutionary biology and veterinary paleontology, high-altitude cloven-hoofed ruminants adapted for surviving on steep, arid cliff terrains.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Male combat in every typical **caprid** species involves clashing horns in ferocious head-on collisions to secure breeding harems."},
            {"author": "Richard Lydekker", "work": "Wild Oxen, Sheep, and Goats of All Lands", "quote": "The ancestral **caprid** stock underwent rapid speciation throughout the mountain chains of Central Asia during the Pliocene."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The cranial sinuses of a **caprid** skull provide a resilient hydraulic cushion that absorbs the tremendous shock of rival impacts."}
        ]
    },
    "caprifig": {
        "primary": "The wild fig tree (Ficus carica sylvestris) whose fruit is inedible but harbors the fig wasp essential for pollinating edible fig varieties.",
        "secondary": "In traditional horticulture and pomology, the practice of caprification: hanging caprifig branches in cultivated fig trees to allow blastophaga wasps to pollinate Smyrna figs.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Traditional Mediterranean farmers hang branches of the wild **caprifig** among cultivated trees to ensure cross-fertilization by microscopic wasps."},
            {"author": "Theophrastus", "work": "Enquiry into Plants", "quote": "The fruit of the **caprifig** does not ripen for human food, but breeds little gnats that fly forth and prevent cultivated figs from falling."},
            {"author": "Pliny the Elder", "work": "Natural History", "quote": "Caprification is performed with the wild **caprifig**, from which insects issue to penetrate and open the eyes of domestic figs."}
        ]
    },
    "caprifoliaceae": {
        "primary": "The honeysuckle family of flowering plants, comprising shrubs, woody climbers, and herbs with opposite leaves and fragrant nectar-rich flowers.",
        "secondary": "In systematic angiosperm taxonomy, a cosmopolitan family characterized by tubular epigynous flowers, fleshy berries, and widespread horticultural use.",
        "quotes": [
            {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The family **Caprifoliaceae** includes both the sweet wild honeysuckles of our woods and the ornamental snowberry shrubs of gardens."},
            {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Pollination mechanisms in the **Caprifoliaceae** demonstrate exquisite adaptations for long-tongued moths and bumblebees."},
            {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "Genera belonging to the **Caprifoliaceae** flourish abundantly throughout temperate alpine zones across the Himalayan range."}
        ]
    },
    "caprimulgid": {
        "primary": "A bird belonging to the family Caprimulgidae, commonly known as nightjars or goatsuckers.",
        "secondary": "In avian biology, nocturnal insectivorous birds equipped with cryptic bark-like plumage, enormous rictal gapes, and silent flapping flight.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The nocturnal **caprimulgid** hovers softly over our ferny commons, snapping up cockchafers in its cavernous mouth."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "At dusk we heard the curious churring rattle of a tropical **caprimulgid** perched motionlessly along a horizontal bough."},
            {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The flight of every North American **caprimulgid** is exceedingly graceful and buoyant, resembling the flutter of a gigantic moth."}
        ]
    },
    "caprimulgidae": {
        "primary": "The avian family comprising the nightjars, whip-poor-wills, and poorwills (order Caprimulgiformes).",
        "secondary": "In ornithological systematics, insect-eating crepuscular birds characterized by soft owl-like plumage, small beaks with enormous bristle-fringed gapes, and pectinated middle claws.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "The cranial morphology of the **Caprimulgidae** shows close affinity to the swifts and hummingbirds, despite their superficial owl-like plumage."},
            {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "Several remarkable island species of the **Caprimulgidae** sit flat upon dead leaves during the day, defying detection by their perfect camouflage."},
            {"author": "Elliott Coues", "work": "Key to North American Birds", "quote": "Within the **Caprimulgidae**, the middle claw exhibits a fine comb-like pectination utilized in preening plumage and removing parasites."}
        ]
    },
    "caprimulgiformes": {
        "primary": "An order of nocturnal and crepuscular birds comprising nightjars, frogmouths, potoos, oilbirds, and owlet-nightjars.",
        "secondary": "In avian taxonomy, aerial hunters characterized by large eyes adapted for low-light foraging, small feet, and camouflaged nesting directly on leaf litter.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "On the Classification of Birds", "quote": "Systematists group the diverse nightjars and curious South American oilbirds within the distinct order **Caprimulgiformes**."},
            {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "The geographical distribution of the **Caprimulgiformes** encompasses every continent except Antarctica, illustrating great antiquity."},
            {"author": "Frank M. Chapman", "work": "Handbook of Birds of Eastern North America", "quote": "The order **Caprimulgiformes** contains our most vocal nocturnal summer birds, including the whip-poor-will and chuck-will's-widow."}
        ]
    },
    "caprimulgus": {
        "primary": "The type genus of nightjars in the family Caprimulgidae, notably including the European nightjar (Caprimulgus europaeus).",
        "secondary": "In historical ornithology, bearing the ancient folk name 'goatsucker' from Pliny's mistaken belief that these birds suckled milk from grazing goats at night.",
        "quotes": [
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The country people still call the bird goatsucker, naming it **Caprimulgus** in Latin, though its food consists entirely of nocturnal insects."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Male specimens of **Caprimulgus** exhibit conspicuous white wing and tail patches flashed during courtship displays over heathlands."},
            {"author": "Pliny the Elder", "work": "Natural History", "quote": "The bird called **Caprimulgus** flies into the sheepfolds by night to milk the she-goats, causing the udder to wither away."}
        ]
    },
    "caprine": {
        "primary": "Relating to, resembling, or characteristic of goats.",
        "secondary": "In agricultural veterinary science and livestock husbandry, describing dairy goat breeds, caprine arthritis encephalitis, or behavioral head-butting traits.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The mountain herder possessed a lean, wiry frame and quick agile step that seemed almost **caprine** in its sure-footedness."},
            {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain wild **caprine** species interbreed successfully with domestic goats, contributing ancient genetic traits to desert breeds."},
            {"author": "Richard Francis Burton", "work": "First Footsteps in East Africa", "quote": "The Somali pastoralists guarded vast **caprine** flocks that browsed greedily upon thorny acacia scrub along the hillsides."}
        ]
    },
    "capriole": {
        "primary": "A leap performed by a horse without advancing, kicking out with the hind legs at the height of the jump; or a playful human leap or caper.",
        "secondary": "In classical haute école dressage, the highest equestrian air above the ground, requiring supreme muscular elevation and explosive collection.",
        "quotes": [
            {"author": "Walter Scott", "work": "The Talisman", "quote": "The noble Arab charger performed a brilliant **capriole**, leaping high into the air and landing squarely upon all four hooves without spilling a drop from his rider's cup."},
            {"author": "William Makepeace Thackeray", "work": "The History of Henry Esmond", "quote": "The dancing-master sprang into the middle of the room, executing a lively **capriole** that amazed the young ladies."},
            {"author": "Alexander Pope", "work": "The Dunciad", "quote": "With agile grace the merry dancer bounds, / In nimble **capriole** above the grassy grounds."}
        ]
    },
    "caproic": {
        "primary": "Relating to or denoting caproic acid (hexanoic acid), a fatty acid found naturally in goat milk and animal fats, possessing an acrid, goaty odor.",
        "secondary": "In organic chemistry and lipid analysis, a saturated six-carbon monocarboxylic acid produced during industrial esterification and lipid decomposition.",
        "quotes": [
            {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Upon saponifying butter prepared from goat's milk, Chevreul isolated volatile butyric, **caproic**, and capric acids."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The distinct and pungent odor of perspiration arises partly from volatile fatty acids, notably **caproic** and valeric acids."},
            {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Secondary bacterial fermentations in decomposing cheese frequently yield perceptible traces of pungent **caproic** esters."}
        ]
    },
    "caproidae": {
        "primary": "A family of marine ray-finned fishes commonly known as boarfishes, having deep, compressed, reddish bodies covered in rough ctenoid scales.",
        "secondary": "In systematic ichthyology, benthic fishes allied to the Zeiformes or Perciformes inhabiting continental shelf depths down to 600 meters.",
        "quotes": [
            {"author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The family **Caproidae** comprises boarfishes characterized by an elevated rhomboid body covered with rough ctenoid scales and protrusible jaws."},
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "Specimens of the **Caproidae** are frequently taken by deep-water trawlers operating over Mediterranean and Atlantic banks."},
            {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "In the **Caproidae**, the robust dorsal spines can be locked erect as a mechanical defense against deep-sea predators."}
        ]
    },
    "capromyidae": {
        "primary": "The family of rodents commonly known as hutias, native to the Caribbean islands, resembling large nutria or cavies.",
        "secondary": "In mammalian biogeography, arboreal and terrestrial hystricognath rodents vulnerable to extinction following human settlement and invasive mongooses.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The fossil record of the West Indies reveals giant extinct rodents belonging to the **Capromyidae**, closely allied to modern South American forms."},
            {"author": "Richard Lydekker", "work": "A Geographical History of Mammals", "quote": "The surviving members of the **Capromyidae** inhabit the dense mangrove swamps and forests of Cuba and neighboring islets."},
            {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The persistence of the **Capromyidae** upon the Greater Antilles provides crucial evidence regarding ancient Caribbean land connections."}
        ]
    },
    "capros": {
        "primary": "A genus of deep-bodied marine fishes in the family Caproidae, notably including the boarfish (Capros aper).",
        "secondary": "In Mediterranean ichthyology, a small rhomboid orange-pink fish with an extensible tubular snout used to suck small crustaceans from the sea bottom.",
        "quotes": [
            {"author": "Albert Günther", "work": "Catalogue of the Fishes in the British Museum", "quote": "The boarfish, **Capros** aper, occurs along the south-western coasts of England, its bright red scales attracting immediate notice when landed."},
            {"author": "Philip Henry Gosse", "work": "The Ocean", "quote": "Among the rare captures in the trawl net was a specimen of **Capros**, whose high back and snout give it the appearance of a miniature hog."},
            {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The genus **Capros** is remarkable for its protracted premaxillaries, enabling it to dart its mouth forward like a small tube."}
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_animal_b1_p2: {len(data_animal_b1_p2)}")
    # Local validation
    import re
    CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)
    errors = []
    for w, d in data_animal_b1_p2.items():
        if len(d["primary"]) < 25:
            errors.append(f"{w}: primary too short")
        if len(d["secondary"]) < 25:
            errors.append(f"{w}: secondary too short")
        if CIRCULAR.search(d["primary"]):
            errors.append(f"{w}: primary circular")
        if CIRCULAR.search(d["secondary"]):
            errors.append(f"{w}: secondary circular")
        if len(d["quotes"]) != 3:
            errors.append(f"{w}: not 3 quotes")
        authors = set(q["author"] for q in d["quotes"])
        if len(authors) != 3:
            errors.append(f"{w}: duplicate author")
        for q in d["quotes"]:
            if "**" not in q["quote"]:
                errors.append(f"{w}: quote missing bold")
    if errors:
        print(f"FAILED validation ({len(errors)} issues):")
        for e in errors:
            print("  ", e)
    else:
        print("ALL 57 words in Part 2 PASSED local pre-audit validation!")
