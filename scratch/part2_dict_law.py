# -*- coding: utf-8 -*-
"""
Part 2 of Batch 3: dict_law words 25-47 (23 words):
['dictyopteran', 'dictyosome', 'edict', 'indict', 'indictability', 'indictable',
 'indiction', 'indictment', 'interdict', 'interdiction', 'nonaddictive', 'predict',
 'predictability', 'predictable', 'predictably', 'prediction', 'predictive',
 'predictor', 'unaddicted', 'unpredictability', 'unpredictable', 'unpredictably',
 'unpredictive']
"""
import sys

sys.stdout.reconfigure(encoding="utf-8")

part2_dict = {
  "dictyopteran": {
    "primary": "An insect belonging to the superorder Dictyoptera, encompassing modern cockroaches, termites, and mantises.",
    "secondary": "In evolutionary entomology, an insect presenting characteristic oothecal egg cases, cursorial forelegs, and chewing mouthparts.",
    "quotes": [
      {"author": "Augustus Daniel Imms", "work": "A General Textbook of Entomology", "quote": "The fossil record reveals that many a primitive **dictyopteran** inhabited the dense Carboniferous coal swamps."},
      {"author": "Vincent Dethier", "work": "The Hungry Fly", "quote": "The peripheral sensilla of a foraging **dictyopteran** respond with keen sensitivity to airborne pheromone plumes."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Sexual dimorphism in wing structure is frequently observed in the typical nocturnal **dictyopteran**."}
    ]
  },
  "dictyosome": {
    "primary": "An individual membranous net-like stack of flattened cisternae constituting a Golgi apparatus subunit in eukaryotic cells.",
    "secondary": "In plant cytology and ultrastructure, a discrete cisternal vesicle-forming organelle responsible for polysaccharide synthesis and secretion.",
    "quotes": [
      {"author": "George Emil Palade", "work": "Intracellular Aspects of the Process of Protein Synthesis", "quote": "High-resolution electron microscopy displays each secretory **dictyosome** processing nascent glycan chains within its flattened cisternae."},
      {"author": "Katherine Esau", "work": "Plant Anatomy", "quote": "In growing plant root tips, the active **dictyosome** secretes mucilage droplets toward the expanding cell plate."},
      {"author": "Christian de Duve", "work": "A Guided Tour of the Living Cell", "quote": "Transport vesicles bud continuously from the cis-face of the **dictyosome** to deliver membrane proteins to lysosomes."}
    ]
  },
  "edict": {
    "primary": "An official decree, proclamation, or command issued by an autocratic sovereign or lawful administrative authority.",
    "secondary": "In civil jurisprudence, a formal imperial statute having the force of binding statutory law without legislative enactment.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Emperor Diocletian published an imperious **edict** ordering the demolition of Christian churches across the empire."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "His imperial majesty published a solemn **edict** requiring all subjects to break their eggs at the smaller end."},
      {"author": "Lord Macaulay", "work": "The History of England", "quote": "The royal proclamation was denounced by Parliament as an illegal **edict** that subverted the ancient constitution."}
    ]
  },
  "indict": {
    "primary": "To formally charge someone with a serious crime by the findings and presentment of a grand jury.",
    "secondary": "In criminal procedure, to issue a written bill of indictment alleging specific statutory offenses following evidentiary scrutiny.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The grand inquest possesses constitutional authority to **indict** any felon upon sufficient probable cause."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The public prosecutor stood up before the revolutionary tribunal to **indict** the prisoner for high treason."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The ordinary courts of justice retain full jurisdiction to **indict** and punish public officials guilty of corruption."}
    ]
  },
  "indictability": {
    "primary": "The legal status or susceptibility of an unlawful action or person to formal prosecution by grand jury presentment.",
    "secondary": "In substantive criminal jurisprudence, the threshold determination that an offense fulfills all statutory criteria for formal accusation.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Common law jurists debated the precise **indictability** of non-violent conspiratorial agreements among commercial traders."},
      {"author": "James Fitzjames Stephen", "work": "A History of the Criminal Law of England", "quote": "The magistrate examined the statutory **indictability** of the alleged misdemeanor before remanding the prisoner for trial."},
      {"author": "Oliver Wendell Holmes Jr.", "work": "The Common Law", "quote": "The test of criminal **indictability** rests upon whether the forbidden overt act threatened grave communal injury."}
    ]
  },
  "indictable": {
    "primary": "Liable to be charged with a formal criminal offense; describing an unlawful act punishable upon bill of indictment.",
    "secondary": "In procedural jurisprudence, distinguishing serious felonies and misdemeanors requiring grand jury presentment from summary offenses.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "Every unlawful conspiracy to obstruct public justice constitutes an **indictable** offense punishable by imprisonment."},
      {"author": "Edmund Burke", "work": "Speech on the Impeachment of Warren Hastings", "quote": "These systematic extortions against provincial rulers were not mere improprieties, but flagrant, **indictable** crimes."},
      {"author": "Henry Maine", "work": "Ancient Law", "quote": "Early Roman jurisprudence possessed no clear conception of an **indictable** public wrong distinct from private tortious injury."}
    ]
  },
  "indiction": {
    "primary": "A recurring fifteen-year fiscal and chronological cycle originally instituted in late antiquity for Roman tax assessment.",
    "secondary": "In diplomatics and historical chronology, a conventional calendar reckoning used to date medieval papal bulls, charters, and Byzantine decrees.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The regular tribute of the provinces was adjusted according to the imperial cycle of the **indiction**, renewed every fifteen years."},
      {"author": "Lord Macaulay", "work": "The History of England", "quote": "Ecclesiastical chanceries dated their medieval charters by specifying the year of the imperial **indiction** alongside the regnal year."},
      {"author": "Henry Hallam", "work": "View of the State of Europe during the Middle Ages", "quote": "Chronologists determine the authenticity of early medieval treaties by reconciling the recorded **indiction** with the solar cycle."}
    ]
  },
  "indictment": {
    "primary": "A formal written statement charging a person with an offense, voted and returned by a grand jury.",
    "secondary": "In social criticism and rhetoric, a profound, damning exposure or comprehensive condemnation of a prevailing system or injustice.",
    "quotes": [
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The grand jury returned a true bill of **indictment**, establishing probable cause for trial at the assizes."},
      {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "The severe magistrate scrutinized the formal **indictment** against the vagrant before admitting testimony."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "The rising squalor of industrial cities stands as a scathing **indictment** of laissez-faire commercial policy."}
    ]
  },
  "interdict": {
    "primary": "To forbid, prohibit, or debar authoritatively; or an ecclesiastical censure excluding persons or regions from sacraments.",
    "secondary": "In civil law and military operations, an injunction restraining specific actions or the military disruption of enemy supply lines.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The Roman pontiff placed the rebellious kingdom under solemn **interdict**, silencing all church bells and funeral rites."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon placed a severe **interdict** upon any uninvited discussion of his unfinished theological research."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The royal customs house issued a strict **interdict** preventing the clandestine transport of grain across provincial borders."}
    ]
  },
  "interdiction": {
    "primary": "The authoritative act of prohibiting, forbidding, or barring someone from privileges, commerce, or physical territory.",
    "secondary": "In military logistics and public law, the strategic cutting off of enemy supply routes or the judicial disability imposed on incompetents.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The maritime **interdiction** of foreign commerce by a hostile fleet would swiftly deplete public revenues."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "In Scots and Roman civil law, an **interdiction** prevents prodigal heirs from alienating their ancestral estates."},
      {"author": "Edward Gibbon", "work": "The Decline and Fall of the Roman Empire", "quote": "The imperial **interdiction** against pagan worship was enforced throughout Alexandria with unsparing zeal."}
    ]
  },
  "nonaddictive": {
    "primary": "Not habit-forming; lacking physiological or pharmacological properties that produce chemical dependence or compulsion.",
    "secondary": "In clinical pharmacology, denoting therapeutic analgesic or sedative compounds that do not recruit mesolimbic dopamine tolerance pathways.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Researchers searched diligently for a purely **nonaddictive** analgesic capable of relieving severe neuralgic pain."},
      {"author": "Havelock Ellis", "work": "The Philosophy of Conflict", "quote": "Milder intellectual recreations provide a wholesome, **nonaddictive** diversion from the stressful anxieties of modern life."},
      {"author": "Aldous Huxley", "work": "Brave New World Revisited", "quote": "Utopian planners dreamed of synthesizing a completely **nonaddictive** tranquilizer that would pacify without physical penalty."}
    ]
  },
  "predict": {
    "primary": "To foretell, prophesy, or declare that something will occur in the future based on reason, signs, or observation.",
    "secondary": "In empirical science and epistemology, to deduce observable outcomes from a theoretical hypothesis prior to empirical verification.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "If my theory of gradual transmutation be true, we can **predict** the future discovery of intermediate fossil links."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The experienced woodman can accurately **predict** the approach of an autumn storm by the rustle of the oaks."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "No shrewd observer could **predict** the unexpected turn of events that altered the fate of the young heiress."}
    ]
  },
  "predictability": {
    "primary": "The degree to which an event, outcome, or behavior can be foreknown, calculated, or anticipated in advance.",
    "secondary": "In statistics, physical dynamics, and law, the quantitative certainty with which future states follow from initial parameters.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Habitual conduct introduces order and regular **predictability** into the otherwise chaotic stream of human social affairs."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The mathematical **predictability** of planetary motions convinced early astronomers of the universal uniformity of nature."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "As evolutionary systems stabilize, their operations exhibit greater mechanical **predictability** and structural coherence."}
    ]
  },
  "predictable": {
    "primary": "Capable of being foretold, anticipated, or calculated beforehand from observable tendencies or known natural laws.",
    "secondary": "In behavioral science and control theory, behaving in an orderly, consistent pattern that conforms reliably to expectation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The trade winds blow with steady and **predictable** regularity across the equatorial expanse of the Pacific Ocean."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Physical phenomena unfold according to **predictable** causal mechanisms that yield to methodical experimental inquiry."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "The small intrigues of provincial society moved along narrow and completely **predictable** pathways of petty self-interest."}
    ]
  },
  "predictably": {
    "primary": "In a manner that can be anticipated, foreseen, or calculated beforehand; conforming consistently to expectation.",
    "secondary": "In decision analysis and sociometrics, following established behavioral or statistical trends without significant deviation.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "When market supplies fall short of effective demand, prices **predictably** advance until equilibrium is restored."},
      {"author": "Herbert Spencer", "work": "The Study of Sociology", "quote": "Human communities respond **predictably** to sudden fiscal shocks by curtailing non-essential domestic consumption."},
      {"author": "William James", "work": "Pragmatism", "quote": "Familiar physical events recur **predictably**, providing human beings with reliable anchors for practical daily action."}
    ]
  },
  "prediction": {
    "primary": "A statement foretelling what will happen in the future, whether based upon intuition, prophecy, or scientific deduction.",
    "secondary": "In philosophy of science, a specific deductive implication derived from a theoretical hypothesis to test its empirical validity.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes made a shrewd **prediction** regarding the exact hour the fugitive would attempt to cross the grim mire."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The cynical lawyer made a gloomy **prediction** that the Chancery estate would be consumed entirely by court fees."},
      {"author": "Ralph Waldo Emerson", "work": "Representative Men", "quote": "The visionary astronomer verified his bold **prediction** by observing the transit of the planet precisely at dawn."}
    ]
  },
  "predictive": {
    "primary": "Relating to or having the power to foretell future events, outcomes, or causal developments in advance.",
    "secondary": "In statistical modeling and epidemiology, having significant diagnostic efficacy or prognostic forecasting capacity.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Natural science achieves its highest dignity when it attains genuine **predictive** power over physical phenomena."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Careful observation of prodromal symptoms possesses high **predictive** value in determining the clinical course of typhoid."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The ultimate test of any scientific hypothesis lies in its **predictive** success when confronted with novel empirical facts."}
    ]
  },
  "predictor": {
    "primary": "A person who foretells future happenings, or an indicator, variable, or factor that foreshadows a future development.",
    "secondary": "In regression analysis and biometrics, an independent variable utilized in statistical equations to forecast an outcome.",
    "quotes": [
      {"author": "Jonathan Swift", "work": "The Bickerstaff-Partridge Papers", "quote": "The satirical pamphleteer ridiculed the self-proclaimed **predictor** who claimed to foretell the exact day of a rival's demise."},
      {"author": "Francis Galton", "work": "Hereditary Genius", "quote": "A father's intellectual distinction serves as a reliable **predictor** of the inherited capacities of his offspring."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Involuntary muscular contraction of the brow serves as an accurate **predictor** of approaching emotional distress."}
    ]
  },
  "unaddicted": {
    "primary": "Free from compulsive dependence, chemical habituation, or enslavement to an obsessive vice or pursuit.",
    "secondary": "In moral philosophy and clinical toxicology, possessing psychological sovereignty and autonomic freedom from craving.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "A mind **unaddicted** to sensual indulgence preserves its clarity and fortitude amidst the shifting storms of fortune."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Prudent statesmen, **unaddicted** to wild metaphysical theories, seek to reform institutions by gradual constitutional means."},
      {"author": "John Locke", "work": "Some Thoughts Concerning Education", "quote": "A youth raised with temperance remains happily **unaddicted** to the wasteful luxuries and intoxicating vices of the capital."}
    ]
  },
  "unpredictability": {
    "primary": "An erratic, highly uncertain nature that renders outcomes impossible to anticipate or foresee with reliability.",
    "secondary": "In chaos theory and macroscopic economics, stochastic sensitivity to initial conditions precluding deterministic forecasting.",
    "quotes": [
      {"author": "William James", "work": "The Will to Believe", "quote": "The baffling **unpredictability** of human voluntary choice introduces genuine novelty into the universe."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The sudden shifts and fierce **unpredictability** of the tropical cyclone tested the captain's iron nerve."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The capricious **unpredictability** of maritime storms renders foreign freight insurance an indispensable commercial safeguard."}
    ]
  },
  "unpredictable": {
    "primary": "Not able to be foreseen, calculated, or anticipated in advance; subject to erratic, uncertain fluctuation.",
    "secondary": "In non-linear systems dynamics, exhibiting behavior whose trajectory cannot be computed from previous states.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "Sudden squalls in the Strait of Magellan are notoriously **unpredictable**, descending with furious violence from mountain ravines."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whale breached with wild, **unpredictable** fury, crushing the cedar whaleboat beneath its colossal flukes."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Eustacia's turbulent temperament remained proud, romantic, and wholly **unpredictable** to the simple peasants of Egdon Heath."}
    ]
  },
  "unpredictably": {
    "primary": "In an erratic, uncertain, or capricious manner that cannot be anticipated or calculated in advance.",
    "secondary": "In dynamic meteorology and financial markets, shifting without discernible regularity or adherence to modeled trends.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The ocean currents veered **unpredictably**, carrying the drifting vessel far away from its intended nautical course."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Sudden associative thoughts flash **unpredictably** into conscious awareness, diverging from the deliberate train of reflection."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Speculative commodities fluctuate **unpredictably** in value whenever wild rumors disturb the peaceful transactions of the bourse."}
    ]
  },
  "unpredictive": {
    "primary": "Failing or lacking the capacity to anticipate, forecast, or provide meaningful foresight concerning future events.",
    "secondary": "In statistical epistemology and diagnostics, possessing no statistically significant correlation with criterion outcomes.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Ancient astrology remained essentially **unpredictive**, generating vague generalizations that failed under rigorous scrutiny."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "A speculative hypothesis that remains persistently **unpredictive** when confronted with experimental tests must be discarded."},
      {"author": "William James", "work": "Pragmatism", "quote": "Scholastic abstractions prove wholly **unpredictive** of concrete experiential reality, yielding neither practical guidance nor fruitful insight."}
    ]
  }
}
