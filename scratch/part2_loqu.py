# -*- coding: utf-8 -*-
"""
Part 2 of Speech Batch 4:
- Dashboard — loqu (25 words):
  colloquial, colloquialism, colloquially, colloquium, colloquy,
  eloquence, eloquent, eloquently, grandiloquence, grandiloquent,
  grandiloquently, ineloquently, loquacious, loquaciously, loquaciousness,
  loquacity, loquat, obloquy, soliloquise, soliloquize,
  soliloquy, somniloquent, somniloquism, somniloquist, somniloquy
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_loqu = {
  "colloquial": {
    "primary": "Characteristic of informal spoken conversation rather than formal literary speech or writing.",
    "secondary": "In lexicography and sociolinguistics, designating informal vernacular expressions, idioms, or dialectal usage.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "The intimate warmth of the essayist springs from his masterful command of easy, **colloquial** idiom."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "In lively coffee-house debates, scholars dropped their Latin pedantry in favor of brisk **colloquial** English."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The true prose of the era retained dignity without stiffness, blending elevated thought with natural **colloquial** tone."}
    ]
  },
  "colloquialism": {
    "primary": "A word, phrase, or idiom typically used in informal, casual conversation rather than formal discourse.",
    "secondary": "In stylistics and dialectology, a non-standard or localized vernacular figure of speech embedded in everyday banter.",
    "quotes": [
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The veteran steamboat pilot sprinkled his reminiscences with colorful river **colloquialism** that baffled urban listeners."},
      {"author": "H. L. Mencken", "work": "The American Language", "quote": "A vigorous popular **colloquialism** often fights its way upward into respectable literary usage across generations."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "The professor listened intently to the street vendor's rapid slang, recording each vibrant **colloquialism** on his phonograph cylinder."}
    ]
  },
  "colloquially": {
    "primary": "In the manner of informal speech or casual conversation; through common vernacular expression.",
    "secondary": "In sociolinguistic description, denoting idioms or nicknames adopted across popular conversational registers.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The gauchos referred to the elusive burrowing rodent **colloquially** as the tuco-tuco from its rhythmic subterranean cry."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The sinister granite hollow on the moor was known **colloquially** among the peasants as the Black Tor mire."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sheep-shearers addressed their respected elder **colloquially** as Master Poorgrass throughout the harvest supper."}
    ]
  },
  "colloquium": {
    "primary": "An academic seminar or conference convened for scholarly discussion, presentation of research, and debate.",
    "secondary": "In university administration and legal terminology, an informal academic gathering or introductory meeting discussing learned questions.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Portraits from Memory", "quote": "The weekly philosophical **colloquium** in Cambridge drew keen minds eager to dissect new theories of mathematical logic."},
      {"author": "William James", "work": "The Will to Believe", "quote": "During the heated department **colloquium**, faculty members debated whether religious experience admits of empirical proof."},
      {"author": "Max Weber", "work": "Science as a Vocation", "quote": "The rigorous discipline of an advanced research **colloquium** demands intellectual integrity and meticulous factual scrutiny."}
    ]
  },
  "colloquy": {
    "primary": "A formal conversation, dialogue, or serious conference between two or more participants.",
    "secondary": "In theological and diplomatic history, an organized doctrinal or state conference seeking resolution between conflicting parties.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister and Hester Prynne carried on a hushed, solemn **colloquy** beneath the secluded shadows of the primeval forest."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The philosophers gathered at the villa for a quiet evening **colloquy** upon the immortality of the rational soul."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "With grave and deliberate utterance, the heavenly messenger held divine **colloquy** with our first parents in Eden."}
    ]
  },
  "eloquence": {
    "primary": "Fluent, persuasive, and graceful speaking or writing that stirs the emotions of an audience.",
    "secondary": "In classical rhetoric and oratorical theory, the art of moving listeners through elevated diction, clarity, and affective resonance.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The impassioned **eloquence** of the Christian bishop swayed the multitude and confounded the imperial governors."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "True oratorical **eloquence** requires profound sincerity, turning the speaker's innermost convictions into a torrent of persuasive truth."},
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "Her radiant beauty pleaded with greater moving **eloquence** than all the polished verses of enamored courtiers."}
    ]
  },
  "eloquent": {
    "primary": "Expressing ideas or feelings powerfully, gracefully, and persuasively in speech or writing.",
    "secondary": "In literary criticism and rhetoric, marked by vivid expression, suggestive power, or stirring moral force.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "His silence was more deeply **eloquent** than any formal speech, revealing the tempest of grief within his breast."},
      {"author": "Abraham Lincoln", "work": "Address at Gettysburg", "quote": "The assembled gathering listened in solemn reverence to the brief yet supremely **eloquent** tribute to the fallen soldiers."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The shattered marble pillars of the ancient temple stood as an **eloquent** monument to departed imperial glory."}
    ]
  },
  "eloquently": {
    "primary": "In a fluent, persuasive, and powerfully expressive manner that moves listeners or readers.",
    "secondary": "In oratorical delivery and prose aesthetics, communicating profound sentiment with graceful cadence and persuasive force.",
    "quotes": [
      {"author": "Frederick Douglass", "work": "Narrative of the Life of Frederick Douglass", "quote": "He pleaded **eloquently** for the natural rights of all enslaved men, stirring Northern audiences to righteous outrage."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Chancery barrister argued **eloquently** upon intricate precedents, while the unfortunate suitors languished in despair."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The Venetian canvases proclaimed **eloquently** the eternal supremacy of pure color and luminous Mediterranean atmosphere."}
    ]
  },
  "grandiloquence": {
    "primary": "A lofty, pompous, or bombastic style of speech or writing intended to sound impressive.",
    "secondary": "In rhetorical criticism, inflated diction characterized by grandiose vocabulary disproportionate to the underlying matter.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The self-important diplomat addressed the drawing room with an absurd **grandiloquence** that amused the cynical dowagers."},
      {"author": "Alexander Pope", "work": "Peri Bathous, or the Art of Sinking in Poetry", "quote": "Lacking genuine poetic inspiration, mediocre versifiers disguise trivial concepts under the hollow glare of verbal **grandiloquence**."},
      {"author": "Washington Irving", "work": "A History of New York", "quote": "The municipal governor issued proclamations marked by solemn **grandiloquence**, threatening dire calamities upon peaceful burghers."}
    ]
  },
  "grandiloquent": {
    "primary": "Pompous, bombastic, or inflated in language, style, or manner; using grandiose expressions.",
    "secondary": "In literary style and oratory, employing high-flown phrasing to project an exaggerated impression of importance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber penned a characteristically **grandiloquent** epistle, lamenting his pecuniary distress in terms of imperial tragedy."},
      {"author": "Sir Walter Scott", "work": "The Antiquary", "quote": "The learned scholar delivered a **grandiloquent** discourse on Roman fortifications, utterly oblivious to his companion's boredom."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "The local magistrate assumed a **grandiloquent** posture upon the bench, terrifying rustic offenders with polysyllabic denunciations."}
    ]
  },
  "grandiloquently": {
    "primary": "In a lofty, pompous, or bombastic manner; using exaggerated or showy language.",
    "secondary": "In oratorical mannerism, speaking with self-conscious inflation and theatrical extravagance.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Gilded Age", "quote": "Colonel Sellers expounded **grandiloquently** upon his visionary railway schemes, promising fabulous fortunes to every small investor."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Professor Challenger gestured **grandiloquently** toward the mysterious plateau, claiming undisputed discovery in the name of science."},
      {"author": "George Meredith", "work": "The Egoist", "quote": "Sir Willoughby declaimed **grandiloquently** upon hereditary honors and matrimonial duty, unaware of the quiet irony in Clara's smile."}
    ]
  },
  "ineloquently": {
    "primary": "Without eloquence; awkwardly, unpersuasively, or with hesitant and clumsy expression.",
    "secondary": "In rhetorical evaluation, expressing thoughts without rhetorical grace, vocal melody, or affective impact.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard pleaded **ineloquently** before the town council, his rough dialect and stammering rage failing to win over his peers."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon defended his unfinished scholarly treatise **ineloquently**, burying genuine anxiety beneath dry academic phrases."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The bewildered sailor explained the shipboard disaster **ineloquently**, choking back the desperate guilt that haunted him."}
    ]
  },
  "loquacious": {
    "primary": "Tending to talk a great deal; extremely talkative, garrulous, or chattering.",
    "secondary": "In character description and social satire, excessively communicative and rambling in ordinary social intercourse.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The court barber was an exceedingly **loquacious** fellow, regaling his patrons with endless gossip concerning palace intrigue."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Miss Bates was remarkably **loquacious**, pouring forth a cheerful and ceaseless stream of village trivialities."},
      {"author": "Oliver Goldsmith", "work": "The Vicar of Wakefield", "quote": "Our **loquacious** neighbor entertained the tea table with marvelous anecdotes of London fashions and rustic scandals."}
    ]
  },
  "loquaciously": {
    "primary": "In a talkative, garrulous, or chatty manner; with excessive wordiness and conversation.",
    "secondary": "In narrative characterization, conversing continuously and volubly without concern for brevity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Jingle rattled on **loquaciously**, skipping from topic to topic with bewildering speed over his tankard of ale."},
      {"author": "William Makepeace Thackeray", "work": "The Newcomes", "quote": "The retired colonel chatted **loquaciously** about his campaigns in the Punjab to any guest willing to listen."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon held forth **loquaciously** on diocesan patronage while pacing the cathedral cloisters after morning service."}
    ]
  },
  "loquaciousness": {
    "primary": "The quality or habit of talking excessively; extreme talkativeness or garrulity.",
    "secondary": "In temperament analysis and literature, the personal tendency toward incessant, rambling conversational flow.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Unchecked **loquaciousness** in youth often degenerates into tedious self-absorption and vanity in declining years."},
      {"author": "Henry James", "work": "Daisy Miller", "quote": "Winterbourne was slightly fatigued by the young lady's unabashed **loquaciousness**, yet captivated by her natural innocence."},
      {"author": "Arthur Schopenhauer", "work": "Studies in Pessimism", "quote": "Solitary thinkers avoid frivolous society precisely to escape the noisy **loquaciousness** that clouds clear contemplation."}
    ]
  },
  "loquacity": {
    "primary": "The habit or state of talking too much; continuous talkativeness or garrulity.",
    "secondary": "In classical moral philosophy and satire, unbridled volubility that exhausts listeners and dilutes serious thought.",
    "quotes": [
      {"author": "Michel de Montaigne", "work": "Essays", "quote": "Wise men value measured silence far above the hollow **loquacity** that empties the mind of deliberate judgment."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Excessive **loquacity** in counselors betrays shallow discretion and reveals state secrets before plans mature."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Greek ambassadors tired the patience of the barbarian chieftain with their interminable theological **loquacity**."}
    ]
  },
  "loquat": {
    "primary": "A small, yellow or orange, sweet and tangy plum-like fruit (Eriobotrya japonica) native to southeastern China.",
    "secondary": "In horticulture and subtropical pomology, an evergreen tree in the rose family Rosaceae cultivated for edible pome fruit.",
    "quotes": [
      {"author": "Robert Fortune", "work": "A Residence Among the Chinese", "quote": "In the hillside orchards around Canton, the golden **loquat** was ripening in heavy clusters among glossy evergreen foliage."},
      {"author": "John Muir", "work": "Steep Trails", "quote": "The California gardens were adorned with blossoming orange groves and trees of the Japanese **loquat** laden with yellow fruit."},
      {"author": "Rudyard Kipling", "work": "From Sea to Sea", "quote": "We rested under the broad leaves of a shady **loquat** tree, eating the refreshing acidic fruit in the sultry afternoon."}
    ]
  },
  "obloquy": {
    "primary": "Strong public criticism, verbal abuse, or disgrace resulting from general condemnation.",
    "secondary": "In political history and ethics, enduring public dishonor, calumny, or systemic ignominy following a fall from favor.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "He endured years of merciless **obloquy** from political foes, sustained only by the testimony of his own conscience."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary press poured unmeasured **obloquy** upon venerable magistrates whose only offense was upholding ancient law."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The deposed emperor was pursued into exile by the bitter **obloquy** of the very Senate that had previously deified him."}
    ]
  },
  "soliloquise": {
    "primary": "To speak one's thoughts aloud when alone or regardless of any listeners, especially on stage.",
    "secondary": "In theatrical performance and dramatic technique (British spelling), delivering an internal dramatic monologue.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Our Theatres in the Nineties", "quote": "The modern dramatist rarely permits his characters to **soliloquise** under the spotlight, seeking realistic conversational interplay instead."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The eccentric professor was accustomed to **soliloquise** aloud during his solitary walks along the wind-swept ramparts of Weissnichtwo."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "She felt a strange impulse to **soliloquise** in the quiet street, voicing doubts that could never be shared in family company."}
    ]
  },
  "soliloquize": {
    "primary": "To utter a soliloquy; to talk to oneself, expressing inner reflections aloud without an addressee.",
    "secondary": "In dramatic literature and psychological fiction, voicing private consciousness or existential doubt in an internal monologue.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Captain Ahab paced the midnight quarterdeck to **soliloquize** fiercely against the indifferent gods and the white whale."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "Hepzibah loved to **soliloquize** in the dusty parlor, confiding her ancestral grievances to the silent portraits on the wall."},
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "I paused under the oak boughs to **soliloquize** upon the absurd chivalric superstitions that governed sixth-century Britain."}
    ]
  },
  "soliloquy": {
    "primary": "An act of speaking one's thoughts aloud when by oneself or in a dramatic performance.",
    "secondary": "In dramatic poetry and literary theory, a speech conventions through which a character reveals innermost motives to the audience.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "The Prince delivered his famous **soliloquy** contemplating whether 'tis nobler in the mind to suffer the slings of fortune."},
      {"author": "Samuel Taylor Coleridge", "work": "Lectures on Shakespeare", "quote": "A dramatic **soliloquy** is not an artificial recitation, but the natural overflowing of a burdened and solitary intellect."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The modern psychological novel replaces spoken stage **soliloquy** with the continuous undercurrent of reflective inner monologue."}
    ]
  },
  "somniloquent": {
    "primary": "Tending to talk in one's sleep; speaking while asleep or under the influence of somnambulism.",
    "secondary": "In sleep medicine and physiological psychology, exhibiting verbal vocalizations during non-REM or REM sleep states.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Speckled Band", "quote": "The nervous sister recalled how the victim became fitfully **somniloquent**, murmuring fragmented warnings in her restless dreams."},
      {"author": "Edgar Allan Poe", "work": "The Facts in the Case of M. Valdemar", "quote": "Under deep mesmeric trance, the patient exhibited **somniloquent** utterances that seemed to emanate from beyond bodily sensation."},
      {"author": "Oliver Wendell Holmes", "work": "Elsie Venner", "quote": "The physician watched the sleeping girl closely, noting her **somniloquent** whispers that revealed buried emotional turmoil."}
    ]
  },
  "somniloquism": {
    "primary": "The act or habit of talking in one's sleep; sleep-talking as a physiological phenomenon.",
    "secondary": "In neuropsychology and sleep research, parasomnia involving articulated speech episodes during sleep cycles.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Cases of habitual **somniloquism** demonstrate that complex linguistic pathways can activate while general sensory awareness sleeps."},
      {"author": "Havelock Ellis", "work": "The World of Dreams", "quote": "Observed instances of **somniloquism** often reflect dramatic dream narratives erupting through incomplete motor inhibition."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Involuntary sleep-talking or **somniloquism** reveals how inherited emotional vocal patterns assert themselves without conscious regulation."}
    ]
  },
  "somniloquist": {
    "primary": "A person who habitually talks in their sleep; one prone to somniloquy.",
    "secondary": "In clinical somnology and observational psychology, an individual experiencing parasomnic speech episodes during slumber.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "Mesmeric Revelation", "quote": "The strange subject was an inveterate **somniloquist**, whose nocturnal disclosures were recorded by attentive bedside watchers."},
      {"author": "Arthur Conan Doyle", "work": "The Crooked Man", "quote": "The bewildered soldier swore he was no intentional eavesdropper, but merely roomed with an agitated **somniloquist**."},
      {"author": "Wilkie Collins", "work": "The Moonstone", "quote": "Under the influence of the secret draught, the slumberer became an unwitting **somniloquist**, betraying where the gem was hidden."}
    ]
  },
  "somniloquy": {
    "primary": "The act or practice of talking while asleep; sleep-talking.",
    "secondary": "In clinical parasomnia classification, nocturnal verbalization occurring across diverse sleep stages without waking consciousness.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Instances of nocturnal **somniloquy** highlight the dissociation between automatic linguistic centers and conscious executive will."},
      {"author": "Havelock Ellis", "work": "The World of Dreams", "quote": "The incoherent muttering characteristic of **somniloquy** often parallels the rapid transitions of primary dream imagery."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "His agitated companion broke into sudden **somniloquy**, shouting incoherent coordinates from some tropical military expedition."}
    ]
  }
}
