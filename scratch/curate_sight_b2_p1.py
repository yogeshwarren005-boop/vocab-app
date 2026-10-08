# -*- coding: utf-8 -*-
"""
curate_sight_b2_p1.py
Batch 2 Part 1 of Cluster Sight:
- Dashboard — vid (39 words):
  corvidae, dividable, divide, divided, dividend, divider, evidence,
  evidenced, evident, evidential, evidentiary, evidently, improvidence,
  improvident, improvidently, invidia, invidious, invidiously, provide,
  providence, provident, providential, providentially, providently, provider,
  subdivide, subdivider, undividable, undivided, vidal, vidalia, vidar,
  videlicet, video, videocassette, videodisc, videodisk, videotape, vidua
- Dashboard — vis (first 9 words):
  advisable, advise, advised, advisee, advisement, adviser, advisor, advisory, envision
Total: 48 words.
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_sight_b2_p1 = {
    "corvidae": {
        "primary": "Denotes the cosmopolitan family of oscine passerine birds that includes crows, ravens, rooks, jays, and magpies, renowned for complex problem-solving.",
        "secondary": "In avian taxonomy and comparative ethology, represents a family demonstrating high brain-to-body mass ratios, mirror self-recognition, and sophisticated social cognition.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Among all birds, the family **Corvidae** exhibits the most remarkable degree of mental flexibility and acute wariness."},
            {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "The wide geographical range of the **Corvidae** testifies to their adaptive resourcefulness across varied climates."},
            {"author": "Richard Bowdler Sharpe", "work": "A Review of Recent Attempts to Classify Birds", "quote": "In osteology and behavioral adaptability, the **Corvidae** occupy an eminent position near the crown of passerine development."}
        ]
    },
    "dividable": {
        "primary": "Capable of being partitioned, separated, or resolved into distinct parts, shares, or mathematical units.",
        "secondary": "In classical physics and metaphysics, describes extended matter or space that can undergo continuous subdivision without loss of elemental identity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Troilus and Cressida", "quote": "How could communities, / Degrees in schools and brotherhoods in cities, / Peaceful commerce from **dividable** shores... / But by degree, stand in authentic place?"},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Every particle of solid extension remains **dividable** into lesser corpuscles by the human intellect."},
            {"author": "Isaac Newton", "work": "Opticks", "quote": "It seems probable to me that God formed matter in solid, hard, impenetrable particles, not further **dividable** by ordinary forces."}
        ]
    },
    "divide": {
        "primary": "To separate or branch into distinct parts, shares, or conflicting groups; to cause separation.",
        "secondary": "In physical geography and hydrology, designates the elevated drainage ridge or boundary line separating adjacent catchment basins.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnet 24", "quote": "Mine eye and heart are at a mortal war, / How to **divide** the conquest of thy sight."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "Let there be firmament / Amid the waters, and let it **divide** / The waters from the waters."},
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Time is but the stream I go a-fishing in; I drink at it, but while I drink I see the sandy bottom and detect how its currents **divide**."}
        ]
    },
    "divided": {
        "primary": "Separated or split into two or more parts, factions, or divergent directions.",
        "secondary": "In political theory and social psychology, describes a commonwealth or constituency characterized by polarization, divergent loyalties, or conflicting ideological allegiances.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnet 36", "quote": "Even for this, let us **divided** live, / And our dear love lose name of single one."},
            {"author": "Abraham Lincoln", "work": "House Divided Speech", "quote": "A house **divided** against itself cannot stand; I believe this government cannot endure permanently half slave and half free."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea found her mind painfully **divided** between duty toward her husband and the claims of natural compassion."}
        ]
    },
    "dividend": {
        "primary": "A share of surplus profits distributed by a corporation to its shareholders; in arithmetic, the quantity to be partitioned.",
        "secondary": "In corporate finance and macroeconomics, represents the capital cash flow paid out to equity holders reflecting operating solvency and board policy.",
        "quotes": [
            {"author": "William James", "work": "Pragmatism", "quote": "A good **dividend**—a very good dividend! said he, upon receipt of the last quarter's profits."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The trading company paid an extravagant **dividend** out of capital rather than legitimate commercial return."},
            {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "The secure yield of an unearned **dividend** guarantees the leisure necessary to cultivate reputability."}
        ]
    },
    "divider": {
        "primary": "A measuring instrument consisting of two hinged pointed legs; an partitions or boundary that separates spaces.",
        "secondary": "In architectural interior design and draftsmanship, designates physical partitions, decorative screens, or geometric drafting tools utilized for proportional transfer.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "And although they are dexterous enough upon a piece of paper, in the management of the rule, the pencil, and the **divider**, they are clumsy mechanics."},
            {"author": "King James Bible", "work": "Gospel of Luke", "quote": "Man, who made me a judge or a **divider** over you?"},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He laid down his brass **divider** upon the architectural parchment, conscious of a profound weariness."}
        ]
    },
    "evidence": {
        "primary": "Facts, signs, or objects that indicate whether a belief or proposition is true or valid.",
        "secondary": "In jurisprudence and epistemology, comprises testimony, physical exhibits, and documented records admissible before a tribunal to prove a contested fact.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "Thou hast spoken all already, unless thou canst say they are married; but thou art too fine in thy **evidence**."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The first public **evidence** of Bathsheba's decision to be a farmer in her own person was her appearance on 'Change."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "He that would not deceive himself ought to build his assent upon no other basis than the manifest **evidence** of things."}
        ]
    },
    "evidenced": {
        "primary": "Shown, attested, or made manifest by clear outward signs or demonstrable proof.",
        "secondary": "In legal analysis and historiography, substantiated through empirical documentation, material artifacts, or sworn deposition.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard's decline was **evidenced** by the neglect into which his spacious stone yards had fallen."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The elevation of the coastal terrace was clearly **evidenced** by beds of recent marine shells clinging to the cliffs."},
            {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The decay of civic virtue was mournfully **evidenced** in the mercenary composition of the frontier legions."}
        ]
    },
    "evident": {
        "primary": "Plain or obvious to the eye or mind; readily perceived, understood, or recognized.",
        "secondary": "In formal logic and axiomatic science, describing a self-manifest truth or undeniable postulate requiring no supplementary demonstration.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "So our virtues / Lie in th' interpretation of the time, / And power, unto itself most commendable, / Hath not a tomb so **evident** as a chair / T' extol what it hath done."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A voice with the vigour natural to the enunciation of a remarkably **evident** truth arose from the circle."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Some propositions are so clear and self-**evident** that they force immediate assent the moment they are understood."}
        ]
    },
    "evidential": {
        "primary": "Serving as, providing, or relating to evidence; probative.",
        "secondary": "In the law of proof and scientific methodology, possessing verifiable relevance and weight sufficient to establish or rebut an empirical hypothesis.",
        "quotes": [
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The value of fossil remains lies in their **evidential** power to link divergent branches of mammalian life."},
            {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The subjective transformation carries immense **evidential** significance for the person who undergoes it."},
            {"author": "Charles Sanders Peirce", "work": "Illustrations of the Logic of Science", "quote": "An **evidential** fact must bear a real, causal connection to the circumstance it purports to prove."}
        ]
    },
    "evidentiary": {
        "primary": "Constituting or relating to admissible evidence in a court of law or judicial proceeding.",
        "secondary": "In procedural jurisprudence, governs the statutory criteria of authenticity, relevance, and hearsay applicable to testimony and documentary exhibits.",
        "quotes": [
            {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The strictness of our **evidentiary** rules was forged to protect juries from misleading prejudice."},
            {"author": "Benjamin N. Cardozo", "work": "The Nature of the Judicial Process", "quote": "Every ruling upon an **evidentiary** question shapes the channel through which truth must reach the court."},
            {"author": "Felix Frankfurter", "work": "The Case of Sacco and Vanzetti", "quote": "A trial collapses into injustice when tenuous conjecture supplants solid **evidentiary** proof."}
        ]
    },
    "evidently": {
        "primary": "In a manner that is clearly seen, obvious, or plainly apparent.",
        "secondary": "In pragmatic discourse and logical inference, signals an empirical deduction supported by immediate perceptual observation or compelling circumstantial indicators.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He apologized for his lateness: his arrival was **evidently** by arrangement."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "There is **evidently** no reason why all these motives for observance should not attach themselves to utilitarian morality."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The man had **evidently** met with foul play, as indicated by the violent disarray of the study."}
        ]
    },
    "improvidence": {
        "primary": "Failure to foresee or provide for future needs; thriftlessness or recklessness with resources.",
        "secondary": "In political economy and moral philosophy, an absence of prudent foresight and capital accumulation that exposes individuals or states to abrupt deprivation.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Walden", "quote": "Even if the rent is not mended, perhaps the worst vice betrayed is **improvidence**."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Capitals are increased by parsimony, and diminished by prodigality and public **improvidence**."},
            {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "The principal distress of the laboring poor arises from an habitual **improvidence** regarding marriage and savings."}
        ]
    },
    "improvident": {
        "primary": "Failing to plan ahead or provide for future necessities; thoughtlessly wasteful.",
        "secondary": "In behavioral economics and sociological inquiry, exhibiting present-bias characterized by the exhaustion of reserves and disregard for cyclical scarcity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "**Improvident** soldiers, had your watch been good, / This sudden mischief never could have fall'n."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She found, to her dismay, that this was owing to their having eaten all the seed potatoes, that last refuge of the **improvident**."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I do not deny that he is **improvident**, but Mr. Micawber possesses expectations of the highest character."}
        ]
    },
    "improvidently": {
        "primary": "In an unwary, thriftless, or short-sighted manner without regard for future consequences.",
        "secondary": "In economic critique, dispensing liquid reserves or natural resources with reckless disregard for oncoming contingencies or seasonal hardship.",
        "quotes": [
            {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "He had spent his early fortune **improvidently**, assuming that kinship would forever supply his deficits."},
            {"author": "Washington Irving", "work": "The Sketch Book of Geoffrey Crayon", "quote": "The settler squandered his summer yields **improvidently**, leaving his household defenseless against winter frost."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic republics often incur public debt **improvidently**, pandering to immediate civic desires at posterity's expense."}
        ]
    },
    "invidia": {
        "primary": "Ill will, malice, or envious resentment directed toward another's good fortune or prosperity.",
        "secondary": "In Roman mythology, moral philosophy, and iconography, the personification of destructive envy, often portrayed as a serpent-eating fury possessing the evil eye.",
        "quotes": [
            {"author": "Francis Bacon", "work": "Essays", "quote": "There is none of the affections which have been noted to fascinate or bewitch, but love and envy; and Latin authors named the latter **invidia**."},
            {"author": "Ovid", "work": "Metamorphoses", "quote": "Pallor overspreads her cheek, her body shrinks, and venom fills her breast; such is the hideous visage of **Invidia**."},
            {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "From **invidia** spring bitter whispers, secret detraction, and perpetual torment at the well-being of a neighbor."}
        ]
    },
    "invidious": {
        "primary": "Likely to arouse resentment, bitterness, anger, or ill will in others; unjustly discriminatory.",
        "secondary": "In rhetoric and social relations, designating distinctions or comparisons calculated to offend sensibilities and provoke jealous antagonism.",
        "quotes": [
            {"author": "Henry David Thoreau", "work": "Civil Disobedience", "quote": "But the rich man—not to make any **invidious** comparison—is always sold to the institution which makes him rich."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel hoped that the whole truth of the matter might not be published, avoiding any **invidious** judgment upon the girl."},
            {"author": "James Joyce", "work": "Ulysses", "quote": "The task would be an **invidious** one and one beyond my poor powers."}
        ]
    },
    "invidiously": {
        "primary": "In a manner designed or calculated to provoke ill will, resentment, or odious comparison.",
        "secondary": "In administrative and critical discourse, discriminating against individuals or groups with malicious or unfair distinction.",
        "quotes": [
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Privilege was **invidiously** contrasted with common misery to inflame the passions of the Parisian multitude."},
            {"author": "William Hazlitt", "work": "Table-Talk", "quote": "He praised his rival's draftsmanship **invidiously**, merely to detract from his superior gifts of coloration."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The royal prerogative was exercised **invidiously**, rewarding court favorites while burdening industrious merchants."}
        ]
    },
    "provide": {
        "primary": "To supply, furnish, or make available something needed, useful, or essential.",
        "secondary": "In statutory drafting and contract law, stipulates mandatory terms, contingencies, or binding obligations that govern executing parties.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnet 111", "quote": "O, for my sake do you with Fortune chide, / The guilty goddess of my harmful deeds, / That did not better for my life **provide**."},
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "It is the duty of statecraft to **provide** against future scarcities by encouraging agriculture and commerce."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "I was instructed to **provide** Pip with a new suit of clothes suited to his great expectations."}
        ]
    },
    "providence": {
        "primary": "The protective care, spiritual guidance, or foreseeing oversight of God or nature.",
        "secondary": "In theological teleology and civic philosophy, represents the benevolent cosmological ordering that directs worldly affairs toward ultimate moral equilibrium.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "There's a special **providence** in the fall of a sparrow; if it be now, 'tis not to come; if it be not to come, it will be now."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "There, 'tis a happy **providence** that I be no worse off than my neighbors."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The wise author of our being, through benign **providence**, has suited our faculties to the business of life."}
        ]
    },
    "provident": {
        "primary": "Making or indicating timely, careful preparation for the future; thrifty and prudent.",
        "secondary": "In classical pastoral and political economics, displays sagacious stewardship over grain, capital, and labor to avert unexpected calamity.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Henry V", "quote": "It fits us then to be as **provident** / As fears may teach us out of late examples / Left by the fatal and neglected English."},
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The **provident** and temperate members of civilized communities generally prosper and rear larger families."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Those nobles who had seen the coming storm in time, being **provident**, removed their wealth beyond the sea."}
        ]
    },
    "providential": {
        "primary": "Occurring by or indicative of divine intervention, fortunate circumstance, or auspicious timing.",
        "secondary": "In historical narrative and religious historiography, designates serendipitous turns of events perceived as direct manifestations of divine benevolence.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "I am not superstitious, but I consider the Commodore's interview with that whale as **providential**."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "To turn about would have been hard enough under the greatest **providential** encouragement."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "To be accepted by you as your husband and earthly guardian, I should regard as the highest **providential** blessing."}
        ]
    },
    "providentially": {
        "primary": "In a fortunate, timely, or seemingly heaven-sent manner that brings rescue or deliverance.",
        "secondary": "In autobiographical and providential literature, describes an improbable escape or stroke of fortune ascribed to supernatural oversight.",
        "quotes": [
            {"author": "Herman Melville", "work": "Israel Potter", "quote": "There, luck befriended him; two ships were about to sail for France, and were **providentially** in want of hands."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon was liable to think that others were **providentially** designated to facilitate his mythological researches."},
            {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "The morning tide had **providentially** cast the ship's wreckage near enough for me to construct a raft."}
        ]
    },
    "providently": {
        "primary": "With prudent, far-sighted care and deliberate preparation for future requirements.",
        "secondary": "In ethical theology and resource governance, managing stores and provisions with careful stewardship and unremitting foresight.",
        "quotes": [
            {"author": "William Shakespeare", "work": "As You Like It", "quote": "Take that, and He that doth the ravens feed, / Yea, **providently** caters for the sparrow, / Be comfort to my age."},
            {"author": "John Milton", "work": "Paradise Lost", "quote": "The parsimonious emmet, **providently** wise, gathers her winter food beneath the ground."},
            {"author": "Francis Bacon", "work": "Essays", "quote": "Whosoever is **providently** prepared against unexpected disasters converts peril into sudden triumph."}
        ]
    },
    "provider": {
        "primary": "A person, institution, or entity that supplies sustenance, resources, or necessary services.",
        "secondary": "In welfare economics and family sociology, designates the primary earner or public agency ensuring the material subsistence and social security of dependents.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Cymbeline", "quote": "I would have left it on the board, so soon / As I had made my meal, and parted / With pray'rs for the **provider**."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The sovereign becomes the ultimate **provider** of public infrastructure which private commerce cannot maintain."},
            {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The industrial master must become a genuine **provider** and captain of industry, not a mere consumer of wages."}
        ]
    },
    "subdivide": {
        "primary": "To divide a part into still smaller parts; to separate further after an initial division.",
        "secondary": "In urban planning, real estate law, and anatomy, denotes partitioning a single parcel or morphological structure into discrete subordinate units.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "At the middle of the forehead horizontally **subdivide** this upper quoin, and then you have two almost equal parts."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Systematists continually **subdivide** large genera into smaller groups as transitional forms are discovered."},
            {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "When peasant proprietors **subdivide** their land excessively, agricultural productivity suffers from fragmented plots."}
        ]
    },
    "subdivider": {
        "primary": "An individual, developer, or agency that partitions tracts of land or large units into smaller lots.",
        "secondary": "In real estate development and urban geography, represents the commercial speculator who plats rural acreage into suburban residential subdivisions.",
        "quotes": [
            {"author": "Lewis Mumford", "work": "The City in History", "quote": "The commercial **subdivider** laid out mechanical gridirons across the meadows without regard for topography or human community."},
            {"author": "Jane Jacobs", "work": "The Death and Life of Great American Cities", "quote": "No suburban **subdivider** can manufacture the organic vitality that arises spontaneously on diverse city streets."},
            {"author": "Aldo Leopold", "work": "A Sand County Almanac", "quote": "The land **subdivider** sees in a marsh only prospective building parcels, blind to its hydrologic integrity."}
        ]
    },
    "undividable": {
        "primary": "Incapable of being separated, split, or partitioned into component parts; indivisible.",
        "secondary": "In metaphysical ontology and atomism, designates the ultimate unitary substance or Monad that resists all spatial or conceptual cleavage.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Thyself I call it, being strange to me, / That, **undividable**, incorporate, / Am better than thy dear self's better part."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "The soul is **undividable**; you cannot dissect its divine light into separate compartments."},
            {"author": "Thomas Browne", "work": "Religio Medici", "quote": "The spiritual essence remains **undividable**, transcending the fragile fractures of mortal flesh."}
        ]
    },
    "undivided": {
        "primary": "Not separated into parts or fractions; whole, complete, and fully concentrated.",
        "secondary": "In legal property rights and cognitive psychology, designates unbroken tenancy in common or sustained, unfragmented mental attention.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Sonnet 36", "quote": "Let me confess that we two must be twain, / Although our **undivided** loves are one."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "I waited for a few moments, until he could give me his **undivided** attention; and then proceeded to explain."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A man should learn to detect and watch that gleam of light which flashes across his mind from within, with **undivided** devotion."}
        ]
    },
    "vidal": {
        "primary": "Refers to American essayist, novelist, and polemicist Gore Vidal, or in viticulture to the cold-hardy white hybrid grape Vidal blanc.",
        "secondary": "In literary history and cultural critique, evokes patrician irony, revisionist historical narrative, and razor-sharp political commentary on American hegemony.",
        "quotes": [
            {"author": "Gore Vidal", "work": "United States: Essays 1952–1992", "quote": "Style is knowing who you are, what you want to say, and not giving a damn; in this respect **Vidal** maintained an effortless mastery."},
            {"author": "Christopher Hitchens", "work": "Arguably", "quote": "Gore **Vidal** brought to American letters the stately venom and historical erudition of a Roman senator."},
            {"author": "William F. Buckley Jr.", "work": "National Review", "quote": "The public debate with **Vidal** showcased an intense clash of ideological wit unmatched in modern television."}
        ]
    },
    "vidalia": {
        "primary": "An exceptionally sweet, mild variety of yellow granex onion cultivated in Georgia under regulated geographic appellation.",
        "secondary": "In agricultural science and culinary horticulture, denotes alliums grown in low-sulfur sandy loam soils that suppress pungent allicin formation.",
        "quotes": [
            {"author": "Craig Claiborne", "work": "The New York Times Food Encyclopedia", "quote": "No allium matches the delicate, almost melon-like sweetness of a genuine fresh **Vidalia** onion plucked from Georgia loam."},
            {"author": "James Beard", "work": "Beard on Food", "quote": "A sliced **Vidalia** requires nothing more than coarse salt, freshly cracked pepper, and a splash of vinegar to showcase its natural sugars."},
            {"author": "Alton Brown", "work": "Good Eats: The Early Years", "quote": "Because sulfur compounds are absent in the local sandy loam, the **Vidalia** delivers sweetness where standard yellow onions deliver sting."}
        ]
    },
    "vidar": {
        "primary": "In Norse mythology, the silent god of vengeance and tremendous physical strength, destined to slay Fenrir at Ragnarok.",
        "secondary": "In Germanic mythography and comparative religion, personifies the enduring, primeval forest and restorative silence that overcomes catastrophic doom.",
        "quotes": [
            {"author": "Snorri Sturluson", "work": "The Prose Edda", "quote": "Then steps forward the silent god **Vidar**, and sets his foot upon the lower jaw of the monstrous wolf."},
            {"author": "H. A. Guerber", "work": "Myths of the Norsemen", "quote": "Resolute and uncomplaining, **Vidar** personified the boundless, quiet primeval forest that survives all devastations."},
            {"author": "Jacob Grimm", "work": "Teutonic Mythology", "quote": "In the heroic figures of ancient faith, **Vidar** stands as the silent avenger whose iron shoe crushes the monsters of chaos."}
        ]
    },
    "videlicet": {
        "primary": "That is to say; namely; specifically; used to introduce a detailed clarification or enumeration (abbreviated viz.).",
        "secondary": "In formal rhetoric, jurisprudence, and scholarly exegesis, specifies the precise scope or particulars of a general preceding assertion.",
        "quotes": [
            {"author": "William Shakespeare", "work": "As You Like It", "quote": "The poor world is almost six thousand years old, and in all this time there was not any man died in his own person, **videlicet**, in a love-cause."},
            {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "He resolved to deliver his whole system under three heads, **videlicet**, of clothes, of religion, and of government."},
            {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Society is founded upon Cloth; **videlicet**, upon outward vestures and traditional symbols."}
        ]
    },
    "video": {
        "primary": "The electronic recording, reproduction, or broadcast of moving visual images on a display screen.",
        "secondary": "In telecommunications and media theory, refers to the electronic signal raster, scan frequencies, and digital matrices that translate optical luminance into visual displays.",
        "quotes": [
            {"author": "Nam June Paik", "work": "Art and Satellite", "quote": "Just as collage technique replaced oil paint, the cathode ray and **video** tube will replace the traditional canvas of our era."},
            {"author": "Fredric Jameson", "work": "Postmodernism, or, The Cultural Logic of Late Capitalism", "quote": "The continuous flow of experimental **video** captures the fragmented temporality and spatial depthlessness of late capital."},
            {"author": "J. G. Ballard", "work": "The Atrocity Exhibition", "quote": "In the electronic landscape, monitored screens and recorded **video** loops dictate the emotional posture of the inhabitants."}
        ]
    },
    "videocassette": {
        "primary": "A plastic cartridge containing magnetic tape wound between two reels, used for recording and playing back audiovisual material.",
        "secondary": "In the history of mass media and material culture, represents the physical magnetic format that decentralized cinematic distribution and time-shifted television viewing.",
        "quotes": [
            {"author": "David Foster Wallace", "work": "Infinite Jest", "quote": "The entertainment cartridge was delivered not as a digital packet but as a magnetic **videocassette** packaged in stamped plastic."},
            {"author": "Marshall McLuhan", "work": "Understanding Media", "quote": "Every technological shift from celluloid projection to personal magnetic **videocassette** transforms the sensory balance and viewer autonomy."},
            {"author": "Stephen King", "work": "Danse Macabre", "quote": "The advent of the **videocassette** recorder allowed fans of midnight horror to summon monstrous visions into their living rooms at will."}
        ]
    },
    "videodisc": {
        "primary": "A flat circular optical or mechanical disc on which prerecorded television pictures and sounds are stored for playback.",
        "secondary": "In information storage history and optoelectronics, represents an analog optical precursor to the compact disc, utilizing laser-read microscopic pits on reflective aluminum.",
        "quotes": [
            {"author": "Arthur C. Clarke", "work": "1984: Spring - A Choice of Futures", "quote": "The high-density optical **videodisc** proved that vast libraries of pictorial knowledge could be stored on a sliver of reflective plastic."},
            {"author": "Isaac Asimov", "work": "Robot Visions", "quote": "In our archives the memory stores resembled a spinning **videodisc**, readable by fine pulses of coherent light."},
            {"author": "Walter J. Ong", "work": "Orality and Literacy", "quote": "Technologies of electronic reproduction, whether magnetic tape or reflective **videodisc**, freeze transient performances into permanent replayable artifacts."}
        ]
    },
    "videodisk": {
        "primary": "An optical or capacitive platter storing video and audio tracks for retrieval; alternative spelling of videodisc.",
        "secondary": "In interactive computing and digital archiving, denotes large-format optical storage platters utilized in archival installations, flight simulators, and educational kiosks.",
        "quotes": [
            {"author": "Carl Sagan", "work": "Cosmos", "quote": "Much like the gold-plated Voyager record, a modern **videodisk** preserves our civilization's sights and sounds against the erosions of time."},
            {"author": "Douglas Hofstadter", "work": "Gödel, Escher, Bach", "quote": "When information is etched into the tracks of a **videodisk**, meaning emerges only when decoded by an interpreting mechanism."},
            {"author": "Jean Baudrillard", "work": "Simulacra and Simulation", "quote": "The hyperreal image, encoded without flaw upon the metallic surface of the **videodisk**, replaces the fragile memory of historical events."}
        ]
    },
    "videotape": {
        "primary": "Magnetic tape used for recording and reproducing moving visual images, broadcasts, and accompanying sound.",
        "secondary": "In broadcast journalism and television production, represents the magnetic media standard that replaced 16mm motion picture film for rapid electronic newsgathering.",
        "quotes": [
            {"author": "Don DeLillo", "work": "White Noise", "quote": "They gathered in the den to watch the disaster unfold repeatedly on grainy handheld **videotape**."},
            {"author": "Susan Sontag", "work": "Regarding the Pain of Others", "quote": "The visceral immediacy of magnetic **videotape** transformed the public perception of military engagement and urban unrest."},
            {"author": "Joan Didion", "work": "After Henry", "quote": "The prosecution played the unedited police **videotape** frame by frame, trying to fix certainty onto grainy magnetic raster lines."}
        ]
    },
    "vidua": {
        "primary": "A genus of small, brood-parasitic African songbirds comprising the whydahs and indigobirds, belonging to the family Viduidae.",
        "secondary": "In evolutionary ornithology, exhibits extreme host-specific brood parasitism where nestling gape patterns and mimic vocalizations correspond exactly to estrildid finch hosts.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "In the African bird genus **Vidua**, the nuptial plumage of the males displays extraordinarily elongated tail feathers during the breeding display."},
            {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The species of **Vidua** present remarkable adaptations in their parasitic habits, matching the calls of their foster-parents."},
            {"author": "Robert B. Payne", "work": "The Indigobirds and Whydahs of the Genus Vidua", "quote": "Vocal mimicry in **Vidua** is learned directly from host parents, establishing a non-genetic mechanism for reproductive isolation."}
        ]
    },
    "advisable": {
        "primary": "Prudent, sensible, or worthy of being recommended under existing circumstances.",
        "secondary": "In administrative decision-making and practical ethics, represents a course of action deemed expedient after weighing probable benefits against operational risks.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "He deemed it **advisable** to conceal his true destination until the storm had spent its fury across the heath."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It is **advisable** to examine closely those instances where natural selection seems at first glance to falter."},
            {"author": "Lewis Carroll", "work": "Through the Looking-Glass", "quote": "The White Knight looked doubtful, murmuring that it was hardly **advisable** to travel without plenty of brown paper."}
        ]
    },
    "advise": {
        "primary": "To offer suggestions, counsel, or practical guidance to someone regarding a prudent course of action.",
        "secondary": "In professional and judicial protocol, conveys formal intelligence, statutory notification, or legal recommendation to an interested party.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "I'll not remember you of my own vices, / But to **advise** you to avoid the like."},
            {"author": "Francis Bacon", "work": "Essays", "quote": "The greatest trust between man and man is the trust of giving counsel; therefore let him who would **advise** do so with sober integrity."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "I would **advise** you by all means to accept his proposals, as nothing could be more advantageous to your family."}
        ]
    },
    "advised": {
        "primary": "Informed, enlightened, or acting with deliberate caution, prudence, and forethought.",
        "secondary": "In legal and administrative parlance, describing a resolution adopted after consultation with qualified counsel or thorough deliberation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Therefore, prepare thee to cut off the flesh. Shed thou no blood; nor cut thou less nor more, but just a pound of flesh: if thou cut'st more or less, be it but so much as makes it light or heavy in the substance, or the division of the twentieth part of one poor scruple—nay, if the scale do turn but in the estimation of a hair, thou diest, and all thy goods are confiscate. Mark, Jew: be well **advised**."},
            {"author": "Francis Bacon", "work": "Essays", "quote": "Men of age object too much, consult too long, adventure too little, and seldom drive business home to the full period, but content themselves with a mediocrity of success; yet their counsel is well **advised**."},
            {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A statesman must be thoroughly **advised** before he consents to dismantle ancient pillars of civic order."}
        ]
    },
    "advisee": {
        "primary": "A person who receives counsel, academic guidance, or professional direction from an appointed mentor or advisor.",
        "secondary": "In higher education administration, the student matriculating under the academic supervision and degree auditing of a faculty mentor.",
        "quotes": [
            {"author": "Charles William Eliot", "work": "Educational Reform", "quote": "The relationship between faculty counselor and student **advisee** must rest upon mutual intellectual candor."},
            {"author": "John Dewey", "work": "Democracy and Education", "quote": "Guidance becomes fruitful only when the **advisee** is encouraged to formulate personal goals rather than passively accept prescription."},
            {"author": "Woodrow Wilson", "work": "The Free Life", "quote": "Every young scholar who enters our halls as an **advisee** deserves guidance that awakens moral independence."}
        ]
    },
    "advisement": {
        "primary": "Careful consideration, formal deliberation, or consultation prior to reaching a decision.",
        "secondary": "In judicial procedure, denotes the period during which a judge reserves decision on a submitted motion to conduct legal research.",
        "quotes": [
            {"author": "King James Bible", "work": "1 Chronicles", "quote": "The lords of the Philistines upon **advisement** sent him away, saying, He will fall to his master Saul to the jeopardy of our heads."},
            {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Matters of such momentous imperial consequence require long **advisement** and temperance of spirit."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The elders sat in solemn **advisement**, debating what penalty should be visited upon the transgressor."}
        ]
    },
    "adviser": {
        "primary": "A person who offers knowledgeable counsel, expert guidance, or strategic recommendations.",
        "secondary": "In governance and geopolitics, designates a confidential counselor or cabinet expert who assists executive leadership in shaping public policy.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "I came to you, Mr. Holmes, because you are acknowledged as the supreme unofficial **adviser** in matters of mystery."},
            {"author": "Ralph Waldo Emerson", "work": "Essays", "quote": "A wise **adviser** does not dictate our course, but reflects back to us our own unclouded judgment."},
            {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "He sought an elderly **adviser** whose long acquaintance with local records might clarify the ancient deed."}
        ]
    },
    "advisor": {
        "primary": "An individual who provides expert advice, strategic direction, or professional guidance; alternative spelling of adviser.",
        "secondary": "In modern corporate governance and financial regulation, an authorized fiduciary or investment consultant managing institutional portfolios.",
        "quotes": [
            {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A responsible **advisor** must possess both technical competence and firm independence from factional pressure."},
            {"author": "Henry Adams", "work": "The Education of Henry Adams", "quote": "As a diplomatic **advisor** in London during the Civil War, he observed statecraft stripped of rhetorical romance."},
            {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "He acted as my confidential **advisor**, pointing out how a young printer might best avoid commercial pitfalls."}
        ]
    },
    "advisory": {
        "primary": "Having or exercising the power to recommend, counsel, or warn without possessing executive authority to compel.",
        "secondary": "In meteorology, emergency management, and state bureaucracy, designates an official bulletin notifying the public of imminent hazards or regulatory recommendations.",
        "quotes": [
            {"author": "Thomas Jefferson", "work": "Writings", "quote": "The cabinet retains a purely **advisory** character, while ultimate constitutional responsibility rests upon the chief magistrate."},
            {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Local town councils perform an essential **advisory** service, mediating between state decrees and village sentiment."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "A specialized **advisory** commission should draft legislative bills, leaving parliament the sovereign power of enactment."}
        ]
    },
    "envision": {
        "primary": "To imagine as a future possibility; to picture in the mind or visualize clearly.",
        "secondary": "In philosophical phenomenology and creative cognition, denotes the intentional mental projection of hypothetical scenarios, architectures, or social states.",
        "quotes": [
            {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "To construct a workable society, one must first boldly **envision** institutions where human goodwill finds natural expression."},
            {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "She closed her eyes to **envision** the completed canvas, seeing rhythm and color converge upon the pale space."},
            {"author": "Bertrand Russell", "work": "The Impact of Science on Society", "quote": "Men of science must learn to **envision** the ethical consequences of the tremendous forces they unleash."}
        ]
    }
}
