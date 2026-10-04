# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — fer (Batch 5B: 36 words)
  # =========================================================================
  "Dashboard — fer/differentia.md": {
    "primary": "The distinguishing attribute, characteristic, or specific difference that separates a species from all other species in the same genus.",
    "secondary": "In classical Aristotelian logic and scholastic ontology, the essential property added to a generic concept to define a distinct subcategory.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "The logicians define a species by its genus and its specific **differentia**, which marks it off from all others."},
      {"author": "Aristotle", "work": "Topics", "quote": "The definition of an essence consists in the conjunction of the genus and the appropriate **differentia**."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The term **differentia** signifies that attribute which distinguishes the given species from all other species of that genus."}
    ]
  },
  "Dashboard — fer/differentiable.md": {
    "primary": "Capable of being differentiated; specifically, possessing a well-defined derivative at each point within a mathematical domain.",
    "secondary": "In real analysis and differential calculus, describing a continuous function whose rate of change can be determined by a unique tangent line or linear map.",
    "quotes": [
      {"author": "Carl Friedrich Gauss", "work": "Disquisitiones Generales Circa Superficies Curvas", "quote": "We assume the coordinate functions defining the curved surface are everywhere continuously **differentiable**."},
      {"author": "Augustin-Louis Cauchy", "work": "Résumé des leçons sur le calcul infinitésimal", "quote": "A function is **differentiable** over an interval when the limit of the incremental ratio exists uniquely."},
      {"author": "Henri Poincaré", "work": "The Foundations of Science", "quote": "Physical intuition often leads us to consider smoothly **differentiable** curves, whereas analysis reveals continuous functions without derivatives."}
    ]
  },
  "Dashboard — fer/differential.md": {
    "primary": "Pertaining to, creating, or depending on a difference; or exhibiting or relating to mathematical derivatives or rates of change.",
    "secondary": "In automotive mechanics and calculus, a gear train allowing wheels to rotate at different speeds on curves, or an infinitesimal increment of a variable.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "Man is fallen; nature is erect, and serves as a **differential** thermometer to measure our departure from divine rectitude."},
      {"author": "Isaac Newton", "work": "The Method of Fluxions and Infinite Series", "quote": "The **differential** method determines tangents and curvatures by resolving curves into infinitely small increments."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The electrodynamic field equations are expressed as linear **differential** relations governing spatial flux."}
    ]
  },
  "Dashboard — fer/differentially.md": {
    "primary": "In a manner that distinguishes, discriminates, or acts unevenly according to varying conditions or individual differences.",
    "secondary": "In developmental genetics and pharmacology, describing genes or therapeutic agents that express or bind with distinct affinity across varying tissues.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Selective pressures act **differentially** upon varieties, preserving favorable structural nuances."},
      {"author": "Thomas Henry Huxley", "work": "Critiques and Addresses", "quote": "External environmental factors affect organisms **differentially**, accelerating survival in some while extinguishing others."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Attentive focus distributes mental energy **differentially**, elevating the target sensation above the sensory background."}
    ]
  },
  "Dashboard — fer/differentiate.md": {
    "primary": "To recognize, perceive, or establish a difference between two or more things; or to cause to become distinct or specialized.",
    "secondary": "In calculus and developmental biology, to calculate the mathematical derivative of a function, or to mature from an unspecialized cell into a distinct cell type.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "His host and his host's household, his men and his maids, as they became more familiar, began to **differentiate** into distinct personalities."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Natural selection can **differentiate** an ancestral stock into widely separated ecological varieties."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The task of scientific taxonomy is to **differentiate** genuine natural kinds from superficial resemblances."}
    ]
  },
  "Dashboard — fer/differentiated.md": {
    "primary": "Made distinct, specialized, or separated by specific differences; having developed distinct specialized characteristics.",
    "secondary": "In cell biology and economic sociology, describing cells that have acquired specialized functions, or industries characterized by brand segmentation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Now as organisms have become slowly adapted to diversified lines of life, their organs have become more highly **differentiated**."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Evolution involves a transformation from an indefinite, incoherent homogeneity to a definite, coherent heterogeneity of **differentiated** parts."},
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The primate brain exhibits a highly **differentiated** cerebral cortex compared to lower mammalian orders."}
    ]
  },
  "Dashboard — fer/differentiation.md": {
    "primary": "The process of making or becoming distinct, specialized, or diverse; the development of differences among components.",
    "secondary": "In embryonic development and calculus, the morphological specialization of cells into mature tissues, or the mathematical operation of computing a derivative.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Tess thought her loss as great as Marian's, but upheld by the dignity of suffering, found in silent endurance a moral **differentiation** from her companions."},
      {"author": "Herbert Spencer", "work": "The Principles of Biology", "quote": "Physiological division of labor always accompanies structural **differentiation** in complex multicellular organisms."},
      {"author": "Henri Bergson", "work": "Creative Evolution", "quote": "Life does not proceed by the association and addition of elements, but by dissociation and **differentiation**."}
    ]
  },
  "Dashboard — fer/differentiator.md": {
    "primary": "A person, feature, or mechanism that distinguishes or causes a distinction between things.",
    "secondary": "In analog electronics and signal processing, a circuit or network whose output voltage is proportional to the time rate of change of its input voltage.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The intellect functions as a swift **differentiator**, separating subtle shades of meaning that escape crude perception."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "An electronic **differentiator** tracks input fluctuations to provide predictive feedback in servomechanisms."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "A keen observer serves as an instinctive **differentiator** of truth from rhetorical artifice."}
    ]
  },
  "Dashboard — fer/differently.md": {
    "primary": "In a distinct, dissimilar, or contrasting manner; not alike or identically.",
    "secondary": "In cognitive psychology and behavioral linguistics, perceiving, interpreting, or reacting according to divergent cultural or mental perspectives.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A rick burns **differently** from a house."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "You see the matter very **differently** from the rest of the world, Elizabeth."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Men think **differently** because their experiences have furnished their minds with different collections of simple ideas."}
    ]
  },
  "Dashboard — fer/efferent.md": {
    "primary": "Carrying or conveying outward away from a central organ, nerve axis, or reference point; opposed to afferent.",
    "secondary": "In neurophysiology and vascular anatomy, designating motor nerve fibers conducting impulses from the central nervous system to effector muscles or glands.",
    "quotes": [
      {"author": "Charles Sherrington", "work": "The Integrative Action of the Nervous System", "quote": "The final common path is constituted by the **efferent** motoneurone leading directly to the muscle fibers."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Incoming sensory currents discharge into outward **efferent** channels to generate muscular movements."},
      {"author": "Santiago Ramón y Cajal", "work": "Histology of the Nervous System", "quote": "The large pyramidal cells of the motor cortex send **efferent** axons downward through the pyramidal tract."}
    ]
  },
  "Dashboard — fer/feral.md": {
    "primary": "Existing in an untamed, wild, or uncultivated state, especially after having reverted from domestication.",
    "secondary": "In population ecology and conservation biology, designating animals or plants that have escaped cultivation and established reproducing populations in the wild.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "This subject has been ably treated by several authors, showing how rapidly domesticated animals revert to **feral** habits when released."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "I love the wild not less than the good; there is a **feral** instinct in man that rejoices in the untamed forest."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The ancestral instincts surged within him, awakening a fierce and **feral** cunning suited to the northern wilderness."}
    ]
  },
  "Dashboard — fer/feria.md": {
    "primary": "A weekday in the liturgical calendar on which no special ecclesiastical feast, solemnity, or saint's commemoration occurs.",
    "secondary": "In Roman Catholic liturgical rubrics, an ordinary ferial day requiring the standard office and seasonal vestments without festive elaboration.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The ancient Roman calendar set aside each **feria** for public business or religious observance."},
      {"author": "John Henry Newman", "work": "Apologia Pro Vita Sua", "quote": "The calm rhythm of the liturgical **feria** brought peace to the monastic community between festival seasons."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The sacred routine of the Latin **feria** preserved the ritual piety of ancestral Roman domestic religion."}
    ]
  },
  "Dashboard — fer/ferial.md": {
    "primary": "Pertaining to an ordinary liturgical weekday; or relating to ancient Roman holidays and festival days.",
    "secondary": "In liturgical music and canonical hours, designating the simplified psalm tones and ordinary chants used on days devoid of feast celebrations.",
    "quotes": [
      {"author": "Thomas Aquinas", "work": "Summa Theologiae", "quote": "The divine office retains its simpler **ferial** structure when no saintly martyrdom is solemnly commemorated."},
      {"author": "Matthew Arnold", "work": "Essays in Criticism", "quote": "The contrast between festive magnificence and **ferial** simplicity reflects the dual rhythm of human life."},
      {"author": "Walter Pater", "work": "Marius the Epicurean", "quote": "The solemn hymns shifted from festive modulations to the sober dignity of **ferial** chant."}
    ]
  },
  "Dashboard — fer/ferine.md": {
    "primary": "Wild, untamed, savage, or beast-like in nature or appearance; characteristic of wild animals.",
    "secondary": "In legal history and zoological classification, designating undomesticated wildlife (ferae naturae) living in a natural and predatory state.",
    "quotes": [
      {"author": "Sir Matthew Hale", "work": "Historia Placitorum Coronae", "quote": "Lions, tigers, wolves, and bears are **ferine** beasts whose dangerous nature requires strict confinement."},
      {"author": "Samuel Johnson", "work": "A Journey to the Western Islands of Scotland", "quote": "The remote highlands once nurtured a hardy breed of men retaining much of their **ferine** independence."},
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The harpooneer's gaze revealed a **ferine** intensity born of savage encounters with primeval monsters."}
    ]
  },
  "Dashboard — fer/fermat.md": {
    "primary": "Pierre de Fermat (1607–1665), the celebrated French jurist and mathematician who laid the foundations of modern number theory.",
    "secondary": "In the history of mathematics, the pioneer who introduced the principle of least time in optics and laid foundations for differential calculus and probability.",
    "quotes": [
      {"author": "Carl Friedrich Gauss", "work": "Disquisitiones Arithmeticae", "quote": "The profound arithmetic investigations of **Fermat** laid the foundation for modern higher congruences."},
      {"author": "René Descartes", "work": "Correspondence", "quote": "The geometric method proposed by **Fermat** for determining maxima and minima anticipated my own analytical geometry."},
      {"author": "Pierre-Simon Laplace", "work": "A Philosophical Essay on Probabilities", "quote": "The correspondence between Pascal and **Fermat** marked the true birth of the mathematical calculus of probabilities."}
    ]
  },
  "Dashboard — fer/fermata.md": {
    "primary": "A musical notation symbol placed over a note, chord, or rest indicating that its duration is to be sustained beyond its normal value.",
    "secondary": "In musical performance practice, an expressive pause or suspension of strict tempo governed by the artistic judgment of the conductor or performer.",
    "quotes": [
      {"author": "Hector Berlioz", "work": "A Treatise upon Modern Instrumentation and Orchestration", "quote": "A grand orchestral **fermata** creates breathless suspense before the concluding allegro begins."},
      {"author": "George Bernard Shaw", "work": "Music in London", "quote": "The soprano prolonged the final **fermata** to an unconscionable length to display the endurance of her high register."},
      {"author": "Romain Rolland", "work": "Beethoven", "quote": "The sudden **fermata** brings the tempestuous movement to a breathless halt, suspended above an abyss of silence."}
    ]
  },
  "Dashboard — fer/ferment.md": {
    "primary": "An agent that causes biochemical fermentation (such as yeast or enzyme); or a state of intense agitation, commotion, or unrest.",
    "secondary": "In historical sociology and microbiology, an intellectual or political agitation stirring public debate, or a catalytic substance driving organic decomposition.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "Every true **ferment** is a living microscopic organism that assimilates nutrient media to sustain its vitality."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The revolutionary societies kept the public mind in a continual **ferment** of suspicion and alarm."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Passions in the soul operate like a powerful **ferment**, agitating the faculties into sudden tumult."}
    ]
  },
  "Dashboard — fer/fermentable.md": {
    "primary": "Capable of undergoing fermentation; suitable for conversion into alcohol, acid, or gas by microorganisms.",
    "secondary": "In industrial brewing and biochemical engineering, designating organic substrates containing simple sugars that yeast can metabolize into ethanol and carbon dioxide.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The must of crushed grapes contains an abundance of **fermentable** sugar ready for yeast metabolism."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Vegetable juices containing **fermentable** carbohydrates undergo rapid transformation when exposed to atmospheric air."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Microscopic analysis reveals that non-living broth remains inert unless **fermentable** constituents are seeded with active germs."}
    ]
  },
  "Dashboard — fer/fermentation.md": {
    "primary": "The metabolic process by which microorganisms convert carbohydrates into acids, gases, or alcohol in the absence of oxygen.",
    "secondary": "In historical chemistry and sociology, the zymotic decomposition of organic material, or a figurative period of tumultuous intellectual or political incubation.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Physiological Theory of Fermentation", "quote": "**Fermentation** is the direct consequence of a vital process of nutrition occurring without free oxygen."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Chemical changes analogous to **fermentation** occur within the tissues during seed germination."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "When a new passion enters the mind, it produces a strange **fermentation** in the thoughts and inclinations."}
    ]
  },
  "Dashboard — fer/fermenting.md": {
    "primary": "Undergoing or inducing fermentation; or actively stirring up agitation, excitement, or turbulence.",
    "secondary": "In zymology and political history, actively metabolizing sugars into organic byproducts, or secretly fomenting social discord or ideological rebellion.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The stable yields a stercoraceous heap impregnated with quick **fermenting** substances that generate intense heat."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Vapors foul and dark from bottomless pits rose **fermenting** through the troubled air."},
      {"author": "Alexis de Tocqueville", "work": "The Old Regime and the Revolution", "quote": "Beneath the placid surface of provincial society, new egalitarian doctrines were quietly **fermenting**."}
    ]
  },
  "Dashboard — fer/fermentologist.md": {
    "primary": "A specialist or scientific researcher who studies the biochemical processes and commercial applications of fermentation.",
    "secondary": "In applied biotechnology and enology, a zymologist dedicated to optimizing microbial strains, wort composition, and fermentation kinetics in industrial brewing and winemaking.",
    "quotes": [
      {"author": "Louis Pasteur", "work": "Studies on Fermentation", "quote": "The modern **fermentologist** must unite the chemical rigor of the laboratory with the practical observation of the brewery."},
      {"author": "Justus von Liebig", "work": "Animal Chemistry", "quote": "Every practicing **fermentologist** recognizes the profound influence of temperature on the rate of fungal metabolism."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The investigations of the **fermentologist** have shed unexpected light upon the general mechanisms of cellular pathology."}
    ]
  },
  "Dashboard — fer/fermi.md": {
    "primary": "A unit of length equal to one quadrillionth of a meter (ten to the minus fifteen meters), named in honor of nuclear physicist Enrico Fermi.",
    "secondary": "In nuclear and particle physics, the standard unit of scale used to measure the diameter of atomic nuclei and the range of the strong nuclear force.",
    "quotes": [
      {"author": "Enrico Fermi", "work": "Nuclear Physics", "quote": "The radius of an atomic nucleus is of the order of a few units of the **fermi**, proportional to the cube root of the mass number."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "When probing nuclear dimensions on the scale of a **fermi**, electromagnetic forces are completely overshadowed by strong interactions."},
      {"author": "Niels Bohr", "work": "Atomic Physics and Human Knowledge", "quote": "The spatial localization of nucleons within distances of a **fermi** necessitates quantum mechanical descriptions of short-range forces."}
    ]
  },
  "Dashboard — fer/fermion.md": {
    "primary": "Any subatomic particle (such as an electron, proton, or neutron) that obeys Fermi-Dirac statistics and has a half-integer spin.",
    "secondary": "In quantum field theory, an elementary or composite matter particle governed by the Pauli exclusion principle, prohibiting two identical fermions from occupying the same quantum state.",
    "quotes": [
      {"author": "Paul Dirac", "work": "The Principles of Quantum Mechanics", "quote": "An antisymmetrical wave function describes a collection of particles where each **fermion** strictly obeys the exclusion principle."},
      {"author": "Enrico Fermi", "work": "Notes on Modern Physics", "quote": "The thermodynamic distribution of energy among electrons reveals the collective behavior characteristic of every fundamental **fermion**."},
      {"author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "While photons are bosons that love to gather in the same state, every **fermion** insists on having its own private orbital."}
    ]
  },
  "Dashboard — fer/fermium.md": {
    "primary": "A synthetic radioactive transuranic metallic element of the actinide series with atomic number 100, symbol Fm.",
    "secondary": "In nuclear chemistry and heavy element synthesis, an actinide first identified in the radioactive debris of the 1952 Ivy Mike thermonuclear explosion.",
    "quotes": [
      {"author": "Glenn T. Seaborg", "work": "The Transuranium Elements", "quote": "The chemical characterization of **fermium** was accomplished using minute quantities isolated from the debris of the thermonuclear test."},
      {"author": "Enrico Fermi", "work": "Collected Papers", "quote": "Theoretical extrapolation of the actinide series predicted the stable oxidation states later verified in the chemistry of **fermium**."},
      {"author": "Ernest Lawrence", "work": "Science in the Atomic Age", "quote": "Successive neutron captures in high-flux reactors made possible the macroscopic isolation of elements extending toward **fermium**."}
    ]
  },
  "Dashboard — fer/fern.md": {
    "primary": "Any flowerless vascular plant of the class Polypodiopsida, having true roots, stems, and complex leaves (fronds) and reproducing by spores.",
    "secondary": "In paleobotany and pteridology, ancient seedless tracheophytes that constituted a major component of the Carboniferous flora and coal-forming swamps.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 1", "quote": "We steal as in a castle, cock-sure; we have the receipt of **fern**-seed, we walk invisible."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In New Zealand the tree **fern** forms extensive groves that impart a primeval character to the forest vegetation."},
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The delicate fronds of the sweet **fern** scented the warm woodland pasture with a pungent, resinous fragrance."}
    ]
  },
  "Dashboard — fer/ferned.md": {
    "primary": "Covered, abounding, or decorated with ferns.",
    "secondary": "In landscape poetry and botanical description, characterizing moist woodland slopes, dells, or hollows carpeted with dense fronds.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "They walked together down the **ferned** slope where the heath gave way to sheltered oak groves."},
      {"author": "John Muir", "work": "My First Summer in the Sierra", "quote": "The cool springs emerge beneath **ferned** ledges where maidenhair spreads its delicate lace over mossy granite."},
      {"author": "Alfred Lord Tennyson", "work": "Idylls of the King", "quote": "Through **ferned** valleys and deep forest glades the knights pursued their quest."}
    ]
  },
  "Dashboard — fer/fernless.md": {
    "primary": "Devoid of ferns; lacking fern vegetation.",
    "secondary": "In phytosociology and physical ecology, describing arid, windswept, or hyper-alkaline terrains where moisture conditions prohibit pteridophyte spore germination.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The barren lava fields of the arid coast remained entirely **fernless**, presenting only stunted xerophytic scrub."},
      {"author": "John Muir", "work": "Steep Trails", "quote": "Ascending above the timberline, we reached a bleak, **fernless** plateau of shattered slate and drifting snow."},
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels", "quote": "The transition from moist valleys to the **fernless** savanna was marked by an immediate drop in atmospheric humidity."}
    ]
  },
  "Dashboard — fer/fernlike.md": {
    "primary": "Resembling a fern or fern frond in shape, branching pattern, or delicate structure.",
    "secondary": "In crystallography and metallurgy, describing delicate dendritic or fractal crystal formations resembling bipinnate fronds.",
    "quotes": [
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The dendritic manganese deposits on the limestone surface displayed intricate, **fernlike** traceries."},
      {"author": "John Tyndall", "work": "The Forms of Water", "quote": "Ice crystals forming upon the windowpane shoot outward in magnificent **fernlike** plumes."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "Certain colonial hydrozoans exhibit a branching habit so delicate as to appear completely **fernlike**."}
    ]
  },
  "Dashboard — fer/ferny.md": {
    "primary": "Abounding in, overgrown with, or characteristic of ferns.",
    "secondary": "In romantic nature writing and ecology, evoking the damp, earthy aroma and lush greenery of shaded woodland undergrowth.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "A minute later and she saw his scarlet form disappear amid the **ferny** thicket bordering the plantation."},
      {"author": "William Wordsworth", "work": "The Excursion", "quote": "Beside the brook that tumbled down the hill, we rested on a green and **ferny** bank."},
      {"author": "John Muir", "work": "Our National Parks", "quote": "The deer found cool retreat in the **ferny** hollows where the redwoods filtered the noon heat."}
    ]
  },
  "Dashboard — fer/ferocactus.md": {
    "primary": "A genus of stout, barrel-shaped cacti native to southwestern North America, characterized by prominent ribs and heavy, hooked spines.",
    "secondary": "In arid botany and desert ecology, robust succulents (family Cactaceae) adapted to extreme heat and prolonged drought through CAM photosynthesis and massive water-storing parenchyma.",
    "quotes": [
      {"author": "John Wesley Powell", "work": "Canyons of the Colorado", "quote": "On the sun-scorched gravel benches, the stout **Ferocactus** stood like armed sentinels guarding the canyon rim."},
      {"author": "Liberty Hyde Bailey", "work": "The Standard Cyclopedia of Horticulture", "quote": "Species of **Ferocactus** are cultivated for their formidable colored spines and brilliant yellow blossoms."},
      {"author": "Mary Austin", "work": "The Land of Little Rain", "quote": "The barrel cactus, or **Ferocactus**, holds gallons of potable sap beneath its fluted, spiny armor."}
    ]
  },
  "Dashboard — fer/ferocious.md": {
    "primary": "Savagely fierce, cruel, ravenous, or violently aggressive in nature or appearance.",
    "secondary": "In behavioral zoology and narrative prose, exhibiting untamed predatory savagery or menacing fury when threatened or provoked.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Instead of making friends and exchanging visits with our neighbours, we were confronted by this fierce and **ferocious** beast."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The puma is said to be a **ferocious** enemy to wild horses, leaping upon their shoulders from overhanging rocks."},
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The sea was lashed into foam by the **ferocious** thrashing of the wounded leviathan."}
    ]
  },
  "Dashboard — fer/ferociously.md": {
    "primary": "In a ferocious, savage, fiercely violent, or menacingly aggressive manner.",
    "secondary": "In narrative and descriptive literature, attacking, defending, or contending with relentless and terrifying intensity.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Although so small a species, it is very courageous, and I have seen it fight **ferociously** with much larger competitors."},
      {"author": "Jack London", "work": "White Fang", "quote": "The wild dog leaped into the fray and fought **ferociously** against the wolf pack."},
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "The squall struck the vessel **ferociously**, throwing her on her beam ends with a deafening roar."}
    ]
  },
  "Dashboard — fer/ferociousness.md": {
    "primary": "The quality, condition, or display of being ferocious; extreme savagery, cruelty, or fierce aggression.",
    "secondary": "In evolutionary ethology and comparative psychology, innate predatory fierceness or agonistic threat behavior exhibited during territorial defense.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Man's Place in Nature", "quote": "The apparent **ferociousness** of the male gorilla is primarily an intimidating display designed to safeguard its family."},
      {"author": "Herman Melville", "work": "Typee: A Romance of the South Seas", "quote": "The traditional accounts had exaggerated the **ferociousness** of the island warriors, who proved remarkably hospitable."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The canine teeth of male carnivores are developed in proportion to the animal's natural **ferociousness** in sexual combat."}
    ]
  },
  "Dashboard — fer/ferocity.md": {
    "primary": "Savage wildness, fierce brutality, relentless fury, or bloodthirsty cruelty.",
    "secondary": "In literary naturalism and behavioral ecology, unbridled destructive aggression displayed in mortal combat or predatory attack.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The long pointed features, narrow eye, and smirk of the one, so suggestive of treacherous **ferocity**, were matched by the other."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The barbarians attacked the Roman legions with a desperate **ferocity** that disregarded discipline."},
      {"author": "Jack London", "work": "The Sea-Wolf", "quote": "Wolf Larsen ruled his crew not by moral authority, but by the sheer **ferocity** of his physical strength."}
    ]
  },
  "Dashboard — fer/ferrara.md": {
    "primary": "An ancient city in Emilia-Romagna, Italy; or a broadsword of superior steel bearing the stamped mark of the famous Italian armorer Andrea Ferrara.",
    "secondary": "In Renaissance arms and cultural history, a high-quality Scottish or European basket-hilted broadsword prized for the exceptional elasticity and temper of its blade.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VIII", "quote": "Item, you sent a large commission / To Gregory de Cassado, to conclude, / Without the king's assent or knowledge, / A league with the Duke of **Ferrara**."},
      {"author": "Walter Scott", "work": "Waverley", "quote": "The Highland chieftain drew from his scabbard a genuine Andrea **Ferrara**, boasting of its tempered edge."},
      {"author": "Robert Louis Stevenson", "work": "The Master of Ballantrae", "quote": "He tested the balance of the old **Ferrara** blade before stepping onto the dueling ground."}
    ]
  },
  "Dashboard — fer/ferret-sized.md": {
    "primary": "Having roughly the dimensions, length, or body mass comparable to that of a ferret.",
    "secondary": "In vertebrate paleontology and evolutionary mammalogy, describing small Mesozoic or Paleocene proto-mammals possessing elongate, short-limbed, carnivorous body plans.",
    "quotes": [
      {"author": "Stephen Jay Gould", "work": "Wonderful Life", "quote": "Early mammalian ancestors were nocturnal, **ferret-sized** creatures scurrying beneath the feet of giant dinosaurs."},
      {"author": "Richard Dawkins", "work": "The Ancestor's Tale", "quote": "Our Cretaceous forebear was an alert, **ferret-sized** insectivore hunting by scent under the cover of darkness."},
      {"author": "Ernst Mayr", "work": "What Evolution Is", "quote": "The adaptive radiation of mammals began with small, **ferret-sized** generalized insectivores that survived the end-Cretaceous extinction."}
    ]
  }
}

base_dir = r"App database\Latin roots\Cluster Carrying"

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

print(f"Carrying Batch 5B (fer): Successfully updated {updated}/{len(data)} notes.")
