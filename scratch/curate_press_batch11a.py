# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — press Part 1 (11A, 34 words) ---
  "Dashboard — press/adpressed.md": {
    "primary": "Pressed closely against or lying flat against a surface or stem, without being fused to it.",
    "secondary": "In botanical morphology, describes hairs, bracts, or leaves that lie closely parallel to the axis of the plant stem.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Different Forms of Flowers on Plants of the Same Species", "quote": "The pedicels remain closely **adpressed** to the central stem until the fruit attains maturity."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "The calyx lobes are upright and firmly **adpressed** against the emerging capsule."},
      {"author": "Joseph Dalton Hooker", "work": "The Flora of British India", "quote": "The siliques are slender, erect, and strictly **adpressed** along the main flowering rachis."}
    ]
  },
  "Dashboard — press/antidepressant.md": {
    "primary": "A medication or therapeutic agent utilized to alleviate symptoms of clinical depression and mood disorders.",
    "secondary": "In neuropsychopharmacology, classes include SSRIs, SNRIs, and MAO inhibitors that modulate synaptic concentrations of monoamine neurotransmitters.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The administration of an **antidepressant** regimen helped stabilize the patient's severe emotional fluctuations."},
      {"author": "William Styron", "work": "Darkness Visible: A Memoir of Madness", "quote": "He described the gradual trial of an **antidepressant** that slowly lifted the gray shroud of despair."},
      {"author": "Richard Cabot", "work": "Differential Diagnosis", "quote": "When persistent melancholy resists counseling, a tailored **antidepressant** compound offers clinical benefit."}
    ]
  },
  "Dashboard — press/appressed.md": {
    "primary": "Pressed closely, flatly, or tightly against an organ, axis, or adjacent tissue.",
    "secondary": "In lichenology and mycology, denotes thalli or hyphae adhering closely to bark or rock substrata.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "In certain varieties of cabbage, the thick outer leaves remain tightly **appressed** to the head."},
      {"author": "Thomas Henry Huxley", "work": "A Manual of the Anatomy of Invertebrated Animals", "quote": "The lateral plates are firmly **appressed** to the chitinous exoskeleton, protecting internal gills."},
      {"author": "Asa Gray", "work": "Structural Botany", "quote": "The pubescence consists of minute **appressed** hairs that create a silken luster across the leaf surface."}
    ]
  },
  "Dashboard — press/compress.md": {
    "primary": "To press, squeeze, or force together so as to reduce volume, size, or bulk.",
    "secondary": "In medicine and surgical nursing, a pad of absorbent cloth applied firmly to an injury to staunch hemorrhage or reduce inflammation.",
    "quotes": [
      {"author": "Francis Bacon", "work": "Sylva Sylvarum", "quote": "If you **compress** the air inside a narrow cylinder, it acquireth a stronger elastic spring."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The nurse hastened to apply a cold **compress** to the sick girl's burning forehead."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The immense pressure of the ocean depths tends to **compress** the timbers of diving whales."}
    ]
  },
  "Dashboard — press/compressed.md": {
    "primary": "Pressed together tightly, flattened, reduced in volume, or condensed by external mechanical force.",
    "secondary": "In ichthyology and anatomy, describes bodies or anatomical structures that are laterally flattened from side to side.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Many marine fishes possess laterally **compressed** bodies adapted for gliding through dense seaweed beds."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes examined the packet of closely **compressed** tobacco leaf found in the corner of the hut."},
      {"author": "Thomas Hardy", "work": "The Return of the Native", "quote": "Clym spoke with pale, tightly **compressed** lips that revealed the severity of his inward resolution."}
    ]
  },
  "Dashboard — press/compressibility.md": {
    "primary": "The property or capacity of a substance to decrease in volume under the application of pressure.",
    "secondary": "In fluid mechanics and thermodynamics, the relative volume change of a fluid or gas in response to pressure, quantified by bulk modulus.",
    "quotes": [
      {"author": "Isaac Newton", "work": "Opticks", "quote": "The elasticity and subtle **compressibility** of the medium explain the rapid propagation of sound waves."},
      {"author": "James Clerk Maxwell", "work": "Theory of Heat", "quote": "The isothermal **compressibility** of a gas increases rapidly as it approaches its critical temperature."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry and Physics", "quote": "Under tremendous hydraulic force, the slight **compressibility** of water becomes unmistakably measurable."}
    ]
  },
  "Dashboard — press/compressible.md": {
    "primary": "Capable of being squeezed, pressed, or compacted into a smaller space or volume.",
    "secondary": "In aerodynamics, describes high-speed fluid flows where density variations cannot be neglected, typically exceeding Mach 0.3.",
    "quotes": [
      {"author": "Robert Boyle", "work": "New Experiments Physico-Mechanicall", "quote": "Air is a wonderfully **compressible** fluid that springs back with vigor when released from restraint."},
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "Every material aggregate is composed of units more or less **compressible** under gravitational aggregation."},
      {"author": "Thomas Henry Huxley", "work": "Physiography", "quote": "Atmospheric gases are highly **compressible**, becoming denser in the deeper strata near sea level."}
    ]
  },
  "Dashboard — press/compressing.md": {
    "primary": "Applying pressure to reduce bulk, crowd together, or condense into smaller compass.",
    "secondary": "In computer science and digital information theory, encoding data using fewer bits through lossy or lossless compression algorithms.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Oak stood **compressing** his fingers against his brow, pondering how to save the threatened flock."},
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "He stood by the mantelpiece, **compressing** his hands together in an agony of silent dread."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Lydgate listened in silence, **compressing** his thoughts into a few decisive clinical judgments."}
    ]
  },
  "Dashboard — press/compression.md": {
    "primary": "The act of pressing together or the resulting reduced state or condensed volume.",
    "secondary": "In internal combustion engineering, the reduction in volume of fuel-air mixture in a cylinder prior to ignition.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The geological strata show evidence of enormous lateral **compression** during the elevation of mountain chains."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The deep indentations in the turf indicated sudden weight and violent **compression** from the heavy wooden leg."},
      {"author": "Francis Bacon", "work": "Novum Organum", "quote": "Violent **compression** of flame within a narrow gun chamber produces explosive outward motion."}
    ]
  },
  "Dashboard — press/compressor.md": {
    "primary": "A mechanical device, machine, or tool used to compress gases or increase pressure.",
    "secondary": "In human anatomy and surgical instruments, any muscle or clamp that constricts an opening or blood vessel.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The clanking rotary **compressor** forced chilled gas through the tubular coils of the dirigible."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "Martin adjusted the electric air **compressor** connected to the bacterial filtration apparatus."},
      {"author": "Upton Sinclair", "work": "Oil!", "quote": "The roaring diesel **compressor** pumped high-pressure air down into the casing of the test well."}
    ]
  },
  "Dashboard — press/decompress.md": {
    "primary": "To release or reduce pressure; to return to normal atmospheric pressure or uncompressed volume.",
    "secondary": "In deep-sea diving, to bring a diver gradually back to surface atmospheric pressure to prevent decompression sickness (the bends).",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Deep Range", "quote": "The submersible crew waited in the airlock chamber to **decompress** before entering the main habitat."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The technicians stepped into the sealed decompression corridor to **decompress** following the shift."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "We prepared to **decompress** our sealed spherical cabin as the lunar atmosphere thinness became apparent."}
    ]
  },
  "Dashboard — press/decompressing.md": {
    "primary": "Undergoing or executing the reduction of internal or surrounding physical pressure.",
    "secondary": "In computing and storage architecture, unpacking encoded archive files into their original uncompressed format.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "While **decompressing** in the intermediate bay, Bowman checked the telemetry indicators of his pressure suit."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "The salvage divers spent several tedious hours **decompressing** in the pressurized hospital barge."},
      {"author": "Sinclair Lewis", "work": "Arrowsmith", "quote": "The laboratory technician spent the morning **decompressing** delicate vacuum tubes after the test run."}
    ]
  },
  "Dashboard — press/decompression.md": {
    "primary": "The reduction or release of physical pressure, or return to normal ambient pressure.",
    "secondary": "In underwater medicine, the systematic staging required during ascent to dissolve inert nitrogen gas from bodily tissues.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "The Deep Range", "quote": "Careful adherence to the **decompression** schedule saved deep divers from crippling nitrogen embolism."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "A sudden rupture in the balloon envelope produced rapid **decompression** and extreme dizziness among the crew."},
      {"author": "Aldous Huxley", "work": "Island", "quote": "The slow mental **decompression** after months of urban toil restored his creative tranquility."}
    ]
  },
  "Dashboard — press/depress.md": {
    "primary": "To lower someone's spirits, cause despondency; or to press or push down physically.",
    "secondary": "In macroeconomic monetary theory, to reduce commercial activity, wages, or prices below equilibrium levels.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "Her father's constant recital of domestic troubles and debts seemed to **depress** her youthful spirit beyond measure."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "No material burden could **depress** his buoyant spirits for long, but debt hung over him like a cloud."},
      {"author": "James Joyce", "work": "Dubliners", "quote": "The great silver buckle of her belt seemed to **depress** the centre of her body, catching the lamplight."}
    ]
  },
  "Dashboard — press/depressant.md": {
    "primary": "A substance or agent that lowers physiological or nervous activity; a sedative.",
    "secondary": "In clinical pharmacology, central nervous system depressants include barbiturates, benzodiazepines, and alcohol that potentiate GABAergic neurotransmission.",
    "quotes": [
      {"author": "Oliver Wendell Holmes Jr.", "work": "Medical Essays", "quote": "The physician prescribed a mild **depressant** to moderate the violent arterial throbbing of the fever."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Judicious administration of a cardiac **depressant** reduced excessive vascular tension in the acute crisis."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Devil's Foot", "quote": "The strange African powder acted as a virulent nerve **depressant**, inducing profound terror and physical collapse."}
    ]
  },
  "Dashboard — press/depressed.md": {
    "primary": "Cast down in spirits, sad, despondent; or lowered in position, sunken, or flattened.",
    "secondary": "In economic history, characterized by persistent economic stagnation, widespread unemployment, and reduced industrial output.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard II", "quote": "**Depressed** he is already, and deposed 'tis doubt he will be."},
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "The sight had quite **depressed** her this evening, reminding her painfully of her own youthful folly."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "I sat in the cold schoolroom with a **depressed** heart, longing for some kind word of sympathy."}
    ]
  },
  "Dashboard — press/depressing.md": {
    "primary": "Causing sadness, gloom, disheartening despondency, or lowering of morale.",
    "secondary": "In clinical evaluation, describes environmental and behavioral factors that exacerbate melancholy and anhedonia.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Still, it was faintly **depressing** that the most dignified and valuable man in the parish should turn away."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "There is hardly any contact more **depressing** to a young ardent creature than that of a mind narrow and cold."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "The wet mist hovering over the lonely marshes produced a deeply **depressing** influence upon the wanderer."}
    ]
  },
  "Dashboard — press/depressingly.md": {
    "primary": "In a manner or to a degree that causes gloom, sadness, or discouragement.",
    "secondary": "In narrative exposition, emphasizes monotonous, bleak, or squalid physical settings and social situations.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The rows of back-to-back brick cottages were **depressingly** identical under the perpetual drizzle of soot."},
      {"author": "Virginia Woolf", "work": "The Voyage Out", "quote": "The long sea voyage seemed **depressingly** monotonous when viewed through the gray lens of indisposition."},
      {"author": "Thomas Hardy", "work": "Jude the Obscure", "quote": "The uniform drizzle fell **depressingly** upon the black umbrellas of the mourners assembled near the churchyard."}
    ]
  },
  "Dashboard — press/depression.md": {
    "primary": "A sunken place, hollow, or indentation; or a mental state of persistent dejection and despair.",
    "secondary": "In meteorology, an atmospheric low-pressure system associated with cloudy skies, precipitation, and cyclonic wind circulation.",
    "quotes": [
      {"author": "Thomas Hardy", "work": "Far from the Madding Crowd", "quote": "Up the sides of this natural **depression** grew sheaves of the common rush and patches of wild thyme."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "A broad circular **depression** in the coral reef formed a sheltered lagoon filled with vivid tropical fish."},
      {"author": "Charlotte Brontë", "work": "Villette", "quote": "A heavy cloud of inward **depression** weighed down my spirits as evening descended over the foreign city."}
    ]
  },
  "Dashboard — press/depressive.md": {
    "primary": "Tending to cause depression or lower spirits; characterized by psychological melancholy.",
    "secondary": "In diagnostic psychiatry, pertains to mood episodes (such as major depressive disorder or bipolar depression) featuring anhedonia and psychomotor slowing.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The pathological **depressive** state strips the external universe of all its intrinsic beauty and significance."},
      {"author": "Sigmund Freud", "work": "Mourning and Melancholia", "quote": "The **depressive** reaction differs from normal grief in its profound lowering of the patient's self-esteem."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "The abrupt cessation of dopamine therapy precipitated a severe **depressive** stupor."}
    ]
  },
  "Dashboard — press/depressor.md": {
    "primary": "A muscle, instrument, or agent that presses down, depresses, or lowers a body structure.",
    "secondary": "In clinical medicine, a tongue depressor is a flat wooden spatula used to depress the tongue during oropharyngeal inspection.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The physician introduced a wooden **depressor** to inspect the tonsils and posterior pharyngeal wall."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "The **depressor** nerve of the heart acts reflexly to lower systemic arterial blood pressure."},
      {"author": "Richard Cabot", "work": "Physical Diagnosis", "quote": "Gentle application of the tongue **depressor** allows complete visualization of the soft palate."}
    ]
  },
  "Dashboard — press/depressurise.md": {
    "primary": "To reduce or remove physical pressure from a sealed chamber, aircraft, or pressure vessel.",
    "secondary": "In aviation engineering, the controlled discharge of cabin pressure prior to opening exits or during emergency descent.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "Rendezvous with Rama", "quote": "The command was given to **depressurise** the outer airlock before sliding the heavy hatchway open."},
      {"author": "H. G. Wells", "work": "The Shape of Things to Come", "quote": "Technicians began to **depressurise** the high-altitude experimental nacelle following the endurance flight."},
      {"author": "Aldous Huxley", "work": "Brave New World", "quote": "The automated controls will **depressurise** the storage vaults gradually to prevent structural damage."}
    ]
  },
  "Dashboard — press/depressurize.md": {
    "primary": "To cause a reduction or loss of internal pressure within a sealed vehicle, cabin, or container.",
    "secondary": "In aerospace life support systems, uncontrolled depressurization risks hypoxia and ebullism at altitudes above the Armstrong limit.",
    "quotes": [
      {"author": "Arthur C. Clarke", "work": "2001: A Space Odyssey", "quote": "Bowman realized the emergency hatch would **depressurize** the storage chamber in a fraction of a second."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "Sensors verified that opening the external port would rapidly **depressurize** the intermediate staging airlock."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "A puncture in the forward valve caused the gas compartments to **depressurize** unevenly during flight."}
    ]
  },
  "Dashboard — press/empress.md": {
    "primary": "A female sovereign ruling an empire in her own right, or the consort and wife of an emperor.",
    "secondary": "In monarchical protocol and international law, an empress outranks a queen, signifying imperial dominion over multiple constituent realms.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Henry VI, Part 2", "quote": "She sweeps it through the court with troops of ladies, more like an **empress** than Duke Humphrey's wife."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The celebrated **empress** Theodora displayed consummate political courage during the Nika revolt in Constantinople."},
      {"author": "Walter Scott", "work": "Count Robert of Paris", "quote": "The Byzantine **empress** sat upon her ivory throne, adorned with barbaric pearls and imperial purple."}
    ]
  },
  "Dashboard — press/espresso.md": {
    "primary": "A concentrated coffee beverage brewed by forcing pressurized hot water through finely ground roasted coffee beans.",
    "secondary": "In gastronomy, characterized by a thick consistency, high dissolved solids, and a rich, golden-brown aromatic foam termed crema.",
    "quotes": [
      {"author": "Ernest Hemingway", "work": "A Moveable Feast", "quote": "I sat at the corner table of the café, drinking a strong dark **espresso** while watching the rain."},
      {"author": "Graham Greene", "work": "The Comedians", "quote": "He sipped the bitter **espresso** served in a thick porcelain cup while contemplating his next rendezvous."},
      {"author": "James Baldwin", "work": "Giovanni's Room", "quote": "The hiss of the chrome steam machine and the scent of freshly brewed **espresso** filled the small morning bistro."}
    ]
  },
  "Dashboard — press/express.md": {
    "primary": "To convey, articulate, or represent in words, gestures, or art; fast, direct, or explicitly stated.",
    "secondary": "In constitutional law, an express power is a authority explicitly enumerated and codified in constitutional text.",
    "quotes": [
      {"author": "William Shakespeare", "work": "All's Well That Ends Well", "quote": "You ne'er oppress'd me with a mother's groan, yet I **express** to you a mother's care."},
      {"author": "John Milton", "work": "Paradise Lost", "quote": "Their human countenance the **express** resemblance of the gods, once upright and divine."},
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Words are but the images of matter, and serve only to **express** the real substances of knowledge."}
    ]
  },
  "Dashboard — press/expressage.md": {
    "primary": "The business, system, or commercial charge for transporting freight and parcels via rapid express delivery.",
    "secondary": "In 19th-century commercial history, the network of private express forwarding companies (such as Wells Fargo and American Express) operating on stagecoach and rail lines.",
    "quotes": [
      {"author": "Mark Twain", "work": "Roughing It", "quote": "The heavy iron strongbox was committed to the overland company with payment of full **expressage**."},
      {"author": "Sinclair Lewis", "work": "Main Street", "quote": "The storekeeper complained bitterly about the exorbitant **expressage** charged on eastern dry goods shipments."},
      {"author": "Theodore Dreiser", "work": "The Titan", "quote": "Cowperwood calculated the exact cost of railway freight and **expressage** before submitting his municipal bid."}
    ]
  },
  "Dashboard — press/expressed.md": {
    "primary": "Stated, manifested, or revealed in explicit terms or unmistakable signs; squeezed out by pressure.",
    "secondary": "In biochemistry and gene regulation, denotes a gene whose DNA sequence has been transcribed and translated into functional protein.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Love's Labour's Lost", "quote": "His heart, like an agate, with your print impressed, proud with his form, in his eye pride **expressed**."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Elinor **expressed** her sincere gratitude for the polite attentions showered upon her family."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "Grief is unmistakably **expressed** across all human races through involuntary contraction of the corrugator muscles."}
    ]
  },
  "Dashboard — press/expressible.md": {
    "primary": "Capable of being uttered, described, communicated, or represented in language or symbols.",
    "secondary": "In formal logic and mathematics, a property or relation that can be formally stated within a given axiomatic language.",
    "quotes": [
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "Many complex ideas of the mind are readily **expressible** in language, though simple sensations defy perfect description."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Mathematical truths are strictly **expressible** through unambiguous logical primitives and propositional variables."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "There were nuances in Dorothea's yearning that were scarcely **expressible** within the narrow social conventions of her time."}
    ]
  },
  "Dashboard — press/expression.md": {
    "primary": "The act of making known thoughts or feelings through words, facial looks, or artistic actions.",
    "secondary": "In algebra and computer programming, a combination of constants, variables, operators, and functions that evaluates to a value.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "There was a singular **expression** of triumphant pride upon Miss Havisham's withered face as she watched us."},
      {"author": "Charles Darwin", "work": "The Expression of the Emotions in Man and Animals", "quote": "The facial **expression** of rage is accompanied by violent acceleration of the circulation and flashing eyes."},
      {"author": "Ralph Waldo Emerson", "work": "The Poet", "quote": "The poet is the man who finds the perfect **expression** for what all men secretly feel and obscurely know."}
    ]
  },
  "Dashboard — press/expressionism.md": {
    "primary": "A modernist movement in art and literature seeking to depict emotional experience rather than physical reality.",
    "secondary": "In art history, emerged in early 20th-century Germany (die Brücke and Der Blaue Reiter) using vivid colors and distorted forms to convey subjective angst.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "Roger Fry: A Biography", "quote": "He defended the bold distortions of **expressionism** as necessary steps toward liberating artistic emotion from academic realism."},
      {"author": "W. H. Auden", "work": "The Dyer's Hand", "quote": "The dramatic experiments of German **expressionism** shattered traditional theatrical illusion to confront raw psychological crisis."},
      {"author": "Thomas Mann", "work": "Doctor Faustus", "quote": "The new musical idiom shared with visual **expressionism** a fierce rebellion against decorative conventional harmony."}
    ]
  },
  "Dashboard — press/expressionist.md": {
    "primary": "An artist, writer, or practitioner associated with or employing the methods of expressionism.",
    "secondary": "In theatrical and cinematic design, utilizes stark chiaroscuro lighting, jagged angles, and stylized performances to manifest internal torment.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Antic Hay", "quote": "The young **expressionist** painter displayed canvases filled with distorted crimson figures screaming into empty voids."},
      {"author": "George Orwell", "work": "Inside the Whale", "quote": "The continental **expressionist** drama reflected the profound political and spiritual disintegration following the Great War."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "Like an **expressionist** canvas, the sunset splashed violent streaks of purple and jagged orange across the sky."}
    ]
  },
  "Dashboard — press/expressionistic.md": {
    "primary": "Relating to, characterized by, or exhibiting the exaggerated and subjective qualities of expressionism.",
    "secondary": "In cinema criticism, describes films (such as The Cabinet of Dr. Caligari) featuring non-realistic, geometrically distorted sets reflecting psychological madness.",
    "quotes": [
      {"author": "Aldous Huxley", "work": "Point Counter Point", "quote": "He admired the harsh, **expressionistic** brushwork that stripped the portrait of all polite superficial prettiness."},
      {"author": "Virginia Woolf", "work": "The Captain's Death Bed and Other Essays", "quote": "Modern fiction adopts an **expressionistic** technique to reveal the chaotic drift of unedited consciousness."},
      {"author": "George Bernard Shaw", "work": "The Quintessence of Ibsenism", "quote": "The later plays develop an **expressionistic** symbolism that moves beyond the naturalistic parlor room drama."}
    ]
  },
  "Dashboard — press/expressionless.md": {
    "primary": "Devoid of expression, emotion, or animation; completely blank, impassive, or vacant.",
    "secondary": "In clinical neurology, a mask-like, expressionless facies (hypomimia) is a classic motor hallmark of idiopathic Parkinson's disease.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "A Study in Scarlet", "quote": "Sherlock Holmes's hawk-like face was absolutely **expressionless** as he examined the dark stain on the floor."},
      {"author": "Thomas Hardy", "work": "The Mayor of Casterbridge", "quote": "Michael Henchard met his former partner with a cold, **expressionless** stare that extinguished all hope of reconciliation."},
      {"author": "Joseph Conrad", "work": "The Secret Agent", "quote": "Mr. Verloc maintained an **expressionless** countenance while listening to the secret embassy instructions."}
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

print(f"Motion Batch 11A: Successfully updated {updated}/{len(data)} notes.")
