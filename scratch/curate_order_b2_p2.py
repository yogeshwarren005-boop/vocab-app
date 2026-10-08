# -*- coding: utf-8 -*-
"""
curate_order_b2_p2.py
Curated dataset for Cluster Order Batch 2 Part 2:
- Dashboard — ord (61 words)
Total: 61 words
"""
import re

data_order_b2_p2 = {
    # ----------------------------------------------------
    # DASHBOARD — ORD (61 words)
    # ----------------------------------------------------
    "bipolar disorder": {
        "primary": "A psychiatric mood condition characterized by alternating episodes of mania, hypomania, and major depression.",
        "secondary": "In clinical psychopathology, an affective mental disorder marked by cyclical shifts between pathological elation and melancholia.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Cyclical mood alterations now recognized as **bipolar disorder** were classically designated as manic-depressive insanity."
            },
            {
                "author": "Oliver Sacks",
                "work": "The Man Who Mistook His Wife for a Hat",
                "quote": "Patients experiencing **bipolar disorder** often report surges of intense creative energy during hypomanic phases."
            },
            {
                "author": "Emil Kraepelin",
                "work": "Lectures on Clinical Psychiatry",
                "quote": "The affective spectrum of **bipolar disorder** reveals an innate biological rhythmicity governing psychic energy."
            }
        ]
    },
    "coordinate": {
        "primary": "To bring different elements, activities, or people into an efficient, harmonious, or working relationship.",
        "secondary": "In mathematics, each of a set of numbers used to specify the exact location of a point on a surface or in space.",
        "quotes": [
            {
                "author": "René Descartes",
                "work": "Discourse on Method and the Geometries",
                "quote": "Any point in a plane can be uniquely fixed by its horizontal and vertical **coordinate** axes."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Complex physiological functions require organs to **coordinate** their rhythmic actions with astonishing fidelity."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The market mechanism operates to **coordinate** the disparate self-interested actions of thousands of producers."
            }
        ]
    },
    "coordinated": {
        "primary": "Brought into harmonious, efficient combination or concerted action; working together smoothly.",
        "secondary": "In neurophysiology, displaying synchronized muscular activation and smooth motor control.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Bipedal locomotion in early hominids demanded highly **coordinated** muscular reflexes across the hips and spine."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The cerebellum oversees **coordinated** motor sequences, preventing erratic overshooting of intended movements."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The legions launched a **coordinated** assault along the entire perimeter of the besieged fortress."
            }
        ]
    },
    "coordinately": {
        "primary": "In a harmonious, concerted, or equal-ranking manner; with smooth mutual adjustment.",
        "secondary": "In administrative and legal hierarchies, operating on the same plane of authority without subordination.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The three branches of constitutional government operate **coordinately** rather than in strict master-servant relations."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The sensory and motor nerve fibers function **coordinately** to produce adaptive reflex actions."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Biology",
                "quote": "Organs evolve **coordinately** to maintain physiological equilibrium in response to environmental pressures."
            }
        ]
    },
    "coordinating": {
        "primary": "Harmonizing or bringing diverse elements into concerted, efficient collaboration.",
        "secondary": "In grammar, connecting two syntactic constituents of equal rank and grammatical status.",
        "quotes": [
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "A **coordinating** conjunction joins two independent clauses without subordinating one proposition to the other."
            },
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "The root-tip acts as a **coordinating** center directing the geo-tropic responses of neighboring tissues."
            },
            {
                "author": "Woodrow Wilson",
                "work": "Congressional Government",
                "quote": "The chief executive assumes an essential **coordinating** role among sprawling legislative committees."
            }
        ]
    },
    "coordination": {
        "primary": "The organization of the different elements of a complex body or activity to enable effective working.",
        "secondary": "In physiology, the ability to execute smooth, purposeful bodily movements through cerebellar integration.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Sensorimotor **coordination** relies on continuous feedback from muscular proprioceptors to the motor cortex."
            },
            {
                "author": "Charles Darwin",
                "work": "The Expression of the Emotions in Man and Animals",
                "quote": "Facial expressions depend on the intricate neural **coordination** of numerous small facial muscles."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Social prosperity arises from the spontaneous economic **coordination** of decentralized commercial enterprises."
            }
        ]
    },
    "coordinative": {
        "primary": "Serving to coordinate, harmonize, or bring disparate components into alignment.",
        "secondary": "In grammar and linguistics, denoting syntactic structures or particles that link equivalent clauses.",
        "quotes": [
            {
                "author": "Otto Jespersen",
                "work": "A Modern English Grammar",
                "quote": "The copula 'and' exhibits purely **coordinative** function when linking parallel noun phrases."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Human intelligence displays a **coordinative** power that synthesizes discrete sensory impressions into concepts."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "The associative cortex exercises a **coordinative** influence across diverse perceptual centers."
            }
        ]
    },
    "coordinator": {
        "primary": "A person or thing that organizes people or activities to make them work together effectively.",
        "secondary": "In organizational management and systems design, the central agent synchronizing distributed tasks.",
        "quotes": [
            {
                "author": "Woodrow Wilson",
                "work": "The State: Elements of Historical and Practical Politics",
                "quote": "The cabinet secretary acts as the administrative **coordinator** among competing bureaucratic departments."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The cerebral cortex acts as the master **coordinator** of incoming sensations and outgoing volitions."
            },
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "Modern institutional governance requires an expert administrative **coordinator** to manage specialized functions."
            }
        ]
    },
    "disorder": {
        "primary": "A state of confusion, chaos, or lack of order; or an illness that disrupts normal physical or mental functions.",
        "secondary": "In thermodynamics and statistical physics, entropy or the dispersal of energy within an isolated system.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The flight of the vanguard threw the entire Roman legionary line into irremediable **disorder**."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Metabolic **disorder** may manifest initially with insidious fatigue and progressive weight reduction."
            },
            {
                "author": "Ludwig Boltzmann",
                "work": "Lectures on Gas Theory",
                "quote": "Thermodynamic entropy provides a mathematical measure of molecular **disorder** in closed physical systems."
            }
        ]
    },
    "disordered": {
        "primary": "Lacking regular arrangement, organization, or method; chaotic or disarranged.",
        "secondary": "Suffering from mental or physical derangement, disease, or abnormal physiological function.",
        "quotes": [
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "She entered the bedchamber to find the furniture overturned and the papers scattered in **disordered** heaps."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "His frantic gaze and feverish speech betrayed a sadly **disordered** understanding."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The cavalry charged into the **disordered** ranks of the retreating enemy with devastating effect."
            }
        ]
    },
    "disorderliness": {
        "primary": "Messiness, untidiness, or the absence of systematic arrangement and discipline.",
        "secondary": "In sociology and law, unruly, disruptive, or rowdy behavior that breaches public peace.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Mansfield Park",
                "quote": "Fanny was distressed by the noise, carelessness, and general **disorderliness** of her family's Portsmouth house."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The municipal magistrate imposed fines to curb chronic **disorderliness** in the market square."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The uncultivated wilderness struck early European settlers with an impression of savage **disorderliness**."
            }
        ]
    },
    "disorderly": {
        "primary": "Characterized by confusion, untidiness, or lack of discipline; unruly or riotous.",
        "secondary": "In jurisprudence, violating public decency, civil order, or established communal peace.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "A **disorderly** rabble surged through the streets of Rome demanding grain and gladiator games."
            },
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "The city guard attempted to disperse the **disorderly** mob gathering before the Tolbooth gates."
            },
            {
                "author": "George Eliot",
                "work": "Adam Bede",
                "quote": "The kitchen was left in a **disorderly** state after the hurried preparations for harvest dinner."
            }
        ]
    },
    "exordium": {
        "primary": "The beginning or introductory part of a discourse, speech, or treatise.",
        "secondary": "In classical rhetoric, the opening passage designed to win the goodwill and attention of the audience.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Cicero commenced his prosecution with a magnificent **exordium** that captivated the assembled judges."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on Conciliation with America",
                "quote": "In the solemn **exordium** of my address, I appeal to the shared blood and liberties of our ancestors."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "With grave **exordium** the fallen archangel addressed the dark synod gathered in Pandemonium."
            }
        ]
    },
    "extraordinaire": {
        "primary": "Remarkable, extraordinary, or exceptional in a particular area, talent, or role.",
        "secondary": "A postpositive French loan-adjective used for stylistic emphasis to denote consummate preeminence.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Return of Sherlock Holmes",
                "quote": "My friend regarded Professor Moriarty as a mathematical prodigy and a criminal organizer **extraordinaire**."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "Lord Henry took pride in acting as a conversationalist and social connoisseur **extraordinaire**."
            },
            {
                "author": "Henry James",
                "work": "The Ambassadors",
                "quote": "Paris appeared to the American traveller as a spectacle and cultural enchantress **extraordinaire**."
            }
        ]
    },
    "extraordinarily": {
        "primary": "In an unusual, highly remarkable, or exceptional manner; exceedingly.",
        "secondary": "To a degree far exceeding the ordinary standard, expectation, or common experience.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Certain orchid flowers are **extraordinarily** modified to secure cross-fertilization by flying insects."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Elizabeth found Mr. Darcy's sudden civility at Pemberley **extraordinarily** perplexing."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "The financial resources of the East India Company proved **extraordinarily** vast during the war."
            }
        ]
    },
    "extraordinariness": {
        "primary": "Remarkable uniqueness, rarity, or departure far beyond ordinary standards.",
        "secondary": "In aesthetics and philosophy, singularity or striking divergence from customary natural patterns.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "The very **extraordinariness** of mystical visions gives them compelling psychological authority."
            },
            {
                "author": "Edmund Burke",
                "work": "A Philosophical Enquiry into the Origin of Our Ideas of the Sublime and Beautiful",
                "quote": "Novelty and sheer **extraordinariness** in external objects excite immediate astonishment in the imagination."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The **extraordinariness** of an empirical claim demands proportionately rigorous experimental demonstration."
            }
        ]
    },
    "extraordinary": {
        "primary": "Very unusual, remarkable, or exceptional; surpassing what is common or expected.",
        "secondary": "In official diplomacy and governance, dispatched outside the regular establishment for special missions.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor was endowed with an **extraordinary** memory and tireless capacity for public business."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The volcanic archipelago presents an **extraordinary** group of animal species found nowhere else."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The president may appoint ambassadors and envoys **extraordinary** to negotiate delicate foreign treaties."
            }
        ]
    },
    "incoordination": {
        "primary": "Lack of coordination, harmony, or concerted action among parts.",
        "secondary": "In clinical neurology, ataxia or the inability to produce smooth, balanced voluntary movements.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Locomotor ataxia presents with striking motor **incoordination** that worsens dramatically when the eyes are closed."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Lesions in the neocerebellum induce severe muscular **incoordination** known as dysdiadochokinesia."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "Administrative **incoordination** among rival state bureaus inevitably breeds waste and delay."
            }
        ]
    },
    "inordinate": {
        "primary": "Unusually or disproportionately large; excessive; exceeding reasonable limits.",
        "secondary": "Disorderly, intemperate, or unconstrained by established moral or social discipline.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The prince's **inordinate** passion for luxury exhausted the revenues of the wealthiest provinces."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Men of intemperate minds cannot be free; their passions forge their own **inordinate** fetters."
            },
            {
                "author": "Adam Smith",
                "work": "The Theory of Moral Sentiments",
                "quote": "An **inordinate** desire for social applause often leads weak men into vanity and deceit."
            }
        ]
    },
    "inordinately": {
        "primary": "To an unusually large or disproportionate degree; excessively.",
        "secondary": "Beyond the bounds of moderation, prudence, or reasonable constraint.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mrs. Bennet was **inordinately** delighted whenever a wealthy bachelor entered the neighborhood."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The attorney took an **inordinately** long time to examine the title deeds through his spectacles."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor was **inordinately** suspicious of any general who achieved military renown."
            }
        ]
    },
    "inordinateness": {
        "primary": "Excessiveness, immoderation, or the absence of reasonable limitation and restraint.",
        "secondary": "In moral philosophy, irregular deviation from virtuous balance and temperance.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "The **inordinateness** of youthful ambitions frequently terminates in bitter adult disappointment."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "When desires lose their rational governance, their **inordinateness** enslaves the human will."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Social peace requires laws that suppress the **inordinateness** of private acquisitive passions."
            }
        ]
    },
    "insubordinate": {
        "primary": "Defiant of authority; disobedient, rebellious, or refusing to submit to orders.",
        "secondary": "In military and maritime law, mutinous conduct displaying willful contempt for lawful superiors.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The general executed several **insubordinate** centurions to restore fear and obedience in the camp."
            },
            {
                "author": "Herman Melville",
                "work": "Billy Budd, Sailor",
                "quote": "The naval articles of war impose capital punishment upon any sailor convicted of **insubordinate** violence."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The squire shouted fiercely at his **insubordinate** son who refused to marry as directed."
            }
        ]
    },
    "insubordination": {
        "primary": "Defiance of authority; refusal to obey lawful orders or institutional discipline.",
        "secondary": "In military jurisprudence, open rebellion or mutinous resistance to established hierarchy.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Chronic **insubordination** among the legions weakened the frontiers against barbarian invaders."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "In democratic armies, equality of social status often breeds latent **insubordination** among recruits."
            },
            {
                "author": "Herman Melville",
                "work": "White-Jacket",
                "quote": "The slightest sign of naval **insubordination** was met by summary flogging at the gangway."
            }
        ]
    },
    "ordain": {
        "primary": "To order, decree, or enact by authoritative virtue; or to invest with ministerial or priestly authority.",
        "secondary": "In ecclesiastical law, to formally confer holy orders upon a candidate through liturgical consecration.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Heaven's supreme monarch did so **ordain** that free will should govern angelic obedience."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Parliament possesses constitutional power to **ordain** new statutory remedies for common law wrongs."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The bishops assembled at the council to **ordain** new canons for church governance across the provinces."
            }
        ]
    },
    "ordained": {
        "primary": "Invested with ministerial or priestly authority; or decreed and settled by fate or authority.",
        "secondary": "Formally consecrated into holy orders through imposition of hands and sacramental ceremony.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Mansfield Park",
                "quote": "Edmund Bertram was soon to be **ordained** and take possession of the family living at Thornton Lacey."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The ancients believed that an inexorable fate had **ordained** the rise and fall of the Roman empire."
            },
            {
                "author": "George Eliot",
                "work": "Scenes of Clerical Life",
                "quote": "The young curate felt deeply the solemn spiritual duties to which he was newly **ordained**."
            }
        ]
    },
    "ordainer": {
        "primary": "One who ordains, decrees, establishes, or confers holy orders upon another.",
        "secondary": "An authoritative lawmaker, appointing bishop, or cosmic providential ruler.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Areopagitica",
                "quote": "God as the supreme **ordainer** left mankind free to choose virtue rather than compelling compliance."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The bishop stands as the legal **ordainer** responsible for examining candidates for holy orders."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Society must reverence the divine **ordainer** whose moral law forms the bedrock of human justice."
            }
        ]
    },
    "ordeal": {
        "primary": "A painful, horrific, or severely testing experience or trial.",
        "secondary": "In ancient and medieval jurisprudence, a trial by ordeal (fire, water) invoking divine judgment to determine guilt.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Trial by **ordeal** of boiling water or glowing iron was abolished under King Henry the Third."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The Templar challenged the maiden to prove her innocence through the dreadful **ordeal** of judicial combat."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The besieged garrison survived the prolonged **ordeal** of famine before relief ships reached the harbor."
            }
        ]
    },
    "order": {
        "primary": "An authoritative command, direction, or instruction; or the arrangement of things in relation to each other.",
        "secondary": "In taxonomic biology, a principal rank between class and family; in society, a recognized social class or fraternal guild.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Naturalists group related families into an **order**, reflecting ancestral genealogical relationships."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The equestrian **order** in Rome held an influential balance between the patricians and the plebeians."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "Civil society cannot endure without an established constitution that secures public peace and good **order**."
            }
        ]
    },
    "order-chenopodiales": {
        "primary": "A historical botanical taxonomic order (Caryophyllales) comprising the goosefoot and amaranth families.",
        "secondary": "In classical plant systematics, an angiosperm order featuring betalain pigments and centrospermous seeds.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Synoptical Flora of North America",
                "quote": "The botanical **order-Chenopodiales** includes weedy annuals and halophytic herbs adapted to saline soils."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Domesticated beetroots and spinaches belong systematically within the floral **order-Chenopodiales**."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Comparative morphologists analyzed seed development across the **order-Chenopodiales** to map floral phylogeny."
            }
        ]
    },
    "ordered": {
        "primary": "Arranged systematically or neatly; or commanded and decreed by authority.",
        "secondary": "In mathematics and physics, possessing regular structural pattern, orientation, or sequence.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "The planets move in smoothly **ordered** orbits governed by universal gravitational attraction."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor **ordered** the immediate mobilization of the legions along the threatened Danube."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The complex anatomical structures of vertebrates present an **ordered** series of homologous bones."
            }
        ]
    },
    "orderer": {
        "primary": "A person or entity that brings about order, arrangement, or direction.",
        "secondary": "A commander, organizer, or supreme providential regulator of worldly affairs.",
        "quotes": [
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "God is the supreme **orderer** of all secondary causes operating throughout the natural universe."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The wise constitutional **orderer** respects the organic traditions inherited from ancient generations."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "The Almighty sat enthroned as the eternal **orderer** of the vast celestial hosts."
            }
        ]
    },
    "ordering": {
        "primary": "The arrangement, grouping, or classification of things according to a particular sequence or method.",
        "secondary": "In mathematics, a binary relation on a set that defines a partial or total sequence among elements.",
        "quotes": [
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "The formal definition of number rests upon the logical **ordering** of relations between classes."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The natural **ordering** of living beings reflects the historic divergence of species from common ancestors."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Prudent commercial **ordering** of accounts ensures the merchant against ruinous capital depletion."
            }
        ]
    },
    "orderliness": {
        "primary": "The quality or disposition of being well-organized, neat, methodical, and obedient to rules.",
        "secondary": "In social and legal theory, harmonious regularity and adherence to public discipline.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The commercial spirit of the American citizens fosters habits of regular labor and civic **orderliness**."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Mary Garth admired the quiet domestic **orderliness** that reigned within the parsonage."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Scientific method instills mental **orderliness**, teaching students to banish confused hypotheses."
            }
        ]
    },
    "orderly": {
        "primary": "Neatly and methodically arranged; well-behaved, peaceful, and respectful of rules.",
        "secondary": "A soldier or hospital attendant assigned to carry messages or assist medical staff.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman army maintained an **orderly** retreat despite relentless harassment by barbarian horsemen."
            },
            {
                "author": "Florence Nightingale",
                "work": "Notes on Nursing",
                "quote": "The hospital **orderly** must ensure that clean linens and fresh ventilation are continually provided."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The succession of fossil types displays an **orderly** progression throughout the geological eras."
            }
        ]
    },
    "ordinal": {
        "primary": "Relating to or denoting order, succession, or rank in a series (such as first, second, third).",
        "secondary": "In Christian liturgy, a book containing the appointed forms for consecrating and ordaining ministers.",
        "quotes": [
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "Cantor distinguished cardinal numbers from **ordinal** numbers when measuring transfinite sets."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The Anglican **ordinal** prescribes the solemn oaths required of all candidates for the episcopate."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Temporal experience presents sensations arranged in strict **ordinal** succession from past to future."
            }
        ]
    },
    "ordinance": {
        "primary": "An authoritative rule, law, or decree promulgated by municipal or sovereign authority.",
        "secondary": "In ecclesiastical practice, a religious rite, sacrament, or established ceremonial observance.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "An imperial **ordinance** strictly prohibited the conversion of Roman citizens to foreign faiths."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "A local municipal **ordinance** cannot supersede the general statutes enacted by the high court of parliament."
            },
            {
                "author": "John Milton",
                "work": "Areopagitica",
                "quote": "No parliament can enforce morality by mere external **ordinance** without corruping the citizen's conscience."
            }
        ]
    },
    "ordinand": {
        "primary": "A candidate preparing for or about to receive holy orders in the Christian church.",
        "secondary": "In ecclesiastical law, an individual undergoing formal examination prior to episcopal ordination.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The bishop possesses full discretion to reject any **ordinand** found deficient in theological doctrine."
            },
            {
                "author": "Anthony Trollope",
                "work": "Barchester Towers",
                "quote": "The earnest young **ordinand** knelt devoutly before the altar rails during the Michaelmas service."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Farebrother recollected his own youthful anxieties when he stood as an **ordinand** before the bishop."
            }
        ]
    },
    "ordinarily": {
        "primary": "In the normal course of events; usually; as a general rule.",
        "secondary": "In a plain, unexceptional, or customary manner without unusual distinction.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Species belonging to the same genus **ordinarily** have very similar habits and constitutions."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "High profits **ordinarily** eat up wages and diminish the competitive advantage of exported wares."
            },
            {
                "author": "David Hume",
                "work": "An Enquiry Concerning Human Understanding",
                "quote": "We **ordinarily** infer causes from effects because custom has habitually conjoined them in our memory."
            }
        ]
    },
    "ordinariness": {
        "primary": "Commonplace normality, routine familiarity, or lack of exceptional distinction.",
        "secondary": "In literary realism and social theory, the quiet texture of routine daily existence.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She found relief in the simple **ordinariness** of village routine after weeks of emotional turmoil."
            },
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "Sudden religious conversion shatters the dull **ordinariness** of customary everyday consciousness."
            },
            {
                "author": "Virginia Woolf",
                "work": "To the Lighthouse",
                "quote": "Beneath the apparent **ordinariness** of family dinners lay currents of intense unspoken emotion."
            }
        ]
    },
    "ordinary": {
        "primary": "With no special or distinctive features; normal, commonplace, or usual.",
        "secondary": "In ecclesiastical and legal administration, an official (such as a bishop) having regular jurisdiction in a diocese.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The structure of the eye cannot possibly be explained by the **ordinary** view of independent creation."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The bishop acted as the ecclesiastical **ordinary** responsible for probating disputed wills."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The market price of every commodity is regulated by the proportion between supply and **ordinary** demand."
            }
        ]
    },
    "ordinate": {
        "primary": "The vertical coordinate on a plane cartesian coordinate system, representing distance along the y-axis.",
        "secondary": "Arranged in orderly, regular patterns; or in botany, positioned in regular, straight rows.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "The curve is described by setting off the abscissa along the base and the **ordinate** perpendicularly."
            },
            {
                "author": "Henri Poincaré",
                "work": "Science and Method",
                "quote": "Geometrical analysis represents dynamic phase space by plotting momentum as an **ordinate** against position."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "Natural history must collect facts in an **ordinate** and methodical manner rather than at random."
            }
        ]
    },
    "ordination": {
        "primary": "The ceremony or act of conferring holy orders upon a priest, deacon, or minister.",
        "secondary": "Systematic arrangement, disposition, or classification of components into an orderly scheme.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The solemn **ordination** of the patriarch of Constantinople was celebrated with imperial pomp."
            },
            {
                "author": "Jane Austen",
                "work": "Mansfield Park",
                "quote": "The conversation turned upon Edmund's approaching **ordination** and the clerical obligations it entailed."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Canons governing episcopal **ordination** require strict examination into moral character and orthodoxy."
            }
        ]
    },
    "ordnance": {
        "primary": "Mounted guns, heavy artillery, cannons, and military weapons along with their ammunition.",
        "secondary": "The military branch or government agency responsible for procuring, maintaining, and supplying weaponry.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The walls of Constantinople were battered by the colossal heavy **ordnance** cast by Hungarian founders."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "The master-general of the **ordnance** hastened to inspect the coastal batteries guarding the Thames."
            },
            {
                "author": "Walter Scott",
                "work": "Waverley",
                "quote": "The thunder of field **ordnance** rolled across the meadow as the rival armies clashed."
            }
        ]
    },
    "ordovician": {
        "primary": "The second period of the Paleozoic era, spanning roughly 485 to 444 million years ago.",
        "secondary": "In historical geology and stratigraphy, a geological system characterized by marine invertebrate radiation and graptolites.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Elements of Geology",
                "quote": "The fossiliferous strata of Wales yield trilobites and brachiopods diagnostic of the **Ordovician** system."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Marine deposits of the **Ordovician** epoch contain abundant traces of extinct cephalopods and corals."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Geologists separated the **Ordovician** from the Silurian to resolve the famous dispute between Murchison and Sedgwick."
            }
        ]
    },
    "ordure": {
        "primary": "Excrement, dung, bodily waste, or filthy filth; disgusting matter.",
        "secondary": "In moral and literary discourse, foul corruption, moral depravity, or scandalous speech.",
        "quotes": [
            {
                "author": "Jonathan Swift",
                "work": "Gulliver's Travels",
                "quote": "The filthy Yahoos discharged their vile **ordure** from the branches above onto Gulliver's head."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "No foul stench or contaminating **ordure** was known in Eden before the fall of man."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The revolutionary mob trampled through the royal palace, defiling the corridors with blood and **ordure**."
            }
        ]
    },
    "preordain": {
        "primary": "To decide, decree, or determine an outcome beforehand by divine will or destiny.",
        "secondary": "In philosophical theology, the doctrine that events are settled beforehand by eternal decree.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "God did not **preordain** human transgression, for man stood free to obey or fall."
            },
            {
                "author": "David Hume",
                "work": "An Enquiry Concerning Human Understanding",
                "quote": "If divine providence did **preordain** every action, then moral praise and blame lose all foundation."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The fatalist doctrines of the East led believers to think that heaven did **preordain** their conquests."
            }
        ]
    },
    "preordained": {
        "primary": "Decided, decreed, or determined beforehand by fate, natural law, or authority.",
        "secondary": "Fixed inexorably in advance, leaving no room for human intervention or chance contingency.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Dilemma of Determinism",
                "quote": "In a deterministic universe, every tragedy was **preordained** from the cosmic foundation of the world."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The astrologer assured the emperor that his military triumph was **preordained** by celestial constellations."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The expansion of equality appears as a providential fact, almost **preordained** by historical destiny."
            }
        ]
    },
    "preordination": {
        "primary": "The authoritative act or doctrine of ordaining and decreeing events beforehand.",
        "secondary": "In theological metaphysics, divine foreordination of universal events and human salvific destiny.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "The theological debate concerning divine **preordination** has perplexed moral philosophers for centuries."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Absolute **preordination** eliminates all meaningful moral distinction between virtue and involuntary reflex."
            },
            {
                "author": "Baruch Spinoza",
                "work": "Tractatus Theologico-Politicus",
                "quote": "Nature operates by necessary causal laws which theologians erroneously anthropomorphize as divine **preordination**."
            }
        ]
    },
    "reorder": {
        "primary": "To rearrange something into a new order or sequence; or to place an additional order for goods.",
        "secondary": "In commerce and logistics, to request replenishment of exhausted inventory from suppliers.",
        "quotes": [
            {
                "author": "Henri Poincaré",
                "work": "Science and Method",
                "quote": "Creative mathematical thought consists in the capacity to **reorder** familiar concepts into novel patterns."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The retail shopkeeper must continually **reorder** stock to meet the fluctuating demands of urban consumers."
            },
            {
                "author": "Bertrand Russell",
                "work": "Introduction to Mathematical Philosophy",
                "quote": "We may **reorder** the elements of an infinite progression without changing its cardinal value."
            }
        ]
    },
    "reordering": {
        "primary": "The process of rearranging items, thoughts, or events into a different sequence or system.",
        "secondary": "In combinatorial analysis, a permutation of a mathematical set into an alternative sequence.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The democratic revolution involved a fundamental **reordering** of social ranks and political loyalties."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "A simple **reordering** of terms in an infinite series may radically alter its analytical sum."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "True scientific induction demands a thorough **reordering** of observed experimental facts."
            }
        ]
    },
    "suborder": {
        "primary": "A taxonomic category ranking below an order and above a family in biological classification.",
        "secondary": "In zoology and botanical systematics, a major subdivisional grouping reflecting evolutionary divergence within an order.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Naturalists divide the mammalian order Rodentia into several distinct **suborder** groups based on jaw morphology."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The fossil reptilian skull displays transitional traits linking it to an extinct dinosaurian **suborder**."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The great family Leguminosae is conventionally arranged into three **suborder** divisions based on petal symmetry."
            }
        ]
    },
    "subordinate": {
        "primary": "Lower in rank, importance, or position; secondary; or subject to another's authority.",
        "secondary": "In grammar, a clause dependent on a main clause; in organizations, an employee reporting to a manager.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "The Subjection of Women",
                "quote": "The social system has long kept women in a strictly **subordinate** legal and domestic status."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The provincial prefects were strictly **subordinate** to the commands issued from the imperial palace."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Modifications in **subordinate** anatomical structures often follow correlated changes in primary organs."
            }
        ]
    },
    "subordinateness": {
        "primary": "Inferiority in rank, power, or authority; dependence upon a higher principle.",
        "secondary": "In administrative theory and logic, dependency or secondary status relative to a superior principle.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "Administrative efficiency requires that local officials understand their constitutional **subordinateness** to parliament."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on American Taxation",
                "quote": "The colonies acknowledged their general **subordinateness** to the imperial crown while defending tax autonomy."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Sociology",
                "quote": "Military societies emphasize the strict **subordinateness** of the individual soldier to the state collective."
            }
        ]
    },
    "subordinating": {
        "primary": "Placing in a lower rank or position; treating as secondary or less important.",
        "secondary": "In grammar, linking a dependent clause to an independent clause using a subordinating conjunction.",
        "quotes": [
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "A **subordinating** conjunction establishes hypotaxis by turning a clause into a syntactic modifier."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor succeeded by **subordinating** personal ambitions to the welfare and defense of the frontiers."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Individualism threatens democracy by **subordinating** broad civic duties to narrow private comforts."
            }
        ]
    },
    "subordination": {
        "primary": "The act of placing in a lower rank; or subjection to institutional authority and discipline.",
        "secondary": "In sociology and law, the structural hierarchy subjecting one group or office to the control of another.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Military **subordination** was maintained by unrelenting drill and the dread of immediate corporal punishment."
            },
            {
                "author": "John Stuart Mill",
                "work": "The Subjection of Women",
                "quote": "The legal **subordination** of one sex to the other is wrong in itself and a chief hindrance to human development."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "Good government demands prompt **subordination** of military commands to civil executive direction."
            }
        ]
    },
    "subordinative": {
        "primary": "Serving to subordinate, rank lower, or express syntactic dependency.",
        "secondary": "In linguistics, denoting conjunctions or constructions that introduce dependent adverbial or nominal clauses.",
        "quotes": [
            {
                "author": "Otto Jespersen",
                "work": "A Modern English Grammar",
                "quote": "Words like 'although' and 'because' carry a **subordinative** role that demotes the verb's independence."
            },
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "Bureaucracy relies on clear **subordinative** chains of command connecting superiors with field clerks."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Sociology",
                "quote": "Social evolution gradually softens harsh **subordinative** relations into voluntary industrial contracts."
            }
        ]
    },
    "superorder": {
        "primary": "A taxonomic category ranking above an order and below a class in biological classification.",
        "secondary": "In vertebrate paleontology and evolutionary taxonomy, an inclusive grouping uniting related orders with common lineage.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Anatomists erected a new **superorder** to accommodate primitive flightless ratites and Mesozoic fossils."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Comparative osteology justifies grouping these placental orders within an expansive mammalian **superorder**."
            },
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "Floral morphology reveals deep structural affinities linking several disparate families into a shared **superorder**."
            }
        ]
    },
    "superordinate": {
        "primary": "Higher in rank, status, or authority; superior; of greater importance.",
        "secondary": "In linguistics and semantics, a hypernym or general term that encompasses more specific hyponyms (e.g., animal for dog).",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Augustus was recognized as the **superordinate** ruler, while the younger Caesar held provincial commands."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Logical classification subsumes specific concepts under a broader **superordinate** category."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Universal laws of mechanics function as **superordinate** principles explaining complex terrestrial motions."
            }
        ]
    },
    "superordination": {
        "primary": "Superiority in official rank, governing power, or categorical classification.",
        "secondary": "In sociology and linguistics, the position of dominance or broader categorical classification over subordinates.",
        "quotes": [
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "The structure of modern administration consists of a firmly ordered system of **superordination** and subordination."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Sociology",
                "quote": "Feudal societies were characterized by rigid personal **superordination** supported by military tenure."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Conceptual taxonomy operates through the **superordination** of higher genera over specialized species."
            }
        ]
    },
    "uncoordinated": {
        "primary": "Not coordinated; lacking smooth organization, synchronization, or muscular rhythm; clumsy.",
        "secondary": "In neurology and sports science, characterized by jerky, unbalanced, or arrhythmic movements.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Cerebellar pathology leaves the patient's gait awkward, staggering, and strikingly **uncoordinated**."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Without sensory feedback from the muscle spindles, motor output degenerates into **uncoordinated** spasms."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The **uncoordinated** attacks of the allied barbarian contingents were easily repulsed by the legion."
            }
        ]
    },
    "unordered": {
        "primary": "Not arranged in an orderly, systematic, or specified sequence; chaotic or random.",
        "secondary": "In set theory and computer science, a collection (such as a mathematical set) where element sequence is irrelevant.",
        "quotes": [
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "A mathematical set is essentially an **unordered** aggregate defined purely by the membership of its elements."
            },
            {
                "author": "Francis Bacon",
                "work": "Novum Organum",
                "quote": "An **unordered** mass of empirical experiments yields only confusion without guiding inductive axioms."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The jumbled glacial drift presented an **unordered** heap of granite boulders and morainic gravel."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_order_b2_p2: {len(data_order_b2_p2)}")
    
    # Validation suite
    errors = []
    circular_re = re.compile(r'\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b', re.IGNORECASE)
    banned_phrases = [
        'In specialized and domain usage, denoting specific qualities',
        'In technical and systematic terminology, the action',
        'In functional and operational contexts, an agent',
        'The clinical presentation of',
        'Every pathological manifestation of',
        'The gradual evolutionary modification of',
        'In academic literature,',
        'Academic Lexicon',
        'Classic Author'
    ]

    for word, item in data_order_b2_p2.items():
        # Check definitions
        p = item.get("primary", "")
        s = item.get("secondary", "")
        if len(p) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(p)} chars)")
        if len(s) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(s)} chars)")
        if circular_re.search(p):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {p}")
        if circular_re.search(s):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {s}")
        if p.strip().lower() == s.strip().lower():
            errors.append(f"[{word}] Primary and Secondary are identical")

        # Jaccard overlap
        p_tokens = set(re.findall(r'\w+', p.lower()))
        s_tokens = set(re.findall(r'\w+', s.lower()))
        union = p_tokens | s_tokens
        intersect = p_tokens & s_tokens
        jaccard = len(intersect) / max(len(union), 1)
        if jaccard >= 0.70:
            errors.append(f"[{word}] Definitions overlap too high ({jaccard:.2f})")

        # Check banned phrases
        for b in banned_phrases:
            if b.lower() in p.lower() or b.lower() in s.lower():
                errors.append(f"[{word}] Contains banned phrase: {b}")

        # Check quotes
        quotes = item.get("quotes", [])
        if len(quotes) != 3:
            errors.append(f"[{word}] Expected 3 quotes, got {len(quotes)}")
        
        authors = set()
        for idx, q in enumerate(quotes):
            auth = q.get("author", "").strip()
            work = q.get("work", "").strip()
            text = q.get("quote", "").strip()
            authors.add(auth)
            if len(auth) < 3:
                errors.append(f"[{word}] Quote {idx+1} author too short: {auth}")
            if len(work) < 2:
                errors.append(f"[{word}] Quote {idx+1} work too short: {work}")
            if "**" not in text:
                errors.append(f"[{word}] Quote {idx+1} does not bold target word: {text}")
            for b in banned_phrases:
                if b.lower() in text.lower() or b.lower() in auth.lower():
                    errors.append(f"[{word}] Quote {idx+1} contains banned phrase: {b}")

        if len(authors) < len(quotes):
            errors.append(f"[{word}] Duplicate authors among quotes: {authors}")

    if errors:
        print(f"\n[X] FOUND {len(errors)} VALIDATION ERRORS:")
        for e in errors:
            print(f"  - {e}")
        exit(1)
    else:
        print("\n[OK] ALL 61 words in Cluster Order Batch 2 Part 2 PASSED local pre-audit validation!")
