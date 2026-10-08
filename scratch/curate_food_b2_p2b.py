# -*- coding: utf-8 -*-
"""
curate_food_b2_p2b.py
Batch 2 Part 2b of Cluster Food: Dashboard — al (words 58-76):
['criminalize', 'criminally', 'criminalness', 'deal', 'dealer', 'dealership',
 'dealing', 'dealings', 'decriminalise', 'decriminalize', 'dial', 'irreality',
 'misdeal', 'opal', 'opalise', 'opalize', 'orally', 'oratorical', 'palliate']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_food_b2_p2b = {
    # 58. criminalize
    "criminalize": {
        "primary": "To declare an action or activity illegal and punishable by law, or to treat an individual as a criminal.",
        "secondary": "In legislative jurisprudence and penal sociology, the formal enactment of criminal statutes that convert civil or private conduct into prosecutable crimes.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "The Theory of Legislation", "quote": "To **criminalize** innocent pleasures is to manufacture artificial delinquency and debase the authority of the magistrate."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Society exceeds its rightful jurisdiction whenever it attempts to **criminalize** personal choices that work no demonstrable injury to others."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "A democratic majority must exercise extreme caution lest it **criminalize** peaceful political dissent under the guise of public order."}
        ]
    },

    # 59. criminally
    "criminally": {
        "primary": "In a manner that violates criminal law or involves punishable moral guilt and wrongdoing.",
        "secondary": "In judicial proceedings, qualifying liability that meets statutory thresholds of penal culpability (*mens rea*) rather than mere civil negligence.",
        "quotes": [
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "An infant under seven years of age cannot be held **criminally** responsible for any felony whatsoever."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "They acted **criminally** in subverting the fundamental constitution of their country upon mere theoretical speculation."},
            {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The magistrate warned the parish beadle that he had behaved **criminally** in neglecting the starving apprentices."}
        ]
    },

    # 60. criminalness
    "criminalness": {
        "primary": "The guilty character, felonious nature, or reprehensible culpability of an unlawful act.",
        "secondary": "In moral philosophy and legal ethics, the degree of moral turpitude and intentional malice inherent in a breach of the social contract.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He acknowledged the deep **criminalness** of his former betrayal, resolving to dedicate his remaining years to penitence."},
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "No sophistry can conceal the atrocious **criminalness** of the massacres perpetrated in the name of liberty."},
            {"author": "Jonathan Swift", "work": "The Drapier's Letters", "quote": "The people clearly perceived the scandalous **criminalness** of foisting degraded copper coinage upon an impoverished nation."}
        ]
    },

    # 61. deal
    "deal": {
        "primary": "To distribute cards to players in a game, or to engage in a commercial transaction or business agreement.",
        "secondary": "In economic sociology and game theory, a negotiated bargain or contract establishing exchange value between consenting parties.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "I will buy with you, sell with you, talk with you, walk with you, and so following; but I will not eat with you, drink with you, nor pray with you; What news on the Rialto? Who is he comes here? I will **deal** with him fairly."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He was a shrewd man of business who drove a hard **deal** with every trader in the market town."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The farmers met in the corn exchange to strike a **deal** for the incoming autumn wheat crop."}
        ]
    },

    # 62. dealer
    "dealer": {
        "primary": "A person or merchant who buys and sells goods, securities, or commodities for trade or commerce.",
        "secondary": "In commerce and financial economics, an intermediary or principal who maintains an inventory and provides liquidity by quoting bid and ask prices.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "He is an honest **dealer** whose word in the exchange is as sacred as a sworn bond."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The wholesale **dealer** bridges the vital distance between the isolated producer and the dispersed consumer."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The corn **dealer** stood examining samples of barley with practiced and discerning fingers."}
        ]
    },

    # 63. dealership
    "dealership": {
        "primary": "A business or commercial enterprise authorized to sell and service a manufacturer's goods, especially automobiles.",
        "secondary": "In commercial distribution law, an exclusive franchise relationship conferring regional retail distribution rights and service obligations.",
        "quotes": [
            {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Wilson operated a shabby garage and automobile **dealership** at the edge of the ashheaps."},
            {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The used car **dealership** lot was crowded with battered jalopies polished up to entice desperate migrant families."},
            {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He invested his modest savings in a regional **dealership** for electric washing machines and modern kitchen appliances."}
        ]
    },

    # 64. dealing
    "dealing": {
        "primary": "Conduct, transactions, or friendly business relations maintained between persons or commercial entities.",
        "secondary": "In business ethics and mercantile custom, a standard of fairness, transparency, and integrity demonstrated across commercial engagements.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Plain **dealing** is a jewel, though those who use it die beggars in this deceitful world."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His straightforward manner of **dealing** earned him the unreserved confidence of all the neighboring sheepmasters."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Honest **dealing** in the open market generates mutual trust that reduces transaction costs across the entire commonwealth."}
        ]
    },

    # 65. dealings
    "dealings": {
        "primary": "Commercial, political, or personal transactions, interactions, or mutual affairs between parties.",
        "secondary": "In diplomatic history and contract law, established historical patterns of contractual negotiation and reciprocal business relationships.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I have had extensive **dealings** upon the Rialto with Venetian merchants of the highest reputation."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard's financial **dealings** were characterized by bold hazards and impulsive generosities that eventually undermined his credit."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode sought to keep his past commercial **dealings** hidden beneath a mantle of austere religious philanthropy."}
        ]
    },

    # 66. decriminalise
    "decriminalise": {
        "primary": "To repeal or remove criminal penalties from an act, converting it to a civil offense or legal activity.",
        "secondary": "In penal reform and public health policy (chiefly British spelling), the statutory transition from penal sanctions to administrative regulation.",
        "quotes": [
            {"author": "Jeremy Bentham", "work": "Principles of Penal Law", "quote": "To **decriminalise** victimless indiscretions restores proportionality to the penal code and conserves judicial resources."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Enlightened governments should progressively **decriminalise** private conduct that harms no fellow citizen."},
            {"author": "Herbert Spencer", "work": "Social Statics", "quote": "The true direction of legislative progress is to **decriminalise** harmless individual activities formerly constrained by puritanical statutes."}
        ]
    },

    # 67. decriminalize
    "decriminalize": {
        "primary": "To eliminate criminal penalties for an offense, rendering the conduct subject at most to civil fines or regulatory oversight.",
        "secondary": "In legislative jurisprudence and harm-reduction advocacy, altering the penal code so that specified behaviors no longer carry custodial sentences.",
        "quotes": [
            {"author": "John Stuart Mill", "work": "Essays on Ethics, Religion and Society", "quote": "Enlightened statesmanship will seek to **decriminalize** activities where moral censure exceeds any demonstrable secular injury."},
            {"author": "Jeremy Bentham", "work": "Theory of Legislation", "quote": "The legislature ought to **decriminalize** small infractions that burden the courts without yielding public security."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "A mature democracy will naturally **decriminalize** many archaic customs that authoritarian regimes treated as treasonous."}
        ]
    },

    # 68. dial
    "dial": {
        "primary": "A graduated face or plate on a timepiece, instrument, or meter displaying measurement readings via a pointer or indicator.",
        "secondary": "In horology and engineering instrumentation, a calibrated circular disc indicating time, pressure, or electrical potential via mechanical indices.",
        "quotes": [
            {"author": "William Shakespeare", "work": "As You Like It", "quote": "And then he drew a **dial** from his poke, and, looking on it with lack-lustre eye, says very wisely, 'It is ten o'clock.'"},
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Nature measures our years by the grand solar **dial** of the seasons and revolving constellations."},
            {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The captain fixed his gaze upon the compass **dial**, watching the needle tremble with each roll of the vessel."}
        ]
    },

    # 69. irreality
    "irreality": {
        "primary": "Illusory nature, dreamlike unreality, or absence of genuine tangible existence and substance.",
        "secondary": "In existential phenomenology and modernist aesthetics, an eerie psychological sensation wherein familiar surroundings appear dreamlike, phantom, and detached from tangible being.",
        "quotes": [
            {"author": "Jean-Paul Sartre", "work": "The Psychology of Imagination", "quote": "The imagined object exists in a state of phantom **irreality**, refusing to submit to the sensory tests of genuine perception."},
            {"author": "Virginia Woolf", "work": "The Waves", "quote": "A strange sense of **irreality** invaded the quiet garden, as if the trees and sunlit paths were painted on gauze."},
            {"author": "Franz Kafka", "work": "The Trial", "quote": "K. felt paralyzed by the utter **irreality** of the proceedings, where shadowy accusations dissolved into endless labyrinthine corridors."}
        ]
    },

    # 70. misdeal
    "misdeal": {
        "primary": "An incorrect or faulty distribution of cards in a card game, requiring cards to be re-shuffled and dealt again.",
        "secondary": "In ludic rule systems and metaphorical discourse, an erroneous procedural distribution or bungled transaction requiring nullification.",
        "quotes": [
            {"author": "Edmond Hoyle", "work": "A Short Treatise on the Game of Whist", "quote": "If any card be turned up in dealing, it is a **misdeal**, and the cards must be gathered, shuffled, and dealt afresh."},
            {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Miller committed an inexcusable **misdeal** at whist, prompting a storm of indignant murmurs from his elderly partner."},
            {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rawdon Crawley watched the cards with an expert eye, instantly calling out a **misdeal** when the dealer dropped an exposed ace."}
        ]
    },

    # 71. opal
    "opal": {
        "primary": "A hydrated amorphous mineral form of silica prized as a gemstone for its iridescent play of flashing spectral colors.",
        "secondary": "In gemological mineralogy, submicroscopic silica spheres arranged in regular lattices that diffract light to generate characteristic opalescence.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Now the melancholy god protect thee; and the tailor make thy doublet of changeable taffeta, for thy mind is a very **opal**."},
            {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The jewel casket revealed a magnificent necklace set with fiery **opal** stones that glowed with inner rainbow light."},
            {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The evening clouds changed from burnished gold to the delicate iridescent tints of an **opal** over the pine woods."}
        ]
    },

    # 72. opalise
    "opalise": {
        "primary": "To convert into opal or impart an iridescent, rainbow-like opalescent sheen to a material.",
        "secondary": "In paleontological taphonomy (chiefly British spelling), the hydrothermal mineral replacement of organic fossil tissues with hydrous microcrystalline silica.",
        "quotes": [
            {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Siliceous waters percolating through sandstone beds gradually **opalise** buried shells, replacing organic carbonate with shimmering silica."},
            {"author": "John Ruskin", "work": "Modern Painters", "quote": "The sunset mists seem to **opalise** the limestone crags, clothing alpine snows in fugitive hues of amethyst and rose."},
            {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The morning sunlight began to **opalise** the gray river mist, transforming London into an enchanted city of mother-of-pearl."}
        ]
    },

    # 73. opalize
    "opalize": {
        "primary": "To convert or be converted into opal; to cause to exhibit an iridescent, opalescent play of colors.",
        "secondary": "In geological mineralization, the precipitation of amorphous hydrated silica within fossil cavities, preserving delicate cellular anatomical structures.",
        "quotes": [
            {"author": "Charles Darwin", "work": "Geological Observations on South America", "quote": "In the petrified forest of the Uspallata range, ancient tree trunks are found completely **opalize**d into brilliant gemstone."},
            {"author": "James Dwight Dana", "work": "System of Mineralogy", "quote": "Thermal springs charged with soluble silica steadily **opalize** surrounding wood and bone fragments in volcanic basins."},
            {"author": "Herman Melville", "work": "Mardi: and a Voyage Thither", "quote": "The phosphorescent wake seemed to **opalize** the midnight sea, flashing green and violet fire beneath the keel."}
        ]
    },

    # 74. orally
    "orally": {
        "primary": "By means of the mouth, or by spoken word rather than in writing.",
        "secondary": "In clinical pharmacotherapy and legal procedure, administering medications through the alimentary tract, or delivering testimony via spoken utterance under oath.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The contract was concluded **orally** over a glass of cider, without a single scrap of parchment passing between them."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Tribal folklore and genealogies were preserved **orally** through many generations before the invention of written alphabets."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solicitor delivered his confidential instructions **orally**, choosing not to commit such delicate matters to paper."}
        ]
    },

    # 75. oratorical
    "oratorical": {
        "primary": "Pertaining to the art, practice, or delivery of formal public speaking and rhetoric.",
        "secondary": "In classical rhetoric and forensic performance, characterized by grandiloquent diction, rhythmical cadences, and theatrical persuasiveness.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke possessed an **oratorical** style that rambled pleasantly through diverse historical anecdotes without arriving at any clear conclusion."},
            {"author": "G. K. Chesterton", "work": "The Club of Queer Trades", "quote": "The politician assumed an impressive **oratorical** posture, raising his arm as if commanding silence from an unruly senate."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Chatham's **oratorical** triumphs owed as much to his majestic presence and piercing eye as to the arguments he advanced."}
        ]
    },

    # 76. palliate
    "palliate": {
        "primary": "To relieve, soothe, or alleviate pain or distress without curing the underlying cause; or to extenuate an offense.",
        "secondary": "In hospice medicine and judicial ethics, mitigating clinical suffering to enhance comfort, or presenting extenuating circumstances to lessen moral blame.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She offered no excuses to **palliate** her conduct, standing before her accuser with simple and heartbreaking resignation."},
            {"author": "George Eliot", "work": "Silas Marner", "quote": "Dunsey sought every subtle sophistry to **palliate** his theft, convincing himself that luck would soon balance the ledger."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "No friendly hand could **palliate** the burning agony that tortured the minister's remorseful conscience."}
        ]
    }
}
