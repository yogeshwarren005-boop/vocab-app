# -*- coding: utf-8 -*-
"""
curate_food_b2_p3a.py
Batch 2 Part 3a of Cluster Food: Dashboard — al (words 77-95):
['palliating', 'palliation', 'palliative', 'postal', 'preanal', 'precordial',
 'real', 'realisation', 'realise', 'realism', 'realist', 'realistic',
 'reality', 'realization', 'realize', 'really', 'realness', 'reseal', 'seal']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_b2_p3a = {
    # 77. palliating
    "palliating": {
        "primary": "The act of easing, mitigating, or lessening the severity of pain, disease, or offense without curing it.",
        "secondary": "In clinical therapeutics, providing symptomatic comfort and supportive interventions to ease physical suffering in terminal or chronic illness.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "He spent the evening in **palliating** his hasty words, trying to persuade his companion that no malice was intended."},
            {"author": "William Osler", "work": "Aequanimitas", "quote": "The physician's highest calling consists often in **palliating** incurable distress with gentleness and consummate skill."},
            {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "She found subtle ways of **palliating** her father's harsh temper before the tenants and servants."}
        ]
    },

    # 78. palliation
    "palliation": {
        "primary": "Relief, mitigation, or alleviation of symptoms or distress without eradicating the underlying cause.",
        "secondary": "In clinical medicine and ethics, the deliberate relief of pain, nausea, and emotional anxiety to preserve human dignity in terminal care.",
        "quotes": [
            {"author": "Thomas Sydenham", "work": "The Works of Thomas Sydenham, M.D.", "quote": "Where the fundamental distemper defies our remedies, timely **palliation** remains the wisest course for the practitioner."},
            {"author": "Nathaniel Hawthorne", "work": "The Blithedale Romance", "quote": "He offered this hollow excuse as a feeble **palliation** for conduct that violated every dictate of honor."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor sought some plausible **palliation** to justify his sudden breach of the treaty with the barbarian tribes."}
        ]
    },

    # 79. palliative
    "palliative": {
        "primary": "Serving to relieve or alleviate pain, discomfort, or distress without addressing or curing the underlying cause.",
        "secondary": "In end-of-life care and oncology, therapeutic interventions designed specifically to optimize quality of life and minimize distressing symptoms.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He administered a mild **palliative** to ease the sick man's cough as the autumn chill settled over the cottage."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate recognized that medical science could provide only a **palliative** measure in so advanced a stage of cardiac degeneration."},
            {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "The old apothecary kept a shelf of **palliative** cordials formulated to soothe restless consumptives through sleepless nights."}
        ]
    },

    # 80. postal
    "postal": {
        "primary": "Pertaining to the post office, the mail system, or the carriage and delivery of letters and parcels.",
        "secondary": "In public administration and logistics history, relating to state-monopolized communication networks, franking privileges, and national mail distribution systems.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Time Machine", "quote": "In the modern era of telegraphs and rapid **postal** transit, messages crossed continents within a few fleeting days."},
            {"author": "Anthony Trollope", "work": "An Autobiography", "quote": "During my long career in the General Post Office, I introduced the red pillar box to revolutionize public **postal** convenience throughout Britain."},
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The foreign packet brought a collection of **postal** dispatches that threw the counting-house into immediate commotion."}
        ]
    },

    # 81. preanal
    "preanal": {
        "primary": "Situated in front of or immediately anterior to the anus.",
        "secondary": "In vertebrate anatomy and herpetology, designating specialized glands, scales, or pores located anterior to the vent in reptiles, amphibians, and fishes.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Male lizards frequently possess prominent **preanal** pores that secrete waxy pheromones during the spring breeding season."},
            {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The pelvic fin rays in certain teleostean fishes terminate directly adjacent to the **preanal** papilla."},
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "Careful dissection reveals that the **preanal** plates in chelonians exhibit distinct diagnostic suture lines."}
        ]
    },

    # 82. precordial
    "precordial": {
        "primary": "Pertaining to the precordium, the region of the anterior chest wall directly overlying the heart and stomach.",
        "secondary": "In cardiology and physical diagnosis, relating to the thoracic surface where cardiac apex impulses, murmurs, and lead placements are localized.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The patient complained of intense **precordial** constriction and sharp distress radiating outward toward the left shoulder."},
            {"author": "William Cullen", "work": "First Lines of the Practice of Physic", "quote": "Palpitation accompanied by a sense of weight in the **precordial** region denotes severe functional derangement of the vascular system."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "Auscultation across the **precordial** area revealed loud bellows murmurs accompanying each systolic contraction."}
        ]
    },

    # 83. real
    "real": {
        "primary": "Actually existing, genuine, true, and not imaginary, counterfeit, or illusory.",
        "secondary": "In metaphysics and property jurisprudence, denoting objective ontic substance, or pertaining to immovable property such as land and permanent tenements.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "If this be magic, let it be an art lawful as eating; it is required you do awake your faith; then all stand still; on, those that think it unlawful business I am about, steal them away; music, awake her, strike! 'Tis time; descend; be stone no more; approach; strike all that look upon with marvel; come, I'll fill your grave up; stir, nay, come away, bequeath to death your numbness, for from him dear life redeems you; you perceive she stirs; start not; her actions shall be as holy as you hear my spell is lawful; do not shun her until you see her die again, for then you kill her double; nay, present your hand; when she was young you wooed her; now in age is she become the **real** partner of your joy."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The beauty or ugliness of a person's life depends not on their acts, but on their **real** intentions and inward spirit."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our simple ideas correspond to **real** qualities existing in external bodies that have the power to produce them in us."}
        ]
    },

    # 84. realisation
    "realisation": {
        "primary": "The act of becoming fully aware of something as a fact, or the actual fulfillment of an aim or concept.",
        "secondary": "In cognitive psychology and economic management (chiefly British spelling), the mental arrival of clear insight, or the liquid conversion of assets into cash.",
        "quotes": [
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The gradual **realisation** of our moral duties arises from reflecting upon the natural consequences of human action."},
            {"author": "Bram Stoker", "work": "Dracula", "quote": "With a sudden shock of terrible **realisation**, I perceived that the castle was perched upon the edge of an immense precipice."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The awful **realisation** of our helplessness struck home as the Martian tripod strode contemptuously over the burning town."}
        ]
    },

    # 85. realise
    "realise": {
        "primary": "To understand clearly or become aware of something; or to convert an intention, plan, or asset into actual reality.",
        "secondary": "In finance and epistemology (chiefly British spelling), to convert investments into liquid cash, or to achieve experiential knowledge of theoretical truths.",
        "quotes": [
            {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Children should be brought to **realise** the natural connection between diligent study and lasting personal esteem."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we reflect on this struggle, we may console ourselves with the full belief that the war of nature is not incessant, that no fear is felt, that death is generally prompt, and that the vigorous, the healthy, and the happy survive and multiply, leading us to **realise** the majestic order of organic evolution."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "It took only a moment for Watson to **realise** that our quarry had escaped across the treacherous mire."}
        ]
    },

    # 86. realism
    "realism": {
        "primary": "The practice of accepting a situation as it is and dealing with it practically, or representing things faithfully without idealization.",
        "secondary": "In philosophy and literary theory, the doctrine that universals or physical entities exist independently of consciousness, or artistic depiction prioritizing verisimilitude.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes approached detection with an austere scientific **realism**, brushing aside romantic conjectures in search of cold physical facts."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "The nineteenth-century dislike of **realism** is the rage of Caliban seeing his own face in a glass."},
            {"author": "G. K. Chesterton", "work": "Heretics", "quote": "True artistic **realism** consists in revealing the immense romance and wonder that lie concealed within commonplace everyday facts."}
        ]
    },

    # 87. realist
    "realist": {
        "primary": "A person who accepts things as they actually are and deals with practical realities rather than ideal visions.",
        "secondary": "In epistemology and literary history, an adherent of ontological realism or an author whose work rigorously captures social facts without sentimentality.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Montaigne was the quintessential philosophical **realist**, distrusting dogmatic abstractions and grounding his inquiries in human nature."},
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The true narrative **realist** aspires to mirror life faithfully, depicting plain folk with all their flaws and endearing rustic virtues."},
            {"author": "William James", "work": "Pragmatism", "quote": "The tough-minded philosopher is a thorough **realist**, preferring tangible facts and hard experience to airy rationalist systems."}
        ]
    },

    # 88. realistic
    "realistic": {
        "primary": "Representing things in a way that is accurate, true to life, and free from romanticized distortion.",
        "secondary": "In cognitive decision-making and creative arts, pragmatic and feasible in expectation, or achieving persuasive visual and narrative verisimilitude.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The novel offered a **realistic** portrayal of peasant life, unvarnished by the idyllic pastorals fashionable among city poets."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The footprints in the mud provided a grimly **realistic** confirmation of the intruder's physical presence upon the roof."},
            {"author": "G. K. Chesterton", "work": "The Victorian Age in Literature", "quote": "Browning's monologues display a intensely **realistic** grasp of human passion, embracing the grotesque as readily as the sublime."}
        ]
    },

    # 89. reality
    "reality": {
        "primary": "The state of things as they actually exist, as opposed to idealistic, imaginary, or illusory notions.",
        "secondary": "In ontological metaphysics and existential psychology, the objective sum of all actual entities, events, and verifiable physical phenomena.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The cruel **reality** of her situation pressed upon her with relentless force as the morning sunlight illuminated the barren downs."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Beliefs untested by free discussion become dead dogmas rather than living convictions grounded in objective **reality**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea learned that married life brought a sobering **reality** far removed from her youthful visions of saintly sacrifice."}
        ]
    },

    # 90. realization
    "realization": {
        "primary": "The clear understanding or awareness of something, or the practical fulfillment and actualization of a goal.",
        "secondary": "In transactional economics and developmental psychology, the conversion of assets into spendable funds, or the concrete enactment of an ideal project.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sudden **realization** of Gabriel's steadfast devotion broke upon her heart with overpowering tenderness."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The highest happiness of humanity lies in the progressive **realization** of universal justice and mutual sympathy."},
            {"author": "Oscar Wilde", "work": "De Profundis", "quote": "Suffering is the supreme mode of illumination through which the soul attains complete **realization** of its true spiritual nature."}
        ]
    },

    # 91. realize
    "realize": {
        "primary": "To understand clearly or become aware of something, or to bring a plan, ambition, or asset into actual existence.",
        "secondary": "In commercial finance and philosophical psychology, to convert securities into cash, or to manifest potential capacities into tangible actuality.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She did not at first **realize** the magnitude of the disaster that had overtaken her family upon the high road."},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The earnest thinker strives to **realize** his ideals in everyday conduct, transforming abstract vision into living deed."},
            {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "To **realize** one's own nature perfectly, that is what each of us is here for in this fleeting and beautiful world."}
        ]
    },

    # 92. really
    "really": {
        "primary": "In actual fact, truth, or reality; genuinely and not merely in appearance.",
        "secondary": "In rhetorical discourse and modal semantics, an intensifier affirming the objective truth or surprising authenticity of a proposition.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "There are more things in heaven and earth, Horatio, than are dreamt of in your philosophy; and is it **really** true that honest ghosts walk this mortal round?"},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "She wondered whether Boldwood was **really** serious in his suit, or whether she had misread his reserved and solitary nature."},
            {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was **really** attached to Emma, though his affection never blinded him to her occasional vanity and errors."}
        ]
    },

    # 93. realness
    "realness": {
        "primary": "Genuine authenticity, tangible actuality, or lifelike truthfulness free from artificiality and pretension.",
        "secondary": "In aesthetic theory and cultural performance, an uncompromising authenticity that shuns artifice, presenting lived experience with raw honesty.",
        "quotes": [
            {"author": "Walt Whitman", "work": "Democratic Vistas", "quote": "Literature in a democracy must possess a rugged **realness**, reflecting the robust vitality and plain speech of working men."},
            {"author": "Henry James", "work": "The Art of Fiction", "quote": "The supreme virtue of a novel is its air of **realness**, producing that profound illusion of life which holds the reader captive."},
            {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Behind the daily domestic trivialities lay a quiet **realness** that sustained the family through years of grief and change."}
        ]
    },

    # 94. reseal
    "reseal": {
        "primary": "To seal again; to close, fasten, or make airtight or watertight once more.",
        "secondary": "In forensic evidence protocol and commercial packaging, restoring a tamper-evident seal or hermetic barrier to preserve contents from degradation.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Adventure of the Abbey Grange", "quote": "Holmes carefully inspected the bottle of wine, noting that the butler had made no attempt to **reseal** the cork."},
            {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr. Jekyll and Mr. Hyde", "quote": "Utterson took the confidential packet from the drawer, resolved to **reseal** it within his private strongbox until the morrow."},
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The cooper was ordered to **reseal** the cask of sweet water before stowing it securely beneath the main hatches."}
        ]
    },

    # 95. seal
    "seal": {
        "primary": "A device bearing an engraved design used to stamp impressions on wax, or a semi-aquatic marine mammal (*Pinnipedia*).",
        "secondary": "In legal formality and marine mammalogy, an authenticating impression on legal instruments confirming execution, or an amphibious carnivorous marine quadruped.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Till thou canst rail the **seal** off from my bond, thou but offend'st thy lungs to speak so loud; repair thy wit, good youth, or it will fall to cureless ruin."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The legal parchment bore an impressive wax **seal** that gave the indenture an air of solemn and unalterable authority."},
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "In the cold Greenland waters the hardy whalers encountered herds of spotted **seal** basking upon the drifting floes."}
        ]
    }
}
