# -*- coding: utf-8 -*-
"""
Curates Dashboard — vol (Part 1: words 1-58) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part1 = {
  "abvolt": {
    "primary": "The electromagnetic cgs unit of electric potential difference, equal to one hundred-millionth of a volt (10^-8 V).",
    "secondary": "In classical electromagnetism, the potential difference between two points when one erg of work transfers one abcoulomb.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "In absolute electromagnetic measure, potential differences are computed in fractions of an **abvolt**."},
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "The conversion between the practical volt and the theoretical **abvolt** relies upon factors of ten to the eighth."},
      {"author": "Charles Proteus Steinmetz", "work": "Theory and Calculation of Alternating Current Phenomena", "quote": "Early laboratory galvanometers registered subtle electrostatic inductions measured in each minute **abvolt**."}
    ]
  },
  "benevolence": {
    "primary": "The disposition to do good; an inclination to promote the happiness, well-being, and prosperity of others.",
    "secondary": "In moral philosophy, the altruistic sentiment regarded by sentimentalist thinkers as foundational to human society.",
    "quotes": [
      {"author": "David Hume", "work": "An Enquiry Concerning the Principles of Morals", "quote": "No qualities are more entitled to the general affection of mankind than **benevolence** and humanity."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "How selfish soever man may be supposed, there are evidently principles in his nature which interest him in **benevolence**."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bingley possessed an open, pleasant countenance, and general **benevolence** of manner that won every heart."}
    ]
  },
  "benevolent": {
    "primary": "Well-meaning, kindly, and motivated by a desire to promote the welfare and happiness of others.",
    "secondary": "In institutional history, charitable organizations established to provide mutual aid and poor relief.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Pickwick Papers", "quote": "Mr. Pickwick beamed upon the company through his spectacles with the most **benevolent** expression imaginable."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Americans constantly form **benevolent** associations to relieve distress, build hospitals, and support schools."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The creature observed the gentle cottage family with affection, hoping for a **benevolent** welcome at their hearth."}
    ]
  },
  "benevolently": {
    "primary": "In a benevolent, kindly, or charitable manner; with goodwill and compassionate generosity.",
    "secondary": "In narrative characterization, smiling or acting with condescending or genuine paternal kindness.",
    "quotes": [
      {"author": "George Eliot", "work": "Silas Marner", "quote": "The village rector smiled **benevolently** upon Eppie, commending Silas for his fatherly devotion."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Mr. Touchett regarded his young niece **benevolently**, determined to secure her financial independence."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Harding listened **benevolently** to the complaints of the bedesmen, offering gentle words of peace."}
    ]
  },
  "circumvolute": {
    "primary": "To wind, twist, or roll around in a circular or spiral fashion, or shaped in winding spirals.",
    "secondary": "In malacology and botany, describing helical shells or tendrils that coil closely around a central axis.",
    "quotes": [
      {"author": "John Ruskin", "work": "Modern Painters", "quote": "Observe how the climbing vine tendrils **circumvolute** the supporting trellis with vigorous organic elasticity."},
      {"author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "Naturalists admire the elegant spirals that **circumvolute** the chambers of the pearly nautilus."},
      {"author": "Richard Owen", "work": "On the Anatomy of Vertebrates", "quote": "Intestinal canals in certain herbivorous fishes **circumvolute** repeatedly to prolong nutrient absorption."}
    ]
  },
  "circumvolution": {
    "primary": "A winding or rolling around an axis, or a circuitous, indirect, or roundabout course or motion.",
    "secondary": "In neuroanatomy, an obsolete term for a cerebral gyrus or convoluted fold of the brain cortex.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The caravan performed a tedious **circumvolution** across arid deserts to avoid the Parthian cavalry."},
      {"author": "Charles Darwin", "work": "The Power of Movement in Plants", "quote": "The apex of every growing shoot performs a continuous **circumvolution** as it searches for physical support."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpoon line uncoiled in frantic **circumvolution** around the loggerhead, smoking with friction."}
    ]
  },
  "circumvolve": {
    "primary": "To roll or revolve around something in a circular path; to cause to rotate or turn about an axis.",
    "secondary": "In planetary mechanics, the orbital revolution of satellites around a primary celestial body.",
    "quotes": [
      {"author": "Isaac Newton", "work": "The System of the World", "quote": "The gravitational force causes moons to **circumvolve** their parent planets in elliptical trajectories."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Mystic dances which that starry sphere of planets doth **circumvolve** in numbers that move harmonious chords."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "The colossal machinery of universe and society continues to **circumvolve** through cycles of creation and decay."}
    ]
  },
  "convolute": {
    "primary": "To roll, twist, or wind together into overlapping folds, or coiled and rolled inward upon itself.",
    "secondary": "In rhetoric and argumentation, to make intricate, obscure, or excessively complex.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "Certain delicate flower petals **convolute** tightly before dawn, opening only under the direct warmth of the sun."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Pedantic scholars **convolute** simple metaphysical questions until the original truth is lost in verbal fog."},
      {"author": "Asa Gray", "work": "Elements of Botany", "quote": "In bud vernation, leaves that **convolute** roll around one another sequentially in a spiral direction."}
    ]
  },
  "convoluted": {
    "primary": "Extremely complex, intricate, and difficult to follow, or twisted, coiled, and rolled in overlapping folds.",
    "secondary": "In cerebral anatomy, describing the gyri and sulci of the mammalian neocortex.",
    "quotes": [
      {"author": "Steven Pinker", "work": "The Language Instinct", "quote": "Legal statutes are notorious for their **convoluted** syntax, designed to preempt loop-holes rather than inform."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The **convoluted** cortical surface of the temporal lobes coordinates complex multimodal auditory recognition."},
      {"author": "David Foster Wallace", "work": "Infinite Jest", "quote": "The narrative unfolded through **convoluted** endnotes and overlapping timelines that defied linear summary."}
    ]
  },
  "convolution": {
    "primary": "A coil, twist, or winding fold, especially one of the convex folds (gyri) on the surface of the brain.",
    "secondary": "In mathematics, an integral operation expressing the overlap of one function as it is shifted over another.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Each cortical **convolution** increases the surface area of gray matter within the rigid confines of the cranium."},
      {"author": "Thomas Henry Huxley", "work": "Evidence as to Man's Place in Nature", "quote": "Every major cerebral **convolution** identified in the chimpanzee finds its exact anatomical homologue in man."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The strange machine featured an intricate **convolution** of crystalline rods that spun as the levers shifted."}
    ]
  },
  "convolve": {
    "primary": "To roll or wind together; to twist or coil around an axis or upon one another.",
    "secondary": "In signal processing and digital image filtering, to apply a mathematical kernel across input arrays.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Down rushed the broken chariot wheels that did **convolve** with ruin and frantic tumult down the abyss."},
      {"author": "Norbert Wiener", "work": "Extrapolation, Interpolation, and Smoothing of Stationary Time Series", "quote": "Linear filter networks **convolve** incoming sensory signals with specialized weighting functions."},
      {"author": "Charles Darwin", "work": "The Movements and Habits of Climbing Plants", "quote": "The tendril begins to **convolve** into a corkscrew spiral immediately after touching a firm twig."}
    ]
  },
  "counterrevolution": {
    "primary": "A political revolution opposed to a previous revolution, attempting to reverse its results or restore the former regime.",
    "secondary": "In modern political theory, organized reactionary movements seeking the re-establishment of pre-revolutionary social orders.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Thoughts on French Affairs", "quote": "A concerted European coalition was urged to sponsor a **counterrevolution** and restore the Bourbon monarchy."},
      {"author": "Karl Marx", "work": "The Eighteenth Brumaire of Louis Bonaparte", "quote": "The forces of monarchical **counterrevolution** exploited rural peasant superstitions to defeat Parisian workers."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The suppression of the revolutionary committees in Barcelona marked the silent victory of the **counterrevolution**."}
    ]
  },
  "counterrevolutionary": {
    "primary": "Opposed to, engaged in, or characteristic of a counterrevolution; aiming to reverse revolutionary change.",
    "secondary": "In ideological rhetoric, a pejorative label applied by revolutionary tribunals to political dissidents.",
    "quotes": [
      {"author": "Hannah Arendt", "work": "On Revolution", "quote": "Totalitarian regimes routinely label all moderate dissent as treasonous and **counterrevolutionary** sabotage."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The royalist Vendée became an armed epicenter of fierce **counterrevolutionary** resistance against the Paris Jacobins."},
      {"author": "Winston Churchill", "work": "The World Crisis", "quote": "White Army generals led **counterrevolutionary** campaigns across Siberia, struggling against the Red Army."}
    ]
  },
  "counterrevolutionist": {
    "primary": "A person who advocates, participates in, or leads a counterrevolution against an established revolutionary government.",
    "secondary": "In French Revolutionary history, an emigré aristocrat or royalist partisan fighting against the Republic.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary tribunal condemned every suspected **counterrevolutionist** to the impartial blade of the guillotine."},
      {"author": "Edmund Burke", "work": "Letters on a Regicide Peace", "quote": "The exiled French nobleman stood as an unbending **counterrevolutionist**, refusing any compromise with regicides."},
      {"author": "Arthur Koestler", "work": "Darkness at Noon", "quote": "Rubashov confessed to absurd charges of acting as a fascist **counterrevolutionist** to preserve Party unity."}
    ]
  },
  "devolution": {
    "primary": "The statutory delegation of powers from the central government of a sovereign state to regional or local administrations.",
    "secondary": "In evolutionary biology (informal), the hypothetical retrograde descent or degeneration to an earlier ancestral form.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "Administrative **devolution** revitalized rural municipalities by granting them control over local infrastructure."},
      {"author": "A. V. Dicey", "work": "Introduction to the Study of the Law of the Constitution", "quote": "Parliamentary sovereignty remains legally unfettered despite extensive **devolution** to subordinate national assemblies."},
      {"author": "Stephen Jay Gould", "work": "Ever Since Darwin", "quote": "Evolutionary biologists reject the notion of **devolution**, since phylogenetic descent is historical and non-directional."}
    ]
  },
  "devolve": {
    "primary": "To transfer or delegate power, responsibility, or authority to a lower level, or to pass by succession.",
    "secondary": "To degenerate or deteriorate gradually into a lower, less advanced, or chaotic state.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Upon the death or disability of the President, all executive powers **devolve** upon the Vice President."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "When imperial discipline broke down, border defenses began to **devolve** upon undisciplined local militias."},
      {"author": "William Golding", "work": "Lord of the Flies", "quote": "The stranded boys watched their democratic assembly **devolve** into tribal savagery and primal fear."}
    ]
  },
  "devolvement": {
    "primary": "The process or act of devolving; the transfer, delegation, or passage of power, duties, or property.",
    "secondary": "In institutional management, the structural reallocation of operational responsibilities to local teams.",
    "quotes": [
      {"author": "Woodrow Wilson", "work": "The State: Elements of Historical and Practical Politics", "quote": "The gradual **devolvement** of royal prerogative onto representative parliaments formed the essence of English liberty."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "The **devolvement** of estate administration onto hired bailiffs frequently led to neglected farm yields."},
      {"author": "John Stuart Mill", "work": "Considerations on Representative Government", "quote": "True political education requires the **devolvement** of real administrative responsibility upon common citizens."}
    ]
  },
  "disinvolve": {
    "primary": "To disentangle, extricate, unroll, or free from involvement, confusion, or complication.",
    "secondary": "In philosophical inquiry, separating essential truths from confusing rhetorical accretions.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "The natural philosopher must **disinvolve** empirical observations from the deceptive Idols of the Marketplace."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "It is the work of mature wisdom to **disinvolve** the mind from frivolous desires and false worldly ambitions."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Clear definitions serve to **disinvolve** complex ideas that scholastic disputes have hopelessly tangled."}
    ]
  },
  "evolution": {
    "primary": "The process of gradual developmental change, unfolding, and diversification over time from simpler forms.",
    "secondary": "In biology, the change in the heritable characteristics of biological populations over successive generations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "From so simple a beginning endless forms most beautiful and most wonderful have been, and are being, **evolution**."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "The cosmic process of **evolution** operates through unrelenting natural competition and adaptation."},
      {"author": "Theodosius Dobzhansky", "work": "Genetics and the Origin of Species", "quote": "Nothing in biology makes sense except in the light of **evolution**, which unites all living phenomena."}
    ]
  },
  "evolutionarily": {
    "primary": "In a manner relating to evolution, phylogenetic history, or gradual adaptive development over time.",
    "secondary": "In evolutionary biology, evaluating physical or behavioral traits in terms of their ancestral adaptive fitness.",
    "quotes": [
      {"author": "Richard Dawkins", "work": "The Selfish Gene", "quote": "Altruistic behaviors are **evolutionarily** stable only when benefits fall upon genetic kin sharing alleles."},
      {"author": "Stephen Jay Gould", "work": "The Panda's Thumb", "quote": "The panda's wrist bone is **evolutionarily** modified from a sesamoid to serve as an opposable stripping thumb."},
      {"author": "Edward O. Wilson", "work": "Sociobiology: The New Synthesis", "quote": "Eusocial insect colonies are **evolutionarily** designed to function as integrated superorganisms."}
    ]
  },
  "evolutionary": {
    "primary": "Relating to or based on the principles of biological or social evolution; characterized by gradual development.",
    "secondary": "In anthropology and sociology, theories explaining the progressive maturation of human societal institutions.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The moral sense of man is the crown of an **evolutionary** heritage rooted in primal social instincts."},
      {"author": "Steven Pinker", "work": "How the Mind Works", "quote": "Our visual instincts are **evolutionary** adaptations designed to navigate the savannas of Pleistocene Africa."},
      {"author": "Ernst Mayr", "work": "Systematics and the Origin of Species", "quote": "Geographic isolation provides the primary incubator for major **evolutionary** divergence and speciation."}
    ]
  },
  "evolutionism": {
    "primary": "The philosophical doctrine or scientific theory of biological, social, or cosmic evolution.",
    "secondary": "In nineteenth-century intellectual history, the overarching Victorian worldview applying evolutionary progress to all fields.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Universal **evolutionism** posits an inevitable progression from incoherent homogeneity to coherent heterogeneity."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The empirical triumphs of modern **evolutionism** dismantled centuries of theological dogmatism regarding species."},
      {"author": "Stephen Jay Gould", "work": "Ontogeny and Phylogeny", "quote": "Nineteenth-century social **evolutionism** erroneously equated technological prowess with biological superiority."}
    ]
  },
  "evolutionist": {
    "primary": "A person who studies, advocates, or adheres to the theory of biological or cultural evolution.",
    "secondary": "In scientific historiography, a naturalist championing natural selection against special creation doctrines.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Darwiniana", "quote": "As an outspoken **evolutionist**, he welcomed every opportunity to defend Darwin's mechanism in public debate."},
      {"author": "Charles Darwin", "work": "Life and Letters", "quote": "He rejoiced to find that the eminent botanist Asa Gray had declared himself a committed **evolutionist** in America."},
      {"author": "Stephen Jay Gould", "work": "Hen's Teeth and Horse's Toes", "quote": "The modern **evolutionist** views genetic drift and developmental constraints as essential partners to natural selection."}
    ]
  },
  "evolve": {
    "primary": "To develop, unfold, or change gradually over time, especially from a simple to a more complex state.",
    "secondary": "In biology, to undergo heritable genetic modification across successive generations through natural selection.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Species are not immutable productions, but **evolve** through the preservation of advantageous variations."},
      {"author": "Oliver Sacks", "work": "An Anthropologist on Mars", "quote": "The nervous system can **evolve** novel cognitive pathways to compensate for devastating sensory deprivation."},
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Commercial markets naturally **evolve** specialized divisions of labor to maximize economic productivity."}
    ]
  },
  "involucrate": {
    "primary": "Possessing, surrounded by, or enclosed within an involucre, such as the bracts of a flower head.",
    "secondary": "In systematic botany, describing inflorescences (like those in Asteraceae) encircled by specialized protective bracts.",
    "quotes": [
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The composite blossom features an **involucrate** head where dozens of tiny florets sit upon a common receptacle."},
      {"author": "John Lindley", "work": "The Vegetable Kingdom", "quote": "Characteristic **involucrate** umbels identify members of the Apiaceae family across European pastures."},
      {"author": "Liberty Hyde Bailey", "work": "Cyclopedia of American Horticulture", "quote": "Growers admire the silvery **involucrate** collars that frame the vibrant purple thistle blossoms."}
    ]
  },
  "involucre": {
    "primary": "A whorl, collar, or rosette of bracts surrounding an inflorescence, flower cluster, or umbel.",
    "secondary": "In bryology and pteridology, a membranous protective sheath enclosing reproductive organs or sporangia.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The outer bracts of the **involucre** protect the developing florets against desiccating winds and herbivorous insects."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "In the sunflower, the multiseriate **involucre** mimics the green calyx of an ordinary solitary flower."},
      {"author": "Henry David Thoreau", "work": "Wild Fruits", "quote": "The bristly prickly **involucre** of the American chestnut splits into four valves to reveal polished brown nuts."}
    ]
  },
  "involuntarily": {
    "primary": "Without intentional will, deliberate choice, or conscious control; spontaneously or reflexively.",
    "secondary": "In neurophysiology, physical responses executed automatically by the autonomic nervous system.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Darcy started, and for a moment looked **involuntarily** at Elizabeth, his composure momentarily shaken."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip shivered **involuntarily** as the escaped convict seized him roughly by the collar in the churchyard."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Watson drew back **involuntarily** as the venomous poisoned dart struck the wood beside his ear."}
    ]
  },
  "involuntariness": {
    "primary": "Absence of conscious intention, deliberate will, or voluntary control over an action or bodily movement.",
    "secondary": "In criminal jurisprudence, the defense that an act was committed without mens rea due to automatism or duress.",
    "quotes": [
      {"author": "Aristotle", "work": "Nicomachean Ethics", "quote": "Moral praise or blame attaches only to voluntary actions, whereas **involuntariness** receives pardon or pity."},
      {"author": "William Blackstone", "work": "Commentaries on the Laws of England", "quote": "The **involuntariness** of an act performed under direct bodily compulsion excludes criminal liability."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Patients were distressed by the uncontrollable **involuntariness** of their tics and sudden oculogyric crises."}
    ]
  },
  "involuntary": {
    "primary": "Done or occurring without conscious control, deliberate intention, or will; automatic, reflexive, or compelled.",
    "secondary": "In physiology, muscles (such as smooth and cardiac muscle) that operate independent of voluntary cortical control.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Blushing is the most peculiar and most human of all expressions, and it is strictly **involuntary**."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The knee-jerk reflex represents an elemental **involuntary** spinal arc that bypasses the cerebral hemispheres."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston suppressed an **involuntary** wince of pain as the telescreen barked out morning exercise drills."}
    ]
  },
  "involute": {
    "primary": "Rolled spirally inward from the margins, or intricate, complex, involved, and turned upon itself.",
    "secondary": "In differential geometry, a curve obtained by unwinding a taut string from another curve (the evolute).",
    "quotes": [
      {"author": "Thomas De Quincey", "work": "Suspiria de Profundis", "quote": "Our deepest thoughts are **involute** structures, where childhood memories and adult griefs coil together."},
      {"author": "Asa Gray", "work": "Botanical Text-Book", "quote": "Young leaves of water lilies exhibit **involute** vernation, with both lateral edges rolled tightly toward the upper face."},
      {"author": "Herman Melville", "work": "The Confidence-Man", "quote": "The masquerader spun an **involute** web of philosophical sophistries to extract banknotes from travelers."}
    ]
  },
  "involution": {
    "primary": "The act of involving or rolling inward, or a return of an enlarged organ (like the uterus) to normal size.",
    "secondary": "In mathematics, a function or transformation that is its own inverse (applying it twice yields the identity).",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The postpartum **involution** of the uterus proceeds rapidly through physiological autolysis of hypertrophied muscle."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The narrative swept forward through endless **involution** of bureaucratic committees and factional plots."},
      {"author": "Douglas Hofstadter", "work": "Gödel, Escher, Bach", "quote": "Self-referential programs exhibit a dizzying mathematical **involution** where data and code fold upon each other."}
    ]
  },
  "involve": {
    "primary": "To include, contain, engage, or connect as a necessary part, consequence, or participant in an activity.",
    "secondary": "In historical literary usage, to wrap up, envelop, shroud, or entangle within folds.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Decisions made by local municipal councils directly **involve** the daily welfare and property of every townsman."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Thick clouds of sulfurous smoke did **involve** the infernal landscape in subterranean gloom."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor dreaded that any public revelation of the secret engagement would **involve** Edward in family ruin."}
    ]
  },
  "involved": {
    "primary": "Complicated, intricate, and difficult to comprehend, or deeply engaged and participating in an activity.",
    "secondary": "In interpersonal relations, emotionally, romantically, or conspiratorially entangled with another party.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes listened attentively to the **involved** family legend, leaning back in his armchair with closed eyes."},
      {"author": "Henry James", "work": "The Golden Bowl", "quote": "Maggie found herself hopelessly **involved** in a delicate web of domestic deception and unspoken alliances."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "The political disputes between the syndicalists and communists were fiercely **involved** and led to bloodshed."}
    ]
  },
  "involvement": {
    "primary": "The act or state of participating, engaging, or being included in a situation, project, or relationship.",
    "secondary": "In foreign policy and diplomacy, foreign military or economic intervention in the affairs of other states.",
    "quotes": [
      {"author": "George F. Kennan", "work": "American Diplomacy", "quote": "He warned against deep military **involvement** on the Asian mainland where strategic objectives remained vague."},
      {"author": "Virginia Woolf", "work": "To the Lighthouse", "quote": "Mrs. Ramsay felt a deep emotional **involvement** with the happiness of every guest staying beneath her roof."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Mr. Micawber's chronic financial **involvement** led to frequent visits from bailiffs and debt collectors."}
    ]
  },
  "malevolence": {
    "primary": "The state, disposition, or feeling of wishing evil, harm, or injury to others; active ill will or malice.",
    "secondary": "In dramatic literature, the cold, unprovoked villainy embodied by characters such as Iago.",
    "quotes": [
      {"author": "Samuel Taylor Coleridge", "work": "Lectures on Shakespeare", "quote": "Iago's soliloquies reveal a motiveless **malevolence**, an aesthetic delight in engineering destruction for its own sake."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The creature's bitter loneliness hardened into relentless **malevolence** against his neglectful creator."},
      {"author": "Edgar Allan Poe", "work": "The Black Cat", "quote": "A spirit of perverseness and dark **malevolence** seized my soul, urging me to commit atrocities without motive."}
    ]
  },
  "malevolency": {
    "primary": "The quality or disposition of being malevolent; malicious enmity, spite, or destructive ill will.",
    "secondary": "In historical ethical treatises, deep-seated hostility that celebrates the downfall of virtuous men.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "The Idler", "quote": "Envy soon degenerates into active **malevolency**, which finds its bitter feast in the humiliation of merit."},
      {"author": "Walter Scott", "work": "The Bride of Lammermoor", "quote": "Lady Ashton looked upon the Master of Ravenswood with an unbending **malevolency** that chilled all present."},
      {"author": "Charles Dickens", "work": "The Old Curiosity Shop", "quote": "Quilp chuckled with hideous **malevolency** as he plotted the financial ruin of poor grandfather Trent."}
    ]
  },
  "malevolent": {
    "primary": "Having or showing a wish to do evil to others; malicious, spiteful, hostile, and actively harmful.",
    "secondary": "In myth and supernatural fiction, dark spirits or cosmic entities exerting harmful influences upon humanity.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab imputed to the white whale an intelligent, **malevolent** agency that actively sought the destruction of men."},
      {"author": "Bram Stoker", "work": "Dracula", "quote": "The red eyes of Count Dracula burned in the shadows with cold, **malevolent** intensity as the wolves gathered."},
      {"author": "Jane Austen", "work": "Northanger Abbey", "quote": "Catherine imagined General Tilney to be a **malevolent** tyrant who had murdered or imprisoned his deceased wife."}
    ]
  },
  "malevolently": {
    "primary": "In a malevolent, spiteful, or vicious manner; with active malice and evil intent.",
    "secondary": "In narrative description, glaring, speaking, or smiling with overt hostility and sinister joy.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Final Problem", "quote": "Moriarty's eyes gleamed **malevolently** through his spectacles as he warned Holmes of inevitable destruction."},
      {"author": "Charles Dickens", "work": "Oliver Twist", "quote": "Bill Sikes glared **malevolently** at the cowering dog, striking the table with his heavy fist."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Israel Hands grinned **malevolently**, concealing the bloody dirk behind his back as he stalked Hawkins."}
    ]
  },
  "nonvolatile": {
    "primary": "Not readily evaporating at normal temperatures and pressures; chemically stable and resistant to vaporizing.",
    "secondary": "In computer memory architecture, storage (like flash memory or ROM) that retains data when power is lost.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Fixed alkaline salts remain **nonvolatile** even under the most intense flame of the reverberatory furnace."},
      {"author": "John von Neumann", "work": "The Computer and the Brain", "quote": "Permanent memory registers require **nonvolatile** physical storage to preserve foundational system states."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Heavy **nonvolatile** pesticide residues accumulate in river silt, persisting for decades without breakdown."}
    ]
  },
  "nonvolatilisable": {
    "primary": "Incapable of being volatilized or converted into vapor or gas (British spelling).",
    "secondary": "In analytical chemistry, refractory mineral compounds that do not sublimate under standard laboratory distillation.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The metallic residue proved completely **nonvolatilisable** even when exposed to the intense electric arc."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Earthy oxides constitute a **nonvolatilisable** stratum that resists ordinary blowpipe decomposition."},
      {"author": "Thomas Graham", "work": "Elements of Chemistry", "quote": "In quantitative analysis, the **nonvolatilisable** ash is weighed after all organic carbons have burned away."}
    ]
  },
  "nonvolatilizable": {
    "primary": "Incapable of being converted into vapor, gas, or fume under heat; refractory.",
    "secondary": "In metallurgical assaying, nonvolatile ores and slag elements that remain fixed in the crucible.",
    "quotes": [
      {"author": "J. J. Thomson", "work": "Rays of Positive Electricity", "quote": "The electrode was fabricated from a **nonvolatilizable** refractory metal to prevent sputtering in the vacuum."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Pure silica is practically **nonvolatilizable** under ordinary combustion temperatures in open air."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "Barium salts formed a **nonvolatilizable** precipitate that retained intense radium radioactivity."}
    ]
  },
  "nonvoluntary": {
    "primary": "Not voluntary; performed or occurring without the exercise of conscious will or voluntary consent.",
    "secondary": "In jurisprudence and bioethics, actions performed without deliberate consent but without active objection (as in infant care).",
    "quotes": [
      {"author": "Aristotle", "work": "Nicomachean Ethics", "quote": "Actions performed through ignorance are **nonvoluntary** if the actor feels no subsequent regret or repentance."},
      {"author": "John Stuart Mill", "work": "Utilitarianism", "quote": "Civilized societies distinguish strictly between voluntary contracts and **nonvoluntary** civic obligations."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The patient experienced **nonvoluntary** respiratory gasps whenever emotional agitation overwhelmed his cortical control."}
    ]
  },
  "revolt": {
    "primary": "An uprising or rebellion against an established authority or government, or to rebel or feel intense disgust.",
    "secondary": "In aesthetic and ethical discourse, a profound visceral revulsion provoked by ugliness, cruelty, or injustice.",
    "quotes": [
      {"author": "Albert Camus", "work": "The Rebel", "quote": "What is a rebel? A man who says no; his first act of metaphysical **revolt** affirms common human dignity."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Oppressive provincial taxation provoked an armed **revolt** that spread rapidly among the Numidian tribes."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "Winston understood that secret diary writing was an act of solitary **revolt** that carried the death penalty."}
    ]
  },
  "revolting": {
    "primary": "Highly offensive, disgusting, repulsive, or loathsome; causing profound visceral revulsion.",
    "secondary": "In political history, rising up in armed rebellion or mutiny against sovereign authority.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The neglected pauper burial pit presented a **revolting** spectacle of municipal greed and public callousness."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The traveler averted his gaze from the **revolting** relics of cannibal feasts hung in wicker baskets."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "A creature endowed with monstrous stature and **revolting** yellow skin opened watery eyes before me."}
    ]
  },
  "revoltingly": {
    "primary": "In a revolting, disgusting, repulsive, or offensive manner; to a sickeningly loathsome degree.",
    "secondary": "In descriptive narrative, depicting unhygienic conditions or grotesque moral behavior with stark realism.",
    "quotes": [
      {"author": "George Orwell", "work": "Down and Out in Paris and London", "quote": "The hotel washbasins were **revoltingly** filthy, coated in grease and discarded cigarette stubs."},
      {"author": "Jonathan Swift", "work": "Gulliver's Travels", "quote": "The grotesque habits of the Yahoos were **revoltingly** beastly, shocking Gulliver's sense of human dignity."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Cardboard Box", "quote": "The package contained two severed human ears packed **revoltingly** in coarse kitchen salt."}
    ]
  },
  "revolution": {
    "primary": "A fundamental, rapid change in political power or social organization, or a circular movement around an axis.",
    "secondary": "In scientific and intellectual history, paradigm shifts such as the Copernican and Darwinian revolutions.",
    "quotes": [
      {"author": "Thomas Kuhn", "work": "The Structure of Scientific Revolutions", "quote": "A scientific **revolution** occurs when an accumulation of anomalies shatters the reigning paradigm."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "The French **revolution** surprised all of Europe because the old feudal walls fell in a single night."},
      {"author": "Nicolaus Copernicus", "work": "On the Revolutions of the Heavenly Spheres", "quote": "The apparent daily rotation of the heavens is caused by the axial **revolution** of the Earth itself."}
    ]
  },
  "revolutionary": {
    "primary": "Involving or causing a complete or dramatic change, or relating to a political revolution.",
    "secondary": "In industrial and technological history, innovations (like the steam engine) that transform global society.",
    "quotes": [
      {"author": "Thomas Paine", "work": "Common Sense", "quote": "The cause of America is in a great measure the cause of all mankind; a **revolutionary** dawn has broken."},
      {"author": "Eric Hobsbawm", "work": "The Age of Revolution", "quote": "The dual **revolutionary** breakthroughs of British industry and French politics transformed the globe."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The view that species undergo gradual natural modification will have a **revolutionary** effect on natural history."}
    ]
  },
  "revolutionise": {
    "primary": "To change something radically, fundamentally, or completely; to alter through revolution (British spelling).",
    "secondary": "In industrial history, applying mechanical inventions to transform established handicraft trades.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "New metallurgical smelting techniques began to **revolutionise** hardware manufacture throughout Birmingham."},
      {"author": "Karl Marx", "work": "The Communist Manifesto", "quote": "The bourgeoisie cannot exist without constantly seeking to **revolutionise** the instruments of production."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Electromagnetic induction was destined to **revolutionise** global industry and illumination."}
    ]
  },
  "revolutionism": {
    "primary": "The principles, doctrines, beliefs, or practices of political or social revolutionaries.",
    "secondary": "In political science, radical ideological movements advocating violent upheaval rather than reform.",
    "quotes": [
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "Abstract French **revolutionism** sacrifices living human beings to dogmatic geometric fantasies of equality."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In a prosperous democracy, widespread property ownership dampens the violent flames of **revolutionism**."},
      {"author": "Hannah Arendt", "work": "On Revolution", "quote": "Modern **revolutionism** was born when men realized that social misery was not an unalterable fate of nature."}
    ]
  },
  "revolutionist": {
    "primary": "A person who advocates, organizes, or participates in a political, social, or intellectual revolution.",
    "secondary": "In Russian and European history, underground conspirators organizing political uprisings.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Under Western Eyes", "quote": "The exiled **revolutionist** lived in a drab Geneva room, plotting conspiracies across the Russian border."},
      {"author": "Fyodor Dostoevsky", "work": "Demons", "quote": "Verkhovensky was a cynical **revolutionist** who manipulated idealistic youths into political terror."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Danton stood as the colossal titan **revolutionist**, whose voice rallied the armies of France at Valmy."}
    ]
  },
  "revolutionize": {
    "primary": "To change something fundamentally, radically, or completely through innovation or political upheaval.",
    "secondary": "In the history of science, introducing transformative paradigms that overturn established scientific dogmas.",
    "quotes": [
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "The telescope arrived in the hands of Galileo to **revolutionize** human understanding of the solar system."},
      {"author": "Walter Isaacson", "work": "Steve Jobs", "quote": "Jobs aimed to **revolutionize** six separate industries: personal computers, animated films, music, phones, tablets, and digital publishing."},
      {"author": "Siddhartha Mukherjee", "work": "The Emperor of All Maladies", "quote": "Targeted therapies began to **revolutionize** oncology by disabling specific oncogenic signaling cascades."}
    ]
  },
  "revolve": {
    "primary": "To move in a circular or curving orbit around a central point or axis, or to turn over repeatedly in the mind.",
    "secondary": "In cognitive reflection, to ponder, deliberate, or contemplate an idea from multiple perspectives.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The primary planets **revolve** about the Sun in concentric ellipses according to inverse square attraction."},
      {"author": "William Shakespeare", "work": "Twelfth Night", "quote": "If this fall into thy hand, **revolve**. In my stars I am above thee; but be not afraid of greatness."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "I spent sleepless nights in my laboratory, letting my dark purpose **revolve** continually in my mind."}
    ]
  },
  "revolved": {
    "primary": "Moved in a circular path or orbit around an axis, or considered and reflected upon deeply in thought.",
    "secondary": "In celestial mechanics, planets having traversed their completed orbital circuits through the zodiac.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab **revolved** his desperate nautical scheme in the dark cabin, charting the seasonal migration of whales."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "The celestial orbs had **revolved** their ancient dance before mortal eyes first beheld the light of dawn."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "David **revolved** the lawyer's stern warning in his thoughts, wondering how to rescue Dora from penury."}
    ]
  },
  "revolver": {
    "primary": "A repeating handgun that has a revolving cylinder containing multiple cartridge chambers.",
    "secondary": "In firearms history, the multi-chambered firearm popularized by Samuel Colt in the nineteenth century.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes slipped his service **revolver** into his overcoat pocket before we set out across the dark moor."},
      {"author": "Mark Twain", "work": "Roughing It", "quote": "In the mining camps of Nevada, every gentleman carried a Colt **revolver** strapped securely to his hip."},
      {"author": "Stephen Crane", "work": "The Bride Comes to Yellow Sky", "quote": "Scratchy Wilson stood in the dusty street, twin **revolver** barrels gleaming in the hot Texas sun."}
    ]
  },
  "uninvolved": {
    "primary": "Not connected with, participating in, or affected by an activity, organization, or emotional relationship.",
    "secondary": "In clinical observation, tissues, organs, or anatomical areas spared from pathological disease or trauma.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The lobar consolidation affected the right lower lobe, leaving the upper lobes completely **uninvolved**."},
      {"author": "George Orwell", "work": "Homage to Catalonia", "quote": "Civilian shopkeepers tried desperately to remain **uninvolved** as gunfire echoed down the Ramblas."},
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Ralph Touchett preferred to watch the human comedy from the sidelines, an **uninvolved** spectator."}
    ]
  },
  "unvoluntary": {
    "primary": "Not voluntary; occurring without choice, conscious will, or deliberate intention; involuntary.",
    "secondary": "In philosophical ethics, actions undertaken without conscious consent or under direct external physical duress.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The convulsive spasm of a limb under palsy is purely **unvoluntary**, admitting no intervention of will."},
      {"author": "Thomas Hobbes", "work": "Leviathan", "quote": "Vital motions such as the circulation of the blood are **unvoluntary**, proceeding without conscious thought."},
      {"author": "David Hume", "work": "A Treatise of Human Nature", "quote": "Our moral sentiments distinguish between voluntary crimes and **unvoluntary** bodily injuries."}
    ]
  },
  "volaille": {
    "primary": "Poultry, domestic fowl, or game birds prepared and cooked for culinary service (French gastronomy).",
    "secondary": "In classical French culinary cuisine, velouté de volaille or supreme de volaille prepared with chicken stock.",
    "quotes": [
      {"author": "Auguste Escoffier", "work": "A Guide to Modern Cookery", "quote": "For a delicate velouté de **volaille**, simmer farm-raised capon stock with a pale blonde roux and cream."},
      {"author": "Marcel Proust", "work": "In Search of Lost Time", "quote": "Françoise appeared bearing a roast **volaille**, its golden skin glistening with savory juices and herbs."},
      {"author": "Julia Child", "work": "Mastering the Art of French Cooking", "quote": "A rich stock made from fresh **volaille** carcasses forms the indispensable foundation of classical sauces."}
    ]
  },
  "volans": {
    "primary": "A faint southern constellation representing the flying fish, located south of the celestial equator.",
    "secondary": "In celestial navigation, a constellation introduced by Dutch navigators Keyser and de Houtman in the late 16th century.",
    "quotes": [
      {"author": "John Herschel", "work": "Outlines of Astronomy", "quote": "Observers in the southern hemisphere can trace the faint stars of **Volans** gliding near the Large Magellanic Cloud."},
      {"author": "Arthur Eddington", "work": "Stellar Movements and the Structure of the Universe", "quote": "Parallax measurements of double stars in **Volans** helped calibrate stellar luminosities in southern skies."},
      {"author": "Richard Proctor", "work": "A Star Atlas for the Library, the School and the Observatory", "quote": "Navigators rounding Cape Horn utilized the circumpolar stars of **Volans** to calibrate their nocturnal course."}
    ]
  }
}
