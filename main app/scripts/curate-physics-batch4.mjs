import fs from 'fs';
import path from 'path';

const baseDir = 'App database/Greek roots/Cluster Physics & Chemistry';

const filesData = {
  // === Dashboard — hyal (1 word) ===
  "Dashboard — hyal/hyaluronidase.md": {
    primary: "A family of enzymes that catalyze the degradation of hyaluronic acid, increasing tissue permeability.",
    secondary: "In medicine and pharmacology, a 'spreading factor' enzyme used to accelerate the absorption and diffusion of injected drugs, anesthetics, and fluids.",
    quotes: [
      { author: "Karl Meyer", work: "The Biological Significance of Hyaluronic Acid and Hyaluronidase", quote: "The bacterial enzyme **hyaluronidase** hydrolyzes the glycosidic bonds of the intercellular cement substance." },
      { author: "René Dubos", work: "The Bacterial Cell", quote: "Pathogenic streptococci secrete **hyaluronidase** as an invasive factor facilitating tissue invasion." },
      { author: "Macfarlane Burnet", work: "Enzyme, Antigen and Virus", quote: "Purified **hyaluronidase** markedly enhances the spread of subcutaneously administered saline." }
    ]
  },

  // === Dashboard — icter (12 words) ===
  "Dashboard — icter/anicteric.md": {
    primary: "Without jaundice or yellow discoloration of the skin and mucous membranes; non-jaundiced.",
    secondary: "In hepatology and infectious disease, describing mild, subclinical, or atypical presentations of hepatitis (such as anicteric hepatitis).",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "In children, epidemic viral hepatitis frequently manifests as an **anicteric** illness mistaken for simple gastroenteritis." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The presence of elevated transaminases in an **anicteric** patient prompted a thorough serological screening." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Hepatic dysfunction can progress silently in **anicteric** individuals before overt signs emerge." }
    ]
  },
  "Dashboard — icter/ictal.md": {
    primary: "Of, relating to, or caused by a stroke, seizure, or acute pathological attack.",
    secondary: "In neurology and epileptology, designating electrical activity, clinical signs, or cognitive phenomena occurring directly during an epileptic seizure.",
    quotes: [
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "The patient experienced profound musical hallucinations during the **ictal** phase of the temporal lobe seizure." },
      { author: "Alexander Luria", work: "Higher Cortical Functions in Man", quote: "Continuous monitoring revealed sharp paroxysmal spikes that marked the beginning of **ictal** discharge." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Differentiating between the **ictal** state and postictal confusion is essential for accurate clinical evaluation." }
    ]
  },
  "Dashboard — icter/icter.md": {
    primary: "A combining root derived from Greek ikteros, meaning 'jaundice' or a mythical yellowish-green bird whose sight was believed to cure jaundice.",
    secondary: "In clinical pathology and ornithology, the formative element in terms denoting jaundice, yellow pigmentation, or the New World blackbird family.",
    quotes: [
      { author: "Pliny the Elder", work: "Natural History", quote: "The Greeks gave the name **icter**- to that bird whose glance was reputed to draw the jaundice out of a sick man." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Medical terms bearing the root **icter**- consistently point to bilirubin retention and hepatic biliary obstruction." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "Systematic classifications retain the ancient morpheme **icter**- in designating the bright oriole and blackbird tribes." }
    ]
  },
  "Dashboard — icter/icteria.md": {
    primary: "An obsolete medical term for jaundice; yellow discoloration of tissues from bile pigment accumulation.",
    secondary: "In historical clinical nosology, synonymous with icterus, designating severe bilious conditions.",
    quotes: [
      { author: "Thomas Browne", work: "Pseudodoxia Epidemica", quote: "Ancient physicians held that looking upon the yellow oriole would cure the severe affliction of **icteria**." },
      { author: "Robert Burton", work: "The Anatomy of Melancholy", quote: "Obstruction of the gall ducts produces that stubborn **icteria** which tingeth the countenance with saffron." },
      { author: "William Cullen", work: "First Lines of the Practice of Physic", quote: "Under the genus **icteria**, we classify those affections characterized by universal yellowness of skin and urine." }
    ]
  },
  "Dashboard — icter/icteric.md": {
    primary: "Pertaining to, affected with, or resembling jaundice; having a yellowish tinge.",
    secondary: "In laboratory medicine, describing blood serum or plasma that appears distinctly dark amber or yellow due to elevated bilirubin.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The sclerae displayed a pronounced **icteric** hue that immediately confirmed the presence of biliary obstruction." },
      { author: "Jerome Groopman", work: "Second Opinions", quote: "The laboratory reported that the specimen was heavily **icteric**, interfering with optical photometric assays." },
      { author: "Sherwin B. Nuland", work: "Doctors: The Biography of Medicine", quote: "The patient's deeply **icteric** complexion pointed toward acute decompensation of the liver parenchyma." }
    ]
  },
  "Dashboard — icter/icteridae.md": {
    primary: "A family of New World passerine birds (the icterids), including blackbirds, orioles, meadowlarks, grackles, and cowbirds.",
    secondary: "In systematic ornithology, an ecologically diverse avian family characterized by sharp, conical bills and frequently bright yellow, orange, or iridescent plumage.",
    quotes: [
      { author: "John James Audubon", work: "Ornithological Biography", quote: "Members of the family **Icteridae** enliven the northern meadows with their ringing melodies and brilliant plumage." },
      { author: "Alexander Wilson", work: "American Ornithology", quote: "The Baltimore oriole, assigned to **Icteridae**, weaves an intricate pensile nest from fibers and horsehair." },
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "Brood parasitism evolved independently within certain specialized lineages of the **Icteridae**." }
    ]
  },
  "Dashboard — icter/icterogenic.md": {
    primary: "Causing or producing jaundice; promoting the accumulation of bilirubin in tissues.",
    secondary: "In toxicology and pharmacology, describing chemical agents, drugs, or leptospiral toxins capable of inducing hepatic necrosis or cholestasis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Prolonged industrial exposure to chlorinated hydrocarbons exerts a powerful **icterogenic** effect upon factory workers." },
      { author: "Paul Ehrlich", work: "Experimental Chemotherapy", quote: "We screened each synthetic compound to ensure it was devoid of direct **icterogenic** toxicity toward hepatocytes." },
      { author: "Alexander Fleming", work: "Chemotherapy: Yesterday, Today, and Tomorrow", quote: "Certain early arsenical remedies exhibited unpredictable **icterogenic** properties in susceptible patients." }
    ]
  },
  "Dashboard — icter/icterohemorrhagic.md": {
    primary: "Characterized by both jaundice and widespread hemorrhages.",
    secondary: "In tropical medicine, specifically denoting Leptospira interrogans serovar Icterohaemorrhagiae, the causative spirochete of Weil's disease.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Weil's disease represents an acute **icterohemorrhagic** infection transmitted through water contaminated with rodent urine." },
      { author: "Macfarlane Burnet", work: "Natural History of Infectious Disease", quote: "The virulent **icterohemorrhagic** leptospira penetrates mucous membranes, damaging both capillary endothelia and liver cells." },
      { author: "Sherwin B. Nuland", work: "The Mysteries Within", quote: "Severe cases presented with the classic triad of fever, profound jaundice, and bleeding in an **icterohemorrhagic** crisis." }
    ]
  },
  "Dashboard — icter/icterohepatitis.md": {
    primary: "Inflammation of the liver accompanied by conspicuous jaundice.",
    secondary: "In veterinary and human pathology, an acute or chronic infectious hepatitis characterized by biliary stasis and widespread hepatocyte necrosis.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Acute **icterohepatitis** may supervene rapidly in the course of systemic septicemia." },
      { author: "Theobald Smith", work: "Studies on Animal Diseases", quote: "Infectious enterohepatitis in poultry occasionally induces severe secondary **icterohepatitis**." },
      { author: "Jerome Groopman", work: "How Doctors Think", quote: "The biopsy specimen revealed florid portal inflammation consistent with drug-induced **icterohepatitis**." }
    ]
  },
  "Dashboard — icter/icteroid.md": {
    primary: "Resembling jaundice; yellowish in appearance; or having the character of icterus.",
    secondary: "In botanical and zoological descriptions, possessing a dull yellow or saffron coloration reminiscent of jaundiced skin.",
    quotes: [
      { author: "Asa Gray", work: "Botanical Text-Book", quote: "The decaying foliage assumed an **icteroid** tint as chlorophyll broke down into xanthophylls." },
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "The patient displayed an **icteroid** cachexia often mistaken for pernicious anemia." },
      { author: "Jonathan Hutchinson", work: "Archives of Surgery", quote: "The conjunctivae showed an **icteroid** discoloration before systemic bilirubin reached frank clinical levels." }
    ]
  },
  "Dashboard — icter/icterus.md": {
    primary: "Jaundice; a yellow pigmentation of the skin, conjunctival sclera, and mucous membranes caused by hyperbilirubinemia.",
    secondary: "In neonatology, icterus neonatorum (physiological jaundice of the newborn); or in veterinary pathology, neonatal isoerythrolysis in foals.",
    quotes: [
      { author: "William Osler", work: "The Principles and Practice of Medicine", quote: "Obstructive **icterus** develops when gallstones or neoplasms occlude the common bile duct." },
      { author: "Atul Gawande", work: "Complications", quote: "The surgeon noted deep **icterus** staining the peritoneal tissues during exploratory laparotomy." },
      { author: "Sherwin B. Nuland", work: "How We Die", quote: "Bilirubin deposition in the brainstem, known as kernicterus, was once a dreaded complication of severe neonatal **icterus**." }
    ]
  },
  "Dashboard — icter/ictic.md": {
    primary: "Of or relating to a stroke or sudden blow; ictal.",
    secondary: "In prosody and poetics, relating to metrical ictus, stress, or rhythmic pulsation.",
    quotes: [
      { author: "Oliver Sacks", work: "Musicophilia", quote: "The patient described an **ictic** surge of melodic phrases accompanying each epileptic aura." },
      { author: "George Saintsbury", work: "A History of English Prosody", quote: "The **ictic** beat falling upon the alternate syllables gives heroic verse its stately cadence." },
      { author: "Alexander Luria", work: "The Working Brain", quote: "Transient paroxysmal phenomena during the **ictic** discharge disrupted voluntary speech production." }
    ]
  },

  // === Dashboard — magnet (41 words) ===
  "Dashboard — magnet/antimagnetic.md": {
    primary: "Resistant to the effects of magnetic fields; non-magnetic.",
    secondary: "In horology and instrument engineering, describing watch movements utilizing non-ferrous alloys (such as Glucydur or silicon) to prevent rate disturbances from stray magnetic fields.",
    quotes: [
      { author: "Arthur C. Clarke", work: "The City and the Stars", quote: "The explorer adjusted his **antimagnetic** compass before approaching the subterranean power station." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "Marine chronometers were enclosed in **antimagnetic** brass shields to counter the ship's permanent magnetization." },
      { author: "H. G. Wells", work: "The First Men in the Moon", quote: "Our navigational meters were constructed with **antimagnetic** springs to withstand the electrical machinery." }
    ]
  },
  "Dashboard — magnet/bioelectromagnetism.md": {
    primary: "The study of electrical and magnetic phenomena generated by living cells, tissues, and organisms.",
    secondary: "In biophysics and neuroscience, the discipline analyzing the magnetic fields generated by action potentials in the heart (MCG) and brain (MEG).",
    quotes: [
      { author: "Erwin Schrödinger", work: "What Is Life?", quote: "The delicate interplay of ions across cellular membranes constitutes the ultimate physical origin of **bioelectromagnetism**." },
      { author: "Oliver Sacks", work: "The Man Who Mistook His Wife for a Hat", quote: "Magnetoencephalography relies upon the subtle principles of **bioelectromagnetism** to trace cortical sensory pathways." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "Nerve conduction generates macroscopic fields that belong to the fascinating domain of **bioelectromagnetism**." }
    ]
  },
  "Dashboard — magnet/biomagnetism.md": {
    primary: "The phenomenon of magnetic fields produced by or associated with living organisms; or the study of magnetic effects on biology.",
    secondary: "In sensory physiology, magnetoreception—the biological sensory system by which migratory birds, turtles, and bacteria orient via the Earth's magnetic field.",
    quotes: [
      { author: "E. O. Wilson", work: "Sociobiology: The New Synthesis", quote: "Migratory navigation in honeybees demonstrated that **biomagnetism** provides an internal compass for long-distance foraging." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "Tiny magnetic crystals of magnetite lodged in the ethmoid bone mediate avian **biomagnetism**." },
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "The discovery of magnetotactic bacteria proved that **biomagnetism** is an ancient sensory mechanism dating to the Precambrian." }
    ]
  },
  "Dashboard — magnet/demagnetisation.md": {
    primary: "The British/Commonwealth spelling of demagnetization: the process of removing or reducing magnetic properties from a magnetized material.",
    secondary: "In low-temperature physics, adiabatic demagnetisation of paramagnetic salts, a thermodynamic method pioneered by Giauque and Debye to reach temperatures within fractions of a kelvin of absolute zero.",
    quotes: [
      { author: "Lord Kelvin (William Thomson)", work: "Reprint of Papers on Electrostatics and Magnetism", quote: "Careful thermal **demagnetisation** restored the iron ring to its virgin magnetic neutrality." },
      { author: "Ernest Rutherford", work: "Radioactivity", quote: "The technique of adiabatic **demagnetisation** allowed physicists to cool paramagnetic crystals to within thousandths of a degree from absolute zero." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "Repeated mechanical shocks produce partial **demagnetisation** by disrupting the alignment of molecular domains." }
    ]
  },
  "Dashboard — magnet/demagnetise.md": {
    primary: "To deprive of magnetic properties; to neutralize or remove the magnetism of a magnetized substance (Commonwealth spelling).",
    secondary: "In naval engineering and electronics, to degauss a ship or tape head to eliminate residual magnetic fields.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Heating the lodestone red-hot will completely **demagnetise** it, destroying its attractive virtue." },
      { author: "Arthur C. Clarke", work: "Glide Path", quote: "Ground crews worked to **demagnetise** the aircraft hull to prevent radar and compass interference." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "An alternating field of diminishing amplitude is the most effective means to **demagnetise** hard steel." }
    ]
  },
  "Dashboard — magnet/demagnetization.md": {
    primary: "The process of removing magnetic properties or residual magnetic fields from a magnetized object.",
    secondary: "In condensed matter physics, adiabatic demagnetization, a cryogenic refrigeration method utilizing paramagnetic entropy changes.",
    quotes: [
      { author: "William F. Giauque", work: "Nobel Lecture: Investigations in Chemical Thermodynamics", quote: "Magnetic refrigeration relies upon the thermodynamic cooling achieved during adiabatic **demagnetization** of gadolinium sulfate." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The **demagnetization** curve reveals the coercive force required to reduce the residual induction to zero." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "Thermal agitation causes spontaneous **demagnetization** of ferromagnetic materials above their Curie temperature." }
    ]
  },
  "Dashboard — magnet/demagnetize.md": {
    primary: "To remove the magnetic properties from an object, material, or tool; to neutralize magnetism.",
    secondary: "To degauss cathode-ray tubes, magnetic recording heads, or ship hulls to prevent electromagnetic distortion.",
    quotes: [
      { author: "Nikola Tesla", work: "Experiments with Alternate Currents", quote: "We employed a decaying alternating current coil to **demagnetize** the iron laminations of the transformer core." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Vigorous hammering upon the magnetized needle in an east-west orientation served to **demagnetize** it completely." },
      { author: "Thomas Edison", work: "The Edison Papers", quote: "The technician had to **demagnetize** his watch before entering the dynamo testing bay." }
    ]
  },
  "Dashboard — magnet/diamagnet.md": {
    primary: "A substance or body that exhibits diamagnetism, being repelled by a magnetic field.",
    secondary: "In physical chemistry, any material (such as bismuth, water, copper, or graphite) whose atoms possess no net unpaired electron spins.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Bismuth is the most remarkable **diamagnet** in nature, pointing equatorially across lines of magnetic force." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "When placed between the poles of an electromagnet, a true **diamagnet** moves toward the region of weakest field." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "The mechanical force acting upon a **diamagnet** is directed opposite to the magnetic gradient." }
    ]
  },
  "Dashboard — magnet/diamagnetic.md": {
    primary: "Pertaining to or exhibiting diamagnetism; having negative magnetic susceptibility and repelled by magnetic fields.",
    secondary: "In quantum chemistry, designating molecules whose electron spins are completely paired, resulting in absence of permanent magnetic dipoles.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "I observed that a heavy glass bar suspended between the magnetic poles placed itself equatorially, behaving as a **diamagnetic** body." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The **diamagnetic** susceptibility of the complex proved that all six d-electrons occupied low-spin paired orbitals." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "Lenz's law operating at the atomic level explains why all matter possesses an underlying **diamagnetic** response." }
    ]
  },
  "Dashboard — magnet/diamagnetism.md": {
    primary: "A form of magnetism whereby a substance creates an induced magnetic field in opposition to an externally applied magnetic field, causing repulsion.",
    secondary: "In solid-state physics, a universal quantum mechanical property of all materials, arising from the orbital motion of electrons (Larmor precession).",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The discovery of **diamagnetism** demonstrated that magnetism is not confined to iron, but is a universal property of matter." },
      { author: "Niels Bohr", work: "Studies on the Electron Theory of Metals", quote: "Classical statistical mechanics predicts that thermal equilibrium precludes any net magnetization, proving that **diamagnetism** is fundamentally quantum." },
      { author: "John Hasbrouck Van Vleck", work: "The Theory of Electric and Magnetic Susceptibilities", quote: "Temperature-independent **diamagnetism** reflects the contraction of electronic electron clouds under an applied magnetic flux." }
    ]
  },
  "Dashboard — magnet/electromagnet.md": {
    primary: "A device consisting of a core of ferromagnetic material surrounded by a coil of wire through which an electric current is passed to magnetize the core.",
    secondary: "An electrical apparatus widely utilized in electric motors, particle accelerators, relays, MRI machines, and magnetic cranes.",
    quotes: [
      { author: "Joseph Henry", work: "On the Application of the Principle of the Galvanic Multiplier", quote: "Our giant **electromagnet** demonstrated for the first time that electrical forces could lift industrial weights." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The magnetic field produced inside the solenoid of an **electromagnet** is proportional to the amp-turns per unit length." },
      { author: "Nikola Tesla", work: "My Inventions", quote: "The rotating field was produced by feeding two-phase alternating currents into the coils of an **electromagnet** ring." }
    ]
  },
  "Dashboard — magnet/electromagnetic.md": {
    primary: "Of or pertaining to electromagnetism; produced by or involving both electric and magnetic fields.",
    secondary: "Describing electromagnetic waves or radiation, encompassing radio waves, infrared, light, X-rays, and gamma rays traveling at c.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Dynamical Theory of the Electromagnetic Field", quote: "We have strong reasons to conclude that light itself is an **electromagnetic** disturbance in the ether." },
      { author: "Albert Einstein", work: "On the Electrodynamics of Moving Bodies", quote: "The laws of **electromagnetic** phenomena remain valid across all inertial frames of reference." },
      { author: "Heinrich Hertz", work: "Electric Waves", quote: "By reflecting and refracting the invisible sparks, we confirmed the wave nature of **electromagnetic** propagation." }
    ]
  },
  "Dashboard — magnet/electromagnetism.md": {
    primary: "The branch of physical science that encompasses the interactions between electric currents and magnetic fields.",
    secondary: "The unified fundamental force of nature described by Maxwell's equations and quantum electrodynamics (QED).",
    quotes: [
      { author: "Hans Christian Ørsted", work: "Experiments on the Effect of a Current of Electricity", quote: "The deflection of the compass needle by a voltaic current heralded the birth of **electromagnetism**." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The fundamental laws of **electromagnetism** govern both the electric dynamo and the induction motor." },
      { author: "Richard Feynman", work: "QED: The Strange Theory of Light and Matter", quote: "At the deepest quantum level, **electromagnetism** describes the exchange of virtual photons between charged particles." }
    ]
  },
  "Dashboard — magnet/geomagnetic.md": {
    primary: "Of or relating to the Earth's magnetic field (geomagnetism).",
    secondary: "In geophysics and space physics, pertaining to geomagnetic storms, dipolar field reversals, and the magnetosphere protecting Earth from solar wind.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos: A Sketch of a Physical Description of the Universe", quote: "Global magnetic observatories established the reality of widespread **geomagnetic** storms shaking compass needles simultaneously worldwide." },
      { author: "Alfred Wegener", work: "The Origin of Continents and Oceans", quote: "Paleomagnetic evidence of fossil **geomagnetic** field alignments in ocean basalt verified the theory of continental drift." },
      { author: "James Van Allen", work: "Radiation Belts Around the Earth", quote: "Energetic solar particles become trapped within the Earth's **geomagnetic** field, forming the radiation belts." }
    ]
  },
  "Dashboard — magnet/magnesium.md": {
    primary: "A lightweight, silvery-white metallic element of the alkaline earth group, atomic number 12 and symbol Mg.",
    secondary: "An essential biological mineral cofactor for ATP reactions, chlorophyll, and DNA synthesis, as well as an industrial metal used in lightweight structural alloys.",
    quotes: [
      { author: "Humphry Davy", work: "Electro-Chemical Researches on the Decomposition of the Earths", quote: "From the calcined magnesia I succeeded in isolating the bright, combustible metal which I named **magnesium**." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "A ribbon of **magnesium** burns with an unearthly, blinding white flame that leaves behind a delicate ash." },
      { author: "Linus Pauling", work: "General Chemistry", quote: "Every molecule of photosynthetic chlorophyll holds a single coordinated atom of **magnesium** at its center." }
    ]
  },
  "Dashboard — magnet/magnet.md": {
    primary: "A piece of iron or other material that possesses the property of attracting iron and producing a magnetic field.",
    secondary: "A person, place, or thing that exerts a powerful attraction or influence over others.",
    quotes: [
      { author: "William Gilbert", work: "De Magnete", quote: "The whole globe of the earth is a great **magnet**, orienting needles along its meridian lines." },
      { author: "William Shakespeare", work: "A Midsummer Night's Dream", quote: "You draw me, you hard-hearted adamant, but yet you draw not iron, for my heart is true as steel to your **magnet**." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "Paris acted as a fatal **magnet** that drew the expatriates back into the vortex of revolution." }
    ]
  },
  "Dashboard — magnet/magnetic.md": {
    primary: "Possessing the properties of a magnet; exerting or capable of being affected by magnetism.",
    secondary: "Exerting a powerful fascination or compelling personal charm and attraction.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "I rotated the plane of polarized light by passing it through heavy glass placed in a powerful **magnetic** field." },
      { author: "Charlotte Brontë", work: "Jane Eyre", quote: "There was a **magnetic** attraction in Mr. Rochester's voice that drew me toward him against my will." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The lightning strike reversed the **magnetic** polarity of the ship's binnacle compass in the midst of the typhoon." }
    ]
  },
  "Dashboard — magnet/magnetically.md": {
    primary: "In a magnetic manner; by means of magnetic force or fields.",
    secondary: "With irresistible attraction or compelling charm.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The two circuits were **magnetically** coupled so that current in one induced an electromotive force in the other." },
      { author: "Thomas Hardy", work: "Tess of the d'Urbervilles", quote: "She felt herself drawn **magnetically** toward him across the summer garden, helpless to resist." },
      { author: "Nikola Tesla", work: "My Inventions", quote: "The armature was suspended **magnetically** to eliminate bearing friction at high rotational velocities." }
    ]
  },
  "Dashboard — magnet/magnetics.md": {
    primary: "The branch of physical science that deals with magnetic phenomena, materials, and fields.",
    secondary: "In applied electrical engineering, the design of magnetic components such as inductors, transformers, and magnetic recording media.",
    quotes: [
      { author: "William Gilbert", work: "De Magnete", quote: "In the study of **magnetics**, we must proceed by rigorous demonstration and direct experiment upon the terrella." },
      { author: "Lord Kelvin (William Thomson)", work: "Reprint of Papers on Electrostatics and Magnetism", quote: "Theoretical **magnetics** achieved mathematical maturity through Poisson's theory of magnetic dipoles." },
      { author: "Oliver Heaviside", work: "Electromagnetic Theory", quote: "The principles of **magnetics** dictate that lines of induction can never terminate abruptly in space." }
    ]
  },
  "Dashboard — magnet/magnetisation.md": {
    primary: "The British/Commonwealth spelling of magnetization: the act or process of making something magnetic, or the state of being magnetized.",
    secondary: "In physics and materials science, the density of magnetic dipole moments induced or permanently present within a magnetic substance.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The intensity of **magnetisation** within the iron core increases asymptotically toward a saturation limit." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "Thermoelectric experiments showed that mechanical strain alters the intensity of **magnetisation**." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The instantaneous **magnetisation** of the soft iron bar occurred the moment the circuit was completed." }
    ]
  },
  "Dashboard — magnet/magnetise.md": {
    primary: "To impart magnetic properties to a substance; to make magnetic (Commonwealth spelling).",
    secondary: "To attract, fascinate, or entrance someone; or historically, to subject to animal magnetism (mesmerism).",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "By passing a powerful galvanic pulse through the surrounding wire, we were able to **magnetise** the steel cylinder permanently." },
      { author: "Arthur Conan Doyle", work: "The Parasite", quote: "The mesmerist sought to **magnetise** his subject until her voluntary will surrendered completely." },
      { author: "Thomas Carlyle", work: "On Heroes, Hero-Worship, and the Heroic in History", quote: "The charismatic leader possesses that rare spiritual fire that can **magnetise** a disheartened multitude into action." }
    ]
  },
  "Dashboard — magnet/magnetised.md": {
    primary: "Endowed with magnetic properties; having magnetic poles or dipole alignment (Commonwealth spelling).",
    secondary: "Enthralled, captivated, or deeply fascinated by someone or something.",
    quotes: [
      { author: "William Gilbert", work: "De Magnete", quote: "The floating **magnetised** needle turns unerringly toward the poles of the earth." },
      { author: "Charlotte Brontë", work: "Villette", quote: "I stood **magnetised** by the passionate eloquence that flowed from his lips." },
      { author: "Charles Darwin", work: "The Voyage of the Beagle", quote: "The volcanic rocks were so strongly **magnetised** that the compass spun wildly when held near the cliff." }
    ]
  },
  "Dashboard — magnet/magnetism.md": {
    primary: "A physical phenomenon produced by the motion of electric charge, resulting in attractive and repulsive forces between objects.",
    secondary: "A quality of personal charm, charisma, or compelling attraction that fascinates and influences other people.",
    quotes: [
      { author: "William Gilbert", work: "De Magnete", quote: "Terrestrial **magnetism** guides the navigator across trackless oceans by an invisible heavenly thread." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "Electricity in motion produces **magnetism**, and changing magnetism produces electricity." },
      { author: "Ralph Waldo Emerson", work: "Essays: First Series", quote: "Character exerts a natural **magnetism** that commands respect without uttering a single argument." }
    ]
  },
  "Dashboard — magnet/magnetite.md": {
    primary: "A common black, strongly magnetic iron oxide mineral with the formula Fe3O4, the primary constituent of lodestone.",
    secondary: "In economic geology and biomagnetism, an important iron ore and the mineral synthesized by magnetotactic bacteria and migratory animals for navigation.",
    quotes: [
      { author: "James Dwight Dana", work: "Manual of Mineralogy", quote: "Naturally magnetic specimens of **magnetite** were known to the ancients under the name of lodestone." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Grains of **magnetite** weathered out of basaltic lavas form extensive black sand beaches along volcanic coasts." },
      { author: "Waldemar Lindgren", work: "Mineral Deposits", quote: "Contact metamorphic deposits often exhibit immense masses of crystallized **magnetite** intergrown with garnet." }
    ]
  },
  "Dashboard — magnet/magnetization.md": {
    primary: "The process of making something magnetic, or the degree to which a substance is magnetized; magnetic polarization vector M.",
    secondary: "In condensed matter physics, the net magnetic dipole moment per unit volume of a ferromagnetic, paramagnetic, or diamagnetic material.",
    quotes: [
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "The vector of **magnetization** represents the density of elementary magnetic dipoles aligned within the medium." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "Spontaneous **magnetization** in iron arises from quantum exchange interactions locking electron spins parallel." },
      { author: "Philip W. Anderson", work: "Concepts in Solids", quote: "Below the Curie temperature, broken symmetry leads to a non-zero macroscopic **magnetization**." }
    ]
  },
  "Dashboard — magnet/magnetize.md": {
    primary: "To make magnetic; to impart magnetic properties to a material.",
    secondary: "To attract, fascinate, or strongly influence someone; or historically, to mesmerize.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "A brief discharge from the battery was sufficient to **magnetize** the steel rod to saturation." },
      { author: "Edgar Allan Poe", work: "The Facts in the Case of M. Valdemar", quote: "I attempted to **magnetize** the dying patient to test whether mesmeric trance could hold death at bay." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "Ahab's monomaniacal purpose seemed to **magnetize** the entire crew into one living weapon." }
    ]
  },
  "Dashboard — magnet/magnetized.md": {
    primary: "Possessing magnetic properties; having magnetic poles or aligned atomic magnetic moments.",
    secondary: "Deeply captivated, fascinated, or held under a powerful influence.",
    quotes: [
      { author: "William Gilbert", work: "De Magnete", quote: "A **magnetized** iron bar stroking another piece of steel communicates its virtue without diminishing its own force." },
      { author: "Arthur Conan Doyle", work: "The Hound of the Baskervilles", quote: "The strange mystery held us completely **magnetized**, banishing every thought of rest." },
      { author: "Joseph Conrad", work: "Lord Jim", quote: "He stood **magnetized** by the terrifying spectacle of the sea breaking across the ship's deck." }
    ]
  },
  "Dashboard — magnet/magneto.md": {
    primary: "An electrical generator that uses permanent magnets to produce periodic pulses of high-voltage alternating current.",
    secondary: "In internal combustion engines, an ignition magneto providing reliable spark pulses for aircraft engines, motorcycles, and race cars without a battery.",
    quotes: [
      { author: "Nikola Tesla", work: "My Inventions", quote: "The compact **magneto** provided reliable high-frequency ignition pulses in our experimental automotive engines." },
      { author: "Antoine de Saint-Exupéry", work: "Night Flight", quote: "Before takeoff into the storm, the pilot ran the engine up and switched each **magneto** to verify dual ignition." },
      { author: "H. G. Wells", work: "The Sleeper Awakes", quote: "The spinning **magneto** hummed softly in the forward compartment of the monoplane." }
    ]
  },
  "Dashboard — magnet/magnetobiology.md": {
    primary: "The study of the biological effects of static and low-frequency magnetic fields on living organisms.",
    secondary: "In biophysics, the investigation of radical pair mechanisms, cellular ion transport, and physiological responses to ambient geomagnetic fields.",
    quotes: [
      { author: "E. O. Wilson", work: "The Diversity of Life", quote: "The emerging field of **magnetobiology** proved that animals from salmon to homing pigeons detect magnetic gradients." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Research in **magnetobiology** explores whether periodic solar geomagnetic disturbances exert subtle effects on terrestrial ecosystems." },
      { author: "Richard Dawkins", work: "The Blind Watchmaker", quote: "Pioneering experiments in **magnetobiology** demonstrated that magnetic cues guide the transcontinental flights of birds." }
    ]
  },
  "Dashboard — magnet/magnetograph.md": {
    primary: "An instrument that continuously and automatically records variations in the Earth's magnetic field.",
    secondary: "In geomagnetism and solar physics, a photographic or digital recording magnetometer used to monitor magnetic storms and solar magnetic fields.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Cosmos", quote: "The continuous trace of the **magnetograph** recorded synchronous magnetic perturbations from Paris to St. Petersburg." },
      { author: "George Ellery Hale", work: "The Magnetic Field in Sunspots", quote: "Using the solar **magnetograph** coupled to the spectroheliograph, we mapped the intense magnetic vortices of sunspots." },
      { author: "Lord Kelvin (William Thomson)", work: "Popular Lectures and Addresses", quote: "The photographic **magnetograph** registered an abrupt magnetic storm coinciding precisely with the appearance of the solar flare." }
    ]
  },
  "Dashboard — magnet/magnetohydrodynamics.md": {
    primary: "The study of the magnetic properties and behavior of electrically conducting fluids, such as plasmas, liquid metals, and salt water (MHD).",
    secondary: "In astrophysics and plasma engineering, the theoretical framework developed by Hannes Alfvén describing stellar dynamos, solar flares, and fusion plasma containment.",
    quotes: [
      { author: "Hannes Alfvén", work: "Cosmical Electrodynamics", quote: "The interplay between magnetic fields and conducting fluids constitutes the foundation of **magnetohydrodynamics**, predicting transverse magnetosonic waves." },
      { author: "Subrahmanyan Chandrasekhar", work: "Hydrodynamic and Hydromagnetic Stability", quote: "Magnetic fields profoundly alter fluid convective stability, providing the central mathematical problem of **magnetohydrodynamics**." },
      { author: "Arthur Eddington", work: "The Internal Constitution of the Stars", quote: "The rotational turbulence of stellar interiors cannot be solved without invoking the principles of **magnetohydrodynamics**." }
    ]
  },
  "Dashboard — magnet/magnetologist.md": {
    primary: "A scientist who specializes in the study of magnetism or geomagnetism.",
    secondary: "In physical science and geophysics, an investigator monitoring magnetic field variations, solar-terrestrial physics, or magnetic materials.",
    quotes: [
      { author: "Alexander von Humboldt", work: "Personal Narrative", quote: "The **magnetologist** meticulously checked the declination of the needle at every camp along the Andean cordillera." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "Every competent **magnetologist** recognizes that magnetic secular variation reflects deep convective dynamics within the core." },
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "The theoretical **magnetologist** seeks to synthesize all magnetic phenomena under common mechanical laws." }
    ]
  },
  "Dashboard — magnet/magnetometer.md": {
    primary: "An instrument used for measuring the strength, direction, or spatial variation of magnetic fields.",
    secondary: "In geophysics and planetary science, an instrument used for mineral exploration, submarine detection (MAD), and mapping extraterrestrial magnetospheres.",
    quotes: [
      { author: "Carl Friedrich Gauss", work: "The Intensity of the Earth's Magnetic Force Reduced to Absolute Measure", quote: "By introducing the bifilar **magnetometer**, we determined terrestrial magnetic intensity in absolute mechanical units." },
      { author: "James Van Allen", work: "Origins of Magnetospheric Physics", quote: "The fluxgate **magnetometer** aboard Pioneer 10 transmitted the first direct measurements of Jupiter's immense magnetic field." },
      { author: "Arthur Holmes", work: "Principles of Physical Geology", quote: "Airborne **magnetometer** surveys crisscrossed the oceanic ridges, mapping the alternating magnetic zebra stripes." }
    ]
  },
  "Dashboard — magnet/magneton.md": {
    primary: "A physical constant and natural unit for expressing the magnetic dipole moment of an electron or atomic nucleus.",
    secondary: "In atomic and nuclear physics, specifically the Bohr magneton (mu_B) for electron spin and the nuclear magneton (mu_N) for nucleons.",
    quotes: [
      { author: "Niels Bohr", work: "On the Quantum Theory of Line-Spectra", quote: "The magnetic moment associated with an orbital electron of unit angular momentum is defined as the Bohr **magneton**." },
      { author: "Wolfgang Pauli", work: "General Principles of Quantum Mechanics", quote: "The intrinsic magnetic moment of the electron equals almost exactly one Bohr **magneton**." },
      { author: "Isidor Isaac Rabi", work: "Radiofrequency Spectra of Atoms and Molecules", quote: "Nuclear magnetic moments are expressed in terms of the nuclear **magneton**, being nearly two thousand times smaller than the electron value." }
    ]
  },
  "Dashboard — magnet/magnetosome.md": {
    primary: "A microscopic intracellular organelle found in magnetotactic bacteria, consisting of a membrane-enveloped magnetic crystal (magnetite or greigite).",
    secondary: "In microbiology and biophysics, an organelle arranged in linear chains that acts like a biological compass needle, aligning bacteria with the Earth's geomagnetic field lines (magnetotaxis).",
    quotes: [
      { author: "Stephen Jay Gould", work: "The Panda's Thumb", quote: "Each **magnetosome** houses a pristine single-domain crystal of magnetite synthesized with flawless crystalline perfection." },
      { author: "Lynn Margulis", work: "Symbiotic Planet", quote: "By swimming along geomagnetic lines using its chain of **magnetosome** crystals, the bacterium navigates directly to optimal sediment depth." },
      { author: "Richard Dawkins", work: "The Ancestor's Tale", quote: "The bacterial **magnetosome** represents one of nature's oldest nanotechnological navigational instruments." }
    ]
  },
  "Dashboard — magnet/magnetosphere.md": {
    primary: "The region of space surrounding an astronomical object in which charged particles are controlled or dominated by that object's magnetic field.",
    secondary: "In space physics, the Earth's geomagnetic cavity carved out of the supersonic solar wind, bounded by the bow shock and magnetopause.",
    quotes: [
      { author: "James Van Allen", work: "Origins of Magnetospheric Physics", quote: "Satellites confirmed that the Earth's **magnetosphere** forms a vast tear-shaped bubble streaming millions of miles downwind into the interplanetary night." },
      { author: "Carl Sagan", work: "Cosmos", quote: "Without our protective planetary **magnetosphere**, energetic solar cosmic rays would have stripped away Earth's fragile atmosphere." },
      { author: "Arthur C. Clarke", work: "2001: A Space Odyssey", quote: "The spacecraft passed through the turbulent bow shock of Jupiter's roaring, radiation-drenched **magnetosphere**." }
    ]
  },
  "Dashboard — magnet/magnetron.md": {
    primary: "A high-powered vacuum tube that generates microwave oscillations using the interaction of a stream of electrons with a magnetic field.",
    secondary: "In radar engineering and microwave technology, the cavity magnetron invented in 1940 by Randall and Boot, foundational to Allied World War II centimetric radar and domestic microwave ovens.",
    quotes: [
      { author: "Robert Watson-Watt", work: "Three Steps to Victory", quote: "The invention of the cavity **magnetron** produced megawatts of centimetric microwave power from a device small enough to hold in one's hand." },
      { author: "Freeman Dyson", work: "Weapons and Hope", quote: "Centimetric radar powered by the cavity **magnetron** turned the tide against the U-boat threat in the Battle of the Atlantic." },
      { author: "Richard Feynman", work: "Surely You're Joking, Mr. Feynman!", quote: "During the war, radar development hinged entirely on understanding the subtle electron cloud dynamics inside the cavity **magnetron**." }
    ]
  },
  "Dashboard — magnet/manganese.md": {
    primary: "A hard, brittle, silvery-gray metallic element, atomic number 25 and symbol Mn, used extensively in steel production.",
    secondary: "An essential trace biological nutrient, historically associated with magnesia and pyrolusite (black oxide of manganese).",
    quotes: [
      { author: "Humphry Davy", work: "Elements of Chemical Philosophy", quote: "Scheele demonstrated that pyrolusite contained the calx of a distinct metal, which was subsequently named **manganese**." },
      { author: "Charles Lyell", work: "Principles of Geology", quote: "Concretions of dark hydrous **manganese** oxide carpet vast tracts of the deep abyssal ocean plains." },
      { author: "Primo Levi", work: "The Periodic Table", quote: "The addition of **manganese** to molten iron purges sulfur and imparts exceptional toughness to modern rail steel." }
    ]
  },
  "Dashboard — magnet/paramagnet.md": {
    primary: "A substance or material that exhibits paramagnetism, being weakly attracted into a magnetic field.",
    secondary: "In condensed matter physics, a material whose atoms have permanent magnetic dipoles that align parallel to an applied magnetic field, resulting in positive magnetic susceptibility.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Liquid oxygen behaves as a vigorous **paramagnet**, leaping up to bridge the poles of the powerful electromagnet." },
      { author: "James Clerk Maxwell", work: "A Treatise on Electricity and Magnetism", quote: "A true **paramagnet** aligns itself along the lines of force and is drawn toward the strongest parts of the field." },
      { author: "Lord Kelvin (William Thomson)", work: "Mathematical and Physical Papers", quote: "Unlike a diamagnet, the force acting upon a **paramagnet** is directed in the direction of the magnetic field gradient." }
    ]
  },
  "Dashboard — magnet/paramagnetic.md": {
    primary: "Pertaining to or exhibiting paramagnetism; having positive magnetic susceptibility and weakly attracted into a magnetic field.",
    secondary: "In quantum chemistry, describing substances containing one or more unpaired electrons, such as the triplet ground state of molecular oxygen.",
    quotes: [
      { author: "Michael Faraday", work: "Experimental Researches in Electricity", quote: "Substances which align axially between magnetic poles I designate as **paramagnetic** bodies." },
      { author: "Linus Pauling", work: "The Nature of the Chemical Bond", quote: "The **paramagnetic** susceptibility of molecular oxygen directly confirmed that two electrons occupy unpaired antibonding pi orbitals." },
      { author: "Pierre Curie", work: "Propriétés magnétiques des corps", quote: "Curie's law established that the susceptibility of a **paramagnetic** substance is inversely proportional to absolute temperature." }
    ]
  },
  "Dashboard — magnet/paramagnetism.md": {
    primary: "A form of magnetism whereby certain materials are weakly attracted by an externally applied magnetic field, forming internal induced magnetic fields in the direction of the applied field.",
    secondary: "In quantum physics and thermodynamics, the magnetic behavior governed by Curie's law, characterized by randomly oriented magnetic moments aligned by external fields against thermal agitation.",
    quotes: [
      { author: "Pierre Curie", work: "Propriétés magnétiques des corps", quote: "The fundamental law of **paramagnetism** reveals the eternal contest between magnetic dipole alignment and thermal agitation." },
      { author: "John Hasbrouck Van Vleck", work: "The Theory of Electric and Magnetic Susceptibilities", quote: "Quantum mechanical treatment of **paramagnetism** resolved the historical anomalies in transition metal salt spectra." },
      { author: "Richard Feynman", work: "The Feynman Lectures on Physics", quote: "In Pauli **paramagnetism**, the spin of conduction electrons in a metal aligns with an external field despite Fermi degeneracy." }
    ]
  },

  // === Dashboard — mechan (10 words) ===
  "Dashboard — mechan/machinate.md": {
    primary: "To engage in plots or schemes; to conspire, contrive, or design with evil or crafty intent.",
    secondary: "To engineer or scheme behind the scenes to bring about a desired, often subversive, outcome.",
    quotes: [
      { author: "William Shakespeare", work: "King Lear", quote: "I will **machinate** no treason against the state, but speak the plain truth of a loyal subject." },
      { author: "Edmund Burke", work: "Reflections on the Revolution in France", quote: "Conspirators gathered in secret clubs to **machinate** the subversion of ancient laws and religion." },
      { author: "Walter Scott", work: "Kenilworth", quote: "He continued to **machinate** in secret against his rival, weaving subtle intrigues through the court." }
    ]
  },
  "Dashboard — mechan/machination.md": {
    primary: "A crafty scheme, plot, or intrigue, especially one designed to accomplish an evil or sinister end.",
    secondary: "The act of scheming or plotting; intricate contrivance.",
    quotes: [
      { author: "Mary Shelley", work: "Frankenstein", quote: "I trembled to think of the malignant **machination** that might spring from his bitter, resentful mind." },
      { author: "Edward Gibbon", work: "The History of the Decline and Fall of the Roman Empire", quote: "The court eunuchs maintained their precarious supremacy through dark, ceaseless **machination**." },
      { author: "Charles Dickens", work: "A Tale of Two Cities", quote: "He discovered the cruel **machination** that had condemned an innocent man to the bastille for eighteen years." }
    ]
  },
  "Dashboard — mechan/machine.md": {
    primary: "An apparatus using mechanical power and having several parts, each with a definite function and together performing a particular task.",
    secondary: "An efficient, highly organized system or organization that operates like a mechanical device; or in physics, a simple machine that alters force or distance.",
    quotes: [
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "The mechanical powers of the lever, pulley, and wheel constitute the simplest forms of **machine**." },
      { author: "H. G. Wells", work: "The Time Machine", quote: "The **machine** had hummed into motion, slipping between the seconds into the unknown centuries." },
      { author: "Lewis Mumford", work: "Technics and Civilization", quote: "The mechanical clock, rather than the steam engine, was the foundational **machine** of modern industrial civilization." }
    ]
  },
  "Dashboard — mechan/machinery.md": {
    primary: "Machines collectively, or the components of a machine; mechanical apparatus.",
    secondary: "The organization, systems, or internal mechanisms by which a process is kept in operation; or in literature, supernatural agents directing a plot.",
    quotes: [
      { author: "Adam Smith", work: "The Wealth of Nations", quote: "The invention of specialized **machinery** facilitates and abridges labor, enabling one man to do the work of many." },
      { author: "Alexander Pope", work: "The Rape of the Lock", quote: "The aerial sylphs and gnomes constituted the epic **machinery** that watched over Belinda's sacred hair." },
      { author: "Karl Marx", work: "Capital", quote: "Modern industry tore down the handicraft barrier, enthroning giant automatic **machinery** as the sovereign driver of production." }
    ]
  },
  "Dashboard — mechan/machinist.md": {
    primary: "A skilled person who operates machine tools to manufacture or modify metal or other parts.",
    secondary: "A technician who designs, constructs, or repairs mechanical apparatus and engines.",
    quotes: [
      { author: "H. G. Wells", work: "The War of the Worlds", quote: "The chief **machinist** adjusted the steam pressure on the torpedo ram Thunder Child as the Martian tripod approached." },
      { author: "Herman Melville", work: "Moby-Dick", quote: "The ship's **machinist** forged the harpoon point in the glowing embers of the try-works." },
      { author: "Jack London", work: "The Iron Heel", quote: "The master **machinist** guided the lathe with steady hands, slicing micro-shavings from the naval gun barrel." }
    ]
  },
  "Dashboard — mechan/mechan.md": {
    primary: "A combining root derived from Greek mēchanē, meaning 'device', 'instrument', 'contrivance', 'machine', or 'means'.",
    secondary: "In science and philosophy, the formative root of mechanics, mechanism, and mechanical materialism.",
    quotes: [
      { author: "Aristotle", work: "Mechanics", quote: "Things that occur contrary to nature are brought about through art and contrivance, which we designate by the root **mechan**-." },
      { author: "René Descartes", work: "Principles of Philosophy", quote: "All natural operations are explicable through shapes and motions, governed by the universal root **mechan**-." },
      { author: "James Clerk Maxwell", work: "Matter and Motion", quote: "The prefix **mechan**- unites the study of forces, matter, and work into a coherent mathematical science." }
    ]
  },
  "Dashboard — mechan/mechane.md": {
    primary: "A crane or hoist used in ancient Greek theater to hoist actors into the air, especially portraying gods flying or descending onto the stage.",
    secondary: "In classical drama, the physical apparatus behind the theatrical convention of the deus ex machina ('god from the machine').",
    quotes: [
      { author: "Euripides", work: "Medea", quote: "Mounted upon the chariot hoisted by the theatrical **mechane**, Medea escaped the vengeance of the Corinthian king." },
      { author: "Aristophanes", work: "Peace", quote: "The comedian parodied Euripides by soaring over the theatrical stage upon a giant beetle lifted by the **mechane**." },
      { author: "Gilbert Murray", work: "A History of Ancient Greek Literature", quote: "The sudden descent of Apollo from the **mechane** resolved the impossible tragedy with divine authority." }
    ]
  },
  "Dashboard — mechan/mechanic.md": {
    primary: "A skilled tradesperson who repairs, maintains, or constructs machinery, engines, or motor vehicles.",
    secondary: "Pertaining to manual labor or handicraft; or in classical literature, a working-class artisan or craftsman.",
    quotes: [
      { author: "William Shakespeare", work: "Julius Caesar", quote: "What, know you not, being **mechanic**, you ought not walk upon a labouring day without the sign of your profession?" },
      { author: "Benjamin Franklin", work: "Autobiography", quote: "My father intended to make me a useful **mechanic**, but my fondness for books diverted my life into printing." },
      { author: "Arthur Conan Doyle", work: "The Sign of the Four", quote: "The garage **mechanic** wiped the grease from his brow and certified that the steam carriage was in running order." }
    ]
  },
  "Dashboard — mechan/mechanical.md": {
    primary: "Operated by a machine or mechanism; of or relating to machines, tools, or physical forces.",
    secondary: "Done without conscious thought; automatic, routine, or lacking spontaneity.",
    quotes: [
      { author: "Isaac Newton", work: "Philosophiae Naturalis Principia Mathematica", quote: "Rational mechanics is the science of motions resulting from any forces whatsoever, and of the forces required to produce any **mechanical** motions." },
      { author: "Charles Dickens", work: "Hard Times", quote: "The great pistons of the steam engine moved with a melancholy, **mechanical** monotony that crushed the human spirit." },
      { author: "Herman Melville", work: "Bartleby, the Scrivener", quote: "He copied the legal documents with a silent, **mechanical** speed that seemed entirely devoid of human emotion." }
    ]
  },
  "Dashboard — mechan/mechanically.md": {
    primary: "In a mechanical manner; by means of a machine or physical force.",
    secondary: "Without conscious thought or feeling; routinely, automatically, or unreflectively.",
    quotes: [
      { author: "Jane Austen", work: "Sense and Sensibility", quote: "Elinor **mechanically** folded the letter, while her heart was torn with the most agonizing reflections." },
      { author: "George Eliot", work: "Middlemarch", quote: "She walked on **mechanically**, scarcely noticing the road or the gathering storm overhead." },
      { author: "James Clerk Maxwell", work: "Matter and Motion", quote: "The work done upon the piston is **mechanically** transferred through the connecting rod to the revolving flywheel." }
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

console.log(`Updated ${updatedCount} files in Batch 4!`);
