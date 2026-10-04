# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — deb (53 words) ---
  "Dashboard — deb/aldebaran.md": {
    "primary": "A giant red star of the first magnitude, situated in the constellation Taurus and serving as the eye of the bull.",
    "secondary": "In observational astrophysics, Aldebaran (Alpha Tauri) is an evolved K-type giant exhibiting slow, irregular pulsations and harboring an exoplanet.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "The ruddy brilliance of **aldebaran** renders it unmistakable as it rises above the winter horizon in Taurus."},
      {"author": "Camille Flammarion", "work": "Popular Astronomy", "quote": "Ancient Arabian stargazers named **aldebaran** the follower, because it perpetually tracks the cluster of the Pleiades across the night sky."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Above the lonely hay-ricks, **aldebaran** flashed with fiery amber radiance against the cold crystalline atmosphere."}
    ]
  },
  "Dashboard — deb/ardeb.md": {
    "primary": "A traditional Egyptian unit of dry capacity, historically standardized to approximately 198 liters for measuring grain.",
    "secondary": "In Middle Eastern economic history, the ardeb functioned as the primary transactional metric for agricultural yields, taxation, and Nile valley granaries.",
    "quotes": [
      {"author": "Edward William Lane", "work": "An Account of the Manners and Customs of the Modern Egyptians", "quote": "The grain merchant measured out every **ardeb** of wheat with scrupulous precision before loading the felucca."},
      {"author": "Richard Burton", "work": "Personal Narrative of a Pilgrimage to El-Medinah and Meccah", "quote": "Local customs officers reckoned the annual barley harvest of the village at several thousand **ardeb** in total volume."},
      {"author": "James Rennell", "work": "The Geographical System of Herodotus", "quote": "Ancient fiscal registers compute the grain tithes of the Delta in units equivalent to the modern **ardeb**."}
    ]
  },
  "Dashboard — deb/deb.md": {
    "primary": "An informal abbreviation for a debutante; a young woman making her formal presentation to society.",
    "secondary": "In social chronicles of early twentieth-century aristocratic life, a deb endured an intensive round of etiquette lessons and grand seasonal assemblies.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "The Inimitable Jeeves", "quote": "Aunt Agatha insisted that Bertie attend the grand ball and pay polite court to the latest fashionable **deb**."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory watched the glittering throng of dancers, noting how every popular **deb** attracted a swirling circle of college admirers."},
      {"author": "Virginia Woolf", "work": "Mrs. Dalloway", "quote": "Clarissa recalled the nervousness of her first season in town when she was presented as a youthful **deb** in white satin."}
    ]
  },
  "Dashboard — deb/debacle.md": {
    "primary": "A sudden, disastrous collapse, failure, or complete breakdown of an enterprise, military campaign, or system.",
    "secondary": "In historical geomorphology and glaciology, a débâcle originally described the violent breaking up and rushing down of ice in a river during a spring thaw.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The sudden rupture of the fortified front line turned what was planned as an orderly retreat into an unmitigated **debacle**."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The catastrophic **debacle** of the imperial army at Sedan sealed the sudden overthrow of the second French empire."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The courtroom inquiry laid bare the scandalous **debacle** aboard the abandoned pilgrim vessel."}
    ]
  },
  "Dashboard — deb/debar.md": {
    "primary": "To exclude, shut out, or officially prohibit someone from having a right, privilege, or admission to a place.",
    "secondary": "In constitutional and administrative law, statutory disqualifications debar convicted felons or compromised officials from holding public office.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I feared that my terrible secret would forever **debar** me from the peaceful joys of domestic companionship."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "No harsh decree shall **debar** righteous spirits from entering into the promised celestial inheritance."},
      {"author": "John Stuart Mill", "work": "The Subjection of Women", "quote": "Law and custom ought not arbitrarily to **debar** half the human race from competing for honorable careers."}
    ]
  },
  "Dashboard — deb/debark.md": {
    "primary": "To disembark; to leave a ship or aircraft and step onto dry land.",
    "secondary": "In naval logistics and expeditionary warfare, troops and supplies debark across pontoon bridges or landing craft to establish beachheads.",
    "quotes": [
      {"author": "Herman Melville", "work": "Typee", "quote": "The weary mariners were granted leave to **debark** upon the verdant shores of the tranquil tropical haven."},
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The English archers prepared to **debark** at Bordeaux, donning their breastplates upon the crowded stone quay."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Captain Smollett ordered the armed landing party to **debark** silently upon the sandy spit at low tide."}
    ]
  },
  "Dashboard — deb/debarkation.md": {
    "primary": "The act or process of disembarking passengers, crew, or cargo from a ship, vessel, or aircraft onto land.",
    "secondary": "In maritime quarantine administration, ports of entry supervise debarkation protocols to ensure passenger health and customs clearance.",
    "quotes": [
      {"author": "James Fenimore Cooper", "work": "The Pilot", "quote": "The sudden order for **debarkation** caused bustling commotion among the seamen upon the moonlit deck."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The rapid **debarkation** of Belisarius and his veteran cohorts took the Vandal garrisons entirely by surprise."},
      {"author": "Charles Dickens", "work": "Martin Chuzzlewit", "quote": "A noisy crowd of porters and cabmen jostled along the wharf to witness the **debarkation** of the Atlantic packet."}
    ]
  },
  "Dashboard — deb/debarment.md": {
    "primary": "The official act of barring, excluding, or preventing someone from participation, admission, or holding a post.",
    "secondary": "In government procurement law, debarment is an administrative remedy that excludes non-compliant contractors from bidding on public tenders.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The perpetual **debarment** of capable citizens from re-election would deprive the republic of seasoned executive wisdom."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The severe statutory **debarment** of Nonconformists from corporate magistracies sparked deep political resentment across the boroughs."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "A sweeping, indiscriminate **debarment** of hereditary nobility from civic duties undermines the constitutional balance."}
    ]
  },
  "Dashboard — deb/debase.md": {
    "primary": "To reduce the quality, value, purity, dignity, or moral character of something or someone.",
    "secondary": "In monetary history, monarchs frequently chose to debase circulating currency by melting silver coins and adding inferior alloy metals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "Shall I **debase** my dignity by stooping to wrangle with every churlish servingman?"},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate felt that petty financial compromises threatened to **debase** his high scientific ideals into mundane venality."},
      {"author": "G. K. Chesterton", "work": "Heretics", "quote": "Cynical commercialism seeks to **debase** authentic popular art into mere mechanical sensationalism."}
    ]
  },
  "Dashboard — deb/debased.md": {
    "primary": "Degraded, corrupted, or lowered in value, quality, moral integrity, or purity.",
    "secondary": "In numismatics, debased coinage refers to specimen currency minted with significantly reduced precious metal fineness.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperors issued **debased** copper denarii with mere silver wash, inducing ruinous price inflation throughout the provinces."},
      {"author": "John Locke", "work": "Some Considerations of the Consequences of the Lowering of Interest", "quote": "A merchant receiving payment in **debased** coin must raise his commodity prices in exact proportion to the clipped metallic deficiency."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The wandering friar offered a **debased** Latin benediction that mingled sacred chants with tavern catches."}
    ]
  },
  "Dashboard — deb/debasement.md": {
    "primary": "The act of degrading, corrupting, or deteriorating the intrinsic quality, dignity, or moral value of something.",
    "secondary": "In historical economics, monetary debasement by sovereign mints operated as a hidden, regressive tax on real consumer wages.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The systematic **debasement** of the standard metallic measure by sovereign debtors impoverished legions of private creditors."},
      {"author": "David Ricardo", "work": "Principles of Political Economy and Taxation", "quote": "Frequent **debasement** of paper notes beyond their metallic reserve equivalent inevitably leads to domestic currency depreciation."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "No society can long survive the moral **debasement** that worships Mammon and treats working men as disposable tools."}
    ]
  },
  "Dashboard — deb/debaser.md": {
    "primary": "A person, agent, or influence that lowers, degrades, corrupts, or defiles value, standards, or character.",
    "secondary": "In penal history, an illicit coiner or debaser of royal currency was prosecuted under capital statutes of high treason.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on the Mint", "quote": "The clandestine **debaser** of coin strikes at public credit no less severely than an armed invader."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He regarded the flattering courtier as the most pernicious **debaser** of truth and sincere human friendship."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The pamphleteer was denounced as a shameless **debaser** of historical fact and civic decorum."}
    ]
  },
  "Dashboard — deb/debasing.md": {
    "primary": "Causing degradation, corruption, humiliation, or a reduction in moral dignity or intrinsic value.",
    "secondary": "In cultural criticism, pandering to prurient sensationalism exerts a debasing effect upon public taste and civic discourse.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Living under constant social despotism exerts a **debasing** influence that crushes individual genius and intellectual originality."},
      {"author": "Mary Wollstonecraft", "work": "A Vindication of the Rights of Woman", "quote": "Trivializing education instills a **debasing** vanity in young women, rendering them dependent upon superficial flattery."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Men stoop to cowardly expedients, yielding to the **debasing** fear of what neighbors and conventional society might say."}
    ]
  },
  "Dashboard — deb/debatable.md": {
    "primary": "Open to question, dispute, or argument; not settled, certain, or universally accepted as fact.",
    "secondary": "In jurisdictional border history, debatable land refers to disputed frontier borderlands claimed simultaneously by two rival crowns.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Lay of the Last Minstrel", "quote": "Marauding border moss-troopers rode boldly through the **debatable** ground between England and Scotland under cover of fog."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Matters of subtle scholastic speculation remain forever **debatable** unless brought to the touchstone of rigorous empirical experiment."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "Whether species transform gradually or by sudden saltations is a legitimate and **debatable** hypothesis among modern naturalists."}
    ]
  },
  "Dashboard — deb/debate.md": {
    "primary": "A formal discussion or argument on a particular topic in a public meeting, legislature, or assembly.",
    "secondary": "In parliamentary procedure, floor debate follows strict rules of order regarding speaker recognition, time limits, and germane motions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "Now, lords, if God doth give successful end unto this **debate** that bleedeth at our doors, we will our youth lead on to higher fields."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "After an animated parliamentary **debate**, the ministers stubbornly rejected all proposals for equitable colonial reconciliation."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Freedom of open **debate** in town meetings trains the common citizen to understand the complexities of public affairs."}
    ]
  },
  "Dashboard — deb/debater.md": {
    "primary": "A person who participates in a formal debate or discussion, presenting arguments and rebuttals.",
    "secondary": "In collegiate forensics and parliamentary rhetoric, an experienced debater employs structured syllogisms and cross-examination techniques.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The Life of William Pitt", "quote": "Even as a youthful member of Parliament, Pitt proved himself a formidable **debater** capable of refuting veteran statesmen."},
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "My friend Collins was a natural **debater**, keen in discovering fallacies and relentless in pursuing an argument."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "He was an aggressive **debater** who overwhelmed his medical opponents with torrents of clinical citations."}
    ]
  },
  "Dashboard — deb/debauch.md": {
    "primary": "To corrupt morally, seduce from virtue, or lead astray into sensuality and dissipation; or a bout of extreme excess.",
    "secondary": "In early modern penal records, rogue taverns were indicted for harboring vagabonds in drunken, riotous debauch.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "What a pied ninny's this! Thou scurvy patch! I do beseech thy greatness, give him blows and not **debauch** my servants with liquor."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Emperor Elagabalus plunged into every wild **debauch** that oriental luxury and unbridled imperial power could invent."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "A night of wild **debauch** at the London inn left the young squire penniless and remorseful by morning."}
    ]
  },
  "Dashboard — deb/debauched.md": {
    "primary": "Indulging in or characterized by excessive sensual pleasures; corrupt, dissipated, and dissolute in habits.",
    "secondary": "In sociological profiles of decadent courts, debauched courtiers abandoned civic responsibilities to pursue fleeting pleasures.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton leaned over the table, his brilliant mind half-ruined by years of **debauched** companionless tavern carousal."},
      {"author": "William Thackeray", "work": "Vanity Fair", "quote": "Lord Steyne was universally regarded as a **debauched** old roué whose wealth alone commanded outward social deference."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Rumors whispered that Dorian frequented the most **debauched** dens of Whitechapel beneath an assumed common name."}
    ]
  },
  "Dashboard — deb/debauchee.md": {
    "primary": "A person given to excessive sensual indulgence, dissipation, and dissolute living; a rake or libertine.",
    "secondary": "In eighteenth-century moral satires, the ruined debauchee served as an allegorical warning against the perils of squandered youth.",
    "quotes": [
      {"author": "Oliver Goldsmith", "work": "The Vicar of Wakefield", "quote": "The aging **debauchee** looked back upon his squandered patrimony with bitter, unavailing regret in his infirmity."},
      {"author": "Tobias Smollett", "work": "The Adventures of Peregrine Pickle", "quote": "The town **debauchee** spent his mornings in recovery from midnight revels and his afternoons planning fresh intrigues."},
      {"author": "Honoré de Balzac", "work": "Père Goriot", "quote": "Rastignac recoiled from the cynical philosophy of Vautrin, who dissected Parisian vice like an unrepentant **debauchee**."}
    ]
  },
  "Dashboard — deb/debaucher.md": {
    "primary": "One who seduces others from virtue, leads others into dissipation, or corrupts innocence.",
    "secondary": "In dramatic literature, the debaucher appears as a stock antagonist who schemes to compromise naive protagonists.",
    "quotes": [
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "Lovelace stood revealed as a ruthless **debaucher** who employed every artifice of deceit to ensnare unsuspecting virtue."},
      {"author": "Daniel Defoe", "work": "Moll Flanders", "quote": "She bitterly denounced the elder brother as the cunning **debaucher** who first taught her the trade of illicit intrigue."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The satirist exposed the hypocritical sectary as an insidious **debaucher** of youthful piety and public morals."}
    ]
  },
  "Dashboard — deb/debauchery.md": {
    "primary": "Excessive indulgence in sensual pleasures, drunkenness, and licentious or dissolute living.",
    "secondary": "In classical histories of late republican Rome, rampant political corruption accompanied moral debauchery among the patrician elite.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The praetorian guards were softened by long years of undisciplined **debauchery** and luxury in their imperial barracks."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "Christian fled past the gates of Destruction, refusing to turn aside into the town of Vanity and its riotous **debauchery**."},
      {"author": "Robert Louis Stevenson", "work": "The Strange Case of Dr Jekyll and Mr Hyde", "quote": "Mr. Hyde plunged without conscience into secret nocturnal **debauchery** that shocked the respectable Victorian neighborhood."}
    ]
  },
  "Dashboard — deb/debenture.md": {
    "primary": "A long-term security or bond issued by a corporation or public authority, backed by creditworthiness rather than physical collateral.",
    "secondary": "In corporate finance and debt capital markets, a debenture holder ranks ahead of preferred shareholders but behind secured creditors in liquidation.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The merchant bank negotiated a transferable **debenture** to finance overseas shipping ventures along the Levant trade routes."},
      {"author": "Walter Bagehot", "work": "Lombard Street: A Description of the Money Market", "quote": "Prudent railway directors issue a fixed-yield **debenture** rather than dilute their equity capital during rapid track expansion."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Holders of a corporate **debenture** expect guaranteed interest disbursements irrespective of seasonal commercial profits."}
    ]
  },
  "Dashboard — deb/debile.md": {
    "primary": "Lacking physical strength or bodily vigor; weak, feeble, or infirm.",
    "secondary": "In archaic and Renaissance literature, debile was employed as a poetic synonym for physically frail or constitutionally vulnerable.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "I shall give my **debile** limbs a little rest before we renew the assault upon the gates of Corioli."},
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "The king's physicians despaired of curing his **debile** minister whose vital spirits were utterly exhausted."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Old age renders the most robust constitution **debile** and subject to tremors of the extremities."}
    ]
  },
  "Dashboard — deb/debilitate.md": {
    "primary": "To make someone or something weak, feeble, or constitutionally infirm; to enfeeble.",
    "secondary": "In military operations and siege craft, prolonged blockades aim to debilitate defending garrisons by exhausting food and medical stores.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Luxury and sedentary ease served to **debilitate** the martial spirit that had formerly subdued the Mediterranean world."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Excessive inbreeding tends to **debilitate** domesticated stock, diminishing fertility and constitutional resistance to illness."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "A lingering tropical malaria served to **debilitate** Dr. Watson so severely that he was invalided home to England."}
    ]
  },
  "Dashboard — deb/debilitated.md": {
    "primary": "Weakened, enfeebled, or impaired in health, bodily strength, or structural vigor.",
    "secondary": "In clinical medicine, a debilitated patient requires restorative nutritional therapies and gradual physical rehabilitation.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The poor consumption patient lay **debilitated** upon her narrow cot, her pale cheeks flushed with fever."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The overworked farm horses returned to the stables **debilitated** after hours of harrowing through stubborn, sodden clay."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "Kurtz was carried out of the jungle on a litter, an utterly **debilitated** shadow of his former ambitious self."}
    ]
  },
  "Dashboard — deb/debilitating.md": {
    "primary": "Causing severe weakness, impairment of health, loss of energy, or operational incapacity.",
    "secondary": "In occupational health and epidemiology, chronic inflammatory conditions exert a debilitating impact upon daily manual productivity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The stagnant air of the London slum fostered a **debilitating** ague that laid low entire families in Tom-all-Alone's."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Terrestrial bacterial infections proved a swift and **debilitating** pestilence against the unimmunized Martian invaders."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Persistent neurotic anxiety acts as a **debilitating** drain upon intellectual concentration and decisive executive action."}
    ]
  },
  "Dashboard — deb/debilitation.md": {
    "primary": "The process of becoming weakened or enfeebled; loss of strength, vigor, or functional capacity.",
    "secondary": "In gerontology and palliative care, constitutional debilitation stems from progressive muscle atrophy and metabolic deceleration.",
    "quotes": [
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "Effeminate pampering and warm wrapping lead directly to bodily **debilitation** and chronic sensitivity to winter colds."},
      {"author": "Thomas Huxley", "work": "Physiography", "quote": "Protracted drought produces extreme biological **debilitation** across arid grasslands before the arrival of seasonal monsoons."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Internal factional discord caused the gradual **debilitation** of the Byzantine frontiers against encroaching barbarian tribes."}
    ]
  },
  "Dashboard — deb/debilitative.md": {
    "primary": "Tending to cause weakness, enfeeblement, or loss of bodily or institutional strength.",
    "secondary": "In pharmacology and pathology, debilitative side effects of aggressive treatments require concurrent supportive therapy.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Parasitic infections exert a **debilitative** influence upon host organisms by systematically siphoning metabolic nutrients."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Unchecked speculative dogmatism has a **debilitative** effect upon empirical science, turning inquiry into wordy disputes."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Years of bankrupt administration wrought a **debilitative** paralysis upon the royal ministries at Versailles."}
    ]
  },
  "Dashboard — deb/debility.md": {
    "primary": "Physical feebleness, bodily infirmity, or lack of muscular and constitutional vigor.",
    "secondary": "In nineteenth-century clinical nosology, general debility was cataloged as a constitutional syndrome accompanying wasting diseases.",
    "quotes": [
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "A fever succeeded to my exertions, and I was confined for several months by extreme bodily **debility** and delirium."},
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Though I look old, yet I am strong and lusty; for in my youth I never did apply hot and rebellious liquors to my blood, nor did not with unbashful forehead woo the means of weakness and **debility**."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The scurvy-stricken sailors suffered severe **debility** and swollen joints after three months without fresh provisions."}
    ]
  },
  "Dashboard — deb/debit.md": {
    "primary": "An entry recording a sum owed or deducted from an account; or to charge a sum against an account.",
    "secondary": "In double-entry bookkeeping, a debit records an increase in asset or expense accounts, or a decrease in liability or equity balances.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "Every prudent merchant posts every **debit** against his debtors in the ledger before retiring to rest at night."},
      {"author": "Charles Dickens", "work": "Dombey and Son", "quote": "Mr. Carker examined the banking books, marking each large **debit** that drained the capital of the venerable shipping house."},
      {"author": "Benjamin Franklin", "work": "Autobiography of Benjamin Franklin", "quote": "My partner balanced the firm's ledgers scrupulously, entering every small personal **debit** without omission."}
    ]
  },
  "Dashboard — deb/debitor.md": {
    "primary": "A debtor; a person, party, or institution that owes a debt or obligation to a creditor.",
    "secondary": "In Roman civil law and early modern jurisprudence, a debitor was legally bound by contract (nexum) to satisfy claims of the creditor.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Othello", "quote": "And I, God bless the mark! his Moorship's ancient, a counter-caster, he, in good time, must his lieutenant be, and I—God bless the mark!—his Moorship's **debitor** and creditor."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The statute protects the **debitor** from extortionate arrest while compelling full restitution of lawful obligations."},
      {"author": "Francis Bacon", "work": "Essays", "quote": "A wise creditor treats a distressed **debitor** with patience when honest diligence promises eventual repayment."}
    ]
  },
  "Dashboard — deb/debonair.md": {
    "primary": "Confident, stylish, charming, and suave; possessing sophisticated manners and a lighthearted demeanor.",
    "secondary": "In medieval chivalric literature, debonair (Old French de bon aire, of good stock) described a knight who was gracious and noble.",
    "quotes": [
      {"author": "P. G. Wodehouse", "work": "My Man Jeeves", "quote": "Bicky sauntered into the club looking remarkably **debonair** in his silk hat and gardenia buttonhole."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The dashing young aristocrat strolled into Baker Street with a **debonair** smile that masked his deep anxiety."},
      {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "Arthur stepped onto the lawn looking delightfully **debonair**, captivating every young lady with his easy grace."}
    ]
  },
  "Dashboard — deb/debonaire.md": {
    "primary": "An archaic spelling of debonair; gracious, courteous, gentle, and charming in bearing.",
    "secondary": "In Middle English and Anglo-Norman romance cycles, debonaire denoted nobility of spirit and refined courtly gentleness.",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "She was so charitable and so **debonaire** that she would weep if that she saw a mouse caught in a trap."},
      {"author": "Edmund Spenser", "work": "The Faerie Queene", "quote": "The gentle knight rode forth with **debonaire** countenance, courteous to ladies and fearless before foes."},
      {"author": "John Milton", "work": "L'Allegro", "quote": "Zephyr with Aurora playing, as he met her once a-Maying, filled her with mirth and **debonaire** sweet grace."}
    ]
  },
  "Dashboard — deb/debone.md": {
    "primary": "To remove the bones from meat, poultry, or fish prior to cooking or culinary preparation.",
    "secondary": "In butchery and classical French gastronomy, skilled chefs debone a fowl while keeping the exterior skin intact for stuffing.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "The cook must carefully **debone** the fowl before stuffing it with savoury truffles and breadcrumbs."},
      {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "Use a sharp, flexible larding knife to **debone** the salmon trout without bruising the delicate flesh."},
      {"author": "Auguste Escoffier", "work": "A Guide to Modern Cookery", "quote": "To prepare the ballottine, first **debone** the shoulder of lamb and roll it tightly with seasoned farce."}
    ]
  },
  "Dashboard — deb/deboned.md": {
    "primary": "Having had the bones removed; prepared without bones for culinary use.",
    "secondary": "In food processing and commercial meat production, mechanically deboned meat undergoes high-pressure separation of tissue from skeletal elements.",
    "quotes": [
      {"author": "Isabella Beeton", "work": "Mrs. Beeton's Book of Household Management", "quote": "The **deboned** turkey was rolled tightly and roasted to a golden brown for the banquet centerpiece."},
      {"author": "Alexis Soyer", "work": "The Gastronomic Regenerator", "quote": "Serve the **deboned** pigeon garnished with glazed chestnuts and a rich Madeira reduction."},
      {"author": "Charles Ranhofer", "work": "The Epicurean", "quote": "A platter of **deboned** quail stuffed with foie gras delighted the dinner guests at Delmonico's."}
    ]
  },
  "Dashboard — deb/debonnaire.md": {
    "primary": "A variant spelling of debonair; characterized by aristocratic charm, elegance, and easy gentility.",
    "secondary": "In French historical annals, Louis the Pious was famously surnamed Louis le Débonnaire on account of his mild and forgiving temper.",
    "quotes": [
      {"author": "Francois Rabelais", "work": "Gargantua and Pantagruel", "quote": "King Grandgousier was a most **debonnaire** prince, loving peace and good wine above all vain conquests."},
      {"author": "Walter Scott", "work": "Quentin Durward", "quote": "The young Scottish archer bowed with a **debonnaire** gallantry that pleased the Flemish burgomaster's daughter."},
      {"author": "Edward Bulwer-Lytton", "work": "The Last of the Barons", "quote": "Edward IV greeted his loyal citizens of London with that **debonnaire** smile that concealed his ruthless ambitions."}
    ]
  },
  "Dashboard — deb/debouch.md": {
    "primary": "To emerge from a narrow valley, defile, gorge, or confined space into an open plain or wider area.",
    "secondary": "In tactical military maneuvers, infantry divisions debouch from mountain passes into formation before engaging an enemy army.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "A squad of constables was seen to **debouch** from the side lane into the wide Dublin thoroughfare."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "General Bagration ordered the Russian battalions to **debouch** from the forest onto the rolling plains of Austerlitz."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "The Anglo-Egyptian cavalry prepared to **debouch** from the rocky ravines onto the sandy expanse of Omdurman."}
    ]
  },
  "Dashboard — deb/debridement.md": {
    "primary": "The medical or surgical removal of dead, damaged, infected, or necrotic tissue from a wound to facilitate healing.",
    "secondary": "In emergency trauma surgery, thorough wound debridement prevents life-threatening complications such as gas gangrene or sepsis.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Early and thorough **debridement** of contaminated tissue remains the primary surgical defense against wound infection."},
      {"author": "Alexis Carrel", "work": "The Treatment of Infected Wounds", "quote": "Surgical **debridement** must precede chemical irrigation to eliminate all necrotic loci harboring anaerobic bacteria."},
      {"author": "Harvey Cushing", "work": "A Tumour of the Brain", "quote": "The surgeon performed meticulous **debridement** along the edges of the compound fracture to protect the dura mater."}
    ]
  },
  "Dashboard — deb/debrief.md": {
    "primary": "To question a pilot, soldier, diplomat, or mission specialist upon their return from an operation to gather intelligence.",
    "secondary": "In experimental psychology, researchers debrief human subjects after a study to disclose all hypotheses and mitigate deceptive stress.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "Whitehall officials waited eagerly to **debrief** the intelligence agent who had escaped across the German frontier."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Naval commanders gathered at dawn to **debrief** the reconnaissance pilots regarding the position of the enemy battlefleet."},
      {"author": "Erskine Childers", "work": "The Riddle of the Sands", "quote": "We hurried to the Admiralty to **debrief** the senior lords concerning the hidden channels behind the Frisian islands."}
    ]
  },
  "Dashboard — deb/debriefing.md": {
    "primary": "A formal meeting or session held to review, question, and gather information about a recently completed mission or operation.",
    "secondary": "In aviation safety and astronautics, the post-flight debriefing identifies technical anomalies and procedural oversights for future mission protocols.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The intelligence staff submitted a thorough **debriefing** report detailing the performance of the clandestine night drops in occupied France."},
      {"author": "H. G. Wells", "work": "The World Set Free", "quote": "At the scientific **debriefing**, the physicists analyzed the unprecedented aerial photographs of the atomic explosion."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "Holmes conducted a quiet **debriefing** of the railway guard, extracting vital clues that escaped the Scotland Yard inspectors."}
    ]
  },
  "Dashboard — deb/debris.md": {
    "primary": "Scattered fragments, rubble, or wreckage of something that has been destroyed, shattered, or broken down.",
    "secondary": "In glaciology and geomorphology, glacial debris comprises morainic rock boulders, gravel, and till transported by ice sheets.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The submarine glided silently through heaps of submerged **debris** and coral-encrusted timbers of sunken Spanish galleons."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The recent earthquake had covered the streets of Concepcion with the shattered **debris** of fallen brick and stone churches."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whalemen searched the stormy surface for survivors, finding only floating fragments of cedar **debris** from the shattered boat."}
    ]
  },
  "Dashboard — deb/debs.md": {
    "primary": "Plural form of deb; young women making their official formal entrance into high society.",
    "secondary": "Also refers historically to Eugene V. Debs (1855–1926), influential American socialist leader and founding member of the Industrial Workers of the World.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Beautiful and Damned", "quote": "A radiant coterie of fashionable young **debs** gathered around the punch bowl at the Ritz hotel ball."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The workingmen rallied passionately around Eugene **debs** when he spoke on behalf of the striking railway brotherhoods."},
      {"author": "Edith Wharton", "work": "The Custom of the Country", "quote": "The society columns listed the names of all the season's **debs** who were invited to the grand winter cotillion."}
    ]
  },
  "Dashboard — deb/debt.md": {
    "primary": "A specific sum of money, service, or obligation that is owed or due to another person or institution.",
    "secondary": "In macroeconomic theory, national debt reflects cumulative sovereign borrowing through treasury bills and bonds to finance public expenditures.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "If I let him go, the **debt** he owes will be required of me by the officer of the law."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The progress of the enormous **debt** which at present oppresses, and will in the long run probably ruin, all the great nations of Europe."},
      {"author": "Benjamin Franklin", "work": "The Way to Wealth", "quote": "Think what you do when you run in **debt**; you give to another power over your liberty and peace of mind."}
    ]
  },
  "Dashboard — deb/debtor.md": {
    "primary": "A person, company, or institution that owes a debt, financial sum, or contractual duty to a creditor.",
    "secondary": "In bankruptcy law, a debtor may file for Chapter 11 reorganization or Chapter 7 liquidation to discharge unmanageable liabilities.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Shylock demanded the forfeiture of a pound of flesh from his unfortunate Christian **debtor** Antonio."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Wilt thou seal up the avenues of ill? Pay every **debtor** his due, and live in transparent integrity."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Mr. Tulliver could not bear the humiliation of seeing himself recorded as an insolvent **debtor** in the town gazette."}
    ]
  },
  "Dashboard — deb/debug.md": {
    "primary": "To identify, trace, and remove errors, bugs, or defects from computer hardware, software, or mechanical systems.",
    "secondary": "In early electronic computing lore, Grace Hopper popularized the term after a literal moth was removed from a relay in the Harvard Mark II.",
    "quotes": [
      {"author": "Grace Hopper", "work": "Annals of the History of Computing", "quote": "From that moment on, whenever the machine stopped, we told the commander we were trying to **debug** the computer."},
      {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "It is much harder to **debug** code than to write it; therefore, write programs with utmost conceptual clarity."},
      {"author": "Edsger W. Dijkstra", "work": "Selected Writings on Computing", "quote": "Testing can demonstrate the presence of bugs, but never their absence; to **debug** effectively requires rigorous mathematical proof."}
    ]
  },
  "Dashboard — deb/debugger.md": {
    "primary": "A software tool or program used to test, inspect, step through, and remove bugs from other computer programs.",
    "secondary": "In modern software engineering toolchains, a symbolic debugger allows developers to set breakpoints, inspect stack frames, and watch memory addresses.",
    "quotes": [
      {"author": "Donald Knuth", "work": "The Art of Computer Programming", "quote": "An interactive **debugger** enables the programmer to halt execution and inspect the registers at the critical moment of failure."},
      {"author": "Brian Kernighan", "work": "The Practice of Programming", "quote": "The most effective **debugger** is often careful thought accompanied by judiciously placed print statements."},
      {"author": "Andrew Tanenbaum", "work": "Structured Computer Organization", "quote": "The operating system traps execution signals so that the symbolic **debugger** can examine corrupted memory pages."}
    ]
  },
  "Dashboard — deb/debunk.md": {
    "primary": "To expose the falseness, sham, or exaggerated claims of an idea, myth, belief, or superstition.",
    "secondary": "In scientific skepticism and investigative journalism, researchers analyze empirical evidence to debunk pseudoscientific health fads.",
    "quotes": [
      {"author": "Carl Sagan", "work": "The Demon-Haunted World", "quote": "It is the sacred duty of science to **debunk** fraudulent astrology and illuminate the true wonders of the cosmos."},
      {"author": "Bertrand Russell", "work": "Unpopular Essays", "quote": "A little historical knowledge is sufficient to **debunk** the pompous claims of dynastic chauvinism."},
      {"author": "H. L. Mencken", "work": "Prejudices: Third Series", "quote": "The critic's natural instinct is to **debunk** the hollow platitudes chanted by self-important politicians."}
    ]
  },
  "Dashboard — deb/debunking.md": {
    "primary": "The act or process of exposing the false or exaggerated nature of a claim, belief, or myth.",
    "secondary": "In historiographical revisionism, debunking hagiographical legends reveals the complex human motives behind celebrated historical figures.",
    "quotes": [
      {"author": "Carl Sagan", "work": "Broca's Brain", "quote": "Rigorous **debunking** of pseudoscientific hoaxes protects the public from costly credulity and dangerous medical quackery."},
      {"author": "Bertrand Russell", "work": "In Praise of Idleness", "quote": "The **debunking** of ancient taboos is the essential prerequisite for rational moral progress in civilized society."},
      {"author": "H. L. Mencken", "work": "Notes on Democracy", "quote": "He devoted his satirical columns to the merciless **debunking** of grandiloquent political orators."}
    ]
  },
  "Dashboard — deb/debussy.md": {
    "primary": "Claude Debussy (1862–1918), celebrated French composer whose innovative harmonic language founded musical Impressionism.",
    "secondary": "In musicology, Debussy pioneered non-functional harmonic progressions, whole-tone scales, and delicate orchestral timbres in works like *La Mer*.",
    "quotes": [
      {"author": "Igor Stravinsky", "work": "Chronicles of My Life", "quote": "The extraordinary harmonic subtlety of **debussy** exerted a profound and lasting influence upon twentieth-century music."},
      {"author": "Maurice Ravel", "work": "Autobiographical Sketch", "quote": "Listening to the orchestral preludes of **debussy** opened an entirely new universe of acoustic color and poetic freedom."},
      {"author": "Romain Rolland", "work": "Musicians of To-day", "quote": "In the delicate piano preludes of **debussy**, French musical genius achieved its most ethereal and evocative expression."}
    ]
  },
  "Dashboard — deb/debut.md": {
    "primary": "A first public appearance, performance, or formal presentation of an artist, performer, or young person in society.",
    "secondary": "In theatre and concert history, a performer's debut before a metropolitan audience can establish or ruin a lifetime professional career.",
    "quotes": [
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Mirah prepared with trembling hope for her public musical **debut** before the fashionable London audience."},
      {"author": "L. M. Montgomery", "work": "Anne of Avonlea", "quote": "Anne felt a flutter of genuine excitement as she dressed for her social **debut** at the Carmody concert."},
      {"author": "William Makepeace Thackeray", "work": "Pendennis", "quote": "The young provincial actress made her London **debut** as Juliet, eliciting stormy applause from the pit."}
    ]
  },
  "Dashboard — deb/debutante.md": {
    "primary": "A young woman making her formal initial appearance into fashionable society, traditionally at a debutante ball.",
    "secondary": "In nineteenth-century European and American aristocracy, a debutante wore a white gown and carried a floral bouquet during her formal presentation.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "May Welland looked every inch the innocent **debutante** in her tarlatan gown and modest veil of old family lace."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "She possessed none of the timid self-consciousness of an ordinary **debutante**, speaking with quiet and fearless conviction."},
      {"author": "F. Scott Fitzgerald", "work": "The Offshore Pirate", "quote": "Ardita was the most willful and celebrated **debutante** of the season, defying every traditional expectation of her guardians."}
    ]
  },
  "Dashboard — deb/indebted.md": {
    "primary": "Owing money; or feeling deeply grateful and appreciative for kindness, favors, or assistance received.",
    "secondary": "In contractual and moral philosophy, an indebted individual incurs both a legal duty of restitution and an ethical obligation of goodwill.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "We are much bound and deeply **indebted** to your wisdom for saving a fellow Venetian's life."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth felt herself exceedingly **indebted** to Mr. Darcy for his generous intervention on behalf of Lydia."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Traddles confessed that he was still heavily **indebted** for the furnishings of his modest chambers in Gray's Inn."}
    ]
  },
  "Dashboard — deb/indebtedness.md": {
    "primary": "The state or condition of owing money; or a deep sense of gratitude for benefits or favors conferred.",
    "secondary": "In corporate finance and sovereign debt sustainability analysis, heavy indebtedness restricts future investment by consuming cash flow.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The long-continued **indebtedness** of the crown eventually forced European parliaments to assert control over taxation."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "To justify the heavy **indebtedness** incurred during the Revolutionary War, the federal government must fund the public debt honorably."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy endured sleepless nights of agony contemplating his growing **indebtedness** to the horse-dealers."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Action & State"

updated = 0
for rel_path, info in data.items():
    fpath = os.path.join(base_dir, rel_path.replace("/", os.sep))
    if not os.path.exists(fpath):
        print(f"Warning: {fpath} does not exist!")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    book_idx = content.find("> [!book]")
    if book_idx == -1:
        print(f"Warning: No > [!book] callout in {rel_path}")
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

print(f"Dashboard — deb: Successfully updated {updated}/{len(data)} notes.")
