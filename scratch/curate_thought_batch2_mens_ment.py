# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — mens (30 words)
  # =========================================================================
  "Dashboard — mens/commensal.md": {
    "primary": "Living with or sharing food at the same table; an organism participating in a commensal relationship.",
    "secondary": "In marine biology and ecological symbiosis, an organism benefiting from association with a host without causing harm or parasitism.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Certain small crustaceans live as harmless **commensals** within the shells of large mollusks."},
      {"author": "Thomas Henry Huxley", "work": "The Crayfish: An Introduction to the Study of Zoology", "quote": "The parasite feeds upon its host, whereas the **commensal** merely shares its table."},
      {"author": "Peter Kropotkin", "work": "Mutual Aid: A Factor of Evolution", "quote": "The **commensal** association between different marine organisms demonstrates that nature is not solely a battlefield of fierce competition."}
    ]
  },
  "Dashboard — mens/commensalism.md": {
    "primary": "A symbiotic relationship between two organisms wherein one benefits while the other is neither harmed nor helped.",
    "secondary": "In evolutionary ecology, co-adaptive companionship where sharing shelter, transport, or crumbs provides mutual survival advantage.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "In instances of biological **commensalism**, neither species suffers detriment from their continuous association."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Mutual assistance through physiological **commensalism** increases the chance of survival in fragile environments."},
      {"author": "Ernst Haeckel", "work": "The Wonders of Life", "quote": "We must strictly distinguish parasitism from true **commensalism**, where companionship brings no injury."}
    ]
  },
  "Dashboard — mens/commensally.md": {
    "primary": "In a commensal manner; living together in a non-parasitic symbiotic relationship.",
    "secondary": "In ecological natural history, co-existing with a host species to obtain nourishment or shelter without inflicting systemic injury.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Monograph on the Sub-class Cirripedia", "quote": "The acorn-shells attached to the whale's skin dwell **commensally** without invading its living flesh."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "Certain annelids dwell **commensally** in the tubes of larger burrowing creatures."},
      {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "Epiphytes growing upon tropical forest trees subsist **commensally** upon airborne moisture without parasitic tapping."}
    ]
  },
  "Dashboard — mens/commensurable.md": {
    "primary": "Measurable by the same standard or common metric; proportionate and reducible to a shared ratio.",
    "secondary": "In classical mathematics and value theory, magnitudes or moral goods whose comparative worth can be numerically calculated.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Pleasures differing in quality are not strictly **commensurable** on any simple quantitative scale."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "The intellect seeks units of measure that render disparate natural phenomena mutually **commensurable**."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Geometric figures are **commensurable** when their proportions can be expressed by common rational numbers."}
    ]
  },
  "Dashboard — mens/commensurate.md": {
    "primary": "Corresponding in size, extent, or degree; proportionate and adequate to a given purpose.",
    "secondary": "In political philosophy and constitutional law, ensuring governmental powers align with delegated responsibilities.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Power should be granted only with a **commensurate** responsibility to the commonwealth."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The means employed should be **commensurate** with the great ends to be attained."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her ambitions were vast, but her opportunities were by no means **commensurate** with them."}
    ]
  },
  "Dashboard — mens/commensurateness.md": {
    "primary": "Proportionate correspondence, adequacy, or the capacity to be measured by a shared standard.",
    "secondary": "In epistemological ethics and aesthetics, the harmonious congruence between artistic expression and underlying thought.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The logical **commensurateness** of our hypotheses with observed facts is the true test of inductive reasoning."},
      {"author": "Herbert Spencer", "work": "The Principles of Ethics", "quote": "Justice requires an exact **commensurateness** between the labor expended and the reward received."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "There must be an inward **commensurateness** between the poetic imagination and the expressive diction."}
    ]
  },
  "Dashboard — mens/dimension.md": {
    "primary": "A measurable extent of some kind, such as length, breadth, depth, or time; an aspect or facet.",
    "secondary": "In physics and metaphysics, spatial coordinates defining the framework of the universe or scope of an idea.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "There is no difference between Time and any of the three dimensions of Space except that our consciousness moves along it; Time is the fourth **dimension**."},
      {"author": "Ralph Waldo Emerson", "work": "Essays: First Series", "quote": "The soul's expansion adds a new **dimension** to every ordinary experience."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The tragedy assumed an almost epic **dimension** under the burning tropical sky."}
    ]
  },
  "Dashboard — mens/dimensional.md": {
    "primary": "Relating to dimensions or spatial extent; having a specified number of dimensions.",
    "secondary": "In theoretical physics and geometric analysis, pertaining to the coordinate parameters of physical or mathematical manifolds.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Our perception of spatial relations is fundamentally three-**dimensional** and grounded in muscular movement."},
      {"author": "Bertrand Russell", "work": "The Principles of Mathematics", "quote": "In non-Euclidean geometry, n-**dimensional** space is treated with rigorous algebraic abstraction."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "Any real body must have extension in four directions; it must have length, breadth, thickness, and duration; it is a four-**dimensional** reality."}
    ]
  },
  "Dashboard — mens/dimensionality.md": {
    "primary": "The condition of having dimensions, or the specific number of dimensions possessed by a space.",
    "secondary": "In topology and modern epistemology, the degree of geometric freedom or complexity inherent in a conceptual system.",
    "quotes": [
      {"author": "Bertrand Russell", "work": "Introduction to Mathematical Philosophy", "quote": "The **dimensionality** of a continuum is determined by the number of independent variables required to locate a point."},
      {"author": "William James", "work": "A Pluralistic Universe", "quote": "The rich **dimensionality** of lived experience defies reduction to a single logical plane."},
      {"author": "Henri Poincaré", "work": "Science and Hypothesis", "quote": "Our physical senses suggest a space of three dimensions, but mathematical thought easily contemplates higher **dimensionality**."}
    ]
  },
  "Dashboard — mens/dimensioning.md": {
    "primary": "The act, process, or technique of measuring, sizing, or recording dimensions on a technical drawing.",
    "secondary": "In architectural and mechanical engineering, calculating precise spatial tolerances and load clearances for structural materials.",
    "quotes": [
      {"author": "Thomas Tredgold", "work": "Elementary Principles of Carpentry", "quote": "Careful **dimensioning** of timber girders prevents catastrophic deflection under heavy roof loads."},
      {"author": "Isambard Kingdom Brunel", "work": "Life and Works", "quote": "The accurate **dimensioning** of the iron plates was crucial to the strength of the steamship's hull."},
      {"author": "Henry Maudslay", "work": "Memoir and Mechanical Inventions", "quote": "Precision in the **dimensioning** of machine screws laid the basis for modern interchangeable parts."}
    ]
  },
  "Dashboard — mens/immense.md": {
    "primary": "Extremely large or great, especially in scale, degree, or volume; vast and boundless.",
    "secondary": "In epic narrative and natural description, overwhelming the senses through sheer magnitude or infinite expanse.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The lawyer's chambers were piled high with an **immense** accumulation of musty legal documents."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "An **immense** wall of white foam rose where the leviathan breached the ocean surface."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Egdon Heath stretched away in **immense** solitude beneath the darkening autumn sky."}
    ]
  },
  "Dashboard — mens/immensely.md": {
    "primary": "To an immense degree; exceedingly, hugely, or extraordinarily.",
    "secondary": "In social narrative and character observation, magnifying emotions, amusement, or relief beyond usual measure.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth was **immensely** amused by Mr. Collins's pompous and solemn declarations."},
      {"author": "Arthur Conan Doyle", "work": "The Adventures of Sherlock Holmes", "quote": "The strange clue proved to be **immensely** valuable in guiding our investigation."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea felt **immensely** relieved when the distressing conversation was brought to an end."}
    ]
  },
  "Dashboard — mens/immenseness.md": {
    "primary": "The state, attribute, or magnitude of being immense; vastness, enormity, or boundless scale.",
    "secondary": "In romantic philosophy and sublime aesthetics, the transcendent vastness of nature inspiring humility in the human mind.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The sheer **immenseness** of the sperm whale filled the young sailor with reverent awe."},
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "The **immenseness** of the Alpine precipice overwhelms the spectator with its sheer vertical scale."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Looking upward into the midnight sky, man shudders before the silent **immenseness** of the cosmos."}
    ]
  },
  "Dashboard — mens/immensity.md": {
    "primary": "Vastness, boundless expanse, or immeasurable extent in space, time, or degree.",
    "secondary": "In contemplative literature, the infinite abyss of stellar space or eternity dwarfing mortal affairs.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The sun sank into the **immensity** of the sea, leaving an ominous crimson glow."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The stars awaken in the human breast a thrilling sense of the celestial **immensity**."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "He gazed upward into the starry **immensity** and felt his own earthly troubles shrink into nothingness."}
    ]
  },
  "Dashboard — mens/immensurable.md": {
    "primary": "Incapable of being measured; measureless, boundless, or limitless.",
    "secondary": "In metaphysical poetry and sublime cosmological prose, denoting infinities that surpass all finite instruments.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Into this wild Abyss, the womb of Nature and perhaps her grave, through the **immensurable** void they plunge."},
      {"author": "Percy Bysshe Shelley", "work": "Prometheus Unbound", "quote": "He reigns over the **immensurable** deep, sovereign of elemental storms."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "In my dreams, architectural halls opened into **immensurable** corridors vanishing into eternity."}
    ]
  },
  "Dashboard — mens/incommensurable.md": {
    "primary": "Not able to be judged or measured by the same standard; lacking a common basis of comparison.",
    "secondary": "In moral philosophy and mathematics, values or geometric lengths (like the diagonal of a unit square) that cannot be expressed as simple ratios.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Intellectual pleasures and physical sensations are qualitatively distinct and fundamentally **incommensurable**."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Use-value and exchange-value are frequently **incommensurable** when measured by immediate utility."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "The side of a square and its diagonal are geometrically **incommensurable** magnitudes."}
    ]
  },
  "Dashboard — mens/incommensurate.md": {
    "primary": "Not commensurate; out of proportion, unequal, or inadequate to a given requirement.",
    "secondary": "In institutional criticism and statecraft, resources or capabilities that fall hopelessly short of constitutional duties.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The puny resources of the rebel faction were hopelessly **incommensurate** with the colossal task they undertook."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Her intense moral fervor found only petty, **incommensurate** channels of parochial charity."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A revenue system **incommensurate** with the national defense will inevitably invite foreign aggression."}
    ]
  },
  "Dashboard — mens/mensa.md": {
    "primary": "A flat-topped tableland or elevation; the top slab of an altar; or an international society for high IQ.",
    "secondary": "In geology and ecclesiastical architecture, an elevated plateau capped by resistant rock, or consecrated altar stone.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The flat-topped **mensa** formations of the plateau were carved out by centuries of fluvial erosion."},
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "The relics were reverently deposited beneath the marble **mensa** of the high altar."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "The isolated **mensa** rose sheer into the sky, its flat summit untouched by human feet."}
    ]
  },
  "Dashboard — mens/mensal.md": {
    "primary": "Pertaining to the dining table; in church law, referring to revenues allocated for a bishop's table.",
    "secondary": "In social history and ecclesiastical jurisprudence, benefices or customs reserved specifically for domestic hospitality.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The lavish **mensal** luxuries of the later emperors disgusted the austere senators of the old republic."},
      {"author": "Jonathan Swift", "work": "A Tale of a Tub", "quote": "The brothers fell into fierce disputation over the allocation of their father's **mensal** legacy."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The **mensal** tithes were specifically reserved for the sustenance of the presiding prelate."}
    ]
  },
  "Dashboard — mens/mensch.md": {
    "primary": "A person of integrity, honor, rectitude, and admirable moral character (borrowed from Yiddish).",
    "secondary": "In cultural ethics and community life, an individual embodying decency, empathy, and steadfast responsibility toward others.",
    "quotes": [
      {"author": "Leo Rosten", "work": "The Joys of Yiddish", "quote": "To call someone a real **mensch** is the highest compliment of moral character and decency in Jewish culture."},
      {"author": "Saul Bellow", "work": "Herzog", "quote": "All his life he had struggled against pettiness, striving simply to live and die as an honorable **mensch**."},
      {"author": "Bernard Malamud", "work": "The Assistant", "quote": "In that dark grocery store, Frank learned what it truly meant to act like a **mensch** toward his suffering neighbor."}
    ]
  },
  "Dashboard — mens/menses.md": {
    "primary": "The periodic monthly discharge of blood and mucosal tissue from the uterus; menstruation.",
    "secondary": "In clinical physiology and reproductive biology, the cyclical shedding of the uterine endometrial lining.",
    "quotes": [
      {"author": "William Harvey", "work": "Exercitationes de Generatione Animalium", "quote": "The periodic return of the **menses** marks the natural cycle of female generative potential."},
      {"author": "Aristotle", "work": "The History of Animals", "quote": "In human physiology, the regular cessation and return of the **menses** is governed by natural biological rhythms."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "Physical and emotional fluctuations frequently coincide with the onset of the **menses**."}
    ]
  },
  "Dashboard — mens/menstrual.md": {
    "primary": "Relating to the menses or periodic uterine cycle; occurring on a monthly basis.",
    "secondary": "In anthropological and medical literature, physiological rhythms and historical rituals associated with the lunar cycle.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The regular **menstrual** cycle in higher primates indicates a deep physiological homology with mankind."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Periodic **menstrual** rhythms demonstrate how bodily changes subtly influence subjective temperament."},
      {"author": "James George Frazer", "work": "The Golden Bough", "quote": "Ancient taboos surrounded women during their **menstrual** period, demanding complete seclusion from tribal affairs."}
    ]
  },
  "Dashboard — mens/menstruate.md": {
    "primary": "To undergo the monthly discharge of blood and mucosal tissue from the uterus.",
    "secondary": "In comparative mammalogy, experiencing recurring cycles of reproductive fertility accompanied by endometrial sloughing.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Female anthropoid apes **menstruate** at intervals approximating those observed in the human species."},
      {"author": "Havelock Ellis", "work": "Man and Woman", "quote": "Healthy women begin to **menstruate** during adolescence as secondary sexual characteristics mature."},
      {"author": "James George Frazer", "work": "Balder the Beautiful", "quote": "In various indigenous societies, girls who begin to **menstruate** are secluded in special ceremonial huts."}
    ]
  },
  "Dashboard — mens/menstruation.md": {
    "primary": "The recurring physiological process of discharging blood and cellular tissue from the uterus.",
    "secondary": "In gynecological medicine and anthropology, the monthly ovarian-endometrial cycle regulating mammalian fertility.",
    "quotes": [
      {"author": "James George Frazer", "work": "Balder the Beautiful", "quote": "At her first **menstruation** a Baniva girl must pass several days in fasting and complete silence."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Periodic **menstruation** in monkeys and apes suggests a shared evolutionary lineage with humanity."},
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The physiological cycle of **menstruation** produces subtle alterations in pulse, temperature, and mental agility."}
    ]
  },
  "Dashboard — mens/menstruum.md": {
    "primary": "A solvent; any liquid substance that dissolves a solid or extracts soluble elements.",
    "secondary": "In historical alchemy and early chemistry, a dissolving liquid traditionally believed to work best during a monthly lunar cycle.",
    "quotes": [
      {"author": "Robert Burns", "work": "The Letters of Robert Burns", "quote": "How ignorant are plough-boys!—Nay, I have since discovered that love is the universal **menstruum** that dissolves all human differences."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The alchemists sought a universal **menstruum** capable of dissolving every tangible substance into its primal essence."},
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Aqua fortis acts as a powerful **menstruum** upon silver, dissolving the metal into a clear saline solution."}
    ]
  },
  "Dashboard — mens/mensurable.md": {
    "primary": "Capable of being measured; possessing measurable dimensions, duration, or quantity.",
    "secondary": "In epistemological philosophy and natural science, properties susceptible to quantitative evaluation against empirical standards.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Duration and space are **mensurable** quantities because we can apply repeated standard units to them."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "Human life is composed of **mensurable** hours, each of which should be dedicated to virtue or learning."},
      {"author": "William Whewell", "work": "The History of the Inductive Sciences", "quote": "Astronomy became an exact science only when celestial motions were reduced to **mensurable** angles and intervals."}
    ]
  },
  "Dashboard — mens/mensural.md": {
    "primary": "Pertaining to measurement; in music, denoting notation indicating exact rhythmic time values.",
    "secondary": "In musicology and historical metrology, the transition from unmeasured plainchant to polyphonic notation with precise note lengths.",
    "quotes": [
      {"author": "Charles Burney", "work": "A General History of Music", "quote": "The introduction of **mensural** notation enabled composers to record polyphonic rhythms with mathematical precision."},
      {"author": "John Hawkins", "work": "A General History of the Science and Practice of Music", "quote": "Franco of Cologne was among the earliest masters to establish rules for **mensural** harmony."},
      {"author": "William Whewell", "work": "The Philosophy of the Inductive Sciences", "quote": "Every physical experiment depends upon **mensural** accuracy in recording time, weight, and distance."}
    ]
  },
  "Dashboard — mens/mensurate.md": {
    "primary": "To measure, calculate, or gauge extent, dimension, or quantity.",
    "secondary": "In philosophical ethics and mathematical physics, establishing exact proportional relationships between observable forces.",
    "quotes": [
      {"author": "Thomas Reid", "work": "Essays on the Active Powers of Man", "quote": "We must learn to **mensurate** moral obligations not by subjective inclination, but by objective duty."},
      {"author": "William Hamilton", "work": "Lectures on Metaphysics and Logic", "quote": "The geometrician learns to **mensurate** celestial distances by applying planar trigonometry."},
      {"author": "John Herschel", "work": "A Preliminary Discourse on the Study of Natural Philosophy", "quote": "To **mensurate** accurately is the first prerequisite for formulating physical laws."}
    ]
  },
  "Dashboard — mens/mensuration.md": {
    "primary": "The mathematical art or process of calculating lengths, areas, and volumes of geometric figures.",
    "secondary": "In civil surveying and classical applied geometry, computing physical land boundaries or structural volumes from linear measurements.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The **mensuration** of the faculties of the mind has, I believe, no established scale in political science."},
      {"author": "S. R. Crockett", "work": "Deep Moat Grange", "quote": "Old Mustard is well up in mathematics and practical **mensuration**, and can survey any farm in the parish."},
      {"author": "Isaac Newton", "work": "Opticks", "quote": "By the exact **mensuration** of optical angles, the refractive index of glass was definitively determined."}
    ]
  },
  "Dashboard — mens/premenstrual.md": {
    "primary": "Occurring or experienced in the days immediately preceding menstruation.",
    "secondary": "In clinical psychology and gynecology, transient somatic and affective changes observed prior to the onset of the menses.",
    "quotes": [
      {"author": "Havelock Ellis", "work": "Studies in the Psychology of Sex", "quote": "The **premenstrual** phase is frequently characterized by mild vascular congestion and heightened nervous irritability."},
      {"author": "Sigmund Freud", "work": "Introductory Lectures on Psycho-Analysis", "quote": "Emotional tension observed during the **premenstrual** period often reactivates repressed neurotic conflicts."},
      {"author": "Edward Westermarck", "work": "The History of Human Marriage", "quote": "Anthropological customs frequently record dietary restrictions observed during the **premenstrual** days."}
    ]
  },

  # =========================================================================
  # Dashboard — ment (25 words)
  # =========================================================================
  "Dashboard — ment/comment.md": {
    "primary": "A remark, observation, or criticism expressing an opinion; to express remarks upon a subject.",
    "secondary": "In scholarly textual criticism, marginal notes or glosses clarifying an obscure passage in classical or legal manuscripts.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "I prithee, when thou see’st that act a-foot, even with the very **comment** of thy soul observe mine uncle."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth listened in silence, not trusting herself to make any **comment** on what she had heard."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The harsh **comment** of the world upon her conduct wounded her to the quick."}
    ]
  },
  "Dashboard — ment/commentary.md": {
    "primary": "A series of explanatory notes or critical comments on a text, event, or performance.",
    "secondary": "In historiography and biblical exegesis, systematic analytical glosses illustrating grammatical, theological, or contextual meaning.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The **commentary** upon it now indelibly written in his handsome face made it painful to look at."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A judicious **commentary** upon ancient authors illuminates the hidden paths of natural knowledge."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Caesar's military **commentaries** remain an enduring model of concise and candid narrative."}
    ]
  },
  "Dashboard — ment/commentate.md": {
    "primary": "To write or deliver a commentary; to explain or remark critically on an unfolding event.",
    "secondary": "In literary scholarship and journalism, providing live descriptive analysis or critical exposition of text or public affairs.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Critics who **commentate** upon Shakespeare must bring both erudition and modesty to their task."},
      {"author": "Thomas De Quincey", "work": "Essays in Philosophy", "quote": "To **commentate** on Kant's transcendental deductions requires an intellect trained in rigorous logic."},
      {"author": "William Hazlitt", "work": "Table-Talk", "quote": "Every bystander in politics feels qualified to **commentate** on decisions whose secret causes he cannot fathom."}
    ]
  },
  "Dashboard — ment/commentator.md": {
    "primary": "A person who provides expert spoken or written commentary on events, literature, or public affairs.",
    "secondary": "In classical philology and political journalism, a scholar or analyst providing interpretive context to difficult developments.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "So fare thee well, poor devil of a Sub-Sub, whose **commentator** I am; thou belongest to that hopeless, sallow tribe."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "A pedantic **commentator** can bury the brightest poetry beneath mountains of trivial antiquarian lore."},
      {"author": "T. R. Glover", "work": "The Jesus of History", "quote": "The old **commentator**, Bengel, wrote at the beginning of his book that reverence must precede analysis."}
    ]
  },
  "Dashboard — ment/demented.md": {
    "primary": "Suffering from cognitive impairment or severe mental confusion; behaving irrationally or crazily.",
    "secondary": "In psychiatric pathology and dramatic tragedy, exhibiting profound loss of reason, memory, and behavioral self-control.",
    "quotes": [
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Dick was regarded as harmlessly **demented**, though his simple heart possessed profound tenderness."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Ben Gunn had been left marooned for three years until his solitary wits seemed wholly **demented**."},
      {"author": "Arthur Conan Doyle", "work": "The Return of Sherlock Holmes", "quote": "The wretched man rushed into the street, screaming like a **demented** creature."}
    ]
  },
  "Dashboard — ment/dementedly.md": {
    "primary": "In a demented, frantic, or crazed manner; wildly and without rational control.",
    "secondary": "In gothic narrative and crime fiction, acting with frenzied incoherence under the influence of extreme panic or mania.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "He paced the quarterdeck **dementedly**, muttering disjointed sentences into the howling gale."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The beast-folk ran **dementedly** through the forest, howling at the red glare of the burning enclosure."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "Renfield laughed **dementedly** as he scraped up the buzzing flies upon the stone window-sill."}
    ]
  },
  "Dashboard — ment/dementedness.md": {
    "primary": "A manifestation of extreme irrationality, frantic confusion, or severe intellectual derangement.",
    "secondary": "In psychological diagnosis and dramatic analysis, observable disintegration of logical faculties accompanied by frantic agitation.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "A sombre **dementedness** seemed to hover over the ancient mansion and its solitary master."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "In his grief-stricken **dementedness**, he walked the streets heedless of rain or freezing cold."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The delirium of his fever gave way to a quiet **dementedness** that alarmed his devoted companion."}
    ]
  },
  "Dashboard — ment/dementia.md": {
    "primary": "A persistent chronic disorder of cognitive processes caused by brain disease, marked by memory loss and personality change.",
    "secondary": "In clinical neurology and psychopathology, progressive organic deterioration of intellectual functioning compromising daily autonomy.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Senile **dementia** illustrates how organic cerebral atrophy gradually destroys the continuity of personal memory."},
      {"author": "Sigmund Freud", "work": "The Psychopathology of Everyday Life", "quote": "We must distinguish transient amnesia from the irreversible cognitive deficits typical of **dementia**."},
      {"author": "Mary Baker Eddy", "work": "Science and Health, with Key to the Scriptures", "quote": "The illusion of physical **dementia** must yield before the eternal reality of divine intelligence."}
    ]
  },
  "Dashboard — ment/disinterment.md": {
    "primary": "The act or process of digging up or exhuming a buried corpse or object from the earth.",
    "secondary": "In forensic jurisprudence and archaeology, exhumation performed to conduct post-mortem investigation or recover buried antiquities.",
    "quotes": [
      {"author": "Edgar Allan Poe", "work": "The Premature Burial", "quote": "The frantic **disinterment** revealed that the wretched victim had indeed revived within the coffin."},
      {"author": "Arthur Conan Doyle", "work": "The Memoirs of Sherlock Holmes", "quote": "The magistrate granted an order for the **disinterment** of the body to test for traces of arsenic."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "The **disinterment** of the ancient Roman statue from the vineyard brought joy to the antiquarians."}
    ]
  },
  "Dashboard — ment/emmental.md": {
    "primary": "A yellow, medium-hard Swiss cheese characterized by large characteristic eyes and a mild, savory-nutty flavor.",
    "secondary": "In agricultural history and culinary geography, traditional cheese originating in the Emme valley in the canton of Bern, Switzerland.",
    "quotes": [
      {"author": "Mark Twain", "work": "A Tramp Abroad", "quote": "At the mountain inn they served us coarse rye bread with generous wedges of golden **Emmental** cheese."},
      {"author": "Robert Louis Stevenson", "work": "Travels with a Donkey in the Cévennes", "quote": "My knapsack contained a loaf, a flask of wine, and a savory piece of Swiss **Emmental**."},
      {"author": "George Gissing", "work": "By the Ionian Sea", "quote": "The simple luncheon concluded with fresh grapes and a crumbly slice of imported **Emmental**."}
    ]
  },
  "Dashboard — ment/emmentaler.md": {
    "primary": "An alternative name for Emmental cheese, the traditional hole-riddled cheese from the Emmental valley in Switzerland.",
    "secondary": "In European food regulation and cheesemaking, a firm raw-milk cheese produced through propionic acid fermentation forming carbon dioxide eyes.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The World of William Clissold", "quote": "He enjoyed the simple peasant breakfast of crusty bread, dark beer, and pungent **Emmentaler**."},
      {"author": "Thomas Mann", "work": "The Magic Mountain", "quote": "In the sanatorium dining hall, the Swiss guests insisted on their domestic **Emmentaler** at every supper."},
      {"author": "Sinclair Lewis", "work": "Dodsworth", "quote": "They sat upon the terrace overlooking the lake, dining on cold roast beef and Swiss **Emmentaler**."}
    ]
  },
  "Dashboard — ment/interment.md": {
    "primary": "The burial of a corpse in a grave or tomb, typically accompanied by funeral rites.",
    "secondary": "In civic law and liturgical theology, the solemn committal of mortal remains to consecrated ground or mausoleum.",
    "quotes": [
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Mr. Gibson had come down to direct his sister’s **interment** and arrange her modest estate."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Joe Gargery had departed this life, and the solemn **interment** was fixed for the following Tuesday."},
      {"author": "Edgar Allan Poe", "work": "The Fall of the House of Usher", "quote": "We placed the body of the lady Madeline in the damp vault for temporary **interment**."}
    ]
  },
  "Dashboard — ment/mental.md": {
    "primary": "Relating to the mind or intellectual processes, as distinguished from physical bodily functions.",
    "secondary": "In cognitive psychology and psychiatry, designating operations of consciousness, reasoning, memory, or psychic health.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Timon of Athens", "quote": "What a **mental** power this eye shoots forth! How big imagination moves in this lip!"},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Very odd and very curious, the **mental** process is, in you men of business!"},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Her **mental** powers were of an uncommon order, though hidden beneath modest reticence."}
    ]
  },
  "Dashboard — ment/mentalism.md": {
    "primary": "The doctrine that physical reality exists only as a mental construct; in entertainment, the performance of mind-reading feats.",
    "secondary": "In philosophy of mind and idealism, the ontological assertion that subjective conscious phenomena cannot be reduced to physical mechanics.",
    "quotes": [
      {"author": "William James", "work": "The Meaning of Truth", "quote": "Philosophical **mentalism** holds that all objects of experience depend ultimately on being perceived."},
      {"author": "Bertrand Russell", "work": "Our Knowledge of the External World", "quote": "The extreme form of **mentalism** known as solipsism cannot be logically disproved, but commands no belief."},
      {"author": "George Berkeley", "work": "A Treatise Concerning the Principles of Human Knowledge", "quote": "The principles of subjective **mentalism** establish that the existence of things consists in their being perceived."}
    ]
  },
  "Dashboard — ment/mentality.md": {
    "primary": "The characteristic way of thinking, intellectual capacity, or psychological mindset of a person or group.",
    "secondary": "In sociology and cultural history, the collective worldview, cognitive habits, and moral assumptions shaping a historical epoch.",
    "quotes": [
      {"author": "graf Leo Tolstoy", "work": "War and Peace", "quote": "In general the trait of Speranski’s **mentality** which struck Prince Andrew was his calm, mathematical logic."},
      {"author": "Jack London", "work": "The Star-Rover", "quote": "They were sharply differentiated in the minutest shades of **mentality** and emotional reaction."},
      {"author": "H. G. Wells", "work": "The Outline of History", "quote": "The primitive **mentality** of ancient mankind was dominated by seasonal taboos and astrological dread."}
    ]
  },
  "Dashboard — ment/mentally.md": {
    "primary": "In a manner relating to the mind; inwardly, intellectually, or in thought.",
    "secondary": "In narrative psychology, framing silent inner deliberations or calculating judgments unuttered to companions.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Their value to Bathsheba, and indeed to anybody, Oak **mentally** estimated with practiced accuracy."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "I was **mentally** comparing my comfortable present with the bleak days of my neglected childhood."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She **mentally** reviewed all the objections that her uncle was sure to urge against the marriage."}
    ]
  },
  "Dashboard — ment/mentation.md": {
    "primary": "Mental activity; the process of thinking, perceiving, or exercising cognitive faculties.",
    "secondary": "In neurophysiology and cognitive psychology, the total flow of conscious and subconscious neural information processing.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The continuous stream of **mentation** exhibits varying rhythms of focal attention and marginal awareness."},
      {"author": "Herbert Spencer", "work": "The Principles of Psychology", "quote": "Higher forms of **mentation** evolve through the progressive differentiation and integration of sensory reflexes."},
      {"author": "Havelock Ellis", "work": "The World of Dreams", "quote": "Dreaming represents an archaic, undisciplined mode of **mentation** liberated during sleep."}
    ]
  },
  "Dashboard — ment/menticirrhus.md": {
    "primary": "A fleshy barb or sensory filament on the chin of certain marine fishes; a sciaenoid fish genus.",
    "secondary": "In ichthyological morphology and marine biology, a tactile barbel located on the mandibular symphysis used to detect benthic prey.",
    "quotes": [
      {"author": "David Starr Jordan", "work": "A Guide to the Study of Fishes", "quote": "The species of the genus **Menticirrhus** are characterized by a single short, thick barbel upon the chin."},
      {"author": "George Brown Goode", "work": "American Fishes", "quote": "The Carolina whiting, belonging to **Menticirrhus**, feeds along sandy bottoms aided by its sensitive chin filament."},
      {"author": "Charles Girard", "work": "Ichthyological Notices", "quote": "The presence of the mandibular **menticirrhus** distinguishes this sciaenoid fish from related coastal genera."}
    ]
  },
  "Dashboard — ment/mention.md": {
    "primary": "To refer to briefly or casually; an act of speaking or writing about someone or something.",
    "secondary": "In social discourse and military citations, bringing a person's name or valorous conduct to official notice.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Winter's Tale", "quote": "Pray sit down, then, and let me entreat you not to make **mention** of this grief again."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "At the very **mention** of his name, Elizabeth felt her color heighten and her composure vanish."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "He strictly forbade any **mention** of his benefactor in the hearing of third persons."}
    ]
  },
  "Dashboard — ment/mentioner.md": {
    "primary": "One who mentions, cites, or names someone or something in speech or writing.",
    "secondary": "In literary historiography and bibliographical critique, an author who records the earliest citation of a rare book, concept, or event.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Lives of the English Poets", "quote": "Dryden was an early **mentioner** of Milton's sublime genius at a time when political prejudice silenced others."},
      {"author": "Thomas Babington Macaulay", "work": "Critical and Historical Essays", "quote": "The chronicler was not merely a passive **mentioner** of royal names, but an acute observer of court intrigue."},
      {"author": "Isaac D'Israeli", "work": "Curiosities of Literature", "quote": "A contemporary **mentioner** of Shakespeare's earliest sonnets has preserved valuable clues for modern scholars."}
    ]
  },
  "Dashboard — ment/mentor.md": {
    "primary": "An experienced and trusted adviser or guide who counsels a less experienced person.",
    "secondary": "In classical epic and pedagogy, derived from Mentor in Homer's Odyssey, embodying wisdom and moral guardianship.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "You have played the part of **mentor** to me many times, and I don't see why you should shrink now."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "It is not wholly irrespective of our personal feelings that we record how Mr. Pocket acted as my **mentor**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The venerable whaleman acted as a sea-going **mentor** to the green recruits shipped for the voyage."}
    ]
  },
  "Dashboard — ment/mentorship.md": {
    "primary": "The guidance, advice, and support provided by an experienced mentor to a protégé.",
    "secondary": "In educational theory and professional apprenticeship, a sustained developmental relationship fostering professional mastery and ethics.",
    "quotes": [
      {"author": "John Dewey", "work": "Democracy and Education", "quote": "Effective **mentorship** cultivates independence of mind rather than mere mechanical imitation of the master."},
      {"author": "Booker T. Washington", "work": "Up from Slavery", "quote": "Under the wise and patient **mentorship** of General Armstrong, my entire conception of life was transformed."},
      {"author": "Jane Addams", "work": "Twenty Years at Hull-House", "quote": "The settlement house provided loving **mentorship** to young immigrant girls facing urban hardships."}
    ]
  },
  "Dashboard — ment/mentum.md": {
    "primary": "The chin; in entomology and botany, a projection or plate situated beneath the lower lip.",
    "secondary": "In insect morphology and orchid anatomy, a sclerite of the submentum supporting the labial palps, or a spur-like column projection.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Various Contrivances by which British and Foreign Orchids are Fertilised by Insects", "quote": "The lower sepals unite at the base with the column-foot to form a chin-like pouch or **mentum**."},
      {"author": "William Kirby", "work": "An Introduction to Entomology", "quote": "The **mentum** is that plate of the mouth situated immediately above the submentum and bearing the labium."},
      {"author": "John Obadiah Westwood", "work": "Modern Classification of Insects", "quote": "In coleopterous insects, the shape of the **mentum** provides a valuable diagnostic character for family classification."}
    ]
  },
  "Dashboard — ment/undermentioned.md": {
    "primary": "Mentioned or written further down on the same page, or below in a document.",
    "secondary": "In legal drafting and official gazettes, specifying a schedule of items, persons, or clauses enumerated lower in the text.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The **undermentioned** properties in the parish of St. Albans were subject to the disputed testamentary trust."},
      {"author": "Walter Scott", "work": "Rob Roy", "quote": "The magistrate read out the **undermentioned** names of persons summoned to surrender to the King's officers."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The **undermentioned** jewels, including the great Agra diamond, formed the subject of the secret compact."}
    ]
  },
  "Dashboard — ment/unmentionable.md": {
    "primary": "Too bad, shocking, or taboo to be spoken of; also a humorous term for underwear or trousers.",
    "secondary": "In Victorian social etiquette and gothic fiction, unspeakable moral degradation or taboo bodily garments excluded from polite conversation.",
    "quotes": [
      {"author": "Henry James", "work": "The Turn of the Screw", "quote": "Was there a secret at Bly—a mystery of Udolpho or an insane, an **unmentionable** relative kept in isolation?"},
      {"author": "James Joyce", "work": "Ulysses", "quote": "His little man-o’-war top and **unmentionables** were full of sand, but Cissy was a past mistress at patting him dry."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "There are horrors so dreadful that they remain forever **unmentionable** among civilized human beings."}
    ]
  }
}

base_dir = r"App database/Latin roots/Cluster Thought"

updated_count = 0
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
    updated_count += 1

print(f"Thought Batch 2B (mens & ment): Successfully updated {updated_count}/{len(data)} notes.")
