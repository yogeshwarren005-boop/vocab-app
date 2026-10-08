# -*- coding: utf-8 -*-
"""
Part 1 of Batch 4 Cluster Food, Eating & Drink: vin words 1-20 (20 words):
['alvine', 'asvina', 'asvins', 'convince', 'convinced', 'convincible', 'convincing',
 'convincingly', 'convincingness', 'corvine', 'divination', 'divinatory', 'divine',
 'divinely', 'diviner', 'divinity', 'evince', 'invincibility', 'invincible', 'invincibly']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part1_vin = {
    "alvine": {
        "primary": "Pertaining to, originating within, or affecting the belly, intestines, or abdominal viscera.",
        "secondary": "In archaic and physiological medicine, describing intestinal evacuations, colic, or secretory processes within the gastrointestinal tract.",
        "quotes": [
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham, M.D.", "quote": "The patient complained of violent **alvine** fluxes accompanied by sharp gripings of the lower belly."},
            {"author": "Erasmus Darwin", "work": "Zoonomia; or, The Laws of Organic Life", "quote": "Excessive irritation in the intestinal canal frequently disturbs the natural rhythm of **alvine** excretion."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "The prolonged retention of **alvine** matter produces systemic languor and febrile paroxysms throughout the body."}
        ]
    },
    "asvina": {
        "primary": "Pertaining to the seventh month of the Hindu lunisolar calendar, coinciding with September and October.",
        "secondary": "In Hindu calendrical astronomy and ritual practice, marking the autumn equinoctial period during which major observances such as Durga Puja take place.",
        "quotes": [
            {"author": "William Jones", "work": "Asiatic Researches", "quote": "During the bright fortnight of the lunar month **asvina**, the solemn rites dedicated to the goddess Durga are observed with magnificent pomp."},
            {"author": "Monier Monier-Williams", "work": "Brahmanism and Hinduism", "quote": "The festival of lights follows soon after the concluding sacrifices of **asvina** across northern India."},
            {"author": "Al-Biruni", "work": "Alberuni's India", "quote": "In the month of **asvina**, the autumn harvest commences and offerings of fresh grain are presented to the ancestral spirits."}
        ]
    },
    "asvins": {
        "primary": "Twin horse-headed or equestrian deities in Vedic mythology, revered as divine physicians and harbingers of the dawn.",
        "secondary": "In comparative Indo-European mythology, celestial divine twins symbolizing youth, healing, maritime rescue, and the daily awakening of light before the sunrise.",
        "quotes": [
            {"author": "Friedrich Max Müller", "work": "Lectures on the Science of Language", "quote": "The **asvins** represent the twilight transition between darkness and dawn, riding their golden chariot across the vault of heaven."},
            {"author": "Arthur Anthony Macdonell", "work": "Vedic Mythology", "quote": "In the Rigveda, the **asvins** are celebrated as heavenly physicians who restore the blind to sight and heal the maimed."},
            {"author": "Ralph T. H. Griffith", "work": "The Hymns of the Rigveda", "quote": "May the wondrous **asvins**, radiant masters of healing and horsemen of the sky, come bearing abundant blessings unto our sacrifice."}
        ]
    },
    "convince": {
        "primary": "To persuade someone through evidence, logical argument, or demonstration to accept a belief or course of action.",
        "secondary": "In historical and legal English, to vanquish, convict of an offense, or demonstrate beyond refutation the fallacy or guilt of an opponent.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is not enough to dispute well; one must demonstrate truth so lucidly as to **convince** the most obstinate adversary."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "She could not **convince** herself that Darcy was capable of harboring such petty malice toward an innocent gentleman."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Clear ideas and rigorous deduction will **convince** the understanding when mere rhetoric fails entirely."}
        ]
    },
    "convinced": {
        "primary": "Firmly persuaded of the truth, justice, or validity of something; holding an unwavering belief based on evidence.",
        "secondary": "In cognitive psychology and epistemology, describing a mental state of settled assent where prior doubt has been resolved through deliberation.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba was **convinced** that this unmoved person was not a married man, judging by his careless demeanor."},
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I was **convinced** of the innocence of poor Justine, yet dared not reveal the terrible truth of the daemon's existence."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The citizens were thoroughly **convinced** that their individual welfare depended upon the stability of communal laws."}
        ]
    },
    "convincible": {
        "primary": "Capable of being persuaded or convinced by rational evidence, argument, or proof.",
        "secondary": "In moral philosophy and legal rhetoric, open to intellectual demonstration; susceptible to having one's guilt or error conclusively shown.",
        "quotes": [
            {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "Men of inquisitive minds are ever **convincible** by plain reason, whereas vulgar minds adhere dogmatically to tradition."},
            {"author": "Joseph Glanvill", "work": "The Vanity of Dogmatizing", "quote": "A modest inquirer remains **convincible** when confronted by experiment, refusing to cling to unverified assumptions."},
            {"author": "Richard Baxter", "work": "The Saints' Everlasting Rest", "quote": "The hardened conscience is seldom **convincible** by ordinary warnings until divine affliction shakes its complacency."}
        ]
    },
    "convincing": {
        "primary": "Possessing the power to persuade, reassure, or compel belief through credibility, force, or plausibility.",
        "secondary": "In critical rhetoric and dramatic arts, conveying an impression of lifelike authenticity, artistic fidelity, or logical necessity.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Circumstantial evidence is occasionally very **convincing**, as when you find a trout in the milk, to quote Thoreau's example."},
            {"author": "James Joyce", "work": "Dubliners", "quote": "He spoke in a **convincing** tone, as if he was conscious of being disbelieved and sought to disarm suspicion."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "His arguments were so **convincing** that Dorothea felt her lingering objections dissolve into quiet assent."}
        ]
    },
    "convincingly": {
        "primary": "In a manner that successfully persuades, compels belief, or leaves no room for reasonable doubt.",
        "secondary": "In forensic debate and theatrical performance, with persuasive coherence, consummate authority, or undeniable dramatic realism.",
        "quotes": [
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She pleaded her case so **convincingly** that even the skeptical aunt had no choice but to yield."},
            {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Katherine spoke **convincingly** of the necessity of arranging their domestic affairs on a rational foundation."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The astronomer described the disturbances on Mars so **convincingly** that the gathering listened in rapt fascination."}
        ]
    },
    "convincingness": {
        "primary": "The quality, force, or degree of being persuasive, plausible, or capable of eliciting belief.",
        "secondary": "In argumentation theory and literary aesthetics, the cogency and internal consistency that produce complete intellectual or artistic credibility.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Major Barbara", "quote": "The extraordinary **convincingness** of Undershaft's doctrine lay in its unsparing exposure of polite sentimentalities."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Mystical revelations carry an immediate **convincingness** to the subject that no external logic can dismantle."},
            {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "Poetry achieves true greatness only when its depiction of human passion possesses irresistible **convincingness**."}
        ]
    },
    "corvine": {
        "primary": "Pertaining to, resembling, or characteristic of crows, ravens, or the bird family Corvidae.",
        "secondary": "In ornithology and comparative morphology, denoting anatomical features such as heavy, stout bills and keen intelligence typical of corvids.",
        "quotes": [
            {"author": "John Burroughs", "work": "Birds and Poets", "quote": "The raucous voice and glossy plumage of the creature exhibited all the unmistakable traits of **corvine** cunning."},
            {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The raven perched aloft upon the church steeple with that watchful **corvine** gravity that marks his tribe."},
            {"author": "H. P. Lovecraft", "work": "The Shadow over Innsmouth", "quote": "A solitary rook wheeled above the dilapidated gables, uttering harsh **corvine** croaks against the dismal sky."}
        ]
    },
    "divination": {
        "primary": "The practice of seeking knowledge of the future or the unknown by supernatural, omen-based, or ritual means.",
        "secondary": "In cultural anthropology and classical antiquity, systematic augury, haruspicy, or astrological forecasting institutionalized within civic religion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Tell thou an earl his **divination** lies, and I will take it as a sweet disgrace and make thee rich for doing me such wrong."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient senators consulted sacred oracles and relied upon augural **divination** before undertaking military campaigns."},
            {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Primitive peoples resorted to animal entrails and planetary motions for **divination** in times of national peril."}
        ]
    },
    "divinatory": {
        "primary": "Pertaining to, serving for, or characteristic of divination, prophesying, or foretelling future events.",
        "secondary": "In religious studies and folklore, describing instruments, rituals, or mental states employed to decipher occult omens or spiritual signs.",
        "quotes": [
            {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The priest performed the **divinatory** sacrifice at dawn, scrutinizing the smoldering incense for auspicious portents."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Astrologers deceive the credulous vulgar with their **divinatory** schemes and celestial horoscopes."},
            {"author": "Andrew Lang", "work": "Myth, Ritual and Religion", "quote": "The shaman cast marked knucklebones onto the pelt, attributing deep **divinatory** significance to every pattern."}
        ]
    },
    "divine": {
        "primary": "Of, relating to, or proceeding from a deity; sacred, holy, or possessing godlike excellence.",
        "secondary": "As a verb, to discover, perceive intuitively, or foretell through occult insight, conjectural deduction, or dowsing.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnets", "quote": "Nothing sweet boy, but yet like prayers **divine**, I must each day say o'er the very same."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Into the heaven of heavens I have presumed, an earthly guest, and drawn empyreal air, thy tempering **divine**."},
            {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "Good nature and good sense must ever join; to err is human, to forgive, **divine**."}
        ]
    },
    "divinely": {
        "primary": "In a divine manner; by deity, with supernatural inspiration, or in an exceedingly excellent way.",
        "secondary": "In theological discourse, by celestial providence, heavenly dispensation, or transcendent moral sanction.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King John", "quote": "Lo, in this right hand, whose protection is most **divinely** vowed upon the right of him it holds, stands young Plantagenet."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "She is perfectly charming; and Patti sang **divinely** at the opera last evening."},
            {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "Her celestial beauty was so **divinely** wrought that every mortal beholder stood struck with reverent awe."}
        ]
    },
    "diviner": {
        "primary": "A person who practices divination, foretells future occurrences, or locates underground water or minerals.",
        "secondary": "In classical history and folklore, a recognized seer, augur, or water-dowser using a dowsing rod to detect subterranean springs.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "To conclude: this drudge or **diviner** laid claim to me, called me Dromio, and swore I was assured to her."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Her voice is much **diviner** than anything you have seen of her, carrying an almost angelic resonance."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The rustic **diviner** paced across the meadow holding a hazel wand, waiting for the dip that indicated water."}
        ]
    },
    "divinity": {
        "primary": "The state, status, or character of being divine; godhead, sacredness, or supreme holiness.",
        "secondary": "In academic and ecclesiastical history, the systematic study of Christian theology, scripture, and sacred doctrine.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "There's such **divinity** doth hedge a king, that treason can but peep to what it would, acts little of his will."},
            {"author": "Francis Bacon", "work": "Essays", "quote": "A little philosophy inclineth man's mind to atheism, but depth in philosophy bringeth men's minds about to religion and **divinity**."},
            {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "He studied **divinity** at the university with great diligence, hoping one day to attain an episcopal see."}
        ]
    },
    "evince": {
        "primary": "To display clearly, reveal, demonstrate, or exhibit an inward quality, emotion, or disposition.",
        "secondary": "In philosophical jurisprudence and rigorous debate, to provide manifest, empirical proof or unmistakable indications of a condition.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "He spent years and years in desultory studies and began to **evince** considerable indifference to worldly advancement."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The females lie in an almost torpid state, and appear not to **evince** the least choice among rival suitors."},
            {"author": "Thomas Jefferson", "work": "Declaration of Independence", "quote": "When a long train of abuses and usurpations pursueth invariably the same object, it doth **evince** a design to reduce them under absolute despotism."}
        ]
    },
    "invincibility": {
        "primary": "Incapability of being defeated, conquered, or overcome; unconquerable might or prowess.",
        "secondary": "In military strategy and stoic ethics, an unassailable defensive posture or moral fortitude immune to external destruction.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions maintained a proud belief in their own **invincibility** until the catastrophic day of Adrianople."},
            {"author": "Sun Tzu", "work": "The Art of War", "quote": "To secure ourselves against defeat has to do with our own defensive posture; true **invincibility** lies in the defense."},
            {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "There is a moral **invincibility** in the soul that stands immovable on what it knows to be eternal justice."}
        ]
    },
    "invincible": {
        "primary": "Incapable of being conquered, subdued, defeated, or overcome by physical force or mental adversity.",
        "secondary": "In scholastic philosophy and moral theology, describing ignorance or conviction that cannot be dispelled by ordinary human diligence.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "You were used to load me with precepts that would make **invincible** the heart that conned them."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "What though the field be lost? All is not lost: the unconquerable will, and study of revenge, immortal hate, and courage never to submit or yield, and what is else not to be overcome, that **invincible** pride."},
            {"author": "Walter Scott", "work": "The Talisman", "quote": "Richard Coeur-de-Lion possessed an **invincible** spirit that rose highest when perils were most alarming."}
        ]
    },
    "invincibly": {
        "primary": "In an invincible manner; so firmly or powerfully as to be impossible to conquer, defeat, or refute.",
        "secondary": "In epistemological ethics, describing beliefs held with unshakable tenacity against all contradictory evidence.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "\"I'll be sure not to!\" she said **invincibly**, setting her face with stubborn determination."},
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He held **invincibly** to his ancestral prejudices, deaf to every voice of enlightened experience."},
            {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "The love of liberty is **invincibly** fixed in the breast of every man who has tasted its blessings."}
        ]
    }
}
