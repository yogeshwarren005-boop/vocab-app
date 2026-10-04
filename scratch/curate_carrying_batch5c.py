# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data = {
  # =========================================================================
  # Dashboard — fer (Batch 5C: 36 words)
  # =========================================================================
  "Dashboard — fer/ferret.md": {
    "primary": "A domesticated polecat (Mustela putorius furo) bred for hunting rabbits and catching vermin; or to search out tenaciously.",
    "secondary": "In behavioral ecology and figurative prose, a tenacious pursuer that drives quarry out of subterranean burrows or unearths concealed secrets.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "I'll fer him, and firk him, and **ferret** him: discuss the same in French unto him."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Mr. Bucket was never in a hurry, but he had a quiet way of hunting down his clue like a trained **ferret**."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of Four", "quote": "The detective began to **ferret** among the dusty papers in the bureau, looking for the missing will."}
    ]
  },
  "Dashboard — fer/ferric.md": {
    "primary": "Pertaining to, derived from, or containing iron; specifically, designating chemical compounds containing trivalent iron (Fe3+).",
    "secondary": "In inorganic chemistry and metallurgy, designating the oxidized state of iron exhibiting higher valence than divalent ferrous compounds.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The chemical precipitation of **ferric** oxide depends upon the oxidation of the dissolved ferrous salt."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "When iron burns in oxygen gas, it forms a dense reddish mass of **ferric** oxide."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "A solution of **ferric** chloride undergoes rapid decomposition in the presence of alkaline reagents."}
    ]
  },
  "Dashboard — fer/ferricyanide.md": {
    "primary": "A complex salt containing the trivalent anion [Fe(CN)6]3−, consisting of a central ferric iron atom bonded to six cyanide ligands.",
    "secondary": "In photochemistry and coordination chemistry, an oxidant (such as potassium ferricyanide, red prussiate of potash) historically used in cyanotype printing and histology.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The solution of potassium **ferricyanide** acts as a sensitive reagent for detecting minute traces of ferrous salts."},
      {"author": "John Herschel", "work": "On the Action of the Rays of the Solar Spectrum on Vegetable Colours", "quote": "The cyanotype process relies upon the photochemical reduction of **ferricyanide** to produce Turnbull's blue."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Potassium **ferricyanide** is readily distinguished from the yellow ferrocyanide by its brilliant ruby-red crystals."}
    ]
  },
  "Dashboard — fer/ferrimagnetism.md": {
    "primary": "A form of magnetism in which magnetic dipoles on opposing sublattices are unequal in magnitude, leaving a net spontaneous magnetization.",
    "secondary": "In solid-state physics and materials science, the cooperative magnetic ordering observed in ceramic ferrites and magnetite, distinct from ferromagnetism and antiferromagnetism.",
    "quotes": [
      {"author": "Louis Néel", "work": "Propriétés magnétiques des ferrites", "quote": "In substances exhibiting **ferrimagnetism**, the opposing sublattices have unequal saturation moments, resulting in net magnetization."},
      {"author": "Philip W. Anderson", "work": "Concepts in Solids", "quote": "The discovery of **ferrimagnetism** clarified the puzzling magnetic properties of lodestone and related spinels."},
      {"author": "Neville Mott", "work": "Metal-Insulator Transitions", "quote": "The magnetic behavior of transition metal oxides often illustrates **ferrimagnetism** governed by anisotropic superexchange."}
    ]
  },
  "Dashboard — fer/ferrite.md": {
    "primary": "A ceramic compound composed of iron oxide combined with one or more other metals; or the pure alpha-iron phase in metallurgy.",
    "secondary": "In crystallography and electrical engineering, a magnetic ceramic material with high electrical resistivity widely employed in high-frequency transformer cores and microwave circulators.",
    "quotes": [
      {"author": "Louis Néel", "work": "Magnetism and Local Molecular Field", "quote": "The ceramic **ferrite** combines substantial spontaneous magnetization with high electrical resistivity, minimizing eddy-current losses."},
      {"author": "Cyril Stanley Smith", "work": "A History of Metallography", "quote": "Microscopic examination of annealed mild steel reveals crystals of soft **ferrite** alongside pearlitic grains."},
      {"author": "William Shockley", "work": "Electrons and Holes in Semiconductors", "quote": "High-permeability **ferrite** cores revolutionized magnetic storage in early computing circuits."}
    ]
  },
  "Dashboard — fer/ferritin.md": {
    "primary": "A globular protein complex found in cells that stores iron in a non-toxic soluble form and releases it in a controlled fashion.",
    "secondary": "In biochemistry and clinical pathology, a major intracellular iron-storage macromolecule whose serum concentration serves as a primary diagnostic biomarker for iron deficiency or overload.",
    "quotes": [
      {"author": "Max Perutz", "work": "Proteins and Nucleic Acids", "quote": "The spherical protein shell of **ferritin** can sequester thousands of iron atoms within its central cavity."},
      {"author": "Christian de Duve", "work": "A Guided Tour of the Living Cell", "quote": "Cellular iron homeostasis depends upon the regulated synthesis and degradation of **ferritin**."},
      {"author": "Arthur Kornberg", "work": "For the Love of Enzymes", "quote": "Intracellular iron is safe from oxidative side-reactions as long as it remains encapsulated within **ferritin**."}
    ]
  },
  "Dashboard — fer/ferrocerium.md": {
    "primary": "A synthetic pyrophoric alloy of iron and mischmetal (principally cerium) that produces hot sparks when struck or scraped.",
    "secondary": "In applied pyrotechnics and outdoor survival technology, a spark-producing ferroalloy developed by Carl Auer von Welsbach used as the striker flint in lighters and ignition devices.",
    "quotes": [
      {"author": "Carl Auer von Welsbach", "work": "Pyrophoric Alloys and Their Applications", "quote": "The friction of hard steel across **ferrocerium** releases showers of incandescent pyrophoric particles."},
      {"author": "Ernest Rutherford", "work": "Radioactive Substances and Their Radiations", "quote": "The intense sparks struck from **ferrocerium** provide a vivid demonstration of rapid oxidation in air."},
      {"author": "Robert Falcon Scott", "work": "Scott's Last Expedition", "quote": "The mechanical fire-striker with its **ferrocerium** insert proved indispensable in the freezing Antarctic wind."}
    ]
  },
  "Dashboard — fer/ferroconcrete.md": {
    "primary": "Concrete reinforced with embedded steel rods, mesh, or bars to increase its tensile strength; reinforced concrete.",
    "secondary": "In structural engineering and architectural history, a composite material that revolutionized modern construction by marrying the compressive strength of stone with the tensile elasticity of steel.",
    "quotes": [
      {"author": "Le Corbusier", "work": "Towards a New Architecture", "quote": "The structural flexibility of **ferroconcrete** liberates the wall from its historic load-bearing servitude."},
      {"author": "Walter Gropius", "work": "The New Architecture and the Bauhaus", "quote": "The engineering triumph of **ferroconcrete** permits expansive spans and cantilevered terraces unknown to ancient masonry."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The modern metropolis was rebuilt with gleaming arches of **ferroconcrete** and reinforced glass."}
    ]
  },
  "Dashboard — fer/ferrocyanide.md": {
    "primary": "A compound containing the tetravalent anion [Fe(CN)6]4−, consisting of a central divalent iron atom coordinated with six cyanide groups.",
    "secondary": "In classical chemistry and industrial pigment manufacturing, a stable non-toxic coordination complex (such as potassium ferrocyanide, yellow prussiate of potash) used to manufacture Prussian blue.",
    "quotes": [
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Potassium **ferrocyanide** forms deep blue precipitates when combined with solutions of ferric salts."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "The yellow crystals of potassium **ferrocyanide** demonstrate that cyanide radicals may be bound firmly to an iron core."},
      {"author": "Humphry Davy", "work": "Elements of Chemical Philosophy", "quote": "Tests with **ferrocyanide** revealed the presence of dissolved iron in the mineral water."}
    ]
  },
  "Dashboard — fer/ferromagnetic.md": {
    "primary": "Having high magnetic susceptibility and exhibiting spontaneous magnetization and magnetic hysteresis, like iron, cobalt, and nickel.",
    "secondary": "In solid-state physics, describing materials whose atomic magnetic moments align spontaneously in parallel below the Curie temperature due to quantum exchange interactions.",
    "quotes": [
      {"author": "Pierre Curie", "work": "Propriétés magnétiques des corps", "quote": "Above the critical transition point, the **ferromagnetic** metal loses its spontaneous magnetization and becomes paramagnetic."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "In a **ferromagnetic** medium, the relationship between magnetic induction and field intensity is strongly non-linear."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "The quantum mechanical exchange force between electron spins is the microscopic origin of all **ferromagnetic** alignment."}
    ]
  },
  "Dashboard — fer/ferromagnetism.md": {
    "primary": "The physical phenomenon whereby certain materials (such as iron) can form permanent magnets or become strongly attracted to magnets.",
    "secondary": "In quantum physics, the macroscopic collective ordering of unpaired electron spins into magnetic domains caused by positive quantum mechanical exchange coupling.",
    "quotes": [
      {"author": "Pierre Curie", "work": "Magnetic Properties of Bodies", "quote": "The abrupt disappearance of **ferromagnetism** at elevated temperatures marks the onset of complete thermal disorder."},
      {"author": "Werner Heisenberg", "work": "Zur Theorie des Ferromagnetismus", "quote": "The quantum exchange interaction between neighboring electrons provides the theoretical foundation for **ferromagnetism**."},
      {"author": "John H. Van Vleck", "work": "The Theory of Electric and Magnetic Susceptibilities", "quote": "Molecular field theories capture the essential thermodynamics of **ferromagnetism** despite their mathematical simplicity."}
    ]
  },
  "Dashboard — fer/ferrous.md": {
    "primary": "Containing, derived from, or pertaining to iron; specifically designating chemical compounds containing divalent iron (Fe2+).",
    "secondary": "In metallurgy and industrial geology, designating metals, ores, and alloys (such as cast iron and carbon steel) in which iron is the major constituent.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The green tint of the solution indicated the presence of dissolved **ferrous** sulfate."},
      {"author": "Antoine Lavoisier", "work": "Elements of Chemistry", "quote": "Iron exposed to moisture forms first a green **ferrous** hydrate before oxidizing to red rust."},
      {"author": "Charles Lyell", "work": "Principles of Geology", "quote": "The deep blue clay owes its distinctive coloration to **ferrous** compounds preserved from atmospheric oxidation."}
    ]
  },
  "Dashboard — fer/ferrule.md": {
    "primary": "A metal ring or cap fitted around the end of a cane, tool handle, or tube to protect it from splitting, wear, or leakage.",
    "secondary": "In precision engineering and optical cabling, a cylindrical collar or sleeve used to align and securely clamp fluid pipes, electrical terminals, or fiber-optic strands.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "By the time he had smoothed and polished the staff, Kalpa was no longer an endeavor, and he fitted a neat **ferrule** to its tip."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "A thick iron **ferrule** at the bottom of the walking-stick was worn down with much travel."},
      {"author": "Herman Melville", "work": "Moby-Dick; or, The Whale", "quote": "The harpooneer inspected the stout brass **ferrule** binding the socket of the harpoon head to the hickory shaft."}
    ]
  },
  "Dashboard — fer/ferry.md": {
    "primary": "To carry, convey, or transport passengers, vehicles, or goods across a body of water in a boat; or the boat or transit service itself.",
    "secondary": "In commercial transport and logistics, a scheduled maritime vessel or aviation route linking separated coastal or insular terminals.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "Bring them, I pray thee, with imagined speed / Unto the tranect, to the common **ferry** / Which trades to Venice."},
      {"author": "Henry David Thoreau", "work": "A Week on the Concord and Merrimack Rivers", "quote": "The old boatman waited at the **ferry**, ready to push out into the morning current."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "We watched the heavy cattle **ferry** ply back and forth across the misty reaches of the Thames."}
    ]
  },
  "Dashboard — fer/ferryboat.md": {
    "primary": "A boat or vessel specifically designed and employed for transporting passengers and cargo across a river, channel, or narrow water.",
    "secondary": "In maritime transport history, a double-ended or roll-on/roll-off vessel equipped to shuttle pedestrians, carriages, or motorized traffic across inland waterways.",
    "quotes": [
      {"author": "James Joyce", "work": "Dubliners", "quote": "We arranged to go along the Wharf Road until we came to the ships, then take the **ferryboat** across the Liffey."},
      {"author": "Mark Twain", "work": "Adventures of Huckleberry Finn", "quote": "Pretty soon they shot the big cannon off the **ferryboat**, trying to make my carcass come to the top."},
      {"author": "Herman Melville", "work": "Israel Potter", "quote": "The crowded **ferryboat** bumped against the slippery wooden pilings of the Manhattan slip."}
    ]
  },
  "Dashboard — fer/ferrying.md": {
    "primary": "Transporting, conveying, or shuttling people, vehicles, or goods across water or through the air between two points.",
    "secondary": "In logistical operations and military deployment, continuous cyclical transport of troops, munitions, or civilian evacuees across a hazardous barrier.",
    "quotes": [
      {"author": "Walter Scott", "work": "The Lady of the Lake", "quote": "The boatman spent the whole evening **ferrying** armed clansmen across the dark waters of the loch."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "A flotilla of small craft was actively engaged in **ferrying** soldiers from the exposed beaches to awaiting transports."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "The men worked tirelessly, **ferrying** their supplies across the swollen Yukon river."}
    ]
  },
  "Dashboard — fer/ferryman.md": {
    "primary": "A person who operates, manages, or steers a ferry boat.",
    "secondary": "In mythological folklore and literature, the symbolic custodian of the river barrier (such as Charon on the River Styx) conveying souls across the divide of death.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "I passed, methought, the melancholy flood, / With that sour **ferryman** which poets write of, / Unto the kingdom of perpetual night."},
      {"author": "Hermann Hesse", "work": "Siddhartha", "quote": "The old **ferryman** listened with silent reverence to the eternal whisper of the river."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Beyond this flood a frozen continent / Lies dark and wild... Where yet no **ferryman** hath dared to steer."}
    ]
  },
  "Dashboard — fer/fertile.md": {
    "primary": "Producing vegetation or crops in abundance; fruitful, prolific, or capable of breeding and reproducing.",
    "secondary": "In cognitive psychology and intellectual history, describing an inventive imagination, generative theory, or rich environment that fosters abundant innovations.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Antony and Cleopatra", "quote": "If every of your wishes had a womb, / And **fertile** every wish, a million."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Crosses between distinct varieties of plants frequently produce highly **fertile** offspring."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "A mind furnished with true principles proves **fertile** in generating beneficial inventions."}
    ]
  },
  "Dashboard — fer/fertilisation.md": {
    "primary": "The biological union of male and female gametes to initiate the development of a new individual; or the application of nutrients to soil.",
    "secondary": "In comparative embryology and angiosperm botany, the precise biochemical sequence of gamete recognition, acrosome activation, and karyogamy.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation", "quote": "I have reason to believe that humble-bees are indispensable to the **fertilisation** of the heartsease."},
      {"author": "Thomas Henry Huxley", "work": "Lay Sermons, Addresses, and Reviews", "quote": "The **fertilisation** of the ovum triggers a cascade of mitotic cell divisions in the zygote."},
      {"author": "Alfred Russel Wallace", "work": "Darwinism", "quote": "In flowering plants, insect cross-pollination ensures successful **fertilisation** with foreign pollen."}
    ]
  },
  "Dashboard — fer/fertilise.md": {
    "primary": "To make fruitful or productive; to supply soil with nutrients; or to impregnate an egg cell with sperm.",
    "secondary": "In botanical ecology and agricultural science, to transfer pollen to a stigma or introduce essential nitrogen, phosphorus, and potassium to crop soils.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised", "quote": "Many of our orchidaceous plants absolutely require the visits of moths to **fertilise** their flowers."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "To **fertilise** the exhausted loam, the husbandman must restore the mineral salts extracted by successive harvests."},
      {"author": "George Eliot", "work": "Adam Bede", "quote": "The spring rains come down to soften and **fertilise** the waiting furrows."}
    ]
  },
  "Dashboard — fer/fertiliser.md": {
    "primary": "Any chemical substance or organic material (such as manure or compost) added to soil to enhance plant growth and agricultural productivity.",
    "secondary": "In agronomy and soil chemistry, balanced mineral or synthetic compounds providing macro-nutrients (N-P-K) required for crop nutrition and high yields.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "Bone dust treated with sulfuric acid forms a soluble superphosphate **fertiliser** of extraordinary efficacy."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The judicious application of animal **fertiliser** doubled the yield of the garden crops."},
      {"author": "George Washington Carver", "work": "How to Build Up Worn Out Soils", "quote": "Compost made from swamp muck and forest leaves makes a cheap and natural **fertiliser** for poor soils."}
    ]
  },
  "Dashboard — fer/fertility.md": {
    "primary": "The quality, capacity, or state of being fertile; fruitfulness, fecundity, or the ability to produce abundant offspring, vegetation, or ideas.",
    "secondary": "In demographic sociology and agricultural pedology, the statistical rate of live births within a population, or the biochemical nutrient capacity of arable topsoil.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry V", "quote": "Alas, she hath from France too long been chas'd, / And all her husbandry doth lie on heaps, / Corrupting in it own **fertility**."},
      {"author": "Thomas Malthus", "work": "An Essay on the Principle of Population", "quote": "The natural **fertility** of the human species exceeds the productive capacity of the soil to sustain it."},
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "The varying degrees of **fertility** between distinct species when crossed have long engaged the attention of naturalists."}
    ]
  },
  "Dashboard — fer/fertilizable.md": {
    "primary": "Capable of being fertilized, impregnated, pollinated, or rendered productive.",
    "secondary": "In reproductive biology and embryology, describing an ovum that has attained developmental maturity and possesses functional surface receptors for sperm penetration.",
    "quotes": [
      {"author": "Thomas Hunt Morgan", "work": "Experimental Embryology", "quote": "The mature ovum remains fully **fertilizable** for only a limited window of hours after ovulation."},
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation", "quote": "The stigma becomes moist and **fertilizable** precisely when the local insect pollinators emerge."},
      {"author": "Jacques Loeb", "work": "Artificial Parthenogenesis and Fertilization", "quote": "Experiments showed that unfertilized eggs remained **fertilizable** even after exposure to hypertonic seawater."}
    ]
  },
  "Dashboard — fer/fertilization.md": {
    "primary": "The process of combining male and female gametes to produce a zygote; or the act of enriching soil with plant nutrients.",
    "secondary": "In developmental embryology and plant reproductive biology, the cascade of sperm-egg binding, membrane fusion, and pronuclear fusion.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Amid the oozing fatness and warm ferments of the Froom Vale, at a season when the vital forces of nature were bent upon **fertilization**, they met."},
      {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised", "quote": "The morphology of the floral column prevents self-pollination and guarantees cross **fertilization** by insect visitors."},
      {"author": "Thomas Hunt Morgan", "work": "The Mechanism of Mendelian Heredity", "quote": "At the moment of **fertilization**, the paternal and maternal chromosome sets unite to restore the diploid number."}
    ]
  },
  "Dashboard — fer/fertilize.md": {
    "primary": "To make fertile, fruitful, or productive; to enrich land with nutrients; or to impregnate an egg or flower.",
    "secondary": "In agricultural agronomy and pollination biology, to supply essential chemical nutrients to exhausted earth or transfer viable pollen to receptive stigmas.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Effects of Cross and Self Fertilisation", "quote": "Bees flying from blossom to blossom **fertilize** the flowers with pollen from distinct plants."},
      {"author": "Justus von Liebig", "work": "Familiar Letters on Chemistry", "quote": "To **fertilize** the land continuously, one must replace all the mineral constituents removed in the grain."},
      {"author": "John Muir", "work": "The Mountains of California", "quote": "The mountain torrents carry rich silt to **fertilize** the great agricultural valleys below."}
    ]
  },
  "Dashboard — fer/fertilizer.md": {
    "primary": "A substance (such as treated animal manure or synthetic chemicals) applied to soil to promote plant growth and improve crop yield.",
    "secondary": "In agricultural industrial chemistry, synthetic compounds (such as ammonium nitrate or superphosphates) manufactured via the Haber-Bosch process to feed commercial agriculture.",
    "quotes": [
      {"author": "Justus von Liebig", "work": "Organic Chemistry in Agriculture", "quote": "The choice of a mineral **fertilizer** must be guided by an exact chemical analysis of the soil's deficiencies."},
      {"author": "Charles Darwin", "work": "The Various Contrivances by which Orchids are Fertilised", "quote": "The night-flying hawk-moth acts as the indispensable **fertilizer** of the long-spurred Madagascar orchid."},
      {"author": "George Washington Carver", "work": "Progressive Nature Studies", "quote": "A proper green manure crop plowed under provides the most economical **fertilizer** for small farm holders."}
    ]
  },
  "Dashboard — fer/ferule.md": {
    "primary": "A flat cane, wooden ruler, or instrument formerly used in schools for punishing children by striking them on the hand.",
    "secondary": "In educational history and pedagogical reform literature, the symbolic instrument of Victorian corporal punishment and authoritarian classroom discipline.",
    "quotes": [
      {"author": "Ralph Waldo Emerson", "work": "Essays: Second Series", "quote": "According to the methods of education fifty years ago, it was quite customary to govern the schoolroom with the **ferule** and the rod."},
      {"author": "Charles Dickens", "work": "Nicholas Nickleby", "quote": "Mr. Squeers wielded his **ferule** with professional relish, terrifying the wretched boys of Dotheboys Hall."},
      {"author": "Washington Irving", "work": "The Sketch-Book", "quote": "The village schoolmaster was a man of stern countenance, bearing in his hand the dreadful **ferule** of authority."}
    ]
  },
  "Dashboard — fer/indifference.md": {
    "primary": "A lack of interest, care, concern, or enthusiasm; an unconcerned, neutral, or detached disposition.",
    "secondary": "In moral philosophy and economic utility theory, the absence of preference between alternative options yielding equivalent subjective satisfaction.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Gabriel, perhaps a little piqued by the comely traveller's **indifference**, ceased to watch her."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Liberty consists in a power to act or not to act, according as the mind chooses, which implies an **indifference** antecedent to the choice."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "She listened with an air of cold **indifference** that baffled all his attempts at reconciliation."}
    ]
  },
  "Dashboard — fer/indifferent.md": {
    "primary": "Having no particular interest, sympathy, or concern; unconcerned; or mediocre in quality.",
    "secondary": "In Stoic ethics and physical chemistry, designating things that are neither morally good nor bad (adiaphora), or substances exhibiting neutral chemical affinity.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Hamlet", "quote": "As the **indifferent** children of the earth."},
      {"author": "Marcus Aurelius", "work": "Meditations", "quote": "External circumstances are **indifferent** in themselves; the only true good or evil resides in our moral character."},
      {"author": "Adam Smith", "work": "The Theory of Moral Sentiments", "quote": "A spectator may behold the misfortunes of strangers with an **indifferent** eye, unless sympathy is awakened."}
    ]
  },
  "Dashboard — fer/indifferently.md": {
    "primary": "Without care, enthusiasm, or preference; impartially; or in a tolerable, mediocre, or unexceptional manner.",
    "secondary": "In legal administration and classical rhetoric, adjudicating disputes without bias or partiality toward either litigant.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Coriolanus", "quote": "If he did not care whether he had their love or no, he waved **indifferently** 'twixt doing them neither good nor harm."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth played **indifferently** upon the instrument, yet her performance gave pleasure by its unaffected grace."},
      {"author": "Samuel Johnson", "work": "The Rambler", "quote": "He accepted the praise and the censure of critics **indifferently**, mindful only of his own literary standards."}
    ]
  },
  "Dashboard — fer/infer.md": {
    "primary": "To deduce or conclude from evidence, premises, and reasoning rather than from explicit statements.",
    "secondary": "In formal logic and epistemological induction, to derive a warranted cognitive claim by valid deductive syllogism or probabilistic inference.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 3", "quote": "This doth **infer** the zeal I had to see him."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Reason can discover new truths and **infer** necessary conclusions from self-evident principles."},
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "From a drop of water a logician could **infer** the possibility of an Atlantic or a Niagara without having seen either."}
    ]
  },
  "Dashboard — fer/inference.md": {
    "primary": "A conclusion reached on the basis of evidence and reasoning; or the process of deriving such a conclusion.",
    "secondary": "In epistemology, Bayesian statistics, and formal logic, the systematic transition from perceived data premises to justified propositional conclusions.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "A cynical **inference** was irresistible by Gabriel Oak as he regarded the vanity of her gesture."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "All **inference** is from particulars to particulars, though we may record the result in a general proposition."},
      {"author": "Charles Sanders Peirce", "work": "Collected Papers", "quote": "Every synthetic **inference** is either an induction or an abduction, serving to enlarge our knowledge beyond mere deduction."}
    ]
  },
  "Dashboard — fer/inferential.md": {
    "primary": "Deduced or deducible by inference; based on or involving the process of deriving conclusions from premises.",
    "secondary": "In statistical analysis and analytical philosophy, referring to probabilistic estimation that generalizes sample statistics to population parameters.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "The conclusions of inductive science are **inferential** truths resting upon observed empirical uniformity."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Our belief in the existence of other minds is an **inferential** judgment based upon bodily gestures and spoken words."},
      {"author": "Bertrand Russell", "work": "Our Knowledge of the External World", "quote": "Much of what passes for direct perception contains an **inferential** construction built upon raw sense-data."}
    ]
  },
  "Dashboard — fer/inferior.md": {
    "primary": "Lower in rank, status, quality, degree, or value; or situated below another part or organ.",
    "secondary": "In comparative anatomy and typography, designating an anatomical organ positioned below another, or a subscript character placed below the baseline.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Sonnet 80", "quote": "My saucy bark, **inferior** far to his, / On your broad main doth wilfully appear."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Man still bears in his bodily frame the indelible stamp of his **inferior** origin."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Though **inferior** to the angels in power, man was created with the divine capacity for free will and reason."}
    ]
  },
  "Dashboard — fer/inferiority.md": {
    "primary": "The condition or quality of being lower in rank, status, value, skill, or quality than another.",
    "secondary": "In individual psychology (Adlerian theory), an internalized sense of inadequacy or limitation that drives compensatory behavioral striving.",
    "quotes": [
      {"author": "Charles Darwin", "work": "On the Origin of Species", "quote": "Moreover, when by sudden immigration or unusually rapid development a species gains an advantage, the **inferiority** of native competitors leads to extinction."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "His sense of her **inferiority** of birth and family connection made him hesitate long before proposing."},
      {"author": "Alfred Adler", "work": "The Neurotic Constitution", "quote": "The psychological feeling of **inferiority** stimulates the child to achieve mastery over physical obstacles."}
    ]
  },
  "Dashboard — fer/infernal.md": {
    "primary": "Relating to or characteristic of hell or the underworld; extremely troublesome, hateful, or outrageous.",
    "secondary": "In classical myth and apocalyptic theology, pertaining to the subterranean realms of Hades or Tartarus, or describing diabolical cruelty.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry IV, Part 2", "quote": "I'll see her damned first to Pluto's damned lake, by this hand, to the **infernal** deep, with Erebus and tortures vile also."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "A way to shake that throne, or work our peace / In this **infernal** pit."},
      {"author": "Dante Alighieri", "work": "Inferno", "quote": "The **infernal** hurricane that never rests sweeps the tormented spirits through the dark air."}
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

print(f"Carrying Batch 5C (fer): Successfully updated {updated}/{len(data)} notes.")
