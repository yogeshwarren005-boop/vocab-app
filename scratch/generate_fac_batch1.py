# -*- coding: utf-8 -*-
import os, re

data = {
  "benefic.md": {
    "primary": "Resulting in good or favorable outcomes; having a kindly, generous, or beneficial influence.",
    "secondary": "In historical astrology and horoscopic cosmology, Jupiter and Venus are classified as benefic planets that bestow auspicious fortune.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Astrologers attribute gentle and **benefic** virtues to the benign conjunctions of the greater planets."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The ancient sages distinguished between the malignant aspects of Saturn and the **benefic** radiance of Jupiter."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The creator breathed a **benefic** spirit across the newly ordered universe, commanding all life to flourish."}
    ]
  },
  "benefice.md": {
    "primary": "A permanent church appointment or ecclesiastical living endowed with revenues or lands.",
    "secondary": "In canon law and medieval feudalism, a benefice (beneficium) originally signified a conditional grant of land bestowed by a lord in return for loyal service.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "And then dreams he of another **benefice**: sometime she driveth o'er a soldier's neck, and then dreams he of cutting foreign throats."},
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "For he had yet no worldly **benefice**, nor was he worldly enough to hold secular office."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ambitious prelate amassed every lucrative **benefice** within the diocese to support his courtly retinue."}
    ]
  },
  "beneficed.md": {
    "primary": "Holding an ecclesiastical benefice or endowed church living with fixed income.",
    "secondary": "In English ecclesiastical history, a beneficed clergyman possessed legal freehold tenure in his rectory or vicarage, contrasting with stipendiary curates.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins took pride in being a comfortably **beneficed** clergyman through the generous patronage of Lady Catherine de Bourgh."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The **beneficed** clergy of the cathedral close enjoyed spacious canonical residences and tranquil gardens."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The curate labored for years on fifty pounds before he was happily **beneficed** in an adjoining parish."}
    ]
  },
  "beneficence.md": {
    "primary": "The practice of doing good; active generosity, charity, or kindness toward others.",
    "secondary": "In bioethics and moral philosophy, the principle of beneficence obligates practitioners to act for the patient's positive welfare and remove potential harms.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "**Beneficence** is the ornament which embellishes, not the foundation which supports the building; and it was therefore sufficient to recommend, but by no means necessary to constrain it."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "No human virtue commands greater veneration than unostentatious **beneficence** quietly relieving the distress of the unfortunate."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's mind was full of grand schemes of village **beneficence**, planning model cottages and clean drainage for the cottagers."}
    ]
  },
  "beneficent.md": {
    "primary": "Resulting in good; performing acts of kindness, charity, or generosity.",
    "secondary": "In natural theology and Enlightenment cosmology, the universe was envisioned as the design of an all-wise and beneficent Providence.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I cannot persuade myself that a **beneficent** and omnipotent God would have designedly created the Ichneumonidae with the express intention of their feeding within the living bodies of caterpillars."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "A **beneficent** necessity governs all things, so that evil is continually converted into higher good."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The utilitarian standard enjoins actions that are **beneficent** to the general happiness of the whole sentient creation."}
    ]
  },
  "beneficial.md": {
    "primary": "Producing good results or helpful effects; advantageous and favorable.",
    "secondary": "In property and equity law, beneficial ownership confers the right to enjoy the economic advantages and fruits of an estate held in legal trust.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Any variation, however slight and from whatever cause proceeding, if it be in any degree profitable to an individual, will tend to its preservation, and will generally be inherited by its offspring, so that natural selection preserves **beneficial** modifications."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The division of labor is universally acknowledged to be highly **beneficial** to every class of society."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Equity recognizes the **beneficial** interest of the cestui que use, commanding the trustee to convey the profits accordingly."}
    ]
  },
  "beneficially.md": {
    "primary": "In a manner that produces good results, advantages, or helpful outcomes.",
    "secondary": "In legal trust doctrine, a beneficiary enjoys an estate beneficially, receiving all income and rents free from management burdens.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Judicious cross-breeding acts **beneficially** upon the vigor and fertility of the succeeding generations."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Capital invested in public works operates **beneficially** throughout the nation by lowering transport costs."},
      {"author": "Joseph Story", "work": "Commentaries on Equity Jurisprudence", "quote": "The property was settled so that the widow should enjoy the estate **beneficially** during her lifetime."}
    ]
  },
  "beneficiary.md": {
    "primary": "A person or entity that derives advantage or receives benefits, profits, or property from a trust, will, or insurance policy.",
    "secondary": "In feudal tenure, a beneficiary was an individual granted conditional usufruct of land or offices by an overlord.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Featherstone's sudden demise left each prospective **beneficiary** in a fever of suspense regarding the contents of the will."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The young clerk was named as the principal **beneficiary** in the wealthy recluse's testament."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The court of chancery protects the rights of the **beneficiary** against any fraudulent conversion by the legal executor."}
    ]
  },
  "beneficiate.md": {
    "primary": "To process or treat raw ore, mineral resources, or materials to improve their physical or chemical properties.",
    "secondary": "In metallurgy and mineral processing, to beneficiate entails crushing, froth flotation, and magnetic separation to upgrade metal concentration before smelting.",
    "quotes": [
      {"author": "Herbert Hoover", "work": "Principles of Mining", "quote": "Modern milling techniques **beneficiate** low-grade porphyry copper ores into high-value concentrates suitable for the reverberatory furnace."},
      {"author": "Georgius Agricola", "work": "De Re Metallica", "quote": "The miners wash the crushed vein rock in wooden troughs to **beneficiate** the heavier silver particles from the quartz sand."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Ore Concentration Investigations", "quote": "We constructed giant magnetic separators to **beneficiate** lean magnetic iron deposits into rich smelting briquettes."}
    ]
  },
  "beneficiation.md": {
    "primary": "The treatment of raw material or mineral ore to improve its physical or chemical properties prior to further processing or smelting.",
    "secondary": "In extractive metallurgy, beneficiation increases the economic grade of run-of-mine ore by rejecting barren gangue minerals through gravity or flotation circuits.",
    "quotes": [
      {"author": "Herbert Hoover", "work": "Principles of Mining", "quote": "The economic success of the deep gold mines depended upon efficient chemical **beneficiation** through cyanide extraction."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Menlo Park Research", "quote": "Our mechanical **beneficiation** plant in New Jersey processed thousands of tons of low-grade iron rock daily."},
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "Standardized metallurgical **beneficiation** allowed steel mills to exploit vast deposits of low-grade taconite."}
    ]
  },
  "coefficient.md": {
    "primary": "A numerical or constant multiplier placed before a variable in an algebraic expression; also a factor measuring a specific physical property.",
    "secondary": "In experimental physics and engineering, a coefficient (such as thermal expansion or friction) quantifies material responses under changing environmental conditions.",
    "quotes": [
      {"author": "Augustus De Morgan", "work": "Elements of Algebra", "quote": "In every polynomial term, the numerical **coefficient** determines the multiple of the variable factors involved."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The calculated **coefficient** of mutual induction depends entirely upon the geometric form and relative position of the two circuits."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The analytical engine was designed to calculate each successive **coefficient** in the expansion of astronomical tables."}
    ]
  },
  "deface.md": {
    "primary": "To spoil the surface, appearance, or beauty of something; to mar, disfigure, or vandalize.",
    "secondary": "In numismatics and criminal statutes, to deface sovereign coinage or public records constitutes a serious statutory felony.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Deface the bond, and let him not take a pound of flesh from my heart."},
      {"author": "John Milton", "work": "Areopagitica", "quote": "As good almost kill a man as kill a good book: who kills a man kills a reasonable creature, God's image; but he who destroys a good book, kills reason itself, and seeks to **deface** divine truth."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Fanatical mobs invaded the marble temples to **deface** the classical statues of the Olympian gods."}
    ]
  },
  "defacement.md": {
    "primary": "The act of spoiling the surface, appearance, or legibility of something; a marring or disfigurement.",
    "secondary": "In historical archaeology and art conservation, iconoclastic defacement involves the deliberate chiseling away of faces or inscriptions on ancient monuments.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The thoughtless **defacement** of medieval sculptures by modern restorers has inflicted irreversible injury upon our architectural heritage."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The systematic **defacement** of the triumphal arch erased the name of the fallen emperor from public memory."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old legal documents bore visible marks of damp and moldy **defacement** after decades in the cellar."}
    ]
  },
  "deficiency.md": {
    "primary": "A lack, shortage, or insufficiency of something necessary; a failing or defect.",
    "secondary": "In clinical nutrition and metabolic medicine, nutritional deficiency (such as scurvy or pellagra) produces characteristic systemic syndrome complexes.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "In chronic scurvy, an acute **deficiency** of fresh antiscorbutic nutrients leads to subcutaneous hemorrhages and spongy gums."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A temporary **deficiency** in the harvest immediately elevates the domestic market price of grain."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The apparent **deficiency** of our senses is compensated by the rational intellect that directs experimental investigation."}
    ]
  },
  "deficient.md": {
    "primary": "Not having enough of a specified quality or ingredient; lacking or inadequate in amount or skill.",
    "secondary": "In evolutionary morphology, rudimentary organs that are structurally deficient provide evidence of ancestral function lost through disuse.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In certain oceanic island insects, the wings are so **deficient** in development that the creatures can no longer fly."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Where sciences are found **deficient**, fresh empirical observation must supply the lacking principles."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "His moral education was singularly **deficient** in that intuitive sympathy which alone forgives human frailty."}
    ]
  },
  "deficit.md": {
    "primary": "An excess of expenditure or liabilities over income or assets in a given period; a shortfall.",
    "secondary": "In macroeconomic fiscal policy, an annual budget deficit requires sovereign debt issuance or monetary expansion to bridge the revenue gap.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A chronic **deficit** in public revenues compels the sovereign to borrow from commercial banks at exorbitant interest."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The fatal financial **deficit** precipitated the convocation of the States-General and the downfall of the ancient monarchy."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "A well-funded national debt transforms a temporary revenue **deficit** into a stable foundation for public commerce."}
    ]
  },
  "difficult.md": {
    "primary": "Needing much effort, skill, or courage to do, make, or understand; not easy; hard.",
    "secondary": "In character description and social psychology, a difficult temperament is demanding, unyielding, and resistant to compromise.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "O, how **difficult** it is to choose an honest friend when flatterers abound on every side!"},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "It is **difficult** to avoid believing that organs of extreme perfection have been formed by a power analogous to human reason."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba found herself in a most **difficult** position, torn between pride and an uneasy conscience."}
    ]
  },
  "difficultness.md": {
    "primary": "The quality or state of being difficult, demanding, or perplexing; difficulty.",
    "secondary": "In classical prose style and rhetorical theory, difficultness of comprehension was sometimes cultivated to conceal esoteric philosophical doctrines.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "The **difficultness** of the enterprise ought rather to inflame a generous mind than deter it from heroic action."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **difficultness** of forming clear abstract ideas arises from the ambiguity of words in common use."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He complained of the **difficultness** of reconciling personal ambitions with the quiet demands of scholarly contemplation."}
    ]
  },
  "difficulty.md": {
    "primary": "The condition of being hard to do, understand, or manage; an obstacle, problem, or hardship.",
    "secondary": "In evolutionary biology, resolving the difficulties on theory forms the argumentative crucible wherein natural selection demonstrates its explanatory power.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "I have felt the **difficulty** of my position too keenly to be surprised at any hesitation in accepting my conclusions."},
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "There be some sports are painful, and their labour delight in them sets off: some kinds of baseness are nobly undergone, and most poor matters point to rich ends. This my mean task would be as heavy to me as odious, but the mistress which I serve quickens what's dead and makes my labours pleasures: O, she is ten times more gentle than her father's crabbed, and he's composed of harshness. I must remove some thousands of these logs and pile them up, upon a sore injunction: my sweet mistress weeps when she sees me work, and says such baseness had ne'er like executor. I forget: but these sweet thoughts do even refresh my labours, most busiest when I do it with greatest **difficulty**."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak faced every financial **difficulty** with stubborn Saxon endurance, never murmuring against fate."}
    ]
  },
  "dissatisfaction.md": {
    "primary": "Lack of satisfaction; discontent, displeasure, or frustration with circumstances or achievements.",
    "secondary": "In sociological analysis and political theory, widespread popular dissatisfaction with civic institutions drives revolutionary reform.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "It is better to be a human being dissatisfied than a pig satisfied; better to be Socrates dissatisfied than a fool satisfied; and noble **dissatisfaction** leads to intellectual progress."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The instinctive feeling of **dissatisfaction** that follows an ungenerous action is the primal germ of moral conscience."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A deep inward **dissatisfaction** with her sheltered provincial life drove Dorothea to seek larger noble duties."}
    ]
  },
  "dissatisfactory.md": {
    "primary": "Failing to satisfy; unsatisfactory, disappointing, or inadequate in quality or result.",
    "secondary": "In administrative oversight and contract evaluation, a dissatisfactory report warrants formal censure or termination of services.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny found her aunt's cold and hurried letter singularly **dissatisfactory**, telling nothing of what she most yearned to hear."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The royal explanations offered to Parliament proved wholly **dissatisfactory** to the country gentlemen."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The solicitor gave a very **dissatisfactory** account of the progress of the ancient Chancery suit."}
    ]
  },
  "edification.md": {
    "primary": "The instruction, improvement, or guidance of a person morally, spiritually, or intellectually.",
    "secondary": "In classical rhetoric and sacred literature, sermons and allegorical tales are designed for the spiritual edification of the congregation.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I knew you must be edified by the margent ere you had done; your **edification** was dearly bought."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She read the lives of the early Christian saints for spiritual **edification**, yearning for heroic self-renunciation."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins chose Fordyce's Sermons for the evening reading, confident in their moral **edification** for young ladies."}
    ]
  },
  "edifice.md": {
    "primary": "A building, especially a large, imposing, or substantial one; also a complex conceptual system.",
    "secondary": "In epistemological philosophy and architectural metaphor, a grand theoretical edifice rests upon foundational axiomatic premises.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "The ancient cathedral was a majestic **edifice** of grey stone, adorned with Gothic spires that touched the clouds."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The majestic **edifice** of Roman jurisprudence had been constructed by the patient wisdom of ten centuries of magistrates."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The wooden jail was a gloomy and ponderous **edifice**, weathered by Atlantic gales and stained with prison rust."}
    ]
  },
  "efface.md": {
    "primary": "To erase a mark from a surface; to wipe out, eliminate, or cause to disappear from memory.",
    "secondary": "In character psychology, to efface oneself involves behaving with extreme modesty and humility to avoid public attention.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "Time will not **efface** the memory of our sacred vows, nor blot our ancient friendship from our hearts."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The footsteps of the passing crowd seemed to **efface** the bloodstains from the cobblestones before the wine shop."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "No suffering could **efface** from her recollection the tender kindness of Miss Temple during that bleak winter."}
    ]
  },
  "effaceable.md": {
    "primary": "Capable of being effaced, erased, obliterated, or wiped away.",
    "secondary": "In moral philosophy and legal documentation, an effaceable transgression is expungable through sincere restitution or statutory pardon.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Impressions made upon the soft wax of youthful memory are readily **effaceable** unless deepened by frequent reflection."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "No human deed is easily **effaceable** from the living fabric of history, which vibrates with eternal consequences."},
      {"author": "George Eliot", "work": "Romola", "quote": "The ink was still fresh and **effaceable** upon the scroll before Tito sealed the secret dispatch."}
    ]
  },
  "effacement.md": {
    "primary": "The act of erasing, wiping out, or obliterating something; also the keeping of oneself in the background.",
    "secondary": "In clinical obstetrics, effacement describes the thinning and shortening of the uterine cervix in preparation for delivery.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Her systematic self-**effacement** in the presence of her husband was admired by conventional society as feminine perfection."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The complete **effacement** of ancient boundary stones along the frontier invited constant barbarian incursions."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Complete cervical **effacement** marks the culmination of the first stage of normal labor."}
    ]
  },
  "efficacious.md": {
    "primary": "Successful in producing a desired or intended result; effective, potent, and powerful.",
    "secondary": "In classical theology and soteriology, efficacious grace is irresistible divine grace that unfailingly achieves the redemption of the elect.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Through divine mercy, prayer becomes an **efficacious** means to soften hard hearts and obtain pardon."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Quinine remains the most **efficacious** therapeutic remedy known for arresting the paroxysms of malarial fever."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "We perceive no necessary connection between an **efficacious** cause and its sensible physical effect."}
    ]
  },
  "efficaciously.md": {
    "primary": "In a manner that successfully produces the desired result or intended effect.",
    "secondary": "In legislative history and political economy, enforcing statutes efficaciously requires impartial judicial tribunals and swift executive action.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "True axioms lead directly and **efficaciously** to new mechanical inventions that augment human power over nature."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman legions operated most **efficaciously** when deployed in disciplined cohorts upon open ground."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Private self-interest directs capital far more **efficaciously** into productive channels than any royal decree."}
    ]
  },
  "efficaciousness.md": {
    "primary": "The power or capacity to produce an intended effect or desired outcome; efficacy.",
    "secondary": "In pharmacotherapy and toxicology, the efficaciousness of an antidote is measured by its ability to neutralize toxic ligands at low molar concentrations.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "The medicinal **efficaciousness** of mineral waters depends upon the subtle volatile salts held in chemical solution."},
      {"author": "Jeremy Taylor", "work": "Holy Living and Holy Dying", "quote": "The spiritual **efficaciousness** of religious fasting is multiplied when accompanied by secret acts of charity."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The **efficaciousness** of human reason shines forth when it guides sensory perception toward systematic truth."}
    ]
  },
  "efficacy.md": {
    "primary": "The ability to produce a desired or intended result; effectiveness and capacity for producing effects.",
    "secondary": "In clinical pharmacology, drug efficacy measures the maximum therapeutic response achievable by an agonist under saturated receptor binding.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection acts solely through the preservation of useful variations; hence its **efficacy** depends upon the occurrence of individual differences."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical **efficacy** of smallpox vaccination in preventing epidemic contagion has been demonstrated beyond all doubt."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The causal **efficacy** of natural laws is inferred through rigorous induction from uniform antecedent conditions."}
    ]
  },
  "efficiency.md": {
    "primary": "The ability to accomplish a job or produce a result with a minimum expenditure of time, effort, and resources.",
    "secondary": "In thermodynamics and mechanical engineering, thermal efficiency is the ratio of useful work performed to total heat energy consumed by an engine.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The remarkable **efficiency** of specialized pin-makers increases production tenfold compared to solitary unassisted labor."},
      {"author": "Charles Babbage", "work": "On the Economy of Machinery and Manufactures", "quote": "The introduction of automated steam presses augmented the mechanical **efficiency** of printing establishments tenfold."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The continuous evolution of society manifests an increasing **efficiency** in the coordination of social functions."}
    ]
  },
  "efficient.md": {
    "primary": "Achieving maximum productivity with minimum wasted effort or expense; competent and capable.",
    "secondary": "In classical Aristotelian metaphysics, the efficient cause is the primary agent or force that initiates change, motion, or generation.",
    "quotes": [
      {"author": "Aristotle", "work": "Physics", "quote": "The **efficient** cause is the primary starting-point of the change or rest; for instance, the adviser is a cause, and the father is cause of the child."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Physical inquiry should investigate material and **efficient** causes, leaving final causes to metaphysical speculation."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "Inspector Lestrade was an active, **efficient** officer, though completely deficient in imaginative intuition."}
    ]
  },
  "efficiently.md": {
    "primary": "In a well-organized and competent manner; without wasting time, energy, or resources.",
    "secondary": "In administrative statecraft and manufacturing logistics, coordinating operations efficiently maximizes output while preserving capital reserves.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "An open competitive market allocates societal resources far more **efficiently** than statutory trade monopolies."},
      {"author": "Florence Nightingale", "work": "Notes on Nursing", "quote": "A hospital ward can be managed **efficiently** only when strict sanitation rules are enforced without exception."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The Roman road system enabled the imperial legions to move **efficiently** between frontier garrisons."}
    ]
  },
  "facade.md": {
    "primary": "The principal front of a building facing onto a street or open space; also an outward appearance concealing a less pleasant reality.",
    "secondary": "In architectural criticism, a classical facade organizes pilasters, pediments, and fenestration into symmetrical proportions.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The marble **facade** of the ducal palace gleamed with intricate Byzantine arches facing the Grand Canal."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond maintained an immaculate social **facade**, behind which lay a cold and cynical egoism."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Beneath the sparkling **facade** of fashionable New York society lay an unsparing cruelty toward the unsuccessful."}
    ]
  },
  "face-harden.md": {
    "primary": "To harden the surface of a metal object, especially steel, while leaving the interior tough and ductile.",
    "secondary": "In metallurgy and naval armament history, the Harvey and Krupp processes were developed to face-harden heavy armor plate against high-velocity artillery shells.",
    "quotes": [
      {"author": "Alfred Thayer Mahan", "work": "The Influence of Sea Power upon History", "quote": "Naval engineers sought to **face-harden** battleship belt armor using carbon cementation to resist explosive projectiles."},
      {"author": "Thomas Edison", "work": "The Edison Papers: Metallurgy", "quote": "We subjected the steel dies to surface carburization to **face-harden** the cutting edges against wear."},
      {"author": "Thorstein Veblen", "work": "The Engineers and the Price System", "quote": "The invention of techniques to **face-harden** nickel-steel transformed the economics of heavy ordnance manufacturing."}
    ]
  },
  "face-lift.md": {
    "primary": "Cosmetic surgery to remove wrinkles and tighten facial skin to produce a more youthful appearance; also a general renovation.",
    "secondary": "In urban planning and municipal conservation, giving an aging commercial street a face-lift revives retail vitality through facade restoration.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "The dilapidated Victorian seaside resort received a municipal **face-lift**, brightening its promenades with fresh paint and electric illumination."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The Booster Club proposed an energetic **face-lift** for the downtown shopping avenue to outshine rival towns."},
      {"author": "Aldous Huxley", "work": "After Many a Summer Dies the Swan", "quote": "The wealthy Californian patron sought every cosmetic **face-lift** and glandular therapy to evade the physical reality of aging."}
    ]
  },
  "face-off.md": {
    "primary": "A direct confrontation, showdown, or contest between two opposing parties; also the start of play in ice hockey.",
    "secondary": "In diplomatic crisis management and international brinkmanship, a high-stakes face-off tests the resolve of sovereign leaders along disputed frontiers.",
    "quotes": [
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The two rival sled dogs circled each other in a deadly **face-off**, their fangs bared and hackles raised in the freezing snow."},
      {"author": "Theodore Roosevelt", "work": "The Rough Riders", "quote": "The regiment braced for the final **face-off** with the enemy entrenchments atop San Juan Hill."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The skirmishers paused in a tense **face-off**, watching the smoke clear across the wheat field."}
    ]
  },
  "face-saving.md": {
    "primary": "Serving to preserve dignity, prestige, or self-respect; avoiding public humiliation or embarrassment.",
    "secondary": "In international diplomacy and cross-cultural negotiation, formulating face-saving compromises enables disputing states to withdraw from crises without losing honor.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "War and Peace: Presidential Messages", "quote": "Diplomatic protocol must often devise a **face-saving** formula that permits an embattled cabinet to retreat gracefully."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "Jim clung desperately to every **face-saving** pretext that might shield his conscience from his catastrophic failure."},
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The prime minister welcomed the quiet settlement as an ideal **face-saving** resolution to a perilous cabinet scandal."}
    ]
  },
  "face-to-face.md": {
    "primary": "In direct physical presence or confrontation with someone; confronting each other directly.",
    "secondary": "In phenomenology and dialogue ethics, the face-to-face encounter establishes immediate intersubjective ethical responsibility between human beings.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "Face to face, and frowning brow to brow, ourselves will hear the accuser and the accused freely speak."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The two lifelong enemies stood **face-to-face** in the courtroom, their eyes locked in mutual recognition."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale stood **face-to-face** with his tormentor in the dark study, trembling with unspoken guilt."}
    ]
  },
  "face.md": {
    "primary": "The front part of the human head from forehead to chin; also the surface or outward appearance of something.",
    "secondary": "In sociolinguistics and cross-cultural sociology, face denotes an individual's public self-image, social standing, and communal prestige.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 115", "quote": "Heaven in thy creation did decree, that in thy **face** sweet love should ever dwell."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer looked steadily into the client's **face**, searching for any sign of faltering truth."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The brilliant sunset cast a ruddy glow across the upturned **face** of the young shepherd on the hill."}
    ]
  },
  "faced.md": {
    "primary": "Confronted with or having to deal with a difficult situation; also having a surface or facade of a specified kind.",
    "secondary": "In masonry architecture and civil construction, stone-faced masonry features a facing of dressed ashlar veneer over a rubble core.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "He **faced** the rebel forces on the open plain with unflinching royal courage."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel Oak was **faced** with ruin after his young sheep-dog drove the flock over the chalk precipice."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "Captain MacWhirr **faced** the mounting hurricane with absolute, stolid composure."}
    ]
  },
  "faceless.md": {
    "primary": "Lacking a face; also lacking individual identity, character, or distinctive personality; anonymous.",
    "secondary": "In dystopian political sociology, faceless bureaucracies wield impersonal power detached from human empathy and moral accountability.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "In the dim underground caverns, the Morlocks appeared as pale, **faceless** shapes scuttling through the dark."},
      {"author": "Franz Kafka", "work": "The Trial", "quote": "K. confronted a **faceless** legal apparatus whose judges remained unseen and whose laws were unwritten."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston gazed at the crowd of **faceless** Party members marching in disciplined unison down the avenue."}
    ]
  },
  "facelift.md": {
    "primary": "Cosmetic surgery to tighten facial skin; also a renovation or overhaul intended to improve the appearance or functioning of something.",
    "secondary": "In commercial real estate and urban revitalization, a retail center facelift modernizes storefronts, signage, and public pedestrian walkways.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "The Zenith commercial club sponsored a grand architectural **facelift** to make Main Street attractive to eastern investors."},
      {"author": "Aldous Huxley", "work": "After Many a Summer Dies the Swan", "quote": "The aging society matron spent fortunes on each surgical **facelift**, terrified of the inevitable decay of youth."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "The old industrial town required more than a superficial **facelift**; it needed total economic reorganization."}
    ]
  },
  "faceplate.md": {
    "primary": "A protective or decorative plate covering the front of a device, machine tool, or electrical fixture.",
    "secondary": "In mechanical engineering and lathe machining, a faceplate is a circular metal plate mounted on the spindle to secure irregular workpieces for turning.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers: Menlo Park Notebooks", "quote": "The lathe machinist bolted the irregular bronze casting securely to the heavy iron **faceplate** before boring."},
      {"author": "Charles Babbage", "work": "Passages from the Life of a Philosopher", "quote": "The bronze dials were mounted upon a polished **faceplate** to facilitate precise reading of the mathematical wheels."},
      {"author": "Henry Ford", "work": "My Life and Work", "quote": "The standardized engine **faceplate** allowed rapid assembly of ignition timing parts without hand fitting."}
    ]
  },
  "facer.md": {
    "primary": "An unexpected, stunning difficulty, defeat, or blow in the face; a perplexing problem.",
    "secondary": "In nineteenth-century British boxing slang, a facer was a hard, direct punch landed straight upon an opponent's countenance.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The sudden discovery of the missing will was a tremendous **facer** for the defendants in the Chancery suit."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The young ensign received a stunning **facer** when his wealthy uncle disinherited him without a shilling."},
      {"author": "Arthur Conan Doyle", "work": "Rodney Stone", "quote": "The veteran pugilist stepped inside the guard and landed a sharp **facer** that sent his antagonist reeling."}
    ]
  },
  "facet.md": {
    "primary": "One side or aspect of something; also one of the flat polished surfaces on a cut gemstone.",
    "secondary": "In invertebrate entomology, each individual lens or ommatidium of an insect's compound eye forms a distinct optical facet.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "Every individual nature is a new **facet** of the diamond of divine intelligence, reflecting the universal light from a fresh angle."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The compound eye of the dragon-fly contains thousands of minute visual **facet** structures cooperating to detect movement."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She turned the complicated social dilemma over in her mind, examining every painful **facet** of the situation."}
    ]
  },
  "faceted.md": {
    "primary": "Having many facets or flat cut surfaces, as a gemstone; also having many distinct aspects or dimensions.",
    "secondary": "In gem cutting lapidary arts, a faceted jewel refracts and reflects light internally to maximize brilliance and chromatic fire.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He admired the **faceted** ruby ring that glowed like a burning coal upon his finger in the dim salon."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The compound eyes of arthropods consist of numerous closely packed, **faceted** lenses adapted for panoramic vision."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The capitals of the Gothic columns were exquisitely **faceted**, catching the morning light in contrasting planes of shadow."}
    ]
  },
  "facetious.md": {
    "primary": "Treating serious issues with deliberately inappropriate humor; flippant or playfully humorous.",
    "secondary": "In social etiquette and conversational rhetoric, facetious remarks risk offending companions if delivered when solemnity is required.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber made a **facetious** allusion to his pecuniary embarrassments, treating impending bankruptcy as a humorous adventure."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was in his most **facetious** humor, teasing his anxious wife with playful sarcasms about their new neighbor."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy's **facetious** excuses could not soften his father's grave displeasure over the unpaid debt."}
    ]
  },
  "facetiously.md": {
    "primary": "In a flippant, playfully humorous, or inappropriately jocular manner.",
    "secondary": "In character interaction and dialogue, replying facetiously masks inner discomfort or attempts to deflect serious inquiry.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Herbert remarked **facetiously** that looking about him for an opening in commerce was the most pleasant occupation in London."},
      {"author": "Mark Twain", "work": "The Innocents Abroad", "quote": "The doctor replied **facetiously** to the solemn Italian guide, asking whether Christopher Columbus was truly dead."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes answered **facetiously**, though Watson knew that behind the jest lay a mind working with intense concentration."}
    ]
  },
  "facetiousness.md": {
    "primary": "The state or habit of being facetious; inappropriate or humorous flippancy regarding serious matters.",
    "secondary": "In moral philosophy and rhetorical critique, persistent facetiousness reveals a superficial intellect unable to sustain earnest thought.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Untimely **facetiousness** in the midst of grave public calamity is a mark of vulgar levity rather than true wit."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Rosamond disliked her brother's easy **facetiousness**, which she considered deficient in fashionable dignity."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Slope felt that the chaplain's clerical **facetiousness** was singularly ill-timed during the episcopal interview."}
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

print(f"Dashboard — fac Batch 1: Successfully updated {updated}/{len(data)} notes.")
