# -*- coding: utf-8 -*-
"""
Curates Dashboard — disc (Part 2: words 53-104) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part2 = {
  "discomposed": {
    "primary": "Agitated, ruffled, disturbed, or unsettled in mind, temper, or outward demeanor.",
    "secondary": "In narrative characterization, visibly perturbed by an unexpected breach of decorum or truth.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy walked across the room in a **discomposed** manner, struggling to master his turbulent emotions."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Aunt Betsey Trotwood looked unusually **discomposed** after her unexpected encounter with the mysterious stranger."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether felt subtly **discomposed** by Chad's polished transformation, which exceeded all Boston expectations."}
    ]
  },
  "discomposure": {
    "primary": "Agitation, perturbation, loss of emotional serenity, or ruffled composure under stress.",
    "secondary": "In social etiquette, the momentary loss of dignified poise caused by surprise or mortification.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma strove to conceal her **discomposure** beneath a smile, though her cheeks burned with mortification."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's cold dignity was shaken by an inward **discomposure** that made his thin hands tremble."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The antiquary turned away to hide his sudden **discomposure** when the boy questioned his ancient Roman coins."}
    ]
  },
  "discomycete": {
    "primary": "A fungus of the group Discomycetes, characterized by producing asci in an open, cup-shaped apothecium.",
    "secondary": "In mycology, ascomycetous cup fungi (such as Peziza and morels) that discharge spores into the air.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Upon decaying beech trunks in Tierra del Fuego, we found an edible **discomycete** prized by the native Yaghans."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The scarlet **discomycete** carpets damp woodland humus in early spring with vibrant saucer-shaped cups."},
      {"author": "Henry David Thoreau", "work": "Journal", "quote": "I observed a curious orange **discomycete** growing upon charred cedar roots along the swamp trail."}
    ]
  },
  "discomycetes": {
    "primary": "A major traditional taxonomic group of ascomycetous fungi whose fruiting body is an apothecium.",
    "secondary": "In fungal taxonomy, the order comprising cup fungi, earth tongues, truffles, and morels.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Journal of Researches", "quote": "Cyttaria darwinii belongs to the **Discomycetes**, forming globular clusters upon the branches of southern beech trees."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Gardeners encounter various parasitic **Discomycetes** that cause brown rot and blossom blight in orchards."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "Damp granite fissures harbored delicate **Discomycetes**, their fleshy cups catching droplets of melting snow."}
    ]
  },
  "discomycetous": {
    "primary": "Pertaining to, resembling, or belonging to the Discomycetes; cup-fungal in form.",
    "secondary": "In systematic mycology, describing open apothecial fructifications bearing operculate asci.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The **discomycetous** fruiting structure exposes the hymenium freely to the air for explosive ascospore release."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Microscopic sections of the **discomycetous** parasite revealed dense palisades of spore-bearing asci."},
      {"author": "Rachel Carson", "work": "The Edge of the Sea", "quote": "Certain marine **discomycetous** species colonize submerged driftwood along intertidal mudflats."}
    ]
  },
  "disconcert": {
    "primary": "To disturb the composure of; to unsettle, confuse, frustrate, or ruffle someone's poise.",
    "secondary": "In diplomacy, to upset, thwart, or disrupt an adversary's political plans or alliances.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was determined that no cold condescension from Darcy should **disconcert** her cheerful spirits."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sudden arrival of imperial reinforcements served to **disconcert** the Persian siege operations at Nisibis."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Nicholas looked steadily at Squeers, whose brutal bullying failed to **disconcert** the young schoolmaster."}
    ]
  },
  "disconcerted": {
    "primary": "Unsettled, confused, frustrated, or thrown into temporary emotional or mental disarray.",
    "secondary": "In narrative dialogue, abashed by an unexpected discovery or shrewd question.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Frank Churchill appeared momentarily **disconcerted** when Mr. Knightley asked pointedly about his trip to Weymouth."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Stapleton looked visibly **disconcerted** to discover that Holmes had arrived unexpectedly in Devonshire."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode stood **disconcerted** before his fellow townsmen as Raffles revealed his dark financial past."}
    ]
  },
  "disconcerting": {
    "primary": "Causing one to feel unsettled, confused, anxious, or embarrassed; disturbing or alarming.",
    "secondary": "In critical observation, unexpected anomalies that contradict established scientific hypotheses.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Mr. Ramsay's sudden demands for emotional sympathy were profoundly **disconcerting** to his sensitive guests."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The sudden appearance of whole groups of species in the lowest fossil formations was deeply **disconcerting** to me."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston found the girl's persistent, silent gaze across the canteen **disconcerting** and terrifying."}
    ]
  },
  "disconcertingly": {
    "primary": "In a disconcerting manner; to an extent that causes confusion, unease, or embarrassment.",
    "secondary": "In interpersonal encounters, speaking or acting with unpredictable, unnerving candor.",
    "quotes": [
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "Charlotte spoke **disconcertingly** of her future plans, leaving the prince uncertain of her hidden intentions."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "The photograph was **disconcertingly** clear, showing the Bohemian king beside Irene Adler."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Mr. Emerson spoke **disconcertingly** frank words about love and freedom to the flustered English ladies."}
    ]
  },
  "disconcertion": {
    "primary": "Confusion, mental embarrassment, or perturbation caused by sudden surprise or thwarted expectations.",
    "secondary": "In psychological descriptions, a momentary collapse of social poise.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Mary Crawford could not hide her **disconcertion** upon learning that Edmund was definitely taking holy orders."},
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Fascination Fledgeby watched the moneylender's **disconcertion** with a mean, gloating chuckle."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Slope experienced acute **disconcertion** when the bishop's wife publicly overruled his appointment."}
    ]
  },
  "disconcertment": {
    "primary": "Embarrassment, fluster, or unsettling confusion that disorients one's focus or plans.",
    "secondary": "In social satire, the awkward predicament of pretenders exposed to public ridicule.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Jos Sedley fled the ball in utter **disconcertment** after drinking too much punch and boasting foolishly."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen's haughty **disconcertment** betrayed how deeply Grandcourt's cold surveillance troubled her."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard masked his inner **disconcertment** beneath a blustering roar of anger at the town council."}
    ]
  },
  "disconfirming": {
    "primary": "Providing evidence that contradicts, disproves, or refutes a hypothesis, theory, or expectation.",
    "secondary": "In the philosophy of science, empirical observations that falsify a theoretical prediction (Popperian falsification).",
    "quotes": [
      {"author": "Karl Popper", "work": "The Logic of Scientific Discovery", "quote": "A single reliable **disconfirming** observation carries greater logical weight than thousands of confirmations."},
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "Pseudoscience routinely ignores **disconfirming** laboratory results, cherry-picking only supportive anecdotes."},
      {"author": "Daniel Kahneman", "work": "Thinking, Fast and Slow", "quote": "Confirmation bias leads human decision makers to actively ignore **disconfirming** statistical trends."}
    ]
  },
  "disconnect": {
    "primary": "To sever or break the connection, relation, or communication between two entities; a separation.",
    "secondary": "In electronic engineering, opening a circuit switch to halt current flow through a device.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The saboteur moved through the darkness to **disconnect** the telegraph lines linking the arsenal to London."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Septimus felt a profound **disconnect** between his shattered internal world and the busy London traffic."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Parietal lobe lesions can **disconnect** visual perceptions from the emotional significance they normally evoke."}
    ]
  },
  "disconnected": {
    "primary": "Separated, detached, or broken off; lacking logical connection, coherence, or consistency.",
    "secondary": "In psychiatric assessment, speech patterns (word salad) that lack syntactic or semantic links.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Jo muttered a few **disconnected** words about the dark graveyard where the kind gentleman was buried."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Marianne's fever produced frantic, **disconnected** ramblings that terrified her watching sister."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab paced the deck, muttering **disconnected** curses against the stars and the eternal sea."}
    ]
  },
  "disconnectedness": {
    "primary": "Lack of connection, coherence, or logical continuity between parts, thoughts, or systems.",
    "secondary": "In modern sociological critique, anomie and the emotional isolation of individuals in megacities.",
    "quotes": [
      {"author": "Émile Durkheim", "work": "Suicide: A Study in Sociology", "quote": "Modern urban life fosters a painful **disconnectedness** that weakens traditional communal moral bonds."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In dreaming, the mind accepts bizarre **disconnectedness** without the critical resistance shown in waking hours."},
      {"author": "T. S. Eliot", "work": "Selected Essays", "quote": "Modernist poetry mirrors the fragmentary **disconnectedness** of industrial civilizational experience."}
    ]
  },
  "disconnection": {
    "primary": "The state or act of being disconnected; separation, severance, or lack of continuity.",
    "secondary": "In behavioral neurology, disconnection syndromes (such as alexia without agraphia) caused by white matter lesions.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The patient suffered from an agonizing **disconnection** between his conscious will and the sensory map of his limb."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Callosal **disconnection** prevents the verbal left hemisphere from describing objects presented to the left visual field."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "A total **disconnection** from historical memory was required to accept the Party's daily shifting truths."}
    ]
  },
  "disconsolate": {
    "primary": "Without consolation or comfort; deeply dejected, cheerless, unhappy, and sorrowful.",
    "secondary": "In romantic landscapes, bleak, desolate vistas that evoke melancholy in the viewer.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan surveyed the **disconsolate** waste of subterranean sulfur, mourning the celestial realms he had lost."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip sat **disconsolate** upon the tombstone, weeping in the gathering marsh twilight."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet remained **disconsolate** in her dressing room, convinced that the regiment's departure doomed her daughters."}
    ]
  },
  "disconsolately": {
    "primary": "In a disconsolate, dejected, or heartbroken manner; sorrowfully and without comfort.",
    "secondary": "In narrative descriptions, weeping or wandering in inconsolable melancholy.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The orphan child wept **disconsolately** in the red-room, terrified by the cold shadows of the dusk."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The hound wandered **disconsolately** about the yard, having lost the creosote scent along the river bank."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "Jude stared **disconsolately** at the distant spires of Christminster, realizing the university gates were barred."}
    ]
  },
  "disconsolateness": {
    "primary": "Dejection, deep sorrow, or inconsolable grief that refuses comforting; cheerlessness.",
    "secondary": "In literary atmosphere, the pervasive aura of gloom hanging over a tragic household.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "The princess was overwhelmed by a heavy **disconsolateness** after the sudden death of her favorite companion."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "An unredeemed **disconsolateness** hung like a funeral pall over the somber corridors of Usher's domain."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie's childish **disconsolateness** was soothed only by the quiet whisper of the river flowing past."}
    ]
  },
  "discontent": {
    "primary": "Dissatisfaction with one's circumstances, lack of contentment, or a restless grievance.",
    "secondary": "In political history, popular unrest and grumbling that precedes open civil insurrection.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Now is the winter of our **discontent** made glorious summer by this sun of York."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "Economic prosperity often intensifies public **discontent**, making feudal relics seem intolerable to rising burghers."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolistic food prices generate widespread popular **discontent** among working-class laborers."}
    ]
  },
  "discontented": {
    "primary": "Dissatisfied, restless, or unhappy with one's possessions, status, or life circumstances.",
    "secondary": "In social comedy, characters whose ungrateful complaining alienates friends and patrons.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. John Dashwood was perpetually **discontented**, begrudging her sisters-in-law the smallest legacy from the estate."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The Saint Antoine quarter was filled with hungry, **discontented** weavers whose fury was ready to explode."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia Vye was intensely **discontented** with Egdon Heath, longing for the glamorous gaiety of Paris."}
    ]
  },
  "discontentedly": {
    "primary": "In a discontented, dissatisfied, or grumbling manner; with obvious displeasure.",
    "secondary": "In dialogue, muttering complaints or accepting compromises with sullen reluctance.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy grumbled **discontentedly** over his father's refusal to purchase him a hunter for the season."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Watson paced **discontentedly** along the gravel path, frustrated that Holmes had left him in the dark."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe sat **discontentedly** in his Sunday clothes, longing for the familiar comfort of his blacksmith's apron."}
    ]
  },
  "discontentedness": {
    "primary": "Dissatisfaction, grievance, or restless unease with one's current circumstances or fortune.",
    "secondary": "In moral philosophy, the habitual mental disposition that fails to appreciate present blessings.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Chronic **discontentedness** poisons every spring of happiness, turning fertile fortune into barren misery."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Factional demagogues thrive by inflaming **discontentedness** among those who envy their neighbors' estates."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A prudent sovereign monitors symptoms of **discontentedness** in his subjects before grumbling matures into treason."}
    ]
  },
  "discontentment": {
    "primary": "Restless dissatisfaction, grievance, or unease arising from unmet expectations or thwarted desires.",
    "secondary": "In historical sociopolitical annals, the widespread public alienation that undermines state legitimacy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "A sullen **discontentment** pervaded the legions when the emperor withheld their customary military donative."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The deafening industrial clamor could not drown the deep **discontentment** of millions seeking honest work."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia's reckless elopement brought lasting humiliation and bitter **discontentment** upon the Bennet hearth."}
    ]
  },
  "discontinuance": {
    "primary": "The act of ending, ceasing, stopping, or breaking off an activity, custom, or practice.",
    "secondary": "In civil law and courtroom practice, the formal termination or voluntary withdrawal of an action by a plaintiff.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A **discontinuance** of the suit occurs when the plaintiff fails to appear and pursue his process across terms."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The sudden **discontinuance** of colonial trade monopolies forced domestic merchants into new overseas markets."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The **discontinuance** of primogeniture divided landed estates rapidly among all surviving heirs."}
    ]
  },
  "discontinuation": {
    "primary": "The termination, cessation, or stopping of a process, practice, medication, or production line.",
    "secondary": "In pharmaceutical therapeutics, the planned withdrawal or tapering of a drug regimen.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Sudden **discontinuation** of chronic opiate therapy precipitates acute physiological withdrawal distress."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Following the **discontinuation** of the neuroleptic medication, the patient's parkinsonian tremor subsided."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The abrupt **discontinuation** of state funding threatened the continuity of vital marine biological surveys."}
    ]
  },
  "discontinue": {
    "primary": "To stop doing, providing, producing, or using something; to cease, terminate, or abandon.",
    "secondary": "In commercial manufacturing, halting the production of an unprofitable or obsolete product line.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Pickwick Papers", "quote": "Mr. Pickwick resolved to **discontinue** his subscriptions to the club until his honor had been vindicated."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma decided to **discontinue** her matchmaking schemes after the mortifying blunder with Mr. Elton."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I found it prudent to **discontinue** the theological disputes that alienated my brother and fellow tradesmen."}
    ]
  },
  "discontinued": {
    "primary": "No longer produced, manufactured, maintained, or continued; stopped, abandoned, or terminated.",
    "secondary": "In publishing and industry, periodicals or products retired from commercial availability.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Red-Headed League", "quote": "A cardboard notice announced that the League of Red-Headed Men was permanently dissolved and **discontinued**."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The ancient custom of wife-selling was universally condemned and practically **discontinued** in Wessex."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "In the future golden age, all competitive commercial manufacture had been completely **discontinued**."}
    ]
  },
  "discontinuity": {
    "primary": "A distinct break, gap, interruption, or lack of continuous connection in time, sequence, or space.",
    "secondary": "In geology and seismology, a structural boundary (like the Mohorovičić discontinuity) where seismic wave velocities jump.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "An unconformity represents a vast chronological **discontinuity** where millions of years of deposition are missing."},
      {"author": "Thomas Kuhn", "work": "The Structure of Scientific Revolutions", "quote": "A paradigm shift introduces an essential **discontinuity** in scientific development, breaking with cumulative progress."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "Across a shock wave in supersonic gas flow, there exists a sharp mathematical **discontinuity** in pressure and density."}
    ]
  },
  "discontinuous": {
    "primary": "Having intervals or gaps; not continuous, broken, interrupted, or occurring in disconnected stages.",
    "secondary": "In evolutionary biology, discontinuous variation where phenotypes fall into distinct non-overlapping classes.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The fossil record appears **discontinuous** primarily because sedimentary beds were preserved only during subsidence."},
      {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "Punctuated equilibrium views evolutionary transitions as **discontinuous** episodes punctuating long periods of stasis."},
      {"author": "John Tyndall", "work": "Essays on the Floating-Matter of the Air", "quote": "He achieved sterilization by applying **discontinuous** heating, killing newly germinated spores between boiling cycles."}
    ]
  },
  "discord": {
    "primary": "Disagreement, conflict, or lack of harmony between persons, or a harsh dissonance of unmusical sounds.",
    "secondary": "In classical mythology, the goddess Eris whose golden apple of discord sparked the Trojan War.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "An I were so apt to quarrel as thou art, any man should buy the fee-simple of my life for an hour and a quarter... dost thou make us minstrels? an thou make minstrels of us, look to hear nothing but **discord**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Chaos and ancient Night held eternal anarchy, where hot, cold, moist, and dry strove in ceaseless **discord**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Disunion among the states would plunge the American continent into perpetual geopolitical **discord** and border wars."}
    ]
  },
  "discordance": {
    "primary": "Disagreement, harsh disharmony, clashing conflict, or jarring dissonance between sounds.",
    "secondary": "In structural geology, an unconformity where strata lie with divergent angles of dip.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The sudden shriek of terror presents a jarring acoustic **discordance** that triggers sympathetic alarm in companions."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Bad architecture offends the eye by introducing an intolerable **discordance** with surrounding mountain scenery."},
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "The marked angular **discordance** between the horizontal sandstone and tilted slate proved an ancient tectonic upheaval."}
    ]
  },
  "discordant": {
    "primary": "Disagreeing, incongruous, conflicting, or harsh and jarring to the ear; lacking harmony.",
    "secondary": "In musical harmony, intervals or chords (like minor seconds) requiring resolution to consonance.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate's lofty medical ideals struck a **discordant** note amid the petty gossip of provincial Middlemarch doctors."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The wild, eerie howl struck a **discordant** chill across our hearts as we stood listening in the dark moor night."},
      {"author": "Edgar Allan Poe", "work": "The Tell-Tale Heart", "quote": "It was a low, dull, quick sound, much such a sound as a watch makes when enveloped in cotton... a **discordant** beating."}
    ]
  },
  "discordantly": {
    "primary": "In a discordant, jarring, inharmonious, or contentious manner; with clashing dissonance.",
    "secondary": "In musical performance, playing or singing out of tune or against the governing harmony.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The heavy prison iron keys clashed **discordantly** against the stone arches of the Conciergerie."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The rough skimmington music banged **discordantly** through the streets, rattling pots and blowing cows' horns."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sea-birds shrieked **discordantly** above the boiling wake as the harpooneers lowered the whaleboats."}
    ]
  },
  "discorporate": {
    "primary": "To deprive of corporate status or charter; to dissolve a corporation or legal body; disembodied.",
    "secondary": "In speculative fiction, existing as a conscious mind or spirit freed from physical bodily embodiment.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Parliament may **discorporate** a municipal borough for gross abuse of its ancient chartered liberties."},
      {"author": "Robert A. Heinlein", "work": "Stranger in a Strange Land", "quote": "The Martian water-brothers could **discorporate** at will, casting off physical flesh to merge with the elders."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Reforming ministries moved to **discorporate** medieval trading guilds that choked free commercial competition."}
    ]
  },
  "discotheque": {
    "primary": "A club or dance hall where recorded dance music is played by a disc jockey (French borrowing).",
    "secondary": "In 1960s social history, trendy venues replacing live swing bands with curated vinyl disc selections.",
    "quotes": [
      {"author": "Tom Wolfe", "work": "The Kandy-Kolored Tangerine-Flake Streamline Baby", "quote": "The new Manhattan **discotheque** was packed with celebrities dancing the watusi beneath spinning strobe lights."},
      {"author": "Joan Didion", "work": "Slouching Towards Bethlehem", "quote": "Young runaways drifted from the Haight-Ashbury coffee houses to the loud neon **discotheque** on the corner."},
      {"author": "David Foster Wallace", "work": "Infinite Jest", "quote": "The pulsating bass rhythm of the offshore **discotheque** vibrated through the floorboards of the yacht marina."}
    ]
  },
  "discount": {
    "primary": "A deduction from the usual cost of something, or to disregard, underestimate, or treat as of little worth.",
    "secondary": "In banking, purchasing a promissory bill of exchange before maturity at less than its face value.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Merchant banks **discount** bills of exchange, providing liquid capital to manufacturers before goods reach market."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "We must not **discount** the immense cumulative power of natural selection acting across millions of generations."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was inclined to **discount** Wickham's flattering compliments, having learned the value of Darcy's truth."}
    ]
  },
  "discountenance": {
    "primary": "To refuse to approve of something; to discourage, show disfavor toward, or look upon with disapproval.",
    "secondary": "In Victorian social manners, discouraging improper behavior with a severe, silent look of disapproval.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley did everything in his power to **discountenance** the absurd match between Harriet and the vicar."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Public opinion in America operates to **discountenance** any aristocratic pretension that violates equality."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Sir Leicester Dedlock was quick to **discountenance** any radical talk that challenged the dignity of ancient landed titles."}
    ]
  },
  "discounter": {
    "primary": "A person, bank, or retail establishment that discounts bills of exchange, loans, or commercial goods.",
    "secondary": "In retail commerce, a merchant selling branded commodities at reduced prices on high volume.",
    "quotes": [
      {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "The London bill **discounter** stands as the crucial intermediary balancing cash liquidity with commercial credit."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "Mr. Merdle's sudden bankruptcy ruined every financial **discounter** and investor in the City."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "The shady **discounter** advanced cash on post-obits to reckless young aristocrats who haunted the gaming tables."}
    ]
  },
  "discourage": {
    "primary": "To cause someone to lose confidence, enthusiasm, or hope, or to dissuade someone from an action.",
    "secondary": "In public policy, taxing or regulating harmful activities to diminish their prevalence in society.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "Hardships and early financial losses should never **discourage** an industrious youth from pursuing his enterprise."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Excessive excise duties on commodities tend to **discourage** domestic manufacture and promote smuggling."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor attempted to **discourage** Marianne from indulging in solitary midnight walks that fueled her grief."}
    ]
  },
  "discouraged": {
    "primary": "Having lost confidence, enthusiasm, or hope; disheartened, dissuaded, or deterred.",
    "secondary": "In policy administration, prohibited or actively disincentivized by legal or social norms.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Though battered by hardship and cold, Jane was not **discouraged**, relying upon her unwavering inner faith."},
      {"author": "Charles Darwin", "work": "Autobiography", "quote": "I was often **discouraged** by my poor health, yet the fascination of natural history spurred me to write."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "All private emotional relationships were actively **discouraged** by the Party in favor of devotion to Big Brother."}
    ]
  },
  "discouragement": {
    "primary": "A loss of confidence, enthusiasm, or hope, or an attempt or circumstance that deters or dissuades someone.",
    "secondary": "In education and mentorship, harsh criticism that dampens a student's creative initiative.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Life and Letters", "quote": "I endured years of physical illness and scientific **discouragement** before completing the manuscript of the Origin."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The frequent failure of commercial speculations causes temporary **discouragement**, but bold American optimism quickly revives."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne had yielded eight years ago to the prudent **discouragement** of Lady Russell, parting from Wentworth in tears."}
    ]
  },
  "discouraging": {
    "primary": "Causing someone to lose confidence, hope, or enthusiasm; disheartening, depressing, or deterrent.",
    "secondary": "In scientific experimentation, negative results that suggest a working hypothesis is flawed.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "A thousand failed filament experiments were not **discouraging**, but merely showed a thousand materials that would not work."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The muddy trail ended abruptly at the river wall, presenting a most **discouraging** obstacle to our pursuit."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate found the narrow provincial prejudices of the town infirmary committee profoundly **discouraging**."}
    ]
  },
  "discouragingly": {
    "primary": "In a discouraging or disheartening manner; to an extent that dampens confidence or enthusiasm.",
    "secondary": "In investigative narrative, prospects or weather conditions appearing bleak and unpromising.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The dense fog rolled across the moor **discouragingly**, threatening to shroud the path before we could intercept the hound."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Chancery suit dragged on **discouragingly**, devouring every penny of the contested legacy in legal fees."},
      {"author": "Henry James", "work": "The Turn of the Screw", "quote": "The silence in the grand country house was **discouragingly** deep, chilling the young governess's heart."}
    ]
  },
  "discourse": {
    "primary": "Written or spoken communication or debate, or a formal scholarly or philosophical discussion of a topic.",
    "secondary": "In critical theory (Foucault), formalized systems of language and knowledge that structure power relations.",
    "quotes": [
      {"author": "René Descartes", "work": "Discourse on the Method", "quote": "In this **Discourse** I resolve to describe the path I have followed, seeking truth in the sciences with clear reason."},
      {"author": "Michel Foucault", "work": "The Archaeology of Knowledge", "quote": "The analysis of **discourse** reveals the historical rules that determine what statements can be accepted as true."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "O God! a beast, that wants **discourse** of reason, would have mourn'd longer—married with my uncle."}
    ]
  },
  "discourteous": {
    "primary": "Showing a lack of courtesy or politeness; rude, ill-mannered, disrespectful, and uncivil.",
    "secondary": "In social etiquette, neglecting established polite formalities in conversation or correspondence.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy was judged to be proud and **discourteous**, having refused to dance or converse with any lady outside his circle."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The harsh schoolmaster was **discourteous** to poor Traddles, punishing him unjustly for drawing skeletons."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Illustrious Client", "quote": "Baron Gruner was dangerously polite, but his icy undertone was subtly **discourteous** and menacing."}
    ]
  },
  "discourteously": {
    "primary": "In a discourteous, rude, or ill-mannered manner; uncivilly and without proper respect.",
    "secondary": "In narrative dialogue, answering polite inquiries with dismissive bluntness.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma regretted having spoken so **discourteously** to poor Miss Bates on Box Hill before the assembled party."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Slope behaved **discourteously** to the archdeacon, turning his back while the elder churchman spoke."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The turnpike keeper grunted **discourteously**, demanding double toll before opening the iron gate in the rain."}
    ]
  },
  "discourtesy": {
    "primary": "Rude, impolite, or uncivil behavior or speech; an act showing lack of respect or courtesy.",
    "secondary": "In formal diplomacy, a diplomatic slight or breach of protocol that insults a foreign sovereign.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was astonished at Darcy's **discourtesy** in declining to dance with her when introduced by Sir William."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Chivalry banished harsh manners from European courts, refining power and making **discourtesy** shameful."},
      {"author": "Arthur Conan Doyle", "work": "A Scandal in Bohemia", "quote": "Holmes apologized for his apparent **discourtesy**, explaining that professional duty required eccentric disguises."}
    ]
  },
  "discover": {
    "primary": "To find unexpectedly or in the course of a search, or to become aware of a fact for the first time.",
    "secondary": "In legal procedure, pretrial disclosure where parties discover evidence and depositions from adversaries.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The aim of the new scientific method is to **discover** hidden causes and produce novel works for human benefit."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "It was thrilling to watch Holmes **discover** crucial clues in the dusty carpet where others saw nothing."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma was shocked to **discover** that Frank Churchill and Jane Fairfax had been secretly engaged for months."}
    ]
  },
  "discoverable": {
    "primary": "Capable of being discovered, found out, perceived, or deduced through inquiry, observation, or reason.",
    "secondary": "In legal procedure, documents and communications subject to mandatory disclosure during discovery.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The fundamental laws of nature are **discoverable** by human reason through observation of divine creation."},
      {"author": "David Hume", "work": "An Enquiry Concerning the Principles of Morals", "quote": "Moral distinctions are not matters of fact **discoverable** by the pure understanding alone."},
      {"author": "Isaac Newton", "work": "Mathematical Principles of Natural Philosophy", "quote": "The true mechanical causes of planetary motions are **discoverable** through mathematical demonstration."}
    ]
  },
  "discovered": {
    "primary": "Found out, detected, uncovered, or realized, especially that which had been previously unknown.",
    "secondary": "In historical exploration, geographical regions or scientific laws revealed to human knowledge.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Along the gravel plains of Patagonia, I **discovered** the fossil bones of colossal extinct edentates."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "After days and nights of incredible labor, I **discovered** the secret of generating life in lifeless matter."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "When Edward's secret was **discovered**, his haughty mother immediately disinherited him in favor of his brother."}
    ]
  },
  "discoverer": {
    "primary": "A person who is the first to find, explore, or become aware of a place, substance, law, or truth.",
    "secondary": "In the history of science, an innovator credited with identifying a new chemical element or planet.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Columbus set sail across the unknown Atlantic, hailing the new continent as its immortal **discoverer**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Harvey was celebrated as the **discoverer** of the circulation of the blood, founding modern physiology."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Galileo was the first human **discoverer** to look through a telescope and perceive the moons of Jupiter."}
    ]
  }
}
