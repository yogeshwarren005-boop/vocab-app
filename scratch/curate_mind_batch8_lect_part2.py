# -*- coding: utf-8 -*-
"""
Curates Dashboard — lect (Part 2: words 66-130) in Cluster Mind & Knowledge.
"""
import os, sys, re

sys.stdout.reconfigure(encoding="utf-8")

data_part2 = {
  "electromagnet": {
    "primary": "A soft metal core made into a magnet by the passage of an electric current through a surrounding coil.",
    "secondary": "In industrial engineering, heavy magnetic hoists used in salvage yards to lift scrap iron and steel.",
    "quotes": [
      {"author": "Joseph Henry", "work": "On the Production of Currents and Sparks of Electricity", "quote": "By winding insulated copper wire in multiple compact layers, we constructed a powerful **electromagnet** capable of lifting a ton."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Placing heavy glass within the jaws of a powerful **electromagnet** rotated the plane of polarized light."},
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "The polyphase alternating field in the stator acted as a revolving **electromagnet**, dragging the rotor without brushes."}
    ]
  },
  "electromagnetic": {
    "primary": "Relating to the interrelation of electric currents or fields and magnetic fields.",
    "secondary": "In physics, the fundamental interaction (one of four universal forces) mediated through massless photons.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Dynamical Theory of the Electromagnetic Field", "quote": "We have strong reasons to conclude that light itself is an **electromagnetic** disturbance in the form of waves."},
      {"author": "Albert Einstein", "work": "On the Electrodynamics of Moving Bodies", "quote": "Maxwell's **electromagnetic** equations lead to asymmetries which do not appear to be inherent in the phenomena."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "The propagation of **electromagnetic** radiation through empty space is described completely by wave equations."}
    ]
  },
  "electromagnetics": {
    "primary": "The branch of physical science that deals with the physical phenomena and laws of electromagnetism.",
    "secondary": "In electrical engineering curricula, the mathematical study of Maxwell's equations and wave propagation.",
    "quotes": [
      {"author": "Oliver Heaviside", "work": "Electromagnetic Theory", "quote": "Modern vector analysis simplified the mathematical foundations of theoretical **electromagnetics** immensely."},
      {"author": "Charles Proteus Steinmetz", "work": "Theory and Calculation of Transient Electric Phenomena", "quote": "Practical engineering in **electromagnetics** required developing symbolic complex number notations for alternating circuits."},
      {"author": "Heinrich Hertz", "work": "Electric Waves", "quote": "Experimental verification of Maxwell's **electromagnetics** proved that radio oscillations travel at the speed of light."}
    ]
  },
  "electromagnetism": {
    "primary": "One of the fundamental physical interactions, involving forces between electrically charged particles.",
    "secondary": "In the history of science, the unified physical theory synthesizing electricity, optics, and magnetism.",
    "quotes": [
      {"author": "Hans Christian Ørsted", "work": "Experiments on the Effect of a Current of Electricity on the Magnetic Needle", "quote": "The deflection of the compass needle by a galvanic wire demonstrated the long-sought reality of **electromagnetism**."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The comprehensive mathematical laws of **electromagnetism** bind light, electricity, and magnetic induction into unity."},
      {"author": "Carl Sagan", "work": "Cosmos", "quote": "Without **electromagnetism**, atomic nuclei could not bind electrons, and chemical molecules could never form."}
    ]
  },
  "electromechanical": {
    "primary": "Relating to, involving, or operated by a combination of electrical and mechanical processes or devices.",
    "secondary": "In technology history, relays, stepping switches, and calculating tabulators that preceded solid-state electronics.",
    "quotes": [
      {"author": "Alan Turing", "work": "Enigma and the Bombe", "quote": "The British Bombe utilized high-speed **electromechanical** drums to test thousands of cipher combinations each minute."},
      {"author": "Claude Shannon", "work": "A Symbolic Analysis of Relay and Switching Circuits", "quote": "Boolean algebra maps directly onto the open and closed states of **electromechanical** switching relays."},
      {"author": "Norbert Wiener", "work": "Cybernetics", "quote": "Early industrial servomechanisms combined **electromechanical** sensors with hydraulic governors to regulate artillery."}
    ]
  },
  "electrometer": {
    "primary": "An electrical instrument designed for measuring electric potential difference or electrostatic charge without current draw.",
    "secondary": "In radiation physics, quadrant and gold-leaf instruments used to measure ionization caused by radioactive ores.",
    "quotes": [
      {"author": "Lord Kelvin", "work": "Reprint of Papers on Electrostatics and Magnetism", "quote": "The absolute quadrant **electrometer** allowed physicists to determine electric potentials in true electrostatic units."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "We measured the radioactivity of pitchblende by observing the rate of discharge upon a Curie quartz-piezoelectric **electrometer**."},
      {"author": "Ernest Rutherford", "work": "Radioactivity", "quote": "The ionization produced by alpha radiation was quantified with a calibrated quadrant **electrometer** in air."}
    ]
  },
  "electromotive": {
    "primary": "Tending to produce or maintain an electric current; relating to electromotive force (EMF).",
    "secondary": "In electrochemistry, the potential energy difference across a voltaic cell measured in open-circuit volts.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Relative motion between a conductor and magnetic field lines generates an induced **electromotive** force."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The total **electromotive** intensity along a closed circuit equals the negative time rate of change of magnetic flux."},
      {"author": "Oliver Heaviside", "work": "Electrical Papers", "quote": "Impressed **electromotive** forces drive charge through resistance, dissipating energy as Joule heat."}
    ]
  },
  "electromyogram": {
    "primary": "A recorded graphical tracing of the electrical potentials generated by muscle tissue during contraction; an EMG.",
    "secondary": "In clinical neurology, a diagnostic record evaluating myopathies, peripheral neuropathies, and motor neuron disease.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The diagnostic **electromyogram** showed intact motor unit action potentials despite dense sensory neglect in the limb."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "A normal concentric needle **electromyogram** demonstrates electrical silence when resting muscle is completely relaxed."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Fibrillation potentials detected upon the **electromyogram** provide crucial diagnostic evidence of denervation."}
    ]
  },
  "electromyograph": {
    "primary": "An instrument or medical apparatus used for recording the electrical activity and potentials of muscle fibers.",
    "secondary": "In clinical neurophysiology laboratories, an amplifier system connected to needle electrodes and audio monitors.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The physician adjusted the audio amplifier of the **electromyograph**, listening to the characteristic crackle of muscle units."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Connecting a dual-channel **electromyograph** allowed researchers to monitor reciprocal inhibition in opposing flexors."},
      {"author": "Atul Gawande", "work": "Complications", "quote": "The neurologist wheeled in the **electromyograph** to evaluate mysterious progressive weakness in the patient's legs."}
    ]
  },
  "electromyographic": {
    "primary": "Relating to or obtained by electromyography; pertaining to the recording of muscle electrical activity.",
    "secondary": "In biomechanics and ergonomics, evaluating muscular fatigue and activation patterns during physical labor.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "High-density **electromyographic** arrays reveal how motor units are recruited in strict order of increasing size."},
      {"author": "Oliver Sacks", "work": "The Man Who Mistook His Wife for a Hat", "quote": "Extensive **electromyographic** testing confirmed that his muscular weakness had a peripheral neuropathic origin."},
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Post-traumatic nerve repairs were monitored over months using serial **electromyographic** conduction studies."}
    ]
  },
  "electromyography": {
    "primary": "The medical diagnostic technique of recording and evaluating the electrical activity produced by skeletal muscles.",
    "secondary": "In clinical medicine, needle electrode examination paired with nerve conduction velocity studies.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Clinical **electromyography** provides an indispensable window into motor neuron survival and neuromuscular transmission."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The physical therapist relied upon **electromyography** to guide biofeedback training for re-educating paretic muscles."},
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "Advances in diagnostic **electromyography** helped untangle complex peripheral neuropathies from primary myopathies."}
    ]
  },
  "electron": {
    "primary": "A stable subatomic particle with a negative elementary electric charge, acting as the primary carrier of electricity in solids.",
    "secondary": "In quantum mechanics, a fundamental lepton possessing half-integer spin (1/2) that occupies atomic orbital shells.",
    "quotes": [
      {"author": "J. J. Thomson", "work": "Cathode Rays", "quote": "We have in the cathode rays matter in a new state, consisting of universal corpuscles, known now as the **electron**."},
      {"author": "Niels Bohr", "work": "On the Constitution of Atoms and Molecules", "quote": "The **electron** revolves around the nucleus in discrete stationary orbits without radiating electromagnetic energy."},
      {"author": "Richard Feynman", "work": "QED: The Strange Theory of Light and Matter", "quote": "Quantum electrodynamics calculates with astonishing precision how an **electron** interacts with photons of light."}
    ]
  },
  "electronegative": {
    "primary": "Having a tendency to attract electrons or acquire negative charge in chemical bonds; negatively charged.",
    "secondary": "In chemistry, nonmetallic elements such as fluorine and oxygen that sit high on the Pauling scale.",
    "quotes": [
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Fluorine is the most **electronegative** of all elements, pulling bonding electron density intensely toward its nucleus."},
      {"author": "Jöns Jacob Berzelius", "work": "Treatise on Chemistry", "quote": "His dualistic theory classified all elements into electropositive metals and **electronegative** acid-formers."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "During decomposition, the **electronegative** element migrates towards the positive anode of the cell."}
    ]
  },
  "electronegativity": {
    "primary": "The chemical property describing the tendency of an atom to attract shared electron pairs in a chemical bond toward itself.",
    "secondary": "In structural chemistry, the quantitative scale formulated by Linus Pauling based on bond dissociation energies.",
    "quotes": [
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "The degree of ionic character in a covalent bond is determined directly by the difference in **electronegativity**."},
      {"author": "Svante Arrhenius", "work": "Textbook of Chemistry", "quote": "Trends across the periodic table reveal that atomic **electronegativity** increases toward the upper right corner."},
      {"author": "Robert Mulliken", "work": "A New Scale of Electronegativity", "quote": "Mulliken defined **electronegativity** as the arithmetic mean of an atom's ionization potential and electron affinity."}
    ]
  },
  "electroneutral": {
    "primary": "Possessing balanced positive and negative electrical charges; bearing zero net electric charge.",
    "secondary": "In cellular biochemistry, ion transport mechanisms (such as Na+/H+ exchangers) that maintain zero net charge transfer.",
    "quotes": [
      {"author": "Svante Arrhenius", "work": "The Theory of Electrolytic Dissociation", "quote": "The bulk aqueous electrolyte remains strictly **electroneutral**, containing equal totals of positive and negative equivalents."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Certain transport proteins perform **electroneutral** exchange, swapping one chloride ion for one bicarbonate ion."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Chemistry", "quote": "A normal chemical compound is completely **electroneutral** until electrical forces separate its constituent ions."}
    ]
  },
  "electronic": {
    "primary": "Relating to electrons, electronic devices, digital systems, or computer technology; operated by microcircuits.",
    "secondary": "In physics, transitions of electrons between quantized atomic energy levels emitting or absorbing photons.",
    "quotes": [
      {"author": "Claude Shannon", "work": "The Mathematical Theory of Communication", "quote": "High-speed **electronic** circuits process information as binary digits transmitted across noisy channels."},
      {"author": "Walter Isaacson", "work": "The Innovators", "quote": "The transition from mechanical switches to solid-state **electronic** semiconductors unleashed the digital revolution."},
      {"author": "Arthur C. Clarke", "work": "Profiles of the Future", "quote": "Solid-state **electronic** microprocessors will soon compress library archives into pocketsize hand-held crystals."}
    ]
  },
  "electronically": {
    "primary": "By means of electronic devices, computers, or digital telecommunications; in an electronic manner.",
    "secondary": "In commerce and banking, transmitting financial payments and data packets across network lines.",
    "quotes": [
      {"author": "Nicholas Negroponte", "work": "Being Digital", "quote": "Information that was formerly printed upon heavy paper is now distributed **electronically** across the globe."},
      {"author": "Carl Sagan", "work": "Contact", "quote": "The radio telescope array was steered **electronically**, synthesizing a synthetic aperture miles across."},
      {"author": "Shoshana Zuboff", "work": "The Age of Surveillance Capitalism", "quote": "Every consumer transaction is captured **electronically**, converted into behavioral surplus data for modeling."}
    ]
  },
  "electronics": {
    "primary": "The branch of physics and engineering that deals with the emission, flow, and control of electrons in semiconductors and circuits.",
    "secondary": "In industrial technology, commercial devices containing microchips, transistors, and printed circuit boards.",
    "quotes": [
      {"author": "Richard Feynman", "work": "There's Plenty of Room at the Bottom", "quote": "Miniaturization in solid-state **electronics** will allow us to engrave entire encyclopedias on the head of a pin."},
      {"author": "Walter Isaacson", "work": "Steve Jobs", "quote": "Jobs combined passion for austere Zen design with fanatical reverence for clean engineering inside consumer **electronics**."},
      {"author": "John von Neumann", "work": "The Computer and the Brain", "quote": "The operational speed of biological synapses is millions of times slower than modern vacuum-tube **electronics**."}
    ]
  },
  "electrophoresis": {
    "primary": "The migration of dispersed colloidal particles or macromolecules in a fluid under the influence of an electric field.",
    "secondary": "In molecular genetics, gel electrophoresis used to separate and size DNA, RNA, and protein fragments.",
    "quotes": [
      {"author": "Arne Tiselius", "work": "A New Apparatus for Electrophoretic Analysis of Colloidal Mixtures", "quote": "Moving boundary **electrophoresis** allowed us to separate serum globulins into distinct alpha, beta, and gamma fractions."},
      {"author": "James D. Watson", "work": "The Double Helix", "quote": "Polyacrylamide gel **electrophoresis** provided clean resolution of radioactive nucleic acid restriction bands."},
      {"author": "Siddhartha Mukherjee", "work": "The Gene", "quote": "Under the blue fluorescent transilluminator, the glowing **electrophoresis** lanes revealed the mutant Huntington gene."}
    ]
  },
  "electrophoretic": {
    "primary": "Relating to, produced by, or utilized in electrophoresis; pertaining to particle migration in electric fields.",
    "secondary": "In physical chemistry, electrophoretic mobility measuring the velocity of a charged particle per unit field strength.",
    "quotes": [
      {"author": "Arne Tiselius", "work": "Nobel Lecture", "quote": "The **electrophoretic** mobility of proteins depends upon net surface charge, molecular size, and buffer pH."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Phosphorylated protein bands were identified by their altered **electrophoretic** migration on SDS-PAGE gels."},
      {"author": "Linus Pauling", "work": "Sickle Cell Anemia, a Molecular Disease", "quote": "Our **electrophoretic** analysis demonstrated that sickle hemoglobin carries a distinct surface charge from normal hemoglobin."}
    ]
  },
  "electrophoridae": {
    "primary": "The historical family of gymnotiform freshwater neotropical fishes comprising the electric eel (Electrophorus electricus).",
    "secondary": "In ichthyological systematics, electric knifefishes possessing electrogenic organs capable of producing high-voltage discharges.",
    "quotes": [
      {"author": "Alexander von Humboldt", "work": "Personal Narrative of Travels to the Equinoctial Regions", "quote": "Indigenous fishermen guided our canoes to the murky Amazonian pools inhabited by the formidable **Electrophoridae**."},
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "The electric organs of **Electrophoridae** present a celebrated difficulty for natural selection, having evolved independently in several lines."},
      {"author": "Richard Owen", "work": "Lectures on the Comparative Anatomy of Vertebrates", "quote": "The giant electric batteries of the **Electrophoridae** are constructed from thousands of modified, stacked electrocytes."}
    ]
  },
  "electrophorus": {
    "primary": "A physical apparatus invented by Alessandro Volta in 1775 to generate electrostatic charge by electrostatic induction.",
    "secondary": "In zoological taxonomy, the genus containing the electric eel (Electrophorus electricus) of South American rivers.",
    "quotes": [
      {"author": "Alessandro Volta", "work": "Letters on the Electrophorus", "quote": "I constructed an **electrophorus** of resin and brass that supplies perpetual electric charge without repeated rubbing."},
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The metal cover of the **electrophorus** acquires a charge of the opposite sign when touched while resting upon the cake."},
      {"author": "Alexander von Humboldt", "work": "Views of Nature", "quote": "The discharge of a giant **Electrophorus** stunned horses driven into the Llanos marshland to capture specimens."}
    ]
  },
  "electroplate": {
    "primary": "To coat an object with a thin layer of metal (such as silver, gold, or nickel) using electrolytic deposition.",
    "secondary": "In decorative arts, silver-plated hollowware manufactured by galvanic electrodeposition on base metals.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Chemical Manipulation", "quote": "By using a cyanide bath, one can evenly **electroplate** copper tableware with a durable, brilliant film of pure silver."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "We built automated vats to **electroplate** delicate phonograph cylinders with copper prior to mass stamping."},
      {"author": "Charles Dickens", "work": "Our Mutual Friend", "quote": "The Veneerings were brand-new people in a brand-new house, looking as though they had just been dipped in an **electroplate** bath."}
    ]
  },
  "electroplater": {
    "primary": "A person or commercial enterprise that electroplates metals and conducts electrodeposition manufacturing.",
    "secondary": "In Victorian manufacturing history, tradesmen operating galvanic baths to produce affordable silver-plated utensils.",
    "quotes": [
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The prosperous **electroplater** supplied Birmingham showrooms with glittering teapots and tableware for the middle class."},
      {"author": "Arthur Conan Doyle", "work": "The Red-Headed League", "quote": "Vincent Spaulding claimed to work as an assistant to an **electroplater** in the dim cellar beneath the pawnshop."},
      {"author": "H. G. Wells", "work": "Tono-Bungay", "quote": "His uncle apprenticed him briefly to an **electroplater**, where he learned the pungent smells of acid vats and dynamos."}
    ]
  },
  "electropositive": {
    "primary": "Having a tendency to lose electrons and form positive ions in chemical reactions; carrying a positive charge.",
    "secondary": "In inorganic chemistry, metallic elements (such as sodium, potassium, and cesium) with low electronegativities.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "Hydrogen and metallic bases are **electropositive**, migrating toward the negative cathode in electrolysis."},
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Alkali metals are the most **electropositive** elements in the periodic system, reacting vigorously with halogens."},
      {"author": "Jöns Jacob Berzelius", "work": "Theory of Chemical Proportions", "quote": "Chemical combination occurs because **electropositive** and electronegative radicals attract and neutralize each other."}
    ]
  },
  "electroretinogram": {
    "primary": "A recorded graphical tracing of the electrical potentials generated by the retina in response to light stimulation; an ERG.",
    "secondary": "In clinical ophthalmology, a diagnostic test measuring photopic and scotopic rod and cone photoreceptor function.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "The Island of the Colorblind", "quote": "The islanders' **electroretinogram** confirmed complete congenital absence of cone function, with only rod signals remaining."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "A flash of bright light produces a biphasic **electroretinogram**, with an a-wave from photoreceptors and a b-wave from bipolar cells."},
      {"author": "Santiago Ramón y Cajal", "work": "The Structure of the Retina", "quote": "The complex neural strata of the retina generate distinctive electrical responses captured upon the **electroretinogram**."}
    ]
  },
  "electroscope": {
    "primary": "An early scientific instrument used to detect the presence, sign, and magnitude of electric charge on a body.",
    "secondary": "In radioactivity history, the gold-leaf electroscope used to measure ionizing radiation and discover cosmic rays.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The delicate gold leaves of the **electroscope** diverged widely the moment the charged rod approached the brass disc."},
      {"author": "Marie Curie", "work": "Radioactive Substances", "quote": "A charged gold-leaf **electroscope** discharged rapidly when brought near pitchblende residues, revealing strong activity."},
      {"author": "Victor Hess", "work": "The Discovery of Cosmic Rays", "quote": "Taking an airtight **electroscope** aloft in a free balloon revealed that ionizing radiation increases dramatically with altitude."}
    ]
  },
  "electroshock": {
    "primary": "The administration of brief electric currents to the brain to treat psychiatric disorders; electroconvulsive therapy (ECT).",
    "secondary": "In clinical psychiatry, a treatment introduced by Cerletti and Bini in 1938 for severe, medication-resistant depression.",
    "quotes": [
      {"author": "Sylvia Plath", "work": "The Bell Jar", "quote": "She dreaded the violent morning sessions of **electroshock** that wiped out memory and left a dry, scorched taste."},
      {"author": "Kay Redfield Jamison", "work": "An Unquiet Mind", "quote": "When pharmacotherapy failed to lift the paralyzing depression, modern bilateral **electroshock** restored her vitality."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Post-encephalitic depression proved stubbornly unresponsive to conventional sedatives, leading some to attempt **electroshock**."}
    ]
  },
  "electrosleep": {
    "primary": "A therapeutic state of sleep or relaxation induced by the passage of low-intensity electrical currents through the brain.",
    "secondary": "In mid-twentieth-century neurotherapy, cranial electrotherapy stimulation (CES) used experimentally for insomnia and anxiety.",
    "quotes": [
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "Soviet neuropsychiatrists explored **electrosleep** therapy, applying gentle pulsed currents to soothe agitated insomniacs."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Early studies on **electrosleep** attempted to synchronize cortical slow-wave oscillations through rhythmic cranial pulses."},
      {"author": "Kay Redfield Jamison", "work": "Touched with Fire", "quote": "Alternative treatments like **electrosleep** were briefly evaluated as non-pharmacological therapies for intractable mood disorders."}
    ]
  },
  "electrostatic": {
    "primary": "Relating to stationary electric charges, their equilibrium distributions, and the forces between them.",
    "secondary": "In physics, Coulomb's law describing the inverse-square electrostatic force between stationary charged particles.",
    "quotes": [
      {"author": "Charles-Augustin de Coulomb", "work": "Recherches sur l'Électricité et le Magnétisme", "quote": "The **electrostatic** attraction between two charged spheres varies inversely as the square of the distance between them."},
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The lines of force in an **electrostatic** field originate on positive charges and terminate on negative charges."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "Because opposite charges cancel out so precisely in bulk matter, the colossal magnitude of **electrostatic** forces is hidden."}
    ]
  },
  "electrostatically": {
    "primary": "In an electrostatic manner; by means of stationary electric charges or electrostatic attraction.",
    "secondary": "In industrial manufacturing, applying paint or powder coatings using electrostatic attraction to coat workpieces evenly.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Experimental Researches in Electricity", "quote": "The dust particles were **electrostatically** attracted to the rubbed amber rod, clinging to its polished surface."},
      {"author": "Ernest Rutherford", "work": "Radioactive Transformations", "quote": "Beta rays were **electrostatically** deflected between charged parallel plates in a high-vacuum tube."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Industrial smokestacks installed precipitating plates to **electrostatically** capture fly ash before releasing flue gases."}
    ]
  },
  "electrostatics": {
    "primary": "The branch of physics that studies stationary electric charges, electrostatic fields, and Coulomb forces.",
    "secondary": "In classical field theory, Gauss's law and Poisson's equations determining electric potentials from charge distributions.",
    "quotes": [
      {"author": "James Clerk Maxwell", "work": "A Treatise on Electricity and Magnetism", "quote": "The foundational theorems of **electrostatics** were formulated by Cavendish, Coulomb, and Poisson with geometric elegance."},
      {"author": "Lord Kelvin", "work": "Reprint of Papers on Electrostatics and Magnetism", "quote": "The method of electrical images solved previously intractable boundary problems in theoretical **electrostatics**."},
      {"author": "Richard Feynman", "work": "The Feynman Lectures on Physics", "quote": "In **electrostatics**, the curl of the electric field is zero, which allows us to define a scalar potential."}
    ]
  },
  "electrosurgery": {
    "primary": "The application of high-frequency alternating electrical current to biological tissue to cut, coagulate, or fulgurate.",
    "secondary": "In modern operating theaters, utilizing Bovie electrosurgical generators to minimize intraoperative hemorrhage.",
    "quotes": [
      {"author": "Harvey Cushing", "work": "Electrosurgery as an Aid to the Removal of Intracranial Tumors", "quote": "The introduction of modern **electrosurgery** allowed us to excise vascular meningiomas that were previously inoperable."},
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Delicate hemostasis achieved through **electrosurgery** preserves the anatomical planes necessary for radical dissection."},
      {"author": "Atul Gawande", "work": "Better", "quote": "The surgeon tapped the foot pedal of the **electrosurgery** unit, vaporizing tissue with microsecond bursts of current."}
    ]
  },
  "electrotherapist": {
    "primary": "A medical specialist or practitioner who uses electrical currents and electrotherapy to treat physical ailments.",
    "secondary": "In historical physical medicine, a clinician operating galvanic, faradic, and high-frequency spark apparatus.",
    "quotes": [
      {"author": "William Osler", "work": "The Principles and Practice of Medicine", "quote": "The consulting **electrotherapist** applied rhythmic faradic stimulation to prevent disuse atrophy in paralyzed muscles."},
      {"author": "Arthur Conan Doyle", "work": "The Adventure of the Creeping Man", "quote": "Dr. Watson consulted a London **electrotherapist** regarding experimental currents for peripheral nerve rehabilitation."},
      {"author": "Nikola Tesla", "work": "High Frequency Oscillators for Electro-Therapeutic and Other Purposes", "quote": "Physicians and the skilled **electrotherapist** welcomed high-frequency currents that generated deep diathermic tissue warmth."}
    ]
  },
  "electrotherapy": {
    "primary": "The use of electrical energy and currents as a medical treatment to relieve pain, promote healing, or stimulate muscles.",
    "secondary": "In physical rehabilitation, modalities including TENS, neuromuscular electrical stimulation (NMES), and iontophoresis.",
    "quotes": [
      {"author": "William Stewart Halsted", "work": "Surgical Papers", "quote": "Following tendon repairs, gentle **electrotherapy** helped re-establish voluntary motor unit firing without tension."},
      {"author": "Oliver Sacks", "work": "A Leg to Stand On", "quote": "The rehabilitation clinic utilized **electrotherapy** to awaken dormant proprioceptive circuits in the paretic leg."},
      {"author": "Thomas Edison", "work": "The Diary and Sundry Observations", "quote": "Medical interest in **electrotherapy** prompted inquiries into our battery designs for portable clinical applications."}
    ]
  },
  "electrum": {
    "primary": "A natural or artificial alloy of gold and silver with trace copper, prized in antiquity for coinage and jewelry.",
    "secondary": "In numismatics, the pale yellow alloy used by the ancient Lydian kings in the 7th century BC to mint the earliest coins.",
    "quotes": [
      {"author": "Herodotus", "work": "The Histories", "quote": "The Lydians were the first men of whom we have knowledge who minted and used coins of gold and **electrum**."},
      {"author": "Pliny the Elder", "work": "Natural History", "quote": "When gold contains twenty percent silver, it is known as **electrum**, shining with a paler and cooler luster."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The sacred vessels of the temple in Jerusalem were fashioned from pure gold, silver, and gleaming **electrum**."}
    ]
  },
  "intellect": {
    "primary": "The faculty of reasoning, understanding, and thinking objectively, especially with regard to abstract matters.",
    "secondary": "In classical philosophy, the highest rational part of the soul (nous) that apprehends universal truths and forms.",
    "quotes": [
      {"author": "Aristotle", "work": "De Anima", "quote": "The human **intellect** is in a certain sense potentially whatever is thinkable, though actually it is nothing until it thinks."},
      {"author": "Immanuel Kant", "work": "Critique of Pure Reason", "quote": "Thoughts without content are empty, intuitions without concepts are blind; the **intellect** unites both in judgment."},
      {"author": "George Eliot", "work": "Middlemarch", "quote": "Dorothea was filled with reverent eagerness to be directed by a man of profound learning and superior **intellect**."}
    ]
  },
  "intellectual": {
    "primary": "Relating to the intellect, reason, or rational thinking, or a person possessing highly developed mental faculties.",
    "secondary": "In cultural history, a writer, academic, or thinker engaged in public critical discourse and political ideas.",
    "quotes": [
      {"author": "John Stuart Mill", "work": "On Liberty", "quote": "Truth gains more even by the errors of one who, with due study and preparation, thinks for himself, than by the true opinions of those who only hold them because they do not suffer themselves to think: that is **intellectual** freedom."},
      {"author": "George Orwell", "work": "The Lion and the Unicorn", "quote": "The English **intellectual** is characterized by a persistent emotional detachment from common national sentiment."},
      {"author": "Virginia Woolf", "work": "A Room of One's Own", "quote": "Intellectual freedom depends upon material things; poetry depends upon **intellectual** freedom."}
    ]
  },
  "intellectually": {
    "primary": "In an intellectual manner; with regard to the intellect, rational reasoning, or scholarly thought.",
    "secondary": "In critical evaluation, evaluating ideas or arguments on their logical and cognitive merit.",
    "quotes": [
      {"author": "Henry James", "work": "The Portrait of a Lady", "quote": "Gilbert Osmond was **intellectually** fastidious, rejecting modern vulgarities in favor of refined aesthetic seclusion."},
      {"author": "Bertrand Russell", "work": "The Problems of Philosophy", "quote": "Philosophy expands our thoughts beyond private hopes, rendering the mind **intellectually** free and impartial."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "Gwendolen found herself **intellectually** overmatched whenever Deronda quietly questioned her frivolous worldly ambitions."}
    ]
  },
  "lectern": {
    "primary": "A tall stand with a slanted top used to support a book, Bible, or lecture notes for a speaker or reader.",
    "secondary": "In church architecture, a carved eagle or brass pedestal supporting the gospel book in the sanctuary.",
    "quotes": [
      {"author": "Charles Dickens", "work": "The Mystery of Edwin Drood", "quote": "The choir master stepped up to the brass eagle **lectern** to begin the evensong service in the cathedral."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "Mr. Arabin stood beside the carved oak **lectern**, delivering his sermon with earnest and unadorned eloquence."},
      {"author": "Thomas Hardy", "work": "Tess of the d'Urbervilles", "quote": "The vicar rested his Bible upon the ancient church **lectern**, reading the lesson to the quiet village flock."}
    ]
  },
  "lectin": {
    "primary": "A plant or animal protein that binds specifically and reversibly to carbohydrates or cell surface glycoproteins.",
    "secondary": "In immunology and cellular biology, plant agglutinins (such as concanavalin A) used to identify cell surface glycans.",
    "quotes": [
      {"author": "Paul Ehrlich", "work": "Collected Papers on Immunology", "quote": "Ricin represents an extraordinarily potent phytotoxic **lectin** that agglutinates mammalian erythrocytes in vitro."},
      {"author": "Siddhartha Mukherjee", "work": "The Song of the Cell", "quote": "Researchers used fluorescently labeled **lectin** markers to track the dense carbohydrate forest on cancer cell coats."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Cellular recognition during synaptogenesis is mediated in part by **lectin** interactions with axonal glycan ligands."}
    ]
  },
  "lector": {
    "primary": "A person who reads Scripture lessons or prayers aloud during a religious worship service.",
    "secondary": "In European university systems, an academic lecturer or teacher of modern foreign languages.",
    "quotes": [
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The young Julian served as a **lector** in the Christian church of Nicomedia before turning to ancient pagan philosophy."},
      {"author": "Walter Scott", "work": "The Monastery", "quote": "The monastic **lector** ascended the wooden pulpit to read solemn homilies while the brethren dined in silence."},
      {"author": "Marcel Proust", "work": "Guermantes Way", "quote": "The German university appointed an exchange **lector** to instruct Parisian scholars in Goethe and Schiller."}
    ]
  },
  "lecture": {
    "primary": "An educational talk given to an audience or students, or a stern, solemn reprimand or scolding.",
    "secondary": "In academia, the traditional instructional method delivered by a professor in an auditorium.",
    "quotes": [
      {"author": "Michael Faraday", "work": "The Chemical History of a Candle", "quote": "In every **lecture** delivered to young listeners, I endeavor to let simple physical experiments speak for themselves."},
      {"author": "Jane Austen", "work": "Sense and Sensibility", "quote": "Mrs. Ferrars gave her daughter-in-law a severe private **lecture** on the necessity of family decorum."},
      {"author": "William James", "work": "Pragmatism", "quote": "The audience assembled in Boston for the opening **lecture** on philosophical pragmatism and common sense."}
    ]
  },
  "lecturer": {
    "primary": "A person who delivers lectures, especially a member of the academic teaching staff at a university or college.",
    "secondary": "In Victorian public culture, an itinerant speaker delivering educational discourses at mechanics' institutes.",
    "quotes": [
      {"author": "Thomas Carlyle", "work": "On Heroes, Hero-Worship, and the Heroic in History", "quote": "The **lecturer** stood before his London audience, speaking of Odin and the ancient Norse warrior spirit."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "The scientific **lecturer** illustrated his discourse with magic lantern slides of prehistoric reptiles."},
      {"author": "Ralph Waldo Emerson", "work": "Self-Reliance", "quote": "As an itinerant lyceum **lecturer**, he traversed frozen New England towns, preaching self-trust to young minds."}
    ]
  },
  "lectureship": {
    "primary": "The position, office, or appointment of a lecturer, especially an endowed post at a university.",
    "secondary": "In ecclesiastical history, a salaried preaching appointment funded by parishioners or guilds.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Endowed university **lectureship** positions often produce indolence in professors whose salaries do not depend on fees."},
      {"author": "Samuel Johnson", "work": "Lives of the Poets", "quote": "Swift obtained a modest cathedral **lectureship** in Dublin, which provided leisure for political pamphleteering."},
      {"author": "Anthony Trollope", "work": "Barchester Towers", "quote": "The newly established theological **lectureship** became the bone of fierce contention between High and Low churchmen."}
    ]
  },
  "lecturing": {
    "primary": "The activity or practice of delivering academic lectures, or reprimanding and scolding someone lengthily.",
    "secondary": "In higher education, the traditional pedagogical mode of oral instruction from prepared notes.",
    "quotes": [
      {"author": "Michael Faraday", "work": "Selected Correspondence", "quote": "My **lecturing** duties at the Royal Institution consume my mornings, leaving only afternoons for research."},
      {"author": "Mark Twain", "work": "Autobiography", "quote": "I spent three years **lecturing** across Australia, India, and South Africa to pay off my publishers' debts."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mr. Knightley was not fond of **lecturing** Emma, but sincere affection compelled him to point out her error."}
    ]
  },
  "nonelected": {
    "primary": "Not chosen by election; appointed, inherited, bureaucratic, or civil service in character.",
    "secondary": "In political science, judicial, regulatory, or administrative officials serving without electoral mandates.",
    "quotes": [
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The **nonelected** judiciary acts as an indispensable aristocratic brake upon the sudden passions of popular majorities."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "Federal judges remain **nonelected**, holding office during good behavior to guarantee judicial independence."},
      {"author": "Max Weber", "work": "Economy and Society", "quote": "Modern states rely upon permanent **nonelected** civil servants to administer complex administrative laws."}
    ]
  },
  "nonelective": {
    "primary": "Not elective; appointed or hereditary rather than chosen by popular vote, or mandatory in curricula.",
    "secondary": "In academic scheduling, required compulsory core subjects that all matriculated students must complete.",
    "quotes": [
      {"author": "A. V. Dicey", "work": "The Law of the Constitution", "quote": "The House of Lords represents a **nonelective** legislative chamber founded upon hereditary peerage and tradition."},
      {"author": "Edmund Burke", "work": "Reflections on the Revolution in France", "quote": "The monarchy is a **nonelective** magistracy that shields the kingdom from the turbulent feuds of faction."},
      {"author": "William Osler", "work": "Aequanimitas", "quote": "Basic human anatomy remained a strict **nonelective** requirement throughout the first two medical school years."}
    ]
  },
  "nonintellectual": {
    "primary": "Not intellectual; relating to practical, physical, or emotional matters rather than abstract rational thought.",
    "secondary": "In cultural sociology, describing activities, pastimes, or personalities unconcerned with academic scholarship.",
    "quotes": [
      {"author": "George Orwell", "work": "The Road to Wigan Pier", "quote": "The northern coal miners took pride in hearty **nonintellectual** recreations such as pigeon fancying and rugby."},
      {"author": "Bertrand Russell", "work": "In Praise of Idleness", "quote": "A balanced human life requires healthy **nonintellectual** physical labor and wholesome outdoor pursuits."},
      {"author": "Virginia Woolf", "work": "The Waves", "quote": "Percival stood as the supreme **nonintellectual** hero, commanding admiration through unreflecting bodily grace."}
    ]
  },
  "recollect": {
    "primary": "To remember, recall, or bring back to mind that which had been previously known or experienced.",
    "secondary": "In spiritual contemplation, to compose and collect one's mental faculties and emotions in quiet meditation.",
    "quotes": [
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Elizabeth tried to **recollect** some conversation that might justify Jane's optimistic hopes regarding Bingley."},
      {"author": "Charles Dickens", "work": "Great Expectations", "quote": "Pip could vividly **recollect** the terrifying cold mist rising from the marsh on that fateful Christmas morning."},
      {"author": "William Wordsworth", "work": "Preface to Lyrical Ballads", "quote": "Poetry takes its origin from emotion **recollected** in tranquility, contemplated until the feeling revives."}
    ]
  },
  "recollection": {
    "primary": "The action of remembering something, or a memory, impression, or mental revival of past events.",
    "secondary": "In introspective philosophy, the conscious retrieval of sensory or cognitive experiences from memory stores.",
    "quotes": [
      {"author": "Plato", "work": "Meno", "quote": "Socrates argued that all true learning is essentially **recollection** of eternal forms known before birth."},
      {"author": "Jane Austen", "work": "Persuasion", "quote": "The sweet **recollection** of their early love haunted Anne whenever she walked along the Somerset lanes."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The **recollection** of past imperial glory inspired the Romans to revolt against their Gothic masters."}
    ]
  },
  "recollective": {
    "primary": "Having the faculty or power of recollecting or remembering; relating to memories of past events.",
    "secondary": "In cognitive psychology, memory mechanisms involved in explicit, conscious episodic recall.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The **recollective** faculty depends upon associative neural paths connecting current sensory cues with past traces."},
      {"author": "Samuel Taylor Coleridge", "work": "Biographia Literaria", "quote": "Fancy is merely an aggregating and **recollective** power, whereas true Imagination is plastic and unifying."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Hippocampal synaptic plasticity underpins the **recollective** vividness of declarative autobiographical memory."}
    ]
  },
  "reelect": {
    "primary": "To elect someone again to a political office, public post, or official position they currently hold.",
    "secondary": "In democratic governance, renewing an official's term through a successful electoral campaign.",
    "quotes": [
      {"author": "Abraham Lincoln", "work": "Letter to Thurlow Weed", "quote": "The American people resolved to **reelect** the administration to preserve the Union and complete emancipation."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "The desire to **reelect** their favorite magistrates makes voters attentive to every act of local governance."},
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The constitutional eligibility to **reelect** the executive magistrate provides a powerful incentive for faithful service."}
    ]
  },
  "reelection": {
    "primary": "The election of someone to a further term of office or position; the act or outcome of being reelected.",
    "secondary": "In political campaigning, strategies and fundraising focused on defending an incumbent's seat.",
    "quotes": [
      {"author": "Alexander Hamilton", "work": "The Federalist Papers", "quote": "The prospect of **reelection** is necessary to give the magistrate a personal interest in defending his office."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "An incumbent president seeking **reelection** becomes a pliant tool in the hands of the electoral majority."},
      {"author": "Winston Churchill", "work": "The Second World War", "quote": "President Roosevelt secured an unprecedented fourth term **reelection** to guide the Allied coalition to final victory."}
    ]
  },
  "select": {
    "primary": "To carefully choose from a group of alternatives, or chosen for excellence, rarity, or high quality.",
    "secondary": "In evolutionary biology, natural forces that select adaptive phenotypic variations over generations.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Man can act only on external and visible characters; nature cares nothing for appearances, she can **select** for the good of the being."},
      {"author": "Jane Austen", "work": "Emma", "quote": "Mrs. Elton took pride in her **select** musical parties, boasting that only the first families were admitted."},
      {"author": "Francis Bacon", "work": "The Essays", "quote": "A wise prince will **select** counselors who dare to speak truth rather than flatter royal whims."}
    ]
  },
  "selected": {
    "primary": "Carefully chosen or singled out from a larger group on the basis of merit, preference, or fitness.",
    "secondary": "In publishing, a curated anthology containing chosen representative works or essays.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "Breeders have **selected** minute variations in pigeons for centuries, producing extraordinary breeds."},
      {"author": "William Wordsworth", "work": "Preface to Lyrical Ballads", "quote": "The principal object was to choose incidents and situations from common life, and to describe them in **selected** language."},
      {"author": "Edward Gibbon", "work": "The History of the Decline and Fall of the Roman Empire", "quote": "The praetorian guards **selected** Claudius from behind a palace curtain and proclaimed him emperor."}
    ]
  },
  "selection": {
    "primary": "The action of carefully choosing someone or something, or a curated collection of selected things.",
    "secondary": "In evolutionary biology, natural selection or sexual selection driving evolutionary adaptation.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "This preservation of favorable variations and the rejection of injurious variations, I call Natural **Selection**."},
      {"author": "Thomas Henry Huxley", "work": "Evolution and Ethics", "quote": "Cosmic nature operates through ruthless natural **selection**, whereas human civilization strives to curb competition."},
      {"author": "Jane Austen", "work": "Pride and Prejudice", "quote": "Mr. Bennet was delighted with his library, which contained an admirable **selection** of classical authors."}
    ]
  },
  "selective": {
    "primary": "Characterized by careful choice, high standards, or discrimination; tending to choose only certain things.",
    "secondary": "In pharmacology, drug molecules designed to bind selectively to specific receptor subtypes without off-target effects.",
    "quotes": [
      {"author": "William James", "work": "The Principles of Psychology", "quote": "Consciousness is at all times a **selective** agency, accentuating some aspects of sensation while suppressing others."},
      {"author": "Charles Darwin", "work": "The Descent of Man", "quote": "Female choice exerts a powerful **selective** pressure that enhances ornamental plumage and birdsong in males."},
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "Modern psychopharmacology developed **selective** serotonin reuptake inhibitors to reduce autonomic side effects."}
    ]
  },
  "selectively": {
    "primary": "In a selective manner; by careful choice, or so as to affect or choose only certain specific items.",
    "secondary": "In cellular biochemistry, biological membranes that selectively permit the passage of specific ions and metabolites.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "Agriculturalists breed cattle **selectively**, pairing only those beasts that display superior milk yield or hardiness."},
      {"author": "Eric Kandel", "work": "In Search of Memory", "quote": "Voltage-gated potassium channels open **selectively** to permit the rapid efflux of potassium ions during repolarization."},
      {"author": "Oliver Sacks", "work": "Awakenings", "quote": "The dopaminergic drug acted **selectively** on nigrostriatal terminals, leaving cortical pathways undisturbed."}
    ]
  },
  "selectivity": {
    "primary": "The capacity to choose selectively, discriminating precision, or sensitivity to specific stimuli.",
    "secondary": "In radio engineering, the ability of a receiver circuit to isolate a desired frequency from adjacent signals.",
    "quotes": [
      {"author": "Linus Pauling", "work": "The Nature of the Chemical Bond", "quote": "Enzymatic catalysis achieves extraordinary chemical **selectivity** through precise lock-and-key steric fits."},
      {"author": "William James", "work": "The Principles of Psychology", "quote": "The supreme **selectivity** of human attention allows a scholar to read uninterrupted amid street clamor."},
      {"author": "Nikola Tesla", "work": "My Inventions", "quote": "Tuned resonant circuits achieved astonishing radio **selectivity**, filtering out atmospheric static interference."}
    ]
  },
  "selectman": {
    "primary": "An elected member of a board of officials who administer the local government of a New England town.",
    "secondary": "In American civic history, the quintessential municipal magistrate executing the decisions of the town meeting.",
    "quotes": [
      {"author": "Henry David Thoreau", "work": "Walden", "quote": "The town **selectman** came down the road to inspect my rustic cabin, questioning its architectural conformity."},
      {"author": "Alexis de Tocqueville", "work": "Democracy in America", "quote": "In New England, the **selectman** is elected directly by his neighbors to pave roads, build schools, and collect taxes."},
      {"author": "Nathaniel Hawthorne", "work": "The Scarlet Letter", "quote": "A venerable **selectman** of the colony walked in the solemn procession, his severe brow crowned with Puritan dignity."}
    ]
  },
  "selector": {
    "primary": "A person or device that selects, chooses, or switches between different options, settings, or circuits.",
    "secondary": "In telecommunications, an automated rotary switch or mechanical crossbar connecting telephone circuits.",
    "quotes": [
      {"author": "Claude Shannon", "work": "A Symbolic Analysis of Relay and Switching Circuits", "quote": "An automated **selector** switch routes incoming calls by translating dial pulses into relay connections."},
      {"author": "Charles Darwin", "work": "The Variation of Animals and Plants under Domestication", "quote": "The pigeon fancier acts as an intentional **selector**, pairing prize carriers to enhance wattle growth."},
      {"author": "Alan Turing", "work": "Computing Machinery and Intelligence", "quote": "The electronic **selector** shifted the central processing unit between arithmetic registers in microseconds."}
    ]
  },
  "uncollected": {
    "primary": "Not gathered, assembled, or collected; not brought together into a collection or publication.",
    "secondary": "In finance, accounts receivable, revenues, or taxes that remain outstanding and unreceived.",
    "quotes": [
      {"author": "Virginia Woolf", "work": "The Common Reader", "quote": "Scores of brilliant critical essays remained **uncollected** in obscure periodicals until after the author's death."},
      {"author": "Charles Dickens", "work": "Little Dorrit", "quote": "The landlord lamented his **uncollected** rents, surveying the impoverished tenants of Bleeding Heart Yard."},
      {"author": "Charles Darwin", "work": "Autobiography", "quote": "Valuable fossil specimens remained **uncollected** along the Patagonian cliffs due to the rising tide."}
    ]
  },
  "uncollectible": {
    "primary": "Incapable of being collected, recovered, or redeemed, especially an unpaid financial debt or bad loan.",
    "secondary": "In commercial accounting, writing off bad debts as uncollectible losses against fiscal revenues.",
    "quotes": [
      {"author": "Adam Smith", "work": "The Wealth of Nations", "quote": "Reckless merchant loans become utterly **uncollectible** when speculative trade bubbles burst across the exchange."},
      {"author": "Anthony Trollope", "work": "The Way We Live Now", "quote": "The railway shares proved entirely **uncollectible**, collapsing into worthless scraps of decorative paper."},
      {"author": "Charles Dickens", "work": "Bleak House", "quote": "Costs in the Chancery suit had grown so vast that the estate's liabilities were permanently **uncollectible**."}
    ]
  },
  "unselected": {
    "primary": "Not chosen, picked, or singled out from a larger pool of candidates, items, or variations.",
    "secondary": "In statistical genetics, random control populations that have not undergone artificial or directed breeding.",
    "quotes": [
      {"author": "Charles Darwin", "work": "The Origin of Species", "quote": "In wild populations, **unselected** random variations are eliminated whenever seasonal hardships strike."},
      {"author": "George Eliot", "work": "Daniel Deronda", "quote": "The **unselected** suitors lingered in the drawing room, watching Gwendolen bestow her smiles upon Grandcourt."},
      {"author": "Francis Galton", "work": "Hereditary Genius", "quote": "Comparing **unselected** school populations against gifted cohorts revealed marked divergences in mental ability."}
    ]
  },
  "unselective": {
    "primary": "Lacking discrimination, careful choice, or critical standards; not selective, choosing without discernment.",
    "secondary": "In chemical pharmacology, medications or reagents that bind broadly across multiple receptor subtypes.",
    "quotes": [
      {"author": "Eric Kandel", "work": "Principles of Neural Science", "quote": "First-generation tricyclic antidepressants were **unselective**, triggering dry mouth and sedation via muscarinic blockade."},
      {"author": "Henry James", "work": "The Art of the Novel", "quote": "The novelist must avoid an **unselective** dump of raw realistic facts, crafting scenes with aesthetic restraint."},
      {"author": "Rachel Carson", "work": "Silent Spring", "quote": "Broad-spectrum pesticides represent an **unselective** chemical assault that slaughters beneficial pollinators alongside pests."}
    ]
  }
}
