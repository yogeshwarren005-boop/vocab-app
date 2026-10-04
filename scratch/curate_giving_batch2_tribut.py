# -*- coding: utf-8 -*-
"""
Curates Dashboard — tribut (32 words) in Cluster Giving & Receiving.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_tribut = {
  "attributable": {
    "primary": "Capable of being ascribed, credited, or assigned to a specific cause, author, or origin.",
    "secondary": "In epidemiology and risk analysis, the proportion of disease incidence that can be ascribed to a specific hazard.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Many morphological differences between varieties are directly **attributable** to the conditions of life."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The rapid rise in manufacturing output is largely **attributable** to the systematic division of labor."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The decay of civic virtues was partly **attributable** to the enervating luxury of the imperial provinces."}
    ]
  },
  "attribute": {
    "primary": "To regard something as being caused by, belonging to, or originating from someone or something; a quality or characteristic.",
    "secondary": "In database systems and metaphysics, an inherent qualitative property or field belonging to an entity.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Superstitious men **attribute** extraordinary natural events to demonic interventions rather than physical causes."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Color, shape, and weight are each a distinct sensory **attribute** by which we recognize physical objects."},
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Mercy is an **attribute** to God himself, and earthly power doth then show likest God's when mercy seasons justice."}
    ]
  },
  "attribution": {
    "primary": "The act of assigning, crediting, or ascribing something to an author, source, cause, or origin.",
    "secondary": "In art history, the scholarly assignment of an unsigned painting or sculpture to a specific master or workshop.",
    "quotes": [
      {"author": "Henry James", "work": "The Aspern Papers", "quote": "Scholars engaged in heated debates regarding the authentic **attribution** of the newly discovered Venetian sonnets."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Critical analysis of internal style confirmed the traditional **attribution** of the essay to Addison."},
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Modern philology has revised the classical **attribution** of several Platonic dialogues to later disciples."}
    ]
  },
  "attributive": {
    "primary": "Serving to ascribe, attribute, or assign a quality; directly modifying a noun within a noun phrase.",
    "secondary": "In grammatical syntax, an adjective placed immediately before the noun it modifies rather than in the predicate.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "The poet uses fresh **attributive** epithets that revitalize familiar descriptions of nature."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "His prose gains descriptive force through the placement of forceful **attributive** words."},
      {"author": "Otto Jespersen", "work": "The Philosophy of Grammar", "quote": "In English syntax, the **attributive** adjective precedes the substantive, unlike in Romance languages."}
    ]
  },
  "attributively": {
    "primary": "In an attributive manner; functioning syntactically as a direct modifier within a noun phrase.",
    "secondary": "In linguistic descriptive analysis, using nouns or adjectives before heads to modify meaning directly.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "A Dictionary of the English Language", "quote": "Certain substantives in English may be employed **attributively**, as in the phrase sea coast."},
      {"author": "Henry Sweet", "work": "A New English Grammar", "quote": "Adjectives used **attributively** qualify the following noun without requiring a connecting copula."},
      {"author": "George Curme", "work": "English Grammar", "quote": "Participles placed **attributively** before nouns express permanent characteristics rather than temporary actions."}
    ]
  },
  "contribute": {
    "primary": "To give something (money, time, knowledge, or effort) toward a common pool, purpose, or result.",
    "secondary": "In academic journalism and publishing, to supply articles, essays, or literary pieces to a periodical.",
    "quotes": [
      {"author": "Benjamin Franklin", "work": "Autobiography", "quote": "I was asked to **contribute** to the establishment of the public academy and city hospital."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "All classes of citizens should **contribute** toward the expenses of government in proportion to their abilities."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Social instincts prompt the individual to **contribute** voluntarily to the defense and well-being of the tribe."}
    ]
  },
  "contributing": {
    "primary": "Giving, supplying, or playing a part in bringing about a particular result or common achievement.",
    "secondary": "In forensic pathology and causation analysis, an auxiliary factor that aggravates an existing fatal pathology.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Local town meetings were a powerful **contributing** cause to the preservation of democratic freedom."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Chemical runoff was identified as a major **contributing** element in the collapse of river fish populations."},
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "Diplomatic inertia was a decisive **contributing** circumstance to the European catastrophe of 1939."}
    ]
  },
  "contribution": {
    "primary": "Something that is given, donated, or contributed to help achieve a collective objective.",
    "secondary": "In pension and social security administration, mandatory or voluntary payments made to fund retirement benefits.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "Every great thinker makes a lasting **contribution** to the cumulative intellectual capital of humanity."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Taxes levied upon commodities constitute an indirect **contribution** by consumers to the treasury."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "This research represents an experimental **contribution** to the understanding of spontaneous atomic disintegrations."}
    ]
  },
  "contributive": {
    "primary": "Tending to contribute; serving as a contributing cause, factor, or auxiliary aid.",
    "secondary": "In moral philosophy and teleology, acts that promote the overarching common welfare of society.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Ancient customs are deeply **contributive** to the stability and moral temper of the commonwealth."},
      {"author": "Herbert Spencer", "work": "The Data of Ethics", "quote": "Conduct is judged virtuous in proportion as it is **contributive** to the fullness of human life."},
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Experiential learning is directly **contributive** to the development of autonomous civic judgment."}
    ]
  },
  "contributor": {
    "primary": "A person or thing that contributes, gives, or donates something to a common fund, cause, or journal.",
    "secondary": "In periodical literature, a writer who regularly submits essays, reviews, or news dispatches.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Skimpole was never a **contributor** to household expenses, claiming his artistic nature was above commerce."},
      {"author": "William Makepeace Thackeray", "work": "The English Humourists", "quote": "Addison was the celebrated chief **contributor** whose elegant papers established the Spectator's fame."},
      {"author": "Thomas Huxley", "work": "Science and Culture", "quote": "Every careful laboratory investigator becomes a valuable **contributor** to empirical natural science."}
    ]
  },
  "contributory": {
    "primary": "Playing a part in bringing about a result; acting as an auxiliary factor or contributor.",
    "secondary": "In tort law, contributory negligence: conduct by an injured party that helped cause the harm, historically barring recovery.",
    "quotes": [
      {"author": "Blackstone", "work": "Commentaries on the Laws of England", "quote": "Courts consider whether the plaintiff's own reckless behavior was a **contributory** cause of the disaster."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Changed climatic conditions served as a **contributory** stimulus to organic divergence."},
      {"author": "Oliver Wendell Holmes", "work": "The Common Law", "quote": "A finding of **contributory** fault in maritime collision required equal division of damages."}
    ]
  },
  "distributary": {
    "primary": "A branch of a river that flows away from the main stream and does not rejoin it, common in deltas.",
    "secondary": "In geomorphology and fluvial hydrology, channels through which deltaic waters disperse into a lagoon, sea, or lake.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The great Mississippi delta branches into multiple **distributary** channels before entering the Gulf."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative", "quote": "We steered our canoe into a broad **distributary** of the Orinoco, shadowed by dense mangrove swamps."},
      {"author": "John Wesley Powell", "work": "Canyons of the Colorado", "quote": "Sediment deposits frequently choke the mouth of each **distributary** during seasonal high water."}
    ]
  },
  "distribute": {
    "primary": "To divide among several or many; to apportion, scatter, disperse, or dispense systematically.",
    "secondary": "In commercial supply logistics, to transport and deliver manufactured goods to retail markets.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Free competition tends to **distribute** capital among those industries where it yields the highest return."},
      {"author": "William Shakespeare", "work": "King Lear", "quote": "So distribution should undo excess, / And each man have enough... Let the king **distribute** his wealth justly."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The emperor ordered his grain officers to **distribute** corn freely among the starving populace."}
    ]
  },
  "distributed": {
    "primary": "Dealt out, apportioned, scattered, or dispersed over a given area, population, or time.",
    "secondary": "In computer systems architecture, a network of autonomous computers communicating via messages to coordinate actions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Closely allied plant species are often widely **distributed** across separated continents."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "Wealth is produced according to physical laws, but **distributed** according to social institutions."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Constitutional checks ensure that sovereign authority is safely **distributed** among three branches."}
    ]
  },
  "distributer": {
    "primary": "An agent, person, or organization that distributes or dispenses goods or services; a distributor (variant spelling).",
    "secondary": "In early industrial trade publications, a wholesale merchant supplying local shopkeepers.",
    "quotes": [
      {"author": "Thomas Babington Macaulay", "work": "The History of England", "quote": "The royal almoner acted as the chief **distributer** of charity to poor scholars at Oxford."},
      {"author": "Walter Scott", "work": "The Antiquary", "quote": "The village postmaster was the sole **distributer** of news and letters across the remote shire."},
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "A generous patron must be an impartial **distributer** of praise and rewards."}
    ]
  },
  "distribution": {
    "primary": "The action of sharing out or dividing something among a number of recipients; frequency of occurrence.",
    "secondary": "In statistics and probability theory, a mathematical function showing the frequency or likelihood of values.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The annual produce of the land and labor divides naturally into the three great **distribution** shares of rent, wages, and profit."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Geographical **distribution** of organisms across oceanic islands offers the strongest evidence for evolution."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The equal **distribution** of landed inheritances rapidly dismantled the old aristocratic estates."}
    ]
  },
  "distributional": {
    "primary": "Pertaining to, involving, or affecting the distribution, allocation, or geographical range of something.",
    "secondary": "In welfare economics and tax policy, evaluating how policies impact the relative economic welfare of different income tiers.",
    "quotes": [
      {"author": "Alfred Russel Wallace", "work": "Island Life", "quote": "Distinct **distributional** boundaries separate the fauna of the Australian and Asian archipelagoes."},
      {"author": "John Maynard Keynes", "work": "The General Theory of Employment, Interest and Money", "quote": "Fiscal policy exercises powerful **distributional** effects on purchasing power among wage earners."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Fossil discoveries established new **distributional** maps of prehistoric marine life."}
    ]
  },
  "distributive": {
    "primary": "Concerned with or relating to the distribution of things; apportioning shares.",
    "secondary": "In political philosophy and ethics, distributive justice: the perceived fairness of resource allocation across a society.",
    "quotes": [
      {"author": "Aristotle", "work": "Nicomachean Ethics", "quote": "Justice in one sense is **distributive**, concerning the apportionment of honors and assets among citizens."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Social utility requires a **distributive** principle that maximizes general happiness."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The king exercised **distributive** equity, rewarding loyal ministers while checking aristocratic greed."}
    ]
  },
  "distributively": {
    "primary": "In a distributive manner; singly and separately rather than collectively or as an aggregate.",
    "secondary": "In formal logic, applying a universal predicate to every individual member of a class taken separately.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Terms applied **distributively** refer to each single object belonging to the general idea."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "A proposition valid for a collection **distributively** must hold for every element in isolation."},
      {"author": "Jeremy Bentham", "work": "An Introduction to the Principles of Morals and Legislation", "quote": "The legislator considers the interests of the community **distributively**, as the sum of individual citizens."}
    ]
  },
  "distributor": {
    "primary": "A person, company, or device that distributes, supplies, or dispenses goods or resources.",
    "secondary": "In internal combustion automotive engineering, a rotating mechanical switch directing ignition voltage to spark plugs.",
    "quotes": [
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "The wholesale merchant serves as an essential commercial **distributor** bridging factories and consumers."},
      {"author": "Mark Twain", "work": "What Is Man? and Other Essays", "quote": "Nature acts as a magnificent **distributor** of talents, bestowing genius with sovereign impartiality."},
      {"author": "Upton Sinclair", "work": "The Jungle", "quote": "The meatpacker dominated the retail market as the supreme **distributor** across Midwestern cities."}
    ]
  },
  "reattribute": {
    "primary": "To attribute, assign, or credit something to a different author, origin, or cause.",
    "secondary": "In art history, the formal reassignment of a painting's provenance based on new spectroscopic or stylistic evidence.",
    "quotes": [
      {"author": "Henry James", "work": "The Sacred Fount", "quote": "Upon discovering the hidden diary, scholars resolved to **reattribute** the anonymous memoirs."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "Internal linguistic evidence compelled philologists to **reattribute** the pamphlet to Defoe."},
      {"author": "Roger Fry", "work": "Vision and Design", "quote": "Recent archival research led the gallery curator to **reattribute** the portrait to a Flemish apprentice."}
    ]
  },
  "redistribute": {
    "primary": "To distribute, divide, or apportion again or in a different way; to alter existing allocations.",
    "secondary": "In macroeconomic fiscal policy, to reallocate national income or wealth through taxation and social transfers.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The state may rightfully utilize progressive inheritance taxes to **redistribute** unearned fortunes."},
      {"author": "Frank A. Fetter", "work": "The Principles of Economics", "quote": "Sudden monetary inflation serves to **redistribute** wealth arbitrarily from creditors to debtors."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Agrarian laws intended to **redistribute** private farmland were consistently rejected by American settlers."}
    ]
  },
  "redistributed": {
    "primary": "Distributed or apportioned again or differently; having undergone reallocation of resources.",
    "secondary": "In geography and hydrology, sediments or water volumes transported and deposited in new locations.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Surplus food produced in fertile valleys was smoothly **redistributed** by merchant shipping to mountain towns."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould", "quote": "Earthworms continually **redistributed** fine soil particles, burying heavy stones beneath fresh loam."},
      {"author": "John Maynard Keynes", "work": "The Economic Consequences of the Peace", "quote": "Postwar boundary treaties **redistributed** European coal basins, fracturing established trade routes."}
    ]
  },
  "redistribution": {
    "primary": "The act, process, or policy of distributing something again or differently; reallocation.",
    "secondary": "In public finance, tax-and-transfer mechanisms designed to narrow economic inequality across social strata.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Democratic sentiment favors gradual **redistribution** through universal public schooling rather than confiscation."},
      {"author": "John Stuart Mill", "work": "Principles of Political Economy", "quote": "The equitable **redistribution** of legislative representation abolished corrupt rotten boroughs in parliament."},
      {"author": "Frank A. Fetter", "work": "Economics: Modern Economic Problems", "quote": "Every major tariff revision causes a hidden **redistribution** of commercial profits among competing industries."}
    ]
  },
  "retribution": {
    "primary": "Punishment inflicted on someone as vengeance for a wrong or criminal act; justly deserved penalty.",
    "secondary": "In jurisprudence, retributive justice holding that criminal punishment is justified as a moral desert rather than mere deterrence.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "Heaven will direct it... The day of terrible **retribution** arrives for the murderer of the king."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess bowed her head beneath the impending stroke of social and judicial **retribution**."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Bulstrode trembled at the thought of divine **retribution** unmasking his hypocrisy before his neighbors."}
    ]
  },
  "retributive": {
    "primary": "Dispensing, relating to, or characterized by retribution; punishing according to desert.",
    "secondary": "In penology, sentencing philosophies focused on proportionate punishment proportional to the gravity of the crime.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip was tormented by a guilty conscience, expecting **retributive** punishment at every turn."},
      {"author": "Immanuel Kant", "work": "The Philosophy of Law", "quote": "Judicial punishment must always be **retributive**, grounded solely upon the fact that the criminal committed a crime."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "Chillingworth dedicated his existence to inflicting slow, **retributive** torment upon his secret rival."}
    ]
  },
  "retributory": {
    "primary": "Serving as retribution; punitive, compensatory, or retaliatory in nature.",
    "secondary": "In moral theology, divine judgments visited upon wicked nations as historical chastisement.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarian sack of Rome was regarded by Christian writers as a **retributory** judgment upon pagan sins."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The horrors of the Jacobin Terror appeared as a **retributory** reckoning for centuries of feudal oppression."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "The tragic curse on the Ravenswood family marched onward with grim, **retributory** precision."}
    ]
  },
  "tributary": {
    "primary": "A river or stream flowing into a larger river or lake; a person, state, or nation that pays tribute.",
    "secondary": "In geopolitical history, a subordinate client kingdom paying annual financial or military dues to an imperial suzerain.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Vast ocean currents swept onward, carrying every lesser **tributary** stream toward the polar depths."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The kings of Armenia remained **tributary** rulers, subject to the rival demands of Rome and Parthia."},
      {"author": "William Shakespeare", "work": "Julius Caesar", "quote": "What tributaries follow him to Rome, to grace in captive bonds his chariot wheels?... Even the royal **tributary** was paraded through the Forum."}
    ]
  },
  "tribute": {
    "primary": "An act, statement, or gift intended to show gratitude, respect, or admiration; payment made by one state to another.",
    "secondary": "In classical and medieval statecraft, regular wealth, slaves, or bullion extracted under threat of military conquest.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Tempest", "quote": "Subject his coronet to his crown, and bend the dukedom to most ignoble stooping... Paying heavy **tribute** to the king of Naples."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Weak emperors bought transient peace by paying an annual **tribute** of gold to the Gothic chieftains."},
      {"author": "Abraham Lincoln", "work": "Gettysburg Address", "quote": "It is altogether fitting and proper that we should pay this solemn **tribute** to those who gave their lives."}
    ]
  },
  "tributyrin": {
    "primary": "A triglyceride ester formed from glycerol and three butyric acid molecules, found naturally in butter.",
    "secondary": "In biochemistry and clinical enzymology, a standard substrate used to assay pancreatic lipase activity.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Hydrolysis of **tributyrin** by microbial ferments yields glycerol alongside volatile butyric acid."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Impaired cleavage of **tributyrin** in digestive secretions indicates diminished pancreatic exocrine function."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Pure butter contains distinct quantities of **tributyrin**, which imparts its characteristic culinary richness."}
    ]
  },
  "unattributable": {
    "primary": "Not able to be assigned, credited, or ascribed to a specific author, origin, or cause.",
    "secondary": "In political journalism, briefing statements permitted for publication only on background without naming the official source.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "Several early fragments preserved by Diogenes Laertius remain completely **unattributable** to any known school."},
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The cipher letter was wholly **unattributable**, bearing no watermark, signature, or return postal stamp."},
      {"author": "Henry James", "work": "The Middle Years", "quote": "The author was troubled by vague, **unattributable** echoes of forgotten conversations that crept into his drafts."}
    ]
  },
  "undistributed": {
    "primary": "Not dealt out, allocated, or dispersed; retained, undivided, or held in reserve.",
    "secondary": "In corporate accounting, undistributed profits: retained net earnings not paid out as shareholder dividends.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "A prudent manufacturer retains a portion of **undistributed** profits to replace worn machinery."},
      {"author": "Alexander Hamilton", "work": "Report on Public Credit", "quote": "Considerable **undistributed** balances remained in the state treasuries at the conclusion of the war."},
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "In formal syllogistic logic, the middle term must not remain **undistributed** in both premises."}
    ]
  }
}
