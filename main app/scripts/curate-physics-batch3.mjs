import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — electr (43 words) ===
  "Dashboard — electr/electrograph.md": {
    primary: "An apparatus for recording electrical phenomena or transmitting photographs and drawings by telegraphy or wireless.",
    secondary: "In meteorological physics and historical telecommunications, an instrument for recording atmospheric electrical potential variations.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "Continuous photographic traces of the atmospheric potential were obtained using the self-registering **electrograph**." },
      { author: "Nikola Tesla", work: "Colorado Springs Notes", quote: "The sensitive **electrograph** recorded minute terrestrial electrical oscillations induced by lightning strikes hundreds of miles away." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The mechanism of the **electrograph** relies on a photographic cylinder rotated by clockwork beneath an electrometer mirror." }
    ]
  },
  "Dashboard — electr/electrologist.md": {
    primary: "A practitioner skilled in electrolysis for the permanent removal of unwanted human hair or cutaneous blemishes.",
    secondary: "Historically in Victorian science, an investigator or specialist in the therapeutic or experimental applications of electricity.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "For persistent hypertrichosis, consultation with an experienced **electrologist** provides the only permanent clinical remedy." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The **electrologist** carefully inserted the fine platinum needle into the hair follicle before closing the galvanic circuit." },
      { author: "S. Weir Mitchell", work: "Lectures on Diseases of the Nervous System", quote: "The medical **electrologist** employed localized faradic stimulation to assess neuromuscular responsiveness." }
    ]
  },
  "Dashboard — electr/electrolysis.md": {
    primary: "The chemical decomposition of an electrolyte produced by the passage of an electric current through a solution or molten salt.",
    secondary: "In dermatology, the permanent destruction of hair follicles or cosmetic lesions by localized electric current.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "To this process of electro-chemical decomposition I propose to assign the name **electrolysis**." },
      { author: "Humphry Davy", work: "On Some New Phenomena of Chemical Changes Produced by Electricity", quote: "Through the agency of **electrolysis**, the hitherto refractory caustic alkalis surrendered their metallic bases." },
      { author: "Svante Arrhenius", work: "The Theory of Electrolytic Dissociation", quote: "During **electrolysis**, cations migrate toward the negative electrode while anions move toward the positive pole." }
    ]
  },
  "Dashboard — electr/electrolyte.md": {
    primary: "A chemical substance that conducts electricity when dissolved in water or melted, through the movement of dissociated ions.",
    secondary: "In human physiology and medicine, essential mineral ions (such as sodium, potassium, calcium, and chloride) regulating cellular osmotic pressure and membrane potentials.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "I term that compound substance which is capable of being decomposed by the electric current an **electrolyte**." },
      { author: "Svante Arrhenius", work: "Textbook of Electrochemistry", quote: "In an aqueous **electrolyte**, the solute molecules undergo spontaneous dissociation into electrically charged ions." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "We monitored the patient's serum **electrolyte** concentrations hourly to correct the life-threatening hypokalemia." }
    ]
  },
  "Dashboard — electr/electrolytic.md": {
    primary: "Of, relating to, or produced by electrolysis or an electrolyte.",
    secondary: "In electronics, denoting components such as electrolytic capacitors utilizing an oxide dielectric film formed electrochemically.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The **electrolytic** action of a current is strictly proportional to the quantity of electricity that traverses the cell." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The commercial extraction of metallic aluminum relies upon the **electrolytic** reduction of bauxite dissolved in molten cryolite." },
      { author: "Oliver Heaviside", work: "Electromagnetic Theory", quote: "High-capacitance **electrolytic** cells were placed in the circuit to filter out ripple from the rectifying apparatus." }
    ]
  },
  "Dashboard — electr/electromagnet.md": {
    primary: "A soft metal core made into a magnet by the passage of electric current through a surrounding wire coil.",
    secondary: "In physics and electrical engineering, an artificial magnetic device whose magnetic field can be rapidly modulated or switched on and off.",
    quotes: [
      { author: "Joseph Henry", work: "On the Production of Currents and Sparks of Electricity from Magnetism", quote: "By wrapping many insulated coils around the soft iron horseshoe, our powerful **electromagnet** lifted over two thousand pounds." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The core of the **electromagnet** attains intense magnetization the instant current traverses the surrounding helix." },
      { author: "Jules Verne", work: "Twenty Thousand Leagues Under the Sea", quote: "A colossal **electromagnet** powered the rudders and dynamic navigation machinery of Captain Nemo's submarine." }
    ]
  },
  "Dashboard — electr/electromagnetic.md": {
    primary: "Of or relating to the interrelation of electric currents and magnetic fields.",
    secondary: "Pertaining to electromagnetic radiation, spanning gamma rays, X-rays, ultraviolet, visible light, infrared, and radio waves.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Dynamical Theory of the Electromagnetic Field", quote: "Light consists in the transverse undulations of the same medium which is the cause of electric and magnetic phenomena, constituting an **electromagnetic** wave." },
      { author: "Albert Einstein", work: "Relativity: The Special and General Theory", quote: "The electrodynamics of moving bodies revealed that the velocity of an **electromagnetic** signal in vacuum is a universal constant." },
      { author: "Heinrich Hertz", work: "Electric Waves", quote: "These experimental apparatuses proved beyond doubt the transverse nature and wave velocity of **electromagnetic** propagation." }
    ]
  },
  "Dashboard — electr/electromagnetics.md": {
    primary: "The branch of physical science that deals with the phenomena, laws, and mathematical formulation of electromagnetism.",
    secondary: "In applied electrical engineering, the rigorous study of wave propagation, Maxwell's equations, antennas, and transmission waveguides.",
    quotes: [
      { author: "Oliver Heaviside", work: "Electromagnetic Theory", quote: "In the study of modern **electromagnetics**, Maxwell's original twenty equations condense into four elegant vector relations." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "From the viewpoint of fundamental theory, classical **electromagnetics** remains one of the most complete and beautiful structures in science." },
      { author: "Charles Proteus Steinmetz", work: "Theory and Calculation of Transient Electric Phenomena", quote: "High-frequency power lines demand thorough mastery of theoretical **electromagnetics** to avoid destructive surge waves." }
    ]
  },
  "Dashboard — electr/electromagnetism.md": {
    primary: "One of the four fundamental interactions of nature, encompassing the physical forces and interactions between electrically charged particles.",
    secondary: "The unified physical theory demonstrating that electric and magnetic fields are dual aspects of a single fundamental gauge force.",
    quotes: [
      { author: "Hans Christian Ørsted", work: "Experiments on the Effect of a Current of Electricity on the Magnetic Needle", quote: "The conflict of electricity produces a circular magnetic whorl, establishing the reality of **electromagnetism**." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The whole science of **electromagnetism** may be deduced from the conservation of energy applied to electromagnetic fields." },
      { author: "Freeman Dyson", work: "Disturbing the Universe", quote: "The unification of optics with electricity through Maxwellian **electromagnetism** served as the template for all subsequent quantum field theories." }
    ]
  },
  "Dashboard — electr/electromechanical.md": {
    primary: "Relating to, being, or operating by a combination of electrical and mechanical processes or devices.",
    secondary: "Denoting devices such as relays, solenoids, motors, and early teleprinters or analog computers converting electrical energy to mechanical motion.",
    quotes: [
      { author: "Norbert Wiener", work: "Cybernetics: Or Control and Communication in the Animal and the Machine", quote: "Feedback loops in **electromechanical** servomechanisms anticipate the self-regulating homeostatic mechanisms of living organisms." },
      { author: "Claude Shannon", work: "A Symbolic Analysis of Relay and Switching Circuits", quote: "Boolean algebra maps perfectly onto the switching networks of **electromechanical** telephone exchanges." },
      { author: "Nikola Tesla", work: "My Inventions", quote: "The rotary converter represents a harmonious **electromechanical** synthesis of generator and motor upon a single shaft." }
    ]
  },
  "Dashboard — electr/electrometer.md": {
    primary: "An instrument for measuring electric potential difference or electrical charge by means of electrostatic forces.",
    secondary: "A delicate laboratory instrument (such as the quadrant electrometer or gold-leaf electroscope) crucial to early atomic and radiation physics.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "The divided-ring **electrometer** detected minute differences in atmospheric potential without drawing appreciable current." },
      { author: "Marie Curie", work: "Radioactive Substances", quote: "Pierre Curie constructed a piezoelectric quartz balance coupled to an **electrometer** to quantify the ionization produced by uranium rays." },
      { author: "Ernest Rutherford", work: "Radioactivity", quote: "The rate of discharge of the **electrometer** leaf provided a direct measure of alpha-particle emission from the thorium salt." }
    ]
  },
  "Dashboard — electr/electromotive.md": {
    primary: "Producing or capable of producing an electric current, especially through a difference in potential.",
    secondary: "Pertaining to electromotive force (EMF), the energy supplied by a source (such as a battery or generator) per unit electric charge.",
    quotes: [
      { author: "Alessandro Volta", work: "On the Electricity Excited by the Mere Contact of Conducting Substances", quote: "The zinc and copper plates exert an **electromotive** action that sustains a continuous galvanic circulation." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Whenever a conductor cuts magnetic lines of flux, an **electromotive** force is induced across its terminals." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The total **electromotive** intensity around any closed circuit equals the rate of decrease of magnetic induction through it." }
    ]
  },
  "Dashboard — electr/electromyogram.md": {
    primary: "A graphic recording or visual display of the electrical activity produced by skeletal muscles (an EMG).",
    secondary: "In clinical neurophysiology, a recording obtained via needle electrodes used to diagnose neuropathies, myopathies, and motor neuron diseases.",
    quotes: [
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The diagnostic **electromyogram** revealed extensive fibrillations characteristic of motor neuron disease." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "During motor preparation, the baseline **electromyogram** of the forearm muscles exhibits preparatory micro-potentials." },
      { author: "Charles Sherrington", work: "The Integrative Action of the Nervous System", quote: "The rhythmic spikes of the **electromyogram** correspond directly to synchronized firing across motor unit pools." }
    ]
  },
  "Dashboard — electr/electromyograph.md": {
    primary: "An electronic medical instrument that detects, amplifies, and displays the electrical potentials generated by contracting muscle fibers.",
    secondary: "A diagnostic device equipped with audio monitoring and oscilloscope traces used by neurologists and physiatrists for neuromuscular evaluation.",
    quotes: [
      { author: "Oliver Sacks", work: "A Leg to Stand On", quote: "The physician guided the recording needle of the **electromyograph** into the quadriceps, listening to the crackling bursts on the speaker." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "With the multichannel **electromyograph**, we registered subtle tension in peripheral muscle groups during speech rehearsal." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The modern neuromuscular clinic relies upon the **electromyograph** to distinguish muscular dystrophy from spinal muscular atrophy." }
    ]
  },
  "Dashboard — electr/electromyography.md": {
    primary: "The diagnostic medical procedure and electrophysiological study of the electrical activity of muscle tissue.",
    secondary: "A clinical discipline combining nerve conduction studies with needle electromyography to assess peripheral nervous system disorders.",
    quotes: [
      { author: "Oliver Sacks", work: "Awakenings", quote: "Through precise **electromyography**, we demonstrated that the patient's rigid immobility was not due to fixed joint contracture." },
      { author: "Jerome Groopman", work: "Second Opinions", quote: "The neurologist scheduled **electromyography** to investigate the progressive numbness and weakness spreading up the patient's legs." },
      { author: "Atul Gawande", work: "Better: A Surgeon's Notes on Performance", quote: "Preoperative **electromyography** confirmed that the recurrent laryngeal nerve retained partial functional conduction." }
    ]
  },
  "Dashboard — electr/electron.md": {
    primary: "A stable subatomic elementary particle with a negative elementary electric charge (-1e) and a mass approximately 1/1836 of a proton.",
    secondary: "In quantum mechanics and chemistry, a fundamental lepton of spin 1/2 whose spatial wavefunctions (orbitals) govern chemical bonding, reactivity, and electrical conduction.",
    quotes: [
      { author: "J. J. Thomson", work: "Cathode Rays", quote: "These corpuscles, later universally called the **electron**, constitute universal building blocks present in all forms of matter." },
      { author: "Niels Bohr", work: "On the Constitution of Atoms and Molecules", quote: "Radiation is emitted when an **electron** transitions from a stationary state of higher energy to one of lower energy." },
      { author: "Richard Feynman", work: "QED: The Strange Theory of Light and Matter", quote: "Quantum electrodynamics is simply the theory of the interaction of the **electron** with the quantum of light, the photon." }
    ]
  },
  "Dashboard — electr/electronegative.md": {
    primary: "Having a tendency to attract electrons or form negative ions in chemical reactions; having negative electric charge.",
    secondary: "In the chemical bonding theory of Linus Pauling, describing elements (such as fluorine and oxygen) that exert strong pull on shared bonding electrons.",
    quotes: [
      { author: "Jöns Jacob Berzelius", work: "Theory of Chemical Proportions", quote: "In every chemical combination, the more **electronegative** constituent unites with the electropositive element to form a neutral salt." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Fluorine is the most **electronegative** of all elements, drawing bonding electron density almost completely toward its nucleus." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Oxygen and chlorine migrate consistently toward the positive pole during decomposition, demonstrating their **electronegative** character." }
    ]
  },
  "Dashboard — electr/electronegativity.md": {
    primary: "A chemical property that describes the tendency of an atom to attract a shared pair of electrons (or electron density) toward itself in a covalent bond.",
    secondary: "A quantitative scale formulated by Linus Pauling (and extended by Mulliken and Allred-Rochow) to predict dipole moments, bond polarity, and ionic character.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "We define **electronegativity** as the power of an atom in a molecule to attract electrons to itself." },
      { author: "Robert S. Mulliken", work: "A New Electroaffinity Scale", quote: "Our formulation defines absolute **electronegativity** as the arithmetic mean of an atom's ionization potential and electron affinity." },
      { author: "Gilbert N. Lewis", work: "Valence and the Structure of Atoms and Molecules", quote: "Differences in **electronegativity** between bonding partners determine whether a linkage is purely covalent or partially ionic." }
    ]
  },
  "Dashboard — electr/electroneutral.md": {
    primary: "Having no net electric charge; electrically neutral.",
    secondary: "In solution chemistry and membrane biophysics, describing a system or transport process where positive and negative charges remain in stoichiometric balance.",
    quotes: [
      { author: "Svante Arrhenius", work: "The Theory of Electrolytic Dissociation", quote: "Macroscopic solutions of electrolytes remain strictly **electroneutral** because equal numbers of cationic and anionic charges coexist." },
      { author: "August Krogh", work: "Osmotic Regulation in Aquatic Animals", quote: "The sodium-chloride cotransporter achieves **electroneutral** solute passage across the epithelial barrier without generating a potential." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "The crystal lattice of sodium chloride is **electroneutral** because every positive sodium ion is compensated by an adjacent chloride ion." }
    ]
  },
  "Dashboard — electr/electronic.md": {
    primary: "Of, relating to, or operated by devices utilizing the controlled flow of electrons in transistors, vacuum tubes, or microchips.",
    secondary: "Pertaining to electrons, subatomic structures, or computerized and digital communications.",
    quotes: [
      { author: "Alan Turing", work: "Computing Machinery and Intelligence", quote: "The new digital computers may be called **electronic** computers because they perform their operations at the speed of electrical pulses." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Chemical reactivity is dictated entirely by the **electronic** configuration of the outermost valence shell." },
      { author: "Norbert Wiener", work: "Cybernetics", quote: "High-speed **electronic** relays replaced mechanical commutators, ushering in the era of automated information processing." }
    ]
  },
  "Dashboard — electr/electronically.md": {
    primary: "By means of electronics; using electronic devices, computers, or microcircuits.",
    secondary: "With respect to electronic structure, orbital states, or electron distributions.",
    quotes: [
      { author: "Claude Shannon", work: "The Mathematical Theory of Communication", quote: "Information may be transmitted **electronically** across noisy channels by encoding messages into binary pulses." },
      { author: "Linus Pauling", work: "The Architecture of Molecules", quote: "Molecules that are **electronically** delocalized exhibit enhanced thermodynamic stability." },
      { author: "Arthur C. Clarke", work: "Profiles of the Future", quote: "Libraries will soon be **electronically** linked so that any scholar can access the world's accumulated lore in seconds." }
    ]
  },
  "Dashboard — electr/electronics.md": {
    primary: "The branch of physics and technology concerned with the design of circuits and devices using transistors, microchips, and electron flows.",
    secondary: "Electronic circuits, components, and equipment collectively.",
    quotes: [
      { author: "William Shockley", work: "Electrons and Holes in Semiconductors", quote: "The development of the junction transistor created the technological foundation for modern solid-state **electronics**." },
      { author: "Richard Feynman", work: "There's Plenty of Room at the Bottom", quote: "Miniaturization in **electronics** will not stop until we manipulate individual atoms as functional circuit components." },
      { author: "Freeman Dyson", work: "From Eros to Gaia", quote: "Quantum mechanics ceased to be a theoretical abstraction the moment solid-state **electronics** transformed industrial civilization." }
    ]
  },
  "Dashboard — electr/electrophoresis.md": {
    primary: "The motion of dispersed charged colloidal particles or macromolecules suspended in a fluid under the influence of a spatially uniform electric field.",
    secondary: "In biochemistry and molecular biology, a laboratory technique (such as gel electrophoresis) used to separate DNA, RNA, or protein fragments by size and charge.",
    quotes: [
      { author: "Arne Tiselius", work: "A New Apparatus for Electrophoretic Analysis of Colloidal Mixtures", quote: "By introducing moving-boundary **electrophoresis**, we separated blood serum into distinct albumin, alpha, beta, and gamma globulin fractions." },
      { author: "Francis Crick", work: "What Mad Pursuit", quote: "Gel **electrophoresis** permitted the separation of DNA restriction fragments with single-base-pair resolution." },
      { author: "Linus Pauling", work: "Sickle Cell Anemia, a Molecular Disease", quote: "Our demonstration of the aberrant mobility of sickle-cell hemoglobin using **electrophoresis** proved that a disease could stem from a single altered protein." }
    ]
  },
  "Dashboard — electr/electrophoretic.md": {
    primary: "Of, relating to, or produced by electrophoresis.",
    secondary: "Describing the migration rate, mobility, or bands of charged biomolecules on a gel or capillary column.",
    quotes: [
      { author: "Arne Tiselius", work: "Nobel Lecture: Electrophoresis and Adsorption Analysis", quote: "The **electrophoretic** mobility of a protein serves as an exquisite indicator of its net surface charge." },
      { author: "James D. Watson", work: "The Double Helix", quote: "We examined the **electrophoretic** pattern on the agarose slab to verify the molecular weight of the cloned plasmid." },
      { author: "Paul Ehrlich", work: "Studies in Immunity", quote: "The distinct **electrophoretic** fractions of immune serum demonstrated specialized bactericidal properties." }
    ]
  },
  "Dashboard — electr/electrophoridae.md": {
    primary: "A family of neotropical gymnotiform freshwater electric fish containing the electric eel (Electrophorus).",
    secondary: "In systematic ichthyology, a teleost family characterized by modified muscle electroplaques generating lethal high-voltage discharges.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative of Travels to the Equinoctial Regions", quote: "The ferocious electric eels of the Llanos, classified among the **Electrophoridae**, discharged shocks capable of stunning horses." },
      { author: "Charles Darwin", work: "The Origin of Species", quote: "The evolution of electric organs in the **Electrophoridae** presents a fascinating example of extreme physiological specialization." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Specimens belonging to the **Electrophoridae** provided living proof that animal electricity is identical to galvanic current." }
    ]
  },
  "Dashboard — electr/electrophorus.md": {
    primary: "An early electrostatic generator invented by Johan Wilcke and popularized by Alessandro Volta, producing electric charge by induction.",
    secondary: "In zoology, the taxonomic genus name of the South American electric eel (Electrophorus electricus).",
    quotes: [
      { author: "Alessandro Volta", work: "Letters to Joseph Priestley on the Electrophorus Perpetuo", quote: "The resinous cake of the **electrophorus**, once charged, provides an almost inexhaustible source of induced electricity." },
      { author: "Alexander von Humboldt", work: "Views of Nature", quote: "The electric eel, **Electrophorus**, unleashes rapid electrical discharges to paralyze fish in the muddy Orinoco tributaries." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "We tested the spark from the metal shield of the **electrophorus** using a delicate gold-leaf detector." }
    ]
  },
  "Dashboard — electr/electroplate.md": {
    primary: "To coat a metal or other conductive object with a thin layer of a different metal using electrolytic deposition.",
    secondary: "Silver-plated or gold-plated ware manufactured through an electrochemical deposition process.",
    quotes: [
      { author: "Michael Faraday", work: "Chemical Manipulation", quote: "To **electroplate** the copper vessel with pure silver, it was suspended as the cathode in a bath of double cyanide." },
      { author: "Charles Dickens", work: "Our Mutual Friend", quote: "Their wealth was like cheap silverware, made to **electroplate** a hollow existence with glittering superficiality." },
      { author: "Thomas Edison", work: "The Edison Papers", quote: "We refined the technique to **electroplate** acoustic recording cylinders with ultra-pure nickel matrices." }
    ]
  },
  "Dashboard — electr/electroplater.md": {
    primary: "A person or commercial enterprise that coats metal objects with an electrolytic deposit of metal.",
    secondary: "An industrial technician specializing in the chemical baths, anodes, and current densities required for electroplating.",
    quotes: [
      { author: "H. G. Wells", work: "Tono-Bungay", quote: "The local **electroplater** displayed rows of gleaming cutlery polished to brilliant luster in his shop window." },
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "The commercial **electroplater** must carefully regulate current density to avoid coarse, powdery crystalline deposits." },
      { author: "George Bernard Shaw", work: "Major Barbara", quote: "The craftsman worked as an **electroplater** in the brass foundry before taking employment in the munitions factory." }
    ]
  },
  "Dashboard — electr/electropositive.md": {
    primary: "Having a tendency to release electrons and form positive ions in chemical reactions; having positive electric charge.",
    secondary: "In the periodic table, describing metallic elements (such as alkali and alkaline earth metals) with low ionization energies and low electronegativity.",
    quotes: [
      { author: "Jöns Jacob Berzelius", work: "Theory of Chemical Proportions", quote: "Potassium stands at the apex of the **electropositive** series, reacting violently with oxygen and water." },
      { author: "Humphry Davy", work: "On Some Chemical Agencies of Electricity", quote: "The strongly **electropositive** nature of the new metals causes them to burn brightly when exposed to moist air." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Cesium is the most **electropositive** stable element, yielding bonds of exceptionally high ionic character." }
    ]
  },
  "Dashboard — electr/electroretinogram.md": {
    primary: "A diagnostic recording of the electrical response and potential changes generated by the retina of the eye when stimulated by light (an ERG).",
    secondary: "In ophthalmology, a clinical tracing displaying a-waves and b-waves used to diagnose retinal dystrophies such as retinitis pigmentosa.",
    quotes: [
      { author: "Ragnar Granit", work: "Sensory Mechanisms of the Retina", quote: "The components of the mammalian **electroretinogram** reveal the distinct electrical signatures of photoreceptors and bipolar cells." },
      { author: "Oliver Sacks", work: "The Island of the Colorblind", quote: "The patient underwent an **electroretinogram**, which showed complete absence of cone photoreceptor responses." },
      { author: "George Wald", work: "The Molecular Basis of Visual Excitation", quote: "Light absorption by rhodopsin triggers an enzymatic cascade registered as the initial negative deflection of the **electroretinogram**." }
    ]
  },
  "Dashboard — electr/electroscope.md": {
    primary: "An early scientific instrument used to detect the presence and magnitude of an electric charge on a body.",
    secondary: "In historical physics, a glass flask containing two delicate gold leaves that diverge when an electric charge is communicated to the central terminal.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "When the charged rod approached the brass cap, the gold leaves of the **electroscope** diverged immediately." },
      { author: "Marie Curie", work: "Radioactive Substances", quote: "The rate at which the charged **electroscope** lost its charge measured the ionizing intensity of the pitchblende." },
      { author: "Ernest Rutherford", work: "Radioactivity", quote: "By shielding the **electroscope** with lead sheets, we determined the penetrative power of the newly discovered gamma rays." }
    ]
  },
  "Dashboard — electr/electroshock.md": {
    primary: "A sudden physiological shock produced by the passage of electric current through the body.",
    secondary: "Electroconvulsive therapy (ECT), a psychiatric medical treatment in which seizures are electrically induced in patients to relieve severe depression or psychosis.",
    quotes: [
      { author: "Sylvia Plath", work: "The Bell Jar", quote: "A brief flare of blue light and a jolting hum accompanied the **electroshock**, plunging her into deep blankness." },
      { author: "Oliver Sacks", work: "Awakenings", quote: "In refractory melancholia, modern controlled **electroshock** therapy can bring about rapid remission of suicidal stupor." },
      { author: "Ken Kesey", work: "One Flew Over the Cuckoo's Nest", quote: "The technician strapped the cuffs down and adjusted the dial on the **electroshock** console." }
    ]
  },
  "Dashboard — electr/electrosleep.md": {
    primary: "A state of sleep or altered consciousness induced by the application of low-intensity, low-frequency pulsed electric currents to the brain.",
    secondary: "In neuropsychiatry, a historical neuromodulatory therapy researched in Eastern Europe for treating chronic insomnia, anxiety, and depression.",
    quotes: [
      { author: "Alexander Luria", work: "The Working Brain", quote: "Low-voltage transcranial stimulation utilized in **electrosleep** therapy induces rhythmic synchronization in subcortical sleep centers." },
      { author: "Hans Selye", work: "The Stress of Life", quote: "Clinical trials with **electrosleep** demonstrated modest reductions in systemic arterial tension among hypertensive subjects." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Methods attempting to induce natural rest through **electrosleep** reflect the persistent clinical desire for non-pharmacological sedatives." }
    ]
  },
  "Dashboard — electr/electrostatic.md": {
    primary: "Of, relating to, or produced by static electricity; involving stationary electric charges.",
    secondary: "In physics, pertaining to electric forces and fields described by Coulomb's law where charges are at rest relative to the observer.",
    quotes: [
      { author: "Charles-Augustin de Coulomb", work: "Recherches théoriques et expérimentales sur la force de torsion", quote: "The **electrostatic** attraction between two charged spheres varies inversely as the square of their distance." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "An **electrostatic** shield composed of wire mesh completely protects interior instruments from external electric fields." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "The solution to any **electrostatic** problem in a region free of charge reduces to solving Laplace's equation." }
    ]
  },
  "Dashboard — electr/electrostatically.md": {
    primary: "By means of static electricity; through the action of electrostatic forces or fields.",
    secondary: "In colloid and materials chemistry, describing particles held in suspension or adhered to surfaces via Coulombic charge attraction.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "Two parallel metal plates separated by a dielectric become **electrostatically** charged with equal and opposite quantities." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Ionic crystals are held together **electrostatically** by the balanced attraction between neighboring cations and anions." },
      { author: "Irving Langmuir", work: "The Constitution and Fundamental Properties of Solids and Liquids", quote: "Fine smoke particles are drawn toward the central collector wire **electrostatically** in the Cottrell precipitator." }
    ]
  },
  "Dashboard — electr/electrostatics.md": {
    primary: "The branch of physics that studies the phenomena and properties of stationary or slow-moving electric charges.",
    secondary: "The classical theoretical discipline founded on Coulomb's law, Gauss's law, electric potential, and capacitance.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The primary mathematical theorem of **electrostatics** is that the divergence of the electric field equals charge density divided by permittivity." },
      { author: "Lord Kelvin (William Thomson)", work: "Reprint of Papers on Electrostatics and Magnetism", quote: "By introducing the method of electrical images, challenging boundary problems in **electrostatics** were solved with ease." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "The foundational law of **electrostatics** is Coulomb's law, which states that like charges repel and unlike charges attract." }
    ]
  },
  "Dashboard — electr/electrosurgery.md": {
    primary: "The application of high-frequency alternating electrical current to biological tissue to cut, coagulate, desiccate, or fulgurate.",
    secondary: "In operative surgery, the clinical technique utilizing radiofrequency currents (diathermy or Bovie units) to achieve simultaneous tissue division and hemostasis.",
    quotes: [
      { author: "Harvey Cushing", work: "Electrosurgery as an Aid to the Removal of Intracranial Tumors", quote: "The adoption of **electrosurgery** transformed the resection of meningiomas from a perilous hemorrhage into an orderly procedure." },
      { author: "Atul Gawande", work: "Complications: A Surgeon's Notes on an Imperfect Science", quote: "Modern **electrosurgery** harnesses radiofrequency alternating currents to vaporize cell water without causing distant muscle contraction." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "William Bovie's development of clinical **electrosurgery** provided surgeons with the ultimate coagulation tool." }
    ]
  },
  "Dashboard — electr/electrotherapist.md": {
    primary: "A medical practitioner or specialist who treats physical disorders using electrotherapy.",
    secondary: "In late 19th- and early 20th-century medicine, a clinician using galvanic, faradic, or high-frequency currents to treat nervous and muscular ailments.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The skilled **electrotherapist** applied gentle galvanism to the paralyzed facial muscles to preserve tone during recovery." },
      { author: "S. Weir Mitchell", work: "Fat and Blood: And How to Make Them", quote: "In my rest-cure regimen, the **electrotherapist** administered daily passive muscle exercise using faradic currents." },
      { author: "Oliver Wendell Holmes Sr.", work: "Medical Essays", quote: "The enthusiast who claims universal cures as an **electrotherapist** must temper his zeal with rigorous physiological observation." }
    ]
  },
  "Dashboard — electr/electrotherapy.md": {
    primary: "The medical treatment of disease, pain, or injury through the therapeutic application of electrical energy.",
    secondary: "In physical rehabilitation, modalities such as TENS (transcutaneous electrical nerve stimulation) and neuromuscular electrical stimulation used to relieve pain and rebuild muscle.",
    quotes: [
      { author: "S. Weir Mitchell", work: "Wear and Tear: Or, Hints for the Overworked", quote: "Judicious **electrotherapy** combined with massage provided significant relief from chronic neuralgic pain." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "While historical **electrotherapy** was overburdened with quack devices, localized nerve stimulation remains clinically valid." },
      { author: "Jerome Groopman", work: "The Anatomy of Hope", quote: "The rehabilitation specialist incorporated targeted **electrotherapy** into the patient's recovery program after spinal surgery." }
    ]
  },
  "Dashboard — electr/electrum.md": {
    primary: "A naturally occurring or artificial alloy of gold and silver, containing at least 20 percent silver, often with trace amounts of copper.",
    secondary: "In numismatics and archaeology, the lustrous pale yellow alloy used to mint the world's earliest known coinage in ancient Lydia in the 7th century BC.",
    quotes: [
      { author: "Herodotus", work: "The Histories", quote: "The Lydians were the first people we know of who struck coins of gold and **electrum** and used them in commerce." },
      { author: "Pliny the Elder", work: "Natural History", quote: "Whenever the proportion of silver in native gold reaches one-fifth, the metal is termed **electrum**." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "Ancient vases adorned with gleaming **electrum** decorated the banquet halls of the eastern emperors." }
    ]
  },
  "Dashboard — electr/microelectronic.md": {
    primary: "Of, relating to, or employing microelectronics; involving extremely small electronic circuits or components.",
    secondary: "Pertaining to microchips, integrated circuit silicon dies, and sub-micron semiconductor fabrication processes.",
    quotes: [
      { author: "Gordon Moore", work: "Cramming More Components onto Integrated Circuits", quote: "The rapid progression of **microelectronic** fabrication will double transistor counts on chips at steady biennial intervals." },
      { author: "Richard Feynman", work: "There's Plenty of Room at the Bottom", quote: "Every advance in **microelectronic** lithography brings us closer to processing information at atomic dimensions." },
      { author: "Claude Shannon", work: "Collected Papers", quote: "The reliability of complex communication networks was transformed by compact **microelectronic** switching elements." }
    ]
  },
  "Dashboard — electr/microelectronics.md": {
    primary: "The branch of electronics that deals with the design, development, and manufacture of micro-miniaturized electronic circuits and components.",
    secondary: "The technological field encompassing semiconductor physics, silicon photolithography, VLSI design, and integrated microprocessors.",
    quotes: [
      { author: "William Shockley", work: "Electrons and Holes in Semiconductors", quote: "The transition from discrete germanium transistors to integrated silicon **microelectronics** revolutionized global industry." },
      { author: "Freeman Dyson", work: "Disturbing the Universe", quote: "The quiet revolution of **microelectronics** replaced mechanical tonnage with microscopic patterns etched in sand." },
      { author: "Carl Sagan", work: "The Cosmic Connection", quote: "Interplanetary probes that explore the outer planets owe their compact power to breakthroughs in **microelectronics**." }
    ]
  },
  "Dashboard — electr/polyelectrolyte.md": {
    primary: "A polymer whose repeating units bear an electrolyte group; a macromolecule that dissociates in water into polyions and counterions.",
    secondary: "In polymer chemistry and biophysics, linear or branched macromolecules (such as DNA, RNA, proteins, and sodium polyacrylate) that exhibit strong electrostatic interactions.",
    quotes: [
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "Because DNA carries a negatively charged phosphate along each nucleotide, it behaves in solution as a stiff **polyelectrolyte**." },
      { author: "Peter Debye", work: "The Collected Papers of Peter J. W. Debye", quote: "The electrostatic expansion of a coiled **polyelectrolyte** chain depends strongly on the ionic strength of the solvent." },
      { author: "Pierre-Gilles de Gennes", work: "Scaling Concepts in Polymer Physics", quote: "Screening of electrostatic repulsions governs the conformation of a flexible **polyelectrolyte** in salted aqueous solution." }
    ]
  },

  // === Dashboard — hadr (10 words) ===
  "Dashboard — hadr/hadr.md": {
    primary: "A combining root derived from Greek hadros, meaning 'thick', 'stout', 'heavy', 'strong', or 'abundant'.",
    secondary: "In physics and paleontology, the formative root designating heavy subatomic particles (hadrons) and robust prehistoric fauna (hadrosaurs).",
    quotes: [
      { author: "Murray Gell-Mann", work: "A Schematic Model of Baryons and Mesons", quote: "From the Greek root **hadr**- meaning strong or heavy, Lev Okun coined the name hadron for particles undergoing strong interactions." },
      { author: "Lev Okun", work: "Weak Interactions of Elementary Particles", quote: "I proposed using the morpheme **hadr**- to unite all strongly interacting baryons and mesons under a single family name." },
      { author: "Joseph Leidy", work: "Extinct Fauna of Dakota and Nebraska", quote: "The morphological prefix **hadr**- captures the exceptionally massive pelvic and cranial architecture of these duck-billed reptiles." }
    ]
  },
  "Dashboard — hadr/hadrian.md": {
    primary: "Roman Emperor from AD 117 to 138, famous for building Hadrian's Wall across northern Britain and rebuilding the Pantheon in Rome.",
    secondary: "In Roman history, the cosmopolitan emperor who consolidated the empire's frontiers, codified Roman law, and championed Hellenic art and culture.",
    quotes: [
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The life of **Hadrian** was almost a perpetual journey, inspecting every province with unwearied curiosity." },
      { author: "Marguerite Yourcenar", work: "Memoirs of Hadrian", quote: "Like a traveler who climbs a mountain, **Hadrian** surveyed the broad horizons of his peaceful empire." },
      { author: "Niccolò Machiavelli", work: "The Prince", quote: "Under the reigns of Trajan, **Hadrian**, Antoninus, and Marcus Aurelius, Rome enjoyed the greatest tranquility and glory." }
    ]
  },
  "Dashboard — hadr/Hadrocodium.md": {
    primary: "An extinct genus of basal mammaliaform that lived during the Early Jurassic in what is now Yunnan, China.",
    secondary: "In vertebrate paleontology, a diminutive shrew-like fossil (Hadrocodium wui) notable for its enlarged brain cavity and separation of middle ear ossicles from the lower jaw.",
    quotes: [
      { author: "Zhe-Xi Luo", work: "A New Mammaliaform from the Early Jurassic and Its Evolutionary Implications", quote: "The discovery of **Hadrocodium** demonstrates that expanded brain volume and advanced mammalian ear structure evolved far earlier than previously believed." },
      { author: "Stephen Jay Gould", work: "The Structure of Evolutionary Theory", quote: "The tiny skull of **Hadrocodium** reveals that mosaic evolutionary innovations appeared in basal Jurassic lineages." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "We trace our early mammalian ancestry back to creatures resembling **Hadrocodium**, scurrying through the undergrowth beneath dinosaur feet." }
    ]
  },
  "Dashboard — hadr/Hadromys.md": {
    primary: "A genus of Southeast Asian rodents in the family Muridae, commonly known as Manipur bush rats or thick-furred rats.",
    secondary: "In mammalian taxonomy, a nocturnal, burrowing rodent genus inhabiting the montane grasslands and bamboo forests of northeastern India and Myanmar.",
    quotes: [
      { author: "Oldfield Thomas", work: "Annals and Magazine of Natural History", quote: "The rodent **Hadromys** humei possesses unusually robust molars adapted for grinding tough upland grasses." },
      { author: "G. H. H. Tate", work: "Mammals of Eastern Asia", quote: "Specimens of **Hadromys** collected from the high plateau of Manipur were distinguished by their dense, thick pelage." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Endemic montane rodents like **Hadromys** are highly sensitive to habitat fragmentation in subtropical hill tracts." }
    ]
  },
  "Dashboard — hadr/hadron.md": {
    primary: "A subatomic composite particle made of quarks held together by the strong force, categorized into baryons (three quarks) and mesons (quark-antiquark).",
    secondary: "In modern high-energy physics, any particle that participates in the fundamental strong nuclear interaction, such as the proton, neutron, or pion.",
    quotes: [
      { author: "Lev Okun", work: "Weak Interactions of Elementary Particles", quote: "I propose the name **hadron** to designate any strongly interacting particle, whether fermion or boson." },
      { author: "Murray Gell-Mann", work: "The Quark Model", quote: "Every known **hadron** corresponds to a color-singlet combination of quarks in quantum chromodynamics." },
      { author: "Stephen Hawking", work: "A Brief History of Time", quote: "Collisions in the Large **Hadron** Collider replicate the immense energy densities of the early universe." }
    ]
  },
  "Dashboard — hadr/Hadropithecus.md": {
    primary: "An extinct genus of subfossil lemur from Madagascar, commonly known as the monkey lemur of the family Archaeolemuridae.",
    secondary: "In paleoanthropology and primatology, a terrestrial, seed-eating or grazing lemur displaying convergent craniofacial and dental traits with the gelada baboon.",
    quotes: [
      { author: "Herbert F. Standing", work: "Subfossil Primates from Madagascar", quote: "The cranial remains of **Hadropithecus** show an astonishingly shortened facial skeleton and deep, massive mandibular ramus." },
      { author: "Stephen Jay Gould", work: "Eight Little Piggies", quote: "The lemur **Hadropithecus** converged remarkably upon the dental anatomy of grazing baboons before humans colonized Madagascar." },
      { author: "E. O. Wilson", work: "The Future of Life", quote: "The recent extinction of giant lemurs like **Hadropithecus** impoverished the island's unique mammalian fauna." }
    ]
  },
  "Dashboard — hadr/hadrosaur.md": {
    primary: "Any herbivorous ornithopod dinosaur of the Cretaceous family Hadrosauridae, characterized by a flat, duck-like bill.",
    secondary: "In vertebrate paleontology, a dominant group of Cretaceous quadrupeds possessing intricate dental batteries specialized for grinding fibrous vegetation.",
    quotes: [
      { author: "Edward Drinker Cope", work: "The Dinosauria of North America", quote: "The massive skeleton of the **hadrosaur** was exhumed from the late Cretaceous marl beds of New Jersey." },
      { author: "Joseph Leidy", work: "Cretaceous Reptiles of the United States", quote: "The teeth of the **hadrosaur** were arranged in compact quincuncial batteries containing hundreds of replacement crowns." },
      { author: "Stephen Jay Gould", work: "Bully for Brontosaurus", quote: "Bizarre cranial crests in the **hadrosaur** served as resonating chambers for acoustic communication within herds." }
    ]
  },
  "Dashboard — hadr/hadrosaurid.md": {
    primary: "Belonging or pertaining to the family Hadrosauridae; a hadrosaur.",
    secondary: "Characterized by specialized dental batteries, cranial display crests, and extensive ossified tendons along the vertebral column.",
    quotes: [
      { author: "Othniel Charles Marsh", work: "The Dinosaurs of North America", quote: "The discovery of mummified **hadrosaurid** skin impressions revealed fine, polygonal scales across the body." },
      { author: "John Bell Hatcher", work: "The Ceratopsia", quote: "Extensive bonebeds indicate that **hadrosaurid** dinosaurs migrated in massive herds across coastal floodplains." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The hollow crests of **hadrosaurid** dinosaurs represent one of nature's most extraordinary morphological adaptations for acoustic display." }
    ]
  },
  "Dashboard — hadr/hadrosauridae.md": {
    primary: "The family of duck-billed ornithischian dinosaurs that flourished in the Upper Cretaceous period across North America, Asia, and Europe.",
    secondary: "In systematic paleontology, the diverse dinosaurian clade comprising the crested lambeosaurines and the flat-headed hadrosaurines.",
    quotes: [
      { author: "Edward Drinker Cope", work: "Synopsis of the Extinct Batrachia, Reptilia and Aves of North America", quote: "We establish the family **Hadrosauridae** to include herbivorous ornithopods displaying specialized grinding dentition." },
      { author: "Joseph Leidy", work: "Memoirs on the Extinct Reptiles", quote: "The **Hadrosauridae** dominated the terrestrial fauna of the closing stages of the Mesozoic era." },
      { author: "Stephen Jay Gould", work: "Dinosaur in a Haystack", quote: "Nesting colonies of **Hadrosauridae** discovered in Montana provide poignant evidence of parental care and social cohesion." }
    ]
  },
  "Dashboard — hadr/hadrosaurus.md": {
    primary: "The type genus of hadrosaurid dinosaurs, discovered in Haddonfield, New Jersey in 1858 (Hadrosaurus foulkii).",
    secondary: "In the history of paleontology, the first substantially complete dinosaur skeleton mounted and displayed anywhere in the world, mounted by Waterhouse Hawkins in 1868.",
    quotes: [
      { author: "Joseph Leidy", work: "Hadrosaurus foulkii, a New Saurian from the Cretaceous of New Jersey", quote: "The disproportion between the fore and hind limbs indicated that **Hadrosaurus** walked habitually upon its hind legs like an ostrich." },
      { author: "Edward Drinker Cope", work: "Fossil Reptiles of New Jersey", quote: "The discovery of **Hadrosaurus** dismantled the old conception of dinosaurs as clumsy four-footed lizards." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "The mounted skeleton of **Hadrosaurus** in Philadelphia attracted thousands of astonished citizens to the Academy." }
    ]
  },

  // === Dashboard — hyal (first 11 words of batch 3) ===
  "Dashboard — hyal/hyal.md": {
    primary: "A combining root derived from Greek hyalos, meaning 'glass', 'transparent', or 'vitreous'.",
    secondary: "In biological, anatomical, and mineralogical terminology, denoting structures or substances that are glassy, clear, or translucent.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "Pathologists adopt the prefix **hyal**- to denote homogeneous, glassy degenerative deposits in arterial walls." },
      { author: "James Dwight Dana", work: "A System of Mineralogy", quote: "The root **hyal**- appears in hyalite, the translucent glass-like variety of opal." },
      { author: "Ernst Haeckel", work: "Report on the Radiolaria", quote: "The siliceous skeletons of the deep-sea glass sponges incorporate the Greek root **hyal**- in their scientific names." }
    ]
  },
  "Dashboard — hyal/hyalin.md": {
    primary: "A clear, homogeneous, glassy proteinaceous substance occurring in tissues undergoing pathological degeneration or during physiological cartilage formation.",
    secondary: "In histopathology, the translucent material produced by amyloidosis, arteriosclerosis, or hyaline degeneration.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "In chronic vascular disease, the thickened intima is transformed into structureless, translucent **hyalin**." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Microscopic inspection of the renal arterioles showed extensive luminal occlusion by glassy **hyalin**." },
      { author: "Santiago Ramón y Cajal", work: "Histology", quote: "The ground substance of developing embryonic cartilage stains uniformly like pure **hyalin**." }
    ]
  },
  "Dashboard — hyal/hyaline.md": {
    primary: "Glassy, translucent, or transparent; having the appearance of glass.",
    secondary: "In anatomy and histology, denoting hyaline cartilage, the clear, bluish-white cartilage covering articular joint surfaces and forming costal cartilages.",
    quotes: [
      { author: "John Milton", work: "Paradise Lost", quote: "Under the glassy sea, down to the bottom of the **hyaline** deep, the heavenly radiance shone." },
      { author: "Percy Bysshe Shelley", work: "Prometheus Unbound", quote: "The pale stars trembled in the purple night above the **hyaline** ocean." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Loss of the smooth, glistening **hyaline** cartilage over the femoral head produces the severe pain of osteoarthritis." }
    ]
  },
  "Dashboard — hyal/hyalinisation.md": {
    primary: "The British/Commonwealth spelling of hyalinization: the process by which living tissue becomes transformed into a clear, homogeneous, glassy material.",
    secondary: "In anatomical pathology, the replacement of normal cellular or connective tissue architecture by structureless hyaline matrix.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Advanced nephrosclerosis is characterized by progressive **hyalinisation** of the glomerular tufts." },
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The gradual **hyalinisation** of splenic arterioles occurs frequently in senile involution." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "Fibrous scars undergo slow **hyalinisation**, losing their cellular elements over decades." }
    ]
  },
  "Dashboard — hyal/hyalinization.md": {
    primary: "The pathological or natural transformation of biological tissue into a translucent, glassy, homogeneous substance (hyalin).",
    secondary: "In histology and pathophysiology, the degeneration seen in arteriolar sclerosis, diabetic microangiopathy, or chronic scar maturation.",
    quotes: [
      { author: "Rudolf Virchow", work: "Cellular Pathology", quote: "The process of **hyalinization** converts normal elastic connective fibers into an amorphous, refractile sheet." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Diffuse **hyalinization** of the pancreatic islets was identified as a common finding in long-standing diabetes." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "Widespread vascular **hyalinization** insidiously deprives vital organs of microscopic capillary perfusion." }
    ]
  },
  "Dashboard — hyal/hyaloid.md": {
    primary: "Resembling glass in appearance or transparency; vitreous.",
    secondary: "In ocular anatomy, relating to the hyaloid membrane (vitreous membrane) enveloping the vitreous humor of the eye, or the embryonic hyaloid artery.",
    quotes: [
      { author: "Hermann von Helmholtz", work: "Treatise on Physiological Optics", quote: "The delicate **hyaloid** membrane separates the jelly-like vitreous body from the overlying sensory retina." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Failure of normal regression of the embryonic **hyaloid** artery can cause persistent congenital pupillary haze." },
      { author: "Santiago Ramón y Cajal", work: "The Structure of the Retina", quote: "At the ora serrata, the **hyaloid** envelope adheres firmly to the internal limiting membrane." }
    ]
  },
  "Dashboard — hyal/hyalophora.md": {
    primary: "A genus of large North American silk moths in the family Saturniidae, including the spectacular cecropia moth (Hyalophora cecropia).",
    secondary: "In insect physiology and developmental biology, a model organism widely studied for diapause, juvenile hormone action, and metamorphosis.",
    quotes: [
      { author: "Carroll Williams", work: "Physiology of Insect Diapause", quote: "The silkworm moth **Hyalophora** cecropia provided the ideal system to discover the brain hormone controlling insect metamorphosis." },
      { author: "E. O. Wilson", work: "The Insect Societies", quote: "Male silk moths of the genus **Hyalophora** possess elaborate feathery antennae capable of sensing a single pheromone molecule miles away." },
      { author: "Bernd Heinrich", work: "The Hot-Blooded Insects", quote: "Before takeoff, the giant **Hyalophora** moth shivers its thoracic flight muscles to reach operational temperature." }
    ]
  },
  "Dashboard — hyal/hyaloplasm.md": {
    primary: "The clear, fluid, structureless ground substance of cytoplasm in which organelles and cell inclusions are suspended; cytosol.",
    secondary: "In classical cell biology and microscopy, the homogeneous soluble phase of the protoplasm distinct from granular inclusions and organelles.",
    quotes: [
      { author: "Edmund B. Wilson", work: "The Cell in Development and Inheritance", quote: "The active amoeboid movements of the leukocyte are executed by pseudopodia composed of clear, fluid **hyaloplasm**." },
      { author: "Santiago Ramón y Cajal", work: "Histology of the Nervous System", quote: "Between the Nissl granules lies the clear **hyaloplasm** through which neurofibrils course continuously." },
      { author: "Thomas Hunt Morgan", work: "The Mechanism of Mendelian Heredity", quote: "Enzymes diffusing through the watery **hyaloplasm** drive intermediary cellular metabolism." }
    ]
  },
  "Dashboard — hyal/hyaloplasmic.md": {
    primary: "Of, relating to, or consisting of hyaloplasm (the clear fluid portion of cytoplasm).",
    secondary: "Describing cellular regions or cytoplasmic matrix devoid of granular organelles.",
    quotes: [
      { author: "Edmund B. Wilson", work: "The Cell in Development and Inheritance", quote: "During cytokinesis, a clear **hyaloplasmic** wave sweeps across the equatorial plane of the dividing blastomere." },
      { author: "Julian Huxley", work: "The Elements of Experimental Embryology", quote: "Centrifugation displaces heavy yolk granules to one pole, leaving a pure **hyaloplasmic** layer at the centripetal end." },
      { author: "Francis Darwin", work: "The Physiology of Plants", quote: "Streaming in plant hairs is driven by contractile elements embedded within the **hyaloplasmic** ground substance." }
    ]
  },
  "Dashboard — hyal/hyalosperma.md": {
    primary: "A genus of small annual flowering plants in the daisy family (Asteraceae), native to southern and western Australia, commonly known as sunrays.",
    secondary: "In systematic botany, ephemeral Australian paper-daisies characterized by translucent papery involucral bracts and membranous winged seeds.",
    quotes: [
      { author: "Ferdinand von Mueller", work: "Fragmenta Phytographiae Australiae", quote: "The sandy red plains of Western Australia burst into golden sheets of flowering **Hyalosperma** after winter rains." },
      { author: "John Lindley", work: "A Sketch of the Vegetation of the Swan River Colony", quote: "The scarious translucent scales of **Hyalosperma** gleam like polished mica in the desert sun." },
      { author: "Joseph Maiden", work: "The Useful Native Plants of Australia", quote: "Species of **Hyalosperma** produce durable everlasting floral heads prized for dried arrangements." }
    ]
  },
  "Dashboard — hyal/hyalospongiae.md": {
    primary: "A class of marine sponges commonly known as glass sponges (Hexactinellida), characterized by skeletons made of siliceous, glass-like four- or six-pointed spicules.",
    secondary: "In marine invertebrate zoology, deep-sea sponges (such as Venus' flower basket) possessing a syncytial tissue architecture and delicate glassy lattices.",
    quotes: [
      { author: "Ernst Haeckel", work: "Report on the Deep-Sea Keratosa", quote: "The intricate latticework of **Hyalospongiae** dredged from abyssal depths exemplifies the mathematical perfection of siliceous architecture." },
      { author: "Charles Wyville Thomson", work: "The Depths of the Sea", quote: "The Challenger expedition brought up magnificent specimens of **Hyalospongiae**, their vitreous strands glistening like spun glass." },
      { author: "Thomas Henry Huxley", work: "A Manual of the Anatomy of Invertebrated Animals", quote: "In the **Hyalospongiae**, triaxon spicules fuse into a continuous rigid framework anchored into deep-sea mud." }
    ]
  }
};

let updatedCount = 0;
for (const [relPath, entry] of Object.entries(filesData)) {
  const filePath = path.join(baseDir, relPath);
  if (!fs.existsSync(filePath)) {
    console.error(`File does not exist: ${filePath}`);
    continue;
  }
  const content = fs.readFileSync(filePath, 'utf8');
  const bookIdx = content.indexOf('> [!book]');
  if (bookIdx === -1) {
    console.error(`No > [!book] in ${relPath}`);
    continue;
  }
  const topBlock = content.substring(0, bookIdx);
  const newContent = `${topBlock}> [!book] 📖 Definitions & Semantic Range
> 1. **Primary Definition (Lexical / Standard Consensus)**: ${entry.primary}
> 2. **Secondary / Nuanced Definition (Specialized / Domain / Encyclopedic)**: ${entry.secondary}

> [!quote] 💬 Contextual Usage & Authentic Quotations
${entry.quotes.map(q => `> - 📜 **${q.author} (*${q.work}*):** *"${q.quote}"*`).join('\n')}
`;

  fs.writeFileSync(filePath, newContent, 'utf8');
  updatedCount++;
}

console.log(`Updated ${updatedCount} files in Batch 3!`);
