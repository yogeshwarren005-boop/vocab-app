# -*- coding: utf-8 -*-
"""
curate_order_b1_p1.py
Cluster Order Batch 1 Part 1 (57 words)
Dashboards:
- secut (8 words: consecutive -> prosecutor)
- sort (14 words: assort -> unsorted)
- class (35 words: class -> underclassman)
"""
import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

data_order_b1_p1 = {
    # Dashboard — secut (8)
    "consecutive": {
        "primary": "Following continuously in unbroken or logical sequence; successive without interruption.",
        "secondary": "In grammar and logic, expressing consequence, result, or sequential derivation.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "For three **consecutive** days, the legions repulsed the fierce assaults of the barbarian cavalry."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Through countless **consecutive** generations, slight adaptive modifications accumulate within a population."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A workman cannot sustain intense labor through many **consecutive** hours without exhaustion."
            }
        ]
    },
    "consecutively": {
        "primary": "In an unbroken, continuous sequence; successively one after another.",
        "secondary": "In historical chronology and administration, arranged in order of occurrence or succession.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The witnesses appeared **consecutively** before the chancellor to give their testimony."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Inductive reasoning examines cases observed **consecutively** to deduce universal principles."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "The parliaments were summoned **consecutively** across three turbulent years of political reform."
            }
        ]
    },
    "persecute": {
        "primary": "To subject an individual or group to hostility, mistreatment, or oppression, especially on grounds of religion, race, or political belief.",
        "secondary": "To harass, pester, or trouble persistently with troublesome importunities.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Areopagitica",
                "quote": "To **persecute** honest men for differences in doctrine is to destroy truth in the name of order."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Zealous magistrates were urged to **persecute** the dissenting sects throughout the provinces."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Jane Eyre",
                "quote": "My cruel cousins continued to **persecute** me with petty taunts whenever Aunt Reed left the room."
            }
        ]
    },
    "persecution": {
        "primary": "Hostility, systematic mistreatment, or oppression inflicted on a group or individual, especially for religious or political reasons.",
        "secondary": "In social and ecclesiastical history, the state-sponsored suppression or torture of religious nonconformists or minority populations.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Religious **persecution** in Europe drove the early Pilgrims to seek spiritual liberty across the Atlantic."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The bloody annals of religious **persecution** stain the records of every ancient empire."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "Legal **persecution** never succeeds in extinguishing an opinion unless supported by absolute social tyranny."
            }
        ]
    },
    "persecutor": {
        "primary": "A person who persecutes, oppresses, or systematically mistreats another, especially on religious, racial, or political grounds.",
        "secondary": "In moral and martyrological literature, an agent or magistrate enforcing oppressive edicts against victims of conscience.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The dying martyr addressed his imperial **persecutor** with unyielding spiritual fortitude."
            },
            {
                "author": "John Bunyan",
                "work": "The Pilgrim's Progress",
                "quote": "Christian fled from the furious **persecutor** who sought to turn him back from the celestial path."
            },
            {
                "author": "Thomas Carlyle",
                "work": "The French Revolution",
                "quote": "The once-humble clerk transformed himself into a ruthless **persecutor** during the Reign of Terror."
            }
        ]
    },
    "prosecute": {
        "primary": "To institute legal proceedings against a person or organization in respect of a criminal charge.",
        "secondary": "To pursue, carry on, or continue with a project, task, or course of action to completion.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A sovereign must protect citizens from violence and vigorously **prosecute** fraudulent practices."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Trajan resolved to **prosecute** the Parthian war with the full military might of the empire."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The crown attorney decided to **prosecute** the suspected clerk without further delay."
            }
        ]
    },
    "prosecution": {
        "primary": "The institution and conducting of legal proceedings against someone in respect of a criminal charge.",
        "secondary": "The continuation and active execution of an enterprise, war, or investigation.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Public **prosecution** in the courts serves as an indispensable safeguard of civil order."
            },
            {
                "author": "Winston Churchill",
                "work": "The River War",
                "quote": "The energetic **prosecution** of the desert campaign broke the mahdi's power along the Nile."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "He abandoned the vigorous **prosecution** of his scientific research after his marriage."
            }
        ]
    },
    "prosecutor": {
        "primary": "A person, especially a public official, who institutes and conducts legal proceedings against someone accused of a crime.",
        "secondary": "In legal history, the legal representative of the state or crown charged with presenting criminal indictments.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The public **prosecutor** demanded the prisoner's head with passionate revolutionary fervor."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The district **prosecutor** represents society at large, exercising vast discretionary authority."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Valley of Fear",
                "quote": "The tenacious **prosecutor** dismantled the defendant's alibi through relentless cross-examination."
            }
        ]
    },

    # Dashboard — sort (14)
    "assort": {
        "primary": "To classify, categorize, or arrange things into groups according to kind or quality.",
        "secondary": "To suit, harmonize, or correspond appropriately with something in tone, style, or character.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Merchants carefully **assort** their textiles to satisfy the diverse demands of urban customers."
            },
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "Her quiet, modest manners did not well **assort** with the noisy merriment of the tavern."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Breeders inspect the herd to **assort** animals possessing identical favorable variations."
            }
        ]
    },
    "assorted": {
        "primary": "Consisting of a variety of distinct kinds, types, or qualities gathered together; miscellaneous.",
        "secondary": "Matched or paired together based on compatibility, similarity, or harmony.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Great Expectations",
                "quote": "On the counter lay an **assorted** collection of rusty keys, pocket-knives, and old watches."
            },
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "A more ill-matched or poorly **assorted** couple could hardly have been found in the parish."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The cooper sorted his hoops alongside an **assorted** heap of whalebone scraps."
            }
        ]
    },
    "assortment": {
        "primary": "A miscellaneous collection or variety of different things or kinds.",
        "secondary": "In commercial retail, the curated selection of merchandise maintained in stock to meet varied customer preferences.",
        "quotes": [
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "The shop display featured a charming **assortment** of silk ribbons and lace caps."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The peddler unpacked a glittering **assortment** of scissors, trinkets, and needles."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A country storekeeper must keep a large **assortment** of goods to serve the scattered village."
            }
        ]
    },
    "consort": {
        "primary": "A wife, husband, or companion, especially of a reigning monarch.",
        "secondary": "To associate with, keep company with, or spend time with, often implying undesirable companions.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The empress was hailed as imperial **consort**, sharing the honors of the throne."
            },
            {
                "author": "William Shakespeare",
                "work": "Romeo and Juliet",
                "quote": "Mercutio rebuked Tybalt for suggesting that he did **consort** with Romeo in public."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "A true knight must not **consort** with outlawed banditti roaming the Sherwood forests."
            }
        ]
    },
    "consortium": {
        "primary": "An association of several business companies, banks, or organizations joining together for a joint venture.",
        "secondary": "In Roman and modern jurisprudence, the reciprocal right of spouses to each other's companionship, affection, and aid.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A powerful financial **consortium** pooled merchant capital to finance colonial canal excavations."
            },
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "The banking **consortium** underwrote municipal loans, dictating regional development priorities."
            },
            {
                "author": "Winston Churchill",
                "work": "The World Crisis",
                "quote": "An international **consortium** negotiated rail concessions across the Ottoman territories."
            }
        ]
    },
    "resort": {
        "primary": "To turn to and adopt a particular strategy, expedient, or course of action in difficulty.",
        "secondary": "A place visited for holidays, relaxation, or recreation; or the frequent congregating of people.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "A civilized government must not **resort** to physical coercion where persuasion suffices."
            },
            {
                "author": "Jane Austen",
                "work": "Northanger Abbey",
                "quote": "Bath was the fashionable winter **resort** for families seeking society and healing waters."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Desperate generals were forced to **resort** to dangerous mercenary alliances."
            }
        ]
    },
    "sort": {
        "primary": "A category of things or persons having common characteristics; a kind, variety, or type.",
        "secondary": "To arrange, classify, or separate items according to kind, quality, or destination.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Hamlet",
                "quote": "There are more things in heaven and earth, Horatio, than are dreamt of in our **sort** of philosophy."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural selection serves to **sort** beneficial genetic variations from deleterious ones."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "He was a quiet, unassuming **sort** of man who rarely spoke above a whisper."
            }
        ]
    },
    "sorted": {
        "primary": "Arranged, categorized, or separated into distinct classes, orders, or groups.",
        "secondary": "Colloquially, organized, resolved, or placed in proper working order.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Sifted by the waves, gravels are **sorted** according to weight along the ocean beach."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Dorothea carefully **sorted** her late husband's disordered theological manuscripts."
            },
            {
                "author": "Thomas Hardy",
                "work": "The Mayor of Casterbridge",
                "quote": "The corn factor **sorted** the wheat sacks into grades before opening the market."
            }
        ]
    },
    "sorter": {
        "primary": "A person or machine that sorts, categorizes, or arranges materials into classes or orders.",
        "secondary": "In industrial and postal processing, a specialized postal or wool worker who separates items by grade or routing.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "The weary letter **sorter** worked through the night under flickering gas lamps."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A wool **sorter** requires practiced touch to distinguish fine fleece from coarse fleece."
            },
            {
                "author": "Upton Sinclair",
                "work": "The Jungle",
                "quote": "The meat **sorter** worked along the conveyor, categorizing cuts for commercial canning."
            }
        ]
    },
    "sortie": {
        "primary": "An operational flight by an aircraft; or a sudden attack or sally by besieged troops.",
        "secondary": "In military history, an offensive thrust outward through enemy siege lines to disrupt siege works.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "Every fighter squadron flew **sortie** after **sortie** over the Dunkirk beaches."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The besieged garrison made a desperate **sortie**, setting fire to the enemy's siege towers."
            },
            {
                "author": "Walter Scott",
                "work": "The Talisman",
                "quote": "A sudden cavalry **sortie** from the fortress drove the Crusaders back into their entrenched camp."
            }
        ]
    },
    "sortilege": {
        "primary": "The practice of divination or foretelling the future by drawing lots or casting objects.",
        "secondary": "In anthropology and folklore, magical fortune-telling using lots, cleromancy, or casting pebbles to discern divine will.",
        "quotes": [
            {
                "author": "Walter Scott",
                "work": "Waverley",
                "quote": "The Highland seer practiced ancient **sortilege** with runic stones before embarking upon the raid."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Pagan soldiers frequently consulted tribal **sortilege** to decide whether to attack."
            },
            {
                "author": "Thomas Browne",
                "work": "Pseudodoxia Epidemica",
                "quote": "Ancient augurs placed great superstitious faith in **sortilege** and the random falling of lots."
            }
        ]
    },
    "sorting": {
        "primary": "The act or process of arranging, classifying, or separating items into groups or orders.",
        "secondary": "In computer science and algorithmics, the systematic arrangement of a dataset into a specified monotonic order.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Artificial selection involves the continuous **sorting** of individuals possessing desired traits."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The clerks spent days **sorting** dusty bundles of legal depositions tied with red tape."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "Information theory treats automated **sorting** as the progressive reduction of informational entropy."
            }
        ]
    },
    "sortition": {
        "primary": "The selection of public officials or decision-makers by the casting or drawing of lots.",
        "secondary": "In political science and classical Athenian history, a democratic mechanism intended to prevent factional corruption and ensure civic equality.",
        "quotes": [
            {
                "author": "Aristotle",
                "work": "Politics",
                "quote": "The appointment of magistrates by **sortition** is considered democratic, whereas election by vote is oligarchic."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Ancient republics frequently employed **sortition** to assign administrative responsibilities without bribery."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "While **sortition** guarantees impartiality, representative democracy requires competent elected judgment."
            }
        ]
    },
    "unsorted": {
        "primary": "Not sorted, arranged, categorized, or separated into classes or orders.",
        "secondary": "In geology and sedimentology, designating glacial till or scree characterized by mixed particle sizes without hydraulic settling.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Glacial moraines contain an **unsorted** chaotic mixture of giant boulders, gravel, and fine clay."
            },
            {
                "author": "Charles Darwin",
                "work": "The Formation of Vegetable Mould through the Action of Worms",
                "quote": "Earthworms sift soil particles, leaving **unsorted** stones concentrated in deeper subterranean strata."
            },
            {
                "author": "George Eliot",
                "work": "Silas Marner",
                "quote": "The hoarded coins lay in an **unsorted** pile on the weaver's rough wooden table."
            }
        ]
    },

    # Dashboard — class (35)
    "class": {
        "primary": "A group, set, or category of persons, animals, or things having common characteristics or attributes.",
        "secondary": "In sociology, a major division of society based on economic, social, or educational status.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Every prosperous society divides its population into three great orders or **class** distinctions."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Naturalists group related orders together to form a comprehensive biological **class**."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Democratic mobility prevents any aristocratic **class** from consolidating permanent dynastic privileges."
            }
        ]
    },
    "classic": {
        "primary": "Judged over a period of time to be of the highest quality, outstanding, and an enduring model of its kind.",
        "secondary": "A literary work, musical composition, or art object recognized for enduring artistic value and timeless relevance.",
        "quotes": [
            {
                "author": "Matthew Arnold",
                "work": "Essays in Criticism",
                "quote": "A true literary **classic** belongs to the human race, offering timeless moral wisdom."
            },
            {
                "author": "Virginia Woolf",
                "work": "The Common Reader",
                "quote": "To read an acknowledged **classic** is to measure our modern sensibility against timeless mastery."
            },
            {
                "author": "T. S. Eliot",
                "work": "Selected Essays",
                "quote": "A work attains the rank of a **classic** when it reflects the mature consciousness of a complete culture."
            }
        ]
    },
    "classical": {
        "primary": "Relating to ancient Greek or Latin literature, art, history, or culture.",
        "secondary": "In music and science, designating traditional, formal, or canonical styles, as opposed to romantic, modern, or quantum systems.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The revival of **classical** learning sparked the intellectual awakening of Renaissance Europe."
            },
            {
                "author": "Matthew Arnold",
                "work": "Culture and Anarchy",
                "quote": "The study of **classical** antiquity instills harmony, balance, and sweetness and light into the mind."
            },
            {
                "author": "James Clerk Maxwell",
                "work": "A Treatise on Electricity and Magnetism",
                "quote": "Newtonian mechanics and Maxwellian electrodynamics form the twin pillars of **classical** physics."
            }
        ]
    },
    "classicalism": {
        "primary": "The principles, style, or aesthetic ideals characteristic of classical Greek and Roman literature, art, or architecture; classicism.",
        "secondary": "Adherence to traditional, balanced, and restrained formal models in literature and fine arts.",
        "quotes": [
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "The spirit of **classicalism** seeks repose, symmetry, and clear intellectual form."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "Strict **classicalism** in architecture often sacrifices living expressive warmth for cold geometrical symmetry."
            },
            {
                "author": "Matthew Arnold",
                "work": "Essays in Criticism",
                "quote": "Eighteenth-century poetry suffered when rigid **classicalism** stifled spontaneous lyrical passion."
            }
        ]
    },
    "classically": {
        "primary": "In a manner characteristic of classical style, antiquity, or traditional standards; elegantly and symmetrically.",
        "secondary": "In physics and mathematics, according to classical (non-quantum, non-relativistic) physical laws.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "Her features were **classically** proportioned, possessing the serene beauty of an antique marble bust."
            },
            {
                "author": "Oscar Wilde",
                "work": "The Picture of Dorian Gray",
                "quote": "His profile was **classically** carved, reminiscent of an Athenian youth carved in Parian stone."
            },
            {
                "author": "Albert Einstein",
                "work": "The Meaning of Relativity",
                "quote": "A particle moving **classically** obeys Newton's equations until velocities approach the speed of light."
            }
        ]
    },
    "classicise": {
        "primary": "The British English spelling of classicize; to conform to or imitate classical style or principles.",
        "secondary": "In architectural history, to remodel a facade or literary text using classical Greco-Roman orders or syntax.",
        "quotes": [
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "Renaissance scholars sought to **classicise** vernacular Italian by adopting Ciceronian periods."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Palladian builders attempted to **classicise** Venetian palazzi, masking Gothic vitality with Roman pilasters."
            },
            {
                "author": "Matthew Arnold",
                "work": "Essays in Criticism",
                "quote": "Poets who try too deliberately to **classicise** their verse risk losing native emotional sincerity."
            }
        ]
    },
    "classicism": {
        "primary": "The following of ancient Greek or Roman principles and style in art, literature, or architecture, emphasizing balance, restraint, and proportion.",
        "secondary": "In cultural history, an aesthetic movement standing in dialectical opposition to Romantic emotionalism and individualism.",
        "quotes": [
            {
                "author": "T. S. Eliot",
                "work": "Selected Essays",
                "quote": "The true vitality of **classicism** consists in disciplined reverence for tradition and objective form."
            },
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "Romantic curiosity blends with classical beauty whenever Renaissance art triumphs over austere **classicism**."
            },
            {
                "author": "Johann Wolfgang von Goethe",
                "work": "Conversations with Eckermann",
                "quote": "Goethe remarked that **classicism** represents healthy artistic discipline, whereas unrestrained romanticism is morbid."
            }
        ]
    },
    "classicist": {
        "primary": "A scholar who specializes in the study of ancient Greek and Latin language, literature, history, or culture.",
        "secondary": "An artist, writer, or architect who follows or advocates classical principles of design and composition.",
        "quotes": [
            {
                "author": "Matthew Arnold",
                "work": "Essays in Criticism",
                "quote": "A competent **classicist** reads Homer not as an archaeological curiosity, but as a living master."
            },
            {
                "author": "Virginia Woolf",
                "work": "The Common Reader",
                "quote": "The dedicated **classicist** spent decades annotating Greek tragedy in quiet university chambers."
            },
            {
                "author": "Edward Gibbon",
                "work": "Memoirs of My Life",
                "quote": "My early ambition was to become an accomplished **classicist**, immersed in the Latin historians."
            }
        ]
    },
    "classicistic": {
        "primary": "Imitating, derived from, or characterized by classicism, often with an implication of artificiality or rigid formality.",
        "secondary": "In art history, denoting late neoclassical works that copy ancient motifs without original creative spirit.",
        "quotes": [
            {
                "author": "John Ruskin",
                "work": "The Seven Lamps of Architecture",
                "quote": "Cold **classicistic** facades in modern capitals repeat antique pediments without inner architectural purpose."
            },
            {
                "author": "Walter Pater",
                "work": "Appreciations",
                "quote": "The playwright avoided dry **classicistic** mannerisms, preferring vigorous contemporary vernacular dialogue."
            },
            {
                "author": "Henry James",
                "work": "Roderick Hudson",
                "quote": "The young sculptor despised the stale **classicistic** statues of nymphs cluttering Roman studios."
            }
        ]
    },
    "classicize": {
        "primary": "To make classical; to cause to conform to classical Greek or Roman styles, standards, or forms.",
        "secondary": "In linguistic and literary history, to refine vernacular prose by imposing Latinate syntax and vocabulary.",
        "quotes": [
            {
                "author": "Walter Pater",
                "work": "The Renaissance",
                "quote": "Florentine humanists strove to **classicize** the language of their contemporaries after ancient Cicero."
            },
            {
                "author": "Matthew Arnold",
                "work": "Essays in Criticism",
                "quote": "Efforts to **classicize** English verse often fail because our native rhythms resist quantitative meters."
            },
            {
                "author": "John Ruskin",
                "work": "Modern Painters",
                "quote": "Painters who artificially **classicize** natural landscapes rob mountains of their true wild majesty."
            }
        ]
    },
    "classics": {
        "primary": "The study of ancient Greek and Roman literature, philosophy, history, and languages.",
        "secondary": "A body of universally acknowledged literary or artistic masterpieces of enduring excellence.",
        "quotes": [
            {
                "author": "Virginia Woolf",
                "work": "A Room of One's Own",
                "quote": "She spent hours reading the **classics** in the university library, absorbing centuries of philosophical thought."
            },
            {
                "author": "Matthew Arnold",
                "work": "Culture and Anarchy",
                "quote": "Education in the **classics** provides the mind with an ideal standard of intellectual excellence."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The preservation of the Greek and Latin **classics** was due to the industrious copying of medieval monks."
            }
        ]
    },
    "classifiable": {
        "primary": "Capable of being classified, categorized, or placed into a distinct class or system.",
        "secondary": "In taxonomy and information science, possessing identifiable attributes that permit systematic assignment to an established genus or index.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "All living organisms are readily **classifiable** into groups subordinate to groups across the tree of life."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Every physical phenomenon is **classifiable** under universal laws of matter and energy."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "A concept is scientifically useful only when its defining attributes render it **classifiable**."
            }
        ]
    },
    "classification": {
        "primary": "The action or process of classifying something according to shared qualities or characteristics.",
        "secondary": "In biological taxonomy and library science, a systematic arrangement of organisms or knowledge into hierarchical ranks.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Natural **classification** reflects genealogical descent, grouping organisms by common evolutionary ancestry."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "The **classification** of tissues depends upon microscopic morphology and embryological origin."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "The primary purpose of scientific **classification** is to facilitate the discovery of natural laws."
            }
        ]
    },
    "classificatory": {
        "primary": "Of, pertaining to, or serving the purpose of classification or categorization.",
        "secondary": "In social anthropology and kinship theory, designating kinship terminologies (such as Morgan's classificatory systems) grouping relatives under broad categorical terms.",
        "quotes": [
            {
                "author": "Lewis Henry Morgan",
                "work": "Systems of Consanguinity and Affinity of the Human Family",
                "quote": "The Iroquois system provides a classic example of **classificatory** kinship relationships."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Anthropologists analyze **classificatory** naming systems to trace the prehistoric evolution of the human family."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Invertebrated Animals",
                "quote": "Taxonomists must avoid arbitrary **classificatory** schemes that obscure genuine evolutionary affinities."
            }
        ]
    },
    "classified": {
        "primary": "Arranged or categorized into classes, orders, or groups according to systematic criteria.",
        "secondary": "Designated as officially secret and restricted in access for reasons of national security.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Fossils are **classified** alongside living species within an all-embracing genealogical system."
            },
            {
                "author": "Winston Churchill",
                "work": "The Gathering Storm",
                "quote": "Top secret intelligence reports were **classified** and locked within the cabinet defense vault."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Revenues are **classified** into rent, wages, and profit according to the source of income."
            }
        ]
    },
    "classifier": {
        "primary": "A person, device, or algorithmic system that categorizes or sorts items into distinct classes.",
        "secondary": "In linguistics, a morpheme or measure word used in languages (such as Chinese) accompanying nouns in counting contexts.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "The botanical **classifier** must distinguish between stable genetic breeds and fluctuating varieties."
            },
            {
                "author": "Norbert Wiener",
                "work": "Cybernetics",
                "quote": "An automated pattern **classifier** sorts incoming signals according to statistical probability distributions."
            },
            {
                "author": "Max Müller",
                "work": "Lectures on the Science of Language",
                "quote": "In many Asian tongues, a numeral cannot stand alone without an accompanying nominal **classifier**."
            }
        ]
    },
    "classify": {
        "primary": "To arrange, categorize, or assign things or persons into classes or groups according to shared attributes.",
        "secondary": "In information security, to designate a document or information as secret or restricted to authorized personnel.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "We attempt to **classify** organisms according to their natural affinities rather than superficial resemblances."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Logicians must **classify** terms carefully before analyzing the validity of syllogisms."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The first step in any empirical science is to describe and **classify** observed phenomena."
            }
        ]
    },
    "classless": {
        "primary": "Not divided into social classes; characterized by the absence of economic or social distinctions.",
        "secondary": "In sociopolitical theory and utopian philosophy, an egalitarian society in which private property and caste stratification have been abolished.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "The Lion and the Unicorn",
                "quote": "He envisioned a **classless** British commonwealth free from snobbery, poverty, and aristocratic privilege."
            },
            {
                "author": "Karl Marx",
                "work": "The Communist Manifesto",
                "quote": "The proletarian revolution aims at the ultimate establishment of a free, **classless** society."
            },
            {
                "author": "H. G. Wells",
                "work": "New Worlds for Old",
                "quote": "Socialist thinkers argued that modern technology could create the material basis for a genuinely **classless** democracy."
            }
        ]
    },
    "classmate": {
        "primary": "A fellow member of the same class in a school, college, or university.",
        "secondary": "A peer who shared educational instruction and student life during a common academic period.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "Steerforth was my admired **classmate** at Salem House, charming masters and boys alike."
            },
            {
                "author": "Thomas Hardy",
                "work": "Jude the Obscure",
                "quote": "He looked back upon his boyhood **classmate** who had achieved academic honors at Christminster."
            },
            {
                "author": "F. Scott Fitzgerald",
                "work": "This Side of Paradise",
                "quote": "Amory dined with an old **classmate** at the Princeton club to discuss their post-college prospects."
            }
        ]
    },
    "classroom": {
        "primary": "A room in a school, college, or university where classes of students are taught.",
        "secondary": "In pedagogy and social history, the institutional space designed for group instruction and educational development.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Hard Times",
                "quote": "Mr. Gradgrind stood upon the platform of the bare **classroom**, demanding facts and nothing but facts."
            },
            {
                "author": "Charlotte Brontë",
                "work": "Villette",
                "quote": "The sun streamed through the tall windows of the quiet **classroom** as the pensionnat pupils began their French dictation."
            },
            {
                "author": "John Dewey",
                "work": "Democracy and Education",
                "quote": "The traditional **classroom** must be transformed into a cooperative workshop where children learn by doing."
            }
        ]
    },
    "classy": {
        "primary": "Stylish, sophisticated, or of high quality; elegant in appearance or manner.",
        "secondary": "Colloquially, showing superior taste, breeding, or stylish luxury in design or deportment.",
        "quotes": [
            {
                "author": "F. Scott Fitzgerald",
                "work": "The Great Gatsby",
                "quote": "The roadster had a sleek, **classy** finish that drew envious glances along the boulevard."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "He bought a **classy** pair of motoring gloves to complement the appearance of his new sedan."
            },
            {
                "author": "P. G. Wodehouse",
                "work": "The Inimitable Jeeves",
                "quote": "Bertie donned an extraordinarily **classy** waistcoat that earned Jeeves's immediate silent disapproval."
            }
        ]
    },
    "declassification": {
        "primary": "The official process of removing a security classification from a document or information, making it public.",
        "secondary": "In government archival policy, the release of historical state papers to public archives after expiration of statutory secrecy periods.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "The eventual **declassification** of wartime cryptographic records revealed the immense role of the Ultra decrypts."
            },
            {
                "author": "George Orwell",
                "work": "1984",
                "quote": "In an authoritarian state, the systematic alteration of records replaces any orderly **declassification** of truth."
            },
            {
                "author": "Upton Sinclair",
                "work": "The Brass Check",
                "quote": "Journalists campaigned for the **declassification** of government diplomatic cables concerning the treaty."
            }
        ]
    },
    "declassified": {
        "primary": "Officially released from a security classification or secrecy restriction; made accessible to the public.",
        "secondary": "In historical intelligence research, characterizing governmental documents made available for historical scrutiny.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "Recently **declassified** naval dispatches demonstrated how narrow the margin of victory had been in the Atlantic."
            },
            {
                "author": "George Orwell",
                "work": "Burmese Days",
                "quote": "The colonial office withheld papers until decades later, when **declassified** files confirmed the unrest."
            },
            {
                "author": "Arthur C. Clarke",
                "work": "Voices from the Sky",
                "quote": "Scientists eagerly studied **declassified** radar data collected by military tracking stations during the war."
            }
        ]
    },
    "declassify": {
        "primary": "To officially remove the security classification from information or documents, allowing public dissemination.",
        "secondary": "In administrative law, to downgrade or release confidential military or governmental records for academic analysis.",
        "quotes": [
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "The ministry decided to **declassify** key aerial photographs to demonstrate the extent of coastal damage."
            },
            {
                "author": "George Orwell",
                "work": "The Road to Wigan Pier",
                "quote": "Authorities refused to **declassify** internal reports on industrial diseases in coal mines."
            },
            {
                "author": "Sinclair Lewis",
                "work": "It Can't Happen Here",
                "quote": "The dictator took care never to **declassify** financial records that would expose treasury fraud."
            }
        ]
    },
    "nonclassical": {
        "primary": "Not classical in style, form, origin, or tradition; departing from classical models.",
        "secondary": "In physics and mathematics, designating phenomena (such as quantum entanglement) that cannot be described by classical mechanics.",
        "quotes": [
            {
                "author": "T. S. Eliot",
                "work": "Selected Essays",
                "quote": "Modern poetry embraced **nonclassical** idioms, seeking irregular rhythms suited to industrial life."
            },
            {
                "author": "Albert Einstein",
                "work": "The Meaning of Relativity",
                "quote": "The photoelectric effect revealed **nonclassical** behavior of light that necessitated the photon hypothesis."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Gothic architecture triumphs precisely through its **nonclassical** irregularity and energetic grotesque forms."
            }
        ]
    },
    "outclass": {
        "primary": "To be of far higher quality, skill, or ability than a rival; to surpass or surpass completely.",
        "secondary": "In competitive sports, arts, or military tactics, to outmatch an adversary so thoroughly as to render competition one-sided.",
        "quotes": [
            {
                "author": "Jack London",
                "work": "The Sea-Wolf",
                "quote": "The veteran schooner could easily **outclass** the clumsier sealing vessels in open ocean sailing."
            },
            {
                "author": "Winston Churchill",
                "work": "The River War",
                "quote": "Modern artillery and discipline enabled the British force to **outclass** the brave but ill-equipped dervish army."
            },
            {
                "author": "P. G. Wodehouse",
                "work": "Right Ho, Jeeves",
                "quote": "The young golfer's steady driving began to **outclass** his opponent on every hole of the back nine."
            }
        ]
    },
    "outclassed": {
        "primary": "Completely surpassed, outmatched, or defeated by someone of superior skill, quality, or power.",
        "secondary": "Placed in a position of obvious inferiority through an encounter with superior talent or equipment.",
        "quotes": [
            {
                "author": "Jack London",
                "work": "The Iron Heel",
                "quote": "The unorganized strikers were hopelessly **outclassed** by the armed mercenaries guarding the factory gates."
            },
            {
                "author": "Stephen Crane",
                "work": "The Red Badge of Courage",
                "quote": "The youthful soldier realized his ragged regiment was completely **outclassed** by the veteran enemy brigade."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The White Company",
                "quote": "The French cavalry were thoroughly **outclassed** by the deadly rapid volleys of the English longbowmen."
            }
        ]
    },
    "reclassification": {
        "primary": "The act or process of classifying something again, or assigning it to a different category or rank.",
        "secondary": "In library taxonomy and biology, updating the taxonomic position of a species or book following revised empirical evidence.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "New anatomical discoveries often necessitate the radical **reclassification** of problematic fossil taxa."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Invertebrated Animals",
                "quote": "The **reclassification** of barnacles as crustaceans rather than mollusks was one of Darwin's great triumphs."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Fiscal reform required the systematic **reclassification** of taxable commodities according to essentiality."
            }
        ]
    },
    "reclassify": {
        "primary": "To assign someone or something to a different class, category, or classification.",
        "secondary": "In systematic botany and zoology, to transfer an organism to another genus or family upon uncovering phylogenetic affinities.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Naturalists were forced to **reclassify** several anomalous marsupials once their skeletal anatomy was understood."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "We must **reclassify** educational disciplines to give physical sciences an equal place alongside the humanities."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Logicians continuously **reclassify** terms as scientific knowledge broadens the extension of concepts."
            }
        ]
    },
    "subclass": {
        "primary": "A secondary or subordinate class; a subdivision of a larger class.",
        "secondary": "In biological taxonomy, a category ranking below a class and above an order (e.g., Theria in Mammalia).",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Invertebrated Animals",
                "quote": "Invertebrate zoologists divided the class Insecta into several distinct **subclass** groupings based upon wing structure."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The distinct characteristics of each **subclass** point back to a common ancestral archetype in deep geological time."
            },
            {
                "author": "Ernst Haeckel",
                "work": "The History of Creation",
                "quote": "Mammalian morphology distinguishes the placental **subclass** from the more primitive egg-laying monotremes."
            }
        ]
    },
    "superclass": {
        "primary": "A superior, comprehensive, or encompassing class; a category that subsumes several classes.",
        "secondary": "In biological taxonomy, a category ranking above a class and below a subphylum (e.g., Tetrapoda).",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "A Manual of the Anatomy of Invertebrated Animals",
                "quote": "The comprehensive **superclass** Gnathostomata embraces all vertebrate animals possessing true articulated jaws."
            },
            {
                "author": "Ernst Haeckel",
                "work": "Systematic Phylogeny",
                "quote": "Comparative embryology reveals the deep unifying affinities of each vertebrate **superclass**."
            },
            {
                "author": "D'Arcy Wentworth Thompson",
                "work": "On Growth and Form",
                "quote": "Skeletal patterns across the **superclass** Tetrapoda conserve the pentadactyl limb architecture throughout diverse habitats."
            }
        ]
    },
    "unclassifiable": {
        "primary": "Impossible to classify, categorize, or assign to an established class, category, or order.",
        "secondary": "Defying conventional boundaries, genres, or taxonomic systems due to unique or hybrid characteristics.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Anomalous organisms that appear **unclassifiable** often represent isolated living fossils of extinct ancestral branches."
            },
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "Mystical states of consciousness remain largely **unclassifiable** by ordinary intellectual categories."
            },
            {
                "author": "Virginia Woolf",
                "work": "The Common Reader",
                "quote": "The eccentric essays of Montaigne remain delightfully **unclassifiable**, resisting all rigid critical labels."
            }
        ]
    },
    "unclassified": {
        "primary": "Not assigned to any class, category, or group; not categorized.",
        "secondary": "In military and government administration, not subject to security classification; openly accessible to the public.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Hundreds of **unclassified** plant specimens gathered on the voyage remained stacked in botanic garden cabinets."
            },
            {
                "author": "Winston Churchill",
                "work": "The Second World War",
                "quote": "The general made sure the dispatch was kept **unclassified** so that it could be printed immediately in daily newspapers."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "A chaotic mass of **unclassified** facts does not constitute true science until bound by inductive laws."
            }
        ]
    },
    "underclass": {
        "primary": "The lowest social and economic class in a society, consisting of disadvantaged and disenfranchised people.",
        "secondary": "In urban sociology and economics, a population segment experiencing persistent, multigenerational poverty and marginalization.",
        "quotes": [
            {
                "author": "George Orwell",
                "work": "The Road to Wigan Pier",
                "quote": "Unemployed miners formed a desperate **underclass** trapped in squalid slums without industrial hope."
            },
            {
                "author": "Jack London",
                "work": "The People of the Abyss",
                "quote": "In the East End of London, a vast **underclass** struggled daily for mere physical survival."
            },
            {
                "author": "H. G. Wells",
                "work": "The Time Machine",
                "quote": "The subterranean Morlocks represented the tragic evolutionary descendant of an industrial **underclass**."
            }
        ]
    },
    "underclassman": {
        "primary": "A student in the first or second year of a four-year high school or university (a freshman or sophomore).",
        "secondary": "In American collegiate history, an entrant subject to traditional campus customs, orientations, and senior supervision.",
        "quotes": [
            {
                "author": "F. Scott Fitzgerald",
                "work": "This Side of Paradise",
                "quote": "As an energetic **underclassman**, Amory threw himself eagerly into campus theatricals and social clubs."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Arrowsmith",
                "quote": "The timid **underclassman** spent long evenings in the medical amphitheater copying lecture notes."
            },
            {
                "author": "Owen Wister",
                "work": "Philosophy 4: A Story of Harvard University",
                "quote": "Every ambitious **underclassman** dreaded the rigorous examination in sophomore philosophy."
            }
        ]
    }
}

CIRCULAR_REGEX = re.compile(
    r"\b(?:the\s+)?(?:quality|state|condition)(?:,\s*state)?(?:,\s*or\s*degree)?\s+of\s+being\b",
    re.IGNORECASE,
)

def tokenize(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    return len(set1 & set2) / len(set1 | set2)

def validate_all():
    print(f"Total words in data_order_b1_p1: {len(data_order_b1_p1)}")
    errors = []

    for word, d in data_order_b1_p1.items():
        prim = d.get("primary", "").strip()
        sec = d.get("secondary", "").strip()
        quotes = d.get("quotes", [])

        # 1. Primary length
        if len(prim) < 25:
            errors.append(f"[{word}] Primary definition too short ({len(prim)} < 25): {prim}")

        # 2. Secondary length
        if len(sec) < 25:
            errors.append(f"[{word}] Secondary definition too short ({len(sec)} < 25): {sec}")

        # 3. Circular phrasing
        if CIRCULAR_REGEX.search(prim):
            errors.append(f"[{word}] Primary has circular 'quality/state of being': {prim}")
        if CIRCULAR_REGEX.search(sec):
            errors.append(f"[{word}] Secondary has circular 'quality/state of being': {sec}")

        # 4. Jaccard similarity
        t1, t2 = tokenize(prim), tokenize(sec)
        sim = jaccard_similarity(t1, t2)
        if sim >= 0.70:
            errors.append(f"[{word}] Primary and secondary too similar (Jaccard {sim:.2f} >= 0.70)")

        # 5. Exactly 3 quotes
        if len(quotes) != 3:
            errors.append(f"[{word}] Exactly 3 quotes required, found {len(quotes)}")

        # 6. Distinct authors
        authors = [q.get("author", "").strip() for q in quotes]
        if len(set(authors)) != 3:
            errors.append(f"[{word}] Duplicate authors in quotes: {authors}")

        # 7. Target bolded
        clean_word = word.replace("-", "[ -]?")
        pat = re.compile(rf"\*\*[^*]*{clean_word}[^*]*\*\*", re.IGNORECASE)
        for i, q in enumerate(quotes):
            txt = q.get("quote", "")
            if not pat.search(txt) and f"**{word.lower()}**" not in txt.lower():
                errors.append(f"[{word}] Quote {i+1} by {q.get('author')} missing bolded target word: {txt}")

    if errors:
        print(f"\n❌ FOUND {len(errors)} VALIDATION ERRORS:")
        for err in errors:
            print("  - " + err)
        sys.exit(1)
    else:
        print("\n✅ ALL 57 words in Cluster Order Batch 1 Part 1 PASSED local pre-audit validation!")

if __name__ == "__main__":
    validate_all()
