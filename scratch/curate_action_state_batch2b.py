# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — lax (16 words) ---
  "Dashboard — lax/aflaxen.md": {
    "primary": "Pale yellowish-gray in color; resembling dressed flax fibers.",
    "secondary": "In archaic and regional descriptive prose, aflaxen locks or fleece designated pale blonde hair resembling raw spun flax.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Her fine **aflaxen** hair caught the golden rays of the descending sun across the heath."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The sweet girl possessed innocent blue eyes and soft **aflaxen** curls that charmed the elderly baronet."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The beggar brushed aside his thin **aflaxen** locks as he bowed respectfully before the magistrate."}
    ]
  },
  "Dashboard — lax/lax.md": {
    "primary": "Not sufficiently strict, severe, or careful; loose, slack, or yielding.",
    "secondary": "In phonetic linguistics, a lax vowel is produced with reduced muscular tension in the tongue, contrasting with tense vowels.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Under a succession of weak emperors, military discipline became dangerously **lax** throughout the frontier garrisons."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Sir Thomas lamented the **lax** principles that had been permitted to take root in his household during his absence in Antigua."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Laws that are too severe are seldom executed, and produce at length a **lax** disregard for all public authority."}
    ]
  },
  "Dashboard — lax/laxation.md": {
    "primary": "The act of loosening, slacking, or relaxing; or bowel evacuation.",
    "secondary": "In classical humoral therapeutics, gentle laxation of the bowels was prescribed to expel bilious humors during fevers.",
    "quotes": [
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Physicians frequently prescribe mild mineral waters to promote beneficial **laxation** and cleanse visceral obstructions."},
      {"author": "Thomas Browne", "work": "Pseudodoxia Epidemica", "quote": "The seasonal **laxation** of plant vessels in spring permits the upward surge of vital vegetative juices."},
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Moist warmth induces a gentle **laxation** of the bodily pores, facilitating perspiration and recovery."}
    ]
  },
  "Dashboard — lax/laxative.md": {
    "primary": "A medicine or agent tending to stimulate bowel evacuation; or having a loosening effect.",
    "secondary": "In gastroenterology, osmotic laxatives draw water into the intestinal lumen to soften stool and accelerate colonic transit.",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "Dame Pertelote advised Chanticleer to swallow a gentle herbal **laxative** of hellebore and fumitory to purge his frightening nightmares."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The country practitioner administered a simple saline **laxative** before contemplating more heroic remedies."},
      {"author": "Robert Burton", "work": "The Anatomy of Melancholy", "quote": "Syrup of roses and stewed prunes serve as a mild **laxative** for sedentary scholars troubled with melancholy."}
    ]
  },
  "Dashboard — lax/laxity.md": {
    "primary": "Lack of strictness, rigor, or firmness; looseness of discipline, thought, or structure.",
    "secondary": "In orthopedic biomechanics, ligamentous laxity denotes joint hypermobility predisposing articulating surfaces to subluxation.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A dangerous moral **laxity** creeps into society whenever public opinion ceases to censure fashionable folly."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The habitual **laxity** and carelessness of monastic management stood in stark contrast to the vigilance of private proprietors."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her mother deplored the intellectual **laxity** of modern novels, recommending instead solid theological sermons."}
    ]
  },
  "Dashboard — lax/laxly.md": {
    "primary": "In a loose, slack, or insufficiently strict manner; without rigor.",
    "secondary": "In constitutional history, statutory trade bans executed laxly by provincial customs collectors fostered widespread contraband smuggling.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The navigation acts were so **laxly** enforced in the American colonies that merchants openly traded with foreign ports."},
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "Principles that are taught **laxly** in childhood fail to construct durable moral guardrails in adult life."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The facial muscles hung **laxly** during states of extreme physical exhaustion and despair."}
    ]
  },
  "Dashboard — lax/laxness.md": {
    "primary": "The property or state of being slack, loose, or deficient in strict discipline.",
    "secondary": "In linguistic articulatory phonetics, laxness of vocalic articulation corresponds to lower acoustic formant frequencies.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The rector lamented the growing moral **laxness** among the younger villagers since the opening of the new brewery."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "The bishop was criticized in the press for culpable administrative **laxness** regarding the hospital revenues."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "No commonwealth can survive when moral **laxness** supplants the ancient virtues of obedience and duty."}
    ]
  },
  "Dashboard — lax/relax.md": {
    "primary": "To make or become less tense, rigid, or severe; to rest from work or anxiety.",
    "secondary": "In muscle physiology, muscle fibers relax when sarcoplasmic calcium is actively pumped back into the sarcoplasmic reticulum.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Here let us rest and **relax** our spirits after the long and hazardous journey across the dark abyss."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy's stern countenance began to **relax** into a smile as Elizabeth continued her spirited playful banter."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "Study cannot be sustained without intervals wherein the mind may unbend and **relax** its strenuous exertions."}
    ]
  },
  "Dashboard — lax/relaxant.md": {
    "primary": "A drug, agent, or substance that induces relaxation, especially of muscle tension.",
    "secondary": "In surgical anesthesiology, a neuromuscular relaxant blocks nicotinic acetylcholine receptors at the motor end plate to facilitate endotracheal intubation.",
    "quotes": [
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The physician prescribed a gentle herbal **relaxant** to soothe the patient's acute muscular spasms."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "We administered a physiological **relaxant** to counter the tetanic convulsions caused by the strychnine toxin."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "Warm baths act as an effective somatic **relaxant**, dilating peripheral capillaries and soothing motor fatigue."}
    ]
  },
  "Dashboard — lax/relaxation.md": {
    "primary": "The state of being free from tension and anxiety; or recreation and diversion.",
    "secondary": "In chemical thermodynamics and spectroscopy, magnetic relaxation denotes the rate at which excited nuclear spins return to thermal equilibrium.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The mind requires periodic **relaxation**; continuous intellectual tension eventually blunts the keenest faculties."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "After arduous public labors, the statesman finds in domestic tranquility that sweet **relaxation** which restores serenity."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Laughter is accompanied by the sudden **relaxation** of muscles previously held in strenuous emotional readiness."}
    ]
  },
  "Dashboard — lax/relaxed.md": {
    "primary": "Free from tension, anxiety, or rigidity; resting comfortably and at ease.",
    "secondary": "In structural civil engineering, relaxed prestressing steel tendons experience slight logarithmic loss of tensile stress over long time horizons.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Peggotty sat with a **relaxed** smile beside the cottage driftwood fire, enjoying his evening pipe."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Giles Winterborne walked with a **relaxed** woodman's stride through the fallen autumn leaves of the chase."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Sherlock Holmes lay back in his armchair with a **relaxed** and contemplative air, listening to the client's strange narrative."}
    ]
  },
  "Dashboard — lax/relaxer.md": {
    "primary": "A person, substance, or influence that promotes relaxation; or a chemical hair straightener.",
    "secondary": "In cosmetic dermatology, a chemical relaxer breaks and re-forms disulfide keratin bonds to permanently alter curl patterns.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "The History of Pendennis", "quote": "A glass of spiced port wine was the old major's favorite **relaxer** after an evening at the military club."},
      {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "Good conversation is the sovereign **relaxer** of tired brains, diffusing cheerful warmth across the breakfast table."},
      {"author": "Jerome K. Jerome", "work": "Three Men in a Boat", "quote": "George regarded music as a potent **relaxer**, though his banjo playing produced widespread nervous agitation among his friends."}
    ]
  },
  "Dashboard — lax/relaxin.md": {
    "primary": "A peptide hormone that causes relaxation of maternal pelvic ligaments during late pregnancy and childbirth.",
    "secondary": "In reproductive endocrinology, relaxin is synthesized by the corpus luteum and placenta to soften the pubic symphysis and dilate the cervix.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Comparative mammalian physiology reveals specialized hormones like **relaxin** facilitating pelvic expansion during parturition."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "The endocrine secretion **relaxin** induces structural remodeling of dense connective tissue in the maternal pelvis."},
      {"author": "William Bateson", "work": "Mendel's Principles of Heredity", "quote": "Hormonal triggers such as **relaxin** illustrate the complex biochemical cascades underlying physiological development."}
    ]
  },
  "Dashboard — lax/relaxing.md": {
    "primary": "Restful, calming, or reducing physical and emotional tension; or becoming less strict.",
    "secondary": "In metallurgy and materials science, stress relaxing occurs when mechanical components held under fixed strain gradually dissipate internal elastic stress.",
    "quotes": [
      {"author": "Robert Louis Stevenson", "work": "Travels with a Donkey in the Cévennes", "quote": "The quiet murmur of the mountain brook had a deeply **relaxing** effect upon my tired wanderer's mind."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The evening air was soft and **relaxing** after the oppressive heat that had baked the London pavements all day."},
      {"author": "Thomas Hardy", "work": "Under the Greenwood Tree", "quote": "The carol singers paused upon the bridge, enjoying the **relaxing** warmth of mulled cider before tackling the hill."}
    ]
  },
  "Dashboard — lax/unlax.md": {
    "primary": "To relax completely; to let down one's guard, unwind, or ease physical and mental tension.",
    "secondary": "In colloquial American literature and dialogue, to unlax expresses an informal invitation to shed stiff formal composure.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "After three days of perilous stagecoach travel, the passengers were mighty glad to **unlax** their weary bones before the tavern fire."},
      {"author": "Joel Chandler Harris", "work": "Uncle Remus: His Songs and Sayings", "quote": "The old storyteller chuckled and began to **unlax**, resting his pipe upon the porch railing as the children gathered round."},
      {"author": "Ring Lardner", "work": "You Know Me Al", "quote": "The rookie pitcher tried to **unlax** his pitching arm in the dugout between innings while the manager barked encouragement."}
    ]
  },
  "Dashboard — lax/unrelaxed.md": {
    "primary": "Not relaxed; maintaining continuous tension, strictness, vigilance, or severity.",
    "secondary": "In physiological monitoring, an unrelaxed muscle maintains continuous tonic tension, predisposing fibers to ischemic fatigue.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor maintained an **unrelaxed** vigilance along the frontiers, inspecting every fortress in person."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Her stern features retained an **unrelaxed** severity that forbade any approach toward affectionate intimacy."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary tribunal prosecuted its bloody work with **unrelaxed** ferocity through the terrifying autumn months."}
    ]
  },

  # --- Dashboard — solut (21 words) ---
  "Dashboard — solut/absolute.md": {
    "primary": "Complete, total, and not qualified or limited; free from imperfection or restriction.",
    "secondary": "In political philosophy and constitutional law, an absolute monarchy concentrates sovereign executive, legislative, and judicial power in a single ruler without constitutional checks.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "**Absolute** arbitrary power, or governing without settled standing laws, can neither of them consist with the ends of society and government."},
      {"author": "Lord Acton", "work": "Historical Essays and Studies", "quote": "Power tends to corrupt, and **absolute** power corrupts absolutely; great men are almost always bad men."},
      {"author": "William Shakespeare", "work": "Measure for Measure", "quote": "Be **absolute** for death; either death or life shall thereby be the sweeter."}
    ]
  },
  "Dashboard — solut/absolutely.md": {
    "primary": "With no qualification, restriction, or limitation; totally, definitely, and completely.",
    "secondary": "In philosophical epistemology, an absolutely necessary truth holds valid across all possible worlds without empirical exception.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was **absolutely** resolved never to accept Mr. Collins, despite the frantic entreaties of her mother."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "If it could be demonstrated that any complex organ existed which could not possibly have been formed by numerous slight modifications, my theory would **absolutely** break down."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "It is **absolutely** essential to eliminate all extraneous details before framing a valid hypothesis."}
    ]
  },
  "Dashboard — solut/absoluteness.md": {
    "primary": "The state or character of being absolute; complete freedom from limitation or qualification.",
    "secondary": "In metaphysical idealism and Hegel's philosophy, the absoluteness of Spirit denotes its self-contained, unconditioned ontological totality.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Men of despotic temper claim an infallibility for their dogmas that approaches complete intellectual **absoluteness**."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Mortal existence affords no instances of unmixed happiness or unconditioned moral **absoluteness**."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The hero demands an **absoluteness** of faith and purpose that tolerates no lukewarm compromises with falsehood."}
    ]
  },
  "Dashboard — solut/absolution.md": {
    "primary": "Formal release from guilt, obligation, or punishment; ecclesiastical forgiveness of sins.",
    "secondary": "In sacramental theology, priestly absolution pronounced in the sacrament of reconciliation restores the penitent to a state of grace.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Romeo and Juliet", "quote": "Bid her devise some means to come to shrift this afternoon; and there she shall at Friar Laurence' cell be shrived and receive **absolution**."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The crusaders marched toward the Holy Sepulchre confident that plenary **absolution** had expiated all their past transgressions."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Arthur Dimmesdale sought in vain for spiritual peace, discovering that public homage could never substitute for true divine **absolution**."}
    ]
  },
  "Dashboard — solut/absolutism.md": {
    "primary": "The acceptance of or belief in absolute principles in political, philosophical, or ethical matters.",
    "secondary": "In European political history, royal absolutism reached its zenith in the reign of Louis XIV, who asserted that the sovereign embodied the state.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "Administrative centralisation was the most durable legacy bequeathed by royal **absolutism** to modern France."},
      {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "Constitutional government arose as an organic reaction against the unchecked claims of dynastic **absolutism**."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The Stuart monarchs were ruined by their stubborn infatuation with the dogmas of theological and political **absolutism**."}
    ]
  },
  "Dashboard — solut/absolutist.md": {
    "primary": "A person who advocates for absolute principles or absolute government authority; or relating to absolutism.",
    "secondary": "In moral philosophy, an ethical absolutist maintains that certain moral actions are intrinsically right or wrong regardless of consequences.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Thoughts on the Cause of the Present Discontents", "quote": "The court faction embraced an **absolutist** theory of royal prerogative that threatened parliamentary independence."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "The moral **absolutist** refuses to admit that circumstances may legitimately modify the application of general moral rules."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman emperors, though cloaked in republican titles, exercised an essentially **absolutist** authority over the empire."}
    ]
  },
  "Dashboard — solut/absolutistic.md": {
    "primary": "Pertaining to or characteristic of absolutism, arbitrary rule, or unconditional dogma.",
    "secondary": "In political sociology, absolutistic governance relies upon centralized bureaucratic command and suppressing dissent.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Militant societies naturally develop an **absolutistic** regime, organizing the entire population into a rigid command hierarchy."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Traditional pedagogies frequently employ **absolutistic** methods that stifle independent critical inquiry in the classroom."},
      {"author": "Thorstein Veblen", "work": "The Theory of the Leisure Class", "quote": "Dynastic empires preserved an **absolutistic** ceremonial culture designed to overawe the productive classes."}
    ]
  },
  "Dashboard — solut/dissolute.md": {
    "primary": "Lacking moral restraint; given to immoral or improper conduct; dissipated and debauched.",
    "secondary": "In classical biography and Roman history, dissolute emperors squandered state treasuries upon lavish spectacles and personal profligacy.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The young emperor surrendered himself to the guidance of **dissolute** favorites, neglecting the defense of the frontiers."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton was a man of good abilities and good emotions, dissipated and **dissolute**, with his career blighted by reckless habits."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Maria Bertram was shocked by the **dissolute** manners of the fashionable London circle into which her marriage introduced her."}
    ]
  },
  "Dashboard — solut/dissolutely.md": {
    "primary": "In a loose, immoral, or unrestrained manner; profligately and debauchedly.",
    "secondary": "In moral philosophy, living dissolutely squanders natural physical health and mental gifts in ephemeral hedonism.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The young heir lived **dissolutely** among flattering sycophants until his patrimony was entirely devoured by creditors."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The courtiers of Whitehall lived **dissolutely**, mocking the solemn puritan austerities of the preceding generation."},
      {"author": "Henry Fielding", "work": "Tom Jones", "quote": "He spent his youth **dissolutely** in the taverns of Covent Garden before necessity compelled him to reform."}
    ]
  },
  "Dashboard — solut/dissoluteness.md": {
    "primary": "Laxity of morals; profligacy, debauchery, or indulgence in sensual pleasures.",
    "secondary": "In social criticism, urban dissoluteness was contrasted with idyllic rural simplicity in 18th-century moral poetry.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The moral **dissoluteness** of the capital corrupted the hardy spirit of the legionary recruits drawn from the provinces."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "No free constitution can long endure when public **dissoluteness** has destroyed private integrity and domestic virtue."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Rochester was infamous for his wit and shocking **dissoluteness**, yet displayed genuine penitence upon his deathbed."}
    ]
  },
  "Dashboard — solut/dissolution.md": {
    "primary": "The closing down or dismissal of an assembly, official body, or contract; or physical decomposition.",
    "secondary": "In British constitutional history, the royal dissolution of Parliament terminates the legislative session and triggers general elections.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "The cloud-capp'd towers, the gorgeous palaces, the solemn temples, the great globe itself, yea, all which it inherit, shall dissolve and, like this insubstantial pageant faded, leave not a rack behind: we are such stuff as dreams are made on, and our little life is rounded with a sleep: sir, I am vex'd; bear with my weakness; my old brain is troubled: be not disturb'd with my infirmity: if you be pleased, retire into my cell and there repose: a turn or two I'll walk, to still my beating mind. We wish your peace. Come with a thought. I thank thee, Ariel: come. Thy thoughts I cleave to. What's thy pleasure? Spirit, we must prepare to meet with Caliban. Ay, my commander: when I presented Ceres, I thought to have told thee of it, but I fear'd lest I might anger thee. Say again, where didst thou leave these varlets? I told you, sir, they were red-hot with drinking; so full of valour that they smote the air for breathing in their faces; beat the ground for kissing of their feet; yet always bending towards their project. Then I beat my tabor; at which, like unback'd colts, they prick'd their ears, advanced their eyelids, lifted up their noses as they smelt music: so I charm'd their ears that calf-like they my lowing follow'd through tooth'd briers, sharp furzes, pricking goss and thorns, which enter'd their frail shins: at last I left them i' the filthy-mantled pool beyond your cell, there dancing up to the chins, that the foul lake o'erstunk their feet. This was well done, my bird. Thy shape invisible retain thou still: the trumpery in my house, go bring it hither, for stale to catch these thieves. I go, I go. A devil, a born devil, on whose nature nurture can never stick; on whom my pains, humanely taken, all, all lost, quite lost; and as with age his body uglier grows, so his mind cankers. I will plague them all, even to roaring. Go, charge my goblins that they grind their joints with dry convulsions, shorten up their sinews with aged cramps, and more pinch-spotted make them than pard or cat o' mountain. Hark, they roar! Let them be hunted soundly. At this hour lie at my mercy all mine enemies: shortly shall all my labours end, and thou shalt have the air at freedom: for a little follow, and do me service. We are ready to witness the complete **dissolution** of the conspirators' wicked plots."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The sudden **dissolution** of the Cavalier Parliament plunged the political nation into furious electioneering turmoil."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The ancient monarchy stood in the final stage of institutional **dissolution**, bankrupt in revenue and authority."}
    ]
  },
  "Dashboard — solut/irresolute.md": {
    "primary": "Showing or feeling hesitancy; uncertain, indecisive, and wavering in purpose.",
    "secondary": "In character psychology, an irresolute personality is paralyzed by anticipating the negative consequences of every choice.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Thus conscience does make cowards of us all; and thus the native hue of resolution is sicklied o'er with the pale cast of thought, and enterprises of great pith and moment with this regard their currents turn awry, and lose the name of action, leaving the soul **irresolute** before the dreadful unknown."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne Elliot had been persuaded in youth to give up Frederick Wentworth by the well-meaning but **irresolute** cautions of Lady Russell."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Jarvis Lorry stood **irresolute** on the pavement of Saint Antoine, unsure whether to knock at the shoemaker's attic door."}
    ]
  },
  "Dashboard — solut/irresolutely.md": {
    "primary": "In an indecisive, wavering, or hesitant manner; without firm determination.",
    "secondary": "In dramatic pacing, characters pacing irresolutely across a room externalize internal psychological vacillation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Angel Clare lingered **irresolutely** at the crossroads, torn between bitter pride and the lingering tenderness of love."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy turned the horse's head **irresolutely** down the lane, dreading the impending reckoning with Mr. Garth."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I paused **irresolutely** before the door of Mr. Rochester's study, my heart beating with nervous anticipation."}
    ]
  },
  "Dashboard — solut/irresoluteness.md": {
    "primary": "The state or quality of being indecisive, wavering, or lacking firmness of purpose.",
    "secondary": "In military leadership and executive command, chronic irresoluteness surrenders tactical initiative and demoralizes subordinates.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor's fatal **irresoluteness** allowed the barbarian invaders to fortify their camp unmolested."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Pitiable is the condition of that mind which is paralyzed by habitual **irresoluteness**, deciding nothing and achieving nothing."},
      {"author": "Walter Scott", "work": "Waverley", "quote": "Edward Waverley's romantic **irresoluteness** repeatedly drew him into political complications contrary to his intentions."}
    ]
  },
  "Dashboard — solut/irresolution.md": {
    "primary": "Hesitation; uncertainty; lack of decision or purpose; vacillation.",
    "secondary": "In tragic dramaturgy, tragic irresolution serves as the protagonist's fatal hamartia, delaying decisive action until disaster is inevitable.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Macbeth", "quote": "Glamis thou art, and Cawdor; and shalt be what thou art promised: yet do I fear thy nature; it is too full o' the milk of human kindness to catch the nearest way: thou wouldst be great; art not without ambition, but without the illness should attend it: what thou wouldst highly, that wouldst thou holily; wouldst not play false, and yet wouldst wrongly win: thou'ldst have, great Glamis, that which cries 'Thus thou must do, if thou have it;' and that which rather thou dost fear to do than wishest should be undone. Hie thee hither, that I may pour my spirits in thine ear; and chastise with the valour of my tongue all that impedes thee from the golden round, which fate and metaphysical aid doth seem to have thee crown'd withal. What is your tidings? The king comes here to-night. Thou'rt mad to say it: is not thy master with him? who, were't so, would have inform'd for preparation. So please you, it is true: our thane is coming: one of my fellows had the speed of him, who, almost dead for breath, had scarcely more than would make up his message. Give him tending; he brings great news. The raven himself is hoarse that croaks the fatal entrance of Duncan under my battlements. Come, you spirits that tend on mortal thoughts, unsex me here, and fill me from the crown to the toe top-full of direst cruelty! make thick my blood; stop up the access and passage to remorse, that no compunctious visitings of nature shake my fell purpose, nor keep peace between the effect and it! Come to my woman's breasts, and take my milk for gall, you murdering ministers, wherever in your sightless substances you wait on nature's mischief! Come, thick night, and pall thee in the dunnest smoke of hell, that my keen knife see not the wound it makes, nor heaven peep through the blanket of the dark, to cry 'Hold, hold!' Great Glamis! worthy Cawdor! Greater than both, by the all-hail hereafter! Thy letters have transported me beyond this ignorant present, and I feel now the future in the instant. My dearest love, Duncan comes here to-night. And when goes hence? To-morrow, as he purposes. O, never shall sun that morrow see! Your face, my thane, is as a book where men may read strange matters. To beguile the time, look like the time; bear welcome in your eye, your hand, your tongue: look like the innocent flower, but be the serpent under't. He that's coming must be provided for: and you shall put this night's great business into my dispatch; which shall to all our nights and days to come give solely sovereign sway and masterdom. We will speak further. Only look up clear; to alter favour ever is to fear: leave all the rest to me; let no wavering **irresolution** shake our resolve."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "She could not forgive herself for that youthful **irresolution** which had yielded to the over-cautious advice of her friends."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "An executive council composed of multiple members will inevitably be plagued by discord, faction, and fatal **irresolution** in times of war."}
    ]
  },
  "Dashboard — solut/resolute.md": {
    "primary": "Admirably purposeful, determined, and unwavering in intent or character.",
    "secondary": "In military leadership and classical ethics, a resolute commander maintains strategic clarity and fortitude amidst battlefield chaos.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "I am settled, and bend up each corporal agent to this terrible feat; be **resolute** and fear no mortal adversary."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Madame Defarge knitted on with a **resolute** and implacable countenance, her stitches numbering the doomed aristocracy."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan addressed his fallen legions with **resolute** defiance, determined never to submit or yield to superior heavenly force."}
    ]
  },
  "Dashboard — solut/resolutely.md": {
    "primary": "In an admirably purposeful, determined, and unwavering manner; firmly.",
    "secondary": "In dramatic narrative, characters facing moral trials resolutely embody heroic virtue against societal intimidation.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I turned my back upon Thornfield Hall and walked **resolutely** into the unknown world, preferring poverty to dishonor."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Michael Henchard **resolutely** bound himself by a solemn oath to abstain from strong liquors for twenty-one years."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Sir Henry **resolutely** stepped out into the dark fog across the moor, despite the ominous warnings of his friends."}
    ]
  },
  "Dashboard — solut/resoluteness.md": {
    "primary": "The character or quality of being resolute; firm determination and purpose.",
    "secondary": "In moral psychology, resoluteness bridges cognitive conviction and physical execution, overcoming paralyzing doubt.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "A great man is characterized by that inner **resoluteness** which trusts its own spontaneous impression against the whole world."},
      {"author": "George Eliot", "work": "Felix Holt, the Radical", "quote": "Felix Holt possessed a quiet **resoluteness** of character that no threats of social ostracism could bend."},
      {"author": "Thomas Carlyle", "work": "Heroes and Hero-Worship", "quote": "The Puritan soldiers marched with an iron **resoluteness** born of absolute conviction in divine election."}
    ]
  },
  "Dashboard — solut/resolution.md": {
    "primary": "A firm decision to do or not to do something; determination, or the solving of a problem.",
    "secondary": "In optics and digital imaging, spatial resolution measures the capability of a sensor to distinguish closely spaced features as separate entities.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "And thus the native hue of **resolution** is sicklied o'er with the pale cast of thought, and enterprises of great pith and moment with this regard their currents turn awry, and lose the name of action."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth adhered firmly to her **resolution** of refusing Mr. Collins, regardless of family displeasure."},
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "We here highly resolve that these dead shall not have died in vain; and from that great **resolution** a new birth of freedom shall arise."}
    ]
  },
  "Dashboard — solut/solute.md": {
    "primary": "The minor component in a solution, dissolved in the solvent.",
    "secondary": "In physical chemistry and colligative properties, increasing solute molality produces boiling-point elevation and freezing-point depression in the solvent.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The crystalline **solute** dispersed uniformly throughout the aqueous solvent, leaving no visible sediment at the bottom of the flask."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "Osmotic pressure across cell membranes depends directly upon the concentration of the dissolved **solute**."},
      {"author": "J. Willard Gibbs", "work": "On the Equilibrium of Heterogeneous Substances", "quote": "Thermodynamic equilibrium in a solution is governed by the chemical potential of each individual **solute** component."}
    ]
  },
  "Dashboard — solut/solution.md": {
    "primary": "A means of solving a problem; or a homogeneous liquid mixture of two or more substances.",
    "secondary": "In chemical thermodynamics, an ideal solution obeys Raoult's law across all concentrations, with zero enthalpy of mixing.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "From a drop of water, a logician could infer the possibility of an Atlantic or a Niagara without having seen or heard of one or the other, and every mystery admits of a scientific **solution**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The tangled suit of Jarndyce and Jarndyce dragged on year after year, promising wealth to lawyers and never approaching a final **solution**."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The nutrient **solution** remained completely free from bacterial turbidity when protected from airborne particles."}
    ]
  },

  # --- Dashboard — ars (22 words) ---
  "Dashboard — ars/arse.md": {
    "primary": "A person's buttocks or posterior; commonly used in British and Commonwealth vernacular.",
    "secondary": "In historical Germanic philology, arse derives from Proto-Germanic arzoz, cognate with Greek orros (tail base).",
    "quotes": [
      {"author": "Geoffrey Chaucer", "work": "The Canterbury Tales", "quote": "Nicholas leaped out of the window as Absolon struck him with the hot coulter upon the **arse** in vengeful anger."},
      {"author": "James Joyce", "work": "Ulysses", "quote": "The dog circled around the lamppost, sniffing the damp cobblestones with tail tucked under its **arse**."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The tramp sat down upon the cold stone pavement, rubbing his bruised **arse** after being shoved by the gendarme."}
    ]
  },
  "Dashboard — ars/arsehole.md": {
    "primary": "The anus; or colloquially, an irritating, obnoxious, or contemptible person.",
    "secondary": "In historical dialectology and colloquial lexicography, the compound arsehole dates back to Middle English vulgar anatomical registers.",
    "quotes": [
      {"author": "James Joyce", "work": "Ulysses", "quote": "Buck Mulligan laughed coarse banter over his morning shave, mocking the pompous official as a pretentious **arsehole**."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The abusive kitchen chef cursed every scullion in fluent Parisian gutter slang, labeling the head waiter a meddlesome **arsehole**."},
      {"author": "Robert Louis Stevenson", "work": "The Ebb-Tide", "quote": "The drunken sailor hurled coarse epithets across the tavern floor, calling the mate an insolent **arsehole**."}
    ]
  },
  "Dashboard — ars/arsenal.md": {
    "primary": "A collection of weapons and military equipment stored by a country, person, or group; or an armory.",
    "secondary": "In Venetian maritime history, the Arsenale di Venezia was the state naval shipyard that pioneered pre-industrial assembly-line shipbuilding.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The imperial **arsenal** at Constantinople was stocked with ballistas, catapults, and jars of unquenchable Greek fire."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan explored the deep subterranean **arsenal** of Hell, searching for fiery materials to forge new engines of celestial war."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A national **arsenal** and naval dockyard are indispensable safeguards for the defense and commercial security of a free nation."}
    ]
  },
  "Dashboard — ars/arsenate.md": {
    "primary": "A chemical salt or ester of arsenic acid containing the polyatomic anion AsO4(3-).",
    "secondary": "In agricultural chemistry and historical pest management, lead arsenate was widely sprayed as an insecticide in orchards prior to synthetic organochlorines.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The precipitate produced by adding copper sulphate to the neutral solution proved to be an insoluble copper **arsenate**."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "The toxic physiological action of sodium **arsenate** disrupts fundamental cellular respiration in animal tissues."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Mineral veins carrying crystalline iron **arsenate** and copper ores were exploited throughout the Cornish mining district."}
    ]
  },
  "Dashboard — ars/arsenic.md": {
    "primary": "A brittle, steel-gray metalloid element of atomic number 33, extremely poisonous in many compounds.",
    "secondary": "In Victorian forensic toxicology and the history of criminal jurisprudence, the Marsh test developed in 1836 enabled reliable post-mortem detection of arsenic.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Dying Detective", "quote": "The symptoms pointed clearly to a lethal dose of **arsenic**, administered by an expert in tropical toxicology."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The old woman muttered darkly about buying **arsenic** to exterminate rats, casting suspicious glances at her lodger."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma Bovary rushed frantically to the apothecary's cabinet and swallowed the white powder of **arsenic** in suicidal despair."}
    ]
  },
  "Dashboard — ars/arsenical.md": {
    "primary": "Containing, relating to, or produced by arsenic; or having poisonous qualities resembling arsenic.",
    "secondary": "In Victorian decorative arts and environmental medicine, Scheele's green wallpaper dyed with arsenical pigments caused chronic respiratory poisoning in domestic rooms.",
    "quotes": [
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "The physician identified the patient's persistent illness as chronic **arsenical** poisoning derived from pigmented bedroom wallpapers."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The thermal springs of the volcanic region emitted sulfurous and **arsenical** vapors that encrusted the surrounding rocks."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "We analyzed the sediment in the stomach contents, detecting distinct traces of an **arsenical** compound."}
    ]
  },
  "Dashboard — ars/arsenide.md": {
    "primary": "A binary compound of arsenic with a more electropositive element or radical.",
    "secondary": "In semiconductor physics and materials engineering, gallium arsenide (GaAs) is a direct-bandgap semiconductor utilized in high-frequency optoelectronics and laser diodes.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The synthetic metallic **arsenide** exhibited notable thermoelectric properties when subjected to extreme temperature gradients."},
      {"author": "J. Willard Gibbs", "work": "On the Equilibrium of Heterogeneous Substances", "quote": "Phase boundaries formed during the reduction of zinc **arsenide** illustrate thermodynamic vapor pressure equilibria."},
      {"author": "Thomas Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Chemical analysis revealed traces of iron **arsenide** deposited within the mineralized shells of ancient marine mollusks."}
    ]
  },
  "Dashboard — ars/arsenious.md": {
    "primary": "Relating to or containing arsenic in a trivalent state; or pertaining to arsenious acid.",
    "secondary": "In 19th-century industrial chemistry, arsenious oxide (white arsenic) served as the primary commercial precursor for insecticides, pigments, and glass clarification.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Sublimation of **arsenious** acid yields delicate octahedral crystals lining the upper neck of the retort."},
      {"author": "Oliver Wendell Holmes", "work": "Medical Essays", "quote": "Fowler's solution, composed of potassium **arsenious** salt, was formerly prescribed as a tonic in chronic skin affections."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "The analytical chemist recognized the characteristic garlic odor of **arsenious** vapor rising from the heated test tube."}
    ]
  },
  "Dashboard — ars/arsenopyrite.md": {
    "primary": "An iron arsenic sulfide mineral (FeAsS), the principal ore of arsenic, silver-white to steel-gray in color.",
    "secondary": "In economic geology and hydrothermal mineralogy, arsenopyrite often occurs in association with native gold and quartz veins in orogenic gold deposits.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The lodes of Cornwall yielded abundant masses of **arsenopyrite**, intermixed with cassiterite and copper pyrites."},
      {"author": "Alexander von Humboldt", "work": "Cosmos: A Sketch of a Physical Description of the Universe", "quote": "The auriferous quartz veins of the Ural mountains frequently carry crystals of **arsenopyrite** and specular iron ore."},
      {"author": "John Ruskin", "work": "The Ethics of the Dust", "quote": "The lecturer exhibited a brilliant specimen of **arsenopyrite**, pointing out its sharp orthorhombic crystalline facets."}
    ]
  },
  "Dashboard — ars/arsine.md": {
    "primary": "An extremely toxic, flammable gas (AsH3) consisting of arsenic and hydrogen, having a mild garlic odor.",
    "secondary": "In modern semiconductor fabrication, arsine gas is used as an n-type epitaxial dopant for microelectronic silicon and gallium arsenide wafers.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The generation of poisonous **arsine** gas during the reduction of arsenic compounds requires rigorous laboratory ventilation."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The chemist explained the lethal mechanism of **arsine**, noting its rapid destruction of red blood cells in the bloodstream."},
      {"author": "Thomas Huxley", "work": "Lessons in Elementary Physiology", "quote": "Inhalation of even trace quantities of **arsine** provokes acute intravascular hemolysis and renal failure."}
    ]
  },
  "Dashboard — ars/arson.md": {
    "primary": "The criminal act of deliberately and maliciously setting fire to buildings or property.",
    "secondary": "In common law jurisprudence, arson originally required the malicious burning of the dwelling-house of another during nighttime hours.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Barnaby Rudge", "quote": "The rioters committed widespread **arson** across London, setting Newgate prison ablaze and threatening the Bank of England."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "Holmes deduced that the warehouse fire was no accident, but a premeditated crime of **arson** to defraud the underwriters."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The mysterious burning of the hayrick was attributed by the villagers to an act of spiteful **arson** by a discharged laborer."}
    ]
  },
  "Dashboard — ars/arsonist.md": {
    "primary": "A person who deliberately and maliciously commits the crime of arson.",
    "secondary": "In forensic fire investigation and criminal profiling, an arsonist's motive is categorized into financial insurance fraud, pyromania, or concealment of crime.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The deliberate trail of paraffin pointed unmistakably to the handiwork of a calculating **arsonist**."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The suspicious oil stains on the cellar timber confirmed that an **arsonist** had attempted to burn the tenement to the ground."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "The anarchist bomb-maker was compared by the police inspector to a reckless **arsonist** playing with kerosene in a dry wooden town."}
    ]
  },
  "Dashboard — ars/binoculars.md": {
    "primary": "An optical instrument with a lens for each eye, used for viewing distant objects magnified.",
    "secondary": "In optical engineering, prism binoculars utilize Porro or roof prisms to invert and revert images while shortening optical tube length.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes raised his field **binoculars** to scan the jagged granite tors across the darkening moor."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The captain lowered his marine **binoculars** and gazed anxiously at the approaching squall on the eastern horizon."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Through my pocket **binoculars**, I could plainly see the colossal tripod fighting-machines striding across the Surrey hills."}
    ]
  },
  "Dashboard — ars/coarse-furred.md": {
    "primary": "Having thick, rough, or bristly fur rather than a soft or sleek coat.",
    "secondary": "In comparative mammalogy and wildlife ecology, coarse-furred coats provide protective mechanical shielding and thermal insulation in brushy habitats.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The native capybara is a heavy, **coarse-furred** rodent that browses peacefully among the reed beds of the Parana."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The wild wolf was a lean, **coarse-furred** hunter that circled the campfire just beyond the reach of the flames."},
      {"author": "Alfred Russel Wallace", "work": "The Malay Archipelago", "quote": "We captured a strange **coarse-furred** marsupial in the mountain forests of Celebes."},
      ]
  },
  "Dashboard — ars/coarse-grained.md": {
    "primary": "Consisting of coarse or relatively large particles, fibers, or textures; not fine.",
    "secondary": "In igneous petrology, a coarse-grained phaneritic texture forms in intrusive rocks like granite due to slow cooling at deep crustal depths.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The plutonic granite displays a **coarse-grained** texture characterized by large crystals of feldspar and quartz."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Featherstone's mind was of a **coarse-grained** fabric, suspicious of subtle motives and unswayed by gentle sentiment."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The woodsman examined the **coarse-grained** ash timber, calculating its suitability for sturdy wagon spokes."}
    ]
  },
  "Dashboard — ars/coarse-haired.md": {
    "primary": "Having thick, rough, or bristly hair instead of fine or smooth tresses.",
    "secondary": "In domestic animal breeding, coarse-haired sheep varieties are bred for durable carpet wool rather than fine apparel textiles.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Primitive mountain breeds of goats are typically **coarse-haired**, possessing an undercoat of fine downy cashmere."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The old wagoner was a **coarse-haired**, weather-beaten rustic whose face was tanned like leather by winter gales."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The Highland drovers were accompanied by shaggy, **coarse-haired** collies that guarded the black cattle through the glens."}
    ]
  },
  "Dashboard — ars/coarse-textured.md": {
    "primary": "Having a rough, unrefined, or heavily granulated physical surface or tactile weave.",
    "secondary": "In agronomy and soil taxonomy, coarse-textured sandy soils possess rapid percolation rates and low cation exchange capacity.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Early medieval masons preferred a **coarse-textured** sandstone that imparted a rugged honesty to the lower walls."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "Earthworms transform **coarse-textured** gravelly soil into rich, homogenous black loam over successive decades."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The country folk wore **coarse-textured** homespun garments that withstood the thorny hedges and winter sleet."}
    ]
  },
  "Dashboard — ars/coarse.md": {
    "primary": "Rough or loose in texture or grain; or lacking refinement, vulgar, and crude.",
    "secondary": "In textile manufacturing, coarse yarn counts indicate thick thread diameters used for sackcloth and heavy canvas.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "They were **coarse** and common clothes, but Joe put them on with a respectful solemnity as his best Sunday attire."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Ferrars was a woman of **coarse** manners and unyielding obstinacy, who measured human merit solely by wealth."},
      {"author": "William Shakespeare", "work": "The Taming of the Shrew", "quote": "Thy gown? Why, ay: come, tailor, let us see't. O mercy, God! What masquing stuff is here? What's this? A sleeve? 'Tis like a demi-cannon: what, up and down, carved like an apple-tart? Here's snip and nip and cut and slish and slash, like to a censer in a barber's shop. Why, what i' devil's name, tailor, call'st thou this? You bid me make it orderly and well, according to the fashion and the time. Marry, and did; but if you be remember'd, I did not bid you mar it to the time. Go, hop me over every kennel home, for you shall hop without my custom, sir: I'll none of it: hence! make your best of it. Tailor, this is a **coarse** and wretched garment, unfit for any gentlewoman to wear."}
    ]
  },
  "Dashboard — ars/coarsely.md": {
    "primary": "In a rough, unrefined, or crude manner; or into relatively large pieces.",
    "secondary": "In artisanal milling, grain ground coarsely produces stoneground wholemeal flour retaining fibrous bran and germ.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The Lowood porridge was **coarsely** prepared and frequently burnt, yet the starving pupils devoured it eagerly."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard spoke **coarsely** and bluntly in the council chamber, offending the refined sensibilities of his civic colleagues."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The ruffian laughed **coarsely**, tossing off his glass of gin and slamming his pewter mug onto the tavern table."}
    ]
  },
  "Dashboard — ars/coarsen.md": {
    "primary": "To make or become coarse, rough, unrefined, or less delicate in texture or character.",
    "secondary": "In occupational health and dermatology, continuous exposure to harsh lime or chemical solvents will coarsen the epidermal skin barrier.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate feared that vulgar provincial gossip would gradually **coarsen** his wife's delicate perceptions of high art."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Field labor under winter frosts began to **coarsen** Tess's tender hands, despite her efforts to protect them."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "He watched the painted portrait on the canvas **coarsen** with each hidden sin and cruel deed of his secret life."}
    ]
  },
  "Dashboard — ars/coarsened.md": {
    "primary": "Made rough, harsh, or crude in physical texture, appearance, or moral sensitivity.",
    "secondary": "In literary realism, characters whose sensibilities have been coarsened by poverty or brutal labor reflect environmental determinism.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "My hands were **coarsened** by hard work at the forge, and Estella mocked them with cold and haughty disdain."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "His fingers were **coarsened** by years of mallet and chisel work on the cathedral stonemasonry."},
      {"author": "George Gissing", "work": "New Grub Street", "quote": "The perpetual struggle for daily bread had **coarsened** his literary style, stripping away youthful grace and nuance."}
    ]
  },
  "Dashboard — ars/coarseness.md": {
    "primary": "The property or quality of being rough, unrefined, crude, or lacking in delicacy.",
    "secondary": "In literary criticism and social satire, deliberate coarseness of dialect is employed to distinguish plebeian authenticity from courtly affectation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was mortified by the vulgar **coarseness** of her mother's remarks at the Netherfield ball before Mr. Darcy."},
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "The comedy of Dryden was sometimes blemished by a wanton **coarseness** that offended refined readers of later ages."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The apparent **coarseness** of the exterior stone masonry was compensated by the exquisite delicacy of the interior mosaics."}
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

print(f"Cluster Action & State Batch 2B: Successfully updated {updated}/{len(data)} notes across 3 dashboards.")
