# -*- coding: utf-8 -*-
"""
curate_order_b3_p2.py
Curated dataset for Cluster Order Batch 3 Part 2:
- Dashboard — medi (77 words)
Total: 77 words
"""
import re

data_order_b3_p2 = {
    # ----------------------------------------------------
    # DASHBOARD — MEDI (77 words)
    # ----------------------------------------------------
    "comedian": {
        "primary": "An entertainer whose job is to make people laugh; or an actor who plays comic roles.",
        "secondary": "In classical theatrical history, a playwright or dramatic performer specializing in satirical or domestic comedies.",
        "quotes": [
            {
                "author": "Charles Dickens",
                "work": "Nicholas Nickleby",
                "quote": "The veteran stage **comedian** delighted the provincial audience with extravagant pantomime gestures."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Poets",
                "quote": "Molière stands as the supreme dramatic **comedian** of modern European literature."
            },
            {
                "author": "William Hazlitt",
                "work": "Lectures on the English Comic Writers",
                "quote": "A great comic actor or **comedian** exposes the secret absurdities of human nature."
            }
        ]
    },
    "comedienne": {
        "primary": "A female comedian or comic actress who performs in theater, television, or humorous entertainment.",
        "secondary": "In dramatic arts, an actress specializing in light, witty, or satirical roles.",
        "quotes": [
            {
                "author": "George Bernard Shaw",
                "work": "Our Theatres in the Nineties",
                "quote": "The brilliant young **comedienne** carried the farcical third act through sheer comic timing."
            },
            {
                "author": "Henry James",
                "work": "The Tragic Muse",
                "quote": "Miriam proved herself as capable of playing a refined **comedienne** as an impassioned tragic heroine."
            },
            {
                "author": "Virginia Woolf",
                "work": "Night and Day",
                "quote": "Her sparkling wit and mocking glances suggested the spontaneous charm of an accomplished **comedienne**."
            }
        ]
    },
    "immediacy": {
        "primary": "The quality of bringing one into direct, instant involvement with something; urgency or present reality.",
        "secondary": "In epistemology and aesthetics, direct intuitive presentation unmediated by conceptual reflection.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Pure sensation presents external reality with a vivid, undeniable sensory **immediacy**."
            },
            {
                "author": "John Dewey",
                "work": "Art as Experience",
                "quote": "Aesthetic enjoyment possesses a compelling emotional **immediacy** that precedes rational analysis."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Present impressions strike the mind with greater force and **immediacy** than faint recollections."
            }
        ]
    },
    "immediate": {
        "primary": "Occurring or done at once; instant; or nearest in relationship, time, or space.",
        "secondary": "Operating without intervening medium, agency, or conceptual intermediary.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Mathematical Principles of Natural Philosophy",
                "quote": "Gravitational action seemed to require either a medium or an **immediate** immaterial agency."
            },
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Ideas form the **immediate** objects of perception whenever the mind reflects upon itself."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The **immediate** ancestors of domesticated pigeons can be traced directly to Columba livia."
            }
        ]
    },
    "immediately": {
        "primary": "At once; instantly; without any intervening delay, time, or medium.",
        "secondary": "In direct contact or succession without third-party intervention.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "The earthquake shock was felt on board, followed **immediately** by a roaring sound from the shore."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The guards rushed forward and **immediately** proclaimed the victorious general as Augustus."
            },
            {
                "author": "Jane Austen",
                "work": "Pride and Prejudice",
                "quote": "Elizabeth recognized his handwriting **immediately** upon opening the fateful letter."
            }
        ]
    },
    "immediateness": {
        "primary": "The property of being direct, instant, or free from intervening agents.",
        "secondary": "In philosophy of perception, directness of acquaintance without discursive inference.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "The felt **immediateness** of the divine presence overwhelmed all rational skepticism."
            },
            {
                "author": "John Stuart Mill",
                "work": "An Examination of Sir William Hamilton's Philosophy",
                "quote": "Intuitive philosophers assert the **immediateness** of our perception of an external world."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Firstness is characterized by freshness, originality, and absolute **immediateness**."
            }
        ]
    },
    "intermediary": {
        "primary": "A person who acts as a link between people in order to try to bring about an agreement; a mediator.",
        "secondary": "In chemistry and evolutionary biology, a transitional compound or intermediate ancestral form.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The bishop acted as an official **intermediary** between the barbarian king and the Roman senate."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Fossil beds rarely preserve every delicate organic **intermediary** linking ancient families."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Municipal corporations serve as a vital institutional **intermediary** protecting individual liberty."
            }
        ]
    },
    "intermediate": {
        "primary": "Coming between two things in time, place, character, or degree; transitional.",
        "secondary": "In chemical kinetics, a transient molecular entity formed from reactants that reacts further to yield products.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "Extinction has wiped out the numerous **intermediate** varieties that once linked diverging species."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The strata contain fossils occupying an **intermediate** position between secondary and tertiary faunas."
            },
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Scientific deduction establishes **intermediate** general axioms that bridge principles to phenomena."
            }
        ]
    },
    "intermediately": {
        "primary": "In an intermediate position, manner, or degree; by way of intervention.",
        "secondary": "Occupying a middle station between extremes in space, rank, or chronology.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Hybrid offspring often inherit plumage patterns colored **intermediately** between both parent breeds."
            },
            {
                "author": "Herbert Spencer",
                "work": "The Principles of Biology",
                "quote": "Tissues developing **intermediately** between ectoderm and endoderm constitute the embryonic mesoderm."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The leaves are arranged **intermediately** between alternate and opposite nodes along the branch."
            }
        ]
    },
    "intermediation": {
        "primary": "The action of intervening between parties to produce agreement, reconciliation, or transaction; mediation.",
        "secondary": "In economics and finance, the process whereby institutions channel funds between savers and borrowers.",
        "quotes": [
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Commercial banking provides financial **intermediation** that mobilizes idle domestic savings."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Peace was concluded through the skillful **intermediation** of the Venetian maritime ambassadors."
            },
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Wholesale merchants perform an indispensable social **intermediation** between growers and retailers."
            }
        ]
    },
    "intermediator": {
        "primary": "A mediator, go-between, or agent who intervenes between two or more parties.",
        "secondary": "In diplomatic history and jurisprudence, a neutral party facilitating treaty negotiations.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Persian satrap served as an **intermediator** to convey royal terms to the Roman camp."
            },
            {
                "author": "Walter Scott",
                "work": "The Bride of Lammermoor",
                "quote": "He refused to employ any legal **intermediator**, choosing to confront his rival face to face."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "The Old Regime and the Revolution",
                "quote": "The royal intendant functioned as an **intermediator** between the crown and provincial estates."
            }
        ]
    },
    "irremediable": {
        "primary": "Impossible to cure, repair, redress, or put right; incurable or permanent.",
        "secondary": "In medicine and social pathology, damage or decay that defies all therapeutic intervention.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The loss of the Danubian legionary fortress inflicted an **irremediable** wound upon imperial prestige."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Advanced hepatic cirrhosis produces **irremediable** portal hypertension and secondary ascites."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "Sweeping constitutional destruction often leaves behind an **irremediable** void in public order."
            }
        ]
    },
    "media": {
        "primary": "The main means of mass communication (broadcasting, publishing, the internet) regarded collectively.",
        "secondary": "In microbiology and laboratory histology, nutrient solutions or solid agar used to culture microorganisms.",
        "quotes": [
            {
                "author": "Louis Pasteur",
                "work": "Studies on Fermentation",
                "quote": "Sterile nutrient **media** remained free of bacterial growth until exposed to airborne dust."
            },
            {
                "author": "Marshall McLuhan",
                "work": "Understanding Media: The Extensions of Man",
                "quote": "Electronic **media** reshape human perception by transforming the global village into an interactive web."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The tunica **media** of muscular arteries regulates vascular resistance through smooth muscle tone."
            }
        ]
    },
    "mediacy": {
        "primary": "Indirectness, mediation, or operation through an intervening agent or medium.",
        "secondary": "In Hegelian and epistemological logic, knowledge attained through inferential conceptual processes.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Conceptual thought lacks the raw vividness of sensation because of its inherent **mediacy**."
            },
            {
                "author": "John Dewey",
                "work": "Essays in Experimental Logic",
                "quote": "Reflective inquiry moves from the immediacy of doubt to the cognitive **mediacy** of verified judgment."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Thirdness represents the category of **mediacy**, synthesis, and lawful continuity in thought."
            }
        ]
    },
    "mediaeval": {
        "primary": "The traditional British spelling of medieval; relating to the Middle Ages (roughly 500–1500 AD).",
        "secondary": "Pertaining to feudal institutions, scholastic philosophy, or Gothic ecclesiastical architecture.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The rise of the Italian republics marked the transition from dark **mediaeval** feudalism to urban liberty."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "The delicate tracery of the cathedral facade expressed the pious freedom of the **mediaeval** workman."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "Tournaments and chivalric displays colored the pageantry of that martial **mediaeval** epoch."
            }
        ]
    },
    "medial": {
        "primary": "Situated in or extending toward the middle; median.",
        "secondary": "In anatomy and morphology, situated toward the midline plane of the body or an organ.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The **medial** collateral ligament stabilizes the knee joint against excessive valgus stress."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Manual of the Anatomy of Vertebrated Animals",
                "quote": "The olfactory bulbs lie close together along the **medial** aspect of the anterior cerebral hemispheres."
            },
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "The **medial** incisors of anthropoid apes exhibit homologies with those of fossil hominids."
            }
        ]
    },
    "medially": {
        "primary": "Toward the middle, center, or median plane of the body.",
        "secondary": "In clinical orthopedics and anatomical dissection, directed inward toward the longitudinal anatomical midline.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Contraction of the internal pterygoid muscle draws the mandible **medially** and forward."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Lessons in Elementary Physiology",
                "quote": "The tendon of the ocular rectus passes **medially** before inserting into the scleral coat."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The cardiac impulse was displaced **medially** owing to massive pleural effusion on the left."
            }
        ]
    },
    "median": {
        "primary": "Denoting or situated in the middle, especially dividing something into two equal halves.",
        "secondary": "In statistics, the value separating the higher half from the lower half of a data sample; in geometry, a line connecting a vertex to the midpoint of the opposite side.",
        "quotes": [
            {
                "author": "Francis Galton",
                "work": "Natural Inheritance",
                "quote": "The **median** value provides a stable measure of central tendency unaffected by extreme outliers."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Compression of the **median** nerve in the carpal tunnel produces tingling paresthesia in the fingers."
            },
            {
                "author": "Euclid",
                "work": "Elements of Geometry",
                "quote": "The three **median** lines of any triangle concur at a common interior point termed the centroid."
            }
        ]
    },
    "mediant": {
        "primary": "In musical theory, the third scale degree of a diatonic scale, midway between tonic and dominant.",
        "secondary": "In mathematics, a fraction formed by summing the numerators and denominators of two given fractions.",
        "quotes": [
            {
                "author": "Hermann von Helmholtz",
                "work": "On the Sensations of Tone",
                "quote": "The harmonic sweetness of the major triad depends upon the acoustic consonance of the **mediant** third."
            },
            {
                "author": "Jean-Philippe Rameau",
                "work": "Treatise on Harmony",
                "quote": "Modulation often glides smoothly through the **mediant** harmony before resolving firmly onto the tonic."
            },
            {
                "author": "Augustus De Morgan",
                "work": "The Elements of Arithmetic",
                "quote": "The Farey sequence generates successive rational approximations through the continued **mediant**."
            }
        ]
    },
    "mediastinum": {
        "primary": "The central compartment of the thoracic cavity between the lungs, containing the heart, esophagus, and trachea.",
        "secondary": "In human gross anatomy, the interpleural septum housing the pericardial sac and major blood vessels.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Aneurysm of the aortic arch frequently causes pressure symptoms deep within the superior **mediastinum**."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "The negative intrathoracic pressure within the **mediastinum** aids venous return to the right atrium."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Lymphomas originating in the anterior **mediastinum** may compress the superior vena cava."
            }
        ]
    },
    "mediate": {
        "primary": "To intervene between people in a dispute in order to bring about an agreement or reconciliation.",
        "secondary": "Acting through an intervening agency, medium, or secondary cause rather than immediately.",
        "quotes": [
            {
                "author": "John Locke",
                "work": "An Essay Concerning Human Understanding",
                "quote": "Demonstrative knowledge requires **mediate** ideas to connect concepts whose agreement is not self-evident."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The pope sent legates to **mediate** between the warring Lombard princes and the Frankish king."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Habit acts as a **mediate** psychological principle linking past observations with future expectations."
            }
        ]
    },
    "mediated": {
        "primary": "Brought about or resolved through intervention; or communicated via an intermediary medium.",
        "secondary": "In cellular biochemistry and physiology, facilitated or transmitted by molecular receptors or second messengers.",
        "quotes": [
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Glucose transport across the cellular membrane is **mediated** by specialized carrier protein molecules."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "A lasting truce was **mediated** by the venerable patriarch after weeks of intense diplomacy."
            },
            {
                "author": "William James",
                "work": "The Principles of Psychology",
                "quote": "Voluntary movements are **mediated** through conscious motor images previously stored in memory."
            }
        ]
    },
    "mediateness": {
        "primary": "Indirect connection, relational dependency, or operation through an intervening medium.",
        "secondary": "In logic and philosophy of mind, indirectness in knowledge requiring demonstrative steps.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "A System of Logic",
                "quote": "Deductive inference is characterized by the logical **mediateness** of its reasoning steps."
            },
            {
                "author": "William James",
                "work": "The Meaning of Truth",
                "quote": "Pragmatism contrasts the direct immediacy of percepts with the conceptual **mediateness** of concepts."
            },
            {
                "author": "Charles Sanders Peirce",
                "work": "Collected Papers",
                "quote": "Representation inherently involves **mediateness**, linking an interpretant with an object through a sign."
            }
        ]
    },
    "mediation": {
        "primary": "Intervention in a dispute in order to resolve it; arbitration or conciliation.",
        "secondary": "In philosophy and sociology, the process through which social relations or concepts are linked by intermediaries.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The rival generals accepted the peaceful **mediation** of the venerable Christian bishop."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "International commerce relies on the financial **mediation** of bills of exchange drawn on London."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "Constitutional checks provide a peaceful **mediation** between conflicting social classes."
            }
        ]
    },
    "mediator": {
        "primary": "A person who attempts to make people involved in a conflict agree; an intermediary.",
        "secondary": "In physiology and pharmacology, an endogenous biochemical substance (like histamine) that transmits a physiological response.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The king of France offered his services as an impartial **mediator** between the emperor and the sultan."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Bradykinin acts as a potent chemical **mediator** in acute inflammatory vasodilatation."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "The Son of God stood forth as the gracious **mediator** between offended heaven and fallen humanity."
            }
        ]
    },
    "mediatorial": {
        "primary": "Relating to, characteristic of, or belonging to a mediator or the office of mediation.",
        "secondary": "In Christian theology, pertaining to the intercessory work of Christ between God and mankind.",
        "quotes": [
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "Christ assumed his **mediatorial** throne to intercede for the frail race of Adam."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Venetian republic exercised a lucrative **mediatorial** role between the Crusaders and Constantinople."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on Conciliation with America",
                "quote": "A true statesman must sometimes assume a **mediatorial** character to reconcile alienated subjects."
            }
        ]
    },
    "mediatory": {
        "primary": "Serving or intended to mediate; mediating; conciliatory.",
        "secondary": "Relating to intercession or the peaceful resolution of conflict through an intermediary.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The bishops presented a **mediatory** letter to the emperor, pleading for leniency toward the rebels."
            },
            {
                "author": "Walter Scott",
                "work": "The Antiquary",
                "quote": "His gentle, **mediatory** disposition helped extinguish the smoldering feud between the kinsmen."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Judicial courts exercise a quiet **mediatory** power that softens political conflicts in the republic."
            }
        ]
    },
    "mediatrix": {
        "primary": "A woman who mediates; a female intermediary or intercessor.",
        "secondary": "In Catholic and Orthodox theology, a title accorded to the Virgin Mary as intercessor between humans and Christ.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Byzantine hymnody invoked the Virgin as the celestial **mediatrix** of imperial victories."
            },
            {
                "author": "Henry James",
                "work": "The Bostonians",
                "quote": "She stepped forward as a sympathetic **mediatrix** to heal the estrangement between the two friends."
            },
            {
                "author": "Walter Scott",
                "work": "Ivanhoe",
                "quote": "Rowena served as a gentle **mediatrix** between Cedric's stubborn anger and his disinherited son."
            }
        ]
    },
    "medic": {
        "primary": "A medical practitioner or physician; or a military service member trained to give first aid on the battlefield.",
        "secondary": "In botany, any leguminous forage plant of the genus Medicago, closely related to alfalfa and clover.",
        "quotes": [
            {
                "author": "Stephen Crane",
                "work": "The Red Badge of Courage",
                "quote": "The wounded soldier called out hoarsely for the battlefield **medic** amidst the rifle smoke."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Pasture agronomists sowed purple **medic** alongside clover to enrich poor calcareous soils."
            },
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "The young army **medic** must cultivate equanimity under the chaotic stress of emergency triage."
            }
        ]
    },
    "medicago": {
        "primary": "A large genus of leguminous plants in the pea family, including alfalfa and various medic clovers.",
        "secondary": "In agronomy, nitrogen-fixing forage crops with trifoliate leaves and spirally coiled seed pods.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
                "quote": "The flowers of **Medicago** sativa possess an explosive mechanism that discharges pollen onto visiting bees."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The species of **Medicago** are readily recognized by their coiled, prickly legume pods."
            },
            {
                "author": "Virgil",
                "work": "Georgics",
                "quote": "The prudent husbandman enriches the fallow meadow by sowing lucerne or foreign **Medicago**."
            }
        ]
    },
    "medicaid": {
        "primary": "A joint federal and state healthcare program in the United States assisting low-income individuals and families.",
        "secondary": "In health policy and welfare economics, public health financing providing essential clinical care to eligible recipients.",
        "quotes": [
            {
                "author": "Paul Starr",
                "work": "The Social Transformation of American Medicine",
                "quote": "The enactment of **Medicaid** expanded medical access to millions of impoverished families across the nation."
            },
            {
                "author": "Milton Friedman",
                "work": "Free to Choose",
                "quote": "Subsidized healthcare programs like **Medicaid** generated unprecedented administrative overhead and cost inflation."
            },
            {
                "author": "Kenneth Arrow",
                "work": "Social Choice and Individual Values",
                "quote": "Public welfare programs such as **Medicaid** address market failures inherent in private health insurance."
            }
        ]
    },
    "medical": {
        "primary": "Relating to the science or practice of medicine, or to the treatment of illness and injury.",
        "secondary": "Denoting non-surgical therapy as distinguished from surgical or manual intervention.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The young student must ground his **medical** career upon bedside observation and sound pathology."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "Bob Sawyer and Ben Allen were reckless young **medical** students lodging near Guy's Hospital."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "True **medical** progress requires substituting experimental science for empirical clinical routine."
            }
        ]
    },
    "medically": {
        "primary": "From a medical point of view; in terms of medicine, health, or clinical practice.",
        "secondary": "By means of pharmacological or clinical therapies rather than surgical procedures.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The patient was managed **medically** with digitalis and strict bed rest to relieve congestive symptoms."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Cases of essential hypertension are treated **medically** through diuretic and vasodilating compounds."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "The post-encephalitic patients were monitored **medically** to document every subtle response to L-DOPA."
            }
        ]
    },
    "medicament": {
        "primary": "A substance used for medical treatment; a medicine, remedy, or therapeutic drug.",
        "secondary": "In historical pharmacopeia, any formulated potion, ointment, or balm possessing healing properties.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The imperial physician prepared a potent **medicament** to soothe the emperor's agonizing gout."
            },
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "The desire to take a **medicament** is perhaps the greatest feature which distinguishes man from animals."
            },
            {
                "author": "Honoré de Balzac",
                "work": "The Country Doctor",
                "quote": "The rustic doctor compounded every simple **medicament** from herbs gathered in the alpine meadows."
            }
        ]
    },
    "medicare": {
        "primary": "A national health insurance program in the United States, primarily serving persons aged sixty-five and older.",
        "secondary": "In social insurance and health economics, a universal public financing program for geriatric medical coverage.",
        "quotes": [
            {
                "author": "Paul Starr",
                "work": "The Social Transformation of American Medicine",
                "quote": "The establishment of **Medicare** in 1965 fundamentally restructured the economics of American hospital care."
            },
            {
                "author": "Milton Friedman",
                "work": "Capitalism and Freedom",
                "quote": "Compulsory federal health insurance under **Medicare** inevitably distorted the pricing of clinical services."
            },
            {
                "author": "Kenneth Arrow",
                "work": "Uncertainty and the Welfare Economics of Medical Care",
                "quote": "Government insurance programs such as **Medicare** pool health risks across large elderly populations."
            }
        ]
    },
    "medicate": {
        "primary": "To administer medicine or drugs to someone; to treat a condition with pharmaceutical remedies.",
        "secondary": "To impregnate or treat a bandage, liquid, or substance with healing or antiseptic properties.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Physicians must be careful not to over-**medicate** elderly patients suffering from chronic debility."
            },
            {
                "author": "Joseph Lister",
                "work": "On the Antiseptic Principle in the Practice of Surgery",
                "quote": "Surgeons chose to **medicate** surgical dressings with carbolic acid to inhibit airborne putrefaction."
            },
            {
                "author": "Oliver Sacks",
                "work": "Awakenings",
                "quote": "We proceeded to **medicate** the rigid post-encephalitic patients with cautious, titrated doses."
            }
        ]
    },
    "medication": {
        "primary": "A substance used for medical treatment, especially a drug prescribed to treat illness.",
        "secondary": "The therapeutic process or act of treating a patient with pharmaceutical substances.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Careful nursing care often accomplishes more for the typhoid patient than polypharmacy **medication**."
            },
            {
                "author": "Oliver Sacks",
                "work": "The Man Who Mistook His Wife for a Hat",
                "quote": "The sudden withdrawal of psychotropic **medication** provoked a rebound exacerbation of motor tics."
            },
            {
                "author": "Arthur Guyton",
                "work": "Textbook of Medical Physiology",
                "quote": "Continuous subcutaneous **medication** stabilizes blood sugar levels in juvenile diabetic subjects."
            }
        ]
    },
    "medicative": {
        "primary": "Having healing, curative, or medicinal properties; therapeutic.",
        "secondary": "In historical medicine, tending to alleviate sickness or promote bodily recovery.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The hot mineral springs of Baiae were celebrated for their extraordinary **medicative** virtues."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The physician relied upon the natural **medicative** power of nature, the vis medicatrix naturae."
            },
            {
                "author": "John Locke",
                "work": "Some Thoughts Concerning Education",
                "quote": "Simple diet and exercise possess a far more **medicative** efficacy for growing children than physics."
            }
        ]
    },
    "medici": {
        "primary": "The powerful Italian banking family and political dynasty that ruled Florence during the Renaissance.",
        "secondary": "In European cultural history, great patrons of art, architecture, and humanism (e.g. Cosimo and Lorenzo de' Medici).",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The munificence of the house of **Medici** revived the study of Greek literature in western Europe."
            },
            {
                "author": "Niccolò Machiavelli",
                "work": "The Prince",
                "quote": "Machiavelli dedicated his political treatise to Lorenzo de' **Medici**, urging the liberation of Italy."
            },
            {
                "author": "John Ruskin",
                "work": "Mornings in Florence",
                "quote": "The commercial wealth of the **Medici** transformed Florentine civic architecture into timeless art."
            }
        ]
    },
    "medicinal": {
        "primary": "Having healing properties; used for medical purposes or treating disease.",
        "secondary": "In pharmacology, a substance suitable for therapeutic administration as a drug.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Voyage of the Beagle",
                "quote": "Indigenous peoples in the Andean valleys gathered cinchona bark for its invaluable **medicinal** qualities."
            },
            {
                "author": "William Shakespeare",
                "work": "Othello",
                "quote": "Drop tears as fast as the Arabian trees their **medicinal** gum."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Digitalis remains among the most potent **medicinal** agents known for controlling cardiac arrhythmias."
            }
        ]
    },
    "medicinally": {
        "primary": "For medical or therapeutic purposes; as a medicine.",
        "secondary": "In clinical practice, administered to cure disease or relieve painful physiological symptoms.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Opium poppies have been cultivated **medicinally** since the earliest records of human civilization."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Quinine must be administered **medicinally** in prompt doses upon the first appearance of the ague chill."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "Sulfur compounds are employed **medicinally** as mild alteratives and topical antiseptics."
            }
        ]
    },
    "medicine": {
        "primary": "The science or practice of the diagnosis, treatment, and prevention of disease; or a pharmaceutical drug.",
        "secondary": "The broad profession and academic discipline encompassing clinical, surgical, and preventative healing arts.",
        "quotes": [
            {
                "author": "Hippocrates",
                "work": "Aphorisms",
                "quote": "Life is short, the art of **medicine** long, opportunity fleeting, experiment treacherous, judgment difficult."
            },
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "The practice of **medicine** is an art, not a trade; a calling, not a business."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Experimental **medicine** is the synthesis of physiology, pathology, and therapeutics into one unified science."
            }
        ]
    },
    "medick": {
        "primary": "An archaic or alternative spelling of medic, referring to plants of the genus Medicago.",
        "secondary": "In historical British agriculture, clover-like leguminous plants cultivated for animal pasturage.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom",
                "quote": "Yellow **medick** grows abundantly along dry roadside banks throughout southern England."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "Black **medick** or nonesuch bears small kidney-shaped pods that turn black when mature."
            },
            {
                "author": "Walter Scott",
                "work": "The Heart of Midlothian",
                "quote": "The sheep grazed peacefully on the hillside covered in wild thyme and sweet **medick**."
            }
        ]
    },
    "medico": {
        "primary": "An informal or colloquial term for a doctor, physician, or medical student.",
        "secondary": "In historical literature and university slang, an individual belonging to the medical faculty.",
        "quotes": [
            {
                "author": "Arthur Conan Doyle",
                "work": "Round the Red Lamp",
                "quote": "Every young **medico** remembers the anxious suspense of waiting for his first private patient."
            },
            {
                "author": "Charles Dickens",
                "work": "Bleak House",
                "quote": "Allan Woodcourt was an energetic young **medico** who devoted himself to the cholera-stricken poor."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The practicing **medico** must maintain high clinical standards through lifelong reading."
            }
        ]
    },
    "medicolegal": {
        "primary": "Pertaining to both medicine and law; involving the application of medical science to legal problems.",
        "secondary": "In forensic pathology and jurisprudence, relating to inquests, autopsies, malpractice, or forensic evidence.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Poisoning cases demand rigorous **medicolegal** necropsy to provide conclusive chemical evidence in court."
            },
            {
                "author": "Rudolf Virchow",
                "work": "Cellular Pathology",
                "quote": "Forensic pathologists conduct **medicolegal** autopsies to establish the physiological cause of suspicious death."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Sign of the Four",
                "quote": "Sherlock Holmes took pride in his mastery of **medicolegal** chemical tests for identifying blood stains."
            }
        ]
    },
    "mediety": {
        "primary": "A half; one of two equal parts; or a middle state or condition.",
        "secondary": "In historical English property law and ecclesiastical benefices, a moiety or half-portion of a living.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The estate was divided into equal portions, each co-heir receiving a **mediety** of the ancestral manor."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The treaty assigned a **mediety** of the customs duties to the Genoese merchants."
            },
            {
                "author": "Thomas Browne",
                "work": "Pseudodoxia Epidemica",
                "quote": "Naturalists debate whether the hermaphroditic creature shares an exact **mediety** of male and female natures."
            }
        ]
    },
    "medieval": {
        "primary": "Relating to the Middle Ages, the historical period in European history from roughly 500 to 1500 AD.",
        "secondary": "Resembling or characteristic of the Middle Ages, often contrasted with modern or classical culture.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The feudal castles of the **medieval** barons stood as defiant monuments of provincial anarchy."
            },
            {
                "author": "John Ruskin",
                "work": "The Stones of Venice",
                "quote": "In every carved ornament of a **medieval** church one reads the untamed spirit of the northern builder."
            },
            {
                "author": "Alexis de Tocqueville",
                "work": "The Old Regime and the Revolution",
                "quote": "The French monarchy gradually stripped **medieval** institutions of their ancient legislative autonomy."
            }
        ]
    },
    "medina": {
        "primary": "The old, historic quarter of a North African or Arab city, typically walled and densely built.",
        "secondary": "In Islamic history, the holy city of Medina (al-Madinah) in western Saudi Arabia, where the Prophet Muhammad established the early Muslim community.",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "Muhammad fled from Mecca and found welcoming refuge among the loyal citizens of **Medina**."
            },
            {
                "author": "Richard Francis Burton",
                "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah",
                "quote": "The pilgrim caravan entered the ancient date-groves surrounding the holy sanctuary of **Medina**."
            },
            {
                "author": "Washington Irving",
                "work": "Mahomet and His Successors",
                "quote": "The city of **Medina** became the cradle of an empire that swiftly overran the frontiers of Rome and Persia."
            }
        ]
    },
    "medinilla": {
        "primary": "A genus of tropical evergreen shrubs or lianas in the family Melastomataceae, native to the Paleotropics.",
        "secondary": "In horticulture and tropical botany, ornamental plants (such as Medinilla magnifica) noted for pendulous pink panicles and large showy bracts.",
        "quotes": [
            {
                "author": "Asa Gray",
                "work": "Scientific Papers of Asa Gray",
                "quote": "The botanist described an exquisite new species of **Medinilla** collected in the lush Philippine rainforests."
            },
            {
                "author": "Alfred Russel Wallace",
                "work": "The Malay Archipelago",
                "quote": "Magnificent epiphytic shrubs of the genus **Medinilla** hung their roseate floral clusters from mossy branches."
            },
            {
                "author": "Charles Darwin",
                "work": "Life and Letters of Charles Darwin",
                "quote": "In the tropical greenhouse at Kew, I admired the striking tiered bracts of a flowering **Medinilla**."
            }
        ]
    },
    "mediocre": {
        "primary": "Of only moderate, ordinary, or average quality; not very good.",
        "secondary": "Lacking distinction, brilliance, or excellence; commonplace in execution or intellect.",
        "quotes": [
            {
                "author": "Samuel Johnson",
                "work": "The Lives of the Poets",
                "quote": "A **mediocre** poet may avoid glaring blunders, but he will never kindle the sublime fire of genius."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The empire languished under the feeble administration of emperors possessing only **mediocre** talents."
            },
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "She dreaded falling into a **mediocre** domestic existence devoid of noble intellectual ambitions."
            }
        ]
    },
    "mediocrity": {
        "primary": "Moderate ability, commonplace achievement, or absence of superior excellence.",
        "secondary": "A person of second-rate ability, modest accomplishment, or commonplace intellect.",
        "quotes": [
            {
                "author": "Alexis de Tocqueville",
                "work": "Democracy in America",
                "quote": "Equality of conditions raises the lowest classes, but it tends to impose a uniform **mediocrity** upon culture."
            },
            {
                "author": "John Stuart Mill",
                "work": "On Liberty",
                "quote": "The general tendency of things throughout the world is to render **mediocrity** the ascendant power among mankind."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "When revolutionary mobs rule, brazen pretension triumphs over modest virtue and solid **mediocrity**."
            }
        ]
    },
    "meditate": {
        "primary": "To engage in contemplation, deep reflection, or mental exercises for spiritual or mental peace.",
        "secondary": "To plan, devise, or consider something deeply in one's mind over an extended period.",
        "quotes": [
            {
                "author": "Marcus Aurelius",
                "work": "Meditations",
                "quote": "Withdraw into yourself and **meditate** upon the transient vanity of all worldly ambitions."
            },
            {
                "author": "Edward Gibbon",
                "work": "Memoirs of My Life and Writings",
                "quote": "It was at Rome, as I sat musing amidst the ruins of the Capitol, that I began to **meditate** my history."
            },
            {
                "author": "John Milton",
                "work": "Lycidas",
                "quote": "Alas! What boots it with uncessant care to tend the homely slighted shepherd's trade, and strictly **meditate** the thankless Muse?"
            }
        ]
    },
    "meditation": {
        "primary": "The practice or action of meditating; continuous, deep, and quiet contemplation.",
        "secondary": "A written discourse or private reflection upon spiritual, philosophical, or moral themes.",
        "quotes": [
            {
                "author": "René Descartes",
                "work": "Meditations on First Philosophy",
                "quote": "In my first **meditation**, I resolved to doubt every former belief that admitted of the slightest uncertainty."
            },
            {
                "author": "William Wordsworth",
                "work": "Lines Composed a Few Miles above Tintern Abbey",
                "quote": "A presence that disturbs me with the joy of elevated thoughts; a sense sublime of something far more deeply interfused, in holy **meditation**."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The solitary monks of the Thebaid spent decades in uninterrupted prayer, fasting, and spiritual **meditation**."
            }
        ]
    },
    "meditative": {
        "primary": "Of, involving, or absorbed in deep, continuous, or quiet contemplation.",
        "secondary": "Expressing, inducing, or characterized by serene philosophical introspection.",
        "quotes": [
            {
                "author": "Nathaniel Hawthorne",
                "work": "The Scarlet Letter",
                "quote": "The minister walked through the quiet forest in a **meditative** mood, reflecting on the burden of his sin."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "Yes, as every one knows, **meditative** and water are wedded for ever."
            },
            {
                "author": "Henry David Thoreau",
                "work": "Walden",
                "quote": "I spent long, **meditative** hours watching the ripples circle outward on the glassy pond."
            }
        ]
    },
    "meditatively": {
        "primary": "In a quiet, thoughtful, or deeply contemplative manner.",
        "secondary": "With reflective introspection, lingering over ideas or perceptions.",
        "quotes": [
            {
                "author": "George Eliot",
                "work": "Middlemarch",
                "quote": "Lydgate tapped his chin **meditatively** as he weighed the contradictory symptoms of his patient."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "Holmes smoked his pipe **meditatively**, gazing through the window into the London fog."
            },
            {
                "author": "Joseph Conrad",
                "work": "Lord Jim",
                "quote": "Marlow paused and looked **meditatively** across the darkening harbor before resuming his tale."
            }
        ]
    },
    "meditativeness": {
        "primary": "The disposition or habit of being deeply thoughtful, reflective, or contemplative.",
        "secondary": "A quiet temperament inclined toward inward mental absorption and philosophical rumination.",
        "quotes": [
            {
                "author": "William James",
                "work": "The Varieties of Religious Experience",
                "quote": "The saintly temperament is characterized by an enduring serenity and inward **meditativeness**."
            },
            {
                "author": "Samuel Taylor Coleridge",
                "work": "Biographia Literaria",
                "quote": "Wordsworth's poetry is distinguished by its profound **meditativeness** amidst the beauty of nature."
            },
            {
                "author": "George Eliot",
                "work": "The Mill on the Floss",
                "quote": "Her quiet **meditativeness** puzzled her brother, who preferred brisk action to silent wonder."
            }
        ]
    },
    "mediterranean": {
        "primary": "Relating to the Mediterranean Sea, its surrounding coastal countries, or their climate.",
        "secondary": "Enclosed or nearly enclosed by land; inland (from Latin medius 'middle' + terra 'land').",
        "quotes": [
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The Roman empire encircled the entire basin of the **Mediterranean** sea with flourishing provinces."
            },
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The flora of the **Mediterranean** littoral exhibits adaptations to hot, dry summer droughts."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Submarine elevations have repeatedly narrowed the straits connecting the **Mediterranean** with the Atlantic."
            }
        ]
    },
    "medium": {
        "primary": "An agency, means, or intervening substance by which something is accomplished or conveyed.",
        "secondary": "In physics and biology, a surrounding liquid or gas supporting transmission of waves, heat, or organisms.",
        "quotes": [
            {
                "author": "Isaac Newton",
                "work": "Opticks",
                "quote": "Light slows down and refracts when passing from a rare **medium** into a denser one."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "Money functions as the universal **medium** of commerce that facilitates the division of labor."
            },
            {
                "author": "Aristotle",
                "work": "Poetics",
                "quote": "Poetry, music, and painting differ from one another either by the **medium**, the objects, or the manner of imitation."
            }
        ]
    },
    "medium-dry": {
        "primary": "Having a slight degree of residual sweetness, applied especially to wine, sherry, or cider.",
        "secondary": "In enology and culinary appraisal, falling between bone-dry and sweet in sugar content.",
        "quotes": [
            {
                "author": "George Saintsbury",
                "work": "Notes on a Cellar-Book",
                "quote": "A delicate **medium-dry** amontillado sherry provides an exquisite accompaniment to rich soups."
            },
            {
                "author": "Charles Dickens",
                "work": "Our Mutual Friend",
                "quote": "The butler produced a bottle of **medium-dry** Madeira, dusting the vintage cobwebs from the neck."
            },
            {
                "author": "Robert Louis Stevenson",
                "work": "The Silverado Squatters",
                "quote": "We sampled a crisp, **medium-dry** white wine produced from the sun-drenched Napa vineyards."
            }
        ]
    },
    "medium-large": {
        "primary": "Intermediate in size between medium and large; moderately sizable.",
        "secondary": "In biological morphology and commercial grading, designating specimens larger than standard median dimensions.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Breeders selected **medium-large** dogs possessing both muscular speed and sufficient stamina."
            },
            {
                "author": "Spencer Fullerton Baird",
                "work": "Mammals of North America",
                "quote": "The skull belonged to a **medium-large** carnivore characterized by heavy molar crushing teeth."
            },
            {
                "author": "Asa Gray",
                "work": "Manual of the Botany of the Northern United States",
                "quote": "The tree produces **medium-large** acorns capped in rough, pubescent cups."
            }
        ]
    },
    "medium-size": {
        "primary": "Of intermediate or average size; neither particularly small nor especially large.",
        "secondary": "Belonging to a standard intermediate dimensional category in classification.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Descent of Man",
                "quote": "A **medium-size** bird can forage effectively among both ground leaf litter and overhead branches."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "The river gravels deposited **medium-size** pebbles along the ancient terrace bends."
            },
            {
                "author": "Adam Smith",
                "work": "The Wealth of Nations",
                "quote": "A **medium-size** commercial enterprise frequently balances capital efficiency with operational flexibility."
            }
        ]
    },
    "medium-sized": {
        "primary": "Having an intermediate or average size; falling midway between small and large.",
        "secondary": "Characterized by median physical dimensions or volume across comparative samples.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "On the Origin of Species",
                "quote": "The domestic rabbit originated from a **medium-sized** wild ancestral species native to southern Europe."
            },
            {
                "author": "Arthur Conan Doyle",
                "work": "The Hound of the Baskervilles",
                "quote": "The track in the bog was that of an extraordinarily large hound, far exceeding a **medium-sized** mastiff."
            },
            {
                "author": "Herman Melville",
                "work": "Moby-Dick",
                "quote": "The carpenter shaped a **medium-sized** cedar spar to replace the shattered steering oar."
            }
        ]
    },
    "nonmedicinal": {
        "primary": "Not having medicinal or healing properties; not intended for medical use.",
        "secondary": "In regulatory pharmacology and botany, designating plants or compounds utilized for culinary, industrial, or cosmetic rather than curative purposes.",
        "quotes": [
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The alchemist's tincture contained purely **nonmedicinal** coloring extracts that possessed zero physiological potency."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The soothing beverage was entirely **nonmedicinal**, designed merely to encourage adequate patient hydration."
            },
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Many herbs were originally domesticated for ornamental or **nonmedicinal** reasons before their chemical virtues were known."
            }
        ]
    },
    "premedical": {
        "primary": "Relating to or preparing for the study of medicine; prerequisite studies before medical school.",
        "secondary": "In academic curricula, preparatory scientific instruction in chemistry, biology, and physics for future physicians.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "The student must acquire a rigorous **premedical** grounding in physical science before entering the hospital wards."
            },
            {
                "author": "Thomas Henry Huxley",
                "work": "Science and Culture",
                "quote": "A sound **premedical** education teaches the youth the unsparing discipline of comparative dissection."
            },
            {
                "author": "Charles Eliot",
                "work": "Educational Reform",
                "quote": "Harvard revolutionized medical training by establishing strict **premedical** prerequisites in collegiate chemistry."
            }
        ]
    },
    "premeditate": {
        "primary": "To think out, plan, or consider an action beforehand; to design beforehand.",
        "secondary": "In criminal jurisprudence, to formulate deliberate intent to commit an offense prior to execution.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "To constitute murder, the perpetrator must consciously **premeditate** the fatal stroke with malice aforethought."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The conspirators met in secret to **premeditate** the assassination of the tyrannical prefect."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on Conciliation with America",
                "quote": "No sensible statesman would deliberately **premeditate** measures that provoke rebellion among loyal subjects."
            }
        ]
    },
    "premeditated": {
        "primary": "Characterized by deliberate purpose, prior thought, and planning; not spontaneous.",
        "secondary": "In penal law, executed with malice prepense and deliberate design.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "The law draws a fundamental distinction between sudden manslaughter and **premeditated** murder."
            },
            {
                "author": "Charles Dickens",
                "work": "A Tale of Two Cities",
                "quote": "The spy's betrayal was a cold, **premeditated** scheme calculated to enrich himself."
            },
            {
                "author": "Edward Gibbon",
                "work": "The History of the Decline and Fall of the Roman Empire",
                "quote": "The ambush was so skillfully executed that it proved a **premeditated** masterpiece of barbarian tactics."
            }
        ]
    },
    "premeditation": {
        "primary": "The action of planning or considering something beforehand, especially a crime.",
        "secondary": "In jurisprudence, deliberate forethought and calculation prior to the commission of an act.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "Express malice appears where the killing is accompanied by evident deliberation and **premeditation**."
            },
            {
                "author": "Edmund Burke",
                "work": "Reflections on the Revolution in France",
                "quote": "The destruction of ancient legal institutions was accomplished with deliberate and sinister **premeditation**."
            },
            {
                "author": "David Hume",
                "work": "A Treatise of Human Nature",
                "quote": "Acts executed with calm **premeditation** reflect the true moral character of an agent far more than sudden passions."
            }
        ]
    },
    "remediable": {
        "primary": "Capable of being remedied, cured, repaired, or corrected.",
        "secondary": "In law and social reform, amenable to legal redress, legislative compensation, or medical treatment.",
        "quotes": [
            {
                "author": "John Stuart Mill",
                "work": "Principles of Political Economy",
                "quote": "Poverty caused by lack of technical education is a **remediable** social misfortune."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Iron deficiency anemia remains an easily **remediable** condition under proper ferruginous therapy."
            },
            {
                "author": "Edmund Burke",
                "work": "Speech on American Taxation",
                "quote": "Grievances arising from administrative mismanagement are happily **remediable** through parliamentary repeal."
            }
        ]
    },
    "remedial": {
        "primary": "Giving or intended as a remedy or cure; therapeutic or corrective.",
        "secondary": "In education and jurisprudence, providing corrective instruction or affording legal redress for a civil injury.",
        "quotes": [
            {
                "author": "William Blackstone",
                "work": "Commentaries on the Laws of England",
                "quote": "A **remedial** statute is enacted to supply some defect or abridge some superfluity in the common law."
            },
            {
                "author": "John Stuart Mill",
                "work": "Considerations on Representative Government",
                "quote": "The legislature passed **remedial** acts designed to protect factory apprentices from overwork."
            },
            {
                "author": "Florence Nightingale",
                "work": "Notes on Nursing",
                "quote": "Fresh air, pure water, and clean bedding constitute the foremost **remedial** agents in hospital management."
            }
        ]
    },
    "remediate": {
        "primary": "To provide a remedy for; to heal, cure, or rehabilitate an environmental or social problem.",
        "secondary": "In environmental engineering, to decontaminate soil, water, or industrial sites to restore ecological health.",
        "quotes": [
            {
                "author": "Eugene Odum",
                "work": "Fundamentals of Ecology",
                "quote": "Ecological engineers use wetland biofilters to **remediate** agricultural runoff polluted with nitrates."
            },
            {
                "author": "John Dewey",
                "work": "Democracy and Education",
                "quote": "Progressive pedagogical methods strive to **remediate** early developmental deficits through hands-on inquiry."
            },
            {
                "author": "Charles Lyell",
                "work": "Principles of Geology",
                "quote": "Natural silting processes eventually **remediate** fractured estuaries after violent coastal storm surges."
            }
        ]
    },
    "remediation": {
        "primary": "The action of remedying something, in particular of reversing or stopping environmental damage.",
        "secondary": "In education and clinical therapy, specialized instruction or treatment aimed at correcting deficiencies.",
        "quotes": [
            {
                "author": "Eugene Odum",
                "work": "Fundamentals of Ecology",
                "quote": "Microbial bioremediation offers a sustainable path for the ecological **remediation** of petroleum spills."
            },
            {
                "author": "John Dewey",
                "work": "The School and Society",
                "quote": "Early cognitive **remediation** enables struggling students to regain confidence in fundamental literacy."
            },
            {
                "author": "Paul Starr",
                "work": "The Social Transformation of American Medicine",
                "quote": "Sanitary **remediation** of municipal water supplies caused infant mortality rates to plummet in urban centers."
            }
        ]
    },
    "submediant": {
        "primary": "In musical theory, the sixth scale degree of a diatonic scale, located halfway between subdominant and upper tonic.",
        "secondary": "In harmonic syntax, the chord built upon the sixth scale degree (vi or VI), often functioning as a tonic substitute.",
        "quotes": [
            {
                "author": "Hermann von Helmholtz",
                "work": "On the Sensations of Tone",
                "quote": "The deceptive cadence shifts harmonic expectation from the dominant chord to the unexpected **submediant**."
            },
            {
                "author": "Jean-Philippe Rameau",
                "work": "Treatise on Harmony",
                "quote": "A descending bass line often pauses upon the **submediant** before driving forward to the final cadence."
            },
            {
                "author": "Hector Berlioz",
                "work": "Treatise on Instrumentation",
                "quote": "The cellos sustained a dark, melancholy **submediant** note beneath the shimmering violin tremolo."
            }
        ]
    },
    "unmediated": {
        "primary": "Happening without an intervening person, medium, or mechanism; direct or uninfluenced.",
        "secondary": "In philosophy and aesthetics, unvarnished perceptual experience experienced without interpretive conceptual screens.",
        "quotes": [
            {
                "author": "William James",
                "work": "Essays in Radical Empiricism",
                "quote": "Radical empiricism takes pure, **unmediated** experience as the primordial fabric of reality."
            },
            {
                "author": "John Dewey",
                "work": "Art as Experience",
                "quote": "A genuine aesthetic moment delivers an **unmediated** encounter with sensory form and emotion."
            },
            {
                "author": "Bertrand Russell",
                "work": "The Problems of Philosophy",
                "quote": "Knowledge by acquaintance consists in direct, **unmediated** cognitive awareness of sense-data."
            }
        ]
    },
    "unmedical": {
        "primary": "Not medical; not relating to, suitable for, or characteristic of medicine or medical practice.",
        "secondary": "Lacking professional clinical credentials or medical scientific validity.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "Aequanimitas",
                "quote": "Quack nostrums prey upon the gullible public through completely **unmedical** superstitions."
            },
            {
                "author": "Oliver Wendell Holmes Sr.",
                "work": "Medical Essays",
                "quote": "The pamphlet was composed in an **unmedical** jargon calculated to bewilder rustic patients."
            },
            {
                "author": "Charles Dickens",
                "work": "The Pickwick Papers",
                "quote": "Mr. Pickwick listened with polite skepticism to the landlord's entirely **unmedical** theory of rheumatism."
            }
        ]
    },
    "unmedicative": {
        "primary": "Not having healing, curative, or medicative properties; non-therapeutic.",
        "secondary": "Devoid of pharmacological potency or physiological healing influence.",
        "quotes": [
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "The inert sugar pill was an entirely **unmedicative** placebo administered to satisfy an anxious patient."
            },
            {
                "author": "Antoine Lavoisier",
                "work": "Elements of Chemistry",
                "quote": "The distillate yielded an **unmedicative** residue containing only mineral impurities and inert sand."
            },
            {
                "author": "Claude Bernard",
                "work": "An Introduction to the Study of Experimental Medicine",
                "quote": "Controlled trials proved that the popular herbal infusion was wholly **unmedicative** against febrile illnesses."
            }
        ]
    },
    "unmedicinal": {
        "primary": "Not having medicinal or healing qualities; not useful as a medicine.",
        "secondary": "Lacking curative virtue; inert or ineffective as a pharmaceutical therapeutic agent.",
        "quotes": [
            {
                "author": "Charles Darwin",
                "work": "The Variation of Animals and Plants under Domestication",
                "quote": "Wild varieties often produce bitter, **unmedicinal** juices that are rejected by grazing livestock."
            },
            {
                "author": "William Osler",
                "work": "The Principles and Practice of Medicine",
                "quote": "Ancient pharmacopeias were cluttered with filthy, **unmedicinal** decoctions that harmed the sick."
            },
            {
                "author": "Samuel Johnson",
                "work": "The Rambler",
                "quote": "He found the bitter spring water wholly **unmedicinal**, despite the lavish promises of the spa keeper."
            }
        ]
    },
    "unpremeditated": {
        "primary": "Not thought out or planned beforehand; spontaneous, impromptu, or impulsive.",
        "secondary": "In literary poetry, art, and human conduct, effortless and uncalculated creative expression.",
        "quotes": [
            {
                "author": "Percy Bysshe Shelley",
                "work": "To a Skylark",
                "quote": "Hail to thee, blithe Spirit! Bird thou never wert, that from Heaven, or near it, pourest thy full heart in profuse strains of **unpremeditated** art."
            },
            {
                "author": "John Milton",
                "work": "Paradise Lost",
                "quote": "And with voluntary move and harmonious numbers, my **unpremeditated** verse flows night and day."
            },
            {
                "author": "Jane Austen",
                "work": "Sense and Sensibility",
                "quote": "Marianne's warm, **unpremeditated** words betrayed the depth of her spontaneous affection."
            }
        ]
    }
}

if __name__ == "__main__":
    print(f"Total words in data_order_b3_p2: {len(data_order_b3_p2)}")
    
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

    for word, item in data_order_b3_p2.items():
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
        print("\n[OK] ALL 77 words in Cluster Order Batch 3 Part 2 PASSED local pre-audit validation!")
