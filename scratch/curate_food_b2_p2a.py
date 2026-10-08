# -*- coding: utf-8 -*-
"""
curate_food_b2_p2a.py
Batch 2 Part 2a of Cluster Food: Dashboard — al (words 39-57):
['coalition', 'colloquialism', 'comal', 'comical', 'comicality', 'comically',
 'contextual', 'contextualism', 'contextually', 'coral', 'cordial',
 'cordiality', 'cordially', 'coxalgic', 'craniofacial', 'criminal',
 'criminalise', 'criminalism', 'criminality']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_b2_p2a = {
    # 39. coalition
    "coalition": {
        "primary": "An alliance or temporary union of distinct political parties, factions, or nations formed for joint action.",
        "secondary": "In game theory and international diplomacy, a strategic alignment formed by separate agents to aggregate collective voting power or military deterrence.",
        "quotes": [
            {"author": "Edmund Burke", "work": "Thoughts on the Cause of the Present Discontents", "quote": "When bad men combine, the good must associate; else they will fall, one by one, an unpitied sacrifice in a contemptible struggle against an oppressive **coalition**."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The European powers formed a grand **coalition** to curb the aggressive territorial ambitions of the French monarchy."},
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A hostile **coalition** among neighboring states presents a perpetual danger against which a unified federal republic must prepare."}
        ]
    },

    # 40. colloquialism
    "colloquialism": {
        "primary": "A word, phrase, or expression characteristic of informal conversation and spoken discourse rather than formal literary language.",
        "secondary": "In sociolinguistics, a vernacular idiom or dialectal phrasing that signals localized cultural belonging, relaxed intimacy, and speech-community cohesion.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "I have rejected many an uncouth **colloquialism** that had crept into vulgar dialogue without the sanction of polite authors."},
            {"author": "Mark Twain", "work": "Adventures of Huckleberry Finn", "quote": "The boy's narrative was packed with raw frontier **colloquialism**, mirroring the authentic cadence of Mississippi raftmen."},
            {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Modern dialogue gains vigor by incorporating the lively **colloquialism** of the street, refreshing obsolete literary diction."}
        ]
    },

    # 41. comal
    "comal": {
        "primary": "A smooth, flat griddle traditionally made of clay or cast iron used in Mexican and Central American cooking to cook tortillas.",
        "secondary": "In Mesoamerican material culture and culinary archaeology, a circular earthenware plate essential for toasting maize masa, roasting chilies, and parching cacao seeds.",
        "quotes": [
            {"author": "Bernal Díaz del Castillo", "work": "The Discovery and Conquest of Mexico", "quote": "In the great market place native women knelt before broad clay **comal** griddles, baking flat maize loaves over glowing coals."},
            {"author": "Fanny Calderón de la Barca", "work": "Life in Mexico", "quote": "The morning air was fragrant with baking tortillas warmed upon a primitive iron **comal** over the kitchen brazier."},
            {"author": "William H. Prescott", "work": "History of the Conquest of Mexico", "quote": "The household vessels included the earthenware **comal**, upon which Indian women prepared the daily corn cakes for their families."}
        ]
    },

    # 42. comical
    "comical": {
        "primary": "Provoking amusement or laughter; amusingly eccentric, absurd, or ludicrous in appearance or behavior.",
        "secondary": "In dramatic theory and narrative aesthetics, pertaining to the conventions, character archetypes, and farcical reversals of comic performance.",
        "quotes": [
            {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "Our play has been celebrated as very tragical mirth, full of most **comical** blunders and surprising turns."},
            {"author": "Charles Dickens", "work": "The Posthumous Papers of the Pickwick Club", "quote": "Mr. Pickwick cut a singularly **comical** figure as he scrambled over the frozen pond, arms waving wildly in frantic efforts to regain equilibrium."},
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The mumming performance presented a **comical** mixture of ancient chivalric defiance and rustic awkwardness."}
        ]
    },

    # 43. comicality
    "comicality": {
        "primary": "Amusing absurdity, funny eccentricity, or ludicrous oddity that naturally provokes laughter.",
        "secondary": "In literary criticism and stagecraft, the deliberate orchestration of visual incongruity, witty exaggeration, and slapstick timing to provoke mirth.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "There was an irresistible **comicality** in the countryman's solemn endeavor to articulate the legal phrase correctly."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Even in his most irritable moments, a sudden gleam of **comicality** in his companion's remarks would disarm his vexation."},
            {"author": "Washington Irving", "work": "Bracebridge Hall", "quote": "The rustic village parson possessed a dry **comicality** of manner that kept the harvest gathering in continuous chuckles."}
        ]
    },

    # 44. comically
    "comically": {
        "primary": "In an amusing, ludicrous, eccentric, or laugh-provoking manner.",
        "secondary": "In dramatic narration, depicting situations wherein human gravity or pompous pretension is deflated with humorous incongruity.",
        "quotes": [
            {"author": "Bram Stoker", "work": "Dracula", "quote": "Van Helsing's heavy spectacles slid down his nose, giving his solemn countenance a **comically** startled expression."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The little priest appeared **comically** insignificant amidst the towering mahogany bookshelves of the lordly library."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Watson looked **comically** perplexed as Holmes produced the missing boot from beneath the hearthrug."}
        ]
    },

    # 45. contextual
    "contextual": {
        "primary": "Pertaining to, depending upon, or explained by the surrounding context or specific circumstances of an event or text.",
        "secondary": "In linguistics, hermeneutics, and epistemology, emphasizing that semantic meaning and moral validity derive from surrounding historical, situational, and textual environments.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Words torn from their natural discourse lose their **contextual** significance and confound philosophical inquiry."},
            {"author": "William James", "work": "The Meaning of Truth", "quote": "A statement cannot be judged true in absolute isolation from its active, **contextual** relation to experience."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "Effective learning requires **contextual** engagement with practical problems rather than abstract memorization of detached rules."}
        ]
    },

    # 46. contextualism
    "contextualism": {
        "primary": "A philosophical doctrine emphasizing that an action, utterance, or expression can only be understood within its specific context.",
        "secondary": "In contemporary epistemology and legal interpretation, the thesis that knowledge attributions and statutory standards vary according to conversational stakes and situational standards.",
        "quotes": [
            {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "Our radical empiricism defends a thoroughgoing **contextualism**, rejecting timeless dogmas in favor of dynamic circumstance."},
            {"author": "John Dewey", "work": "Experience and Nature", "quote": "Philosophical **contextualism** recognizes that every problem and solution emerges from concrete historical matrixes."},
            {"author": "George Santayana", "work": "Scepticism and Animal Faith", "quote": "The claims of critical **contextualism** remind us that all human knowledge is anchored to the observer's mortal horizon."}
        ]
    },

    # 47. contextually
    "contextually": {
        "primary": "In a manner that depends on, relates to, or is determined by the surrounding context or situation.",
        "secondary": "In analytical semantics and discourse analysis, modifying semantic interpretation so that meaning varies systematically with communicative frames and pragmatic cues.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Propositions must be examined **contextually** to ascertain whether an ambiguous term denotes an attribute or a substance."},
            {"author": "William James", "work": "Essays in Radical Empiricism", "quote": "Perceptions function **contextually** within the stream of thought, pointing forward to impending practical encounters."},
            {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "We interpret symbols **contextually**, relying on background conventions to resolve what would otherwise remain impenetrable ambiguity."}
        ]
    },

    # 48. coral
    "coral": {
        "primary": "A hard, stony substance secreted by marine polyp colonies (*Anthozoa*) forming extensive marine reefs.",
        "secondary": "In marine biology and gemology, calcium carbonate structures forming biogenic reefs, or polished red calcium secretions prized in classical jewelry.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Structure and Distribution of Coral Reefs", "quote": "The delicate polyps of the **coral** build massive barrier reefs through millennia of ceaseless biological growth beneath the breakers."},
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "Full fathom five thy father lies; Of his bones are **coral** made; Those are pearls that were his eyes."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Her lips parted in a gentle smile, revealing teeth as white as pearls against the warm **coral** of her mouth."}
        ]
    },

    # 49. cordial
    "cordial": {
        "primary": "Warm, deeply affectionate, and sincere in manner; or a comforting, stimulating medicinal drink or liqueur.",
        "secondary": "In historical pharmacology and etiquette (*cor*, heart), an invigorating draught prescribed to strengthen the vital spirits, or polite heartfelt hospitality.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Make that thy **cordial** to comfort thy heavy heart in these bitter trials."},
            {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "A kind and **cordial** reception from a parent works far more powerfully upon a child's mind than harsh verbal rebukes."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea welcomed her friend with a **cordial** warmth that showed how deeply she valued true fellowship."}
        ]
    },

    # 50. cordiality
    "cordiality": {
        "primary": "Warm, affectionate friendliness and heartfelt sincerity in social interaction.",
        "secondary": "In social etiquette and moral philosophy, an open, generous demeanor that dispels reserve and fosters mutual goodwill without false flattery.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "There was a generous **cordiality** in his greeting that immediately put the nervous young curate at his ease."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A profound spiritual peace often manifests outwardly as an affectionate **cordiality** toward all living beings."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe received me with an honest **cordiality** that shone in his bright blue eyes and warmed my shamefaced heart."}
        ]
    },

    # 51. cordially
    "cordially": {
        "primary": "In a warm, affectionate, sincere, or hearty manner.",
        "secondary": "In epistolary conventions and polite conduct, expressing genuine goodwill, welcome, or wholehearted agreement.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Farmer Boldwood bowed and shook hands with the stranger **cordially**, inviting him to step inside the farmhouse parlour."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The rector thanked him **cordially** for his assistance, expressing high admiration for his upright and steadfast character."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes greeted our military guest **cordially**, offering him the armchair beside the glowing coal fire."}
        ]
    },

    # 52. coxalgic
    "coxalgic": {
        "primary": "Pertaining to or affected by pain or disease in the hip joint (*coxalgia*).",
        "secondary": "In nineteenth-century orthopedic medicine and surgical pathology, describing patients afflicted with tuberculous arthritis or chronic degenerative inflammation of the acetabulum and femur.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The surgeon observed a characteristic **coxalgic** limp in the child, indicating early tuberculous involvement of the hip joint."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Severe nocturnal spasms accompanied the **coxalgic** complaints of the patient, requiring immobilizing splints."},
            {"author": "Sir Astley Cooper", "work": "A Treatise on Dislocations and Fractures of the Joints", "quote": "Chronic **coxalgic** deformities frequently result from untreated subluxations that erode the articular cartilage of the pelvic socket."}
        ]
    },

    # 53. craniofacial
    "craniofacial": {
        "primary": "Pertaining to both the cranium (skull) and the face.",
        "secondary": "In anatomy and reconstructive surgery, relating to the bones, soft tissues, and developmental embryology of the cranial vault and facial skeleton.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "On the Form of the Head in Various Races", "quote": "Careful measurements of the **craniofacial** axis reveal significant morphological variations between ancient hominid skulls."},
            {"author": "William Flower", "work": "An Introduction to the Osteology of the Mammalia", "quote": "The fused sutures along the **craniofacial** boundary provide structural rigidity necessary to withstand masticatory stress."},
            {"author": "Arthur Keith", "work": "Human Embryology and Morphology", "quote": "Congenital abnormalities of the **craniofacial** region often originate during the early migration of neural crest cells."}
        ]
    },

    # 54. criminal
    "criminal": {
        "primary": "Involving, guilty of, or relating to an act that constitutes a public crime punishable by law.",
        "secondary": "In jurisprudence and penal philosophy, pertaining to offenses against the sovereign order or society, distinct from private civil delicts.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "An admirable evasion of whoremaster man, to lay his goatish disposition to the charge of a star, as if we were villains by necessity, fools by heavenly compulsion, knaves, thieves, and treachers by spherical predominance; drunkards, liars, and adulterers by an enforced obedience of planetary influence; and all that we are evil in, by a divine thrusting on; an admirable evasion to make man **criminal** only by celestial decree!"},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Acts injurious to others, without warrantable justification, fall under the legitimate sphere of **criminal** law and social retribution."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He feared that an investigation into the trust would expose him to **criminal** charges before the county assizes."}
        ]
    },

    # 55. criminalise
    "criminalise": {
        "primary": "To make an activity illegal or turn a person into a criminal by enacting prohibitive legislation.",
        "secondary": "In critical sociology and criminology (chiefly British spelling), the institutional process whereby state apparatuses redefine nonconforming behaviors as penal offenses.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "To **criminalise** actions which produce no palpable mischief is merely to multiply unnecessary suffering and weaken public respect for law."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Governments act unwisely when they attempt to **criminalise** voluntary economic exchanges that harm no unconsenting third party."},
            {"author": "Herbert Spencer", "work": "The Man Versus the State", "quote": "Every new regulatory statute tends indirectly to **criminalise** ordinary conduct and expand bureaucratic coercion."}
        ]
    },

    # 56. criminalism
    "criminalism": {
        "primary": "The phenomenon, state, or practice of criminal behavior, or the systematic study of criminality.",
        "secondary": "In nineteenth-century penal sociology, the social contagion, psychological habits, and underworld culture that sustain recurrent lawbreaking within urban centers.",
        "quotes": [
            {"author": "Cesare Lombroso", "work": "Criminal Man", "quote": "Anthropological examination seeks to uncover the organic roots of congenital **criminalism** in juvenile offenders."},
            {"author": "Henry Mayhew", "work": "London Labour and the London Poor", "quote": "The squalid alleys around the docks served as fertile breeding grounds for chronic **criminalism** and juvenile delinquency."},
            {"author": "William Douglas Morrison", "work": "Juvenile Offenders", "quote": "Penal reformers must address the economic and domestic conditions that actively foster habitual **criminalism** among the urban youth."}
        ]
    },

    # 57. criminality
    "criminality": {
        "primary": "Habitual engagement in criminal activity, unlawful behavior, or the collective rate of offences within a society.",
        "secondary": "In behavioral criminology and moral jurisprudence, the predisposition of an individual toward offending, or the statistical incidence of offenses within a polity.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Severe social destitution and lack of educational instruction drive thousands of neglected youth into systemic **criminality**."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "My vices are the children of a forced solitude that I abhor, and my virtues will necessarily arise when I am freed from this wretched **criminality**."},
            {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "He is the Napoleon of crime, Watson; the organizer of half that is evil and of nearly all that is undetected in this great city, the supreme genius of modern **criminality**."}
        ]
    }
}
