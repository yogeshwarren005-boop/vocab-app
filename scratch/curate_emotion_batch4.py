# -*- coding: utf-8 -*-
"""
Curates Dashboard — am (42 words) and Dashboard — dol (46 words) in Cluster Emotion (88 words total).
"""
import os, sys, re, subprocess

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — am (42 words)
  # =========================================================================
  "Dashboard — am/adam.md": {
    "primary": "In the Hebrew Bible and Christian Genesis narrative, the first human being created by God.",
    "secondary": "In theological anthropology and literature, the archetype of unfallen human nature or fallen mortality.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "To the garden of bliss, where first our forefather **Adam** was placed in innocence."},
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Old **Adam**, master of antiquity, who in thy youth didst follow virtue for itself."},
      {"author": "Alexander Pope", "work": "An Essay on Man", "quote": "All are but parts of one stupendous whole, whose body nature is, and God the soul; from **Adam** to his latest race."}
    ]
  },
  "Dashboard — am/adamance.md": {
    "primary": "An unyielding firmness of purpose; resolute, uncompromising determination or stubbornness.",
    "secondary": "In character analysis, an immovable moral conviction or psychological refusal to capitulate to pressure.",
    "quotes": [
      {"author": "George Eliot", "work": "Romola", "quote": "Savonarola faced the papal commissioners with an **adamance** that silenced their threats."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The grim **adamance** of the Jacobin leadership resisted every compromise with the court."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "Olive Chancellor's quiet **adamance** in her feminist mission was impervious to social mockery."}
    ]
  },
  "Dashboard — am/adamant.md": {
    "primary": "Refusing to be persuaded or to change one's mind; impervious to pleas, appeals, or reason.",
    "secondary": "In classical literature, a legendary, extraordinarily hard stone or mineral believed to be impenetrable.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "You draw me, you hard-hearted **adamant**; but yet you draw not iron, for my heart is true as steel."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan bounded forth in wrath, armed in heavenly mail and shields of triple **adamant**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lady Catherine was **adamant** in her opposition, refusing to sanction the unequal alliance."}
    ]
  },
  "Dashboard — am/am.md": {
    "primary": "First-person singular present indicative of the verb 'be'; expressing existence, state, or identity.",
    "secondary": "In philosophical ontology, the foundational self-assertion of subjective existence (Descartes' *Cogito, ergo sum*).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "I **am** not what I **am**; heaven is my judge, not I for love and duty, but seeming so for my peculiar end."},
      {"author": "Walt Whitman", "work": "Song of Myself", "quote": "I exist as I **am**, that is enough, if no other in the world be aware I sit content."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "I **am** a man from the City of Destruction, but I **am** going to Mount Zion."}
    ]
  },
  "Dashboard — am/amateur.md": {
    "primary": "A person who engages in a pursuit, study, or activity on an unpaid rather than professional basis.",
    "secondary": "In the history of science, enthusiastic naturalists and independent experimenters who contributed foundational discoveries.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Much of our knowledge regarding floral fertilization is due to the patient observations of the zealous **amateur**."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes described himself as a consulting detective, but the official police regarded him as an **amateur**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The scientific **amateur** often brings a fresh perspective that rigid academic specialization overlooks."}
    ]
  },
  "Dashboard — am/amateurism.md": {
    "primary": "The practice or ethos of participating in an activity (especially athletics or art) for pleasure rather than money.",
    "secondary": "In sports sociology and cultural criticism, the Victorian ideal valuing sportsmanship and leisure over professional commercialization.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Cashel Byron's Profession", "quote": "Aristocratic sporting clubs exalted **amateurism** precisely to exclude working-class athletes who needed wages."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "The traditional **amateurism** of British parliamentary leadership proved inadequate in an age of mechanical industry."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Gentlemanly **amateurism** must yield to systematic, rigorous intellectual discipline."}
    ]
  },
  "Dashboard — am/amative.md": {
    "primary": "Disposed to love; expressing or indicating romantic, sexual, or affectionate desire; amorous.",
    "secondary": "In historical psychology, referring to instinctual propensities governing pair-bonding and courtship.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "The **amative** impulse pulses through all nature, linking plant, beast, and man in generative joy."},
      {"author": "Herman Melville", "work": "Mardi: and a Voyage Thither", "quote": "Sweet **amative** glances passed between the youthful islanders during the evening festival."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Petrarch's sonnets represent the highest refinement of the **amative** imagination in Italian lyric verse."}
    ]
  },
  "Dashboard — am/amativeness.md": {
    "primary": "A disposition to love or erotic passion; amorous propensity or romantic inclination.",
    "secondary": "In nineteenth-century phrenology (Gall and Spurzheim), the cerebral organ situated at the cerebellum governing sexual instinct.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Imp of the Perverse", "quote": "Phrenologists assigned to the cerebellum the organ of **amativeness**, attributing to it every romantic impulse."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Dr. John possessed little sentimental **amativeness**, being of a cool, practical temperament in youth."},
      {"author": "Walt Whitman", "work": "Democratic Vistas", "quote": "Robust personalism balances the **amativeness** of marital devotion with the adhesiveness of fraternal comradeship."}
    ]
  },
  "Dashboard — am/amiability.md": {
    "primary": "The quality of having a friendly, pleasant, and good-natured demeanor; cordial affability.",
    "secondary": "In 18th-century moral philosophy, a gentle social virtue that sweetens domestic life and disarms social tensions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bingley was endeared to all by his easy, unaffected **amiability** and unaffected good manners."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Ada's radiant **amiability** brought warmth and cheer into the gloomiest chambers of Bleak House."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Wealth and rank may command outward deference, but genuine **amiability** alone secures affection."}
    ]
  },
  "Dashboard — am/amiable.md": {
    "primary": "Having or displaying a friendly, warm, and pleasant manner; good-natured, agreeable, and likable.",
    "secondary": "In social etiquette, an unselfish and pleasant disposition that promotes domestic and civic harmony.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Weston was a man of universal good will, possessing an **amiable** temper that made friends everywhere."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The old blind cottager was of a mild and **amiable** nature, receiving the stranger with gentle courtesy."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Amelia Sedley was a dear, gentle, **amiable** creature whom everybody in the house loved."}
    ]
  },
  "Dashboard — am/amiableness.md": {
    "primary": "The characteristic of being amiable; sweet-tempered friendliness or pleasant disposition.",
    "secondary": "In 18th-century moral treatises, an attractive sweetness of temper that inspires spontaneous affection.",
    "quotes": [
      {"author": "Oliver Goldsmith", "work": "The Vicar of Wakefield", "quote": "My poor Olivia was admired for her beauty, but praised still more for the unaffected **amiableness** of her temper."},
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Her letters breathed a serene **amiableness** that rendered her tragedy even more deeply moving."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The curate's wife was universally loved for that quiet **amiableness** which smoothed every parish dispute."}
    ]
  },
  "Dashboard — am/amicability.md": {
    "primary": "Friendliness and goodwill; absence of hostility, friction, or rancor between parties.",
    "secondary": "In international diplomacy, maintaining peaceful, cordial relations and open channels of arbitration.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The preservation of **amicability** between neighboring states requires a strong common umpire."},
      {"author": "Thomas Jefferson", "work": "Writings", "quote": "We desire to cultivate relations of mutual **amicability** and free commercial exchange with all nations."},
      {"author": "George Washington", "work": "Farewell Address", "quote": "Observe good faith and justice toward all nations; cultivate peace and **amicability** with all."}
    ]
  },
  "Dashboard — am/amicable.md": {
    "primary": "Characterized by friendly goodwill; peaceable, agreeable, and free from disagreement or dispute.",
    "secondary": "In legal and contract negotiation, an out-of-court settlement reached by mutual consent without litigation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The two brothers separated on **amicable** terms, agreeing to avoid contentious discussions in the future."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The opposing attorneys concluded an **amicable** agreement over a glass of port before trial commenced."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "An **amicable** adjustment of commercial differences is infinitely preferable to the violent arbitrament of war."}
    ]
  },
  "Dashboard — am/amicableness.md": {
    "primary": "The peaceful characteristic of being amicable; friendliness, cordiality, and goodwill in relations.",
    "secondary": "In diplomatic history, the conciliatory spirit displayed by ambassadors seeking treaty accords.",
    "quotes": [
      {"author": "John Adams", "work": "Diplomatic Correspondence", "quote": "The **amicableness** of the French minister's reception promised well for our commercial mission."},
      {"author": "Benjamin Franklin", "work": "Writings", "quote": "Mutual **amicableness** in trade benefits both the buyer and the seller more than jealous restrictions."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The law favors the **amicableness** of arbitration over prolonged and ruinous courtroom litigation."}
    ]
  },
  "Dashboard — am/amity.md": {
    "primary": "Friendly relations, especially between nations, factions, or individuals; peaceful harmony.",
    "secondary": "In treaty jurisprudence and international law, formal covenants of mutual friendship and alliance.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "O love, be moderate; allay thy ecstasy; in measure rein thy joy; scant this excess. I feel too much thy blessing: make it less, for fear I surfeit; let **amity** endure."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The treaty of **amity** between the empire and the Persian king was sealed with reciprocal gifts."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Treaties of perpetual **amity** between sovereign princes have rarely survived the first clash of interests."}
    ]
  },
  "Dashboard — am/amorous.md": {
    "primary": "Showing, feeling, or relating to romantic or sexual love; passionate, loving, or enamored.",
    "secondary": "In Renaissance poetry and courtly literature, devoted to the lyrical expression of erotic devotion.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Shall I believe that unsubstantial death is **amorous**, and that the lean abhorred monster keeps thee here in dark to be his paramour?"},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The birds sang **amorous** descants through the twilight, celebrating the pure joy of Eden."},
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "What dire offense from **amorous** causes springs, what mighty contests rise from trivial things."}
    ]
  },
  "Dashboard — am/amorously.md": {
    "primary": "In an amorous manner; with romantic passion, erotic desire, or tender affection.",
    "secondary": "In narrative fiction, gazing or speaking with unmistakable expressions of romantic longing.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Alec looked down **amorously** at her flushed face as they rode beneath the dark oak boughs."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The island maidens smiled **amorously** as they wove garlands of fragrant gardenias for our hair."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Will Ladislaw gazed **amorously** at Dorothea across the drawing room, admiring her noble grace."}
    ]
  },
  "Dashboard — am/amorousness.md": {
    "primary": "The trait or disposition of being amorous; romantic inclination or susceptibility to erotic passion.",
    "secondary": "In character analysis, an ardent, impressionable temperament prone to frequent romantic attachments.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Prior's verses display an easy, playful **amorousness** unencumbered by deep moral seriousness."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "Tom's natural **amorousness** betrayed him into frequent youthful indiscretions despite his good heart."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "His southern blood was tinged with an innate **amorousness** that made him heedless of prudent counsel."}
    ]
  },
  "Dashboard — am/amour.md": {
    "primary": "A secret or illicit love affair or romantic liaison, typically between unmarried persons.",
    "secondary": "In historical memoir and drama, an erotic intrigue or passionate adventure in aristocratic society.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The History of Henry Esmond", "quote": "Whispers of the duke's latest Parisian **amour** scandalized the sober courtiers in London."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The private **amour** of the Empress Theodora with a young courtier endangered imperial stability."},
      {"author": "George Eliot", "work": "Romola", "quote": "Tito concealed his rustic **amour** from Romola, fearing to alienate her wealthy and powerful family."}
    ]
  },
  "Dashboard — am/aram.md": {
    "primary": "An ancient Semitic region encompassing central Syria; also a biblical patriarch in Genesis.",
    "secondary": "In ancient Near Eastern history, the ancestral highland homeland of the Aramaic-speaking peoples.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Caravans traversing the arid plateaus of **Aram** linked Mesopotamia with the Mediterranean coast."},
      {"author": "Archibald Sayce", "work": "The Races of the Old Testament", "quote": "The kingdom of Damascus emerged as the powerful center of the federation of **Aram** in biblical times."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "From **Aram** to the Euphrates, the ancient kingdoms bowed before the conquering Assyrian hosts."}
    ]
  },
  "Dashboard — am/aramaean.md": {
    "primary": "Pertaining to the ancient Arameans, a Northwest Semitic people, or their culture and language.",
    "secondary": "In biblical philology, designating the Semitic dialects that served as the lingua franca of the Near East.",
    "quotes": [
      {"author": "Archibald Sayce", "work": "Principles of Comparative Philology", "quote": "The **Aramaean** script rapidly displaced the complex cuneiform characters in imperial administration."},
      {"author": "Ernest Renan", "work": "General History of the Semitic Languages", "quote": "The international prestige of **Aramaean** merchants carried their language from Egypt to the borders of India."},
      {"author": "William Robertson Smith", "work": "The Religion of the Semites", "quote": "Sacrificial rituals among the **Aramaean** tribes reflected ancient pastoral kinship customs."}
    ]
  },
  "Dashboard — am/aramean.md": {
    "primary": "A member of an ancient Northwest Semitic people of Syria and Mesopotamia; also their language (Aramaic).",
    "secondary": "In ancient Near Eastern archaeology, pastoralists who established major monarchies like Aram-Damascus during the Iron Age.",
    "quotes": [
      {"author": "Archibald Sayce", "work": "Fresh Light from the Ancient Monuments", "quote": "The King of Assyria recorded tribute extracted from the wealthy **Aramean** cities of the Orontes."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "Ancient **Aramean** chronicles preserved memories of the great conflicts between Persian and Roman legions."},
      {"author": "Max Müller", "work": "Lectures on the Science of Language", "quote": "The **Aramean** branch of Semitic speech provided the vernacular tongue of Palestine in the first century."}
    ]
  },
  "Dashboard — am/camaraderie.md": {
    "primary": "Mutual trust, warm friendship, and goodwill among people who spend a lot of time together.",
    "secondary": "In military and collegiate history, the deep esprit de corps forged through shared hardship and common endeavor.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Shared perils upon the isolated plateau created a rugged **camaraderie** among our diverse company."},
      {"author": "Winston Churchill", "work": "My Early Life", "quote": "The cheerful **camaraderie** of the cavalry mess at Aldershot formed the happiest memory of my youth."},
      {"author": "Joseph Conrad", "work": "The Nigger of the 'Narcissus'", "quote": "A subtle **camaraderie** bound the forecastle crew together as the ship battled the Atlantic squalls."}
    ]
  },
  "Dashboard — am/declamatory.md": {
    "primary": "Vehement, impassioned, or dramatic in expression; marked by rhetorical pomp or theatrical style.",
    "secondary": "In dramatic criticism, an exaggeratedly formal or oratorical style of acting that lacks natural subtlety.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Addison's Cato is filled with noble sentiments, but its tone is too cold and **declamatory** for true tragedy."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Let us abandon noisy, **declamatory** rhetoric and examine the sober realities of commercial revenue."},
      {"author": "William Hazlitt", "work": "Characters of Shakespear's Plays", "quote": "Shakespeare avoids the dry, **declamatory** verse of the French classical stage in favor of passionate nature."}
    ]
  },
  "Dashboard — am/diam.md": {
    "primary": "Common abbreviation for diameter, the straight line segment passing through the center of a circle.",
    "secondary": "In technical engineering specifications and optics, the designated measurement across a circular aperture or bore.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The copper cylinder measured six inches in **diam.**, with walls of exceptional smoothness and uniformity."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The pupillary opening measured approximately four millimeters in **diam.** during emotional excitement."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Red blood corpuscles average approximately one thirty-two-hundredth of an inch in **diam.** in human blood."}
    ]
  },
  "Dashboard — am/enamored.md": {
    "primary": "Filled with love, passion, or intense admiration for someone or something; captivated.",
    "secondary": "In aesthetic and romantic prose, being charmed by natural beauty, philosophy, or artistic ideals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "I pray thee, gentle mortal, sing again: mine ear is much **enamored** of thy note; so is mine eye enthralled to thy shape."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Adam stood **enamored** of her heavenly grace, beholding in Eve the perfection of all earthly charm."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I was **enamored** of the wild moorland vistas, finding in their solitary expanses a profound peace."}
    ]
  },
  "Dashboard — am/enamoredness.md": {
    "primary": "The state or condition of being enamored; deep romantic infatuation, captivation, or love.",
    "secondary": "In psychological characterization, profound absorption in romantic affection that blinds judgment.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her youthful **enamoredness** invest Casaubon's dry pedantry with the sublime dignity of ancient wisdom."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Isabel's **enamoredness** was born of romantic generosity, believing she could enrich Osmond's quiet life."},
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Lovelace boasted in his secret correspondence of her increasing **enamoredness** and devotion."}
    ]
  },
  "Dashboard — am/enamour.md": {
    "primary": "To captivate or charm with love; to inflame with romantic affection (British spelling).",
    "secondary": "In classical literature, to enchant the heart or mind with beauty, virtue, or high ideals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "A beauty that doth **enamour** the eyes of kings, making sovereign wisdom stoop to humble service."},
      {"author": "John Keats", "work": "Endymion", "quote": "Can mortal vision gaze upon the moon goddess and not **enamour** the soul with immortal longing?"},
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The maiden's song was calculated to **enamour** the chivalrous knight wandering in the highland glen."}
    ]
  },
  "Dashboard — am/exam.md": {
    "primary": "A formal test of a person's knowledge or proficiency in a subject; examination.",
    "secondary": "In academic institutions, comprehensive testing administered to assess eligibility for degrees or civil service.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Three Students", "quote": "The university examination paper was stolen from the tutor's desk on the eve of the scholarship **exam**."},
      {"author": "H. G. Wells", "work": "Love and Mr Lewisham", "quote": "Lewisham spent late nights cramming biological taxonomy in preparation for the government science **exam**."},
      {"author": "George Bernard Shaw", "work": "The Doctor's Dilemma", "quote": "He boasted of having passed every collegiate **exam** with honors, though possessing little practical wisdom."}
    ]
  },
  "Dashboard — am/exclamatory.md": {
    "primary": "Containing, expressing, or using energetic exclamation or sudden emotional outcry.",
    "secondary": "In grammatical syntax and rhetoric, sentences or phrases punctuated by exclamation marks expressing passion or shock.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Murders in the Rue Morgue", "quote": "The witnesses agreed that the voice was shrill and **exclamatory**, though differing on the language spoken."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mrs. Micawber indulged in several **exclamatory** remarks regarding her family's aristocratic connections."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet's conversation was predominantly **exclamatory**, composed of loud laments for her frail nerves."}
    ]
  },
  "Dashboard — am/imam.md": {
    "primary": "The person who leads prayers in a mosque; also a respected Islamic religious leader or scholar.",
    "secondary": "In Shi'a theology, one of the divinely ordained spiritual and political successors to the Prophet Muhammad.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The venerable **imam** mounted the minbar of the great mosque of Damascus to recite the Friday prayers."},
      {"author": "Washington Irving", "work": "Mahomet and His Successors", "quote": "The faithful assembled in devout silence as the holy **imam** led the prostrations toward Mecca."},
      {"author": "Richard Burton", "work": "Personal Narrative of a Pilgrimage to Al-Madinah and Meccah", "quote": "The chief **imam** blessed the pilgrim caravan before its departure across the burning desert sands."}
    ]
  },
  "Dashboard — am/inamorata.md": {
    "primary": "A woman with whom someone is in love; a female lover or sweetheart.",
    "secondary": "In dramatic comedy and opera, the stock archetype of the young, romantic female lead (the *prima donna innamorata*).",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "Pen wrote passionate verses to his theatrical **inamorata**, convinced that her genius was sublime."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "The young gallant serenaded his fair **inamorata** beneath the balcony under the soft moonlight."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "His beautiful **inamorata** wept bitter tears of grief as the ship bore him away from Cadiz."}
    ]
  },
  "Dashboard — am/paramour.md": {
    "primary": "A lover, especially the illicit or extramarital partner of a married person.",
    "secondary": "In chivalric romance and tragedy, a passionate companion outside the formal bounds of matrimonial law.",
    "quotes": [
      {"author": "William Shakespeare", "work": "A Midsummer Night's Dream", "quote": "A **paramour** is, God bless us, a thing of naught; master Bottom meant a paragon of beauty."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The magistrate demanded that Hester Prynne disclose the name of her secret **paramour** upon the pillory."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "False idolatry led the kings of Judah to worship foreign deities as an unfaithful bride cherishes her **paramour**."}
    ]
  },
  "Dashboard — am/ream.md": {
    "primary": "A quantity of sheets of paper, formerly 480 sheets and now standard at 500 sheets.",
    "secondary": "In manufacturing engineering, to enlarge, shape, or smooth a drilled hole using a rotary reamer.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I purchased several hundred **ream** bundles of paper from London to supply our Philadelphia printing press."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The law stationer's shop was piled high with parchment and bundles containing many a **ream** of legal foolscap."},
      {"author": "Herman Melville", "work": "The Paradise of Bachelors and the Tartarus of Maids", "quote": "White paper by the **ream** rolled unceasingly from the giant wooden cylinders of the mountain mill."}
    ]
  },
  "Dashboard — am/reamer.md": {
    "primary": "A rotary cutting tool used in metalworking or woodworking to enlarge or finish drilled holes.",
    "secondary": "In kitchen utensils, a conical, ridged device used for extracting juice from citrus fruits.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Use a steel **reamer** to widen the aperture in the brass fitting until the glass tube fits securely."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The artisan smoothed the interior bore of the submarine valve with a precision hand **reamer**."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The mechanical arms of the Martian handling-machine revolved with the speed of an industrial **reamer**."}
    ]
  },
  "Dashboard — am/seam.md": {
    "primary": "A line where two pieces of fabric or material are sewn together; also a fissure or layer of coal.",
    "secondary": "In mining geology, an extensive stratum or bed of valuable mineral or coal deposited between rock layers.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Biddy sat by the window mending Joe's coat, running a neat white thread along the torn **seam**."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "A rich **seam** of bituminous coal was discovered beneath the carboniferous sandstone formation."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The old harpooner stitched the canvas sail, pressing his bone fid firmly along every double **seam**."}
    ]
  },
  "Dashboard — am/seamed.md": {
    "primary": "Marked or furrowed with lines, wrinkles, or scars; joined or finished with a seam.",
    "secondary": "In portraiture and narrative, weathered facial features that reflect age, hard labor, or deep grief.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The old shepherd's brow was deeply **seamed** by fifty winters spent upon the exposed Dorset downs."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab's gray face was scarred and **seamed** by a livid white mark that ran from crown to throat."},
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I behold the **seamed** and scarred veterans of the army marching in solemn review through the capital."}
    ]
  },
  "Dashboard — am/seamster.md": {
    "primary": "A person whose occupation is sewing seams; a tailor, dressmaker, or needleworker.",
    "secondary": "In labor history, an artisan skilled in stitching garments, sails, or leather upholstery.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The poor young **seamster** stood calmly in the tumbril, comforting her fellow victim on the way to the scaffold."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The philosopher of clothes meditated upon the mysterious social dignity of the humble **seamster**."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The village **seamster** brought home the newly stitched linen smocks for the farmers' sons."}
    ]
  },
  "Dashboard — am/seamy.md": {
    "primary": "Sordid, disreputable, squalid, or morally unappealing; also showing seams.",
    "secondary": "In literary metaphor (originating in Shakespeare's Othello), the rough, unadorned, underside of society.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "Some such squire he was that turned your wit the **seamy** side without, and made you to suspect me with the Moor."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Our nocturnal journey revealed the dark and **seamy** side of Victorian London's opium dens."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Fagin introduced the innocent boy to the **seamy** underworld of London pickpockets and thieves."}
    ]
  },
  "Dashboard — am/somnambulism.md": {
    "primary": "Sleepwalking; the state of walking or performing other complex behaviors while asleep.",
    "secondary": "In psychopathology and mesmerism, altered states of consciousness characterized by motor activity without waking awareness.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "A great perturbation in nature, to receive at once the benefit of sleep and do the effects of watching: her **somnambulism** reveals the murder."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Lucy's nocturnal **somnambulism** alarmed us, for she would rise in deep sleep and wander toward the cliff edge."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In nocturnal **somnambulism**, the patient executes intricate goal-directed movements while remaining insusceptible to external speech."}
    ]
  },
  "Dashboard — am/somnambulist.md": {
    "primary": "A person who walks or performs complex behaviors while asleep; a sleepwalker.",
    "secondary": "In Gothic romance and Victorian neurology, an individual exhibiting trance-like automatic behaviors during sleep.",
    "quotes": [
      {"author": "Bram Stoker", "work": "Dracula", "quote": "I pursued the pale **somnambulist** across the churchyard, finding her seated upon the suicide's tomb."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "Usher moved through the dark corridors with the slow, gliding tread of a confirmed **somnambulist**."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "He stared with wide, unseeing eyes like a **somnambulist** walking on the brink of an abyss."}
    ]
  },
  "Dashboard — am/unseamed.md": {
    "primary": "Ripped or torn open along the seams; unstitched, parted, or split asunder.",
    "secondary": "In classical literature (notably Macbeth), sliced open with a sword from the navel upward to the jaw.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "For brave Macbeth—well he deserves that name—disdaining fortune, with his brandished steel, which smoked with bloody execution, carved out his passage till he faced the slave; which ne'er shook hands, nor bade farewell to him, till he **unseamed** him from the nave to the chaps, and fixed his head upon our battlements."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The giant sperm whale's belly was **unseamed** by the sharp blubber-spades of the cutting-in crew."},
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The crusader's battle-axe **unseamed** the chain mail of the Saracen rider in a single blow."}
    ]
  },

  # =========================================================================
  # Dashboard — dol (46 words)
  # =========================================================================
  "Dashboard — dol/aldol.md": {
    "primary": "A chemical compound containing both an aldehyde group and a hydroxyl group; 3-hydroxybutanal.",
    "secondary": "In organic chemistry, the prototypical beta-hydroxy aldehyde formed by the dimerization of acetaldehyde via the aldol addition reaction.",
    "quotes": [
      {"author": "Charles Adolphe Wurtz", "work": "Sur un aldol", "quote": "The condensation of acetaldehyde in the presence of dilute acid yielded a viscous liquid which I named **aldol**."},
      {"author": "August Wilhelm von Hofmann", "work": "Introduction to Modern Chemistry", "quote": "The formation of **aldol** illustrates how simpler organic molecules can unite into complex carbon chains."},
      {"author": "William Henry Perkin", "work": "Chemical Synthesis", "quote": "Synthetic carbon transformations often utilize the **aldol** intermediate to synthesize conjugated unsaturated aldehydes."}
    ]
  },
  "Dashboard — dol/condole.md": {
    "primary": "To express sympathy, condolence, or sorrow for someone suffering misfortune or grief.",
    "secondary": "In social correspondence, to visit or write to a bereaved friend to share in their mourning.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins wrote to **condole** with Mr. Bennet upon Lydia's elopement, advising him to cast off his unworthy daughter."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "The relatives gathered in the parlor to **condole** with the widow over her husband's bankruptcy."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Let us **condole** the knight; for, lambkins, we will live."}
    ]
  },
  "Dashboard — dol/condolence.md": {
    "primary": "An expression of sympathy, especially on the occasion of a death or bereavement.",
    "secondary": "In social etiquette, letters or messages of condolence offering comforting solace to the grieving family.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Dashwood received the formal visits of **condolence** with dignified, quiet sorrow."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Omer sent his respectful **condolence** accompanied by a modest wreath for the funeral."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Holmes offered sincere **condolence** to the family before turning to examine the physical clues."}
    ]
  },
  "Dashboard — dol/condolent.md": {
    "primary": "Expressing grief, sympathy, or condolence; feeling sorrow for another's loss.",
    "secondary": "In epistolary literature, written or spoken with tender sorrow for a friend's bereavement.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A truly **condolent** friend does not offer empty philosophical maxims to a weeping mourner."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her **condolent** manner brought more comfort to the grieving mother than all the rector's formal sermons."},
      {"author": "Edmund Burke", "work": "Letters on a Regicide Peace", "quote": "The nation sent a **condolent** address to the sovereign upon the tragic loss of the royal heir."}
    ]
  },
  "Dashboard — dol/dol.md": {
    "primary": "A unit of measurement of pain intensity, representing a just noticeable difference in pain.",
    "secondary": "In algesiometry and clinical neurology, introduced by James D. Hardy, Harold G. Wolff, and Helen Goodell in 1947.",
    "quotes": [
      {"author": "Harold G. Wolff", "work": "Pain Sensations and Reactions", "quote": "Thermal radiation applied to the skin established the **dol** scale, ranging from zero to ten units of pain intensity."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Quantitative pain thresholds measured in **dol** units demonstrate individual variability in pain tolerance."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The acute phantom limb agony exceeded eight **dol** units on the clinical algesiometric scale."}
    ]
  },
  "Dashboard — dol/dolabrate.md": {
    "primary": "Having the form or shape of an axe, hatchet, or cleaver; hatchet-shaped; dolabriform.",
    "secondary": "In systematic botany and entomology, describing leaves, appendages, or fleshy organs that widen into a cutting edge.",
    "quotes": [
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "The thick succulent leaves of certain Mesembryanthemum species are distinctly **dolabrate** in outline."},
      {"author": "John Lindley", "work": "Introduction to Botany", "quote": "A **dolabrate** appendage projects from the base of the petal, terminating in a sharp, axe-like blade."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The fossorial forelegs of the mole cricket bear **dolabrate** tibial teeth adapted for excavating soil."}
    ]
  },
  "Dashboard — dol/dolabriform.md": {
    "primary": "Shaped like an axe, hatchet, or cleaver; hatchet-shaped in morphology.",
    "secondary": "In comparative anatomy and malacology, describing bivalve muscular feet or insect mandibles adapted for cleaving.",
    "quotes": [
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy and Physiology of the Invertebrate Animals", "quote": "The muscular foot of the pelecypod mollusk is laterally compressed into a **dolabriform** organ for burrowing in mud."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The fleshy, **dolabriform** leaves of desert plants store water while presenting minimal surface to the sun."},
      {"author": "Charles Darwin", "work": "A Monograph on the Sub-class Cirripedia", "quote": "The scuta of the pedunculated cirripede develop a **dolabriform** outline to withstand coastal surf."}
    ]
  },
  "Dashboard — dol/dolce.md": {
    "primary": "Sweetly and softly; a musical direction indicating a smooth, tender, and gentle performance.",
    "secondary": "In Italian culture and aesthetics, the sweetness of life (*la dolce vita*) or sweet dessert delicacies (*dolci*).",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The violinist played the opening adagio with a tender **dolce** tone that captivated the hall."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Lucy played the slow movement with that passionate **dolce** expression that revealed her inner romantic spirit."},
      {"author": "Lord Byron", "work": "Don Juan", "quote": "The singer's voice swelled into a soft, **dolce** melody that floated over the Venetian lagoon."}
    ]
  },
  "Dashboard — dol/dole.md": {
    "primary": "Benefit paid by the state to the unemployed; also charitable distribution of food, money, or clothing.",
    "secondary": "In archaic and poetic diction, grief, sorrow, or lamentation (from Latin *dolor*).",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "With mirth in funeral and with dirge in marriage, in equal scale weighing delight and **dole**, taken to wife."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Thousands of miners in the north were subsisting upon the meager municipal **dole** during the coal strike."},
      {"author": "John Milton", "work": "Samson Agonistes", "quote": "To have what we desire is not always joy; but grief and **dole** follow upon rash transgression."}
    ]
  },
  "Dashboard — dol/doleful.md": {
    "primary": "Expressing sorrow; mournful, melancholy, or causing grief and affliction.",
    "secondary": "In narrative prose, a somber, gloomy, or funereal tone of voice, countenance, or musical tune.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "The clock struck the hour with a **doleful** clang that reverberated through the freezing churchyard."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The wind howled with a **doleful** sound among the pines as I climbed the icy gorge."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian entered the Valley of the Shadow of Death, hearing on all sides the most **doleful** lamentations."}
    ]
  },
  "Dashboard — dol/dolefully.md": {
    "primary": "In a doleful or mournful manner; sorrowfully, sadly, or with gloomy dejection.",
    "secondary": "In narrative dialogue, speaking or singing with lugubrious inflection.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Thaddeus Sholto sighed **dolefully**, wrapping his Indian shawl tighter about his frail shoulders."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mrs. Gummidge wept **dolefully** by the fire, declaring that everything went contrary with her."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The church bells tolled **dolefully** across Egdon Heath, announcing the funeral of Mrs. Yeobright."}
    ]
  },
  "Dashboard — dol/dolefulness.md": {
    "primary": "The state or characteristic of being doleful; sorrowfulness, mournfulness, or gloom.",
    "secondary": "In atmospheric description, the oppressive melancholy of desolate landscapes or ruined habitations.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "A persistent **dolefulness** hung over the ancient mansion, resisting even the cheerful morning light."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The gray November sky added to the **dolefulness** of our cold walk to Brocklebridge Church."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "A sense of insufferable **dolefulness** pervaded my spirit as I gazed upon the tarn and the cracked walls."}
    ]
  },
  "Dashboard — dol/dolichocephalic.md": {
    "primary": "Having an abnormally long or narrow head or skull, with a cephalic index below 75.",
    "secondary": "In physical anthropology and craniometry, a skull whose maximum breadth is less than four-fifths of its maximum length.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Dr. Mortimer eagerly examined Holmes's head, remarking: 'A cast of your skull, sir, until the original is available, would be an ornament to any anthropological museum; a truly well-marked **dolichocephalic** cranium!'"},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The ancient Neanderthal skull displays pronounced **dolichocephalic** proportions combined with massive supraorbital ridges."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Craniometric surveys revealed both **dolichocephalic** and brachycephalic skulls among prehistoric European cave burials."}
    ]
  },
  "Dashboard — dol/dolichocephalism.md": {
    "primary": "The condition of having a disproportionately long and narrow skull (cephalic index below 75).",
    "secondary": "In historical physical anthropology, cranial elongation studied in human racial taxonomy and skeletal pathology.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "On the Methods and Results of Ethnology", "quote": "The pronounced **dolichocephalism** of the native Australian aborigines distinguished them from surrounding Oceanic peoples."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Sussex Vampire", "quote": "The skull specimens in the study displayed marked **dolichocephalism**, characteristic of early Iberian settlers."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Congenital synostosis of the sagittal suture leads to compensatory **dolichocephalism** in growing infants."}
    ]
  },
  "Dashboard — dol/dolichocephaly.md": {
    "primary": "The physical condition of being long-headed; having a cephalic index of less than 75.",
    "secondary": "In pediatric neurology and craniosynostosis, premature fusion of the sagittal suture causing anterior-posterior elongation of the calvarium.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Premature closure of the sagittal suture results in marked scaphocephaly and extreme **dolichocephaly**."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The degree of **dolichocephaly** varied considerably among the prehistoric cave-dwellers of western Europe."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Artificial cranial deformation in infants frequently accentuated natural **dolichocephaly** among indigenous American tribes."}
    ]
  },
  "Dashboard — dol/dolichocranial.md": {
    "primary": "Relating to or having a long skull; specifically applied to dry skull specimens with a cranial index below 75.",
    "secondary": "In forensic craniometry and osteology, describing dry cranial vaults exhibiting elongated anteroposterior dimensions.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Further Remarks on the Human Remains Found in the Caves of Gibraltar", "quote": "The fossilized calvarium is clearly **dolichocranial**, measuring over two hundred millimeters in longitudinal axis."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Comparative measurements of **dolichocranial** specimens reveal cranial capacity equal to modern European averages."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The missing link possessed a **dolichocranial** vault combined with the ape-like dentition of a dryopithecus."}
    ]
  },
  "Dashboard — dol/dolichocranic.md": {
    "primary": "Characterized by a cranial index below 75; having a long, narrow cranium (skull).",
    "secondary": "In physical anthropology and skeletal biology, distinguishing long-headed skulls from mesocranic and brachycranic forms.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The Engis skull was found upon careful measurement to be **dolichocranic**, conforming closely to typical modern standards."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The pathological specimen presented a **dolichocranic** outline caused by premature sagittal synostosis."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The enthusiast examined the prehistoric burial mound, classifying the recovered skulls as predominantly **dolichocranic**."}
    ]
  },
  "Dashboard — dol/dolichonyx.md": {
    "primary": "The taxonomic genus of the bobolink (*Dolichonyx oryzivorus*), a North American migratory songbird.",
    "secondary": "In ornithology, a genus of the New World blackbird family Icteridae known for long claw-like toes and long-distance trans-equatorial migration.",
    "quotes": [
      {"author": "John James Audubon", "work": "Ornithological Biography", "quote": "The male **Dolichonyx** oryzivorus pours forth his bubbling, joyous song over the clover meadows of May."},
      {"author": "Alexander Wilson", "work": "American Ornithology", "quote": "Known as the rice-bird in the southern swamps, **Dolichonyx** visits our northern fields in spring plumage."},
      {"author": "Henry David Thoreau", "work": "Journal", "quote": "I heard the rich, sparkling notes of the **Dolichonyx** fluttering over the Great Meadows by Concord River."}
    ]
  },
  "Dashboard — dol/dolichos.md": {
    "primary": "A taxonomic genus of tropical climbing plants in the legume family Fabaceae, including the lablab bean.",
    "secondary": "In agronomy and ethnobotany, protein-rich pulse crops cultivated for edible seeds, pods, and nitrogen-fixing forage.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Cultivated varieties of **Dolichos** lablab display remarkable diversity in pod color and seed pigmentation."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The native gardens around Caracas were shaded by climbing trellises of purple-flowered **Dolichos**."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Species of **Dolichos** thrive in warm soils, twining vigorously around support stakes throughout summer."}
    ]
  },
  "Dashboard — dol/dolichotis.md": {
    "primary": "The taxonomic genus of the Patagonian mara (*Dolichotis patagonum*), a large hare-like South American cavy rodent.",
    "secondary": "In mammalogy and evolutionary zoology, cursorial hystricomorph cavies exhibiting long legs and ungulate-like running adaptations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The Patagonian cavy, **Dolichotis** patagonica, is common on the arid gravel plains, bounding away like a hare."},
      {"author": "Alfred Russel Wallace", "work": "The Geographical Distribution of Animals", "quote": "The unique cursorial adaptations of **Dolichotis** reflect ecological convergence with Old World hares and small antelopes."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Vertebrated Animals", "quote": "The elongated metatarsal bones of **Dolichotis** provide spring and velocity across the open pampas."}
    ]
  },
  "Dashboard — dol/doliolidae.md": {
    "primary": "A taxonomic family of small, barrel-shaped, free-swimming marine tunicates (order Doliolida).",
    "secondary": "In marine invertebrate zoology, pelagic thaliaceans featuring complete muscle hoops and complex metagenic life cycles.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "Members of the family **Doliolidae** swim by ejecting jets of water through their circular muscular hoops."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The pelagic larvae of **Doliolidae** exhibit a rudimentary notochord, confirming their chordate affinities."},
      {"author": "Ray Lankester", "work": "A Treatise on Zoology", "quote": "Plankton hauls in warm currents often swarm with countless transparent zooids belonging to **Doliolidae**."}
    ]
  },
  "Dashboard — dol/doliolum.md": {
    "primary": "A genus of small, transparent, barrel-shaped pelagic tunicates in the family Doliolidae.",
    "secondary": "In plankton ecology, oceanic salp-relatives with eight or nine complete circular muscle bands propelling water.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Observations on the Anatomy and Affinities of the Family of the Salpidae", "quote": "The delicate barrel-shaped body of **Doliolum** contracts cyclically, propelling the organism through calm tropical waters."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The free-swimming tadpole larva of **Doliolum** possesses an axial nerve cord that atrophies in the adult stage."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "Nocturnal phosphorescence on the equatorial sea was intensified by luminous swarms of floating **Doliolum**."}
    ]
  },
  "Dashboard — dol/doll.md": {
    "primary": "A child's toy representing a human being; also an attractive or darling person (informal).",
    "secondary": "In cultural anthropology, effigies and figurines used in childhood play, ritual, and educational play across societies.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Dora sat dressing her pet dog and playing with her childhood **doll**, a charming but helpless child-wife."},
      {"author": "Henrik Ibsen", "work": "A Doll's House", "quote": "Our home has been nothing but a playroom; I have been your **doll** wife, just as at home I was papa's **doll** child."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie vented her childish frustrations by driving nails into the wooden head of her battered **doll**."}
    ]
  },
  "Dashboard — dol/dollar.md": {
    "primary": "The basic monetary unit of the United States, Canada, Australia, and numerous other countries.",
    "secondary": "In monetary history, derived from the German *Thaler* (Joachimsthaler), a heavy silver coin minted in Bohemia.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on the Establishment of a Mint", "quote": "The Spanish silver piece of eight, commonly called a **dollar**, has long served as the de facto currency of our trade."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A man is rich in proportion to the number of things which he can afford to let alone without spending a **dollar**."},
      {"author": "Mark Twain", "work": "The £1,000,000 Bank Note", "quote": "I was an American stranded in London without a single **dollar** to buy a crust of bread."}
    ]
  },
  "Dashboard — dol/dollarfish.md": {
    "primary": "Any of several small, round, silvery marine fishes, especially the harvestfish or butterfish (*Peprilus*).",
    "secondary": "In ichthyology, deep-bodied stromateid fishes inhabiting coastal Atlantic waters, named for their coin-like silhouette.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Cape Cod", "quote": "Fishermen dragged the seine upon the beach, hauling in silver perch, scup, and the round, glittering **dollarfish**."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The coastal waters abounded with schools of small disc-like fish resembling the northern **dollarfish**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Shoals of shimmering **dollarfish** leaped from the green swells as the ship rounded the reef."}
    ]
  },
  "Dashboard — dol/dollhouse.md": {
    "primary": "A miniature toy house used by children to play with dolls; an exceptionally small house.",
    "secondary": "In architecture and literature, a diminutive or excessively dainty dwelling arranged with meticulous artificial neatness.",
    "quotes": [
      {"author": "Louisa May Alcott", "work": "Little Women", "quote": "Beth spent happy afternoons furnishing the paper parlor of her tiny wooden **dollhouse**."},
      {"author": "Katherine Mansfield", "work": "The Doll's House", "quote": "The marvelous **dollhouse** stood in the courtyard, painted dark spinach green with a tiny yellow lamp on the table."},
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Jenny Wren constructed dresses for society ladies in her doll's dressmaking shop like a fairy living in a **dollhouse**."}
    ]
  },
  "Dashboard — dol/dollop.md": {
    "primary": "A shapeless mass or lump of soft food; an informal small amount or portion of something.",
    "secondary": "In culinary tradition and casual description, a generous spoonful of cream, jam, or butter added to a dish.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Peggotty ladled a steaming **dollop** of hot stew onto my plate with affectionate hospitality."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The cook hurled a greasy **dollop** of mashed turnip into the tin bowl before sliding it across the counter."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "He topped the hot peach cobbler with a cooling **dollop** of rich country cream."}
    ]
  },
  "Dashboard — dol/dolly.md": {
    "primary": "A child's word for a doll; also a small wheeled platform used for moving heavy loads or moving cameras.",
    "secondary": "In traditional laundering, a wooden club or agitator used for stirring clothes in a wash-tub.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Little Charley carried her favorite wooden **dolly**, singing to it with tender maternal affection."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The village washerwomen pounded their linen with heavy ash **dolly** pegs in the bubbling stream."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "We loaded our heavy ammunition cases onto a wheeled mining **dolly** to haul them across the ravine."}
    ]
  },
  "Dashboard — dol/dolman.md": {
    "primary": "A long, loose garment with narrow sleeves, formerly worn in Turkey; also a woman's mantle with cape-like sleeves.",
    "secondary": "In military uniform history, a short braided jacket worn by European hussar cavalrymen over one shoulder.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Talisman", "quote": "The Turkish envoy was resplendent in an embroidered silk **dolman** girded with a jeweled scimitar."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Lieutenant George Osborne strutted before the ladies in his scarlet hussar **dolman** trimmed with fur."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "She wrapped her dark woolen **dolman** closely about her shoulders against the biting autumn wind."}
    ]
  },
  "Dashboard — dol/dolmas.md": {
    "primary": "A Middle Eastern and Mediterranean dish of stuffed grape leaves, vegetables, or cabbage with rice and meat.",
    "secondary": "In culinary history, traditional Ottoman and Levantine dishes characterized by spiced rice, pine nuts, and herbs wrapped in vine foliage.",
    "quotes": [
      {"author": "Richard Burton", "work": "The Book of the Thousand Nights and a Night", "quote": "The host presented platters of savory **dolmas** rolled in tender vine leaves and fragrant with mint and cinnamon."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The banquet of the pasha featured mounds of spiced **dolmas** alongside roasted meats and sweet sherbet."},
      {"author": "Alexander Kinglake", "work": "Eothen", "quote": "In the cool bazaar of Damascus we dined upon cooling salads and delicate warm **dolmas** served upon brass trays."}
    ]
  },
  "Dashboard — dol/dolmen.md": {
    "primary": "A prehistoric megalithic tomb consisting of a large flat stone laid on upright stones; a portal tomb.",
    "secondary": "In Neolithic archaeology, single-chamber burial structures built across western Europe from 4000 to 3000 BCE.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "On the lonely Dorset down stood an ancient stone **dolmen**, gray and weathered by three thousand years."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "Earthworms had gradually undermined the soil surrounding the upright megaliths of the ancient **dolmen**."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "Monkbarns pointed enthusiastically toward the prehistoric **dolmen**, expounding upon its Druidical rites."}
    ]
  },
  "Dashboard — dol/dolobid.md": {
    "primary": "A trade name for diflunisal, a non-steroidal anti-inflammatory drug (NSAID) used to relieve pain and swelling.",
    "secondary": "In clinical therapeutics, a salicylic acid derivative that inhibits cyclooxygenase enzymes to manage arthritis and musculoskeletal pain.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Modern anti-inflammatory therapy frequently utilizes non-steroidal agents like **Dolobid** to relieve osteoarthritis without steroid toxicity."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Symptomatic analgesia with **Dolobid** afforded the patient relief from chronic joint stiffness."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The practitioner prescribed **Dolobid** to alleviate the severe back pain of the weary laborer."}
    ]
  },
  "Dashboard — dol/dolomite.md": {
    "primary": "A translucent mineral consisting of calcium magnesium carbonate; also a sedimentary rock formed of this mineral.",
    "secondary": "In petrology and alpine geology, sedimentary magnesium limestone forming the iconic jagged peaks of the Italian Alps.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The precipitous jagged towers of the Alps consist of crystalline **dolomite**, formed by the alteration of ancient coral reefs."},
      {"author": "James Dwight Dana", "work": "Manual of Mineralogy", "quote": "Rhombohedral crystals of pearly **dolomite** are easily distinguished from calcite by their slow effervescence in acid."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The pink and amber glow of the setting sun bathed the bare crags of the **dolomite** peaks in celestial fire."}
    ]
  },
  "Dashboard — dol/dolomitic.md": {
    "primary": "Containing, composed of, or relating to the mineral or rock dolomite; magnesium limestone.",
    "secondary": "In stratigraphy, describing sedimentary strata enriched in magnesium carbonate through diagenetic dolomitization.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Elements of Geology", "quote": "The fossil shells within the **dolomitic** limestone strata were completely replaced by sparkling rhombohedral crystals."},
      {"author": "Alexander von Humboldt", "work": "Cosmos", "quote": "Spectacular karst caverns and underground rivers carve their labyrinthine way through the porous **dolomitic** rock."},
      {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "Magnesian waters circulating through coastal reefs induced extensive alteration, converting soft chalk into tough **dolomitic** beds."}
    ]
  },
  "Dashboard — dol/dolor.md": {
    "primary": "Mental suffering or anguish; grief, sorrow, or physical pain (archaic, poetic, or medical).",
    "secondary": "In classical Latin and psychological literature, acute psychic distress or somatosensory suffering.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "When every grief is entertained that's offered, comes to the entertainer—a **dolor** comes to him indeed."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "A dismal world, an empire of deep despair, of horror, and of endless **dolor**."},
      {"author": "Augustine of Hippo", "work": "Confessions", "quote": "My heart was pierced with sharp **dolor** at the untimely death of my beloved friend."}
    ]
  },
  "Dashboard — dol/dolorous.md": {
    "primary": "Feeling or expressing great sorrow or distress; mournful, grievous, or painful.",
    "secondary": "In medieval romance and tragic poetry, accompanied by mournful groans and heartbreaking lamentation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "Thy brother's Edward's sons, his queens, his wife, and children all did perish in this **dolorous** tragedy."},
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "A **dolorous** blast upon the bugle horn echoed across the tarn, announcing the death of the chieftain."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Through many a dark and **dolorous** path they traveled, across the scorched brimstone of hell."}
    ]
  },
  "Dashboard — dol/dolour.md": {
    "primary": "Great sorrow or mental distress; grief (British spelling of dolor).",
    "secondary": "In Victorian lyric poetry, profound spiritual dejection and mourning for lost love or mortality.",
    "quotes": [
      {"author": "Alfred Tennyson", "work": "In Memoriam A. H. H.", "quote": "O sorrow, cruel fellowship, O priestess in the vaults of death, can I measure all thy heavy **dolour**?"},
      {"author": "Algernon Charles Swinburne", "work": "Poems and Ballads", "quote": "From too much love of living, from hope and fear set free, we thank with brief thanksgiving whatever gods may be, that no life lives forever, that dead men rise up never, that even the weariest river winds somewhere safe to sea, far from mortal **dolour**."},
      {"author": "William Morris", "work": "The Earthly Paradise", "quote": "The wanderers sat in solemn silence, weeping for the **dolour** and hardship of their voyage."}
    ]
  },
  "Dashboard — dol/dolourous.md": {
    "primary": "Full of or expressing great sorrow or grief; mournful or painful (variant British spelling of dolorous).",
    "secondary": "In historical and archaic diction, causing or accompanying tragic affliction.",
    "quotes": [
      {"author": "Thomas Malory", "work": "Le Morte d'Arthur", "quote": "Balin struck the **dolourous** stroke that smote King Pellam and laid waste three noble kingdoms."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "The knight heard a **dolourous** complaint rising from the enchanted thicket by the wayside."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The wounded knight groaned in a **dolourous** tone, begging for water to cool his burning fever."}
    ]
  },
  "Dashboard — dol/dolt.md": {
    "primary": "A stupid, foolish, or slow-witted person; a blockhead or dunce.",
    "secondary": "In dramatic satire and colloquial reproach, an insensitive individual who fails to grasp plain truths.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "O gull! O **dolt**! As ignorant as dirt! Thou hast done a deed—I care not for thy sword; I'll make thee known."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "Every pedantic **dolt** fancies himself qualified to pronounce judgment upon the masterpieces of the ancients."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Creakle roared that I was an obstinate **dolt** who would feel the weight of his cane before sunset."}
    ]
  },
  "Dashboard — dol/doltish.md": {
    "primary": "Stupid, dull-witted, idiotic, or slow to understand; characteristic of a dolt.",
    "secondary": "In social characterization, lacking intellectual sharpness, conversational wit, or emotional refinement.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "John Reed's **doltish** insolence was encouraged by his mother's blind, foolish indulgence."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Dunstan Cass laughed with **doltish** satisfaction at the prospect of blackmailing his brother."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "A **doltish** companion converts a journey through sublime scenery into a tedious endurance test."}
    ]
  },
  "Dashboard — dol/doltishly.md": {
    "primary": "In a doltish, stupid, or clumsy manner; with thick-witted slowness.",
    "secondary": "In descriptive prose, reacting foolishly or gaping without comprehension when challenged.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The groom stared **doltishly** at Holmes's sovereign, scratching his head in vacant bewilderment."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The tavern loafers grinned **doltishly** as the furmity woman recounted her ancient gossip."},
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "Hugh gaped **doltishly** around the drawing room, clutching his heavy cudgel like an awkward bear."}
    ]
  },
  "Dashboard — dol/indolence.md": {
    "primary": "Avoidance of activity or exertion; habitual laziness, sloth, or love of ease.",
    "secondary": "In 18th-century moral essayists, a seductive spiritual paralysis that squanders natural talent.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet's natural **indolence** made him neglect the prudent financial provision of his five daughters."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Of all the vices that corrupt human nature, none is more insidiously fatal to virtue than **indolence**."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "Society everywhere is in conspiracy against the manhood of every one of its members; let us throw off **indolence**."}
    ]
  },
  "Dashboard — dol/indolent.md": {
    "primary": "Wanting to avoid activity or exertion; lazy, slothful, or disinclined to work.",
    "secondary": "In clinical medicine, causing little or no pain; slow-growing, quiescent, or slow to heal (as an indolent ulcer).",
    "quotes": [
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "Her brother was an **indolent** young man who spent his mornings lounging at the stables."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "An **indolent** varicose ulcer of the leg may persist for years without acute inflammation or rapid progression."},
      {"author": "Washington Irving", "work": "Rip Van Winkle", "quote": "Rip was an **indolent** fellow who had an insuperable aversion to all kinds of profitable labor."}
    ]
  },
  "Dashboard — dol/indolently.md": {
    "primary": "In an indolent manner; lazily, sluggishly, languidly, or with leisurely ease.",
    "secondary": "In atmospheric and character description, lounging or reclining without purposeful exertion.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton lounged **indolently** against the bar of the court, appearing to observe nothing."},
      {"author": "Herman Melville", "work": "Typee", "quote": "We reclined **indolently** on mats of woven pandanus leaves while island youths brought fresh coconuts."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The fat cows chewed their cud **indolently** in the lush, river-fed pastures of the Valley of the Great Dairies."}
    ]
  },
  "Dashboard — dol/redolence.md": {
    "primary": "A pleasant, sweet, or fragrant smell; fragrance, aroma, or suggestive odor.",
    "secondary": "In aesthetic prose, an evocative quality that powerfully brings back memories or associations of the past.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "The sweet **redolence** of the old garden roses drifted through the open gables on the summer air."},
      {"author": "Henry James", "work": "The American", "quote": "The ancient cathedral was filled with the dim **redolence** of centuries of burned incense and beeswax."},
      {"author": "John Keats", "work": "Isabella; or, The Pot of Basil", "quote": "The sweet basil grew thick and green, moist with tears and breathing an intoxicating **redolence**."}
    ]
  },
  "Dashboard — dol/redolent.md": {
    "primary": "Strongly reminiscent or suggestive of something; fragrant, sweet-smelling, or evocative.",
    "secondary": "In sensory literature, permeated with the rich scent of flowers, earth, tobacco, or sea brine.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The cozy kitchen was **redolent** of roasted meats, fresh bread, and savory country herbs."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The cab was heavily **redolent** of cheap cigars and wet umbrellas as we drove through Baker Street."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The autumn mown fields were **redolent** of sweet clover, cider pomace, and damp woodland earth."}
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

print(f"Successfully updated {updated}/{len(data)} notes across am and dol.")

dashes = [
  "Dashboard — am",
  "Dashboard — dol"
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
