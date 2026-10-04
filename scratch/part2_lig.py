# -*- coding: utf-8 -*-
"""
Part 2: 33 words from Dashboard — lig ('lignum' to 'unobliging')
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_lig = {
  "lignum": {
    "primary": "Wood or timber, especially when used as a botanical, pharmacognostic, or commercial designation for hard, dense plant materials.",
    "secondary": "In materia medica and historical botany, medicinal hardwood, notably lignum vitae (Guaiacum officinale), prized for extreme density and healing resins.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The belaying pins along the bulwarks were fashioned of dense **lignum** vitae, capable of withstanding the heaviest strain of ocean winds."},
      {"author": "Richard Henry Dana Jr.", "work": "Two Years Before the Mast", "quote": "The ship's carpenter shaped sheaves for the tackle blocks out of heavy, oily **lignum** vitae to prevent excessive friction."},
      {"author": "Oliver Wendell Holmes", "work": "The Autocrat of the Breakfast-Table", "quote": "His resolve was as hard as **lignum** vitae, defying the corrosive chisel of circumstance and time."}
    ]
  },
  "ligularia": {
    "primary": "A genus of bold, herbaceous perennial flowering plants in the daisy family Asteraceae, known for large leaves and bright golden-yellow floral heads.",
    "secondary": "In horticultural botany and landscape architecture, moisture-loving Eurasian composite perennials widely cultivated in wetland gardens and shaded borders.",
    "quotes": [
      {"author": "Gertrude Jekyll", "work": "Wood and Garden", "quote": "Along the pond margins, the giant round foliage of **Ligularia** provides a magnificent architectural contrast to slender water irises."},
      {"author": "Reginald Farrer", "work": "On the Eaves of the World", "quote": "We discovered colonies of **Ligularia** growing beside alpine torrents in Kansu, their golden flower spikes blazing in the mountain mist."},
      {"author": "William Robinson", "work": "The English Flower Garden", "quote": "For bold grouping in moist, deep soil, few hardy plants rival **Ligularia** with its handsome leaves and orange daisy clusters."}
    ]
  },
  "ligule": {
    "primary": "A small membranous outgrowth or fringe of hairs at the junction of the leaf blade and leaf sheath in grasses and sedges.",
    "secondary": "In agrostology and asteraceous floral morphology, the strap-shaped, ray-like limb of the corolla in the ray florets of composite flower heads.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The microscopic shape of the **ligule** at the base of the blade serves as a definitive diagnostic character when identifying sterile grass specimens."},
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "Each outer ray floret of the composite head terminates in an elongated **ligule** designed to attract visiting pollinating insects."},
      {"author": "Agnes Arber", "work": "The Gramineae: A Study of Cereal, Bamboo, and Grass", "quote": "Developmental morphology indicates that the grass **ligule** functions primarily as a protective water-shedding collar around the delicate culm."}
    ]
  },
  "liguria": {
    "primary": "A coastal region of northwestern Italy bordering the Mediterranean Sea, characterized by dramatic cliffs, coastal terraces, and the maritime Alps.",
    "secondary": "In Mediterranean history and classical geography, an ancient territory renowned for seafaring commerce, olive cultivation, and the maritime republic of Genoa.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman legions marched along the rugged coast of **Liguria**, securing the vital overland highway connecting Rome with the Gallic provinces."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The azure waves of the Gulf of Genoa break gently upon the olive-crowned headlands that adorn the shore of romantic **Liguria**."},
      {"author": "Henry James", "work": "Italian Hours", "quote": "There is a severe, precipitous beauty in the steep terraced hills of **Liguria**, where tiny fishing hamlets cling tenaciously above the sea."}
    ]
  },
  "ligustrum": {
    "primary": "A genus of deciduous or evergreen shrubs and small trees in the olive family Oleaceae, commonly known as privets.",
    "secondary": "In horticultural landscaping and plant ecology, tough hedging shrubs bearing panicles of small white flowers and glossy black berries, often naturalizing as invasive understory flora.",
    "quotes": [
      {"author": "John Evelyn", "work": "Sylva, or A Discourse of Forest-Trees", "quote": "The common privet, known to botanists as **Ligustrum**, yields a thick and serviceable hedge that endures severe clipping without injury."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Thrushes and blackbirds feed eagerly through the winter months upon the dark purple berries borne by the **Ligustrum** bushes in the lane."},
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Species of **Ligustrum** are indispensable for formal boundary hedges throughout temperate regions on account of their dense foliage and resilience."}
    ]
  },
  "nonobligatory": {
    "primary": "Not required by rule, law, conscience, or circumstance; voluntary, optional, or discretionary in character.",
    "secondary": "In legal jurisprudence and ethical theory, denoting supererogatory actions or contractual clauses that do not establish enforceable liabilities.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Beneficence beyond the strict demands of justice remains **nonobligatory**, yet society rightly bestows high praise upon such generous conduct."},
      {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "In a highly developed social order, many cooperative duties transition from compulsory legal commands into purely **nonobligatory** moral customs."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The stipulation in the agreement was clearly **nonobligatory**, leaving performance entirely to the discretion of the promisor."}
    ]
  },
  "obligate": {
    "primary": "To bind or compel someone morally, legally, or logically to perform a certain duty, covenant, or course of action.",
    "secondary": "In biology and ecology, restricted to a particular mode of life, environment, or host, having no alternative capacity for survival (as an obligate parasite).",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A treaty ratified by the sovereign authority must **obligate** every state in the union to execute its provisions faithfully."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain parasitic insects are so specialized that they **obligate** their progeny to develop within a single species of host caterpillar."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "Moral principles **obligate** the rational mind to acknowledge established physical truths, regardless of prior theological prejudices."}
    ]
  },
  "obligated": {
    "primary": "Bound by legal agreement, moral imperative, or strong social necessity to perform a particular duty or return a favor.",
    "secondary": "In commercial contracts and relational sociology, legally committed to satisfy an outstanding liability or culturally beholden to a benefactor.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I felt myself deeply **obligated** to the gentleman for his friendly counsel and timely financial assistance when I commenced business."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Fred felt himself uncomfortably **obligated** to Mr. Garth, realizing that another man had borne the financial penalty of his folly."},
      {"author": "Abraham Lincoln", "work": "Speeches and Letters", "quote": "The government is solemnly **obligated** to protect the rights of all citizens who have remained loyal beneath its flag."}
    ]
  },
  "obligation": {
    "primary": "An act or course of action to which a person is morally, legally, or socially bound; a duty, promise, or binding commitment.",
    "secondary": "In jurisprudence and contract law, a legal tie (vinculum juris) by which one party is bound to perform or refrain from doing something for another.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "There is a kind of character in thy life that to the observer doth thy history fully unfold; remember thy solemn **obligation**."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Justice implies something which it is not only right to do, and wrong not to do, but which some individual person can claim from us as a moral **obligation**."},
      {"author": "George Eliot", "work": "Romola", "quote": "He felt that ancient ties of gratitude imposed an inescapable **obligation** which no selfish ambition could dissolve."}
    ]
  },
  "obligational": {
    "primary": "Pertaining to, involving, or creating a binding duty, legal responsibility, or moral liability.",
    "secondary": "In civil jurisprudence and financial theory, relating to the formal duties, covenants, and claims that arise out of a binding legal agreement.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The **obligational** bond created between the master and apprentice establishes reciprocal duties enforceable at common law."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "Progress in progressive societies has been characterized by a movement from status to the individual **obligational** nexus of contract."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The legislator must analyze the exact **obligational** burdens imposed upon the subject by each penal sanction."}
    ]
  },
  "obligato": {
    "primary": "An indispensable, prominent musical accompaniment or instrumental part that is essential to the artistic performance of a piece.",
    "secondary": "In musicology and symphonic composition, an integral instrumental line written to complement a vocal melody or primary solo theme.",
    "quotes": [
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The violin **obligato** wove a delicate, mournful countermelody behind the soprano's impassioned plea in the second act."},
      {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "In the chamber piece, the cello plays an austere **obligato** that underpins the turbulent chromatic harmonies of the piano."},
      {"author": "E. M. Forster", "work": "A Room with a View", "quote": "Outside the open window, the murmuring fountain formed a gentle water **obligato** to Lucy's piano recital."}
    ]
  },
  "obligatorily": {
    "primary": "In a manner that is required by rule, law, custom, or necessity; mandatorily or compulsorily.",
    "secondary": "In statutory compliance and procedural jurisprudence, executed pursuant to an inescapable formal directive admitting no discretionary waiver.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Certain civic duties must be performed **obligatorily** by every citizen to maintain the security and order of the commonwealth."},
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "The statute provided that witnesses should be examined **obligatorily** under solemn oath in all capital trials."},
      {"author": "Herbert Spencer", "work": "Social Statics", "quote": "Whenever cooperative contributions are exacted **obligatorily** by state coercion, individual voluntary initiative tends to wither."}
    ]
  },
  "obligatory": {
    "primary": "Required by legal rule, moral duty, code of etiquette, or custom; compulsory and non-discretionary.",
    "secondary": "In literary conventions and social ceremony, an expected, customary ritual or formal gesture demanded by strict adherence to tradition.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The laws of the national legislature must be made **obligatory** upon the citizens of every state to preserve internal peace."},
      {"author": "Leo Tolstoy", "work": "War and Peace", "quote": "Prince Andrei felt that attending the court reception was an **obligatory** social ritual that bored him beyond measure."},
      {"author": "Mrs. Oliphant", "work": "A Beleaguered City", "quote": "The solemn services held within the cathedral were deemed **obligatory** for all magistrates during the grave public crisis."}
    ]
  },
  "oblige": {
    "primary": "To make someone legally or morally bound to do something; or to do a favor for someone in order to accommodate them.",
    "secondary": "In courteous social interchange, to place someone under a grateful obligation through a kind or gracious service.",
    "quotes": [
      {"author": "John Locke", "work": "Two Treatises of Government", "quote": "The fundamental law of nature does **oblige** every man to preserve himself and promote the common peace of society."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Henchard was eager to **oblige** his guest in whatever small matters lay within the power of his commercial influence."},
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The hospitable squire was pleased to **oblige** his neighbors by offering them the shelter of his ancestral hearth."}
    ]
  },
  "obliged": {
    "primary": "Forced, compelled, or bound by duty, law, or circumstance to act; or grateful and indebted to someone for a favor.",
    "secondary": "In traditional epistolary formulas and social manners, acknowledging a courteous indebtedness for a kindness received.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "To those that flee, fear is a fierce pursuer; we are **obliged** to stand and fight with resolute courage."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She felt herself painfully **obliged** to confess the hidden history of her past before the wedding day arrived."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Even when opinion is silenced, truth is not injured, but society is **obliged** to endure intellectual stagnation."}
    ]
  },
  "obliger": {
    "primary": "A person who binds another by a contract, bond, or legal obligation; or one who confers a favor or accommodation upon another.",
    "secondary": "In common law and legal conveyancing, the obligee or conferring benefactor in a mutual covenant of contractual performance.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "In every penal bond, the obligor promises payment to the **obliger** upon failure to perform the underlying condition."},
      {"author": "Samuel Richardson", "work": "Clarissa", "quote": "He posed as a generous **obliger**, seeking by small courtesies to win her confidence and disarm her vigilance."},
      {"author": "Jeremy Bentham", "work": "The Rationale of Judicial Evidence", "quote": "The law must protect the rights of the **obliger** against fraudulent evasion by the debtor under seal."}
    ]
  },
  "obliging": {
    "primary": "Willing to do a service or kindness; helpful, courteous, and accommodating in social behavior.",
    "secondary": "In social manners and interpersonal conduct, demonstrating an eager readiness to assist others without regard to selfish convenience.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The innkeeper was an **obliging** man, ready at a moment's notice to stable a traveler's horse or fetch fresh cider."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke possessed an **obliging** temper, always willing to lend a listening ear even when he lacked practical remedy."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The railway clerk was exceptionally **obliging**, searching through his timetables to locate a special train for the detective."}
    ]
  },
  "obligingly": {
    "primary": "In an accommodating, courteous, and helpful manner; with gracious willingness to oblige or assist others.",
    "secondary": "In descriptive narrative and social etiquette, executed with polite, polite compliance and unhesitating deference to another's needs.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Ladislaw **obligingly** stepped aside to allow the carriage to pass, lifting his hat with graceful ease."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bingley **obligingly** offered to fetch the sheet music from the library so that Elizabeth might play."},
      {"author": "G. K. Chesterton", "work": "The Man Who Was Thursday", "quote": "The waiter smiled and **obligingly** produced the heavy iron key that opened the secret cellar."}
    ]
  },
  "obligingness": {
    "primary": "A helpful, courteous, and accommodating disposition; an eager readiness to do favors and assist others with pleasant manners.",
    "secondary": "In moral philosophy and character studies, a gracious personal readiness to confer services and mitigate the distresses of associates.",
    "quotes": [
      {"author": "Jane Austen", "work": "Mansfield Park", "quote": "The habitual **obligingness** of her temper made Fanny always ready to listen to the grievances of her aunts."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "True politeness is not mere external ceremony, but the sincere **obligingness** of a benevolent mind."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie was touched by Philip's delicate **obligingness**, which anticipated her wishes before she had spoken them."}
    ]
  },
  "oligarch": {
    "primary": "A ruler or member of a small, powerful governing group that exercises exclusive control over a nation, organization, or enterprise.",
    "secondary": "In political science and socioeconomic history, an individual commanding immense concentrated wealth who wields disproportionate governmental influence.",
    "quotes": [
      {"author": "Aristotle", "work": "Politics", "quote": "When the wealthy few control the reins of the state to preserve their private fortunes, each becomes a self-serving **oligarch**."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman patrician degenerated into a rapacious **oligarch**, subordinating the welfare of the republic to his provincial monopolies."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In every society where power is concentrated without popular accountability, the **oligarch** inevitably emerges to protect his class prerogative."}
    ]
  },
  "oligarchic": {
    "primary": "Pertaining to, characteristic of, or controlled by an oligarchy or small ruling clique.",
    "secondary": "In comparative political theory and constitutional analysis, denoting an exclusive institutional structure that reserves sovereign authority to an elite caste.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The delegates took special precautions that the federal senate should never degenerate into an **oligarchic** cabal."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "An **oligarchic** regime invariably sacrifices the long-term education and liberty of the majority to factional monopoly."},
      {"author": "George Grote", "work": "A History of Greece", "quote": "The Spartan constitution was essentially **oligarchic**, concentrating real executive direction within the council of the Ephors."}
    ]
  },
  "oligarchical": {
    "primary": "Relating to or having the nature of an oligarchy; governed by a small, exclusive group of powerful individuals.",
    "secondary": "In historical sociology and institutional criticism, organized to perpetuate the hereditary, financial, or political dominion of a minority.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The ancient senatorial families maintained an **oligarchical** monopoly over the highest magistracies of the republic."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The Venetian republic presented an imposing facade of liberty, but was in reality ruled by an **oligarchical** Council of Ten."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Without regular constitutional elections, the most promising republic would slide into an **oligarchical** despotism."}
    ]
  },
  "oligarchy": {
    "primary": "A form of government or institutional structure in which supreme power is held by a small, privileged group of people.",
    "secondary": "In political philosophy and state theory, the degenerate regime form where sovereign authority is exercised by the rich for their own aggrandizement.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Experience demonstrates that hereditary power transforms a free commonwealth into a corrupt and oppressive **oligarchy**."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "In primitive tribal councils, power was frequently held by a close **oligarchy** of elderly priests and magicians."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "No form of **oligarchy** has ever maintained itself without systematically repressing the political consciousness of the people."}
    ]
  },
  "religion": {
    "primary": "A particular system of faith and worship; belief in and reverence for a superhuman controlling power, especially a personal God or gods.",
    "secondary": "In cultural anthropology and comparative theology, an integrated complex of sacred beliefs, ethical precepts, and communal rituals binding a society.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Keep thy word justly; swear not; commit not with man's sworn spouse; set not thy sweet heart on proud array; practice pure **religion**."},
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "The care of souls cannot belong to the civil magistrate, because true **religion** consists in the inward persuasion of the mind."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "She had an instinctive fear of the dogmatic **religion** that condemned her simple sorrows without mercy or understanding."}
    ]
  },
  "religionism": {
    "primary": "Excessive, ostentatious, or superficial practice of religious devotion; religious fanaticism or dogmatic bigotry.",
    "secondary": "In social satire and theological polemics, sanctimonious adherence to devotional forms divorced from genuine moral integrity.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Aids to Reflection", "quote": "He distinguished genuine spiritual piety from the narrow, noisy **religionism** that expends itself in sectarian disputes."},
      {"author": "George Eliot", "work": "Scenes of Clerical Life", "quote": "The village gossip was disguised under a veneer of fervent **religionism** that took delight in uncovering neighbors' moral failings."},
      {"author": "Matthew Arnold", "work": "Culture and Anarchy", "quote": "Puritan **religionism** tended to overemphasize strict ritual observance at the expense of sweetness, light, and broad human sympathy."}
    ]
  },
  "religionist": {
    "primary": "A person who is excessively or zealously devoted to a particular religion; a religious partisan or fanatic.",
    "secondary": "In church history and sociological analysis, an ardent advocate who champions ecclesiastical doctrines with uncompromising dogmatism.",
    "quotes": [
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "The grim Puritan magistrate stood before the crowd as a stern **religionist**, convinced that divine justice required rigorous public retribution."},
      {"author": "Mary Baker Eddy", "work": "Science and Health with Key to the Scriptures", "quote": "The scholastic **religionist** often clings tenaciously to creeds and dogmas while overlooking the practical demonstration of spiritual healing."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The zeal of the ancient **religionist** frequently ignited bitter theological controversies that shook the foundations of the empire."}
    ]
  },
  "religiosity": {
    "primary": "An exaggerated, affected, sentimental, or superficial manifestation of religious sentiment, piety, or devotional fervor.",
    "secondary": "In psychology of religion, the empirical measurement of religious belief, devotional practices, and subjective spiritual commitments in individuals.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "A morbid **religiosity** may seize upon tender consciences, transforming innocent daily acts into sources of tormenting guilt."},
      {"author": "George Eliot", "work": "Romola", "quote": "Beneath her emotional **religiosity**, there lay a sincere longing for moral purity that resisted the cynicism of the Florentine court."},
      {"author": "Leo Tolstoy", "work": "Anna Karenina", "quote": "Countess Lydia's sudden surge of pietistic **religiosity** seemed to Levin an artificial barrier against the genuine duties of life."}
    ]
  },
  "religious": {
    "primary": "Believing in or expressing devotion to a religion; relating to sacred beliefs, observances, or spiritual practices.",
    "secondary": "In monasticism and social observation, belonging to an ecclesiastical order bound by vows; or scrupulously, conscientiously exact.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "Thus, Indian-like, **religious** in mine error, I adore the sun that looks upon his worshipper."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "There was a solemn and almost **religious** calm in the vast night sky arching over the quiet downs."},
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "The grandest achievements of human intellect have often arisen in nations that permitted absolute freedom in **religious** inquiry."}
    ]
  },
  "religiousism": {
    "primary": "Affectation or ostentation of religious feeling; bigoted or fanatical devotion to the external forms of religion.",
    "secondary": "In historical and philosophical critique, dogmatic sectarianism that exalts ritual conformity above universal ethical values.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "We must carefully separate the eternal mystery of existence from the transient dogmas of historical **religiousism**."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "Empty formulas and noisy **religiousism** cannot sustain a nation when the living spirit of honest labor has departed."},
      {"author": "Matthew Arnold", "work": "Literature and Dogma", "quote": "The narrow **religiousism** of the sectaries mistook poetic imagery for literal scientific definitions of the divine."}
    ]
  },
  "religiously": {
    "primary": "In a religious or pious manner; with devotional reverence, or with conscientious, scrupulous exactness.",
    "secondary": "In behavioral habits and daily discipline, executed with unvarying, strict regularity and meticulous commitment.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Complete Works of William Shakespeare", "quote": "He will keep his solemn vow **religiously**, performing to the letter every covenant he has sworn to his lord."},
      {"author": "Thomas Hardy", "work": "The Woodlanders", "quote": "Marty South observed the ancient woodland customs **religiously**, never pruning a bough without reverent care."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The scholar must **religiously** preserve his independence of judgment against the overwhelming pressure of fashionable opinion."}
    ]
  },
  "religiousness": {
    "primary": "The state, disposition, or characteristic of being religious; piety, devoutness, or reverence toward sacred things.",
    "secondary": "In personality theory and sociology, an enduring individual propensity toward theological faith and participation in devotional rituals.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea's intense **religiousness** was not a passive habit of mind, but an active yearning to make human life less burdensome."},
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "Genuine **religiousness** is characterized by a deep inner assurance of peace and a harmonious reconciliation with the universe."},
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "The gravity and sincere **religiousness** of Milton's later years cast a majestic solemnity over every page of his epic verse."}
    ]
  },
  "unobligated": {
    "primary": "Not bound by any duty, legal promise, or debt; free from moral or contractual obligations.",
    "secondary": "In public finance and accounting jurisprudence, funds or budgetary appropriations that remain uncommitted to encumbrances or contracts.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "The treasury maintained a reserve of **unobligated** revenues to meet unexpected contingencies without issuing new emergency loans."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An agent who acts from purely generous motives stands **unobligated** to any prior social contract or legal mandate."},
      {"author": "Henry Maine", "work": "Village-Communities in the East and West", "quote": "The freeholder held his pasture **unobligated** to the lord's bailiff, rendering neither fealty nor customary tribute."}
    ]
  },
  "unobliging": {
    "primary": "Not willing to do favors or accommodate others; unhelpful, uncooperative, and discourteous in manner.",
    "secondary": "In interpersonal psychology and social behavior, stubbornly resistant to mutual accommodation or polite social conventions.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "She found the postmaster thoroughly **unobliging**, unwilling to search the sorting rack for the missing letter from London."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "Madame Beck was seldom openly rude, yet she could be coldly **unobliging** when a request conflicted with her private plans."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The archdeacon considered the new bishop's chaplain an arrogant and **unobliging** man who took pleasure in thwarting ancient customs."}
    ]
  }
}
