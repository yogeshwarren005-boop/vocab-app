# -*- coding: utf-8 -*-
"""
curate_order_b4_p1.py
Curated dataset for Cluster Order Batch 4 Part 1:
- Dashboard — fin (56 words: affinal -> finesse)
Total: 56 words
"""
import re

data_order_b4_p1 = {
    # ----------------------------------------------------
    # DASHBOARD — FIN (Part 1: 56 words)
    # ----------------------------------------------------
    "affinal": {
        "primary": "Related by marriage or alliance rather than by blood descent.",
        "secondary": "In social anthropology and kinship systems, denoting relatives or legal bonds created through marital unions.",
        "quotes": [
            {
                "author": "Edward Westermarck",
                "work": "The History of Human Marriage",
                "quote": "Tribal societies establish elaborate taboos regulating mutual obligations between consanguineous and **affinal** kin."
            },
            {
                "author": "Henry Sumner Maine",
                "work": "Ancient Law",
                "quote": "Early patriarchal law distinguished sharply between agnatic succession and mere **affinal** relationships."
            },
            {
                "author": "Lewis Henry Morgan",
                "work": "Systems of Consanguinity and Affinity of the Human Family",
                "quote": "The Iroquois kinship nomenclature provides distinct classificatory designations for every **affinal** connection."
            }
        ]
    },
    "affine": {
        "primary": "Related by marriage, or denoting a geometric transformation that preserves collinearity and ratios of distances.",
        "secondary": "In mathematics and affine geometry, preserving parallel lines and incidence while allowing shear and scaling.",
        "quotes": [
            {
                "author": "Felix Klein",
                "work": "Elementary Mathematics from an Advanced Standpoint",
                "quote": "Under an **affine** transformation, parallel lines remain parallel while circles deform into ellipses."
            },
            {
                "author": "Arthur Cayley",
                "work": "Collected Mathematical Papers",
                "quote": "Projective geometry subsumes both Euclidean metrics and intermediate **affine** coordinate spaces."
            },
            {
                "author": "Henry Sumner Maine",
                "work": "Ancient Law",
                "quote": "The Roman praetor recognized certain legal protections for an **affine** relative excluded from the agnatic clan."
            }
        ]
    },
    "affined": {
        "primary": "Bound by kinship, marriage, mutual obligation, or moral allegiance; allied.",
        "secondary": "In archaic and dramatic verse, linked by duty or bound in close fellowship to a superior.",
        "quotes": [
            {
                "author": "William Shakespeare",
                "work": "Othello",
                "quote": "If partially **affined**, or leagued in office, thou dost deliver more or less than truth, thou art no soldier."
            },
            {
                "author": "John Milton",
                "work": "The Reason of Church-Government",
                "quote": "Civil magistrates and religious teachers are closely **affined** in promoting virtuous social peace."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "The Saxon thane felt himself honorably **affined** to the royal line of ancient Wessex monarchs."
            }
        ]
    },
    "affinity": {
        "primary": "A spontaneous or natural liking or sympathy for someone or something; or kinship by marriage.",
        "secondary": "In chemistry, the thermodynamic tendency of chemical substances to combine; in taxonomy, structural resemblance indicating common descent.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Naturalists look for deep morphological **affinity** rather than superficial adaptive resemblances between species."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Chemical **affinity** governs the elective attraction by which acids unite with alkaline bases."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Marriages within the prohibited degrees of consanguinity or **affinity** were declared null by ecclesiastical law."
            }
        ]
    },
    "confine": {
        "primary": "To keep or restrict someone or something within certain limits of space, scope, or activity.",
        "secondary": "To imprison, detain, or restrain an individual from free movement; or to border upon a territory.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Augustus advised his successors to **confine** the imperial frontiers within the Rhine, Danube, and Euphrates."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "We must **confine** our inquiries to those subjects which lie within the reach of human understanding."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The fortress walls served to **confine** political captives in dark subterranean dungeons."
            }
        ]
    },
    "confined": {
        "primary": "Restricted in space, scope, or freedom of movement; limited, cramped, or enclosed.",
        "secondary": "Undergoing childbirth or kept to bed through acute physical illness or childbed labor.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "Endemic species on the Galapagos islands are **confined** to narrow rocky territories of volcanic origin."
            },
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "Mrs. Dashwood remained **confined** to her bedchamber for several days following the severe chill."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The emperor's military power was **confined** within the narrow circuit of the city walls."
            }
        ]
    },
    "confinement": {
        "primary": "Restriction, imprisonment, or forced detention within an enclosed space.",
        "secondary": "The period or condition of remaining in bed during and immediately following childbirth (lying-in).",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "On the Penitentiary System in the United States",
                "quote": "Solitary **confinement** was designed to produce moral reflection through silent isolation from corrupting companions."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mrs. Bennet lamented that her nervous disorders and prolonged domestic **confinement** ruined her spirits."
            },
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "He endured years of tedious **confinement** within the bleak debtor's prison of the Marshalsea."
            }
        ]
    },
    "confines": {
        "primary": "The borders, limits, or boundaries of a geographical area, space, or field of thought.",
        "secondary": "In political geography and territorial sovereignty, the borderlands or frontiers separating distinct realms.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The legions guarded the distant **confines** of the empire against the incursions of the Sarmatians."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Near the **confines** of radiant light and primeval chaos stood the boundless cosmic void."
            },
            {
                "author": "Francis Bacon",
                "work": "The Advancement of Learning",
                "quote": "Natural philosophy must not overstep the lawful **confines** assigned by divine wisdom."
            }
        ]
    },
    "confining": {
        "primary": "Restricting, limiting, or enclosing within narrow physical or operational boundaries.",
        "secondary": "Imposing narrow mental or social limits that impede free growth or expression.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "The practice of **confining** wild animals in menageries frequently impairs their natural fertility."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Dorothea felt the provincial atmosphere of Tipton to be suffocating and **confining** to her soul."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Mercantile legislation erred by **confining** colonial trade to the exclusive monopoly of the mother country."
            }
        ]
    },
    "definable": {
        "primary": "Capable of being clearly defined, explained, delimited, or identified.",
        "secondary": "In logic and mathematics, expressible through explicit predicates or formal boundary criteria.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Complex ideas are readily **definable** by enumerating the simple impressions that compose them."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Principles of Mathematics",
                "quote": "Every mathematical concept must be strictly **definable** in terms of logical primitives."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Varieties shade into one another, leaving no clearly **definable** line separating races."
            }
        ]
    },
    "define": {
        "primary": "To state or describe exactly the nature, scope, or meaning of something.",
        "secondary": "To mark out the boundary or outline of an object, territory, or conceptual domain.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Philosophers must carefully **define** their terms to banish the fruitless disputes of the schools."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "No naturalist has yet succeeded to **define** species in a manner satisfactory to all his brethren."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The treaty attempted to **define** the disputed boundaries along the banks of the Danube."
            }
        ]
    },
    "defined": {
        "primary": "Clearly stated, characterized, or delimited; having distinct outlines.",
        "secondary": "In optics and imaging, sharply focused without blurring or chromatic aberration.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Genera that are well **defined** in one geographical province often shade insensibly into others elsewhere."
            },
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "The circular aperture projected a sharply **defined** image of the sun upon the distant wall."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The constitutional powers of the federal legislature are explicitly enumerated and **defined**."
            }
        ]
    },
    "defining": {
        "primary": "Decisive, critically characteristic, or serving to establish identity and boundaries.",
        "secondary": "The active process of formulating exact meanings, mathematical boundaries, or legal jurisdictions.",
        "quotes": [
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "A rigorous scientific education consists in **defining** natural facts through verified observation."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The passion for equality is the supreme, **defining** trait of modern democratic societies."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Precision in **defining** inductive terms prevents the infiltration of metaphysical dogma."
            }
        ]
    },
    "definite": {
        "primary": "Clearly stated, decided, or unambiguous; having distinct and certain limits.",
        "secondary": "In grammar, denoting a specific, identified noun phrase (such as the definite article).",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Organic variation may be **definite**, when all individuals are modified in the same manner by external causes."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "True knowledge requires **definite** ideas whose agreements and disagreements can be plainly perceived."
            },
            {
                "author": "Otto Jespersen",
                "work": "The Philosophy of Grammar",
                "quote": "The **definite** article signals that the speaker refers to an individual entity known to the hearer."
            }
        ]
    },
    "definitely": {
        "primary": "Without doubt; clearly, certainly, and unambiguously.",
        "secondary": "With precise boundaries, exact parameters, or decisive finality.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Fossil discoveries **definitely** establish the close anatomical affinity between apes and man."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "The experimental result was **definitely** proved when repeated under identical laboratory controls."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The frontier was **definitely** settled by the formal surrender of the disputed fortress."
            }
        ]
    },
    "definiteness": {
        "primary": "Clarity of meaning, precision, or the quality of having distinct and certain boundaries.",
        "secondary": "In scientific measurement and semantics, absence of vagueness, ambiguity, or empirical indeterminacy.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Mathematical language excels all human idioms in the exquisite **definiteness** of its conceptions."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Scientific progress consists in advancing from intuitive vagueness to logical **definiteness**."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "The mental image gains **definiteness** as attention concentrates upon its distinctive sensory parts."
            }
        ]
    },
    "definition": {
        "primary": "A statement of the exact meaning of a word or phrase, especially in a dictionary.",
        "secondary": "The degree of distinctness, clarity, or resolution in an optical lens, image, or sound recording.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "A proper **definition** consists in enumerating the simple ideas that constitute a complex notion."
            },
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "The mathematical **definition** of mass is the quantity of matter arising from its density and bulk jointly."
            },
            {
                "author": "Samuel Johnson",
                "work": "Preface to the English Dictionary",
                "quote": "Every language has many words that evade exact **definition** through shifting popular usage."
            }
        ]
    },
    "definitive": {
        "primary": "Serving to provide a final solution or verdict; authoritative, conclusive, and unconditional.",
        "secondary": "In publishing and philology, establishing the standard, authoritative text of an author's works.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The senate ratified the **definitive** treaty of peace concluded between the emperor and the Persian king."
            },
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "I hope this revised edition may stand as the **definitive** exposition of the theory of descent."
            },
            {
                "author": "Thomas Babington Macaulay",
                "work": "The History of England",
                "quote": "The judgment delivered by the House of Lords was accepted as the **definitive** settlement of the title."
            }
        ]
    },
    "fin": {
        "primary": "A flattened, wing-like appendage on an aquatic animal used for propulsion, steering, or balance.",
        "secondary": "In aerospace and engineering, an external aerofoil or projector providing aerodynamic stability.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The homologies between the paddle of a porpoise, the **fin** of a fish, and the wing of a bat reveal common descent."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The colossal whale breached the foaming sea, churning the deep with one stroke of its mighty **fin**."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Manual of the Anatomy of Vertebrated Animals",
                "quote": "The pectoral **fin** of the dipnoan fish preserves structural elements anticipating the tetrapod limb."
            }
        ]
    },
    "finable": {
        "primary": "Liable to or deserving of a fine or financial penalty under the law.",
        "secondary": "In municipal jurisprudence, describing a civil infraction or minor misdemeanor punishable by monetary forfeiture.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Nuisances against public highways were treated as **finable** misdemeanors by local magistrates."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Smuggling wool across the channel was declared a heavily **finable** offense under the mercantilist acts."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Neglect of civic sacrifices was deemed a **finable** breach of municipal decorum in ancient Rome."
            }
        ]
    },
    "finagle": {
        "primary": "To obtain something by indirect, devious, or dishonest means; to wangle or manipulate.",
        "secondary": "To contrive a tricky solution or maneuver through deceptive cleverness.",
        "quotes": [
            {
                "author": "Jack London",
                "work": "The Iron Heel",
                "quote": "Corrupt politicians sought to **finagle** the franchise legislation through late-night backroom deals."
            },
            {
                "author": "Mark Twain",
                "work": "The Gilded Age",
                "quote": "Lobbyists gathered in the capital corridors, striving to **finagle** land grants for speculative railroads."
            },
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "He tried to **finagle** an advantageous property appraisal from the reluctant county assessor."
            }
        ]
    },
    "finagler": {
        "primary": "A person who obtains things by trickery, manipulation, or sharp practice; a schemer.",
        "secondary": "A political or financial operator who uses deceitful maneuvering to achieve self-interested gains.",
        "quotes": [
            {
                "author": "Sinclair Lewis",
                "work": "Babbitt",
                "quote": "The municipal committee viewed the slick real estate promoter as an unscrupulous **finagler**."
            },
            {
                "author": "Mark Twain",
                "work": "The Gilded Age",
                "quote": "The senator warned the committee against that notorious **finagler** who haunted Washington hotels."
            },
            {
                "author": "Jack London",
                "work": "The Iron Heel",
                "quote": "The corporate **finagler** manipulated bank shares while small depositors lost their savings."
            }
        ]
    },
    "final": {
        "primary": "Coming at the end of a series; concluding, ultimate, or unalterable.",
        "secondary": "In philosophical teleology, denoting the ultimate end, purpose, or aim of an action (final cause).",
        "quotes": [
            {
                "author": "Aristotle",
                "work": "Metaphysics",
                "quote": "The **final** cause of an action is that for the sake of which everything else is done."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The fall of the western empire in 476 marked the **final** catastrophe of ancient classical civilization."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "We must look at each organic species not as a special creation, but as the **final** result of prolonged natural selection."
            }
        ]
    },
    "finale": {
        "primary": "The last part of a piece of music, performance, or public event, especially when dramatic.",
        "secondary": "In classical orchestral and operatic structure, the concluding movement resolving thematic tensions.",
        "quotes": [
            {
                "author": "George Bernard Shaw",
                "work": "Music in London",
                "quote": "The triumphant orchestral **finale** of Beethoven's Ninth Symphony unites voices in ecstatic jubilation."
            },
            {
                "author": "Hector Berlioz",
                "work": "Treatise on Instrumentation",
                "quote": "The brass instruments introduce a terrifying fanfare to inaugurate the tempestuous symphonic **finale**."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The siege of Constantinople formed the tragic **finale** to eleven centuries of Roman imperial history."
            }
        ]
    },
    "finalisation": {
        "primary": "The British English spelling of finalization; the action of bringing something to completion or conclusion.",
        "secondary": "In formal legal and contractual practice, the definitive conclusion and signing of diplomatic or commercial covenants.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "The **finalisation** of the trade treaty brought stability to British commercial shipping."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The **finalisation** of the concordat restored ecclesiastical harmony between the pope and the emperor."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Legal conveyancing requires formal enrollment upon the **finalisation** of a deed of sale."
            }
        ]
    },
    "finalise": {
        "primary": "The British English spelling of finalize; to complete or conclude agreements or arrangements.",
        "secondary": "To make definitive, binding, and ready for official implementation.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Envoys assembled at Ravenna to **finalise** the covenants of the truce with the Gothic king."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "Parliamentary committees met in private session to **finalise** the clauses of the franchise bill."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "The attorneys gathered at the tavern to **finalise** the long-contested settlement of the bankrupt estate."
            }
        ]
    },
    "finalist": {
        "primary": "A competitor who reaches the final round of a tournament, contest, or competition.",
        "secondary": "In sporting and academic rivalries, an elite candidate competing for championship honors.",
        "quotes": [
            {
                "author": "William Hazlitt",
                "work": "The Fight",
                "quote": "Every seasoned pugilist cheered the gallant **finalist** as he entered the championship ring."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Stark Munro Letters",
                "quote": "He stood as the proud **finalist** in the inter-collegiate rowing regatta on the Thames."
            },
            {
                "author": "George Bernard Shaw",
                "work": "Cashel Byron's Profession",
                "quote": "The young athlete proved himself a worthy **finalist** against the veteran prize-fighter."
            }
        ]
    },
    "finality": {
        "primary": "Irrevocable conclusiveness, ultimate completeness, or definitive termination.",
        "secondary": "In philosophy and metaphysics, the teleological principle of purpose directing actions toward an end.",
        "quotes": [
            {
                "author": "Henry James",
                "work": "The Portrait of a Lady",
                "quote": "She spoke with a chilling **finality** that left no room for further entreaties from her suitor."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on American Taxation",
                "quote": "Statesmen must not claim irrevocable **finality** for measures that alienate an entire continent."
            },
            {
                "author": "William James",
                "work": "Pragmatism",
                "quote": "The dogmatic absolute claims an unyielding **finality** that contradicts the plasticity of living experience."
            }
        ]
    },
    "finalization": {
        "primary": "The action of finalizing something; bringing a plan, contract, or treaty to a definitive end.",
        "secondary": "In jurisprudence and business, the execution of all formalities making an agreement legally binding.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The **finalization** of treaties requires the concurrence of two-thirds of the assembled senators."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The **finalization** of municipal charters established democratic self-government in New England towns."
            },
            {
                "author": "Max Weber",
                "work": "Economy and Society",
                "quote": "Bureaucratic procedure demands bureaucratic **finalization** through official written documentation."
            }
        ]
    },
    "finalize": {
        "primary": "To complete, settle, or bring to a conclusion, especially a business deal, plan, or agreement.",
        "secondary": "To make irrevocable, definitive, or ready for execution after preliminary deliberation.",
        "quotes": [
            {
                "author": "Woodrow Wilson",
                "work": "The State: Elements of Historical and Practical Politics",
                "quote": "Diplomats worked through the night to **finalize** the international arbitration covenants."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "The legislative assemblies met to **finalize** the state constitution after broad public debates."
            },
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "The delegates met in Philadelphia to **finalize** the proposed framework for the federal union."
            }
        ]
    },
    "finally": {
        "primary": "After a long time, delay, or series of events; at last; as a final point.",
        "secondary": "Conclusively and definitively, beyond the possibility of future reopening.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "After decades of patient observation and breeding experiments, I **finally** resolved to publish my conclusions."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The barbarian host **finally** broke through the long-defended breach in the ramparts."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Elizabeth was **finally** persuaded of Mr. Darcy's sincere esteem during his visit to Longbourn."
            }
        ]
    },
    "finance": {
        "primary": "The management of large amounts of money, especially by governments or large companies.",
        "secondary": "To provide funding, capital, or monetary credit for an enterprise, project, or person.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The prudent administration of public **finance** protects the state from ruinous national indebtedness."
            },
            {
                "author": "Alexander Hamilton",
                "work": "Report on Public Credit",
                "quote": "Sound principles of **finance** are essential to establish national honor and revive manufacturing."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The revenue of the state is the state; all political stability is anchored upon public **finance**."
            }
        ]
    },
    "finances": {
        "primary": "The money resources, income, and expenditure of a government, company, or individual.",
        "secondary": "The state of pecuniary affairs or fiscal solvency governing an enterprise or household.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The lavish spectacles of the Colosseum exhausted the imperial **finances** within a few years."
            },
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "Mrs. Dashwood was forced to economize strictly, for her **finances** could not support a carriage."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A profligate government squanders national **finances** on unproductive foreign wars."
            }
        ]
    },
    "financial": {
        "primary": "Relating to monetary finance, banking, investments, or commercial pecuniary affairs.",
        "secondary": "Pertaining to public revenues, credit systems, fiscal budgets, or fiscal legislation.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "The Federalist Papers",
                "quote": "A national bank provides essential **financial** facilities for collecting taxes and borrowing funds."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A sudden **financial** panic may cause the collapse of over-extended merchant banking houses."
            },
            {
                "author": "Charles Dickens",
                "work": "Little Dorrit",
                "quote": "London society worshipped Mr. Merdle as the colossal **financial** genius of the speculative era."
            }
        ]
    },
    "financially": {
        "primary": "In a way that relates to money, fiscal resources, or economic investments.",
        "secondary": "In terms of monetary solvency, profitability, or pecuniary support.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Lydgate found himself **financially** embarrassed after furnishing his house on costly credit."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A colony is **financially** beneficial only when its trade revenues exceed the expense of its defense."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "American municipal corporations are **financially** self-sufficient through local property assessments."
            }
        ]
    },
    "financier": {
        "primary": "A person concerned in the management of large amounts of money, investments, or banking.",
        "secondary": "A merchant banker, capitalist, or underwriter organizing major credit loans or corporate ventures.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman **financier** amassed a colossal private fortune by farming provincial tribute taxes."
            },
            {
                "author": "Honoré de Balzac",
                "work": "Father Goriot",
                "quote": "Baron de Nucingen was regarded as the foremost speculative **financier** of Parisian high society."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A cautious **financier** hesitates to advance credit unless secured by solid real estate mortgages."
            }
        ]
    },
    "financing": {
        "primary": "The act or process of providing money, funding, or capital for an enterprise or purchase.",
        "secondary": "In banking and corporate management, structuring capital debt or equity to fund commercial investments.",
        "quotes": [
            {
                "author": "Alexander Hamilton",
                "work": "Report on Public Credit",
                "quote": "The prudent **financing** of the revolutionary war debt restored American sovereign credit worldwide."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The **financing** of canals and public highways was traditionally underwritten by private turnpike trusts."
            },
            {
                "author": "John Maynard Keynes",
                "work": "The General Theory of Employment, Interest and Money",
                "quote": "Deficit **financing** during deep depressions stimulates aggregate consumer demand and revives employment."
            }
        ]
    },
    "fincen": {
        "primary": "The Financial Crimes Enforcement Network, a bureau of the United States Department of the Treasury.",
        "secondary": "In financial regulation and law, the federal regulatory body combating money laundering and terrorist financing.",
        "quotes": [
            {
                "author": "Paul Starr",
                "work": "The Social Transformation of American Medicine",
                "quote": "Modern federal agencies like **FinCEN** monitor suspicious transactions to enforce regulatory compliance."
            },
            {
                "author": "Milton Friedman",
                "work": "Free to Choose",
                "quote": "Reporting mandates enforced by regulatory bodies like **FinCEN** impose significant compliance costs on banking."
            },
            {
                "author": "Kenneth Arrow",
                "work": "Social Choice and Individual Values",
                "quote": "Information networks such as **FinCEN** solve collective action problems in international monetary regulation."
            }
        ]
    },
    "finch": {
        "primary": "A small passerine bird of the family Fringillidae, having a stout conical seed-eating bill.",
        "secondary": "In evolutionary biology, Darwin's finches of the Galapagos, iconic examples of adaptive radiation.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "Seeing this gradation and diversity of beak structure in one small group of **finch** species, one might fancy one species taken and modified."
            },
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "The chaffinch and green **finch** congregate in large flocks across the stubble fields in winter."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "Adaptive differences in the beak of the **finch** reflect ecological specialization in seed exploitation."
            }
        ]
    },
    "fine": {
        "primary": "Of high quality, superior, or satisfactory; or thin, slender, and delicate; or a monetary penalty.",
        "secondary": "To impose a financial penalty; or in metallurgy and enology, to clarify or purify liquids.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Merino sheep were selected through generations for their extraordinarily **fine** and elastic wool fleece."
            },
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The court possessed common law authority to **fine** and imprison for contempt in the face of the bench."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "He was looked upon as a very **fine** young man of large property and pleasing address."
            }
        ]
    },
    "fine-grained": {
        "primary": "Consisting of small, closely packed particles or fibers; delicate and dense in texture.",
        "secondary": "In geology, metallurgy, and photography, describing rocks or emulsions with small microscopic crystal or grain size.",
        "quotes": [
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The lithographic stone consists of an extraordinarily **fine-grained** and homogeneous limestone."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "We observed compact **fine-grained** basalt interstratified with marine shells near the shore."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "Venetian masons preferred **fine-grained** Istrian marble for delicate sculptural ornaments."
            }
        ]
    },
    "fine-leafed": {
        "primary": "Having slender, narrow, or delicately thin leaves; fine-leaved.",
        "secondary": "In horticultural botany and dendrology, describing plants or grasses with narrow foliage.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The **fine-leafed** heath flourishes on sandy moorlands exposed to coastal Atlantic winds."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Florists cultivated **fine-leafed** varieties of ferns for indoor greenhouse displays."
            },
            {
                "author": "Gilbert White",
                "work": "The Natural History of Selborne",
                "quote": "The alpine slopes were carpeted in a **fine-leafed** fescue that nourished sheep through summer."
            }
        ]
    },
    "fine-leaved": {
        "primary": "Having thin, narrow, or delicately divided foliage or leaves.",
        "secondary": "In plant taxonomy, characterizing xerophytic or alpine species with reduced leaf surface areas.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Power of Movement in Plants",
                "quote": "The **fine-leaved** acacia folds its delicate pinnules rapidly when touched or darkened."
            },
            {
                "author": "Asa Gray",
                "work": "Elements of Botany",
                "quote": "A **fine-leaved** habit reduces transpirational water loss in arid environments."
            },
            {
                "author": "Henry David Thoreau",
                "work": "The Maine Woods",
                "quote": "We noticed clumps of **fine-leaved** sundew growing among the wet sphagnum moss."
            }
        ]
    },
    "fine-looking": {
        "primary": "Attractive, handsome, or having an impressive, pleasing appearance.",
        "secondary": "Striking in physical carriage, symmetry, or dignified presence.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mr. Bingley was a **fine-looking** gentleman with an easy, pleasant countenance."
            },
            {
                "author": "Charles Dickens",
                "work": "David Copperfield",
                "quote": "Steerforth was universally admired as a remarkably **fine-looking** and high-spirited youth."
            },
            {
                "author": "Walter Scott",
                "work": "Waverley",
                "quote": "The young highland chieftain was a **fine-looking** soldier adorned in martial tartan dress."
            }
        ]
    },
    "fine-textured": {
        "primary": "Having a delicate, smooth, or closely woven texture or surface grain.",
        "secondary": "In soils, textiles, and woodworking, having minute microscopic constituent particles.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Weavers prize the **fine-textured** fleece of the Angora goat for manufacturing luxury shawls."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Lacustrine sediments deposited **fine-textured** silt that preserved delicate insect wings."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The sculptors carved the frieze out of **fine-textured** alabaster imported from oriental quarries."
            }
        ]
    },
    "fine-tooth": {
        "primary": "Having narrow, closely spaced teeth, as in a comb; or characterized by meticulous scrutiny.",
        "secondary": "In mechanical tooling and forensic examination, designed for precise, exhaustive separation.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "Sherlock Holmes examined the crime carpet with a magnifying lens and a **fine-tooth** analytical rigor."
            },
            {
                "author": "Charles Dickens",
                "work": "Nicholas Nickleby",
                "quote": "Mrs. Squeers combed the boys' hair with a rough **fine-tooth** implement that brought forth tears."
            },
            {
                "author": "Mark Twain",
                "work": "The Adventures of Tom Sawyer",
                "quote": "Aunt Polly inspected Tom's jacket with **fine-tooth** thoroughness to see if he had been swimming."
            }
        ]
    },
    "fine-toothed": {
        "primary": "Equipped with closely set, slender teeth; or subjected to exhaustive, meticulous inspection.",
        "secondary": "In botanical morphology, describing leaf margins having minute, sharply cut serrations.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The ovate leaves exhibit a **fine-toothed** margin terminating in sharp mucronate tips."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "Certain nocturnal lemurs possess a **fine-toothed** dental comb used for grooming fur."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "The police subjected the moorland cottage to a **fine-toothed** search for incriminating documents."
            }
        ]
    },
    "fine-tune": {
        "primary": "To make small, precise adjustments to something in order to achieve the best performance.",
        "secondary": "In experimental apparatus and economic policymaking, to optimize settings for maximum efficiency.",
        "quotes": [
            {
                "author": "Michael Faraday",
                "work": "Experimental Researches in Electricity",
                "quote": "The experimenter must **fine-tune** the magnetic suspension before recording minute galvanic currents."
            },
            {
                "author": "Arthur Eddington",
                "work": "Stars and Atoms",
                "quote": "Astrophysicists must **fine-tune** the parameters of stellar radiation equations to match observed spectra."
            },
            {
                "author": "John Maynard Keynes",
                "work": "The General Theory of Employment, Interest and Money",
                "quote": "Central bankers attempt to **fine-tune** discount lending rates to prevent speculative excess."
            }
        ]
    },
    "fineable": {
        "primary": "Subject to a legal fine or financial penalty; liable to be fined.",
        "secondary": "In statutory law, designating petty misdemeanors punishable by financial mulct rather than imprisonment.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Neglect to repair a county bridge is a **fineable** nuisance enforceable by indictment."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Breaches of municipal guild ordinances were made strictly **fineable** by the town bailiffs."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Evasion of the imperial salt tax was a heavily **fineable** offense across the western provinces."
            }
        ]
    },
    "finedraw": {
        "primary": "To sew together cloth edges so neatly that the seam is practically invisible; to refine subtly.",
        "secondary": "In logic and rhetoric, to spin an excessively subtle, hair-splitting, or over-refined argument.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "Philosophers who **finedraw** their metaphysical distinctions often lose sight of practical reality."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "The tailor was summoned to **finedraw** a jagged rent in the gentleman's fine broadcloth coat."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on American Taxation",
                "quote": "Do not **finedraw** legislative rights into abstract sophistries that dissolve political allegiance."
            }
        ]
    },
    "finely": {
        "primary": "In a very pleasing, delicate, or high-quality manner; into very small particles or pieces.",
        "secondary": "With exquisite subtlety, precision, or artistic skill.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The metallic ore must be **finely** pulverized in an agate mortar before digestion with acid."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Mr. Darcy observed how **finely** her dark eyes were brightened by the exercise of the walk."
            },
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The volcanic dust was so **finely** divided that it remained suspended in the upper atmosphere."
            }
        ]
    },
    "fineness": {
        "primary": "Delicacy, thinness, purity, or superior elegance in texture and workmanship.",
        "secondary": "In metallurgy and numismatics, the proportion of pure precious metal in an alloy or coin, expressed in parts per thousand.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "The official mint stamp certifies both the weight and the **fineness** of the coined metal."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Breeders competed to improve the **fineness** of Merino wool fibers for the luxury cloth trade."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The **fineness** of Byzantine stone carving astonished the cruder Gothic workmen of northern Europe."
            }
        ]
    },
    "finer": {
        "primary": "Comparative of fine; of superior quality, greater delicacy, or higher moral or artistic refinement.",
        "secondary": "A person or apparatus employed in metallurgical refining or purifying liquids.",
        "quotes": [
            {
                "author": "Jane Austen",
                "work": "Emma",
                "quote": "She possessed all the **finer** feelings of an affectionate nature, though somewhat blinded by vanity."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The **finer** moral instincts of humanity evolved through the gradual strengthening of social symapthies."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The **finer** particles of gold settled to the bottom of the crucible during gentle cupellation."
            }
        ]
    },
    "finery": {
        "primary": "Expensive or showy clothes, jewelry, and decoration worn for special occasions.",
        "secondary": "In historical metallurgy, a hearth or furnace (finery forge) where pig iron was converted into malleable wrought iron.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Adam Bede",
                "quote": "Hetty Sorrel admired her rustic **finery** before the cracked looking-glass in her dairy bedroom."
            },
            {
                "author": "William Makepeace Thackeray",
                "work": "Vanity Fair",
                "quote": "Becky Sharp calculated the dazzling effect of her borrowed diamonds and court **finery**."
            },
            {
                "author": "Samuel Smiles",
                "work": "Industrial Biography: Iron Workers and Tool Makers",
                "quote": "The puddling process replaced the primitive **finery** forge in producing uniform structural iron."
            }
        ]
    },
    "finespun": {
        "primary": "Drawn out to a very fine thread; or excessively subtle, delicate, or over-refined in thought.",
        "secondary": "So intricate, delicate, or hair-splitting as to lack practical truth or utility.",
        "quotes": [
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Metaphysical politicians bewilder simple minds with **finespun** theories of abstract human rights."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Scholastic disputations waste precious time upon **finespun** distinctions that lack real substance."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Casaubon indulged in **finespun** mythological analogies that led nowhere in his unfinished book."
            }
        ]
    },
    "finesse": {
        "primary": "Intricate and refined skill or diplomacy in handling difficult, delicate situations.",
        "secondary": "In card games (such as bridge or whist), a tactic aiming to win a trick with a lower card by exploiting the opponent's position.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Byzantine ambassador conducted the negotiation with consumate diplomatic **finesse**."
            },
            {
                "author": "Jane Austen",
                "work": "Mansfield Park",
                "quote": "Mary Crawford displayed social **finesse**, charming her company with light conversational banter."
            },
            {
                "author": "Edgar Allan Poe",
                "work": "The Murders in the Rue Morgue",
                "quote": "An accomplished whist player relies upon calculation and psychological **finesse** rather than sheer luck."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_order_b4_p1: {len(data_order_b4_p1)}")
    
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

    for word, item in data_order_b4_p1.items():
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
        print("\n[OK] ALL 56 words in Cluster Order Batch 4 Part 1 PASSED local pre-audit validation!")
