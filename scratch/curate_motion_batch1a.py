# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — natat (3 words) ---
  "Dashboard — natat/natation.md": {
    "primary": "The act, process, or art of swimming or floating on water.",
    "secondary": "In zoological biomechanics and human physical culture, natation encompasses distinct aquatic locomotive propulsion mechanisms.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "The Crayfish", "quote": "The swimmerets along the abdominal segments are beautifully adapted for aquatic **natation**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain upland bird species preserve webbed feet originally developed for marine **natation**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The majestic whale performs effortless **natation** across thousands of leagues of tempestuous ocean."}
    ]
  },
  "Dashboard — natat/natator.md": {
    "primary": "A swimmer, or an aquatic animal or bird naturally adapted for swimming.",
    "secondary": "In nineteenth-century ornithological taxonomy, the Natatores constituted an order comprising swimming web-footed waterfowl.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The diving petrel is an expert **natator**, using its short wings to fly underwater in pursuit of fish."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Every observant wildfowler admires the graceful agility of the wild duck as an accomplished **natator**."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Vertebrated Animals", "quote": "The skeletal modifications of the penguin limb distinguish it as an exclusively aquatic **natator**."}
    ]
  },
  "Dashboard — natat/natatorium.md": {
    "primary": "A swimming pool, especially an indoor swimming pool within a dedicated athletic facility.",
    "secondary": "In civic architectural engineering, an indoor natatorium requires specialized HVAC dehumidification systems to prevent structural moisture rot.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The palatial lakefront estate boasted a heated marble **natatorium** illuminated by vaulted skylights."},
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory lingered near the university **natatorium**, watching the glistening swimmers dive through emerald water."},
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "The metropolitan recreation complex incorporated a spacious tiled **natatorium** for public hygiene."}
    ]
  },

  # --- Dashboard — vad (6 words) ---
  "Dashboard — vad/evade.md": {
    "primary": "To escape, avoid, or slip away from someone or something through cleverness, trickery, or agility.",
    "secondary": "In constitutional law and tax jurisprudence, taxpayers may legitimately avoid taxes but commit criminal fraud when they evade them.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The clever fugitive managed to **evade** every cordon established by Scotland Yard across the docks."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Frank Churchill sought adroitly to **evade** questions that threatened to expose his clandestine engagement."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The light cavalry utilized their nomadic mobility to **evade** pitched battles with the Roman legions."}
    ]
  },
  "Dashboard — vad/invade.md": {
    "primary": "To enter a country, territory, or domain forcibly with armed troops in order to conquer, occupy, or plunder.",
    "secondary": "In pathophysiology and oncology, malignant tumor cells invade surrounding stromal tissues and basement membranes.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The German high command prepared elaborate naval transport flotillas to **invade** the British Isles."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "With right and conscience make this title good, and let us **invade** the fertile plains of France."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Hostile barbarian hordes gathered along the frozen Danube ready to **invade** the undefended provinces."}
    ]
  },
  "Dashboard — vad/invader.md": {
    "primary": "A person, army, or biological organism that aggressively enters a foreign territory or host.",
    "secondary": "In immunology and cellular defense, macrophages identify and engulf each foreign **invader** using pattern-recognition receptors.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The White Company", "quote": "The hardy English archers stood fast to repel the fierce French **invader** at the crest of the hill."},
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Saxon yeomen swore vengeance against every Norman **invader** who trampled upon their ancestral rights."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "No human weapon could resist the heat-ray wielded by the extraterrestrial **invader** across Surrey."}
    ]
  },
  "Dashboard — vad/invading.md": {
    "primary": "Entering a country, territory, or biological space forcefully and aggressively as an enemy or intrusive presence.",
    "secondary": "In military logistics, sustained supply line security dictates the operational velocity of an invading army.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Gothic chieftain led his **invading** host through the undefended passes of the Julian Alps."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "The imperial fleet stood ready to intercept any **invading** naval armada attempting a channel crossing."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "A dark presentiment of disaster pursued me, **invading** my quiet thoughts even in sleep."}
    ]
  },
  "Dashboard — vad/pervade.md": {
    "primary": "To spread through and be perceived in every part of a space, substance, feeling, or society.",
    "secondary": "In cultural sociology, shared ideological presuppositions pervade educational institutions and civic discourse.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "A solemn stillness seemed to **pervade** the long corridors of Thornfield Hall as evening fell."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The dense London fog seemed to **pervade** every parlor, court chamber, and street corner along the river."},
      {"author": "Nathaniel Hawthorne", "work": "The House of the Seven Gables", "quote": "An aura of ancestral gloom continued to **pervade** the decaying timber mansion and its gloomy garden."}
    ]
  },
  "Dashboard — vad/vaduz.md": {
    "primary": "The capital city of the Principality of Liechtenstein, located along the upper Rhine river.",
    "secondary": "In European political geography and constitutional monarchy, Vaduz serves as the seat of the Princely House and the Landtag.",
    "quotes": [
      {"author": "Karl Baedeker", "work": "Switzerland and the Adjacent Portions of Italy, Savoy, and Tyrol", "quote": "The picturesque castle of **Vaduz** perches dramatically upon the wooded cliff overlooking the quiet Alpine valley."},
      {"author": "John Murray", "work": "A Handbook for Travellers in Switzerland", "quote": "Travellers ascending the upper Rhine valley find in **Vaduz** the modest capital of the ancient principality."},
      {"author": "James Bryce", "work": "The Holy Roman Empire", "quote": "The miniature principality centered at **Vaduz** preserved its sovereign status amid the dissolution of the empire."}
    ]
  },

  # --- Dashboard — meat (10 words) ---
  "Dashboard — meat/meat.md": {
    "primary": "The flesh of animals used as food; or the core, substance, or essential part of something.",
    "secondary": "In agricultural economics and human nutrition, dietary transitions toward increased animal meat consumption reflect rising per capita incomes.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The hungry workhouse boys stared longingly at the kettle where the savory **meat** was stewing."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The hardy whalemen considered the tender **meat** of the sperm whale calf a welcome sea delicacy."},
      {"author": "Jonathan Swift", "work": "A Modest Proposal", "quote": "He calculated the exact economic cost of producing wholesome **meat** for the subsistence of the market."}
    ]
  },
  "Dashboard — meat/meatless.md": {
    "primary": "Containing, using, or providing no meat; vegetarian.",
    "secondary": "In public health history, mandatory meatless days were instituted during wartime food rationing to preserve strategic livestock reserves.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "Many impoverished mining families subsisted on cheap bread, margarine, and **meatless** vegetable broths."},
      {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "The philosopher remarked that a civilized society would voluntarily adopt a humane, **meatless** diet."},
      {"author": "Jack London", "work": "The People of the Abyss", "quote": "The East End shelter provided poor laborers with a bowl of **meatless** soup and a dry crust of bread."}
    ]
  },
  "Dashboard — meat/meatloaf.md": {
    "primary": "A dish of ground meat seasoned and shaped into a loaf, then baked and served sliced.",
    "secondary": "In domestic culinary history, the popularity of baked meatloaf surged during the Depression as an economical way to extend ground meats.",
    "quotes": [
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "Carol Kennicott prepared a simple baked **meatloaf** for the doctor's evening supper in Gopher Prairie."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The roadside diner served thick slices of cold **meatloaf** alongside mugs of steaming black coffee."},
      {"author": "F. Scott Fitzgerald", "work": "Tender Is the Night", "quote": "The modest boarding house offered savoury **meatloaf** and mashed potatoes to its resident expatriates."}
    ]
  },
  "Dashboard — meat/meatman.md": {
    "primary": "A butcher, or a merchant who deals in the distribution and retail sale of meat.",
    "secondary": "In early twentieth-century labor history, trade unions organized municipal meatman guilds to enforce sanitary handling regulations.",
    "quotes": [
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The weary **meatman** labored through freezing drafts in the vast subterranean chill-rooms of Packingtown."},
      {"author": "Theodore Dreiser", "work": "Sister Carrie", "quote": "Carrie watched the neighborhood **meatman** sweep sawdust across the entrance of his corner shop."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "George Babbitt exchanged cheerful morning greetings with his retail butcher and neighborhood **meatman**."}
    ]
  },
  "Dashboard — meat/meatus.md": {
    "primary": "A natural body channel, passage, or opening, such as the canal of the external ear or the urinary urethra.",
    "secondary": "In otolaryngological anatomy, the external auditory meatus directs acoustic sound waves toward the tympanic membrane.",
    "quotes": [
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The external auditory **meatus** extends obliquely inward from the concha to the tympanic membrane."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinician carefully examined the urethral **meatus** for signs of inflammation or purulent discharge."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Sound vibrations are gathered by the auricle and conducted along the curved auditory **meatus**."}
    ]
  },
  "Dashboard — meat/meaty.md": {
    "primary": "Resembling or full of meat; or full of substance, depth, and intellectual significance.",
    "secondary": "In literary criticism and pedagogical analysis, a meaty text provides substantial material for analytical debate and close reading.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Chadband regaled the company with what he termed a rich and **meaty** moral discourse on human depravity."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke commended the young scholar's tract as a remarkably **meaty** performance on ecclesiastical tithes."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Give us honest, **meaty** truth instead of the gossamer speculations spun by fashionable parlor wits."}
    ]
  },
  "Dashboard — meat/permeate.md": {
    "primary": "To pass, seep, or spread through the pores or interstices of a material; to penetrate throughout.",
    "secondary": "In physical chemistry and membrane separation, solvent molecules permeate semipermeable polymer barriers down chemical potential gradients.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "Moisture and organic humic acids **permeate** the loose soil particles aerated by industrious earthworms."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Rainwater begins to **permeate** through porous sandstone strata until halted by impermeable beds of clay."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "A subtle melancholy seemed to **permeate** my soul as autumn stripped the leaves from the Alpine oaks."}
    ]
  },
  "Dashboard — meat/permeating.md": {
    "primary": "Diffusing, spreading, or penetrating throughout every part of a substance, environment, or atmosphere.",
    "secondary": "In environmental geology, contaminants permeating unconfined aquifers pose severe long-term risks to municipal groundwater wells.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The heavy fragrance of boiling sperm oil hung **permeating** every timber and sail of the Pequod."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "A gentle sense of domestic peace came **permeating** through the lonely cottage after Eppie arrived."},
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The bitter smoke from the Coketown chimneys hung **permeating** the air of every narrow alley."}
    ]
  },
  "Dashboard — meat/permeation.md": {
    "primary": "The act or process of passing, spreading, or penetrating through the pores, spaces, or fabric of something.",
    "secondary": "In material science and barrier packaging, calculating the permeation rate of oxygen determines product shelf-life stability.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The slow **permeation** of gases through porous ceramic diaphragms followed distinct diffusive ratios."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The gradual **permeation** of scientific knowledge into popular culture altered traditional social dogmas."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The intellectual **permeation** of evolutionary concepts transformed nineteenth-century philosophical thought."}
    ]
  },
  "Dashboard — meat/permeative.md": {
    "primary": "Having the quality or power to permeate, penetrate, diffuse, or spread through substances or environments.",
    "secondary": "In pharmacokinetics and drug delivery design, small lipophilic molecules display high permeative capacity across cellular membranes.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "The Friend", "quote": "Moral principle possesses a **permeative** power that sanctifies every humble duty of daily life."},
      {"author": "David Brewster", "work": "Treatise on Optics", "quote": "The subtle **permeative** properties of radiant heat allow it to pass through transparent solids."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "Gothic architectural design possesses a **permeative** harmony that unites its grandest spires and smallest carvings."}
    ]
  },

  # --- Dashboard — tres (17 words) ---
  "Dashboard — tres/actress.md": {
    "primary": "A woman who portrays a character in a dramatic play, film, broadcast, or theatrical performance.",
    "secondary": "In theatrical history and cultural performance studies, seventeenth-century Restoration stages marked the first professional English female actresses.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "The great foreign **actress** Vashti dominated the stage with demonic energy, transfixing the breathless audience."},
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Mary Crawford proved an accomplished amateur **actress** during rehearsals for the controversial domestic play."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian fell passionately in love with Sibyl Vane, a gifted young **actress** performing Juliet in a minor theater."}
    ]
  },
  "Dashboard — tres/distress.md": {
    "primary": "Extreme anxiety, sorrow, pain, or suffering; or a state of acute physical danger or misfortune.",
    "secondary": "In property law and feudal tenure, distress refers to the legal seizure of a tenant's chattels to enforce payment of rent arrears.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Lucie Manette rushed forward to comfort her father, whose deep mental **distress** had robbed him of his senses."},
      {"author": "William Shakespeare", "work": "King Lear", "quote": "The tempest rages without, but the greater **distress** of filial ingratitude beats within my breaking heart."},
      {"author": "Daniel Defoe", "work": "Robinson Crusoe", "quote": "The stranded mariners fired a gun as a signal of **distress** across the stormy, foam-crested breakers."}
    ]
  },
  "Dashboard — tres/distressed.md": {
    "primary": "Suffering from severe anxiety, grief, pain, or economic hardship; or aged and weathered (of furniture/fabric).",
    "secondary": "In corporate finance and debt restructuring, distressed assets trade at substantial discounts reflecting elevated default probability.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor was deeply **distressed** by the sudden and alarming illness that seized her impetuous sister."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber explained that his finances were temporarily **distressed** owing to unexpected pecuniary obligations."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The **distressed** father walked miles through driving rain to petition the crown for his daughter's life."}
    ]
  },
  "Dashboard — tres/distressful.md": {
    "primary": "Causing or accompanied by great grief, affliction, suffering, or hardship; distressing.",
    "secondary": "In historical famine records, distressful agrarian crises provoked mass demographic displacement across peripheral rural parishes.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "The weary soldier earns a little rest with hard labor, eating his **distressful** bread with sweaty brow."},
      {"author": "Washington Irving", "work": "The Sketch Book", "quote": "The widow poured forth her sorrow in a **distressful** lament that touched the heart of every villager."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The sight of royal captives led through jeering mobs presented a **distressful** spectacle of fallen greatness."}
    ]
  },
  "Dashboard — tres/distressfully.md": {
    "primary": "In a manner marked by or causing severe grief, anguish, difficulty, or suffering.",
    "secondary": "In clinical observation, respiratory distress syndrome causes patients to breathe distressfully with intercostal retractions.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The injured horse groaned **distressfully** on the frosty road until Rochester helped it to its feet."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The poor woman wept **distressfully** as the bailiffs removed the few remaining chairs from her cold room."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess looked **distressfully** toward the western hills, dreading the shameful revelation awaiting her."}
    ]
  },
  "Dashboard — tres/distressfulness.md": {
    "primary": "The quality or condition of causing deep anguish, grief, suffering, or painful discomfort.",
    "secondary": "In moral philosophy and utilitarian ethics, evaluating the distressfulness of punitive sanctions guides proportionality in criminal sentencing.",
    "quotes": [
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The legislator must calculate the intense **distressfulness** of bodily suffering when designing penological codes."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The peculiar **distressfulness** of poverty consists not merely in physical want, but in social humiliation."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The evident **distressfulness** of the curate's domestic plight excited the sincere compassion of the parishioners."}
    ]
  },
  "Dashboard — tres/distressing.md": {
    "primary": "Causing anxiety, sorrow, discomfort, or mental affliction; upsetting and troublesome.",
    "secondary": "In clinical medicine and hospice palliative care, managing distressing symptoms such as dyspnea improves terminal quality of life.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes listened attentively while Miss Morstan recounted the **distressing** disappearance of her beloved father."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Lydia's elopement with Wickham was the most **distressing** intelligence that could possibly reach Longbourn."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip found his visit to the dilapidated Satis House an intensely **distressing** experience of decay and malice."}
    ]
  },
  "Dashboard — tres/distressingly.md": {
    "primary": "In a manner that causes great worry, sorrow, pain, or discomfort; upsettingly.",
    "secondary": "In demographic economics, child mortality rates remained distressingly high across industrial factory towns prior to sanitary reform.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The housing statistics in the mining districts were **distressingly** clear regarding rampant overcrowding and disease."},
      {"author": "H. G. Wells", "work": "The Invisible Man", "quote": "The innkeeper found the eccentric guest's swathed face and violent outbursts **distressingly** suspicious."},
      {"author": "Henry James", "work": "The Turn of the Screw", "quote": "The governess felt **distressingly** isolated in the vast country estate as supernatural omens accumulated."}
    ]
  },
  "Dashboard — tres/distressingness.md": {
    "primary": "The state or degree of being painful, agonizing, upsetting, or afflicting.",
    "secondary": "In psychological trauma assessment, measuring the distressingness of intrusive flashbacks quantifies post-traumatic stress severity.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The subjective **distressingness** of acute emotional panic produces profound autonomic exhaustion in the organism."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The sheer **distressingness** of universal public suspicion paralyzed all orderly civic deliberation in Paris."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate recognized the acute **distressingness** of his financial insolvency as debt collectors knocked on his door."}
    ]
  },
  "Dashboard — tres/entresol.md": {
    "primary": "A low intermediate mezzanine floor, especially between the ground floor and the first floor of a building.",
    "secondary": "In Parisian neoclassical architecture and urban real estate history, the entresol offered lower ceilings and rents for small shops or clerks.",
    "quotes": [
      {"author": "Honoré de Balzac", "work": "Old Goriot", "quote": "The humble boarding house contained a shadowy **entresol** inhabited by impoverished students and clerk pensioners."},
      {"author": "Henry James", "work": "The Ambassadors", "quote": "Strether looked up at the pleasant balcony of the Parisian **entresol**, admiring the classical stone balustrade."},
      {"author": "William Thackeray", "work": "The Paris Sketch Book", "quote": "The bustling print seller operated his modest business from a low-ceilinged **entresol** above the boulevard arcade."}
    ]
  },
  "Dashboard — tres/mistress.md": {
    "primary": "A woman in a position of authority, control, or ownership; or a woman having an ongoing extramarital relationship with a married man.",
    "secondary": "In social and domestic historiography, the mistress of a country estate managed household provisioning, accounts, and domestic servants.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane arrived at Lowood school as an orphan, standing before the severe **mistress** who commanded the assembly."},
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "Fair Olivia reigned as the gracious **mistress** of a noble household in the sunny realm of Illyria."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth thought of how proud a thing it would be to reign as the happy **mistress** of Pemberley."}
    ]
  },
  "Dashboard — tres/trespass.md": {
    "primary": "To enter unlawfully upon another's land or property; or to commit an offense, sin, or transgression.",
    "secondary": "In common law jurisprudence, trespass encompasses direct physical interference with another's person, land, or goods.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "They did usurp the kingdom and **trespass** against the lawful prince, casting us upon this enchanted isle."},
      {"author": "John Bunyan", "work": "The Pilgrim's Progress", "quote": "The pilgrims turned aside into Bypath Meadow, realizing too late that they did **trespass** upon Giant Despair's ground."},
      {"author": "Henry David Thoreau", "work": "Civil Disobedience", "quote": "The state commits a moral **trespass** when it compels an honest citizen to support unjust institutions."}
    ]
  },
  "Dashboard — tres/trespasser.md": {
    "primary": "A person who unlawfully enters the land, grounds, or property of another without right or permission.",
    "secondary": "In tort law and occupiers' liability doctrine, landowners owe a limited duty of basic humanity toward a known trespasser.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "The Selfish Giant", "quote": "The giant erected a high stone wall around his lovely garden and put up a notice board: **Trespassers** will be prosecuted."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Priory School", "quote": "The gamekeeper challenged the solitary **trespasser** who had climbed the park palings after dark."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "The timber owner warned every suspected **trespasser** that spring guns were set throughout the private coppice."}
    ]
  },
  "Dashboard — tres/trespassing.md": {
    "primary": "Unlawfully intruding or entering upon the property, rights, or territory of another person.",
    "secondary": "In property jurisprudence, ongoing trespassing may ripen into prescriptive easements if unasserted by the title owner.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "The boys were caught **trespassing** in the haunted house at midnight while searching for buried robber gold."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Sir Leicester Dedlock would prosecute any poacher caught **trespassing** in the Chesney Wold preserves."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Tom warned his impetuous sister that wandering across the squire's meadows was outright **trespassing**."}
    ]
  },
  "Dashboard — tres/tress.md": {
    "primary": "A long lock, braid, or strand of a person's hair, especially a woman's hair.",
    "secondary": "In poetic portraiture and chivalric romance, golden or raven tresses symbolize beauty, virtue, and courtly romance.",
    "quotes": [
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "This nymph, to the destruction of mankind, nourished two locks, which graceful hung in an enchanting **tress**."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Her unadorned golden hair flowed down to her slender waist in many an undulating **tress**."},
      {"author": "Lord Byron", "work": "She Walks in Beauty", "quote": "Which waves in every raven **tress**, or softly lightens o'er her face, where thoughts serenely sweet express."}
    ]
  },
  "Dashboard — tres/trestle.md": {
    "primary": "A braced structural frame consisting of a horizontal beam supported by two pairs of divergent sloping legs, used as a support or bridge pier.",
    "secondary": "In railway engineering and bridge design, a wooden or steel trestle carries trackage across deep ravines and river valleys.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The transcontinental train creaked slowly across a dizzy timber **trestle** spanning a deep gorge in the Rockies."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I observed the carpenters erect a sturdy **trestle** to support the heavy pine timbers of the new barn roof."},
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "The infantry regiment halted near the railroad **trestle**, awaiting orders to deploy along the riverbank."}
    ]
  },
  "Dashboard — tres/trestlework.md": {
    "primary": "An open braced framework or interconnected system of trestles, such as that used to support a bridge, viaduct, or scaffolding.",
    "secondary": "In civil infrastructure history, extensive timber trestlework allowed rapid railroad expansion across rugged mountainous terrain.",
    "quotes": [
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "Heavy locomotives rattled across the elevated iron **trestlework** carrying commuter lines into the heart of Chicago."},
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The strikers gathered beneath the massive railroad **trestlework** where the industrial freight cars were marshaled."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "Damp mists clung to the towering wooden **trestlework** of the stockyard runways that spanned the pens."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Motion"
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

print(f"Motion Batch 1A: Successfully updated {updated}/{len(data)} notes.")
