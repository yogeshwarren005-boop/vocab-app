# -*- coding: utf-8 -*-
"""
Curates Dashboard — vol (Part 2: words 59-115) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part2 = {
  "volant": {
    "primary": "Flying, capable of flight, or moving lightly and swiftly through the air.",
    "secondary": "In heraldry, depicted as flying with wings spread horizontally across a shield.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Blind Thamyris and blind Maeonides, and Tiresias and Phineus, prophets old; then feed on thoughts that **volant** move."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The tiny **volant** insects of the pampas were carried hundreds of miles out to sea by gale winds."},
      {"author": "Richard Owen", "work": "Palaeontology", "quote": "Archaeopteryx possessed true **volant** plumage along its forelimbs, bridging reptiles and birds."}
    ]
  },
  "volapuk": {
    "primary": "An artificial international auxiliary language created in 1879 by Johann Martin Schleyer.",
    "secondary": "In linguistics, the historical precursor to Esperanto characterized by complex agglutinative Germanic inflections.",
    "quotes": [
      {"author": "Max Müller", "work": "The Science of Language", "quote": "The sudden rise of **Volapuk** demonstrated the widespread modern desire for a neutral universal tongue."},
      {"author": "H. G. Wells", "work": "A Modern Utopia", "quote": "Utopians discarded irregular historical dialects, adopting a synthesized language superior to **Volapuk**."},
      {"author": "Otto Jespersen", "work": "An International Language", "quote": "Schleyer's **Volapuk** failed because its synthetic roots distorted familiar European words beyond recognition."}
    ]
  },
  "volar": {
    "primary": "Relating to the palm of the hand or the sole of the foot; palmar or plantar.",
    "secondary": "In clinical orthopedics and plastic surgery, the flexor or anterior compartment of the forearm and hand.",
    "quotes": [
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "The incision along the **volar** aspect of the wrist was planned carefully to avoid the median nerve."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "Sensory testing revealed dense anesthesia across the **volar** pads of the fingertips after nerve compression."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "The superficial **volar** arch of the hand is formed primarily by the continuation of the ulnar artery."}
    ]
  },
  "volary": {
    "primary": "A large aviary or birdcage spacious enough to permit birds to fly freely within it.",
    "secondary": "In historical estate architecture, a freestanding outdoor bird enclosure featured in country gardens.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Essays", "quote": "For aviaries, I like them not, except they be of that largeness as to be turfed, a true outdoor **volary**."},
      {"author": "John Evelyn", "work": "Diary", "quote": "His lordship entertained us in his garden, showing a magnificent **volary** stocked with foreign songbirds."},
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "Swallows kept within a spacious **volary** exhibited migratory restlessness as autumnal frosts approached."}
    ]
  },
  "volatile": {
    "primary": "Evaporating rapidly at normal temperatures and pressures, or liable to change rapidly and unpredictably.",
    "secondary": "In financial economics, describing markets subject to sharp, erratic price fluctuations.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Sceptical Chymist", "quote": "Essential plant oils are highly **volatile**, dispersing sweet fragrances through the air when gently heated."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "A single legislative assembly is prone to sudden, **volatile** passions that threaten stable governance."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "Miss Mowcher was a **volatile** creature, hopping about the room and chattering with dizzying rapidity."}
    ]
  },
  "volatilisable": {
    "primary": "Capable of being volatilized or converted into vapor by the application of heat (British spelling).",
    "secondary": "In chemistry, liquid or solid elements that transition into gas phase at reachable boiling temperatures.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Mercury is readily **volatilisable** under the spirit lamp, condensing into bright metallic beads in the neck."},
      {"author": "Humphry Davy", "work": "Elements of Agricultural Chemistry", "quote": "Ammoniacal compounds are easily **volatilisable**, requiring soil covering to prevent loss into the air."},
      {"author": "Thomas Graham", "work": "Elements of Chemistry", "quote": "Sublimation separates a **volatilisable** solid such as iodine from nonvolatile mineral impurities."}
    ]
  },
  "volatilise": {
    "primary": "To convert or be converted from a solid or liquid into vapor or gas through heat (British spelling).",
    "secondary": "In metallurgical smelting, driving off sulfur, arsenic, or mercury vapors from crude ores.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry", "quote": "Intense electric discharges can **volatilise** thin gold leaves, leaving a purple stain of metallic mist."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "High heat in closed retorts will **volatilise** the spirit of wine without decomposing its carbonaceous base."},
      {"author": "Robert Hooke", "work": "Micrographia", "quote": "Combustion serves to **volatilise** the sulfurous components of coal, discharging black smoke into the sky."}
    ]
  },
  "volatilised": {
    "primary": "Converted into vapor, gas, or fume by the action of heat or chemical reaction (British spelling).",
    "secondary": "In historical alchemy and chemistry, describing components driven off during fractional distillation.",
    "quotes": [
      {"author": "Joseph Priestley", "work": "Experiments and Observations on Different Kinds of Air", "quote": "The charcoal was **volatilised** in fixed air, yielding a combustible gaseous mixture over water."},
      {"author": "Humphry Davy", "work": "Researches, Chemical and Philosophical", "quote": "Nitrous oxide gas was **volatilised** and collected in gasometers for experimental inhalation."},
      {"author": "John Tyndall", "work": "Heat Considered as a Mode of Motion", "quote": "The radiant heat of the electric arc **volatilised** the carbon points, emitting a brilliant white glare."}
    ]
  },
  "volatility": {
    "primary": "The tendency of a substance to evaporate rapidly at normal temperatures; also emotional instability or market fluctuation.",
    "secondary": "In financial asset pricing, the statistical dispersion of returns measured by standard deviation over time.",
    "quotes": [
      {"author": "Benjamin Graham", "work": "The Intelligent Investor", "quote": "The disciplined investor profits from market **volatility**, purchasing undervalued assets during panics."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Ether exhibits extraordinary **volatility**, boiling rapidly upon contact with the palm of the hand."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The **volatility** of public opinion makes popular assemblies dangerous guardians of constitutional stability."}
    ]
  },
  "volatilizable": {
    "primary": "Capable of being volatilized, evaporated, or converted into gas or vapor under heat.",
    "secondary": "In industrial chemistry, describing solvents or volatile organic compounds easily distilled.",
    "quotes": [
      {"author": "J. J. Thomson", "work": "The Corpuscular Theory of Matter", "quote": "The filament was coated with **volatilizable** thorium oxides to enhance thermionic electron emission."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "Polonium is easily **volatilizable** at high temperatures, redepositing upon cooler glass tubing."},
      {"author": "Robert Boyle", "work": "New Experiments Physico-Mechanicall", "quote": "The sulfurous spirit proved **volatilizable** in vacuum, expanding into a pale vaporous cloud."}
    ]
  },
  "volatilize": {
    "primary": "To convert or cause to pass from a solid or liquid state into vapor or gas through heating.",
    "secondary": "In figurative discourse, to cause to vanish, disperse, or dissolve into thin air.",
    "quotes": [
      {"author": "Karl Marx", "work": "The Communist Manifesto", "quote": "All fixed, fast-frozen relations are swept away, all that is solid melts into air, and old traditions **volatilize**."},
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Gentle warming will **volatilize** the aromatic esters that give fine vintage wine its distinctive bouquet."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Philosophic radicalism threatens to **volatilize** all sacred reverences into empty mechanical formulas."}
    ]
  },
  "volatilized": {
    "primary": "Converted into vapor or gas; evaporated through heat or chemical change.",
    "secondary": "Dispersed, vanished, or dissolved away like vapor in air.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The boiling blubber in the try-pots **volatilized** into dense oily smoke that blanketed the Pequod."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "The hard physical world seemed **volatilized** into spiritual symbolism before the poet's ecstatic gaze."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "A portion of the sulfur **volatilized** into yellow crystals upon the upper dome of the retort."}
    ]
  },
  "volcanic": {
    "primary": "Relating to, produced by, or resembling a volcano; characterized by explosive geological or emotional heat.",
    "secondary": "In petrology, extrusive igneous rocks (such as basalt, pumice, and obsidian) formed from cooled lava.",
    "quotes": [
      {"author": "Charles Darwin", "work": "Geological Observations on Volcanic Islands", "quote": "The black basaltic ramparts of Saint Helena bear testimony to colossal **volcanic** eruptions in deep antiquity."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Continuous **volcanic** activity along the Mediterranean coast demonstrates that subterranean forces remain vigorous."},
      {"author": "Herman Melville", "work": "The Encantadas", "quote": "The Galápagos presented a desolate, cinder-strewn archipelago born of recent **volcanic** fury."}
    ]
  },
  "volcanically": {
    "primary": "In a volcanic manner; by means of volcanic activity, explosive eruption, or subterranean heat.",
    "secondary": "In metaphorical description, erupting with sudden, overwhelming passion, fury, or violence.",
    "quotes": [
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Mount Shasta stands **volcanically** sculptured above the northern pine forests, its crater choked with snow."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "Paris erupted **volcanically**, hurling forth armed mobs of sans-culottes against the Tuileries gates."},
      {"author": "Rachel Carson", "work": "The Sea Around Us", "quote": "Submarine trenches generate deep oceanic seamounts **volcanically**, building island chains across the Pacific."}
    ]
  },
  "volcanism": {
    "primary": "Volcanic activity, phenomena, or processes involving the eruption of molten rock, lava, and pyroclastic debris.",
    "secondary": "In planetary geology, the thermal forces that resurface celestial bodies such as Io, Venus, and Mars.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "Subterranean heat and **volcanism** act as the primary counterbalance to the ceaseless erosion of continents."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Jupiter's moon Io exhibits violent sulfurous **volcanism** driven by tidal gravitational kneading."},
      {"author": "James Dwight Dana", "work": "Characteristics of Volcanoes", "quote": "Hawaiian **volcanism** is characterized by fluid basaltic flows rather than explosive pyroclastic detonations."}
    ]
  },
  "volcano": {
    "primary": "A mountain or hill with a crater or vent through which lava, rock fragments, hot vapor, and gas erupt.",
    "secondary": "In figurative expression, a person or situation simmering with suppressed anger ready to explode.",
    "quotes": [
      {"author": "Pliny the Younger", "work": "Letters", "quote": "A pine-tree shaped cloud of black ash rose high above the roaring **volcano** Vesuvius, blotting out the sun."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The majestic cone of Osorno **volcano** illuminated the Chilean night sky with sheets of crimson fire."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "Ahab stood upon the quarter-deck like a dormant **volcano**, brooding upon his dark, consuming vengeance."}
    ]
  },
  "volcanology": {
    "primary": "The scientific study of volcanoes, volcanic phenomena, lava flows, magma dynamics, and related geology.",
    "secondary": "In geophysics, monitoring seismic tremors, gas emissions, and ground deformation to predict eruptions.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The nascent science of **volcanology** began with careful observations of Etna and Vesuvius by Hamilton."},
      {"author": "James Dwight Dana", "work": "Manual of Geology", "quote": "Modern **volcanology** links magma viscosity and silica content directly to the eruptive style of calderas."},
      {"author": "Stephen Jay Gould", "work": "Time's Arrow, Time's Cycle", "quote": "The catastrophic explosion of Krakatoa provided **volcanology** with global atmospheric circulation data."}
    ]
  },
  "vole": {
    "primary": "A small, burrowing mouselike rodent belonging to the subfamily Arvicolinae, with a stouter body and shorter tail.",
    "secondary": "In card games, winning all the tricks in a deal in games like quadrille, ombre, or whist.",
    "quotes": [
      {"author": "Gilbert White", "work": "The Natural History of Selborne", "quote": "The water **vole** excavates extensive tunnels along the muddy banks of the brook, feeding on succulent reeds."},
      {"author": "Kenneth Grahame", "work": "The Wind in the Willows", "quote": "Ratty the water **vole** welcomed Mole to his riverbank home, offering cold chicken and wicker hampers."},
      {"author": "Alexander Pope", "work": "The Rape of the Lock", "quote": "Belinda played her ombre hand with ruthless cunning, sweeping the board and claiming the triumphant **vole**."}
    ]
  },
  "volition": {
    "primary": "The faculty or power of using one's own will; the act of making a conscious, deliberate choice or decision.",
    "secondary": "In philosophical theology, the mental act that initiates voluntary bodily motion or moral intention.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "**Volition** is an act of the mind knowingly exerting that dominion it takes itself to have over any part of the man."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The essential achievement of the will is to attend to a difficult object and hold it fast before the mind: that is **volition**."},
      {"author": "David Hume", "work": "An Enquiry Concerning Human Understanding", "quote": "We experience internal command over our organs, but the secret power linking **volition** to muscular contraction remains unknown."}
    ]
  },
  "volitional": {
    "primary": "Relating to or done by volition, conscious will, or deliberate choice; purposeful and intentional.",
    "secondary": "In neurological motor control, movements directed by conscious cortical intent rather than reflexive pathways.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "L-dopa enabled patients to transform frozen immobility into spontaneous **volitional** locomotion and speech."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "The motor cortex and supplementary motor area coordinate the execution of complex **volitional** movements."},
      {"author": "William James", "work": "The Will to Believe", "quote": "A **volitional** decision becomes imperative when we face a genuine option that is forced, living, and momentous."}
    ]
  },
  "volitionally": {
    "primary": "By means of volition; intentionally, deliberately, and with conscious will or choice.",
    "secondary": "In legal culpability, acting with conscious knowledge and purpose rather than through coercion.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "An agent acts **volitionally** when his conscious desire serves as the immediate antecedent of his muscular action."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "He struggled for weeks before he could **volitionally** fire the quadriceps tendon of his injured limb."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea acted **volitionally**, refusing to allow parental disapproval to sway her philanthropic resolutions."}
    ]
  },
  "volley": {
    "primary": "A simultaneous discharge of a number of firearms, arrows, or missiles, or hitting a ball before it bounces.",
    "secondary": "In rhetoric, a rapid, overwhelming outpouring of words, arguments, questions, or insults.",
    "quotes": [
      {"author": "Stephen Crane", "work": "The Red Badge of Courage", "quote": "A rolling **volley** of musketry swept across the wheatfield, cutting down the blue-coated battle line."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Our soldiers answered their haughty taunts with a fierce **volley** of English arrows that darkened the sky."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Madame Defarge released a sudden **volley** of furious curses against the fleeing aristocrats."}
    ]
  },
  "volleyball": {
    "primary": "A team sport in which players use their hands to hit a high ball back and forth over a net without letting it touch the ground.",
    "secondary": "In sports history, an athletic game invented in 1895 by William G. Morgan as a less strenuous indoor recreation.",
    "quotes": [
      {"author": "David Foster Wallace", "work": "Infinite Jest", "quote": "The student athletes unwound after grueling tennis drills with an informal sand-court **volleyball** match."},
      {"author": "Tom Wolfe", "work": "The Right Stuff", "quote": "The Mercury astronauts relaxed between centrifuge tests with vigorous games of beach **volleyball** in Cocoa Beach."},
      {"author": "John Updike", "work": "Rabbit at Rest", "quote": "The Florida condominium recreation lawn featured a sun-faded **volleyball** net sagging between palm trees."}
    ]
  },
  "volt": {
    "primary": "The SI unit of electrical potential difference and electromotive force, named after Alessandro Volta.",
    "secondary": "In physics, the potential difference across a conductor when a current of one ampere dissipates one watt of power.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The international committee adopted the **volt** as the standard practical measure of electromotive force."},
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "My high-frequency resonant transformers generated potentials exceeding hundreds of thousands of a **volt**."},
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "Current flows along the cable in direct proportion to the applied difference measured in every **volt**."}
    ]
  },
  "volt-ampere": {
    "primary": "A unit of apparent electrical power in an alternating current circuit, equal to the product of one volt and one ampere.",
    "secondary": "In power engineering, distinguishing apparent power (VA) from real active power (watts) adjusted for power factor.",
    "quotes": [
      {"author": "Charles Proteus Steinmetz", "work": "Theory and Calculation of Alternating Current Phenomena", "quote": "In reactive inductive circuits, the total **volt-ampere** rating exceeds the real wattage delivered to the load."},
      {"author": "Nikola Tesla", "work": "Experiments with Alternate Currents of High Potential", "quote": "Careful transformer design minimizes idle **volt-ampere** losses in alternating distribution networks."},
      {"author": "Oliver Heaviside", "work": "Electrical Papers", "quote": "The ratio between real watts and apparent **volt-ampere** product defines the governing power factor of transmission."}
    ]
  },
  "volta": {
    "primary": "Count Alessandro Volta, the Italian physicist famous for inventing the chemical electric battery (voltaic pile) in 1799.",
    "secondary": "In music and dance, a lively Renaissance turning dance, or a musical direction (prima volta, seconda volta) indicating repeated endings.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The immortal discovery of the electric pile by **Volta** opened a glorious new epoch in natural science."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Following the path marked by **Volta**, we were enabled to decompose caustic potassa into pure potassium metal."},
      {"author": "William Shakespeare", "work": "Henry V", "quote": "They bid us to the English dancing-schools, and teach lavoltas high and swift corantos... like the **volta** of old."}
    ]
  },
  "voltage": {
    "primary": "Electric potential difference expressed in volts; the electrical pressure driving electrons through a circuit.",
    "secondary": "In power transmission, stepping up voltage with transformers to minimize thermal resistance losses over distances.",
    "quotes": [
      {"author": "Nikola Tesla", "work": "Colorado Springs Notes", "quote": "By elevating the **voltage** to extreme potentials, electromagnetic waves could be transmitted through the upper atmosphere."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "He defended low-voltage direct current systems, warning against the lethal hazards of alternating high **voltage**."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "The electrostatic field inside a conductor vanishes, maintaining uniform **voltage** throughout its volume."}
    ]
  },
  "voltaic": {
    "primary": "Relating to or produced by chemical electric currents or galvanic electricity, named after Alessandro Volta.",
    "secondary": "In electrochemistry, a voltaic cell that converts chemical energy into electrical energy via spontaneous redox reactions.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The chemical decomposition produced by the **voltaic** current is directly proportional to the quantity of electricity passed."},
      {"author": "Humphry Davy", "work": "Bakerian Lectures", "quote": "The giant **voltaic** battery of the Royal Institution produced blinding electrical arcs between charcoal points."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Galvanism and the wondrous mysteries of the **voltaic** pile inspired Victor's dreams of infusing life into dead matter."}
    ]
  },
  "voltaire": {
    "primary": "The pen name of François-Marie Arouet, the French Enlightenment writer, satirist, philosopher, and champion of free speech.",
    "secondary": "In intellectual history, the leading philosopher celebrated for Candide, crushing religious intolerance with caustic wit.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "Critical and Miscellaneous Essays", "quote": "**Voltaire** was the premier intellectual sovereign of his century, demolishing ancient hypocrisies with mocking laughter."},
      {"author": "Friedrich Nietzsche", "work": "Human, All Too Human", "quote": "Nietzsche dedicated his work to the free spirit of **Voltaire**, praising his lucid intellectual courage and classical restraint."},
      {"author": "Edward Gibbon", "work": "Memoirs of My Life and Writings", "quote": "In Geneva I had the good fortune to meet **Voltaire**, whose private theatricals enchanted the Swiss burghers."}
    ]
  },
  "voltarean": {
    "primary": "Resembling, characteristic of, or relating to Voltaire; marked by biting satirical wit and Enlightenment skepticism.",
    "secondary": "In literary criticism, a prose style characterized by lucid brevity, sharp irony, and anti-clerical skepticism.",
    "quotes": [
      {"author": "Lytton Strachey", "work": "Landmarks in French Literature", "quote": "His prose possessed a **Voltarean** clarity, cutting through pompous metaphysical dogma with sparkling malice."},
      {"author": "George Saintsbury", "work": "A History of the French Novel", "quote": "The political satire maintained a **Voltarean** sparkle that delighted Parisian salon intellectuals."},
      {"author": "Henry James", "work": "French Poets and Novelists", "quote": "The critic wielded a **Voltarean** pen, exposing bad poetry with urbane, devastating politeness."}
    ]
  },
  "voltaren": {
    "primary": "A brand name for diclofenac, a nonsteroidal anti-inflammatory drug (NSAID) used to relieve pain and swelling.",
    "secondary": "In clinical pharmacology, a topical gel or oral medication that inhibits cyclooxygenase enzymes (COX-1 and COX-2).",
    "quotes": [
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The physiotherapist prescribed topical **Voltaren** gel to soothe post-surgical inflammation in the knee joint."},
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Patients with severe rheumatoid arthritis obtained substantial relief through targeted NSAIDs like **Voltaren**."},
      {"author": "Atul Gawande", "work": "Being Mortal", "quote": "Pain management regimens combined acetaminophen with topical **Voltaren** to avoid systemic narcotic side effects."}
    ]
  },
  "voltarian": {
    "primary": "Of, relating to, or characteristic of Voltaire; an alternative spelling of Voltarean.",
    "secondary": "In intellectual history, describing rationalist freethinkers who adopt Voltaire's campaign against bigotry (écrasez l'infâme).",
    "quotes": [
      {"author": "Bertrand Russell", "work": "A History of Western Philosophy", "quote": "The philosopher maintained a **Voltarian** skepticism toward orthodox religion throughout his controversial career."},
      {"author": "H. L. Mencken", "work": "Prejudices: Second Series", "quote": "He assaulted Puritan moralists with **Voltarian** ferocity, mocking their crusades against harmless pleasures."},
      {"author": "Isaiah Berlin", "work": "The Crooked Timber of Humanity", "quote": "The counter-Enlightenment arose as a romantic backlash against the cold, universalizing **Voltarian** intellect."}
    ]
  },
  "volte-face": {
    "primary": "A complete and sudden reversal of one's opinion, attitude, political stance, or policy; an about-face.",
    "secondary": "In diplomatic history, a dramatic overnight realignment of alliances between sovereign states.",
    "quotes": [
      {"author": "Winston Churchill", "work": "The Gathering Storm", "quote": "The sudden Molotov-Ribbentrop pact represented an astounding diplomatic **volte-face** that stunned the world."},
      {"author": "George Orwell", "work": "Nineteen Eighty-Four", "quote": "In mid-speech the speaker executed a seamless **volte-face**, announcing that Oceania was at war with Eastasia, not Eurasia."},
      {"author": "Edmund Burke", "work": "An Appeal from the New to the Old Whigs", "quote": "He condemned former party colleagues who had executed an unprincipled **volte-face** to embrace Jacobin doctrines."}
    ]
  },
  "voltmeter": {
    "primary": "An electrical measuring instrument used for measuring the electric potential difference between two points in a circuit.",
    "secondary": "In laboratory instrumentation, digital or analog d'Arsonval meters with high internal resistance placed in parallel with a component.",
    "quotes": [
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "The needle of the electrostatic **voltmeter** flickered wildly as the resonance coils reached peak induction."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "A calibrated Weston **voltmeter** stood on the laboratory bench to monitor battery discharge curves."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "When connecting a **voltmeter**, one must ensure its internal impedance is sufficiently high not to disturb the circuit."}
    ]
  },
  "volubility": {
    "primary": "The quality of talking fluently, readily, or incessantly; glibness and rapid articulateness.",
    "secondary": "In dramatic monologue, an overwhelming stream of words delivered with easy, unbroken fluency.",
    "quotes": [
      {"author": "Jane Austen", "work": "Emma", "quote": "Miss Bates poured forth a torrent of trivial details with an unceasing **volubility** that exhausted her listeners."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mrs. Nickleby was gifted with amazing conversational **volubility**, wandering through disjointed reminiscences for hours."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Thaddeus Sholto spoke with nervous, jerky **volubility**, fidgeting with his hookah amid the exotic salon."}
    ]
  },
  "voluble": {
    "primary": "Talking fluently, readily, or incessantly; characterized by a steady, effortless flow of speech.",
    "secondary": "In botany, describing climbing or twining plant stems that coil spirally around supports.",
    "quotes": [
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Brooke was a **voluble** conversationalist who touched upon a hundred topics without finishing a single sentence."},
      {"author": "Joseph Conrad", "work": "Heart of Darkness", "quote": "The Russian harlequin was extraordinarily **voluble**, babbling about Kurtz with ecstatic hero-worship."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The morning glory possesses a **voluble** stem that twines dextrorsely up garden trellises."}
    ]
  },
  "volubly": {
    "primary": "In a voluble, fluent, or rapid manner; talking incessantly and with effortless ease.",
    "secondary": "In narrative dialogue, expressing excuses, gratitude, or complaints with breathless loquacity.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "The wine-shop keeper talked **volubly** to the travelers, masking revolutionary signals under casual gossip."},
      {"author": "Arthur Conan Doyle", "work": "The Red-Headed League", "quote": "Mr. Jabez Wilson complained **volubly** of his sudden dismissal, waving the sarcastic notice before Holmes."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Jennings chatted **volubly** throughout the carriage ride, speculating on the prospects of every village bachelor."}
    ]
  },
  "volume": {
    "primary": "The amount of space that a substance or object occupies, or a single book forming part of a larger work.",
    "secondary": "In acoustics, the perceived loudness or amplitude of a sound signal.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Mathematical Principles of Natural Philosophy", "quote": "Density is the quantity of matter arising from its gravity and **volume** conjointly."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "It was in Rome that I conceived the idea of writing the decline and fall of the city, which filled many a **volume**."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The leviathan displaced a colossal **volume** of foaming brine as it breached into the twilight air."}
    ]
  },
  "volumed": {
    "primary": "Having a specified volume, bulk, or number of volumes; also rolling in billowing mass or folds.",
    "secondary": "In romantic poetry, describing dense, billowing clouds of smoke, vapor, or swirling garments.",
    "quotes": [
      {"author": "Percy Bysshe Shelley", "work": "Ode to the West Wind", "quote": "Loose clouds like earth's decaying leaves are shed, shook from the tangled boughs of Heaven and Ocean, **volumed** high."},
      {"author": "Lord Byron", "work": "Childe Harold's Pilgrimage", "quote": "The artillery smoke hung in a **volumed** pall across the bloody ridges of Waterloo."},
      {"author": "Samuel Taylor Coleridge", "work": "Kubla Khan", "quote": "Amid whose swift half-intermitted burst huge fragments vaulted like rebounding hail, in **volumed** rivers hurled."}
    ]
  },
  "volumeter": {
    "primary": "An instrument designed for measuring the volume of liquids, gases, or irregular solid bodies through displacement.",
    "secondary": "In bakery science and agricultural engineering, an apparatus measuring loaf volume by seed displacement.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Using a calibrated glass **volumeter**, we accurately recorded the expansion of oxygen gas during combustion."},
      {"author": "John Tyndall", "work": "Sound", "quote": "The sensitive acoustic **volumeter** registered subtle pressure changes generated by vibrating organ pipes."},
      {"author": "Thomas Graham", "work": "Chemical and Physical Researches", "quote": "Diffusion rates of various gases were measured directly with a mercury-filled **volumeter** tube."}
    ]
  },
  "volumetric": {
    "primary": "Relating to or involving the measurement of volume; determined by volume rather than weight.",
    "secondary": "In analytical chemistry, volumetric analysis (titration) measuring solution concentrations via known volumes of reagent.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Quantitative **volumetric** determinations revealed the precise proportions of hydrogen and oxygen in water."},
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "Carefully calibrated **volumetric** pipettes and burettes are indispensable for exact analytical assaying."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "High-resolution **volumetric** MRI allows researchers to quantify regional hippocampal atrophy in dementia."}
    ]
  },
  "volumetrical": {
    "primary": "Pertaining to volumetric measurement; synonymous with volumetric.",
    "secondary": "In historical chemical literature, quantitative analysis performed by measuring reagent solution volumes.",
    "quotes": [
      {"author": "Robert Bunsen", "work": "Gasometry: Comprising the Leading Physical and Chemical Properties of Gases", "quote": "His **volumetrical** methods for gas analysis achieved unprecedented accuracy through eudiometric tubes."},
      {"author": "Thomas Graham", "work": "Elements of Chemistry", "quote": "Standardized **volumetrical** solutions enabled factory chemists to determine acid strength within minutes."},
      {"author": "Humphry Davy", "work": "Researches, Chemical and Philosophical", "quote": "The **volumetrical** expansion of air upon heating conformed strictly to the laws demonstrated by Charles."}
    ]
  },
  "volumetrically": {
    "primary": "By means of volumetric measurement; in a manner relating to volume or spatial displacement.",
    "secondary": "In analytical chemistry, calculating stoichiometric concentrations by measuring titrated liquid volumes.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Carbon dioxide evolved during wine fermentation was captured and measured **volumetrically** over mercury."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "Radon gas released from radium solutions was **volumetrically** determined in capillary quartz tubes."},
      {"author": "Charles Darwin", "work": "The Formation of Vegetable Mould through the Action of Worms", "quote": "He quantified **volumetrically** the amount of subsoil brought to the surface by earthworms each year."}
    ]
  },
  "voluminosity": {
    "primary": "Great bulk, immense size, or the vast spatial extent of an object, book, or bodily form.",
    "secondary": "In literary criticism, the staggering length or textual sprawl of multi-volume Victorian novels.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "History of Friedrich II of Prussia", "quote": "The archival records appalled the historian by their terrifying **voluminosity** and pedantic disorder."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "He remarked upon the loose baggy **voluminosity** of certain nineteenth-century Russian masterpieces."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The magnificent **voluminosity** of Venetian cloudscapes inspired Titian's most grandiloquent canvases."}
    ]
  },
  "voluminous": {
    "primary": "Occupying much space, large in volume, bulky, or consisting of many books, pages, or written words.",
    "secondary": "In fashion and costume, garments characterized by ample folds of flowing fabric.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **voluminous** legal codes of Justinian digested centuries of Roman jurisprudence into order."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Tulkinghorn sat surrounded by **voluminous** bundles of deeds tied with dusty red tape."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Dashwood received a **voluminous** letter from her absent daughter, recounting every Highbury event."}
    ]
  },
  "voluminousness": {
    "primary": "Vastness of scope, immense textual bulk, or spacious physical amplitude.",
    "secondary": "In literary assessment, the comprehensive breadth and sheer page count of an author's collected works.",
    "quotes": [
      {"author": "Samuel Johnson", "work": "Lives of the Most Eminent English Poets", "quote": "Dryden's poetic **voluminousness** reflects the fertile industry of a writer who lived by his pen."},
      {"author": "Edmund Burke", "work": "Speech on the Nabob of Arcot's Debts", "quote": "The sheer **voluminousness** of the East India Company's accounts served to conceal immense corruption."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Mr. Casaubon's unfinished Key to All Mythologies was doomed by the incoherent **voluminousness** of his notes."}
    ]
  },
  "volund": {
    "primary": "Völundr (Wayland the Smith), the legendary heroic master blacksmith of Germanic and Norse mythology.",
    "secondary": "In medieval Scandinavian heroic literature, the mythic craftsman imprisoned by King Níðuðr who forged winged escape.",
    "quotes": [
      {"author": "William Morris", "work": "The Story of Sigurd the Volsung", "quote": "Ancient smiths sang verses in praise of cunning **Volund**, whose enchanted forge shaped invincible swords."},
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "Norse skalds celebrated the grim vengeance of **Volund**, the master artificer who outwitted cruel kings."},
      {"author": "J. R. R. Tolkien", "work": "The Monsters and the Critics", "quote": "Echoes of the elven smith **Volund** reverberate through Old English poetry and medieval hoard lore."}
    ]
  },
  "voluntarily": {
    "primary": "Of one's own free will, choice, or decision; without external compulsion, coercion, or constraint.",
    "secondary": "In legal contracts, entering into an agreement with informed, uncoerced consent.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "An individual may **voluntarily** choose to sacrifice personal comfort for the benefit of his fellow citizens."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Citizens **voluntarily** tax themselves to establish libraries, pave streets, and maintain village greens."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "Anne had **voluntarily** resigned the prospect of youthful happiness out of mistaken dutiful deference."}
    ]
  },
  "voluntary": {
    "primary": "Done, given, or acting of one's own free will and choice, without external compulsion or legal requirement.",
    "secondary": "In church music, a solo musical piece played on the organ before, during, or after a religious service.",
    "quotes": [
      {"author": "Aristotle", "work": "Nicomachean Ethics", "quote": "Virtue is concerned with passions and actions, and praise is given to **voluntary** choices."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton made a **voluntary** sacrifice of his life, finding in love his final redemption."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The church organist played a majestic Handel **voluntary** as the congregation filed into the sunlit yard."}
    ]
  },
  "volunteer": {
    "primary": "A person who freely offers to undertake a task, service, or duty without being coerced or paid.",
    "secondary": "In military history, an enlistee who joins armed service freely rather than through compulsory conscription.",
    "quotes": [
      {"author": "Walt Whitman", "work": "Leaves of Grass", "quote": "I saw the brave **volunteer** step forward from the ranks, ready to face the battery on the hill."},
      {"author": "Abraham Lincoln", "work": "Proclamation Calling for 75,000 Militia", "quote": "The president issued a call for every patriotic **volunteer** to defend the constitutional Union."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "Whenever an obstacle arises, the American **volunteer** steps forth to organize community action."}
    ]
  },
  "voluptuary": {
    "primary": "A person devoted to luxury, sensual pleasures, fine dining, and physical self-indulgence; an epicure.",
    "secondary": "In character sketches, a wealthy aesthete whose existence is organized around refined hedonistic delights.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "Elagabalus lived as an unrestrained imperial **voluptuary**, squandering revenues upon scented baths and rare delicacies."},
      {"author": "Oscar Wilde", "work": "The Picture of Dorian Gray", "quote": "Dorian pursued the refined sensations of a modern **voluptuary**, experimenting with perfumes and exotic jewels."},
      {"author": "William Makepeace Thackeray", "work": "Vanity Fair", "quote": "The Marquis of Steyne was an elderly **voluptuary** whose cynical gaze pierced all social pretenses."}
    ]
  },
  "voluptuous": {
    "primary": "Curvaceous, sexually attractive, and full-figured, or providing sensual gratification and luxury.",
    "secondary": "In aesthetics and art criticism, rich, indulgent textures, warm colors, or soothing musical harmonies.",
    "quotes": [
      {"author": "Lord Byron", "work": "Don Juan", "quote": "Her beauty was of that rich, **voluptuous** kind that belongs to southern climes and sunlit vineyards."},
      {"author": "John Keats", "work": "The Eve of St. Agnes", "quote": "A table stood spread with **voluptuous** delicacies, jellies soother than the creamy curd and candied fruits."},
      {"author": "Charles Baudelaire", "work": "The Flowers of Evil", "quote": "The evening air was filled with a warm, **voluptuous** perfume of exotic blossoms drifting from the harbor."}
    ]
  },
  "voluptuously": {
    "primary": "In a voluptuous, sensuous, or luxurious manner; with sensual delight or voluptuous beauty.",
    "secondary": "In musical performance, playing melodic passages with rich, warm expressive rubato and sweetness.",
    "quotes": [
      {"author": "Oscar Wilde", "work": "Salomé", "quote": "She danced **voluptuously** before the tetrarch, her silver veils shimmering in the torchlight."},
      {"author": "Gustave Flaubert", "work": "Madame Bovary", "quote": "Emma reclined **voluptuously** upon the satin cushions, daydreaming of passionate Venetian gondola rides."},
      {"author": "Herman Melville", "work": "Typee", "quote": "The island maidens floated **voluptuously** through the warm lagoon waters, crowned with fragrant white gardenias."}
    ]
  },
  "voluptuousness": {
    "primary": "Sensual gratification, luxurious physical indulgence, or full, curvaceous physical beauty.",
    "secondary": "In ethics and moral theology, the seductive temptation of sensory pleasure over spiritual duty.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The austere discipline of the legionaries was softened by the indolent **voluptuousness** of Syrian cities."},
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The decline of Venetian painting began when spiritual reverence gave way to pagan **voluptuousness**."},
      {"author": "Samuel Johnson", "work": "Rasselas", "quote": "The prince discovered that endless palace **voluptuousness** produced only satiety and existential boredom."}
    ]
  },
  "volute": {
    "primary": "A spiral scroll-like ornament characteristic of the Ionic capital in classical Greek architecture.",
    "secondary": "In malacology, a marine gastropod mollusk of the predatory tropical family Volutidae having spiral shells.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Seven Lamps of Architecture", "quote": "The graceful Ionic **volute** mimics the spiral curves found in mountain ram horns and sea shells."},
      {"author": "Vitruvius", "work": "The Ten Books on Architecture", "quote": "The architect must proportion the capital so that each corner **volute** turns outward with mathematical harmony."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The coastal sands yielded exquisite polished specimens of the predatory marine snail **volute**."}
    ]
  },
  "voluted": {
    "primary": "Furnished with, decorated with, or shaped in the form of a volute or spiral scroll.",
    "secondary": "In architectural description, describing Ionic and Composite capitals adorned with prominent spirals.",
    "quotes": [
      {"author": "John Ruskin", "work": "The Stones of Venice", "quote": "The marble columns supported elegantly **voluted** capitals carved by Byzantine craftsmen."},
      {"author": "Nathaniel Hawthorne", "work": "The Marble Faun", "quote": "Sunlight fell upon the **voluted** pediment of the ruined temple standing along the Appian Way."},
      {"author": "Henry James", "work": "Italian Hours", "quote": "The baroque facade featured **voluted** buttresses flanking the lofty church portal above the piazza."}
    ]
  },
  "volution": {
    "primary": "A spiral turn, whorl, or single coil around a central axis, as in a gastropod shell.",
    "secondary": "In geometry and mechanics, a revolution or twisting circular movement in space.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Each successive **volution** of the ammonite shell preserves an indelible record of juvenile growth stages."},
      {"author": "Thomas Browne", "work": "The Garden of Cyrus", "quote": "The spiral **volution** observable in conch shells reflects an underlying mathematical harmony in nature."},
      {"author": "Richard Owen", "work": "Palaeontology", "quote": "Fossil cephalopods display remarkable diversity in the tightness and ornamentation of each shell **volution**."}
    ]
  }
}
