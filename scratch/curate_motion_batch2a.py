# -*- coding: utf-8 -*-
import os, sys, re
sys.stdout.reconfigure(encoding="utf-8")

data = {
  # --- Dashboard — pel (21 words) ---
  "Dashboard — pel/compel.md": {
    "primary": "To force, drive, or obligate someone to do something; or to bring about by overwhelming force.",
    "secondary": "In jurisprudence and procedural law, courts issue subpoenas and writs to compel witness testimony and document disclosure.",
    "quotes": [
      {"author": "William Shakespeare", "work": "The Merchant of Venice", "quote": "The quality of mercy is not strained; it droppeth as the gentle rain from heaven, and no mortal power can **compel** it."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth declared that no argument could **compel** her to accept a proposal that offended her judgment."},
      {"author": "John Locke", "work": "A Letter Concerning Toleration", "quote": "No civil magistrate has the moral authority to **compel** men to conform to an outward religious profession."}
    ]
  },
  "Dashboard — pel/dispel.md": {
    "primary": "To drive away, scatter, or cause to vanish, especially doubts, fears, clouds, or illusions.",
    "secondary": "In clinical psychotherapy and cognitive restructuring, empirical evidence is used to dispel irrational catastrophizing thoughts.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes's calm explanation served to **dispel** the superstitious terrors that had haunted Dartmoor."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The morning sun rose over the Alpine peaks, helping to **dispel** the dark gloom that enveloped my mind."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "Rochester's tender words had power to **dispel** my anxious misgivings and quiet my beating heart."}
    ]
  },
  "Dashboard — pel/expel.md": {
    "primary": "To force out, drive away, or eject from a place, group, country, or academic institution.",
    "secondary": "In pulmonary physiology and respiratory mechanics, diaphragmatic and intercostal contractions expel alveolar air during expiration.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The Roman senate resolved to **expel** corrupt governors who had plundered the Asian provinces."},
      {"author": "Charles Dickens", "work": "David Copperfield", "quote": "The headmaster threatened to **expel** any student caught violating the strict school rules."},
      {"author": "Thomas Carlyle", "work": "The French Revolution", "quote": "The revolutionary assembly voted to **expel** all royalist deputies from the halls of the convention."}
    ]
  },
  "Dashboard — pel/expelling.md": {
    "primary": "Forcibly driving out, discharging, or ejecting matter, air, or individuals from an enclosure.",
    "secondary": "In marine biology and cephalopod defense, octopuses escape predators by expelling dense clouds of black melanin ink.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The whale breached violently, **expelling** a mighty column of vaporous spray high into the morning air."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The cuttlefish darted backward across the rock pool, **expelling** a dark fluid that concealed its flight."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "The Martian canister detonated with a dull thud, **expelling** heavy coils of suffocating black smoke."}
    ]
  },
  "Dashboard — pel/impel.md": {
    "primary": "To drive, force, or urge someone forward or into action, either physically or by moral motivation.",
    "secondary": "In Newtonian mechanics, external net forces impel massive bodies into accelerated linear or rotational trajectories.",
    "quotes": [
      {"author": "John Milton", "work": "Paradise Lost", "quote": "What cause moved our grand parents in that happy state, favored of heaven, to fall, and what did **impel** their disobedience?"},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "An intense desire to benefit mankind seemed to **impel** young Dorothea toward great humanitarian schemes."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "A dark fascination appeared to **impel** Chillingworth to probe the deepest secrets of the minister's troubled soul."}
    ]
  },
  "Dashboard — pel/impelled.md": {
    "primary": "Driven, pushed, or urged onward by strong physical force, conviction, passion, or necessity.",
    "secondary": "In aerospace ballistics, combustion gasses expanding through convergent-divergent nozzles leave rockets impelled into orbit.",
    "quotes": [
      {"author": "Charles Dickens", "work": "A Tale of Two Cities", "quote": "Sydney Carton was **impelled** by a sublime devotion to sacrifice his life for the peace of Lucie."},
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The slender whaleboat was **impelled** across the choppy water by the rhythmic, powerful strokes of the crew."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "Frankenstein was **impelled** by an obsessive scientific ambition to uncover the hidden mechanism of vital life."}
    ]
  },
  "Dashboard — pel/impellent.md": {
    "primary": "Having the quality or power of impelling, driving, or urging forward; an impelling force or motive.",
    "secondary": "In hydrodynamics and propulsion engineering, an impellent jet provides reactive forward thrust in fluid conduits.",
    "quotes": [
      {"author": "Herbert Spencer", "work": "First Principles", "quote": "The primary **impellent** force behind social progress is the relentless pressure of human population growth."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "True artistic imagination operates as an **impellent** power that harmonizes intellect and sensory emotion."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific curiosity serves as the chief **impellent** motive driving researchers through tedious experimental trials."}
    ]
  },
  "Dashboard — pel/impeller.md": {
    "primary": "A rotating device equipped with blades or vanes used to force, pump, or increase the flow of a fluid.",
    "secondary": "In centrifugal pump engineering, fluid enters the axial eye of the impeller and gains velocity through radial centrifugal acceleration.",
    "quotes": [
      {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "The laboratory apparatus featured a motorized brass **impeller** that whipped the experimental emulsion into foam."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "A powerful turbine **impeller** drove cooling seawater through the condensing pipes of the electrical engines."},
      {"author": "Arthur Conan Doyle", "work": "The Lost World", "quote": "Challenger rigged a small mechanical **impeller** to circulate fresh river water through their makeshift camp filter."}
    ]
  },
  "Dashboard — pel/impelling.md": {
    "primary": "Driving, urging, or pushing forward with persistent force, energy, or moral imperative.",
    "secondary": "In behavioral economics and decision theory, subconscious cognitive biases act as impelling factors in risk valuation.",
    "quotes": [
      {"author": "Joseph Conrad", "work": "Lord Jim", "quote": "An irresistible impulse seemed to be **impelling** him to speak, yet pride sealed his lips in stony silence."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The unseen currents of destiny were **impelling** Tess toward that desolate junction of Wessex roads."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "Maggie felt the warm, **impelling** tide of youthful enthusiasm carrying her beyond the narrow boundaries of St. Ogg's."}
    ]
  },
  "Dashboard — pel/pel.md": {
    "primary": "A picture element in digital graphics, synonymous with pixel; or the Latin etymological stem meaning to drive or strike.",
    "secondary": "In display hardware engineering and raster graphics architecture, each addressable pel contains discrete sub-elements for RGB chromatic emission.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Valley of Fear", "quote": "The cryptanalyst carefully examined each marked dot and miniature **pel** upon the cipher manuscript."},
      {"author": "H. G. Wells", "work": "The Time Machine", "quote": "The strange mosaic screen resolved into shimmering points of color, each luminous **pel** contributing to the shifting illusion."},
      {"author": "Mark Twain", "work": "A Connecticut Yankee in King Arthur's Court", "quote": "The telegrapher logged every electrical mark and distinct dot upon the tape with mathematical precision."}
    ]
  },
  "Dashboard — pel/pelage.md": {
    "primary": "The hairy, woolly, or furry coat covering the skin of a mammal.",
    "secondary": "In mammalian mammalogy and thermal ecology, seasonal molting produces a dense, insulated winter pelage to minimize conductive heat loss.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "The protective coloration of the Arctic hare's white winter **pelage** conceals it against the snow from hunting foxes."},
      {"author": "Jack London", "work": "The Call of the Wild", "quote": "Buck's heavy **pelage** grew thicker and coarser as the bitter Arctic winter settled over the Klondike."},
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The northern moose possesses a dark, bristly **pelage** well suited to turning aside the icy rains of the wilderness."}
    ]
  },
  "Dashboard — pel/propel.md": {
    "primary": "To drive, push, or cause to move forward or onward, typically through the application of mechanical or physical force.",
    "secondary": "In aerospace rocketry and astronautics, expanding combustion exhausts propel launch vehicles into orbital velocities.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The harpooneers bent their muscular backs to the oars to **propel** the whaleboat alongside the swimming monster."},
      {"author": "Jules Verne", "work": "From the Earth to the Moon", "quote": "Colossal charges of gun-cotton were calculated to **propel** the projectile vehicle beyond Earth's gravitational grasp."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "Giant mechanical tripods marched across the countryside, using articulated iron joints to **propel** the Martian machines."}
    ]
  },
  "Dashboard — pel/propellant.md": {
    "primary": "A chemical substance, explosive charge, or compressed gas used to provide thrust or propel a projectile or vehicle.",
    "secondary": "In chemical rocket propulsion, liquid bipropellant systems combine liquid oxidizers and hydrocarbon fuels within regenerative thrust chambers.",
    "quotes": [
      {"author": "Jules Verne", "work": "From the Earth to the Moon", "quote": "Barbicane tested the explosive velocity of pyroxyle as a revolutionary **propellant** for the Columbiad cannon."},
      {"author": "H. G. Wells", "work": "The First Men in the Moon", "quote": "Cavor explained that the mechanical sphere required no chemical **propellant** once cavorite screens were opened."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Bruce-Partington Plans", "quote": "The military secret involved a stabilized smokeless cordite **propellant** designed for naval artillery."}
    ]
  },
  "Dashboard — pel/propellent.md": {
    "primary": "Capable of propelling, driving, or urging forward; serving as an agent of forward propulsion.",
    "secondary": "In internal ballistics, modern nitrocellulose powders provide steady propellent gas expansion down the gun barrel without bore fouling.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "Scientific reasoning acts as a **propellent** power that advances human knowledge beyond superstitious tradition."},
      {"author": "David Brewster", "work": "Treatise on Optics", "quote": "The experimentalist measured the **propellent** velocity imparted to luminous particles under concentrated radiation."},
      {"author": "Herbert Spencer", "work": "The Principles of Sociology", "quote": "Economic necessity serves as the chief **propellent** agency driving primitive tribes to migrate into fertile valleys."}
    ]
  },
  "Dashboard — pel/propeller.md": {
    "primary": "A mechanical device with rotating radiating blades positioned on a shaft, used to propel a ship or aircraft.",
    "secondary": "In naval architecture and marine hydrodynamics, variable-pitch propeller blades optimize cavitation margins across varying vessel speeds.",
    "quotes": [
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The massive bronze **propeller** of the Nautilus turned silently, driving the submarine through the Atlantic depths."},
      {"author": "Joseph Conrad", "work": "Typhoon", "quote": "The Nan-Shan plunged into the mountainous sea until her racing **propeller** rose thrashing clear of the foam."},
      {"author": "H. G. Wells", "work": "The War in the Air", "quote": "The aerial battle-cruiser swung gracefully into the wind as its twin **propeller** blades began their droning hum."}
    ]
  },
  "Dashboard — pel/propelling.md": {
    "primary": "Driving, urging, or pushing forward through applied physical or mechanical force.",
    "secondary": "In aquatic locomotion, undulating caudal fins create traveling vortex wakes propelling teleost fish through water.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The oarsmen strained at their sweeps, **propelling** the cedar craft through boiling sheets of ocean spray."},
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The marine iguana swam with great ease, **propelling** its body through the surf by sinuous lateral movements of its tail."},
      {"author": "Robert Louis Stevenson", "work": "Treasure Island", "quote": "Silver leaned forward on his crutch, **propelling** his heavy frame across the sandy beach with astonishing agility."}
    ]
  },
  "Dashboard — pel/propellor.md": {
    "primary": "An alternative spelling of propeller, designating a rotating bladed device providing propulsion to a vessel or aircraft.",
    "secondary": "In early aviation and aeronautical engineering patents, engineers documented propeller and propellor thrust efficiency curves.",
    "quotes": [
      {"author": "H. G. Wells", "work": "When the Sleeper Wakes", "quote": "Graham watched the soaring monoplane, admiring the blur of its twin-bladed wooden **propellor** in the dawn light."},
      {"author": "Rudyard Kipling", "work": "Actions and Reactions", "quote": "The postal dirigible cruised steadily through the upper air currents, driven by a quiet humming **propellor**."},
      {"author": "Arthur Conan Doyle", "work": "The Poison Belt", "quote": "Challenger inspected the motor launch, ensuring that the submerged **propellor** was free of river weeds."}
    ]
  },
  "Dashboard — pel/repel.md": {
    "primary": "To drive back, fend off, or resist an attack, enemy, or intrusion; or to cause feelings of intense distaste.",
    "secondary": "In classical electromagnetism and electrostatics, like electrical charges repel each other according to Coulomb's inverse-square law.",
    "quotes": [
      {"author": "William Shakespeare", "work": "Richard III", "quote": "If we be conquered, let men conquer us, not these bastard Bretons, whom our fathers have beaten and did **repel**."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Estella's cold and haughty manner seemed designed to **repel** any genuine expression of affection from Pip."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Diamagnetic substances are those which are repelled by magnetic poles, as like poles **repel** each other in space."}
    ]
  },
  "Dashboard — pel/repellant.md": {
    "primary": "An alternative spelling of repellent, denoting a substance or quality that drives away pests, moisture, or unwanted intrusion.",
    "secondary": "In textile technology and surface finishing, hydrophobic wax coatings impart water-repellant properties to heavy canvas outerwear.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "The Maine Woods", "quote": "The Indian guides applied an aromatic oil to their hands as an effective **repellant** against blackflies."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Certain plants secrete bitter resins that act as a natural **repellant** against phytophagous larvae."},
      {"author": "Thomas Carlyle", "work": "Past and Present", "quote": "A cold, selfish pedantry is the most **repellant** feature that can disfigure human intellectual culture."}
    ]
  },
  "Dashboard — pel/repellent.md": {
    "primary": "Causing intense aversion or disgust; or capable of driving away insects, water, or other intrusive agents.",
    "secondary": "In sensory physiology and chemical ecology, alarm pheromones emit chemically repellent volatile compounds to deter predators.",
    "quotes": [
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "The savage pygmy displayed a facial expression that was grotesque and utterly **repellent** to civilized eyes."},
      {"author": "Mary Shelley", "work": "Frankenstein", "quote": "The monster beheld his own **repellent** features reflected in the pool and wept at his hideous deformity."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Darcy's initial demeanor at the assembly ball was pronounced disagreeable and thoroughly **repellent**."}
    ]
  },
  "Dashboard — pel/repelling.md": {
    "primary": "Driving back, forcing away, or resisting an advancing force, liquid, or intrusive entity; causing revulsion.",
    "secondary": "In colloid chemistry and interface phenomena, electrostatic double layers generate repelling forces that stabilize colloidal suspensions.",
    "quotes": [
      {"author": "Walter Scott", "work": "Ivanhoe", "quote": "The Saxon archers rained arrows upon the Norman attackers, **repelling** every desperate assault against the palisade."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The two suspended pith balls exhibited mutually **repelling** tendencies when charged with identical vitreous electricity."},
      {"author": "Charlotte Brontë", "work": "Jane Eyre", "quote": "There was something cold and **repelling** in St. John Rivers's austere manner that checked any spontaneous confidence."}
    ]
  },

  # --- Dashboard — phor (21 words) ---
  "Dashboard — phor/anaphora.md": {
    "primary": "The deliberate repetition of a word or phrase at the beginning of successive sentences, clauses, or poetic lines.",
    "secondary": "In classical rhetoric and stylistic prose, anaphora establishes rhythmic cadence, emotional emphasis, and memorable oratorical climaxes.",
    "quotes": [
      {"author": "Quintilian", "work": "Institutio Oratoria", "quote": "The orator heightened the emotional urgency of his plea by employing **anaphora** across successive interrogative clauses."},
      {"author": "Alexander Pope", "work": "An Essay on Criticism", "quote": "Careful poets employ harmonious **anaphora** to link rhyming couplets into a seamless thematic whole."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Coleridge analyzed how Milton's majestic blank verse used **anaphora** to accumulate sublime spiritual momentum."}
    ]
  },
  "Dashboard — phor/chromatophore.md": {
    "primary": "A pigment-containing or light-reflecting cell found in the skin of cephalopods, amphibians, fish, and reptiles.",
    "secondary": "In marine invertebrate neurobiology, radial muscle fibers contract around each chromatophore to produce rapid chromatic camouflage.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Voyage of the Beagle", "quote": "The cuttlefish displayed rapid chromatic changes as each **chromatophore** expanded and contracted across its iridescent skin."},
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "Microscopic sections through the cephalopod integument reveal layers of radiant **chromatophore** cells linked to neural fibers."},
      {"author": "H. G. Wells", "work": "The Sea Raiders", "quote": "The mysterious tentacled sea monster flushed dark crimson as every dermal **chromatophore** darkened under excitement."}
    ]
  },
  "Dashboard — phor/diaphoresis.md": {
    "primary": "Profuse, heavy perspiration or sweating, often artificially induced or occurring as a clinical symptom.",
    "secondary": "In clinical cardiology and emergency medicine, sudden diaphoresis combined with substernal chest pressure suggests acute myocardial infarction.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The sudden defervescence of the patient's fever was accompanied by drenching nocturnal **diaphoresis** and profound relief."},
      {"author": "Arthur Conan Doyle", "work": "Round the Red Lamp", "quote": "The old doctor noted the cold clammy **diaphoresis** bead upon the forehead of the poisoned patient."},
      {"author": "Henry Gray", "work": "Anatomy of the Human Body", "quote": "Sympathetic autonomic stimulation of the eccrine sweat glands induces generalized systemic **diaphoresis** under acute stress."}
    ]
  },
  "Dashboard — phor/diaphoretic.md": {
    "primary": "Producing, stimulating, or promoting perspiration; an agent or medicine that induces sweating.",
    "secondary": "In historical pharmacotherapy and herbal medicine, elderflower, antimony, and Dover's powder were administered as a diaphoretic to break fevers.",
    "quotes": [
      {"author": "William Osler", "work": "Aequanimitas", "quote": "The physician prescribed a warm herbal infusion and a mild **diaphoretic** to promote cutaneous capillary circulation."},
      {"author": "Tobias Smollett", "work": "The Expedition of Humphry Clinker", "quote": "Doctor Lewis recommended a gentle **diaphoretic** draught to resolve the stubborn autumnal catarrh."},
      {"author": "Oliver Goldsmith", "work": "The Vicar of Wakefield", "quote": "The kind apothecary administered a soothing **diaphoretic** mixture to calm the feverish invalid."}
    ]
  },
  "Dashboard — phor/dysphoria.md": {
    "primary": "A persistent, profound state of emotional unease, dissatisfaction, anxiety, or discontent.",
    "secondary": "In clinical psychiatry and mood diagnostics, dysphoria manifests as pervasive restlessness, anhedonia, and affective irritability.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The melancholy temperament often experiences periods of acute **dysphoria** where the entire universe seems devoid of meaning."},
      {"author": "H. G. Wells", "work": "The New Machiavelli", "quote": "A wave of restless **dysphoria** swept over the young politician, leaving him dissatisfied with his parliamentary success."},
      {"author": "Thomas Mann", "work": "The Magic Mountain", "quote": "Hans Castorp recognized a peculiar psychological **dysphoria** settling upon the convalescents in the alpine sanatorium."}
    ]
  },
  "Dashboard — phor/dysphoric.md": {
    "primary": "Characterized by, afflicted with, or expressing severe emotional discontent, restlessness, or dysphoria.",
    "secondary": "In neuropsychopharmacology, kappa-opioid receptor agonists elicit dysphoric cognitive responses and perceptual aversion in clinical trials.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "In chronic neurasthenia, patients endure a **dysphoric** mood that colors every sensory perception with gloom."},
      {"author": "Virginia Woolf", "work": "Mrs Dalloway", "quote": "Septimus experienced sudden **dysphoric** terrors that tore him away from the sunlit reality of the London park."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Casaubon passed into a silent, **dysphoric** retreat whenever his mythological scholarship was politely questioned."}
    ]
  },
  "Dashboard — phor/electrophoresis.md": {
    "primary": "The migration of dispersed colloidal particles or charged macromolecules under the influence of an applied electric field.",
    "secondary": "In molecular genetics and biochemistry, gel electrophoresis separates DNA, RNA, and protein fragments according to molecular size and net charge.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The migration of suspended particles under galvanic tension demonstrates the foundational principles of modern **electrophoresis**."},
      {"author": "Thomas Henry Huxley", "work": "Science and Culture", "quote": "The laboratory separation of biological albuminous substances relies upon electrical migration techniques related to **electrophoresis**."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "By employing zone **electrophoresis**, researchers isolated aberrant hemoglobin molecules in hereditary sickle-cell anemia."}
    ]
  },
  "Dashboard — phor/electrophoretic.md": {
    "primary": "Pertaining to, produced by, or utilized in electrophoresis.",
    "secondary": "In analytical clinical chemistry, measuring the electrophoretic mobility of serum globulins provides diagnostic patterns for paraproteinemias.",
    "quotes": [
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The abnormal protein exhibited a distinctive **electrophoretic** mobility profile compared to healthy adult hemoglobin."},
      {"author": "Thomas Henry Huxley", "work": "Lessons in Elementary Physiology", "quote": "Modern biochemical analyses verify that **electrophoretic** separation reveals multiple distinct enzymatic fractions in serum."},
      {"author": "Francis Crick", "work": "What Mad Pursuit", "quote": "The laboratory technician prepared the agarose gel for the **electrophoretic** fractionation of digested viral DNA."}
    ]
  },
  "Dashboard — phor/euphoria.md": {
    "primary": "A feeling or state of intense excitement, happiness, well-being, or elation.",
    "secondary": "In clinical psychopathology and addiction medicine, drug-induced euphoria alters dopaminergic mesolimbic reward pathways.",
    "quotes": [
      {"author": "William James", "work": "The Varieties of Religious Experience", "quote": "The mystical awakening was accompanied by a luminous **euphoria** that bathed the soul in serene heavenly joy."},
      {"author": "H. G. Wells", "work": "The Food of the Gods", "quote": "A reckless **euphoria** seized the giant youth as he strode across the countryside, feeling his boundless strength."},
      {"author": "Thomas De Quincey", "work": "Confessions of an English Opium-Eater", "quote": "The preliminary stage of intoxication produced an ethereal **euphoria** that banished all mortal sorrows for hours."}
    ]
  },
  "Dashboard — phor/metaphor.md": {
    "primary": "A figure of speech in which a word or phrase is applied to an object or action to which it is not literally applicable; an emblem.",
    "secondary": "In cognitive linguistics and conceptual blending theory, metaphor structures abstract human conceptual reasoning through embodied schemas.",
    "quotes": [
      {"author": "Aristotle", "work": "Poetics", "quote": "By far the greatest thing is to be a master of **metaphor**; it is the one thing that cannot be learned from others."},
      {"author": "John Locke", "work": "An Essay Concerning Human Understanding", "quote": "If we would speak of things as they are, we must allow that all figurative speech and **metaphor** serve only to mislead the judgment."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "A living **metaphor** awakens the dormant imagination by revealing the secret affinity between disparate natural forms."}
    ]
  },
  "Dashboard — phor/metaphoric.md": {
    "primary": "Characteristic of, relating to, or involving metaphor; figurative rather than literal.",
    "secondary": "In literary semiotics and hermeneutics, metaphoric language establishes polysemic layers of meaning within narrative allegory.",
    "quotes": [
      {"author": "Francis Bacon", "work": "The Advancement of Learning", "quote": "Ancient fables concealed deep political and philosophical truths beneath their rich **metaphoric** veil."},
      {"author": "Ralph Waldo Emerson", "work": "Nature", "quote": "All spiritual facts are expressed in **metaphoric** imagery drawn directly from the visible forms of the physical universe."},
      {"author": "Thomas Carlyle", "work": "Sartor Resartus", "quote": "Language itself is an immense fabric of **metaphoric** symbols woven by the creative spirit of humanity."}
    ]
  },
  "Dashboard — phor/metaphorical.md": {
    "primary": "Expressing or representing something through figurative comparison; symbolic and non-literal.",
    "secondary": "In philosophical theology, mystical texts employ metaphorical descriptions of the divine to overcome the limits of human speech.",
    "quotes": [
      {"author": "David Hume", "work": "Dialogues Concerning Natural Religion", "quote": "Cleanthes warned against taking the **metaphorical** expressions of ancient poets as exact metaphysical descriptions of deity."},
      {"author": "John Stuart Mill", "work": "A System of Logic", "quote": "Philosophical confusion arises when a **metaphorical** term is mistakenly treated as an empirical physical entity."},
      {"author": "George Eliot", "work": "The Mill on the Floss", "quote": "The roaring river operated as a **metaphorical** mirror of Maggie's passionate, turbulent inner nature."}
    ]
  },
  "Dashboard — phor/metaphorically.md": {
    "primary": "In a figurative or non-literal manner, through the symbolic use of metaphor.",
    "secondary": "In sociolinguistic discourse analysis, speakers employ military idioms metaphorically to structure commercial and political competition.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "Mr. Boffin remarked that he was speaking **metaphorically** when he referred to gold as the marrow of civilized bones."},
      {"author": "Arthur Conan Doyle", "work": "The Sign of the Four", "quote": "Holmes observed that the witness had expressed himself **metaphorically**, but the underlying clue was solid fact."},
      {"author": "Mark Twain", "work": "Life on the Mississippi", "quote": "The veteran steamboat pilot was speaking **metaphorically** when he declared that the river could smell a rising snag."}
    ]
  },
  "Dashboard — phor/phoradendron.md": {
    "primary": "A botanical genus of American mistletoes in the sandalwood family Santalaceae, parasitic upon woody trees.",
    "secondary": "In botanical ecology and phytopathology, species of Phoradendron penetrate host xylem conduits with invasive haustoria to extract sap.",
    "quotes": [
      {"author": "John Muir", "work": "The Mountains of California", "quote": "Dense clumps of parasitic **Phoradendron** clung to the rugged branches of the desert junipers along the canyon wall."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The mistletoe genus **Phoradendron** illustrates the intricate co-evolution between parasitic plants and bird seed dispersers."},
      {"author": "Asa Gray", "work": "Manual of the Botany of the Northern United States", "quote": "Botanical collectors identify the American mistletoe by the thick evergreen foliage and clustered berries of **Phoradendron**."}
    ]
  },
  "Dashboard — phor/phoronid.md": {
    "primary": "A marine, worm-like lophophorate invertebrate of the phylum Phoronida, living in secreted chitinous tubes in seafloor sediments.",
    "secondary": "In invertebrate marine zoology, each phoronid projects an anterior horseshoe-shaped lophophore of ciliated tentacles for suspension feeding.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The anatomical organization of the solitary **phoronid** links it structurally to both brachiopods and bryozoans."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The curious tube-dwelling **phoronid** preserves primitive lophophorate characteristics of deep evolutionary significance."},
      {"author": "E. B. Wilson", "work": "The Cell in Development and Inheritance", "quote": "Embryological cleavage in the **phoronid** exhibits radial blastomere division followed by an actinotroch larva."}
    ]
  },
  "Dashboard — phor/phoronida.md": {
    "primary": "A small phylum of marine benthic invertebrates comprising horseshoe worms that filter-feed from inside chitinous tubes.",
    "secondary": "In phylogenetic systematics and lophotrochozoan evolutionary biology, Phoronida forms a sister taxon to Brachiopoda within the Lophophorata.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "Taxonomists classify the horseshoe worms under the distinct invertebrate phylum **Phoronida** based on their lophophore anatomy."},
      {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "The coelomic cavity and actinotrocha larval stage of the **Phoronida** provide critical insights into deuterostome affinities."},
      {"author": "Ernst Haeckel", "work": "The History of Creation", "quote": "The evolutionary lineage of the **Phoronida** represents an ancient offshoot among marine coelomate organisms."}
    ]
  },
  "Dashboard — phor/phoronidea.md": {
    "primary": "An alternative zoological taxonomic designation for the lophophorate worm phylum or class Phoronida.",
    "secondary": "In historical zoological monographs, the order Phoronidea was defined by tubular benthic habit and circulatory vascular loops.",
    "quotes": [
      {"author": "Thomas Henry Huxley", "work": "Manual of the Anatomy of Invertebrated Animals", "quote": "The structural morphology of the **Phoronidea** exhibits an anterior tentacular crown dedicated to ciliary respiration and feeding."},
      {"author": "E. Ray Lankester", "work": "A Treatise on Zoology", "quote": "Comparative anatomists debated whether the **Phoronidea** should be grouped alongside the Polyzoa or the Brachiopoda."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The singular larval metamorphosis observed across the **Phoronidea** underscores the antiquity of marine invertebrate lineages."}
    ]
  },
  "Dashboard — phor/phosphoric.md": {
    "primary": "Of, relating to, or containing phosphorus, especially in its pentavalent state; or glowing with faint phosphorescence.",
    "secondary": "In agricultural soil science and industrial chemistry, phosphoric acid serves as the foundational chemical precursor for phosphate fertilizers.",
    "quotes": [
      {"author": "Herman Melville", "work": "Moby-Dick", "quote": "The Pequod cut through the midnight sea, leaving a long wake of green **phosphoric** radiance shimmering behind her."},
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "When phosphorus burns in oxygen, it yields dense white clouds of **phosphoric** acid anhydride that dissolve in water."},
      {"author": "Jules Verne", "work": "Twenty Thousand Leagues Under the Sea", "quote": "The salon window revealed swarms of oceanic medusae that illuminated the black abyss with **phosphoric** light."}
    ]
  },
  "Dashboard — phor/phosphorous.md": {
    "primary": "Of, relating to, or containing trivalent phosphorus; or emitting light in the dark without noticeable heat.",
    "secondary": "In inorganic synthetic chemistry, phosphorous acid acts as a powerful reducing agent by virtue of its oxidizable phosphorus-hydrogen bond.",
    "quotes": [
      {"author": "Robert Boyle", "work": "The Aerial Noctiluca", "quote": "The curious chemist observed the mild **phosphorous** vapor that emanated from the newly prepared mineral cake."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "The spectral hound's muzzle and eyes were ringed with a bluish **phosphorous** preparation that glowed in the dark."},
      {"author": "H. G. Wells", "work": "The Island of Doctor Moreau", "quote": "The tropical surf broke upon the dark volcanic coral reef in a fringe of soft, **phosphorous** fire."}
    ]
  },
  "Dashboard — phor/phosphorus.md": {
    "primary": "A highly reactive nonmetallic chemical element (symbol P, atomic number 15) essential for organic life and glowing in darkness when oxidized.",
    "secondary": "In cellular biochemistry and energetic metabolism, adenosine triphosphate utilizes high-energy phosphorus anhydride bonds to drive biological work.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "A single spark touches the dry **phosphorus**, and instantly it bursts into a dazzling, incandescent white flame."},
      {"author": "Arthur Conan Doyle", "work": "The Hound of the Baskervilles", "quote": "Holmes touched the hound's dead snout with his finger and sniffed the distinctive acrid scent of **phosphorus**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Organic bones and teeth contain large quantities of phosphate of lime, proving the ubiquitous necessity of **phosphorus** in life."}
    ]
  },
  "Dashboard — phor/semaphore.md": {
    "primary": "An apparatus or system for conveying visual signals and information using movable arms, mechanical flags, or lights.",
    "secondary": "In computer science and concurrent programming, Edsger Dijkstra introduced the semaphore primitive to synchronize access to shared resources.",
    "quotes": [
      {"author": "Alexander Dumas", "work": "The Count of Monte Cristo", "quote": "The telegraph tower waved its wooden **semaphore** arms across the hilltops, transmitting financial intelligence to Paris."},
      {"author": "Thomas Hardy", "work": "A Pair of Blue Eyes", "quote": "The railway signalman pulled the heavy iron lever, raising the mechanical **semaphore** to indicate a clear track."},
      {"author": "H. G. Wells", "work": "The War of the Worlds", "quote": "A military **semaphore** station flashed urgent optical signals toward London from the crest of Richmond Hill."}
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

print(f"Motion Batch 2A: Successfully updated {updated}/{len(data)} notes.")
