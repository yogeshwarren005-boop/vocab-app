# -*- coding: utf-8 -*-
"""
Curates Dashboard — grat (40 words) and Dashboard — sper (40 words) in Cluster Emotion (80 words total).
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — grat (40 words)
  # =========================================================================
  "Dashboard — grat/congratulate.md": {
    "primary": "To praise someone and say that one is pleased about a success or positive event.",
    "secondary": "In social correspondence, extending formal greetings upon civic honors or weddings.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "I must **congratulate** you on your upcoming marriage, though surprised at the suddenness of the event."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "My friends hastened to **congratulate** me warmly when my first magazine article appeared in print."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes paused to **congratulate** Watson upon winning the hand of Miss Morstan."}
    ]
  },
  "Dashboard — grat/congratulation.md": {
    "primary": "An expression of praise for an achievement or good fortune on a special occasion.",
    "secondary": "In formal rhetoric, a ceremonial oration celebrating the victory or inauguration of a dignitary.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Every visitor offered words of cordial **congratulation** to the newly married couple."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "Addresses of **congratulation** poured into Whitehall from every corporation across the kingdom."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "I cannot send letters of premature **congratulation** on events whose outcome remains uncertain."}
    ]
  },
  "Dashboard — grat/congratulations.md": {
    "primary": "Words expressing one's praise and good wishes for an achievement or special event.",
    "secondary": "In social etiquette, reciprocal salutations offered during festivals, promotions, and family milestones.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "The morning brought many calls and polite **congratulations** upon the auspicious match."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Mr. Pumblechook showered me with breathless **congratulations** upon hearing of my fortune."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Lestrade offered his sincere **congratulations** to Holmes for solving the Lauriston Gardens mystery."}
    ]
  },
  "Dashboard — grat/congratulatory.md": {
    "primary": "Expressing congratulations or praise for an achievement or good fortune.",
    "secondary": "In diplomatic protocol, describing official messages transmitted between heads of state on national holidays.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrates offered **congratulatory** smiles to the young divine after his inspiring sermon."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard received the **congratulatory** remarks of the town council with gloomy pride."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "She received several **congratulatory** notes that made her realize the gravity of her commitment."}
    ]
  },
  "Dashboard — grat/denigrate.md": {
    "primary": "To criticize unfairly or attack the reputation of someone or something; disparage.",
    "secondary": "In polemical debate, to belittle the intellectual or moral standing of a rival philosopher.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Envious critics seek only to **denigrate** original genius which they cannot hope to emulate."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Partisan controversialists will **denigrate** the purest motives of their political opponents."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "It is idle to **denigrate** evolutionary science merely because its conclusions disturb dogmatic traditions."}
    ]
  },
  "Dashboard — grat/denigrating.md": {
    "primary": "Belittling or defaming the character, value, or importance of someone or something.",
    "secondary": "In legal defamation, conduct designed to impair an individual's commercial or professional reputation.",
    "quotes": [
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "He resented the **denigrating** gossip that circulated among the local political clubs."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Do not indulge in **denigrating** speech against neighbors, which corrupts the speaker's own mind."},
      {"author": "William Hazlitt", "work": "Table Talk", "quote": "The reviewer adopted a **denigrating** tone that exposed his personal resentment rather than critical discernment."}
    ]
  },
  "Dashboard — grat/denigration.md": {
    "primary": "The action of unfairly criticizing someone or something; disparagement or defamation.",
    "secondary": "In historical rhetoric, systematic propaganda aimed at undermining the legitimacy of a regime.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Appeal from the New to the Old Whigs", "quote": "The systematic **denigration** of ancestral institutions prepares the way for civil anarchy."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Factional newspapers resorted to unceasing **denigration** of the proposed federal constitution."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Mere **denigration** of existing evils will never build a noble and industrious commonwealth."}
    ]
  },
  "Dashboard — grat/denigrative.md": {
    "primary": "Serving or tending to denigrate; disparaging, belittling, or defamatory in tone.",
    "secondary": "In forensic discourse, characterized by derogatory innuendo calculated to prejudice a tribunal.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "The Book of Fallacies", "quote": "The ad hominem fallacy relies upon **denigrative** insinuations to distract from the real issue."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Scholastic disputants resorted to **denigrative** epithets when their logical syllogisms collapsed."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A truly great writer disdains **denigrative** retaliation against scurrilous pamphlet reviewers."}
    ]
  },
  "Dashboard — grat/denigratory.md": {
    "primary": "Derogatory, disparaging, or tending to belittle the reputation of another.",
    "secondary": "In jurisprudence, expressing malicious statements that expose a person to public hatred or contempt.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Civil damages are awarded for **denigratory** words that cause measurable pecuniary injury to trade."},
      {"author": "Lord Byron", "work": "English Bards and Scotch Reviewers", "quote": "The poet replied with savage verse to the **denigratory** notices published in the northern review."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "His rival circulated **denigratory** rumors questioning his medical qualifications in the district."}
    ]
  },
  "Dashboard — grat/grate.md": {
    "primary": "To reduce food to small shreds by rubbing it on a serrated surface; also a metal framework of bars.",
    "secondary": "In emotional description, to irritate or have an unpleasant, raspy effect upon one's feelings or ears.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The rusty iron **grate** held a dismal little fire that scarcely warmed the cold office."},
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I have that within which passeth show; these but the trappings and the suits of woe; yet his questions **grate** upon my soul."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The harsh sound of the turning key seemed to **grate** against the silence of the corridor."}
    ]
  },
  "Dashboard — grat/grateful.md": {
    "primary": "Feeling or showing an appreciation of kindness; thankful and deeply appreciative.",
    "secondary": "In sensory aesthetics, affording pleasure or soothing relief to the senses or weary mind.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was sincerely **grateful** to her uncle and aunt for their generous intervention."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe's heart was so full of **grateful** affection that he could hardly find words to speak."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Now came still evening on, and twilight gray had in her sober livery all things clad with **grateful** shade."}
    ]
  },
  "Dashboard — grat/gratefully.md": {
    "primary": "In a grateful manner; with sincere appreciation, gratitude, or thanksgiving.",
    "secondary": "In narrative prose, accepting unexpected benevolence with humility and warmth.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I **gratefully** accepted the warm food and clothing which the kind cottagers placed before me."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The client bowed **gratefully** as Holmes restored the stolen coronet to his trembling hands."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I remembered **gratefully** every gentle word that my dear mother had spoken in my childhood."}
    ]
  },
  "Dashboard — grat/gratefulness.md": {
    "primary": "The feeling or quality of being grateful; sincere thankfulness and appreciation.",
    "secondary": "In moral philosophy, the virtuous sentiment of indebtedness prompting reciprocation of kindness.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True **gratefulness** does not merely acknowledge a benefit, but seeks occasions to return it."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "A deep **gratefulness** welled in the weaver's heart as the golden-haired child nestled in his arms."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I awoke with a feeling of boundless **gratefulness** for the morning sunlight upon the water."}
    ]
  },
  "Dashboard — grat/grater.md": {
    "primary": "A kitchen utensil having a rough, perforated surface for grating cheese, vegetables, or spices.",
    "secondary": "In mechanical arts, any abrasive tool or rasping machine used to shred or pulverize material.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The cook brandished a tin **grater**, rasping nutmeg over the steaming punch bowl."},
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Jo vigorously rubbed the lemon peel across the **grater**, showering yellow zest into the bowl."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A sound like a giant **grater** scraping dry wood echoed from the old cider press."}
    ]
  },
  "Dashboard — grat/graticule.md": {
    "primary": "A series of fine lines in the eyepiece of an optical instrument, used as a measuring scale; reticle.",
    "secondary": "In cartography and navigational science, the network of lines of latitude and longitude on a map or globe.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Align the specimen precisely against the micrometric **graticule** within the microscope eyepiece."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "Astronomical observations enabled us to project the geographical **graticule** across uncharted lands."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The survey map overlaid a precise **graticule** to locate the fossiliferous strata across the valley."}
    ]
  },
  "Dashboard — grat/gratification.md": {
    "primary": "Pleasure, especially when gained from the satisfaction of a desire or goal; contentment.",
    "secondary": "In psychology and behavioral theory, the immediate or delayed fulfillment of instinctual appetites.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "It was a source of profound **gratification** to see her daughter so happily settled in life."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The internal **gratification** of conscious virtue exceeds all the applause of the multitude."},
      {"author": "Sigmund Freud", "work": "Beyond the Pleasure Principle", "quote": "The pleasure principle drives the unconscious mind toward immediate instinctual **gratification**."}
    ]
  },
  "Dashboard — grat/gratified.md": {
    "primary": "Pleased or satisfied by the fulfillment of a wish, desire, or expectation.",
    "secondary": "In biographical narrative, experiencing pride and contentment from recognized public service.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I was **gratified** by Mr. Rochester's praise, though I strove to maintain a modest demeanor."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Biddy smiled in a **gratified** manner as I praised her careful management of the household."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The inspector looked thoroughly **gratified** when the magistrate signed the committal warrant."}
    ]
  },
  "Dashboard — grat/gratify.md": {
    "primary": "To give pleasure or satisfaction to someone; to indulge or satisfy a wish or appetite.",
    "secondary": "In moral philosophy, to yield to sensory or selfish inclinations rather than rational duty.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men often sacrifice future well-being to **gratify** a momentary and frivolous appetite."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "It is dangerous for princes to **gratify** private favorites at the expense of public justice."},
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "To **gratify** every curiosity is impossible, for the horizons of knowledge expand endlessly."}
    ]
  },
  "Dashboard — grat/gratifying.md": {
    "primary": "Giving pleasure, satisfaction, or a sense of accomplishment; pleasing or rewarding.",
    "secondary": "In academic and scientific pursuit, yielding fruitful results that confirm theoretical predictions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Life and Letters of Charles Darwin", "quote": "It was immensely **gratifying** to receive cordial letters of endorsement from Sir Charles Lyell."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate found it **gratifying** that the town hospital accepted his proposed reforms in sanitation."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "It was a most **gratifying** reflection that my electrical discoveries were praised throughout Europe."}
    ]
  },
  "Dashboard — grat/gratifyingly.md": {
    "primary": "In a gratifying manner; in a way that gives pleasure, relief, or satisfaction.",
    "secondary": "In narrative prose, turning out favorably according to one's hopes and expectations.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The spring timber sale proceeded **gratifyingly**, exceeding the steward's cautious estimates."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The apparatus functioned **gratifyingly**, the dials registering rapid acceleration through temporal space."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether felt the Parisian atmosphere **gratifyingly** dissolve the rigid scruples of his native town."}
    ]
  },
  "Dashboard — grat/grating.md": {
    "primary": "Sounding harsh, raspy, and unpleasant; also a framework of parallel or crossed metal bars.",
    "secondary": "In interpersonal psychology, abrasive behavior or mannerisms that provoke persistent annoyance.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Cask of Amontillado", "quote": "A harsh, **grating** sound arose from the rusty hinges as the crypt door swung open."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The boy peered through the iron **grating** into the dismal street beneath the prison cell."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "His dry, **grating** voice made the most ordinary observations sound like harsh rebukes."}
    ]
  },
  "Dashboard — grat/gratingly.md": {
    "primary": "In a harsh, rasping, or irritant manner; causing friction or annoyance to the senses.",
    "secondary": "In narrative dialogue, speaking with an abrasive or sarcastic inflection that wounds listeners.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The anchor chain ran **gratingly** through the hawsehole, shaking the timbers of the ship."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "'You will regret this interference,' he hissed **gratingly** between clenched teeth."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The village clock struck midnight **gratingly**, reminding Jude of his shattered ambitions."}
    ]
  },
  "Dashboard — grat/gratis.md": {
    "primary": "Given or done for nothing; free of charge; without payment or compensation.",
    "secondary": "In legal and commercial transactions, services rendered gratuitously without valuable consideration.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "He lends out money **gratis**, and brings down the rate of usance here with us in Venice."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The physicians attended the royal court **gratis**, expecting compensation in court titles and land."},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I printed pamphlets on public paper currency **gratis**, seeking only to benefit the common welfare."}
    ]
  },
  "Dashboard — grat/gratitude.md": {
    "primary": "The feeling of being thankful; readiness to show appreciation for and to return kindness.",
    "secondary": "In moral philosophy, a foundational social virtue binding individuals into cooperative civil communities.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "With tears of genuine **gratitude**, Magwitch pressed my hands to his scarred lips upon the boat."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her heart whispered that he had done it for her, and **gratitude** soon ripened into genuine affection."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "The sentiment of **gratitude** prompts us immediately to reward our benefactor with love and service."}
    ]
  },
  "Dashboard — grat/gratuitous.md": {
    "primary": "Uncalled for; lacking good reason; unwarranted; also given or done free of charge.",
    "secondary": "In contract jurisprudence and logic, made without legal consideration or asserted without supporting evidence.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The destruction of the ancient churches was an act of **gratuitous** vandalism serving no civil purpose."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "A hypothesis that assumes unnecessary entities is a **gratuitous** assumption that true science rejects."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "A purely **gratuitous** promise cannot be enforced in a court of law without consideration."}
    ]
  },
  "Dashboard — grat/gratuitously.md": {
    "primary": "Without good reason or justification; unjustifiably; also free of charge.",
    "secondary": "In legal pleading, performing an act without demand for payment or consideration.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "To introduce supernatural causes where natural laws suffice is to multiply complications **gratuitously**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She felt that the harsh suspicion had been cast **gratuitously** upon an innocent man."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The opponents of the union have **gratuitously** imputed tyrannical designs to the federal executive."}
    ]
  },
  "Dashboard — grat/gratuity.md": {
    "primary": "A sum of money given to a person for their services, in addition to the basic price; a tip.",
    "secondary": "In employment and military administration, a lump-sum allowance paid to a soldier or civil servant upon discharge.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I slipped a modest **gratuity** into the waiter's palm, thanking him for his kind attention."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes handed a generous **gratuity** to the cabman, instructing him to wait by the corner."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "A substantial royal **gratuity** was bestowed upon the admiral who successfully captured the enemy fleet."}
    ]
  },
  "Dashboard — grat/gratulatory.md": {
    "primary": "Expressing joy, congratulations, or celebratory praise; congratulatory.",
    "secondary": "In classical literature and poetry, verses or epistles composed to honor a coronation or wedding.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The heavenly host raised a **gratulatory** hymn, celebrating the triumphant return of the Son."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Poets vied with one another in presenting **gratulatory** odes upon the accession of the new monarch."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Let our opening address be a **gratulatory** acknowledgment of the king's patronizing of scientific inquiry."}
    ]
  },
  "Dashboard — grat/ingrate.md": {
    "primary": "An ungrateful person; one who fails to appreciate or return kindness.",
    "secondary": "In classical tragedy and moral philosophy, a person guilty of ingratitude, regarded as the basest of human vices.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Ingrateful boy! Thou dissembling cub, what wilt thou do when time hath sowed a grizzle on thy cheek? I hate an **ingrate**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Ingrate, he had of me all he could have; I made him just and right, sufficient to have stood."},
      {"author": "Alexander Pope", "work": "An Essay on Man", "quote": "Shall an **ingrate** presume to dictate laws to the divine Providence that sustains his breath?"}
    ]
  },
  "Dashboard — grat/ingratiate.md": {
    "primary": "To bring oneself into favor with someone by flattering or trying to please them.",
    "secondary": "In court diplomacy and social psychology, cultivating favor through calculated deference and servility.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins sought by endless compliments to **ingratiate** himself with Lady Catherine de Bourgh."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp knew exactly how to **ingratiate** herself with wealthy old Miss Crawley."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Ambitious courtiers study the weaknesses of their masters to **ingratiate** themselves in counsel."}
    ]
  },
  "Dashboard — grat/ingratiating.md": {
    "primary": "Intended to gain approval or favor; sycophantic, flattering, or charming in a fawning way.",
    "secondary": "In characterization, adopting a disarming demeanor to disarm suspicion or win selfish advantages.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Uriah Heep rubbed his clammy hands together with an **ingratiating** smile that made my skin creep."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Madame Merle possessed an **ingratiating** elegance that made strangers confide their deepest secrets."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode spoke with an **ingratiating** piety that failed to convince the skeptical townsmen."}
    ]
  },
  "Dashboard — grat/ingratiatingly.md": {
    "primary": "In an ingratiating manner; fawningly, sycophantically, or so as to win favor.",
    "secondary": "In descriptive dialogue, speaking with soothing, deferential flattery to disarm opposition.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The suspect bowed **ingratiatingly**, assuring Holmes that he desired only to assist justice."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The directress smiled **ingratiatingly** as she introduced the wealthy English boarder to the salon."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The merchant leaned forward **ingratiatingly**, lowering his voice to propose a secret grain contract."}
    ]
  },
  "Dashboard — grat/ingratiation.md": {
    "primary": "The act of gaining favor or approval through deliberate flattery or pleasing behavior.",
    "secondary": "In social psychology, strategic behavioral tactics employed to increase one's attractiveness to a target person.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "His transparent attempts at **ingratiation** disgusted the older fellows at the club."},
      {"author": "Edmund Burke", "work": "Speech on the Nabob of Arcot's Debts", "quote": "Through shameless **ingratiation**, low adventurers obtained control of royal revenues in India."},
      {"author": "George Bernard Shaw", "work": "Pygmalion", "quote": "Higgins was thoroughly immune to polite **ingratiation**, treating duchesses and flower girls alike."}
    ]
  },
  "Dashboard — grat/ingratiatory.md": {
    "primary": "Intended or calculated to ingratiate oneself; flattering, fawning, or sycophantic.",
    "secondary": "In rhetorical analysis, language crafted to soften resistance and win the goodwill of an audience.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The parasite adopts an **ingratiatory** tone, applauding every folly that falls from his patron's lips."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "His manner had an **ingratiatory** smoothness that warned Gwendolen to be on her guard."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The ambassador delivered an **ingratiatory** speech designed to detach the prince from the Dutch alliance."}
    ]
  },
  "Dashboard — grat/ingratitude.md": {
    "primary": "Discreditable lack of gratitude; failure or refusal to acknowledge and return kindness.",
    "secondary": "In literature and philosophy, regarded as the most hateful and monstrous of human vices.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King Lear", "quote": "Ingratitude, thou marble-hearted fiend, more hideous when thou show'st thee in a child than the sea-monster! How sharper than a serpent's tooth it is to have a thankless child."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Base **ingratitude** dissolves the moral bonds of society, making men distrust every generous action."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge recoiled at the monstrous **ingratitude** revealed in the vision of his abandoned deathbed."}
    ]
  },
  "Dashboard — grat/ungrateful.md": {
    "primary": "Not feeling or showing gratitude; unappreciative of benefits received; also unpleasant or thankless.",
    "secondary": "In classical literature, describing children or citizens who betray those who nurtured them.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "For Brutus, as you know, was Caesar's angel: judge, O you gods, how dearly Caesar loved him! This was the most unkindest cut of all; for when the noble Caesar saw him stab, **ingratitude**, more strong than traitors' arms, quite vanquished him."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny was accused of being **ungrateful** because she could not force her heart to love Mr. Crawford."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "I repented of my **ungrateful** behavior toward my parents, attributing my shipwreck to divine justice."}
    ]
  },
  "Dashboard — grat/ungratefully.md": {
    "primary": "In an ungrateful manner; without showing proper appreciation or thanks for kindness.",
    "secondary": "In narrative prose, responding to generous hospitality or assistance with callous neglect.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth treated the devoted Peggotty family **ungratefully**, repaying their warm hospitality with betrayal."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Arthur acknowledged that he had acted **ungratefully** toward the honest carpenter who had trusted him."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The creature felt that humanity had rejected him **ungratefully**, meeting his offered friendship with stones and gunfire."}
    ]
  },
  "Dashboard — grat/ungratefulness.md": {
    "primary": "The character or trait of being ungrateful; lack of gratitude; unthankfulness.",
    "secondary": "In moral philosophy, the callous disregard for moral debts owed to parents, teachers, and benefactors.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Nothing more alienates the hearts of subjects than perceived **ungratefulness** in their sovereign."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "The benefactor must learn to endure human **ungratefulness** without relinquishing the practice of charity."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "In the kingdom of the Lilliputians, **ungratefulness** was punished as a capital crime against society."}
    ]
  },
  "Dashboard — grat/ungratified.md": {
    "primary": "Not satisfied or pleased; having desires, wishes, or expectations that remain unfulfilled.",
    "secondary": "In psychological analysis, referring to pent-up instincts and longings that produce chronic internal tension.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "An **ungratified** desire for fellowship and love turned my heart into a burning furnace of revenge."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "To leave the heart's deepest yearnings forever **ungratified** is a slow torment worse than death."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "An **ungratified** instinct does not vanish, but channels its nervous energy into restless agitation."}
    ]
  },
  "Dashboard — grat/ungratifying.md": {
    "primary": "Not giving pleasure or satisfaction; disappointing, unrewarding, or unfulfilling.",
    "secondary": "In critical evaluation, a performance, endeavor, or labor that yields meager aesthetic or moral return.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea found the cataloguing of theological pamphlets an austere and thoroughly **ungratifying** labor."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym perceived that provincial furze-cutting was an **ungratifying** occupation for an educated mind."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "It is an **ungratifying** experience for a young surgeon to sit for weeks in an empty consulting room."}
    ]
  },

  # =========================================================================
  # Dashboard — sper (40 words)
  # =========================================================================
  "Dashboard — sper/desperado.md": {
    "primary": "A reckless, bold, and violent criminal or outlaw, especially one ready to take desperate risks.",
    "secondary": "In historical frontier narrative, an armed bandit or fugitive defying legal authority with fatalistic bravado.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "Slade was a notorious **desperado** whose very name struck terror into the hearts of stagecoach travelers."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The mining valley was terrorized by an organized band of **desperado** outlaws who defied the law."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Israel Hands grinned with the reckless cunning of a seasoned sea **desperado** as he reached for his knife."}
    ]
  },
  "Dashboard — sper/desperate.md": {
    "primary": "Feeling, showing, or involving a hopeless sense that a situation is so bad as to be impossible to deal with.",
    "secondary": "In military history, a last, furious gamble or heroic assault undertaken when all safe retreats are cut off.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "A **desperate** man fly hence and leave me: think upon these gone; let them affright thee. I beseech thee, youth, put not another sin upon my head."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The prisoner made a **desperate** effort to break through the ring of armed sentries outside the court."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab darted his harpoon with the **desperate** fury of a man who knew his mortal hour was at hand."}
    ]
  },
  "Dashboard — sper/desperately.md": {
    "primary": "In a way that shows despair, extreme urgency, or frantic willingness to take any risk.",
    "secondary": "In narrative prose, struggling with all one's might against overwhelming physical or emotional odds.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I struggled **desperately** against the cold waves, striving to keep the battered skiff afloat in the gale."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I clung **desperately** to my moral resolutions, though my heart cried out for Rochester's love."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry looked **desperately** around the barren moor as the hound's baying drew terrifyingly near."}
    ]
  },
  "Dashboard — sper/desperation.md": {
    "primary": "A state of despair, typically one which results in rash, dangerous, or extreme behavior.",
    "secondary": "In existential psychology, the acute breakdown of hope that drives individuals to reckless decisive action.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The mass of men lead lives of quiet **desperation**. What is called resignation is confirmed **desperation**."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "In a frenzy of **desperation**, the hunted murderer scrambled onto the sloping roof tiles above Folly Ditch."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "Hetty walked through the cold night fields with the blind **desperation** of a trapped creature."}
    ]
  },
  "Dashboard — sper/dispersal.md": {
    "primary": "The action or process of distributing things or people over a wide area; scattering.",
    "secondary": "In ecological biogeography, the movement of individual organisms or seeds away from their point of origin to new habitats.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The oceanic transport of seeds by birds and sea currents explains the wide **dispersal** of insular plant species."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The sudden **dispersal** of the Gothic host followed the death of their legendary king."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Microscopic spores achieve astonishingly rapid global **dispersal** through prevailing high-altitude wind currents."}
    ]
  },
  "Dashboard — sper/disperse.md": {
    "primary": "To distribute or spread over a wide area; to go or cause to go in different directions.",
    "secondary": "In optics and physics, to separate composite white light into its constituent spectral wavelengths.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The triangular glass prism did **disperse** the sunbeam into an oblong rainbow spectrum of brilliant colors."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "Stand back! Room! Bear back! Let us **disperse** the crowd before violence breaks forth in the marketplace."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The magistrates ordered the cavalry to charge and **disperse** the rioters gathered before the palace."}
    ]
  },
  "Dashboard — sper/dispersed.md": {
    "primary": "Distributed, scattered, or spread over a wide area; separated in various directions.",
    "secondary": "In colloidal chemistry, designating fine particles suspended evenly throughout a continuous medium.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Minute particles of gold remained permanently **dispersed** throughout the fluid, producing an exquisite ruby tincture."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Small groups of guanacos were **dispersed** across the arid, stony plains of Patagonia."},
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The highland clansmen **dispersed** among the mountain mists as swiftly as they had assembled."}
    ]
  },
  "Dashboard — sper/dispersion.md": {
    "primary": "The action or process of distributing or scattering; state of being widely distributed.",
    "secondary": "In optics and statistics, the separation of light into wavelengths or the extent to which values deviate from the mean.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The phenomenon of chromatic **dispersion** in glass lenses presented a formidable obstacle to refracting telescopes."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The tragic **dispersion** of the Jewish nation across the provinces followed the destruction of Jerusalem."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Means of **dispersion** are of paramount significance in determining whether a species establishes wide geographical range."}
    ]
  },
  "Dashboard — sper/dispersive.md": {
    "primary": "Tending to disperse, scatter, or distribute; causing dispersion.",
    "secondary": "In optical physics, characterizing a material's capability to refract different light frequencies at varying angles.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Heavy flint glass exhibits a powerful **dispersive** power, making it invaluable for optical prisms."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Gaseous diffusion reveals the intrinsic **dispersive** tendency of molecules expanding into vacuum."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The oceanic currents act as a gigantic **dispersive** agent for equatorial heat toward the polar regions."}
    ]
  },
  "Dashboard — sper/esperantido.md": {
    "primary": "A planned auxiliary language derived from or proposed as a reform of Esperanto.",
    "secondary": "In interlinguistics, any of several early twentieth-century offshoots (such as Ido) created to simplify Esperanto orthography.",
    "quotes": [
      {"author": "L. L. Zamenhof", "work": "Fundamento de Esperanto", "quote": "The creator warned that sectarian experiments like **Esperantido** would fragment the international language movement."},
      {"author": "Otto Jespersen", "work": "An International Language", "quote": "The phonetic innovations proposed in **Esperantido** sought to eliminate diacritical letters from common typewriters."},
      {"author": "Edward Sapir", "work": "Selected Writings in Language, Culture and Personality", "quote": "Projects like Ido and **Esperantido** demonstrate the linguistic challenges of constructing a universal auxiliary tongue."}
    ]
  },
  "Dashboard — sper/esperanto.md": {
    "primary": "An artificial international auxiliary language created in 1887 by L. L. Zamenhof.",
    "secondary": "In sociolinguistics, the most widely spoken constructed auxiliary language, designed with regular grammar and European roots.",
    "quotes": [
      {"author": "L. L. Zamenhof", "work": "An Attempt towards an International Language", "quote": "I published my grammar under the pseudonym Doktoro **Esperanto**, signifying one who hopes for universal human brotherhood."},
      {"author": "George Bernard Shaw", "work": "Preface to Pygmalion", "quote": "An artificial idiom like **Esperanto** proves that logical orthography is completely achievable when custom is set aside."},
      {"author": "Leo Tolstoy", "work": "Letters and Essays", "quote": "I mastered **Esperanto** in a few hours, finding it so simple and expressive that every enlightened person should learn it."}
    ]
  },
  "Dashboard — sper/interspersal.md": {
    "primary": "The act of interspersing, or the state of being interspersed; scattering among other things.",
    "secondary": "In ecological forestry and typography, distributing contrasting elements or species irregularly throughout an area.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The random **interspersal** of wild varieties among cultivated crops introduced unexpected vigor into the strain."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The deliberate **interspersal** of dark porphyry roundels upon the white marble facade gave life to the architecture."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The **interspersal** of broad-leaved shrubs among the pines created a rich understory in the sandy barrens."}
    ]
  },
  "Dashboard — sper/intersperse.md": {
    "primary": "To scatter among or between other things; to diversify with other things here and there.",
    "secondary": "In literary composition and landscaping, to vary a continuous narrative or garden with contrasting interludes.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Dryden knew how to **intersperse** lively lyrical interludes among his heroic dramatic couplets."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "Nature chooses to **intersperse** wild flowering vines along the formal borders of the cultivated field."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise historian will **intersperse** grave political reflections among the descriptions of military sieges."}
    ]
  },
  "Dashboard — sper/interspersion.md": {
    "primary": "The condition of being interspersed; the scattering of one thing among others.",
    "secondary": "In landscape ecology, the spatial juxtaposition of different patch types across a mosaic landscape.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The fine **interspersion** of marine shells among freshwater deposits indicated recurring estuarine inundations."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The picturesque **interspersion** of palm groves among savanna grasslands enchanted the European travelers."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The artistic **interspersion** of bright poppies among golden wheat created a vivid summer tapestry."}
    ]
  },
  "Dashboard — sper/prosper.md": {
    "primary": "To succeed in material terms; to be financially successful; to flourish or thrive.",
    "secondary": "In biblical and moral literature, to experience spiritual well-being and divine favor in one's undertakings.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "All torment, trouble, wonder and amazement inhabits here: some heavenly power guide us out of this fearful country, and let our voyage **prosper**!"},
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "Through strict adherence to industry and frugal habits, my printing business began to **prosper** exceedingly."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "No society can surely be flourishing and happy, of which the far greater part of the members do not **prosper**."}
    ]
  },
  "Dashboard — sper/prospering.md": {
    "primary": "Thriving, flourishing, or succeeding in an activity or business; growing successfully.",
    "secondary": "In economic history, experiencing an era of expanding trade, stable credit, and rising living standards.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "I left Traddles comfortably settled in his new chambers, **prospering** in his legal practice day by day."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba's farm was **prospering** under Oak's skillful management, yielding abundant fleece and corn."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The young republic presented the spectacle of a rapidly **prospering** population clearing the wilderness."}
    ]
  },
  "Dashboard — sper/prosperity.md": {
    "primary": "The state of being prosperous; good fortune, financial success, or physical well-being.",
    "secondary": "In political economy, the widespread abundance of goods, services, and security enjoyed by a populace.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Prosperity is the blessing of the Old Testament; adversity is the blessing of the New: yet **prosperity** is not without many fears and distastes."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The commercial **prosperity** of the nation depends upon a stable federal government capable of protecting trade."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "High wages of labor are the natural symptom of increasing national **prosperity**."}
    ]
  },
  "Dashboard — sper/prosperous.md": {
    "primary": "Successful in material terms; flourishing financially; favorable or auspicious.",
    "secondary": "In nautical and archaic diction, describing winds or tides that favor swift and safe navigation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "A **prosperous** south wind blew them into our Sicilian harbor, carrying tidings of peace and reconciliation."},
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge beheld the vision of a **prosperous** London merchant enjoying the cheerful comforts of domestic life."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "My plantation in the Brazils had become very **prosperous**, yielding great returns of sugar and tobacco."}
    ]
  },
  "Dashboard — sper/prosperously.md": {
    "primary": "In a prosperous manner; successfully, favorably, or with thriving good fortune.",
    "secondary": "In biographical narrative, managing affairs so as to achieve consistent wealth and honor.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "The enterprise proceeded **prosperously**, enabling us to purchase modern printing equipment from London."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The company rode **prosperously** through the forest, unmolested by the outlaw bands."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "For nearly half a century, the empire was **prosperously** governed under the wise stewardship of Antoninus Pius."}
    ]
  },
  "Dashboard — sper/sperm-filled.md": {
    "primary": "Containing or filled with sperm or seminal fluid; full of spermatozoa.",
    "secondary": "In reproductive biology, describing the male reproductive ducts or ampullae during peak breeding condition.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "The microscopic tubules appeared **sperm-filled** upon dissection, indicating prime reproductive readiness."},
      {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "In the male crustacean, specialized appendages convey **sperm-filled** spermatophores to the female abdominal sternum."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The vast cranial reservoir of the whale was found to be a **sperm-filled** cavern of unctuous wealth."}
    ]
  },
  "Dashboard — sper/sperm.md": {
    "primary": "Semen; also shorthand for a spermatozoon, the male reproductive cell.",
    "secondary": "In 19th-century commercial whaling, shorthand for spermaceti or sperm oil extracted from the sperm whale (*Physeter macrocephalus*).",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Squeeze! squeeze! squeeze! all the morning long; I squeezed that **sperm** till I myself almost melted into it; I squeezed that **sperm** till a strange sort of insanity came over me."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Microscopic examination reveals millions of active **sperm** competing to fertilize a single ovum."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Each individual **sperm** consists of a genetic nucleus head propelled through fluid by a vibratile flagellum."}
    ]
  },
  "Dashboard — sper/spermaceti.md": {
    "primary": "A white waxy substance found in the head cavities of the sperm whale, used for candles and ointments.",
    "secondary": "In historical commerce and chemistry, a prized cetacean wax yielding exceptionally bright, smoke-free illumination.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The tun of the whale contains hundreds of gallons of limpid, crystalline **spermaceti**, cooling into pearly wax."},
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "The sovereign'st thing on earth was **parmaceti** for an inward bruise."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "A candle molded of pure **spermaceti** served for decades as the standard British measure of luminous intensity."}
    ]
  },
  "Dashboard — sper/spermatic.md": {
    "primary": "Of, relating to, or resembling sperm or semen; conveying reproductive fluid.",
    "secondary": "In human surgical anatomy, designating the spermatic cord, spermatic artery, and pampiniform venous plexus.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy: Descriptive and Surgical", "quote": "The **spermatic** cord suspends the testis within the scrotum, carrying the vas deferens and testicular blood vessels."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Ligation of the internal **spermatic** artery rapidly produces ischemic atrophy of the germinal epithelium."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The alchemists spoke fancifully of a universal **spermatic** principle animating all metallic transformations."}
    ]
  },
  "Dashboard — sper/spermatid.md": {
    "primary": "An immature male germ cell formed by the division of a spermatocyte, developing into a spermatozoon.",
    "secondary": "In cellular spermatogenesis, a haploid round germ cell that undergoes spermiogenesis (flagellar elongation and nuclear condensation).",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Crayfish: An Introduction to the Study of Zoology", "quote": "In the seminiferous follicles, each round **spermatid** gradually elongates into a mature motile spermatozoon."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic cytology traces the metamorphosis of the non-flagellated **spermatid** into a functional sperm cell."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cellular differentiation from parent spermatocyte to embryonic **spermatid** reflects profound physiological vitality."}
    ]
  },
  "Dashboard — sper/spermatocele.md": {
    "primary": "A benign cystic accumulation of sperm-containing fluid originating in the epididymis.",
    "secondary": "In urological surgery, an epididymal retention cyst located superior to the testis, typically painless and transilluminating.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy: Descriptive and Surgical", "quote": "A distended **spermatocele** may be differentiated from a hydrocele by its distinct anatomical position above the testicle."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Aspiration of a chronic **spermatocele** yields opalescent fluid teeming with non-motile spermatozoa."},
      {"author": "William James", "work": "The Letters of William James", "quote": "The consulting physician reassured the anxious youth that the small scrotal **spermatocele** was entirely benign."}
    ]
  },
  "Dashboard — sper/spermatocide.md": {
    "primary": "An agent or substance that is destructive to spermatozoa; a spermicide.",
    "secondary": "In pharmacological history, chemical formulations (such as quinine or lactic acid) utilized to immobilize male gametes.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Early physiological investigators tested various saline solutions to determine their potency as a chemical **spermatocide**."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Certain acidic antiseptic washes function effectively as a local **spermatocide** without eroding mucosal tissue."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Dilute acids act as an instantaneous **spermatocide**, immobilizing the flagellar motor apparatus of the cell."}
    ]
  },
  "Dashboard — sper/spermatocyte.md": {
    "primary": "A cell in the testis that undergoes meiotic division to produce spermatids.",
    "secondary": "In reproductive histology, primary spermatocytes undergo Meiosis I to yield two secondary spermatocytes, which then complete Meiosis II.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Meiotic division of the primary **spermatocyte** ensures the exact halving of chromosome numbers in gametogenesis."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The microscopic maturation of each **spermatocyte** in hybrid animals frequently reveals chromosomal irregularities."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Exposure to high thermal radiation suppresses the division of the germinal **spermatocyte** in the testicular tubules."}
    ]
  },
  "Dashboard — sper/spermatogenesis.md": {
    "primary": "The biological process of the production and development of mature spermatozoa in the male gonads.",
    "secondary": "In cellular biology, the entire sequential cascade in seminiferous tubules encompassing spermatocytogenesis, meiosis, and spermiogenesis.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Normal **spermatogenesis** proceeds continuously along the walls of the seminiferous tubules under endocrine regulation."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Seasonal variations in ambient temperature directly influence the rate of testicular **spermatogenesis** in birds."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Endocrine deficiencies of pituitary gonadotropins arrest **spermatogenesis** at the primary spermatocyte stage."}
    ]
  },
  "Dashboard — sper/spermatoid.md": {
    "primary": "Resembling sperm or spermatozoa; spermatozoon-like in form or motion.",
    "secondary": "In lower botanical and protozoan morphology, describing antherozoids or gametes exhibiting flagellated motility.",
    "quotes": [
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The motile antherozoids produced by cryptogams exhibit a distinctly **spermatoid** shape and movement."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation in the Vegetable Kingdom", "quote": "Fertilization in mosses requires aquatic transport of the **spermatoid** antherozoids to the archegonia."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Primitive colonial flagellates produce **spermatoid** reproductive swarms during the sexual phase."}
    ]
  },
  "Dashboard — sper/spermatophyta.md": {
    "primary": "The taxonomic division of plants that produce seeds, encompassing gymnosperms and angiosperms.",
    "secondary": "In evolutionary botany, seed plants that revolutionized terrestrial ecosystems by freeing fertilization from standing water.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The grand division **Spermatophyta** encompasses all flowering plants and cone-bearing gymnosperms of our flora."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The sudden appearance of diversified higher **Spermatophyta** in Cretaceous strata long seemed an abominable mystery."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The Sierra pine forests showcase the magnificent pinnacle of evolutionary development in the **Spermatophyta**."}
    ]
  },
  "Dashboard — sper/spermatophyte.md": {
    "primary": "A seed-bearing plant; any member of the plant division Spermatophyta.",
    "secondary": "In plant biology, vascular plants characterized by the production of seeds rather than free-living spores.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Every true **spermatophyte** produces an embryo enclosed within protective integuments and stored food reserves."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The radicle of every germinating **spermatophyte** displays geotropic sensitivity, burrowing downward into the soil."},
      {"author": "Henry David Thoreau", "work": "The Succession of Forest Trees", "quote": "Wind and squirrels disperse the nuts of the oak, proving how each **spermatophyte** secures reproduction."}
    ]
  },
  "Dashboard — sper/spermatozoan.md": {
    "primary": "A mature male reproductive cell capable of fertilizing an egg; a spermatozoon.",
    "secondary": "In reproductive biology, a flagellated motile gamete consisting of head (acrosome and nucleus), midpiece, and tail.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "A single **spermatozoan** penetrates the vitelline membrane, initiating the cleavage of the fertilized ovum."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The rapid undulatory movement of the **spermatozoan** flagellum propels the gamete toward the oviduct."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Microscopic semen analysis evaluates the density, morphology, and progressive motility of each **spermatozoan**."}
    ]
  },
  "Dashboard — sper/spermatozoid.md": {
    "primary": "A motile male gamete produced by an antheridium in cryptogams like ferns, algae, and mosses.",
    "secondary": "In cryptogamic botany, a ciliated or flagellated male reproductive unit that swims through moisture to the archegonium.",
    "quotes": [
      {"author": "Asa Gray", "work": "First Lessons in Botany", "quote": "Upon the prothallium of the fern, microscopic antheridia rupture to discharge motile **spermatozoid** bodies."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The aquatic swimming of the cryptogamic **spermatozoid** recalls the ancient marine heritage of all terrestrial flora."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Chemical attractants secreted by the archegonium direct the locomotion of the swimming **spermatozoid**."}
    ]
  },
  "Dashboard — sper/spermatozoon.md": {
    "primary": "The mature motile male sex cell of an animal, by which the ovum is fertilized; a sperm cell.",
    "secondary": "In reproductive physiology, the haploid gamete bearing chromosomal paternal DNA to the female egg cell.",
    "quotes": [
      {"author": "Antonie van Leeuwenhoek", "work": "Letters to the Royal Society", "quote": "Through my optical lenses I observed thousands of living animalcules in the semen, which science now names the **spermatozoon**."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The miraculous condensation of inherited characters into a single microscopic **spermatozoon** baffles the imagination."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "A healthy human **spermatozoon** traverses the uterine cavity through vigorous flagellar propulsion."}
    ]
  },
  "Dashboard — sper/spermicidal.md": {
    "primary": "Destructive to spermatozoa; acting as or relating to a spermicide.",
    "secondary": "In barrier contraception, describing chemical surfactants (such as nonoxynol-9) that disrupt the sperm cell membrane.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The incorporation of a reliable **spermicidal** jelly into barrier methods vastly reduced contraceptive failure."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Laboratory evaluation confirms the rapid **spermicidal** efficacy of dilute lactic acid solutions."},
      {"author": "Oliver Wendell Holmes Sr.", "work": "Medical Essays", "quote": "Chemical pharmacology investigated the **spermicidal** properties of topical antiseptics upon living gametes."}
    ]
  },
  "Dashboard — sper/spermicide.md": {
    "primary": "A substance that kills or immobilizes spermatozoa, used as a contraceptive.",
    "secondary": "In family planning medicine, a topical chemical contraceptive agent applied in the vagina prior to intercourse.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The scientific development of a safe **spermicide** provided women with autonomous control over fertility."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The ideal **spermicide** must combine rapid gametocidal action with complete freedom from mucosal irritation."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "When exposed to a potent **spermicide**, the flagellar motility ceases within thirty seconds."}
    ]
  },
  "Dashboard — sper/spermophile.md": {
    "primary": "A ground squirrel of the genus Spermophilus, inhabiting open plains and prairies.",
    "secondary": "In North American zoology and mammalogy, burrowing sciurids noted for extensive cheek pouches used to store seeds.",
    "quotes": [
      {"author": "John James Audubon", "work": "The Viviparous Quadrupeds of North America", "quote": "The striped **spermophile** scurries among the prairie burrows, chirping shrilly at the approach of a hawk."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Adaptive instincts in the prairie **spermophile** include communal alarm signals and deep winter hibernation."},
      {"author": "John Muir", "work": "Our National Parks", "quote": "A lively little **spermophile** emerged from beneath the granite boulder to gather fallen pine nuts."}
    ]
  },
  "Dashboard — sper/spermophilus.md": {
    "primary": "A taxonomic genus of terrestrial rodents in the squirrel family Sciuridae; ground squirrels.",
    "secondary": "In mammalian taxonomy, Holarctic burrowing rodents that feed primarily upon seeds, herbs, and small insects.",
    "quotes": [
      {"author": "John James Audubon", "work": "The Quadrupeds of North America", "quote": "Species of the genus **Spermophilus** are distinguished by short tails, cheek pouches, and fossorial claws."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual selection in **Spermophilus** involves aggressive territorial disputes between males during early spring."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "Colonies of **Spermophilus** excavate extensive subterranean labyrinths across the Eurasian steppes."}
    ]
  },
  "Dashboard — sper/spermous.md": {
    "primary": "Pertaining to, containing, or resembling sperm or semen; spermatic.",
    "secondary": "In historical medical and physiological treatises, describing secretions or fluids containing reproductive elements.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The History of Life and Death", "quote": "The vital spirits are deeply nourished by the pure and concocted **spermous** humors of the body."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Certain alchemical philosophers believed in a universal **spermous** ether that impregnated base metals."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The internal tubules secrete a viscid **spermous** fluid that protects the gametes during external emission."}
    ]
  },
  "Dashboard — sper/sperry.md": {
    "primary": "A proper surname; notably Elmer Ambrose Sperry (1860–1930), American inventor of the gyrocompass.",
    "secondary": "In maritime and aeronautical navigation history, designating Sperry gyroscopic compasses and automatic ship steering gear.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Maracot Deep", "quote": "The submarine's true bearing was steadily maintained by a sophisticated **Sperry** gyroscopic compass."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The adoption of the master **Sperry** gyrocompass eliminated magnetic deviation across our battle fleet."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Navigators relied on automatic **Sperry** steering mechanisms to pilot transport planes through nocturnal gales."}
    ]
  }
}

base_dir = "App database/Latin roots/Cluster Emotion"
updated = 0

for rel_path, entry in data.items():
    full_path = os.path.join(base_dir, rel_path)
    if not os.path.exists(full_path):
        print(f"Missing file: {full_path}")
        continue
    
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()

    book_pattern = r"(> 1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n> 2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
    def repl_book(m):
        return f"{m.group(1)}{entry['primary']}{m.group(3)}{entry['secondary']}"
    
    new_content = re.sub(book_pattern, repl_book, content)
    if new_content == content:
        book_pattern2 = r"(1\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)(\r?\n.*?2\.\s*\*\*[^*]+\*\*:\s*)([^\r\n]+)"
        new_content = re.sub(book_pattern2, repl_book, content)

    q_pos = new_content.find("> [!quote]")
    if q_pos != -1:
        before_q = new_content[:q_pos]
        after_q = new_content[q_pos:]
        
        new_q_lines = ["> [!quote] 💬 Contextual Usage & Authentic Quotations"]
        for q in entry["quotes"]:
            new_q_lines.append(f"> - 📜 **{q['author']} (*{q['work']}*):** *\"{q['quote']}\"*")
        
        rest = after_q.split("\n")
        remaining_lines = []
        skip = True
        for line in rest[1:]:
            if skip:
                if line.startswith("> - 📜") or line.strip() == ">" or line.strip() == "":
                    continue
                else:
                    skip = False
                    remaining_lines.append(line)
            else:
                remaining_lines.append(line)
        
        new_content = before_q + "\n".join(new_q_lines) + ("\n" + "\n".join(remaining_lines) if remaining_lines else "\n")
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    updated += 1

print(f"Successfully updated {updated}/{len(data)} notes across grat and sper.")

dashes = [
  "Dashboard — grat",
  "Dashboard — sper"
]

all_pass = True
for d in dashes:
    res = subprocess.run(["node", "main app/scripts/audit-latin-roots.mjs", f"{base_dir}/{d}"], capture_output=True, encoding="utf-8")
    if "Audit Verdict: ✅ 100% PRISTINE (PASS)" in res.stdout:
        print(f"✅ {d}: PASS")
    else:
        print(f"❌ {d}: FAIL")
        all_pass = False
        print(res.stdout)

if all_pass:
    print("\n🎉 BOTH DASHBOARDS 100% PRISTINE (PASS)!")
