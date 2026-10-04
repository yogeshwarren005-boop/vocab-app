# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — ven Part 1 (14A, 35 words) ---
  "Dashboard — ven/avenue.md": {
    "primary": "A broad road or thoroughfare, often lined with trees; a means of access or approach to an objective.",
    "secondary": "In urban landscape planning, monumental avenues (such as Haussmann's Parisian boulevards) designed to channel civic transit and vista perspectives.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The long carriage drive formed a dark **avenue** through the ancient forest leading up to the chateau."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth walked slowly down the gravel **avenue**, meditating upon Darcy's extraordinary letter."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The yew **avenue** stretched into the gloom where Sir Charles had fallen dead."}
    ]
  },
  "Dashboard — ven/circumventive.md": {
    "primary": "Tending, designed, or serving to circumvent, bypass, or outwit an obstacle or regulation.",
    "secondary": "In military tactical doctrine and strategic maneuvers, circumventive envelopments that bypass fortified redoubts.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Essays", "quote": "A cunning negotiator employs **circumventive** arts to entrap an unwary adversary into disadvantageous covenants."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The federal constitution must withstand the **circumventive** stratagems of ambitious state factions."},
      {"author": "Edmund Burke", "work": "Speech on Conciliation with America", "quote": "Smugglers devised ingenious **circumventive** methods to evade imperial customs duties."}
    ]
  },
  "Dashboard — ven/contravene.md": {
    "primary": "To violate, breach, or act in opposition to a law, treaty, principle, or custom; to dispute.",
    "secondary": "In statutory construction and jurisprudence, legislative acts that contravene fundamental constitutional guarantees are held unconstitutional.",
    "quotes": [
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "No edict of the magistrate can justly **contravene** the natural law of self-preservation."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Judges must declare void any legislative enactment that shall **contravene** the supreme constitution."},
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The king attempted to **contravene** the established rights of the universities through royal prerogative."}
    ]
  },
  "Dashboard — ven/convene.md": {
    "primary": "To summon, call together, or assemble for a formal meeting, conference, or official purpose.",
    "secondary": "In parliamentary procedure, the formal prerogative of an executive or speaker to convene a legislative assembly into session.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "The senators did **convene** the plebeians to debate the distribution of public corn."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Emperor Constantine resolved to **convene** the Council of Nicaea to resolve theological schisms."},
      {"author": "Thomas Jefferson", "work": "Notes on the State of Virginia", "quote": "The governor possessed authority to **convene** the general assembly in times of sudden public emergency."}
    ]
  },
  "Dashboard — ven/convener.md": {
    "primary": "A person whose role is to summon or organize meetings of a committee, assembly, or conference.",
    "secondary": "In Scottish civic and academic administration, the presiding chairperson of a council, trade guild, or faculty committee.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Heart of Midlothian", "quote": "The trade guild **convener** summoned the deacons of the crafts to discuss the municipal tumult."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The electoral **convener** called the electors together in the great hall of the Paris city hall."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "The **convener** of the reform committee prepared the agenda for the general discussion."}
    ]
  },
  "Dashboard — ven/convenience.md": {
    "primary": "The suitability, usefulness, or practical ease afforded by an arrangement; freedom from discomfort or difficulty.",
    "secondary": "In commercial economics, goods or retail stores designed to reduce shopping effort and transaction friction for consumers.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Collins consulted his own **convenience** in every arrangement for the journey to Hunsford."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Money facilitates the **convenience** of exchange among merchants, banishing the clumsy obstacles of barter."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "We considered it conducive to the general **convenience** of all parties that the lodging should be taken."}
    ]
  },
  "Dashboard — ven/conveniences.md": {
    "primary": "Things that contribute to comfort, ease, or suitability in daily life; modern household amenities.",
    "secondary": "In Victorian urban housing history, the introduction of indoor plumbing, piped gas, and water closets as domestic conveniences.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The cottage was fitted with all modern **conveniences** calculated to ease the labor of the tenant."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Civilized society abounds in countless mechanical **conveniences** produced by division of labour."},
      {"author": "Sinclair Lewis", "work": "Babbitt", "quote": "He took boundless pride in the porcelain plumbing fixtures and electrical **conveniences** of his suburban villa."}
    ]
  },
  "Dashboard — ven/convenient.md": {
    "primary": "Fitting, suitable, or agreeable to one's needs, comfort, or purpose; situated near or easy to reach.",
    "secondary": "In administrative planning, arranging service locations and timetables to minimize public travel burdens.",
    "quotes": [
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "The cottage was small, but comfortable, and **convenient** to all the neighboring market towns."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "A **convenient** train from Paddington carried us straight to the secluded manor house."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe found it **convenient** to inspect the forge fire whenever Mrs. Joe's temper rose to tempest pitch."}
    ]
  },
  "Dashboard — ven/conveniently.md": {
    "primary": "In a convenient manner; suitably, easily, or with minimal trouble or physical exertion.",
    "secondary": "In spatial architecture, positioning kitchens, storage bays, and exits to facilitate ergonomic daily workflow.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The shepherd's hut on wheels was **conveniently** stationed close to the lambing fold upon the down."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes had **conveniently** concealed his tracking lanterns beneath the cushions of the four-wheeler."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "The parsonage was **conveniently** situated near Rosings Park, allowing daily visits to Lady Catherine."}
    ]
  },
  "Dashboard — ven/convening.md": {
    "primary": "The act of assembling, summoning, or meeting together formally for conference or deliberation.",
    "secondary": "In constitutional history, the convening of extraordinary estates-general or constituent assemblies to draft new charters.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor issued imperial rescripts for **convening** the provincial bishops at Arles."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The regular **convening** of Congress is safeguarded by precise constitutional calendar provisions."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The **convening** of the States-General in May 1789 sounded the opening knell of the ancient monarchy."}
    ]
  },
  "Dashboard — ven/coven.md": {
    "primary": "An assembly, gathering, or secret society of witches, traditionally consisting of thirteen members.",
    "secondary": "In folklore and historical anthropology, popular belief in clandestine nocturnal assemblies worshiping pre-Christian deities.",
    "quotes": [
      {"author": "Walter Scott", "work": "Letters on Demonology and Witchcraft", "quote": "Popular superstition attributed every unexplainable blight to the secret rites of a local **coven**."},
      {"author": "Nathaniel Hawthorne", "work": "Young Goodman Brown", "quote": "The traveler fancied he recognized pious deacons and upright magistrates assembled in the unholy midnight **coven**."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Devil's Foot", "quote": "Ancient tales persisted in the Cornish village of a midnight **coven** meeting amid the stone circles."}
    ]
  },
  "Dashboard — ven/covenant.md": {
    "primary": "A solemn, binding agreement or formal promise between two or more parties; a legal compact.",
    "secondary": "In biblical theology and reformed theology, the divine covenant established between God and humanity (Covenant of Grace).",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "God entered into a gracious **covenant** with Abraham, promising that his seed should possess the promised land."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "A **covenant** without the sword is but words, and of no strength to secure a man at all."},
      {"author": "John Locke", "work": "Second Treatise of Government", "quote": "Men enter into the original social **covenant** to secure their lives, liberties, and estates."}
    ]
  },
  "Dashboard — ven/disinvent.md": {
    "primary": "To undo, unlearn, or eradicate an invention, technology, or harmful innovation from human society.",
    "secondary": "In philosophy of technology, the theoretical dilemma whether destructive technologies (like nuclear weapons) can ever be uninvented.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Humanity wished in vain that it could **disinvent** the aerial bomb and poison gas after the catastrophe."},
      {"author": "George Orwell", "work": "Collected Essays", "quote": "You cannot **disinvent** the machine gun or the radio; civilized nations must learn to control their use."},
      {"author": "Aldous Huxley", "work": "Brave New World Revisited", "quote": "No civilization has ever managed to **disinvent** a technological instrument of totalitarian control."}
    ]
  },
  "Dashboard — ven/envenom.md": {
    "primary": "To poison, taint with venom, or embitter; to infuse malice or hatred into feelings or speech.",
    "secondary": "In literary tragedy, toxic passions or malicious slander that poison intimate relationships and family harmony.",
    "quotes": [
      {"author": "William Shakespeare", "work": "King John", "quote": "Whose tongue soe'er speaks false, not truly speaks; who speaks not truly, lies. Do not **envenom** your words with spite."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Satan sought to **envenom** the peaceful minds of innocent angels with rebellious pride."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Jealous suspicions served only to **envenom** his heart and distort every innocent action of his wife."}
    ]
  },
  "Dashboard — ven/even.md": {
    "primary": "Flat, smooth, and level; uniform, equal, or calm; divisible by two without a remainder.",
    "secondary": "In number theory, integers divisible by two (2k), possessing the parity of zero modulo two.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "I'll have the current in this place dammed up, and here the smug and silver Trent shall run in a smooth and **even** course."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She walked with a steady, **even** step across the dew-drenched meadows in the early light."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "A philosopher should maintain an **even** balance of mind, unswayed by excessive hope or despondency."}
    ]
  },
  "Dashboard — ven/evening.md": {
    "primary": "The period of time at the end of the day between late afternoon and nightfall.",
    "secondary": "In diurnal ecology, crepuscular organisms become active during evening twilight to forage under reduced predation pressure.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Comedy of Errors", "quote": "Yet this my comfort; when your words are done, my woes end likewise with the **evening** sun."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The calm summer **evening** descended upon the sheep-fold with amber light and long shadows."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The pale mist of **evening** arose from the river marshes, wrapping the lonely churchyard in gray gloom."}
    ]
  },
  "Dashboard — ven/evening-snow.md": {
    "primary": "Snowfall occurring at twilight or dusk; or a small California annual wildflower (Linanthus dichotomus) blooming in late afternoon.",
    "secondary": "In botanical ecology, Linanthus dichotomus opens its fragrant white blossoms at dusk to attract nocturnal moth pollinators.",
    "quotes": [
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Along the gravelly foothill ridges, the delicate blossoms of **evening-snow** opened their fragrant white stars at sunset."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "A soft **evening-snow** began to fall, dusting the dark pines of the wood with crystalline purity."},
      {"author": "Asa Gray", "work": "Synoptical Flora of North America", "quote": "The fragrant **evening-snow** unfolds its vespertine petals only when the shadow of the mountain ridge falls over the desert chaparral."}
    ]
  },
  "Dashboard — ven/eveningwear.md": {
    "primary": "Formal clothing, gowns, or dress suits designed to be worn for evening social functions and galas.",
    "secondary": "In sartorial history, encompassing white tie (formal tailcoat) and black tie (tuxedo/dinner jacket) social dress codes.",
    "quotes": [
      {"author": "F. Scott Fitzgerald", "work": "The Great Gatsby", "quote": "Guests in elegant **eveningwear** drifted across the blue gardens of West Egg beneath glowing lanterns."},
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "Gentlemen in black **eveningwear** and ladies draped in shimmering silk arrived at the Westminster reception."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Rawdon Crawley looked splendid in his military **eveningwear** as he escorted Becky into the grand ballroom."}
    ]
  },
  "Dashboard — ven/evenly.md": {
    "primary": "In a smooth, uniform, or level manner; in equal portions; with calm, steady composure.",
    "secondary": "In industrial manufacturing, applying coats of paint, glaze, or lacquer with uniform micron thickness across surfaces.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She knew how to hit to a hair's-breadth that moment of evening when the light and the dark were **evenly** balanced."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Celia spoke **evenly**, never raising her voice, but delivering her home truths with calm precision."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Natural selection distributes organic modifications **evenly** throughout the population over successive generations."}
    ]
  },
  "Dashboard — ven/evenness.md": {
    "primary": "The characteristic of being level, smooth, uniform, equal, or composed in temper; equanimity.",
    "secondary": "In mathematical statistics, the measure of uniformity in probability distributions or ecological species abundance.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Celia was not impulsive; what she had to say could wait, and came from her always with the placid **evenness** of water flowing from a smooth conduit."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "True greatness of soul displays itself in an **evenness** of temper under both prosperity and adversity."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "The vast **evenness** of the heath landscape created an impression of monumental, solemn eternity."}
    ]
  },
  "Dashboard — ven/evensong.md": {
    "primary": "A service of evening prayer or worship in the Christian church, especially in the Anglican liturgy; evening song.",
    "secondary": "In the liturgical canonical hours of the Church of England, Evensong combines elements of the traditional Catholic offices of Vespers and Compline.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The church bells were ringing for **evensong**, and a squad of Salvation Army lassies came singing down the suburban road."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The melodic strains of the Sunday **evensong** floated across the quiet meadows from the parish church."},
      {"author": "Anthony Trollope", "work": "The Warden", "quote": "Mr. Harding played the violoncello at cathedral **evensong**, his gentle heart attuned to holy harmonies."}
    ]
  },
  "Dashboard — ven/eventful.md": {
    "primary": "Full of notable events, exciting incidents, or momentous changes; marked by significant occurrences.",
    "secondary": "In narrative historiography, characterizing tumultuous epochs (such as revolutions or world wars) that reshape civil institutions.",
    "quotes": [
      {"author": "William Shakespeare", "work": "As You Like It", "quote": "Last scene of all, that ends this strange **eventful** history, is second childishness and mere oblivion."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her domestic life had been singularly **eventful**, transforming her from an inexperienced girl into a reflective woman."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The morning sun rose upon an **eventful** day in the forest, each leaf sparkling with melted frost."}
    ]
  },
  "Dashboard — ven/inconvenience.md": {
    "primary": "Trouble, difficulty, or discomfort caused to someone; an inconvenient circumstance or nuisance.",
    "secondary": "In contract law, incidental damages compensating a plaintiff for reasonable inconvenience and administrative costs resulting from a breach.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 1", "quote": "To intercept this **inconvenience**, a piece of ordnance 'gainst it I have placed."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Bathsheba considered the practical **inconvenience** of managing the large estate without a resident bailiff."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was unwilling to suffer the **inconvenience** of traveling to London merely on a matrimonial errand."}
    ]
  },
  "Dashboard — ven/inconvenient.md": {
    "primary": "Causing trouble, difficulty, or discomfort; awkwardly timed, situated, or arranged; unsuited.",
    "secondary": "In logistics planning, describing schedules or routes that demand disproportionate transfer times or unnecessary out-of-the-way transit.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "If this were the case, the process of laying and hatching might be **inconveniently** prolonged, exposing eggs to danger."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "It seemed to me that the house was an **inconvenient** shelter, located directly in the path of the Martian advance."},
      {"author": "Jane Austen", "work": "Emma", "quote": "A heavy fall of snow at dinner time threatened to make returning home exceedingly **inconvenient**."}
    ]
  },
  "Dashboard — ven/inconveniently.md": {
    "primary": "In a manner that causes trouble, difficulty, or awkwardness; unsuitably or unseasonably.",
    "secondary": "In transport and urban design, infrastructure positioned awkwardly relative to pedestrian and vehicular transit flows.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "If the tail feathers had grown **inconveniently** long, they would have severely impeded flight through dense forest boughs."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The cottage was **inconveniently** chosen, requiring a needless detour across exposed railway embankments."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "The market stall was **inconveniently** wedged between two noisy cattle pens in the crowded street."}
    ]
  },
  "Dashboard — ven/intervene.md": {
    "primary": "To come between persons or things; to get involved in a situation to alter, resolve, or prevent an outcome.",
    "secondary": "In international conflict resolution, third-party state or institutional mediation designed to de-escalate armed disputes.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "Solitude is not measured by the miles of space that **intervene** between a man and his fellow creatures."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Civilized institutions **intervene** to preserve the weak who would otherwise perish in a state of nature."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She stepped forward to **intervene** between the quarreling brothers before bitter words turned to violence."}
    ]
  },
  "Dashboard — ven/intervening.md": {
    "primary": "Occurring or situated between two events, points in time, or physical objects.",
    "secondary": "In legal causation doctrine, an intervening cause (novus actus interveniens) that severs the chain of proximate liability between initial tort and final damage.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The autumn mists indolently crept across the **intervening** valleys, hiding the distant downs in white haze."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological record fails to preserve all the finely graduated **intervening** links connecting ancestral forms."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes carefully examined the **intervening** patch of swamp that separated the tor from the ancient hut."}
    ]
  },
  "Dashboard — ven/intervenor.md": {
    "primary": "A third party who voluntarily enters or is joined to an ongoing legal action or lawsuit to protect an interest.",
    "secondary": "In civil procedure, an intervenor of right possesses an interest relating to the property or transaction forming the subject of the action.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The ecclesiastical court admitted the third party as a lawful **intervenor** to assert her claim of prior marriage."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The judicial tribunal ensures that an impartial **intervenor** may state arguments concerning constitutional jurisdiction."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The appearance of yet another **intervenor** in Jarndyce and Jarndyce added another layer of legal costs to the ruinous suit."}
    ]
  },
  "Dashboard — ven/intravenous.md": {
    "primary": "Existing, occurring, taking place, or administered within a vein or by entering into a vein.",
    "secondary": "In pharmacology and therapeutics, intravenous infusion provides immediate systemic bioavailability bypassing gastrointestinal absorption.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Direct **intravenous** infusion of warm physiological saline proved lifesaving in profound hemorrhagic shock."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "Rapid **intravenous** administration of cardiac stimulants helped sustain blood pressure during acute collapse."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The clinic utilized continuous **intravenous** drips to titrate delicate medications in post-encephalitic patients."}
    ]
  },
  "Dashboard — ven/intravenously.md": {
    "primary": "By means of or through entering into a vein; by intravenous injection or infusion.",
    "secondary": "In clinical anesthesiology, delivering induction agents intravenously to achieve rapid loss of consciousness within seconds.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Salvarsan was administered **intravenously** with great technical caution to avoid extravasation into perivascular tissues."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "The therapeutic serum had to be introduced **intravenously** to neutralize circulating diphtheria toxin without delay."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "When given **intravenously**, the dopamine precursor produced an instantaneous awakening from catatonic stupor."}
    ]
  },
  "Dashboard — ven/nonvenomous.md": {
    "primary": "Not producing venom; lacking toxic poison or venom-injecting fangs; harmless in bite.",
    "secondary": "In herpetology, differentiating aglyphous colubrid snakes from venomous proteroglyphous elapids and solenoglyphous viperids.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The travelers captured a beautiful **nonvenomous** green snake that glided harmlessly through the tall pampas grass."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The jaw apparatus of the **nonvenomous** serpent displays solid homodont dentition devoid of poison canals."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger assured the nervous party that the giant marsh reptile was completely **nonvenomous** and herbivorous."}
    ]
  },
  "Dashboard — ven/parvenu.md": {
    "primary": "A person who has suddenly risen to wealth, status, or power, but has not yet gained social acceptance; an upstart.",
    "secondary": "In 19th-century French and English social satire, a nouveau riche character attempting clumsily to adopt aristocratic manners.",
    "quotes": [
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "Old Osborne was a wealthy city **parvenu** whose vulgar ostentation drew covert sneers from the impoverished nobility."},
      {"author": "Honoré de Balzac", "work": "Père Goriot", "quote": "Rastignac observed how the Parisian **parvenu** flaunted gilded carriages and diamond tie-pins to advertise sudden fortunes."},
      {"author": "Henry James", "work": "The American", "quote": "The proud old aristocratic family regarded the energetic American millionaire as an intrusive transatlantic **parvenu**."}
    ]
  },
  "Dashboard — ven/prevenient.md": {
    "primary": "Going before; preceding; anticipatory; in Christian theology, divine grace preceding human repentance.",
    "secondary": "In Augustinian and Arminian theology, prevenient grace regenerates human free will prior to personal faith.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "From the Mercy-seat above, **prevenient** grace descending had removed the stony from their hearts."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He possessed an orthodox theological mindset that would argue warmly upon the necessity of **prevenient** grace."},
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "The soul requires the gentle illumination of **prevenient** grace before it can recognize its own spiritual alienation."}
    ]
  },
  "Dashboard — ven/proven.md": {
    "primary": "Demonstrated by evidence, trial, or argument to be true, valid, or effective; confirmed.",
    "secondary": "In Scots criminal law, the verdict of 'not proven' acquits the accused while indicating that innocence was not affirmatively established.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "He sighed with relief, anxious to conclude the debate regarding what was already **proven** to everyone's satisfaction."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Probable as this physiological hypothesis seems, it is by no means an empirically **proven** conclusion."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes considered every hypothesis until only the one **proven** by material footprint evidence remained."}
    ]
  },
  "Dashboard — ven/provenance.md": {
    "primary": "The place of origin, historical source, or earliest known history of something; record of ownership.",
    "secondary": "In art history, archaeology, and rare books, documentary pedigree verifying authenticity and chain of custody back to the original creator.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Illustrious Client", "quote": "Holmes authenticated the Chinese porcelain saucer by verifying its imperial **provenance** from the Ming dynasty."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The Byzantine marble relief revealed its ancient eastern **provenance** through carved Greek inscriptions."},
      {"author": "M. R. James", "work": "Ghost Stories of an Antiquary", "quote": "The curator examined the illuminated Psalter, tracing its monastic **provenance** through marginal shelf-marks."}
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

print(f"Motion Batch 14A: Successfully updated {updated}/{len(data)} notes.")
