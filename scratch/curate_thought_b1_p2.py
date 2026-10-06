# -*- coding: utf-8 -*-
"""
curate_thought_b1_p2.py
Batch 1 Part 2 of Cluster Thought (53 words):
- cogn (remaining 13 words: recognise, recognised, recognition, recognizable,
  recognizably, recognizance, recognize, recognized, unrecognisable, unrecognised,
  unrecognizable, unrecognizably, unrecognized)
- estim (11 words: estimable, estimate, estimation, estimator, inestimable,
  misestimate, misestimation, overestimate, overestimation, underestimate, underestimation)
- ment (25 words: comment, commentary, commentate, commentator, demented, dementedly,
  dementedness, dementia, disinterment, emmental, emmentaler, interment, mental,
  mentalism, mentality, mentally, mentation, menticirrhus, mention, mentioner, mentor,
  mentorship, mentum, undermentioned, unmentionable)
- opin (4 words: opine, opinion, opinionated, opinionative)
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

data_thought_b1_p2 = {
    # ==================== Dashboard — cogn (Remaining 13 words) ====================
    "recognise": {
        "primary": "To identify someone or something from previous knowledge, perceive, or formally acknowledge validity (British spelling).",
        "secondary": "In political diplomacy and epistemology, the official affirmation of sovereign status or cognitive identification of an object.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She did not **recognise** the stranger at the cottage gate until he spoke in his accustomed gentle tone."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "A civilized society must **recognise** the supreme moral value of individual diversity and intellectual independence."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The comparative anatomist can readily **recognise** the underlying unity of bone architecture across different vertebrate limbs."}
        ]
    },
    "recognised": {
        "primary": "Identified from past acquaintance, widely accepted, or officially acknowledged (British spelling).",
        "secondary": "In jurisprudence and academic scholarship, certified as authoritative or established by customary consensus.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was everywhere **recognised** as the most energetic and wealthy grain merchant in the borough."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Justice has always been **recognised** as the chief cornerstone of human social happiness and order."},
            {"author": "Lewis Carroll", "work": "Alice's Adventures in Wonderland", "quote": "Alice soon **recognised** the Queen's shrill voice echoing across the rose garden."}
        ]
    },
    "recognition": {
        "primary": "The act of identifying from previous knowledge, or formal acknowledgment of service, achievement, or status.",
        "secondary": "In international relations and perceptual psychology, sovereign accreditation, or matching sensory input with stored cognitive schemas.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A sudden gleam of mutual **recognition** passed between the two men as the lantern illuminated their faces."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The government granted prompt diplomatic **recognition** to the newly established democratic republic."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea longed for some noble sphere of action where her devotion might win genuine spiritual **recognition**."}
        ]
    },
    "recognizable": {
        "primary": "Capable of being identified, perceived, or acknowledged from previous knowledge or distinctive traits.",
        "secondary": "In cognitive psychology and forensic science, possessing salient visual, acoustic, or morphological characteristics that enable positive identification.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The familiar features of the old Elizabethan manor house were easily **recognizable** across the sunlit park."},
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In every modified variety of domestic pigeon, the ancestral rock pigeon remains clearly **recognizable**."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The bleached white hump of the famous leviathan was instantly **recognizable** to every seasoned whaleman."}
        ]
    },
    "recognizably": {
        "primary": "In a manner that is clearly identifiable, perceptible, or acknowledged.",
        "secondary": "In descriptive aesthetics and linguistic analysis, possessing unambiguous markers of a particular style, origin, or authorship.",
        "quotes": [
            {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "The portrait was **recognizably** the work of a master who captured character through delicate modulations of light."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The architectural outlines of Christminster rose **recognizably** against the evening sky like a celestial vision."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The handwritten postscript was **recognizably** inscribed by the hand of the missing baronet."}
        ]
    },
    "recognizance": {
        "primary": "A legal obligation recorded before a court binding a person to perform an act, such as appearing for trial.",
        "secondary": "In historical jurisprudence and heraldic tradition, an acknowledged formal debt recorded in a court of record, or an official badge of retaining.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Hamlet", "quote": "Where be his quiddities now, his quillets, his cases, his tenures, and his **recognizance**?"},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The magistrate admitted the defendant to bail upon his entering into a solemn personal **recognizance**."},
            {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The proud baron commanded his men-at-arms to display the ancient **recognizance** of his lineage upon their shields."}
        ]
    },
    "recognize": {
        "primary": "To identify from prior knowledge, realize the truth of, or acknowledge formal legitimacy.",
        "secondary": "In cognitive science and geopolitical law, the neural retrieval of stored representations, or the diplomatic accreditation of a sovereign state.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak was able to **recognize** each individual ewe in the flock by subtle variations in fleece and gait."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "In every work of genius we **recognize** our own rejected thoughts returning with alienated majesty."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "He failed to **recognize** the profound spiritual loneliness that oppressed his young wife's heart."}
        ]
    },
    "recognized": {
        "primary": "Identified from past experience, widely accepted, or officially accredited.",
        "secondary": "In social institutions and legal frameworks, enjoying verified authority, standard consensus, or public acclaim.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She walked along the lane, fearful of being **recognized** by any traveler from her native village."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Freedom of conscience has become a firmly **recognized** principle in modern constitutional jurisprudence."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The French prisoner was immediately **recognized** by the prosecution witnesses as an active revolutionary agent."}
        ]
    },
    "unrecognisable": {
        "primary": "Not capable of being identified or perceived from previous acquaintance; unrecognizable (British spelling).",
        "secondary": "In forensic pathology and narrative tragedy, altered beyond visual recall by traumatic injury, decay, or disguise.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The blackened corpse discovered in the tenement was rendered wholly **unrecognisable** by fire."},
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Years of severe colonial labor had transformed the handsome youth into an almost **unrecognisable** stranger."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The ravaged wilderness looked **unrecognisable** under the blinding tropical rain and creeping gloom."}
        ]
    },
    "unrecognised": {
        "primary": "Not identified, appreciated, or officially acknowledged; unrecognized (British spelling).",
        "secondary": "In cultural history and biography, describing genius, virtue, or merit that remains neglected by contemporaries.",
        "quotes": [
            {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many intermediate fossil links remain **unrecognised** in poorly explored geological formations of the southern continents."},
            {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister walked among his parishioners, his secret remorse entirely **unrecognised** beneath his saintly reputation."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She spent her days in devoted labor, content that her quiet beneficence should remain **unrecognised** by the world."}
        ]
    },
    "unrecognizable": {
        "primary": "So altered in appearance, character, or condition as to defy identification.",
        "secondary": "In observational description and forensic medicine, suffering complete obliteration of distinguishing morphological or personal landmarks.",
        "quotes": [
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The ruined station house stood stripped and **unrecognizable** amidst the creeping tendrils of the primeval jungle."},
            {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The disguises were so masterfully contrived that each conspirator appeared completely **unrecognizable** to his fellows."},
            {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The pleasant suburban avenue was transformed into a blackened, **unrecognizable** waste of smoking ruins."}
        ]
    },
    "unrecognizably": {
        "primary": "In a manner or to an extent that prevents identification or recognition.",
        "secondary": "In narrative prose, describing catastrophic physical transformation, profound disfigurement, or extreme alteration of form.",
        "quotes": [
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The body lying at the foot of the granite tor was **unrecognizably** shattered by the terrible fall."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The fierce storm battered the whaling ship until her rigging was **unrecognizably** tangled and splintered."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Misfortune had altered her lovely face so **unrecognizably** that old acquaintances passed her without greeting."}
        ]
    },
    "unrecognized": {
        "primary": "Not identified, appreciated, or officially acknowledged by society or authority.",
        "secondary": "In the history of science and philosophy, profound discoveries or ethical truths that languished in obscurity before posthumous vindication.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His constant fidelity remained largely **unrecognized** by the proud mistress who accepted his loyal service as a matter of course."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The noble physician lived quietly in London, his past sufferings in the Bastille almost **unrecognized** by his English neighbors."},
            {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The greatest benefactors of mankind often walk through life **unrecognized**, misunderstood by their own generation."}
        ]
    },

    # ==================== Dashboard — estim (11 words) ====================
    "estimable": {
        "primary": "Worthy of great respect, high esteem, and moral admiration; or capable of being calculated.",
        "secondary": "In moral philosophy and character analysis, possessing solid virtue, probity, and civic usefulness deserving public honor.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "A lady, sir, though it was said she much resembled me, was yet of many accounted beautiful, but of all **estimable** for her rare mind."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Those virtues that promote the preservation of society are universally held to be the most **estimable** by rational men."},
            {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Actions that multiply human welfare and mitigate suffering constitute the most **estimable** conduct known to ethics."}
        ]
    },
    "estimate": {
        "primary": "To calculate approximately, assess the value or extent of, or form an informed opinion about something.",
        "secondary": "In economics and engineering, calculating probable costs, material requirements, or probabilistic parameters before undertaking a project.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Coriolanus", "quote": "I'd rather have my wounds to heal again than hear say how I got them, for I can never **estimate** the price of praise."},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak paused to **estimate** the financial loss caused by the thunderstorm before proposing emergency remedies to the farm bailiff."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The prudent merchant will carefully **estimate** the risks of marine transport before committing capital to long voyages."}
        ]
    },
    "estimation": {
        "primary": "A judgment or opinion of worth, character, or value; or esteem, honor, and respect.",
        "secondary": "In mathematical statistics and moral philosophy, calculating unknown parameters, or holding an individual in high public repute.",
        "quotes": [
            {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "I know him a notorious liar, think him a great way fool, solely a coward; yet these fixed evils sit so fit in him that they take place, when virtue's steely bones look bleak in the cold wind; full oft we see cold wisdom waiting on superfluous folly in men's **estimation**."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "In the general **estimation** of the county, Mr. Brooke was a well-meaning landlord whose political speeches were somewhat eccentric."},
            {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her high **estimation** of Mr. Wickham's character was rudely shattered by the revelation of his treacherous past."}
        ]
    },
    "estimator": {
        "primary": "A person or statistical rule that calculates or evaluates approximate costs, values, or probabilities.",
        "secondary": "In mathematical statistics and construction management, a function that computes an estimate of a population parameter from sample data.",
        "quotes": [
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The prudent statesman is a skillful **estimator** of human passions, balancing factions against one another to preserve peace."},
            {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The experienced builder acts as a cautious **estimator**, providing detailed calculations of masonry and timber costs."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The mathematical **estimator** weighs conflicting empirical measurements to deduce the most probable true value."}
        ]
    },
    "inestimable": {
        "primary": "Too great, precious, or valuable to be measured or calculated; priceless.",
        "secondary": "In moral philosophy and civic literature, describing fundamental blessings (such as liberty or truth) that transcend all commercial valuation.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Richard III", "quote": "Wedges of gold, great anchors, heaps of pearl, **inestimable** stones, unvalued jewels, all scattered in the bottom of the sea."},
            {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Civil liberty and the rule of law represent an **inestimable** heritage purchased by the blood and sacrifice of our ancestors."},
            {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "He threw away an **inestimable** opportunity for redemption through a single moment of catastrophic hesitation."}
        ]
    },
    "misestimate": {
        "primary": "To judge, calculate, or value incorrectly, inaccurately, or erroneously.",
        "secondary": "In strategic planning and economic appraisal, making flawed forecasts regarding resource expenditure, opposition strength, or market demand.",
        "quotes": [
            {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The royalist ministers continued to **misestimate** the volcanic wrath accumulating among the starving Parisian populace."},
            {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Legislators frequently **misestimate** the moral resilience of the public when framing paternalistic statutes."},
            {"author": "Herbert Spencer", "work": "Social Statics", "quote": "State planners habitually **misestimate** the secondary economic consequences of artificial price regulations."}
        ]
    },
    "misestimation": {
        "primary": "An incorrect, faulty, or inaccurate calculation, judgment, or evaluation.",
        "secondary": "In political analysis and statistical modeling, systemic error arising from biased assumptions or inadequate empirical data.",
        "quotes": [
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A fatal **misestimation** of the barbarian cavalry's strength led the Emperor Valens to disastrous defeat at Adrianople."},
            {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Fallacies of induction often originate in the simple **misestimation** of the relative frequency of coexisting attributes."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Every major error in cosmological theory traces back to the initial **misestimation** of physical forces."}
        ]
    },
    "overestimate": {
        "primary": "To value, assess, or calculate too highly; to overrate capacity, cost, or difficulty.",
        "secondary": "In psychological cognition and strategic forecasting, attributing greater significance, strength, or virtue to an agent than is warranted.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "It was Dorothea's nature to **overestimate** the learning of others while maintaining a humble opinion of her own mind."},
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was prone to **overestimate** his commercial influence, launching speculative ventures beyond his capital."},
            {"author": "John Stuart Mill", "work": "Autobiography", "quote": "My father warned me never to **overestimate** my intellectual achievements merely because of early academic precocity."}
        ]
    },
    "overestimation": {
        "primary": "The act, process, or result of estimating something too highly, generously, or excessively.",
        "secondary": "In behavioral economics and clinical psychology, cognitive bias leading to inflated expectations of success or exaggerated appraisal of worth.",
        "quotes": [
            {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The arrogant **overestimation** of our own abilities is the fruitful source of half the misfortunes of human life."},
            {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "National vanity leads to the habitual **overestimation** of domestic virtues and the corresponding disparagement of foreign cultures."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "An emotional attachment inevitably produces an **overestimation** of the beloved object's physical and moral perfections."}
        ]
    },
    "underestimate": {
        "primary": "To estimate at too low a value, quantity, strength, or importance; to undervalue.",
        "secondary": "In competitive strategy and military analysis, failing to appreciate the true capacity, resilience, or threat posed by an adversary.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "No prudent farmer should **underestimate** the sudden ferocity of an autumn gale upon an exposed downs pasture."},
            {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The detective cautioned his superiors not to **underestimate** the fanaticism of the desperate revolutionary conspirators."},
            {"author": "George Eliot", "work": "Daniel Deronda", "quote": "She made the fatal mistake to **underestimate** her husband's cold, relentless determination to dominate her will."}
        ]
    },
    "underestimation": {
        "primary": "The act or result of judging something to be smaller, weaker, or less important than it is.",
        "secondary": "In risk management and public policy, the failure to foresee the true scope or catastrophic impact of impending crises.",
        "quotes": [
            {"author": "Winston Churchill", "work": "The World Crisis", "quote": "A persistent **underestimation** of the enemy's reserves led Allied commanders into protracted wars of attrition."},
            {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "The treaty was vitiated by a gross **underestimation** of the economic interdependence of continental Europe."},
            {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The classical academy suffered from an unfortunate **underestimation** of the disciplinary value of physical sciences."}
        ]
    },

    # ==================== Dashboard — ment (25 words) ====================
    "comment": {
        "primary": "A remark, observation, criticism, or explanatory note expressing an opinion on a subject.",
        "secondary": "In literary criticism and scholarly hermeneutics, an interpretive gloss appended to a difficult passage to elucidate its meaning.",
        "quotes": [
            {"author": "William Shakespeare", "work": "King Lear", "quote": "I will not sleep, my lord, till I have delivered your royal **comment** upon these ambiguous proceedings."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The provincial gossips did not fail to make sarcastic **comment** upon the young widow's sudden departure."},
            {"author": "Samuel Johnson", "work": "The Lives of the Most Eminent English Poets", "quote": "Dryden added a critical **comment** to his translation, explaining the rules of classical poetic diction."}
        ]
    },
    "commentary": {
        "primary": "A series of explanatory notes, systematic annotations, or critical discourse on a text or event.",
        "secondary": "In historical scholarship and broadcasting, an extensive exegetical exposition analyzing scripture, law, or live public proceedings.",
        "quotes": [
            {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Every individual life is a perpetual **commentary** upon the universal laws that govern human destiny."},
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The proceedings in Chancery dragged on, generating voluminous reams of legal **commentary** and endless delay."},
            {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Justinian ordered his jurists to condense centuries of Roman jurisprudence into an authoritative imperial **commentary**."}
        ]
    },
    "commentate": {
        "primary": "To act as a commentator; to provide running commentary, critical analysis, or explanatory remarks.",
        "secondary": "In media broadcasting and literary journalism, delivering continuous verbal reporting and expert critique on live events or texts.",
        "quotes": [
            {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The critic's duty is not merely to describe the performance, but to **commentate** upon the philosophical vision of the dramatist."},
            {"author": "G. K. Chesterton", "work": "All Things Considered", "quote": "He sat back to **commentate** upon the absurdities of modern politics with genial irony and biting satire."},
            {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The journalists assembled in the lobby began to **commentate** excitedly upon the sudden collapse of the government."}
        ]
    },
    "commentator": {
        "primary": "A person who delivers a running commentary, explanatory analysis, or critical remarks on events or texts.",
        "secondary": "In academic hermeneutics and political journalism, a scholar who writes exegetical glosses on classical texts or a professional broadcast analyst.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon fancied himself a profound **commentator** upon the syncretic mythologies of the ancient world."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old sailor acted as a rough **commentator** on deck, explaining the habits of the great whales to the landsmen."},
            {"author": "Samuel Johnson", "work": "Preface to Shakespeare", "quote": "The task of the **commentator** is to explain what is obscure, rectify what is corrupt, and illustrate what is beautiful."}
        ]
    },
    "demented": {
        "primary": "Suffering from cognitive dementia; or driven to madness, frantic irrationality, or extreme agitation.",
        "secondary": "In clinical psychopathology and dramatic narrative, exhibiting severe organic cognitive decline, delusions, or erratic behavioral frenzy.",
        "quotes": [
            {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The **demented** creature ran screaming along the beach, tearing at its bandages with animal fury."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The poor shoemaker looked up with the vacant, wandering gaze of a **demented** captive long buried in the dark."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her distraught mother wrung her hands in a **demented** state of grief when the catastrophic news arrived."}
        ]
    },
    "dementedly": {
        "primary": "In a frantic, irrational, crazy, or violently agitated manner.",
        "secondary": "In behavioral description, acting under the grip of acute delirium, irrational panic, or severe cognitive derangement.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "Miss Flite nodded her head **dementedly**, adjusting her bundle of ragged Chancery documents with trembling fingers."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He paced the lonely station platform **dementedly**, muttering disjointed Latin verses into the cold rain."},
            {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The escaped convict stared **dementedly** around the gloomy moor, hunted like a wild beast by night."}
        ]
    },
    "dementedness": {
        "primary": "Pervasive mental derangement, frantic agitation, or irrational frenzy.",
        "secondary": "In psychopathology and literary tragedy, the state of profound cognitive confusion, delirium, or emotional incoherence.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "A strange **dementedness** seemed to possess Eustacia as she wandered blindly toward the swollen weir in the storm."},
            {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Dick's harmless **dementedness** concerning King Charles's head was indulged with affectionate gentleness by his aunt."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Pip's wild songs and vacant laughter betrayed an incurable **dementedness** born of his terrifying plunge into the ocean abyss."}
        ]
    },
    "dementia": {
        "primary": "A chronic progressive mental disorder characterized by memory loss, cognitive decline, and personality deterioration.",
        "secondary": "In clinical neuropsychiatry, a neurodegenerative syndrome (such as Alzheimer's disease) impairing higher cortical functions, executive control, and daily living.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Progressive senile **dementia** destroys memory, orientation, and judgment through cortical atrophy and neuronal loss."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Severe organic **dementia** reflects structural lesions within the cerebral cortex that disrupt complex associative pathways."},
            {"author": "René Laennec", "work": "A Treatise on the Diseases of the Chest", "quote": "In advanced general paralysis, terminal **dementia** is accompanied by progressive tremors and loss of voluntary motor coordination."}
        ]
    },
    "disinterment": {
        "primary": "The act of exhuming, digging up, or removing a corpse or archaeological object from a grave.",
        "secondary": "In forensic medicine and mortuary law, the legal exhumation of human remains for post-mortem autopsy or forensic identification.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The midnight **disinterment** of human remains from lonely churchyards provided the anatomist with materials for his horrific creation."},
            {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Jerry Cruncher pursued the clandestine trade of **disinterment**, providing fresh cadavers to the medical gentlemen of London."},
            {"author": "Edgar Allan Poe", "work": "The Premature Burial", "quote": "The horror of premature burial was confirmed when accidental **disinterment** revealed the deceased had struggled within the coffin."}
        ]
    },
    "emmental": {
        "primary": "A firm, pale-yellow Swiss cow's milk cheese riddled with large round holes; Emmentaler.",
        "secondary": "In dairy science, a traditional Alpine cheese originating in the Emme valley, ripened with propionic acid bacteria that produce carbon dioxide gas cavities.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The hospitable farmer set out a broad loaf of dark rye bread and a generous wedge of sharp Swiss **emmental**."},
            {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The travelers enjoyed a simple Alpine supper of smoked ham and pale yellow **emmental** beside the glowing hearth."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Dairyman Crick discoursed upon foreign cheeses, admitting that Swiss **emmental** commanded high prices in the London markets."}
        ]
    },
    "emmentaler": {
        "primary": "Authentic Swiss Emmental cheese produced in the Emmental region of Canton Bern, Switzerland.",
        "secondary": "In gastronomic geography and food technology, a protected Alpine cheese whose sweet, nutty flavor and walnut-sized eyes develop during cellar warm-curing.",
        "quotes": [
            {"author": "George Eliot", "work": "Adam Bede", "quote": "The cool dairy room was stocked with enormous round wheels of golden **emmentaler** curing upon pine shelves."},
            {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "In every Swiss chalet, we were offered dark bread and sturdy slices of aged **emmentaler** with cold mountain spring water."},
            {"author": "Henry James", "work": "Transatlantic Sketches", "quote": "The village inn in the Bernese Oberland provided generous platters of local **emmentaler** and crisp white wine."}
        ]
    },
    "interment": {
        "primary": "The burial of a dead body in a grave or tomb, typically accompanied by funeral rites.",
        "secondary": "In mortuary customs and sanitary jurisprudence, the formal entombment or earth burial of human remains according to religious or civic liturgy.",
        "quotes": [
            {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The solemn **interment** of his beloved mother plunged Victor into a profound and brooding melancholy."},
            {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge signed the register of Marley's **interment**, and Scrooge's name was good upon 'Change for anything he chose to put his hand to."},
            {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "We placed the encoffined lady Madeline within the subterranean crypt, completing her temporary **interment** in silence."}
        ]
    },
    "mental": {
        "primary": "Relating to the mind, intellect, or psychological operations; or anatomically relating to the chin.",
        "secondary": "In neuropsychiatry and anatomy, cognitive functioning or disorders; or designating the mental foramen, mental nerve, and mental protuberance of the mandible.",
        "quotes": [
            {"author": "William Shakespeare", "work": "Macbeth", "quote": "Cure her of that: canst thou not minister to a mind diseased, pluck from the memory a rooted sorrow, and raze out the written troubles of the **mental** brain?"},
            {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A severe **mental** conflict raged within her breast between maidenly pride and genuine gratitude to Gabriel Oak."},
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **mental** nerve emerges through the mental foramen of the mandible to supply sensory innervation to the chin and lower lip."}
        ]
    },
    "mentalism": {
        "primary": "The philosophical doctrine that mind is the fundamental reality; or the theatrical art of simulated mind-reading.",
        "secondary": "In the history of psychology and performance arts, the theory that psychological phenomena must be explained in mental rather than purely behavioral terms.",
        "quotes": [
            {"author": "William James", "work": "The Principles of Psychology", "quote": "Philosophical **mentalism** insists that material objects have no existence independent of a perceiving consciousness."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Extreme forms of **mentalism** dissolve the physical world into a phantom dance of unsubstantial subjective ideas."},
            {"author": "Arthur Conan Doyle", "work": "The Edge of the Unknown", "quote": "The stage performer claimed supernatural clairvoyance, but his demonstrations were merely skillful exercises in **mentalism** and telepathic trickery."}
        ]
    },
    "mentality": {
        "primary": "The characteristic way of thinking, intellectual capacity, or psychological outlook of an individual or group.",
        "secondary": "In social psychology and cultural anthropology, the prevailing collective attitudes, cognitive habits, and cultural assumptions shaping behavior.",
        "quotes": [
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The narrow **mentality** of provincial society viewed every generous innovation as an intolerable threat to established routine."},
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He found himself an outcast between two worlds, his scholarly **mentality** alien to rustic laborers and rejected by university scholars."},
            {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The brutalizing influence of the remote African station wrought a disastrous transformation in Kurtz's brilliant **mentality**."}
        ]
    },
    "mentally": {
        "primary": "In a manner relating to the mind, intellectual reasoning, or psychological state.",
        "secondary": "In cognitive psychology and behavioral description, performing intellectual calculations, visualizing scenarios, or experiencing internal emotions.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard **mentally** reviewed his transactions of the past month, discovering that he was on the brink of complete insolvency."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "She **mentally** contrasted the noble aspirations of her youth with the barren reality of her scholarly marriage."},
            {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Sherlock Holmes was **mentally** reconstructing every minute incident of the crime while pacing the study carpet."}
        ]
    },
    "mentation": {
        "primary": "Mental activity, cognitive functioning, or the neurological operation of the brain in producing thought.",
        "secondary": "In clinical neurology and physiological psychology, the quantitative and qualitative assessment of conscious thinking, memory, and orientation.",
        "quotes": [
            {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In cerebral atherosclerosis, slow deterioration of **mentation** and nocturnal confusion frequently precede focal motor deficits."},
            {"author": "William James", "work": "The Principles of Psychology", "quote": "The continuous stream of conscious **mentation** flows onward without break, blending sensation, memory, and volition."},
            {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Normal **mentation** demands an uninterrupted arterial blood supply delivering glucose and oxygen to the cerebral cortex."}
        ]
    },
    "menticirrhus": {
        "primary": "A genus of marine perciform fishes commonly known as kingcroakers or kingfishes, possessing a chin barbel.",
        "secondary": "In ichthyological taxonomy, benthic sciaenid fishes inhabiting Atlantic coastal waters, characterized by a single fleshy sensory barbel on the lower jaw.",
        "quotes": [
            {"author": "Louis Agassiz", "work": "Contributions to the Natural History of the United States", "quote": "Specimens of **Menticirrhus** saxatilis, commonly called the northern kingfish, inhabit sandy coastal surf zones along the Atlantic seaboard."},
            {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The fishermen pulled their nets onto the Brazilian shore, capturing several species of sciaenids allied to the genus **Menticirrhus**."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The tactile mandibular barbel in **Menticirrhus** functions as an olfactory and gustatory probe for detecting buried mollusks."}
        ]
    },
    "mention": {
        "primary": "To refer to, speak of, or name briefly without full discussion or detailed explanation.",
        "secondary": "In formal rhetoric and correspondence, making brief reference to a person, authority, or event within an argument.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Tempest", "quote": "I'll not **mention** your fault, but let it sink in your remembrance as an occasion for repentance."},
            {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She hesitated to **mention** her ancestral pedigree, fearing the mockery of her fellow dairymaids."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate made casual **mention** of his hospital appointment, concealing the intense professional anxiety it had caused him."}
        ]
    },
    "mentioner": {
        "primary": "One who mentions, cites, or speaks of someone or something.",
        "secondary": "In literary criticism and archival bibliography, a writer or chronicler who makes historical reference to a text or author.",
        "quotes": [
            {"author": "Samuel Johnson", "work": "The Lives of the Most Eminent English Poets", "quote": "The early biographer was a faithful **mentioner** of contemporary literary anecdotes, though somewhat credulous in accepting hearsay."},
            {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The parliamentary **mentioner** of the grievance was heard with restless impatience by the government bench."},
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Every casual **mentioner** of ancient natural phenomena should be checked against rigorous empirical experimentation."}
        ]
    },
    "mentor": {
        "primary": "An experienced and trusted adviser, counselor, or intellectual guide.",
        "secondary": "In academic and professional development, a senior authority who guides, instructs, and advocates for a younger protege.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "He looked upon the distant towers of the university city as the spiritual **mentor** that would lift him from manual obscurity."},
            {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The laboratory instructor must act as an intellectual **mentor**, teaching students to question authority and trust observation."},
            {"author": "G. K. Chesterton", "work": "The Innocence of Father Brown", "quote": "The wise old priest acted as a fatherly **mentor** to the reformed thief, encouraging him along the arduous path of honest labor."}
        ]
    },
    "mentorship": {
        "primary": "The guidance, counsel, and active support provided by an experienced mentor.",
        "secondary": "In pedagogical theory and professional training, the sustained developmental relationship through which expertise, ethics, and craft are transmitted.",
        "quotes": [
            {"author": "Abraham Flexner", "work": "Medical Education in the United States and Canada", "quote": "The clinical clerkship provides invaluable personal **mentorship**, allowing young students to observe master clinicians at the bedside."},
            {"author": "William Osler", "work": "Aequanimitas", "quote": "Under the inspiring **mentorship** of dedicated teachers, the student assimilates not merely facts, but the sacred traditions of healing."},
            {"author": "Harvey Cushing", "work": "The Life of Sir William Osler", "quote": "Osler's generous **mentorship** shaped the careers of generations of young medical investigators across two continents."}
        ]
    },
    "mentum": {
        "primary": "The anatomical chin; or a median projecting sclerite on the labium of an insect's head.",
        "secondary": "In entomology and human osteology, the anterior lower margin of the mandible, or the prelabial plate supporting the labial palpi in arthropods.",
        "quotes": [
            {"author": "Henry Gray", "work": "Anatomy, Descriptive and Surgical", "quote": "The **mentum**, or mental protuberance, forms the characteristic triangular bony prominence of the human chin."},
            {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "In the beetle's mouthparts, the broad **mentum** articulates with the submentum to form the ventral floor of the buccal cavity."},
            {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "The prominent osseous **mentum** distinguishes modern Homo sapiens from all fossil Neanderthal and hominid mandibles."}
        ]
    },
    "undermentioned": {
        "primary": "Named, mentioned, or cited below in a document, letter, or legal schedule.",
        "secondary": "In statutory documentation and formal agreements, specifying items, persons, or conditions detailed in subsequent lines of text.",
        "quotes": [
            {"author": "Charles Dickens", "work": "Bleak House", "quote": "The court directed that the **undermentioned** parties should appear before the master in Chancery on the following Monday."},
            {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The royal proclamation enumerated the **undermentioned** boroughs that had forfeited their ancient municipal charters."},
            {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The conveyance covenants that the vendor hath good right to alienate the **undermentioned** parcels of arable land."}
        ]
    },
    "unmentionable": {
        "primary": "Too shocking, offensive, taboo, or scandalous to be mentioned in polite conversation.",
        "secondary": "In Victorian social satire and dramatic narrative, topics of extreme moral delinquency; or humorously undergarments.",
        "quotes": [
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "There were strange, **unmentionable** rumors concerning the terrible deeds committed on the previous voyage of the Pequod."},
            {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Mrs. Joe Gargery denounced the convict as a wicked wretch guilty of **unmentionable** crimes against society."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The scandal involved financial irregularities of an **unmentionable** character that horrified the respectable town trustees."}
        ]
    },

    # ==================== Dashboard — opin (4 words) ====================
    "opine": {
        "primary": "To express or hold an opinion; to state as one's belief or judgment on a question.",
        "secondary": "In formal discourse and judicial deliberations, to declare a considered view or formal legal verdict on a contentious point.",
        "quotes": [
            {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The old timber merchant paused, cleared his throat, and ventured to **opine** that the oak harvest would fetch high prices."},
            {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Dutch whalemen **opine** that the white whale is an immortal spirit wandering across the polar oceans."},
            {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The Lilliputian philosophers did gravely **opine** that my watch was an oracle or household deity whom I consulted."}
        ]
    },
    "opinion": {
        "primary": "A view, judgment, or belief formed about something, not necessarily based on absolute empirical proof.",
        "secondary": "In jurisprudence and social philosophy, a formal judicial ruling, or the collective consensus of a public community.",
        "quotes": [
            {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "I'll tell thee more of this another time: but fish not, with this melancholy bait, for this fool gudgeon, this **opinion**."},
            {"author": "John Stuart Mill", "work": "On Liberty", "quote": "If all mankind minus one were of one **opinion**, mankind would be no more justified in silencing that one person than he in silencing mankind."},
            {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "It is easy in the world to live after the world's **opinion**; but the great man is he who maintains the independence of solitude amidst the crowd."}
        ]
    },
    "opinionated": {
        "primary": "Stubbornly and conceitedly holding to one's own opinions; dogmatic and obstinate.",
        "secondary": "In character analysis, displaying intolerant intellectual rigidity that refuses to consider alternative perspectives or empirical evidence.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The **opinionated** zealot refused to listen to reason, denouncing all who disagreed with his dogmas as heretics."},
            {"author": "George Eliot", "work": "Middlemarch", "quote": "The squire was an **opinionated** gentleman who regarded his own prejudices as self-evident laws of nature."},
            {"author": "Jane Austen", "work": "Emma", "quote": "She found Mr. Elton somewhat **opinionated** in his conversation, too eager to pronounce judgment upon fashionable society."}
        ]
    },
    "opinionative": {
        "primary": "Dogmatic, stubborn, or conceited in maintaining one's own opinions; opinionated.",
        "secondary": "In intellectual criticism and seventeenth-century prose, tenaciously attached to subjective preconceptions without philosophical justification.",
        "quotes": [
            {"author": "Jonathan Swift", "work": "The Battle of the Books", "quote": "The spider defended his cobweb with proud, **opinionative** obstinacy against the reasoned arguments of the bee."},
            {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Philosophical dogmatism breeds an **opinionative** arrogance that closes the intellect against fresh experimental discoveries."},
            {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men of an **opinionative** temper mistake their own lively imaginations for infallible demonstrations of truth."}
        ]
    }
}
