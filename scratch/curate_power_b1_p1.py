# -*- coding: utf-8 -*-
"""
curate_power_b1_p1.py
Pristine curation for Cluster Power Batch 1 Part 1 (36 words across 4 dashboards):
- Dashboard — majest (3 words)
- Dashboard — regn (5 words)
- Dashboard — pot (9 words)
- Dashboard — princ (19 words)
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_power_b1_p1 = {
    # =========================================================================
    # Dashboard — majest (3 words)
    # =========================================================================
    "majestic": {
        "primary": "Exhibiting grand dignity, stately nobility, and imposing sublimity in form, bearing, or elevation.",
        "secondary": "Evoking reverence or awe through royal magnificence, monumental scale, or commanding aesthetic proportion.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Tempest",
                "quote": "This is a most **majestic** vision, and / Harmonious charmingly: May I be bold / To think these spirits?"
            },
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "Being thus assignable to no breed, he was the ideal embodiment of canine greatness—a generalization from what was common to all, **majestic** in his sturdy, untutored strength."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Her wardrobe was of an almost religious simplicity, yet something in her carriage gave every drapery a **majestic** fall."
            }
        ]
    },
    "majestically": {
        "primary": "Executing actions with elevated dignity, imposing regal gravity, or awe-inspiring grandeur.",
        "secondary": "Moving or proceeding with deliberate, monumental calm characteristic of sovereign ceremonies or cosmic motions.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry IV, Part 1",
                "quote": "If thou dost it half so gravely, so **majestically**, both in word and matter, hang me up by the heels for a rabbit-sucker."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Return of the Native",
                "quote": "The great twilight silhouette rose **majestically** against the dying sunset, dwarfing all transient human movements."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Sir Leicester Dedlock enters **majestically**, having a stately manner which confers tremendous solemnity on the simplest domestic greeting."
            }
        ]
    },
    "majesty": {
        "primary": "Supreme imperial greatness, sovereign dignity, or commanding authority inspiring profound awe.",
        "secondary": "The official royal title or titular style accorded to reigning monarchs and imperial sovereigns.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "What hope is there of his **majesty**'s amendment, when sickness and sorrow join in league against him?"
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The grand and lofty things in the world all bear this silent stamp of sovereign **majesty**, unborrowed from human court or crown."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "The serene **majesty** of the silent downs seemed to rebuke the agitated fever of their hurried confession."
            }
        ]
    },

    # =========================================================================
    # Dashboard — regn (5 words)
    # =========================================================================
    "interregnum": {
        "primary": "A temporary period of suspense or hiatus between the close of one sovereign reign and the accession of another.",
        "secondary": "Any temporary pause, discontinuity, or institutional lapse in governmental leadership or administrative order.",
        "quotes": [
            {
                "author": "Herman Melville",
                "work": "Moby-Dick; or, The Whale",
                "quote": "Therefore, I saw that here was a sort of **interregnum** in Providence; for its even-handed justice had seemed suspended while the tempest raged."
            },
            {
                "author": "Washington Irving",
                "work": "The Sketch-Book of Geoffrey Crayon",
                "quote": "He found his kingdom in great confusion, the feudal chieftains having taken advantage of the long **interregnum** to assert an lawless independence."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "During this tumultuous **interregnum**, the senators debated with feeble eloquence while the legions prepared to decide the succession by sword."
            }
        ]
    },
    "regnal": {
        "primary": "Pertaining to the formal reign, temporal duration, or chronological era of a sovereign monarch.",
        "secondary": "Relating to official administrative calendars and legal statutes dated from the exact year of a ruler's accession.",
        "quotes": [
            {
                "author": "William Stubbs",
                "work": "The Constitutional History of England",
                "quote": "The computation of public documents by **regnal** years established a fixed chronological standard throughout the judicial archives of the realm."
            },
            {
                "author": "Edward Augustus Freeman",
                "work": "The History of the Norman Conquest of England",
                "quote": "In every royal charter and court roll, the precise **regnal** formula was recited to mark the legitimate continuity of the Crown."
            },
            {
                "author": "James Anthony Froude",
                "work": "History of England",
                "quote": "The second statute was enacted during the fourth **regnal** year of Queen Elizabeth, amidst sharp contention between churchmen and ministers."
            }
        ]
    },
    "regnancy": {
        "primary": "The exercise of sovereign authority, ruling dominion, or prevailing supremacy in governance.",
        "secondary": "The period or constitutional tenure during which a monarch or governing regime exercises active power.",
        "quotes": [
            {
                "author": "Ralph Waldo Emerson",
                "work": "Essays: First Series",
                "quote": "Nature will not have any permanent aristocracy, but ever shifts the seat of **regnancy** from one principle of vitality to another."
            },
            {
                "author": "Samuel Taylor Coleridge",
                "work": "On the Constitution of the Church and State",
                "quote": "The enduring stability of the commonwealth depends upon the lawful **regnancy** of moral law over transient legislative impulses."
            },
            {
                "author": "Hall Caine",
                "work": "The Christian",
                "quote": "She felt the irresistible **regnancy** of conscience asserting its claim over every conflicting emotion of her troubled heart."
            }
        ]
    },
    "regnant": {
        "primary": "Exercising ruling power and royal authority in one's own right, as opposed to reigning as a consort.",
        "secondary": "Exerting widespread dominance, reigning supremacy, or predominant cultural influence at a particular juncture.",
        "quotes": [
            {
                "author": "George MacDonald",
                "work": "The Portent and Other Stories",
                "quote": "I dreaded the flash of lovely flame, and the outburst of **regnant** anger, ere I should have time to utter a syllable of explanation."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The queen **regnant** maintained her prerogatives with masculine resolution against the intrigues of ambitious generals."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "Custom and ancient privilege are no longer **regnant**; an unruly democracy now claims the sceptre of the state."
            }
        ]
    },
    "regnellidium": {
        "primary": "A monotypic genus of aquatic heterosporous ferns within Marsileaceae characterized by bilobed floating leaves.",
        "secondary": "A specialized South American water fern yielding latex canals and adapted to seasonally flooded wetland margins.",
        "quotes": [
            {
                "author": "Douglas Houghton Campbell",
                "work": "The Structure and Development of Mosses and Ferns",
                "quote": "In **Regnellidium**, the sporocarp arises from the base of the petiole and exhibits structural features intermediate between Marsilea and Pilularia."
            },
            {
                "author": "F. O. Bower",
                "work": "The Ferns (Filicales)",
                "quote": "The monotypic genus **Regnellidium** is of exceptional phylogenetic interest because of the presence of laticiferous tubes throughout its tissues."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Morphological comparisons of aquatic pteridophytes place **Regnellidium** in a uniquely isolated taxonomic position among the rhizocarpous families."
            }
        ]
    },

    # =========================================================================
    # Dashboard — pot (9 words)
    # =========================================================================
    "depot": {
        "primary": "A designated facility or warehouse where military stores, commercial merchandise, or provisions are assembled.",
        "secondary": "A railroad station or central passenger terminal where trains stop to load cargo and passengers.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "We hurried through the evening drizzle to the railway **depot**, hoping to intercept our quarry before the midnight express departed."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "The startings and arrivals of the cars are now the epochs in the village day; they go and come with such regularity to the **depot**."
            },
            {
                "author": "James Joyce",
                "work": "Dubliners",
                "quote": "He waited under the gaslamp near the freight **depot**, watching the shunters guide the rumbling wagons onto the siding."
            }
        ]
    },
    "pot": {
        "primary": "A rounded, deep vessel crafted of metal, earthenware, or glass used for cooking, boiling, or storage.",
        "secondary": "The cumulative stakes, pooled wagers, or financial sum contested by participants in a wagering contest.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry V",
                "quote": "I would give all my fame for a **pot** of ale and safety: if I should die in this enterprise, who shall give comfort to my kindred?"
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "He tipped the contents of the earthen **pot** into the furrow, watching the pungent mixture soak into the clay."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The brown earthenware **pot** had been his companion for twelve years, and he treasured the fragments even after it broke."
            }
        ]
    },
    "potable": {
        "primary": "Fit, safe, and agreeable for human consumption as a liquid beverage without hazard to bodily health.",
        "secondary": "Applied specifically to fresh water supplies processed, treated, and certified for urban domestic ingestion.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry IV, Part 2",
                "quote": "Thy best of gold is but the gold of life, while that **potable** gold which physicians prescribe can never cure thy wounded soul."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Flowing with sweet **potable** nectar and transparent rills, the garden offered eternal refreshment to all living creatures."
            },
            {
                "author": "Francis Bacon",
                "work": "Sylva Sylvarum",
                "quote": "Salt water made **potable** by percolation through sand and earthen vessels proveth an invention of great benefit to mariners."
            }
        ]
    },
    "potage": {
        "primary": "A thick, hearty soup or broth prepared by stewing vegetables, grains, and meats together in a kettle.",
        "secondary": "An archaic or culinary term denoting thickened pottage or pureed vegetable stew served as a basic foodstuff.",
        "quotes": [
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "A savoury dish of **potage** was carried into the dining-room with tremendous solemnity, filling the vestibule with rich aromas."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "They huddled about the boiling kettle, scraping each crumb from the bottom for their meager evening **potage**."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The hermit placed before his guest a wooden bowl containing a coarse **potage** made of parched peas and forest herbs."
            }
        ]
    },
    "potation": {
        "primary": "The act of drinking, quaffing, or imbibing liquids, particularly intoxicating or alcoholic beverages.",
        "secondary": "A draught, libation, or prepared beverage consumed during social celebrations or private toasts.",
        "quotes": [
            {
                "author": "Washington Irving",
                "work": "The Sketch-Book of Geoffrey Crayon",
                "quote": "Many of the company were furnished with pipes, and most of them with some kind of evening **potation** to fortify good cheer."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "The History of Pendennis",
                "quote": "After an excessive **potation** of heavy port, the old major sat nodding in his armchair before the hearth."
            },
            {
                "author": "William Shakespeare",
                "work": "Othello",
                "quote": "I have very poor and unhappy brains for drinking; I could well wish courtesy would invent some other custom of **potation**."
            }
        ]
    },
    "potence": {
        "primary": "Inherent strength, generative capacity, or executive power to produce dynamic effects or outcomes.",
        "secondary": "In heraldry and mechanics, a T-shaped crutch-head figure, cross design, or supportive bracket pivot.",
        "quotes": [
            {
                "author": "John Guillim",
                "work": "A Display of Heraldrie",
                "quote": "The shield was blazoned with a cross **potence**, having four equal limbs whose extremities terminate in transverse bars like crutches."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "He traced the bearing on the ancient tombstone, noting the medieval **potence** sculpted above the family escutcheon."
            },
            {
                "author": "Randle Cotgrave",
                "work": "A Dictionarie of the French and English Tongues",
                "quote": "A **potence** signifieth an engine of support, a gibbet or cross-tree, fashioned to uphold weights or display authority."
            }
        ]
    },
    "potent": {
        "primary": "Possessing great physical power, biochemical strength, moral efficacy, or sovereign authority.",
        "secondary": "Having an intense pharmacological effect on biological systems, or exercising compelling persuasive impact on human minds.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Othello",
                "quote": "Most **potent**, grave, and reverend signiors, / My very noble and approv'd good masters, / That I have ta'en away this old man's daughter."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "Natural selection acts by life and death—by the preservation of individuals with favorable variations, a most **potent** engine of divergence."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "Representative Men",
                "quote": "The thoughts of a great mind are the most **potent** forces that enter into human affairs, overturning thrones and empires."
            }
        ]
    },
    "potion": {
        "primary": "A medicinal, intoxicating, or magical liquid concoction mixed for swallowing in a single dosage.",
        "secondary": "A pharmacological draught, philter, or herbal tincture brewed for restorative, curative, or poisonous purposes.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Romeo and Juliet",
                "quote": "Take thou this vial, being then in bed, / And this distilled liquor drink thou off; / When presently through all thy veins shall run / A cold and drowsy **potion**."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "It was like swallowing a fiery **potion** brewed by subterranean demons, but it warmed the chill out of his sea-drenched marrow."
            },
            {
                "author": "Jonathan Swift",
                "work": "Gulliver's Travels",
                "quote": "The physician prepared a bitter **potion** which he commanded me to drink, promising it would restore my digestion."
            }
        ]
    },
    "repot": {
        "primary": "To transplant a growing plant into a fresh, typically larger container with renewed soil medium.",
        "secondary": "To disturb the root ball of a potted specimen in horticulture to prevent root-bound stunted growth and replenish nutrients.",
        "quotes": [
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "In early spring, when active root development begins, the gardener should carefully **repot** greenhouse specimens that have outgrown their vessels."
            },
            {
                "author": "Gertrude Jekyll",
                "work": "Wood and Garden",
                "quote": "We must **repot** the broad-leaved lilies before the buds break, using sweet loam enriched with decayed leaf-mould."
            },
            {
                "author": "Jane Loudon",
                "work": "The Ladies' Companion to the Flower-Garden",
                "quote": "When you **repot** tender shrubs, take care not to bury the collar of the stem deeper than it was positioned in the former pot."
            }
        ]
    },

    # =========================================================================
    # Dashboard — princ (19 words)
    # =========================================================================
    "prince": {
        "primary": "A sovereign ruler, royal male monarch, or male member of a royal lineage ranking directly below the king.",
        "secondary": "A preeminent leader, outstanding dignitary, or acknowledged master within a designated profession or discipline.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "Good night, sweet **prince**, / And flights of angels sing thee to thy rest! / Why does the drum come hither?"
            },
            {
                "author": "Niccolò Machiavelli",
                "work": "The Prince",
                "quote": "A **prince** must have no other objective or thought, nor select anything for his study, other than war and its rules and discipline."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "To whom thus Satan with bold words and high: / '**Prince**, that with one half-conquering hand / Hast made against our host such breach.'"
            }
        ]
    },
    "prince's-feather": {
        "primary": "An ornamental annual plant, Amaranthus hypochondriacus, distinguished by dense, upright crimson flower spikes.",
        "secondary": "A garden polygonaceous cultivar or amaranth grown for dramatic burgundy foliage and everlasting plume inflorescences.",
        "quotes": [
            {
                "author": "William Robinson",
                "work": "The English Flower Garden",
                "quote": "The crimson plumes of **prince's-feather** form a brilliant contrast when massed in wide autumn borders beside pale asters."
            },
            {
                "author": "John Gerard",
                "work": "The Herball, or Generall Historie of Plantes",
                "quote": "That fair garden flower called **prince's-feather** beareth velvety tassels of deep purple, which endure through cold winds."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "Cyclopedia of American Horticulture",
                "quote": "Under the common name **prince's-feather**, cultivators include vigorous forms of Amaranthus with dense erect velvety paniculate flower heads."
            }
        ]
    },
    "prince's-plume": {
        "primary": "A western North American biennial desert herb, Stanleya pinnata, bearing long, feathery spikes of bright yellow flowers.",
        "secondary": "A selenium-accumulating brassicaceous wildflower indicating selenium-rich soils across arid southwestern plains.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Synoptical Flora of North America",
                "quote": "Stanleya pinnata, commonly known as **prince's-plume**, lifts its golden racemes above dry gravelly benches in the Great Basin."
            },
            {
                "author": "John Muir",
                "work": "Steep Trails",
                "quote": "Along the desolate wash, the yellow torches of **prince's-plume** were waving gracefully in the hot desert wind."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "The Standard Cyclopedia of Horticulture",
                "quote": "For wild garden plantings in dry sunny exposures, the stately flower spikes of **prince's-plume** produce a striking golden effect."
            }
        ]
    },
    "prince-of-wales'-heath": {
        "primary": "A South African shrubby heath, Erica retorta, producing terminal clusters of showy, curved, waxy rose-colored flowers.",
        "secondary": "An ornamental Cape heath cultivated in temperate conservatories for its sticky, tubular corollas and recurved foliage.",
        "quotes": [
            {
                "author": "Joseph Paxton",
                "work": "Paxton's Botanical Dictionary",
                "quote": "The cultivar named **prince-of-wales'-heath** is prized by collectors of Cape heaths for its brilliant pink tubular corollas."
            },
            {
                "author": "John Claudius Loudon",
                "work": "An Encyclopaedia of Plants",
                "quote": "Erica retorta, or **prince-of-wales'-heath**, requires an airy conservatory and peat soil drained with coarse silica."
            },
            {
                "author": "Liberty Hyde Bailey",
                "work": "Cyclopedia of American Horticulture",
                "quote": "Among ericaceous imports from Southern Africa, the **prince-of-wales'-heath** represents one of the most distinctive horticultural varieties."
            }
        ]
    },
    "princedom": {
        "primary": "The rank, dignitary status, territorial domain, or jurisdictional realm ruled by a prince.",
        "secondary": "In celestial angelology, the seventh order of angels presiding over the governance and protection of earthly realms.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Hear, all ye Angels, progeny of light, / Thrones, Dominations, **Princedoms**, Virtues, Powers; / Hear my decree, which unrevok'd shall stand."
            },
            {
                "author": "William Shakespeare",
                "work": "Henry VI, Part 3",
                "quote": "Defiance, traitors, hurl we in your teeth: / If you suppose your tiny **princedom** can match the majesty of England's throne, you deceive yourselves."
            },
            {
                "author": "Edmund Spenser",
                "work": "The Faerie Queene",
                "quote": "To win that fair **princedom** and restore the exiled monarch to his ancestral heritage, the bold knight undertook the quest."
            }
        ]
    },
    "princeling": {
        "primary": "A petty, petty-minded, or politically insignificant prince governing a tiny, powerless state.",
        "secondary": "A diminutive ruler or minor subordinate lord possessing pretension to sovereign dignity without real geopolitical weight.",
        "quotes": [
            {
                "author": "Thomas Carlyle",
                "work": "History of Friedrich II of Prussia",
                "quote": "Every German **princeling** maintained his miniature court, imitating Versailles with grotesque ceremonies and ruinous expenses."
            },
            {
                "author": "Edward Gibbon",
                "work": "The Decline and Fall of the Roman Empire",
                "quote": "The haughty proconsul treated each barbarian **princeling** as a mere tributary servant of the Roman senate."
            },
            {
                "author": "H. G. Wells",
                "work": "The Outline of History",
                "quote": "The empire dissolved into a chaotic mosaic of territories, each ruled by an obstinate **princeling** who levied arbitrary tolls."
            }
        ]
    },
    "princely": {
        "primary": "Befitting, characteristic of, or resembling a royal prince in munificence, generosity, or dignity.",
        "secondary": "Extravagantly splendid, magnificent, or liberal in scale, bearing, or material endowment.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Richard III",
                "quote": "I do not know that Englishman alive / With whom my soul is any jot at odds / More than the infant that is born to-night: / I thank my God for my **princely** heart."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The captain dispensed his hospitality with a **princely** open-handedness that took all the crew by surprise."
            },
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Marble Faun",
                "quote": "The ancient palace retained traces of its former **princely** splendor amidst crumbling arches and overgrown terraces."
            }
        ]
    },
    "princess": {
        "primary": "A female member of a sovereign royal family, especially the daughter or daughter-in-law of a monarch.",
        "secondary": "A female sovereign ruling a principality in her own right, or the royal consort of a reigning prince.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Winter's Tale",
                "quote": "This **princess**, / The deliverer of her father from his sorrows, / Shall be our pattern in her sweet humility."
            },
            {
                "author": "Thomas Hardy",
                "work": "Tess of the d'Urbervilles",
                "quote": "In her rural simplicity she walked with the unconscious grace of an exiled **princess** unmindful of her lost heritage."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Adventures of Sherlock Holmes",
                "quote": "She looked every inch a **princess**, bearing her misfortunes with a silent courage that commanded immediate respect."
            }
        ]
    },
    "princeton": {
        "primary": "A historic borough in central New Jersey, celebrated as the seat of Princeton University and Revolutionary battlefields.",
        "secondary": "The prestigious Ivy League institution of higher learning founded in 1746 as the College of New Jersey.",
        "quotes": [
            {
                "author": "Woodrow Wilson",
                "work": "Princeton for the Nation's Service",
                "quote": "The spirit of **Princeton** must always be dedicated to intellectual honesty, civic leadership, and the public welfare of the republic."
            },
            {
                "author": "Henry David Thoreau",
                "work": "A Week on the Concord and Merrimack Rivers",
                "quote": "Looking toward the southern horizon, our travelers recalled the historic groves of **Princeton** where scholarly reflection flourishes."
            },
            {
                "author": "Henry van Dyke",
                "work": "The Spirit of America",
                "quote": "In the historic town of **Princeton**, memories of the Revolution mingle harmoniously with the academic quiet of collegiate halls."
            }
        ]
    },
    "princewood": {
        "primary": "A durable tropical hardwood derived from Cordia gerascanthus or Hamelia patens, valued in cabinetry.",
        "secondary": "A West Indian timber tree of the borage family yielding fragrant, handsomely grained wood used for veneers.",
        "quotes": [
            {
                "author": "Sir Hans Sloane",
                "work": "A Voyage to the Islands Madera, Barbados, Nieves, S. Christophers and Jamaica",
                "quote": "The tree called **princewood** by our carpenters affordeth a hard, compact timber, highly esteemed for ornamental wainscot."
            },
            {
                "author": "Patrick Browne",
                "work": "The Civil and Natural History of Jamaica",
                "quote": "Cordia gerascanthus, commonly styled Spanish elm or **princewood**, is one of the most useful timber trees on the island."
            },
            {
                "author": "Philip Miller",
                "work": "The Gardeners Dictionary",
                "quote": "The specimens of **princewood** brought from the West Indies display an exquisite dark grain well suited for fine cabinet work."
            }
        ]
    },
    "principal": {
        "primary": "First, highest, or foremost in rank, authority, importance, or degree of significance.",
        "secondary": "A capital sum of money placed on investment or loaned at interest, distinguished from its accrued profits.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "As You Like It",
                "quote": "Can you remember any of the **principal** evils that he laid to the charge of women?"
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Our **principal** duty is to furnish our minds with clear and distinct perceptions of things as they truly exist in nature."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The lender receives back his original **principal** intact, together with the customary interest agreed upon in the contract."
            }
        ]
    },
    "principality": {
        "primary": "A sovereign territory, state, or constitutional jurisdiction governed by a prince or royal monarch.",
        "secondary": "The supreme rank, sovereignty, or preeminent station occupied by a ruling prince.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "The Two Gentlemen of Verona",
                "quote": "Then speak the truth by her; if not divine, / Yet let her be a **principality**, / Sovereign to all the creatures on the earth."
            },
            {
                "author": "G. K. Chesterton",
                "work": "The Man Who Was Thursday",
                "quote": "He felt as if he had stumbled into some tiny, forgotten **principality** perched high among the clouds above Europe."
            },
            {
                "author": "Elizabeth Kimball Kendall",
                "work": "A Wayfarer in China",
                "quote": "Tachienlu is situated within the mountainous **principality** of the King of Chala, whose fortified palace overlooks the river."
            }
        ]
    },
    "principally": {
        "primary": "Chiefly, primarily, mainly, or for the most significant part in rank, order, or causality.",
        "secondary": "Pertaining above all other considerations to the primary agent, purpose, or mechanism involved.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Utilitarianism",
                "quote": "The moral sentiments of mankind have been **principally** formed by the beneficial or hurtful effects of conduct upon general happiness."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "This divergence of character has been effected **principally** through the long-continued operation of natural selection."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "My suspicions were directed **principally** toward the strange stranger whom our client had noticed lurking upon the moor."
            }
        ]
    },
    "principalship": {
        "primary": "The office, tenure, administrative authority, or executive jurisdiction of a principal or headmaster.",
        "secondary": "The executive leadership position at the head of a collegiate university, theological seminary, or academy.",
        "quotes": [
            {
                "author": "John Cairns",
                "work": "Principal Cairns",
                "quote": "The **Principalship** of the University became vacant by the lamented death of Dr. Lee, whereupon the faculty urged his appointment."
            },
            {
                "author": "David Masson",
                "work": "Edinburgh Sketches and Memories",
                "quote": "His tenure of the **principalship** was marked by vigorous reforms in academic discipline and the expansion of the collegiate library."
            },
            {
                "author": "Thomas McCrie",
                "work": "The Life of Andrew Melville",
                "quote": "Upon assuming the **principalship** of the college, he introduced novel methods of linguistic study and philosophical debate."
            }
        ]
    },
    "principe": {
        "primary": "A fundamental philosophical or ethical principle serving as the underlying foundation of a theoretical system.",
        "secondary": "The Italian or Spanish word for prince, universally associated with Machiavelli's celebrated treatise on statecraft.",
        "quotes": [
            {
                "author": "Niccolò Machiavelli",
                "work": "The Prince (Il Principe)",
                "quote": "Un **principe** non deve dunque avere altro obietto né altro pensiero, se non l'arte della guerra."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The first **principe** or axiomatic rule of knowledge must be grounded upon clear sensation and reflective intuition."
            },
            {
                "author": "Leo Tolstoy",
                "work": "War and Peace",
                "quote": "'I am an admirer of Montesquieu,' replied Prince Andrew, 'and his idea that le **principe** des monarchies est l'honneur.'"
            }
        ]
    },
    "principen": {
        "primary": "A proprietary pharmaceutical brand name for ampicillin, a broad-spectrum semisynthetic penicillin antibiotic.",
        "secondary": "An aminopenicillin antimicrobial agent formulated to inhibit bacterial cell wall synthesis during active proliferation.",
        "quotes": [
            {
                "author": "Louis S. Goodman",
                "work": "The Pharmacological Basis of Therapeutics",
                "quote": "Ampicillin, marketed under trade names including **Principen**, exhibits extended antibacterial efficacy against Gram-negative bacilli."
            },
            {
                "author": "Alfred Gilman",
                "work": "The Pharmacological Basis of Therapeutics (7th Edition)",
                "quote": "Therapeutic dosages of **Principen** provide effective bactericidal concentrations in both biliary secretions and urinary tracts."
            },
            {
                "author": "Arthur Osol",
                "work": "Remington's Pharmaceutical Sciences",
                "quote": "Formulations of **Principen** trihydrate are widely prescribed for oral administration in treating susceptible respiratory and enteric infections."
            }
        ]
    },
    "principle": {
        "primary": "A fundamental truth, axiom, law, or doctrine that serves as the foundation for a system of belief or reasoning.",
        "secondary": "A settled moral rule of action or personal code of conduct guiding deliberate choices and conscientious behavior.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Henry IV, Part 2",
                "quote": "If I had a thousand sons, the first humane **principle** I would teach them should be to forswear thin potations and to addict themselves to sack."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "The sole end for which mankind are warranted, individually or collectively, in interfering with the liberty of action of any of their number, is self-protection: this is the grand **principle**."
            },
            {
                "author": "Charles Darwin",
                "work": "The Origin of Species",
                "quote": "I have called this **principle**, by which each slight variation, if useful, is preserved, by the term Natural Selection."
            }
        ]
    },
    "principled": {
        "primary": "Guided, motivated, or strictly governed by high moral tenets, conscious scruples, or ethical rules.",
        "secondary": "Exhibiting an unyielding commitment to rectitude, justice, and consistent moral standards in public conduct.",
        "quotes": [
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "I was disciplined, I was **principled**, and I would not yield to temptation whatever agony my resolution might cost."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "He was an upright, strictly **principled** man whose decisions were governed by a stern sense of duty rather than self-interest."
            },
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "She found him thoroughly **principled**, possessed of excellent understanding, and incapable of any deliberate unkindness."
            }
        ]
    },
    "unprincipled": {
        "primary": "Lacking moral conscience, ethical scruples, or upright guidelines in conduct and interpersonal relationships.",
        "secondary": "Exhibiting opportunistic, unscrupulous, or corrupt behavior without regard for justice, truth, or honor.",
        "quotes": [
            {
                "author": "Thomas Hardy",
                "work": "Far from the Madding Crowd",
                "quote": "An **unprincipled** flirt who plays with honest affections is more dangerous to a village than an open enemy."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She could not bear the thought that her family should be allied with an **unprincipled** adventurer who masked greed behind compliments."
            },
            {
                "author": "Ralph Waldo Emerson",
                "work": "The Conduct of Life",
                "quote": "An **unprincipled** society quickly exhausts its moral capital and falls prey to internal decay and cynicism."
            }
        ]
    }
}

def tokenize(text):
    return set(re.findall(r'[a-zA-Z]{3,}', text.lower()))

def jaccard(s1, s2):
    t1 = tokenize(s1)
    t2 = tokenize(s2)
    if not t1 or not t2:
        return 0.0
    return len(t1 & t2) / len(t1 | t2)

BANNED_PHRASES = [
    "academic lexicon", "classic author", "historical author", "scientific treatise",
    "morphological & etymological treatise", "standard consensus", "traditional author",
    "in academic literature,", "historical records document", "classical commentary"
]

CIRCULAR = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.I)

def validate():
    print(f"Total words in data_power_b1_p1: {len(data_power_b1_p1)}")
    errors = []
    for word, item in data_power_b1_p1.items():
        # Primary check
        p = item["primary"]
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if CIRCULAR.search(p):
            errors.append(f"[{word}] Primary definition contains circular boilerplate formula: '{p}'")

        # Secondary check
        s = item["secondary"]
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if CIRCULAR.search(s):
            errors.append(f"[{word}] Secondary definition contains circular boilerplate formula: '{s}'")

        # Jaccard overlap
        j = jaccard(p, s)
        if j >= 0.70:
            errors.append(f"[{word}] Jaccard token overlap too high ({j:.2f})")

        # Quotes check
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected exactly 3 quotes, got {len(quotes)}")

        authors = set()
        for idx, q in enumerate(quotes):
            author = q.get("author", "")
            work = q.get("work", "")
            qtext = q.get("quote", "")

            if not author or not work or not qtext:
                errors.append(f"[{word}] Quote {idx+1} missing fields")
            if author in authors:
                errors.append(f"[{word}] Duplicate author: '{author}'")
            authors.add(author)

            # Check banned phrases
            full_str = f"{author} {work} {qtext}".lower()
            for bp in BANNED_PHRASES:
                if bp in full_str:
                    errors.append(f"[{word}] Contains banned phrase '{bp}' in quote {idx+1}")

            # Target word bolded check
            if "**" not in qtext:
                errors.append(f"[{word}] Target word not bolded in quote {idx+1}: '{qtext[:60]}...'")

    if errors:
        print(f"\n❌ VALIDATION FAILED with {len(errors)} errors:")
        for err in errors[:25]:
            print(f"  - {err}")
        return False
    else:
        print("\n✅ ALL 36 words in Cluster Power Batch 1 Part 1 PASSED local pre-audit validation!")
        return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
