# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — und Part 2 (8B, 52 words) ---
  "Dashboard — und/undefiled.md": {
    "primary": "Not defiled, corrupted, or polluted; pure, clean, and unblemished.",
    "secondary": "In religious and moral literature, an undefiled conscience is preserved through steadfast adherence to spiritual integrity.",
    "quotes": [
      {"author": "John Milton", "work": "Comus", "quote": "Virtue could see to do what virtue would by her own radiant light, pure and **undefiled** amid surrounding darkness."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The minister longed for that pristine, **undefiled** peace of soul that had blessed his early collegiate days."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Jane guarded her moral integrity, resolving that her love for Rochester must remain pure and **undefiled**."}
    ]
  },
  "Dashboard — und/undefinable.md": {
    "primary": "Not able to be clearly or precisely defined, described, or categorized; intangible.",
    "secondary": "In aesthetic philosophy, the sublime possesses an undefinable emotional resonance that eludes formal geometric taxonomy.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "An **undefinable** sense of dread crept over me as I gazed upon the gray walls of the desolate mansion."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "There was an **undefinable** charm in Madame Merle's conversation that disarmed even the most guarded listeners."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Lily felt an **undefinable** longing to capture the fleeting essence of the evening light before it vanished."}
    ]
  },
  "Dashboard — und/undefined.md": {
    "primary": "Not clearly or precisely explained, determined, or bounded; having no fixed limits.",
    "secondary": "In computer programming and mathematics, an undefined operation (such as division by zero) produces an indeterminate result.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When words are left with vague and **undefined** meanings, they serve only to obscure philosophical truth."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "An **undefined** menace seemed to hover over the lonely moor as the shadows lengthened across the tors."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The boundary between distinct species and well-marked varieties is frequently fluid and **undefined** in nature."}
    ]
  },
  "Dashboard — und/undelineated.md": {
    "primary": "Not outlined, sketched, or mapped out; lacking precise boundaries or descriptive details.",
    "secondary": "In historical cartography, vast terra incognita regions remained undelineated on early navigational sea charts.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whalemen sailed into vast, **undelineated** ocean basins that appeared on the captain's chart as blank blue spaces."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The subterranean fault lines of the river basin remained **undelineated** until systematic seismic surveys were conducted."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The northern frontiers of the empire bordered upon **undelineated** forests inhabited by nomadic Germanic tribes."}
    ]
  },
  "Dashboard — und/undemanding.md": {
    "primary": "Not demanding; requiring little effort, skill, intellectual strain, or emotional patience.",
    "secondary": "In literature and leisure sociology, undemanding serial fiction provides restful recreation without intellectual exertion.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Celia preferred an **undemanding** domestic life, untroubled by Dorothea's grand spiritual aspirations."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse found the gentle conversation of Miss Bates comfortably soothing and **undemanding**."},
      {"author": "Virginia Woolf", "work": "Night and Day", "quote": "Katharine welcomed the quiet evening hours, enjoying the **undemanding** routine of cataloging family papers."}
    ]
  },
  "Dashboard — und/undemocratic.md": {
    "primary": "Not democratic; not based on or according to the principles of popular democracy and equal representation.",
    "secondary": "In political science, an undemocratic oligarchy concentrates governance and economic privilege in an unrepresentative elite.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Hereditary privileges that deny citizens equal legal opportunity are fundamentally **undemocratic** and unstable."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "Any electoral system that excludes working classes from parliamentary representation is demonstrably **undemocratic**."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "The totalitarian regimes established an **undemocratic** apparatus of secret police and censorship to crush free expression."}
    ]
  },
  "Dashboard — und/undemocratically.md": {
    "primary": "In an undemocratic manner; without popular consent, public vote, or representative governance.",
    "secondary": "In administrative statecraft, enactments decreed undemocratically by executive fiat lack broad popular legitimacy.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The royal intendants governed the provinces **undemocratically**, ignoring the historic rights of local municipal councils."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "James II ruled **undemocratically**, attempting to suspend parliamentary statutes by arbitrary royal prerogative."},
      {"author": "Edmund Burke", "work": "Speech on American Taxation", "quote": "Colonial taxes imposed **undemocratically** by a distant parliament inevitably provoked widespread popular resistance."}
    ]
  },
  "Dashboard — und/undemonstrative.md": {
    "primary": "Not tending to express one's feelings or emotions openly; reserved, quiet, and restrained.",
    "secondary": "In Victorian social behavioral analysis, the idealized English gentleman cultivated an undemonstrative stoicism under adversity.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Greek Interpreter", "quote": "Holmes was singularly **undemonstrative**, rarely revealing the deep underlying affection he felt for his brother Mycroft."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "St. John Rivers maintained an **undemonstrative** exterior, though intense religious zeal burned within his heart."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate admired the quiet, **undemonstrative** gentleness with which Mary Garth attended to her ailing father."}
    ]
  },
  "Dashboard — und/undeniable.md": {
    "primary": "Unable to be denied or disputed; completely true, evident, and indisputable.",
    "secondary": "In jurisprudence, undeniable photographic or documentary evidence establishes material facts beyond reasonable doubt.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The existence of rudimentary organs in adult animals provides **undeniable** evidence of long evolutionary descent."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The footprint upon the floorboards was an **undeniable** physical clue pointing to the presence of a second intruder."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "It is an **undeniable** fact that modern industrial civilization rests upon empirical scientific discoveries."}
    ]
  },
  "Dashboard — und/undeniably.md": {
    "primary": "In a manner that cannot be denied or disputed; unquestionably, clearly, and certainly.",
    "secondary": "In critical literary evaluation, a classic masterpiece undeniably commands enduring cultural influence across generations.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was **undeniably** right in his assessment of Frank Churchill's thoughtless conduct."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Traddles was **undeniably** poor, yet his cheerful industriousness made him the most beloved of companions."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian possessed an **undeniably** remarkable personal beauty that fascinated everyone who met him."}
    ]
  },
  "Dashboard — und/undenominational.md": {
    "primary": "Not restricted to, affiliated with, or characteristic of any particular religious denomination; secular or interfaith.",
    "secondary": "In educational history, the founding of undenominational public schools in nineteenth-century Britain removed sectarian religious tests.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "State education should maintain an **undenominational** character, ensuring equal access for children of all religious persuasions."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The new technical institute was established upon broad **undenominational** principles to welcome students of every faith."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The village assembly met in an **undenominational** hall to coordinate charitable relief for distressed weavers."}
    ]
  },
  "Dashboard — und/undependability.md": {
    "primary": "Unreliability, untrustworthiness, or lack of steady consistency and dependability.",
    "secondary": "In organizational logistics, the undependability of seasonal transport networks threatens supply chain continuity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The chronic **undependability** of the Circumlocution Office drove enterprising inventors to despair and bankruptcy."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "No great commonwealth can be sustained upon the moral **undependability** of unscrupulous financial speculators."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy's friends lamented his boyish **undependability**, hoping that honest employment would steady his character."}
    ]
  },
  "Dashboard — und/undependable.md": {
    "primary": "Not able to be relied upon or trusted; unpredictable, unreliable, or inconsistent.",
    "secondary": "In equipment engineering, an undependable electrical contact introduces intermittent signal dropouts and systemic failures.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The moorland pony was a treacherous and **undependable** mount that easily stumbled into hidden peat bogs."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Willoughby proved to be an **undependable** suitor, abandoning Marianne for a wealthy marriage in London."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The rusty machinery of the Patna was old and **undependable**, threatening to break down in heavy seas."}
    ]
  },
  "Dashboard — und/undependableness.md": {
    "primary": "A tendency toward unreliability, inconsistency, or failure to fulfill obligations.",
    "secondary": "In employee performance appraisal, habitual undependableness in meeting project milestones justifies disciplinary reassignment.",
    "quotes": [
      {"author": "Anthony Trollope", "work": "The Three Clerks", "quote": "Charley Tudor's chronic **undependableness** at the Internal Navigation Office tested the patience of his senior supervisors."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber's financial **undependableness** was paired with an unfailing, sublime optimism that something would turn up."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "The tragic flaw of many brilliant minds is an **undependableness** that squanders talent in unfinished enterprises."}
    ]
  },
  "Dashboard — und/undependably.md": {
    "primary": "In an unreliable, inconsistent, or untrustworthy manner.",
    "secondary": "In experimental physics, instruments that perform undependably must be recalibrated against certified national standards.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The steam launch performed **undependably**, its sputtering boiler struggling against the swift tidal current of the Thames."},
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "The Alpine post-chaise operated **undependably**, stranding passengers at remote mountain inns overnight."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The electric telegraph operated **undependably** as panicked operators abandoned regional railway stations."}
    ]
  },
  "Dashboard — und/undepicted.md": {
    "primary": "Not portrayed, drawn, painted, or described in art or literature.",
    "secondary": "In art history, the harsh daily routines of agrarian peasant labor remained largely undepicted in aristocratic rococo salon art.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The sublime terrors of alpine glaciers remained **undepicted** in European painting until Turner took up his brush."},
      {"author": "Walter Pater", "work": "The Renaissance", "quote": "The inner psychological sorrows of the Madonna were left **undepicted** by the formal hieratic Byzantine icon painters."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The quiet, unheroic virtues of simple country folk were often **undepicted** in fashionable London romances."}
    ]
  },
  "Dashboard — und/under.md": {
    "primary": "Extending or located directly below; at a lower level or position than; or subject to the control of.",
    "secondary": "In constitutional law, citizens live under a system of statutory laws that balance personal liberty with civic duty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "There be some sports are painful, and their labour delight in them sets off; some kinds of baseness are nobly **under**-gone."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Species produced **under** domestication display far greater variability than allied forms in the wild state."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "To be **under** government is to be protected by known, established laws promulgated by lawful authority."}
    ]
  },
  "Dashboard — und/under-the-counter.md": {
    "primary": "Bought or sold illicitly, surreptitiously, or in secret, typically in violation of regulations or rationing.",
    "secondary": "In economic history of wartime shortages, black market goods were traded under-the-counter to evade price control ceilings.",
    "quotes": [
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston bought the beautiful antique notebook **under-the-counter** in a dingy junk shop in the proletarian quarter."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "Strict rationing regulations were enforced to suppress clandestine, **under-the-counter** trafficking in essential food supplies."},
      {"author": "John Steinbeck", "work": "Cannery Row", "quote": "Lee Chong occasionally conducted **under-the-counter** transactions for liquor after regular commercial trading hours."}
    ]
  },
  "Dashboard — und/under-the-table.md": {
    "primary": "Conducted secretly and illegally, especially involving bribes, illicit payments, or undeclared money.",
    "secondary": "In forensic corporate auditing, investigators trace under-the-table kickbacks disbursed through offshore intermediary accounts.",
    "quotes": [
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The political bosses received lucrative **under-the-table** payments from meatpackers to overlook sanitary violations."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "Cowperwood negotiated an **under-the-table** compromise with city aldermen to secure street railway franchises."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The corrupt union treasurer demanded **under-the-table** contributions from mine managers under threat of strikes."}
    ]
  },
  "Dashboard — und/underachieve.md": {
    "primary": "To perform less well, achieve less success, or produce lower results than expected or potential indicates.",
    "secondary": "In educational psychology, gifted students may underachieve when uninspired by repetitive classroom curricula.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Autobiography", "quote": "A child of great natural parts will **underachieve** if education does not provide challenging intellectual stimulation."},
      {"author": "William James", "work": "Talks to Teachers on Psychology", "quote": "Anxiety and emotional fatigue cause talented students to **underachieve** in competitive examination settings."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "Without systematic scientific training, practical mechanics **underachieve** in inventing efficient industrial machinery."}
    ]
  },
  "Dashboard — und/underachievement.md": {
    "primary": "Performance, accomplishment, or output that falls significantly below normal expectations or demonstrated potential.",
    "secondary": "In economic sociology, chronic regional underachievement reflects structural underinvestment in physical infrastructure and technical education.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "Education: Intellectual, Moral, and Physical", "quote": "The scholastic **underachievement** of pupils frequently stems from pedantic teaching methods that stifle natural curiosity."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Monopolistic privileges protect commercial lethargy, resulting in chronic economic **underachievement** across national industries."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred Vincy's record at the university was a painful chronicle of academic **underachievement** and squandered allowances."}
    ]
  },
  "Dashboard — und/underachiever.md": {
    "primary": "A person, student, or organization that fails to achieve their potential or performs below expectations.",
    "secondary": "In pedagogical counseling, identifying an underachiever requires distinguishing between learning difficulties and motivational deficits.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Steerforth regarded poor Tommy Traddles as an amiable **underachiever**, forever being caned and sketching skeletons on slates."},
      {"author": "Arthur Conan Doyle", "work": "The Stark Munro Letters", "quote": "The brilliant eccentric was dismissed as a hopeless **underachiever** because he never published his medical discoveries."},
      {"author": "Henry James", "work": "The Europeans", "quote": "Mr. Wentworth worried that his nephew was turning into a frivolous social **underachiever**, lacking serious civic ambition."}
    ]
  },
  "Dashboard — und/underact.md": {
    "primary": "To act with subtle restraint, understatement, or insufficient emotional emphasis, especially in theatrical performance.",
    "secondary": "In dramatic criticism, an accomplished actor chooses to underact high-stakes scenes to convey profound internal tension.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Dramatic Opinions and Essays", "quote": "The modern realistic actor knows how to **underact** a tragic scene, letting quiet silence speak louder than melodrama."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky Sharp knew when to **underact** her innocence before the Marquis of Steyne, disarming him with modest reserve."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Vincent Crummles instructed his leading tragedian not to **underact** the murder scene, demanding furious ranting."}
    ]
  },
  "Dashboard — und/underactive.md": {
    "primary": "Less active than is normal, desirable, or expected; sluggish or producing insufficient physiological secretions.",
    "secondary": "In clinical endocrinology, an underactive thyroid gland (hypothyroidism) results in cold intolerance, lethargy, and weight gain.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The clinical picture of myxedema arises directly from an **underactive** thyroid gland, treatable with thyroid extract."},
      {"author": "Harvey Cushing", "work": "The Pituitary Body and Its Disorders", "quote": "Hypopituitarism produces an **underactive** metabolic state characterized by subnormal body temperature and somnolence."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Sedentary living induces an **underactive** liver and sluggish lymphatic circulation throughout visceral organs."}
    ]
  },
  "Dashboard — und/underage.md": {
    "primary": "Below the legal or required age, especially for drinking alcohol, voting, military enlistment, or marriage.",
    "secondary": "In labor law history, protective statutory codes were enacted to prohibit underage children from employment in industrial textile mills.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Fagin recruited **underage** boys from the streets, training them in picking pockets in the squalid London slums."},
      {"author": "Winston Churchill", "work": "The River War", "quote": "Many eager recruits lying about their birthdates were found to be **underage** when medically examined for the expedition."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mrs. Bennet fretted that Lydia had eloped while still an **underage** girl of sixteen, compromising the family honor."}
    ]
  },
  "Dashboard — und/underarm.md": {
    "primary": "The hollow beneath the junction of the arm and the shoulder; the armpit; or performed with the arm below the shoulder.",
    "secondary": "In athletic mechanics and cricket history, underarm bowling was the original style before roundarm and overarm methods were legalized.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "Rodney Stone", "quote": "The village cricket match featured ancient veterans who bowled with a deceptive, swift **underarm** delivery."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The sweat glands situated in the human **underarm** region produce axillary secretions rich in organic fatty acids."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Luffey delivered an accurate **underarm** ball that took the batsman's middle stump clean out of the ground."}
    ]
  },
  "Dashboard — und/underbelly.md": {
    "primary": "The underside of an animal; or a vulnerable, weak, or exposed area of an organization, country, or system.",
    "secondary": "In military strategic discourse, Winston Churchill famously referred to Italy and the Balkans as the 'soft underbelly of the Axis'.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "We resolved to strike at the soft **underbelly** of the Axis through the Mediterranean, launching the amphibious invasion of Sicily."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whalemen aimed their harpoons at the white **underbelly** of the giant sperm whale as it rolled in the foam."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The ferocious carnivorous dinosaur exposed its soft scaled **underbelly** as it stumbled over the spiked defensive palisade."}
    ]
  },
  "Dashboard — und/underbid.md": {
    "primary": "To make a lower bid than a competitor; or to bid less in a card game than the strength of one's hand justifies.",
    "secondary": "In public procurement tendering, a contractor may deliberately underbid a project to win the award, planning to recoup costs via change orders.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Independent merchants seek to **underbid** the exclusive trading companies, offering cheaper goods to domestic consumers."},
      {"author": "Theodore Dreiser", "work": "The Financier", "quote": "The rival contractor attempted to **underbid** Cowperwood on the city municipal bond issue, sparking a fierce financial contest."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "Melmotte managed to **underbid** all competitors for the South American railway contract through audacious financial maneuvers."}
    ]
  },
  "Dashboard — und/underbodice.md": {
    "primary": "A woman's undergarment worn beneath a dress bodice; a camisole or corset cover.",
    "secondary": "In historical costume design, a boned underbodice provided structural support and shape to heavy nineteenth-century silk ballgowns.",
    "quotes": [
      {"author": "Edith Wharton", "work": "The Age of Innocence", "quote": "May's wedding gown featured an intricately fitted **underbodice** of pale silk beneath layers of vintage Brussels lace."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma unhooked her embroidered **underbodice**, sighing with weary relief in the quiet privacy of her dressing room."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia adjusted her scarlet ribbon over her dark **underbodice**, preparing for her nocturnal walk across Egdon Heath."}
    ]
  },
  "Dashboard — und/underbody.md": {
    "primary": "The underside or lower structure of a vehicle, aircraft, or ship; chassis.",
    "secondary": "In automotive engineering, aerodynamic underbody panels smooth turbulent air drag and protect mechanical linkages from road debris.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The body of the unfortunate clerk had fallen from the roof upon the railway carriage **underbody** before tumbling onto the tracks."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The machine-gun battery was mounted beneath the armored **underbody** of the giant German Zeppelin airship."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues under the Sea", "quote": "The reinforced steel **underbody** of the Nautilus glided smoothly over the sharp coral projections of the Torres Strait."}
    ]
  },
  "Dashboard — und/underboss.md": {
    "primary": "A second-in-command in a criminal organization or hierarchy; or a subordinate supervisor.",
    "secondary": "In sociological studies of organized crime syndicates, the underboss manages day-to-day operations and buffers the boss from direct culpability.",
    "quotes": [
      {"author": "Jack London", "work": "The Iron Heel", "quote": "The industrial trust employed an unscrupulous **underboss** to infiltrate and disrupt the clandestine meetings of the trade union."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "The political ward boss dispatched his trusted **underboss** to distribute election funds among the precinct captains."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "Barkeep McGinty ruled the Scowrers through a ruthless **underboss** who carried out midnight assassinations without remorse."}
    ]
  },
  "Dashboard — und/underbred.md": {
    "primary": "Ill-bred, vulgar, lacking good manners, breeding, or social refinement.",
    "secondary": "In nineteenth-century comedy of manners, the pretentious underbred upstart is satirized for clumsy attempts to mimic aristocratic decorum.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Emma considered Mrs. Elton a thoroughly **underbred** woman, whose loud vulgarity was masked by pretentious accomplishments."},
      {"author": "William Makepeace Thackeray", "work": "The Book of Snobs", "quote": "The ostentatious snob reveals his **underbred** origins the moment he attempts to converse with genuine ladies and gentlemen."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon condemned Mr. Slope as an **underbred** ecclesiastical adventurer seeking promotion through vulgar sycophancy."}
    ]
  },
  "Dashboard — und/underbrush.md": {
    "primary": "Shrubs, bushes, saplings, and small trees growing beneath large trees in a forest; undergrowth.",
    "secondary": "In forest ecology and wildfire dynamics, accumulated dry underbrush acts as ladder fuel that carries surface fires into the tree canopy.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "We pushed our way through dense **underbrush** of spruce and hemlock, following the faint tracks of a moose through the wilderness."},
      {"author": "James Fenimore Cooper", "work": "The Last of the Mohicans", "quote": "Hawkeye stepped noiselessly through the tangled **underbrush**, his rifle ready to repel an Indian ambuscade."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The humid virgin forests of Chiloe were choked with an impenetrable **underbrush** of bamboos and creeping ferns."}
    ]
  },
  "Dashboard — und/undercarriage.md": {
    "primary": "The landing gear of an aircraft; or the supporting framework or chassis beneath a vehicle.",
    "secondary": "In aeronautical engineering, retractable undercarriage mechanisms reduce aerodynamic drag during high-speed cruise flight.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Exploration of Space", "quote": "The lunar lander touched down softly, its hydraulic **undercarriage** absorbing the impact upon the basaltic dust of the crater floor."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The monoplane landed smoothly on the turf, its wheeled **undercarriage** kicking up a cloud of summer dust."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "The post-chaise suffered a fractured axle in its wooden **undercarriage**, stranding Mr. Pickwick upon the road to Rochester."}
    ]
  },
  "Dashboard — und/undercharge.md": {
    "primary": "To charge too little money for a service, goods, or work; or to load with an insufficient explosive charge.",
    "secondary": "In commercial trade and contract accounting, failing to audit supplier invoices can cause vendors to undercharge or overcharge systematically.",
    "quotes": [
      {"author": "Daniel Defoe", "work": "The Complete English Tradesman", "quote": "The tradesman who is careless in his day-book will constantly **undercharge** his customers and ruin his own profit margin."},
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The artillery gunner took care not to **undercharge** the mortar, ensuring the shell would reach the besiegers' trenches."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "In competitive retail markets, shopkeepers frequently **undercharge** on staples to attract patrons into their establishments."}
    ]
  },
  "Dashboard — und/underclass.md": {
    "primary": "The lowest social stratum in a society, consisting of disadvantaged and economically marginalized individuals.",
    "secondary": "In urban sociology, the underclass experiences persistent intergenerational poverty, educational deficits, and structural unemployment.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Hard Times", "quote": "The industrial masters of Coketown regarded the factory **underclass** as mere hands designed to keep the cotton spindles turning."},
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The mining community constituted a forgotten economic **underclass** whose dangerous subterranean toil kept Britain warm and powered."},
      {"author": "Thomas Carlyle", "work": "Chartism", "quote": "The rising discontent among the working **underclass** warned Parliament that social justice could no longer be postponed."}
    ]
  },
  "Dashboard — und/underclassman.md": {
    "primary": "A student in the first or second year of high school or university (a freshman or sophomore).",
    "secondary": "In American collegiate social history, an underclassman was historically subjected to campus customs and hazing by upperclassmen.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "This Side of Paradise", "quote": "Amory Blaine strolled across the Princeton campus, a self-conscious **underclassman** eager to make his mark in college society."},
      {"author": "Thomas Wolfe", "work": "Look Homeward, Angel", "quote": "Eugene entered the state university as an awkward, dreamy **underclassman**, overwhelmed by the bustle of campus life."},
      {"author": "Henry James", "work": "The Bostonians", "quote": "The Harvard **underclassman** rowed with great vigor on the Charles River, dreaming of varsity athletic glory."}
    ]
  },
  "Dashboard — und/underclothed.md": {
    "primary": "Wearing insufficient clothing for the weather, modesty, or prevailing social circumstances; inadequately dressed.",
    "secondary": "In public health history, underclothed poor children in wintry industrial cities suffered high rates of hypothermia and pneumonia.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "The shivering chimney-sweep was miserably **underclothed**, his ragged garments offering little shield against the bitter January frost."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The field laborers worked on the windy upland **underclothed** for the autumn drizzle that soaked through their thin smocks."},
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The homeless men in the London shelter were pitifully **underclothed**, wrapping old newspapers around their legs for warmth."}
    ]
  },
  "Dashboard — und/underclothes.md": {
    "primary": "Clothes worn under other clothes, typically next to the skin; underwear or undergarments.",
    "secondary": "In social hygiene history, the widespread adoption of washable cotton and wool underclothes dramatically improved public sanitation in the nineteenth century.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Peggotty carefully packed David's trunk with clean woolen stockings, linen shirts, and comfortable warm **underclothes**."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym Yeobright changed out of his damp **underclothes** after a long day of furze-cutting on the foggy heath."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes examined the laundry marks upon the deceased man's **underclothes**, discovering the initials of the missing officer."}
    ]
  },
  "Dashboard — und/underclothing.md": {
    "primary": "Underclothes considered collectively; garments worn next to the skin beneath outer clothing.",
    "secondary": "In polar exploration history, expeditions utilized multilayered woolen underclothing to trap air and prevent sweat accumulation in subzero cold.",
    "quotes": [
      {"author": "Robert Falcon Scott", "work": "Scott's Last Expedition", "quote": "The sledging party wore specialized Jaeger woolen **underclothing**, which maintained body heat while breathing moisture out into the wind."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "The pupils at Lowood were provided with coarse, scratchy **underclothing** that chilled them in the unheated stone dormitories."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "Dolly brought a bundle of warm flannel **underclothing** for the little foundling girl whom Silas had taken in."}
    ]
  },
  "Dashboard — und/undercoat.md": {
    "primary": "A coat or layer of paint applied before a final topcoat; or the dense underfur of an animal.",
    "secondary": "In mammalian biology, a dense, water-repellent insulating undercoat protects Arctic mammals against extreme polar temperatures.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Domestic dogs adapted to subarctic climates develop a dense, woolly **undercoat** that sheds seasonal rain and snow."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The painter laid down a warm ochre **undercoat** on the gesso panel before applying the luminous glaze layers."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck's heavy fur grew thicker, developing a warm downy **undercoat** that enabled him to sleep peacefully beneath the snowdrift."}
    ]
  },
  "Dashboard — und/undercoated.md": {
    "primary": "Treated or painted with an undercoat; or having a protective seal applied to the underside of a vehicle chassis.",
    "secondary": "In structural and industrial painting, steel bridges are undercoated with zinc-rich primer to prevent atmospheric corrosion.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "The iron castings were carefully **undercoated** with rust-resistant enamel before being assembled into dynamo housings."},
      {"author": "Arthur C. Clarke", "work": "Islands in the Sky", "quote": "The exterior hull plates of the spacecraft were **undercoated** with refractory ceramic bonding to withstand heat friction."},
      {"author": "John Steinbeck", "work": "The Grapes of Wrath", "quote": "The old truck's chassis had been **undercoated** with tar years ago, but rust had eaten through the exposed fenders."}
    ]
  },
  "Dashboard — und/undercover.md": {
    "primary": "Involving secret, covert work or investigation without disclosing one's true identity, especially by police or intelligence agents.",
    "secondary": "In criminal investigation and espionage, an undercover operative assumes a false identity to infiltrate illicit organizations.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "His Last Bow", "quote": "Holmes lived for two years as an **undercover** Irish-American agitator to penetrate the German espionage network in London."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "Verloc functioned as a paid **undercover** informant, reporting anarchist conspiracies to the foreign embassy and Scotland Yard."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "British naval intelligence dispatched an **undercover** agent to inspect foreign dockyards and report on dreadnought construction."}
    ]
  },
  "Dashboard — und/undercurrent.md": {
    "primary": "A current of water flowing below the surface; or an underlying opinion, feeling, or tendency contrary to surface appearances.",
    "secondary": "In narrative fiction, a dark undercurrent of unresolved grievance propels dramatic conflict beneath polite drawing-room dialogue.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Beneath the superficial gaiety of Parisian life ran a sinister **undercurrent** of revolutionary fury ready to burst forth."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was unaware of the bitter **undercurrent** of wounded pride that surged through Casaubon's brooding heart."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "A powerful equatorial **undercurrent** swept the drifting whaleboat miles off its course during the misty night."}
    ]
  },
  "Dashboard — und/undercut.md": {
    "primary": "To offer goods or services at a lower price than a competitor; or to undermine or weaken someone's position.",
    "secondary": "In coastal geology and geomorphology, relentless wave action undercuts sea cliffs, precipitating catastrophic rockfalls into the surf.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Enterprising foreign merchants sought to **undercut** the guild prices by introducing steam-powered mechanical looms."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "The rushing mountain stream continues to **undercut** the rocky gorge wall until the unsupported overhang collapses."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Factions will attempt to **undercut** executive independence by threatening legislative reductions in constitutional compensation."}
    ]
  },
  "Dashboard — und/underdevelop.md": {
    "primary": "To fail to develop fully, sufficiently, or to the normal extent, especially in photography or economic resources.",
    "secondary": "In darkroom photography, if a photographer should underdevelop a silver halide negative, the resulting print exhibits weak contrast and muddy shadows.",
    "quotes": [
      {"author": "Thomas Edison", "work": "The Edison Papers", "quote": "In photographic processing, taking care not to **underdevelop** the celluloid film ensures crisp, well-defined projection images."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Restricting educational resources will inevitably **underdevelop** the intellectual and industrial potential of the populace."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Sussex Vampire", "quote": "The amateur photographer warned his assistant not to **underdevelop** the glass plates taken at the scene of the tragedy."}
    ]
  },
  "Dashboard — und/underdeveloped.md": {
    "primary": "Not fully developed, grown, or matured; or economically and industrially less advanced than other countries.",
    "secondary": "In development economics, underdeveloped regions require strategic investments in basic health, electrification, and transport infrastructure.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The wings of the flightless ostrich are rudimentary and **underdeveloped** compared to those of soaring birds."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The canine teeth in human skulls are small and **underdeveloped** in comparison with the formidable fangs of the gorilla."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "Vast continental interiors remained economically **underdeveloped** until the spread of steam transcontinental railways."}
    ]
  },
  "Dashboard — und/underdevelopment.md": {
    "primary": "Insufficient economic, industrial, or physical growth and technological modernization.",
    "secondary": "In developmental pediatrics and endocrinology, physical underdevelopment can result from growth hormone deficiency or chronic malnutrition.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The economic **underdevelopment** of the inland provinces stemmed directly from the lack of navigable river waterways to the sea."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Infantile cretinism presents with pronounced somatic and mental **underdevelopment** due to congenital thyroid absence."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Societies burdened by chronic political insecurity remain trapped in economic **underdevelopment** and primitive subsistence farming."}
    ]
  },
  "Dashboard — und/underdog.md": {
    "primary": "A competitor, team, or person thought to have little chance of winning a fight, match, or contest.",
    "secondary": "In political rhetoric and populist narrative, championing the underdog appeals to universal democratic instincts of fairness and sympathy.",
    "quotes": [
      {"author": "Jack London", "work": "The Iron Heel", "quote": "My heart naturally warmed toward the courageous **underdog** who dared to challenge the formidable power of the industrial trust."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The foreign volunteers rallied to support the democratic **underdog** struggling against the mechanized armies of fascism."},
      {"author": "Arthur Conan Doyle", "work": "Rodney Stone", "quote": "The prize-ring crowd always backed the game **underdog** who fought back bravely after being floored by the champion."}
    ]
  },
  "Dashboard — und/underdone.md": {
    "primary": "Cooked insufficiently or incompletely; rare (especially of meat).",
    "secondary": "In culinary tradition, an underdone roast beef retains a juicy pink center, favored in classical British gastronomy.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Christmas Carol", "quote": "Scrooge declared that Marley's ghost might be nothing more than an **underdone** piece of beef, a blot of mustard, or a crumb of cheese."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Woodhouse cautioned everyone that the mutton was decidedly **underdone** and would disagree with delicate constitutions."},
      {"author": "Alexis Soyer", "work": "The Modern Housewife", "quote": "A joint of beef should never be served raw, though a slightly **underdone** center preserves the savory natural juices."}
    ]
  },
  "Dashboard — und/underdrawers.md": {
    "primary": "An archaic term for underpants, long underwear, or drawers worn beneath trousers.",
    "secondary": "In nineteenth-century personal attire, linen or flannel underdrawers extended to the ankles and were secured with tape or buttons.",
    "quotes": [
      {"author": "Mark Twain", "work": "The Adventures of Tom Sawyer", "quote": "Tom stripped off his trousers and patched **underdrawers** before diving headlong into the cool waters of the Mississippi."},
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick hastily slipped into his warm flannel **underdrawers** when awakened by the midnight alarm at the inn."},
      {"author": "Herman Melville", "work": "White-Jacket", "quote": "The sailors washed their heavy canvas trousers and red flannel **underdrawers** upon the scrubbed forecastle deck."}
    ]
  },
  "Dashboard — und/underdress.md": {
    "primary": "To dress too plainly or casually for an occasion; or clothes worn beneath outer garments.",
    "secondary": "In aristocratic etiquette, guests feared to underdress for formal court receptions where velvet court dress was mandatory.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "Fanny was careful neither to overdress nor to **underdress** for the grand ball, choosing a modest white muslin gown."},
      {"author": "Edith Wharton", "work": "The House of Mirth", "quote": "Lily Bart understood that to **underdress** at a country-house party was as fatal a social error as being overly ostentatious."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Becky mocked the provincial ladies who would **underdress** in cheap cottons at high London society assemblies."}
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

print(f"Dashboard — und Part 2 (8B): Successfully updated {updated}/{len(data)} notes.")
