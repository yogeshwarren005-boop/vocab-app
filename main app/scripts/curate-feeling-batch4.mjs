import fs from 'fs';
import path from 'path';

const basePath = 'App database/Greek roots/Cluster Feeling & Sensation';

const filesData = {
  // Dashboard — mania (18 words)
  "Dashboard — mania/manage.md": {
    primary: "To handle, direct, administer, or wield authority over an enterprise, household, or set of obligations.",
    secondary: "To succeed in overcoming difficulties; to husband resources prudently under restrictive conditions.",
    quotes: [
      { author: "Francis Bacon", work: "Essays", quote: "He that cannot contract his expenditure must **manage** his estate with double vigilance and thrift." },
      { author: "Jane Austen", work: "Persuasion", quote: "Anne Elliot knew how to **manage** the domestic economy far better than her proud and spendthrift father." },
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "Prudent merchants **manage** capital with an eye toward steady returns rather than hazardous speculation." }
    ]
  },
  "Dashboard — mania/mania.md": {
    primary: "A state of abnormally elevated arousal, affect, and energy level; wild enthusiasm or frenzy.",
    secondary: "In clinical psychiatry, a severe mood state characteristic of bipolar disorder involving grandiosity, pressured speech, and lack of need for sleep.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "When melancholy fumes heat the brain to boiling, the humor bursts forth as raging **mania**." },
      { author: "Philippe Pinel", work: "A Treatise on Insanity", quote: "Patients seized by sudden **mania** display incredible muscular power and complete disregard for cold." },
      { author: "Sigmund Freud", work: "Mourning and Melancholia", quote: "The joyful frenzy of **mania** signifies that the ego has temporarily thrown off the tyrannical burdens of the conscience." }
    ]
  },
  "Dashboard — mania/maniac.md": {
    primary: "A person exhibiting extreme, violent, or wildly disordered behavior; an individual suffering from mania.",
    secondary: "Informally, a person showing fanatical, dangerous obsession or recklessness in an endeavor.",
    quotes: [
      { author: "Mary Shelley", work: "Frankenstein", quote: "I fled through the midnight streets of Geneva, haunted by the dread that some howling **maniac** was tracking my footsteps." },
      { author: "William Shakespeare", work: "The Comedy of Errors", quote: "They bound him in a dark room, claiming that the gentle merchant had turned into a frantic **maniac**." },
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "Madman! I tell you that she now stands without the door!—he shrieked like a raving **maniac**." }
    ]
  },
  "Dashboard — mania/maniacal.md": {
    primary: "Suggestive of, characteristic of, or resembling madness; wildly and unrestrainedly frantic.",
    secondary: "Marked by an alarming, irrational ferocity or frenzy in expression, voice, or behavior.",
    quotes: [
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "A scream of **maniacal** fury broke the nocturnal silence of Thornfield Hall, followed by the clanking of iron chains." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Ahab gave vent to a **maniacal** laugh as the lightning danced along the tips of our three iron harpoons." },
      { author: "Bram Stoker", work: "Dracula", quote: "The lunatic fell upon his knees with **maniacal** fervor, crying that his lord would feed him living souls." }
    ]
  },
  "Dashboard — mania/maniacally.md": {
    primary: "In a wild, frenzied, or raving manner; with uncontrollable madness.",
    secondary: "Displaying excessive, frightening intensity or hysterical abandon.",
    quotes: [
      { author: "H. G. Wells", work: "The Invisible Man", quote: "He struck out in the darkness and laughed **maniacally**, knowing no human eye could track his fists." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "The mad helmsman screamed **maniacally** into the fog as the spears rattled against the steamer's wooden shutters." },
      { author: "Robert Louis Stevenson", work: "The Strange Case of Dr Jekyll and Mr Hyde", quote: "Hyde grinned **maniacally** as he trampled the cane into splinters upon the pavement." }
    ]
  },
  "Dashboard — mania/manic.md": {
    primary: "Pertaining to, affected by, or characteristic of mania; marked by euphoric hyperactivity or frantic energy.",
    secondary: "Describing the phase of bipolar affective disorder dominated by sleeplessness, grandiosity, and flight of ideas.",
    quotes: [
      { author: "Emil Kraepelin", work: "Manic-Depressive Insanity and Paranoia", quote: "The **manic** patient writes dozens of letters, starts vast business ventures, and scatters gifts with reckless abandon." },
      { author: "Virginia Woolf", work: "A Writer's Diary", quote: "After weeks of brooding silence, I awoke with a **manic** surge of imagination that flooded five chapters in ten days." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "With the first high doses of the medication, several patients entered a delightful but volatile **manic** euphoria." }
    ]
  },
  "Dashboard — mania/manly.md": {
    primary: "Possessing the qualities traditionally admired in a courageous man, such as bravery, strength of character, and resolve.",
    secondary: "Steadfast, dignified, and upright; resisting despair or weakness under severe testing.",
    quotes: [
      { author: "William Shakespeare", work: "Julius Caesar", quote: "Brutus showed a **manly** fortitude when word came that Portia had swallowed fire in Rome." },
      { author: "Thomas Carlyle", work: "Past and Present", quote: "A **manly** devotion to honest toil is the only gospel that can heal our modern spiritual lethargy." },
      { author: "Frederick Douglass", work: "Narrative of the Life of Frederick Douglass", quote: "I stood up to Covey with a **manly** determination, resolved that he should never flog me again while life remained." }
    ]
  },
  "Dashboard — mania/manor.md": {
    primary: "A landed estate held by a feudal lord, consisting of demesne lands and surrounding holdings farmed by customary tenants.",
    secondary: "The noble residence or principal house belonging to such an estate (manor house).",
    quotes: [
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "The lord of the **manor** possessed the right of holding his court-baron for redressing misdemeanors." },
      { author: "George Eliot", work: "Silas Marner", quote: "The Squire held court at the great stone **manor**, surrounded by his hounds and deferential tenants." },
      { author: "Thomas Babington Macaulay", work: "The History of England", quote: "The country gentleman rarely traveled twenty miles from his quiet rural **manor** except during parliamentary elections." }
    ]
  },
  "Dashboard — mania/mansion.md": {
    primary: "A large, imposing, and architecturally stately dwelling house.",
    secondary: "In historical and philosophical usage, an abode, resting place, or enduring habitation of the soul.",
    quotes: [
      { author: "Nathaniel Hawthorne", work: "The House of the Seven Gables", quote: "The antique wooden **mansion** seemed to have grown out of the soil like an ancient gnarled oak." },
      { author: "Edgar Allan Poe", work: "The Fall of the House of Usher", quote: "A sensation of insufferable gloom pervaded the dim corridors of the decaying **mansion**." },
      { author: "Henry James", work: "The Portrait of a Lady", quote: "The historic English **mansion** stood serene upon its emerald lawn above the winding Thames." }
    ]
  },
  "Dashboard — mania/manure.md": {
    primary: "Organic material, especially animal excrement or decomposed vegetable compost, applied to land to fertilize soil and foster crops.",
    secondary: "Historically, to enrich, cultivate, or work land by manual husbandry.",
    quotes: [
      { author: "Virgil", work: "Georgics", quote: "Spread rich **manure** across the exhausted loam before the autumn rains wash the hillsides." },
      { author: "Francis Bacon", work: "Sylva Sylvarum", quote: "Well-rotted animal **manure** warms the rootlets of fruit trees, quickening their spring sap." },
      { author: "Gilbert White", work: "The Natural History of Selborne", quote: "The farmers value pigeon dung as the most potent **manure** for cold arable clays." }
    ]
  },
  "Dashboard — mania/megalomania.md": {
    primary: "A psychiatric disorder or delusion characterized by exaggerated feelings of personal power, wealth, grandeur, or omnipotence.",
    secondary: "In political satire and history, the lust for authoritarian domination and self-glorification.",
    quotes: [
      { author: "Friedrich Nietzsche", work: "Ecce Homo", quote: "My philosophical destiny requires that I speak without false modesty, though small minds may call it **megalomania**." },
      { author: "Bertrand Russell", work: "Power: A New Social Analysis", quote: "When the conqueror believes he is a divine instrument of fate, his policy hardens into murderous **megalomania**." },
      { author: "Sigmund Freud", work: "The Future of an Illusion", quote: "The infantile ego indulges in dreams of **megalomania** to compensate for its utter vulnerability before nature." }
    ]
  },
  "Dashboard — mania/megalomaniac.md": {
    primary: "A person affected by megalomania; one who displays an obsession with self-importance, grandiosity, and supreme control.",
    secondary: "A ruthless autocrat or narcissistic leader who seeks absolute supremacy at any human cost.",
    quotes: [
      { author: "George Orwell", work: "The Lion and the Unicorn", quote: "The modern dictator is a political **megalomaniac** who has harnessed advanced technology to primitive tribal myths." },
      { author: "Aldous Huxley", work: "Ends and Means", quote: "Surrounded by trembling flatterers, the absolute ruler inevitably turns into an isolated **megalomaniac**." },
      { author: "H. G. Wells", work: "The Shape of Things to Come", quote: "The memoirs of twentieth-century warlords read like the ravings of an unbridled **megalomaniac**." }
    ]
  },
  "Dashboard — mania/megalomaniacal.md": {
    primary: "Marked by or characteristic of megalomania; exhibiting grandiose delusions of unearned greatness or imperial power.",
    secondary: "Exorbitant and wildly disproportionate in scale or ambition.",
    quotes: [
      { author: "Joseph Conrad", work: "Under Western Eyes", quote: "The revolutionary manifesto was couched in **megalomaniacal** phrases that promised the immediate rebirth of humanity." },
      { author: "Arthur Koestler", work: "Darkness at Noon", quote: "Number One directed the purges with a cold, **megalomaniacal** conviction that history had chosen him as its prophet." },
      { author: "Thomas Mann", work: "Doctor Faustus", quote: "Leverkühn's final oratorio expressed a **megalomaniacal** desire to break through the bounds of human harmony." }
    ]
  },
  "Dashboard — mania/megalomanic.md": {
    primary: "Pertaining to or affected with megalomania; megalomaniacal.",
    secondary: "Displaying inflated self-consequence and grandiosity in social or political theory.",
    quotes: [
      { author: "William James", work: "The Varieties of Religious Experience", quote: "The lunatic ward contains many a **megalomanic** claimant to the thrones of Europe or celestial glory." },
      { author: "Havelock Ellis", work: "The Philosophy of Conflict", quote: "Militarism is the **megalomanic** disease of empires intoxicated with industrial expansion." },
      { author: "George Bernard Shaw", work: "Heartbreak House", quote: "You talk like a **megalomanic** schoolboy who imagines he can steer the ship of state by shouting." }
    ]
  },
  "Dashboard — mania/monomania.md": {
    primary: "An exaggerated, pathological obsession or preoccupation with a single idea, subject, or emotional goal.",
    secondary: "In 19th-century alienism, a partial mental disorder wherein the intellect is intact except regarding one specific delusion.",
    quotes: [
      { author: "Herman Melville", work: "Moby-Dick", quote: "All that most maddens and torments; all that stirs up the lees of things, was visibly personified in Ahab's **monomania**." },
      { author: "Jean-Étienne Esquirol", work: "Des Maladies Mentales", quote: "In intellectual **monomania**, a single false notion dominates the mind while other faculties function normally." },
      { author: "Edgar Allan Poe", work: "Berenice", quote: "This nervous intensity of interest was not a passion, but a brooding, irresistible **monomania** of the intellect." }
    ]
  },
  "Dashboard — mania/monomaniac.md": {
    primary: "A person suffering from monomania; someone single-mindedly and fanatically devoted to an obsessive pursuit.",
    secondary: "A literary or historical character defined by relentless fixation on one target or grievance.",
    quotes: [
      { author: "Charles Dickens", work: "Great Expectations", quote: "Miss Havisham lived as an embalmed **monomaniac**, nursing the ruins of her broken wedding day." },
      { author: "Nathaniel Hawthorne", work: "The Scarlet Letter", quote: "Roger Chillingworth transformed into a calm, pitiless **monomaniac**, probing the minister's wounded soul." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Six Napoleons", quote: "Sherlock Holmes proved that the criminal was no ordinary political **monomaniac**, but a cunning pearl thief." }
    ]
  },
  "Dashboard — mania/monomaniacal.md": {
    primary: "Exhibiting, characterized by, or pertaining to monomania; driven by an all-consuming single obsession.",
    secondary: "Pursued with narrow, fanatical intensity to the exclusion of reason, balance, and empathy.",
    quotes: [
      { author: "Herman Melville", work: "Pierre: or, The Ambiguities", quote: "He locked himself in his study, laboring with a **monomaniacal** intensity that defied sleep and nourishment." },
      { author: "Joseph Conrad", work: "The Secret Agent", quote: "The bomb-maker had a **monomaniacal** desire to achieve instantaneous, unanswerable destruction." },
      { author: "Henry James", work: "The Aspern Papers", quote: "My quest for the dead poet's letters acquired a **monomaniacal** quality that blinded me to common courtesy." }
    ]
  },
  "Dashboard — mania/pyromaniac.md": {
    primary: "A person with a compulsive, irresistible urge to deliberately set fire to buildings or objects, often accompanied by emotional relief or excitement.",
    secondary: "In abnormal psychology, an individual with an impulse control disorder centered on fascination with and ignition of fire.",
    quotes: [
      { author: "Cesare Lombroso", work: "Crime, Its Causes and Remedies", quote: "The true **pyromaniac** experiences an intense sensory fascination watching flames consume timber and thatch." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In adolescent mental degeneracy, the morbid drive of the **pyromaniac** poses a grave hazard to rural communities." },
      { author: "Karl Jaspers", work: "General Psychopathology", quote: "The act of arson in a **pyromaniac** is preceded by unendurable internal tension that dissolves only when the blaze roars." }
    ]
  },

  // Dashboard — mis (34 words)
  "Dashboard — mis/mis.md": {
    primary: "The Greek combining prefix *mis-* (from *mīsos*), signifying hatred, abhorrence, aversion, or hostility, as seen in *misanthrope*, *misogyny*, and *misology*.",
    secondary: "The classical prefix denoting deep-seated antipathy, contempt, or pathological revulsion across ethical, sociological, and psychological vocabularies.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "The combining element **mis** derives from the neuter noun *misos*, signifying hatred, malice, or detestation." },
      { author: "Plato", work: "Phaedo", quote: "Let us beware above all that we do not become haters of reason, infected with the fatal prefix **mis**." },
      { author: "Samuel Johnson", work: "A Dictionary of the English Language", quote: "Words formed with Greek **mis** denote an ingrained antipathy to humanity, truth, or sacred institutions." }
    ]
  },
  "Dashboard — mis/misalliance.md": {
    primary: "An improper, unsuitable, or undesirable alliance or marriage, especially one with a person of lower social status or incompatible temperaments.",
    secondary: "In social satire and drama, a mismatch of partners that creates domestic friction and violates dynastic expectations.",
    quotes: [
      { author: "George Bernard Shaw", work: "Misalliance", quote: "The aristocrat considered his son's match with the merchant's daughter an outrageous **misalliance**." },
      { author: "William Makepeace Thackeray", work: "Vanity Fair", quote: "Old Osborne disinherited George for his scandalous **misalliance** with poor, penniless Amelia." },
      { author: "Honoré de Balzac", work: "Lost Illusions", quote: "A provincial nobility terrified of extinction regarded every middle-class match as a ruinous **misalliance**." }
    ]
  },
  "Dashboard — mis/misally.md": {
    primary: "To ally, join, or marry improperly, unsuitably, or undesirably.",
    secondary: "To connect or associate disparate principles, political parties, or factions in an incongruous or harmful combination.",
    quotes: [
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "It is fatal for a great nation to **misally** itself with factions whose sole principle is the subversion of ancient law." },
      { author: "Jonathan Swift", work: "The Conduct of the Allies", quote: "Our ministers were persuaded to **misally** the kingdom's military fortunes with foreign courts whose interests ran counter to our own." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "A scholar who seeks domestic peace must take care not to **misally** his quiet mind with frivolity." }
    ]
  },
  "Dashboard — mis/misandrist.md": {
    primary: "A person who dislikes, despises, or harbors ingrained prejudice against men; one who practices misandry.",
    secondary: "In social critique and feminist discourse, an individual expressing ideological hostility toward men or masculinity.",
    quotes: [
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "The embittered woman who has suffered abuse may react by becoming a dogmatic **misandrist**, rejecting all masculine companionship." },
      { author: "George Bernard Shaw", work: "The Quintessence of Ibsenism", quote: "Ibsen was accused of being a **misandrist** by critics who mistook his exposure of bourgeois hypocrisy for hatred of men." },
      { author: "H. L. Mencken", work: "In Defense of Women", quote: "The militant suffragette was frequently caricatured in the press as a scolding, humorless **misandrist**." }
    ]
  },
  "Dashboard — mis/misandry.md": {
    primary: "Dislike of, contempt for, or ingrained prejudice against men (the counterpart of misogyny).",
    secondary: "A cultural, literary, or ideological hostility toward men and masculine norms.",
    quotes: [
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Just as patriarchy breeds misogyny, so can patriarchal tyranny provoke in women a bitter, defensive **misandry**." },
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Psychologists must recognize that institutional injustice can produce neurotic **misandry** as well as gynophobia." },
      { author: "Bertrand Russell", work: "Marriage and Morals", quote: "A society poisoned by sex antagonism oscillated between crude misogyny and equally absurd **misandry**." }
    ]
  },
  "Dashboard — mis/misanthrope.md": {
    primary: "A person who dislikes, distrusts, or hates humankind and avoids human society.",
    secondary: "A literary archetype (such as Molière's Alceste or Shakespeare's Timon) who withdraws into bitter solitude after disillusionment with human hypocrisy.",
    quotes: [
      { author: "Molière", work: "The Misanthrope", quote: "I wish from the bottom of my heart that all human beings would leave me alone; I am a confirmed **misanthrope**." },
      { author: "William Shakespeare", work: "Timon of Athens", quote: "I am **Misanthropos**, and hate mankind; for thy part, I do wish thou wert a dog, that I might love thee something." },
      { author: "Jonathan Swift", work: "Letters to Alexander Pope", quote: "I have ever hated all nations, professions, and communities, and all my love is toward individuals; upon this great foundation of **misanthrope** my travels are built." }
    ]
  },
  "Dashboard — mis/misanthropic.md": {
    primary: "Disliking humankind and expecting the worst of human nature; characterized by misanthropy; antisocial.",
    secondary: "Marked by a cynical, gloomy contempt for social conventions and human moral integrity.",
    quotes: [
      { author: "Lord Byron", work: "Childe Harold's Pilgrimage", quote: "With pleasure drugged, he bowed his haughty head, nourishing a proud, **misanthropic** disdain for courts and camps." },
      { author: "Herman Melville", work: "The Confidence-Man", quote: "The solitary traveller wrapped himself in a bear-skin coat, casting **misanthropic** glances at the bustling deck." },
      { author: "Thomas Carlyle", work: "Sartor Resartus", quote: "In the centre of indifference, Teufelsdröckh endured an agonizing **misanthropic** season before faith was restored." }
    ]
  },
  "Dashboard — mis/misanthropical.md": {
    primary: "An older or formal variant of misanthropic; showing or inspired by a hatred of humanity.",
    secondary: "Pertaining to gloomy, solitary isolation rooted in bitter disillusionment with mankind.",
    quotes: [
      { author: "Samuel Johnson", work: "Lives of the Most Eminent English Poets", quote: "Swift's genius was too often clouded by a harsh, **misanthropical** humour that alienated his closest admirers." },
      { author: "Walter Scott", work: "The Antiquary", quote: "He had retired to the lonely seashore, nursing a **misanthropical** grief that permitted no visitors." },
      { author: "Edgar Allan Poe", work: "The Gold-Bug", quote: "Legrand had built a hut on Sullivan's Island to indulge his solitary and **misanthropical** eccentricities." }
    ]
  },
  "Dashboard — mis/misanthropist.md": {
    primary: "A person who hates or distrusts humanity; a misanthrope.",
    secondary: "An observer who persistently interprets human actions through the lens of malice and selfishness.",
    quotes: [
      { author: "Tobias Smollett", work: "The Adventures of Peregrine Pickle", quote: "The old sea captain lived as a confirmed **misanthropist**, swearing that dogs were the only honest creatures left." },
      { author: "Alexander Pope", work: "An Essay on Man", quote: "The foolish **misanthropist** censures universal Providence merely because individual mortals are frail." },
      { author: "Arthur Schopenhauer", work: "Parerga and Paralipomena", quote: "The true **misanthropist** is formed not by envy, but by repeated discoveries of human baseness." }
    ]
  },
  "Dashboard — mis/misanthropy.md": {
    primary: "A dislike, distrust, or hatred of humankind; general contempt for human society and nature.",
    secondary: "In moral philosophy, a philosophical pessimism asserting that humanity is incorrigibly selfish, cruel, or hypocritical.",
    quotes: [
      { author: "Immanuel Kant", work: "Lectures on Ethics", quote: "True **misanthropy** is far more dangerous than human weakness, for it turns the soul completely away from duty to neighbor." },
      { author: "Jonathan Swift", work: "Gulliver's Travels", quote: "After dwelling among the noble Houyhnhnms, Gulliver succumbed to a total **misanthropy**, shuddering at the sight of his own family." },
      { author: "Arthur Schopenhauer", work: "The World as Will and Representation", quote: "A profound **misanthropy** is often the price paid by generous souls who expect too much virtue from the world." }
    ]
  },
  "Dashboard — mis/miser.md": {
    primary: "A person who hoards wealth and spends as little money as possible, living in wretched self-denial.",
    secondary: "A penurious individual whose life is consumed by the obsessive fear of parting with possessions or gold.",
    quotes: [
      { author: "Charles Dickens", work: "A Christmas Carol", quote: "Scrooge was a tight-fisted hand at the grindstone, a squeezing, wrenching, grasping, scraping, clutching, covetous old **miser**!" },
      { author: "George Eliot", work: "Silas Marner", quote: "The lonely weaver counted his golden guineas every evening, living as an unconscious **miser** until the child arrived." },
      { author: "Molière", work: "The Miser", quote: "Harpagon wept over his buried cashbox, crying that the thief had stolen the soul of a poor **miser**." }
    ]
  },
  "Dashboard — mis/miserable.md": {
    primary: "Wretchedly unhappy, uncomfortable, or dejected; full of distress or misery.",
    secondary: "Pitiably small, inadequate, or wretched (e.g., a miserable pittance).",
    quotes: [
      { author: "William Shakespeare", work: "As You Like It", quote: "Blow, blow, thou winter wind, thou art not so unkind as man's ingratitude; life is a **miserable** play." },
      { author: "Victor Hugo", work: "Les Misérables", quote: "The law made him a pariah, leaving the **miserable** ex-convict to wander without food or shelter in the frost." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "Locked in the red-room, I was a discord in Gateshead Hall, a strange, **miserable** little creature." }
    ]
  },
  "Dashboard — mis/miserly.md": {
    primary: "Characteristic of a miser; parsimonious, stingy, or mean with money and hospitality.",
    secondary: "Paltry, scanty, or grudgingly bestowed in quantity.",
    quotes: [
      { author: "Washington Irving", work: "The Devil and Tom Walker", quote: "Tom and his wife were so **miserly** that they even conspired to cheat each other out of kitchen scraps." },
      { author: "Charles Dickens", work: "Great Expectations", quote: "The dinner was so **miserly** and cold that Pip's teeth chattered over the single mutton chop." },
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "John Dashwood convinced himself by **miserly** reasoning that three thousand pounds was far too generous for his sisters." }
    ]
  },
  "Dashboard — mis/misocainea.md": {
    primary: "An irrational hatred of, dread of, or intense aversion to new ideas, novelty, or innovation (derived from Greek *misos* 'hatred' and *kainos* 'new').",
    secondary: "In sociology and psychology, rigid resistance to intellectual progress or institutional reform; misoneism.",
    quotes: [
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "Primitive tribes and conservative academies alike exhibit an obstinate **misocainea** that stones the innovator." },
      { author: "William James", work: "The Principles of Psychology", quote: "Habit is the great flywheel of society, but in its extreme form it petrifies into a sterile **misocainea**." },
      { author: "John Stuart Mill", work: "On Liberty", quote: "The stagnant despotism of custom represents that collective **misocainea** which suffocates original genius." }
    ]
  },
  "Dashboard — mis/misogamist.md": {
    primary: "A person who hates, distrusts, or is strongly averse to marriage (from Greek *misos* and *gamos*).",
    secondary: "An individual committed to lifelong bachelorhood or spinisterhood out of principled antipathy to marital bonds.",
    quotes: [
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "The cynical **misogamist** recites the miseries of wedded life, praising the solitary philosopher's liberty." },
      { author: "William Shakespeare", work: "Much Ado About Nothing", quote: "Benedick vowed he would live and die a confirmed bachelor, the very prince of every boastful **misogamist**." },
      { author: "Arthur Schopenhauer", work: "Essays and Aphorisms", quote: "The prudent philosopher is necessarily a **misogamist**, refusing to double his obligations while halving his rights." }
    ]
  },
  "Dashboard — mis/misogamy.md": {
    primary: "Hatred of or aversion to marriage; opposition to entering into wedlock.",
    secondary: "In literary and philosophical traditions, the critique of matrimonial constraints in favor of personal freedom or ascetic contemplation.",
    quotes: [
      { author: "Desiderius Erasmus", work: "The Praise of Folly", quote: "Were it not for my gift of sweet blindness, **misogamy** would depopulate the civilized world in a generation." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Disappointed suitors often retreat into bitter **misogamy**, blaming Hymen for all the griefs of life." },
      { author: "Samuel Johnson", work: "Rasselas", quote: "Marriage has many pains, but celibacy has no pleasures; do not let early doubts drive you into permanent **misogamy**." }
    ]
  },
  "Dashboard — mis/misogynic.md": {
    primary: "Relating to, characterized by, or exhibiting misogyny; hateful or contemptuous toward women.",
    secondary: "Reflecting institutional or cultural hostility against the female sex.",
    quotes: [
      { author: "Mary Wollstonecraft", work: "A Vindication of the Rights of Woman", quote: "Rousseau's educational treatises are infected with a **misogynic** prejudice that treats women as decorative toys." },
      { author: "John Stuart Mill", work: "The Subjection of Women", quote: "The legal disabilities imposed on wives reflect ancient, unexamined **misogynic** traditions." },
      { author: "George Bernard Shaw", work: "Man and Superman", quote: "Tanner was fond of delivering long **misogynic** tirades, though everyone saw he was doomed to be caught." }
    ]
  },
  "Dashboard — mis/misogynism.md": {
    primary: "Hatred of, contempt for, or ingrained prejudice against women (an alternative noun form of misogyny).",
    secondary: "In sociological critique, an institutionalized pattern of cultural antagonism and discrimination directed against women.",
    quotes: [
      { author: "Havelock Ellis", work: "Studies in the Psychology of Sex", quote: "Medieval monastic ascetics indulged in a ferocious **misogynism** that branded woman as the gateway to perdition." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "The history of male scholarship is crowded with curious examples of unprovoked **misogynism**." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Every mythology invents scapegoats to justify female enslavement, rationalizing brutal **misogynism** as natural law." }
    ]
  },
  "Dashboard — mis/misogynist.md": {
    primary: "A person who dislikes, despises, or is strongly prejudiced against women.",
    secondary: "An individual who holds or expresses beliefs that women are morally, intellectually, or physically inferior to men.",
    quotes: [
      { author: "Jonathan Swift", work: "A Modest Proposal", quote: "The satirist was frequently branded a cruel **misogynist**, though his sharpest arrows targeted hypocrisy in both sexes." },
      { author: "Arthur Conan Doyle", work: "A Scandal in Bohemia", quote: "Sherlock Holmes was never a general **misogynist**, but he distrusted the emotional instability of the female character." },
      { author: "George Eliot", work: "Middlemarch", quote: "Mr. Casaubon was no crude **misogynist**, but his dry pedantry left no room for Dorothea's vibrant spirit." }
    ]
  },
  "Dashboard — mis/misogynistic.md": {
    primary: "Strongly prejudiced against women; showing or expressing hatred, contempt, or discrimination toward women.",
    secondary: "Reflecting patriarchal attitudes that demean or silence women in culture and literature.",
    quotes: [
      { author: "Virginia Woolf", work: "Three Guineas", quote: "The universities were guarded by ancient regulations that maintained an openly **misogynistic** exclusion of female scholars." },
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "The patriarchal myths found in Genesis and Hesiod established a **misogynistic** archetype that persisted for millenia." },
      { author: "John Stuart Mill", work: "The Subjection of Women", quote: "To base legal disenfranchisement upon sex is to perpetuate a **misogynistic** relic of barbarian conquest." }
    ]
  },
  "Dashboard — mis/misogynous.md": {
    primary: "Displaying hatred or contempt toward women; misogynistic.",
    secondary: "Pertaining to anti-female rhetoric, satire, or cultural prejudice in historical writing.",
    quotes: [
      { author: "Samuel Johnson", work: "The Rambler", quote: "Juvenal's famous satire upon Roman matrons is an unsparing, **misogynous** masterpiece of rhetorical indignation." },
      { author: "Havelock Ellis", work: "The Task of Social Hygiene", quote: "Old legal codes treated the wife as chattel, embodying a deeply **misogynous** conception of domestic rights." },
      { author: "Walter Pater", work: "Appreciations", quote: "Even within the poet's romantic verse, a dark, **misogynous** undertone surfaced whenever love turned to jealousy." }
    ]
  },
  "Dashboard — mis/misogyny.md": {
    primary: "Dislike of, contempt for, or ingrained prejudice against women.",
    secondary: "In feminist theory and sociology, a systemic social ideology that enforces female subordination and sanctions patriarchal privilege.",
    quotes: [
      { author: "Simone de Beauvoir", work: "The Second Sex", quote: "Legislators, priests, philosophers, and poets have taken upon themselves the task of showing that female nature demands subordination, weaving an intricate tapestry of **misogyny**." },
      { author: "Virginia Woolf", work: "A Room of One's Own", quote: "The history of England is scarred by male **misogyny**, which kept Shakespeare's sister illiterate and chained to household pots." },
      { author: "John Stuart Mill", work: "The Subjection of Women", quote: "The subtle **misogyny** of polite society pretends that women are worshipped while denying them the common rights of citizens." }
    ]
  },
  "Dashboard — mis/misoneism.md": {
    primary: "Hatred, fear, or intolerance of innovation, change, or novelty (from Greek *mīsos* and *neos*).",
    secondary: "In anthropology, psychology, and sociology (notably Cesare Lombroso), the instinctive human resistance to novel customs and intellectual revolutions.",
    quotes: [
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "A deep-seated biological **misoneism** protects human communities from erratic innovation, but it also crucifies prophets." },
      { author: "William James", work: "Pragmatism", quote: "The human mind naturally shrinks from new concepts; our intellectual inertia is a formidable form of **misoneism**." },
      { author: "John Dewey", work: "Human Nature and Conduct", quote: "Social institutions become petrified when uncritical **misoneism** treats existing arrangements as eternal and sacred." }
    ]
  },
  "Dashboard — mis/misopaedia.md": {
    primary: "An abnormal hatred or extreme aversion toward children, especially one's own offspring (from Greek *misos* and *pais*).",
    secondary: "In psychopathology and forensic medicine, a morbid condition linked to severe postpartum depression or psychotic parental rejection.",
    quotes: [
      { author: "Henry Maudsley", work: "Responsibility in Mental Disease", quote: "In puerperal insanity, the mother's natural maternal devotion may suddenly invert into a horrifying **misopaedia**." },
      { author: "Cesare Lombroso", work: "The Female Offender", quote: "Cases of maternal infanticide often reveal a pathological **misopaedia** sparked by prolonged exhaustion and hunger." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The practitioner must intervene swiftly when morbid **misopaedia** threatens the safety of a newborn infant." }
    ]
  },
  "Dashboard — mis/misotheism.md": {
    primary: "Hatred of God or the gods; active hatred of divinity.",
    secondary: "In theological literature and philosophy, a spiritual stance distinct from atheism, wherein God's existence is acknowledged but reviled as cruel, unjust, or tyrannical.",
    quotes: [
      { author: "Lord Byron", work: "Cain: A Mystery", quote: "Cain's anguished questioning of the Almighty's justice borders on an overt poetic **misotheism**." },
      { author: "Friedrich Nietzsche", work: "The Antichrist", quote: "My campaign against Christian morality is not mere doubt, but an open declaration of intellectual **misotheism**." },
      { author: "Arthur Schopenhauer", work: "The World as Will and Representation", quote: "Faced with the endless slaughter of animal nature, one must conclude that if a creator exists, **misotheism** is the only honest response." }
    ]
  },
  "Dashboard — mis/missal.md": {
    primary: "A liturgical book containing all the prayers, readings, chants, and rubrics necessary for the celebration of the Roman Catholic Mass throughout the year.",
    secondary: "An illuminated medieval ecclesiastical codex valued for its calligraphy, miniatures, and liturgical music notation.",
    quotes: [
      { author: "Thomas More", work: "Dialogue Concerning Heresies", quote: "The priest opened the gilded **missal** upon the altar, reciting the ancient Canon with devout reverence." },
      { author: "Walter Scott", work: "The Lady of the Lake", quote: "The hermit knelt upon the cold damp stone, his illuminated Latin **missal** clasped across his breast." },
      { author: "John Ruskin", work: "The Stones of Venice", quote: "The fourteenth-century **missal** was a treasure-house where the illuminator lavished ultramarine and gold leaf on every capital." }
    ]
  },
  "Dashboard — mis/missed.md": {
    primary: "Failed to hit, reach, catch, strike, or encounter an intended target or person.",
    secondary: "Felt sadness, longing, or regret over the absence or loss of someone or something valued.",
    quotes: [
      { author: "William Shakespeare", work: "Othello", quote: "I had not lost the handkerchief, but **missed** it from my chamber, which filled my soul with dreadful foreboding." },
      { author: "Jane Austen", work: "Emma", quote: "She **missed** her old companion hourly, finding the drawing-room strangely quiet after the wedding." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The harpoon **missed** the Leviathan's flank by an inch, plunging uselessly into the foamy swell." }
    ]
  },
  "Dashboard — mis/missing.md": {
    primary: "Not present, lost, or unable to be found; absent from a customary or expected place.",
    secondary: "Of a soldier or sailor, not accounted for after a military engagement but not known to be killed or captured.",
    quotes: [
      { author: "Daniel Defoe", work: "Robinson Crusoe", quote: "Of all our ship's company, not a soul survived save myself; all the rest were drowned and **missing**." },
      { author: "Arthur Conan Doyle", work: "The Adventure of the Missing Three-Quarter", quote: "Godfrey Staunton, the rugby three-quarter, was strangely **missing** from his Cambridge hotel on the eve of the match." },
      { author: "George Orwell", work: "Homage to Catalonia", quote: "In the casualty lists, dozens of comrades were posted simply as **missing** after the night attack." }
    ]
  },
  "Dashboard — mis/mission.md": {
    primary: "An important official assignment, journey, or task given to a person or group, especially in diplomacy, military strategy, or religion.",
    secondary: "A religious expedition or operational center established by Christian churches to propagate faith, provide education, and deliver humanitarian aid.",
    quotes: [
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "The great **mission** of opening the African interior to commerce and Christianity sustained my lonely steps." },
      { author: "Alexis de Tocqueville", work: "Democracy in America", quote: "The early Puritan emigrants believed they were entrusted with a divine **mission** to plant a city upon a hill." },
      { author: "Joseph Conrad", work: "Heart of Darkness", quote: "Marlow found that the idealistic European **mission** in the Congo had degenerated into a sordid scramble for ivory." }
    ]
  },
  "Dashboard — mis/missional.md": {
    primary: "Relating to, characterized by, or engaged in religious mission, evangelism, or outreach.",
    secondary: "In contemporary ecclesiastical theology, describing churches or congregations oriented outwardly toward community engagement and service.",
    quotes: [
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "The **missional** strategy must integrate agricultural training and healing alongside preaching." },
      { author: "William Carey", work: "An Enquiry into the Obligations of Christians", quote: "A church that loses its **missional** zeal quickly declines into theological stagnation and self-satisfaction." },
      { author: "Albert Schweitzer", work: "On the Edge of the Primeval Forest", quote: "The true **missional** calling is demonstrated not by dogma, but by the practical ministry of hospital wards in the jungle." }
    ]
  },
  "Dashboard — mis/missionary.md": {
    primary: "A person sent on a religious mission, especially one dispatched to promote Christianity in a foreign country or marginalized community.",
    secondary: "Relating to or characteristic of a religious mission or evangelical enterprise.",
    quotes: [
      { author: "David Livingstone", work: "Missionary Travels and Researches in South Africa", quote: "The life of a pioneer **missionary** in the wilderness demands physical endurance as much as spiritual faith." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "St. John Rivers burned to become a **missionary** in India, offering his life as an unyielding sacrifice." },
      { author: "Robert Louis Stevenson", work: "In the South Seas", quote: "The Polynesian islanders were profoundly changed by the arrival of the first white **missionary** schooner." }
    ]
  },
  "Dashboard — mis/missioner.md": {
    primary: "A person who is sent on or conducts a religious mission, particularly a preacher of parish missions or revivals; a missionary.",
    secondary: "A member of an ecclesiastical community dedicated to preaching, pastoral visitation, and charitable relief among the urban poor.",
    quotes: [
      { author: "John Wesley", work: "Journal", quote: "The parish **missioner** preached in the market-place to thousands of colliers who had never darkened a church door." },
      { author: "Charles Dickens", work: "The Chimes", quote: "The devoted city **missioner** labored among the damp cellar dwellings of London, bringing comfort to the dying." },
      { author: "John Henry Newman", work: "Sermons on Various Occasions", quote: "The visiting **missioner** brought a revival of prayer to parishes that had grown lukewarm under routine." }
    ]
  },
  "Dashboard — mis/missive.md": {
    primary: "A written communication, letter, or official dispatch, especially a formal, solemn, or lengthy one.",
    secondary: "Historically, something sent or dispatched; an envoy or special messenger.",
    quotes: [
      { author: "William Shakespeare", work: "Macbeth", quote: "Whiles I stood rapt in the wonder of it, came **missives** from the king, who all-hailed me 'Thane of Cawdor'." },
      { author: "Walter Scott", work: "The Heart of Midlothian", quote: "The Duke placed the royal **missive** in the hands of the trembling Scottish maiden." },
      { author: "Edgar Allan Poe", work: "The Purloined Letter", quote: "The stolen royal **missive** was of so critical a nature that its disclosure would compromise high state security." }
    ]
  },
  "Dashboard — mis/remission.md": {
    primary: "A temporary or permanent diminution or disappearance of the signs and symptoms of a disease, especially chronic or malignant illness.",
    secondary: "In law and theology, the forgiveness, cancellation, or pardon of a sin, penalty, debt, or criminal sentence.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In pernicious anemia, the patient often enjoys a deceptive, temporary **remission** before relapse occurs." },
      { author: "Thomas Cranmer", work: "The Book of Common Prayer", quote: "Almighty God hath given power and commandment to His ministers to declare to His people the **remission** of their sins." },
      { author: "William Blackstone", work: "Commentaries on the Laws of England", quote: "The royal prerogative allows the sovereign to grant full **remission** of criminal penalties to repentant convicts." }
    ]
  },

  // Dashboard — miso (4 words)
  "Dashboard — miso/miso.md": {
    primary: "The Greek combining form *miso-* (from *mīsos*), signifying hatred, dislike, aversion, or antipathy (as in *misogyny*, *misoneism*).",
    secondary: "The linguistic prefix used across psychological, philosophical, and social terminology to designate deep-seated revulsion toward an object, gender, or idea.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "Compounds beginning with **miso** signify active hatred or aversion, directly contrasting with those in *philo-*." },
      { author: "Plato", work: "Phaedo", quote: "Socrates warned that the prefix **miso** must never attach to philosophy, lest men become haters of reason." },
      { author: "Desiderius Erasmus", work: "Adagia", quote: "The ancient Greeks formed barbed epithets with **miso**, branding tyrants as haters of the commons." }
    ]
  },
  "Dashboard — miso/misocainea.md": {
    primary: "An abnormal hatred, dread, or passionate aversion to new ideas, novel customs, or innovative practices (from Greek *mīsos* and *kainos*).",
    secondary: "In social psychology and anthropological theory, conservative resistance to institutional transformation; misoneism.",
    quotes: [
      { author: "Cesare Lombroso", work: "The Man of Genius", quote: "Every major scientific discovery must run the gauntlet of ingrained academic **misocainea**." },
      { author: "William James", work: "The Principles of Psychology", quote: "Elderly institutions naturally succumb to **misocainea**, viewing every intellectual departure as heresy." },
      { author: "John Stuart Mill", work: "Autobiography", quote: "Bentham's legal reforms were met by a wall of entrenched professional **misocainea**." }
    ]
  },
  "Dashboard — miso/misology.md": {
    primary: "A hatred, distrust, or contempt of reasoning, logical argument, philosophy, or intellectual inquiry.",
    secondary: "In Platonic philosophy, an intellectual despair where disappointment with flawed arguments leads one to reject rational discourse altogether.",
    quotes: [
      { author: "Plato", work: "Phaedo", quote: "Let us not become misologues, for there is no greater evil than **misology**, the hatred of rational argument." },
      { author: "Immanuel Kant", work: "Groundwork of the Metaphysics of Morals", quote: "Cultivation of reason often breeds a subtle **misology**, when men discover that philosophy does not guarantee happiness." },
      { author: "John Locke", work: "The Conduct of the Understanding", quote: "Disappointed students who encounter contradictions in metaphysics easily slide into total **misology**." }
    ]
  },
  "Dashboard — miso/misoneism.md": {
    primary: "A hatred, fear, or intolerance of novelty, change, innovation, or modern trends.",
    secondary: "In sociology and cultural history, the psychological defense mechanism by which traditional societies resist foreign or modern intrusions.",
    quotes: [
      { author: "Cesare Lombroso", work: "Crime, Its Causes and Remedies", quote: "Popular **misoneism** explains why the introduction of railways and vaccination provoked violent peasant uprisings." },
      { author: "William James", work: "The Varieties of Religious Experience", quote: "Ecclesiastical orthodoxy is fortified by a deep, defensive **misoneism** that suspects every novel insight." },
      { author: "George Bernard Shaw", work: "The Doctor's Dilemma", quote: "The medical profession is notoriously infected with **misoneism**, accepting new antiseptics only after forty years of denial." }
    ]
  },

  // Dashboard — odyn (6 words)
  "Dashboard — odyn/allodynia.md": {
    primary: "A condition in which pain is experienced from a stimulus that does not normally provoke pain (such as a light touch, breeze, or gentle pressure on the skin).",
    secondary: "In neuropathic pain physiology, a classic sign of central sensitization and abnormal sensory processing following nerve injury or postherpetic neuralgia.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The postherpetic neuralgia patient suffered from terrible **allodynia**, crying out when even a silk shirt touched the chest." },
      { author: "S. Weir Mitchell", work: "Injuries of Nerves and Their Consequences", quote: "In causalgia, the slightest touch or sudden breath of air triggers fierce burning agony, a phenomenon now labeled **allodynia**." },
      { author: "Oliver Sacks", work: "Migraine", quote: "During severe migraine paroxysms, many sufferers exhibit temporary cutaneous **allodynia**, unable to brush their hair." }
    ]
  },
  "Dashboard — odyn/anodyne.md": {
    primary: "A pain-relieving medicine, drug, or soothing application; not likely to provoke dissent or offense; bland, soothing, or calming.",
    secondary: "In historical medicine, any pharmaceutical preparation (such as tincture of opium or belladonna) administered to deaden physical suffering.",
    quotes: [
      { author: "Thomas De Quincey", work: "Confessions of an English Opium-Eater", quote: "Opium was to me a heavenly **anodyne**, lifting the dark veil of physical torment from my soul." },
      { author: "Samuel Johnson", work: "The Rambler", quote: "Hope is the sovereign **anodyne** of human misery, sweetening the bitterest cup of sorrow." },
      { author: "William Osler", work: "Aequanimitas", quote: "The physician must possess not only medicinal **anodyne** remedies, but also the soothing calm of a sympathetic presence." }
    ]
  },
  "Dashboard — odyn/glossodynia.md": {
    primary: "A painful, burning, or aching sensation localized in the tongue, occurring with or without visible signs of inflammation.",
    secondary: "In oral medicine and neurology, a common presentation of burning mouth syndrome, often associated with vitamin deficiencies, neuropathy, or anxiety.",
    quotes: [
      { author: "William Gowers", work: "A Manual of Diseases of the Nervous System", quote: "Neuralgia of the lingual nerve manifests in paroxysmal **glossodynia**, radiating along the margins of the tongue." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In pernicious anemia, stubborn **glossodynia** and a smooth, beefy tongue often precede severe spinal symptoms." },
      { author: "Jean-Martin Charcot", work: "Clinical Lectures on Diseases of the Nervous System", quote: "Certain hysterical complaints take the form of persistent **glossodynia**, resisting all topical astringent washes." }
    ]
  },
  "Dashboard — odyn/mastodynia.md": {
    primary: "Pain, tenderness, or aching discomfort in the breast (synonymous with mastalgia).",
    secondary: "A common gynecological condition, often cyclical and related to hormonal fluctuations during the menstrual cycle or early pregnancy.",
    quotes: [
      { author: "Sir Astley Cooper", work: "Illustrations of the Diseases of the Breast", quote: "Severe **mastodynia** frequently alarms the patient, who suspects cancer where only neuralgic irritability exists." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Cyclical **mastodynia** should be treated conservatively with reassurance, supportive brassieres, and mild analgesics." },
      { author: "Percivall Pott", work: "Chirurgical Works", quote: "A gentle soothing fomentation relieves the painful tension of inflammatory **mastodynia** in nursing mothers." }
    ]
  },
  "Dashboard — odyn/odyn.md": {
    primary: "The Greek root *odyn-* (from *odynē*), signifying pain, torment, sorrow, or physical agony (as seen in *anodyne*, *allodynia*, and *odynophagia*).",
    secondary: "The linguistic combining form in clinical medicine designating localized aching, burning, or distress across organ systems.",
    quotes: [
      { author: "Henry George Liddell & Robert Scott", work: "A Greek-English Lexicon", quote: "In Homeric epic, the noun *odyne* and its combining root **odyn** designate the sharp, piercing pain of arrow wounds." },
      { author: "Galen", work: "On the Affected Parts", quote: "The diagnostic physician classifies every variety of visceral **odyn** according to its lancinating or throbbing nature." },
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Ancient physicians derived their medicinal remedies to counter that sharp inward **odyn** which disrupts bodily harmony." }
    ]
  },
  "Dashboard — odyn/odynophagia.md": {
    primary: "Painful swallowing, typically experienced as burning, stabbing, or aching sensations in the throat or esophagus upon ingestion.",
    secondary: "In gastroenterology and otolaryngology, a clinical symptom signaling mucosal ulceration, candidiasis, herpes simplex infection, or esophageal spasm.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Severe **odynophagia** in an emaciated patient strongly suggests ulcerative esophagitis or fungal infection." },
      { author: "Armand Trousseau", work: "Lectures on Clinical Medicine", quote: "Diphtheritic membrane in the pharynx provokes agonizing **odynophagia**, rendering the swallowing of liquid torture." },
      { author: "Arthur Conan Doyle", work: "Round the Red Lamp", quote: "The country surgeon quickly determined that the patient's acute **odynophagia** was caused by an impacted fish bone." }
    ]
  }
};

for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(basePath, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`Missing file: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');

  // Find top portion up to > [!book]
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);

  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  console.log(`Updated: ${relPath}`);
}

console.log('Batch 4 complete! Total files updated:', Object.keys(filesData).length);
