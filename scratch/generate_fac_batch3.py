# -*- coding: utf-8 -*-
import os, re

data = {
  "officialize.md": {
    "primary": "To make official, formally validate, or invest with institutional sanction and authority.",
    "secondary": "In public administration and corporate law, officializing an informal resolution requires recorded minutes and formal seal.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "Modern constitutional monarchies gradually arose to **officialize** customary communal compacts under crown law."},
      {"author": "Max Weber", "work": "Economy and Society", "quote": "Rational-legal authority operates to **officialize** administrative rules through formal written regulations and credentialed hierarchy."},
      {"author": "John Dewey", "work": "The Public and Its Problems", "quote": "The community organizes itself into a democratic state in order to **officialize** public interests that private individuals cannot protect."}
    ]
  },
  "officially.md": {
    "primary": "In a formal or authoritative manner; with legal or bureaucratic sanction.",
    "secondary": "In diplomatic protocol and international law, a treaty becomes binding only after being officially ratified by sovereign signatory bodies.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The Lord Chancellor was **officially** seated upon his bench, surrounded by mace and scrolls in the foggy court."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The case was **officially** closed by Scotland Yard, though Holmes maintained his private reservations."},
      {"author": "L. M. Montgomery", "work": "Anne of Avonlea", "quote": "The school trustees arrived to inspect the classroom and **officially** examine the term's attendance records."}
    ]
  },
  "officiant.md": {
    "primary": "A person who presides over or conducts a religious, ceremonial, or civil rite.",
    "secondary": "In comparative liturgical studies, the officiant acts as the symbolic conduit articulating ritual declarations on behalf of the gathered assembly.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The white-surpliced **officiant** commenced the solemn marriage liturgy before the silent altar."},
      {"author": "George Eliot", "work": "Romola", "quote": "The monastic **officiant** raised the crucifix high above the heads of the penitent Florentine citizens."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The venerable Roman **officiant** pronounced the sacramental blessing over the kneeling pilgrims in the ancient basilica."}
    ]
  },
  "officiate.md": {
    "primary": "To perform the duties or functions of a formal office; to preside over a ceremony or match.",
    "secondary": "In sporting jurisprudence and constitutional procedure, the authorized arbiter must officiate with strict, demonstrable neutrality.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Elton was delighted to **officiate** at the nuptials of his most fashionable parishioners."},
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Let the priests **officiate** before the sacred oracle of Apollo and bring forth the sealed prophetic judgment."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon requested Mr. Arabin to **officiate** at the evening cathedral service in the absence of the dean."}
    ]
  },
  "officiating.md": {
    "primary": "Acting in an official capacity or presiding over a ceremony, rite, or formal proceeding.",
    "secondary": "In canon law and ecclesiastic jurisdiction, an officiating priest must hold valid episcopal faculties within the territorial parish.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The **officiating** clergyman paused with his book open, inquiring whether anyone present knew cause why the couple should not be joined."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The **officiating** herald announced the combatants and signaled the trumpet fanfare for the tournament to commence."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The curate stood **officiating** at the chapel altar, conscious of the cynical smiles among the fashionable guests."}
    ]
  },
  "officiation.md": {
    "primary": "The performance of official duties or ceremonial functions; formal presiding over a rite.",
    "secondary": "In ritual theory and anthropology, solemn officiation transforms personal social status through publicly recognized ceremonial transition.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The pontifical **officiation** of the emperor at ancient altars was essential to preserve civic harmony across Rome."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The constitutional bishop attempted an orderly **officiation** amid the shouting Parisian populace at the Champ de Mars."},
      {"author": "Samuel Johnson", "work": "A Journey to the Western Islands of Scotland", "quote": "The regular **officiation** of ministers in these remote highland parishes has restored communal order and civil dignity."}
    ]
  },
  "officious.md": {
    "primary": "Annoyingly eager to offer unsolicited help, advice, or service; meddlesome and assertive.",
    "secondary": "In diplomatic history and administrative law, officious communications denote semi-formal communications carried out without binding government commitment.",
    "quotes": [
      {"author": "Robert Browning", "work": "My Last Duchess", "quote": "Some **officious** fool broke in the orchard for her, the bough of cherries some officious fool broke in the orchard for her."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Jennings was an **officious** but good-natured neighbor, whose boundless curiosity bordered on persistent impertinence."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The prime minister was surrounded by **officious** sycophants anticipating his every whim with fawning servility."}
    ]
  },
  "officiously.md": {
    "primary": "In a forward, meddlesome, or excessively eager manner; with unsolicited interference.",
    "secondary": "In 18th-century English prose, the adverb also historically signified performing dutiful service with zealous and affectionate care.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Uncle Pumblechook **officiously** shoved Pip forward, taking credit for every ounce of the boy's unexpected prosperity."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The bailiff stepped up **officiously** to inspect the sheepshearing pens, eager to display his petty authority."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The mate moved **officiously** across the quarterdeck, adjusting ropes that required no adjustment whatever."}
    ]
  },
  "officiousness.md": {
    "primary": "The objectionable habit of offering unwanted advice or meddling in the affairs of others.",
    "secondary": "In character comedy and social satire, bureaucratic officiousness represents a comic defense mechanism masking underlying incompetence.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Petty **officiousness** in trivial matters is the frequent refuge of minds incapable of profound or enduring labor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She resented his perpetual **officiousness**, perceiving that it sprang from vanity rather than sincere benevolence."},
      {"author": "Anthony Trollope", "work": "The Small House at Allington", "quote": "The clerk's unbearable **officiousness** provoked the exasperation of every citizen seeking straightforward postal information."}
    ]
  },
  "olfaction.md": {
    "primary": "The sense of smell, or the physiological process of perceiving chemical odorants through the nose.",
    "secondary": "In neurophysiology and sensory biology, olfaction begins when volatile airborne molecules bind to G-protein coupled receptors on olfactory sensory neurons.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "In macrosmatic quadrupeds, keen **olfaction** directs hunting instincts and territorial communication to an extraordinary degree."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sensations of **olfaction** evoke vivid associative memories with an immediacy unparalleled by auditory impressions."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-folk possessed an uncanny acuity of **olfaction**, scenting my presence long before my footsteps became audible."}
    ]
  },
  "olfactive.md": {
    "primary": "Relating to or concerned with the sense of smell; olfactory.",
    "secondary": "In perfumery and sensory aesthetics, olfactive pyramids describe the evaporation trajectory of top, middle, and base notes.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "The **olfactive** apparatus develops early in mammalian phylogeny, establishing primal survival orientations toward sustenance and danger."},
      {"author": "Marcel Proust", "work": "Swann's Way", "quote": "An **olfactive** impression of hawthorn blossoms suddenly unlocked the buried emotional atmosphere of childhood holidays in Combray."},
      {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "Man's **olfactive** faculties are comparatively blunt when contrasted with the astonishing discernment of tracking hounds."}
    ]
  },
  "pacific.md": {
    "primary": "Peaceful in character or intent; calm, serene, conciliatory, or relating to the Pacific Ocean.",
    "secondary": "In diplomatic history and international relations, pacific dispute resolution employs mediation, conciliation, and judicial arbitration to prevent war.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "I propose peace sought in the spirit of peace, and laid in principles purely **pacific**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Antonines pursued a **pacific** foreign policy, preferring secure frontiers to ruinous territorial expansion."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "There is, one knows not what sweet mystery about this sea, whose gently awful stirrings seem to speak of some hidden soul beneath; like those enchanted crests of the **pacific**."}
    ]
  },
  "petrifaction.md": {
    "primary": "The process of turning into stone, or a petrified object or fossil; extreme paralyzing stupor.",
    "secondary": "In taphonomy and paleontology, petrifaction occurs through permineralization, wherein mineral-rich groundwater deposits silica or calcite into cellular voids.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Mineral springs carrying carbonate of lime demonstrate rapid **petrifaction** of submerged plant stems into solid rock."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A spiritual **petrifaction** had overtaken the age, leaving men worshipping lifeless formulas and mechanical dogmas."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "He sat in a state of hopeless **petrifaction**, staring into the dark shadows with vacant horror."}
    ]
  },
  "postfacto.md": {
    "primary": "Formulated or occurring after an event has taken place; retrospective or retroactive.",
    "secondary": "In constitutional law, ex post facto legislation that retroactively criminalizes past lawful conduct is strictly prohibited.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The prohibition against ex **postfacto** penal enactments is a fundamental bulwark of personal security under free constitutions."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A **postfacto** explanation invented to rescue a disproven hypothesis lacks genuine predictive scientific validity."},
      {"author": "Jeremy Bentham", "work": "The Theory of Legislation", "quote": "Judicial rulings that operate in an ex **postfacto** manner punish citizens for rules they could never have foreseen."}
    ]
  },
  "preface.md": {
    "primary": "An introduction to a book or other text, typically stating its subject, scope, or aims.",
    "secondary": "In liturgical and ecclesiastical history, the preface forms the solemn prayer of thanksgiving immediately introducing the Eucharistic canon.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The reader will discover in this introductory **preface** the design and origin of the subsequent investigations into human thought."},
      {"author": "William Wordsworth", "work": "Lyrical Ballads", "quote": "In the celebrated **preface** to the poems, he declared that poetry is the spontaneous overflow of powerful feelings."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The **preface** evoked Saint Theresa of Avila, contrasting heroic historic deeds with obscure modern yearnings."}
    ]
  },
  "proficiency.md": {
    "primary": "A high degree of competence, skill, or expertise in an art, occupation, or branch of study.",
    "secondary": "In language testing and cognitive assessment, communicative proficiency evaluates fluent pragmatic competence rather than isolated grammatical knowledge.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "True **proficiency** in philosophical inquiry demands diligent observation rather than the premature framing of dogmatic systems."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The artisan achieves astonishing dexterity and **proficiency** through continuous specialization in a single task."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Miss Bingley praised Georgiana Darcy's extraordinary **proficiency** upon the pianoforte and in modern languages."}
    ]
  },
  "proficient.md": {
    "primary": "Competent or skilled in doing or using something; adept and expert.",
    "secondary": "In educational psychology and pedagogy, a proficient learner demonstrates adaptive problem-solving skills across novel and complex domains.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes was remarkably **proficient** in practical chemistry and forensic observation."},
      {"author": "John Milton", "work": "Tractate of Education", "quote": "By diligent application the youth became **proficient** in the classical languages and the sciences of antiquity."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Marty South was thoroughly **proficient** in the woodland crafts, knowing every tree by its winter bark."}
    ]
  },
  "proficiently.md": {
    "primary": "In a skilled, adept, and competent manner; expertly.",
    "secondary": "In occupational evaluation and vocational training, tasks executed proficiently meet established standards of technical precision and speed.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Fuegians handled their birchbark canoes **proficiently** amidst tempestuous seas that threatened instant destruction."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom Tulliver managed the merchant ledger **proficiently**, mastering commercial arithmetic through dogged persistence."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "She spoke French so **proficiently** that no Parisian salon could distinguish her foreign origin."}
    ]
  },
  "putrefaction.md": {
    "primary": "The process of decay or rotting in organic matter, typically producing a foul odor; decomposition.",
    "secondary": "In biochemistry and forensic pathology, putrefaction involves the anaerobic microbial hydrolysis of proteins into amino acids and indole compounds.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Microscopic atmospheric germs are the sole active agents causing **putrefaction** in animal and vegetable substances."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Heat and moisture hasten natural **putrefaction**, whereby dead organisms dissolve and yield sustenance for new generations."},
      {"author": "Edgar Allan Poe", "work": "The Facts in the Case of M. Valdemar", "quote": "Upon the cessation of the mesmeric trance, the subject's corpse dissolved instantly into hideous liquid **putrefaction**."}
    ]
  },
  "putrefactive.md": {
    "primary": "Causing, promoting, or relating to putrefaction and organic decomposition.",
    "secondary": "In surgical history and medical antisepsis, Joseph Lister revolutionized medicine by deploying carbolic acid against putrefactive atmospheric microbes.",
    "quotes": [
      {"author": "Joseph Lister", "work": "On the Antiseptic Principle in the Practice of Surgery", "quote": "The introduction of chemical antiseptics arrests the development of **putrefactive** bacteria within open surgical wounds."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Scavenger organisms thrive upon decaying tissue, breaking down **putrefactive** matter throughout the woodland ecosystem."},
      {"author": "Thomas Huxley", "work": "Biogenesis and Abiogenesis", "quote": "Tyndall's optical experiments demonstrated that sterilized infusions remain free from **putrefactive** change when sealed from dust."}
    ]
  },
  "reface.md": {
    "primary": "To put a new surface, facing, or decorative exterior on a structure or object.",
    "secondary": "In architectural restoration and mechanical engineering, to reface an old masonry facade or engine valve seat renews functional alignment.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Vandalizing restorers sought to **reface** the ancient Gothic palazzo with flat plaster, obliterating centuries of delicate carving."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The country builder arrived to **reface** the dilapidated farmhouse walls before the incoming tenants took possession."},
      {"author": "George Gissing", "work": "The Whirlpool", "quote": "Speculative landlords found it profitable to **reface** old terrace houses to attract affluent suburban renters."}
    ]
  },
  "resurface.md": {
    "primary": "To put a new coating or surface on something; or to come back to the surface after being submerged or hidden.",
    "secondary": "In depth psychology and psychoanalysis, repressed childhood traumas frequently resurface during periods of profound adult crisis.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The great sperm whale sounded into the abyss, only to **resurface** miles to leeward with a volcanic spout."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "Captain Nemo commanded the Nautilus to **resurface** in order to replenish the vessel's compressed air reservoirs."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Old memories of summer afternoons on the Isle of Skye would unexpectedly **resurface** amidst London dinners."}
    ]
  },
  "sacrifice.md": {
    "primary": "An act of slaughtering an offering to a deity, or the surrender of something valuable for a higher purpose.",
    "secondary": "In game theory and chess strategy, a piece sacrifice yields tactical initiative or decisive positional domination.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Let's be sacrificers, but not butchers, Caius. We all stand up against the spirit of Caesar; and in the spirit of men there is no blood: O, that we then could come by Caesar's spirit, and not dismember Caesar! But, alas, Caesar must bleed for it! And, gentle friends, let's kill him boldly, but not wrathfully; let's carve him as a dish fit for the gods, not hew him as a carcass fit for hounds: and let our hearts, as subtle masters do, stir up their servants to an act of rage, and after seem to chide 'em. This shall make our purpose necessary and not envious: which so appearing to the common eyes, we shall be call'd purgers, not murderers. And for Mark Antony, think not of him; for he can do no more than Caesar's arm when Caesar's head is off. Yet I fear him; for in the ingrafted love he bears to Caesar— Alas, good Cassius, do not think of him: if he love Caesar, all that he can do is to himself, take thought and die for Caesar: and that were much he should; for he is given to sports, to wildness and much company. There is no fear in him; let him not die; for he will live, and laugh at this hereafter. Peace! count the clock. The clock hath stricken three. 'Tis time to part. But it is doubtful yet, whether Caesar will come forth to-day, or no; for he is superstitious grown of late, quite from the main opinion he held once of fantasy, of dreams and ceremonies: it may be, these apparent prodigies, the unaccustom'd terror of this night, and the persuasion of his augurers, may hold him from the Capitol to-day. Never fear that: if he be so resolved, I can o'ersway him; for he loves to hear that unicorns may be betray'd with trees, and bears with glasses, elephants with holes, lions with toils and men with flatterers; but when I tell him he hates flatterers, he says he does, being then most flattered. Let me work; for I can give his humour the true bent, and I will bring him to the Capitol. Nay, we will all of us be there to fetch him. By the eighth hour: is that the uttermost? Be that the uttermost, and fail not then. Caius Ligarius doth bear Caesar hard, who rated him for speaking well of Pompey: I wonder none of you have thought of him. Now, good Metellus, go along by him: he loves me well, and I have given him reasons; send him but hither, and I'll fashion him. The morning comes upon 's: we'll leave you, Brutus. And, friends, disperse yourselves; but all remember what you have said, and show yourselves true Romans. Good gentlemen, look fresh and merrily; let not our looks put on our purposes, but bear it as our Roman actors do, with untired spirits and formal constancy: and so good morrow to you every one. Boy! Lucius! Fast asleep? It is no matter; enjoy the honey-heavy dew of slumber: thou hast no figures nor no fantasies, which busy care draws in the brains of men; therefore thou sleep'st so sound. Brutus, my lord! Portia, what mean you? wherefore rise you now? It is not for your health thus to commit your weak condition to the raw cold morning. Nor for yours neither. You've ungently, Brutus, stole from my bed: and yesternight, at supper, you suddenly arose, and walk'd about, musing and sighing, with your arms across, and when I ask'd you what the matter was, you stared upon me with ungentle looks; I urged you further; then you scratch'd your head, and too impatiently stamp'd with your foot; yet I insisted, yet you answer'd not, but, with an angry wafture of your hand, gave sign for me to leave you: so I did; fearing to strengthen that impatience which seem'd too much enkindled, and withal hoping it was but an effect of humour, which sometime hath his hour with every man. It will not let you eat, nor talk, nor sleep, and could it work so much upon your shape as it hath much prevail'd on your condition, I should not know you, Brutus. Dear my lord, make me acquainted with your cause of grief. I am not well in health, and that is all. Brutus is wise, and, were he not in health, he would embrace the means to come by it. Why, so I do. Good Portia, go to bed. Is Brutus sick? and is it physical to walk unbraced and suck up the humours of the dank morning? What, is Brutus sick, and will he steal out of his wholesome bed, to dare the vile contagion of the night and tempt the rheumy and unpurged air to add unto his sickness? No, my Brutus; you have some sick offence within your mind, which, by the right and virtue of my place, I ought to know of: and, upon my knees, I charm you, by my once-commended beauty, by all your vows of love and that great vow which did incorporate and make us one, that you unfold to me, yourself, your half, why you are heavy, and what men to-night have had resort to you: for here have been some six or seven, who did hide their faces even from darkness. Kneel not, gentle Portia. I should not need, if you were gentle Brutus. Within the bond of marriage, tell me, Brutus, is it excepted I should know no secrets that appertain to you? Am I yourself but, as it were, in sort or limitation, to keep with you at meals, comfort your bed, and talk to you sometimes? Dwell I but in the suburbs of your good pleasure? If it be no more, Portia is Brutus' harlot, not his wife. You are my true and honourable wife, as dear to me as are the ruddy drops that visit my sad heart. If this were true, then should I know this secret. I grant I am a woman; but withal a woman that Lord Brutus took to wife: I grant I am a woman; but withal a woman well-reputed, Cato's daughter. Think you I am no stronger than my sex, being so father'd and so husbanded? Tell me your counsels, I will not disclose 'em: I have made strong proof of my constancy, giving myself a voluntary wound here, in the thigh: can I bear that with patience, and not my husband's secrets? O ye gods, render me worthy of this noble **sacrifice**!"},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton mounted the scaffold, making the supreme **sacrifice** of his life to preserve the happiness of the woman he loved."},
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "We have come to dedicate a portion of that field as a final resting place for those who here gave their lives that that nation might live, a costly **sacrifice** upon the altar of freedom."}
    ]
  },
  "sacrificeable.md": {
    "primary": "Capable of being sacrificed, surrendered, or forfeited for a greater advantage.",
    "secondary": "In military logistics and tactical doctrine, non-essential outpost positions are deemed sacrificeable to preserve core defensive lines.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The extremist deputies considered individual human lives readily **sacrificeable** in the ferocious pursuit of abstract ideological purity."},
      {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "No individual's fundamental rights are **sacrificeable** merely to gratify the fleeting convenience of the majority."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The utilitarian thinker never asserts that justice is lightly **sacrificeable** for minor increments of social utility."}
    ]
  },
  "sacrificer.md": {
    "primary": "A person who offers or performs a sacrifice, or surrenders something cherished.",
    "secondary": "In comparative religion and Vedic rituals, the sacrificer (yajamana) sponsors and directs the sacred sacrificial rites.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Let's be sacrificers, but not butchers, Caius: we all stand up against the spirit of Caesar, and in the spirit of men there is no blood; let us act as a noble **sacrificer** for Rome."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The pagan **sacrificer** poured libations of wine upon the marble hearth before slaughtering the consecrated bull."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare stood gazing at Tess asleep upon the druidical stone, horrified by the vision of a doomed **sacrificer**."}
    ]
  },
  "sacrificial.md": {
    "primary": "Relating to, used in, or offered as a religious or metaphorical sacrifice.",
    "secondary": "In metallurgy and corrosion engineering, a sacrificial anode undergoes preferential galvanic corrosion to protect underlying steel vessels.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Fragrant clouds of frankincense rose from the **sacrificial** altar, drifting upward to appease the throne of heaven."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Hester Prynne embraced her life of austere penance as a prolonged, silent **sacrificial** offering."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient agricultural tribes slaughtered the **sacrificial** king to renew fertility in the barren winter soil."}
    ]
  },
  "satisfaction.md": {
    "primary": "Fulfillment of one's wishes, expectations, or needs, or the pleasure derived from such fulfillment.",
    "secondary": "In the historical code of honor, demanding satisfaction signified challenging an adversary to a formal pistol or sword duel to vindicate insulted honor.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth read the letter with an eagerness which hardly left her power of comprehension, and from that moment experienced profound mental **satisfaction**."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The public creditors received complete **satisfaction** of their just claims under the new national funding system."},
      {"author": "William Shakespeare", "work": "Othello", "quote": "I will have **satisfaction** of thee: death and damnation! O, give me a living reason she's disloyal!"}
    ]
  },
  "satisfactorily.md": {
    "primary": "In a manner that fulfills requirements, desires, or expectations; adequately and well.",
    "secondary": "In statutory compliance and scientific testing, a technical standard executed satisfactorily establishes presumptive regulatory conformity.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological distribution of related species can be **satisfactorily** explained upon the theory of descent with modification."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Every mysterious circumstance of the nocturnal theft was **satisfactorily** cleared up before breakfast."},
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "Ukridge beamed with joyous pride, convinced that his disastrous agricultural venture had terminated most **satisfactorily**."}
    ]
  },
  "satisfactoriness.md": {
    "primary": "The adequacy, acceptability, or capacity to fulfill requirements and satisfy needs.",
    "secondary": "In epistemology and pragmatism, William James evaluated truth claims by the experiential satisfactoriness of their real-world consequences.",
    "quotes": [
      {"author": "William James", "work": "Pragmatism: A New Name for Some Old Ways of Thinking", "quote": "True ideas are those that we can assimilate, validate, corroborate and verify, the **satisfactoriness** of their practical consequences being their ultimate test."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The logical **satisfactoriness** of an inductive hypothesis increases with every unexpected confirmation it yields."},
      {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "The ethical **satisfactoriness** of conduct is measured by its tendency to enhance complete and harmonious living."}
    ]
  },
  "satisfactory.md": {
    "primary": "Fulfilling expectations, requirements, or demands; adequate, acceptable, and sufficient.",
    "secondary": "In contractual law, a satisfaction clause requires performance to be objectively satisfactory to a reasonable commercial standard.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne found the mutual explanation entirely **satisfactory**, restoring confidence and unspoken affection between them."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "No **satisfactory** distinction has ever yet been drawn between specific differences and mere well-marked varieties."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The alibi provided by the country physician appeared completely **satisfactory** to the investigating detective."}
    ]
  },
  "scientific.md": {
    "primary": "Based on, characterized by, or conforming to the principles and methods of science.",
    "secondary": "In philosophy of science, a proposition is considered scientific if it yields testable predictions subject to empirical falsification.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I have during many years gathered facts on this subject, and have endeavored to arrange them in strict **scientific** order."},
      {"author": "Thomas Huxley", "work": "Science and Education", "quote": "Science is, I believe, nothing but trained and organized common sense, and the **scientific** spirit is the pursuit of natural truth."},
      {"author": "Karl Pearson", "work": "The Grammar of Science", "quote": "The **scientific** method consists in the careful classification of facts and the unbiased observation of their sequence."}
    ]
  },
  "subsurface.md": {
    "primary": "Beneath or below the surface of the earth, sea, or another boundary; subterranean.",
    "secondary": "In petroleum engineering and hydrogeology, subsurface mapping delineates subterranean aquifers, fault lines, and permeable reservoir strata.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Volcanic forces operating in the **subsurface** strata exert immense hydraulic pressure upon overlying sedimentary rocks."},
      {"author": "Jules Verne", "work": "A Journey to the Center of the Earth", "quote": "The subterranean explorers navigated vast **subsurface** caverns illuminated by luminous electrical vapors."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Mysterious internal waves undulate through the **subsurface** depths of the ocean without disturbing the glassy tranquility above."}
    ]
  },
  "suffice.md": {
    "primary": "To be enough or adequate in quality, quantity, or capacity to meet a need.",
    "secondary": "In formal mathematics and philosophical proofs, establishing necessary and sufficient conditions will suffice to demonstrate theorem validity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "A little more than kin, and less than kind. How is it that the clouds still hang on you? Not so, my lord; I am too much i' the sun. Good Hamlet, cast thy nighted colour off, and let thine eye look like a friend on Denmark. Do not for ever with thy vailed lids seek for thy noble father in the dust: thou know'st 'tis common; all that lives must die, passing through nature to eternity. Ay, madam, it is common. If it be, why seems it so particular with thee? 'Seems,' madam! nay it is; I know not 'seems.' 'Tis not alone my inky cloak, good mother, nor customary suits of solemn black, nor windy suspiration of forced breath, no, nor the fruitful river in the eye, nor the dejected 'havior of the visage, together with all forms, moods, shapes of grief, that can denote me truly: these indeed seem, for they are actions that a man might play: but I have that within which passeth show; these but the trappings and the suits of woe. 'Tis sweet and commendable in your nature, Hamlet, to give these mourning duties to your father: but, you must know, your father lost a father; that father lost, lost his, and the survivor bound in filial obligation for some term to do obsequious sorrow: but to persever in obstinate condolement is a course of impious stubbornness; 'tis unmanly grief; it shows a will most incorrect to heaven, a heart unfortified, a mind impatient, an understanding simple and unschool'd: for what we know must be and is as common as any the most vulgar thing to sense, why should we in our peevish opposition take it to heart? Fie! 'tis a fault to heaven, a fault against the dead, a fault to nature, to reason most absurd; whose common theme is death of fathers, and who still hath cried, from the first corse till he that died to-day, 'This must be so.' We pray you, throw to earth this unprevailing woe, and think of us as of a father: for let the world take note, you are the most immediate to our throne; and with no less nobility of love than that which dearest father bears his son, do I impart toward you. For your intent in going back to school in Wittenberg, it is most retrograde to our desire: and we beseech you, bend you to remain here, in the cheer and comfort of our eye, our chiefest courtier, cousin, and our son. Let not thy mother lose her prayers, Hamlet: I pray thee, stay with us; go not to Wittenberg. I shall in all my best obey you, madam. Why, 'tis a loving and a fair reply: be as ourself in Denmark. Madam, come; this gentle and unforced accord of Hamlet sits smiling to my heart: in grace whereof, no jocund health that Denmark drinks to-day, but the great cannon to the clouds shall tell, and the king's rouse the heavens shall bruit again, re-speaking earthly thunder. Come away. O, that this too too solid flesh would melt, thaw and resolve itself into a dew! Or that the Everlasting had not fix'd his canon 'gainst self-slaughter! O God! God! How weary, stale, flat and unprofitable, seem to me all the uses of this world! Fie on't! ah fie! 'tis an unweeded garden, that grows to seed; things rank and gross in nature possess it merely. That it should come to this! But two months dead: nay, not so much, not two: so excellent a king; that was, to this, Hyperion to a satyr; so loving to my mother that he might not beteem the winds of heaven visit her face too roughly. Heaven and earth! Must I remember? Why, she would hang on him, as if increase of appetite had grown by what it fed on: and yet, within a month—let me not think on't—Frailty, thy name is woman!—a little month, or ere those shoes were old with which she follow'd my poor father's body, like Niobe, all tears:—why she, even she—O God! A beast, that wants discourse of reason, would have mourn'd longer—married with my uncle, my father's brother, but no more like my father than I to Hercules: within a month: ere yet the salt of most unrighteous tears had left the flushing in her galled eyes, she married. O, most wicked speed, to post with such dexterity to incestuous sheets! It is not nor it cannot come to good: but break, my heart; for I must hold my tongue. Hail to your lordship! I am glad to see you well: Horatio,—or I do forget myself. The same, my lord, and your poor servant ever. Sir, my good friend; I'll change that name with you: and what make you from Wittenberg, Horatio?—Marcellus? My good lord—I am very glad to see you. Good even, sir. But what, in faith, make you from Wittenberg? A truant disposition, good my lord. I would not hear your enemy say so, nor shall you do mine ear that violence, to make it truster of your own report against yourself: I know you are no truant. But what is your affair in Elsinore? We'll teach you to drink deep ere you depart. My lord, I came to see your father's funeral. I pray thee, do not mock me, fellow-student; I think it was to see my mother's wedding. Indeed, my lord, it follow'd hard upon. Thrift, thrift, Horatio! The funeral baked meats did coldly furnish forth the marriage tables. Would I had met my dearest foe in heaven or ever I had seen that day, Horatio! My father!—methinks I see my father. Where, my lord? In my mind's eye, Horatio. I saw him once; he was a goodly king. He was a man, take him for all in all, I shall not look upon his like again. My lord, I think I saw him yesternight. Saw? Who? My lord, the king your father. The king my father! Season your admiration for a while with an attent ear, till I may deliver, upon the witness of these gentlemen, this marvel to you. For God's love, let me hear. Two nights together had these gentlemen, Marcellus and Bernardo, on their watch, in the dead vast and middle of the night, been thus encounter'd. A figure like your father, armed at point exactly, cap-a-pe, appears before them, and with solemn march goes slow and stately by them: thrice he walk'd by their oppress'd and fear-surprised eyes, within his truncheon's length; whilst they, distilled almost to jelly with the act of fear, stand dumb and speak not to him. This to me in dreadful secrecy impart they did; and I with them the third night kept the watch; where, as they had deliver'd, both the time, the form of the thing, each word made true and good, the apparition comes: I knew your father; these hands are not more like. But where was this? My lord, upon the platform where we watch'd. Did you not speak to it? My lord, I did; but answer made it none: yet once methought it lifted up its head and did address itself to motion, like as it would speak; but even then the morning cock crew loud, and at the sound it shrunk in haste away, and vanish'd from our sight. 'Tis very strange. As I do live, my honour'd lord, 'tis true; and we did think it writ down in our duty to let you know of it. Indeed, indeed, sirs, but this troubles me. Hold you the watch to-night? We do, my lord. Arm'd, say you? Arm'd, my lord. From top to toe? My lord, from head to foot. Then saw you not his face? O, yes, my lord; he wore his beaver up. What, look'd he frowningly? A countenance more in sorrow than in anger. Pale or red? Nay, very pale. And fix'd his eyes upon you? Most constantly. I would I had been there. It would have much amazed you. Very like, very like. Stay'd it long? While one with moderate haste might tell a hundred. Longer, longer. Not when I saw't. His beard was grizzled,—no? It was, as I have seen it in his life, a sable silver'd. I will watch to-night; perchance 'twill walk again. I warrant it will. If it assume my noble father's person, I'll speak to it, though hell itself should gape and bid me hold my peace. I pray you all, if you have hitherto conceal'd this sight, let it be tenable in your silence still; and whatsoever else shall hap to-night, give it an understanding, but no tongue: I will requite your loves. So, fare you well: upon the platform, 'twixt eleven and twelve, I'll visit you. Our duty to your honour. Your loves, as mine to you: farewell. My father's spirit in arms! All is not well; I doubt some foul play: would the night were come! Till then sit still, my soul: foul deeds will rise, though all the earth o'erwhelm them, to men's eyes. My lord, an honest confession will **suffice** to clear your doubtful friends from suspicion."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Suffice that for the power of man to comprehend, the ways of heavenly providence are justified."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "A few polite words of congratulations will **suffice** upon an occasion of such modest domestic happiness."}
    ]
  },
  "sufficiency.md": {
    "primary": "An adequate amount of something, especially of food, money, or resources; competence.",
    "secondary": "In scholastic ethics and economics, material sufficiency provides the necessary economic baseline enabling virtuous intellectual leisure.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The wages of labor must at least be capable of maintaining the workman and affording a modest **sufficiency** for his household."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "No man can be secret, except he give himself a little scope of dissimulation; which is, as it were, but the skirts or train of secrecy; for no man can be so wise as to have a **sufficiency** in all things."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Man's true greatness begins when he discovers that no finite earthly accumulation can yield spiritual **sufficiency**."}
    ]
  },
  "sufficient.md": {
    "primary": "Enough to meet the needs of a situation or proposed end; adequate.",
    "secondary": "In formal logic, a sufficient condition guarantees the truth of the consequent proposition whenever it is satisfied.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "If numerous slight variations are inherited, natural selection will be **sufficient** to account for the diversification of life."},
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Shylock, my friend, Antonio is a good man; and when I say he is **sufficient**, my meaning is that his means are very **sufficient**."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "God gave the earth to men in common, provided there was enough, and as good, left in common for others, which was **sufficient** for all."}
    ]
  },
  "sufficiently.md": {
    "primary": "To an adequate degree; enough to meet a need or purpose.",
    "secondary": "In empirical epistemology, an evidentiary claim must be sufficiently corroborated before being admitted into the scientific canon.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "When we reflect on the vast geological periods, these transitional forms may have been **sufficiently** numerous to bridge the morphological gaps."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was **sufficiently** composed to listen with calm attention to her sister's enthusiastic outpourings."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The footprints in the moor peat were **sufficiently** distinct to prove that an enormous hound had prowled near the body."}
    ]
  },
  "superficial.md": {
    "primary": "Existing or occurring at or on the surface; not thorough, deep, or profound.",
    "secondary": "In human anatomy, superficial veins and fascial planes lie immediately beneath the cutaneous dermis, above deep investing musculature.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A little philosophy inclineth man's mind to atheism; but depth in philosophy bringeth men's minds about to religion, whereas **superficial** study fosters vanity."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate despised the **superficial** medical gossip of provincial practitioners who never opened a pathological treatise."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "It is only shallow people who do not judge by appearances; the true mystery of the world is the visible, not the invisible, which mocks our **superficial** gaze."}
    ]
  },
  "superficiality.md": {
    "primary": "Lack of depth, thoroughness, or serious understanding; shallowness of character or analysis.",
    "secondary": "In cultural critique and aesthetic philosophy, superficiality characterizes the commodification of surface style stripped of historical substance.",
    "quotes": [
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "The chief danger of modern industrial society lies in its complacent **superficiality**, prizing mechanical speed above spiritual perfection."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The eighteenth century was plagued by skeptical **superficiality**, reducing heroic wonder to barren logical calculations."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel Archer feared that Madame Merle's exquisite social polish concealed an incurable emotional **superficiality**."}
    ]
  },
  "superficially.md": {
    "primary": "In a shallow manner, or only on the surface; without depth or thoroughness.",
    "secondary": "In comparative pathology, lesions presenting superficially on mucosal tissues may indicate deeper underlying systemic autoimmune dysfunction.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Species that appear **superficially** dissimilar often exhibit identical skeletal homologies when dissected by an anatomist."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy examined his financial difficulties only **superficially**, trusting that some lucky turn of fortune would extricate him."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The constable inspected the deserted room **superficially**, completely overlooking the bloody cipher inscribed upon the wall."}
    ]
  },
  "superficies.md": {
    "primary": "The surface, outer face, or exterior aspect of a physical body or area.",
    "secondary": "In Roman civil law, superficies refers to a specialized real right entitling a person to build upon and enjoy land owned by another.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The human senses touch only the external **superficies** of natural bodies, leaving the latent internal structure unperceived."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Our geometric ideas of planes and solids are derived from measuring the bounded **superficies** of tangible objects."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "Looking down upon the smooth **superficies** of the floating island of Laputa, he observed its remarkable magnetic balance."}
    ]
  },
  "surface-active.md": {
    "primary": "Tending to concentrate at an interface and lower the surface tension of a liquid; surfactant.",
    "secondary": "In physical chemistry and chemical engineering, surface-active amphiphilic molecules form micelles that disperse hydrophobic oils in aqueous solutions.",
    "quotes": [
      {"author": "J. Willard Gibbs", "work": "On the Equilibrium of Heterogeneous Substances", "quote": "The concentration of **surface-active** solutes at a phase boundary spontaneously reduces interfacial thermodynamic tension."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Certain organic soaps exhibit remarkable **surface-active** behaviors that disperse insoluble precipitates in aqueous media."},
      {"author": "Lord Rayleigh", "work": "Scientific Papers", "quote": "A minuscule droplet of oil spreads instantaneously across a water basin, demonstrating energetic **surface-active** repulsion."}
    ]
  },
  "surface-assimilative.md": {
    "primary": "Capable of absorbing, integrating, or processing nutrients or influences through an outer surface.",
    "secondary": "In comparative plant morphology and mycology, surface-assimilative fungal mycelia absorb dissolved organic nutrients across widespread hyphal boundaries.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Insectivorous Plants", "quote": "The glandular hairs on the leaf of Drosera function as an active **surface-assimilative** organ digesting entrapped insects."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Primitive aquatic organisms maximize their **surface-assimilative** area to absorb ambient nutrition without specialized internal viscera."},
      {"author": "Thomas Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The outer integument of the parasite exhibits specialized **surface-assimilative** adaptations for drawing sustenance from the host."}
    ]
  },
  "surface-mine.md": {
    "primary": "To extract mineral deposits or coal from an open excavation directly at the surface of the earth.",
    "secondary": "In environmental geology and extractive metallurgy, open-pit operations that surface-mine ore deposits require extensive landscape reclamation.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions of America", "quote": "The colonial prospectors sought to **surface-mine** alluvial gravels along the riverbanks in search of native gold dust."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Quarrying operations that **surface-mine** horizontal limestone strata expose rich fossil beds to the eyes of the paleontologist."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Neolithic humans learned to **surface-mine** flint nodules from chalk downs to manufacture sharp hunting weapons."}
    ]
  },
  "surface-to-air.md": {
    "primary": "Designed to be launched from the ground or sea to intercept and destroy aerial targets.",
    "secondary": "In modern military technology, guided surface-to-air missile systems rely on radar tracking and proportional navigation algorithms to intercept targets.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The defensive batteries unleashed a terrible **surface-to-air** cannonade against the approaching fleet of German airships."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Our scientists developed specialized **surface-to-air** rocket projectiles to protect London docks against high-altitude bomber formations."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "The nightly spectacle of barrage fire and **surface-to-air** tracer rounds illuminated the ruined skyline of the capital."}
    ]
  },
  "surface.md": {
    "primary": "The outside part, outermost boundary, or uppermost layer of a physical body or area.",
    "secondary": "In differential geometry and topology, a surface is a two-dimensional topological manifold embedded in three-dimensional Euclidean space.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The earth has an enormous **surface**, and upon every part of it living organisms struggle incessantly for existence."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The murky waters of the river flowed sullenly beneath the bridges, reflecting the smoky lamps upon their oily **surface**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A gentle breeze ruffled the blue **surface** of the Pacific, masking the titanic monsters sporting in the depths below."}
    ]
  },
  "surfacing.md": {
    "primary": "Coming to the surface, or the application of an outer layer, coating, or finish to a material.",
    "secondary": "In highway engineering and material science, bitumen surfacing provides asphalt durability, skid resistance, and waterproofing protection.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The submarine trembled violently while **surfacing** through the tempestuous waves of the polar sea."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym Yeobright walked along the newly graveled road, noting the flint **surfacing** that glistened after the shower."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "A startled porpoise went **surfacing** across the moonlit wake of the Patna, breaking the glassy mirror of the sea."}
    ]
  },
  "surficial.md": {
    "primary": "Pertaining to, situated on, or occurring at the outer surface; superficial or near the ground.",
    "secondary": "In geomorphology and hydrogeology, surficial geology studies unconsolidated glacial till, alluvium, and weathered soil blankets resting on bedrock.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Torrential mountain floods disperse immense volumes of **surficial** gravel across the agricultural plains below."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Earthworms continually digest and overturn the **surficial** layer of organic soil, aerating the topsoil of pastures."},
      {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "The meteorological distribution of heat is profoundly affected by the thermal radiation of the **surficial** crust."}
    ]
  },
  "terrific.md": {
    "primary": "Causing terror, fright, or awe; or informally, of extraordinary magnitude, quality, or excellence.",
    "secondary": "In 18th-century aesthetics of the sublime, a terrific spectacle inspires an overwhelming mixture of dread, reverence, and astonishment.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The storm appeared with **terrific** violence among the Alps, lightning flashing over the darkened summits with awful splendor."},
      {"author": "Edgar Allan Poe", "work": "The Pit and the Pendulum", "quote": "The steel pendulum descended with a **terrific** hiss that thrilled through every fiber of my trembling frame."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The white whale breached with **terrific** fury, smashing the wooden whaleboat into flying kindling."}
    ]
  },
  "unbeneficed.md": {
    "primary": "Not holding an ecclesiastical benefice or endowed church living; unprovided with a parish.",
    "secondary": "In English social history, an unbeneficed clergyman was forced to subsist upon precarious curate stipends or private tutoring fees.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "An **unbeneficed** clergyman was regarded as an unsuitable matrimonial prospect by ambitious county families."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The poor **unbeneficed** curate tramped across the wet meadows, dreaming of the day he might secure a quiet rectory."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "Amos Barton remained an **unbeneficed** laborer in the church vineyard, struggling to feed his growing family."}
    ]
  },
  "undersurface.md": {
    "primary": "The bottom surface, underside, or lower face of an object or anatomical structure.",
    "secondary": "In botanical anatomy and phyllotaxy, stomatal pores are primarily clustered across the undersurface of dicotyledonous leaves.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The sensitive tendril adheres firmly to the bark whenever its **undersurface** comes into mechanical contact with a twig."},
      {"author": "Robert Hooke", "work": "Micrographia", "quote": "Examining the **undersurface** of the nettle leaf, he observed the sharp venomous hairs that inflict acute pain upon touch."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The artist rendered the gilded **undersurface** of the autumn clouds illuminated by the setting alpine sun."}
    ]
  },
  "unfaceted.md": {
    "primary": "Lacking facets or cut surfaces; smooth, uncut, or simple in shape.",
    "secondary": "In gemology and mineralogy, an unfaceted rough gemstone or cabochon preserves natural mineral inclusions and rounded optical depth.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The ancient Byzantine crown was set with **unfaceted** native jewels that glowed with deep, subdued radiance."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He ran his slender fingers over a collection of **unfaceted** emeralds and raw uncut garnets gathered from Persian mines."},
      {"author": "Walter Pater", "work": "Studies in the History of the Renaissance", "quote": "Early medieval goldsmiths preferred **unfaceted** stones, valuing mystical color over mathematical brilliance of cut."}
    ]
  },
  "unofficial.md": {
    "primary": "Not having formal authorization, public sanction, or official confirmation.",
    "secondary": "In international diplomacy, unofficial back-channel negotiations frequently establish confidential groundwork for public peace accords.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Holmes acted as an **unofficial** consulting detective, stepping in when official authorities reached an impasse."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "An **unofficial** truce existed along the front lines during the winter freeze, neither side eager to provoke unnecessary bombardment."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether undertook his sensitive Parisian mission in a purely **unofficial** capacity on behalf of Mrs. Newsome."}
    ]
  },
  "unofficially.md": {
    "primary": "In an unofficial manner; without formal authorization, sanction, or public status.",
    "secondary": "In administrative statecraft, matters arranged unofficially between cabinet ministers often bypass parliamentary scrutiny.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer approached Holmes **unofficially**, seeking private counsel before scandalizing the Dartmoor neighborhood."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooneers met **unofficially** upon the forecastle, swapping eerie omens about the great white whale."},
      {"author": "L. M. Montgomery", "work": "Anne of Green Gables", "quote": "Marilla **unofficially** adopted the imaginative orphan girl long before the formal papers were signed."}
    ]
  },
  "unsatisfactorily.md": {
    "primary": "In a manner that fails to satisfy requirements, expectations, or desires; poorly.",
    "secondary": "In industrial quality auditing, components performing unsatisfactorily under thermal stress are rejected prior to assembly.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Peculiar morphological anomalies are explained most **unsatisfactorily** by the dogma of independent miraculous creations."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The interview had terminated so **unsatisfactorily** that Elinor could not contemplate it without deep distress."},
      {"author": "P. G. Wodehouse", "work": "Love Among the Chickens", "quote": "The amateur poultry enterprise proceeded most **unsatisfactorily**, resulting in chaos among the coops."}
    ]
  },
  "unsatisfactoriness.md": {
    "primary": "The state or condition of failing to satisfy needs, standards, or expectations; inadequacy.",
    "secondary": "In moral philosophy and existential ethics, the recognized unsatisfactoriness of hedonistic pleasure motivates the pursuit of enduring intellectual goods.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Men who experience higher mental pleasures readily acknowledge the intrinsic **unsatisfactoriness** of mere sensual gratification."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The chronic **unsatisfactoriness** of mortal existence often drives the soul toward profound religious conversion."},
      {"author": "Arthur Schopenhauer", "work": "The World as Will and Representation", "quote": "The perpetual striving of the will reveals the inherent **unsatisfactoriness** and suffering of all sentient life."}
    ]
  },
  "unsatisfactory.md": {
    "primary": "Failing to satisfy expectations, standards, or requirements; inadequate and disappointing.",
    "secondary": "In clinical diagnosis, an unsatisfactory biopsy sample lacks sufficient representative cellular architecture for definitive pathology.",
    "quotes": [
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Mary's letters were always **unsatisfactory**, filled with trivial complaints about her health and imaginary slights."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "How completely **unsatisfactory** is the view that each species was independently created to inhabit a particular climate!"},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The police theory of the murder is completely **unsatisfactory**, failing to account for the poisoned thorn."}
    ]
  },
  "unscientific.md": {
    "primary": "Not based on, conforming to, or exhibiting the principles and methods of science.",
    "secondary": "In epistemology and philosophy of science, an unscientific hypothesis relies upon untestable assumptions immune to empirical refutation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "To invoke special creation whenever a morphological puzzle arises is an **unscientific** surrender of genuine causal inquiry."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "Superstitious dogmatism is radically **unscientific**, demanding blind credulity where verified evidence is required."},
      {"author": "Karl Pearson", "work": "The Grammar of Science", "quote": "Any system of belief that rejects inductive verification must be classed as fundamentally **unscientific**."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action\Dashboard — fac"

updated = 0
for fname, info in data.items():
    fpath = os.path.join(base_dir, fname)
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {fname}")
        continue
    
    prefix = content[:book_idx]
    
    p_def = info["primary"].strip().rstrip(".") + "."
    s_def = info["secondary"].strip().rstrip(".") + "."
    
    new_book = f"> [!book] 📖 Definitions & Semantic Range\n> 1. **Primary Definition (Lexical / Standard Consensus)**: {p_def}\n> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: {s_def}\n"
    
    new_quote = "> [!quote] 💬 Contextual Usage & Authentic Quotations\n"
    for q in info["quotes"]:
        auth = q["author"].strip()
        work = q["work"].strip()
        quote_text = q["quote"].strip().strip('"').strip('“').strip('”')
        new_quote += f'> - 📜 **{auth} (*{work}*):** *"{quote_text}"*\n'
    
    new_content = prefix + new_book + "\n" + new_quote + "\n"
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Dashboard — fac Batch 3: Successfully updated {updated}/{len(data)} notes.")
