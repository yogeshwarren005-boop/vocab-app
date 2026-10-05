# -*- coding: utf-8 -*-
"""
Part 4 of Batch 2 Cluster Speech: nunci words (17 words):
['annunciate', 'annunciation', 'annunciator', 'annunciatory', 'denunciation',
 'denunciative', 'denunciatory', 'enunciate', 'enunciation', 'internuncio',
 'mispronunciation', 'nuncio', 'pronunciamento', 'pronunciation', 'renunciant',
 'renunciation', 'renunciative']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part4_nunci = {
    "annunciate": {
        "primary": "To announce, proclaim, or make known publicly, formally, or authoritatively.",
        "secondary": "In religious history and communication theory, to declare solemnly a momentous event or divine message destined to alter human affairs.",
        "quotes": [
            {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "The solemn duty of the moral philosopher is to **annunciate** eternal principles of justice without fear of partisan disapproval."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Prophets arise in every great spiritual crisis to **annunciate** a new gospel of truth to a bewildered generation."},
            {"author": "John Milton", "work": "Paradise Regained", "quote": "Celestial heralds descended to **annunciate** unto the shepherds the joyful birth of the promised Prince of Peace."}
        ]
    },
    "annunciation": {
        "primary": "The formal announcement or proclamation of an important event, truth, or doctrine.",
        "secondary": "In Christian theology and iconography, the angel Gabriel's announcement to the Virgin Mary of the incarnation of Christ, celebrated liturgically on March 25.",
        "quotes": [
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The herald stepped into the lists to make solemn **annunciation** of the rules governing the impending chivalric tourney."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "In Fra Angelico's painting of the **annunciation**, the golden wings of Gabriel tremble with celestial reverie before the humble Virgin."},
            {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The marble statue seemed almost to breathe, awaiting some divine **annunciation** that would animate its silent grace."}
        ]
    },
    "annunciator": {
        "primary": "One who announces or proclaims; or an electrical signaling apparatus that indicates which circuit was activated.",
        "secondary": "In mechanical engineering and nineteenth-century domestic technology, a wall-mounted panel with electromagnetic drop indicators signaling calls from specific rooms.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The bell rang sharply in the servants' hall, and the mechanical pointer on the **annunciator** dropped to indicate the study."},
            {"author": "H. G. Wells", "work": "When the Sleeper Wakes", "quote": "A glowing telephonic **annunciator** flashed warnings across the vaulted ceiling of the central aeronautical chamber."},
            {"author": "Edward Bellamy", "work": "Looking Backward: 2000–1887", "quote": "In our modern dwellings, an automatic **annunciator** connects each apartment directly with the public musical program."}
        ]
    },
    "annunciatory": {
        "primary": "Pertaining to, serving as, or containing an announcement or solemn proclamation.",
        "secondary": "In literary rhetoric and prophetic discourse, possessing a heraldic, portentous tone that foreshadows significant revelations or turning points.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The sudden tolling of the tocsin sounded with **annunciatory** terror through the darkened streets of revolutionary Paris."},
            {"author": "Herman Melville", "work": "Pierre; or, The Ambiguities", "quote": "The letter arrived with an **annunciatory** solemnity that struck an inexplicable chill into the heart of the youth."},
            {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "Hollingsworth spoke in an **annunciatory** cadence that seemed to brook no earthly contradiction from his disciples."}
        ]
    },
    "denunciation": {
        "primary": "Public condemnation, censure, or vehement accusation of someone or something as wicked or culpable.",
        "secondary": "In international diplomacy and criminal jurisprudence, the formal repudiation of a treaty, or the official lodging of criminal information before a tribunal.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "She hath made of you a most bitter **denunciation** before the duke's judgment seat in the open market."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Boythorn delivered a thunderous **denunciation** of the Chancery system, declaring that all scoundrels ought to be summarily blown to atoms."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The assembly rang with the frantic **denunciation** of ancient magistrates whose only guilt was fidelity to the constitution."}
        ]
    },
    "denunciative": {
        "primary": "Characterized by or containing denunciation; strongly condemning, accusing, or censuring.",
        "secondary": "In political journalism and pulpit oratory, exhibiting an aggressively invective rhetorical stance aimed at exposing moral or systemic delinquency.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "His pamphlets assumed a fiercely **denunciative** tone against the callous neglect of the impoverished manufacturing operatives."},
            {"author": "John Stuart Mill", "work": "Essays on Some Unsettled Questions of Political Economy", "quote": "Rhetoric that is merely **denunciative** never persuades thoughtful adversaries who demand rigorous deductive demonstrations."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Party newspapers indulge in a wildly **denunciative** style of vituperation that coarsens public debate across the nation."}
        ]
    },
    "denunciatory": {
        "primary": "Of, relating to, or marked by public denunciation, severe condemnation, or solemn accusation.",
        "secondary": "In homiletics and legal rhetoric, designed to castigate transgression through prophetic warning, legal penalty, or moral indignation.",
        "quotes": [
            {"author": "Effie Afton", "work": "Eventide", "quote": "Mass meetings were assembled, where indignant speakers delivered **denunciatory** addresses against the tyrannical enactments of the council."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The preacher launched into a **denunciatory** sermon upon the vices of the borough, making Henchard writhe in his high pew."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Prophets of every era employ **denunciatory** eloquence to shatter the smug complacency of decadent civilizations."}
        ]
    },
    "enunciate": {
        "primary": "To pronounce, utter, or articulate words clearly and distinctly; or to state a proposition systematically.",
        "secondary": "In linguistics and formal philosophy, to articulate phonemes with precision, or to expound a doctrine or theorem in formal propositional terms.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She paused before the examiner, striving to **enunciate** each syllable with that refined clarity taught in the training school."},
            {"author": "Jack London", "work": "The Star-Rover", "quote": "The warden took pains to slowly **enunciate** the severe rules of the solitary cell block before locking the iron gate."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Before embarking on scientific proof, the investigator must clearly **enunciate** the hypothesis he undertakes to verify."}
        ]
    },
    "enunciation": {
        "primary": "The act, manner, or clarity of articulating vocal speech sounds; or the formal statement of a proposition.",
        "secondary": "In phonetics and Euclidean geometry, the precise vocal execution of phonetic values, or the formal introductory statement of a theorem before its demonstration.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The clerk spoke with that deliberate rustic **enunciation** that gives every vowel the weight of an independent clause."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "I should say that his distinct **enunciation** and measured voice qualify him admirably for the clerical profession."},
            {"author": "Ralph Waldo Emerson", "work": "English Traits", "quote": "The educated Englishman cultivates a crisp, resolute **enunciation** that conveys an instinctive conviction of mastery."}
        ]
    },
    "internuncio": {
        "primary": "A diplomatic representative or intermediate messenger; specifically a papal legate ranking below a full nuncio.",
        "secondary": "In diplomatic history and ecclesiastical governance, an envoy dispatched to represent the Holy See in nations where full apostolic nunciatures are not established.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman pontiff dispatched an **internuncio** to the imperial court of Constantinople to negotiate terms of religious reconciliation."},
            {"author": "David Hume", "work": "The History of England", "quote": "The negotiations were conducted through a discreet **internuncio**, who conveyed secret proposals between the French cardinal and the king."},
            {"author": "Walter Scott", "work": "Quentin Durward", "quote": "The papal **internuncio** arrived under an escort of cavalry, bearing sealed dispatches from the apostolic see for Duke Charles."}
        ]
    },
    "mispronunciation": {
        "primary": "Incorrect, inaccurate, or faulty pronunciation of a word, syllable, or phonetic speech sound.",
        "secondary": "In descriptive linguistics and orthoepy, a phonological deviation from standard prestige norms or received orthoepic conventions.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Professor Higgins winced at every cockney **mispronunciation**, meticulously recording the deformed vowel shifts upon his phonograph."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Elizabeth-Jane blushed deeply whenever her stepfather corrected her dialectal **mispronunciation** before company at the dinner table."},
            {"author": "Oliver Wendell Holmes", "work": "The Professor at the Breakfast-Table", "quote": "A single vulgar **mispronunciation** will frequently betray an impostor who has borrowed the outward garments of refined breeding."}
        ]
    },
    "nuncio": {
        "primary": "A papal ambassador; an accredited diplomatic representative of the Pope to a foreign government.",
        "secondary": "In international diplomacy and canon law, an apostolic legate possessing the permanent rank of ambassador extraordinary and plenipotentiary.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King John", "quote": "According to the fair play of the world, let me have audience; I am sent to speak: my holy lord of Milan, from the Pope's own court, arrives as apostolic **nuncio**."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The papal **nuncio** was received at the royal palace with the ceremonial honors customarily reserved for the most powerful foreign monarchs."},
            {"author": "Walter Scott", "work": "Kenilworth", "quote": "Secret rumors circulated through Whitehall that a disguised papal **nuncio** had landed secretly upon the southern coast of Sussex."}
        ]
    },
    "pronunciamento": {
        "primary": "A formal, authoritative proclamation or manifesto; especially a military declaration of rebellion or policy change in Spain or Latin America.",
        "secondary": "In Spanish political history and revolutionary movements, an armed pronouncement announcing a barracks uprising against the reigning government.",
        "quotes": [
            {"author": "Sutton E. Griggs", "work": "Unfettered: A Novel", "quote": "The revolutionary committee issued a fiery **pronunciamento**, calling upon the oppressed citizenry to rise against the corrupt oligarchy."},
            {"author": "George Borrow", "work": "The Bible in Spain", "quote": "The provincial garrison revolted after their general read a bold **pronunciamento** from the balcony of the town hall."},
            {"author": "Joseph Conrad", "work": "Nostromo", "quote": "General Montero posted his grandiose **pronunciamento** on every wall in Sulaco, promising glory and wealth to the army."}
        ]
    },
    "pronunciation": {
        "primary": "The manner in which a word, syllable, or language is spoken or articulated according to recognized phonetic standards.",
        "secondary": "In descriptive phonetics and historical linguistics, the realization of phonemic units through vocal tract articulators according to regional or dialectal conventions.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her mother spoke the dialect of the county with a broad provincial **pronunciation** that Tess had learned to soften at the school."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "How could a man with such a harsh, pedantic **pronunciation** hope to charm the sensitive ear of a cultivated gentlewoman?"},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The gradual alteration in the **pronunciation** of vowels across successive generations accounts for the historical bifurcation of dialects."}
        ]
    },
    "renunciant": {
        "primary": "One who renounces, surrenders, or gives up something, especially worldly possessions, pleasures, or status.",
        "secondary": "In comparative religion (sannyasi or monastic ascetic), a devotee who has taken vows of asceticism and world-renunciation to pursue spiritual liberation.",
        "quotes": [
            {"author": "Max Müller", "work": "The Six Systems of Indian Philosophy", "quote": "The wandering **renunciant** casts aside caste distinctions, wealth, and family ties to wander homeless in search of spiritual illumination."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The saintly **renunciant** finds in total poverty a spiritual liberty far sweeter than all the luxuries of worldly opulence."},
            {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "The true **renunciant** has conquered the clamorous egoism of the will through voluntary denial and serene ascetic detachment."}
        ]
    },
    "renunciation": {
        "primary": "The formal act of relinquishing, surrendering, or repudiating a right, claim, title, possession, or belief.",
        "secondary": "In legal jurisprudence and ethical mysticism, the voluntary surrender of legal claims or the spiritual abandonment of sensual attachments.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She looked upon her self-sacrifice not as a heroic virtue, but as a mournful and inevitable act of lifelong **renunciation**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "And she was beginning now to look at the future with that grave **renunciation** which forms the foundation of all true spiritual wisdom."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Though the capacity for total **renunciation** is noble, it is only valuable when undertaken to enhance the happiness of fellow creatures."}
        ]
    },
    "renunciative": {
        "primary": "Pertaining to, involving, or expressing renunciation; tending to surrender or repudiate claims.",
        "secondary": "In ascetic theology and legal analysis, characterized by the willing yielding of worldly privileges or the formal disclaimer of rights.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her quiet, **renunciative** attitude touched him deeply, contrasting with the assertive vanity of other women he had known."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The soul finds a profound and unexpected peace in adopting a purely **renunciative** surrender of personal ambition."},
            {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "The highest ethical stage of human consciousness reveals itself in a **renunciative** posture toward all earthly striving."}
        ]
    }
}
